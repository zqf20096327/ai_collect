# <img src="src-tauri/icons/icon.png" width="48" height="48" alt="" align="absmiddle"> Drifty

AI time tracker for Mac and Windows.

**[Download](https://drifty.so/download/)** · [Website](https://drifty.so/) · [Docs](https://docs.drifty.so/) · [Releases](https://github.com/edgethink00/drifty/releases) · [Changelog](https://drifty.so/changelog/) · [Discord](https://discord.gg/UGCtQAaDGN) · [X](https://x.com/driftyso)

## What it does

<table>
<tr>
<td width="40%" valign="middle">
<h3>Your day, tracked automatically</h3>
Drifty records your apps and tabs. AI names each block of work and marks it focus or drift.
</td>
<td width="60%" align="center"><img src=".github/assets/readme/day.png" alt="A day in Drifty: blocks of work named by AI, such as Dashboard page refactor and Reddit and YouTube break, colored as focus, drift or neutral" width="100%"></td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>Project time without bookkeeping</h3>
Describe a project once. Drifty fills in the time.
</td>
<td width="60%" align="center"><img src=".github/assets/readme/projects.png" alt="Project time over the latest seven days, stacked by project" width="100%"></td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>A way back when you drift</h3>
Companion offers a way back when you drift. The cat keeps you company.
</td>
<td width="60%" align="center"><img src=".github/assets/readme/way-back.png" alt="Companion card offering Return to focus, Take a break or Not a drift, next to Drifty's desk cat" width="100%"></td>
</tr>
<tr>
<td width="40%" valign="middle">
<h3>Bring your own AI</h3>
Run it on your own computer, with your own key or in Drifty Cloud.
</td>
<td width="60%" align="center"><img src=".github/assets/readme/bring-your-own-ai.png" alt="Ways to run Drifty AI: Local AI, a custom endpoint, Claude Code, Codex CLI, your own OpenAI, Anthropic or OpenRouter key, or Drifty Cloud" width="100%"></td>
</tr>
</table>

- **Ask about your day.** Chat answers questions about your records, and agents
  such as Claude Code can read them too.
- **One timeline across devices.** Sign in to sync your Mac and Windows
  computers and see your day on iPhone.

## Privacy

Your activity history stays on your computer unless you use a feature that
needs it. AI classification sends minimized activity fields to the AI you
picked, sync copies your records to your own account, and the leaderboard shows
focus totals only. In the official app, Usage statistics (Settings › Privacy) is
on by default: it sends usage events and, while you are signed in, keeps
minimized activity records to improve Drifty. Chat sharing stays off unless you
turn it on. The [privacy policy](https://drifty.so/privacy/) lists every case.

## What is in this repository

| Path | Contents |
| --- | --- |
| `apps/desktop` | React and Vite user interface |
| `packages/domain` | Shared activity models, time rules and AI prompt building |
| `packages/charts` | Chart components |
| `src-tauri` | Tauri 2 shell, Rust commands and native macOS and Windows code |
| `services/tracker-python` | Activity capture and local storage |
| `integrations/skills` | Agent skill for reading Drifty records |

Drifty Cloud's server (accounts, billing, cloud AI, sync and leaderboard), the
iPhone app and the engine behind the automatic memory beta are not in this
repository.

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

Without Supabase settings a source build runs signed out: tracking, local
history and your own AI connections all work. Signing in, which the official app
asks for, needs Drifty's hosted service.

Checks:

```bash
npm run typecheck
npm run lint
npm test              # web, Python and Rust tests
```

A source build uses the same app identifier as the official app, so quit the
official Drifty before running one. Windows source builds work but are not
documented here yet.

## Release history

Release notes from 1.23.0 are on
[GitHub Releases](https://github.com/edgethink00/drifty/releases). Earlier
installers are in [Legacy releases](https://github.com/edgethink00/drifty_releases/releases)
(Mac 1.6.0–1.23.0, Windows 1.11.26–1.19.2).

## Roadmap

- [x] AI time tracking for Mac (Apple Silicon)
- [x] For Windows
- [x] For iPhone — [App Store](https://apps.apple.com/app/id6824176729)
- [x] For AI agents — [Drifty skill](integrations/skills/drifty/SKILL.md)
- [ ] For Intel Mac — [Waitlist](https://drifty.so/intel-mac/)
- [ ] For Linux — [Waitlist](https://drifty.so/linux/)
- [ ] For Android — [Waitlist](https://drifty.so/android/)
- [ ] For Teams — [Limited beta](https://drifty.so/teams/)

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
