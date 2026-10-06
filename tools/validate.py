#!/usr/bin/env python3
"""Check package structure, portable references, and published file integrity."""
import ast
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import install

TOP_FILES = {'README.md','LICENSE','THIRD_PARTY_NOTICES.md','CHANGELOG.md','MAINTAINING.md','VERSION','.gitignore','.gitattributes','install.py','public-files.json'}

# Assemble reserved terms so the scanner also inspects its own source and fixtures.
PRIVATE_MARKERS = [
    r'/Users/' + r'[^/\s]+/', r'Texas' + r'[ _-]Pacifico',
    r'Master Commercial' + r' Clean', r'theprovider' + r'system@gmail\.com',
    r'\b(?:clean' + r'ing|clean' + r'er|janit' + r'orial)s?\b',
    r'steve[ _-]+han' + r'son', r'mike[ _-]+cam' + r'pion',
    r'janit' + r'orialstore', r'clean' + r'ingcogrow',
    r'gh[pousr]_[A-Za-z0-9]{25,}', r'sk-[A-Za-z0-9]{24,}',
    r'-----BEGIN ' + r'(?:RSA |OPENSSH |EC )?PRIVATE KEY-----',
]

def private_content(text):
    return any(re.search(pattern, text, re.I) for pattern in PRIVATE_MARKERS)

def allowed_files(root):
    path = root/'public-files.json'
    if path.is_symlink():
        raise ValueError('Public file list cannot be a symbolic link')
    names = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(names, list) or not all(isinstance(n, str) for n in names):
        raise ValueError('Invalid public file list')
    if len(names) != len(set(names)):
        raise ValueError('Duplicate public file entry')
    for name in names:
        if name.startswith('/') or '\\' in name or any(p in {'', '.', '..'} for p in name.split('/')):
            raise ValueError('Invalid public file path')
    return set(names)

def package_files(root=ROOT):
    root = Path(root)
    allowed = allowed_files(root)
    result = []
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if rel.parts[0] in {'.git','dist'} or '__pycache__' in rel.parts or path.name.endswith('.pyc'):
            continue
        if path.is_symlink():
            raise ValueError('Package contains a symbolic link: '+rel.as_posix())
        if not path.is_file():
            continue
        name = rel.as_posix()
        if name not in allowed:
            raise ValueError('Unexpected file in public package: '+name)
        result.append(path)
    missing = allowed - {p.relative_to(root).as_posix() for p in result}
    if missing:
        raise ValueError('Missing public files: '+', '.join(sorted(missing)))
    return result

def validate(root=ROOT, check_manifest=True):
    root = Path(root).resolve()
    paths = package_files(root)
    errors = []
    texts = {}
    for path in paths:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding='utf-8')
        texts[rel] = text
        if private_content(rel+'\n'+text):
            errors.append('Excluded content or credential pattern in '+rel)
        if path.suffix == '.py':
            try:
                ast.parse(text,filename=rel)
            except SyntaxError as exc:
                errors.append('Python syntax: '+rel+': '+str(exc))
        if path.suffix == '.json':
            try:
                json.loads(text)
            except ValueError:
                errors.append('Invalid JSON: '+rel)
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)\n]+)\)',text):
                target = target.strip('<>').split('#',1)[0]
                if not target or '://' in target or target.startswith('mailto:'):
                    continue
                resolved = (path.parent/unquote(target)).resolve()
                if root not in resolved.parents or not resolved.is_file():
                    errors.append('Broken or escaping link in '+rel+': '+target)
    missing = TOP_FILES-set(texts)
    errors += ['Missing required file: '+x for x in sorted(missing)]
    permitted = {'!/'+p for p in allowed_files(root)}
    actual = {line for line in texts.get('.gitignore','').splitlines() if line.startswith('!/')} - {'!*/'}
    if permitted != actual:
        errors.append('Git ignore permissions and public file list disagree')
    skill = root/'skills/business-desk'
    entry = (skill/'SKILL.md').read_text(encoding='utf-8')
    if not entry.startswith('---\nname: business-desk\ndescription: '):
        errors.append('Missing skill name or description')
    if entry.count('\n---\n') < 1:
        errors.append('Incomplete frontmatter')
    if len(entry.split()) > 1600:
        errors.append('Skill entry point needs progressive disclosure')
    catalog = json.loads((skill/'references/experts/index.json').read_text(encoding='utf-8'))
    if not catalog or any(p['group'] not in {'active','supplemental'} for p in catalog):
        errors.append('Invalid reference catalog coverage')
    if len({p['slug'] for p in catalog}) != len(catalog):
        errors.append('Duplicate expert references')
    sources = json.loads((skill/'references/experts/sources.json').read_text(encoding='utf-8'))
    known = {p['slug'] for p in catalog}
    for item in catalog:
        if not (skill/'references/experts'/item['brief']).is_file():
            errors.append('Missing expert brief: '+item['slug'])
        if item['sources'] != sum(s['expert']==item['slug'] for s in sources):
            errors.append('Source count mismatch: '+item['slug'])
    for source in sources:
        url = urlsplit(source['url'])
        if source['expert'] not in known or url.scheme not in {'http','https'} or not url.netloc or url.username or url.password:
            errors.append('Invalid source metadata')
    if check_manifest:
        try:
            manifest = install.verify(skill)
            if manifest['version'] != (root/'VERSION').read_text().strip():
                errors.append('Version and skill manifest disagree')
        except (ValueError,OSError,KeyError) as exc:
            errors.append('Skill integrity: '+str(exc))
    if errors:
        raise ValueError('\n'.join(errors))
    return {'ok':True,'files':len(paths),'expert_briefs':len(catalog),'source_entries':len(sources)}

if __name__ == '__main__':
    try:
        print(json.dumps(validate(),indent=2))
    except (ValueError,OSError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(1)
