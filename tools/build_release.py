#!/usr/bin/env python3
"""Build a reproducible local release from validated public package files."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile
from validate import ROOT, package_files, validate

def manifest(root=ROOT):
    skill = root/'skills/business-desk'
    entries = {}
    for path in package_files(root):
        if skill in path.parents and path.name != 'manifest.json':
            entries[path.relative_to(skill).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    result = {'name':'business-desk','version':(root/'VERSION').read_text().strip(),'files':entries}
    (skill/'manifest.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return result

def build(root=ROOT, output=None):
    validate(root)
    output = Path(output) if output else root/'dist'
    output.mkdir(parents=True,exist_ok=True)
    archive = output/'business-desk.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as zipped:
        for path in package_files(root):
            name = 'business-desk/'+path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name,date_time=(2026,10,6,0,0,0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zipped.writestr(info,path.read_bytes())
    sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output/'SHA256SUMS.txt').write_text(sha+'  business-desk.zip\n',encoding='utf-8')
    return {'archive':str(archive),'bytes':archive.stat().st_size,'sha256':sha}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest-only',action='store_true')
    args = parser.parse_args()
    try:
        if args.manifest_only:
            value=manifest()
            print(json.dumps({'version':value['version'],'skill_files':len(value['files'])}))
        else:
            print(json.dumps(build(),indent=2))
    except (ValueError,OSError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(1)
