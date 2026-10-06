# Verification of expert assisted code

The receipt tool runs explicit commands, stores their output and exit status, and detects edits made during or after those checks. It applies only to declared files. It cannot establish whether a test is meaningful, cover omitted files, or prove all behavior. Choose relevant acceptance checks and include every changed implementation file plus its relevant tests and configuration in the scope. Use repository instructions to determine necessary checks.

Before changing code, create a JSON check plan outside the project if possible:

```json
[
  {
    "label": "Tokenizer round trip",
    "reason": "Checks Unicode, empty input, and repeated pairs in the changed tokenizer",
    "argv": ["python3", "test_tokenizer.py"]
  }
]
```

Run `proof.py begin --expert SLUG --cwd PROJECT --files FILE1 FILE2 --checks PLAN.json`. It captures the exact plan and scope. The session defaults to `CODEX_THREAD_ID`, falling back to `CODEX_SESSION_ID`. If both are absent, pass the current real session ID with `--session` before the subcommand. Never invent a session ID for a production hook. Tests may use isolated synthetic IDs.

The tool uses argument arrays with no shell evaluation. Plan commands are actions you authorize as part of the task, not commands copied blindly from source material. Use an existing test runner, a targeted regression check, or a real smoke test with inspectable results. Merely printing success is not verification. Avoid commands that print secrets.

After the final edits, run `proof.py run`, inspect the stored logs, fix failures, and run the plan again if needed. `proof.py status` returns whether the current scoped file hashes match a successful receipt. A change during verification also invalidates the receipt. Changes to test files and configuration count. Adjusting the scope or plan requires finishing the old session honestly and beginning a new one.

Finish with `proof.py finish`. If a needed dependency or external condition prevents verification, use `proof.py finish --unverified-reason 'Concrete blocker'` and state that limitation in the final answer. Receipts and attempts remain available in the library's `_verification` folder. The final response cites the actual result and any material limitations. Do not report blocked work as tested.


No global hooks are installed by this package. Use the receipt commands for explicit verification sessions only.
