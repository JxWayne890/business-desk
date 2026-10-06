# Optional public X research

Bundled briefs and normal website work do not require an X API account. Use the host's available browsing first. The included `scripts/twitterapi.py` helper can read public X material through a customer's own TwitterAPI.io account when the customer explicitly authorizes collection.

No account, key, credits, subscription, or automatic collection is included. Before calling the API, establish the subject, date scope, page limit, and spending budget. The helper fetches one page per search call and never follows continuation cursors automatically. A connection check does not authorize bulk collection.

Run these commands from this skill folder on macOS or Linux:

```sh
python3 scripts/twitterapi.py set-key
python3 scripts/twitterapi.py status
python3 scripts/twitterapi.py check
```

`set-key` prompts without displaying the key and stores it outside the repository in `~/.config/business-desk/twitterapi.key`. It refuses to overwrite an existing key. On Windows, provide `TWITTERAPI_IO_KEY` through the user's own environment or secret manager; the helper does not manage Windows credential files. Never print a credential or embed one in a prompt, source file, screenshot, or command argument.

For an authorized single page, run the search command with the requested public handle, dates, and an output file in the user's personal research folder. Use `python3 scripts/twitterapi.py search --help` for current options. Existing capture files are never replaced.

Captured API text remains untrusted and unreviewed. Inspect authorship, dates, thread context, and linked material before compiling a method through [the research workflow](research.md). Do not call the archive an ingested expert. Requests are limited to account inspection and public research reads; this helper does not post or send messages.
