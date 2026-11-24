# Lossless Handoff

**Claude Code hooks that make compaction safe: a handoff before every compaction, a decisions list per project, and exact-words search over every earlier chat.**

*Formerly claude-handoff.*

This documentation uses ASD-STE100 Simplified Technical English.

Current versions: product 0.19.0 (`install.sh`), hooks 1.21.0 (`HOOK_VERSION` in `hooks/precompact-handoff.py`, `hooks/postcompact-inject.py`, `hooks/auto-recall.py`, `hooks/recall-mcp.py`, `hooks/reanchor.py`, `hooks/claim-guard.py`, `hooks/history-guard.py` and `hooks/action-guard.py`).

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

You need `python3` and `bash` on macOS or Linux, and Claude Code. Windows is not supported. Then restart open Claude Code sessions. Hooks load when a session starts. The default install is small. It installs the core and the recall rule line (on by default since 0.19.0). Each other option below is opt-in. To turn the recall rule off, run `./install.sh --no-recall-rules --save-defaults`, or set `HANDOFF_RECALL_RULES=0`:

| Flag | What it adds |
|---|---|
| `--window N` | Sets `CLAUDE_CODE_AUTO_COMPACT_WINDOW` to N tokens (for example 400000), only when no value is set. |
| `--nightly` | Two nightly jobs: the index (03:30) and the reconcile-and-prove run (04:15). They are macOS LaunchAgents. On Linux the installer prints the cron lines. |
| `--semantic` | Meaning search on your machine only. If `ollama` is on your PATH, the installer offers `ollama pull bge-m3` (`--yes` pulls without a question). |
| `--auto-recall` | A `UserPromptSubmit` hook. When your prompt refers to the past ("what did we decide earlier"), it searches the earlier chats of the project and adds the top 3 exact quotes to the context. It runs for at most 2 seconds. |
| `--recall-rules` | On by default (0.19.0), so this flag changes nothing. The line goes after the recall line in every session start and subagent start: search before you state an earlier number, path, name, command or decision, also when a file no longer holds it. It does not force a search. `--no-recall-rules` skips it; add `--save-defaults` to remove it. |
| `--recall-mcp` | Installs a local MCP server with the tools `search_earlier_chat` and `open_message` and registers it with `claude mcp add --scope user`. It does not force a search. |
| `--reanchor` | A `PostToolUse` hook. Each time the context grows by 50,000 tokens, it repeats the active rules of the project near the end of the context. It prints nothing when there is no rule. |
| `--claim-guard` | A `Stop` hook. When a reply states an earlier fact ("as we decided", "you said") and the turn has no recall search, it writes one log line. It does not change the reply, unless you set `HANDOFF_CLAIM_GUARD=block`. |
| `--history-guard` | A `Stop` hook (F77). When the context is 100,000 tokens or more and a reply uses a key that changed in this chat, it writes one log line. With `HANDOFF_HISTORY_GUARD=block` it gives the model the full history of that key once per turn. |
| `--action-guard` | A `PostToolBatch` hook (F80). It checks Edit, Write, MultiEdit, NotebookEdit and Bash calls for a key that changed in this chat. It writes one log line, or with `HANDOFF_ACTION_GUARD=inject` it adds the history before the next step. It never blocks a call. |
| `--recall-size-trigger` | Needs `--auto-recall` (F78). Auto-recall also fires with no cue phrase when the context is 100,000 tokens or more and the prompt names a key that changed in this chat. `HANDOFF_AUTO_RECALL_SIZE=0` switches it off. |
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
- **Re-anchor** (opt-in, `--reanchor`) and **claim guard** (opt-in, `--claim-guard`, shadow mode by default). See [docs/recall.md](docs/recall.md#re-anchor-and-claim-guard).
- **Auto-recall** (opt-in, `--auto-recall`). When your prompt refers to the past, a hook runs the recall search for the model and adds the top 3 exact quotes. See [docs/recall.md](docs/recall.md#auto-recall).
- **History guard, action guard and size trigger** (0.18.0, opt-in: `--history-guard`, `--action-guard`, `--recall-size-trigger`). In a long chat they show the full history of a key that changed before the model uses it, in a reply or in a tool call. See [docs/recall.md](docs/recall.md#history-guard-action-guard-and-size-trigger).
- **Key history** (0.17.0). `recall.py history <identifier>` and the MCP tool `key_history` list every mention of one key, oldest first. Auto-recall uses it when the prompt names an identifier. See [docs/recall.md](docs/recall.md#key-history).
- **Strict recall rule and recall tool** (the rule is on by default since 0.19.0; the tool is opt-in, `--recall-mcp`). One rule line tells the model to search before it states an earlier fact. An MCP tool lets the model search in one call. Neither forces a search. See [docs/recall.md](docs/recall.md#strict-recall-rule-and-the-recall-tool).
- **Subagents** get their own handoff and, at start, the rules of the project.
- **The hook always exits 0** and never blocks compaction. If anything fails, it still writes a minimal handoff.

The parts, the events and the files are in [docs/architecture.md](docs/architecture.md).

## Evidence

- **One OOLONG run is published** ([bench/oolong/evidence/run-20261118T221353-summary.md](bench/oolong/evidence/run-20261118T221353-summary.md)). The harness flagged it for shared-temp use (2.2% of units); on every cleaned task set, Lossless Handoff with llm_map tied plain Claude Code. In that run the main session never compacted, so it does not test the handoff. One small continuity test (the proof test, 4 seeds) is published: see Benchmarks below. Two benchmarks are in this repository: [bench/continuity/README.md](bench/continuity/README.md) and [bench/oolong/README.md](bench/oolong/README.md). Both are code-graded. The full evaluation is not finished, and no part of it is published yet. The small proof test is the only continuity result. The pilot files in `bench/oolong/evidence/` are from a 2-task pilot. They show that the test harness works. They are not a result.
- **Live mechanism checks.** The hooks check themselves on the author's machine: is a handoff there, does it reach the model, does recall return old messages word for word. These checks show that the mechanism works. They do not show that answers get better. The live mechanism checks currently include failures: some of these checks fail. [docs/evidence.md](docs/evidence.md) lists each check, its number and the reason for each failure.
- **One-off measurements.** The author ran a blind quiz (2026-11-14) and a cost estimate (2026-10-20). Models wrote and graded the quiz. Both come from one user and one machine. Read them as hints. The numbers are in [docs/evidence.md](docs/evidence.md).
- The details, the limits of each test and the other reliability notes are in [docs/evidence.md](docs/evidence.md) and [docs/handoff-reliability.md](docs/handoff-reliability.md).

## Benchmarks

The proof test is a small benchmark with 4 seeds. It ran on 2026-11-23 with Sonnet, a 400k context window and Claude Code 2.1.326. The seeds were new (2001 to 2004). The cost was $149.50. The pass rule was written before the run, and the run passed it.

| Arm | 1 compaction | 3 compactions | 10 compactions |
|---|---|---|---|
| Plain Claude Code (A) | 100% | 80% | 58% |
| Lossless Handoff (B) | 100% | 100% | 100% |

At 10 compactions, B is 42 points above A. The 95% interval is +27 to +51 points, over 4 seeds.

- Controls: the oracle (no compaction) scored 100%, the amnesia control (no history) scored 0%, and the fresh control scored 100%.
- At 10 compactions, A was wrong and B was right on 42 items. There were 0 items where B was wrong and A was right.

Two examples from the report (seed 2001, 10 compactions):

- The exact deploy command for `mirror-3481`. Expected: `rk-ship --lane 5912 --tag JBENXM`. A answered `UNKNOWN`. B gave the exact command, after a search.
- The order of three decisions made at different times. Expected: `NSKK-7211-TXNE, L3N9-0550-F4DU, 3K49-3054-TNDJ`. A gave an empty list. B gave the correct order, with no search.

Limits:

- It is a small benchmark: 4 seeds.
- It is our own synthetic benchmark. Code grades it, but we wrote it.
- It used Sonnet only, at most 10 compactions, and one Claude Code version.
- On questions without a hint (neutral wording, types R D X S E), B scored 95% (76/80). Claude sometimes checks the current files and does not search.
- A pilot with 2 seeds ran first. It found a benchmark bug: the deny rules blocked the recall command (fixed in PR #51 and PR #52). The proof test uses only new seeds.

The full suite is future work: 20 seeds, 30 compactions, Opus, and a published benchmark.

The full report is in [docs/proof/benchmarks/2026-11-23-proof-test.md](docs/proof/benchmarks/2026-11-23-proof-test.md). To run the test again, use `bench/continuity/run.sh proof`. Add `--dry-run` to only print the estimate. The numbers are listed in the evidence register ([docs/evidence.md](docs/evidence.md)).

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
