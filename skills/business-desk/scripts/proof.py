#!/usr/bin/env python3
"""Run a declared verification plan and detect stale proof for scoped expert work."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid
from expert import DEFAULT, read, write, now

def active_path(root, session):
    return root / '_verification' / ('session-' + hashlib.sha256(session.encode()).hexdigest() + '.json')

def snapshot(cwd, files):
    result = {}
    for name in files:
        target = (Path(cwd) / name).resolve()
        if Path(name).is_absolute() or Path(cwd).resolve() not in target.parents:
            raise ValueError('Verification paths must stay inside the project: ' + name)
        if target.exists() and not target.is_file():
            raise ValueError('Declare files, not folders: ' + name)
        result[name] = hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else 'missing'
    return result

def status(record):
    current = snapshot(record['cwd'], record['files'])
    receipt = record.get('receipt')
    if not receipt:
        return {'verified': False, 'reason': 'The declared checks have not run.'}
    if current != receipt['after'] or receipt['before'] != receipt['after']:
        return {'verified': False, 'reason': 'Files changed during or after verification. Run the plan again.'}
    if len(receipt['results']) != len(record['checks']) or not all(r['exit_code'] == 0 for r in receipt['results']):
        return {'verified': False, 'reason': 'At least one declared check failed or did not finish.'}
    return {'verified': True, 'reason': 'All declared checks passed for the current scoped files.',
            'checks': len(receipt['results']), 'finished_at': receipt['finished_at']}

def begin(args, root):
    if not args.session:
        raise ValueError('Set --session to the current Codex session ID, or use CODEX_THREAD_ID.')
    checks = read(args.checks)
    if not isinstance(checks, list) or not checks:
        raise ValueError('Checks must be a nonempty JSON array')
    for check in checks:
        argv = check.get('argv')
        if not isinstance(argv, list) or not argv or not all(isinstance(v, str) and v for v in argv):
            raise ValueError('Each check requires a nonempty argv string array')
        if not check.get('label') or not check.get('reason'):
            raise ValueError('Each check needs a label and an explanation of relevance')
    cwd = Path(args.cwd).expanduser().resolve()
    if not cwd.is_dir():
        raise ValueError('Project directory does not exist')
    files = sorted(set(args.files))
    snapshot(str(cwd), files)
    pointer = active_path(root, args.session)
    if pointer.exists():
        raise ValueError('An expert verification session is already active. Finish it first.')
    run_id = str(uuid.uuid4())
    record = {'schema_version': 1, 'id': run_id, 'session_id': args.session, 'expert': args.expert,
              'cwd': str(cwd), 'files': files, 'checks': checks, 'created_at': now(),
              'timeout_seconds': args.timeout, 'closed': False}
    record_path = root / '_verification' / (run_id + '.json')
    write(record_path, record)
    write(pointer, {'record_path': str(record_path)})
    return {'record': str(record_path), 'scope': files, 'status': 'awaiting_checks'}

def get_record(root, session):
    pointer = active_path(root, session)
    if not pointer.exists():
        raise ValueError('No active expert verification session')
    record_path = Path(read(pointer)['record_path'])
    if record_path.resolve().parent != (root / '_verification').resolve():
        raise ValueError('Invalid verification record path')
    return pointer, record_path, read(record_path)

def run(root, session):
    _, path, record = get_record(root, session)
    before = snapshot(record['cwd'], record['files'])
    results = []
    attempt = str(uuid.uuid4())
    for i, check in enumerate(record['checks']):
        try:
            p = subprocess.run(check['argv'], cwd=record['cwd'], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, timeout=record['timeout_seconds'], shell=False)
            code, output = p.returncode, p.stdout.decode('utf-8', errors='replace')
        except subprocess.TimeoutExpired as e:
            code, output = 124, (e.stdout or b'').decode('utf-8', errors='replace') + '\nCheck timed out.\n'
        except OSError as e:
            code, output = 127, str(e)
        log_path = root / '_verification' / (record['id'] + '-' + attempt + '-' + str(i) + '.log')
        log_path.write_text(output, encoding='utf-8')
        results.append({'label': check['label'], 'argv': check['argv'], 'reason': check['reason'],
                        'exit_code': code, 'log': str(log_path)})
    receipt = {'before': before, 'after': snapshot(record['cwd'], record['files']),
               'results': results, 'finished_at': now()}
    # Preserve each attempt; the live record points to the latest receipt.
    write(root / '_verification' / (record['id'] + '-' + attempt + '.json'), receipt)
    record['receipt'] = receipt
    write(path, record)
    return dict(status(record), record=str(path), results=results)

def finish(root, session, reason=None):
    pointer, path, record = get_record(root, session)
    outcome = status(record)
    if not outcome['verified'] and not reason:
        raise ValueError('Cannot close as verified. Run checks or explicitly give an unverified reason.')
    record['closed'] = True
    record['closed_at'] = now()
    record['outcome'] = outcome
    if reason:
        record['unverified_reason'] = reason
        record['outcome']['verified'] = False
    write(path, record)
    pointer.unlink()
    return dict(record['outcome'], record=str(path), unverified_reason=reason)

def hook(root, payload):
    # Only opted in main sessions. SubagentStop uses a parent session ID, so do not register it.
    if payload.get('hook_event_name') != 'Stop' or not payload.get('session_id'):
        return {}
    session = payload['session_id']
    pointer = active_path(root, session)
    if not pointer.exists():
        return {}
    _, path, record = get_record(root, session)
    if record.get('closed') or Path(payload.get('cwd', '')).resolve() != Path(record['cwd']).resolve():
        return {}
    outcome = status(record)
    if outcome['verified']:
        finish(root, session)
        return {}
    if payload.get('stop_hook_active'):
        finish(root, session, 'Verification still incomplete after the Stop hook continuation.')
        return {'systemMessage': 'Expert work remains unverified. State that limitation in the final response. ' + outcome['reason']}
    return {'decision': 'block', 'reason': 'Expert verification is incomplete. ' + outcome['reason'] +
            ' Read the verification workflow, run the declared plan, or close with an explicit unverified reason and report the limitation. Record: ' + str(path)}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=DEFAULT)
    p.add_argument('--session', default=os.environ.get('CODEX_THREAD_ID') or os.environ.get('CODEX_SESSION_ID'))
    sub = p.add_subparsers(dest='command', required=True)
    b = sub.add_parser('begin')
    b.add_argument('--expert', required=True); b.add_argument('--cwd', default=os.getcwd())
    b.add_argument('--files', nargs='+', required=True); b.add_argument('--checks', required=True)
    b.add_argument('--timeout', type=int, default=120)
    sub.add_parser('run'); sub.add_parser('status'); sub.add_parser('hook')
    f = sub.add_parser('finish'); f.add_argument('--unverified-reason')
    args = p.parse_args()
    root = args.root.expanduser().resolve()
    try:
        if args.command == 'begin':
            if not 1 <= args.timeout <= 600:
                raise ValueError('Timeout must be between 1 and 600 seconds')
            result = begin(args, root)
        elif args.command == 'hook':
            result = hook(root, json.load(sys.stdin))
        elif args.command == 'run':
            result = run(root, args.session or '')
        elif args.command == 'finish':
            result = finish(root, args.session or '', args.unverified_reason)
        else:
            result = status(get_record(root, args.session or '')[2])
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if args.command in ('run', 'status') and not result.get('verified') else 0
    except (ValueError, OSError, KeyError, TypeError) as e:
        if args.command == 'hook':
            print(json.dumps({'systemMessage': 'Expert verification could not be checked: ' + str(e)}))
            return 0
        print(json.dumps({'error': str(e)}))
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
