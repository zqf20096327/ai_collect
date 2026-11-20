# Lossless Handoff

**Claude Code hooks that make compaction safe: a handoff before every compaction, a decisions list per project, and exact-words search over every earlier chat.**

*Formerly claude-handoff.*

This documentation uses ASD-STE100 Simplified Technical English.

Current versions: product 0.14.0 (`install.sh`), hooks 1.16.0 (`HOOK_VERSION` in `hooks/precompact-handoff.py` and `hooks/postcompact-inject.py`).

[![CI](https://github.com/pratikgh0se/lossless-handoff/actions/workflows/ci.yml/badge.svg)](https://github.com/pratikgh0se/lossless-handoff/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/pratikgh0se/lossless-handoff)](https://github.com/pratikgh0se/lossless-handoff/releases/latest)

## The problem and the fix

Every compaction turns a long Claude Code session into a generic summary. The exact next step, the dead ends, your standing rules and your exact wording are gone. The model does the work again or asks again.

Before each compaction, the hooks write a structured handoff and feed it back in. Each project keeps a decisions list that survives compactions. `recall` finds the exact words of earlier chats (keyword search, plus optional local meaning search). Python 3 standard library only.

![How a handoff flows through a compaction](docs/handoff-timeline.svg)

## Quick start

```bash
git clone https://github.com/pratikgh0se/lossless-handoff.git
cd lossless-handoff
./install.sh --dry-run   # show the plan, change nothing
./install.sh
```

You need `python3` and `bash` on macOS or Linux, and Claude Code. Windows is not supported. Then restart open Claude Code sessions. Hooks load when a session starts. The default install is small. It installs the core only. Each option below is opt-in:

| Flag | What it adds |
|---|---|
| `--window N` | Sets `CLAUDE_CODE_AUTO_COMPACT_WINDOW` to N tokens (for example 400000), only when no value is set. |
| `--nightly` | Two nightly jobs: the index (03:30) and the reconcile-and-prove run (04:15). They are macOS LaunchAgents. On Linux the installer prints the cron lines. |
| `--semantic` | Meaning search on your machine only. If `ollama` is on your PATH, the installer offers `ollama pull bge-m3` (`--yes` pulls without a question). |
| `--save-defaults` | Saves the opt-in flags of that run to `~/.config/lossless-handoff/install-defaults`. Every later `./install.sh` run applies them. |

Run `./install.sh --window 400000 --nightly --semantic` to get everything. All flags, the saved defaults file and the upgrade from 0.12.x are in [docs/install.md](docs/install.md). `llm_map` (label each item of a big list with a small model) is now a separate project: [pratikgh0se/llm-map](https://github.com/pratikgh0se/llm-map). See [docs/llm-map.md](docs/llm-map.md).

**Verify.**

```
claude -p --model haiku "say hi" --output-format json   # <session_id> is in the JSON output
claude -p --model haiku --resume <session_id> "/compact"
tail -n 3 ~/.local/state/claude-handoffs/health.jsonl
```

These commands make real model calls and use a small part of your quota. A new line with `"trigger": "manual"` means that the PreCompact hook fired. You can also run `bash tests/smoke.sh`. It uses a temporary HOME and does not touch your real settings.

To check the install without a model call, run `python3 ~/.claude/hooks/postcompact-inject.py --check`. It prints nothing when all is well, or one `HANDOFF CHECK:` line for each problem found. On a new install it can print one line about `cleanupPeriodDays`. `./install.sh --keep-transcripts` sets the value.

**Uninstall.** Run `./uninstall.sh`. Add `--purge` to also delete the saved install defaults. Handoff files, indexes and decisions lists stay. See [docs/install.md](docs/install.md#uninstall).

**Use it.** Work as usual. After a compaction, ask "what exactly did I say about X?". Claude runs recall and quotes you. Try it yourself, from a project folder: `python3 ~/.claude/hooks/recall.py user --last 5`. It prints nothing in a folder with no earlier chats.

## How it works

![Parts, events and files](docs/architecture.svg)

- **Nudge** (`handoff-nudge.py`, PostToolUse). At 75% of the auto-compact window, and again every 25,000 tokens, the hook asks the model to write its own handoff.
- **Handoff** (`precompact-handoff.py`, PreCompact). Just before compaction, the hook writes `<session_id>-latest.md` (14,000 characters at most). It holds the model handoff, a fresh Sonnet summary (it uses your `claude -p` quota) and facts that the hook extracts with no model.
- **Inject** (`postcompact-inject.py`, SessionStart with matcher `compact`). After compaction, the hook feeds the handoff and the decisions list back into the new context.
- **Decisions list.** One plain-text list for each project. It holds what you decided or approved, and why. It survives all compactions. See [docs/decisions-list.md](docs/decisions-list.md).
- **Recall.** `recall.py` finds the exact words of earlier chats with word search and meaning search merged. See [docs/recall.md](docs/recall.md).
- **No silent misses.** A hook cannot force Claude Code to run it. So the hooks write a handoff early, rebuild it after the fact if it is still missing, and, with `--nightly`, count the misses every night. See [docs/hooks-in-detail.md](docs/hooks-in-detail.md#when-a-compaction-is-missed).
- **Subagents** get their own handoff and, at start, the rules of the project.
- **The hook always exits 0** and never blocks compaction. If anything fails, it still writes a minimal handoff.

The parts, the events and the files are in [docs/architecture.md](docs/architecture.md).

## Evidence

- **One OOLONG run is published** ([bench/oolong/evidence/run-20261118T221353-summary.md](bench/oolong/evidence/run-20261118T221353-summary.md)). The harness flagged it for shared-temp use (2.2% of units); on every cleaned task set, Lossless Handoff with llm_map tied plain Claude Code. In that run the main session never compacted, so it does not test the handoff. No scored benchmark result for the handoff's main claim is published yet. Two benchmarks are in this repository: [bench/continuity/README.md](bench/continuity/README.md) and [bench/oolong/README.md](bench/oolong/README.md). Both are code-graded. The full evaluation is not finished, and no part of it is published yet. The pilot files in `bench/oolong/evidence/` are from a 2-task pilot. They show that the test harness works. They are not a result.
- **Live mechanism checks.** The hooks check themselves on the author's machine: is a handoff there, does it reach the model, does recall return old messages word for word. These checks show that the mechanism works. They do not show that answers get better. Some of these checks currently fail. [docs/evidence.md](docs/evidence.md) lists each check, its number and the reason for each failure.
- **One-off measurements.** The author ran a blind quiz (2026-11-14) and a cost estimate (2026-10-20). Models wrote and graded the quiz. Both come from one user and one machine. Read them as hints. The numbers are in [docs/evidence.md](docs/evidence.md).
- The details, the limits of each test and the other reliability notes are in [docs/evidence.md](docs/evidence.md) and [docs/handoff-reliability.md](docs/handoff-reliability.md).

## Limitations

- **One heavy user so far.** All numbers come from the author's machine. Nobody has tested whether it helps other workflows.
- **Handoffs can be cut.** 20% of handoffs (43 of 217) hit the 14,000-character size cap and were truncated.
- **Misses still happen.** 4 of 192 main compactions in the 30-day reconcile had no handoff. The hooks make misses fewer and show them. They do not promise zero.
- **Redaction is pattern-based.** A secret in a shape that the hooks do not know is not masked.
- **Platform.** The nightly jobs (opt-in) are macOS LaunchAgents. On Linux you add the printed cron lines yourself. Windows is not supported.
- **AI-graded evals.** Models wrote and graded the quizzes, on one user's projects. The 19% cost estimate is a single 4.7-day, one-user figure, not a bill.
- The nudge works only if the model obeys it. No hook forces the model to run a recall search.

The full list is in [docs/limitations.md](docs/limitations.md).

## Security and privacy

- The hooks mask known secret shapes as `[REDACTED:<kind>]` before they write handoff files, the decisions list and recall output. The transcripts of Claude Code are not changed.
- The scripts open no connection to a remote host. Word search stays on your machine.
- Meaning search sends message text to the embedding server that you configure (by default Ollama on your own machine). The two per-compaction calls run your local `claude -p`. These calls send conversation text to Anthropic through Claude Code, as usual.

Read [SECURITY.md](SECURITY.md) for the details.

## More

- Docs index: [docs/README.md](docs/README.md). Architecture: [docs/architecture.md](docs/architecture.md). FAQ: [docs/faq.md](docs/faq.md).
- Changes: [CHANGELOG.md](CHANGELOG.md).
- Tests and contributing: [docs/testing.md](docs/testing.md) (the acceptance tests are in [lossless-handoff-tests](https://github.com/pratikgh0se/lossless-handoff-tests)).
- Built on the paper "LCM: Lossless Context Management" by Clint Ehrlich and Theodore Blackman ([arXiv:2605.04050](https://arxiv.org/abs/2605.04050)). This is an independent project. See [docs/background.md](docs/background.md).

MIT license, copyright Pratik Ghose. See [LICENSE](LICENSE).
