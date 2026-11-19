<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.png">
    <img src="docs/assets/banner.png" alt="Who Ate My Tokens? Token observation layer for T3 Code, Claude Code and Codex" width="100%">
  </picture>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-3a2f3d"></a>
  <img alt="Rust" src="https://img.shields.io/badge/built%20with-Rust-c49012">
  <img alt="macOS first" src="https://img.shields.io/badge/macOS-first-8d5fc0">
  <img alt="Local only" src="https://img.shields.io/badge/data-stays%20local-3f7fc2">
</p>

# Who Ate My Tokens

*Your agents, caught snacking live.*

A local, read-only token observation layer for T3 Code, Claude Code and Codex. It shows live threads and subagents with the model behind each one, the 5-hour and weekly limits, a 30-day history and API-equivalent cost by project. One Rust binary, one page, and nothing leaves your machine.

Open it at <http://127.0.0.1:7317> once it is running.

## Screenshots

All images below come from the built-in [demo mode](#demo-mode), so they contain no real data.

| | |
|---|---|
| ![Overview in the light theme](docs/screenshots/overview-light.png) | ![Overview in the dark theme](docs/screenshots/overview-dark.png) |
| ![The 5-hour plate](docs/screenshots/plate.png) | ![The day timeline](docs/screenshots/timeline.png) |
| ![Cost by project](docs/screenshots/projects.png) | ![Thread drill-down](docs/screenshots/drill.png) |
| ![The page on a phone](docs/screenshots/phone.png) | |

## Features

### Live view

- Every active T3 Code thread with its subagents, model, current step, context fill and tokens so far. Click a row, or press Enter on it, for that thread's runs, tool counts, subagents and a 10-minute token timeline.
- Claude Code and Codex sessions outside T3 appear as their own lanes.
- Press `/` to filter by title, project, branch or model. The tab title and favicon show the plate and anything waiting on you.

### Limits

- A 5-hour plate with a run-out forecast from the last 30 minutes, plus Codex's own limit line.
- A weekly meter. When Claude Code's status line reports `rate_limits`, those numbers become the hero percentage and reset time; the local estimate is shown alongside.
- A manual "Calibrate from /usage" fallback, kept only in this browser, for stale or missing reports.

### History and cost

- Today against yesterday and the day before, then the week so far and a compact 30-day strip stacked by model family.
- PRs with CI checks and review states, spoiled leftovers (requests that rebuilt over 50K tokens of expired cache), and API-equivalent dollars at list prices.
- "Who ate it, by project" rolls 30 days up by T3 project title, or by working-folder name outside T3.
- "Copy yesterday", "Copy today" and "Download CSV" for standups and spreadsheets.

### Saving tokens

- Diet tips for today and yesterday: heavy contexts, peak concurrency, marathon sessions, Opus subagents, spoiled cache and the note-taker's share. Each tip names the threads behind it. No message content is read.

### Alerts

- "Notify me" enables desktop notifications for a thread waiting on you, a cache about to go cold, a thread passing 85% context, one thread eating over 25% of the plate in 30 minutes, the plate passing 80% or running out before reset, and a summary after 20:00.

### Sharing

- A tiny `/api/brief` JSON summary for a menu-bar plugin or status line.
- Screenshots can be taken safely with demo mode: open `/?demo` and the page loads synthetic fixtures instead of any live data.

## Quick start

```sh
cargo build --release
scripts/wamt start
scripts/wamt open
scripts/wamt login on        # optional: start at login, low priority
scripts/wamt statusline on   # optional: show the plate in Claude Code
```

Other commands:

```sh
scripts/wamt status          # pid, memory, CPU
scripts/wamt logs            # last log lines
scripts/wamt stop
scripts/wamt restart
scripts/wamt update          # test in Docker, rebuild, restart, health-check
scripts/wamt update --no-docker
scripts/wamt login off
scripts/wamt login status
scripts/wamt statusline off
scripts/wamt statusline status
```

With the login item on, `start`, `stop` and `restart` go through launchd; `stop` keeps it stopped until next login. Stopping loses nothing: the next start reads only what changed since.

## Requirements

- macOS is the first-class target (launchd login item, menu-bar plugin, status line wrapper).
- Linux works for the server itself; the macOS-only launcher is not needed. The Docker scripts below run the Linux build.
- Rust stable, for building from source.
- T3 Code and/or Claude Code and/or Codex installed. Any one of them is enough; the dashboard shows what is present and says so when a source is unavailable.

## Configuration

Every setting is an environment variable. Defaults use `~` below; the binary expands `$HOME` itself.

| Variable | Default | What it does |
|---|---|---|
| `WAMT_BIND` | `127.0.0.1:7317` | Address and port. Keep it on loopback. |
| `WAMT_T3_DB` | `~/.t3/userdata/statev2.sqlite` | T3 Code SQLite database, always opened read-only. |
| `WAMT_CLAUDE_ROOT` | `~/.claude/projects` | Root of Claude Code's JSONL transcripts. |
| `WAMT_CODEX_ROOT` | `~/.codex/sessions` | Root of Codex session files. Only the `sessions` folder is read. |
| `WAMT_STATE` | `.state` | Where the small cache files and log are written. |
| `WAMT_UI` | unset (page compiled in) | Serve the page from a file instead, for UI development. |
| `WAMT_ALLOW_HOSTS` | empty | Comma-separated extra `Host` values to accept, for containers. |
| `WAMT_UTC_OFFSET_MIN` | machine local offset | Override the UTC offset in minutes, mainly for tests. |

The launcher also reads `WAMT_STATE`, `WAMT_URL` (probe URL, default `http://127.0.0.1:7317`) and `WAMT_DRY_RUN=1` (print steps without running them).

## Privacy and security

- Read-only on `~/.t3`, `~/.claude` and `~/.codex`. The T3 database is opened in SQLite `mode=ro` with short read transactions; transcripts are read from the last byte seen, without filling the page cache. No source is written to, locked or copied. Nothing under `~/.t3/userdata/secrets` is read.
- Metadata only: titles, models, statuses, tool names, times and token counts. Message text, tool inputs and outputs, commands and file paths never leave the parser.
- The server listens on 127.0.0.1 only and refuses requests whose `Host` is not localhost. It sends a strict Content Security Policy and `nosniff`, and makes no requests to any outside host. Fonts, the logo and the favicon are compiled into the binary.
- The only files written are in `.state/`: `transcripts.json` (offsets and numbers, about 150 KB), `t3.json` (which thread launched which, about 10 KB), `history.json` (daily totals older than the week, about 5 KB), `cc-limits.json` (Claude's two percentages and reset times) and `wamt.log`. Enabling the status line also writes `settings.json.bak` and `statusline-orig.json` there. Deleting `.state/` is always safe.

## How the numbers are made

- Tokens are counted from transcripts, once per API response (Claude Code writes one response over several lines), and checked with the independent counter in `tools/crosscheck.py`.
- Threads, runs, subagents, PRs and the live step come from T3's database. T3 sessions are joined to transcripts by session id. When T3 does not record which thread launched another, the launch is found inside the `t3_thread_launch` or `create_threads` call that created it.
- The 5-hour estimate opens a window at the first request after the previous one closed (rounded down to 10 minutes) and lasts five hours; T3-recorded resets override the guess. The meter compares weighted usage against the usage at the last limit hit. Chat on claude.ai and other devices count toward the real limit but cannot be seen here.
- The forecast projects weighted usage over the last 30 minutes (idle minutes included, never less than 5) to the cap.
- Claude's own `rate_limits` replace the estimate when the status line is installed. The wrapper writes only those two percentages and reset times; the page ages the report to decide whether it is still fresh.
- Codex counts in totals as its own app and model family, but not in the Claude plate. Its limit line is Codex's own number.
- Days are local calendar days. Seven are kept live (the last three in detail, days 4 to 7 as daily totals). Older days move to `.state/history.json`, which keeps up to 31 days, and are read once on a low-priority background thread from files last written inside that range.
- Dollars are API list-price equivalents, an estimate. Plans are not billed this way.

## Status line integration

`scripts/wamt statusline on` backs up `~/.claude/settings.json` to `.state/settings.json.bak`, saves the original `statusLine` object in `.state/statusline-orig.json`, and points `statusLine.command` at `scripts/statusline.sh`. The wrapper feeds your original command the same stdin, appends the plate and week from Claude Code's own numbers, and stores only `.rate_limits` in `.state/cc-limits.json`. It adds "needs you" when a T3 thread is waiting and the dashboard is running. Errors in the wrapper are swallowed so the status line never breaks. `statusline off` restores the saved object exactly. Only the command is ever printed, never settings values.

## Demo mode

Open <http://127.0.0.1:7317/?demo>. The page shows a small "demo data" tag in the header and never calls `/api/state`, `/events`, `/api/thread`, `/api/timeline` or `/api/brief`. It loads three synthetic JSON files compiled into the binary and served under `/assets/demo/` instead. The fixture workspace is entirely fictional: `acme-api`, `acme-web`, `docs-site` and `infra`, with threads such as "Refactor auth middleware", "Add billing webhooks" and "Fix flaky e2e tests". It includes an orchestrator with children and subagents, Opus, Sonnet, Haiku and GPT models, a 62% plate with a forecast, a weekly meter, 7 and 30-day history, PRs with checks and review states, diet tips, spoiled leftovers and a busy timeline.

Regenerate the fixtures after changing the page:

```sh
python3 tools/make-demo.py
```

The script is seeded, so output is identical on every run. Add `&theme=dark` for the dark theme and `&thread=thread:acme-api:refactor-auth-middleware` to open the drill-down.

## FAQ

**Does this send anything anywhere?** No. There are no outgoing requests of any kind, and the server binds only to loopback.

**Can it change my agent settings?** No. It never writes to `~/.t3`, `~/.claude` or `~/.codex`. The status line installer is the one exception and it only edits `statusLine.command`, with a backup and an exact restore.

**Why is my plate different from Claude's /usage?** The local estimate cannot see claude.ai chat, other devices or other apps. Install the status line integration to use Claude's own numbers.

**Why is T3 data paused but tokens still counting?** A T3 update renamed something this reads. Token figures keep working; the queries in `src/t3.rs` need updating. `scripts/wamt logs` shows details.

**How big is it?** Around 11 to 18 MB of memory and well under 1% CPU while idle. With no page open, it skips building the page data altogether.

**Can I run it without T3 Code?** Yes. Claude Code, Codex, or both work on their own.

**Is there a menu-bar option?** `scripts/swiftbar/wamt.30s.sh` is a SwiftBar or xbar plugin. Symlink it into your plugin folder; it reads only `/api/brief`.

## Disclaimer

Not affiliated with Anthropic, OpenAI or the T3 Code project.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/development.md](docs/development.md). Please report bugs through [GitHub issues](https://github.com/bankerneel/wamt/issues).

## Keywords

T3 Code extension, T3 Code token observation layer, Claude Code usage dashboard, Claude Code token tracker, Claude rate limit monitor, 5-hour limit tracker, weekly limit tracker, Codex usage, LLM cost dashboard, AI agent observability, local-first, Rust.

## License

MIT. See [LICENSE](LICENSE).
