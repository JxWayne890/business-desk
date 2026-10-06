# Installation and updates

## Requirements

Use a local Codex environment that can read files. Python 3.9 or newer runs the installer and optional helpers. No Python packages need to be installed. Business Desk does not include an AI subscription, API credits, hosting, or connected business accounts.

The bundled skill instructions and references can be read directly by Codex without running a helper. Python is needed only for installation, research storage, verification receipts, and the optional X helper.

## A first installation

Extract the full release ZIP. Run the installer from the extracted `business-desk` directory:

```sh
python3 install.py
python3 install.py --check
```

Use `py -3` on Windows if appropriate for your Python installation. The destination defaults to `~/.agents/skills/business-desk`. The installer reads local files, validates their checksums, and copies the complete skill. It makes no network calls and does not modify Codex settings or install hooks.

For a different skill location:

```sh
python3 install.py --skills-dir /path/to/skills
python3 install.py --skills-dir /path/to/skills --check
```

Choose a skill location supported by your host. [Codex's documented skill locations](https://learn.chatgpt.com/docs/build-skills) include the personal `.agents/skills` folder and project `.agents/skills` folders. Do not install duplicate copies under several scanned locations.

## Manual installation

If Python is unavailable, copy the entire `skills/business-desk` folder into your personal `.agents/skills` folder. This provides the instructions and bundled references, but the Python helpers still need Python when invoked. Do not copy only `SKILL.md`.

The installer will not overwrite a manually managed folder during an update. Move a manual installation to a backup outside the scanned skill directory before installing a new copy. This preserves your changes.

## Update and rollback

Run `python3 install.py --update` from a newly extracted release. Every replacement of a managed install creates a backup under `.business-desk-backups` beside the skills directory, not inside it. The installer prints the exact location. New files are verified in a staging folder before the previous installation is moved. A failed final rename restores the previous installation.

To roll back, close any task using the skill, move the current `business-desk` folder aside, and copy the desired backup back to the skill location. Reopen Codex. Keep the old folder until you have checked the restored version.

## Personal libraries

New expert research uses `~/.business-desk/library` by default. The optional `BUSINESS_DESK_LIBRARY` environment setting or the helper's `--root` argument selects another folder. Keep it outside the installed skill directory. The installer never reads, replaces, or deletes that research.

The installed `references/experts` folder contains the bundled summaries. It is separate from a user's own source snapshots and audit records. A newly installed personal library is empty; the bundled references are still available.

## Troubleshooting

* Skill missing: open a fresh task or restart Codex and invoke `$business-desk` explicitly.
* Checksum mismatch: extract a fresh release. Do not disable verification. If you intentionally edited an installed file, preserve your change before updating.
* Existing unmanaged folder: move it to a backup outside the skills directory, then install.
* No browsing or image tool: use the available summaries and writing workflow, and state what cannot be verified or generated.
* An unavailable referenced page: retain the citation and describe the evidence gap. Do not invent a current source.
* Windows X research: use the user's own `TWITTERAPI_IO_KEY` environment setting. Private file credential storage is supported only on macOS and Linux.

To uninstall, remove only the installed `business-desk` skill folder. Your personal library and backups remain available until you choose to remove them.
