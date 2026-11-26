# <img src="src-tauri/icons/icon.png" width="48" height="48" alt="" align="absmiddle"> Drifty

AI time tracker for Mac and Windows.

**[Download](https://drifty.so/download/)** · [Website](https://drifty.so/) · [Docs](https://docs.drifty.so/) · [Releases](https://github.com/edgethink00/drifty/releases) · [Changelog](https://drifty.so/changelog/) · [Discord](https://discord.gg/UGCtQAaDGN) · [X](https://x.com/driftyso)

Drifty records the app, window and supported browser tab
in front of you, and AI sorts each stretch into focus, drift or neutral. You
never start a timer or tag anything. The official app asks you to sign in with
a Drifty account; a build from source runs without one.

## Release history

[GitHub Releases](https://github.com/edgethink00/drifty/releases) lists desktop
release notes starting with 1.23.0. For the original stable installers, see
[Legacy releases](https://github.com/edgethink00/drifty_releases/releases)
(Mac 1.6.0–1.23.0, Windows 1.11.26–1.19.2). Get the current installer from
[drifty.so/download](https://drifty.so/download/).

## What it does

- **Records on its own.** Drifty builds the timeline from the app, window and
  browser tab in front of you, and notices when you step away.
- **Reads the context.** The same browser or editor can be focus for one task
  and drift for another, so Drifty classifies from what was on screen, not only
  from the app name.
- **Bring your own AI.** A local model Drifty downloads for you, a self-hosted
  endpoint, your own OpenAI, Anthropic or OpenRouter key, Codex CLI or Claude
  Code, or Drifty Cloud.
- **Projects without bookkeeping.** Describe a project once and Drifty sorts
  matching work into it.
- **Ask about your day.** Chat answers questions about your records, and agents
  such as Claude Code can read them through the Drifty connector or the
  read-only skill in [`integrations/skills`](integrations/skills/drifty/SKILL.md).
- **Mac and Windows.** With your Drifty account you can sync your computers,
  check your day on iPhone and join the leaderboard.
- **A desk cat, if you want one.** Pet Mode puts Drifty's cat on your desktop.

## Privacy

Your activity history stays on your computer unless you use a feature that
needs it. AI classification sends minimized activity fields to the AI connection
you picked, device sync copies your records to your own account, and the
leaderboard publishes aggregate focus totals only. In the official app, the
Usage statistics setting in Settings › Privacy is on by default: it sends
product usage events and, while you are signed in, keeps minimized activity
records with your account to improve Drifty. Sharing your Chat conversations is
a separate setting that stays off unless you turn it on. The
[privacy policy](https://drifty.so/privacy/) lists every case.

## What is in this repository

| Path | Contents |
| --- | --- |
| `apps/desktop` | React and Vite user interface |
| `packages/domain` | Shared activity models, time rules and AI prompt building |
| `packages/charts` | Chart components |
| `src-tauri` | Tauri 2 shell, Rust commands and native macOS and Windows code |
| `services/tracker-python` | Activity capture and local storage |
| `browser-extension` | Archived Chrome extension experiment; the app does not use it |
| `integrations/skills` | Agent skill for reading Drifty records |

Drifty Cloud's server (accounts, billing, cloud AI, sync and leaderboard) and
the iPhone app are not part of this repository. The automatic memory beta
downloads a separate engine that is not published here either. A build from source runs
fully on your computer; signing in needs Drifty's hosted service.

## Build from source

The steps below are for macOS 13 or later. You need Node.js 24, Rust 1.90 or
later, Python 3 and the Xcode Command Line Tools. Tauri expects the bundled
tracker binaries when it compiles, so build them once before the first
`npm run tauri:dev`.

```bash
npm ci
python3 -m venv .venv
.venv/bin/pip install -r services/tracker-python/requirements-build.txt
DRIFTY_TRACKER_BUILD_PYTHON="$PWD/.venv/bin/python" npm run build:tracker-sidecar
npm run tauri:dev     # run the app
npm run dev:web       # interface only, in a browser at http://127.0.0.1:1420
```

Without Supabase settings the app runs signed out: tracking, local history
and your own AI connections all work.

Checks:

```bash
npm run typecheck
npm run lint
npm test              # web, Python and Rust tests
```

A source build uses the same app identifier as the official app, so quit the
official Drifty before running one. Windows source builds work but are not
documented here yet.

## Community

Come say hi, ask questions and tell us what to build next.

- **[Discord](https://discord.gg/UGCtQAaDGN)** for questions, feedback and release news
- **[X @driftyso](https://x.com/driftyso)** and **[Instagram @drifty.so](https://www.instagram.com/drifty.so/)** for updates
- **[Issues](https://github.com/edgethink00/drifty/issues)** for bugs and feature requests
- **Star this repository** to follow along, and choose *Watch › Custom › Releases* to hear when a new version ships

## Contributing

Bug reports from real setups are the most useful thing you can send. Pull
requests are welcome; please read [CONTRIBUTING.md](CONTRIBUTING.md) first.
Contributors sign the [Contributor License Agreement](CLA.md) once.

Report security issues privately as described in [SECURITY.md](SECURITY.md).

## License

Drifty's source is licensed under the [GNU Affero General Public License
v3.0 only](LICENSE). The Drifty name, logo and cat character are trademarks of
EdgeThink and are not covered by that license; see [TRADEMARKS.md](TRADEMARKS.md).
