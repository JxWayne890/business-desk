#!/usr/bin/env python3
"""Install the complete Business Desk skill without network access."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import uuid

NAME = 'business-desk'
RECEIPT = '.business-desk-install.json'

def files_in(root):
    paths = {}
    for path in root.rglob('*'):
        rel = path.relative_to(root)
        if '__pycache__' in rel.parts or path.name == RECEIPT:
            continue
        if path.is_symlink():
            raise ValueError('Symbolic links are not supported in an install package: ' + str(rel))
        if path.is_file():
            paths[rel.as_posix()] = path
    return paths

def verify(root):
    if root.is_symlink():
        raise ValueError('The skill directory must not be a symbolic link.')
    manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    if manifest.get('name') != NAME or not isinstance(manifest.get('files'), dict) or not manifest['files']:
        raise ValueError('Invalid Business Desk manifest.')
    actual = files_in(root)
    expected = manifest['files']
    if set(actual) != set(expected) | {'manifest.json'}:
        raise ValueError('The package has missing or unexpected files.')
    for rel, wanted in expected.items():
        path = PurePosixPath(rel)
        if path.is_absolute() or '..' in path.parts or '\\' in rel:
            raise ValueError('Invalid manifest path.')
        if hashlib.sha256(actual[rel].read_bytes()).hexdigest() != wanted:
            raise ValueError('File checksum mismatch: ' + rel)
    return manifest

def install(source, skills_dir, update=False):
    source = Path(source).resolve()
    skills_dir = Path(skills_dir).expanduser()
    if skills_dir.is_symlink():
        raise ValueError('Choose a real skills directory rather than a symbolic link.')
    skills_dir = skills_dir.resolve()
    target = skills_dir / NAME
    if target.is_symlink():
        raise ValueError('Existing skill is a symbolic link. It was left unchanged.')
    manifest = verify(source)
    if source == target or source in target.parents or target in source.parents:
        raise ValueError('Install source and destination must be separate folders.')
    if target.exists():
        if not target.is_dir():
            raise ValueError('The destination exists and is not a directory.')
        try:
            current = verify(target)
        except (OSError, ValueError):
            current = None
        if current == manifest:
            return {'status':'already_current','version':manifest['version'],'path':str(target)}
        if not update:
            raise ValueError('An installation already exists. It was preserved. Use --update to back it up and install this version.')
        marker = target / RECEIPT
        if not marker.is_file() or json.loads(marker.read_text(encoding='utf-8')).get('name') != NAME:
            raise ValueError('This folder was not created by this installer. Move it aside manually before installing.')
    skills_dir.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.business-desk-stage-', dir=str(skills_dir.parent)))
    staged = staging / NAME
    backup = None
    try:
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns('__pycache__','*.pyc', RECEIPT))
        verify(staged)
        (staged / RECEIPT).write_text(json.dumps({'name':NAME,'version':manifest['version'],
            'installed_at':datetime.now(timezone.utc).isoformat()},indent=2)+'\n',encoding='utf-8')
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
            backup = skills_dir.parent / '.business-desk-backups' / stamp / NAME
            backup.parent.mkdir(parents=True)
            target.rename(backup)
        try:
            staged.rename(target)
        except OSError:
            if backup and not target.exists():
                backup.rename(target)
            raise
    finally:
        shutil.rmtree(staging)
    return {'status':'updated' if backup else 'installed','version':manifest['version'],
            'path':str(target),'backup':str(backup) if backup else None}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills-dir', type=Path, default=Path.home()/'.agents/skills')
    parser.add_argument('--update', action='store_true', help='Back up an existing managed installation before replacing it.')
    parser.add_argument('--check', action='store_true', help='Check the installed files without changing anything.')
    args = parser.parse_args()
    try:
        if args.check:
            target = args.skills_dir.expanduser() / NAME
            result = {'status':'verified','version':verify(target)['version'],'path':str(target)}
        else:
            result = install(Path(__file__).resolve().parent/'skills'/NAME,args.skills_dir,args.update)
        print(json.dumps(result,indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('Business Desk: '+str(exc),file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
