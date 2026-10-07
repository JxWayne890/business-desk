import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from catalog import source_counts, validate_catalog, x_post_id
from validate import package_files


class CatalogTests(unittest.TestCase):
    def copy_package(self,root):
        for path in package_files(ROOT):
            target=root/path.relative_to(ROOT)
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(path,target)

    def test_posts_are_deduplicated_without_counting_profiles_or_other_hosts(self):
        sources=[
            {'url':'https://x.com/example/status/123','work_id':'one'},
            {'url':'https://twitter.com/example/status/123/photo/1','work_id':'one'},
            {'url':'https://x.com/example','work_id':'identity'},
            {'url':'https://example.org/example/status/123','work_id':'article'},
        ]
        self.assertEqual(source_counts(sources),{'sources':4,'underlying_works':3,'x_posts_cited':1,'other_source_entries':2})
        self.assertIsNone(x_post_id('https://notx.com/example/status/123'))

    def test_published_coverage_has_all_roles_and_website_areas(self):
        result=validate_catalog()
        self.assertEqual(result['active_roles'],46)
        self.assertEqual(result['supplemental_roles'],2)
        self.assertEqual(result['categories'],9)

    def test_inflated_source_count_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            self.copy_package(root)
            path=root/'skills/business-desk/references/experts/index.json'
            data=json.loads(path.read_text(encoding='utf-8'))
            data[0]['x_posts_cited']+=100
            path.write_text(json.dumps(data),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Research count mismatch'):
                validate_catalog(root)

    def test_uncategorized_expert_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            self.copy_package(root)
            path=root/'skills/business-desk/references/experts/categories.json'
            data=json.loads(path.read_text(encoding='utf-8'))
            data[0]['experts'].pop()
            path.write_text(json.dumps(data),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'exactly one'):
                validate_catalog(root)

    def test_invented_website_evidence_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            self.copy_package(root)
            path=root/'skills/business-desk/references/website-categories.json'
            data=json.loads(path.read_text(encoding='utf-8'))
            data[0]['evidence'][0]['source_id']='nonexistent'
            path.write_text(json.dumps(data),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Website evidence'):
                validate_catalog(root)

    def test_readme_cannot_silently_disagree_with_research_data(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            self.copy_package(root)
            path=root/'README.md'
            text=path.read_text(encoding='utf-8').replace('46 active expert roles','99 active expert roles')
            path.write_text(text,encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'README research table is stale'):
                validate_catalog(root)


if __name__=='__main__':
    unittest.main()
