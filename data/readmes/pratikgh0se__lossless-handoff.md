# Lossless Handoff

**Claude Code hooks that aim to make compaction safe: a handoff before every compaction, a decisions list per project, and exact-words search over every earlier chat.**

*Formerly claude-handoff.*

This documentation uses ASD-STE100 Simplified Technical English.

Current versions: product 0.23.0 (`install.sh`), hooks 1.25.0 (`HOOK_VERSION` in `hooks/precompact-handoff.py`, `hooks/postcompact-inject.py`, `hooks/auto-recall.py`, `hooks/recall-mcp.py`, `hooks/reanchor.py`, `hooks/claim-guard.py`, `hooks/history-guard.py` and `hooks/action-guard.py`).

![fair test, 6 seeds, no hint: 100% vs 73%](https://img.shields.io/badge/no%20hint-100%25%20vs%2073%25%20(6%20seeds)-8197a0) ![fair test, 6 seeds, with a hint: no gain](https://img.shields.io/badge/hint-no%20gain-8197a0)

With no hint in the question, Lossless Handoff kept 100% and plain Claude Code 73% (6 seeds, secondary result). With a hint, or when told to search, both score about 100%.

Note on the badges: this is the fair test (2026-11-28, 6 new seeds 4001 to 4006): Sonnet, 400k window, 10 compactions. Plain Claude Code was allowed to search its own chat files. With a hint, plain Claude Code scored 145 of 150 (97%) and Lossless Handoff 150 of 150. The gain is +3.3 points, and the registered rule needs +15 points. We claim no gain with a hint. With no hint, plain Claude Code scored 88 of 120 (73%) and Lossless Handoff 120 of 120 (100%). The registered verdict is INVALID, and secondary results never change it. The earlier numbers (82% vs 100%, and 58% vs 100% with a blocked baseline) overstate the gap with a hint.

[![CI](https://github.com/pratikgh0se/lossless-handoff/actions/workflows/ci.yml/badge.svg)](https://github.com/pratikgh0se/lossless-handoff/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/pratikgh0se/lossless-handoff)](https://github.com/pratikgh0se/lossless-handoff/releases/latest)

## The problem and the fix

Every compaction turns a long Claude Code session into a generic summary. The exact next step, the dead ends, your standing rules and your exact wording are gone. The model does the work again or asks again.

Before each compaction, the hooks write a structured handoff and feed it back in. Each project keeps a decisions list that survives compactions. `recall` finds the exact words of earlier chats (keyword search, plus optional local meaning search). Python 3 standard library only.

![How a handoff flows through a compaction](docs/handoff-timeline.svg)

## Why this exists

![Plain compaction against Lossless Handoff](docs/img/flow.svg)

A compaction replaces the chat with a short summary. Exact commands, error codes and replaced decisions can be gone. Lossless Handoff aims to make compaction safe: to lose nothing important, and to let Claude get the exact old text back.

<details><summary>The four parts</summary>

1. **Handoff.** A hook writes it before each compaction: the goal, the decisions, the dead ends and the next step.
2. **Decisions list.** Your standing rules and decisions come back after every compaction. Your latest words win.
3. **Recall.** Word-for-word search over every earlier chat of the project.
4. **Recall rule.** One line in the new context: if the context does not clearly show a value, run the recall command and copy it exactly. A failed command is not "not found".

The details are in [How it works](#how-it-works) below.

</details>

## Quick start

```bash
git clone https://github.com/pratikgh0se/lossless-handoff.git
cd lossless-handoff
./install.sh --dry-run   # show the plan, change nothing
./install.sh
```

You need `python3` and `bash` on macOS or Linux, and Claude Code. Windows is not supported. Then restart open Claude Code sessions. Hooks load when a session starts. The default install is small. It installs the core and the recall rule line (on by default since 0.19.0). Each other option below is opt-in. To turn the recall rule off, run `./install.sh --no-recall-rules --save-defaults`, or set `HANDOFF_RECALL_RULES=0`:

<details><summary>All install flags</summary>

| Flag | What it adds |
|---|---|
| `--window N` | Sets `CLAUDE_CODE_AUTO_COMPACT_WINDOW` to N tokens (for example 400000), only when no value is set. |
| `--nightly` | Two nightly jobs: the index (03:30) and the reconcile-and-prove run (04:15). They are macOS LaunchAgents. On Linux the installer prints the cron lines. |
| `--semantic` | Meaning search on your machine only. If `ollama` is on your PATH, the installer offers `ollama pull bge-m3` (`--yes` pulls without a question). |
| `--auto-recall` | A `UserPromptSubmit` hook. When your prompt refers to the past ("what did we decide earlier"), it searches the earlier chats of the project and adds the top 3 exact quotes to the context. It runs for at most 2 seconds. |
| `--recall-rules` | On by default (0.19.0), so this flag changes nothing. The line goes after the recall line in every session start and subagent start: if your context does not clearly show an earlier number, path, name, command or decision, run the recall command above before you answer (full path, no `cd`). A failed or denied command is not "not found". It does not force a search. `--no-recall-rules` skips it; add `--save-defaults` to remove it. |
| `--recall-mcp` | Installs a local MCP server with the tools `search_earlier_chat` and `open_message` and registers it with `claude mcp add --scope user`. It does not force a search. |
| `--reanchor` | A `PostToolUse` hook. Each time the context grows by 50,000 tokens, it repeats the active rules of the project near the end of the context. It prints nothing when there is no rule. |
| `--claim-guard` | A `Stop` hook. When a reply states an earlier fact ("as we decided", "you said") and the turn has no recall search, it writes one log line. It does not change the reply, unless you set `HANDOFF_CLAIM_GUARD=block`. |
| `--history-guard` | A `Stop` hook (F77). When the context is 100,000 tokens or more and a reply uses a key that changed in this chat, it writes one log line. With `HANDOFF_HISTORY_GUARD=block` it gives the model the full history of that key once per turn. |
| `--action-guard` | A `PostToolBatch` hook (F80). It checks Edit, Write, MultiEdit, NotebookEdit and Bash calls for a key that changed in this chat. It writes one log line, or with `HANDOFF_ACTION_GUARD=inject` it adds the history before the next step. It never blocks a call. |
| `--recall-size-trigger` | Needs `--auto-recall` (F78). Auto-recall also fires with no cue phrase when the context is 100,000 tokens or more and the prompt names a key that changed in this chat. `HANDOFF_AUTO_RECALL_SIZE=0` switches it off. |
| `--save-defaults` | Saves the opt-in flags of that run to `~/.config/lossless-handoff/install-defaults`. Every later `./install.sh` run applies them. |

</details>

Run `./install.sh --window 400000 --nightly --semantic` to get everything. All flags, the saved defaults file and the upgrade from 0.12.x are in [docs/install.md](docs/install.md). `llm_map` (label each item of a big list with a small model) is now a separate project: [pratikgh0se/llm-map](https://github.com/pratikgh0se/llm-map). See [docs/llm-map.md](docs/llm-map.md).

**Verify.**

```
claude -p --model haiku "say hi" --output-format json   # <session_id> is in the JSON output
claude -p --model haiku --resume <session_id> "/compact"
tail -n 3 ~/.local/state/claude-handoffs/health.jsonl
```

These commands make real model calls and use a small part of your quota. A new line with `"trigger": "manual"` means that the PreCompact hook fired. You can also run `bash tests/smoke.sh`. It uses a temporary HOME and does not touch your real settings.

To check the install without a model call, run `python3 ~/.claude/hooks/postcompact-inject.py --check`. It prints nothing when all is well, or one `HANDOFF CHECK:` line for each problem found. On a new install it can print one line about `cleanupPeriodDays`. `./install.sh --keep-transcripts` sets the value. Since 0.23.0, `--check` also reports failed proof checks of the last 7 days. The same text goes into the `HANDOFF CHECK:` line that chats see. `--check --verbose` lists the latest failures. Details: F91 in [docs/spec.md](docs/spec.md) and [docs/hooks-in-detail.md](docs/hooks-in-detail.md).

**Uninstall.** Run `./uninstall.sh`. Add `--purge` to also delete the saved install defaults. Handoff files, indexes and decisions lists stay. See [docs/install.md](docs/install.md#uninstall).

**Use it.** Work as usual. After a compaction, ask "what exactly did I say about X?". Claude runs recall and quotes you. Try it yourself, from a project folder: `python3 ~/.claude/hooks/recall.py user --last 5`. One call also takes several patterns or ids: `recall.py search "cache" "zebra"` and `recall.py open 1a2b3c4d:57 1a2b3c4d:90` (0.20.0). It prints nothing in a folder with no earlier chats. To read decisions list entries in full, run `recall.py decisions "<words>"`, `recall.py decisions D12` or `recall.py decisions --kind rule` (0.21.0).

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
- **Live mechanism checks.** The hooks check themselves on the author's machine: is a handoff there, does it reach the model, does recall return old messages word for word. These checks show that the mechanism works. They do not show that answers get better. The live mechanism checks currently include failures: some of these checks fail. [docs/evidence.md](docs/evidence.md) lists each check, its number and the reason for each failure. Since 0.23.0, a nightly shape census (`precompact-handoff.py --shape-census`) reports new transcript shapes. A mutation gate (`tools/mutation/run.sh`) plants 20 faults. On 2026-11-26, smoke plus the code-blind tests caught 20 of 20. This shows that the tests catch these faults, not every fault.
- **One-off measurements.** The author ran a blind quiz (2026-11-14) and a cost estimate (2026-10-20). Models wrote and graded the quiz. Both come from one user and one machine. Read them as hints. The numbers are in [docs/evidence.md](docs/evidence.md).
- The details, the limits of each test and the other reliability notes are in [docs/evidence.md](docs/evidence.md) and [docs/handoff-reliability.md](docs/handoff-reliability.md).

## Benchmarks

![Accuracy after 1, 3 and 10 compactions](docs/img/accuracy.svg)

Fair test (2026-11-28): 6 new seeds (4001 to 4006), Sonnet, 400k window, 10 compactions. Plain Claude Code was allowed to search its own chat files. Both arms ran on all 6 seeds.

| Questions (6 seeds) | Plain Claude Code (can search its chat files) | Lossless Handoff |
|---|---|---|
| With a hint (registered primary) | 145 of 150 (97%) | 150 of 150 (100%) |
| No hint (registered secondary) | 88 of 120 (73%); it searched in only 8 of 30 question groups | 120 of 120 (100%) |
| Prompt tells it to search | 150 of 150 (100%) | 150 of 150 (100%) |

With a hint, the gain is +3.3 points. Lossless Handoff was ahead or equal in 6 of 6 seeds (exact sign-flip p = 0.25). The registered primary rule needs +15 points: FAIL. We claim no gain with a hint. With no hint, the gain is +26.7 points, in 6 of 6 seeds (exact sign-flip p = 1/64, 0.016). For facts that live only in the chat history (types S and E), plain Claude Code scored 29 of 48 (60%) and Lossless Handoff 48 of 48. When the prompt tells plain Claude Code to search, both score 150 of 150. So the gain is that no instruction to search is necessary.

Pooled over 8 seeds (3001, 3002 and the 6 new seeds; not confirmatory): with a hint, plain Claude Code scored 186 of 200 (93%) and Lossless Handoff 200 of 200. With no hint, plain Claude Code scored 117 of 160 (73%) and Lossless Handoff 160 of 160.

The registered verdict is INVALID. There are 2 gate failures. First, 20 shell commands on the own chat file of plain Claude Code were blocked, in 19 question groups. Each group also had successful reads, and all its answers were correct. Second, the API safety filter refused the first Lossless Handoff session of seed 4003 (a false positive on synthetic data). It was rerun, so 1 of 7 Lossless Handoff sessions counts as short. Secondary results never change the verdict. The 6-seed run cost $220 ($120.73 and $99.40, plus a $0.10 preflight). The rule was registered before the data (`bench/continuity/SPEC.md` FR.8, `bench/continuity/thresholds.json` block `fair6`).

Earlier run with a blocked baseline: 58% vs 100%. The chart and the table below show that run (4 seeds). In it, plain Claude Code could not read its own chat files. The gain was +42 points (95% interval +27 to +51). It measured 1, 3 and 10 compactions only.

| Arm | 1 compaction | 3 compactions | 10 compactions |
|---|---|---|---|
| Plain Claude Code (A) | 100% | 80% | 58% |
| Lossless Handoff (B) | 100% | 100% | 100% |

Full report: [docs/proof/benchmarks/2026-11-23-proof-test.md](docs/proof/benchmarks/2026-11-23-proof-test.md).

Limits:

- The 6-seed run has the registered verdict INVALID (2 gate failures: 20 blocked shell commands on the own chat file, and 1 of 7 Lossless Handoff sessions short after a safety-filter refusal). The no-hint result is a secondary result. It does not change the verdict.
- The earlier numbers (82% vs 100%, and 58% vs 100% with a blocked baseline) overstate the gap with a hint.
- The earlier run (58% vs 100%, 4 seeds) blocked plain Claude Code from its own chat files, so it overstates the gap. The runner denied `~/.claude/projects/**` for every arm (`deny_rules` in `bench/continuity/runner.py`). Use the fair test numbers (2026-11-28) for the gap.
- Both are small benchmarks: 4 seeds (2001 to 2004) for the blocked run, and 6 seeds (4001 to 4006) for the fair test.
- It is our own synthetic benchmark. Code grades it, but we wrote it.
- It used Sonnet only, at most 10 compactions, and one Claude Code version.

<details><summary>What the test does</summary>

The proof test is a small benchmark with 4 seeds. It plants facts with random answers early in a long scripted session. Filler turns force compactions. Then the runner asks questions and code grades the answers. It ran on 2026-11-23 with Sonnet, a 400k context window and Claude Code 2.1.326. The seeds were new (2001 to 2004). The cost was $149.50. The pass rule was written after the 2-seed pilot and before any proof data, and the run passed it. The older gain rule in the same report needs 20 seeds, and at 4 seeds it gives "small sample: no claim".

- Controls (types R D X S E C M): the oracle (no compaction) scored 100%, the amnesia control (no history) scored 0%, and the fresh control scored 100%. So the test can tell a good result from a bad one.
- On the questions with a hint, at 10 compactions, A was wrong and B was right on 42 items. There were 0 items where B was wrong and A was right. Without a hint, B scored 93% at 3 compactions and 95% at 10, and at 3 compactions there were 2 such items.
- An older test on real projects (model-graded) compared two versions of the handoff, not plain Claude Code. In both versions the score fell with more compactions (1, 2, and 3 or more). See the decisions-list row in [docs/evidence.md](docs/evidence.md#one-off-measurements).

</details>

### Which facts plain Claude Code forgets

![Items correct at 10 compactions, by kind of fact](docs/img/kinds.svg)

Plain Claude Code keeps the simple things the user said. It loses changes, order, exact strings and tool output. A long coding task needs exactly these details.

<details><summary>Numbers and two examples</summary>

Items correct at 10 compactions, 4 seeds. R, D, X, S and E count the questions with a hint and without a hint together. C, M and U have questions with a hint only. Source: the section "Added: kind of fact at 10 compactions" in [the report](docs/proof/benchmarks/2026-11-23-proof-test.md).

| Kind of fact | Where it lived | Plain (A) | Lossless Handoff (B) |
|---|---|---|---|
| Rule the user stated (R) | user message | 32/32 (100%) | 32/32 (100%) |
| Decision (D) | user message | 32/32 (100%) | 32/32 (100%) |
| Conflict, latest word wins (C) | user message | 16/16 (100%) | 16/16 (100%) |
| Decision that replaced an older one (X) | user message | 12/32 (38%) | 32/32 (100%) |
| Exact string, for example a deploy command (S) | a file read once | 4/32 (12%) | 28/32 (88%) |
| Dead end, the exact error code (E) | tool output | 4/32 (12%) | 32/32 (100%) |
| Order of three decisions (M) | user messages at different times | 0/4 (0%) | 4/4 (100%) |
| Fact that only a subagent saw (U) | subagent | 0/12 (0%) | 8/12 (67%) |

Row U is different. The main session never saw this fact, and plain Claude Code scored 0 of 12 with no compaction too. It shows what recall adds.

Two examples from the report (seed 2001, 10 compactions):

- The exact deploy command for `mirror-3481`. Expected: `rk-ship --lane 5912 --tag JBENXM`. A answered `UNKNOWN`. B gave the exact command, after a search.
- The order of three decisions made at different times. Expected: `NSKK-7211-TXNE, L3N9-0550-F4DU, 3K49-3054-TNDJ`. A gave an empty list. B gave the correct order, with no search.

</details>

### The recall rule check (small)

![Recall rule check, 2 seeds, 3 compactions](docs/img/recall-rule.svg)

A small check of fix 0.19.1 used 2 seeds and 1 and 3 compactions ($13.38). It has no verdict. The strict rule re-measure (0.19.0, $70.57) is invalid: Claude Code blocked searches. See [docs/proof/benchmarks/2026-11-24-recall-rule-check.md](docs/proof/benchmarks/2026-11-24-recall-rule-check.md).

<details><summary>Numbers</summary>

Seeds 2001 and 2002, 3 compactions, items correct. At 3 compactions, fix 0.19.1 answered 30 of 30 questions with a hint and 30 of 30 without a hint.

| Version | Hint | No hint |
|---|---|---|
| Before the rule (proof test) | 30/30 | 26/30 |
| Strict rule 0.19.0 | 28/30 | 30/30 |
| Fix 0.19.1 | 30/30 | 30/30 |

Limits: 2 seeds, at most 3 compactions, and no verdict. It shows a direction. It does not prove the fix.

</details>

### What the benchmarks show and do not show

![Shown and not shown yet](docs/img/proved-vs-not-yet.svg)

Limits of the proof test: it is a small benchmark with 4 seeds (2001 to 2004), and it is our own synthetic benchmark. The live mechanism checks currently include failures: see [docs/evidence.md](docs/evidence.md#live-checks-the-proof-run).

<details><summary>The lists in words</summary>

Shown:

- In the fair test (6 seeds, 10 compactions), plain Claude Code that can search its own chat files scored 97% with a hint (145 of 150) and 73% without (88 of 120). Lossless Handoff scored 100% on both. We claim no gain with a hint. The no-hint result is a secondary result (exact sign-flip p = 0.016), and the registered verdict is INVALID.
- In the earlier run with a blocked baseline, plain Claude Code lost facts as compactions added up (100%, 80%, 58% at 1, 3 and 10 compactions).
- On the questions with a hint, Lossless Handoff stopped that loss up to 10 compactions (100%, 100%, 100%), with 0 items where it was wrong and plain Claude Code was right. Without a hint it scored 93% at 3 compactions and 95% at 10, and at 3 compactions there were 2 such items.

Seen, not proved:

- The loss is largest for replaced decisions, exact strings, error codes and order (a table made after the run).
- The mechanism runs on the author's machine. In the 7 days to 2026-11-24 there were 35 compactions with a handoff receipt. The handoff was delivered 35 of 35 times, and the right agent got it 35 of 35 times. The lossless spot check passed 23 of 34 times and failed 11 times. Cause found on 2026-11-25: all 11 failures were subagent checks, and the check did not read recall's subagent label. This was a check bug, not a recall miss. All 26 main-chat checks passed. Fixed in 0.19.2.

Not shown yet:

- Only 4 seeds, only Sonnet, only up to 10 compactions, and one Claude Code version.
- It is our own benchmark, code-graded. No outside benchmark with forced compactions has run yet.
- On questions without a hint (neutral wording, types R D X S E), B scored 95% (76/80). The 4 wrong items are one probe (seed 2002, exact strings). Claude ran the recall command from a different folder and then answered that it did not know.
- A pilot with 2 seeds ran first. It found a benchmark bug: the deny rules blocked the recall command (fixed in PR #51 and PR #52). The proof test uses only new seeds.
- No study of other people's real work.
- The 0.19.1 fix has 2 seeds and at most 3 compactions.

</details>

### What we have not run yet

Not enough money to run the full LoCoMo or OOLONG benchmark with forced compactions 🥲😭😭

The full suite would use 20 seeds, 30 compactions, Opus and an outside benchmark with forced compactions. The OOLONG run that exists never compacted the main session, so it does not test the handoff (see [Evidence](#evidence)).

To run the proof test again, use `bench/continuity/run.sh proof`. Add `--dry-run` to only print the estimate. The numbers are listed in the evidence register ([docs/evidence.md](docs/evidence.md)).

## Limitations

- **One heavy user so far.** All numbers come from the author's machine. Nobody has tested whether it helps other workflows.
- **Handoffs can be cut.** Main chats: 27% of handoffs (75 of 283, 2026-10-16 to 2026-11-25, `health.jsonl`) hit the 14,000-character size cap and were truncated. Subagents: 0 of 42 (2026-11-17 to 2026-11-24). Only the auto-extracted fact sections are cut first.
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
