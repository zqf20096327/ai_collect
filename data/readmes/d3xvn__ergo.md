<p align="center">
  <img src="assets/icon.png" alt="Ergo logo" width="128" />
</p>

<h1 align="center">Ergo</h1>

<p align="center"><strong>A Cursor for Mathematics</strong> — an AI-powered IDE for Lean 4 theorem proving.</p>

<p align="center">
Ergo deeply integrates an LLM agent (Claude) with the Lean 4 language server to give mathematicians a productive, modern environment for writing formal proofs. Think of it as Cursor, but purpose-built for formal mathematics.
</p>

<p align="center">
  <img src="assets/screenshot.png" alt="Ergo screenshot" width="800" />
</p>

---

## Features

### Editor
- **Lean 4 syntax highlighting** with support for keywords, tactics, types, comments, strings, and Unicode math symbols
- **Unicode input** — type `\forall` and it becomes `∀`, `\lambda` → `λ`, etc.
- **Inline diagnostics** — errors and warnings appear as gutter indicators and a compact bar below the editor
- **Auto-save** — files save automatically as you type
- **Undo / Redo** — floating buttons in the editor plus `⌘Z` / `⇧⌘Z`

### Lean Integration
- **Live proof goals** — see the tactic state and expected types in the Infoview as you move your cursor
- **Diagnostics** — errors and warnings from the Lean server, displayed in the Infoview and inline in the editor
- **Hover info** — type information shown in the Infoview panel
- **File progress** — "Lean is checking..." indicator while the server is elaborating
- **One-click toolchain install** — install `elan` and the Lean toolchain directly from the app

### AI Agent
- **Claude-powered assistant** with full tool use — reads files, edits code, creates files, lists directories, gets diagnostics, and reads proof state
- **Auto-applied edits** — the agent writes directly to your files, with an **Undo** button to revert any change
- **Proof-state aware** — the agent sees your current goals, hypotheses, and diagnostics
- **Lemma search** — integrated Loogle (type search) and Moogle (natural language search)

### Build System
- **Build Project** (`⇧⌘B`) — runs `lake build` with streaming output
- **Get Mathlib Cache** — runs `lake exe cache get` to download pre-built oleans (essential for Mathlib projects)
- **Update Dependencies** — runs `lake update`
- **Clean Build** — runs `lake clean`
- **Build output panel** — terminal-like output panel with auto-scroll, error highlighting, and cancel support

### IDE
- **File explorer** with collapsible tree view
- **Tabbed editor** with modified indicators
- **Resizable panels** — drag to resize the sidebar, editor, infoview, and chat
- **Build panel** — appears below the editor with streaming build output and action buttons
- **Project creation** — scaffold new Lean projects with `lake init`
- **Dark theme** — Catppuccin Mocha color scheme throughout

---

## Getting Started

### Prerequisites

- **Flutter** ≥ 3.9 — [install Flutter](https://docs.flutter.dev/get-started/install)
- **Lean 4** — can be installed directly from within Ergo, or manually via [elan](https://github.com/leanprover/elan)

### Run

```bash
# Clone the repo
git clone https://github.com/your-username/ergo.git
cd ergo

# Install dependencies
flutter pub get

# Run on macOS (primary target)
flutter run -d macos

# Or build a release
flutter build macos
```

### First Launch

1. **Open or create a Lean project** from the welcome screen
2. If Lean isn't installed, click **Install Lean Toolchain** — Ergo handles the rest
3. Set your **Claude API key** via `⌘,` or the Edit menu
4. Start writing proofs — the Infoview shows goals and the AI agent is ready in the chat panel

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `⌘O` | Open project |
| `⌘S` | Save file |
| `⇧⌘S` | Save all files |
| `⌘W` | Close tab |
| `⌘B` | Toggle file explorer |
| `⌘\` | Toggle right panel |
| `⇧⌘B` | Build project |
| `⌘,` | Claude API key settings |
| `⌘Z` | Undo |
| `⇧⌘Z` | Redo |
| `\` + abbrev | Unicode input (e.g. `\alpha` → `α`) |

---

## Architecture

```
lib/
├── main.dart              # Entry point
├── app.dart               # MaterialApp + providers
├── models/                # Data models (EditorTab, FileNode, ChatMessage)
├── screens/               # Top-level screen (IdeScreen)
├── services/              # Backend services
│   ├── lean_lsp_service.dart    # JSON-RPC client for Lean 4 LSP
│   ├── claude_service.dart      # Anthropic Claude API with tool use
│   ├── file_service.dart        # File system operations
│   ├── lake_service.dart        # Lake build system commands
│   └── lean_installer.dart      # elan/Lean toolchain installer
├── state/                 # State management (ChangeNotifier + Provider)
│   ├── editor_state.dart
│   ├── lean_state.dart
│   ├── chat_state.dart
│   ├── build_state.dart
│   └── file_explorer_state.dart
├── theme/                 # Catppuccin Mocha dark theme
├── utils/                 # Syntax highlighting, Unicode input
└── widgets/               # All UI components
    ├── code_editor.dart
    ├── infoview_panel.dart
    ├── chat_panel.dart
    ├── file_explorer.dart
    ├── search_panel.dart
    ├── build_panel.dart
    └── ...
```

---

## Tech Stack

- **Flutter** — cross-platform UI (macOS primary, Linux/Windows support)
- **Lean 4 LSP** — language server protocol for goals, diagnostics, hover, and completions
- **Anthropic Claude API** — LLM agent with tool use for code editing and proof assistance
- **Provider** — state management
- **Catppuccin Mocha** — dark color theme

---

## License

MIT
