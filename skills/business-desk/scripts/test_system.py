"""Behavioral regression checks, using temporary libraries and projects only."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import expert
import proof

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'library'
        expert.init(argparse.Namespace(slug='example-person', name='Example Person', scope='Test methods'), self.root)
        self.path = self.root / 'example-person'

    def add(self, text='Understand one example.', url='https://example.org/a', work='work-a'):
        file = Path(self.tmp.name) / 'evidence.txt'
        file.write_text(text, encoding='utf-8')
        return expert.add(argparse.Namespace(slug='example-person', file=str(file), url=url, title='Evidence',
              author='Example Person', work=work, by_subject=True, kind='writing', capture='excerpt',
              published='unknown', notes='Synthetic fixture'), self.root)

    def complete(self, ids):
        p = expert.read(self.path / 'profile.json')
        p.update(identity_status='verified', identity_urls=['https://example.org'])
        expert.write(self.path / 'profile.json', p)
        coverage = {'categories': {c: {'status': 'reviewed', 'notes': 'Synthetic evidence only'} for c in expert.CATEGORIES},
                    'last_researched_at': expert.now(), 'queries': ['Example Person'],
                    'attempts': [{'url': 'https://example.org', 'status': 'inspected'}], 'gaps': []}
        expert.write(self.path / 'coverage.json', coverage)
        for sid in ids:
            (self.path / 'wiki/sources' / (sid + '.md')).write_text('Evidence synthesis.', encoding='utf-8')
        for name in ['hot', 'principles', 'coverage']:
            (self.path / 'wiki' / (name + '.md')).write_text('Synthetic completed synthesis.', encoding='utf-8')

    def rule(self, sources, quote='Understand one example.'):
        return {'principles': [{'id': 'p1', 'title': 'Example method', 'status': 'supported',
                'application': 'Test application', 'evidence': [
                 {'source_id': sid, 'quote': quote, 'locator': 'Opening', 'interpretation': 'Test support'} for sid in sources]}]}

    def test_generic_name_and_duplicate_are_preserved(self):
        first = self.add()
        again = self.add()
        self.assertEqual(again['status'], 'already_present')
        self.assertEqual(expert.read(self.path / 'profile.json')['name'], 'Example Person')
        self.assertEqual(len(expert.read(self.path / 'manifest.json')['sources']), 1)
        newer = self.add(text='Understand one example. Then expand.')
        self.assertEqual(newer['source']['supersedes'], [first['source']['id']])
        self.assertEqual((self.path / first['source']['raw_path']).read_text(), 'Understand one example.')

    def test_mirrors_do_not_promote_a_method(self):
        a = self.add()['source']['id']
        b = self.add(url='https://mirror.example.org/a')['source']['id']
        self.complete([a, b])
        expert.write(self.path / 'principles.json', self.rule([a, b]))
        self.assertTrue(any('two distinct' in e for e in expert.audit(self.path)['errors']))

    def test_distinct_works_pass_and_fabricated_quote_fails(self):
        a = self.add()['source']['id']
        b = self.add(text='Understand one example. A different work.', url='https://example.org/b', work='work-b')['source']['id']
        self.complete([a, b])
        expert.write(self.path / 'principles.json', self.rule([a, b]))
        self.assertTrue(expert.audit(self.path)['ok'])
        expert.write(self.path / 'principles.json', self.rule([a, b], 'Invented attribution'))
        self.assertFalse(expert.audit(self.path)['ok'])

    def test_raw_tampering_and_broken_links_fail(self):
        s = self.add()['source']
        self.complete([s['id']])
        raw = self.path / s['raw_path']
        raw.chmod(0o644)
        raw.write_text('Changed evidence.')
        (self.path / 'wiki/hot.md').write_text('[bad](missing.md)')
        errors = expert.audit(self.path)['errors']
        self.assertTrue(any('changed raw' in e for e in errors))
        self.assertTrue(any('Broken' in e for e in errors))

    def test_research_notes_cannot_corroborate_attributed_methods(self):
        a = self.add()['source']['id']
        b = self.add(text='Understand one example. My notes.', url='https://example.org/b', work='work-b')['source']['id']
        self.complete([a, b])
        manifest = expert.read(self.path / 'manifest.json')
        manifest['sources'][1]['capture'] = 'research_notes'
        expert.write(self.path / 'manifest.json', manifest)
        expert.write(self.path / 'principles.json', self.rule([a, b]))
        self.assertTrue(any('two distinct' in e for e in expert.audit(self.path)['errors']))

    def test_empty_evidence_path_escape_and_overwrite_are_rejected(self):
        with self.assertRaises(ValueError): self.add(text='  ')
        with self.assertRaises(ValueError): expert.safe_slug('../outside')
        with self.assertRaises(ValueError): expert.local(self.path, '../../outside')
        with self.assertRaises(ValueError):
            expert.init(argparse.Namespace(slug='example-person', name='Other', scope='Other'), self.root)

    def test_incomplete_identity_and_coverage_fail(self):
        result = expert.audit(self.path)
        self.assertFalse(result['ok'])
        self.assertTrue(any('Identity' in e for e in result['errors']))
        self.assertTrue(any('Coverage' in e for e in result['errors']))

class ProofTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'library'
        self.project = Path(self.tmp.name) / 'project'
        self.project.mkdir()
        (self.project / 'value.txt').write_text('correct', encoding='utf-8')
        self.session = 'synthetic-session'

    def begin(self, code=None, timeout=5):
        plan = Path(self.tmp.name) / 'plan.json'
        expert.write(plan, [{'label': 'Actual file content', 'reason': 'Checks expected data in the scoped file',
                    'argv': [sys.executable, '-c', code or "from pathlib import Path; assert Path('value.txt').read_text() == 'correct'"]}])
        return proof.begin(argparse.Namespace(session=self.session, checks=str(plan), cwd=str(self.project),
                    files=['value.txt'], expert='example-person', timeout=timeout), self.root)

    def event(self, **kwargs):
        return dict({'hook_event_name': 'Stop', 'session_id': self.session,
                     'cwd': str(self.project), 'stop_hook_active': False}, **kwargs)

    def test_successful_receipt_becomes_stale_after_edit(self):
        self.begin()
        self.assertTrue(proof.run(self.root, self.session)['verified'])
        (self.project / 'value.txt').write_text('incorrect')
        self.assertFalse(proof.status(proof.get_record(self.root, self.session)[2])['verified'])
        self.assertEqual(proof.hook(self.root, self.event())['decision'], 'block')

    def test_failed_command_and_honest_close(self):
        self.begin('raise SystemExit(7)')
        result = proof.run(self.root, self.session)
        self.assertFalse(result['verified'])
        self.assertEqual(result['results'][0]['exit_code'], 7)
        with self.assertRaises(ValueError): proof.finish(self.root, self.session)
        self.assertFalse(proof.finish(self.root, self.session, 'A real failure')['verified'])

    def test_changes_during_run_invalidate_receipt(self):
        self.begin("from pathlib import Path; Path('value.txt').write_text('changed')")
        self.assertFalse(proof.run(self.root, self.session)['verified'])

    def test_timeout_is_not_success(self):
        self.begin('import time; time.sleep(2)', timeout=1)
        result = proof.run(self.root, self.session)
        self.assertFalse(result['verified'])
        self.assertEqual(result['results'][0]['exit_code'], 124)

    def test_hook_scope_and_bounded_continuation(self):
        self.begin()
        other = self.event(); other['session_id'] = 'unrelated'
        self.assertEqual(proof.hook(self.root, other), {})
        other = self.event(); other['cwd'] = self.tmp.name
        self.assertEqual(proof.hook(self.root, other), {})
        other = self.event(); other['hook_event_name'] = 'SubagentStop'
        self.assertEqual(proof.hook(self.root, other), {})
        self.assertEqual(proof.hook(self.root, self.event())['decision'], 'block')
        continued = self.event(); continued['stop_hook_active'] = True
        self.assertIn('unverified', proof.hook(self.root, continued)['systemMessage'])
        self.assertEqual(proof.hook(self.root, self.event()), {})

    def test_passed_hook_closes_and_preserves_receipt(self):
        first = self.begin()
        proof.run(self.root, self.session)
        self.assertEqual(proof.hook(self.root, self.event()), {})
        self.assertTrue(expert.read(first['record'])['closed'])
        self.assertTrue(expert.read(first['record'])['outcome']['verified'])

    def test_scope_cannot_escape_project(self):
        with self.assertRaises(ValueError): proof.snapshot(str(self.project), ['../secret'])

    def test_cli_missing_and_malformed_hook_input_are_json(self):
        script = Path(__file__).parent / 'proof.py'
        r = subprocess.run([sys.executable, str(script), '--root', str(self.root), 'hook'],
                           input='{broken', text=True, capture_output=True)
        self.assertEqual(r.returncode, 0)
        self.assertIn('could not be checked', json.loads(r.stdout)['systemMessage'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
