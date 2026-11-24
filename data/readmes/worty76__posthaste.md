<p align="center">
  <img src="landing-page/public/logo-256.png" width="96" alt="Posthaste logo">
</p>

<h1 align="center">Posthaste</h1>

<p align="center">
  <strong>A fast, local-first note &amp; to-do app built in Rust.</strong><br>
  Keyboard-first for macOS, Windows and Linux, with custom looks, optional
  peer-to-peer device sync, and optional AI polish with your own key.
</p>

<p align="center">
  Capture a thought in two seconds. Get back to work.
</p>

<p align="center">
  <a href="https://posthaste.ink">Download for macOS, Windows and Linux</a>
  ·
  <a href="https://github.com/worty76/Posthaste/releases/latest">Releases</a>
</p>

---

Press the global shortcut from anywhere, type, hit Enter. The window disappears,
focus returns to what you were doing, and the note is waiting in your inbox.

Your notes live in one SQLite file on your machine. No account, no central
server holding your data, no telemetry — nothing leaves your computer unless
you turn on AI polish or experimental device sync yourself.

<p align="center">
  <video src="https://github.com/worty76/Posthaste/raw/main/landing-page/public/demo/posthaste-demo.mp4?v=3" poster="https://github.com/worty76/Posthaste/raw/main/landing-page/public/demo/posthaste-demo-poster.jpg?v=3" width="720" controls muted playsinline></video>
</p>

## Why Posthaste

- **Instant capture** — the windows are created at startup and hidden, so the
  shortcut shows them in milliseconds
- **Local-first** — one database file (attachments included), backup-able from
  Settings. Export your notes as a Markdown checklist that opens in any editor
  (or as JSON), and import it back without losing anything
- **Looks** — built-in looks that always dress the app, or make your own
  with a live editor that refuses anything hard to read; share any look
  with a one-line code. Three fonts ship inside the app under the SIL Open
  Font License (`ui/styles/fonts/`), so the same faces render on every OS
- **AI polish** — optional. Off by default; when you turn it on, your note goes
  straight to the provider you picked: Claude, OpenAI, Gemini,
  OpenRouter, any OpenAI-compatible server, or Ollama on your own computer.
  Keys live in your system keychain, never in the settings
- **Device sync (experimental)** — optional and off by default. Pair two of
  your own computers with a one-time code to sync notes directly over
  encrypted QUIC (iroh). When computers cannot connect directly, encrypted
  traffic passes through the configured relay, which sees only device public
  keys and IP addresses, never note text
- **In-app updates** — signed installers, one click, nothing auto-runs
- **Later** — press L on a to-do you won't get to today. It leaves Today and
  the inbox and waits in Later, your backlog, until you bring it back. No dates,
  no reminders
- **Steps** — break a note into plain one-line steps in Note details: ↑ ↓ move,
  Space ticks, Enter edits, Mod+↑ Mod+↓ reorder, Backspace removes (with Undo).
  Ticking every step never completes the note, and steps never count in Today.
  Steps sync to your other computers once they run this version or later
- **Projects** — group related notes in collapsible project sections across
  Today and the inbox, set or create a project on any note with `P` (or in
  capture with `# project`, or from Note details), and open a project's page
  from the sidebar or with `#` to see its notes across days. Projects can be
  renamed (or merged) and archived from Manage projects; a note's project syncs
  with paired computers, while archive status stays on each computer for now
- **Trash** — deleting a note moves it to Trash, where it waits 30 days. Restore
  it exactly as it was, or erase it for good
- **Earlier days** — ← and → in Today step back through earlier days, as they
  stood then; carried notes say which day they came from, and the inbox's
  calendar marks the days that still have open notes
- **Note details** — press Enter on a to-do in Today (or O in the inbox) for a
  description and attached files, images and docs; it saves as you type
- **Keyboard-driven** — every action has a shortcut; see them all with `?`

## Shortcuts

| | macOS | Windows / Linux |
|---|---|---|
| Capture a note | ⌘⇧Space | Ctrl+Shift+Space |
| Open the inbox | ⌘⌃N | Ctrl+Alt+N |
| See today's notes | ⌘⌃G | Ctrl+Alt+G |

In the capture window: Enter saves, Shift+Enter adds a line, Ctrl/⌘+Enter saves
and starts another, Ctrl/⌘+1–9 toggles active projects, Ctrl/⌘+P opens the
project picker, Ctrl/⌘+I polishes with AI (when enabled), Esc keeps a draft.
In the inbox: ↑/↓ move, E edit, X complete, A archive, R reopen to the inbox,
C copy, / search, L later (or back to the inbox), P set project, # open a
project's page, Delete moves to Trash, 1–5 switch sections
(Inbox, Today, Later, Archive, Trash), N new note, O note details, Ctrl/⌘+B
collapses or expands the sidebar, Ctrl/⌘+, opens Settings. In Trash:
R or Enter restores, Delete erases for good (it asks first). In the Today window: ↑/↓ move, X marks a
note done or not done, L moves it to Later, ←/→ show the previous or next day,
T comes back to today, C opens the calendar, Enter opens note details, Esc closes.
In note details: Esc saves and closes, Ctrl/⌘+Enter marks done, Ctrl/⌘+O adds
files, paste adds an image, Delete on a file removes it. All three global shortcuts are changeable in
Settings, along with how big the floating windows open (Compact, Standard or
Roomy) and the text size across every window (Small, Standard or Large).
Command line: `posthaste --capture`, `--today`, `--inbox`,
`--settings`, `--minimized`.

## Build from source

Prerequisites: Rust (stable), Node 20+ (only to run Vite and the Tauri CLI), and the
[Tauri 2 system dependencies](https://v2.tauri.app/start/prerequisites/) for
your OS. On Debian/Ubuntu:

```sh
sudo apt install libwebkit2gtk-4.1-dev libgtk-3-dev libayatana-appindicator3-dev \
  librsvg2-dev libxdo-dev libssl-dev libdbus-1-dev build-essential
```

The interface is written in Rust and compiled to WebAssembly, which needs
two more tools, once:

```sh
rustup target add wasm32-unknown-unknown
cargo install wasm-bindgen-cli --version 0.2.130 --locked
```

```sh
npm install
npm run tauri dev        # develop
npm run tauri build      # release build + installers for your OS
npm run check            # formatting and rule checks
(cd src-tauri && cargo test --workspace)   # tests
npm run build:ui -- --dev  # rebuild the Rust interface while developing
```

Contributing rules live in the `AGENTS.md` files at the root and in each
source folder. Wayland users: global shortcuts need a desktop binding —
bind `posthaste --capture` and `posthaste --today` to keys in your keyboard
settings.

## Not in it, on purpose

Accounts, central cloud storage, reminders, folders, statistics. Posthaste does one job and
stays out of the way.

Architecture, platform notes, sync design, and release checklist:
[docs/architecture.md](docs/architecture.md),
[docs/platform-notes.md](docs/platform-notes.md),
[docs/sync.md](docs/sync.md), and
[docs/release-guide.md](docs/release-guide.md).

## Code signing policy

Free Windows code signing provided by [SignPath.io](https://signpath.io), certificate by [SignPath Foundation](https://signpath.org).

- **Builds and signing:** All official release installers are built from this repository's `main` branch via GitHub Actions (`.github/workflows/release.yml`). Releases are reviewed and approved by the repository maintainer (`@worty76`).
- **Privacy:** Posthaste is local-first and collects no telemetry, analytics, or user data. All notes stay in a local SQLite database on your own machine.

## Licence

MIT
