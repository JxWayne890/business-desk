#!/usr/bin/env python3
"""Render and verify public expert categories and research counts."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- EXPERT_CATALOG_START -->'
END = '<!-- EXPERT_CATALOG_END -->'


def x_post_id(url):
    parts = urlsplit(url)
    if parts.hostname not in {'x.com','www.x.com','twitter.com','www.twitter.com','mobile.twitter.com'}:
        return None
    match = re.match(r'/[^/]+/status/(\d+)(?:/|$)',parts.path)
    return match.group(1) if match else None


def source_counts(sources):
    return {
        'sources':len(sources),
        'underlying_works':len({s['work_id'] for s in sources}),
        'x_posts_cited':len({x_post_id(s['url']) for s in sources if x_post_id(s['url'])}),
        'other_source_entries':sum(x_post_id(s['url']) is None for s in sources),
    }


def load(root=ROOT):
    folder = Path(root)/'skills/business-desk/references/experts'
    return tuple(json.loads((folder/name).read_text(encoding='utf-8')) for name in ['index.json','categories.json','sources.json'])


def render(root=ROOT, prefix='skills/business-desk/references/experts/', collapsible=True):
    people, categories, sources = load(root)
    lookup = {p['slug']:p for p in people}
    active = sum(p['group']=='active' for p in people)
    supplemental = len(people)-active
    counts = source_counts(sources)
    archived = sum(p['x_archived_posts'] for p in people)
    lines = [
        f"**{active} active expert roles, {supplemental} supplemental imagery references, and {len(categories)} categories.**",
        '',
        f"The expert research catalog, dated October 6, 2026, records **{len(sources)} source entries**, including **{counts['x_posts_cited']} distinct X posts cited** and **{counts['other_source_entries']} other source entries**. The underlying collections contain **{archived:,} archived X posts** across these professionals.",
        '',
        '**How to read the counts:** Archived X posts are collected research inputs. They were not all reviewed, and the archives are not included in this download. X posts cited counts distinct post URLs used in the included references, including inspected text or limited visual observations. Other source entries include articles, books or training excerpts, LinkedIn posts, technical work, and identity references. Multiple entries can belong to one underlying work. A zero in the X column can mean the role is grounded in other public sources.',
        '',
        'These are selected research summaries with coverage gaps. The professionals have not endorsed this package. Source links, capture types, authorship, and candidate or supported method labels are recorded in each brief. Platform documentation cited in the workflow guides is separate from these expert counts.',
        '',
    ]
    for category in categories:
        members = [lookup[s] for s in category['experts']]
        if collapsible:
            lines += ['<details>', '<summary>'+category['name']+' ('+str(len(members))+' references)</summary>', '']
        else:
            lines += ['## '+category['name'],'']
        lines += [category['helps_with'],'','| Professional | Focus | X posts archived | X posts cited | Other source entries |','| :--- | :--- | ---: | ---: | ---: |']
        for p in members:
            name='['+p['name']+']('+prefix+p['brief']+')'
            if p['group']=='supplemental':
                name+=' (supplemental)'
            lines.append('| '+name+' | '+p['role'].replace('|','/')+' | '+f"{p['x_archived_posts']:,}"+' | '+str(p['x_posts_cited'])+' | '+str(p['other_source_entries'])+' |')
        lines.append('')
        if collapsible:
            lines += ['</details>','']
    return '\n'.join(lines).rstrip()


def research_document(root=ROOT):
    return '# Expert categories and research coverage\n\n'+render(root,'../skills/business-desk/references/experts/',False)+'\n'


def validate_catalog(root=ROOT):
    root=Path(root)
    people, categories, sources=load(root)
    known={p['slug'] for p in people}
    membership=[slug for category in categories for slug in category['experts']]
    if len(membership)!=len(set(membership)) or set(membership)!=known:
        raise ValueError('Each professional must appear in exactly one public category')
    category_ids=[c['id'] for c in categories]
    if len(category_ids)!=len(set(category_ids)):
        raise ValueError('Duplicate public category')
    records={(s['expert'],s['source_id']):s for s in sources}
    if len(records)!=len(sources):
        raise ValueError('Duplicate source identifier')
    for p in people:
        assigned=[c for c in categories if p['slug'] in c['experts']]
        if assigned[0]['id']!=p['category']:
            raise ValueError('Expert category disagrees with the catalog')
        if type(p['x_archived_posts']) is not int or p['x_archived_posts']<0:
            raise ValueError('Invalid archive count')
        actual=source_counts([s for s in sources if s['expert']==p['slug']])
        for field,value in actual.items():
            if p[field]!=value:
                raise ValueError('Research count mismatch: '+p['slug']+' '+field)
    website=json.loads((root/'skills/business-desk/references/website-categories.json').read_text(encoding='utf-8'))
    if {c['id'] for c in website}!=set(range(1,25)) or len(website)!=24:
        raise ValueError('Website coverage must contain 24 distinct areas')
    for category in website:
        if category['lead'] not in known or any(s not in known for s in category['support']):
            raise ValueError('Website area references an unavailable expert')
        for evidence in category['evidence']:
            source=records.get((evidence['slug'],evidence['source_id']))
            if not source or any(evidence[k]!=source[k] for k in ['url','work_id']):
                raise ValueError('Website evidence does not match the public source directory')
            if evidence['source_page']!='experts/'+evidence['slug']+'.md':
                raise ValueError('Website evidence path is not portable')
    readme=(root/'README.md').read_text(encoding='utf-8')
    if readme.count(START)!=1 or readme.count(END)!=1:
        raise ValueError('README requires one generated expert catalog')
    actual=readme.split(START,1)[1].split(END,1)[0].strip()
    if actual!=render(root):
        raise ValueError('README research table is stale; run python tools/catalog.py --write')
    if (root/'docs/RESEARCH.md').read_text(encoding='utf-8')!=research_document(root):
        raise ValueError('Research coverage document is stale')
    return {'active_roles':sum(p['group']=='active' for p in people),'supplemental_roles':sum(p['group']=='supplemental' for p in people),'categories':len(categories),**source_counts(sources),'archived_x_posts':sum(p['x_archived_posts'] for p in people)}


def write(root=ROOT):
    path=Path(root)/'README.md'
    text=path.read_text(encoding='utf-8')
    if text.count(START)!=1 or text.count(END)!=1:
        raise ValueError('README requires one generated expert catalog')
    before,rest=text.split(START,1)
    _,after=rest.split(END,1)
    path.write_text(before+START+'\n\n'+render(root)+'\n\n'+END+after,encoding='utf-8')
    (Path(root)/'docs/RESEARCH.md').write_text(research_document(root),encoding='utf-8')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    if args.write:
        write()
    print(json.dumps(validate_catalog(),indent=2))
