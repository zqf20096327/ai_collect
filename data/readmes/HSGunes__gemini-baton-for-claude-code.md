# gemini-baton-for-claude-code

[![Tests](https://github.com/HSGunes/gemini-baton-for-claude-code/actions/workflows/tests.yml/badge.svg)](https://github.com/HSGunes/gemini-baton-for-claude-code/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Gemini Baton is a Claude Code plugin that hands coding tasks to a Gemini sub-agent (through Google's `agy` / Antigravity CLI) while Claude keeps the plan and the final check.

Claude writes the task and acceptance criteria. Gemini implements it in the background, and Claude then runs **your** tests against the result. If the tests fail, the same Gemini conversation gets the failure and fixes it. Most of the token-heavy work runs on your Gemini quota instead of your Claude usage. Unlike one-shot bridges that send a prompt and read the answer, Baton manages long-running tasks with write access: it checks permissions up front, keeps state, continues conversations and runs a test-and-fix loop.

[Türkçe README](README.tr.md)

<p align="center"><img src="assets/demo.svg" alt="Terminal demo: baton hands a failing slugify() fix to Gemini, then pytest passes" width="900"></p>

*Recorded from a real run ([`assets/demo.txt`](assets/demo.txt); path truncated), regenerated with `python3 scripts/make_demo_svg.py assets/demo.txt assets/demo.svg`; Gemini fixed `src/slug.py`, 1 round, 75.2 s, 41,611 tokens (`baton durum`).*

```text
You ─▶ Claude Code            plans, writes the task file, verifies with your tests
         └─▶ baton:ajan-yonetici   optional Sonnet subagent that runs the whole loop
               └─▶ baton CLI ─▶ agy ─▶ Gemini   implements in the background
```

## Features

- **Background tasks.** `baslat` returns immediately and `bekle` blocks until the task finishes, so Claude can do other work in the meantime.
- **Verification by your own tests.** `dogrula --test "<cmd>"` runs your command and sends failures back to Gemini for up to `--tur` fix rounds (default 3; tests run at most `N + 1` times).
- **Continue in context.** `devam` resumes the same Gemini conversation (`--conversation <id>`), so fixes keep the earlier context.
- **Narrow write access.** Gemini may only write to the `--yaz` directories. Missing rules stop the run with exit code 2 before any tokens are spent.
- **Sandboxed by default.** With no `--komut` prefixes the terminal is disabled (`--sandbox`).
- **Context-friendly for Claude.** `rapor` prints a compact summary, and the optional subagent keeps the whole loop out of your main session.
- **Orchestrator models.** agy's orchestrator models can be selected explicitly with `--orkestra` (`--orchestrate`); they are never selected automatically as the default.
- **Zero dependencies.** A single Python 3.10+ file using only the standard library, with 65 tests that run against a fake `agy`.

## Measured cost

Individual measurements from development sessions on this repository:

| Task | Gemini (`baton durum`) | Claude side |
|---|---|---|
| Automatic model catalog feature (model: neon) | ~420k tokens, 716 s | ~48k tokens (Sonnet manager subagent) |
| Orchestrator mode feature (`--orkestra`) | ~459k tokens, 485 s | ~56k tokens (Sonnet manager subagent) |
| End-to-end small fix via `/baton:devret` (model: hydrogen) | ~40k tokens, 36 s | not measured |
| Demo above (slugify fix) | 41,611 tokens, 75.2 s | not measured |

- These are individual measurements from this project's own development sessions, not a benchmark; every task is different. The Gemini column is `baton durum` tokens (input + output; cache reads are not included).
- "Claude side" is the reported total token count of the `baton:ajan-yonetici` Sonnet subagent (writing the task, waiting, checking). The main session only sees a short result; the main session's own tokens are not in this table. The Claude side was not measured for the last two rows.
- Simple math: in the first two tasks, about 10–11% of the combined tokens were on the Claude side and about 89–90% on Gemini (48/(420+48) ≈10.3%; 56/(459+56) ≈10.9%). Tokens are not the same price or quota unit across the two providers; this is not a "money saved" claim, just an indication of where the work shifts.

## Requirements

- Claude Code (for the plugin)
- Google Antigravity CLI `agy` on `PATH`, signed in
- Python 3.10+
- Linux or macOS (CI runs the test suite on both, Python 3.10–3.13). Windows is not supported.

## Quick start

```bash
claude plugin marketplace add HSGunes/gemini-baton-for-claude-code
claude plugin install baton@gemini-baton
mkdir -p ~/.local/bin
ln -sfn "$(ls -d ~/.claude/plugins/cache/gemini-baton/baton/* | sort -V | tail -1)/bin/baton" ~/.local/bin/baton
export AJAN_DIL=en        # English messages (default: Turkish)
baton --help
```

The `ln` step is needed because Claude Code does not put a plugin's `bin/` on `PATH`. If `~/.local/bin` is not on your `PATH`, add it.

Then allow Gemini to write inside your project, once per project (it backs up agy's `settings.json` first):

```bash
cd your-project
baton perms check --write "$PWD" --add-perms
```

Without this rule the subagent stops with `İZİN GEREKLİ` (permission needed) and tells you the exact rule to add; it never grants permissions on its own. Restart Claude Code, then ask:

```text
/baton:devret Add input validation to src/parser.py so empty strings raise ValueError; verify with: python3 -m pytest tests/test_parser.py
```

Claude hands the task to the `baton:ajan-yonetici` subagent. The subagent writes a task file, starts Gemini, waits, runs the test command itself and returns one of `BAŞARILI` (passed), `BAŞARISIZ` (failed) or `İZİN GEREKLİ` (permission needed), together with the changed files and the test output.

## Usage

### From Claude Code

| What you do | What happens |
|---|---|
| `/baton:devret <task>` | The subagent runs the full loop and returns a short, evidence-backed result. |
| Ask Claude to "give this to Gemini" | The `ajan` skill triggers and Claude drives the loop itself. |
| Ask for several independent tasks | Claude starts them in parallel. The skill tells Claude not to run tasks that touch the same files at the same time. |

### From the terminal

```bash
# 1. Start a task in the background (Gemini may write only to ./src)
baton baslat parser-fix -m "Make parse() raise ValueError on empty input" --yaz ./src

# 2. Wait until it finishes
baton bekle parser-fix

# 3. Read the compact report: summary, changed files, open issues
baton rapor parser-fix

# 4a. Tests failed? Continue in the same conversation
baton devam parser-fix -m "tests/test_parser.py::test_empty still fails with KeyError. Fix the root cause, do not relax tests." --bekle

# 4b. Or let baton run the test → fix loop
baton dogrula parser-fix --test "python3 -m pytest tests/test_parser.py" --tur 2
```

`baton durum` lists all tasks (example output with `AJAN_DIL=en`):

```text
TAG         MODEL     STATUS  VERIFY  ROUND  DURATION  LAST STEP       FILES  TOKENS
parser-fix  neon      bitti   -       1      84.2s     agent_response  1      243461
```

For longer tasks, put the context in Markdown files and pass them with `-g` (`-g A -g B` and `-g A B` both accept multiple files; see [examples/GOREV_ORNEK.md](examples/GOREV_ORNEK.md)).

## Command reference

Subcommands are Turkish. The English meaning is in the second column.

| Command | Meaning | Key options |
|---|---|---|
| `baslat <tag>` | start | `-g FILE...` or `-m TEXT`, `--model`, `--orkestra` (`--orchestrate`), `--effort`, `--yaz DIR`, `--oku DIR`, `--komut PREFIX`, `--sure 30m`, `--sandbox`, `--izin-ekle`, `--bekle` |
| `bekle [<tag>...]` | wait | `--zaman-asimi SECONDS` |
| `durum [<tag>]` | status | `--json` |
| `rapor <tag>` | report | `--ham` (raw response) |
| `devam <tag>` | continue | `-m TEXT` (required), `--bekle` |
| `dogrula <tag>` | verify loop | `--test CMD`, `--tur N` (at most N fix rounds, default 3), `--cwd DIR`, `--zaman-asimi SECONDS` |
| `izle <tag>` | follow the live event stream | |
| `iptal <tag>` | cancel running task (SIGTERM, then SIGKILL after 5 s; exit 1 if not running) | |
| `temizle` | delete old tasks | `--gun DAYS` (default 7) |
| `izin kontrol` | check permissions only | `--yaz`, `--komut`, `--izin-ekle` |
| `modeller` (`models`) | list available models and aliases | `--yenile` (`--refresh`), `--json` |

Task tags (`<tag>`) may only contain `[A-Za-z0-9._-]` and must be 1–64 characters long.

Model aliases are derived dynamically from the `agy models` catalog (`<family>`, `<family>-high`, `<family>-orta`, `<family>-low`, plus any full model ID). The default model is selected automatically from the first available family on your account in preference order (`neon` → `hydrogen` → `argon` → `flash`), and can be overridden with `AJAN_MODEL` or `--model`. Run `baton modeller` to inspect available families and aliases. The catalog is cached for 24 hours; when a new Gemini family appears on refresh, a single-line notice is printed to stderr. If orchestrator models exist in the catalog, `orkestra` / `orchestrator` (preferring the `neon` orchestrator, otherwise the first listed) and `orkestra-<suffix>` / `orchestrator-<suffix>` aliases (e.g. `orkestra-g1-pro`, `orkestra-argon`) are also derived; they are never chosen automatically as the default. `--orkestra` (`--orchestrate`) is shorthand for `--model orkestra` and cannot be combined with `--model`.

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `AJAN_DIL` | `tr` | `--help`, message and prompt language: `tr` or `en` |
| `AJAN_AGY` | `agy` | Path to the `agy` binary |
| `AJAN_DIZIN` | `$XDG_STATE_HOME/ajan` or `~/.local/state/ajan` | Task state directory |
| `AJAN_AYAR` | `~/.gemini/antigravity-cli/settings.json` | agy permissions file |
| `AJAN_MODEL` | automatic | Default model alias or full model ID (overridden by `--model`) |

## Permissions

`agy` reads its allow-list from `settings.json`:

```json
{ "permissions": { "allow": ["write_file(/abs/path/to/project/src)", "command(python3 -m pytest)"] } }
```

`baton baslat` checks that every `--yaz` directory and `--komut` prefix is covered. If one is missing, it exits with code 2 and prints the rules to add. `--izin-ekle` adds them after taking a timestamped backup. If `settings.json` is not valid JSON, the file is left untouched and the command fails.

## Keeping token use down

- Every `devam` round re-reads the whole Gemini conversation, so a second round often costs more than the first. Keep `dogrula --tur` low, and when a conversation gets long, start a fresh task with a written diagnosis.
- Use `--model flash-orta` for mechanical tasks. It spends fewer thinking tokens.
- On the Claude side, prefer `rapor` over `izle` or `rapor --ham`.
- Note that `agy` loads your globally enabled MCP servers and its full tool set into every task.
- Reserve `--orkestra` for large, multi-part tasks; orchestrator models may consume more quota (not measured).

## Limitations

- Requires a local, signed-in `agy`. Tasks run on the same machine; there is no remote worker support.
- Subcommands, the skill and the subagent prompts are written in Turkish (English aliases such as `start`, `wait`, `report` also work). Setting `AJAN_DIL=en` translates `--help`, status messages and task prompts; `agy` output and task contents stay as they are.
- The token count shown by `durum` covers input and output; cache reads are not shown.
- Not affiliated with Anthropic or Google.

## Development

```bash
git clone https://github.com/HSGunes/gemini-baton-for-claude-code.git
cd gemini-baton-for-claude-code
python3 -m pytest                    # fake agy; never calls the real CLI
claude plugin validate --strict .
ln -sfn "$PWD/bin/baton" ~/.local/bin/baton   # use your clone directly
```

Without the plugin, `python3 ajan.py --help` works with no install, and `pip install .` registers the `baton` and `ajan` commands.

The social preview image (uploaded in GitHub repository settings, not used in the README) is regenerated with `python3 scripts/make_social_preview.py` (requires Pillow); for the demo, run `python3 scripts/make_demo_svg.py assets/demo.txt assets/demo.svg`.

Issues and pull requests are welcome. Please include a test for behaviour changes. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
