# Maintaining the public edition

Keep the public package separate from the creator's working business files. Bring across only intentional workflow improvements, original summaries, and source metadata. Never copy an entire private workspace or research archive into this repository.

`public-files.json` is the explicit publication list. The Git ignore file permits only those files. A new public file requires a deliberate entry in both places. Validation rejects unexpected files, symbolic links, excluded subject matter, and likely credentials, including inside an existing guide.

Enable the publication check in each maintainer checkout:

```sh
git config core.hooksPath .githooks
```

The push hook inspects every reachable commit proposed for publication, including older snapshots. It reads committed files, so editing the working copy alone cannot conceal content already committed. Keep personal research and business records outside this checkout. Git hooks and automated checks are safeguards, not substitutes for reviewing a public release.

## Release process

1. Edit the relevant skill, guide, or source summary. Preserve source attribution and remaining gaps.
2. Update `VERSION`, the skill manifest version, and `CHANGELOG.md` for the release.
3. Regenerate the skill manifest and run all checks:

```sh
python3 tools/build_release.py --manifest-only
python3 tools/catalog.py --write
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/business-desk/scripts -v
```

4. Inspect the changed file list and the generated archive. Check an installation into an empty temporary folder. Keep customer records and credentials outside the repository.
5. Build the release with `python3 tools/build_release.py`. It writes `dist/business-desk.zip` and `dist/SHA256SUMS.txt`.
6. Commit the reviewed source, push it, and check the repository workflow. Create a versioned GitHub release from that passing commit and attach both files. Use the release notes to explain actual changes and limitations.

Clone the current repository when setting up a new maintainer checkout. Do not merge an archived checkout or attach a release to an unverified old tag. Verify the downloaded release checksum and contents after publishing.

The stable public download URL is the `releases/latest/download/business-desk.zip` link in the README. Keep that asset filename for later releases.

## What the checks establish

Package validation checks local links, metadata, catalog structure, source URLs, file syntax, the export boundary, and file hashes. Tests check fresh installation, repeated installation, updates, backup preservation, rollback, archive extraction, and research helper behavior with synthetic evidence and mocked requests.

These checks do not prove the quality of every AI response, verify all external sources live, or establish a sales or conversion result. Review representative work with the current host tools when behavior changes.

## Updating research

Public briefs contain original summaries, not full evidence snapshots. Add or revise a summary only after reading the relevant original public work. Keep methods with one source labeled as candidates. Preserve joint and company authorship. Record a source link and locator, and describe anything not reviewed.

Do not replace the user's personal library during an install or update. Avoid background update jobs or paid source collection unless the user separately requests them.

## Research counts

The expert index stores the dated archived post counts. Verify these counts against the collection records whenever publishing a research update. The public package contains count metadata and source links, not the underlying archives. Cited X counts are derived from distinct post IDs in the public source directory. Other source entries are counted separately, and multiple entries can refer to one underlying work.

Maintain each professional in exactly one primary category. Regenerate the README and research document with `python3 tools/catalog.py --write`. The validator checks those tables against the metadata, checks cited counts against source URLs, and checks all 24 website areas against the source directory. It cannot independently establish an archive count without the original collection records.
