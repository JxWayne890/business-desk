import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from build_release import manifest
from validate import package_files, validate


class PublicationTests(unittest.TestCase):
    def copy_public(self, root):
        for source in package_files(ROOT):
            target = root/source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def test_existing_guide_cannot_publish_excluded_content(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_public(root)
            path = root/'skills/business-desk/references/examples.md'
            with path.open('a') as handle:
                handle.write('\nCommercial '+'clean'+'ing'+' operations\n')
            manifest(root)
            with self.assertRaisesRegex(ValueError, 'Excluded content'):
                validate(root)

    def test_unknown_brief_is_ignored_and_cannot_be_packaged(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_public(root)
            subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
            relative = 'skills/business-desk/references/experts/personal-operations.md'
            (root/relative).write_text('Personal fixture')
            ignored = subprocess.run(['git', 'check-ignore', '-q', relative], cwd=root)
            self.assertEqual(ignored.returncode, 0)
            with self.assertRaisesRegex(ValueError, 'Unexpected file'):
                package_files(root)

    def test_allowed_file_cannot_link_to_personal_material(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)/'package'
            self.copy_public(root)
            source = Path(temp)/'personal.md'
            source.write_text('Personal fixture')
            target = root/'skills/business-desk/references/examples.md'
            target.unlink()
            try:
                target.symlink_to(source)
            except OSError as exc:
                self.skipTest('Host cannot create symbolic links: '+str(exc))
            with self.assertRaisesRegex(ValueError, 'symbolic link'):
                package_files(root)

    def test_clean_tip_does_not_hide_excluded_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_public(root)
            def git(*args):
                return subprocess.run(['git', *args], cwd=root, check=True, capture_output=True)
            git('init', '-q')
            git('config', 'user.name', 'Package Test')
            git('config', 'user.email', 'test@example.invalid')
            path = root/'README.md'
            original = path.read_text()
            path.write_text(original+'\nCommercial '+'clean'+'ing'+' operations\n')
            git('add', '.')
            git('commit', '-qm', 'Synthetic prior snapshot')
            path.write_text(original)
            git('add', 'README.md')
            git('commit', '-qm', 'Restore public guide')
            self.assertTrue(validate(root)['ok'])
            result = subprocess.run([sys.executable, 'tools/check_publication.py', '--refs', 'HEAD'], cwd=root, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Excluded content', result.stderr)

    def test_forced_ignored_archive_cannot_enter_published_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.copy_public(root)
            def git(*args):
                return subprocess.run(['git', *args], cwd=root, check=True, capture_output=True)
            git('init', '-q')
            git('config', 'user.name', 'Package Test')
            git('config', 'user.email', 'test@example.invalid')
            (root/'dist').mkdir()
            (root/'dist/personal.zip').write_bytes(b'Synthetic private artifact')
            git('add', '.')
            git('add', '-f', 'dist/personal.zip')
            git('commit', '-qm', 'Synthetic forced artifact')
            result = subprocess.run([sys.executable, 'tools/check_publication.py', '--refs', 'HEAD'], cwd=root, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('unapproved', result.stderr)


if __name__ == '__main__':
    unittest.main()
