# Loom

[![ci](https://github.com/nickthelegend/loom/actions/workflows/ci.yml/badge.svg)](https://github.com/nickthelegend/loom/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/@loompad/cli)](https://www.npmjs.com/package/@loompad/cli)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**The shared-memory layer for AI dev environments.** Every coding agent — Claude Code,
OpenCode, Antigravity, Codex, … — keeps its own brain in its own files. Loom makes them
**one brain**: connect your ADEs, and their memory, decisions, and context become a
single shared thread that flows from one agent to the next.

Today that means **Claude Code, Codex, OpenCode, Grok Code and Antigravity** as full
agents, each verified against a real version, plus **Kiro** driven through its own
window —
see [Supported agents](#supported-agents) for exactly how far each one goes, and
[How memory actually reaches a model](#how-memory-actually-reaches-a-model) for the
part most tools gloss over.

An agent doesn't have to be a CLI any more. A **[`model` agent](#agents-that-are-models)**
is an HTTP endpoint — any OpenAI-compatible provider, a model you pick from a list,
nothing to install — which means the cheap work can go somewhere cheap, and on a
provider's free tier it costs nothing at all. Pin one to a
**[thread](#threads-and-who-answers-in-them)** and two conversations run on two models
at once; **[ask several](#asking-several-models-at-once)** and one prompt fans out to
all of them.

And because a fleet you can't see is a fleet you can't trust, every turn, handoff and
route step is exported as **OpenTelemetry** — traces, metrics and logs — and read back
into an in-app **[Observatory](#observability)**.

Loom is **not** another IDE. It's the thin layer *between* your agents — the continuity
and memory they don't share on their own.

```
   CLAUDE.md      AGENTS.md      .antigravity/     ← each ADE's native memory
       │              │               │
       └──────────────┼───────────────┘   import
                      ▼
            ╔═══════════════════╗
            ║  ONE SHARED BRAIN ║   decisions · imported ADE memory · the thread
            ╚═════════╤═════════╝
                      │  projected on every handoff
       ┌──────────────┼───────────────┐
   Claude Code ──▶ OpenCode ──▶ Claude Code      ← baton carries the brain forward
     (plan)        (execute)      (review)
```

<p align="center">
  <img src="docs/img/workspace.png" alt="Loom workspace — one thread over every agent, with the Explorer, the composer, and the agent baton" width="100%">
  <br>
  <em>One thread over every agent — projects and chats on the left, the shared conversation in the middle, the Explorer on the right, and a composer you switch agents from without leaving the box.</em>
</p>

## One link — a teammate, their agents, your repo

Click **Invite** in a project, or run `loom invite`. Loom makes sure you're on a
team that shares this repo (it creates the team and shares the repo if you
haven't) and gives you one https link to send.

Your teammate clicks it. If they already have Loom, it opens in their Loom and
one **Join** does the rest. If they don't, the page shows one command that
installs Loom and joins:

1. **Sign in** with GitHub.
2. **Join** the team, and keep the team key the link carries.
3. **Get the repo.** Loom uses a clone they already have, or clones it. For a
   private repo, *your* Loom adds them as a collaborator the moment they join,
   and *theirs* accepts GitHub's invitation.
4. **Open it with their agents** — whichever of Codex, OpenCode, Claude Code
   and the rest are installed on their machine.
5. **Share** it with the team, so you see each other's live agents, goals and
   files.
6. **Set up your crews**, filled from their own agents.

```bash
loom invite                 # in a project: the link, a QR, and a message to paste
loom join '<link>'          # the same thing from a terminal
```

The invite is the part of the link after `#`. Browsers never send that part to
a server, including the join page's. A link works once and expires in a day.
It carries the team key, so send it the way you'd send a password.

## Quota Relay — a limit doesn't stop the work

Hit Claude's 5-hour window halfway through a task, and the work normally
stops: Claude Code parks the turn until the reset, and Codex ends it with
"try again at 3:04 PM". Loom recognises the limit and responds:

- **It hands the work on.** It stops the parked turn and passes the baton to
  the next agent, with a briefing: "claude ran out of quota; its changes are in
  the working tree, continue from them". It re-sends the same request in the
  same chat.
- **It routes new prompts.** While an agent is out, anything sent to it goes
  to the agent standing in.
- **It gives the chat back.** When the window resets, the baton returns.
- **It waits if it has to.** If no other agent is free, the request is queued
  for the moment the limit lifts.

The thread records each step ("claude hit its usage limit — codex carries on;
claude is back around 19:00"), and your phone gets a push. By default only
your other CLI agents take over, never a metered API model. Another account of
the same CLI gets first choice: an enabled, idle instance on a different account,
or a new instance using an unused registered account. Instances sharing a capped
config directory share its cooldown. Busy or disabled instances aren't cloned
around. `relay.to` sets the fallback order after these same-CLI accounts. `relay.auto: false` only reports the limit, and
`relay.handBack: false` keeps the stand-in. Limits are read from what Claude
and Codex report about their usage windows, and from the error text any CLI
gives ("usage limit", "rate limited", "quota exceeded", with "try again at…"
or "resets in…").

## Proof — is "done" true?

Agents say "all tests pass" when three of fourteen ran, or when none did. When
an agent's reply claims the tests, build, typecheck or lint pass, Loom checks
the claim three ways:

- **What it said.** The claims in its final message, including any numbers
  ("all 14 tests pass").
- **What it ran.** The commands from that turn and their exit codes. A claim
  with no test run behind it, or with a failed one, doesn't hold.
- **A clean re-run.** Loom runs your tests again in a fresh worktree containing
  exactly the agent's uncommitted changes and new files. Dependency folders
  are linked, not reinstalled. Your working tree is never touched.

The verdict goes into the thread as a card: **Verified**, **Didn't hold** (with
the reason, such as "said 14 pass; 11 did"), or **Unverified**. If a "done"
doesn't hold, your phone gets a push. Every turn card also has **Check it**,
to verify any turn on demand.

```bash
loom proof                   # check the newest turn (exits 1 if it didn't hold)
loom proof --test "npm run test:unit"
```

The test command is the one the turn itself ran and passed (a leading
`cd <project> &&` dropped), else one detected from the project (`npm test`,
`cargo test`, `go test ./...`, pytest through the project's `.venv` or
`python3`, `make test`). Override it with `proof.testCommand` in
`.loom/config.json`; `proof.auto: "off"` turns off automatic checks. A re-run
that can't start (exit 126/127, "command not found") is **unverified**, never
"the tests fail".
Pass/fail counts are read from vitest, jest, node:test, mocha, pytest, cargo,
go test, rspec and phpunit output.

## Crews — agents with roles, on one goal

A crew is a few of your agents with jobs: a **lead** who plans, **builders**, a
**reviewer**, a **tester**. You give the crew a goal. The Lead turns it into
cards, and you approve the plan. Each card is then built, reviewed (changes go
back to the same builder), and tested, in the goal's own worktree and branch.
When it's done, you apply it.

```bash
loom crew create ship       # templates: ship · fix · research · solo — seats follow your agents' roles
loom crew create ship --builders claude-code,claude-2 --reviewer codex   # or name them
loom crew goal "Add rate limiting to the public API"
loom crew approve           # or: loom crew say "smaller cards, please"
loom crew                   # cards by stage; questions a teammate asked you
loom crew apply             # merge the goal's branch into yours
```

The **Crew** tab shows the same thing. Every commit carries `Loom-Crew`,
`Loom-Goal`, `Loom-Card` and `Loom-Teammate` trailers. Phase 1 works one card
at a time; [docs/proposals/agent-teams.md](docs/proposals/agent-teams.md) has
the rest of the plan.

## Orchestra — one conductor, many agents, in parallel

Give Loom a goal and let one agent run the others. The **orchestrator** can be any
agent: Claude Code, Codex (ChatGPT), Antigravity, Grok or OpenCode.

1. It reads the repository and splits the goal into a **task graph**.
2. Loom runs every ready task **at the same time** on the **worker** agents the
   plan names. Each task gets its own thread and its own git worktree.
3. Loom merges each finished task into one integration branch.
4. The orchestrator reviews the results. It can accept them, send follow-ups,
   spawn more tasks, or finish.

```bash
loom orchestrate "add OAuth login with tests" -o claude-code -w codex,antigravity,claude-code -p 6
```

```
                 ┌──────────── orchestrator (any agent) ────────────┐
   goal ──▶ plan │  t1 → codex        t2 → antigravity    t3 → codex │ ◀── review, follow up, done
                 └──────┬──────────────────┬────────────────┬──────┘
                        ▼                  ▼                ▼  (after t1)
                   worktree t1        worktree t2      worktree t3
                        └──────── merged into loom/orchestra/<run>/main ──▶ apply to your branch
```

- **Any agent can orchestrate.** The orchestrator never runs shell commands. It
  answers in a small JSON block that Loom parses, so an agent in a sandbox or with
  no tools at all can still lead.
- **Many workers, mixed or the same kind.** Three Codex tasks and two Antigravity
  tasks run side by side as separate CLI sessions, capped by `--parallel` (1–12).
- **Real dependencies.** A task with `dependsOn` starts only after those tasks are
  merged, and it branches from a tip that already contains their work.
- **Nothing touches your branch until you say so.** All work lands on
  `loom/orchestra/<run>/main`. You merge it with `loom orchestra:apply <run>`, or
  with the **Apply** button in the app. Merge conflicts go back to the
  orchestrator, which can ask the worker to resolve them.
- **You're in the loop.** When the orchestrator needs a decision it asks, and the
  run waits for your reply (`loom orchestra:reply <run> "…"`, or the app on your
  phone). You can steer a run mid-flight the same way.
- **Everything is visible.** Every step is an `orchestra` event. The web app,
  desktop app, phone and CLI all watch the same run live, and each task's stream
  sits in its own thread. The project's budgets, quarantine and shared brain apply
  to every worker.

- **Race instead of plan.** `--race` (or the Race switch in Orchestrate) gives
  every worker the whole goal in its own worktree, with no orchestrator. The
  entrants finish side by side, each with its diff, and you keep one:
  **Pick this one** in the app, or `loom orchestra:apply <run> --task race-<agent>`.
- **A restart doesn't lose the run.** If Loom stops mid-run, the run says it
  was interrupted. **Resume** (or `loom orchestra:resume <run>`) picks up the
  tasks that were running and briefs the orchestrator again.

Workers can report progress during a turn with one command per update:

```bash
loom report --checkpoint "Implementation finished; running tests"
loom report --needs-input "Which API version should I support?"
loom report --stuck "The dependency is unavailable"
loom report --done
```

Loom supplies `LOOM_API` (daemon origin), `LOOM_PROJECT_ID`, `LOOM_RUN_ID`,
`LOOM_TASK_ID`, and a private `LOOM_REPORT_TOKEN` to each local worker process.
The token grants only report POSTs for that run. A worker without a shell can
emit the same report in its message; the transcript stays intact:

````text
```loom-report
checkpoint: Implementation finished; running tests
```
````

Use `checkpoint`, `needs_input`, `stuck`, or `done` in the fence. Reports appear
in `loom orchestra <run> --wait --progress` (with `--json`, progress is JSON lines
on stderr). `needs_input` and `stuck` are batched for five seconds into one note
to the orchestrator, even while workers are running. A busy orchestrator receives
the note on its next turn; a run waiting on a human stays paused. Checkpoints and
`done` reports do not wake it. Reports do not change task status: a `done` report
still waits for the worker's turn to end and its work to merge.

API clients POST `{ "kind": "checkpoint", "text": "…" }` to
`/api/projects/:id/orchestra/:run/tasks/:task/report`, authenticated with the run's
report token or an owner/admin bearer token. Text is limited to 4,000 characters
and required except for `done`. The response is `{ report: { at, kind, text } }`;
`at` is server time in milliseconds. GET orchestra runs include each task's
`reports` (latest 20, oldest first) and `lastReport` (`null` before any report).
An `orchestra` WS event with phase `task_report` includes `runId`, `taskId`,
`report`, and the updated `task` summary for clients to render live.

Use `agent[@model][:effort][xN]` to choose a model and build a fleet without
adding roster entries. Agent names, kinds and aliases all work; `xN` (or `×N`)
adds 1–100 instances per spec. The orchestrator takes the same syntax with count
1. Model names and effort values are passed to the agent's provider unchanged.
Omitted selections inherit the roster's options, then the provider's defaults.

```sh
loom orchestrate "implement and verify the feature" \
  -o claude-code@claude-opus-5-5 \
  -w claude-code@claude-opus-5-5x2,codex@gpt-5.6-sol:highx2,codex@gpt-6-solx2 -p 3

# Chain lines accept the same specs, including with --check:
# my-project :: [-o codex@gpt-6-sol -w codex@gpt-5.6-solx2 -p 2] implement the feature
```

Instances have distinct ids, such as `codex@gpt-5.6-sol:high#2`. Repeating a spec
adds another instance. `-p` caps concurrent tasks across the fleet, including
races. The planner sees each worker's model and can override a task with
`{"type":"spawn","agent":"codex@gpt-6-sol","title":"review","prompt":"…","model":"gpt-5.6-sol","effort":"high"}`.
These choices stay pinned through follow-ups and restarts, without changing the
roster. Model and effort overrides currently apply to local workers; `team:<kind>`
continues to use the teammate's configured agent.

`loom orchestra <run>` shows the selections. Its `--json` output includes
`orchestrator`, `workers`, `workerDetails` and `taskDetails`, while `tasks` retains
its outcome counts. For API clients, `POST /api/projects/:id/orchestra` accepts
`workers: string[]` of fleet specs and an `orchestrator` spec. Start, list and
run-detail responses retain `workers: string[]` of instance ids and add
`workerDetails: [{ id, kind, model?, effort? }]`; `orchestrator` and each entry in
`run.tasks` also carry `model?` and `effort?`. The `started` event includes
`workerDetails`, and task events and `/subagents` include task selections.
Absent selections mean provider defaults; older runs may lack `workerDetails`.
Web and phone fleet controls can use these fields without parsing instance ids.

**Ask several coding agents.** `loom compare` gives the same prompt to 2–8 entrants,
each in its own worktree, using Orchestra's race mode. Names, kinds and aliases
resolve to enabled agents in this project; `acp:gemini` selects a configured ACP
agent with the Gemini preset. Repeated specs and `xN` count toward the eight-entry
limit. Model and effort selections follow the fleet rules above.

```sh
loom compare "add OAuth login with tests" \
  -w claude-code@claude-opus-5-5,codex@gpt-5.6-sol,acp:gemini --wait
loom compare <run-id> --wait
loom compare <run-id> --keep <task-id>
```

Without `--wait`, the command returns immediately with the run id and a snapshot.
The comparison table shows each agent/model, task id, status, elapsed time, cost
and files/lines changed. `--keep` waits and applies the chosen finished task using
race apply; the other worktrees are removed, with branches retained for diff/history.
It can also accompany a new prompt with `-w`. Inspect replies in
`loom orchestra <run-id> --json` (`taskDetails`), or through the API.

For composer and phone clients, `POST /api/projects/:id/compare` accepts
`{ "prompt": "...", "entrants": ["codex@model", "acp:gemini"], "chat": "main" }`
and returns `{ run }`, with `run.compare: true` and `run.race: true`. `chat` is
optional; an existing chat keeps the run in that thread. Invalid specs, unknown
agents and counts outside 2–8 return HTTP 400 with `{ error }`. Poll
`GET /api/projects/:id/orchestra/:runId` or consume the existing `orchestra`
WebSocket events. Each task has `agent`, `kind`, `model?`, `effort?`, `status`,
`chat`, `result?`, `files?`, `costUsd?`, `startedAt?` and `finishedAt?` (Unix
milliseconds), plus `diffStat: { files, insertions, deletions }` once its turn
finishes. Unknown costs are omitted; binary files count as files with zero lines.
`GET /api/projects/:id/orchestra/:runId/tasks/:taskId/diff` returns `{ patch }`,
the unified diff against the run's base commit (capped at 400,000 characters).
“Keep this one” is `POST /api/projects/:id/orchestra/:runId/apply` with
`{ "task": "<task-id>" }`; only a `done` entrant can be picked, once per run.
Approach credit: T3 Code's multi-model threads.

Under the hood: [`src/core/orchestra.ts`](src/core/orchestra.ts).
`node scripts/verify-orchestra.mjs` runs a real orchestra against your installed
CLIs and checks the result on disk.

## Codex & GPT‑5.6

Loom is built around orchestrating **OpenAI Codex** as a first‑class agent — and in this
build every Codex turn runs **GPT‑5.6**: Codex's model, pinned in Loom's per‑project agent
config (`.loom/config.json` → `codex → model: "gpt-5.6-terra"`) at high reasoning effort.

> The slug is `gpt-5.6-terra`, not a bare `gpt-5.6` — that is the id Codex actually
> accepts, and asking for `gpt-5.6` is a 400 (`not supported when using Codex with a
> ChatGPT account`). Loom's model picker asks the CLI what it supports
> (`codex debug models`) rather than shipping a list that goes stale, which is exactly
> how this got caught.

- **Codex holds the baton like any other agent.** The adapter
  ([`src/providers/codex/adapter.ts`](src/providers/codex/adapter.ts)) keeps a warm
  `codex app-server` (JSON-RPC) per chat: it opens a thread, streams Codex's items
  (`agentMessage` / `commandExecution` / `fileChange`), its context usage and compaction,
  and **keeps the same thread across turns** (resuming it after a restart) so Codex keeps
  its own context between handoffs.
- **Codex reads and writes the shared brain.** Before a Codex turn, Loom projects the
  unified memory (imported ADE memory + decisions + the thread) into its briefing; its
  replies and memory writes land back in the one shared store. So a handoff
  *Claude Code → Codex* carries the full context, and the next agent inherits what Codex
  learned. *(Verified end‑to‑end: Codex recalled a value another agent set one turn
  earlier, and its turns emit `run_complete` + `memory_add`.)*
- **Voice, on real hardware.** The **LoomPad** is a physical ESP32‑S3 macropad, and the
  loop is: press the **Codex** key to hand Codex the baton, hold the mic and speak, hear
  the reply spoken back through the pad. It lives in this repo under
  [`hardware/orchestrator-pad/`](hardware/orchestrator-pad/README.md) — parametric CAD,
  printable STLs, the wiring diagram, the Arduino firmware and the voice backend — with
  the daemon-side proxy endpoints (`/api/loompad/health`, `/api/loompad/connect`) and the
  status pill that reads them. See [Hardware](#hardware) to print and wire one.
- **Codex as a dev agent, too.** Because Codex is a full agent, you can hand it real work
  inside Loom — `loom route ship "…"` routes *plan → Codex executes → review*, the brain
  flowing hop to hop.

In short: **GPT‑5.6, via Codex, is one of the interchangeable minds Loom keeps in sync** —
start a thread in Claude Code, hand it to Codex mid‑task, and it picks up with the whole
shared context intact.

## Observability

Loom exports its agent activity as **all three OpenTelemetry signals**, and then reads
them back into an in-app **Observatory** so you never have to leave to answer "what is
the fleet doing, and what did it cost".

**Backend-agnostic.** Loom speaks OTLP/HTTP and nothing else — no vendor SDK, no
vendor-specific code path. Point `OTEL_EXPORTER_OTLP_ENDPOINT` at a Collector, Grafana,
Jaeger, SigNoz, Honeycomb, anything with a `/v1/traces` endpoint. An ingestion key
rides in through the standard `OTEL_EXPORTER_OTLP_HEADERS`, so a new destination is a
config change and never a code change.

| Signal | What Loom puts in it |
|---|---|
| **Traces** | every turn as `gen_ai.agent.turn` (model, tokens, cost, duration), tool calls, baton handoffs, route steps, memory folds — one trace per turn |
| **Metrics** | tokens, turn duration, turns, cost, active agents, handoffs — GenAI semantic conventions |
| **Logs** | every message, tool call, edit, decision and error, correlated to the span it happened inside |

The Observatory tab renders it back: a live fleet canvas, per-agent **burn rate** and
budgets, **Span Replay** with a trace waterfall, a **Decisions** explorer, a **Logs**
view, **Time-Travel Replay** that refolds the whole run from the event log, and
**Ask** — a question about your fleet, answered from its own telemetry.

**Self-heal** closes the loop: point your monitoring's webhook at
`POST /api/webhooks/alerts` (the Alertmanager shape SigNoz, Prometheus and Grafana all
send) and a firing alert takes the named agent out of rotation until it resolves. That
is the part a dashboard can't show you — it knows the alert fired, only Loom knows the
fleet reacted.

Two rules run through all of it: **nothing is estimated**, and **absent beats invented**.
Tokens and cost are what each agent's own CLI reported; an adapter that reports tokens
but no dollar figure (codex) produces no cost datapoint rather than a zero, because
zeros are indistinguishable from real cheap turns once summed.

Off with `DO_NOT_TRACK=1`. Full details, every variable, and how to verify it's flowing:
**[docs/observability.md](docs/observability.md)**.

## Why

Every coding agent keeps its own brain. Claude Code's memory can't be read by
OpenCode; Antigravity doesn't know what you decided with Claude an hour ago. Switch
tools and you re-explain your project every time.

Other multi-agent tools answer this by keeping agents **apart** — each in its own
worktree, run in parallel, compare and merge. Loom makes the opposite bet: keep the
agents' **memory together** so work *continues* across them instead of forking.

- **One brain across every ADE** — Loom imports each agent's native memory
  (`CLAUDE.md`, `AGENTS.md`, …) into a unified store, merges it with your decisions and
  the shared thread, and hands the whole thing to whoever picks up next. `loom memory`.
- **The baton** — exactly one agent may *write* at a time; passing it *carries the context*
  (interrupt-safe, memory projected, briefing armed). Not isolation — continuation.
- **Routes** — let Loom drive the chain: `loom route ship "add dark mode"` runs
  plan → execute → review as one command, the brain flowing hop to hop; or `loom route
  auto` lets an LLM pick each next agent.
- **Every surface, one daemon** — a full-screen TUI, a web app, a desktop window, and a
  phone app (voice input, per-prompt diffs, push) — each a paired client of the same
  local daemon over your tailnet.
- **Local-first & yours** — one `npm i -g`, no account, MIT, runs headless on a server.

## Install

Requires **Node ≥ 22.5** (Loom's event log uses the built-in `node:sqlite`).

On **Windows**, install Node.js and Git for Windows, then use PowerShell or
Command Prompt. Bash and WSL are not required. From a source checkout:

```powershell
git clone https://github.com/nickthelegend/loom.git
cd loom
npm.cmd ci
npm.cmd link
loom.cmd doctor
```

For a managed source installation, run `scripts/install.ps1` in PowerShell
(it clones into `%USERPROFILE%\.loom-src`, builds, and links the CLI). Use
`loom.cmd` when PowerShell's execution policy blocks npm's `.ps1` shim.
Install agents separately: `npm.cmd i -g @openai/codex opencode-ai`, then
sign in to the agents you use. Claude Code's native Windows installer is also
detected under `%USERPROFILE%\.local\bin`.

Normal chat, shared memory, routes, Orchestra worktrees and crews use the
standard runtime on Windows. The optional **native continuity** mode
(`brain.continuity: true`) needs verified process containment. On Windows,
every harness runs inside a Job Object, and Loom checks the containment
works on this machine before it offers the mode; if the check fails, the
agent says why and stays on the standard runtime. Leave it off for Orchestra
and crews, which also run outside native continuity on other OSes.

```bash
npm install -g @loompad/cli          # → `loom` on your PATH
```

Other paths:

```bash
# one-liner from source (clones ~/.loom-src, builds, links; re-run to update)
curl -fsSL https://raw.githubusercontent.com/nickthelegend/loom/main/scripts/install.sh | bash

# straight from git
npm install -g github:nickthelegend/loom

# hackable checkout
git clone https://github.com/nickthelegend/loom.git && cd loom
npm install && npm run build && npm link
```

Then verify the setup:

```bash
loom doctor        # checks node, agents, tailscale, daemon (and what it sees vs your shell), providers, and your project
```

Surfaces, all talking to the same daemon:
- **TUI / CLI** — `loom` (default), `loom chat`, `loom send`, …
- **Desktop app (Loom Desktop)** — prebuilt for
  [**macOS**, **Linux**, and **Windows**](https://loompad.tech/#download)
  (`.dmg` · `.AppImage` · `.exe`; the macOS dmg is ad-hoc signed, so right-click → **Open**
  the first time), or build from [`desktop/`](desktop/README.md): `cd desktop && npm
  install && npm start`. Either way it opens a native window that starts the daemon and
  pairs itself.
- **Phone app (LoomPad)** — install the newest
  [Android APK](https://loompad.tech/download/android) (allow unknown sources; Google
  Play is coming), open **Loom**, and **Scan QR code** from the desktop's *Connect a phone*.
  Voice input, per-prompt diffs, push. Or build from source
  ([`app/`](app/README.md)): `cd app && npx expo install && npx expo start`.
- **Web app** — no install; `loom pair` → open the link. Same workspace in the browser.

## Fan out, retry, reap

Three moves the fleet learned for when one turn isn't the right shape:

- **Sub-agents** — a turn can fan a subtask out to a child that runs alongside
  it and **never holds the baton**: `loom spawn "audit the tests" --agent codex`.
  The child gets a narrowed briefing (its task, the project's rules, retrieval
  scoped to its own work — not the parent's thread), reports back as
  `subtask_done`, and everything it learns lands in the one brain. Capped at
  four per project, because each child is a real CLI process.
- **Retry on another agent** — when a turn fails, `loom retry <agentId>`
  re-runs the failed prompt on the agent you choose, with the failure attached
  as a briefing instead of pasted into the message: the thread shows a clean
  prompt twice, and the second agent is told what was tried and what it died of.
- **Reap a hung session** — a CLI that hangs holds `busy` forever and blocks
  every dispatch. `loom stale` names what's hung (busy past ten minutes);
  `loom reap <agentId>` interrupts, stops, respawns from config, and releases
  the baton if the corpse held it.

## Native context continuity (opt-in)

The new deterministic Brain path supports sequential switching between checked
Codex/Claude CLI profiles with scoped native sessions, protected user context,
SQLite search, source-backed checkpoints and delivery diagnostics. It requires no
embedding model or inference package. Enable **Native context continuity** in
Settings → Preferences; the legacy workflow remains the default.

Unknown CLI versions, OpenCode/bridges, attachments and parallel execution are
gated in this mode. Overflow saves a reviewable request instead of silently dropping
user intent. See [native continuity](docs/brain-continuity.md),
[current architecture](ARCHITECTURE.md) and
[remaining verification gates](docs/refactoring/BRAIN-TODO.md).

## Several sessions, one brain

`loom agents:add claude-code` a second time doesn't error — it adds
`claude-code-2`: its own session, its own context window, **the same project
brain**. Name them for their jobs (`--as reviewer --role reviewer`) and pick
per message. Memory import dedupes by file and units are project-scoped, so
what one session learns the others retrieve. One baton still rules them all:
two sessions of a kind never means two writers at once.

## Several accounts per CLI

Register each Claude Code or Codex subscription with its own config directory:

```sh
loom accounts add codex --label personal
loom accounts add codex --label work --dir ~/codex-work
loom accounts                         # IDs, paths and CLI-reported sign-in status
loom accounts login <id>              # interactive login in this terminal
loom agents:add codex --account work  # accepts an ID or a label of this kind
```

Use `claude-code` instead of `codex` for Claude subscriptions. Without `--dir`,
Loom creates a directory under `~/.loom/accounts/<id>` with mode 0700. `LOOM_HOME`
relocates this registry and its default directories. `accounts.json` stores only
`{ accounts: [{ id, kind, label, configDir }] }`; Loom never reads or copies the
credentials inside those directories. Sign-in status comes from the CLI's own
status command; `unknown` means it couldn't establish a verdict.

An agent config can set `account: "<id>"` or `options.configDir: "/absolute/path"`.
`~` is expanded; relative paths are rejected. A named account wins over
`options.configDir`, which wins over the matching `options.env` variable.
Claude gets `CLAUDE_CONFIG_DIR`, Codex gets `CODEX_HOME`. Unconfigured agents
retain their normal CLI environment. Resolved paths are saved with agents added
through Loom, so forgetting an account doesn't change their login.

Quota Relay tries these accounts before switching CLIs. Orchestra distributes
fleet copies round-robin across a kind's registered accounts: `codexx2` with two
accounts runs one worker on each. A selected account starts the rotation; a
single explicitly configured worker keeps its account. `workerDetails` records
the account ID and resolved `configDir`, alongside model and effort, for clients
and saved runs. Remote workers use their own machine's account configuration.

`options.configDir` also maps to [Grok's `GROK_HOME`](https://docs.x.ai/build/settings)
and [OpenCode's `OPENCODE_CONFIG_DIR`](https://github.com/anomalyco/opencode/issues/63129).
OpenCode's config directory alone does not isolate its stored credentials; the
accounts registry supports only Claude Code and Codex. Antigravity has no verified
config-home override here.

The daemon API is available to the owner and unscoped paired clients:

| Endpoint | Request / response |
| --- | --- |
| `GET /api/accounts` | `{ accounts: [{ id, kind, label, configDir, authed }] }`; `authed` is `true`, `false`, or `null` |
| `POST /api/accounts` | `{ kind, label, configDir? }` → `{ account: { id, kind, label, configDir } }` |
| `DELETE /api/accounts/:id` | `{ forgotten: true }`; removes only the registry entry, never the directory |
| `POST /api/accounts/:id/login` | `{ command, bin, args, env }`; displays a terminal command without running a login |

The login display command uses POSIX shell syntax (PowerShell on Windows).
Local clients can execute `bin` with `args` and merge `env` into their terminal
environment without a shell. Project agent creation accepts `account` alongside
`kind`, `role`, `options`, and `count`; successful responses contain the resolved
account ID and `options.configDir`. Project agent status exposes `account?` and
`configDir?`, and usage-limit readings are shared only within one account. No web
or phone account screens are included.

## The Browser tab

On **Loom Desktop**, external HTTP(S) pages open in an isolated browser guest,
including sites that refuse iframe embedding. Back, forward and reload use the
page’s own history; the address bar remembers visited URLs separately for each
project and pane. Cookies and site storage persist in the dedicated
`persist:loom-browser` session, separate from Loom. Permissions, downloads and
popup windows are denied. Local dev-server previews still use Loom’s proxy and
iframe; web and phone builds keep their existing iframe behavior.

Agents write Playwright specs constantly and could never watch them run. The
**Browser** tab (next to Console in the dock) lists the project's specs
(`*.spec.*`, `*.e2e.*` — never inside `node_modules`), runs one on click with
the reporter streaming line by line, records pass/fail in the Console, and on
failure stages the reporter's own words in the composer to hand back to
whichever agent should fix it. Playwright stays the project's dependency (`npx
--no-install`) — a project without it is told so plainly.

**Your dev servers live there too.** Declare them under `servers` in
`.loom/config.json` (Loom suggests them from `package.json` and waits for you
to accept) and the rail shows each one's real state: **running** means a port
answered, **starting** means the process is up but nothing is listening yet,
and **crashed** carries the exit code it died with. Start, stop and restart
from the row; click the row to point the preview at it; open its output under
the page, which is where the reason for a blank frame usually is. A server
that dies while an agent works against it says so in the thread, and every
server Loom started is stopped when the daemon goes.

From the terminal: `loom servers`, `loom servers start|stop|restart <name>`,
`loom servers logs <name> -n 100`.

**The page can talk back.** Click a server and Loom previews it through its
own proxy, which forwards everything (including the socket hot reload rides on)
and injects one small script. The **Page** pane then shows what that page
logged and what it fetched, live — and a click puts any line into the composer
as context, which is the whole point: the loop used to be *see the error,
select it, retype it*. **Pick** turns the cursor into an element picker: click
the thing that's wrong and its selector, text, size, markup and computed
styles (fonts, colours, spacing, layout) land in the composer, along with a
picture of just that element, so any agent can see what you mean. The picture
is taken at your width and colour scheme with the project's own Playwright.
Nothing about the page is rewritten; the script only reports.

**The preview itself** emulates a width (Fit / 375 / 768 / 1280, remembered per
project, scaled down when the dock is narrower), reloads itself when an agent
changes files — a toggle, on by default — and has a camera button that puts a
picture of what you're looking at into the composer. The page is another
origin, so the browser won't let it photograph itself: the daemon takes the
shot with the project's own Playwright, and a project without Playwright is
told exactly that rather than handed an empty file.

**Dark mode, on the page being previewed** — Auto / ☀ / ☾, independent of
Loom's own theme and remembered per project. No API lets one document set
another's `prefers-color-scheme`; Loom isn't outside the page, though — the
proxy served it *and* its stylesheets — so the bridge re-points the page's own
`@media (prefers-color-scheme: …)` rules, sets the UA colour-scheme, and makes
`matchMedia` answer the way you asked (firing `change`, so an app that themes
itself in JavaScript re-renders). Every rewritten rule remembers the media text
it came with, so **Auto is the page exactly as it shipped**; stylesheets Loom
doesn't serve can't be read and aren't claimed. A page you typed into the
address bar rather than previewing through Loom says so instead of offering a
switch that does nothing — and the screenshot drives a real browser, where the
scheme is honoured either way. Both conditions ride along with what you send:
*Screenshot taken at 375×812, dark mode*, and an element pick names them too.

## The workspace

On a wide screen the web app (and the desktop shell around it) is a full workspace for
*driving* agents — still not an editor: Loom shows you the context and the agents do
the writing.

```
┌───────────┬────────────────────────────┬──────────────┐
│ projects  │  Thread · Board · Brain    │  Explorer    │
│  └ chats  │                            │  Search      │
│           │  the conversation, with    │  Source ctl  │
│ New task  │  Update(n files) cards ────┼─▶ diff opens │
│ New proj  │                            │  Agents      │
│ Search    ├────────────────────────────┤              │
│           │  terminal (a real shell)   │              │
└───────────┴────────────────────────────┴──────────────┘
  live · host · baton · spend                    ← status bar
```

- **Projects + chats** in the left rail: a project holds as many conversations as you
  want, and they share one brain, one baton and one working tree. The **agents** live in
  the right panel — click one to aim your next message at it, click its role to rename
  the job (roles are free text: "architect", "the one that writes docs", anything).
- **Thread** is the shared conversation; **Brain** is the unified memory; **Board**
  is everything in flight.
- **Board** is one board with three sources — **GitHub**, **Projects**, **Linear** —
  switched from a segmented control (see [GitHub & Linear, native](#github--linear-native)).
  GitHub is four live columns (working → needs you → in review → ready to merge); cards
  come from **yours** (`+ Task`), **Loom** (which agents are running or blocked), and
  your repo's **PRs** (draft, CI failed, changes requested, approved — read through your
  own `gh`). Search issues and PRs in GitHub's own query language; **Start** hands an
  issue to an agent. Dragging your own card really moves it; dragging a PR card only moves
  where you *see* it — the badge keeps telling the truth, because a drag can't approve a
  review or turn CI green. Each card wears its agent's own logo.
- **Click any change** — an `Update(n files)` card, or a file in Source Control — and the
  diff opens to the right of the chat. It stays closed until you ask for it.
- **Explorer / Search / Source Control / Tasks** in the right panel; every column is
  drag-resizable (double-click a handle to reset).
- **Terminal** (`Ctrl` + `` ` ``) is a real terminal in the project directory — a
  proper pty, so the shell draws its own prompt and `vim`, `less`, `htop`, `^C`
  and `^Z` all behave. `node-pty` is optional: without it (Linux with no build
  toolchain) you get a pipe-backed shell instead, where `cd` and variables still
  persist and `^C` still works, driven a line at a time.
- **New task** (`n`) picks a project, a task, and **one agent — or several**, which run
  it as a pipeline, hop to hop. **New project** (`p`) adds a repo — a native folder
  picker in the desktop app — and reports which ADEs it found on the host.

### Settings, in one place

Everything about a Loom lives behind the gear in the bottom-left: **Setup** (what the
machine still needs to run agents), **Diagnostics** (`loom doctor`, run live on the
daemon), **Updates** (build rev, and how far the checkout is behind its remote),
**Preferences** (theme, the brain extractor, handoff brief style, default agent),
**Devices** (paired clients — revoke one, or pair another), and **About**.

<p align="center">
  <img src="docs/img/settings.png" alt="Loom's Settings screen — Setup, Diagnostics, Updates, Preferences, Devices, About" width="100%">
</p>


### Split: several views in one window

**⌘D** splits the window side by side, and **⌘⇧D** one above the other. Each pane is a whole
Loom view (a project, a chat, any tab), so you can follow several agents' threads at once.

- **Arranging:** drag a chat from a pane's sidebar onto another pane's edge to open it there, or
  drag a pane by its grip to move it.
- **Closing:** a pane's × closes it, and closing the last but one leaves split mode on the pane
  that's left.
- **Saving:** the layout is saved, so it's there when you come back.

Panes keep their contents when the layout changes, so splitting never reloads what you were
looking at. The approach comes from [Nuphos](https://github.com/nuphos/nuphos); the layout
model is ported from its desktop app.
## GitHub & Linear, native

Browse pull requests, issues, and **GitHub Project boards** in-app; open a worktree from
any task; review and approve PRs; and file **Linear** issues with a team selector — no
context switch, no second browser tab.

<p align="center">
  <img src="docs/img/board-projects.png" alt="A GitHub Project board rendered in Loom, items grouped by their Status column" width="100%">
  <br>
  <em>A GitHub Project (v2) board, in-app — items grouped by their Status column, each linking back to its issue or PR.</em>
</p>

- **Browse PRs, issues, and Project boards.** The **GitHub** source is the live kanban;
  the **Projects** source lists the owner's GitHub Project (v2) boards and lays a
  project's items out by Status; search takes github.com's own query language.
- **Review and approve PRs in place.** Open a PR's diff without leaving Loom and post the
  three things a reviewer does — **comment**, **request changes**, **approve**. The review
  is signed as you (through your `gh`); approve asks first, because it publishes.
- **Open a worktree from any task.** One click cuts a checked-out branch in its own
  directory, a sibling of the repo: a **PR** worktree checks the branch out — forks
  included — and an **issue** worktree cuts a fresh branch to start it. An agent can work
  a PR while your main tree stays exactly where you left it.
- **Create Linear issues with a team selector.** Pick a team, write a title and
  description, file it — the new issue's identifier comes straight back.

<p align="center">
  <img src="docs/img/board-linear.png" alt="Loom's Linear source, honest about being off until you connect it" width="100%">
  <br>
  <em>Linear is off until you connect it — and Loom tells you exactly how, because it holds no token of its own.</em>
</p>

PRs opened by Loom (orchestra delivery, crews, board cards and maintenance helpers)
are recorded in the project's `.loom/prs.json`. Every two minutes, Loom checks open
PRs with your `gh` CLI. A failed check queues “CI failed on PR #N (check): … — fix
it and push.” in the owning chat, waiting for any running turn. Failures are sent
once per check and commit; review comments are sent once per comment id, including
inline replies. These signatures survive a restart. GitHub errors back off up to
30 minutes. Tracked team PRs use this queue for CI fixes; older team goals without
a tracking record retain their existing landing loop. Merges and unmerged closes
add a status line and stop polling that PR.

Use `loom prs [--json]` to list watches and their last state, or
`loom prs:watch <number-or-url> [--chat <id-or-title>]` to attach an existing PR
(default: Main). Attaching requires the machine owner's token. A PR has one owning
chat; attaching it again to that chat is idempotent.

Clients can use these API shapes (web and phone controls are separate work):

- `GET /api/projects/:id/prs` → `{ prs: TrackedPr[] }`, including terminal history.
  Each row has `prNumber`, `repo`, `chat`, optional `agentId`, `source`
  (`delivery`, `board`, `orchestra`), `openedAt`, `state` (`OPEN`, `MERGED`, `CLOSED`),
  `url`, and optional `mergeable`, `headRefOid`, `checkedAt`. Times are epoch ms.
- `POST /api/projects/:id/chats/:chat/prs` with `{ pr: number | string }` →
  `{ pr: TrackedPr }`. Strings are positive PR numbers or HTTPS PR URLs.
- `PATCH /api/projects/:id/chats/:chat` with `{ prFeedback: "off" | "ci" | "ci+reviews" }`
  → `{ chat: ChatInfo }`. Main is supported. Default is `ci`; `off` suppresses fix
  prompts while merge/close notices still appear. `ci+reviews` also queues review
  bodies, discussion comments and inline comments. Bots and Loom's own automated
  review messages are skipped. The chat list exposes the effective setting.

**Loom holds no token of its own.** GitHub goes through your `gh` CLI; Linear reads
`LINEAR_API_KEY` from the daemon's own environment (you `export` it) and never stores,
logs, or transmits it anywhere else. No key → an honest "not connected", never a dead
form — the same bet the agent adapters make by shelling out to the CLIs you already have.

## Quickstart

```bash
cd your-project
loom init          # detects the agents installed on this machine, assigns roles
loom               # opens the TUI — a tabbed workspace (Thread · Board · Brain · Diff)
```

To start somewhere new, run `loom new "My project"` or
`loom clone https://github.com/you/repo.git --name "My project"` from any directory.
Both print the registered project id. Folders go under `~/Loom Projects` on the
daemon's machine; set `projectsRoot` to an absolute path in `~/.loom/daemon.json`
to choose another location (`LOOM_HOME` overrides `~/.loom`). Names become lowercase
slugs of up to 60 characters, and existing folders are always refused.

`loom new` creates a README, ignores `.loom/`, initializes Git and makes a first
commit, using Loom's identity if Git has none. Use `--no-git` to skip Git, or
`--agent codex@your-modelx2 --agent opencode` to choose agents and counts (1–8 per
entry; `×2` also works). Without `--agent`, Loom detects installed agents.

Remote clients can use `POST /api/projects/new` with `{ name, agents?: [{ kind,
model?, count? }], git?: boolean }`, returning `{ project, config }`, or
`POST /api/projects/clone` with `{ url, name? }`, returning HTTP 202 `{ jobId, dir }`.
Clones accept HTTPS, `git@host:path`, and SSH URLs. Poll
`GET /api/projects/jobs/:jobId` for `{ status: "cloning" | "done" | "failed",
project?, error?, progress? }`. Jobs last until daemon restart; recent completed
jobs are retained for reconnecting clients. Failed clones remove their partial
folder so the name can be retried. These endpoints require the owner token or an
unscoped paired device; guests and scoped tokens receive 403.
Their WebSockets receive `{ type: "project-job", jobId, dir, status, ... }` as
progress changes and `{ type: "projects", project }` after registration.

```
  ██      ▄████▄  ▄████▄  ▄█▄▄█▄
  ██      ██  ██  ██  ██  ██▀▀██
  ██      ██  ██  ██  ██  ██  ██
  ██████  ▀████▀  ▀████▀  ██  ██
        one thread · every agent

  1 Thread   2 Board   3 Brain   4 Diff                          ↑12  pgup/pgdn
  10:44 claude-code  here's the plan: …
   ⟶ baton: claude-code → opencode
  10:45 opencode     implementing step 1 …

 ╭──────────────────────────────────────────────╮
 │ › Ask anything… "/route ship: add dark mode" │
 │ opencode · executor ⟵ baton                  │
 ╰──────────────────────────────────────────────╯
   shift+tab view · tab agent · ctrl+p palette · esc back/interrupt
   ~ my-project · baton opencode  ➤ ship 2/3
```

The TUI is a **tabbed workspace**, not just a thread:

- **Thread** — the conversation, streamed. **`tab` shifts the active agent/IDE**
  (claude-code → opencode → back); the handoff (interrupt-safe, memory projected, briefing
  armed) happens when you hit enter, so switching is one keystroke, not a ceremony.
- **Board** — agents, your cards, issues and PRs in the four flow columns.
- **Brain** — the memory the project has learned, grouped by kind (failures first), each
  tagged with who learned it.
- **Diff** — the working tree: changed files and a colourised patch.

**`shift+tab` cycles the tabs** (or `/board`, `/brain`, `/diff`, `/thread`, or the
palette); `pgup/pgdn` scrolls the view. **`ctrl+p` opens the command palette**
(fuzzy-filtered: jump to a view, shift to any agent, launch a named route, decision,
interrupt, pair…). `esc` steps back to the thread or interrupts the running turn; `/help`
lists the slash commands.

Prefer plain line-mode (SSH, scripts)? `loom chat` is the same thread as a classic REPL,
and every action also exists as a one-shot command (`loom send`, `loom handoff`, …).

## Routing — multi-hop pipelines

Handoffs are unlimited and manual by default. **Routes** automate a chain of them:

```bash
loom route auto "add a dark-mode toggle"          # DYNAMIC: an LLM picks each hop
loom route ship "add a dark-mode toggle"          # named pipeline from config
loom route planner,executor "fix the flaky test"  # ad-hoc: roles…
loom route claude-code,opencode,claude-code "…"   # …or agent ids, any length
```

Routes started in a chat stay in that chat, including queued `auto` prompts: every
hop, question and route update appears in the original thread.

**`auto` is dynamic routing**: after every hop, a router looks at the task, the hop
history, and the last replies, then picks the next agent — or declares the task done.
The router is Claude (headless, small model, JSON out) with a deterministic
plan→execute→review rules engine as automatic fallback, so routes never stall on a
router failure. Every decision is logged with its reason
(`➤ hop 2 → opencode (plan ready — execute it)`), a hop budget caps runaways
(`--max-hops`, default 8), and `--router rules` skips the LLM entirely.

What happens per hop: interrupt-safe **handoff** → shared-memory **projection** →
**briefing** → the step's role instruction. Then:

- step finishes cleanly → Loom advances to the next agent automatically;
- the agent asks a question → the route **pauses** (`waiting_human`), you get a
  notification, `loom route --status` and the board show the question; you answer in
  the same thread (`loom send "…" --chat <chat>`) and the route **resumes by itself**;
- an agent errors or a step times out (45 min default) → the route fails loudly —
  unless the step carries an [`onFail`](#routes-that-loop-and-steps-that-skip), which
  sends it back to an earlier step instead;
- a step carrying a [condition](#routes-that-loop-and-steps-that-skip) the previous turn
  didn't meet (`reviewer?lines>200`) is **skipped**, with the numbers that decided it;
- **you always outrank the route**: any manual `handoff`/`interrupt` cancels it, and
  `loom route --abort` stops it and interrupts the in-flight turn.

`--detach` returns immediately (fire-and-notify); following with Ctrl-C also leaves the
route running server-side. One route per project at a time (the baton is one write
lock); run routes across *different* projects in parallel freely.

Define named pipelines in `.loom/config.json` — steps are roles or agent ids, and any
step can carry its own focus:

```json
"routes": {
  "ship": ["planner", "executor", "reviewer"],
  "api-only": [
    { "step": "planner",  "instruction": "design the endpoint contract only" },
    { "step": "executor", "instruction": "only touch src/api — no schema changes" },
    { "step": "reviewer", "when": "lines>200", "onFail": "executor" }
  ]
}
```

Per-step instructions are appended to the role guidance for exactly that step — the
next hop never sees them. `when` runs a step only if the previous turn met a condition
Loom measured, and `onFail` sends a failing step back to an earlier one; both are
[explained here](#routes-that-loop-and-steps-that-skip). `loom init` seeds a `ship` route automatically when it
detects at least two roles.

## Commands

| Command | What it does |
|---|---|
| `loom` | **The TUI** — tabbed workspace (Thread · Board · Brain · Diff), `shift+tab` switches view, `tab` shifts agents, `/`-commands + `ctrl+p` palette inline |
| `loom init` | Make the current directory a Loom project (auto-detects agents); in a git repo it offers to add `.loom/` to `.gitignore` (`--gitignore` / `--no-gitignore` to skip the question) |
| `loom new <name> [--agent kind[@model][xN] ...] [--no-git]` | Create and register a new folder in `projectsRoot`; print its project id |
| `loom clone <url> [--name <name>]` | Clone into `projectsRoot`, wait for registration, and print its project id |
| `loom chat` | Same thread as a plain line REPL (`/handoff`, `/interrupt`, `@agent`) |
| `loom send <text>` | One-shot message (`-a <agent>` to address someone specific). `--wait` blocks until the turn ends and prints the reply and cost (`--json` for one object, `--timeout <s>`); it exits 0 done, 1 failed, 2 the agent asked a question, 124 timed out — so a script can drive an agent without reading `.loom/log.db`. Before resuming a session of 100k+ tokens whose prompt cache has likely expired, it warns with the re-read's estimated cost; `--fresh` starts the agent's session in that chat over |
| `loom steer <text> [--chat <chat>]` | Add input to a running turn; otherwise queue it and explain why. `--agent <id>` overrides the chat binding |
| `loom handoff <agent>` | Pass the baton — interrupts, projects memory, briefs the target |
| `loom route <spec> "<task>"` | Run a pipeline (name, or `a,b,c` ids/roles); `--status` / `--abort` / `--detach` |
| `loom routes` | List named pipelines defined for this project |
| `loom interrupt` | Stop the current holder's turn (cancels an active route) |
| `loom update [--check] [--yes]` | Is there a newer Loom — and install it, in the commands it prints first |
| `loom servers [start\|stop\|restart\|logs] [name]` | The project's dev servers: real state, start/stop, and their output |
| `loom queue` | What's lined up behind the running turn — position, who takes it, why it's waiting |
| `loom queue add "<text>" [--to <agent\|orchestrate\|auto>] [--plan]` | Line a prompt up; it goes when nothing is in its way |
| `loom queue edit / to / move / rm / clear` | Rewrite one, send it to someone else, reorder it, drop it, empty the queue |
| `loom queue pause` / `loom queue resume` | Hold the queue where it is · let it run again |
| `loom queue at <when> "<text>"` / `after landed:<run>\|green:<run>` | Queue a prompt for a time, or for a goal landing / going green |
| `loom queue save <name>` / `run <name>` / `recipes` | Keep a queue as a recipe and replay it on any project |
| `loom digest [--since <hours>]` | What happened in this project while you were away |
| `loom decision <text>` | Record a decision into shared memory |
| `loom memory [import]` | The unified brain — one memory across every connected ADE |
| `loom log [-f]` | Show (or follow) the project event log |
| `loom costs` | Project spend: total + per-agent turns, $ and agent time |
| `loom agents` / `loom projects` / `loom status` | Agent roster, project board, daemon health |
| `loom providers` | Where model agents send their turns, and whether each has a key |
| `loom providers:set <id> [--key --base-url --header]` | Point Loom at a provider — the key goes to `~/.loom/providers.json` (0600) or the env, never a project |
| `loom providers:rm <id>` | Forget a provider's key and settings |
| `loom models [agentId] [--provider --free --refresh]` | With an agent: the models it reports. Without: what every configured provider has right now |
| `loom btw "<question>" [--chat c]` | Ask a private read-only side question with the parent’s agent and model |
| `loom ask "<text>" [--models a,b,c \| --free --limit n]` | One prompt to several models at once, a thread each, side by side |
| `loom up [--tailnet] [--restart]` / `loom down` / `loom daemon` | Daemon lifecycle (`--tailnet` binds to your Tailscale IP) |
| `loom pair` | QR deep link that pairs a phone (single-use token) |
| `loom clients [--revoke <id>] [--ping]` | Paired devices: list, revoke, or send a test push |
| `loom orchestra:clean [--dry-run]` | Remove orchestra worktrees left by projects that are no longer registered (`loom doctor` points them out). Finished runs' worktrees are removed by themselves after 7 days; a project on another disk keeps its worktrees beside it (`orchestra.worktreeDir` to choose) |
| `loom doctor [--json] [--fix]` | Diagnose env, daemon, binding, and project config — and where the daemon sees something different from your shell (an agent missing from its PATH, a sign-in, an API key exported only in a terminal), whether each provider answers with the daemon's key, and whether a model agent pinned to a `:free` model keeps getting 429/503 (it suggests `pool:free`). `--fix` repairs what has exactly one safe repair |
| `loom orchestrate "<goal>"` | One orchestrator plans, many workers build in parallel worktrees (`-o`, `-w`, `-p`, `--no-watch`) |
| `loom orchestrate --plan "<goal>"` | Plan mode: the plan and each task's spec land as markdown under `plans/<run>/` for any agent to pick up |
| `loom orchestra [run] [--watch]` | Orchestra runs in this project, or one run's task graph live |
| `loom orchestra:reply / :apply / :abort / :cleanup <run>` | Answer or steer the orchestrator · merge the run into your branch (a race: `--task <entrant>`) · stop it · remove its worktrees |
| `loom orchestrate --race "<goal>" -w a,b` | Race: each agent takes the whole goal in its own worktree, and you keep the one you like |
| `loom orchestra:resume <run>` | Carry on a run Loom stopped by restarting |
| `loom stats` | Today across every project: turns, how many failed, the time and the spend |
| `loom export [--chat <id\|title>] [--out file]` | A chat as Markdown: prompts, replies, tool summaries and turn footers |
| `loom backup [--out file]` | Everything Loom knows in one archive: `~/.loom` and every project's `.loom` (logs copied as consistent snapshots) |
| `loom completion zsh\|bash` | Shell completion: `loom completion zsh >> ~/.zshrc` |
| `loom hub [--host --port --secret]` | Run a self-hosted Team Hub for your team |
| `loom invite` / `loom join <link>` | One link: a teammate joins the team and gets this repo, their agents and your crews |
| `loom crew [status\|create\|goal\|say\|approve\|stop\|resume\|apply\|diff\|remove]` | Crews: agents with roles (lead, builders, reviewer, tester) working one goal |
| `loom team [status\|signin\|create\|invite\|join\|share\|unshare\|brain\|landing\|doctor\|adopt\|deploys\|release-notes\|webhook\|remove\|leave]` | Loom Teams: see teammates' live agents and goals; the shared team brain; landing goal PRs; GitHub webhooks; membership and key rotation |
| `loom land [runId]` | Land a goal's PR: fresh main in, fast tests, push, merge when GitHub's rules pass |
| `loom runner [status\|pair\|join\|start\|stop\|token\|doctor\|install\|revoke\|goal\|move\|back\|jobs]` | Runners: your always-on Loom that takes goals while you're away |
| `loom cloud [status\|enable\|disable\|rotate]` | Loom Cloud relay: reach this daemon from any network, end-to-end encrypted |
| `loom spawn "<task>"` | Fan a subtask out to a child agent — the parent keeps the baton |
| `loom review <agents…> [--file f \| --diff \| --text "…"] [--focus "…"]` | Several agents review the same change at once — **read-only** (their own plan mode where they have one), **nobody takes the baton**, so nobody is asked to hand off for a read. It waits and prints every finding in one list, worst first; two reviewers on the same line show as one finding they agree on. The same card lands in the app with Accept / Reject on each finding. `--diff` (the uncommitted changes) is the default; `--no-wait`, `--json`. A reviewer that takes longer than `review.timeoutMin` (default 15) is stopped and left out, so the others' findings still land |
| `loom council "<goal>" --planner <id> --reviewers <ids>` | One planner, several reviewers, seven stages in one chat (and one card in the app that fills in as they go): the **planner plans** (no edits) → the **reviewers backtest the plan** in parallel, read-only → the **planner accepts or rejects** each finding, recorded as decisions → **only the planner builds** → **Proof** re-runs the tests in a clean checkout → the **reviewers forward-test the diff** → the **planner fixes** what it agrees with, and Proof again. `loom council:status [id]`, `loom council:stop` |
| `loom review:accept <id…>` / `loom review:reject <id…> [--note why]` | Decide on review findings — an accepted one becomes a project decision every agent is briefed with. `loom reviews [id]` lists them |
| `loom subtasks` | Subtasks running right now |
| `loom agents:add <kind> [--as name] [--role r]` | Add an agent session — repeat for a second session of the same kind, same brain |
| `loom agents:add model --model <id> [--tools --write --run "npm test"]` | An agent that *is* a model: no CLI, and what it may read, write or run |
| `loom agents:rm <id>` / `loom agents:available` | Remove a session · what this machine can drive and how many are here |
| `loom watch [--all] [--json]` | Tail a project's events live — turns, handoffs, memory, subtasks |
| `loom retry <agentId>` | Re-run the last failed turn on a different agent, failure attached |
| `loom stale` / `loom reap <agentId>` | Sessions that look hung · respawn one fresh (baton released) |
| `loom budgets` / `loom budget <id> [usd]` | Daily USD caps: measured spend vs cap · set or clear one |
| `loom brain:search "<query>" [--explain]` | Retrieval exactly as a briefing sees it — the score, and the arithmetic behind it |
| `loom brain:forget <memoryId>` | Drop one unit from the project's memory |
| `loom brain:export [file]` / `brain:import <file>` | The project's memory as a portable file — import dedupes |
| `loom brain:conflicts` | Units that likely contradict each other, with the signal that tripped each |
| `loom snapshot [file]` / `loom restore <file>` | Checkpoint brain+board+config · bring one back (brain merges) |
| `loom rewind [checkpoint]` | Points the working tree can go back to · put the files back to one |
| `loom routes:save <name> <steps...>` / `routes:rm` | Define a named pipeline, validated against the roster · remove one |
| `loom task "<title>"` / `loom tasks` | Put a card on the board (`--agent`, `--blocked-by`) · list yours |
| `loom specs` / `loom specs:run <file>` | The project's Playwright specs · run one through the daemon |
| `loom mcp:health` | Each MCP server's live state from the background poll |
| `loom costs --series [days]` | The spend ledger day by day, per agent |
| `loom open` / `loom version` | Open this project in the web app · what's installed |
| `loom rename <name>` / `loom find <query>` | Rename the project (id never moves) · search the thread |

## Supported agents

| Agent | Tier | Transport | Status |
|---|---|---|---|
| Claude Code | adapter (full-duplex) | Claude Agent SDK driving the installed `claude` (stream-json control protocol), resume by session, briefing appended to Claude Code's system prompt | ✅ verified against 2.1.278 with SDK 0.3.283 (2026-09-28) |
| Codex | adapter (full-duplex) | `codex app-server` JSON-RPC, `thread/resume`; found on PATH **or inside Codex.app** | ✅ verified against codex-cli 0.153.4 (2026-09-28) |
| OpenCode | adapter (full-duplex) | `opencode serve` HTTP + SSE (`/prompt`, `/interrupt`, `/event`) | ✅ verified against 1.17.20; re-verified 1.18.31 (2026-09-18) |
| Grok Code | adapter (full-duplex) | `grok -p --output-format json`, `-r <session>` | 🔶 verified against 0.2.54 — **answers only, no tool or edit events** (see below) |
| Antigravity | adapter (full-duplex) | `agy -p` headless, `--conversation <id>` to resume | ✅ verified against agy 1.1.6; re-verified 1.2.6 (2026-09-18) |
| Cursor | — | `cursor-agent --print` | 🔜 coming soon |
| **Model (API)** | adapter (full-duplex) | `POST /v1/chat/completions`, streamed — any OpenAI-compatible provider | ✅ no CLI to install; tools are read-only unless you allow more (see [below](#agents-that-are-models)) |
| Echo | adapter (demo/tests) | in-process | ✅ |
| Kiro | **bridge** (driveable) | Chromium debug port — types into the real chat panel and reads the panel back | 🔶 mechanism verified; its selectors are not (see below) |

**Context and limits.** For Claude Code and Codex, the composer shows the chosen
agent's context in use against its model's window, shows **compacting…** while the
harness compacts (with a "compacted its context · 180k → 12k tokens" line in the
thread when it's done), and calls out a usage-limit window once it passes 80%. Hover
for every window and when it resets.

> The Claude Agent SDK package carries a platform build of Claude Code as an
> optional dependency (about 215 MB installed on macOS arm64). Loom never runs it: it always points
> the SDK at your own `claude`. Installing with `--omit=optional` skips it.

Four of those need their asterisks spelled out, because the table row is
shorter than the truth:

**Codex reports tokens, never money.** Its `turn.completed` carries
`input_tokens` / `output_tokens` and no dollar figure, so Loom shows tokens and
no cost for Codex turns. A USD number derived from a price table we'd have to
keep current is fiction with a decimal point in it.

**Grok can't show you its steps.** `--output-format streaming-json` sounds like
it would help and doesn't: it emits `thought` and `text` deltas and a final
`end`, with no tool calls and no file edits — not even when the turn
demonstrably ran a shell command and wrote a file. So a Grok turn in the thread
is what it said, and `git status` is what it did. Inferring the edits by diffing
the tree would put guesses in the event log dressed as facts. Its permission
mode also defaults to `bypassPermissions`, because headless with no TTY to ask,
every other mode ends the turn `Cancelled` having written nothing.

**Antigravity used to be a bridge, and isn't any more.** Loom drove the IDE's
chat panel over the DevTools protocol: it needed the app open with a debugging
port, it could only watch, and it could never hold the baton. `agy` does the
whole turn headless, so Antigravity is a full agent and the GUI stopped being a
dependency. It reports no dollar cost — the CLI hands us none — so its turns
show a model and a duration and honestly nothing else. The CDP bridge is still
in the tree and still builds, so projects that name it still open; it just isn't
offered any more.

**Kiro is driven, not routed.** It's an Electron app with no
API; Loom connects to the debugging port, finds the chat box, types through the
input pipeline and reads back what the panel gained — the approach
[antigravity_phone_chat](https://github.com/krishnakanthb13/antigravity_phone_chat)
takes, and for the same reason: never touch the provider APIs, drive the app
that's already signed in. Launch it with
`--remote-debugging-port=9222` first.

The driver refuses more than it accepts, on purpose. Kiro is VS Code
family and Monaco — the editor holding your source file — is a
`contenteditable`. Anything under `.monaco-editor` is never a candidate, a
candidate must be labelled like a chat box, and zero-or-several matches is a
refusal that names the fix (`options.selectors.composer`). Typing a prompt into
your code and pressing Enter is not a mistake an error message repairs.

What's verified is the mechanism, against a real Chromium. What is **not**
verified is Kiro's actual chat DOM: it shows no chat panel until you open one,
so there was no composer to read the selectors from. Reachable and driveable are
separate questions, and Loom answers both — an app with no chat panel open
replies to CDP cheerfully and reports
`driveable: false — no chat box on screen`.

**Adapters** run a turn to completion headless and may hold the baton. **Bridges** only observe and receive shared-memory
projections — they never hold the write lock. That's a design decision, not a gap: GUI
agents without a stable API can't be trusted with interrupt-safe writes. See
[docs/integration-notes.md](docs/integration-notes.md) for the verified surfaces.

## Any ACP agent

One agent kind, `acp`, drives any agent that speaks the
[Agent Client Protocol](https://agentclientprotocol.com) over stdio. That includes Claude Code
and Codex through their ACP adapters, Gemini CLI, OpenCode and Grok.

```bash
loom agents:add acp --preset gemini --as gemini     # gemini --experimental-acp
loom agents:add acp --preset claude --as claude-acp # npx @agentclientprotocol/claude-agent-acp
loom agents:add acp --cmd "my-agent --acp" --as mine
```

- **Sessions:** each Loom chat is one ACP session, and it resumes with `session/load` when the agent supports it.
- **MCP servers:** enabled project servers that pass Loom's health filtering are sent when a session is created or loaded. Stdio servers include their arguments and environment; HTTP and SSE servers include their headers and are sent only when the agent advertises support for that transport.
- **What you see:** the agent's thoughts, its plan, each tool call and the diffs it reports show
  up in the thread like any other agent's. Diffs appear as file edits.
- **Permissions are Loom's:**
  - Bypass picks the agent's own "allow" option.
  - Auto runs Loom's Auto policy on the call.
  - Always ask puts each request on an approval card in Loom and on your phone.
  - A request that fails or is interrupted is answered "cancelled", never allowed.

### Several agents on one model

Add up to eight sessions at once, each pinned to the same model:

```sh
loom agents:add claude-code --model claude-opus-5-5 --count 3 --as opus
loom orchestrate "add OAuth login with tests" -o claude-code -w opus,opus-2,opus-3
```

This creates `opus`, `opus-2`, and `opus-3`, each with `options.model` set to
`claude-opus-5-5`. Names already in use get the next free suffix. Omit `--as`
to use the agent kind as the base name. `--model` works with any kind that
accepts a model, including `claude-code`, `codex`, `opencode`, `grok-code`,
`model`, and `acp`. In the app, Add agent offers a model field with suggestions
and a count from 1–8; Orchestra's **+ model** uses the same picker.

## Agents that are models

Every other agent in Loom wraps a CLI. A `model` agent is an HTTP endpoint:

```sh
loom providers:set openrouter --key sk-…          # or $OPENROUTER_API_KEY
loom models --free                                 # what costs nothing today
loom agents:add model --as cheap --role reviewer \
  --model "google/gemma-4-31b-it:free" --tools
```

It streams into the thread like any other agent, shows reasoning as reasoning,
reports its token counts, and holds the baton. Out of the box it is a thinker
rather than an editor — planning, reviewing, summarising, answering, routing,
which is most of what a fleet does between edits and what free quota is very
happy to pay for — and it becomes an editor only when you say so, below.

**It can read the project, if you let it.** `--tools` adds `read_file`,
`list_files` and `search` — read-only, inside the project, with `.git` and
`.loom` off limits and every path proven contained before anything opens it.
Each call shows in the thread, and the loop is bounded at eight hops.

**And write, if you say so.** With `--tools` already on, `--write` adds
`write_file` and `--run "npm test"` adds `run` with that allow-list. (Either
without `--tools` is refused — they're the writing half of it, not a
replacement for it.) Every write and every command is a card you
allow or deny first:

> **write_file** — write src/app.ts: 40 lines (replacing 12) — fix the port
> &nbsp;&nbsp;[Allow] [Deny]

It asks in `auto` as well as `ask`, which is stricter than the CLI mapping and
on purpose: a CLI in your roster is one you installed and signed into, and a
model agent is a name you picked off a provider's list an hour ago. `bypass`
is the only mode that doesn't ask. With nobody to ask, the answer is no.

The allow-list is a prefix match on whole commands and there is no shell — so
`npm test` permits `npm test --watch` and refuses `npm testify`,
`npm test; rm -rf ~`, backticks, pipes and redirection — and a tool is only
offered to the model when it can actually be used.

**Providers Loom knows by name** — and anything else that speaks
`/v1/chat/completions` works with a base URL:

| provider | base URL | free tier |
|---|---|---|
| `openrouter` | `https://openrouter.ai/api` | models whose id ends `:free` |
| `agentrouter` | `https://agentrouter.org` | all of it — but see the note below |
| `groq` | `https://api.groq.com/openai` | — |
| `openai` | `https://api.openai.com` | — |
| `ollama` | `http://127.0.0.1:11434` | local, no key |
| *anything* | `loom providers:set mine --base-url …` | whatever you tell it |

**Keys are never project config.** `.loom/config.json` names a provider;
the key lives in the environment or in `~/.loom/providers.json` (mode 0600),
and nothing — no route, no log, no listing — hands it back. You get the last
four characters, which is enough to tell two keys apart.

**A fallback chain, for when the free pool is dry:**

```json
{ "id": "cheap", "kind": "model", "role": "reviewer",
  "options": { "provider": "openrouter",
               "model": "google/gemma-4-31b-it:free",
               "fallbacks": ["qwen/qwen3.8-27b:free"],
               "tools": true } }
```

**Refusals are read, not guessed at.** A dry free pool (402) or a rate limit
(429) moves to the next model in `fallbacks` and says so once; a model name
that doesn't exist (503) stops, because falling back would hide the typo. And
a provider that rejects *Loom* rather than your key says exactly that —
AgentRouter, for one, only accepts clients it recognises, which is a thing to
ask them about rather than a key to go and regenerate.

## Threads, and who answers in them

A thread can name its own agent. It then answers there whatever the baton is
doing elsewhere, which is what lets two threads talk to two agents at once —
one planning on a free model, one editing with Claude Code, neither waiting for
the other.

Pinning does **not** take the baton. The baton is the write lock for work that
touches the repository; a conversation doesn't need it, and taking it would
stop whatever is actually working. The main thread still follows the baton,
because that's what makes it the main thread.

A thread may pin a **model** and, where supported, **reasoning effort**, without
changing the agent's defaults or restarting its current turn. Claude Code and
Codex receive the selection through their native provider sessions. ACP uses
`session/set_model` when the session advertises models. Other adapters keep a
separate warm instance per agent, model and effort; turns on the same agent
still run in order. Native state stays separate between those model instances.

```sh
loom chat:create "Review" --agent codex --model gpt-5.4 --effort high
loom chat:agent "Review" codex --model gpt-5.4 --effort low
loom chat:agent "Review" codex          # restore the agent's model/effort defaults
loom chat:agent "Review" --clear        # follow the baton again
loom send --chat "Review" "Review the changes"
```

The API returns `{ "chat": ChatInfo }`, and chat listing includes `agentId`,
`model`, and `effort`. Create with `POST /api/projects/:id/chats` and a body such
as `{ "title": "Review", "agentId": "codex", "model": "gpt-5.4", "effort": "high" }`.
Replace the selection with `POST /api/projects/:id/chats/:chatId/agent` and
`{ "agentId": "codex", "model": "gpt-5.4", "effort": "low" }`. This replaces all
three fields: omitted or empty model/effort values inherit the agent defaults;
`{ "agentId": null }` clears all three. Model and effort require a bound agent.
Main continues to follow the baton and cannot be pinned. An explicit send to
another agent uses that agent's defaults. A change leaves an in-flight answer
alone; queued messages retain the selection captured when submitted.

Use `loom send "Review the changes" --model gpt-5.4 --effort high` to override
the model or effort for just one message. The API accepts the same optional
`model` and `effort` strings in `POST /api/projects/:id/messages`, alongside
`text`, `chat`, and `agentId`. For example:
`{ "text": "Review the changes", "chat": "<chat-id>", "effort": "high" }`.
Each omitted or blank field inherits the chat selection (or the agent default
when the chat does not bind that agent). Values are trimmed and validated just
like chat bindings; invalid selections return HTTP 400. These overrides never
change the stored chat or agent defaults. Queued message items carry `model`
and `effort`, with `null` meaning agent defaults, so later chat edits do not
change a waiting message's selection. This also survives a daemon restart.

Effort is supported by Claude Code, Codex, and Antigravity CLI (and the test
`echo` adapter). Unsupported effort choices are rejected. Model IDs are
provider-specific strings (up to 200 characters). For an ACP agent without
session model selection, configure `options.modelFlag` with its documented
startup flag, for example `"--model"`, to use separate model processes. Without
either mechanism, a requested model fails before the prompt is sent.

Approach credit: [T3 Code](https://github.com/pingdotgg/t3code) (MIT), for
per-thread provider and model selection. Web and phone picker updates are
separate from this API and CLI support.

## Move a chat to another machine

`loom chat:move <chat> --to <runner>` accepts a chat id or title and a runner's
exact label or device id. Pair the destination with `loom runner pair` / `join`
first, and share the project with the team. `--no-wait` returns busy if the chat
is running; `--json` prints `{ chat, jobId }`. A teammate's runner must be shared
and the repo's reviewed `loom.team.json` must allow `runners.shared`.

The owner-only API is `POST /api/projects/:id/chats/:chat/move` with
`{ "to": "runnerDeviceId", "wait": true }` (`wait` defaults to true). It waits for
the active turn, then returns `{ chat: ChatInfo, jobId }` once the sealed job is
queued. Queued prompts must be sent or removed first. A competing move or send
returns 409 while the move waits. `GET /api/projects/:id/chats` includes
`movedTo: { device, name, at, jobId }` on the source, whose further sends return
409 `moved to <name>`. `at` is epoch milliseconds.

Poll `GET /api/projects/:id/team/runners` for the job's `state` and `error`;
a completed `chat_move` job includes `result: { projectId, chatId }` identifying
the chat on the destination daemon. A registered project with the same repo is used;
otherwise the runner keeps a new clone as a normal project. The transfer does
not copy uncommitted files. Bring a conversation back by moving the destination
chat to a runner on the original machine; the old source remains readable.

History and instructions travel encrypted to the team. Imported message/tool
events retain text, authors and timestamps, with
`payload.imported: { jobId, eventId, chat }` identifying their source. Payloads
are capped at 2 MiB before sealing: raw tool output is omitted first, then oldest
events, with the omitted-event count on the target's `chat_imported` status.
The target selects its own agent of the same kind, model and effort when
available. Native cursors are sent only to the same owner's machine. A locally
known provider session from a moved chat can resume; otherwise the next turn
gets a one-shot history briefing, which survives daemon restarts. Native session
files and agent credentials are never transferred. Web and phone menus can use
this API; they are not included in this change.

## Side questions

`loom btw "why this approach?" [--chat c]` asks the parent chat's agent and model
without interrupting its work. It prints the side reply and closes the side session.
Main follows the baton; a pinned chat uses its bound agent and model. The selection
is captured when the side opens. Side messages stay in daemon memory, never enter
the project event log or brain, and disappear when closed or when the daemon stops.

Claude and Codex fork the parent's native session in a separate process, in plan
mode with read-only permissions. If there is no native session, or the provider
cannot fork it, the last twenty parent messages supply context instead. Model
endpoint agents use that context with read tools only; echo supports the same path
for testing. Adapters without enforceable read-only execution (including OpenCode)
return an explicit error. Side questions can run while the parent's turn is busy.

The API is ready for web and phone drawers; their screens are separate work:

- `POST /api/projects/:id/chats/:chatId/side` with `{ "text": "question" }`
  returns `{ "sideId": "…" }` immediately. Posting again continues the open drawer.
  An optional `sideId` targets that exact side and returns 404 if it was closed.
  Concurrent sends to one side return 409; empty/non-string text or text over
  32,000 characters returns 400.
- `GET /api/projects/:id/chats/:chatId/side/:sideId` returns
  `{ "messages": [{ "role": "user", "text": "question", "at": 123 }], "busy": true }`.
  Replies have role `agent`; `at` is epoch milliseconds. A failed turn sets
  `busy: false` and an `error` string. Close a failed side before reopening it.
- `DELETE` at the same URL cancels and forgets the side, returning `{ "deleted": true }`.
- WebSocket frames have `{ type: "side", projectId, chat, sideId }` plus one of
  `delta` (text), `message` (the complete message), or `done: true` (optionally `error`).
  A completed agent message replaces the accumulated deltas for that turn. GET is
  the authoritative snapshot after reconnecting; side frames are not log events.

Only owners and unscoped devices can access side HTTP endpoints or receive their
frames; shared-chat guests and project-scoped devices cannot. “Bring back” should
quote the selected answer into the main composer locally. It enters the main
conversation only when the person submits that composer through the normal API.

## Asking several models at once

```sh
loom ask --free --limit 3 "is this migration reversible?"
loom ask --models "openrouter/qwen/qwen3.8-27b:free,ollama/llama3" "review this approach"
```

In the app it's **More → Ask several models…** in the composer: tick the
models (free ones are listed first), and what's in the box goes to each.

One prompt, one thread per model, all at the same time, each thread named
after the model that answered in it. With free quota this costs what asking
one model costs, and picking the good answer takes a person ten seconds.

The agents that run are transient — five asks don't leave five agents in the
roster — and one model failing leaves its error in its own thread while the
others carry on.

## The brain, sharpened

Five retrieval behaviours worth knowing, all inspectable with `explain`:

- **Recency decay** — a unit's match decays toward a floor (7-day half-life,
  never below 0.55): an equal match, fresher, wins; a strong old constraint
  still beats a weak new fact. Age tips ties, it never erases history.
- **A fuzzy channel** — hashed character-trigram vectors catch typos and
  morphology (`sqllite databse` finds `sqlite database`; `deploying` finds
  `deployment`). Honestly **not** synonymy: that needs a model, which is the
  next one.
- **A semantic channel, opt-in** (`brain.semantic`, or Settings → Brain) —
  all-MiniLM-L6-v2 embeddings, so *how does login work* reaches a note about
  Supabase JWKS. Measured on `test/brain-recall.test.ts`, recall@5 goes
  **0.50 → 1.00** on queries that share no word with the memory they want,
  **0.80 → 1.00** across word forms, and stays **1.00** on the literal ones —
  it costs nothing where the lexical channels already worked. It is **not** a
  dependency: the 23MB model needs a ~470MB ONNX runtime, so Loom asks you to
  install it (`npm i -g @huggingface/transformers`) and works exactly as
  before if you don't. Scored relative to the best hit in the query, like
  BM25, because this model's absolute similarities don't mean enough to
  threshold.
- **Contradiction flags** — `loom brain:conflicts` scans same-kind units for
  negation pairs (`always`/`never` on one topic) and same-topic-divergent
  decisions. Every flag names the signal that tripped it, so you can judge the
  judge. Resolution stays human.
- **Portability** — `loom brain:export` writes what the project knows to a
  plain file; `brain:import` brings one in, deduped by hash, so the same file
  twice reports *known* rather than minting duplicates. `loom snapshot` /
  `restore` widen that to brain+board+config — restore **merges** the brain,
  because what the project learned since the snapshot should survive it.

## How memory actually reaches a model

Worth being precise about, because this is the whole premise and it has a soft edge.

Loom **reliably builds** the shared brain (every ADE's imported memory + your decisions
+ the thread) and **reliably writes** it to `.loom/memory/<agent>.md` on every handoff.
That part is solid and tested.

Getting it into the model's context is a different problem, and it depends on the agent:

| Agent | How the brain arrives | Strength |
|---|---|---|
| Claude Code | briefing appended to Claude Code's system prompt — the model *always* sees a summary (recent decisions + messages) plus a pointer to `.loom/memory/claude-code.md`, which it can Read | **strong** — the summary is guaranteed; the full file is one tool-call away |
| Grok Code | the briefing rides in `--rules`, Grok's real system-prompt channel, so `-p` stays your clean prompt | **strong** — `--rules` is a genuine system channel, not text in the turn |
| Codex | no per-turn system channel in `codex app-server`, so the briefing rides in front of your prompt — **framed** as an unmissable `LOOM SESSION MEMORY — authoritative, read first` block | **reliable** — one prompt either way, but framed so it can't be mistaken for chatter |
| OpenCode | no per-prompt system field on `/prompt`, so the same **framed** block is prepended to your prompt | **reliable** — delivered as an authoritative block, not loose text |
| Antigravity, Kiro | nothing tells them the file exists — Loom types into their chat box, which is not a system prompt | **none** — a human has to open it |

So: the **summary always lands**; the **full brain is an invitation**. An agent that
ignores the pointer works from the summary alone. If you need something remembered for
certain, put it in a decision (`loom decision`) — decisions ride in the briefing itself.
There's an opt-in eval (`LOOM_TEST_REAL=1`) that checks a real model actually *uses* an
injected brief, and declines rather than invents when the brief is silent.

Memory also flows **one way**. Loom reads `CLAUDE.md` / `AGENTS.md` and never writes
them, so your ADE's own memory files stay yours. And the import is a **merge, not a
parse**: files are read, capped at 8000 chars, and concatenated under headers. Claude
Code's `@path` imports are **not followed** — a `CLAUDE.md` that is mostly `@` pointers
imports the pointers, not what they point at.

The brain also **learns on its own**. After each turn a small Claude reads what changed
and files what's worth keeping as typed memory *units* — a constraint, a decision, a
convention, a fact, a failure — reconciled on write (add / update / forget, never a
growing blob), the approach [mem0](https://github.com/mem0ai/mem0) pioneered, adapted to
Loom's event log. Every unit's evidence is verified against the turn before it's kept, so
the brain doesn't remember things that were never said. Retrieval is hybrid too — exact
entity matches (file paths, symbols, error codes) unioned with BM25 over the text and a
trigram channel for typos and word forms, and [a real embedding
channel](#the-brain-sharpened) if you turn one on — with failures and constraints biased
to the top of the brief, because getting burned twice is worse than missing a detail.

The brain is the **project's**, not each agent's: a fact one agent learns is scoped to the
chat, not walled off to whoever happened to learn it, so it reaches whichever agent takes
the baton next. (The [`brain-shared` test](test/brain-shared.test.ts) makes this concrete —
five agents each learn one fact, and every other agent's brief then carries all five.) The
**Brain tab** — and `loom tui`'s **Brain** view — show exactly what it has learned; toggle
the extractor off per project in Settings.

<p align="center">
  <img src="docs/img/brain.png" alt="Loom's Brain tab — the memory units it has learned, by kind" width="100%">
  <br>
  <em>The Brain tab — learned memory units, grouped by kind, each traceable to the turn it came from.</em>
</p>

## How it works

- **Event log** (`.loom/log.db`, SQLite via `node:sqlite`, JSONL fallback) — every
  message, tool call, file edit, decision, and handoff, appended in order. The log *is*
  the project's memory; everything else is a view of it.
- **Projection** — on handoff, Loom distills the log into
  `.loom/memory/<agent>.md` (persistent, namespaced) and arms a short one-shot briefing
  injected with the target's next turn (system-prompt append for Claude Code, delimited
  preamble for OpenCode). Two renderers behind one interface:
  - **template** (default) — deterministic, instant, free;
  - **llm** — a small Claude model distills the recent log into a dense doc
    (mission / current state / decisions / risks / next moves). Opt in per project:
    `"projection": { "mode": "llm", "model": "haiku" }`. Any failure or timeout falls
    back to the template — a broken Claude never blocks a handoff. Bridges always get
    template views (no N×LLM waste per hop).
- **Baton** — persisted per project (`.loom/state.json`). Messages route to the holder;
  addressing a non-holder returns `409 not_holder` and the surface asks you to confirm a
  handoff. Ghost holders (agent removed from config) self-heal. Every handoff snapshots
  the outgoing agent's working-tree state (dirty flag + `git status`) into the log.
- **Unified memory ("multiple memory in one")** — each connected ADE keeps its own
  native memory (`CLAUDE.md`, `AGENTS.md`, …). Loom imports them all into one brain
  (`memory_import` events, content-hash deduped), merges them with the project's
  decisions and shared thread, and projects the union into whoever is taking the turn.
  Connect a new agent → its knowledge joins the brain, and everything the others learned
  flows into it. `loom memory` shows the merged brain; it refreshes on open and on every
  handoff. This is the seam an isolation-first tool (separate worktrees) can't own.
- **Decisions** — `loom decision <text>` pins a fact, and any agent line starting
  `Decision: …` is captured automatically. Decisions ride every future projection.
- **Cost telemetry** — agents that report per-turn cost (Claude Code, OpenCode) feed a
  live ledger: `loom costs` breaks it down per agent, the board/TUI/phone app show the
  project total, and every route logs exactly what it spent
  (`✔ route completed (3 steps) · $0.0421`). Totals rehydrate from the event log, so
  they survive restarts.
- **Daemon** — one process, many projects. REST for commands, WebSocket for the live
  stream. Config edits hot-reload when the project is quiet.

## Your phone (Android today, over Tailscale)

The daemon serves a full phone app at `/app` — board, live thread, agent chips, routes.
No app store, no build step; it ships inside Loom.

**Pair from the app.** The web/desktop window has a **Connect a phone** button next to the
terminal: it opens a modal with a QR (and a copy link) and a **Local network / Tailnet**
toggle. Pick one and, if the daemon is still localhost-only, hit **Enable phone access** —
Loom adds a *second listener* on that LAN or tailnet IP (localhost is never disturbed, so
the window you're in doesn't blink) and shows a QR your phone can actually reach. Same
single-use token, no terminal needed.

**Or pair from the terminal:**

```bash
loom up --tailnet     # daemon binds to your Tailscale IP (never 0.0.0.0)
loom pair             # QR appears in the terminal (also `/pair` inside `loom tui`)
```

Scan the QR with your phone camera (for the tailnet path, the phone must be on your
tailnet — install the Tailscale app and sign in; the local-network path just needs the
same Wi-Fi). The link opens `…/app#pair=<token>`; the app claims the **single-use,
10-minute** pairing token from the URL fragment (fragments never hit the network log) and
exchanges it for its own client token. Then:

- **Board** — every project, needs-input dots, baton holder, live route progress.
- **Thread** — the same shared conversation, streaming over WebSocket.
- **Agent chips** — tap `opencode`, hit send: baton shifts (projection + briefing
  included), exactly like `tab` in the TUI.
- **Routes** — the ➤ button opens a picker: choose **auto** (LLM picks each hop), any
  named pipeline, or custom steps, type the task, go. Live banner with hop progress and
  reasons, an abort button, and when a route pauses on a question you answer right
  there and it resumes.
- Chrome menu → *Add to Home screen* installs it like an app.

**Push notifications** come with the native app ([`app/`](app/README.md)): open it once
after pairing and it registers its Expo push token with the daemon. From then on your
phone buzzes when an agent **needs input**, when a **route completes or fails**, and
when a solo turn finishes — route hops are deliberately silent (a 5-step pipeline
buzzes once, not five times). Verify with `loom clients --ping`.

## Your phone, for every computer

The phone app pairs with each computer you run Loom on: your desktop, your laptop, a box in the
cloud. **Account ▸ Computers** shows them all live (answering or not, and how fast), and one tap
switches between them. With Loom Cloud on, each answers from any network, through its own key.

**Approve from the lock screen:** when an agent asks to use a tool, the alert has **Allow** and
**Deny** buttons. The answer goes straight to the computer that asked, without opening the app.

## Permissions: bypass, auto, or always ask

Every agent CLI has its own idea of "may I?". Loom gives you one dropdown with
three words and maps them onto each CLI. Every cell below was checked against the
real CLI with `node scripts/verify-permissions.mjs`, not read off `--help`.

| | Bypass | Auto | Always ask |
|---|---|---|---|
| Claude Code | `bypassPermissions` | `acceptEdits` + Loom's Auto policy *(default)* | **real approvals**: each tool call waits for your Allow / Deny in Loom, on desktop or phone |
| Codex | no sandbox | `workspace-write` *(default)* | **real approvals**: a `read-only` sandbox, and each command or edit waits for your Allow / Deny in Loom |
| Antigravity | `--dangerously-skip-permissions` *(default)* | ✗ unavailable: agy 1.2.6 headless writes into its own scratch folder, not your project | `--mode plan` |
| Grok | `bypassPermissions` *(default)* | `auto` | `plan` |
| OpenCode | allow-all | its defaults *(default)* | ✗ unavailable: opencode 1.18.31 ignores read-only settings on its headless API |

- **What Auto lets Claude Code do.** It edits files and runs commands inside the
  project, its tests included, the same as Codex's `workspace-write`. Refused,
  with the rule that fired named in the refusal: a path outside the project, a
  command that can't be undone (the [shield](#blast-radius-shield-what-cant-be-taken-back)'s
  list), and MCP tools nobody allowed. The project's test command
  (`proof.testCommand` or the detected one) always runs. To allow more, add
  `.loom/config.json` → `permissions.allow`: command prefixes (`"docker compose up"`),
  tool names (`"WebFetch"`) or globs (`"mcp__github__*"`). Add folders an
  agent may read but not write with `readPaths` (`["../chatterbox-api"]`).
- An agent whose Auto is unavailable runs in its default instead (Antigravity
  runs Bypass). Hover a permission badge to see what that agent's mode actually
  allows.
- "Unavailable" cells are shown disabled with the reason, and the API refuses them.
- **Always ask** is answered inside the daemon: Claude Code's permission prompts
  arrive through the Agent SDK's `canUseTool`, and Codex's through app-server
  approval requests. The request appears in the thread as an approval card; nothing
  happens until you answer, and a card closes by itself if the turn ends first.
- `node scripts/verify-approvals.mjs` proves it against the real CLI: the file does
  not exist until you press Allow.

## Plan mode

Turn on **Plan** in the composer and agents write plans, not code.

- **In a chat:** the agent investigates, then writes
  `.loom/plans/<date>-<slug>.md` — Loom's folder, not a new one in your repo — (Goal, Context, Approach, self-contained Tasks, Risks,
  Verification) and stops.
- **In an orchestra** (`loom orchestrate --plan "<goal>"`):
  - the orchestrator's plan becomes `plans/<run>/PLAN.md` plus one spec file per
    task, committed to the run's branch *before* any worker starts;
  - each worker is pointed at its own spec;
  - when the run ends, statuses and results are written back.

Every file has front matter (`id`, `agent`, `depends_on`, `status`) and is written
so another agent, or a teammate, can pick up any task with no other context.

## Git delivery: commit, push, or open a PR

One per-project setting decides what happens to finished work. It's the toggle
next to GitHub in the status bar, or `git.delivery` in `.loom/config.json`.

| | Chat turns | A finished orchestra |
|---|---|---|
| **No commit** *(default)* | left uncommitted | waits on its branch until you Apply |
| **Commit only** | committed, agent as co-author | merged into your branch |
| **Commit & push** | committed and pushed | merged and pushed |
| **Commit & open PR** | committed | its branch pushed, and a PR opened with `gh`: summary, task table, PLAN.md |

A failed push never un-finishes a run. The error is shown, and **Retry delivery**
is one click.

## Edit and retry as chat branches

The daemon API and CLI support alternate turns inside a chat (#375). Editing a
user message or retrying an agent reply activates a new sibling branch and sends
its prompt. Later messages on the previous branch remain available. Web and phone
branch controls are separate work; these commands work now:

```sh
loom chat:branches --chat main --json
loom chat:edit 123 "Revised prompt" --chat main
loom chat:retry 124 --chat main         # 124 is an agent reply event id
loom chat:branch 0 --chat main          # original history; files stay as they are
loom chat:branch abc123 --preview       # inspect the fork checkpoint's patch
loom chat:branch abc123 --rewind-files  # show patch, confirm, then restore files
```

`--chat` accepts an id or title and defaults to `main`. Non-interactive file rewinds
require `--yes`. Branch changes return HTTP 409 while work is running or prompts
are queued. Clear the queue or let it finish before switching.

API paths below start with `/api/projects/:id/chats/:chat`:

| Method and suffix | Request / response |
| --- | --- |
| `GET /branches` | `{ branches, active, siblingsByEventId }` |
| `POST /branches` | `{ fromEventId, mode: "edit", text }` or `{ fromEventId, mode: "retry" }` → `{ branch }` |
| `GET /branches/:branchId/rewind` | Read-only `{ checkpoint, changed: string[], diff }` preview, including untracked files |
| `POST /branches/:branchId/activate` | `{ rewindFiles?: boolean }` → `{ active, rewind?: { restored, undo, changed, diff } }` |

Each branch is `{ id, parent: string|null, forkEventId, createdAt, label? }`;
`createdAt` is epoch milliseconds. Root is `"0"`. `ChatInfo.branches` and
`ChatInfo.activeBranch` are optional for legacy chats. Events optionally carry
`branch`; its absence means root. A branch inherits its parent's events through
`forkEventId`, inclusive, then its own events. Editing replaces the selected user
turn; retrying repeats the user prompt that led to the selected agent reply. Both
discard that turn and its later continuation from the new branch's visible history.
Targets must be visible in the active branch. Existing event ids never change.

`siblingsByEventId` maps the original and alternate prompt/reply event ids to an
ordered array of branch ids, original first. For a **‹ n/m ›** control, walk from
`active` up its parents until a choice matches, then use that choice's index + 1
and the array's length. Activating a choice changes the whole chat's active history.
Refetch `/events?chat=:chat` and `/branches` after switching; a `status` event with
`state: "branch_activated"` announces explicit switches. Chat paging, replay,
agent history and Brain extraction follow the same lineage. Project-wide audit
and cost history still includes every branch.

Switching defaults to history only. A client should show the rewind preview before
sending `rewindFiles: true`. Rewinding restores the selected branch's fork checkpoint;
returning to root restores the fork being left. It preserves Git HEAD and ignored
files, saves an undo checkpoint, and returns the actual applied patch. Missing or
pruned fork checkpoints return 409; switching history still works. Branches share
the working tree, so a new agent turn can edit the current files regardless of the
selected history.

Native resume cursors are isolated by chat, branch and agent. Codex uses
`thread/fork` with the last retained `lastTurnId`; Claude uses `resume`,
`forkSession: true` and the last retained message UUID as `resumeSessionAt`.
These fields were verified against the locally generated Codex app-server types
and installed Claude Agent SDK types. Codex servers that reject the turn-boundary parameter fall back to a whole-session
fork with the divergence briefing. Older histories without native boundary ids
(including a fork before the first turn) use a separate session fork and an explicit
text briefing of the divergence point; that fallback does not physically truncate
the native transcript. Other adapters start an isolated branch session briefed
with the visible history as text. Session cursors and branch metadata survive daemon
restarts. Branching does not undo already extracted shared memories or external
side effects.

Approach credit: A