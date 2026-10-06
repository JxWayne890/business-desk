#!/usr/bin/env python3
"""Validate every commit reachable from refs proposed for publication."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile

from validate import ROOT, allowed_files, private_content, validate


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check_refs(refs):
    commits = git('rev-list', *refs).decode('ascii').splitlines()
    for commit in commits:
        message = git('show', '-s', '--format=%B', commit).decode('utf-8')
        if private_content(message):
            raise ValueError('Excluded content in commit message '+commit)
        with tempfile.TemporaryDirectory(prefix='public-check-') as temp:
            root = Path(temp)
            entries = git('ls-tree', '-rz', '--full-tree', commit).split(b'\0')
            tracked = set()
            for entry in entries:
                if not entry:
                    continue
                meta, raw_name = entry.split(b'\t', 1)
                mode, kind, oid = meta.decode('ascii').split()
                name = raw_name.decode('utf-8')
                tracked.add(name)
                if mode not in {'100644', '100755'} or kind != 'blob':
                    raise ValueError('Only regular public files may be pushed: '+name)
                if name.startswith('/') or '\\' in name or any(p in {'', '.', '..'} for p in name.split('/')):
                    raise ValueError('Invalid Git path')
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(git('cat-file', 'blob', oid))
            if tracked != allowed_files(root):
                raise ValueError('Git snapshot contains unapproved or missing files: '+commit)
            # Read the committed snapshot, never the working tree or just its last diff.
            validate(root)
    return len(commits)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refs', nargs='+')
    args = parser.parse_args()
    refs = args.refs
    if refs is None:
        refs = []
        for line in sys.stdin:
            local_ref, local_sha, remote_ref, remote_sha = line.split()
            if set(local_sha) != {'0'}:
                refs.append(local_sha)
    if refs:
        count = check_refs(refs)
        print('Publication checks passed for '+str(count)+' reachable commits.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        print('Push blocked: '+str(exc), file=sys.stderr)
        raise SystemExit(1)
