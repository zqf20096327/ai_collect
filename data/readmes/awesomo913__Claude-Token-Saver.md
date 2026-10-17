# Claude Token Saver

[![tests](https://github.com/awesomo913/Claude-Token-Saver/actions/workflows/tests.yml/badge.svg)](https://github.com/awesomo913/Claude-Token-Saver/actions/workflows/tests.yml)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![platforms](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Stop paying Claude to read whole files.** Find the function you need in plain
words and hand Claude only that.

```
$ token-saver search ./requests "get environ proxies"
src/requests/utils.py:873  get_environ_proxies (function, ~69 tokens, score 115)
tests/test_utils.py:220  TestGetEnvironProxies (class, ~556 tokens, score 77)
src/requests/cookies.py:211  get (method, ~127 tokens, score 69)
```

That function is **69 tokens**. The file it lives in, `utils.py`, is
**8,618 tokens** (1,155 lines). If Claude opens the file to find it, you pay
for all of them.

## TL;DR

- `pipx install git+https://github.com/awesomo913/Claude-Token-Saver.git`
- `token-saver search . "what you need" --source` returns just the matching
  functions/classes, with token counts, ready to paste into Claude.
- Runs locally on Windows, macOS and Linux. Python, JavaScript and TypeScript.
- Benchmarked on requests, flask and rich; every number is reproducible with
  one command ([results](benchmarks/RESULTS.md)).

## Why

Claude Code often reads an entire file to use one function in it. On a big
project that burns through your usage limits and fills the context window with
code that has nothing to do with your task.

Token Saver indexes every function and class in your project, on your machine,
and lets you (or Claude itself) pull out exactly the block you need.

## Features

- **Search in plain words.** `"load config"` finds `load_config`, `loadConfig`
  and `LoadConfig`. Handles Python and JavaScript/TypeScript.
- **Paste-ready output.** `--source` prints each hit as a code block.
- **Project context for Claude Code.** `bootstrap` writes a short `CLAUDE.md`
  overview and memory files that Claude Code loads at session start.
- **Never overwrites your notes.** Generated text lives between markers in
  `CLAUDE.md` and `MEMORY.md`; everything you or Claude Code wrote is kept.
- **Cheap to refresh.** `prep` does nothing when no source file changed, so it
  is safe to run at the start of every session.
- **Local only.** Your code never leaves your machine.
- **One dependency** (`tiktoken`, for accurate token counts). Windows, macOS
  and Linux, Python 3.10+.

## Quick start

Install it as an isolated command-line tool with [pipx](https://pipx.pypa.io/)
or [uv](https://docs.astral.sh/uv/):

```bash
pipx install git+https://github.com/awesomo913/Claude-Token-Saver.git
# or
uv tool install git+https://github.com/awesomo913/Claude-Token-Saver.git
```

Then:

```bash
token-saver search path/to/project "parse header links" --source   # find code
token-saver bootstrap path/to/project                              # write CLAUDE.md + memory
token-saver prep path/to/project                                   # refresh if anything changed
token-saver clean path/to/project --yes                            # remove everything it wrote
```

`search` exits with code 1 when nothing matches, so it works in scripts.

## Let Claude Code use it for you

**1. Tell Claude to search before it opens files.** Add this to your
project's `CLAUDE.md`:

```markdown
When you need a function or class and don't know which file it is in, run
`token-saver search . "<what you need>" --source` and read that output
instead of opening whole files.
```

**2. Keep the project overview fresh.** Add a SessionStart hook to
`~/.claude/settings.json` (it only does work when files changed):

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          { "type": "command", "command": "token-saver prep \"${CLAUDE_PROJECT_DIR:-.}\" --quiet || true" }
        ]
      }
    ]
  }
}
```

## Benchmarks

Numbers you can check. `python benchmarks/run.py` fetches three popular
open-source projects at pinned commits, asks 100 search questions per row, and
writes every single query and result to [`benchmarks/results/`](benchmarks/results/).

- **name**: search by the function name with spaces (`"get environ proxies"`).
  The easy case.
- **name + 1 typo**: the same with two letters swapped.
- **docstring**: search by the first line of the function's description, e.g.
  `"Returns encodings from given HTTP Header Dict."`. Closest to how people ask.

"Tokens saved" compares the top 3 results with reading the whole file.

<!-- RESULTS:START -->
| Project | Mode | Right block 1st | Right block in top 3 | Tokens saved (median / mean) |
|---|---|---|---|---|
| requests `611c616` | name | 85% | 97% | 95% / 70% |
| requests `611c616` | name + 1 typo | 45% | 64% | 96% / 69% |
| requests `611c616` | docstring | 46% | 70% | 80% / -12% |
| flask `d73fa1c` | name | 64% | 81% | 89% / 57% |
| flask `d73fa1c` | name + 1 typo | 25% | 46% | 89% / 34% |
| flask `d73fa1c` | docstring | 35% | 63% | 73% / -15% |
| rich `9d8f9a3` | name | 71% | 86% | 87% / 34% |
| rich `9d8f9a3` | name + 1 typo | 20% | 47% | 89% / 42% |
| rich `9d8f9a3` | docstring | 36% | 66% | 50% / -28% |

Source: [benchmarks/RESULTS.md](benchmarks/RESULTS.md)
<!-- RESULTS:END -->

**Read these honestly:**

- **Search by name works well** (right block in the top 3 for 81–97% of
  queries). Before the ranking fix in v5.0.0 it put the right block first only
  19–38% of the time.
- **Plain-English and typo search are the weak spots.** Improving them is the
  top item on the roadmap.
- **Small files are a bad deal.** Three snippets can cost more than a short
  file, which is why the average savings is far below the typical (median)
  savings and even negative in docstring mode.
- Token counts use `tiktoken`'s `cl100k_base`. Claude's own tokenizer differs
  a little, so treat them as close estimates.

## What `bootstrap` writes

| Where | What |
|---|---|
| `CLAUDE.md` | A project overview between `<!-- claude-backend:generated -->` markers. Your text outside the markers is kept. |
| `.claude/memory/` and `~/.claude/projects/<project>/memory/` | Architecture, patterns, utilities and conventions notes. In `MEMORY.md` only the Token Saver section is managed; Claude Code's own entries are left alone. |
| `.claude/snippets/` | One file per reusable block, plus an index. Consider adding it to `.gitignore`. |

`clean` removes only these, and leaves your own files in those folders alone.

## FAQ

**Does my code get sent anywhere?** No. Scanning and search run locally. The
only network access is `tiktoken` downloading its vocabulary file once, the
first time it counts tokens.

**Which languages?** Python and JavaScript/TypeScript functions and classes.

**Is this an official Anthropic tool?** No. It is an independent open-source
project.

**How is this different from grep?** grep finds lines; Token Saver returns the
whole function or class, ranked by how well its name, docstring and path match
your words, with a token count so you know what it will cost.

## Windows desktop app (optional)

The original desktop app (tray icon, floating overlay, global hotkey, snippet
queue) is still included and is Windows-only:

```bash
pip install -r requirements.txt
python launch_token_saver.py      # full window
python launch_tray.py             # tray only
python build_exe.py               # standalone .exe via PyInstaller
```

## Roadmap

- Cache the index between `search` calls (today each search re-scans the project).
- Better plain-English search and typo tolerance.
- Hand back fewer, smaller snippets when the file itself is already small.

Ideas and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Develop

```bash
pip install -e ".[dev]"
pytest
python benchmarks/run.py   # re-check the benchmark after changing search
```

## License

[MIT](LICENSE)
