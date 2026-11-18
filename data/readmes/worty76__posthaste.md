<p align="center">
  <img src="landing-page/public/logo-256.png" width="96" alt="Posthaste logo">
</p>

<h1 align="center">Posthaste</h1>

<p align="center">
  <strong>A badass note app with a modern, polished UI.</strong><br>
  Fast, free, customizable, keyboard-first for macOS, Windows and Linux, with six
  built-in looks (or make your own) and optional AI polish with your own key.
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

Your notes live in one SQLite file on your machine. No account, no sync, no
telemetry — nothing leaves your computer unless you turn on AI polish yourself.

<p align="center">
  <video src="https://github.com/worty76/Posthaste/raw/main/landing-page/public/demo/posthaste-demo.mp4?v=3" poster="https://github.com/worty76/Posthaste/raw/main/landing-page/public/demo/posthaste-demo-poster.jpg?v=3" width="720" controls muted playsinline></video>
</p>

## Why Posthaste

- **Instant capture** — the windows are created at startup and hidden, so the
  shortcut shows them in milliseconds
- **Local-first** — one database file (attachments included), backup-able from
  Settings. Export your notes as a Markdown checklist that opens in any editor
  (or as JSON), and import it back without losing anything
- **Looks** — six built-in colour themes, or make your own with a live editor
  that refuses anything hard to read; share any look with a one-line code
- **AI polish** — optional. Off by default; when you turn it on, your note goes
  straight to the provider you picked: Claude, OpenAI, Gemini,
  OpenRouter, any OpenAI-compatible server, or Ollama on your own computer.
  Keys live in your system keychain, never in the settings
- **In-app updates** — signed installers, one click, nothing auto-runs
- **Later** — press L on a to-do you won't get to today. It leaves Today and
  the inbox and waits in Later, your backlog, until you bring it back. No dates,
  no reminders
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

In the capture window: Enter saves, Shift+Enter adds a line, Esc keeps a draft.
In the inbox: ↑/↓ move, E edit, X complete, A archive, C copy, / search,
L later (or back to the inbox), Delete moves to Trash, 1–5 switch sections
(Inbox, Today, Later, Archive, Trash), N new note, O note details. In Trash:
R or Enter restores, Delete erases for good (it asks first). In the Today window: ↑/↓ move, X marks a
note done or not done, L moves it to Later, ←/→ show the previous or next day,
T comes back to today, C opens the calendar, Enter opens note details, Esc closes.
In note details: Esc saves and closes, Ctrl/⌘+Enter marks done, Ctrl/⌘+O adds
files, paste adds an image, Delete on a file removes it. All three shortcuts are changeable in
Settings, and so is how big the floating windows open (Compact, Standard or
Roomy). Command line: `posthaste --capture`, `--today`, `--inbox`,
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

Accounts, sync, reminders, folders, statistics. Posthaste does one job and
stays out of the way.

Platform notes and architecture details: [docs/platform-notes.md](docs/platform-notes.md).

## Licence

MIT
