# agentdream

[![CI](https://github.com/mvplab-ai/agentdream/actions/workflows/ci.yml/badge.svg)](https://github.com/mvplab-ai/agentdream/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/agentdream.svg)](https://pypi.org/project/agentdream/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10 | 3.11 | 3.12 | 3.13](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](pyproject.toml)
[![GitHub stars](https://img.shields.io/github/stars/mvplab-ai/agentdream?style=flat)](https://github.com/mvplab-ai/agentdream/stargazers)

**Sleep-time memory consolidation ("dreaming") for any agent and any model — local-first, reviewable, zero dependencies.**

Website: **[agentdream.dev](https://agentdream.dev)**

![A 25-second terminal highlight: agentdream runs a dry-run dream, shows a cited correction in the report, then applies it on accept. The original store stays unchanged until you accept.](https://raw.githubusercontent.com/mvplab-ai/agentdream/main/docs/demo.gif)

The GIF is a highlight of a real terminal run with the `claude-cli` backend (your Claude Code login, no API key). The quickstart below uses the bundled example and the deterministic backend, so it works offline with no model.

Agents accumulate memory notes that drift: duplicates pile up, old values go stale, and some notes are
simply wrong — the agent keeps acting on them and failing. `agentdream` reads your agent's memory store
plus recent session transcripts and produces a **new, reorganized store** and a report: duplicates merged,
stale values replaced, notes corrected *with citations to the transcript lines that prove it*, and new
insights (recurring mistakes, repeated preferences, converged workflows). Your input store is never
modified; you review the diff and accept all, some, or none of it.

It is an open-source take on the idea behind Anthropic's
[Dreams](https://platform.claude.com/docs/en/managed-agents/dreams) for Claude Managed Agents and the
Letta / UC Berkeley [sleep-time compute](https://arxiv.org/abs/2504.13171) paper — but it runs on your
machine, works with markdown folders (Claude Code's `CLAUDE.md` / memory dirs), JSON, SQLite and
[stancelog](https://github.com/systemagents-ai/stancelog) stores, and with no model at all
(deterministic heuristics), a local model (Ollama, LM Studio, vLLM), the Anthropic or OpenAI APIs, or
your Claude Code login.

## 60-second quickstart

```bash
pip install agentdream               # Python >= 3.10, no dependencies
git clone https://github.com/mvplab-ai/agentdream && cd agentdream     # only for the bundled example below

agentdream dream --memory examples/memory --sessions examples/sessions     # dry run: nothing is changed
agentdream show <job-id>                 # the report: what changed, why, with transcript citations
agentdream accept <job-id>               # apply it (the original is backed up first)
agentdream accept <job-id> --only correct-2ec6281c,merge-a91fbf3a     # ...or just some operations
agentdream accept <job-id> --types merge,replace --min-confidence 0.75  # ...or just the low-risk ones
agentdream discard <job-id>              # ...or throw it away
agentdream restore <job-id>              # undo an accept: put the backup back
```

Point it at your own agent: `--memory` takes a markdown folder or file, a JSON/JSONL file or folder, a
SQLite database or `stancelog:<path>`; `--sessions` takes transcript files, folders or globs (generic
`{"role", "content"}` JSONL, Claude Code session files, OpenAI-style message JSON, or plain
`User: / Assistant:` text — auto-detected).

## Architecture

Entry points share one config and one pipeline. Memory and transcripts are read-only — the input
store is never modified. The pipeline writes a staged store and a report; nothing is applied until
you accept, which takes a backup first so you can restore. Full diagrams and the module map:
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

![agentdream architecture: entry points share one config and one pipeline; memory and transcripts are read-only inputs; the pipeline writes a staged store and report; accept takes a backup first.](https://raw.githubusercontent.com/mvplab-ai/agentdream/main/docs/architecture.png)

## How it works

A dream is a pipeline of small, replaceable phases:

```
load (read-only) → redact secrets → enforce size limits → consolidate → verify → insights → write new store + report
```

* **consolidate** merges duplicates / near-duplicates, replaces stale values with the latest one, and
  resolves stance reversals ("don't use A" … later "use A") keeping a one-line history;
* **verify** checks each note against what actually happened in the transcripts and corrects notes the
  evidence contradicts, citing `file:line` and quoting the lines;
* **insights** surfaces patterns that recur across sessions.

Each change is an **operation** with a stable id, so you can accept them selectively. With an LLM backend
each phase is a structured-JSON prompt whose output is validated (unknown ids and unverifiable citations
are dropped); large inputs are split into token-budgeted chunks and the per-chunk results are merged
deterministically. If the model fails, the deterministic heuristics take over.
Details, diagrams and extension points: **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

## A real run on `examples/`

Generated by `python examples/run_example.py` with the deterministic backend (no model, no network).

**Before** — `examples/memory/MEMORY.md`:

```markdown
## Navigation (Viridian City)

- The PokéCenter in Viridian City is north of the gym. (2026-01-03)
- The Poké Mart in Viridian City sells Potions and Poké Balls.

## Tooling

- Don't use Poetry for dependency management — it was too slow on CI. (2026-01-05)
- Run the test suite with `pytest -q` before committing.
- Run the tests with `pytest -q` before every commit.

## Project facts

- The API server listens on port 8080. (2025-12-01)
- Production deploys go through the `release` branch.
```

(`notes/project.md` also says *"The API server listens on port 9090. (2026-02-10)"*; the five sessions
show the agent walking north of the gym and failing, then finding the PokéCenter south of it, and the
user switching to Poetry.)

**After** — the staged store (nothing applied until you accept):

```markdown
## Navigation (Viridian City)

- The PokéCenter in Viridian City is south of the gym. (2026-03-03)
- The Poké Mart in Viridian City sells Potions and Poké Balls.

## Tooling

- Use Poetry for dependency management. (History: earlier said "Don't use Poetry for dependency management — it was too slow on CI" (2026-01-05); reversed later (examples/sessions/session-04-claude-code.jsonl:2).)
- Run the tests with `pytest -q` before every commit.

## Project facts

- Production deploys go through the `release` branch.
```

plus a new `dream-insights.md` with *"Preference (stated in 2 sessions): Always use type hints in Python
code."*, a recurring-mistake note and a converged `pytest -q` → `git commit -m` workflow.

**Report excerpt** (`report.md`):

```markdown
| Merged | Replaced | Corrected | New insights | Contradictions (temporal) | Unchanged |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 3 | 2 (2) | 3 |

### `correct-2ec6281c` — Corrected from transcript evidence: "The PokéCenter in Viridian City is south of the gym. (2026-03-03)"

- Entries: `MEMORY.md#1`
- Before: The PokéCenter in Viridian City is north of the gym. (2026-01-03)
- After: The PokéCenter in Viridian City is south of the gym. (2026-03-03)
- Why: Transcripts show 'south', not 'north' (3 supporting, 4 refuting observation(s)).
- Evidence:
  - `examples/sessions/session-01.jsonl:3` (refutes, assistant): "Walked north of the gym for 20 steps. No PokéCenter here, only tall grass."
  - `examples/sessions/session-01.jsonl:4` (refutes, assistant): "Still can't find the PokéCenter north of the gym."
  - `examples/sessions/session-02.jsonl:2` (refutes, assistant): "Walked north of the gym again. No PokéCenter here, this is a dead end."
  - `examples/sessions/session-02.jsonl:3` (refutes, assistant): "Still can't find the PokéCenter north of the gym."
  - `examples/sessions/session-03.jsonl:2` (supports, assistant): "It is just south of the gym, next to the Poké Mart."
  - `examples/sessions/session-03.jsonl:3` (supports, assistant): "Healed the whole team at the PokéCenter south of the gym."
- Confidence: 0.80 · origin: deterministic

### `replace-ef9c48dc` — Stale value replaced by the latest: "The API server listens on port 9090. (2026-02-10)"

- Entries: `MEMORY.md#6`, `notes/project.md#1`
- Before: The API server listens on port 8080. (2025-12-01)
- After: The API server listens on port 9090. (2026-02-10)
- Why: Notes give different values for the same subject; the most recent (by timestamp) wins.
```

The report also contains a unified diff of old vs. new store, and `report.json` has the same data for
machines. Operation ids are content hashes, so they are stable across re-runs of the same inputs.

## Does it help?

**On Claude Code itself.** Four coding tasks, run headless through Claude Code (`claude-sonnet-5-5`)
in copies of a project that differ only in `CLAUDE.md`: the drifted notes, the notes after a rule-based
dream, and the notes after a model dream. Three runs each, checked by code:

| Memory file | Tasks passed | Mean turns | Mean cost per task |
|---|---|---|---|
| Before the dream | 6 / 12 | 4.7 | $0.06 |
| After a rule-based dream (no model) | 9 / 12 | 3.3 | $0.05 |
| After a model dream | 12 / 12 | 5.6 | $0.06 |

With a note pointing at the wrong file, every run changed nothing the program reads and finished
anyway. The tasks were written to run into the drift, so this shows what a wrong note costs and that
a dream removes it, not how often your notes are wrong. A model dream also made one task slower by
adding a cautious insight. Reproduce it with `python evals/claude_code/run.py`.

**On the memory store.** `agentdream benchmark` builds a store where every defect is known (duplicates,
stale values, notes the transcripts refute, reversed preferences, paraphrases, plus controls that must
not change) and scores it before and after a dream. 80 facts, 130 notes, 50 sessions:

| | Before | Deterministic, all operations | Deterministic, `--safe` only | Model (`claude-cli`), all operations |
|---|---|---|---|---|
| Facts an agent would read correctly | 50/80 (62%) | 80/80 (100%) | 60/80 (75%) | 80/80 (100%) |
| ...and stated in a single note | 20/80 (25%) | 70/80 (88%) | 50/80 (62%) | 80/80 (100%) |
| Controls and unrelated notes intact | 30/30 | 30/30 | 30/30 | 30/30 |

The rule-based engine fixes everything except paraphrased duplicates (0 of 10); the model catches
those too. The notes are template-generated plain English, so treat the rule-based numbers as an upper
bound. Method, per-task and per-category results, and limits: **[docs/BENCHMARK.md](docs/BENCHMARK.md)**.

## How it compares

agentdream is a **maintenance pass** over a memory store you already have. It is not a new memory
database, and it is not an agent framework. The tools below are complementary more often than they are
alternatives.

| | What it is | Where it runs | What it does with memory | Review before write |
|---|---|---|---|---|
| **agentdream** | Sleep-time consolidation CLI / library / MCP server | Your machine (stdlib-only; optional local or API model) | Merges duplicates, replaces stale values, corrects notes from transcript evidence with citations, surfaces insights. Never mutates the input store. | Yes: dry-run default, accept / partial accept / discard / restore |
| **Anthropic Dreams** | Managed sleep-time workflow for Claude Managed Agents | Anthropic's platform | Same *shape* of workflow (memory + transcripts in, new store + report out) | Managed on the platform |
| **Letta** (formerly MemGPT) | Agent *framework* whose agents edit their own memory | Self-hosted or Letta Cloud | The agent gets tools to manage memory during a run, not a batch consolidation of an existing markdown/JSON/SQLite store | In-agent |
| **Mem0** | Memory *layer* (extract, store, retrieve) | Open-source and hosted | Adds and retrieves memories for an app; not a cited, reviewable rewrite of a store you already keep | Different model |
| **Zep** / Graphiti | Temporal knowledge-graph memory service | Self-hosted or hosted | Builds a graph of facts over interactions | Service-side |

agentdream is an independent open-source project, not affiliated with Anthropic, Letta, Mem0, or Zep.

## Configuration

Every option can come from a CLI flag, an `AGENTDREAM_*` environment variable, a project config file
(`.agentdream.toml`, or `[tool.agentdream]` in `pyproject.toml`, found by walking up from the current
directory) or a user config file (`~/.config/agentdream/config.toml`). Precedence:
**CLI > env > project file > user file > defaults**. `agentdream config` prints every effective value and
where it came from.

```toml
# .agentdream.toml — relative paths are relative to this file
backend = "ollama"
model = "llama3.1:8b"
memory = "memory"
sessions = ["~/.claude/projects/-home-me-myrepo/*.jsonl"]

[limits]
max_sessions = 20
max_chunk_tokens = 8000        # small local context window -> more, smaller chunks

[redaction]
emails = true

[hook]
every = 3                      # Claude Code hook: dream every 3 sessions
```

With that file, `agentdream dream` needs no flags at all; `AGENTDREAM_MODEL=qwen2.5:14b agentdream dream`
overrides one value. All keys, env vars and defaults: **[docs/CONFIG.md](docs/CONFIG.md)**.

## Backends

| Backend | `--backend` | Needs | Notes |
|---|---|---|---|
| Deterministic heuristics | `deterministic` (default) | nothing | Offline, free, reproducible. Rule-based duplicate / contradiction / evidence matching. Handles 5k-entry stores in seconds. |
| Anthropic Messages API | `anthropic` | `ANTHROPIC_API_KEY` | Default model `claude-sonnet-5-5`; `--model` to change. stdlib HTTP, no SDK. |
| OpenAI-compatible | `openai`, `ollama`, `lmstudio`, `vllm` | `OPENAI_API_KEY` for api.openai.com; nothing for local servers | `--base-url` for any compatible server. `ollama` → `http://localhost:11434/v1`, `lmstudio` → `:1234`. |
| Claude Code CLI | `claude-cli` | `claude` on PATH, logged in | Runs `claude -p --output-format json` — uses your Claude Code login, no API key. |

```bash
agentdream dream -m ./memory -s ./logs --backend anthropic --model claude-sonnet-5-5
agentdream dream -m ./memory -s ./logs --backend ollama --model llama3.1:8b --max-chunk-tokens 6000
agentdream dream -m ./memory -s ./logs --backend openai --base-url http://localhost:8000/v1 --model my-vllm-model
agentdream dream -m ./memory -s ./logs --backend claude-cli
```

Every LLM backend falls back to the heuristics if the model is unreachable or returns unusable output (a
warning is recorded in the report). Setup details, custom backends: **[docs/BACKENDS.md](docs/BACKENDS.md)**.

## Claude Code integration

**`/dream` skill** — the quickest way in. Claude runs a dry-run dream, walks you through the report
and applies only what you approve:

```bash
agentdream install-claude-skill                   # .claude/skills/dream/SKILL.md; --user for every project
```

Then type `/dream` in Claude Code, or ask it to clean up your memory.

**MCP server** — let Claude run dreams on request:

```bash
claude mcp add agentdream -- agentdream serve-mcp        # or: -- python -m agentdream serve-mcp
```

Tools: `dream`, `dream_status`, `show_report`, `accept`, `discard`, `list_dreams`. Ask *"dream over my
memory using the last sessions and show me the report"*; Claude calls `dream` and `show_report`, and
`accept` only once you approve.

**Auto-dream after sessions** — an opt-in Claude Code hook:

```bash
cd ~/code/myrepo
agentdream install-claude-hook --every 3          # .claude/settings.json; --local or --user for other scopes
```

After every third session (`SessionEnd`), a background dream runs over those sessions against the
project's Claude memory (`~/.claude/projects/<project>/memory/`, else `CLAUDE.md`). It is a **dry run**
by default: results land in `.agentdream/jobs/` for `agentdream list` / `show` / `accept`.

To keep memory up to date without reviewing every dream, add `--safe`: duplicate merges and stale-value
replacements are applied automatically (with a backup), while corrections and insights, which rest on a
reading of a transcript, stay staged for you. `--apply` applies everything.

```bash
agentdream install-claude-hook --every 3 --safe
```

The hook returns in ~0.1 s, never blocks or fails your session, logs to `.agentdream/hook.log`, and a lock
prevents concurrent dreams. Remove it with `agentdream uninstall-claude-hook`.
Full setup: **[docs/CLAUDE_CODE.md](docs/CLAUDE_CODE.md)**.

## Cursor integration

Add to `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "agentdream": { "command": "agentdream", "args": ["serve-mcp"] }
  }
}
```

The same six tools become available in Cursor's agent. A copy lives in
[`examples/integrations/cursor-mcp.json`](examples/integrations/cursor-mcp.json).

## GitHub Action

A composite action in
[`examples/integrations/github-action`](examples/integrations/github-action/README.md)
runs a dry-run dream and uploads `report.md` and `report.json`. The default backend is
`deterministic`, so the job needs no API key. It does not accept or pass `--apply` unless
`apply` is set to the confirmation string in that README. `contents: read` is enough;
job state goes to `jobs-dir` (default `$RUNNER_TEMP/agentdream-jobs`).
[`.github/workflows/dream-example.yml`](.github/workflows/dream-example.yml) runs it
against `examples/memory` and `examples/sessions`.

## Python API

<!-- test: run -->
```python
from agentdream import accept, dream

job = dream(memory="examples/memory", sessions=["examples/sessions"])  # dry run, deterministic
print(job.status, job.counts["corrected"], job.counts["merged"])         # completed 1 1
for op in job.operations:
    print(f"{op.id:28} {op.type:13} {op.summary[:60]}")

corrections = [op.id for op in job.operations if op.type == "correct"]
result = accept(job, only=corrections, to="reviewed-memory")  # write to a new place, not over the input
print(result.applied_ops, result.target)
```

Background jobs, status and cancellation (state survives restarts in `.agentdream/jobs/<id>/job.json`):

<!-- test: run -->
```python
from agentdream import DreamJob, dream_async

job = dream_async("examples/memory", ["examples/sessions"], instructions="focus on navigation notes")
job.wait(timeout=60)
print(job.status, job.progress)                       # completed 1.0
print(DreamJob.load(job.id).report["counts"]["insights"])
```

`dream()` accepts every config field as a keyword (`backend=`, `model=`, `max_chunk_tokens=`,
`redact_emails=`...); pass an `LLMBackend` instance as `backend` to use a custom model client, and
`pipeline=` to add or replace phases ([extension points](docs/ARCHITECTURE.md#extension-points)).

## Scheduler

```bash
agentdream schedule -m ./memory -s "./logs/*.jsonl" --idle 30m          # after 30 min without new transcript activity
agentdream schedule -m ./memory -s ./logs --every 6h                     # on an interval (when there are new sessions)
agentdream schedule -m ./memory -s ./logs --new-sessions 5 --once        # check once (cron-friendly) and exit
```

The scheduler remembers which sessions it has already dreamed over (`.agentdream/scheduler-state.json`),
so restarts don't re-dream old sessions. Defaults can live in a `[schedule]` config table.

## Safety guarantees

* **The input store is never modified by a dream.** Adapters load read-only (SQLite in `mode=ro`,
  stancelog from a private temp copy), outputs go to a separate staging directory, and adapters refuse to
  write onto their input path. The test suite hashes every input file before and after, for every adapter.
* **Dry run by default.** Nothing is applied until `accept` (or an explicit `--apply`); `accept` backs up
  the target first, refuses if the store changed since the dream (unless `--force`), and swaps the new
  store in by rename; a failure mid-accept puts the original back, and `agentdream restore JOB` undoes a
  completed accept from its backup.
* **Secrets are redacted before analysis** and again over every prompt sent to a model and every report
  quote: 30+ patterns covering provider keys (Anthropic, OpenAI, GitHub, AWS, Slack, Stripe, Google,
  Azure, …), JWTs, private keys, `password=`-style assignments, URL credentials and card numbers, base64
  blobs that decode to a secret, keys wrapped onto the next line, plus a check for long high-entropy tokens.
  Job state (`job.json`), `error.log` and the hook log are redacted too.
  Reports list counts per kind, never the secret.
* **Size limits** (sessions, bytes per transcript, total tokens, chunks per phase) truncate with a notice or
  fail clearly (`--on-limit fail`).
* **Model output is untrusted**: entry ids are normalised (`id='MEMORY.md#1'`, quotes, brackets, comma-joined
  lists, as small local models return them) and resolved only on a unique match; operations naming unknown or
  unseen entry ids are dropped, citations must
  name a real transcript line (a quote that doesn't match it is replaced by the real text and flagged), and
  corrections without verifiable evidence are downgraded to flags.
* **Atomic writes** for job state, reports and stores; job status survives crashes (a job whose worker died
  is marked failed).

How each guarantee is enforced and tested: [docs/ARCHITECTURE.md#safety-guarantees](docs/ARCHITECTURE.md#safety-guarantees).
Edge cases (empty / huge / malformed / hostile inputs, crashes, concurrency, model misbehaviour) and the
behaviour for each: **[docs/EDGE_CASES.md](docs/EDGE_CASES.md)**. How the suite is run, the pass/fail
table, and what was verified live vs mocked: **[docs/TESTING.md](docs/TESTING.md)**.

## FAQ

**How is this different from Anthropic's Dreams?** Dreams is a managed research-preview feature of Claude
Managed Agents: it runs on Anthropic's platform over memory stores that live there. agentdream is a
local, open-source tool with the same shape of workflow (memory + transcripts in, a new store + report
out, review before accepting) for memory that lives on your disk, any agent framework, and any model —
including none. It is an independent implementation, not affiliated with Anthropic.

**How does it compare to Mem0 or Letta?** Those are memory *systems*: they decide what to store while the
agent runs and serve it back (Letta also runs "sleep-time" agents inside its framework). agentdream is a
batch *maintenance* step for a store you already have — files, a JSON blob, a SQLite table — that turns
its output into a reviewable diff. They are complementary; an adapter for another store is ~40 lines.

**Will it modify my memory?** Not unless you accept. `dream` writes a new store into a staging
directory; `accept` applies it with a backup; `discard` deletes the staged copy.

**Does my data leave my machine?** Only if you choose a remote backend (`anthropic`, `openai`, or
`claude-cli`, which talks to Anthropic through your Claude Code login), and then only redacted text. The
default deterministic backend and local OpenAI-compatible servers make no network calls.

**What does it cost?** The deterministic backend is free. With an LLM, a dream makes three calls (one per
phase) when everything fits in `max_chunk_tokens`, more when it is chunked; input is roughly
*3 × memory + 2 × transcripts* tokens (consolidate sees the memory, verify and insights see both). `--max-sessions`, `--max-total-tokens` and `--max-chunks`
bound it.

**Which model should I use?** Start with `deterministic` to see what the heuristics find. For semantic
merges and subtler corrections use a strong instruction-following model that produces reliable JSON —
`claude-sonnet-5-5` is the Anthropic default; on local hardware, a 7–14B instruct model with
`--max-chunk-tokens` set to its context window works for small stores.

**What if the model hallucinates?** Proposals are validated against the real store and transcripts:
unknown entry ids and made-up citations are dropped, a quote that isn't in the cited message is replaced
by the real message text (and flagged), corrections without verifiable evidence become flags, and you still
review everything before it is applied.

**Can it run automatically?** Yes: `agentdream schedule` (idle / interval / every N sessions) or the
Claude Code hook (`install-claude-hook`). Both are dry runs unless you opt in: `--apply` applies
everything, and the hook's `--safe` applies only merges and stale-value replacements.

## Limitations

* The deterministic engine is heuristic English-language pattern matching (subjects, polarity, typed
  values like directions, numbers and on/off states). It is precise on clear-cut cases but misses
  paraphrases an LLM would catch, and it does not understand other languages.
* LLM results depend on the model; small local models can produce shallow or inconsistent proposals
  (they are validated, but may be few). Chunked runs see one part of the input per call: duplicates or
  evidence split across chunks are reconciled by the reduce step only if each chunk proposes them.
* Token counts are estimated (~4 characters per token), not computed with the model's tokenizer.
* When an operation rewrites a note that contained a redacted secret, the new note carries the
  `[REDACTED:…]` placeholder; the report warns about it.
* Markdown stores are parsed as one entry per bullet / paragraph (or per file with front matter); exotic
  layouts may be re-rendered more coarsely than you wrote them (only changed blocks are re-rendered).
* Windows is not covered by CI (the code avoids POSIX-only APIs where possible; file locking uses
  `msvcrt` there). macOS is in CI as a best-effort job (`continue-on-error`) because hosted macOS
  runners are often unavailable.

## Contributing

Issues and PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and the
[Code of Conduct](CODE_OF_CONDUCT.md). Security reports: [SECURITY.md](SECURITY.md).
The core stays stdlib-only; `pip install -e ".[dev]"`, then `python -m pytest -q`,
`ruff check src tests examples` and `mypy`.

## Credits

* Anthropic, [Dreams (Claude Managed Agents)](https://platform.claude.com/docs/en/managed-agents/dreams)
  — the workflow this project reimplements in the open, and
  [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory).
  The PokéCenter example is a nod to the *Claude Plays Pokémon* story of a wrong note corrected from logs.
* Lin, Snell, Wang, Packer, Wooders, Stoica, Gonzalez — *Sleep-time Compute: Beyond Inference Scaling at
  Test-time*, Letta / UC Berkeley, [arXiv:2504.13171](https://arxiv.org/abs/2504.13171).
* [stancelog](https://github.com/systemagents-ai/stancelog) for the contradiction-aware belief-log adapter.

MIT licensed. © 2026 systemagents-ai.
