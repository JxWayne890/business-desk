#!/usr/bin/env python3
"""Read public X material through TwitterAPI.io without exposing the API key."""
import argparse
import datetime as dt
import getpass
import json
import math
import os
from pathlib import Path
import re
import stat
import sys
import urllib.error
import urllib.parse
import urllib.request

KEY_FILE = Path.home() / '.config/business-desk/twitterapi.key'
BASE = 'https://api.twitterapi.io'
ALLOWED = {'/oapi/my/info', '/twitter/user/info', '/twitter/tweet/advanced_search'}


def valid_key(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_-]{16,256}', value):
        raise ValueError('The API key has an unexpected format. Its value was not logged.')
    return value


def save_key(value, path=KEY_FILE):
    if os.name != 'posix':
        raise ValueError('Use TWITTERAPI_IO_KEY on this platform. File credential storage requires macOS or Linux.')
    value = valid_key(value.strip())
    path = Path(path)
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    info = path.parent.lstat()
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid():
        raise ValueError('Credential directory must be a real directory owned by this user.')
    os.chmod(path.parent, 0o700)
    # Do not replace a preexisting key or follow a link.
    fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as stream:
        stream.write(value + '\n')
    return {'credential_saved': True, 'path': str(path), 'permissions': '0600'}


def load_key(path=KEY_FILE):
    supplied = os.environ.get('TWITTERAPI_IO_KEY')
    if supplied:
        return valid_key(supplied.strip())
    if os.name != 'posix':
        raise ValueError('Set TWITTERAPI_IO_KEY in your environment on this platform.')
    fd = os.open(str(path), os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, 'r', encoding='utf-8') as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
            raise ValueError('Credential file must be owned by this user and inaccessible to other users.')
        return valid_key(stream.read(1024).strip())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def request(path, params=None, key=None, opener=None):
    if path not in ALLOWED:
        raise ValueError('This helper supports only the documented account and public research read endpoints.')
    key = valid_key(key) if key is not None else load_key()
    url = BASE + path
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'X-API-Key': key, 'Accept': 'application/json'}, method='GET')
    opener = opener or urllib.request.build_opener(NoRedirect())
    try:
        with opener.open(req, timeout=30) as response:
            data = response.read(8 * 1024 * 1024 + 1)
            if len(data) > 8 * 1024 * 1024:
                raise ValueError('Response exceeded the research page size limit.')
    except urllib.error.HTTPError as exc:
        raise ValueError('TwitterAPI.io returned HTTP %s. No automatic retry was made.' % exc.code) from None
    except (urllib.error.URLError, TimeoutError):
        raise ValueError('TwitterAPI.io request failed or timed out. No automatic retry was made.') from None
    try:
        result = json.loads(data)
    except (ValueError, UnicodeError):
        raise ValueError('TwitterAPI.io returned invalid JSON.') from None
    if not isinstance(result, dict) or result.get('error') or result.get('status') in ('error', 'failed'):
        raise ValueError('TwitterAPI.io returned an unsuccessful response. Response details were not logged.')
    return result


def check_account(fetch=request):
    result = fetch('/oapi/my/info')
    credits = result.get('recharge_credits')
    if isinstance(credits, bool) or not isinstance(credits, (int, float)) or not math.isfinite(credits):
        raise ValueError('Account response did not contain the documented credit balance.')
    return {'authenticated': True, 'recharge_credits': credits,
            'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(),
            'note': 'Bonus credits may be shown separately in the dashboard.'}


def user_name(value):
    value = value.removeprefix('@')
    if not re.fullmatch(r'[A-Za-z0-9_]{1,15}', value):
        raise ValueError('Use a public X handle, not a URL or search expression.')
    return value


def date_seconds(value):
    try:
        date = dt.date.fromisoformat(value)
    except ValueError:
        raise ValueError('Dates must use YYYY-MM-DD.') from None
    return int(dt.datetime.combine(date, dt.time(), dt.timezone.utc).timestamp())


def search_page(handle, since, until, cursor='', fetch=request):
    handle = user_name(handle)
    start, end = date_seconds(since), date_seconds(until)
    if start >= end:
        raise ValueError('The end date must be later than the start date. The end date is exclusive.')
    if not isinstance(cursor, str) or len(cursor) > 8192:
        raise ValueError('Invalid pagination cursor.')
    query = 'from:%s since_time:%s until_time:%s' % (handle, start, end)
    result = fetch('/twitter/tweet/advanced_search', {'query': query, 'queryType': 'Latest', 'cursor': cursor})
    tweets = result.get('tweets')
    more, next_cursor = result.get('has_next_page'), result.get('next_cursor')
    if not isinstance(tweets, list) or not all(isinstance(t, dict) for t in tweets):
        raise ValueError('Search response did not contain a valid tweets list.')
    if not isinstance(more, bool) or not isinstance(next_cursor, str) or (more and (not next_cursor or next_cursor == cursor)):
        raise ValueError('Search response contained invalid pagination state.')
    return {'schema_version': 1, 'provider': 'twitterapi.io', 'handle': handle,
            'since_utc': since, 'until_utc_exclusive': until, 'query': query,
            'fetched_at': dt.datetime.now(dt.timezone.utc).isoformat(),
            'requests_made': 1, 'has_next_page': more, 'next_cursor': next_cursor,
            'capture_status': 'retrieved_not_ingested',
            'coverage_note': 'One search page. Pagination exhaustion does not prove a complete X archive.',
            'tweets': tweets}


def save_page(path, result):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation refuses an existing file or final symbolic link on every platform.
    fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0), 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('set-key', help='Store an existing key using a terminal prompt with input hidden.')
    commands.add_parser('status', help='Check local configuration without making an API request.')
    commands.add_parser('check', help='Make one authenticated account read request.')
    search = commands.add_parser('search', help='Fetch one page only; never automatically continue or retry.')
    search.add_argument('handle')
    search.add_argument('--since', required=True)
    search.add_argument('--until', required=True)
    search.add_argument('--cursor', default='')
    search.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'set-key':
            if not sys.stdin.isatty():
                raise ValueError('Use a terminal for hidden credential entry.')
            result = save_key(getpass.getpass('TwitterAPI.io key (input hidden): '))
        elif args.command == 'status':
            load_key()
            result = {'configured': True, 'source': 'environment' if os.environ.get('TWITTERAPI_IO_KEY') else str(KEY_FILE),
                      'network_request': False}
        elif args.command == 'check':
            result = check_account()
        else:
            if args.out.exists() or args.out.is_symlink():
                raise ValueError('Output already exists. Choose a new capture filename before requesting another page.')
            page = search_page(args.handle, args.since, args.until, args.cursor)
            save_page(args.out, page)
            result = {'saved': str(args.out), 'tweet_count': len(page['tweets']), 'requests_made': 1,
                      'has_next_page': page['has_next_page'], 'capture_status': page['capture_status']}
        print(json.dumps(result, indent=2))
        return 0
    except FileNotFoundError:
        print(json.dumps({'error': 'No saved API key was found. Run set-key in a terminal.'}))
    except FileExistsError:
        print(json.dumps({'error': 'File already exists and was preserved.'}))
    except (ValueError, OSError, EOFError) as exc:
        # Never print OS exception bodies or response bodies, which may contain secrets.
        message = str(exc) if isinstance(exc, ValueError) else 'Local file or input operation failed.'
        print(json.dumps({'error': message}))
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
