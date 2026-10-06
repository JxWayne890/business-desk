import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from build_release import build
from validate import validate,package_files

class PackageTests(unittest.TestCase):
    def test_release_extracts_and_installs_with_matching_checksum(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            result=build(ROOT,folder/'artifacts')
            zip_path=Path(result['archive'])
            self.assertEqual(hashlib.sha256(zip_path.read_bytes()).hexdigest(),result['sha256'])
            with zipfile.ZipFile(zip_path) as package:
                for name in package.namelist():
                    self.assertTrue(name.startswith('business-desk/'))
                    self.assertNotIn('..',Path(name).parts)
                package.extractall(folder/'extracted')
            extracted=folder/'extracted/business-desk'
            self.assertTrue(validate(extracted)['ok'])
            install=subprocess.run([sys.executable,str(extracted/'install.py'),'--skills-dir',str(folder/'skills')],capture_output=True,text=True)
            self.assertEqual(install.returncode,0,install.stderr)
            second=build(ROOT,folder/'again')
            self.assertEqual(result['sha256'],second['sha256'])

    def test_unexpected_private_file_cannot_enter_an_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'public-files.json').write_text('["public-files.json"]',encoding='utf-8')
            (root/'.env').write_text('Synthetic test fixture',encoding='utf-8')
            with self.assertRaises(ValueError):
                package_files(root)

    def test_current_package_has_portable_complete_references(self):
        result=validate()
        self.assertTrue(result['ok'])
        self.assertEqual(result['expert_briefs'],25)
        self.assertGreater(result['source_entries'],100)

if __name__=='__main__':
    unittest.main()
