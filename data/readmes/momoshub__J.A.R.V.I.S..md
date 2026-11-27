# J.A.R.V.I.S.

<p>
  <a href="https://github.com/momoshub/J.A.R.V.I.S./actions/workflows/ci.yml"><img alt="ci" src="https://img.shields.io/github/actions/workflow/status/momoshub/J.A.R.V.I.S./ci.yml?branch=main&label=ci&logo=githubactions&logoColor=white&style=for-the-badge"></a>
  <a href="https://github.com/momoshub/J.A.R.V.I.S./actions/workflows/e2e.yml"><img alt="e2e" src="https://img.shields.io/github/actions/workflow/status/momoshub/J.A.R.V.I.S./e2e.yml?branch=main&label=e2e%20(real%20slack)&logo=slack&logoColor=white&style=for-the-badge"></a>
  <a href="./LICENSE"><img alt="license" src="https://img.shields.io/github/license/momoshub/J.A.R.V.I.S.?style=for-the-badge&color=blue"></a>
  <a href="https://github.com/momoshub/J.A.R.V.I.S./commits/main"><img alt="last commit" src="https://img.shields.io/github/last-commit/momoshub/J.A.R.V.I.S./main?style=for-the-badge&logo=git&logoColor=white"></a>
  <br>
  <img alt="bun" src="https://img.shields.io/badge/runtime-bun-fbf0df?style=for-the-badge&logo=bun&logoColor=black">
  <img alt="typescript" src="https://img.shields.io/badge/typescript-strict-3178c6?style=for-the-badge&logo=typescript&logoColor=white">
  <img alt="claude code" src="https://img.shields.io/badge/brain-claude%20code-d97757?style=for-the-badge&logo=anthropic&logoColor=white">
  <img alt="slack" src="https://img.shields.io/badge/front%20end-slack-4a154b?style=for-the-badge&logo=slack&logoColor=white">
  <img alt="self-updating" src="https://img.shields.io/badge/ships-its%20own%20PRs-8a2be2?style=for-the-badge&logo=github&logoColor=white">
</p>

Jarvis is a harness of harnesses. Claude Code is already a harness around a model; Jarvis is the harness around Claude Code (or the **Anthropic API**), for now. It keeps the sessions, memory, roles and tool sandbox, schedules work, waits on CI and reviewers, runs background workers, and changes and redeploys its own source. Slack is only where people talk to it: one front end, not what it is. Live streaming replies with a tool-call timeline and an admin dashboard come with it.

