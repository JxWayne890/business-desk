import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import install

class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.source=self.root/'source'
        shutil.copytree(ROOT/'skills/business-desk',self.source,ignore=shutil.ignore_patterns('__pycache__'))
        self.skills=self.root/'skills with spaces'
        self.target=self.skills/'business-desk'

    def test_fresh_install_has_all_references_and_is_repeatable(self):
        result=install.install(self.source,self.skills)
        self.assertEqual(result['status'],'installed')
        self.assertEqual(install.verify(self.target),install.verify(self.source))
        self.assertEqual(len(json.loads((self.target/'references/experts/index.json').read_text())),48)
        self.assertTrue((self.target/'references/cold-outreach/workflow.md').is_file())
        self.assertEqual(len(json.loads((self.target/'references/website-categories.json').read_text())),24)
        self.assertEqual(install.install(self.source,self.skills)['status'],'already_current')

    def test_edits_preserved_by_default_and_backed_up_on_update(self):
        install.install(self.source,self.skills)
        notes=self.target/'my-notes.md'
        notes.write_text('My personal changes',encoding='utf-8')
        research=self.root/'personal library'
        research.mkdir()
        (research/'keep.txt').write_text('My research',encoding='utf-8')
        with self.assertRaises(ValueError):
            install.install(self.source,self.skills)
        self.assertTrue(notes.exists())
        with patch.dict(os.environ,{'BUSINESS_DESK_LIBRARY':str(research)}):
            result=install.install(self.source,self.skills,True)
        self.assertEqual(result['status'],'updated')
        self.assertEqual((Path(result['backup'])/'my-notes.md').read_text(),'My personal changes')
        self.assertNotIn(self.skills,Path(result['backup']).parents)
        self.assertEqual((research/'keep.txt').read_text(),'My research')
        install.verify(self.target)

    def test_corrupt_source_never_replaces_existing_install(self):
        install.install(self.source,self.skills)
        original=(self.target/'SKILL.md').read_bytes()
        (self.source/'SKILL.md').write_text('Corrupt source',encoding='utf-8')
        with self.assertRaises(ValueError):
            install.install(self.source,self.skills,True)
        self.assertEqual((self.target/'SKILL.md').read_bytes(),original)

    def test_unmanaged_directory_is_never_replaced(self):
        self.target.mkdir(parents=True)
        (self.target/'notes.txt').write_text('Keep this',encoding='utf-8')
        with self.assertRaises(ValueError):
            install.install(self.source,self.skills,True)
        self.assertEqual((self.target/'notes.txt').read_text(),'Keep this')

    def test_failed_final_move_restores_previous_installation(self):
        install.install(self.source,self.skills)
        (self.target/'notes.txt').write_text('Keep this',encoding='utf-8')
        original=Path.rename
        def fail_stage(path,dest):
            if path.parent.name.startswith('.business-desk-stage-'):
                raise OSError('Synthetic final move failure')
            return original(path,dest)
        with patch.object(Path,'rename',fail_stage),self.assertRaises(OSError):
            install.install(self.source,self.skills,True)
        self.assertEqual((self.target/'notes.txt').read_text(),'Keep this')

    @unittest.skipUnless(os.name=='posix','Symbolic link fixture uses POSIX permissions')
    def test_symbolic_links_are_rejected_without_touching_target(self):
        self.skills.mkdir()
        real=self.root/'real'
        real.mkdir()
        self.target.symlink_to(real,target_is_directory=True)
        with self.assertRaises(ValueError):
            install.install(self.source,self.skills,True)
        self.assertEqual(list(real.iterdir()),[])

    def test_relocated_installed_helpers_use_separate_library(self):
        install.install(self.source,self.skills)
        library=self.root/'separate research'
        env=dict(os.environ,BUSINESS_DESK_LIBRARY=str(library))
        script=self.target/'scripts/expert.py'
        result=subprocess.run([sys.executable,str(script),'init','example-person','--name','Example Person','--scope','Synthetic test'],env=env,text=True,capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        self.assertTrue((library/'example-person/profile.json').is_file())
        result=subprocess.run([sys.executable,str(script),'list'],env=env,text=True,capture_output=True)
        self.assertEqual(json.loads(result.stdout)[0]['name'],'Example Person')
        install.verify(self.target)

    def test_cli_check_and_failure_exit_status(self):
        subprocess.run([sys.executable,str(ROOT/'install.py'),'--skills-dir',str(self.skills)],check=True,capture_output=True)
        result=subprocess.run([sys.executable,str(ROOT/'install.py'),'--skills-dir',str(self.skills),'--check'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        (self.target/'SKILL.md').write_text('Edited',encoding='utf-8')
        result=subprocess.run([sys.executable,str(ROOT/'install.py'),'--skills-dir',str(self.skills),'--check'],capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)

if __name__=='__main__':
    unittest.main()
