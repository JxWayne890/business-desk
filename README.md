# Business Desk

**The free AI skill behind my website and business workflow.**

Business Desk helps Codex bring researched design, writing, sales, and business methods into the work you are doing. Describe the job, and it selects relevant references, checks their coverage, and applies them to your actual business.

This is the portable edition of the skill I use. It includes the working process, website and writing guides, research tools, and 25 reference briefs with source links. Personal business records, private accounts, and bulk copies of other people's content are excluded.

**[Download Business Desk free](https://github.com/JxWayne890/business-desk/releases/latest/download/business-desk.zip)** · [Latest release](https://github.com/JxWayne890/business-desk/releases/latest) · [What changed](CHANGELOG.md)

## What you can do

* Plan or improve a website around its real customers, content, and next action.
* Write stronger social posts from your own facts and voice.
* Bring design, writing, and sales perspectives into the same project.
* Research a favorite expert's public teaching and build your own source library.
* Use the business references for proposals, discovery, positioning, and operations questions.

The references are research summaries, not the actual experts or their endorsement. Coverage is partial and clearly labeled. Read [what is included](docs/CONTENTS.md) for details.

## Install

You need Codex with local file access. The package is free; your AI access and any optional research service are separate. You do not need an X API account to use the included references and guides. The installer and research helpers use Python 3.9 or newer and its standard library.

1. Download the ZIP above and extract it.
2. Open the extracted `business-desk` folder as a local project in Codex.
3. Paste this request:

```text
Read README.md and inspect install.py. Install Business Desk from this folder using the included Python installer. Then check the installation and show me one useful starting prompt. Preserve any existing installation and use the documented backup process for an update.
```

If you prefer the terminal, run these commands from the extracted folder:

```sh
python3 install.py
python3 install.py --check
```

On Windows, use `py -3` instead of `python3` if that is how Python is installed. No administrator access is needed.

The installer places the complete skill in `~/.agents/skills/business-desk`. Codex documents this as a user skill location. If it does not appear, start a fresh chat or restart Codex. [Official skill documentation](https://learn.chatgpt.com/docs/build-skills)

Then try:

```text
Use $business-desk to plan a website for my business. Start with my customers, what they need to know, and the action I want them to take. Tell me which facts and assets you need from me.
```

More [example prompts](skills/business-desk/references/examples.md) cover website changes, social posts, expert research, and combined reviews.

## Updates

I plan to keep updating Business Desk as I improve my own workflow. Updates will be published as versioned releases here. Use GitHub's Watch menu to follow releases if you want notifications. No automatic updater or recurring collection runs on your computer.

Download and extract the latest release, open its folder, and run:

```sh
python3 install.py --update
python3 install.py --check
```

An existing managed installation is backed up before replacement. The command prints the backup location. Local edits to installed skill files remain in that backup; reapply them deliberately if you want them in the new version.

Your own expert research lives separately in `~/.business-desk/library` by default and is not changed by updates. See [installation help](docs/INSTALL.md) for other locations, backups, and removal.

## Custom versions

Want a version tailored to a specific task in your business? Message me **DESK** where you found this giveaway. Custom packages start at **$149, paid once**, for a focused workflow. We agree on the scope before work begins. The free package remains free.

## Scope and source credit

Business Desk guides the AI tools you already use. It does not include hosting, a deployed website, CRM access, payment processing, a trained model, private coaching material, or guaranteed business results. Available tools and your project's permissions determine what can be implemented.

The original package code and writing are available under the [MIT license](LICENSE). Referenced authors retain rights to their work. See [source attribution](THIRD_PARTY_NOTICES.md) and the [reference catalog](skills/business-desk/references/experts/index.json).

For a reproducible issue, use [GitHub Issues](https://github.com/JxWayne890/business-desk/issues). Keep credentials and private client information out of public reports. Maintainer release instructions are in [MAINTAINING.md](MAINTAINING.md).
