import io
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch
import urllib.error
import twitterapi as api

FAKE = 'example_test_key_not_a_real_credential'


class Response(io.BytesIO):
    pass


class Opener:
    def __init__(self, data):
        self.data, self.calls = data, []

    def open(self, request, timeout):
        self.calls.append((request, timeout))
        return Response(json.dumps(self.data).encode())


class IntegrationTests(unittest.TestCase):
    @unittest.skipUnless(os.name == 'posix', 'Private file credentials use POSIX permissions')
    def test_key_private_and_preserved(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ, {}, clear=True):
            path = Path(temp) / 'credentials/key'
            result = api.save_key(FAKE, path)
            self.assertNotIn(FAKE, json.dumps(result))
            self.assertEqual(api.load_key(path), FAKE)
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o600)
            self.assertEqual(stat.S_IMODE(path.parent.stat().st_mode), 0o700)
            with self.assertRaises(FileExistsError):
                api.save_key('different_example_test_credential', path)
            self.assertEqual(api.load_key(path), FAKE)
            path.chmod(0o644)
            with self.assertRaises(ValueError):
                api.load_key(path)

    @unittest.skipUnless(os.name == 'posix', 'Private file credentials use POSIX permissions')
    def test_key_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ, {}, clear=True):
            real = Path(temp) / 'real'
            api.save_key(FAKE, real)
            link = Path(temp) / 'link'
            link.symlink_to(real)
            with self.assertRaises(OSError):
                api.load_key(link)

    def test_request_destination_and_no_secret_url(self):
        opener = Opener({'recharge_credits': 0})
        api.request('/oapi/my/info', key=FAKE, opener=opener)
        request, timeout = opener.calls[0]
        self.assertEqual(request.full_url, 'https://api.twitterapi.io/oapi/my/info')
        self.assertEqual(request.get_method(), 'GET')
        self.assertNotIn(FAKE, request.full_url)
        self.assertEqual(dict(request.header_items())['X-api-key'], FAKE)
        self.assertEqual(timeout, 30)
        for endpoint in ['https://example.org/key', '/twitter/create_tweet', '//example.org']:
            with self.assertRaises(ValueError):
                api.request(endpoint, key=FAKE, opener=opener)
        self.assertEqual(len(opener.calls), 1)

    def test_redirects_blocked(self):
        handler = api.NoRedirect()
        self.assertIsNone(handler.redirect_request(None, None, 302, '', {}, 'https://example.org'))

    def test_account_validates_success_and_omits_unrelated_fields(self):
        result = api.check_account(lambda path: {'recharge_credits': 0, 'api_key': FAKE})
        self.assertTrue(result['authenticated'])
        self.assertNotIn(FAKE, json.dumps(result))
        for bad in [{}, {'recharge_credits': True}, {'recharge_credits': float('nan')}]:
            with self.assertRaises(ValueError):
                api.check_account(lambda path: bad)

    def test_http_error_redacted_and_not_retried(self):
        class Failure:
            count = 0
            def open(self, req, timeout):
                self.count += 1
                raise urllib.error.HTTPError(req.full_url, 401, FAKE, {}, None)
        fail = Failure()
        with self.assertRaises(ValueError) as raised:
            api.request('/oapi/my/info', key=FAKE, opener=fail)
        self.assertEqual(fail.count, 1)
        self.assertNotIn(FAKE, str(raised.exception))
        self.assertIn('401', str(raised.exception))
        with self.assertRaises(ValueError):
            api.request('/oapi/my/info', key=FAKE, opener=Opener({'error': 1, 'message': FAKE}))

    def test_search_one_page_and_untrusted_capture(self):
        calls = []
        def fetch(path, params):
            calls.append((path, params))
            return {'tweets': [{'id': '123', 'text': 'Source content'}], 'has_next_page': True, 'next_cursor': 'next'}
        page = api.search_page('@karpathy', '2023-01-01', '2026-10-06', fetch=fetch)
        self.assertEqual(len(calls), 1)
        self.assertEqual(page['capture_status'], 'retrieved_not_ingested')
        self.assertTrue(page['has_next_page'])
        self.assertEqual(page['next_cursor'], 'next')
        self.assertIn('since_time:1672531200', calls[0][1]['query'])
        self.assertEqual(calls[0][1]['queryType'], 'Latest')
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'capture.json'
            api.save_page(path, page)
            with self.assertRaises(FileExistsError):
                api.save_page(path, {'replacement': True})
            self.assertEqual(json.loads(path.read_text())['tweets'], page['tweets'])

    def test_bad_identity_dates_and_cursor_do_not_fetch(self):
        def unexpected(*args):
            self.fail('Invalid inputs must not make an API request')
        for handle in ['https://x.com/karpathy', 'karpathy OR from:someone', '']:
            with self.assertRaises(ValueError):
                api.search_page(handle, '2023-01-01', '2026-01-01', fetch=unexpected)
        with self.assertRaises(ValueError):
            api.search_page('karpathy', '2026-01-01', '2023-01-01', fetch=unexpected)
        with self.assertRaises(ValueError):
            api.search_page('karpathy', 'bad', '2026-01-01', fetch=unexpected)
        with self.assertRaises(ValueError):
            api.search_page('karpathy', '2023-01-01', '2026-01-01', fetch=lambda *args: {'tweets': [], 'has_next_page': True, 'next_cursor': ''})


if __name__ == '__main__':
    unittest.main(verbosity=2)
