# PiWright

![Release](https://img.shields.io/github/v/release/php-programmist/PiWright)
![License](https://img.shields.io/github/license/php-programmist/PiWright)
![Platform](https://img.shields.io/badge/platform-Windows-blue)

**PiWright** is an open-source desktop GUI for the [pi coding agent](https://github.com/earendil-works/pi) — a native Windows app (Electron + React) that turns pi into a full IDE-like workspace: AI chat, agent-driven kanban, git branch graph, Monaco editor, terminal and remote access from your phone — in one window.

## Highlights

- **Windows + WSL** — two pi backends, native and WSL, auto-detection per project
- **Agent-driven kanban** — the agent picks tasks, moves cards, reports via comments
- **Everything in one window** — chat, git branch graph, diffs, editor, terminal
- **Remote access** — Telegram notifications and a PIN-protected web UI from a phone

---

## Features

### Chat

- Streaming chat with pi over RPC, markdown rendering with syntax highlighting
- Collapsible tool-call blocks (optional single-line mode), nested subagent tool calls as a tree
- **Steer** and queued messages: send follow-ups mid-turn or queue them for the next turn; convert a queued message between steer and follow-up, pull it back into the composer to edit
- **Scheduled prompts**: right-click Send to run a prompt after another session's turn ends or at a set time, with loop iterations and exit condition; cancel from the Scheduled panel
- Live tok/s during streaming, turn timer, per-bucket context token breakdown popover
- **Prompt editing with fork**: edit a sent prompt and fork the session from that point, after any agent reply
- **Rewind**: roll back to any assistant answer — the session forks to a new branch and the working directory is restored from a snapshot taken before the next prompt (current state saved to git stash as a safety net)
- **Built-in `/loop`**: run the agent in iterations with an exit condition, `loop_stop` tool, loop flags in session names and icons
- Interactive question cards (ask_question) with options, free-text answers and multi-select
- Todo widget pinned above the chat, live context-usage indicator with color grading and cache stats
- Paste images and attach files (copied to `.pi/attachments` in the repo root so worktree sessions share them and survive worktree removal), with image previews and lightbox in the chat feed; click a pending attachment thumbnail to preview it before sending
- Resizable composer: auto-growing prompt field, drag handle on the top edge, double-click to reset
- Session history with subagent sessions nested under their parent, unread dots and busy badges per project; rename sessions via dialog, search across history
- Live tok/s during streaming, turn timer, per-bucket context token breakdown popover
- Copy button on code blocks, view-diff button for write tool blocks, full command shown when a tool block is expanded

![Chat with todo widget and tool calls](docs/screenshots/chat.png)

### Kanban

- Kanban boards in a right-rail panel as a task tree: board → columns → tasks with theme accents, counters and collapsible columns; card modal with properties rail and activity feed
- Session status dots on cards (busy, waiting for answer, unread turn) survive session close until the card is opened; live board updates without manual refresh
- Card comments with images and clickable session/commit chips; agent tools for cards, columns and workflow — the agent picks tasks, moves them and reports via comments
- Copyable task and session links (card and session tab context menus) that render as clickable chips in the chat, card description and comments — a task chip opens the card, a session chip opens the session; in input fields tokens render as badges with task/session names, Backspace deletes a badge whole
- A card can open as its own tab with the full card editor, persisted across restarts; cards linked to the current session show as chips in the chat header
- Board themes (built-in + custom via Appearance manager, JSON import/export)
- Durable board storage: cross-process file locking, atomic writes, corrupt-file quarantine

### Projects and backends

- Multiple projects in a sidebar, each with its own sessions, git repo and settings; drag to reorder projects
- Project and branch in the app header (IDE style): project switcher, branch popup, ahead/behind arrows with automatic fetch
- Two pi backends: native Windows and WSL (per-project choice, auto-detection)
- **SSH backend**: run pi on a remote Linux server over SSH (password, key + passphrase or ssh-agent) — remote projects with file browsing, git, terminal and kanban over SFTP/exec; add projects via a remote directory browser, manage servers in Settings → SSH
- Git worktree support: create, reuse and delete worktrees, sessions grouped under the project

### Git panel

- Status with color-coded files (modified / staged / untracked / deleted) grouped into a folder tree
- **Git Log dock**: PHPStorm-style branch graph with side branches shown by default, converging lanes, search by message or hash, branch filter
- Commit context menu: cherry-pick, checkout revision, reset soft/mixed/hard, revert, edit commit message, squash, drop commit, interactive rebase from here, new branch/tag
- Stage / unstage / commit, unified and split diffs; arrow keys step through the files of a commit diff
- Branch popup in IDE style: search, create, checkout, rename, delete, pin branches to the top

![Git Log dock with branch graph](docs/screenshots/git-log-dock.png)

### Files and editor

- File browser with Monaco editor, soft wrap toggle
- Markdown files: Obsidian-style live preview — click a block to edit the source, everything else renders

![Markdown live preview in the file tab](docs/screenshots/files-markdown.png)

### Terminal

- Docked terminal at the bottom (node-pty / ConPTY, native and WSL)
- Multiple tabs, renameable, restored after restart; cmd profile, copy selection to clipboard

![Terminal dock](docs/screenshots/terminal.png)

### Models, MCP and skills

- Manage pi providers and models (`models.json`) for both backends: add, edit, copy between backends
- Model dropdown re-reads the pi model catalog when opened and after saving models
- MCP servers: user-level and per-project, enable/disable, exposure toggles, JSON import, live connection check
- Skills: user-level and per-project directories with toggles

### Notifications and remote access

- Sound notifications for completed turns, questions and errors (system sounds or custom wav), with a play button to preview the selected sound
- Telegram bot notifications with per-event checkboxes and per-session toggle
- Remote control from a phone: built-in WebSocket bridge with PIN auth (static PIN option) serves the web UI — session list, chat with images, abort, dialog answers, session creation; web UI follows the app language, failed server start retries with backoff

![Agent questions on the remote web UI](docs/screenshots/remote-question.png)

![Chat over the remote web UI](docs/screenshots/remote-chat.png)

### Interface

- Project tabs: sessions, files, diffs, kanban boards and task cards, MCP and skills open as tabs in a single window; MRU tab restore on close and Ctrl+Tab switcher, type icons per tab
- **Search Everywhere** overlay on double Shift
- Token usage statistics (File → Statistics): in/out/cached-read charts per day, month, year or custom range with project, model and metric filters, totals and stacked mode
- Resizable/collapsible projects sidebar, new-session and new-worktree buttons in the tab bar
- Dark and light themes, adjustable chat font size
- Settings in the application File menu (Ctrl+,)
- English and Russian UI
- Configurable send key (Enter / Ctrl+Enter), Enter by default; model/thinking selector placement

![Kanban board as a project tab](docs/screenshots/kanban-board.png)

![Kanban card details](docs/screenshots/kanban-card.png)

## Requirements

- Windows 10/11
- Node.js ≥ 22.19 and Git for Windows
- [pi CLI](https://github.com/earendil-works/pi): native (`irm https://pi.dev/install.ps1 | iex`) and/or inside WSL — selectable per project in settings

## Installation

Download the latest installer from [Releases](https://github.com/php-programmist/PiWright/releases/latest). The app checks this feed for updates automatically (configurable in Settings → Launch → Update feed URL). Updates are never downloaded silently — a banner offers to download and install or skip the version; click the version in the projects panel footer to see What's new.
## Building from source
```sh
npm install
npm run build          # compile to out/
npm run dist           # build the NSIS installer (release/)
```
## Development
```sh
npm install
npm run dev            # electron-vite dev (window + HMR)
npm test               # vitest
npm run typecheck      # tsc (node + web configs)
npm run lint           # eslint
```
## Settings
App settings live in `%APPDATA%\PiWright\settings.json` and are editable from the in-app settings window: backends, WSL distro, pi path, update feed, appearance, notifications, remote access.
## Project structure
- `src/main` — Electron main process: pi RPC client, backends (native/WSL), settings, git, files, terminal, MCP, notifications, remote bridge
- `src/preload` — contextBridge, the only IPC boundary
- `src/shared` — IPC contracts and pi protocol types, no side effects
- `src/renderer` — React UI (zustand stores, views)
- `tests` — vitest
## Code signing policy

Free code signing provided by [SignPath.io](https://signpath.io), certificate by [SignPath Foundation](https://signpath.org).

This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

Team roles (solo-maintained project):
- Authors, reviewers and approvers: [@php-programmist](https://github.com/php-programmist)

## License
[MIT](LICENSE)
