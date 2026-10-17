<div align="center">

<img src="apps/web/public/favicon.svg" width="76" alt="">

# Agentry

**Run Claude Code as a service.**

A REST API, a web UI and multi-agent orchestration around the Claude Code CLI, in one container.

[![CI](https://github.com/yeyo11/agentry/actions/workflows/ci.yml/badge.svg)](https://github.com/yeyo11/agentry/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/yeyo11/agentry?style=flat&logo=github&color=d97757)](https://github.com/yeyo11/agentry/stargazers)
[![Node](https://img.shields.io/badge/node-%E2%89%A522-5fa04e?logo=node.js&logoColor=white)](package.json)
[![Image](https://img.shields.io/badge/ghcr.io-agentry-2496ed?logo=docker&logoColor=white)](https://github.com/yeyo11/agentry/pkgs/container/agentry)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-6ba539?logo=openapiinitiative&logoColor=white)](#rest-api)
[![Buy me a coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-ffdd00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/yeyo11)

<img src="docs/media/tour.gif" alt="A tour of Agentry in the Night Shift design: a project's dashboard with what is working now, the command palette, a working chat with its activity and the inspector's changes, an orchestration followed as steps through to its verification, and the accounts with their usage" width="100%">

</div>

Claude Code lives in your terminal. One machine, one session at a time, and nothing to look at
once you close the tab.

Agentry puts it behind a REST API and a web UI: start and watch conversations from anywhere, run a
graph of agents in parallel, browse every transcript the CLI has ever written, and go on in another
agent when one runs out of quota — without giving up a single thing the CLI can do, because
Agentry drives it through the CLI and nothing else.

```bash
docker run -d --init --name agentry --restart unless-stopped -p 127.0.0.1:8787:8787 \
  -v agentry-config:/home/node/.claude -v agentry-data:/data -v agentry-workspace:/workspace \
  ghcr.io/yeyo11/agentry
```

Name all three volumes: the image declares each as a volume, so a command that names fewer still
starts, with the others on volumes Docker made on its own, and replacing the container to update
starts again with empty ones. [Updating](docs/deploy.md#updating-a-container-without-losing-anything)
says how, and Settings → Account warns when a container was started that way.

### What you get

- **Every conversation, from anywhere** — start a chat from the UI or the API, stream the tokens,
  answer follow-up turns, and pick up any session the CLI has ever written on that machine.
- **Answer what Claude asks, as it asks** — a headless chat has nobody to ask, so it is normally
  denied anything that needs permission. Agentry speaks the CLI's control protocol
  (`--permission-prompt-tool stdio`) and routes every prompt to the panel: tool calls with the exact
  command (allow, allow always, or deny with a reason the model reads), questions from
  `AskUserQuestion` with their options, and plans to approve or send back. From the same screen you
  interrupt a turn without losing the session and switch the permission mode or the model mid-run.
- **Orchestration** — a DAG of tasks, each with its own Claude worker, run in parallel with
  dependency context and a synthesis step. Every worker can get its own git worktree and branch,
  so parallel agents never write over each other. An auto-planner drafts the graph; plans are kept,
  so one lost to a closed tab is reloaded instead of paid for twice, and a graph interrupted by a
  restart goes on where it stopped.
- **Multi-account rotation** — usage per window, proactive switching before an account runs out,
  and a run that hits its limit is rotated and resumed on the next account (a chat pinned to the
  account that ran out is unpinned first). Every rotation is
  recorded, so "why did my account change" has an answer that survives a restart.
- **See what an agent really did, and step in** — for every orchestration task and every chat: the
  branch and its commits, the files changed with `+/−`, what is uncommitted, the worker's own checklist, and what it is running right now. A health badge notices
  a hung or repeated command, a chat busy without progress, a loop, a test bent to pass, silence and
  a blown budget, says why in one line and offers three ways in: cancel just that command's process
  tree, send a hint, interrupt. An optional supervisor — Haiku, off by default — wakes once per
  signal when a worker turns `bad`, reads its last steps and proposes the hint, for you to send,
  edit or dismiss.
- **Review the changes without leaving Agentry** — one screen for a chat, a task or the integration
  branch, drawn by a diff comparator of its own (no editor, no diff library). **Reading**, the
  default, shows each file as it is now with a 3 px rail on what is new and what was removed folded
  into a pill; **Unified** and **Side by side** are one key away. Syntax stays muted so only the
  change carries colour, a changed phrase is one mark, and a change fingerprint, a file map (seen,
  not committed, being edited now) and a block rail with `j`/`k`/`n`/`p` keep a long branch
  navigable. The **Step by step** lens replays every edit from the transcript with its own patch and
  the sentence Claude wrote just before it, one click from that place in the conversation, so a chat
  outside a repository can be reviewed too.
- **Verify once, after integrating** — an orchestration can run its checks (build, the browser
  suite) once on the merged branch, after an install step it works out from the lockfile, with a
  fixer agent held to rules Agentry writes and a cap on its attempts and on what it may spend.
  Workers only run the type check and the unit tests; the outcome is on the graph before a pull
  request is offered, and it can fail the graph outright if you ask it to.
- **Orchestration you can revise** — re-run one task of a finished graph with everything that
  depends on it, edit and relaunch a graph as a new one, save graphs as templates, and give a task
  or the whole graph a time and a cost limit.
- **A board of what each project needs done** — a project is created from one of five templates in
  a wizard, and switches its modules on and off in its settings. The Board module gives it a Tasks
  board:
  - work items with YouTrack-style keys (`AGN-12`);
  - five fixed columns with optional limits, dragged by pointer or keyboard;
  - epics, and milestones without dates;
  - acceptance checklists, `blocks` relations, comments and a history the server writes;
  - a list view, and an All projects view.

  "Work on it" starts a chat on an item in its own worktree on `task/<key>`. A selection becomes a
  draft orchestration with its dependencies. A chat's message becomes a task. The item then moves
  itself as that work goes, forward only and never over a person's move, and its card shows live
  while an agent works on it. See [docs/projects.md](docs/projects.md) and
  [docs/work-items.md](docs/work-items.md).
- **A team of agents that works the board** — with the Team module on, a project has members, each a
  Claude Code agent file in `.claude/agents/` (so it works from a terminal too) with a role, a model
  and the paths it may write. Switch the **flow by column** on and a card entering a column starts
  its role's run as that agent:
  - the Product Owner refines in Backlog and To do;
  - the Developer implements in In progress;
  - QA verifies in In review, and sends the card back with its comment a set number of times before
    it waits for you.

  Agents move cards, but only you move one to Done, and at most a set number of runs go at once.
  Members propose what the team should remember, and nothing reaches `CLAUDE.md`, the CLI's memory
  or the project **journal** until you approve it. Every run is handed the journal's newest entries.
  **Documents** reads and edits the repository's documents folder, with the specifications and
  decisions a run wrote tied to their task. See [docs/team-and-flow.md](docs/team-and-flow.md).
- **An assistant that reads the project and proposes what to create** — a read-only Claude Code chat
  (`Read`, `Grep`, `Glob`, `LS`, and `git log`/`git status`/`ls`) that answers through
  `--json-schema`. It proposes a team, agents, skills and commands, and first tasks, each with the
  reason it is proposed, and keeps the list of what it read. You accept or discard each proposal on
  its own, and nothing is written until you accept it: a member through the team, a task in
  Backlog, a resource opened in the editor unsaved. It runs when you create a project, from the
  board ("Suggest tasks") and from a project's resources ("Suggest", "Create with AI"), never on a
  schedule, and shows its model, time and cost like any chat. See [docs/assistant.md](docs/assistant.md).
- **Tools and servers per chat** — start or resume a chat with a named preset of allowed and
  disallowed tools (`read-only`, `no-network`, `everything`, all editable, restorable, one of them
  the default for a chat that picks none) and with only the MCP servers you pick. A fork inherits
  its source's tools, and a resume picks up a server you edited since.
- **Recurring work** — chats and orchestrations on a cron expression and a time zone, with a run
  history and a say in what happens when a slot arrives while the last run is still going (start
  anyway, skip it, or queue it). A window missed while Agentry was down is skipped, never run late.
- **Cost and usage over time** — per day or week, per project and per model, from the cost the CLI
  reports, over any range you pick from a calendar; any transcript, or a whole project's chats,
  exported as Markdown or JSON.
- **Spending limits** — cap any run with a budget the CLI enforces from inside.
- **A limit does not stop the work** — each provider shows how much of its usage limit is spent; at
  a limit a chat offers to continue on another provider with a handoff, to restart there, or to wait
  for the reset, and automated work does what the settings allow (by default, it waits).
- **claude.ai connectors** — the Docs, Gmail and Calendar connectors the CLI can see, their status
  and prepared prompts that start a chat.
- **The whole configuration surface** — settings, instructions, MCP servers, agents, skills,
  commands, output styles, memory, plugins and marketplaces, per user and per project.
- **Safe to expose** — token or OIDC authentication in front of every route, a read-only mode, secrets
  in MCP `env` and `headers` never returned by the API, an audit log of every write you can narrow by
  path, method and status, and a way back in from the environment when the token is lost. See
  [Securing it](#securing-it).
- **On your phone** — installable to a home screen on Android and iPhone as a progressive web app,
  and able to tell you that a chat is waiting while it is closed, over Web Push this server signs
  with its own VAPID key. No app store, no native shell, no third-party push account. The
  push half needs HTTPS: see [On a phone](#on-a-phone).
- **Reach it from your phone, through your own tailnet** — Settings → Remote access serves this
  Agentry on your [Tailscale](https://tailscale.com) tailnet with `tailscale serve` (never Funnel), at
  a stable HTTPS address with a QR code for the phone: no domain, no proxy, nothing on the public
  internet. It only opens while authentication is on, only the node's exact name is let in, and only
  the one Serve rule Agentry added is ever removed. See [docs/tunnel.md](docs/tunnel.md).
- **One container, one volume** — non-root, the CLI baked in and pinned with an update check,
  everything else on a data volume. Compose profiles, a TLS proxy and a Helm chart are in
  [docs/deploy.md](docs/deploy.md).

> [!IMPORTANT]
> **Authentication is off until you turn it on.** That is right for a port bound to `127.0.0.1`, and
> wrong for anything else: with `mode: none`, anyone who reaches the port can start a chat on your
> account and read every transcript on the machine. Before publishing the port, set
> `AGENTRY_AUTH_MODE=token` (or `oidc`) and put a TLS-terminating proxy in front — see
> [Securing it](#securing-it). [SECURITY.md](SECURITY.md) spells out exactly what is and is not protected.

### A project's dashboard: what is working now, and what to pick up

<img src="docs/media/home.png" alt="A project's dashboard in the dark theme: a hero saying one agent is working, tiles for agents running, answers waiting, today's spend and the 5 h limit ring, the chat in progress with the command it is running, a quick-start prompt and the chats to pick up again, above the status bar with the account and its limits" width="100%">

### A board of what the project needs done, and who is working on it

<img src="docs/media/board.png" alt="The Tasks board of a project in the dark theme: five columns with their counts, In progress over its limit of 3 and saying so in words, a card whose chat is working with its live rail, ring spinner and the command it is running, an epic counting its tasks, a card blocked by another, and Done folded to three cards and &quot;and 2 more&quot;" width="100%">

<p align="center"><img src="docs/media/board-mobile.png" alt="The same board on a phone: no horizontal scroll, the columns as sections of one list with a segmented jump between them, the In progress section marked over its limit and the working card first" width="320"></p>

### Workers in parallel, then one branch that was checked

<img src="docs/media/orchestration.png" alt="An orchestration followed as steps: its objective and settings, tiles for tasks, time, cost and parallel workers, a pipeline on stage 2 of 3 followed by integration, verification and pull request, and the stage's two tasks running side by side, the most active one with the energy border" width="100%">

### See what an agent really did, and step in

<img src="docs/media/chat.png" alt="A working chat: its transcript with the tool calls folded into steps and the command it is running now, the composer with its energy border and Interrupt, and beside it the inspector's Changes tab: the totals, the branch and its commit, a change fingerprint, one line per file it changed and Review the changes" width="100%">

<p align="center"><img src="docs/media/chat-mobile.png" alt="The same working chat on a phone: a one-line header, the transcript with its folded steps and what it is running, and the composer with its model and permission chips at the bottom" width="320"></p>

### Review the changes without an editor

<img src="docs/media/changes.png" alt="The review screen of the same chat: a header with the branch, its base, the counts and a change fingerprint, the file map with each file's status letter and +/− beside the diff of src/server.js in Reading mode, the file as it is now with a green rail on its new lines and the removed line folded into a −1 pill" width="100%">

### Work that comes back every night

<img src="docs/media/schedules.png" alt="The schedules page: a nightly chat with its run history open, where a slot that overlapped a running one is marked, and a weekly orchestration, each with its cron expression in words and its next run" width="100%">

## How it talks to Claude

The wrapper drives Claude Code through its CLI, the interface Anthropic ships for programs — no terminal scraping, no undocumented endpoints:

| Need | CLI surface used |
| --- | --- |
| Detect installation | `claude --version` |
| Auth status | `claude auth status --json` |
| Run / continue a conversation | `claude -p --input-format stream-json --output-format stream-json` (one long-lived process per run, multi-turn over stdin; `--resume` when the process is gone) |
| Background tasks & subagents | `system/task_*` events and `Task` tool calls in the stream |
| Live CLI sessions | `claude agents --json` |
| Session history & projects | transcripts in `$CLAUDE_CONFIG_DIR/projects/*/*.jsonl` |
| MCP servers | `claude mcp add-json` / `claude mcp remove` (user scope) |
| Orchestration planner | `--json-schema` structured output |
| Decision engine, `cli` provider | one housekeeping chat per batch of typed questions: `--json-schema` for the answers, `--effort`, `--max-budget-usd`, and no tools, settings or API token in it ([docs/decision-engine.md](docs/decision-engine.md)) |
| Usage limit | `rate_limit_event` messages in the stream (the window, its use and when it resets), and a 429 result when a turn dies on it |
| Codex usage limit | `account/rateLimits/read` and the `account/rateLimits/updated` notification of `codex app-server`: reading costs nothing |
| Tool presets and per-chat MCP servers | `--allowedTools` / `--disallowedTools`, and `--mcp-config` with `--strict-mcp-config` over a file holding only the chosen servers |
| Spending and time limits | `--max-budget-usd` for a cost limit; the time limit is Agentry's own clock |
| claude.ai connectors | `claude mcp list`: the servers it names `claude.ai …` |
| What an agent changed on disk | `git` in the task's worktree, and the `Write`/`Edit` calls in the transcript |
| Stopping one command | The process tree under the CLI's own pid; the CLI writes the failed tool result itself |

The one thing Agentry reads about Claude Code that is not the CLI is the npm registry's metadata for
`@anthropic-ai/claude-code`, to tell you when a newer version exists. It is a plain metadata read
(no Anthropic API), done on demand and once a day, and `AGENTRY_CLI_UPDATE_CHECK=off` stops the daily one.
Agentry asks GitHub the same way about its own releases (`AGENTRY_UPDATE_CHECK=off` stops that one).

## Quick start

On a machine where you are already logged in to Claude Code, mint a long-lived token:

```bash
claude setup-token
```

Then run the published image, pasting that token in:

```bash
docker run -d --init --name agentry --restart unless-stopped -p 127.0.0.1:8787:8787 \
  -e CLAUDE_CODE_OAUTH_TOKEN=sk-ant-oat-... \
  -v agentry-config:/home/node/.claude \
  -v agentry-data:/data \
  -v agentry-workspace:/workspace \
  ghcr.io/yeyo11/agentry
```

The workspace is a named volume too. A folder of your own (`-v "$HOME/projects:/workspace"`) works
as well, as an absolute path: a relative one such as `$PWD/workspace` is a different folder from
wherever you run the command next.

The image carries Claude Code, Codex, Gemini CLI, GitHub Copilot CLI and OpenCode, each at the
version Agentry's driver was written for. Their sign-ins live under `/data`, so the same three
volumes keep them: Settings → Providers shows which ones are signed in.

The UI and the API reference are on <http://localhost:8787> — the panel at `/`, the interactive
OpenAPI docs at `/docs`. Everything else is configured from the UI.

The port is published on `127.0.0.1` only: authentication is off by default (see
[Securing it](#securing-it) and [SECURITY.md](SECURITY.md)), so do not drop that prefix unless you
turn it on and put TLS in front.

<details>
<summary>Building it yourself instead</summary>

```bash
git clone https://github.com/yeyo11/agentry
cd agentry
cp .env.example .env        # paste the token into CLAUDE_CODE_OAUTH_TOKEN
docker compose up --build
```

The image pins the Claude Code it installs (`CLAUDE_CODE_VERSION`, defaulting to the version in
`docker/Dockerfile`), so an image is the same tomorrow as today; set it in `.env` to move. Compose
publishes the port on `127.0.0.1` like the command above, and adds a `tls` profile:

```bash
docker compose --profile tls up -d    # plus Caddy on :80 and :443, in front of Agentry
```

</details>

More ways to run it, with the details — Compose profiles, the TLS proxy, a Helm chart, the pinned
CLI and its update check, health-driven restarts and the signals the server handles — are in
[docs/deploy.md](docs/deploy.md).

Open <http://localhost:8787> for the UI; the API lives under `/api`.

Volumes:

| Volume (`docker run` / compose) | Mount | Purpose |
| --- | --- | --- |
| `agentry-config` / `claude-config` | `/home/node/.claude` | The whole account setup: `settings.json`, `.claude.json` (MCP servers), `CLAUDE.md`, agents, skills, commands and session transcripts |
| `./workspace` / `agentry-workspace` | `/workspace` | Projects Claude works on (default `cwd` for runs) |
| `agentry-data` / `wrapper-data` | `/data` | Wrapper state. Rows in the SQLite store (`wrapper.db`): chats and their executions, orchestrations, plans, each provider's usage limit, the moves and waits between providers, command durations, schedule runs, the supervisor's proposals, the installs registered for Web Push and the audit log. Settings-shaped files: `providers.json` (the order, the limit settings and the model mapping), `auth.json` (the auth mode and the hash of the token, mode 600), `secrets.json` (the sealed secret vault: every key and token given in the setup, mode 600) and `secret.key` (the vault's key when `AGENTRY_SECRET_KEY` is not set, mode 600; see [docs/security-model.md](docs/security-model.md)), `tool-presets.json` (the presets and the default), `orchestration-templates.json`, `schedules.json`, `supervisor.json`, `cli-version.json`, `release.json` (what the last Agentry release check learned) and `push.json` (the VAPID keypair, mode 600). `uploads/` holds attachments, `mcp/` the per-chat MCP config files (mode 600: they can hold a server's secrets) and `provider-homes/` the sign-in, settings and sessions of Codex, Gemini, Copilot and OpenCode, and the GitHub and GitLab sign-ins of `gh` and `glab`, in the Docker image (`CODEX_HOME`, `GEMINI_CLI_HOME`, `COPILOT_HOME`, `XDG_*`, `GH_CONFIG_DIR` and `GLAB_CONFIG_DIR` point there) |

The compose file keeps its original volume names so an existing setup keeps its data; `docker compose`
prefixes them with the project name (`agentry_wrapper-data`…), which is the folder's name unless
`COMPOSE_PROJECT_NAME` is set. Run from another folder, it would start with three empty volumes: set
`COMPOSE_PROJECT_NAME` in `.env` once, before the first start.

## Desktop app (Linux)

Prefer a window to a container? Every [release](https://github.com/yeyo11/agentry/releases) also
carries an AppImage and a `.deb`:

```bash
curl -fsSL https://raw.githubusercontent.com/yeyo11/agentry/main/scripts/install.sh | bash
```

The `.deb` through apt on Debian and Ubuntu, the AppImage under `~/.local` everywhere else. To
install by hand, download either file from the release.

It runs on your machine with your own Claude Code CLI and `~/.claude` login, so nothing is
sandboxed and runs default to `acceptEdits` instead of `bypassPermissions`. The app's top bar is
its title bar, a tray icon lists what is working and what waits for you, and the taskbar shows the
running orchestrations' progress. It updates itself from Help → **Check for updates…**, and never
restarts over running work without asking. Requirements, data locations, CLI detection, the tray,
updating and building from source are in [docs/desktop.md](docs/desktop.md).

## On a phone

Agentry installs to a home screen as a progressive web app: the same bundle the API already serves,
with its own icon and no address bar. No app store, no native shell, nothing extra to build.

- **Android (Chrome, Edge)**: open Agentry and press **Install Agentry** in Settings → Install. The
  browser's own menu offers the same thing, as *Install app*.
- **iPhone and iPad (Safari)**: open Agentry, tap **Share**, then **Add to Home Screen**. iOS has no
  install API, so no button on a page can do it for you — Settings → Install says those two taps.
- **A desktop browser** installs it the same way, from the same tab.

Once installed it starts standalone and paints its own shell from the service worker's cache instead
of a white screen while the bundle downloads. Nothing about the client/server contract changes: the
same relative `/api` calls, the same `Authorization` header, the same two event streams. The worker
caches the shell only — it never answers a request under `/api`, `/docs` or `/openapi.json`, so
`GET /api/events` streams exactly as it does in a tab.

**Being told while the app is closed.** Settings → Notifications has an *Also push to this device*
switch. The browser subscribes with a VAPID key this server made for itself, and from then on a chat
that stops for a permission prompt puts a notification on the phone even with Agentry closed; tapping
it opens that prompt, not just the chat. The per-kind preferences and the interruption level above
the switch decide what is worth waking a device for, and the list below it shows every install registered, this one marked,
each with **Test** and **Remove**. A window that is open and focused shows its usual toast and no
push, so the same news never arrives twice. A test push, and every push on an iPhone or iPad, is
shown even then: a test has no toast of its own, and iOS revokes a subscription whose pushes show
nothing.

Push needs a **secure origin**: `https://…` or `localhost`. On `http://192.168.1.10:8787` — how most
people run Agentry on a LAN — the browser has no service worker at all, so there is no push and no
cached shell; the Settings page says so and names the origin rather than showing a switch that does
nothing. [docs/deploy.md](docs/deploy.md) has the TLS proxy that fixes it. On iPhone and iPad, a push
reaches an app on the Home Screen only, never a Safari tab: install first, then turn the switch on
from the app that starts.

**No domain or proxy?** With Tailscale on this machine and on the phone, Settings → Remote access
serves Agentry on your tailnet at `https://<machine>.<tailnet>.ts.net:8443`, an HTTPS origin with a
real certificate, and so push. Turn on authentication first: the tunnel refuses to open without it.
The tailnet needs MagicDNS and HTTPS certificates on, and the address stays the same while the
machine keeps its name. Only devices on your tailnet can reach it. See
[docs/tunnel.md](docs/tunnel.md).

## Local development

Requires Node 22+, pnpm 10 and a logged-in `claude` CLI in your `PATH`.

```bash
pnpm install
pnpm dev          # API on :8787, UI on :5173 (proxies /api)
pnpm typecheck
pnpm test         # unit tests (core, web, desktop) + API integration tests (node:test)
pnpm build && pnpm e2e   # browser suite: isolated wrapper + headless Chrome, never touches ~/.claude
                         # E2E_SPEC_TIMEOUT (180000 ms) and E2E_TIMEOUT (1500000 ms) bound a spec and the run
                         # E2E_SERVER_START_TIMEOUT (120000 ms) bounds the wait for the API's /api/health
                         # E2E_SHARDS=N runs N isolated shards side by side (default: cores/2, at most 4);
                         # E2E_SHARD=k/N runs only shard k, as each CI job does (split: e2e/timings.json)
E2E_LIVE=1 pnpm e2e chat # specs that talk to Claude (logged-in CLI, costs a few tokens)
pnpm media        # re-record the README's tour and stills (needs pnpm build first, ~2 min)
```

Locally the wrapper uses your real `~/.claude`. Point `CLAUDE_CONFIG_DIR` somewhere else to
experiment with config writes safely.

The browser suite boots its own wrapper with temporary config, workspace and data directories (on
port 8799 when it runs as one shard; each parallel shard gets its own port, sandbox and Chrome), seeds whatever each spec needs and drives headless Chrome over the DevTools
protocol (no Playwright, no dependencies). A spec and the whole run each have a time limit, and Chrome
and the wrapper are closed on every way out (a pass, a failure, a timeout, `SIGINT`, `SIGTERM`, a crash),
by the pid the harness itself started. It covers every page in both themes and at phone
width, the config editors and their save/delete flows, the unsaved-changes guard, the command
palette and the chats list. The health actions need a live CLI process, so the specs that ask for it
(`export const fakeCli = true`) run last, behind one restart of the server, against the fake `claude`
in `e2e/fake-cli` — an executable that speaks just enough stream-json to hang a command, take a hint
and be interrupted; every other spec keeps the real CLI. `E2E_LIVE=1 pnpm e2e chat` additionally
holds a real conversation with Claude (streamed reply, follow-up turn, stop) using your login.

`pnpm media` re-records the tour and the stills this README shows, through the same fake CLI and one
headless Chrome: `scripts/record-media.mjs` boots an isolated wrapper, invents the projects, chats,
graph, schedules and accounts in frame, and writes `docs/media/`: the tour, desktop stills at
1280×800 and the working chat at phone size (390×844). It needs `pnpm build` first and takes about
two minutes. The board's stills (`board.png`, `board-mobile.png` and `work-item.png`) are not part
of it yet: they were captured the same way, with a one-off script against the same kind of sandbox.

## Monorepo layout

```
packages/shared   Types and the message normalizer shared by every package (the API contract)
packages/core     CLI communication: detection, auth, chat manager, transcript store,
                  orchestrator, rotation between providers, config managers
apps/api          Fastify REST API + SSE; serves the built UI in production
apps/web          React + Vite UI
apps/desktop      Electron shell: runs the API as a child process, packaged as AppImage and .deb
e2e/              Browser suite (headless Chrome over CDP, no dependencies)
scripts/          The installer, and record-media.mjs behind `pnpm media`
docker/           Dockerfile and the healthcheck
deploy/           Caddyfile for the `tls` compose profile, and the Helm chart
docs/             Deployment and desktop guides, and the plans
```

Packages export TypeScript sources directly and the API runs through `tsx`, so development needs
no build step except for the UI. The image is built: it ships one compiled JavaScript file
(`/app/api.mjs`) and the built UI (`/app/web`), with no source tree, no `node_modules` and no
transpiler.

## Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `CLAUDE_CODE_OAUTH_TOKEN` | – | Subscription token from `claude setup-token` |
| `ANTHROPIC_API_KEY` | – | Alternative: API key billing |
| `PORT` / `HOST` | `8787` / `127.0.0.1` (`0.0.0.0` in the image) | API listen address. Loopback by default because the API runs commands on the machine and starts with no credential; the image opens it because Compose publishes the container on `127.0.0.1` anyway. Binding every interface while the mode is `none` logs a warning |
| `CLAUDE_BIN` | `claude` | CLI binary to use |
| `CLAUDE_CONFIG_DIR` | `~/.claude` | Claude config dir (`/home/node/.claude` in the image) |
| `AGENTRY_WORKSPACE_DIR` | `./workspace` | Default working directory for runs |
| `AGENTRY_DATA_DIR` | `./data` | Wrapper state |
| `AGENTRY_SECRET_KEY` | – | 32 bytes as hex: the key the secret vault (`secrets.json`) seals the keys and tokens Agentry hands a CLI with. The desktop app passes its own. Without it the Docker image makes one beside the data on the first write (`secret.key`, mode 600), which protects a copy of the files but not the volume, so passing it here is the recommended setup; a source install without it keeps the values plain at 0600. The server drops it from its environment once read |
| `AGENTRY_DEFAULT_PERMISSION_MODE` | `acceptEdits` (`bypassPermissions` in the image) | Mode for runs that do not set one. Without the variable it is editable in Settings → Security and applies to the next run; set, it is shown read-only there. Empty counts as unset |
| `AGENTRY_MAX_CONCURRENT_RUNS` | `8` | Max simultaneous `claude` processes (1 to 64). Editable in Settings → Security unless set here, like the mode above. Empty counts as unset |
| `AGENTRY_SETUP_SEEN` | off | `on` records that the setup assistant was finished or skipped. Without the variable the assistant writes it to `app-settings.json` (`POST /api/setup/seen`). The older `AGENTRY_PROVIDERS_STEP_SEEN`, and a `providersStepSeen` already stored, still count. Empty counts as unset |
| `AGENTRY_PUSH_SUBJECT` | `https://github.com/yeyo11/agentry` | The VAPID `sub` claim of every Web Push this server signs: a `mailto:` or `https:` a push service can complain to, naming a real domain — Apple refuses the whole JWT with `403 BadJwtToken` for something like `mailto:agentry@localhost`. Changing it takes effect on the next start, keypair and registered installs untouched |
| `AGENTRY_AUTH_MODE` | `none` | `none`, `token` or `oidc`. **Seeds** an install that has no `auth.json` yet; after that the setting saved from the UI wins. See [Securing it](#securing-it) |
| `AGENTRY_AUTH_TOKEN` | – | The bearer token to seed with when the mode is `token`. Only its SHA-256 is stored |
| `AGENTRY_AUTH_TOKEN_RESET` | – | `1` makes `AGENTRY_AUTH_TOKEN` replace the stored token on start, on an install that already has one. The change is audited with actor `env`, and a value already applied is not applied twice |
| `AGENTRY_DESKTOP_TOKEN` | – | Set by the desktop app on the server it starts: a secret generated at each launch that its tray sends as a bearer token. Accepted only from loopback, dialled on a loopback name, as the read-only actor `desktop`; kept in memory, never stored, and removed from the environment chats inherit. See [docs/desktop.md](docs/desktop.md) |
| `AGENTRY_READ_ONLY` | `false` | Seeds read-only mode |
| `AGENTRY_OIDC_ISSUER` / `_AUDIENCE` / `_CLIENT_ID` | – | Seed the OIDC settings: the issuer whose JWKS validates a JWT, the `aud` it must carry and the client id. A configured client id refuses a token whose `azp` names another client, and accepts one that carries no `azp` at all |
| `AGENTRY_CLI_UPDATE_CHECK` | on | `off` stops the daily check for a newer Claude Code (the button in Settings keeps working) |
| `AGENTRY_CLI_REGISTRY_URL` | the npm registry | Where that check reads the package metadata: a mirror, for an air-gapped install |
| `AGENTRY_UPDATE_CHECK` | on | `off` stops the daily check for a newer Agentry release (**Check for updates** in Settings keeps working) |
| `AGENTRY_RELEASES_URL` | GitHub's latest release of `yeyo11/agentry` | Where that check asks instead: a mirror or a test fixture. It must answer in GitHub's shape (`tag_name`, `html_url`, `published_at`) |
| `AGENTRY_DISTRIBUTION` | – (a source checkout) | How this server was installed, which decides the update steps the UI offers: `docker` (set by the image), `appimage` or `deb` (set by the desktop app) |
| `AGENTRY_PID_FILE` | `/tmp/agentry.pid` in the image | Where the server writes its pid, so the image's healthcheck can end a wedged server |
| `AGENTRY_HEALTH_RESTART_AFTER` | `3` | Consecutive failed health probes (30 s apart) after which the container restarts itself |
| `AGENTRY_ALLOWED_HOSTS` | – (loopback only) | Comma-separated host names this wrapper answers to besides loopback, each a name or a `*.domain` pattern standing for that domain's subdomains. A `Host` that matches none of them is refused `421` before the credential is read. Ports and letter case are ignored; `GET /api/health` is exempt. Behind a proxy, name the public host here or everything answers `421`. Its hosts are fixed; more can be added in Settings → Security, without a restart ([docs/layered-settings.md](docs/layered-settings.md)); a running tunnel's exact host is added on its own |
| `AGENTRY_TUNNEL` | on | Whether Settings → Remote access may serve Agentry on the tailnet through `tailscale serve`: `on`/`1`/`true` or `off`/`0`/`false`, empty meaning the default; anything else stops the server at startup. In the image, `off` also keeps the entrypoint from starting its own tailscaled. See [docs/tunnel.md](docs/tunnel.md) |
| `AGENTRY_TAILSCALE_MANAGED` | set by the image's entrypoint | `1` when the tailscaled behind the CLI is Agentry's own (the image's), which the app then signs in and out. Not for setting by hand |
| `AGENTRY_TAILSCALE_HOSTNAME` | `agentry` | The node's name when the image's Tailscale signs in (`tailscale up --hostname`); a DNS label, or the server stops at startup |
| `AGENTRY_TUNNEL_PORT` | `8443` | The HTTPS port of Agentry's Serve rule on the tailnet name, kept off 443 so a Serve rule of your own is never touched. Not a port between 1 and 65535 stops the server at startup |
| `TAILSCALE_BIN` | `tailscale` | The Tailscale CLI the tunnel runs |
| `AGENTRY_CORS_ORIGIN` | – (CORS off) | Comma-separated origins (or `*`, which echoes the caller) for external browser clients. The event streams obey this list too. The bundled UI never needs it: in dev it uses the Vite `/api` proxy, in production it is same-origin |
| `VITE_API_TARGET` | `http://localhost:8787` | Where the Vite dev server proxies `/api` |
| `AGENTRY_IDLE_TIMEOUT_MS` | `600000` | Idle runs are closed after this (they resume transparently) |
| `AGENTRY_WEB_DIST` | `apps/web/dist` (`/app/web` in the image) | Built UI the API serves (the desktop app points it at its bundled copy) |
| `AGENTRY_MCP_ENTRY` | the `mcp.mjs` beside the API bundle, when it exists | The bundle of Agentry's own MCP server a confined chat's CLI starts; from source it runs `packages/mcp` with tsx. See [docs/agentry-mcp-server.md](docs/agentry-mcp-server.md) |
| `LOG_LEVEL` | `info` | Fastify/pino log level (`trace` … `fatal`, or `silent`) |

Agentry sets two variables for every chat it starts, so an agent that calls the REST API reaches the
wrapper that runs it and not another one on the same machine: `AGENTRY_API_URL` (this server's API,
e.g. `http://127.0.0.1:34331/api`) and `AGENTRY_CHAT_ID` (the chat's own id). With authentication on,
the agent still needs a token of its own.

## Securing it

Agentry starts with authentication **off**, so a local install keeps working untouched. It also
starts bound to `127.0.0.1` and answering only to loopback host names, so "off" is not the same as
"open". Turn the guard on before the port is reachable by anyone you do not trust, and put a
TLS-terminating proxy in front.

**Modes.** Set from Settings → Security, or seeded from the environment on a fresh install
(`AGENTRY_AUTH_MODE`, `AGENTRY_AUTH_TOKEN`, `AGENTRY_OIDC_*`; once an `auth.json` exists in the data
directory it wins over the environment).

| Mode | What a request must carry |
| --- | --- |
| `none` | Nothing. The default |
| `token` | `Authorization: Bearer <token>`. Only the SHA-256 of the token is stored; the token exists once, in the answer that created it, and can be rotated or removed but never read back |
| `oidc` | A JWT that the issuer's JWKS validates, with the `aud` you configured and an unexpired `exp`. With a client id configured, a token whose `azp` names another client is refused |

- **Which hosts it answers to.** A request whose `Host` is neither loopback nor named in
  `AGENTRY_ALLOWED_HOSTS` is refused `421`, and that happens **before** the credential is looked at,
  so it holds in `mode: none` as well. It is what stops a page on another domain from pointing that
  domain at `127.0.0.1` and driving your install from your own browser. Put a proxy in front and you
  must name the public host there; `GET /api/health` is exempt, so probes are unaffected. Without
  the variable the list is editable in Settings → Security, and a running tunnel adds its own exact
  host, never a pattern, for as long as it answers.
- **Guessing is slowed down.** After ten failed authentications an address is answered `429` with a
  `Retry-After` that doubles from a second to a minute, and is forgotten after fifteen quiet minutes.
  Only a credential that was presented and failed counts (a wrong bearer token, a wrong `?token=`, an
  invalid JWT): a request carrying none is answered `401` and neither counted nor made to wait,
  because on a local install every process shares `127.0.0.1` and something polling without a
  credential would otherwise lock the owner out.
  A token you supply yourself must be at least 24 characters; one Agentry generates is 32 random
  bytes. The wait counts the peer's address, so behind a reverse proxy every client shares one
  count — see [SECURITY.md](SECURITY.md). Through the tunnel, whose client address is not trusted,
  all traffic shares one count of its own, apart from loopback, so a guess from the tailnet never
  makes the desk wait.
- **The tunnel.** Settings → Remote access refuses to open while the mode is `none`, and turning the
  mode to `none` closes it first. Tailscale encrypts it end to end and terminates TLS on this machine,
  so no third party sees the requests; every member of your tailnet who can reach the node can reach
  the address. See [docs/tunnel.md](docs/tunnel.md).
- **What stays open.** `GET /api/health`, so a probe needs no credential, and the built UI bundle,
  which is what gives a `401` a sign-in screen instead of a blank page. `/docs` and `/openapi.json`
  are guarded like everything else.
- **`?token=`.** A browser cannot put a header on an `EventSource`, an `<img>` or a download link,
  so five GETs also accept the credential in the query string: `/api/events`,
  `/api/chats/:id/stream`, `/api/uploads/:id/content`, `/api/chats/:id/export` and
  `/api/projects/:id/export`. Nothing else does. A proxy's access log will record that token, so keep
  query strings out of it for those routes.
- **OIDC is validation only.** Agentry checks a JWT and never talks to a token endpoint or signs
  anyone in; the browser UI signs in with a token, so in `oidc` mode clients bring a JWT their
  identity provider issued (or you run an identity-aware proxy that adds it).
- **Locked out.** Set `AGENTRY_AUTH_TOKEN` to a new value, add `AGENTRY_AUTH_TOKEN_RESET=1` and
  restart: the token in the environment replaces the stored hash, the audit log records it with
  actor `env`, and the mode, the OIDC settings and read-only stay as they were. The hash of the
  value applied is kept, so leaving both variables set does not undo a token rotated afterwards.
  With access to the data volume, deleting `<data dir>/auth.json` still works, but it resets the
  whole guard to whatever the environment seeds.
- **Read-only mode.** Every mutating request answers `405`, except answering a permission prompt (a
  person watching a chat can still unblock it) and the switch itself. The prompt has to belong to the
  chat in the path: a request id from another chat answers `404`, exactly as one that never existed
  does. It is for showing the panel to someone.
- **Secrets are not sent back.** `GET /config/mcp` and `GET /config/settings` return the names in a
  server's `env` and `headers` (and in settings' `env`) with a placeholder instead of the value. A
  write that sends the placeholder back keeps what is stored. The per-chat MCP config files Agentry
  writes for `--mcp-config` do hold real values, so they are mode 600 in a mode 700 directory.
- **Push payloads travel through a relay.** A Web Push goes out to the push service of the browser's
  maker (Mozilla, Apple, Google), encrypted per RFC 8291 so they cannot read it — but they do see
  that an install of yours was notified, and when. What a payload holds is therefore only what a lock
  screen shows anyway: the kind, the title and body, the chat or orchestration id, and the path to
  open. No prompt text, no tool arguments, no secrets. The VAPID private key lives in `push.json`
  (mode 600, in the mode 700 data directory) and no route returns it; `GET /push/subscriptions`
  truncates every endpoint, because a full push endpoint URL is a capability to notify that install.
- **Audit log.** Every mutating request is a row: when, who (a token id, an OIDC subject, or `local`
  when nothing guards the API), method, path, status and a one-line summary taken from the route's
  documentation. Bodies are never recorded, because they hold prompts and secrets. `GET /audit`, or
  Settings → Security.
- **The bundle is served locked down.** The UI (and the SPA fallback) carries `X-Frame-Options: DENY`,
  `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer` and a Content-Security-Policy that
  names the SHA-256 of its one inline script instead of allowing inline script at all. `style-src`
  keeps `'unsafe-inline'`: Vite's build hands out no nonce. The `tls` profile's Caddy sets the three
  simple headers on everything it proxies that did not already send them, `/docs` included, and
  deliberately sets no policy of its own.

**TLS.** Agentry does not terminate TLS itself: a proxy does it better, renews certificates and is
already what you run elsewhere. The proxy must pass `Host` **unchanged**, and the name it passes has
to be in `AGENTRY_ALLOWED_HOSTS` or every request answers `421`; it must set `X-Forwarded-For`,
`X-Forwarded-Proto` and `X-Forwarded-Host`; must not buffer `/api/events` and the chat streams
(`flush_interval -1` in Caddy, `proxy_buffering off` in nginx); and must not cut idle connections
faster than the 15 s heartbeat those streams send. `docker compose --profile tls up -d` runs Caddy
in front of Agentry with all of that already set (`deploy/Caddyfile`); a bare proxy in front of
`mode: none` only encrypts, so **turn authentication on first**. What is still true with everything
on: chats in the image default to `bypassPermissions`, there is one credential for everyone who
holds it, and nothing isolates one person's chats from another's. [SECURITY.md](SECURITY.md) lists
what is and is not protected.

## Deploying

[docs/deploy.md](docs/deploy.md) has the details; in short:

- **Docker Compose**: `docker compose up -d` publishes Agentry on `127.0.0.1:8787`;
  `--profile tls` adds the Caddy proxy on `:80` and `:443` (`AGENTRY_DOMAIN` picks the name).
- **Kubernetes**: the Helm chart in `deploy/helm/agentry` is a Deployment (one replica, `Recreate`),
  a Service and one PersistentVolumeClaim that outlives `helm uninstall`. Its values cover the image
  tag (pinned to a release rather than `latest`), the port, resources, the pod and container
  security contexts, `auth.mode` (`none`, `token`, `oidc`) and `auth.readOnly`. There is no Ingress
  template; bring your own — and if it gives the pod a host name, put that name in
  `AGENTRY_ALLOWED_HOSTS` through the chart's `env`.
- **The tunnel** (Settings → Remote access): the image runs a Tailscale of its own in userspace
  networking, with its node on the data volume, and you sign it in from the app with a login link or
  an auth key. Once open it goes around the published port, the proxy and the Ingress; turn it off
  with `AGENTRY_TUNNEL=off` (or `tunnel.enabled: false`). See
  [docs/deploy.md](docs/deploy.md#the-tunnel-in-docker).
- **A pinned Claude Code**: the image installs a fixed version and Settings → Account says when a
  newer one is published, with how to move. The check reads the npm registry on demand and once a
  day.
- **Restarts**: Docker only marks a container `unhealthy`, so the image's healthcheck ends the server
  itself after three failed probes and Compose's `restart: unless-stopped` starts it again; the chart
  uses ordinary liveness and readiness probes. `SIGTERM` is a clean stop: the chats' transcripts are
  on disk and resume afterwards.

## REST API

**Interactive reference: <http://localhost:8787/docs>** (Scalar) · OpenAPI 3.1 document at
`/openapi.json`. Component schemas are generated from the shared TypeScript types
(`pnpm --filter @agentry/api openapi:schemas` after changing `packages/shared/src/types.ts`), route
docs live in [`apps/api/src/openapi/routes.ts`](apps/api/src/openapi/routes.ts), and a test fails
when a route is added without documentation. The reference is self-hosted: Scalar's cloud
features and telemetry are disabled.

All routes are under `/api` and speak JSON. A refusal is `{ "error": "…" }` with a 4xx status and a
message meant to be read. Anything that fails for a reason nobody planned for is
`500 { "error": "internal error" }` — the detail goes to the server log with the URL, never to the
caller. Two refusals come from the guard rather than from a route: `421` when the `Host` is one this
wrapper does not answer to, and `429` with `Retry-After` after repeated failed credentials (a request with none is only `401`).
Types live in [`packages/shared/src/types.ts`](packages/shared/src/types.ts).

### System

| Method | Route | Description |
| --- | --- | --- |
| GET | `/health` | `{ ok, cli, loggedIn }` — the CLI and login state as the last authenticated read left it. It spawns nothing, so it is a liveness probe and not a login check |
| GET | `/system?refresh=1` | CLI detection, auth status, paths. Cached for 30 s, and a value just past that is served while the refresh runs; `?refresh=1` always takes a fresh reading. Callers arriving together share one detection |
| GET | `/system/cli-version` | Claude Code in use, the version the image pins and the newest published, as the last check left it (never reads the registry) |
| POST | `/system/cli-version/check` | Check the npm registry for a newer Claude Code now (also done once a day) |
| GET | `/system/release` | Agentry in use, the newest release, how this server was installed (`distribution`), as the last check left it (never asks GitHub) |
| POST | `/system/release/check` | Check GitHub for a newer Agentry release now (also done once a day) |
| GET | `/system/storage` | In a Docker install, whether the Claude config dir, the data dir and the workspace sit on a persistent volume or would be lost when the container is replaced (`persistent`, `anonymous`, `container`, `temporary`); `atRisk` says whether any would |
| GET | `/overview` | Everything the dashboard needs in one call |

### Account credentials

The account can be configured at runtime instead of (or on top of) the container environment.
The credential is kept in the secret vault (`secrets.json` in the data volume, mode 600, sealed when
there is a key; see [docs/setup.md](docs/setup.md)), handed to every new `claude` process in its
environment and to no other, and never returned by any endpoint.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/auth` | Fresh auth status, including where the credential comes from |
| PUT | `/auth/credentials` | `{ oauthToken }` or `{ apiKey }` (exactly one) |
| DELETE | `/auth/credentials` | Remove the stored credential; falls back to the container environment |
| POST | `/auth/verify` | Sends a minimal real request. `claude auth status` only reports what is configured, it does not validate the token |

### Setup

The first setup, from the app: what is signed in and what is not, and the sign-ins that do the rest
through each tool's own documented surface. A key is write-only and never in argv, a log, an event
or an answer; every write, and reading a sign-in, is refused to a chat's token. See
[docs/setup.md](docs/setup.md).

| Method | Route | Description |
| --- | --- | --- |
| GET | `/setup` | `{ seen, access, providers, hosts, youtrack, tailscale, methods, secrets }`: the auth mode, each enabled agent's readiness and whether a key is kept for it, each code host's CLI and the hosts it is signed in to, YouTrack, the Tailscale behind Remote access (offered, run by Agentry, its readiness and node name), the sign-in methods per tool, and whether the vault is sealed and its key sits beside the data |
| POST | `/setup/seen` | Record that the setup assistant was finished or skipped (`setupSeen` in `app-settings.json`); `409` when the environment sets it off |
| POST | `/setup/logins` | `{ tool, method: 'key' \| 'device', host?, secret?, variable? }`. A key goes on stdin to the CLI's own login (Codex, gh, glab), into a 0600 file named in `tailscale up --auth-key=file:` and removed after (Tailscale), or into the vault (Claude Code, Gemini, Copilot as `COPILOT_GITHUB_TOKEN`, OpenCode, YouTrack), and the answer comes once it ended; a classic `ghp_` token for Copilot is a `400`. A device sign-in answers at once; `login.updated` carries the URL and the code (Tailscale's login URL has none), then the end, decided by the tool's readiness probe. Copilot's device sign-in is gh's to github.com, whose token Copilot falls back to. Expires after 15 minutes. Tailscale only where Agentry runs its daemon (the image), `409` elsewhere |
| GET | `/setup/logins/:id` | One sign-in: state, URL and code, `error` code, readiness after it ended |
| DELETE | `/setup/logins/:id` | Cancel it; the command's process group is killed |
| DELETE | `/setup/credentials/:tool?host=` | Sign out: `codex logout`, `gh`/`glab auth logout --hostname`, `claude auth logout` plus the vault, `tailscale logout` after the tunnel closes, or the vault alone (Copilot's forgets only the token Agentry keeps, never gh's sign-in) |

### Security

Authentication is off by default (`mode: none`), which is what a local install on loopback wants.
With `token` every route needs `Authorization: Bearer …`; with `oidc` it needs a JWT the issuer's
JWKS validates (`aud` and `exp` are checked). `GET /api/health` stays open, `/docs` does not, and
only the five GETs a browser makes without headers — `/events`, `/chats/:id/stream`,
`/uploads/:id/content`, `/chats/:id/export` and `/projects/:id/export` — also accept the credential
as `?token=`. Only the SHA-256 of a token is stored; the token itself exists once, in the answer
that created it. Lost it? `AGENTRY_AUTH_TOKEN` with `AGENTRY_AUTH_TOKEN_RESET=1` replaces it on the
next start, audited with actor `env` (see [Securing it](#securing-it)).

| Method | Route | Description |
| --- | --- | --- |
| GET | `/security/auth` | Mode, whether a token is set, the OIDC fields and read-only. Never the token |
| PUT | `/security/auth` | `{ mode?, oidc?, readOnly? }`. A mode that would lock everyone out is refused; stays reachable in read-only mode, because it is the switch |
| POST | `/security/token` | Set or rotate the bearer token — `{ token? }`, generated when omitted. Returned once |
| DELETE | `/security/token` | Remove it; refused while the mode is `token` |
| GET | `/audit?limit=&from=&path=&method=&status=` | Mutating requests, newest first: when, actor (token id, OIDC subject, `local`, or `env` for a token reset from the environment), method, path, status and a one-line summary from the route. `path` matches anywhere and literally, `method` exactly, `status` a code (`404`) or a class (`4xx`). `limit` and `from` must be non-negative integers, or the answer is a `400` saying so. Bodies are never recorded |

### Remote access

| Method | Route | Description |
| --- | --- | --- |
| GET | `/tunnel` | `{ state, url, since, reason, enabled, managed, tailscale, port, settings }`: `url` and `since` only while `active`, `reason` (with a `code`) only while `failed`, `enabled` false where the deploy does not offer the tunnel (`AGENTRY_TUNNEL`), `managed` true where Agentry runs the `tailscaled` itself (the image) and signs it in from the setup, `tailscale` whether the CLI is installed, signed in, connected and has HTTPS on (`state`, `version`, `host`, `reason`), read again from the CLI at most every two seconds |
| PUT | `/tunnel/settings` | `{ startWithAgentry }`, off by default. Emits `tunnel.changed` |
| POST | `/tunnel/start` | Adds Agentry's `tailscale serve` rule on `port`; `409` while the auth mode is `none` or where `enabled` is false, `failed` with the reason when Tailscale is not ready or the port serves something else. The address shows, and the node's exact name joins the allowlist, once the rule reads back from the Serve config |
| POST | `/tunnel/stop` | Takes the name off the allowlist and removes only Agentry's Serve rule; turning the auth mode to `none` does it first |

### Usage limits and rotation between providers

Each provider is used with the account its own CLI is signed in to, and Agentry never swaps
accounts. What it does when one reaches its usage limit is the person's choice, in Settings →
Providers (global, with an override per project): **continue** on the next ready provider with a
handoff (what was asked, what was done, what is left, built from the transcript and the worktree's
git state), **restart** there from the original prompt, or **wait** for the reset. The default is
to wait, and nothing goes to another vendor until the settings say so.

- **A person's chat** at a limit is never moved on its own: `limit-hit` raises a banner offering the
  feasible actions, the setting's first, and a click calls `POST /chats/:id/move` or
  `POST /chats/:id/wait`.
- **Automated work** (flow runs, orchestration tasks, the assistant) does what the setting allows,
  and `wait` is the floor when a move cannot happen: no ready provider, none that carries the
  work's tool rules over, no model mapped for it, or every move already made.
- **A move is a new chat** on the next provider in the same worktree, linked both ways
  (`continuedFrom` / `continuedIn`); the run, task or item points to the newest.
- **The model mapping** says which model of one provider stands in for a model of another. It starts
  empty: the first limit with no mapping waits and says why, and `provider.model-map` may suggest a
  counterpart, which only a person's accept writes.
- **A wait** is a row, so two processes on one data directory replay a turn once and a restart picks
  it up again; with no reset time known it ends at `maxWaitHours`.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/providers/candidates?chatId=` | Who could take the chat's work, each with its model and use of the binding window, and the others with the reason they cannot (`excluded`); `movesCapped` when the work has made every move it may |
| GET | `/providers/moves?chatId=&projectId=&state=&limit=` | Moves and waits, newest first; `waiting` and `resuming` rows are the open waits |
| POST | `/providers/moves/:id/cancel` | Stop waiting: a flow run or task then ends `stopped`. `409` when the wait is over. Not open to a chat's token |
| GET | `/providers/model-map/suggestions` | Open `provider.model-map` suggestions: a counterpart nobody has answered yet |
| POST | `/providers/model-map/suggest` | `{ from: { provider, model }, target }` — a person pressing Suggest: asks `provider.model-map` now and answers the suggestion. `204` when nothing was suggested, `409` when the point is off. Not open to a chat's token |
| POST | `/providers/model-map/suggestions/:id` | `{ accept }` — accepting writes the entry (`origin: decision`), dismissing only closes it; either reaches the decision as feedback. `409` when the model already has a counterpart. Not open to a chat's token |
| GET | `/providers/cswap-retirement` | `{ notice }`: what claude-swap left behind (null when there is nothing or it was dismissed) |
| POST | `/providers/cswap-retirement/dismiss` | Do not show the notice again. Not open to a chat's token |
| DELETE | `/providers/cswap-retirement/managed-copy` | Remove Agentry's own copy of claude-swap and nothing else. Not open to a chat's token |

**Coming from claude-swap.** Earlier versions rotated between several Claude accounts through
[claude-swap](https://github.com/realiti4/claude-swap), and that is gone, with the `/accounts`
routes. The account claude-swap left active stays the one Claude Code uses; the notice names it,
lists the projects that had a rotation policy (their provider order is what applies now) and offers
to remove Agentry's copy of the tool. claude-swap's own data is never touched.

### Projects

| Method | Route | Description |
| --- | --- | --- |
| GET | `/projects` | The projects you imported, each with its worktrees and the number of chats under it |
| GET | `/projects/candidates` | Directories chats have run in that are not projects yet, the busiest first: what a first start offers to import |
| GET | `/projects/templates` | The five built-in project templates: the modules each switches on, its board's work item types and column limits, and the team it offers |
| POST | `/projects/import` | `{ path, name?, template?, modules? }` — import a directory; every chat under it is adopted, retroactively. A git worktree is refused. Without a template or modules every module is off; a directory that was a project before gets its settings back. Emits `project.created` |
| POST | `/projects` | `{ name, gitUrl?, template?, modules? }` — create an empty project in the workspace or clone a repository into it, and import it. Emits `project.created` |
| PATCH | `/projects/:id` | `{ name?, key?, modules? }` — rename a project, change its work item key prefix or the modules that are on. Switching a module off hides it and keeps its data |
| GET | `/projects/:id/settings` | The project's settings document (modules, template, key prefix, board). Created on first read with every module off |
| PUT | `/projects/:id/settings` | Replace the settings document whole, validated. Emits `project.updated` |
| GET | `/projects/:id/export?format=markdown\|json` | Download every chat of the project, streamed. `markdown` (default): a header with the dates, models and the cost the CLI reported, then each chat, oldest first, as `/chats/:id/export` renders it. `json`: a `ProjectExport` |
| DELETE | `/projects/:id` | Remove a project from Agentry. Harmless: nothing on disk changes, and its settings and work items are kept for when it is imported again. Emits `project.removed` |
| DELETE | `/projects/:id/state` | Purge everything Claude Code keeps about a project (`claude project purge`). Irreversible, and separate from removing the project |

### Team

A project's team (Team module). Each member is a Claude Code agent file in the project's
`.claude/agents/`, so it also works from a terminal, plus the role, model, responsibility and write
paths Agentry keeps in the project's settings. Agentry writes a starting agent file only where there
is none, and never overwrites one a person wrote or edited: that member is reported as `drifted` (or
`missing` when the file was deleted). Changes need the module on (409 otherwise) and emit
`team.changed`.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/projects/:id/team` | The members, each with its agent file's state, the columns it answers for under the flow and its flow runs, and the agent files no member uses |
| POST | `/projects/:id/team/from-template` | `{ roles? }` — add the template's roles the person accepted, each with its agent file (an existing file is kept). 201 when it added a member, 200 when nothing changed |
| PUT | `/projects/:id/team/:agent` | `{ role, model, responsibility, writes?, commands?, createFile? }` — create or replace a member's metadata. Two members may not share a role. `commands` bounds the shell of its work runs (`[]` is none, absent is unrestricted). The file itself goes through `/config/resources/agents/:name?project=` |
| DELETE | `/projects/:id/team/:agent` | Take a member off the team; its agent file stays |
| GET | `/projects/:id/flow` | The flow by column's runs going and queued, each with its item, role, stage and chat; `enabled` and the per-project cap `maxParallel` |
| GET | `/projects/:id/flow/runs` | The team's activity: every flow run, newest first, paged (`limit`, `cursor`), filtered by `agent`, `role`, `status` (or `outcome`), `itemId` and `before`; each failed or cancelled run carries its `cause` |
| GET | `/projects/:id/flow/waiting` | The cards waiting for the flow: not epics nor done, in a column with a responsible member, with no run queued or running (`{ total, columns }`; 0 while the flow is off) |
| POST | `/projects/:id/flow/start-waiting` | Queue one run per waiting card in board order, as a person (`queuedBy: "person"`); answers `{ queued, startingNow, waiting }`, 409 while the flow is off |
| GET | `/work-items/:itemId/runs` | Every flow run of a work item, newest first, whatever its state |
| POST | `/flow-runs/:runId/retry` | Queue a failed run's step again while its item is still in the run's column (409 otherwise); counts as a person's move |

### Assistant

The project assistant. A run is a read-only Claude Code chat in the project's directory (`Read`,
`Grep`, `Glob`, and `Bash` only for `git log`, `git status` and `ls`, in `dontAsk`) that answers
through `--json-schema`. It proposes a team, resources and work items, and writes nothing: each
proposal is accepted or discarded on its own, and only an accept writes, through the team, the
resources or the board. One run at a time per project and kind (409 otherwise). Runs emit
`assistant.run`, decisions `assistant.proposal`.

| Method | Route | Description |
| --- | --- | --- |
| POST | `/projects/:id/assistant/runs` | `{ kind, model?, description?, resourceKind?, supersede? }` — start a `project`, `work-items` or `resources` run (`sonnet` by default). A project with nothing to read and no description starts no chat and is offered its template's team |
| GET | `/projects/:id/assistant/runs` | `?kind=` — the runs, latest first, with what each read, found and proposed |
| GET | `/assistant/runs/:runId` | A run with every proposal it made |
| POST | `/assistant/runs/:runId/stop` | Stop a running run; it proposes nothing |
| POST | `/assistant/proposals/:proposalId/accept` | `{ member?, resource?, workItem? }` — write the proposal with the person's edits: a member through the team, a resource saved at its scope, a work item created in Backlog with its reason as first comment |
| POST | `/assistant/chats` | `{ prompt, projectId?, model?, effort? }` — start a chat with the Agentry assistant (`sonnet` by default, at the effort recommended for an assistant unless one is given), answering what `POST /chats` answers: 201 with the chat; 400 for an empty prompt, 404 for an unknown project. The chat reads Agentry only through its own MCP server (`agentry`), has no built-in tool, no settings file and no uploads directory, and keeps that confinement when resumed, forked or picked up after a restart. The project is context, not a requirement; the answer language is read from `Accept-Language` |
| POST | `/assistant/proposals/:proposalId/discard` | Discard a pending proposal; nothing is written |
| POST | `/assistant/proposals/:proposalId/restore` | Restore a discarded proposal |

### Work items

A project's board. Changing anything needs the project imported and its **Board** module on (409
otherwise); what a project holds stays readable with the module off, so nothing looks lost. The
server writes each item's history, one entry per field that changed, and every change reaches the
event feed. Filters take comma-separated lists: `status`, `type`, `priority`, `labels`, `assignee`
(`person`, `none`, `role:<role>`), `epicId`, `milestoneId` and `q` (title, description and key).

| Method | Route | Description |
| --- | --- | --- |
| GET | `/projects/:id/work-items?status=&type=&…` | The project's work items in board order, filtered, descriptions left out (`hasDescription`) |
| GET | `/projects/:id/work-items/page?…&limit=&cursor=` | The same list a page at a time (100 by default, 500 at most): `{ items, total, nextCursor }` |
| POST | `/projects/:id/work-items` | `{ title, type?, description?, status?, priority?, labels?, assignee?, epicId?, milestoneId?, acceptanceCriteria? }` — create one; it takes the next number of the project, never reused. Emits `workitem.created` |
| GET | `/projects/:id/work-items/board?…&doneLimit=` | The five columns, each with its limit, its real count, whether it is over the limit, and the items that pass the filter in rank order, descriptions left out. Done holds its newest `doneLimit` items (20 by default) and `more` counts the rest |
| POST | `/projects/:id/work-items/triage` | `{ title, description? }` — what `board.triage` would prefill for a draft: `{ triage: { type, priority, duplicate, decisionId } \| null }`, null unless the point is active and answered in time. Creates nothing |
| POST | `/projects/:id/work-items/orchestrate` | `{ itemIds }` — a draft orchestration to review, not launched: one node per item, `dependsOn` from `blocks` inside the selection, and the blockers left outside it. `POST /orchestrations` launches it |
| GET | `/projects/:id/milestones` | The project's milestones, each with its progress derived from its items |
| POST | `/projects/:id/milestones` | `{ name, description? }` — create a milestone, open, with no date. Emits `milestone.changed` |
| GET | `/work-items?…` | Every work item of the imported projects with the Board module on: the All projects view, descriptions left out |
| GET | `/work-items/page?…&limit=&cursor=` | The All projects list a page at a time: `{ items, total, nextCursor }` |
| GET | `/work-items/board?…&doneLimit=` | The All projects board, with no column limits; Done paged as on a project's board |
| GET | `/work-items/by-key/:key` | The item a key names (`AGN-12`, any case), as `/work-items/:itemId` answers it; 404 when none has it |
| GET | `/work-items/:itemId` | One item with its children, links, comments and history |
| PATCH | `/work-items/:itemId` | Change any field but the status; `acceptanceCriteria` replaces the checklist, keeping the check of entries sent with their `id`. Emits `workitem.updated` |
| DELETE | `/work-items/:itemId` | Delete an item for good; its number is not reused. Emits `workitem.removed` |
| POST | `/work-items/:itemId/move` | `{ status, afterId? }` — move to a column, right after `afterId` (`null` first, absent last). Over the column's limit is allowed and reported. Emits `workitem.moved` |
| PATCH | `/work-items/:itemId/criteria/:criterionId` | `{ checked }` — check or uncheck one acceptance criterion |
| GET | `/work-items/:itemId/comments` | The item's comments, oldest first |
| POST | `/work-items/:itemId/comments` | `{ body }` — comment as the person |
| POST | `/work-items/:itemId/relations` | `{ type: blocks\|blocked_by, itemId }` — relate two items of the project; the item itself (400) and a cycle of `blocks` (409) are refused |
| DELETE | `/work-items/:itemId/relations/:otherId` | Remove the relation between two items |
| GET | `/work-items/:itemId/links` | The chats, orchestration tasks and documents tied to the item, with their state |
| POST | `/work-items/:itemId/links` | `{ kind, role, chatId?, orchestrationId?, taskId?, documentPath? }` — tie a chat, an orchestration task or a document of the documents folder to the item |
| DELETE | `/work-items/:itemId/links/:linkId` | Untie it; the chat, orchestration or file is not touched |
| GET | `/work-items/:itemId/history` | Every change to the item, oldest first, with who made it and why |
| POST | `/work-items/:itemId/work` | "Work on it": a chat prompted with the item, in its own worktree on `task/<key>` (made again if it was deleted by hand), with the options a new chat takes, each checked for its type (400). The item enters `in_progress` when a turn starts and `in_review` when one ends well. An epic is refused (400), and so are an item in `done`, one already being worked on and a plain directory where its worktree goes (409) |
| POST | `/work-items/:itemId/pull-request` | The person's approval: Agentry commits what is left, merges `origin/<default>` into `task/<key>`, pushes it and opens the pull or merge request with the project's host CLI (202; 200 with it already open). A conflict pushes nothing and sends the item back to `in_progress` for the Developer. 400 for an epic; 409 with a `code` when the item is not in review, is being worked on, has nothing to propose, or the project cannot open them (`reason` names why, with the host and a remedy) |
| POST | `/work-items/:itemId/pull-request/refresh` | Ask the host for the item's open PR or MR now: its CI state, a merge (the item moves to Done) or a close |
| GET | `/work-items/:itemId/changes` | What the item's branch changed: commits, files and what is not committed yet. The branch is the last chat's or orchestration node's that worked on the item. `?commit=`/`?uncommitted=1` scope it as `/chats/:id/changes` does |
| GET | `/work-items/:itemId/changes/diff?path=` | One file's diff on the item's branch, with `?context=`, `?commit=` and `?uncommitted=1` as `/chats/:id/changes/diff` takes them |
| POST | `/chats/:id/work-items` | `{ text, title?, type?, priority? }` — create a task in `backlog` from a chat's message, linked to the chat |
| GET | `/chats/:id/work-items` | The work items a chat works on or was the origin of, descriptions left out |
| GET | `/milestones/:milestoneId` | One milestone with its progress |
| PATCH | `/milestones/:milestoneId` | `{ name?, description?, state? }` — edit, close or reopen a milestone |
| DELETE | `/milestones/:milestoneId` | Delete a milestone; its items stay, without it |

### Documents

A project's documents folder, `documents.path` in its settings (`docs` by default): its Markdown
files, and the work items each is tied to. A `path` is relative to the project and `/`-separated,
and is refused (400) when it is absolute, climbs with `..`, has a hidden part, is not Markdown, or
lies outside the folder, symbolic links included. Changing anything needs the **Documents** module
on (409 otherwise); reading does not.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/projects/:id/documents` | The folder's tree, directories first, each file with its title, size, time and ties |
| GET | `/projects/:id/documents/file?path=` | One file's content and ties |
| PUT | `/projects/:id/documents/file?path=` | `{ content, baseUpdatedAt? }` — create or replace a file; a file changed since `baseUpdatedAt` is refused (409). Emits `document.changed` |
| DELETE | `/projects/:id/documents/file?path=` | Delete a file and untie it from every item. Emits `document.changed` |
| POST | `/work-items/:itemId/documents` | `{ path, kind? }` — tie a file on disk to the item, role `reference`: the shorthand of `POST /work-items/:itemId/links` with `kind: document`. Emits `document.changed` and `workitem.updated` |

### Events

One Server-Sent Events stream for the whole app, so a client never has to poll.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/events?since=ID` | Every change as an `AgentryEvent` (`id:`, `event: <type>`, `data: <json>`): runs created, updated, ended and removed; prompts waiting for a person (`run.waiting`, `permission.requested`/`resolved`); rate limits and account rotation; background tasks, subagents and workflows starting and ending; orchestration, task and merge-conflict changes (`orchestration.updated` also carries `verificationStatus` while the checks run); `changes.updated` when a running task's or the integration branch's commits or uncommitted files move; `chat.activity` when what a chat's live execution is doing changes (a tool call, a block being written or thought, a prompt blocking it), at most once per chat per second; `health.changed` when a chat's health changes; `supervisor.proposed` when the supervisor answers one with a hint; `schedule.changed` (created, updated, enabled, disabled, deleted, rescheduled) and `schedule.fired` (every run row written or moved); `workitem.created`, `workitem.updated` (naming the fields that changed), `workitem.moved` (with the previous column and whether the new one is over its limit) and `workitem.removed`; `milestone.changed` (created, updated, closed, reopened, deleted); `team.changed` (created, updated, removed, template); `flow.run` (queued, started, ended, with its outcome); `journal.changed` (added, removed); `memory.proposal` (created, approved, rejected); `document.changed` (written, removed, tied, untied); `assistant.run` (started, read, ended, failed) and `assistant.proposal` (accepted, discarded, restored); `project.created` and `project.removed` (a project imported, created or removed); `project.updated` (name, key, modules or settings); `sessions.changed`; `login.updated` when a sign-in of the setup starts, shows its device code or ends (the URL and the code only, never the key or the CLI's output); `system.release` once per newer Agentry release a check finds (not a notification). Opens with `stream.hello`, which carries the server's `version`; honours `Last-Event-ID` against a bounded in-memory buffer and sends `stream.resync` when that id is gone (refetch everything). A `: ping` comment every 15 s |

```bash
curl -N localhost:8787/api/events
```

### Providers

The agents Agentry can drive, as detection finds them on this machine: one cache with one 5-minute TTL, refreshed by watchers and on demand, with `providers.changed` on the event stream when a status differs. A chat's token gets `403` on the settings write and the refresh.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/providers` | Every provider's status (state, reason, version, binary, config home, account, capabilities, the permission modes its driver honours, and what its handshake or first session confirmed), from the cache |
| GET | `/providers/:id` | One status; `404` for an unknown id |
| GET | `/providers/:id/models` | The provider's model catalog, with tiers, as its last handshake listed it (kept in `provider-catalogs.json`); `404` for a provider with no driver |
| POST | `/providers/refresh` | Detect again now. Not open to a chat's token |
| GET | `/providers/settings` | The document from `providers.json`: enabled and binary override per provider, order, default |
| PUT | `/providers/settings` | Replace it, validated; providers are detected again in the background. Not open to a chat's token |

The routes for what a provider does at its usage limit are under [Usage limits and rotation between providers](#usage-limits-and-rotation-between-providers). Each status carries its `limit` (state, binding window, use, reset and how old the reading is), and `GET /overview` all of them as `limits`.

### Code hosts

The hosts Agentry opens pull and merge requests on, GitHub through `gh` and GitLab through `glab`, as detection finds them on this machine: one cache with one 5-minute TTL, refreshed by watchers and on demand, with `hosts.changed` on the event stream when a status differs. A chat's token gets `403` on the settings write and the refresh.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/hosts` | Every code host's status (state, reason, version, binary, the host names its CLI knows), from the cache |
| GET | `/hosts/:id` | One status (`github` or `gitlab`); `404` for another id |
| POST | `/hosts/refresh` | Detect again now. Not open to a chat's token |
| GET | `/hosts/settings` | The document from `hosts.json`: enabled and binary override per host |
| PUT | `/hosts/settings` | Replace it, validated; hosts are detected again in the background and every project's readiness is read again. Not open to a chat's token |
| GET | `/trackers` | Every issue tracker's status: GitHub and GitLab Issues follow their code host; YouTrack runs `youtrack-app` with the address and token Agentry keeps |
| GET | `/trackers/:id` | One status; `404` for another id |
| POST | `/trackers/refresh` | Detect again now. Not open to a chat's token |
| GET | `/trackers/settings` | The document from `trackers.json`: enabled and binary override per tracker |
| PUT | `/trackers/settings` | Replace it, validated; trackers are detected again in the background. Not open to a chat's token |
| GET | `/trackers/youtrack/credentials` | The YouTrack address, whether a token is saved and whether it is encrypted; never the token. Not open to a chat's token |
| PUT | `/trackers/youtrack/credentials` | `{ host, token? }` — save the address and a permanent token (in the secret vault, 0600, sealed when there is a key); YouTrack is detected again before the answer. Not open to a chat's token |
| DELETE | `/trackers/youtrack/credentials` | Forget them. Not open to a chat's token |
| GET | `/projects/:id/tracker` | The project's tracker (`id`, `scope`, `query`, `statusMap`), or null |
| PUT | `/projects/:id/tracker` | Replace the tracker, validated, leaving the rest of the settings; a null body clears it. Not open to a chat's token |
| GET | `/projects/:id/tracker/issues` | `?query=&page=` — a page of the tracker's own query, each issue marked with the item it was imported as |
| POST | `/projects/:id/tracker/import` | `{ keys }` — one work item per issue, its body a quoted source block; `{ imported, skipped }`. Needs the Board module. Not open to a chat's token |
| POST | `/work-items/:itemId/issues` | `{ key }` — link an issue of the project's tracker to the item. Not open to a chat's token |
| DELETE | `/work-items/:itemId/issues/:key` | Unlink it (`?tracker=` and `?scope=` when a key is linked under two trackers or two repositories). Not open to a chat's token |
| POST | `/work-items/:itemId/issues/:key/sync` | One more write to the tracker for the item's column, never retried; the result is on the issue's `syncState`. Not open to a chat's token |
| GET | `/change-requests/:id` | One change request by the row id of a work item's or an orchestration's: kind, owner, host, `ref`, phase, CI rollup and the fix state |
| GET | `/change-requests/:id/checks` | The checks of the head commit (state, allowed failure, required, rerunnable, has a log), cached 30 s; `?refresh=1` reads the host now; `limitedUntil` while rate-limited |
| GET | `/change-requests/:id/checks/:checkId/log` | The tail of one check's log, cleaned and redacted, with its annotations; `noOutputYet` for a job that has printed nothing; `409 log-unavailable` for a check with no log |
| POST | `/change-requests/:id/checks/rerun` | Run the failed jobs, one job or everything again (`{ scope: 'failed' \| 'check' \| 'all', checkId? }`), then read the list again. Not open to a chat's token |
| POST | `/change-requests/:id/checks/cancel` | Cancel what is running, then read the list again. Not open to a chat's token |
| POST | `/change-requests/:id/checks/:checkId/run` | Play a GitLab manual job, then read the list again. Not open to a chat's token |
| POST | `/change-requests/:id/checks/fix` | Fix the failing checks: the item's Developer (or a chat in an orchestration's integration worktree) gets each failure's log tail → `{ started, prompt, worktree, pullRequest }`; `409` with a `code` when nothing can be fixed now. Not open to a chat's token |
| POST | `/change-requests/:id/push-fix` | Push a finished fix that waits for the person (a plain push, never forced); a failure keeps it waiting for a retry. Not open to a chat's token |
| GET | `/change-requests/:id/threads` | Review threads of the head commit with their comments, cached 30 s (`?refresh=1` reads the host now); outdated and resolved ones are marked |
| GET | `/change-requests/:id/review-drafts` | The person's draft review: notes on lines or general, kept as rows |
| POST | `/change-requests/:id/review-drafts` | Add a note (`path`, `side`, `line`, `startLine`, `body`, `suggestion`) → `201`. Not open to a chat's token |
| PUT | `/change-requests/:id/review-drafts/:draftId` | Change a note. Not open to a chat's token |
| DELETE | `/change-requests/:id/review-drafts/:draftId` | Delete a note. Not open to a chat's token |
| GET | `/change-requests/:id/review-posts` | The attempts to post a review, newest first, and what a partly posted one still has saved on the host, so a stopped review is known after a reload |
| POST | `/change-requests/:id/reviews` | Post the drafts as one review (`{ event: 'comment' \| 'approve', body, headSha? }`; approve is GitLab only; `headSha` is the head the person looked at, refused with `head-moved` when it moved); `409` with a `code`, and a `postId` for `review-partly-posted`. Not open to a chat's token |
| POST | `/change-requests/:id/reviews/:postId/publish-saved` | GitLab: publish the notes a partly posted review saved. Not open to a chat's token |
| POST | `/change-requests/:id/reviews/:postId/discard-saved` | GitLab: discard them (only the notes Agentry saved). Not open to a chat's token |
| POST | `/change-requests/:id/threads/:threadId/reply` | Reply to a thread (`{ body }`) → the thread as the host has it. Not open to a chat's token |
| POST | `/change-requests/:id/threads/:threadId/resolve` | Resolve a thread (idempotent). Not open to a chat's token |
| POST | `/change-requests/:id/threads/:threadId/unresolve` | Reopen a thread (idempotent). Not open to a chat's token |
| GET | `/change-requests/:id/approval` | Whether the viewer approved, approvals left, who approved; `canApprove` and `canRevoke` are GitLab only |
| POST | `/change-requests/:id/approval` | GitLab: approve on the head you looked at (`{ sha }`); `409 head-moved` if it moved. Not open to a chat's token |
| DELETE | `/change-requests/:id/approval` | GitLab: revoke the approval. Not open to a chat's token |
| GET | `/change-requests/:id/reviewers` | The requested reviewers, the review decision and the unresolved count |
| POST | `/change-requests/:id/reviewers` | Request reviewers (`{ add, remove? }`), then read back what the host says. Not open to a chat's token |
| POST | `/change-requests/:id/address` | Address review threads with an agent (`{ threadIds }`, all unresolved when empty) on the fix path of the checks; nothing is replied or resolved by Agentry → `{ started, prompt, worktree, pullRequest }`. Not open to a chat's token |
| GET | `/change-requests/:id/merge` | The merge state: allowed methods and the default, the branch box's default, `canMerge`, the first blocker and the others (code, the host's words, one action), the auto-merge state, `waitingForPipeline`, `autoMergeOff` (Agentry turned auto-merge off for a push or an update, until it is armed again), `canRebaseOnHost` with `rebaseOnHostWhy` and `headSha`; `?refresh=1` reads the host now |
| POST | `/change-requests/:id/merge` | Merge (`{ method, expectedHead, deleteBranch, subject?, body? }`) on the head the person saw → `{ state, merged, branchDeleted }`; `409 head-moved` merges nothing. The person's click: not open to a chat's token |
| POST | `/change-requests/:id/auto-merge` | Arm the host's auto-merge (`{ method, expectedHead }`) → the merge state. Not open to a chat's token |
| DELETE | `/change-requests/:id/auto-merge` | Turn auto-merge off, confirmed by a re-read → the merge state. Not open to a chat's token |
| POST | `/change-requests/:id/update-branch` | Update the branch from its base (Agentry's merge, or the host's rebase on a GitLab `ff` project) → `{ state, conflicts, via }`; the host's rebase is offered only for a clean checkout with nothing unpushed, and a rebase that conflicts falls back to Agentry's merge; `409 conflicts` names the paths and pushes nothing; `409 busy` while a chat or a run works in the checkout. Not open to a chat's token |
| POST | `/change-requests/:id/ready` | Mark ready for review or back to a draft (`{ ready }`) → the merge state. Not open to a chat's token |
| GET | `/projects/:id/code-host` | Whether the project can open pull and merge requests (the readiness, with its reason and remedy) and its parsed `origin`; `404` for an unknown project |

### Webhooks

Where GitHub and GitLab deliver for a hook Agentry registered (tag `Webhooks`). Unauthenticated by design and signature-checked: GitHub's `X-Hub-Signature-256`, or GitLab's `X-Gitlab-Token` plus its `webhook-signature` when it carries one, is verified over the raw body, in constant time, before anything is parsed. A delivery never changes a change request; it only moves the next read of the ones it names to now.

| Method | Route | Description |
| --- | --- | --- |
| POST | `/webhooks/github/:registrationId` | A GitHub delivery. `204` at once (a replayed delivery id or signed body too); `401` with no detail for an unknown registration or a bad signature; `429` past 60 verified deliveries a minute; `413` over 5 MiB |
| POST | `/webhooks/gitlab/:registrationId` | A GitLab delivery, checked by `X-Gitlab-Token` and, when present, `webhook-signature`; answers as above |
| GET | `/projects/:id/webhooks` | A project's registrations plus `available`, the `reason` when not (`no-public-url`; `no-remote`), the `publicUrl`, the `events` and `canRedeliver` (always `false`). The secret is never returned |
| POST | `/projects/:id/webhooks` | Register the repository's hook, on GitHub or GitLab (adopts an Agentry hook already there, never touches another) → `201` with the registration; `409` `no-public-url`, `no-remote`, `already-registered`; `403 hook-no-permission`; `502 hook-unreachable`. Not open to a chat's token |
| POST | `/projects/:id/webhooks/:registrationId/test` | Ping the hook (GitLab: a push test) and read the host's answer back → the registration; `502` when the host did not report an answered delivery. Not open to a chat's token |
| DELETE | `/projects/:id/webhooks/:registrationId` | Delete the hook on the host and its secret here → the registration, now `removed`. Not open to a chat's token |

### Decisions

The decision engine: a decision point puts typed questions to a provider (the Claude CLI, or TypeSafe's Jev with its own key) and runs today's behaviour whenever the answer is missing or below its threshold. Every point is off by default. A point sends nothing until the owner consents to it after previewing its state, and consent names the providers it covers. A chat's token gets `403` on the settings, credentials and consent routes.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/decisions/settings` | The global settings from `decisions.json`; the Jev key is never returned, only `keySet` and `keyHint` |
| PUT | `/decisions/settings` | Replace them whole, validated. Consent is kept as it was. Not open to a chat's token |
| PUT | `/decisions/credentials` | `{ key }` — save the Jev key (mode 600); the answer carries the general privacy notice. Not open to a chat's token |
| DELETE | `/decisions/credentials` | Remove the key; points on `jev` fall back to off-behaviour. Not open to a chat's token |
| POST | `/decisions/test` | `{ provider }` — one small fixed question: `{ ok, latencyMs, model, reason }`. Nothing is recorded |
| GET | `/decisions/points` | The catalogue with the settings in force, optionally for `?projectId=` |
| GET | `/decisions/points/:point/preview` | The exact state of the point's last request, or the fields it may carry, built locally and not sent |
| PUT | `/decisions/points/:point/consent` | `{ granted, stateVersion, providers }` — grant or withdraw consent for what was previewed (`409` when the state changed since). Not open to a chat's token |
| GET | `/decisions` | History, newest first, filtered by `point`, `projectId`, `subjectKind`, `subjectId`, `visible`, `provider`, `mode`, `status`, `since`, `until` and paged with `cursor` and `limit` |
| DELETE | `/decisions` | Delete the rows matching the same filter (every row when none) |
| GET | `/decisions/stats` | Per-point metrics plus Jev cost and Claude runs saved, over `?days=` (30) or `?since=` |
| GET | `/decisions/:id` | One decision: state, questions, answers with probabilities, provider and outcome |
| POST | `/decisions/:id/feedback` | `{ feedback: "useful" \| "not_useful" }` — the person's word on it |
| POST | `/decisions/:id/palette-action` | `{ commandId: string \| null }` — what the palette did with a `palette.intent` proposal: the row records `proposed`, `other` or `dismissed`; the first report wins. `404` unknown id, `400` another point's row or a malformed `commandId`. Not open to a chat's token |
| POST | `/decisions/notification-opened` | `{ key }` — the app was opened from the push with that key; sets `openedAt` on the newest `notification.urgency` row: `{ decisionId }`, null when none matches. Not open to a chat's token |
| DELETE | `/decisions/:id` | Delete one row |
| POST | `/decisions/palette` | `{ query, commands: [{ id, title }] }` — the `palette.intent` point: `{ commandId, confidence, decisionId }`, with `commandId` null when the point is off, unavailable or unsure |

### Push

Web Push over VAPID, signed and sent by this server: a chat that stops for a permission prompt reaches a phone whose app is closed. The keypair is made on first use and kept as `push.json` in the data directory (mode 600); the private half never leaves the server, and there is no third-party push account. What is worth a notification is decided by the same function the browser runs on the same event, so the in-page toast and the notification on a lock screen cannot disagree.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/push/key` | The VAPID public key to subscribe with, and whether push is configured at all |
| GET | `/push/subscriptions` | The registered installs. Endpoints are truncated: a full push endpoint URL is a capability to notify that install |
| POST | `/push/subscriptions` | Register or refresh one — body is the browser's `PushSubscription` JSON plus `kinds` (every kind when omitted), a `level` (`all`, `important`, `urgent` or `silent`; `important` when omitted) and a `label` for the list. An endpoint already registered is refreshed, keeping its `createdAt` |
| DELETE | `/push/subscriptions` | Unregister by `endpoint` (what a browser turning the switch off knows) or by `id` (what the list shows) |
| POST | `/push/test` | Send one test notification to an install by `endpoint` or `id`, or to every registered one. An endpoint the push service reports as gone (404/410) is deleted |

### Chats

A chat is one Claude Code conversation, and its id is the session id: however many times it is
resumed, and whoever started it, it is one chat. Each time Agentry has a `claude -p` process working
on it, that is an **execution** of the chat, with its own outcome, cost and turns. `state` says what
is happening (`working`, `waiting` for a person, `idle`) and `control` what can be done with the chat
now: `interactive` (Agentry has a live execution), `resumable` (nothing holds it), or `readOnly` with
the reason and the way forward (`fork`, or `hint` for a task an orchestration is still running).

**Health.** Every chat with a process of Agentry's, and every running orchestration task, carries a
`health` of `ok`, `warn` or `bad` (the UI words them ok, slow, stuck and looping) with the signals
behind it, each with a one-line reason and a suggested hint text. The signals are a `hung-command`
(a command past its usual time), a `repeat-stall` (the same kind of command hanging or failing again),
`no-progress` (busy with no commit or change), a `loop`, a `weakened-test` (an existing test edited
until it asserts less), `silence`, a `budget` close to its limit, and facts such as a failed last
execution or a nearly full context. "Longer than usual" is measured against the last runs of that
kind of command on this machine (`pnpm e2e`, `cargo test`…), with a fixed 3 minutes until there are
five; the rules prefer silence to a false alarm, so a changed expected value or a deleted test is not
"bent to pass". A change of health is a `health.changed` event and a notification. Every reason and
hint also carries a stable `reasonCode` / `hintCode` and the figures it was built from (`params`), so
a client can say the same sentence in another language instead of showing the server's English. To
step in without ending the turn, `POST /chats/:id/commands/:toolUseId/cancel` kills that one
command's process tree (found under the CLI's pid, never by matching a command line; Linux only),
and `POST /chats/:id/hint` sends a message the worker reads at its next step. With the supervisor
on, a worker that turns `bad` also gets a proposed hint on `health.proposal`, to send, edit or
dismiss.

| Method | Route | Description |
| --- | --- | --- |
| GET | `/chats?project=&loose=1&origin=&workers=0&state=&limit=` | Chats, newest first. Workers of an orchestration and housekeeping chats are left out unless `origin` (comma-separated: `agentry`, `external`, `orchestration`, `internal`) asks for them; `workers=0` keeps an orchestration's synthesis but not its workers; `loose=1` lists those under no project |
| GET | `/usage?from=&to=` | What the chats spent, per day, per project and per orchestration (`from`/`to` are days, `YYYY-MM-DD`, inclusive). Tokens come from the transcripts, per model; the cost is what the CLI reported, so it is `null` for chats started from a terminal and `chatsWithoutCost` says how many a total leaves out |
| GET | `/usage/series?bucket=&from=&to=` | Cost and tokens over time: one point per `day` (default) or `week` (Monday-based) of the range, empty ones included so a chart has no gaps. `costUsd` is the CLI's figure and `null` where none was reported; at most 1000 points |
| GET | `/usage/breakdown?from=&to=` | The same range cut by project and by model, most spent first. The cost per model is the CLI's own `modelUsage[model].costUSD`; nothing is priced from token counts |
| POST | `/chats` | Start a chat. Body: `NewChatRequest` (`prompt` required; `cwd`, `model`, `permissionMode`, `effort`, `appendSystemPrompt`, `allowedTools`, `disallowedTools`, `toolPreset`, `mcp`, `jsonSchema`, `maxBudgetUsd`, `worktree`, `permissionPrompts`, `account`, `attachments`). `toolPreset` (an id from `GET /config/tool-presets`) becomes `--allowedTools` / `--disallowedTools`, and an explicit list wins over the preset's; `mcp: { servers: [...] }` starts the chat with only those servers (`--mcp-config` with `--strict-mcp-config`), an empty list with none. Naming neither tools nor a preset takes the default preset from `GET /config/tool-presets`, and `toolPreset: null` opts out into the CLI's own defaults |
| GET | `/chats/:id` | The chat with its branches, environment and `health` (`ok`, `warn` or `bad`, each signal with a one-line reason: a command running past 3 min, a working chat silent for 3 min, and facts of the chat such as a failed last execution, a full context or a failed branch), `tools` (the preset and MCP servers it was started with, `null` for a chat Agentry did not configure), and a window of its transcript: the newest 200 entries, or `?limit=` of them, with `from` and `total`; `?before=` the `from` of a page reads the one before it (`?sidechains=1` adds subagent messages) |
| GET | `/chats/:id/search?q=&sidechains=1` | Search the whole transcript, pages not loaded included: the matching entries' indices (the space of `from`/`total`) with a snippet each, case-insensitive; at most 500, the newest, with `truncated` |
| GET | `/chats/:id/changes` | What the chat changed on disk: for one in a git worktree its `summary` (branch, base, commits, files with `+/−`, uncommitted files, and `working`: every file that differs from the base in the working tree), and for any chat the `touched` files of its `Write`/`Edit`/`NotebookEdit` calls, read from the transcript. `?commit=<sha>` narrows the files to one commit of the branch (400 for any other), `?uncommitted=1` to the working tree against `HEAD` |
| GET | `/chats/:id/changes/diff?path=` | The unified diff of one file of a chat in a worktree against its base, uncommitted work included. `?context=` sets the unchanged lines around each change (0–500, or `full` for the whole file; `full: true` says it was honoured, never past 20 000 lines), and `?commit=`/`?uncommitted=1` scope it as the summary does |
| GET | `/chats/:id/changes/steps` | Every successful `Edit`, `MultiEdit`, `Write` and `NotebookEdit` of the chat's main transcript, oldest first, each with its unified patch, its `+/−`, the sentence Claude wrote before it (`intent`) and the transcript entry that holds it (`entryIndex`); a call still waiting for its result is the last step, `pending`, while the chat runs |
| GET | `/chats/:id/checklist` | The chat's own plan, from its `TaskCreate`/`TaskUpdate`/`TodoWrite` calls: `{ items[{ text, status }], updatedAt }` |
| GET | `/chats/:id/export?format=markdown\|json` | Download the whole transcript. `markdown` (default) is for reading: cost and models in a header, turns, each tool call folded with its result, subagents left out. `json` is every event, subagents included, nothing cut |
| GET | `/chats/:id/stream?since=SEQ` | Server-Sent Events, one `RunEvent` per message (honours `Last-Event-ID`). Includes ephemeral `partial` events with the text generated so far (token streaming); they are never replayed |
| POST | `/chats/:id/resume` | Body: `ResumeChatRequest` (`prompt`, same options as a new chat). Adds an execution to the same chat, which keeps its id. Decided on the server at this moment from the CLI's own session list and the process table: a chat born in a terminal that nothing holds is adopted and stays `external`; one a terminal holds, or that belongs to an orchestration, is refused with `409` and the reason. A resume that names no `mcp` writes the `--mcp-config` file again from the current definition of the same servers, so an edited URL or a rotated token is picked up |
| POST | `/chats/:id/fork` | Body: `ForkChatRequest`. Continues in a copy: a new chat with the same history that records `derivedFrom` and leaves the original untouched. Allowed on any chat. The copy inherits the source's preset, tools and MCP servers unless the request picks others, so it cannot quietly gain what the source was denied |
| GET | `/chats/:id/handoff?provider=&model=` | The handoff text exactly as a move would send it, built here from the transcript and the git state and sent nowhere; `409` when that provider cannot take the chat |
| POST | `/chats/:id/move` | Body: `MoveChatRequest` (`provider`, `action`: `handoff` \| `restart`, `model?`). A person's click: starts a new chat on that provider in the same worktree, linked both ways, and closes an open wait. `409` when the chat is working and has not reached a limit, was moved already, or the provider cannot take it. Not open to a chat's token |
| POST | `/chats/:id/wait` | A person chooses to wait for the reset: opens a wait (`ProviderMove`), `409` when the chat is not at a limit or is waiting already. Not open to a chat's token |
| POST | `/chats/:id/messages` | `{ text, attachments?, id? }` — another turn for a chat with a live execution (`409` otherwise: resume it). `attachments` are upload ids from `POST /uploads`; `id` is a UUID the client chooses, so a retry is written once. Answers the chat with `message`: its id and how it was taken (`written` into the running turn, `started`, `held` for the next process). The stream says when the agent takes it or when it is lost (`delivery` events), and the chat lists what still waits (`pending`) |
| 