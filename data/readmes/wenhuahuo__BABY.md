# BABY — Build Agent Benchmarks for Yourself

**English** | [中文](README-zh.md)

Turn your own real work into a benchmark — **fully local**, open source, with executable verification.

![racing](assets/baby-racing.png)

> **Background**
> As a PhD student, my daily work spans research idea development, code development, and
> document writing — and almost all of it is done with AI assistance. With flagship models
> advancing so fast, published benchmark scores alone no longer answer "how do I pick the
> right model + harness for my own work" — so I designed the BABY workflow to find the
> best llm+harness combination for myself.

BABY extracts evaluation tasks from your own material — agent chat logs ([OpenCode](https://github.com/anomalyco/opencode)/[Pi](https://github.com/earendil-works/pi) etc.),
git commit history, code projects, and documents — then
runs benchmarks against any agent harness on your machine, graded uniformly by
**executable verification** (code tests, behavior checks) or a **locked rubric judge**.
Everything — extraction, packing, gating, benching, and reporting — runs in the local
web workspace. All data stays local.

## How it works

![BABY workflow architecture](assets/baby-architecture-en.drawio.png)

```
real work ──export──> corpus/ (local normalized corpus)
    ├─ opencode sessions (SQLite)
    ├─ pi sessions (jsonl)
    ├─ git commit history
    └─ documents (md/txt/tex/rst)
corpus ──mine──> candidate list (rule prefilter + LLM classification) ── interactive selection ──> pack
pack ──> tasks/<type>/<id>/{task.toml, instruction.md, environment/snapshot.tar.gz,
                                verifier/, solution/, DRAFT_REVIEW.md}
task ──oracle gate (reference solution replay scores full + anti-leak) ──> admitted
bench ──> task × agent × model matrix ──> scoring (code: executable verification / docs: hard checks + judge)
      ──> comparison report
```

## Quick start

Requirements: Node.js 20+. Scoring/extraction uses any OpenAI-compatible API
(DeepSeek by default).

```bash
git clone https://github.com/wenhuahuo/BABY && cd BABY
cp .env.example .env          # fill in API keys (BABY_API_KEY or DEEPSEEK_API_KEY)
npm install && npm run build
node dist/cli.js start --project /path/to/project --env-file .env
# optional: --port 3210 --data-dir /private/location --no-open
```

The server binds only to `127.0.0.1`, prints and normally opens a one-time bootstrap URL,
then redirects you into the hash-routed web workspace. SQLite data and managed artifact
copies stay under `~/.baby` by default.

Ready-to-run synthetic example: `examples/synthetic-math/` — a minimal task that walks the
full "extract → pack → gate → bench → report" pipeline out of the box.

## The web workspace

![BABY local web workspace](assets/baby-web-overview.png)

The Optima-style Vue workspace covers the full workflow end to end:

- **Overview** — local-only status, workspace totals, and recent runs.
- **Projects** — register/archive local paths; import tasks; extract tasks from Git commits
  or normalized chat sessions; queue Oracle gates and confirm passed tasks.
- **Datasets** — create collections, select tasks into editable drafts, inspect versions,
  and freeze immutable versions.
- **Benchmarks** — create from a dataset version, validate readiness, and queue pending Oracles.
- **Runs / Results** — live run progress, run items and errors, retry/cancel actions, and
  completed extraction/Oracle summaries.
- **Configuration** — reusable Agent runtimes (Pi and OpenCode), tested models, named
  credential environments, and UI density. Each tested model defines its provider, model ID,
  and thinking level once; the configuration adapter maps that definition to both Agent CLIs.

### Running a benchmark

On the Benchmark page, explicitly add Agent + model pairings, then run the sequential
Task × Pairing × Repeat matrix. Every trial uses a fresh snapshot workspace, captures a
redacted local log, supports cancellation, runs the TypeScript verifier, and contributes
to per-pairing reward summaries.

### Extracting tasks

Task extraction on the Projects page uses a centrally configured Pi or OpenCode Agent +
extraction model; the effective runtime is snapshotted when queued. Extraction grants
read-only tools only — shell/edit access and project plugins are disabled.

## Four task types and scoring

| Type | Task shape | Verification | Score |
|---|---|---|---|
| `code-dev` | repo snapshot + requirement → agent modifies code | apply patch to pristine snapshot, run tests / behavior checks (F2P/P2P) | reward ∈ {0,1} + partial |
| `proposal-writing` | material snapshot + writing requirements → document | hard checks (file/field/regex) + rubric judge | 0.4·hard + 0.6·rubric |
| `idea-extraction` | literature/notes → falsifiable hypotheses | structural checks + rubric judge | same |
| `research-survey` | survey brief → survey report | coverage checks + rubric judge | same |

Judge protocol: rubric locked at task admission, evidence-anchored (every score must quote
the document source), disagreement arbitration (two runs differing by >20 points trigger a
third run and take the median), calibration set (human-sampled, kappa ≥ 0.7).

## Project structure

```
BABY/
├── src/cli.ts                   # TypeScript extraction/oracle/verification CLI & web launcher
├── src/task-extract/            # immutable sources · task drafting · snapshots · LLM contracts
├── src/task-verify/             # secure extraction · command execution · Oracle/candidate verification
├── src/baby/judge/              # hard checks · rubric judge · score composition · calibration
├── src/baby/runner/             # agent adapters · code verifier · orchestration · reports
├── web/                         # Vue 3 + TypeScript local workspace (Vite → dist/web)
├── test-ts/                     # TypeScript server, extraction, verification, and web-client tests
├── examples/synthetic-math/     # synthetic example task (no private data)
├── tests/                       # unit tests (hunk parser, etc.)
└── config/bench-config.example.json
```

## Acknowledgments

Thanks to the open-source projects and resources used by BABY:

- [OpenCode](https://github.com/anomalyco/opencode) — source of agent chat logs and one of the agents under test
- [Pi](https://github.com/earendil-works/pi) — source of agent chat logs and one of the agents under test
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — one of the agents under test
- Character design in the images: [ZipZipPipe](https://space.bilibili.com/4168597)
