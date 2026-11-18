# Lossless Handoff

**Claude Code hooks that make compaction safe: a handoff before every compaction, a decisions list per project, and exact-words search over every earlier chat.**

*Formerly claude-handoff.*

[![CI](https://github.com/pratikgh0se/lossless-handoff/actions/workflows/ci.yml/badge.svg)](https://github.com/pratikgh0se/lossless-handoff/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/pratikgh0se/lossless-handoff)](https://github.com/pratikgh0se/lossless-handoff/releases/latest)

![How a handoff flows through a compaction](docs/handoff-timeline.svg)

## TL;DR

- **Without it:** every compaction turns your session into a generic summary. The exact next step, the dead ends, your standing rules and your exact wording are gone, and the model re-does work or asks again.
- **With it:** before each compaction a structured handoff is written and fed back in. Each project keeps a decisions list that survives compactions, and `recall` finds the exact words of earlier chats (keyword plus local semantic search). Python 3 standard library only.
- **No silent misses:** a hook cannot force Claude Code to run it, so a missed compaction is caught three ways: a handoff is written early, rebuilt after the fact if it is still missing, and counted every night. Subagents get their own handoff. See [When a compaction is missed](#when-a-compaction-is-missed).
- **Proof:** in a 30-day reconcile on the author's machine (2026-11-17), 188 of 192 main compactions had a handoff [C2] and 497 of 497 sampled messages came back byte-identical [C1]. The 4 misses and the subagent gap are listed in [Proof, not promises](#proof-not-promises).

## Why this exists

I run Claude Code with a 400k auto-compact window (`CLAUDE_CODE_AUTO_COMPACT_WINDOW=400000`) instead of the 1M default. With 1M, long sessions rarely compact and pay for their whole context on every turn. In a single-user estimate over 4.7 days, the shorter window gave about 19% lower API-equivalent cost [C8] (a dated one-off study, 2026-10-20, not a bill).

The catch is many more compactions, and each one used to lose rules, decisions and exact wording. This tool is what makes running small and compacting often safe. I use it every day, on my own projects. It has one heavy user so far (see [Limitations](#limitations)).

## Install

```bash
git clone https://github.com/pratikgh0se/lossless-handoff.git
cd lossless-handoff
./install.sh --dry-run   # show the plan, change nothing
./install.sh
```

Then restart open Claude Code sessions: hooks load when a session starts. Prerequisites: `python3` and `bash` on macOS or Linux (Windows is not supported), and a Claude Code version that supports `PreCompact`, `SessionStart` and `PostToolUse` hooks with `additionalContext`. Optional: the `claude` binary on `PATH` (used for the fresh summary) and [Ollama](https://ollama.com/download) (meaning search).

The installer sets up, in one go:

- the hooks and `recall.py`, copied to `~/.claude/hooks/`;
- the entries in `~/.claude/settings.json`, merged next to yours, with a timestamped backup;
- the end-of-chat index (a `SessionEnd` hook);
- an install check that runs at session start and prints one line only when something is wrong (`postcompact-inject.py --check`), with an install manifest (`~/.claude/hooks/.handoff-manifest.json`) it compares against;
- on macOS, two nightly jobs: the index (03:30) and the reconcile-and-prove run (04:15);
- a first index of all your projects, started in the background;
- optionally, `ollama pull bge-m3` for meaning search, if `ollama` is on your PATH.

Options: `--window N`, `--no-window`, `--yes` (pull bge-m3 without asking), `--no-nightly`, `--no-nudge` (skip the context nudge, and remove one from an earlier install), `--managed-hooks` (see [Headless runs](#headless-runs)), `--canary` (opt-in nightly end-to-end test, see below), `--dry-run`, `--force`, `--version`, `--help`. Use `--no-nudge` if another tool already nudges you before compaction. Install is idempotent. Full details are in [What install changes](#what-install-changes).

## Quick start

1. Work as usual. When Claude Code compacts, the handoff and decisions list are injected automatically.
2. After a compaction, ask "what exactly did I say about X?" and Claude runs recall and quotes you.
3. Try it yourself: `python3 ~/.claude/hooks/recall.py user --last 5`

## In daily use (measured)

| What | Number |
|---|---|
| Compactions with a handoff | 217 over 32 days, across 23 sessions; the busiest session had 96 compactions |
| Handoff status | 83% ok, 15% reduced, 2% degraded |
| Nightly self-test | passed 31 of 34 runs; the last 7 nights all passed |
| Decisions lists | 12 projects, 495 active entries (84 standing rules), 111 finished |
| Search index | 48,282 chunks from about 30.6k messages across 1,242 sessions |
| Hook time | median 17 s (90th percentile 29 s); it always exits 0 and never blocks compaction |

Numbers are from the author's own machine, one heavy user; collected 2026-11-16.

## How word search and meaning search work together

`recall.py search` runs two searches and merges them.

- **Word search** (keyword or regex) finds exact things: commands, paths, numbers, error strings and names. It is instant and needs no setup. It uses `rg` if installed, else plain Python.
- **Meaning search** (local bge-m3 through Ollama) finds what was said in different words.
- **Fusion.** Results are merged with reciprocal-rank fusion. Each hit is tagged `[word]`, `[meaning]` or `[both]`, so you can see why it matched.

**Example.** Searching "ask the user questions in pop-ups" surfaced an earlier message, "ask me things one by one in pop ups", which shares almost no words with the query. Illustrative output in the real format (ids made up):

```
mode: hybrid
a1b2c3d4:57 2026-11-13T09:12 user [meaning]: ask me things one by one in pop ups
e5f6a7b8:12 2026-11-14T16:40 assistant [word]: I will ask the user questions before changing the config
```

**Real numbers** (author's machine, collected 2026-11-16; 26 searches that had hits, 336 hits):

| Tag | Share of hits |
|---|---|
| `[word]` | 51% |
| `[meaning]` | 43% |
| `[both]` | 6% |

In 4 of 26 searches the best hit came only from meaning search, which keyword search alone would have missed.

Behaviour worth knowing:

- **It degrades gracefully.** With Ollama off the first line says `mode: keyword only` and search still works. In the measured sample, 10 of 28 classifiable searches ran keyword-only, at least one because the embedding service was down.
- **It is incremental.** The index is refreshed at each compaction, at chat end and nightly. None of it delays Claude Code.
- **The decisions list wins.** If recall and the decisions list disagree, or recall disagrees with your latest words, the decisions list and your latest words win. Recall can surface an older statement.

Command reference is in [Recall commands](#recall-commands).

## Local proof

One command runs every test layer on your machine and writes a dated report:

```
tests/local-proof.sh
```

The report goes to `docs/proof/<date>-<sha>.md`. It starts with a one-line verdict and a table, one row per layer. Past reports are in [docs/proof/](docs/proof/); cite them in release PRs.

| Layer | What it does |
|---|---|
| 1 Static | `bash -n`, `shellcheck`, `py_compile` |
| 2 Smoke | `tests/smoke.sh` |
| 3 Acceptance | the separate acceptance suite, repeated (`--repeat N`, default 3), with flaky tests rerun alone |
| 4 Fresh clone | clone the pushed commit, install, `--check`, uninstall twice, all in a temporary HOME |
| 5 Real end to end | 3 real headless Claude Code runs where a main agent and a subagent each compact; checked with `--prove` |
| 6 Real stress | 3 sessions at the same time, a hook killed at its timeout, a missing PreCompact hook |
| 7 Claims | `--claims-lint README.md`, for information only |

Layers 5 and 6 use real model calls and cost about $3 in total (measured $2.96) (the run stops at $4). Use `--no-real` for a free run, `--real-only` for only layers 5 and 6, `--tests-dir DIR` for an existing tests checkout. The run never changes your real `~/.claude`, your real state folder or your launchd jobs; the report shows a before and after check of them.

## Proof it works

Measured on the author's machine on 2026-11-13/14, on the author's own projects. These are measurements, not promises. All tests are AI-written and AI-graded, on one user's projects.

| Test | Result |
|---|---|
| Lossless retrieval: 497 random messages from before a compaction [C1] | 497 of 497 found and returned byte-identical |
| Meaning search, easy paraphrase test, 118 queries | 98% in the top 10, 89% first |
| Blind quiz after compaction, 33 questions | 41/66 with the v0.4 injection, 50/66 with the full decisions list, 65/66 with the decisions list plus recall |
| Handoff quality, 18 real compactions (score out of 100) | Claude Code's summary alone 62; plus the model's own note 68; plus a fresh Sonnet summary 75-76; given the real recent chat 85 |
| Decisions list, 96 questions about older decisions (out of 100) | 13.5 with the 0.2.0 handoff, 56 with the decisions list |
| Continuity, first 13 real compactions | 13 of 13 had a fresh model-written note, no degraded cases |

**Lossless retrieval.** 497 randomly sampled messages (297 of yours and 200 of Claude's; fixed seed) from before a compaction, across 4 projects with up to 196 compactions each, were found by `recall.py search` and returned byte-identical by `recall.py open --full`. Mean search time 0.7 s, worst 3.1 s on a loaded machine. Limits: a sample, not every message. Messages containing secrets are redacted by design. Subagent transcripts are excluded. Messages over 40,000 characters need `--from` paging; that was added in 0.6.1 after the test found one 14,300-character message cut at the old 12,000-character output cap.

**Blind quiz.** 33 questions over 3 projects: 24 about old decisions and 9 about exact details found only in the chats. Sonnet answered from what a new chat receives, and a separate blind grader scored each answer 0 to 2. The one miss with recall was recall surfacing an older statement over a current rule, which led to the "decisions list wins" rule in 0.6.1. Limits: one run, questions written by a model.

**Handoff quality.** A fresh Claude was quizzed on what it needed to carry on (latest request, next step, decisions, dead ends, rules, files). Version 0.2.0 added the fresh Sonnet summary. Treat it as a strong hint, not proof.

**Decisions list.** By age: 1 compaction 21 to 66, 2 compactions 10 to 56, 3 or more 8 to 44. Recent memory was unchanged (62.5).

## Proof, not promises

The tables above are one-off measurements. From 1.10.0 the install also keeps its own evidence, checked by plain code (no model, no cost), and publishes only what that evidence supports.

**Receipts.** Every handoff that `postcompact-inject.py` injects appends a line to `~/.local/state/claude-handoffs/receipts.jsonl`: transcript, boundary time, hashes and the first 300 characters. Receipts start with the first compaction after install, so earlier compactions have none.

**Four checks per receipt** (`precompact-handoff.py --prove`, verdicts in `proofs.jsonl`):

| Check | Passes when |
|---|---|
| `lossless` | 5 sampled messages from the transcript come back word for word through recall's own commands [C1] |
| `right_agent` | every quoted user line in the handoff occurs in the receipt's own transcript, so a subagent never gets the main session's context [C3] |
| `delivered` | the transcript after the boundary holds the injected text [C4] |
| `decisions_safe` | no decision id present before a ledger update is missing after it, and no superseded id came back [C5] |

**Nightly report.** The 04:15 job runs `--reconcile --prove --days 30` and writes `proof-report.md` (summary line first, then failed checks and skip counts) and `reconcile.json`. `--check` shows `proof failed: <n> checks` once when a run has failures.

**Claims register.** `hooks/claims.json` lists each public claim (`C1` to `C8`) with its evidence source, window, refresh time and minimum rate. Each `--prove` run evaluates it into `claims-status.json` and `claims-report.md`:

| Status | Meaning |
|---|---|
| `pass` | rate at or above the minimum, evidence present and fresh |
| `fail` | rate below the minimum |
| `stale` | evidence older than its refresh time |
| `no-data` | no evidence in the window (neither failing nor stale) |

`precompact-handoff.py --claims` prints the table. Claims in this README carry `[C1]` to `[C8]` markers matching the register. C1 to C6 are live: computed from your own transcripts and receipts. C7 (blind quiz) and C8 (cost) are dated one-off studies with a recorded date and a refresh time, not live rates. Before publishing a document that cites claims, run:

```
python3 ~/.claude/hooks/precompact-handoff.py --claims-lint README.md
```

It exits 1 unless every marker is known and `pass`: an unknown, `fail`, `stale` or `no-data` marker blocks publishing. On a machine with no receipts yet, C1 to C6 are `no-data`, so lint is for the author's own machine. On the author's machine, lint reports C2 and C6 as `fail` until about 2026-12-17: the 30-day window still holds misses from before hooks 1.10.0 (deliberate probe runs, and subagent compactions from before the fix). They are not excluded, because hiding real data would make the register worthless.

**What the author's own data says.** In a 30-day reconcile on the author's machine (2026-11-17), 188 of 192 main compactions had a handoff [C2]. The 4 misses: 3 came from a deliberate probe run with user settings switched off, and 1 was a hook most likely killed at its timeout on 2026-10-23. For subagents, 0 of 28 compactions had a handoff before this release; that gap is the bug 1.10.0 fixes. A live subagent test after the fix: right-agent 2/2 [C3], delivered 2/2 [C4], failed 0. A dated one-off blind quiz (2026-11-14, same sessions with and without the handoff) scored 98% with the handoff against 62% with Claude Code's compaction summary alone [C7]. One author, one machine, small counts.

## Built on the LCM paper

Lossless Handoff is based on, and inspired by, **"LCM: Lossless Context Management"** by Clint Ehrlich and Theodore Blackman ([arXiv:2605.04050](https://arxiv.org/abs/2605.04050)). The paper's idea: when a context window fills up, keep every message verbatim in a store and give the model tools to look things up again, so compaction summarises without destroying anything.

This is an independent project. It is not written by, affiliated with or endorsed by the paper's authors, and the paper's benchmark results are theirs: nothing here repeats them as ours. The only numbers in this README are our own, from the author's machine.

| From the paper | What we took | What we did differently, and why |
|---|---|---|
| Immutable store of every message | Claude Code already keeps each message verbatim in `~/.claude/projects/<slug>/<session>.jsonl`; we use those files as the store and never write to them. | No new database for messages. Nothing to migrate, nothing to keep in sync. |
| Search and expand tools over the store | `recall.py search` finds hits, `recall.py open` expands a hit with the messages around it. | A plain command line tool, not an MCP server: it costs about 0 tokens until used. One line in the injected context tells the model it exists. |
| Summaries of older context | A fresh summary at each compaction, plus the model's own handoff. | No summary tree. Hooks cannot change how Claude Code builds its context, so we add a handoff and a decisions list next to Claude Code's own summary instead of replacing it. |
| (not in the paper) | | A per-project decisions list that survives many compactions, and optional search by meaning with a local embedding model, merged with word search. |

```bibtex
@misc{ehrlich2026lcm,
  title         = {LCM: Lossless Context Management},
  author        = {Ehrlich, Clint and Blackman, Theodore},
  year          = {2026},
  eprint        = {2605.04050},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/2605.04050}
}
```

## How it compares (as of 2026-11-16)

Other projects solve parts of this well. Stars were fetched on 2026-11-16 and move quickly. Ticks come from each project's README, not from reading the code or running it. `?` means the README does not say; "partial" means indirect.

| Project | Stars | Approach | Compaction handoff | Decisions list | Verbatim transcript search | Semantic search | No server needed |
|---|---|---|---|---|---|---|---|
| [lossless-claude/lcm](https://github.com/lossless-claude/lcm) | 60 | Every message in SQLite, old context compacted into a summary DAG | ✓ | ✓ | ✓ | ? | no (daemon) |
| [Martian-Engineering/volt](https://github.com/Martian-Engineering/volt) | 302 | Reference LCM coding agent (OpenCode fork), immutable store, expandable summaries | no (replaces compaction) | ? | ✓ | ? | no (Postgres) |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 117,507 | Hooks capture tool calls, a second agent writes compressed observations | partial | partial | no (compressed) | ✓ | no (local worker) |
| [ccf/agentcairn](https://github.com/ccf/agentcairn) | 77 | Markdown vault plus disposable DuckDB index, BM25 and vectors fused | partial | ✓ | no (distilled notes) | ✓ | ✓ |
| [BetaBots-LLC/callimachus](https://github.com/BetaBots-LLC/callimachus) | 49 | Local index of 13 coding-agent tools, FTS5 plus vectors fused | partial | ✓ | ✓ | ✓ | ✓ |
| [grooverLab/fable](https://github.com/grooverLab/fable) | 19 | Byte-for-byte verbatim session archive, stdlib only | no | no | ✓ | no | ✓ |
| **Lossless Handoff** | new | Verbatim transcripts as source of truth, structured handoff, decisions list, word plus meaning search | ✓ | ✓ | ✓ | ✓ (optional, local) | ✓ |

**Pick something else if:**

- you want cross-tool memory at large scale across several agents: [funes](https://github.com/huggingface/funes) (594 stars) or callimachus;
- you want automatic observation capture of every tool call: claude-mem;
- you use agents other than Claude Code, or want summaries built live during the session: volt;
- you want rules with types, approval and drift checks: look at the projects that focus on that. This tool's decisions list is append-style, without contradiction checks beyond marking an entry superseded.

**What this does differently:**

- Verbatim transcripts stay the source of truth, read as plain files, with no database server.
- Regex search and semantic search are fused over the raw transcripts, not over distilled notes.
- A structured handoff and a reasoned decisions list (what was decided, and why) in one tool.

## How it works

1. **Nudge** (`handoff-nudge.py`, PostToolUse). When context reaches 75% of the auto-compact window, and again every 25,000 tokens, one short note is appended to a tool result asking the working model to write its own handoff to `~/.local/state/claude-handoffs/<session_id>-agent.md` with seven fixed headings: Goal, Parallel work running, Decisions and why, Done, In progress, Dead ends, Exact next step. With a 400k window the reminders come at 300k, 325k and 350k, plus one final note worded "Compaction is imminent" at 355k, about 12,000 tokens below the real compaction point (window minus 33,000), so the model still has room to write the file. If the three living sections (Parallel work running, In progress, Exact next step) are byte-identical to the previous reminder, the next note says the handoff is stale and asks for a rewrite. It costs no extra turn.
2. **Handoff** (`precompact-handoff.py`, PreCompact). Just before compaction it writes `<session_id>-latest.md` (capped at 14,000 characters). It starts with an authority line that says whom to believe when sources disagree. Contents:
   - the model's own handoff, if there is one (labelled stale when out of date);
   - a fresh summary written by Sonnet (`claude -p --model sonnet`) of the conversation since the last compaction, labelled "verify against facts". It runs in parallel with the decisions update, so a compaction takes about 20-40 s;
   - a facts section extracted from the transcript without any model: your last 8 messages, files touched, task state, git branch and status, last Bash commands, last assistant message.

   It always exits 0 and never blocks compaction. If anything fails, a minimal handoff is still written.
3. **Inject** (`postcompact-inject.py`, SessionStart with matcher `compact`). After compaction it feeds the handoff back into the new context. Claude Code caps each hook's injected text at 10,000 characters, so it runs three times (`--part 1/2/3`), splitting on section boundaries and always naming the full file path. Three more runs (`--ledger --part 1/2/3`) inject the decisions list. A stale agent handoff is still included, preceded by a warning with the reason.

**Who wins when sources disagree:** the user's latest words, then the project decisions, then the agent handoff, then the fresh summary, then Claude Code's own summary, then the extracted facts. If unsure, the model should ask.

**Works without the model's cooperation.** If the model never writes the agent file, you still get the fresh Sonnet summary plus the facts (status `reduced`). If the summary also fails or is disabled, you get the facts only, and the injected text starts with a `HANDOFF DEGRADED` warning line.

## When a compaction is missed

A hook cannot force Claude Code to run it, so a handoff can be missed (the hook was killed at its timeout, hooks were switched off for a run, the install broke). Hooks 1.10.0 treat that as the case to design for: write early, recover after, detect every miss, check the install, and keep evidence.

| Step | What happens |
|---|---|
| **Early write** | PreCompact writes `<sid>-pending.json` first, then a deterministic handoff (facts and your last messages) before the first model call. A hook killed at its timeout still leaves a handoff. The health line removes the pending file. |
| **HANDOFF RECOVERED** | If a compaction still has no handoff, the SessionStart `compact` hook rebuilds one from the transcript (no model call, 6 s deadline) and the injected text starts with `HANDOFF RECOVERED`. |
| **`--check`** | At session `startup` and `resume`, `postcompact-inject.py --check` prints one `HANDOFF CHECK:` line when a hook is not wired, a hook file is missing or changed since install (it compares the manifest), the two hooks' versions differ, or reconcile found compactions without a handoff. It prints nothing when all is well. |
| **Nightly reconcile and proof** | At 04:15, `precompact-handoff.py --reconcile --prove --days 30` counts every `compact_boundary` in your transcripts against `health.jsonl` and proves each receipt (see [Proof, not promises](#proof-not-promises)). |

Claude Code can also precompute a compaction. PreCompact runs when the summary is built, and the compaction is applied later, sometimes hours later. The messages from that time on stay word for word after the summary. So the handoff from the first moment, plus the kept messages, cover everything. Hooks 1.10.1 see this case: if the handoff is newer than the previous compaction boundary, they inject it with the line `Note: this compaction was prepared at <time>; ...` and do not run recovery.

Restart open Claude Code sessions after installing: hooks load when a session starts. The longer write-up is [docs/handoff-reliability.md](docs/handoff-reliability.md).

## Subagents

When a subagent compacts, Claude Code fires the hooks with `agent_id` set but with the parent's `session_id` and `transcript_path`. Before 1.10.0 that looked like a main-session compaction and no subagent handoff was written. Now each compacting subagent gets its own handoff, built from its own transcript (`<session>/subagents/agent-<agent_id>.jsonl` next to the parent transcript) and stored under `<sid>-a-<agent_id>` files.

- A subagent never reads or writes the main session's handoff, and the other way round [C3].
- A subagent never merges the decisions list and never starts the indexer. The nudge hook ignores subagent events (non-empty `agent_id`), so a subagent is never told to write the main session's handoff file.
- If the subagent transcript is missing, the health row says `degraded` / `agent_transcript_missing` and no handoff is written.
- Reconcile counts subagent compactions separately, and the register tracks that they are covered [C6]. Before 1.10.0 they were not: 0 of 28 in the author's first 30-day reconcile.

**Rules at subagent start (hooks 1.13.0).** A new subagent gets no project rules, and most subagents never compact. So the installer registers a `SubagentStart` hook (`postcompact-inject.py --subagent-start`, timeout 10). It gives the new subagent, and only the subagent, one block of context: the active `rule` entries of the project decisions list (newest first, at most 4,000 characters, cut at an entry boundary) and the recall line. It never gives decisions, tasks, the main agent's handoff or the agent notes [D3]. If there is no ledger or no rule, only the recall line is given. `HANDOFF_SUBAGENT_RULES=0` turns the hook off. Each run adds a row with `event: "subagent_start"` to `health.jsonl`; `--prove` and `--reconcile` skip these rows. The hook takes about 50 ms with 200 rules. `SubagentStart` is a new hook event: restart open Claude Code sessions after you update. The installer prints a line about this only when it adds the entry.

## Headless runs

`claude -p` and the Agent SDK load your user hooks by default. They skip them only with `--bare`, `disableAllHooks`, `--setting-sources` without `user`, or SDK `settingSources: []`.

To keep the handoff hooks in every run except `--bare`, use managed settings:

```
./install.sh --managed-hooks
```

This is a standalone mode that changes nothing else. It writes `~/.local/state/claude-handoffs/managed-settings.json` (an existing system file is read and merged in, never written) and prints the command to install it, which you run yourself because it needs admin rights. The script never runs sudo:

```
# macOS
sudo install -m 644 ~/.local/state/claude-handoffs/managed-settings.json "/Library/Application Support/ClaudeCode/managed-settings.json"
# Linux: /etc/claude-code/managed-settings.json
```

With managed hooks installed, only `--bare` skips them. `--check` accepts hooks from user or managed settings. Reconcile reports any compaction that still got no handoff, headless or not.

## The project decisions list

A handoff is per session, but decisions belong to the project. One plain-text list is kept per project (a git repo, or the folder you started in when there is no repo) at `~/.local/state/claude-handoffs/projects/<project>-<hash>/decisions.md`. One line per decision: an id (`D12`), the date, a kind, what was decided, and why.

- **Kinds.** `[rule]` (a standing rule or working preference), `[decision]` (a choice) or `[task]` (a follow-up you asked for). Older untagged lines count as decisions.
- **What goes in.** Only things you decided or explicitly approved: a choice, a rule, a constraint, a permission, a rejected option. Not plans, not progress, not the assistant's own unapproved ideas.
- **Kept up to date.** At every compaction a second Sonnet call reads the conversation since the last update and the current list, and returns the updated list. When a task is finished the line is marked `RESOLVED` and is no longer injected. Rules are never resolved by the model.
- **Never deleted.** When you change your mind, the old decision is marked `SUPERSEDED by D<n>` with the reason and stays in the file. Before each update the previous list is saved as `decisions.<timestamp>.md` (the newest 20 are kept).
- **Code checks the model.** Sonnet proposes, plain code decides: an entry the model drops is put back, a superseded entry is never revived, existing ids never change, over-long lines are shortened rather than dropped, and a result with no valid line is thrown away. A project lock keeps two compactions in the same repo from overwriting each other.
- **Injected after compaction and in new chats.** Three parts, rules first and always in full, then decisions, then tasks, newest first. What does not fit in 3 x 10,000 characters becomes one-line index entries, so nothing is silently dropped. The same parts are injected at `startup` and `resume`, so a fresh session does not re-ask what you already settled.
- **Tidying an old list.** `python3 ~/.claude/hooks/precompact-handoff.py --ledger-maintain <repo>` runs one maintenance pass: it tags untagged entries, resolves finished tasks and supersedes contradictions. It adds no entries and edits no text.

Turn it off with `HANDOFF_LEDGER=0`. Existing lists are never deleted by turning it off or by uninstalling.

## llm_map: label many items with a small model

`llm_map.py` sends each item of a large list through a small model (Haiku by default) and writes one exact answer per item. The main model then counts or aggregates the answers with a script, so it does not guess a count from a sample.

When to use it: a task needs a label, class, extracted value or check for each of hundreds of items or more. A pre-registered OOLONG test (`bench/oolong/`) showed that plain Claude Code filters with a regex, reads a sample and estimates the count.

```
python3 ~/.claude/hooks/llm_map.py --in reviews.txt --prompt "Label each review as positive, negative or mixed." --out labels.jsonl [--labels "positive|negative|mixed"] [--model haiku] [--batch 100] [--jobs 8] [--max-usd 2.00] [--json-out]
```

- `--in` is a text file with one item per line, or a `.jsonl` file with `text` and an optional `id`.
- `--out` gets one JSON line per item, in input order, with `i`, `text`, `out` and (if it failed) `error`.
- `--labels "a|b|c"` sets the allowed answers (2 or more, split on `|`; not with `--json-out`). `out` is always a canonical label. A reply maps to a label if it equals one (trim, case fold), or if it is a prefix of exactly one label, or exactly one label is a prefix of it. The prefix must end at a word end of the longer text (`numeric` matches `numeric value`; `h` does not match `human being`). Other replies are invalid, are retried once, and then get `out` null and `error: "label: <reply>"`.
- Defaults are 100 items per batch and 8 batches at the same time, so 3,000 items take about one minute. After each batch, stderr gets `llm_map: <done> of <n> items done`.
- A missing, invalid or unparsable answer is retried once. The last stdout line is `llm_map: <n> items, <ok> ok, <failed> failed, <b> batches, cost $<x>`. Exit code 3 means some items failed.
- Cost note: each batch is a real model call and costs money. Haiku batches of 100 items cost a fraction of a cent each. `--max-usd` (default 2.00) stops new batches when the cap would pass; the unsent items get `error: "budget"`.
- Each call runs `claude -p` with no tools, no hooks, no MCP servers and no saved session, in a new temp folder. Lossless Handoff hooks never run for these calls, so they write no handoffs or health rows.
- The installer also writes the skill `~/.claude/skills/llm-map/SKILL.md`. Its description tells Claude Code to use llm_map for each-item tasks on large lists, and its body gives the command and the rule to report exact counts and the number of failed items. Install leaves a skill file that is not ours (no marker line) unchanged; uninstall removes only the marked file.

## Recall commands

`recall.py` searches every earlier chat in the same project (all sessions whose folder is inside the project's git root), read-only, over the transcripts Claude Code already keeps. A summary keeps decisions but loses exact commands, numbers, paths and your own wording; this gets them back.

```
python3 ~/.claude/hooks/recall.py search "zebra-mode"          # words, regex or meaning (hybrid)
python3 ~/.claude/hooks/recall.py search "why we dropped the cache" --meaning
python3 ~/.claude/hooks/recall.py search "deploy.sh" --keyword --fixed --role user
python3 ~/.claude/hooks/recall.py open abcd1234:57             # a hit plus 2 messages each side (--around K, --full)
python3 ~/.claude/hooks/recall.py open abcd1234:57 --full      # the whole message, up to 40,000 chars
python3 ~/.claude/hooks/recall.py open abcd1234:57 --full --from 40000   # next page of a longer message
python3 ~/.claude/hooks/recall.py user --last 20               # your own typed messages, newest first
python3 ~/.claude/hooks/recall.py handoffs                     # this project's handoff files
python3 ~/.claude/hooks/recall.py index                        # build or refresh the index for this project
python3 ~/.claude/hooks/recall.py index --all                  # every project that has a git repo
```

**Summary nodes.** Each compaction in a transcript gets one leaf node: an id (`n` and 10 hex characters), the session, the transcript line range it covers, the time and the token count before the compaction. The hooks read the nodes from Claude Code's own `compact_boundary` records. No model call is made for them. The list is stored in `projects/<project>-<hash>/nodes.jsonl`, and the SessionStart `compact` hook adds new nodes from the saved byte offset, so it reads only new bytes.

```
python3 ~/.claude/hooks/recall.py map                    # one line per node, oldest first: id, time, session, line range, gist
python3 ~/.claude/hooks/recall.py describe <node id>     # the node's fields and the full Claude Code summary of that compaction
python3 ~/.claude/hooks/recall.py search "word" --node <node id>   # only hits inside that node's line range
python3 ~/.claude/hooks/recall.py nodes --backfill       # add nodes for all transcripts of the project at once
```

Each `search` hit ends with `[node <id>]`, or `[node live]` when it is after the last compaction. After a compaction, the injected context has one line that names the newest node. `--prove` checks that every `compact_boundary` has one node and that the line ranges leave no gap or overlap.

**Recall subagent.** The installer writes `~/.claude/agents/recall.md`, a small agent (model `haiku`, tools `Bash` and `Read`) that runs `map`, `search`, `describe` and `open` and returns at most 15 short quotes with message ids and node ids. When the file is installed, the injected recall line tells the main agent to use it for wide lookups so long recalled text stays out of the main context, and to search directly for one exact fact. Nothing blocks the main agent from running `recall.py open` itself.

Every command accepts `--cwd DIR` (default: the current folder). `search` also takes `--session SID8|all`, `--limit N` and `--no-subagents`. Search, `open` and the meaning index include the work of subagents by default. A subagent hit has the id `<sid8>/<agent8>:<line>` and the tag `[agent <agent8>]`; it shows what a subagent saw or did, not what you typed. `--no-subagents` leaves them out. The old `--subagents` flag is still accepted and does nothing. `user` still reads only the main chats, because a subagent's user turns are prompts from the main agent. In a plain pattern (letters, digits, spaces, `-`, `_`, `.`), a space, `-` and `_` match each other, so `ledger key` finds `ledger-key`; `--fixed` keeps the match exact (hooks 1.13.1). A hit line from a tool call ends with ` -> result <id>` when the tool returned a result later in the same chat; run `open <id>` to read what the tool returned. `--keyword` is words only, `--meaning` is the embedding index only. Output is capped at 12,000 characters, and obvious secrets (API keys, tokens, `password=...`) are replaced by `[redacted]` before printing or embedding. `open <id> --full` returns up to 40,000 characters; a longer message ends with a line giving the exact `--from <N>` to continue with.

**Meaning search setup.** It needs a local embedding model: [Ollama](https://ollama.com/download) with `ollama pull bge-m3`. If `ollama` is on your PATH the installer offers to pull it (`--yes` says yes; a non-interactive run skips it and prints the command). If Ollama is not installed, the installer prints a hint and carries on. The installer never installs Ollama itself. Backend settings are `RECALL_EMBED_*` in [Configuration](#configuration).

## What install changes

- Copies `precompact-handoff.py`, `postcompact-inject.py`, `handoff-nudge.py`, `recall.py` and `claims.json` to `~/.claude/hooks/` (a differing existing file is first saved to `~/.claude/hooks/.claude-handoff-backup-<timestamp>/`).
- Copies `agents/recall.md` from this repository to `~/.claude/agents/recall.md` (the recall subagent). It keeps a file of that name that does not hold the marker line `<!-- lossless-handoff:recall-agent -->` and says so. Uninstall removes the file only when it holds the marker. The repository file is the single source: a benchmark or a project can copy the same file into its own `.claude/agents/` folder.
- Writes `~/.claude/hooks/.handoff-manifest.json`: version, time and a SHA-256 per installed file, which `--check` compares.
- Records everything it added in `~/.claude/hooks/.claude-handoff-install.json`, so uninstall removes exactly that.
- Merges into `~/.claude/settings.json` (backup `settings.json.bak-<timestamp>`):
  - a PreCompact hook (timeout 150) and a PostToolUse hook (matcher `*`, timeout 5);
  - a SessionStart `compact` group with the three inject commands and the three `--ledger --part 1/2/3` commands (timeout 10), and `startup` and `resume` groups with the three `--ledger` commands plus `postcompact-inject.py --check` (timeout 5);
  - a `SessionEnd` hook running `recall.py session-end` (timeout 5);
  - a `SubagentStart` hook running `postcompact-inject.py --subagent-start` (timeout 10);
  - `permissions.allow` entries `Edit(~/.local/state/claude-handoffs/**)` (so the model can write its handoff without a prompt) and `Bash(python3 ~/.claude/hooks/recall.py:*)` (so it can run recall without a prompt);
  - `env.CLAUDE_CODE_AUTO_COMPACT_WINDOW` = `"400000"` unless already set (`--window N` picks another value, `--no-window` leaves it alone).
- Creates `~/.local/state/claude-handoffs/`.
- Optionally runs `ollama pull bge-m3`.
- On macOS, unless `--no-nightly`: writes the LaunchAgent `~/Library/LaunchAgents/com.lossless-handoff.recall-index.plist` (daily 03:30, runs `recall.py index --all --max-seconds 3000`, log `~/.local/state/claude-handoffs/recall/index-all.log`) and loads it. On Linux it prints the equivalent crontab line and does not edit your crontab.
- On macOS, unless `--no-nightly`: writes and loads the LaunchAgent `~/Library/LaunchAgents/com.lossless-handoff.handoff-reconcile.plist` (daily 04:15, runs `precompact-handoff.py --reconcile --prove --days 30`, log `~/.local/state/claude-handoffs/reconcile.log`). On Linux it prints that crontab line too (`15 4 * * * python3 ~/.claude/hooks/precompact-handoff.py --reconcile --prove --days 30 >> ~/.local/state/claude-handoffs/reconcile.log 2>&1`, with your real path).
- With `--managed-hooks` (standalone): stages a managed-settings file in the state folder and prints the `sudo install -m 644 ...` command; it changes nothing else and never runs sudo.
- Starts `recall.py index --all` in the background.
- With `--canary` (opt-in, off by default because it makes real model calls, about $0.03-0.10 per run): copies `tools/handoff-canary/` to `~/.claude/hooks/handoff-canary/` and `handoff-canary.sh` to `~/.claude/hooks/`, and on macOS writes the LaunchAgent `com.lossless-handoff.handoff-canary` (daily 03:30, `--catch-up`); on Linux it prints the crontab line. The canary drives two headless Claude Code sessions past a compaction and checks the handoff arrives; see [`tools/handoff-canary/README.md`](tools/handoff-canary/README.md).

Your other hooks and settings are left alone: new entries are appended next to existing ones. If the same hook scripts are already registered from another path, install prints those commands and exits 2, because every hook would run twice; remove them, or pass `--force`. Install fails with a clear message if `python3` is missing or `settings.json` is not valid JSON.

## What gets written where

| Path | Content |
|---|---|
| `~/.local/state/claude-handoffs/<sid>-latest.md` | The handoff that is injected after compaction. `<sid>-<timestamp>.md` is a copy. |
| `<sid>-agent.md` | The model's own handoff (written by the model). |
| `<sid>-agent.meta.json` | Nudge state and timestamps (numbers only, no text). |
| `recall-index.json`, `recall/` | Recall caches: which transcripts belong to which project, and the meaning index (`<project>.sqlite`, `index.log`). Safe to delete. |
| `health.jsonl` | One JSON line per compaction: time, trigger, agent file fresh/stale/absent, fallback result, ledger result (`ok`, `unchanged`, `failed`, `locked`, `disabled`) and counts, duration, size, status `ok` / `reduced` / `degraded`. No message text or paths. Rotates at 5,000 lines. |
| `<sid>-last-health.json`, `<sid>-degraded.json` | Per-session status and degraded reasons. |
| `<sid>-pending.json` | Marker while PreCompact runs; removed by the health line. |
| `<sid>-a-<agent_id>*` | The same files for a compacting subagent (handoff, latest, pending, note). Health rows for subagents carry `agent_id` and `agent_type`. |
| `reconcile.json`, `reconcile.log` | Last reconcile result (with the once-only notice marker for `--check`) and the nightly job's output. |
| `receipts.jsonl`, `proofs.jsonl`, `proof-report.md`, `proof-notice.json` | Proof: one receipt per injected handoff, one verdict per receipt, the report, and the once-only alert marker. |
| `claims-status.json`, `claims-report.md`, `claims-notice.json` | Claims register evaluation and its once-only alert marker. |
| `managed-settings.json` | Only after `install.sh --managed-hooks`: the file you copy to the system location. |
| `~/.claude/hooks/.handoff-manifest.json` | Installed hook file hashes (not in the state folder). |
| `projects/<project>-<hash>/nodes.jsonl`, `nodes.state.json`, `nodes.lock` | Summary nodes: one line per compaction (ids, session, line range, times, token count, paths). It holds no message text. |
| `~/.claude/agents/recall.md` | The recall subagent (user level; not in the state folder). Source file in this repository: `agents/recall.md`. |
| `projects/<project>-<hash>/decisions.md` | The project's decisions list (kept by uninstall). Beside it: `decisions.<timestamp>.md`, `decisions.state.json`, `decisions.lock`. |

Handoff files (`*.md`) are kept for 365 days. Set `HANDOFF_RETENTION_DAYS` to change this, or to `0` to keep them forever. The small status files (`*-degraded.json`, `*-last-health.json`, `*-pending.json`) are removed after 14 days. The `projects/` folder is never cleaned. Longer retention means more of your chat text stays on disk for longer. Claude Code also deletes its own chat transcripts after `cleanupPeriodDays` days (default 30), and recall can only find messages that are still there. Run `./install.sh --keep-transcripts` to set it to 365 (it never lowers a value and never overrides a managed settings file). The session-start check warns if the value is below 90. The directory is outside `~/.claude/` because Claude Code refuses model writes under that path ([ADR 0008](docs/adr/0008-handoffs-directory-under-local-state.md)).

## Verify

```
claude -p --model haiku "say hi" --output-format json   # note the session_id
claude -p --model haiku --resume <session_id> "/compact"
tail -n 3 ~/.local/state/claude-handoffs/health.jsonl
```

A new line with `"trigger": "manual"` means the PreCompact hook fired. In a normal session, run `/compact` and look at the same file. `status` is `ok` (model handoff used), `reduced` (fresh summary used instead) or `degraded` (facts only). You can also run `bash tests/smoke.sh`; it uses a temporary HOME and does not touch your real settings.

To test a real compaction without touching your own install:

1. Install into a temporary home with `HOME=<tmp> LOSSLESS_HANDOFF_NO_LAUNCHCTL=1 ./install.sh --no-nightly`, so no LaunchAgent is written or loaded.
2. Keep your real HOME for the run, because `claude` reads its login from there.
3. Run `claude -p --setting-sources local --settings <tmp>/.claude/settings.json ...` from a fresh folder, with `HANDOFF_STATE_DIR=<tmp>/.local/state/claude-handoffs`. This switches your own hooks off and keeps all handoff files in the temporary folder.
4. To force a compaction quickly, set `CLAUDE_CODE_AUTO_COMPACT_WINDOW=30000` both in the process environment and in the `env` of the settings file you pass with `--settings`. If you run with your own user settings and they set this variable (the installer sets 400000), that value wins over the process environment, so pass `--settings '{"env":{"CLAUDE_CODE_AUTO_COMPACT_WINDOW":"30000"}}'`. Keep each file the agents read under about 20k tokens (for example 900 lines); the Read tool refuses larger files, and then the context does not grow.
5. Check with `HANDOFF_STATE_DIR=... python3 <tmp>/.claude/hooks/precompact-handoff.py --prove --days 1`.

Use a folder name that contains `handoff-canary`, so that the nightly check on your real install does not count these compactions as missed.

## Configuration

| Variable | Effect |
|---|---|
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | Window size in tokens. Nudge thresholds are 75% of it, then every 25,000, then a final note (window minus 45,000). Default 400000 if unset. |
| `HANDOFF_SUMMARY=0` | Disable the fresh summary at compaction (no model call; facts only). |
| `HANDOFF_SUMMARY_MODEL` | Model for the fresh summary. Default `sonnet`. |
| `HANDOFF_SUMMARY_TIMEOUT` | Seconds to wait for the summary (1-300). Default 75. |
| `HANDOFF_LEDGER=0` | Disable the decisions list: no merge call, nothing written, nothing injected. |
| `HANDOFF_LEDGER_MODEL` | Model for the decisions update. Default: the summary model. |
| `HANDOFF_LEDGER_TIMEOUT` | Seconds to wait for the decisions update (1-300). Default 100. The PreCompact hook timeout is 150. |
| `HANDOFF_HAIKU_FALLBACK=0` | Legacy switch from 0.1.x; still honoured and also disables the fresh summary. |
| `RECALL_EMBED_URL`, `RECALL_EMBED_MODEL`, `RECALL_EMBED_BACKEND`, `RECALL_EMBED_KEY` | Meaning search backend. Defaults: Ollama at `http://localhost:11434`, model `bge-m3`. Backend `openai` works with any `/v1/embeddings` server; the key is an optional Bearer token. |
| `HANDOFF_RETENTION_DAYS` | Days to keep handoff `*.md` files. Default 365. `0` keeps them forever. A value that is not a whole number counts as 365. The `*-degraded.json`, `*-last-health.json` and `*-pending.json` files always use 14 days. |
| `HANDOFF_SUBAGENT_RULES=0` | Do not give project rules to a new subagent. The `SubagentStart` hook then prints nothing. |
| `HANDOFF_COMPACT_STEER=0` | Do not print the guidance for Claude Code's own compaction summary. The hook prints it by default. The guidance is added to any text that you type after `/compact`. The effect on summary quality is measured in a later benchmark. |
| `LOSSLESS_HANDOFF_MANAGED_SETTINGS` | Test only. Path of the managed settings file that `install.sh`, `uninstall.sh` and `postcompact-inject.py --check` read instead of `/Library/Application Support/ClaudeCode/managed-settings.json`. The older name `HANDOFF_MANAGED_SETTINGS_PATH` still works. The tools never create the real file. |
| `HANDOFF_STATE_DIR` | Use another directory instead of `~/.local/state/claude-handoffs`. |
| `LOSSLESS_HANDOFF_NO_LAUNCHCTL=1` | `install.sh` and `uninstall.sh` write and remove the LaunchAgent files but never call `launchctl`. Use it for any install into a temporary HOME on macOS: `launchctl` acts on your real login session, so without it a test install loads, and a test uninstall unloads, jobs with the real labels. |
| `HANDOFF_HOOK_CHILD` | Set by the hook for its own summary call so it never recurses. Do not set it yourself. |

## FAQ

**Does it cost tokens?** About one short note per nudge, plus up to about 14,000 characters injected once per compaction and up to about 20,000 characters of decisions. Each compaction adds two `claude -p` Sonnet calls (fresh summary and decisions update; 20-40 s in parallel, roughly $0.10-0.20 of API-equivalent usage). Set `HANDOFF_SUMMARY=0` and `HANDOFF_LEDGER=0` to avoid them.

**Will recall find old messages?** Only while Claude Code still keeps the transcript. The default is 30 days. Run `./install.sh --keep-transcripts` (365 days) or set `"cleanupPeriodDays"` yourself. Handoff files are kept 365 days. A longer retention means more chat text stays on your disk for longer.

**Which new fields does the health row have?** `excerpt_chars` is how many characters of transcript the handoff model received (0 if no model call was made). `excerpt_dropped` is how many characters of the current segment were left out because of the 120,000-character limit (0 if nothing was cut). `--prove --days N` prints `excerpt cut: <c> of <n> compactions, median dropped <m> chars`. This line is information only and never fails a proof run. It measures how often the cut happens; it does not claim any gain in answer quality.

**What does the PreCompact hook print?** A short block of guidance for Claude Code's own summary (quote your words, keep exact values, list running work, end with the next step). The hook gives this guidance only. The effect on summaries is measured in a later benchmark. Set `HANDOFF_COMPACT_STEER=0` to turn it off. The health row has a `steer` field (`printed` or `off`).

**Does it work in the desktop app?** Yes. The desktop app runs the same hooks from `~/.claude/settings.json`.

**Does it work with my existing hooks?** Yes. Install merges into your existing `hooks` groups and never removes or reorders yours; uninstall removes only its own commands.

**Where must `CLAUDE_CODE_AUTO_COMPACT_WINDOW` be set?** In your user `~/.claude/settings.json` under `env` (install does this) or exported in the shell that starts Claude Code. A live test showed `env` in a project's `.claude/settings.json` did not override it.

**What window size should I use?** One that comfortably exceeds your baseline context. Very small windows (below roughly 150k) compact before the 75% nudge is reached; the PreCompact hook then covers it. Savings come from long sessions on 1M-context models; if your sessions rarely pass 300k tokens the window never triggers and you mainly get the handoff. Whether a shorter context also improves answer quality was not measured. See [ADR 0001](docs/adr/0001-compact-window-400k-with-handoff.md).

**Can the nudge be skipped?** Yes. It reads the previous turn's token count, so one very large tool result can jump past the threshold without a nudge. The PreCompact hook still writes a handoff.

**Does it send anything over the network?** The scripts do not, except meaning search, which sends message text to the embedding server you configure (by default Ollama on your own machine). The two per-compaction calls run your local `claude -p`. See `SECURITY.md`.

## Troubleshooting

- Logs and health live in `~/.local/state/claude-handoffs/` (or `$HANDOFF_STATE_DIR`). Start with `tail -n 5 ~/.local/state/claude-handoffs/health.jsonl`: one line per compaction with `status` `ok`, `reduced` or `degraded`.
- `<sid>-degraded.json` and `<sid>-last-health.json` in the same folder say why a compaction was degraded.
- A `HANDOFF CHECK:` line at session start names what is wrong (hook not wired, file missing or changed, version mismatch, compactions without a handoff). Run `./install.sh` again, then restart open sessions. `proof failed` and `claims` lines point at `proof-report.md` and `claims-report.md` in the state folder.
- A `HANDOFF RECOVERED` line at the top of the injected text means PreCompact did not finish and the handoff was rebuilt from the transcript without a model call; check `health.jsonl` and `hooks-error.jsonl`.
- No health line after `/compact`: restart Claude Code (hooks load at startup), then check `~/.claude/settings.json` has the `PreCompact` entry and that `~/.claude/hooks/precompact-handoff.py` exists.
- No nudge: it only fires above 75% of the window (300k for 400k) and needs a usage entry in the transcript; check `CLAUDE_CODE_AUTO_COMPACT_WINDOW`.
- Search says `keyword only`: Ollama is not running or `bge-m3` is not pulled. Start Ollama and run `ollama pull bge-m3`.
- Settings or hooks in a bad state: install and uninstall leave timestamped backups (`settings.json.bak-*`, `~/.claude/hooks/.claude-handoff-backup-*`).
- Something else: run `bash tests/smoke.sh`, then open an issue using the bug report template.

## Tests

Three layers run on every push and pull request (GitHub Actions, Ubuntu and macOS):

1. **Static checks:** `bash -n`, shellcheck and `py_compile`.
2. **Smoke test:** `bash tests/smoke.sh`. It does install, the hooks, recall, the canary and uninstall in a temporary HOME.
3. **Acceptance tests:** the code-blind suite in [lossless-handoff-tests](https://github.com/pratikgh0se/lossless-handoff-tests), at the commit named in `tests.ref`.

**The code-blind rule.** The acceptance tests are written only from [`docs/spec.md`](docs/spec.md), by a writer who never reads the hook code. The people and agents who change the hooks never read the tests. They see only the test names and the assertion output. A behaviour change therefore starts in `docs/spec.md`. The tests follow the spec, and the hooks follow the tests.

**When a pull request changes behaviour:**

1. Amend `docs/spec.md` (a new or changed AC number).
2. Update the tests in lossless-handoff-tests from the spec.
3. Set `tests.ref` in this repository to the new tests commit, in the same pull request.

Run the acceptance tests locally:

```bash
git clone https://github.com/pratikgh0se/lossless-handoff-tests ../lossless-handoff-tests
git -C ../lossless-handoff-tests checkout "$(cat tests.ref)"
HANDOFF_HOOKS_DIR="$PWD/hooks" LOSSLESS_HANDOFF_REPO="$PWD" LOSSLESS_HANDOFF_NO_LAUNCHCTL=1 \
  python3 -W ignore -m unittest discover -s ../lossless-handoff-tests
```

The tests use a temporary HOME and never call `launchctl`, so your own install is not touched.

## Limitations

- **One heavy user so far.** All numbers come from the author's machine. Whether it helps other workflows is untested.
- **Handoffs can be cut.** 20% of handoffs (43 of 217) hit the 14,000-character size cap and were truncated. 15% were `reduced` and 2% `degraded`, and the nightly self-test failed 2 of 34 runs.
- **Recall is new.** It has existed since 2026-11-12, and its use so far is mostly the author's, much of it while building and testing it. The meaning half is a minority of wins (4 of 26 searches had a meaning-only top hit), and 143 meaning hits count lines shown, not proof they were useful.
- **Misses still happen.** 4 of 192 main compactions in the 30-day reconcile had no handoff (see [Proof, not promises](#proof-not-promises)); the early write, recovery and `--check` exist to shrink and surface them, not to promise zero. Receipts only exist from the first compaction after install, so proof rates start small. C7 and C8 are dated one-off studies, not live rates.
- **Platform.** The nightly jobs (index and reconcile-and-prove) are macOS LaunchAgents; on Linux you add the printed cron lines yourself. Windows is not supported. The nightly self-test mentioned above is the canary; it ships in `tools/handoff-canary/` and is opt-in (`./install.sh --canary`, about $0.03-0.10 per run).
- **AI-graded evals.** The quizzes and benchmarks were written and graded by models, on one user's projects. The 19% cost estimate is a single 4.7-day, one-user figure against a modelled counterfactual, not a bill.
- The nudge only works if the model obeys it. If it does not, you still get the fresh summary, which is lossier than the model's own note.
- The fresh summary and the decisions update each run `claude -p --model sonnet` and use some of your quota (75 s and 100 s timeouts by default).
- The decisions list needs `fcntl` (macOS and Linux) and only records what you said in chat; a decision you never wrote or approved is not captured.
- The nudge reads context size from the transcript's last usage entry, so it lags by one assistant message.
- The order in which the three injected parts appear in context is not guaranteed; each part names its number.

## Uninstall

```
./uninstall.sh
```

Removes exactly the hook entries install added (matched by command path; other hooks in those groups stay), the allow rules and the window value if install added them, the macOS LaunchAgents (index and reconcile), the `--check` entries, and the hook files including `recall.py`, `claims.json` and the manifest, after backing up settings. A system managed-settings file is never touched (it needs sudo); uninstall tells you if one is present. Handoff files, receipts, proofs, indexes and the project decisions lists under `~/.local/state/claude-handoffs/` stay; delete that folder yourself if you want them gone. Backups are kept.

## More

- Reliability notes (misses, subagents, headless runs, proof, state files): [docs/handoff-reliability.md](docs/handoff-reliability.md).
- Behaviour contract these hooks and their tests are written from: [docs/spec.md](docs/spec.md).
- Decisions: [ADR 0007](docs/adr/0007-handoff-degraded-vs-reduced.md) (degraded vs reduced), [ADR 0011](docs/adr/0011-handoff-nudge-bounded-channel.md) (the nudge).

MIT license, copyright Pratik Ghose. See `LICENSE`. Security notes: `SECURITY.md`. Changes: `CHANGELOG.md`.
