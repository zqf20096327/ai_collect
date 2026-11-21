**English** | [简体中文](README.zh-CN.md)

# OneAI

**One desktop workbench for all your AI coding CLIs.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Platform: Windows](https://img.shields.io/badge/platform-Windows%2010%2F11-0078d4)
![Electron 31](https://img.shields.io/badge/Electron-31-47848f)

OneAI runs Codex, Claude Code, Kimi Code, OpenCode and other AI coding CLIs side by side, each in its own real terminal, inside one window. Sessions stay alive while you switch between tasks and folders, and quota, usage and accounts are visible at a glance.

## Why OneAI

Working with several AI coding CLIs usually means a pile of terminal windows. It is hard to tell which one is still working, which account each one is logged in with, and how much quota is left. OneAI puts them in one sidebar, grouped by project folder, and keeps every terminal running in the background while you work in another.

## Highlights

- **Folder tree with many tasks**: tasks are grouped under project folders, each with a status light, a Git branch badge and the latest message of its session. A "Needs review" mark tells you when a background task stopped producing output.
- **Persistent terminals**: built on xterm.js and Windows ConPTY (`node-pty`). Switching tasks or folders never ends a process.
- **Live quota in one line**: input / output / cache tokens, cache hit rate, context usage, cost, 5h / 7d limits and the active model in the top bar, with CPU, memory and network speed. Plain text only, no popups.
- **Multiple accounts**: run several Codex, Claude Code and Kimi Code accounts in parallel. An account is only a config directory plus environment variables, and OneAI never reads or copies your credentials.
- **Analytics Dashboard**: sidebar Dashboard (`Ctrl + Shift + D`) with multi-range KPI cards, a rolling 12-month activity heatmap, token / cost / session trends, Top 5 drill-downs, token composition, multi-group live account quotas and a sortable model table (plus the legacy weekly usage panel via `Ctrl + Shift + U`), all read from local session records.
- **Session history**: browse and resume past Claude Code, Codex and Kimi Code sessions.
- **Project tree & file preview**: open the right-side project directory tree drawer (`Ctrl + Shift + E`) to browse, filter and insert relative paths into the terminal, or Ctrl + click a path for a read-only preview with syntax highlighting and a code minimap.
- **Any CLI**: installed CLIs are detected from your `PATH`, and any other command can be added as a custom CLI.
- **English and Simplified Chinese**, 25 themes (light, dark, eye-care and editor palettes), and a short first-run guide.

See [docs/features.md](docs/features.md) for the detailed behavior of every feature.

## Supported CLIs

OneAI looks up these commands on your `PATH` at startup and offers the ones it finds. The list lives in [`src/main/known-clis.json`](src/main/known-clis.json), and Settings → CLI shows the detection state of each.

Codex, Claude Code, Kimi Code, OpenCode, Grok Build, Antigravity, Qwen Code, Aider, Cursor Agent, GitHub Copilot, Amp, Droid, Crush, Goose, iFlow CLI, Auggie, Kiro CLI, Cline and Pi.

A CLI that is not listed can be added under Settings → CLI with a name and a start command. All CLIs run in a normal terminal. Extra features depend on each CLI's local session format:

| | Quota | Task summary and history | Usage statistics | Multiple accounts |
| --- | :---: | :---: | :---: | :---: |
| Codex | yes | yes | yes | yes |
| Claude Code | yes | yes | yes | yes |
| Kimi Code | yes | yes | not yet | yes |
| Antigravity | yes | | yes | |
| Pi | | | yes | |
| Other CLIs and custom CLIs | | | | |

## Install

OneAI currently runs on **Windows 10 / 11 (x64)**, because it relies on the Windows ConPTY API. The AI CLIs themselves are not bundled: install the ones you want separately and make sure their commands are on your `PATH`.

- **Installer**: download `OneAI-Setup-<version>.exe` from the [latest release](https://github.com/keepingFE/oneAI/releases/latest) and run it.
- **From source**: see below.

On first launch OneAI asks for the interface language, then shows a short guide. After that, add a project folder, click the "+" next to it and pick a CLI.

## Build from source

Requires Node.js 18 or newer.

```bash
npm install
npm run dev              # start the workbench in development mode
npm run build            # type-check and build
npm run build:win        # installer: release/OneAI-Setup-<version>.exe
npm run build:portable   # portable build (optional): release/OneAI-Portable-<version>.exe
```

If an old artifact is locked and cannot be overwritten, write the new one to a separate directory:

```bash
npm run build:win -- --config.directories.output=release/ui-polish
```

### Checks

```bash
npm run check:ui     # UI regression check in a hidden Electron window (themes, layout, keyboard, terminal, settings, onboarding)
npm run check:main   # main-process and shared logic unit tests (PTY, TOML, music, summaries, file preview)
npm run check:i18n   # every UI string has an English translation
```

Check artifacts are written to `.tmp/ui-polish/`.

## Tech stack

Electron 31, React 18, TypeScript, Tailwind CSS, Lucide React, `@xterm/xterm`, `node-pty`, Vite 5 and `vite-plugin-electron`.

## Privacy

OneAI runs locally. It has no telemetry or analytics and no update checker. It reads the local session files of the CLIs you use to show history, summaries and usage, and it never reads or copies login credentials. The only network request OneAI makes itself is the Kimi Code quota lookup (`api.kimi.com`), which uses your own Kimi Code login and only happens while you use Kimi Code. If you add online music in Settings, the player also contacts exactly those addresses, and only to play them. The CLIs you start in the terminals talk to their own services as usual.

## Contributing

Issues and pull requests are welcome. Project conventions, directory layout and checks are described in [AGENTS.md](AGENTS.md) (written in Chinese). In short: commit messages are written in English, every user-facing string goes through `t()` with an entry in `src/shared/en.ts`, and `npm run check:ui`, `npm run check:main` and `npm run check:i18n` should pass.

## Contributors

- [Claude](https://claude.com/claude-code) (Anthropic) -- AI pair programmer; much of the code, tests and documentation was written with Claude Code.
- [Codex](https://openai.com/codex) (OpenAI) -- AI pair programmer; also used to write and review code and documentation.
- [Gemini](https://gemini.google.com) (Google) -- AI pair programmer; also used via Antigravity to build, optimize and verify features and documentation.

## License

[MIT](LICENSE)