The story of how it came to build itself: [J.A.R.V.I.S.](https://thediligentengineer.com/J.A.R.V.I.S.)

The codebase is generic - the bot's identity (name, persona, labels) lives in the database and is edited from the dashboard, so the same code runs any assistant.

## Requirements / platform

- **Bun** (CI pins the version in `.github/workflows/ci.yml`), **git**, the **Claude Code CLI** (`claude`) for the default `claude-cli` brain (or an `ANTHROPIC_API_KEY` with `LLM_PROVIDER=anthropic`), and a Slack workspace where you can install an app. `gh` is needed for the review and self-update features.
- **macOS first.** It is developed and run on a Mac. These parts are Mac-only:
  - **desktop control** (`bin/desktop.ts`, `bin/mac-ui.js`: `osascript` and the Accessibility permission, see [Desktop access](#desktop-access));
  - **Keychain token key mode** (`TOKEN_KEY_SOURCE=keychain`; the default `file` mode works anywhere);
  - **restart via launchd**: `bin/jarvis-restart.sh` asks the running bot to exit once idle and relies on a supervisor to start it again. The repo ships no launchd plist; on a Mac write a LaunchAgent with `KeepAlive`, elsewhere use anything that restarts the process on exit (systemd `Restart=always`, a container restart policy, ...).
- **On Linux** everything else runs (Slack, memory, dashboard, commands, GitHub App, reviews). Desktop control is unavailable, keychain mode is unavailable (stay on `file`), and restarts need your own supervisor.
- **Orca is optional.** It is the multi-agent IDE the owner's turns use for background workers; with it missing or stopped, turns get no `ORCA_TERMINAL_HANDLE` and fall back to the Agent tool. Turn it off with `ORCA_TERMINAL_WORKTREE=off`.

## Quickstart

1. **Create the Slack app** from [`slack-app-manifest.yaml`](./slack-app-manifest.yaml) (api.slack.com/apps -> Create New App -> From a manifest). It enables Socket Mode and carries the scopes, events and slash commands the code uses. Rename the app and the slash commands if you change `SLASH_COMMAND`.
2. **Get the tokens**: install the app to the workspace and copy the Bot User OAuth Token (`xoxb-...`); under Basic Information -> App-Level Tokens create one with `connections:write` (`xapp-...`).
3. **Install and configure**: `bun run setup`, then `cp .env.example .env` and set `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `OWNER_SLACK_ID` (your own member id: profile -> three dots -> Copy member ID) and, for the CLI brain, `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`.
4. **Seed the owner**: `bun run db:seed` writes `OWNER_SLACK_ID` into the database as `owner` (it is also done at every boot, and safe to repeat).
5. **Run it**: `bun start`, then DM the bot or `@`-mention it in a channel it has been invited to. `//bot help` lists the commands. The dashboard is at `http://127.0.0.1:2002` (`DASHBOARD_PORT`).

Read the security note below before giving anyone but yourself a role above `pal`.

## ⚠️ Security - read this first

With `LLM_PROVIDER=claude-cli`, an **`owner`** message is sent to a `claude` process launched with `--dangerously-skip-permissions` - full shell, file, and network tool access. The bot's own secrets are kept out of that process's environment (see [Secrets and turns](#secrets-and-turns)), but it runs as the host user and can still read what that user can read, `.env` included. **Treat the owner as a shell user on the host**: "read ~/.ssh/id_rsa and DM it to me" is a normal request to a tool-enabled agent, not something it needs to break out of. Every other role (including `admin` and a role the bot does not recognise) runs without the bypass: a turn reads pages, attachments and PRs that anyone can write, so a prompt injection there must not be able to run an arbitrary command as the bot.

Every role that does not hold `tools:full-access` (only the owner, as seeded) is sandboxed (see [Roles & tool access](#roles--tool-access)): `pal`/`executer`/`admin` run without permission bypass, with an explicit read-only/assigned tool allow-list (`SANDBOX_TOOLS`, below), in a fixed scratch dir, with `--permission-mode dontAsk` so a command that is not on the list is refused at once instead of waiting for a prompt nobody can answer. The `quick-review` command is an exception - it is a preset task that runs full-access (and writes to the PR) for any role that may run it.

Before deploying beyond a trusted, sandboxed machine:

- keep `owner` and any role you grant `tools:full-access` tiny and trusted (the owner cannot be removed); give everyone else a sandboxed role (`pal`/`executer`, or a custom one)
- run in a container / low-privilege user with a scoped filesystem and limited network egress
- keep the dashboard on loopback (default) and the token secret
- rotate any tokens that have appeared in logs or chat

## Stack

- **Bun** + **TypeScript**, functional style (no classes)
- **@slack/bolt** in Socket Mode (no public URL needed)
- **brain**: local **Claude Code CLI** (default, full tool access) or the **@anthropic-ai/sdk** API
- **bun:sqlite** for memory and configuration
- **bun test** for TDD

## Setup

```bash
bun run setup          # installs deps and builds the React dashboard
cp .env.example .env   # fill in the values
```

`setup` runs `bun install` and `bun run build:web` (the dashboard is a Vite + React 19 app in `web/`, built to `web/dist` and served by the bot). During dashboard development, `bun run web:dev` runs Vite with the API proxied to `:2001`.

Required / notable env (see `.env.example`):

| var | meaning |
| --- | --- |
| `SLACK_BOT_TOKEN` | Bot User OAuth token (`xoxb-...`) |
| `SLACK_APP_TOKEN` | App-level token with `connections:write` (`xapp-...`) |
| `SLACK_STREAM_UPDATES` | `true` (default) streams replies live; `false` posts once |
| `LLM_PROVIDER` | `claude-cli` (default) or `anthropic` |
| `CLAUDE_CODE_OAUTH_TOKEN` | long-lived CLI auth from `claude setup-token`; without it the bot borrows the machine's interactive login and dies when that expires |
| `CLAUDE_BIN` / `CLAUDE_MODEL` | claude binary + model alias (claude-cli) |
| `CLAUDE_MODEL_PAL` | model for `pal` chat (default `haiku`) - see [Model per role](#model-per-role) |
| `CLAUDE_SKIP_PERMISSIONS` | the default for a call that carries no role policy (`true` grants full tool access - see the security note). A turn always has one: only the owner gets the bypass, whatever this says (claude-cli) |
| `SANDBOX_TOOLS` | comma list of CLI tool names/patterns (`Read`, `Bash(cat:*)`, `mcp__notion`) that REPLACES the default allow-list of `pal`, of an `executer` or `admin` with no dashboard list and of a role the bot does not recognise. Empty: the built-in read-only default (`PAL_TOOLS` in `src/domain/toolPolicy.ts`: `Read`/`Grep`/`Glob`, web search + fetch, `git` and `gh` read commands, read-only Notion/GitHub MCP; no shell reader is listed on purpose, see below). The bot's own helpers in `bin/` and every denial (writes, `sed -i`, `find -exec`, `rg --pre`, `jq` reading the environment, redirects for the read-only role, secrets, databases, `orca`) are added on top, so a custom list cannot lift one. The owner is never affected |
| `CLAUDE_CWD` | working dir for the CLI; blank = neutral temp dir outside this repo |
| `ORCA_TERMINAL_WORKTREE` | Orca worktree selector the bot opens its own terminal in, handed to every turn as `ORCA_TERMINAL_HANDLE` so it can run `orca orchestration` (default `path:~/Workspaces`; `off` disables). Orca not running = no handle, turns fall back to the Agent tool. A question one of those workers asks (`orca orchestration ask`) is put to the Slack thread that started it as a turn, which answers it with `orca orchestration reply` - see [Orca workers' questions](#orca-workers-questions) |
| `ORCA_REAP_INTERVAL_MS` / `ORCA_REAP_IDLE_MS` / `ORCA_REAP_DRY_RUN` | Idle-worker reaper (default every 30 min, idle for 3 h; interval `0` turns it off, dry run only logs). An Orca worker's interactive agent stays open (hundreds of MB plus MCP children) after its work ends, so the bot closes, through Orca (`worker-release` for a settled worker, `worker-stop` otherwise), sessions whose task is finished/failed, or blocked with no pending gate once the worker itself has ended (or tied to no task, once the worker ended) and whose terminal has been silent that long. Never touched: a worker with a live watch (on its dispatch, Run or task) or an unanswered question, one waiting on an `ask`, one whose terminal was reused, one kept open, one Orca needs a human for, or any session Orca did not start (your own `claude` sessions, the bot's `claude -p` turns). Each close is logged as `[orca-reaper] ...` |
| `STALE_PROMISE_INTERVAL_MS` / `STALE_PROMISE_MIN_AGE_MS` / `STALE_PROMISE_WINDOW_MS` / `STALE_PROMISE_MAX_NUDGES` | Stale-promise sweep (default every 15 min, a promise must be 30 min old, threads active in the last 24 h, at most 3 nudges per sweep; interval `0` turns it off). See "Stale promises" below. Each nudge is logged as `[stale-promise] ...` |
| `ANTHROPIC_API_KEY` / `ANTHROPIC_MODEL` | required only when `LLM_PROVIDER=anthropic` |
| `BOT_NAME` | bootstrap bot name for a fresh DB (default `Assistant`) |
| `BOT_THINKING_LABEL` | bootstrap "thinking" line label |
| `COMMAND_PREFIX` | message command trigger (default `//bot`; legacy `!` always works) |
| `SLASH_COMMAND` | Slack slash command to register (default `/bot`) |
| `OWNER_SLACK_ID` | the owner, cannot be removed |
| `RESTART_TURN_BUDGET_MS` | while a restart waits, new messages still run, each turn on this budget (default `120000`); past it the thread is told to hold on and the turn is cut, then picked up again on the same session after the restart |
| `DRAIN_NOTICE_CHANNEL` | channel for the one restart notice listing waiting threads (unset: silent); also where the inner child logs voice drift unless `inner_child_drift_channel` is set, and where a press on Slack's stop button is reported (the stopped thread is not told) |
| `OFFLINE_ALARM_CHANNEL` | channel told when the host loses its connection, via a Slack scheduled message kept armed; a channel id, not a name (unset: no alarm) |
| `SLASH_MIRROR_CHANNEL` | channel for the owner's copy of other people's slash commands, one thread per run; a channel id (unset: the owner's DM) |
| `GITHUB_APP_ID` | GitHub App id (unset: `app.json` beside the private key) - see [Calling it from GitHub](#calling-it-from-github) |
| `GITHUB_APP_PRIVATE_KEY_PATH` | app private key (default `~/.config/jarvis/github-app/private-key.pem`) |
| `GITHUB_APP_WEBHOOK_SECRET_PATH` / `GITHUB_APP_WEBHOOK_SECRET` | webhook secret file (default `~/.config/jarvis/github-app/webhook-secret`), or the value itself |
| `GITHUB_APP_PORT` | loopback port of the webhook listener (default `2003`) |
| `GITHUB_APP_SLUG` | app slug, `@<slug>` calls it (default `jarvis`) |
| `GITHUB_APP_ALLOWED_OWNERS` | repo owners the app acts for, comma list (default empty: the app acts for no owner until set) |
| `GITHUB_APP_LABEL` | label that calls it on an issue/PR (default `jarvis`) |
| `SELF_PR_AUTHOR` / `SELF_PR_REVIEWER` | gh logins for the bot's own PRs: the author opens the PR and answers reviews, the reviewer posts its reviews (request changes or approve) and merges. Both or neither, and not the same login (otherwise: one account) |
| `ACCEPTED_BOT_IDS` | Slack bot ids, comma list, whose messages are answered as the person they post for. A bot that posts with a person's user token carries both a `bot_id` and that person's `user`; with its id listed the message is handled as that user speaking, authorized through the normal access check (exactly that person's role, never more). A bot message without a `user` is still ignored, and after 3 accepted-bot turns in a row in one thread with no person writing, the bot stops answering bots there until a person does. The turn's context marks such a message `via bot` next to the person. Default empty: every bot message is ignored |
| `REVIEW_ROUNDS_MAX` | review rounds a PR is followed for, the review that was asked for included (default `5`; `0` turns following off). See [Review rounds](#review-rounds) |
| `REVIEW_ROUNDS_IDLE_DAYS` | days without a push after which a reviewed PR is no longer followed (default `7`) |
| `TURN_ENV_PASSTHROUGH` | secret-shaped variable names (`*_TOKEN`, `*_SECRET`, `*_API_KEY`...) an agent turn may still inherit, comma list; default none. A turn's environment is the bot's **minus every credential-shaped variable** (`SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `ANTHROPIC_API_KEY`, the webhook secret, ...): a turn reads untrusted text, so anything in its environment is one `curl` from leaving. `CLAUDE_CODE_OAUTH_TOKEN` is always kept (the CLI needs it). Slack goes through a per-turn ticket instead, see "Secrets and turns". Name a variable here only when a tool a turn runs genuinely needs it |
| `DB_MCP_SERVERS` | names of the local database MCP servers on this host (as `claude mcp list` shows them, e.g. `pg-prod,clickhouse-ro`), comma list. **Security setting:** each is denied by name to every role that may not use databases (pal, executer, side questions), and a denial has to name the server, so a server missing here is reachable by EVERY role. Default empty denies nothing - list every database server you configure (at boot the activity log warns about local servers in `~/.claude.json` that are not listed) |
| `EXECUTER_DB_MCP_SERVERS` | the subset of `DB_MCP_SERVERS` the executer role may query; list only servers whose credential is read-only on the server side. Default empty: executers get none |
| `WORKER_MCP_DENY` | user-scope MCP servers (names as `claude mcp list` shows them) kept out of the Orca workers the bot starts, comma list. Default empty: every worker loads every server, as before. See "Keeping MCP servers out of workers" |
| `WORKER_HOME_DIR` | the one folder every Orca worker starts in (`--worktree path:<it>`); the MCP exclusion is written there and never into a folder you work in. Default `~/.jarvis/worker-home`, created at boot and registered with Orca (as a plain folder) the first time a worker is about to start. See "Keeping MCP servers out of workers" |
| `DASHBOARD_PORT` | dashboard port (local, loopback-only, no auth) |
| `DASHBOARD_ALLOWED_ORIGINS` | extra browser origins allowed to POST (proxy/tunnel access) |
| `DATABASE_PATH` | the live sqlite file (default `data/bot.db`). Put it **outside the git checkout**, `~/` works, e.g. `~/.jarvis/data/bot.db` - see [Where the database lives](#where-the-database-lives) |
| `DATABASE_MIGRATE_FROM` | one-time move: when `DATABASE_PATH` does not exist and this file does, the first boot fills it with a consistent snapshot of this one (the old file is only read). Unset: nothing |
| `TOKEN_DATABASE_PATH` / `TOKEN_DATABASE_MIGRATE_FROM` | the same pair for the token database (default `data/tokens.db`) |
| `TOKEN_KEY_PATH` | the token database key file (default `data/tokens.key`) |
| `TOKEN_KEY_SOURCE` | `file` (default: the key is `TOKEN_KEY_PATH`, unchanged) or `keychain` (macOS only: one Keychain item, see [Per-user tokens](#per-user-claude-tokens)) |
| `TOKEN_KEY_KEYCHAIN_SERVICE` | the Keychain item's service name (default `jarvis-token-key`); the account is the login user |
| `DATABASE_BACKUP_DIR` | where `bin/db-backup.ts` writes snapshots (default `~/.jarvis/backups`) |

Env values for identity only **bootstrap a fresh database**. Once set, the DB values (edited from the dashboard) take precedence, so the code stays generic.

### Where the database lives

Keep the live SQLite files out of the git checkout. Point `DATABASE_PATH`, `TOKEN_DATABASE_PATH` and (with `SLACK_TRANSPORT=inbox`) `INBOX_DATABASE_PATH` at a folder outside the repo (`~/.jarvis/data/`). To move an existing instance without copying by hand, also set `DATABASE_MIGRATE_FROM=data/<old>.db` (and `TOKEN_DATABASE_MIGRATE_FROM=data/tokens.db`): on boot, a missing (or 0-byte / table-less) destination is filled once with a consistent snapshot of the old file (`VACUUM INTO`, so the WAL is included and a running writer is fine). A relative source resolves against the checkout, not the working directory, and the resolved `to`/`from` are logged on every boot. If the source is configured but missing, the bot refuses to start rather than create an empty database. A destination that has tables is never touched, so the lines can stay in `.env`. The old file is only read, never changed or deleted.

Backups: `bun bin/db-backup.ts [--keep N] [--commit]` writes a consistent snapshot of both databases to `DATABASE_BACKUP_DIR` (default `~/.jarvis/backups`, `<name>-<UTC stamp>.db`, newest 14 kept per database). To keep the old "the database is in git" property, make that folder a private git repository of its own and use `--commit`: the history lives in git, and the live file never does. Run it from cron or launchd, e.g. every 6 hours: `0 */6 * * * cd /path/to/repo && bun bin/db-backup.ts --commit`. The token database is ciphertext; its key (`TOKEN_KEY_PATH`, or the Keychain item in keychain mode) is not backed up, so keep a copy of it somewhere safe.

## Run

```bash
bun start        # or: bun dev  (watch mode)
```

The Slack app needs Socket Mode plus the `app_mention`, `message.im`, `reaction_added` event subscriptions (plus `message.channels`, `message.groups`, `message.mpim` for following threads in channels, which need `channels:history`, `groups:history`, `mpim:history`) and the `chat:write`, `app_mentions:read`, `im:history`, `users:read`, `reactions:read`, `reactions:write` scopes. (`reaction_added` + `reactions:read` are what let the owner approve an access request with ✅; `reactions:write` is the bot reacting.) Live streaming uses `chat.startStream`; if your app lacks that capability the bot falls back to a single post automatically.

The **Console** tab additionally needs read scopes to list and open conversations: `channels:read`, `groups:read`, `im:read`, `mpim:read` (and the history scopes above). Without them the Console shows a `missing_scope` error but the rest of the dashboard works.

## Talking to the bot

- DM it, or @-mention it in a channel it is in
- It replies in-thread, streaming the answer live, with tool calls listed in a separate status message that goes away when the turn ends (kept, collapsed, if a step failed)
- Long messages show a configurable "thinking" step first
- It only answers allowlisted users; the owner is always allowed
- Someone it does not know is not turned away: every holder of `access:decide` (the owner, and `admin` as seeded) gets a DM with who spoke and what they said, and whichever of them gets there first decides with a reaction - ✅ adds them under the default role (`role default`, `pal` as seeded), ❌ declines. Either way the person is answered where they asked, and the other copies settle so nobody decides twice. They are answered **once**: tagging again while the request is open says nothing, and someone who was declined cannot re-raise it by asking - there is a 24h cooldown before their asking counts again
- It tags people with their Slack `<@id>` when they are in the conversation
- For workspace questions it calls the Slack Web API through the bot (a helper that presents a per-turn ticket; the bot token itself is never in a turn's environment), never a third-party connector
- **It opens what you share.** Links in a message (or earlier in the thread) are fetched before it answers, and attachments - screenshots, logs, documents - are downloaded and read. It will not ask you to paste something it could have opened, and if something genuinely cannot be read it says so rather than answering around it

### Commands

Every command has two interfaces - use whichever you like. Both triggers are configurable (`SLASH_COMMAND`, `COMMAND_PREFIX`); the defaults are `/bot` and `//bot`:

- **slash**: `<SLASH_COMMAND> <command> <args>` (register that single slash command in the Slack app config; it sub-routes to all commands. Socket Mode needs no request URL)
- **message**: `<COMMAND_PREFIX> <command> <args>` (or the legacy `!<command>`), in a DM or by @-mentioning the bot

A few commands are **internal**: the bot's own tools (today `journey`, its work log, and `bug-report`, which DMs the owner a bug it found in itself with Approve / Reject), run only by the brain in its own turn through the run helper. A typed line, the slash command, the menu, a schedule or the dashboard gets a short refusal whatever the caller's role (the owner included); they are not in `help`, the command menu, the dashboard command list or the role grants, because no role holds them - the brain runs them as whoever its turn serves.

Every command is gated by its own `command:<name>` grant, and its sub-actions by the permission named in the cell (see [Roles & tool access](#roles--tool-access)). **Only `owner` is hard-coded.** `pal`, `executer` and `admin` are custom roles like any other: the *seeded to* column only says which of them a fresh install starts with the grant, and the owner moves it with `role grant` / `role revoke` or the Roles page. A role you create holds exactly what you grant it. Rows marked *owner* are hard-coded and never grantable.

| command | seeded to | effect |
| --- | --- | --- |
| `help` | pal, executer, admin | list the commands you can run |
| `ping` | pal, executer, admin | check the bot is awake |
| `whoami` | pal, executer, admin | show your role, its rank and description, and how many permissions it grants |
| `model` | pal, executer, admin | show the brain and current model |
| `ask <question>` | pal, executer, admin | one-shot question to the brain |
| `model [role\|subagent\|worker\|plan\|loop\|here\|#channel] [name\|default]` | pal, executer, admin (setting: `settings:manage`) | show the brain; `settings:manage` pins a model per role or channel, or for subagents, Orca workers, planning and loop fires |
| `logsource [grafana,datadog\|default]` | pal, executer, admin (setting: `settings:manage`) | where it looks for logs - see [Investigating](#investigating) |
| `inner-child [status]`, `inner-child on\|off`, `inner-child autofix on\|off`, `inner-child channel <#channel>\|off` | pal, executer, admin (setting: `settings:manage`) | whether the self-review feature is on, whether it fixes what it finds (autofix, off by default), its channel and how many issues are open or queued; `settings:manage` switches it, its autofix or sets its channel - see [The inner child](#the-inner-child) |
| `harvest [status]`, `harvest on\|off` | pal, executer, admin (setting: `settings:manage`) | whether the bot reviews its recent conversations and proposes facts and skills to remember (off by default; the owner approves every one), how many it proposed in the last day and how many skill drafts wait; `settings:manage` switches it - see [The learning harvest](#the-learning-harvest) |
| `cloudwatch [--group /log/group] [--last 15m \| --from <t> --to <t>] [--region r] [--limit n] <insights query>` (alias `cw`), `cloudwatch help`, `cloudwatch default <group\|reset>` | executer, admin (runs at once with `cloudwatch:direct`, else Confirm first) | query CloudWatch Logs Insights directly - see [CloudWatch](#cloudwatch) |
| `forget` | pal, executer, admin | wipe the bot's memory of this channel |
| `sys` (alias `vitals`) | admin | how the host, the bot and Orca are doing, as Block Kit: a verdict header, cpu/memory/swap/disk/battery/host/bot/turns fields, the last hour's trend, then Orca's runtime, active runs, workers by status and a table of live workers (one "unreachable" line when Orca is down or slow). The message text keeps the plain report as the fallback |
| `users` | admin | list the allowlist |
| `worker-cost <ctx_...\|run_...>` (alias `wcost`) | admin | tokens and list-price cost of an Orca worker, or every worker in a Run - see [What an Orca worker cost](#what-an-orca-worker-cost) |
| `add @user [role]` | admin; only roles ranking below your own | grant access under any role, custom ones included; no role given means the default one (`pal`); an unknown role name is refused |
| `remove @user` | admin (only someone ranking below your own role) | revoke access |
| `learn <fact>` | executer, admin | teach a durable fact: the owner's own typing is saved at once, anyone else's (and any `learn` the agent runs for itself) waits as *pending* for the owner's approval and is not part of any reply until then |
| `learn pending` / `learn approve <id> [global\|<channel ids>]` / `learn reject <id>` | *owner* | list what waits (with its scope), approve it (it is carried into every reply from then on, or only in the channels you name) or reject it (never). Typed by the owner only: the agent cannot run these for itself. The owner also gets each pending learning as a DM with Approve / Reject buttons |
| `learnings` / `relearn <id> <text>` / `unlearn <id>` | executer, admin | list, reword or delete learnings. Rewording by anyone but the owner sends the learning back to pending |
| `review-policy [owner/repo] [first\|after\|default]` (alias `rvpolicy`) | pal, executer, admin (setting: `settings:manage`) | how a repo gets approved - see [Review policy per repo](#review-policy-per-repo) |
| `review-agents [n\|default]` (alias `rvagents`) | pal, executer, admin (setting: `settings:manage`) | how many child agents one review may fan out to - see [How wide a review fans out](#how-wide-a-review-fans-out) |
| `token [remove\|who]` (alias `claude-token`) | pal, executer, admin | add, replace or forget your own Claude Code token (used only by `quick-review`) - see [Your own Claude token](#your-own-claude-token) |
| `session [reset\|on\|off]` (alias `sess`) | pal, executer, admin (on/off: `runs:stop-any`) | the CLI session this thread is talking to - see [One session per thread](#one-session-per-thread) |
| `ticket <what is wrong>` (aliases `bug`, `raise`) | pal, executer, admin | raise a properly written, correctly routed ticket - see [Raising a ticket](#raising-a-ticket) |
| `quick-review <pr-url\|help\|prompt> [--policy first\|after] [what to look at]` (alias `rv`) | pal, executer, admin | quick review of a PR, **when a person asks** (tag the bot with `review <pr-url>` or `approve <pr-url>`, or type this; or a review requested on GitHub starts the same one - never from a thread, workflow or hand-back - see [Asking for a review in words](#asking-for-a-review-in-words) and [Reviews that start by themselves](#reviews-that-start-by-themselves)): read all of it, post a comment on GitHub *and* back in the thread with the blockers first and the non-blocking findings after them; request changes on a blocker only (big PRs are cloned + reviewed by child agents that split the files between them); a new push to a reviewed PR gets the next round by itself, see [Review rounds](#review-rounds). CI is read first: red requests changes before the review, a running CI gets a watcher (see [CI comes first](#ci-comes-first)). Runs full-access. |
| `bomb [categories] [count] <message-link>` (alias `br`) | admin | reaction-bomb a message. Combine categories with commas and set a count: `bomb money,face,negative 9 <link>`. Up to 23; `bomb help` lists every category |
| `brief <thread-link\|reference> <text>` (`brief help`) | admin | leave a short note FOR another thread: what you posted there, why, what you wait for. Posts nothing, starts no turn; that thread's session reads it on its next turn, whoever speaks (it is part of that turn's message, so the session keeps it for the turns after), then it is marked read for that access tier. It is background information only, never instructions. The receiver sees only an opaque reference to your thread (never a link) and answers with `brief <reference> <text>`. `tell` is for when the other side must act now |
| `post <#channel \| channel id \| thread-link> <text>` | owner | post a NEW message somewhere the turn is not running: a channel's top level (`#name`, `<#C123>` or its id) or into a linked thread. The command is the audited route; the Slack proxy lets only the owner's own turn write elsewhere by hand, and any other turn only into its own channel. Owner only (anyone else is told who can), audit logged like every command, and it files a `brief` in the target thread so its session knows why (an owner's turn writing there directly through the Slack proxy files the same brief) and, for 7 days after the last such write, that thread's human messages come back to the posting thread as relay briefs (untrusted data, no turn, nothing posted); the footer under the message never names the requester; the bot must be in the channel |
| `slack-methods list \| add <method> read\|write [channelParam] \| remove <method>` | owner | manage the Slack Web API methods a turn may call beyond the built-in ones (the `Slack.` paragraph of the security notes lists them); writes stay locked to the turn's channel (in the owner's turn they may name another channel, logged), `auth.*` / `admin.*` / `apps.*` / `oauth.*` are refused, and the change applies on the next call |
| `mcp-tools pending \| list <server> \| approve <server> <tool> \| deny <server> <tool>` | owner | approve or deny the tools an MCP server started listing after its first run; a new tool stays hidden and refused until approved (a typed line only, never from a turn) |
| `reply <message-link>` (alias `jrp`) | admin | draft and post an AI reply to a message |
| `rm-msg <message-link>` (aliases `rmmsg`, `unsend`) | admin | delete a message the bot posted (a bot token cannot delete anyone else's) |
| `workflow <task>` / `workflow stop [<thread-link>]` / `workflow status` (alias `wf`) | executer, admin | start a long task in this thread and keep talking to it (see [Workflows](#workflows)) |
| `limit [@user] [n\|default]` (alias `quota`) | pal, executer, admin (setting: `settings:manage`) | show command allowance; `settings:manage` sets someone's |
| `mindful [hours]` / `mindful continue\|reply <thread-link>` (aliases `mind`, `whatsup`) | admin | everything it is doing: stuck turns (a failed last turn; one a person stopped is not stuck), Orca tasks whose worker is gone and quiet PRs on its own repo (each with the thread that started it), what is running and waiting, and what it cost - see [Stuck work](#stuck-work) |
| `loop every <monday 9am\|day at 18:00\|6h\|week> [--name "PR board"] <prompt>` / `loop list` / `loop rename <id> <name>` / `loop cancel <id>` | admin | run a prompt on a schedule, as a real turn, with nobody present. Every loop has a name: `--name "PR board"` (or `--name board`, `--name=board`) between the schedule and the prompt, else the first four words of the prompt (the command, for a shell loop); `loop rename <id> <name>` changes it later (yours, or the owner's), so `loop rename 3 PR board` fixes a loop that was only ever `loop #3`. A name is plain words: Slack's escapes and links are read first (`&amp;` is `&`, `<url|label>` is `label`), then markup, `<>`, `&` and `|` are stripped and it is clipped to 40 characters; an apostrophe inside a single-quoted name is fine (`--name 'Kai's board'`). The name shows wherever the loop is mentioned: the fire header (`🔁 PR board - loop #3, every 1h · created here`, posted only with a run's reply, where `created here` links to the message that created the loop - a thread reply links into its thread; loops made before that was kept link to their thread, or show no link), `loop list` (the same link per loop), the confirmation, cancel and rename replies, the failure / stopped notices and the settled approval text; the approval DM shows the turn-chosen name on its own line, never in the headline. A shell loop is never typed (not even by the owner): ask me in plain words and I write the script, post the exact command and schedule to the owner's DM and only run it after the owner presses Approve (Reject, or 24h with no answer, deletes it; `loop list` shows it as pending meanwhile). Times are the host's clock, like `remind`; a prompt loop is at most hourly (`every 1h` at the fastest) and a shell loop `every 5m`. Each fire runs on Sonnet (`model:loop`), not the creator's role model. A loop is **silent unless it has something to say**: each fire runs the turn as the creator (prefixed `[loop <id>]`, told nobody is watching and to post nothing in Slack unless the loop's own task asks to send/post/report something or something needs a person, else to reply with exactly `NO_REPLY`), and a run that answers `NO_REPLY` (or ends in it) leaves nothing in Slack, not even a header - except that a run that sets a watch posts its header alone, as the thread the watch reports into. A run that does answer posts one top-level message in the creator's **DM** with the bot - the header line, then the reply - and a reply under it continues the same session; nothing is posted in the channel or thread the loop was created in, which only gets a short confirmation. Want a post every time (`every day send me a fun fact`)? Say so in the prompt. A shell loop runs no turn and spends no tokens; only a failure (non-zero exit or timeout) sends one short line to the creator's DM, and the loop carries on. A run missed while the bot was down happens once on startup, never a backlog. Ten loops per person. `loop help` for the card |
| `promote @user [role]` / `demote @user [role]` | none (owner only until granted) | change role: to the named one, else to the highest role below owner / the least-privileged one |
| `role list` / `show <role>` / `perms [filter]` / `create <name> [from <role>] [description]` / `grant <role> <perm...>` / `revoke <role> <perm...>` / `delete <role>` / `rename <old> <new>` / `rank <role> <n>` / `describe <role> <text>` / `on\|off <role>` / `default <role>` / `denytools <role> <pattern...\|none>` (alias `roles`) | *owner* | see and edit roles and the permissions they grant - see [Roles & tool access](#roles--tool-access) |

A slash command is invisible to everyone but its caller, so the **owner gets a copy in their DM** - one thread per run: a header saying who ran what, with the progress and result threaded under it. Trivial commands (`help`, `ping`, `whoami`, `model`) are not copied, and the owner is never copied on their own.

The power tools also have their own Slack slash commands if you register them (`/rv`, `/br`, `/jrp`) - much quicker than a freeform ask. `br`/`jrp` need the Console's Slack read/write scopes; `rv` is `quick-review` and uses the local `gh` and **writes to the PR** (approve/comment/request-changes).

Examples (with the default prefix): `/bot add @kai admin`, `//bot learn our staging URL is staging.example.com`, `//bot ask summarise the last thread`.

**You do not have to type the command.** Ask in words - "remind me at 3pm", "bomb that message" - and the bot runs the real command, progress and all. The one exception is `quick-review`: the brain never runs it. It starts only from `@bot review <pr-url>` / `@bot approve <pr-url>` or the typed command, see [Asking for a review in words](#asking-for-a-review-in-words).

Anyone may ask, and the command runs **as the person who asked**, so their own role still decides what is allowed - asking in words can never do more than typing it would. The bot never names the actor: each turn is given a short-lived ticket bound to whoever it is talking to, and the ticket is what the command runs as.

## Workflows

A `workflow` turns a thread into a long-running job you can talk to.

```
//bot workflow migrate the webhook handler to the new signature check
```

The bot claims a Claude CLI session id (the *worker*) and keeps that session
for the thread. The worker does the task one step at a time, carrying on by
itself between steps, and posts a short status line after each - it keeps its
own context and files throughout, it is still mid-task, not re-reading a
transcript.

What you say in the thread goes to a separate *front* session on its own
queue, so it is answered while a step is still running. The front gets a
fresh digest each time - is a step running and since when, the worker's last
replies, its most recent tool calls - and answers "status?" from that. When
what you said is meant for the work (an answer to its question, a correction,
a change of plan), the front passes it on: the worker's next step gets
"<you> said mid-task: ...", and an idle worker (blocked on a question, paused,
or done) starts a step for it right away. `workflow stop` ends both and the
thread goes back to normal chat.

- one live workflow per thread, `workflow status` shows it
- `workflow stop <thread-link>` stops the workflow in another thread without posting anything there
- whoever holds `command:workflow` (`executer` and `admin` as seeded, plus the owner) may
  drive one; anyone else still chats normally in the thread without steering the task
- tools are whatever the driver's role allows - a sandboxed `executer` gets a
  sandboxed workflow, and its parallel work uses the Agent tool (foreground
  only in a workflow: a background agent dies with the step). Only an owner's
  workflow worker is told to start Orca workers
- the session id is in the database, so a bot restart does not lose the session
- worker steps may run up to 15 minutes each; front answers are read-only and
  capped at 4 minutes
- an instruction reaches a running worker at its next step boundary, not mid-step

Because it lives in a thread, start it with the message form (`//bot workflow ...`)
rather than the slash command - a slash command has no thread to bind to.

## CloudWatch

`cloudwatch` is the only allowed way to query CloudWatch Logs (`X/jv cloudwatch help` prints this). Logs Insights bills per GB scanned, so a model that reaches for `aws logs` on its own turns an idle question into an invoice; that stays denied to every role, and this command runs the query from the bot itself (the host's `aws` CLI, an argv array, never a shell line).

```
X/jv cloudwatch --group /ecs/prod-api --last 15m fields @timestamp, @message | filter @message like /ERROR/ | sort @timestamp desc
```

- `--group /log/group[,/other]` one or more log groups (up to 10); optional once `cloudwatch default /log/group` is set (`settings:manage`). Each must exist in the region, or nothing runs
- `--last 15m|2h|3d|1w` (default 1h) or `--from <iso> --to <iso>` in UTC; `--region` (default `us-west-2`, or the `cloudwatch_region` setting); `--limit` rows asked of Insights (default 50, at most 1000)
- everything after the flags is the Insights query; Slack's `&lt;` `&gt;` `&amp;` are put back

| who | what happens |
|---|---|
| owner, or a role with `cloudwatch:direct` | the cost warning is posted, then the query runs straight away |
| a role with `command:cloudwatch` (`executer`, `admin` as seeded) | nothing runs. A message with the query, log group(s), range, region, the cost warning and **Confirm and run** / **Cancel** buttons is posted. Only the requester or the owner can press either (anyone else is told so privately). Cancel, or no answer for 15 minutes, means nothing ever runs. Confirm runs it and posts the result in the thread |
| anyone else (`pal` as seeded) | refused, naming the roles that can |

**Cost guard.** Before anything runs the bot reads each log group's stored size and retention (`describe-log-groups`) and estimates the scan as `storedBytes x range / retention` at $0.005 per GB. It is a rough estimate (stored bytes are compressed, a scan reads the original), good for telling 15 minutes from 3 weeks. A range over 3 weeks is flagged **costly**. The warning is shown to the owner and sits on the Confirm message.

**Audit.** Every request is a row in `cloudwatch_requests` (migration v28): who asked and their role, query, groups, region, range, estimate, who confirmed it (or "owner, direct"), status (`pending`, `running`, `done`, `failed`, `cancelled`, `expired`), and the bytes actually scanned. The command is in the command log as well, and every run is a line in the activity log.

**Output** is clipped for Slack: at most 25 rows, each cell and row cut, about 2.8k characters, secrets redacted, and a line saying how many rows were left out or that the limit was hit. A query is stopped (`stop-query`) when it runs past 3 minutes, because the scan is billed while it runs.

The buttons carry `jv:cloudwatch:confirm` / `jv:cloudwatch:cancel` ids but are decided in code and never handed to the model like other `jv:` presses, so a model turn cannot confirm its own query.

### Lazy MCP servers in a bot turn

A bot turn's stdio MCP servers (the database servers) are started lazily: each is
wrapped in `bin/mcp-lazy-proxy.ts`, which answers the tool list from
`~/.jarvis/mcp-schema-cache` and starts the real server only on the first tool
call, and a role that may not use a server (`mcp__<server>` in its denied tools)
does not get it in the config at all. The first turn after a new or edited
server still starts it once to fill the cache.

**New tools are off until the owner approves them.** The first run of a server
takes the tools it lists as its baseline; a tool it lists later is hidden from
every turn and refused if called until the owner runs `X/jv mcp-tools approve
<server> <tool>` (`X/jv mcp-tools pending` lists what is waiting).

**Code mode.** A full-access turn can use a tool from the shell instead of
loading its result into the conversation: `bun bin/mcp.ts list | search <query> |
schema <server> <tool> | call <server> <tool> '<json>' [--fields a,b.c] | types
[<server>...] | run <file.ts | ->`. A call starts the real server (the same
command and env the bot uses), writes the whole result to a file under the temp
directory and prints only its path, size, row count and a short head; `--fields`
keeps only those dotted paths of a JSON result. For many calls or a lot of data,
`types` prints TypeScript declarations of the tools and `run` executes one script
written against them in an isolate with no network, files, process or env (QuickJS
compiled to WebAssembly): it sees only `mcp.<server>.<tool>(args)` and
`console.log`, chains, loops and filters there, and only its final value and logs
reach the context, as a file path and a short head. Credentials stay on the host;
the script has a time (60s), memory (64 MB), tool-call (100) and output limit
(`--timeout`, `--memory`, `--max-calls`). Both refuse a server or tool the turn's
role may not use, check it again on every call a script makes, and honour the
owner's tool approvals.

## Investigating

Asked what went wrong, the bot looks for logs, metrics and traces in a stated
order rather than reaching for whichever backend it noticed first:

1. **Grafana**, via the [`gcx`](https://grafana.com/docs/) CLI. It starts with
   `gcx datasources list` and lets the *type* decide how to query: `gcx logs`
   for Loki, `gcx metrics` for Prometheus, `gcx traces` for Tempo, and the
   datasource proxy for anything else - `gcx logs` refuses a non-Loki
   datasource, so VictoriaLogs, Elasticsearch and friends go through
   `bin/grafana-get.sh`. For a real investigation it loads `gcx`'s own bundled
   `debug-with-grafana` skill.
2. **Datadog**, via the host's read-only Datadog MCP server, and only when Grafana genuinely has
   nothing - no such datasource, or the data does not reach back far enough. An
   empty result is an answer, not a reason to try the next one.

**CloudWatch is never queried by hand.** It bills per GB scanned, so an idle look
there has an invoice attached. A turn's own `aws logs` and `aws cloudwatch` are
denied to every role (`ALWAYS_DISALLOW`). The one allowed path is the
[`cloudwatch` command](#cloudwatch): the bot runs the Logs Insights query itself,
behind a cost estimate and, for `executer` and `admin`, a Confirm button.

The order is configuration:

```
//bot logsource                    where I look, in order
//bot logsource datadog,grafana    reorder  (admins)
//bot logsource default            back to grafana,datadog
```

It requires `gcx` on PATH and a logged-in stack (`gcx login`). Note `gcx` reads
`~/.config/gcx/config.yaml` by default, which is *not* where `gcx login` always
leaves the stack - point `GCX_CONFIG` at the file that actually has it (the
launchd plist sets this) or every query fails with "context references no stack".

`bin/grafana-get.sh` is GET-only by construction and refuses any path outside
the read surface, so a sandboxed role can read through a datasource proxy
without being handed `gcx api`, which can also POST, PUT and DELETE.

## Model per role and per channel

Ordinary chat with a `pal` does not need the expensive model, so it runs on
`CLAUDE_MODEL_PAL` (default `haiku`) while everyone else uses `CLAUDE_MODEL`.
Admins can change any role or channel at runtime, no restart:

```
//bot model                     what I am running, and every override
//bot model pal sonnet          pin a role
//bot model here sonnet         pin this channel
//bot model <#C123> haiku       pin another one
//bot model pal default         clear it
```

**Channel beats role**, so a room with serious work in it can be put on the good
model whoever is talking, and a noisy one can be made cheap for everybody.

The model is chosen per call alongside the caller's tool policy, so it never
changes what anyone is *allowed* to do - a cheaper model is sandboxed
identically. Preset tasks that force a policy keep their own model: `quick-review`
runs full-access whoever asked and wherever it is asked, so a pal's review in a
cheap channel is still done properly.

### Handed-off work: subagents, Orca workers, planning

An owner turn picks the run mode by the job's weight: light work (a few edits,
a TODO comment, one lookup) stays inline, short or side-by-side work that ends
inside the turn goes to the Agent tool, and anything that opens a PR, waits on
CI or a reviewer, or outlives the turn goes to an Orca worker. Other roles have
only the Agent tool.

What a turn hands off runs on its own model, whatever the turn itself is on - an
owner turn talks on Opus, but its helpers do not:

| setting | default | what it covers |
|---|---|---|
| `model:subagent` | `sonnet` | Agent tool subagents in any turn (general-purpose, Explore, review child agents) |
| `model:worker` | `sonnet` | Orca workers an owner turn starts (`worker-start`, `fanout`, the self-fix reviewer); other roles have no Orca |
| `model:plan` | `opus` | the Plan subagent |
| `model:loop` | `sonnet` | the turn a `loop` fires, whatever its creator's role model is (an owner's loop included); a reply someone types in the loop's DM thread is an ordinary turn on the role model |

```
//bot model                     also lists these four
//bot model worker haiku        pin one
//bot model plan default        back to its default
```

Read per turn, so no restart. Subagents get `CLAUDE_CODE_SUBAGENT_MODEL`, and the
built-in Explore and Plan agents are replaced through `--agents` with the same
job and a pinned model, because both inherit the turn's model and ignore that
variable. Workers get it through `BOT_WORKER_MODEL`, which the prompts pass to
`orca ... --model`.

### Keeping MCP servers out of workers

Every `claude` session loads every user-scope server in `~/.claude.json`, and a
stdio server is a process (often three: the launcher, the server, a child) per
session. An Orca worker almost never needs a database server, but each one got
the whole set: on one host 17 workers held about 1.3GB and pushed the machine
into swap. `WORKER_MCP_DENY` (comma list of server names, default empty = every
server loads, as before) names the ones to leave out.

Orca offers no per-launch hook for this: `worker-start` and `worktree create`
take no extra agent arguments, settings file or environment (only `orca
automations` do), and its host-wide agent arguments would also change the
tabs you open yourself. What a session does read, once, when it starts, is the
project settings of its working directory, and `deniedMcpServers` in
`.claude/settings.local.json` there keeps the named servers from starting
(checked on Claude Code 2.1.285: the file written before the launch removes
the stdio servers, the same file written after the session started changes
nothing). So the bot's prompts for starting a worker (the owner's Orca rules,
the reviewer worker) say to run `bin/worker-mcp-trim.ts` first, which
merges the names into that file (other settings in it stay, a file it cannot
parse is left alone, running it twice is the same as once). It does nothing to
the file when the list is empty. The helper, the names and the folder reach a
turn as `BOT_WORKER_MCP_TRIM`, `BOT_WORKER_MCP_DENY` and `BOT_WORKER_HOME`.

That file belongs to the folder, so workers do not start in a folder you work
in: trimming `~/Workspaces` would take the same servers away from your own
Claude sessions there. They start in a dedicated worker home instead,
`WORKER_HOME_DIR` (default `~/.jarvis/worker-home`). Boot creates it; the helper,
run with no argument, registers it with Orca as a plain folder when `orca repo
list` does not know it (`--worktree path:` only takes folders Orca knows), trims
it, and the prompts then start the worker with `--worktree path:$BOT_WORKER_HOME`.
The bot never writes `.claude/settings.local.json` anywhere you work. A worker
that has to change code cuts its own `git worktree add <absolute path>` from the
real repository, so its brief uses absolute paths.

- `fanout` gives each worker a checkout of its own instead: the checkout is
  created first without an agent (`orca worktree create`, no `--agent`),
  trimmed (`worker-mcp-trim.ts <worktree path>`, the file stays out of git in
  that checkout), then launched with `orca agent launch --worktree path:<path>`.
  The one-step launches (`worktree create --agent`, `worker-start --worktree
  new-child`) would start the agent before the file exists, so the prompts
  forbid them.
- Only user-scope servers by name are excluded. The `claude.ai` connectors are
  remote and start no process, and the bot's own turns have their own list
  (`UNAUTHENTICATED_MCP_SERVERS`). A turn the owner's own message started is the exception: it runs
  on the host's interactive login with every claude.ai connector and server an interactive `claude`
  on the Mac has (minus unauthenticated ones and the claude.ai Slack connector, which acts as the
  owner's own identity), so it bills that login rather than the setup token.
- A name that matches no server in `~/.claude.json` excludes nothing, so boot
  logs it as a warning.

## Investigating

```
//bot investigate why did /home crash for this user
```

`investigate` (aliases `inv`, `rca`) walks logs, RUM and traces for a cause and
reports back in the thread - it reads the thread first, so the ids and
timestamps already posted are not asked for again. It files nothing and changes
nothing unless you ask; finding out is the job.

Every chat turn, for every role, can also look in Datadog itself: the host runs
a Datadog MCP server (`claude mcp add --scope user --transport http datadog
https://mcp.datadoghq.com/v1/mcp`, authenticated once with OAuth in a browser;
the claude.ai Datadog connector cannot reach a chat turn, which runs on a
`claude setup-token` credential). Until that OAuth is done a server stays in
`UNAUTHENTICATED_MCP_SERVERS` (`src/infrastructure/llm/mcpConfig.ts`) and no bot turn loads it:
an unauthenticated server makes the CLI inject a needs-authentication notice that the model
copies into its reply. Datadog is authenticated and off that list; `figma` is still on it. Only the read tools are exposed - logs, RUM,
spans, metrics, monitors, incidents, dashboards; anything that edits a notebook
or dashboard, and `execute_code`, is denied. `investigate` stays the route for a
full investigation on the host login, and the fallback when that server's login
lapses: when a question needs Datadog and the tools are not there, the bot runs
`investigate` **itself** through its own command bridge and reports what it
found - and since that run posts its own findings into the thread, the bot says
one line and lets it speak rather than repeating it. Telling someone to go and
type a command it could have run is a hand-off, not an answer; restating what it
already posted is the same message twice.

Separately, anything the bot posts as plain text is converted to mrkdwn on the
way out - `**bold**`, `[label](url)`, `#` headings and `*` bullets all render as
literal characters in Slack otherwise. The prompts still carry the rule, but a
rule a model may ignore is not a guarantee, and what it ignores is the one thing
the reader sees. Code is held out of the conversion, so `**ptr` in a snippet
stays as written.

The prompt also encodes the ways a real investigation went wrong: count on the
de-duplicating field (one crash emits several RUM events, so a naive count came
out 3x too high), check every region rather than the one the report came from,
prove the mechanism with a request timeline instead of a plausible story, and
question an id that returns nothing before concluding there is no data.

### Notion in chat turns

Notion is the one connector a chat turn can use directly. The claude.ai connector
cannot reach a setup-token turn, so the host registers its own server once:
`claude mcp add --scope user --transport http notion https://mcp.notion.com/mcp`, then
authenticate it in `/mcp`. From then on a turn sees `mcp__notion__notion-*`
(search, fetch, create and update pages including properties like Status,
comments). Unverified until set up on the host: unlike the local database servers this is a remote OAuth server, so check with `claude mcp list` and a real call from a chat turn that it loads under the setup token; if it does not, the prompt falls back to `read`/`note`. It writes as the host's Notion identity, so it is the `mcp:notion` grant (seeded from the old `note` floor, admin and up). Other connectors are not widened.

### Why tickets use the host's login

A ticket is the one task that needs a claude.ai connector (Notion), and a
`claude setup-token` credential carries **no connector authorisation at all** -
under one the CLI loads zero `mcp__` tools. That applies to the bot's own token
and to every per-user token alike, so a ticket cannot run on either.

With no Notion credential of our own, the ticket spawn removes
`CLAUDE_CODE_OAUTH_TOKEN` from the child environment and runs on whatever
interactive login the host holds, which does have the connectors. Removing it
matters: merely leaving it out is not enough, since the bot's own token is in
the environment already and would win.

The trade is deliberate and narrow. That usage bills whoever is signed in on the
machine, and if their session lapses the ticket says so by name - "the login on
my host has lapsed" - rather than failing as though the ticket itself was the
problem. Everything else still runs on an explicit token.

## Raising a ticket

```
//bot ticket surveys are not sending for Example Coffee since this morning
```

Or just say it in chat - "the inbox will not load again" - and it raises one for
you. It only does that for an actual defect: a question is not a ticket, a
feature idea is not a bug, and it will not raise the same thing twice.

The point of it is that **it reads rather than guesses**. Before writing
anything it opens the team's own pages - the how-to-raise SOP, the pod ownership
doc - and the tracker's live schema, so the naming format, the required fields,
the priority criteria and the routing all come from the current source of truth
rather than from something baked into this repo. Pod routing follows the
document's stated exceptions too, which is exactly where a guess goes wrong. If
two pods could own it, it says which it chose and why, in one line, so a human
can correct it in seconds.

It also goes and gets the evidence: the rest of the thread, the screenshots
(opened and read), the logs, the code. A ticket that names the failing endpoint
is worth ten that say "it is broken". Where it does not know something it leaves
the field out and says so, rather than inventing an account id.

When the issue is not trivial it adds a short **Risk** section, and that section
is *measured*: "47 accounts hit this in the last 24h, rising" rather than
"affects many merchants". It has the logs and dashboards, so it counts. Blast
radius, whether data is being lost, whether a workaround exists, what happens if
nobody picks it up this week. If the measured risk contradicts the priority the
SOP's criteria produced, it says so outright instead of quietly resolving the
mismatch either way.

For a **genuinely small fix** - a typo, a wrong label, an off-by-one, a missing
null check, a contained CSS fix - it also opens a PR, runs whatever the repo
runs, and requests a reviewer it can justify (CODEOWNERS for the touched files,
else whoever actually worked on them recently, else the pod lead). Anything
needing product judgement, or touching auth, money, schemas or behaviour, is not
small: it raises the ticket and leaves the code alone.

Configure it once (admins):

```
//bot ticket config                        what is set
//bot ticket config tracker <notion url>   the database tickets go in
//bot ticket config sop     <notion url>   how-to-raise: naming, fields, priority
//bot ticket config pods    <notion url>   who owns what, for routing
//bot ticket config repos   my-org             every repo in that org
//bot ticket config repos   my-org, other/repo an org, plus one specific repo
```

`repos` takes whole organisations as well as single repositories. An org covers
everything under it, including repos created later - so before pushing, the bot
confirms with `gh repo view` that the repository really is under a listed org
rather than trusting a similar-looking name.

With no tracker set it refuses to raise anything, and with no repos set it never
opens a PR. Nothing about any particular workspace lives in this codebase.

## Review policy per repo

By default `quick-review` posts "reviewing", runs the review, and approves only once
it has come back clean. A repository can opt in to the faster order instead -
approve immediately and reverse that with a request for changes if the review
turns up something blocking:

```
//bot review-policy owner/repo after      approve only after a clean review (the default)
//bot review-policy owner/repo first      approve up front, reverse on a blocker
//bot review-policy owner/repo default    clear it
//bot review-policy                       the default, and every repo that differs
```

On `after`, the up-front approval is skipped, the brain is told plainly that
nothing is approved (so the review is not written as a formality), and once it
finishes the approval is decided by **asking GitHub** for the PR's review
decision rather than inferring it - `CHANGES_REQUESTED` means no approval, and
it says so in the thread.

### CI comes first

Whichever policy it is on, `quick-review` reads the PR's checks before anything else:

| CI | `first` | `after` |
|---|---|---|
| red | request changes at once (the body and the thread name the failing checks), then review and comment as usual. Never approved | the same |
| green | approve up front, then review | review, then approve if it came back clean |
| running | start a CI watcher, approve up front, then review. If CI later goes red the watcher requests changes | start a CI watcher, review. At the end: clean and CI green approves, a blocker or red requests changes, CI still running waits for the watcher - green approves, red requests changes |

A blocker found by the review still requests changes on top of that, exactly as
before. The watcher is a row on the same timer as `watch` (so it shows in
`watch list`), runs outside any turn, polls once a minute and gives up after an
hour (it says so, and approves nothing). It is idempotent: it will not
approve or request changes twice, it does not request changes on a PR that is
merged or closed, and it never approves while the review is still being
written. A watcher cut loose by a bot restart waits out its hour and does not
approve, since whether the review had finished is only known in memory. A PR
GitHub cannot be read for, or one without checks, goes the old way; no checks at
all counts as green. `watch cancel` in the thread ends the watcher too.

Policies are configuration, in the database: no repository is named anywhere in
this codebase, which matters because it is open.

One run can ask for a different policy without changing anything:

```
//bot quick-review <pr-url> --policy after     hold the approval back, this run only
//bot quick-review <pr-url> --policy first     approve up front, this run only
//bot quick-review <pr-url> --policy default   the built-in default, this run only
//bot quick-review <pr-url> --after            the same, shorter
```

Nothing is written down, so the repository stays on its own policy for the next
review. Asking for the **stricter** run is anyone's call. Asking for the looser
one - approving up front on a repository that deliberately waits for a clean
review - overrules an admin's decision, so it takes an admin. A value that is
not a policy is refused rather than quietly ignored, since a review that ran on
a policy you did not ask for is worse than one that did not run.

It does not collide with the free text. `--policy` and `--policy=x` are flags
wherever they appear and are taken out before the note is built; `policy:x`
counts only when `x` really is a policy, so "check the `policy:handler` code"
stays a note rather than refusing the command. Bare words are just words -
"approve after CI is green" asks for nothing. With several PRs the flag applies
to the whole run whatever order it was typed in.

## Reading what its own credentials cannot see

The bot speaks with its own Slack token, so everything it says arrives under its
own name. The cost is that it only sees what it has been invited to - a channel
or group DM it is not a member of returns `channel_not_found`.

```
//bot read <slack link or #channel> [what you want from it]
```

`read` (aliases `summarise`, `catchup`) opens it through the account's
connectors - Slack, Notion, whatever else is authorised - which see what the
authorising human sees, and reports back in the thread. A private Notion page
linked from a Slack thread is the normal case, not an exception.

"Private", a 403 or an empty page means the **credentials are wrong**, not that
the thing cannot be read. And a hand-rolled `curl` at a private service's
internal API is never the way to find out: it returns an empty body, which
proves nothing. **Owner only**, and not out of timidity: it reads with that person's
access, so whoever can run it can read anything they can - private channels and
DMs included.

Reading through the connector is allowed; **posting through it never is.** A
message sent that way arrives under the human's name rather than the bot's, so
the connector's send, schedule, draft and canvas tools are denied to every role
including full access. The ban used to cover the whole connector, which refused
the harmless half along with the harmful one.

## Desktop access

Some things the bot can be asked to do reach the desktop - taking a screenshot,
closing a window. On macOS that needs the Accessibility permission, which is
granted against the **path of the binary that launched the process**. Under
launchd that is the runtime (`bun`), not `claude` and not a terminal, which is
the first thing people get wrong: a terminal usually has the grant already, so
testing by hand succeeds while the bot still cannot.

The second thing is worse. The grant follows a path, and a package upgrade that
installs into a versioned directory moves the binary - the permission then
silently stops applying, weeks before anyone asks for a screenshot and gets a
confusing refusal.

So it is probed rather than assumed: `AXIsProcessTrusted()` at boot and on a
five minute TTL, logged at startup and reported by `GET /health`. Not by
scripting System Events - that answers a different question (Automation), which
can be granted while Accessibility is not, and reported "allowed" while the real
call was being refused:

```json
{ "ok": true, "slack": "listening, connected for 2m",
  "ui": "desktop UI control: REFUSED - the Accessibility permission is missing or no longer matches this binary (an upgrade moves it). Grant it to /opt/homebrew/bin/bun",
  "uiState": "denied" }
```

It never affects `ok`. Nothing core needs the desktop, which is exactly why its
absence would otherwise go unnoticed - and a probe that fails for some other
reason reports `unknown` rather than blaming a permission.

## The inner child

An always-on part that reads the bot's own finished turns every thirty minutes.
Off until a channel is set: `inner-child channel #channel`, then `inner-child on`
(on is the default once there is a channel). `inner-child off` pauses it and keeps
the channel, `inner-child` shows on/off, autofix, the channel and how many issues
are open and queued. Changing it needs `settings:manage`; the status is open to
everyone. (Under the hood these are the `inner_child_channel`, `inner_child` and
`inner_child_autofix` settings.)

It is built to be cheap, since it spends the owner's model tokens. Triage runs on
a small model (`claude-haiku-4-5-20251001`; the `inner_child_model` setting
changes it, read every run) and reads only what ended since its cursor. It never
catches up on a backlog: `inner-child on` moves the cursor to now, and a cursor
older than 6 hours jumps to now.

- **Defects in the bot itself** are always filed, as queued. Fixing them is
  opt-in: `inner-child autofix on` (the `inner_child_autofix` setting, off by
  default). With autofix on the bot fixes them in that channel, announced before
  and after, at most two fixes a day; off, they just wait in the queue and
  `inner-child status` shows how many. At most 10 are open (queued or being
  fixed) at once; while the queue is full, triage files nothing new and logs it.
  A queued issue nobody got to in 7 days is closed with state `stale` (the row is
  kept, its fingerprint still dedupes). The owner's bug reports win over it: a
  thread whose bug report the owner rejected is never filed from again (an issue
  already queued there is closed as `rejected`, and triage is told not to report
  it), an approved report runs its own fix so the inner child leaves that thread
  alone too (`covered`), and an issue on a thread with a report still waiting for
  the owner is not fixed until they decide.
- **Voice drift** - a final reply that starts a paragraph with a capital (`I`
  and acronyms excepted), uses an em/en dash, a semicolon, an arrow, a markdown
  heading or `**bold**`, or answers in a different language from the thread -
  is never fixed in code and the reply is never edited. The session that wrote
  it gets a private nudge in its own thread to re-check that reply's content
  and correct anything wrong in a new reply; only that correction appears.
  Each event is a `drift_events` row, an activity log line, and a message in
  the drift log channel with the nudge, followed by the session's answer in its
  thread. The channel is the `inner_child_drift_channel` setting, falling back
  to `DRAIN_NOTICE_CHANNEL`; `off` turns drift steering off. One nudge per
  reply, at most 2 per triage run and 4 a day, never in a workflow thread.

Reading it directly (the owner asking what is open, or what it logged): the data
is in the bot's own database, `DATABASE_PATH` of the live `.env` (not the
`data/bot.db` default), read with `sqlite3 -readonly`, never written by hand.

- `self_issues`: `id`, `title`, `severity` (`bug` or `critical`), `evidence`,
  `source_channel` / `source_thread` (where it was seen), `fix_channel` /
  `fix_thread` (where the fix ran), `state`, `created_at` / `updated_at` (ms).
  States: `queued` (open, nobody on it), `fixing` (open, a fix is running),
  `fixed`, `not_fixed`, `failed`, `stale`, `rejected`, `covered`. Unresolved is
  `queued` + `fixing`, plus `failed` / `not_fixed` when asked for everything not
  fixed:
  `select id,state,severity,title,source_channel,source_thread,datetime(created_at/1000,'unixepoch') from self_issues where state in ('queued','fixing') order by severity='critical' desc, id`.
  With `inner_child` set to `off` nothing runs, so the stale prune does not run
  either and old `queued` rows pile up past the cap.
- `drift_events`: `channel_id`, `thread_ts`, `reply_ts`, `rules`, `excerpt`,
  `nudge`, `outcome`, `created_at`.
- Settings besides the three above: `inner_child_cursor` (the last turn read, in
  ms) and `inner_child_drift_channel`.
- Answer with a small Block Kit table (id, severity, title, a link to the source
  thread built from the workspace URL, the channel id and `p<ts without the dot>`).

## The learning harvest

The bot can review its own recent conversations and **propose** what is worth
keeping, the way a self-reviewing agent saves a fact or turns a solved procedure
into a skill, but nothing is ever saved until the owner presses Approve. Off by
default: `harvest on` (the `learning_harvest` setting) starts it, `harvest off`
stops it, `harvest` shows whether it is on, how many proposals it raised in the
last day and how many skill drafts wait. Changing it needs `settings:manage`; the
status is open to everyone. `harvest on` moves the cursor to now, so what was
said while it was off is never read; a cursor left unmoved (a quiet workspace) is read from at most 6 hours back, never further.

Every 30 minutes, once at least 6 turns people wrote have ended since the cursor,
one small-model call (`claude-haiku-4-5-20251001`; the `learning_harvest_model`
setting changes it) reads the batch and may propose:

- **A durable fact the people settled.** It goes through the ordinary learnings
  path (see `learn`): stored pending, never injected, put to the owner with
  Approve / Reject, deduped against every learning ever asked (active, pending
  or rejected) and against the adapter's notes. A fact about one channel is
  scoped to it.
- **A skill.** A multi-step procedure that was solved and is likely to recur, or
  a correction to an existing skill. The owner gets the draft in a DM with
  Approve / Reject: a new skill whole, a change as a diff. Approve writes it into
  the adapter's skills the way a hand edit does (a revision `adapter revert`
  can undo; refused if the skill changed since the draft); Reject is remembered
  by skill name, so neither that draft nor a reworded one is raised again.

What keeps it safe is checked in code, not asked of the model:

- **Only what people typed is read.** The turn log records, from the inbound
  message's own flags (never the text), whether a person typed a turn; a nudge,
  a loop, a watch or background hand-back, an unprompted turn, an
  auto-continue and a turn built from a GitHub issue or PR body are never reviewed, and neither are failed turns. Every proposal
  must cite a turn and quote words from that person's message, verified against
  it, and the quote is shown in the owner's notice. What is guaranteed is that
  the citation is real, not that the proposal follows from it: a person who asks
  the bot to read a page can still have a page-injected suggestion reach the
  owner's approval, which is exactly why the owner decides, with the quote and
  the source thread in front of them. Text the bot read is shown to the model
  only as the bot's answer, labelled as context.
- **Private stays private.** Only public channels are reviewed. A private
  channel, a DM, a group DM or a channel Slack will not describe is never sent to
  the model, so its words cannot end up in a proposal that loads in another
  channel (one call holds many turns, and a proposal citing a public turn could
  otherwise carry private content). A fact is channel-scoped unless the model
  says it holds everywhere; a skill is from a public source by construction.
- **No secrets or personal data.** A proposal with a token, key, password, email,
  phone number or Slack id is dropped.
- **Bounded.** At most 4 proposals a day (facts and skill drafts together), 2 per
  batch, 3 skill drafts waiting at once; the same proposal is never asked twice.
  A skill draft is at most 2000 characters (or a diff that size) so what the
  owner reads is all of what they approve, and it may not set how a skill runs
  (`model`, `worker`, `run`).
- **Decided in code.** The buttons (`jv:harvest:`) are handled by their own
  listener, never a model turn, honoured only from the owner on the untouched
  message they were posted with.

## Staying online

Socket Mode fails in a way that looks like health from every angle: the process
stays up, the supervisor reports it running, the dashboard answers, and the logs
go quiet - which is indistinguishable from a quiet afternoon. Twice that has
been a multi-hour outage nobody could see, because `KeepAlive` only revives a
process that has actually **exited**.

So the connection watches itself. If the socket is not connected and has not
come back within three minutes - including a client stuck reconnecting forever,
which is what both outages actually were - the process exits and the supervisor
starts a fresh one. A blip that heals in seconds is left alone.

`GET /health` reports whether the bot can **hear Slack**, not whether it is
running:

```json
{ "ok": false, "slack": "NOT listening - reconnecting for 14m", "state": "reconnecting" }
```

It answers `503` when deaf, so an uptime check sees an outage instead of a
process that happens to be alive.

## Stuck work

Every 15 minutes, outside any turn, the bot looks for work that died without
saying so: Orca tasks still `dispatched` whose worker is gone (its terminal
exited, it settled without reporting, or Orca no longer knows the dispatch),
and open PRs on its own repo with no commit, comment or review for 30 minutes
that are not simply waiting on a person (an approved PR, or one ready for review
with every check green, is the reviewer's to move, so it is not reported).
It DMs the owner (`OWNER_SLACK_ID`) one short message listing what is new, each
with the Slack thread that started it (recorded when the bot opens the PR), and does not repeat an item for 4
hours - a restart does not reset that. When Orca or `gh` cannot be asked it
says nothing rather than claim all is well; `mindful` shows the same lists on
demand, with a "could not check" line when that happens.

A task is closed rather than reported when its work was in fact done: the worker
succeeded (not died, failed, stopped or waiting on a question) and the Slack
thread that started it holds a message from the bot itself posted after the
worker ended. The task is then set `completed` with the result
"auto-closed: worker succeeded and the thread has a report after it ended", and
`mindful` adds one quiet line, "auto-closed N reported tasks". A person's reply,
a bot post from before the worker ended, no linked thread or a Slack read that
fails never closes anything: the task stays in the list.

## Stale promises

A turn sometimes ends with "next I will update the post" (or "việc tiếp theo là
...", "xong em gửi ...") without setting a watch, a reminder or a worker, so
nothing is left to do it and the thread goes quiet until someone prods it. Every
15 minutes, outside any turn, the bot looks at the threads it spoke in during the
last 24 hours. A thread counts as a stale promise when the newest message is the
bot's own and is over 30 minutes old, no turn, workflow, watch, reminder or live
Orca worker is attached to the thread, and that message really promises more work
(a cheap English + Vietnamese check, then one yes/no question to the small model;
a question to the person, an offer or a finished answer is not a promise). The
bot then steers that thread's own session once, the same internal turn `tell`
uses: do the work now, set a watch, or end with `NO_REPLY` if nothing is pending.
The sweep itself posts nothing to Slack and nobody is DMed. A message is nudged at
most once, even across restarts, a thread is nudged again only after a person has
spoken in it, and at most 3 threads are nudged per sweep.
`STALE_PROMISE_INTERVAL_MS=0` turns it off.

## How the brain runs a command

The brain can run the bot's own commands for whoever it is talking to (and its internal ones, like `journey` and `bug-report`, which nobody else may run). It never
names the actor - the bot mints a one-turn **ticket** bound to the current
speaker, and the command runs as them.

The ticket lives in the spawned CLI's **environment**, not its prompt. That is
not a detail: a thread holds one long-lived session, so every system prompt it
was ever handed is still in its context. A ticket printed there is one the model
will eventually retype from memory - expired by then, since tickets have a TTL,
a use count, and die with a restart. When that happens every command in the
thread comes back `that ticket is not valid any more` and nothing said inside
the conversation can fix it.

It also closed a worse door. A remembered ticket belonged to whoever was
speaking when it was issued, so reusing one would have run a command as somebody
else - exactly the escalation the ticket exists to prevent.

A process environment cannot be stale: it was set when the turn began.

**What the thread sees.** A command a person types shows its output in the
thread. A command the brain runs on its own (checking `mindful`, a status) is
hidden: the output goes back to the brain only and nothing is posted. When the
person directly asked for the command ("bomb that message"), the brain runs it as
`jarvis-run.sh <endpoint> --show <command>` and it shows like a typed one.
The bridge refuses `quick-review` outright, whoever asked: that command runs only from a person's own message. Commands that post by themselves outside this bridge (pickers, GitHub reviews)
are not affected.

## Secrets and turns

A turn is a `claude -p` process whose shell a model drives while it reads text
nobody vetted: messages, web pages, files. Anything in that process's
environment is one `env` or one `curl` away from leaving the host, and the bot
used to hand every turn a copy of its own environment - `SLACK_BOT_TOKEN`
included - and tell it to `curl` Slack with it.

**The environment.** A turn gets the bot's environment minus every
credential-shaped variable: any name with a `TOKEN`, `SECRET`, `PASSWORD`,
`API_KEY`, `ACCESS_KEY`, `PRIVATE_KEY` or `CREDENTIAL` word in it, a password glued to a
prefix (`PGPASSWORD`), or a `_KEY`, `_PAT`, `_PWD` or `_AUTH` ending. That is a rule
by name, so a `*_TOKEN` you add to `.env` later is withheld without a code
change. Two things stay: `CLAUDE_CODE_OAUTH_TOKEN` (the CLI cannot authenticate
without it) and whatever you list in `TURN_ENV_PASSTHROUGH`. The boot log says
how many variables were withheld and their **names**, never their values.

Withheld from every turn: `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`,
`ANTHROPIC_API_KEY`, `GITHUB_APP_WEBHOOK_SECRET`, and the variables that only
name where a secret lives (`TOKEN_KEY_PATH`, `TOKEN_DATABASE_PATH`,
`GITHUB_APP_PRIVATE_KEY_PATH`, `GITHUB_APP_WEBHOOK_SECRET_PATH`, ...), plus any
other credential-shaped variable in the environment the bot was started with.
If `LLM_PROVIDER=claude-cli` is authenticated by `ANTHROPIC_API_KEY` instead of
the recommended `CLAUDE_CODE_OAUTH_TOKEN`, add it to `TURN_ENV_PASSTHROUGH`.

**Slack.** A turn calls Slack through `bin/slack-api.sh <method> key=value...`.
The helper presents `JARVIS_SLACK_TICKET`, a ticket minted for that one process
when it starts and revoked when it exits, to the bot's loopback endpoint
(`POST /api/slack/proxy`). The bot checks the ticket, checks the method against
an allowlist and calls Slack with the token it holds; Slack's own answer comes
back unchanged. The ticket names no person and carries no role, only whether the turn is the owner's: it cannot run a
command or act on GitHub, and a command ticket cannot call Slack.

| | methods |
|---|---|
| read, any channel | `conversations.history`, `conversations.replies`, `conversations.info`, `conversations.list` (public channels), `conversations.join` (public channels), `users.info` |
| write, only the channel the turn runs in (any turn but the owner's) | `chat.postMessage`, `chat.update`, `reactions.add`, `files.getUploadURLExternal`, `files.completeUploadExternal` |
| write, owner's turn, any channel | every channel-scoped write above except `chat.update` (`chat.postMessage`, `reactions.add`, `files.completeUploadExternal`, and the owner's added writes by their own channel parameter; `channels` still refused, no thread_ts means the top level there; each is logged with method and target channel), `chat.update` on a message the bot itself wrote (the bot reads it first and refuses any other author's) |
| added by the owner | whatever `slack-methods` has added (a read, or a write locked to the turn's channel like the built-in writes, except in the owner's turn); stored in the `slack_extra_methods` setting, the built-in rows above cannot be removed |
| files | a private file is `bin/slack-file.sh`, through `POST /api/slack/file`: Slack file urls only, and the token never follows a redirect off Slack |

A `chat.postMessage` or `files.completeUploadExternal` from a turn that runs in a
thread and names no `thread_ts` is posted into that thread; pass `thread_ts=none`
for a deliberate top-level post (the bot removes it before calling Slack), and an
explicit `thread_ts` is used as given.

To allow another Web API method without a code change, the owner runs `X/jv slack-methods add <method> read|write [channelParam]`
(for example `add conversations.setTopic write`; `list` and `remove <method>` manage it). Only a line the owner types changes the list: it is refused when Jarvis runs it for a turn, so a turn cannot widen its own access. The name must look like `family.method`, and
`auth.*`, `admin.*`, `apps.*`, `oauth.*`, `tooling.*` and `openid.*` are refused. The bot's token also needs the method's Slack scope
(`conversations.setTopic` / `setPurpose` need `channels:manage`, and `groups:write` for private channels).

Anything else is refused (`method_not_allowed`), a write to another channel is
`channel_not_allowed`, and a missing, revoked or expired ticket is refused before
anything else. `slack-read.sh`, `slack-react.sh`, `slack-file.sh` and
`slack-upload.sh` are built on the same helper, so a sandboxed role has no more
power than before (reacting and uploading now only work in the turn's own channel). A watch predicate and a loop script are admin-written shell
that runs **as the bot**, so they keep the bot's own environment; `watch reply`
gets a read-only ticket for the length of each check.

**What this does not do.** It takes the token out of the turn's environment.
Reads are not channel-scoped, so a turn in a public channel can still read a
private conversation the bot is in and write it into that channel (the token
allowed the same before). A full-access turn is still the host user: it can read `.env` and the token files
off disk, and the dashboard's loopback API has no authentication, so it can reach
the console routes (`/api/slack/post`, ...) with `curl` and act as the bot in any
channel. Closing those is a separate decision about what a full-access turn may
read and call.

## Stopping a turn

A chat turn can run for the better part of an hour, so there is a way to end one
that is going the wrong way instead of waiting it out.

Send anything while a turn is running and the thread says nothing: the message
queues silently and runs when its turn comes. There is no "still working on ...
yours is next" notice. To end the running turn, press Slack's own stop button on
the session, or use `//bot stop`. Both follow one rule: your own turn, or an admin
or the owner for someone else's. Anyone else's press is ignored (they get a
private notice) and the turn keeps going.

`//bot stop` ends the turn from a thread without needing a new message: a turn
going wrong while you have nothing to add.
It also ends the background agents the thread's turns started outside their
own process - `claude --bg` sessions and Orca workers, from this turn or an
earlier one - and says what it stopped ("stopped the turn, and 1 background
agent it started"). They are found from the thread's tool log (the launch
command and the id it printed) and stopped with `claude stop` /
`orca orchestration worker-stop`, never by killing processes, so nobody
else's session is touched. Background agents started with the Agent tool run
inside the turn and end with it.

Your own turn is yours to stop. Stopping someone else's takes an admin, because
a turn is their work and - with per-user tokens - their money. A button that
outlived its run says so rather than failing: it sat in the channel while the
work finished on its own.

A stopped turn is **not** reported as a failure. It is killed the same way a
timeout kills one, so without care it would come back as "ran past my time
limit"; whoever stopped it already knows, and the thread has been told.

## Orca workers' questions

An owner turn that starts an Orca worker (`orca orchestration worker-start`; no other role may) is that
worker's coordinator, through the bot's own Orca terminal - a bare shell, so
nobody would see a question the worker asks, and it would wait forever. The
bot links every worker to the Slack thread whose turn started it (chat or
workflow; a GitHub App turn has no thread and is not linked), reads each such
Run's mailbox every 30 seconds, and puts any question still waiting to that
thread as a turn opening with `[orca question]`. The turn answers it with
`orca orchestration reply` from what the thread knows, or picks the safe
option and says so; it never waits on the thread. Each question is delivered
once, a delivery a restart cut is retried while the question is still open,
and an answered question or a finished worker gets no turn. In a workflow
thread the question goes to the workflow's worker session, not the front,
since only the worker can run `orca`.

## What an Orca worker cost

Orca keeps no tokens, cost or session id for a worker, so the bot reads them
from the worker's own Claude Code transcript: `worker-read --source
transcript` gives one of its message ids, and that id is the `uuid` of a line
in `~/.claude/projects/<worker folder>/<session>.jsonl` (`$CLAUDE_CONFIG_DIR`
moves the root). The session and its subagents' transcripts are summed, each
API message once, and priced per model at list price (input, output, 5-minute
and 1-hour cache writes and cache reads apart; the one price table is
`MODEL_PRICES` in `src/domain/workerUsage.ts`). When a `watch worker` fires on
a worker that finished or died, the hand-back says what it used and the turn
says it in the thread; the figure is stored in `orca_worker_usage`.
`worker-cost <ctx_...>` answers later (from the stored figure once Orca has
forgotten the dispatch), and `worker-cost <run_...>` totals a Run. Nobody is
invoiced this on a subscription; it is what the work would cost at API prices.

## Followed threads: wait, then ask a cheap model

The bot answers untagged messages in a thread it follows (one it started, or one
somebody pointed it at with `follow`). It used to run a full main-model turn for
each message and let that turn decide to stay quiet, which is the expensive way
to say nothing, and replies burst when people sent several lines in a row. Now
those messages wait in a short per-thread buffer first:

1. Every new message in the thread resets a quiet window (default 25s). A hard cap
   counted from the first buffered message (default 90s) means a busy thread is
   never held for ever.
2. When the window ends, a cheap model (the `pal` model, Haiku by default, no tools)
   reads the batch plus the few messages before it and answers `reply`, `skip` or
   `wait`, with a short reason. `wait` buys one more quiet window, still under the
   cap; at the cap `wait` counts as `reply`. When unsure it answers `reply`, and an
   error, a timeout or an answer that cannot be read is a `reply` too.
3. Only `reply` runs the main turn, once, with every buffered message in order and
   who wrote each.

Never held, and handled exactly as before: tagged messages, DMs, threads that are
just the bot and one person, command lines (`//bot ...`) and spoken review
requests (those are only ever a tag: an untagged reply is never one). A message from somebody off the allowlist is not buffered either. A
one-on-one thread is recognised from the thread itself (the bot has written and
exactly one human has), not from why it is followed: it is followed for good from
its second message on, which makes its route read "asked", and it must still never
wait.

A message that is not held is answered at once, and takes over whatever the thread
had buffered only when it will itself run a chat turn for an allowed user (allowed,
not a command line, has text beyond the tag): that turn reads the buffered messages
in its thread context, so the pending batch is dropped and its inbox rows settle,
and it cannot fire later into a second, out-of-order answer. A message from
somebody off the allowlist (untagged, or an @-mention that becomes an access
request) and a command line answer none of the buffered messages, so they leave the
batch alone to fire on its own. Past the hard cap the gate never loops: a newer
message arriving while the model reads does not restart the window. Any answer
except `skip` replies with the whole current batch; a `skip` settles only the
messages the gate actually read (they were skipped) and carries the unseen ones
into a fresh batch with a new cap, so a skip never swallows a message the model
did not see and a busy thread cannot hold its rows open for ever. The batch runs as its least-privileged author (role, tools and access), so a
lower-role request plus a higher-role "+1" in the same window never runs on the
higher role's tools. A turn that fails marks its rows failed, not done.

A restart does not lose the buffer: a message's inbox row stays open until its
batch is answered or skipped, so after a restart the row is redelivered and the
message is buffered again.

**Settings** (the `settings` table, edited like `follow_own_threads`; read per
message, so a change needs no restart):

| key | default | meaning |
| --- | --- | --- |
| `follow_gate` | on | `off` goes back to one main turn per message |
| `follow_debounce_seconds` | `25` | quiet time after the latest message before the batch is judged |
| `follow_debounce_max_seconds` | `90` | longest a batch is held, from its first message (at most 600) |

Not a number, or not above zero, means the default; the cap is never shorter than the
quiet window. The gate uses the model for the `pal` role (`CLAUDE_MODEL_PAL`, or
`model:pal`), see [Model per role](#model-per-role-and-per-channel).

**Tuning.** Every decision logs one line, including `skip`, so you can see what the
gate is keeping quiet about:

```
follow gate channel=C0123 thread=1731.0001 batch=3 verdict=skip: people are talking among themselves
```

A line for a window that was extended, a verdict that was superseded by a newer
message, or a gate that timed out says so in parentheses. If it skips things it
should have answered, read the reasons first (the prompt is `gateSystem` in
`src/domain/followGate.ts`), or set `follow_gate=off` while you decide. If replies
come too late, lower `follow_debounce_seconds`.

## Muting a thread

`//bot mute` (in the thread, or `//bot mute <thread link>`) turns the bot off for
that one thread: it answers nobody there, even when tagged. A message from a person
is dropped at the door, before any turn or session starts, so it costs no tokens and
gets no reply, no reaction and no "working" placeholder. This holds for channel
threads, a DM thread's replies and an untagged reply it would otherwise follow.
`//bot mute list` shows the muted threads; `//bot mute off` lifts it.

- Known commands still run in a muted thread (`//bot mute off`, with a leading tag
  or the legacy `!status`), which is how `mute off` works from inside it.
  Everything else a person writes is ignored, an unknown command included.
- A mute outranks a `follow`: the follow stays saved but is suppressed while the
  thread is muted, and comes back with `mute off`. `follow list` and `mute list`
  both say so.
- It is about people's messages. Work the bot already has bound to the thread keeps
  running and may still post there: a watch handing the thread back, a loop, a tell
  and a workflow's steps.
- Same role level as `follow` (executer and up). Stored in `muted_threads`
  (`db/muteRepo.ts`), checked in memory.

## One turn at a time

A thread's turns run one after another, never beside each other. Two messages a
few minutes apart used to spawn two independent runs that each did the whole
task: two branches, two implementations, two pull requests, neither aware of the
other.

It is also what the session model requires - a thread holds one CLI session, and
two `--resume` processes on one session id are two conversations overwriting
each other's history. Queued this way, the second message runs with the first's
result already in the session, which is what makes a follow-up mean "and the
rest" rather than "again, from scratch".

Commands are deliberately not queued: a review is its own process with its own
session, and holding one behind a long chat turn would make it look dead.

### Messages queued behind a turn are answered together

Send a, then b, c, d, e while a runs, and b..e do not take four turns of their own:
they wait as one group, and when a ends - finished, failed or stopped - they run
as ONE turn with one reply. The turn reads them from the thread, so each keeps its
author, timestamp, attachments and links, and is told these were several messages
sent while it was busy. The newest message carries the turn (its stream and
reply); the others settle when it ends and post nothing (their inbox rows stay open until then, so a restart that cuts the turn re-delivers each of them).

Only a person's own typed messages from the same author merge. Every turn the bot
starts itself (a watch hand-back, a worker's question, a loop, a nudge, a
workflow step) keeps its own turn and is a barrier the groups do not merge
across: each carries its own instruction, and a turn runs under one person's role
and budget. Messages that arrive while the combined turn runs form the next group.

Stop ends only the running turn, so waiting messages are never dropped by it:
after a stop they start at once as one turn. With nothing running (only messages
queued behind a bot-started turn) there is nothing to stop, and `stop` says how
many are waiting.

## One session per thread

A Slack thread is one conversation, so it gets **one Claude Code CLI session**.
The first message in a thread opens it (`--session-id`), every later one resumes
it (`--resume`), and the model keeps its context, its reasoning and its files
between turns instead of starting cold and being handed a transcript each time.

A resumed turn is given only what it has not seen: everything said in the thread
since its last turn, including messages the bot was not addressed in. The bot's
own SQLite memory still records every turn - it is the fallback when a session
is gone, and what the dashboard reads.

Sessions are keyed by **thread and access tier**, not thread alone. Full-access
(`tools:full-access`, the owner as seeded) and sandboxed roles run the CLI in different
working directories, and the CLI files a session under the directory it ran in -
so they could not share one in any case, and sharing would hand a sandboxed user
whatever a full-access session had read.

A session that will not resume is not an error anyone sees: the CLI prunes its
own history and a committed database outlives the machine it was written on, so
`No conversation found with session ID` means "start a fresh one and read the
thread back in", silently. A genuine failure still surfaces.

```
//bot session          what this thread is on
//bot session reset    drop it; the next message starts fresh
//bot session off      admins: back to a cold call per turn
//bot session on       admins: back on
```

## Calling it from GitHub

A GitHub App lets people call the bot where the work is. Mention it in an
issue or PR comment, a review comment or a submitted review
(`@<slug> why does this fail?`), or add the `jarvis` label to an issue
or PR. It puts 👀 on the comment, posts the request into a Slack channel
(`github-app channel #channel`, else the review inbox channel) and runs a turn
in that post's thread **as the person who called**, matched like the review
inbox does (`review-inbox link <github-login>`, else exactly one display-name
match), so their role applies and the turn runs on the bot's credential. Someone it cannot
place gets one comment explaining how to link, and nothing runs.

**A mention that asks for a review on a PR, the label on a PR, or a review
requested from the app is not that kind of call**: it starts a review, see
[Reviews that start by themselves](#reviews-that-start-by-themselves). (GitHub
does not let a PR request a review from an App's bot - the reviewers API refuses
it - so in practice the mention and the label are the two ways in; if a
`pull_request.review_requested` event with the app as the reviewer does arrive it
is handled the same.) Subscribe the app to `pull_request`, `issue_comment`,
`pull_request_review` and `pull_request_review_comment` events, with pull
requests and issues read & write and contents read.

The turn posts its answer back on the issue/PR, as the app, through
`bin/github-app-comment.sh <owner/repo> <number> <body-file>` -> loopback
`/api/github-app/comment`. The request carries the turn's ticket, and the bot
only posts to the issue that turn's thread was opened for. If the turn ends
without posting, its reply is posted for it.

For anything wider, a turn can act as the app on any repository it is installed on
(`acme`, `cute-me-on-repos`, ...) when the person it runs as holds the action's grant
(`github:<action>`, one per action below: `git` and `push` are separate grants, and `push`
must use the `push` subcommand). As seeded that is the **admin and the owner** (all twelve), and the **executer** for `git` (commit as the app, **identity only, no token**: a role gets the installation token only when it also holds `github:push`), `pr-create`, `pr-edit`, `comment`, `labels-add` and `reviewers-request` - never push, review, merge or close. The owner
grants any of them to another role (`role grant executer github:pr-create github:comment`)
with no code change:

```
bin/github-app.sh pr-create <owner/repo> --head <branch> --base <branch> --title <t> --body-file <f> [--draft]
bin/github-app.sh comment <owner/repo> <n> <body-file>
bin/github-app.sh review <owner/repo> <n> APPROVE|REQUEST_CHANGES|COMMENT [body-file]
bin/github-app.sh pr-edit <owner/repo> <n> [--title <t>] [--body-file <f>]
bin/github-app.sh pr-close|pr-reopen <owner/repo> <n>
bin/github-app.sh pr-merge <owner/repo> <n> [--method merge|squash|rebase]
bin/github-app.sh labels-add|labels-remove <owner/repo> <n> <label>...
bin/github-app.sh reviewers-request <owner/repo> <n> <login|team:slug>...
bin/github-app.sh git <owner/repo> <local-repo-dir> -- <git args>...
bin/github-app.sh push <owner/repo> <local-repo-dir> <branch> [--force-with-lease]
```

`git` runs `git -C <dir> <args>` **as the app**: commits and cherry-picks are
committed by `<slug>[bot]` (`<id>+<slug>[bot]@users.noreply.github.com`,
no GPG signing; the id is looked up once with `GET /users/<slug>[bot]`), and
anything that talks to github.com (fetch, pull, push, ls-remote; an ssh remote
is read as https) carries a fresh installation token. `push` pushes one branch
to the remote of `<dir>` that points at `<owner/repo>`. The token is a one-shot
credential: the bot hands it back for the `git-auth` action (same ticket, same
grant gate (an executer gets the identity with no token, so it can commit but not push), same command log row, no token in the log) and the helper puts
it in that one git process's environment as `http.extraheader` throu