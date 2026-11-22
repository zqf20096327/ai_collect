<p align="center">
  <img src="assets/logo.svg" alt="JARVIS Logo" width="200"/>
</p>

<h1 align="center">J.A.R.V.I.S.</h1>
<p align="center">
  <b>Personal AI Desktop Assistant for Windows</b><br/>
  231 tools. 8 LLM providers. Voice control. Fully configurable. One HUD.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12-blue" alt="Python 3.12"/>
  <img src="https://img.shields.io/badge/react-19-61DAFB" alt="React 19"/>
  <img src="https://img.shields.io/badge/kotlin-jetpack_compose-7F52FF" alt="Kotlin"/>
  <img src="https://img.shields.io/badge/tools-231-green" alt="231 Tools"/>
  <img src="https://img.shields.io/badge/license-MIT-yellow" alt="MIT License"/>
</p>

---

JARVIS is a full-stack personal AI assistant that runs entirely on your Windows machine. It routes requests to local or cloud LLMs, acts on your computer through 231 audited tools across 64 modules, and presents everything through a cinematic heads-up display you can control by voice or keyboard. Simple commands execute instantly through fast-path pattern matching without touching the LLM. New installs start with a guided onboarding wizard, and the assistant name, wake word, and branding are fully configurable.

Say it, see it happen, stay in control.

## Screenshots

| Console | Audit | Repair | Settings |
|---------|-------|--------|----------|
| ![Console](screenshots/jarvis-hud-console.png) | ![Audit](screenshots/jarvis-hud-audit.png) | ![Repair](screenshots/jarvis-hud-repair.png) | ![Settings](screenshots/jarvis-hud-settings.png) |

## Key Features

### First-Run Onboarding

New installs launch a 6-step guided wizard: welcome screen with animated core visual, name your assistant (any name you like), choose a privacy mode, connect an LLM provider (paste a cloud API key or start a local server), pick a theme, and launch. The entire setup takes about 30 seconds and stores everything locally.

### Configurable Assistant Name

Rename the assistant to anything you want from Settings or during onboarding. The name propagates everywhere: title bar, taskbar, wake word, console messages, voice prompts, and the LLM system prompt. The wake word system auto-registers the custom name as a voice alias alongside the built-in "Hey Jarvis" detector.

### AI and Language Models
- **8 LLM providers** out of the box: LM Studio, Ollama, NVIDIA NIM, Anthropic, OpenAI, Google Gemini, OpenRouter, and Groq
- **Runtime model discovery** from each provider's model list, nothing hardcoded
- **Automatic routing** with ordered preference lists and health-based fallback
- **Privacy modes**: Local Only (all cloud blocked), Hybrid, or Cloud
- **Model Ladder**: auto-escalation across 4 tiers (fast local, fast cloud, smart, premium) based on task complexity
- **Streaming responses** with token-by-token output and model attribution

### Computer Control (231 Tools across 64 modules)

**Desktop and Windows**
- Search and launch installed applications
- List, focus, minimize, maximize, and close windows
- UI Automation: snapshot any window's controls, click, type, press hotkeys
- Lock, sleep, restart, shut down (with 30s cancellation window)

**Files and Documents**
- List, search, read, write, move, copy, and delete files
- Create directories with nested paths
- Extract text from PDF, DOCX, XLSX, CSV, PPTX, JSON, ZIP
- Convert between formats (text to PDF, DOCX to TXT, XLSX to CSV)
- Open files with their default application

**Web and Browser**
- Built-in browser powered by Playwright (Edge/Chrome)
- Open pages, snapshot content, read text, click elements, fill forms
- Tab management, navigation (back/forward/reload)
- Chrome DevTools integration: list tabs, navigate, screenshot, run JS, click, type
- Open URLs in the default browser

**Communication**
- Email: list, read, and send via IMAP/SMTP (Gmail, Outlook, Yahoo, iCloud presets)
- Phone calls via Windows Phone Link
- Voice calls via Twilio with TTS: Jarvis speaks a message and gathers DTMF approval (press 1/2)
- Telegram bot integration for remote messaging
- Buffer integration for social media posting, scheduling, and analytics

**Voice and Speech**
- Global hotkey (Ctrl+Alt+J) summons and focuses the command bar
- Wispr Flow dictation integration with auto-send after quiet period
- Text-to-speech for spoken replies (toggle on/off)
- Wake word detection ("Jarvis")
- Built-in STT fallback via faster-whisper
- Voice training and voiceprint recognition

**Media and Entertainment**
- System volume control (set, adjust, mute)
- Media playback control (play/pause, next, previous, stop)
- YouTube search, play, and transcript extraction
- Music search, play, and lyrics (YouTube Music + lyrics.ovh)
- Screen capture with vision model analysis
- Local image generation via Stable Diffusion WebUI (AUTOMATIC1111 / ComfyUI)

**Developer Tools**
- Git status, log, and diff inspection
- Code review copilot: git diff, blame, stats for change analysis
- Incident commander: system state capture, process detail, network audit, service status
- Error explanation with fix suggestions
- Project scaffolding (Python, Node, React, FastAPI, Flask, Next.js, HTML)
- Project analysis (language detection, dependencies, entry points)
- Shell command execution (PowerShell, with timeout and output cap)

**Smart Home**
- Home Assistant integration: list devices, control lights/switches/climate
- Get device states and trigger automations

**Weather and Travel**
- Current weather and 3-day forecast with auto-detected location
- Flight tracking and status lookup

**Timers and Stopwatch**
- Set countdown timers with sound notification
- Stopwatch with start, stop, lap, and reset
- List and cancel active timers

**Quick Notes**
- Create, search, and manage ephemeral notes with tags
- Daily notes with structured sections (tasks, notes, events)
- Append to daily notes under specific sections

**Clipboard History and Manager**
- Automatic capture of clipboard text with secret detection (skips passwords, API keys)
- Full-text search across clipboard history via FTS5
- Source app tracking for each entry
- Clipboard manager: history browsing, pin snippets for quick recall, paste from history

**Conversation Search**
- Full-text search across all past conversations
- Filter by role (user or assistant messages)
- List and browse conversation history

**Response Customization**
- Response style presets: brief, detailed, witty, formal, casual
- Custom response instructions
- Standing instructions (persona) that persist across conversations
- Fast-path intents: common commands (mute, weather, open app, screenshot) run instantly without LLM

**Memory and Knowledge**
- Long-term memory: remember facts and preferences, recall by semantic search
- Memory review and management
- Content digests and summarization

**AI Agents and Planning**
- Create background sub-agents for parallel work
- Multi-step plan creation with user review and approval
- Agent handoff and status tracking
- Deep research pipeline with 5-stage verification
- Background task engine with SQLite checkpointing and crash recovery

**Scheduling and Routines**
- Create, list, and manage scheduled tasks
- Built-in routines: morning briefing, end-of-day recap, health checks
- Condition monitors with custom prompts
- Proactive notifications (opt-in)

**Action Transparency and Dry-Run Mode**
- Action history: query the full execution log by tool name, status, or time to see what happened ("did that email send?")
- Action detail: inspect any audit entry with full arguments and error messages
- Action summary: quick status check showing success/failure/denial counts across recent operations
- Dry-run preview: see exactly what a tool would do (tier, approval needed, side effects, argument validation) without executing it
- Tool inspector: browse all available tools with their tiers, parameters, and approval requirements

**Security, Privacy, and Credentials**
- Security audit log with full action history
- Taint tracking for untrusted content
- Sensitive data redaction in logs
- Credential management via Windows Credential Manager
- Privacy guardian: network connection audit, listening ports scan, startup programs audit, DNS lookup logger
- Credential health check: password strength analysis, HIBP Pwned Passwords k-anonymity check, secure password generator

**Geospatial Intelligence (God's Eye View)**
- 3D globe with live data: flights, ships, satellites, earthquakes, fires, weather, CCTV, traffic
- Military awareness and situation briefs
- One-command setup: clone, install, and launch via `gods_eye_setup` and `gods_eye_start`
- ~30 tools auto-registered through the MCP protocol
- Powered by [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) (MIT, CesiumJS)

**Mobile Device Control (Mobile MCP)**
- Drive iOS and Android devices: simulators, emulators, and real devices
- Screenshot, tap, swipe, type, launch/install apps, read device logs
- Screen recording, clipboard access, GPS spoofing, orientation control
- 35 tools auto-registered via MCP, works with Android SDK and Xcode

**Productivity and Focus**
- Ambient context radar: enumerate and monitor active windows, track app focus history
- Sentinel watchers: condition monitors for CPU, memory, disk, processes, files, and URLs
- Focus forge: deep work sessions with distraction tracking and session history
- Fitness companion: health reminders (hydration, posture, eye breaks), activity logging, daily summaries
- Universal scratchpad: quick notes with tags, full-text search, JSON-backed persistence
- Workflow recorder: record tool sequences as named macros, list and replay workflows

**Screenshot Organization (Clip Curator)**
- Full-screen and active-window capture with metadata
- Tag, search, and browse saved screenshots
- JSON-indexed collection at DATA_DIR/clips

**Extensibility**
- MCP (Model Context Protocol) server support
- Browse and install MCP servers from a catalogue (22 pre-configured servers)
- Configuration presets for quick setup
- Custom skills and macros

### Fast-Path Intent Matching

Simple voice commands like "mute", "open Chrome", "weather", "timer for 5 minutes", and "volume 50" skip the LLM entirely and execute instantly through pattern matching. If the fast-path fails, it falls back to the full LLM pipeline transparently.

### Heads-Up Display

The HUD is built with React 19, TypeScript, and Zustand, rendered in a pywebview/WebView2 frameless window.

- **System Vitals**: real-time CPU, RAM, GPU, VRAM, disk, network, and battery with 60-sample history graphs
- **Core Visual**: animated particle radar that reflects agent state (idle, listening, thinking, acting, awaiting approval, error)
- **Process Radar**: live scanning of running processes
- **Event Stream**: real-time feed of system events and tool actions
- **Transcript**: full conversation with streaming output and model tags
- **Activity Panel**: every tool call with tier badge, arguments, duration, and outcome
- **Approval Cards**: exact action details with Allow/Deny controls, keyboard operable
- **3 Themes**: Ion (cyan), Holographic OS, Sovereign Executive
- **Onboarding Wizard**: guided first-run setup for new installs
- **Navigation**: Console, Audit, Repair, and Settings views

### Android Companion App

A Kotlin + Jetpack Compose mobile app that connects to your JARVIS instance over WebSocket.

- Auto-reconnect with exponential backoff
- Send commands and receive responses
- Real-time status updates
- Material 3 design

### Safety Model

Every tool has a risk tier:

| Tier | Level | Behavior |
|------|-------|----------|
| T0 | Observe | Runs automatically, logged silently |
| T1 | Reversible | Runs automatically, logged visibly |
| T2 | Modify | Requires your approval before execution |
| T3 | Destructive | Requires explicit click every time |

Once a run reads untrusted content (a file, the clipboard, command output), every further action in that run needs approval regardless of tier. JARVIS never elevates privileges, never reads credential stores, and listens on loopback only.

**Kill switch**: Ctrl+Alt+Backspace cancels every run and denies all pending approvals instantly.

### Outcome Verification

After tool execution, built-in verifiers confirm the action succeeded:
- File write: checks the file exists and has the expected size
- File delete: confirms the file is gone
- Directory create: verifies the directory exists
- Shell run: checks exit code
- App launch: confirms the process is running
- Browser open: verifies the page loaded

### Undo Stack

Destructive actions get auto-inferred reverse operations. The undo stack holds the last 50 reversible actions so you can roll back file writes, moves, copies, and clipboard changes.

## Architecture

```
JARVIS
|
|-- Python 3.12 Backend (FastAPI + uvicorn)
|   |-- WebSocket Gateway (loopback only, port 47821)
|   |-- Orchestrator (agent loop, tool dispatch)
|   |-- Provider Router (8 providers, health tracking, fallback)
|   |-- Policy Engine (tier enforcement, taint tracking)
|   |-- Fast-Path Intent Matcher (instant commands)
|   |-- Tool Registry (231 tools across 64 modules, pydantic validation)
|   |-- Background Task Engine (SQLite, checkpointing)
|   |-- Deep Research Pipeline (5-stage with verification)
|   |-- Routine Engine (scheduled proactive tasks)
|   |-- Model Ladder (complexity-based auto-escalation)
|   |-- Outcome Verifier (post-action confirmation)
|   |-- Memory Store (SQLite with WAL mode)
|   |-- Scheduler (cron-like task scheduling)
|   +-- Self-Heal (automatic service recovery)
|
|-- React 19 HUD (TypeScript + Zustand)
|   |-- pywebview / WebView2 frameless window
|   |-- Real-time WebSocket connection
|   |-- 3 cinematic themes
|   +-- Responsive layout
|
+-- Android App (Kotlin + Jetpack Compose)
    |-- WebSocket client with auto-reconnect
    +-- Material 3 UI
```

## Quick Start

### Prerequisites
- Windows 10/11
- Python 3.12+ (via [uv](https://docs.astral.sh/uv/))
- Node.js 18+ (for HUD development)
- At least one LLM provider (LM Studio for local, or a cloud API key)

### Installation

```powershell
# Clone the repository
git clone https://github.com/ankitjha67/JARVIS.git
cd JARVIS

# Set up Python environment (all caches stay on E: drive)
uv sync

# Build the HUD
npm --prefix ui install
npm --prefix ui run build

# Run JARVIS
uv run jarvis
```

On first launch, the onboarding wizard walks you through naming your assistant, choosing a privacy mode, connecting an LLM provider, and picking a theme. You can change all of these later in Settings.

### Hotkeys

| Hotkey | Action |
|--------|--------|
| Ctrl+Alt+J | Summon JARVIS and focus the command bar |
| Ctrl+Alt+Backspace | Kill switch: cancel all runs, deny pending approvals |

### Run Center and document review

Open **Runs** (Ctrl+5) to compare extracts. Enter the CSV or XLSX paths and one or more business-key columns.
Select **Build Excel report** to download every break after the run finishes. Optionally enter a shared numeric
column such as RWA to include the variance waterfall. Saved workflows can be revised and scheduled from Runs.
Excel input and output use openpyxl (`uv pip install openpyxl` if missing).

In the Console, ask Jarvis to compare two local numbered document revisions or trace requirements to UAT
evidence. The regulation comparison accepts Markdown, text, DOCX and text-based PDF, with an optional
`clause,control,owner,policy` CSV. The UAT workflow accepts CSV or XLSX registers with
`requirement_id,requirement` and `test_id,requirement_id,result,evidence` columns. Results are
`pass`, `fail`, `blocked`, or `not run`. Provide a prior requirements register to identify tests for revised requirements.
Ask Jarvis to create or list a case file to track deadlines, evidence references, correspondence drafts, and next actions.

## Development

```powershell
# Run tests
uv run pytest

# Lint
uv run ruff check src tests

# Build HUD (type-check + bundle)
npm --prefix ui run build

# Run HUD in dev mode
npm --prefix ui run dev

# Run HUD tests
npm --prefix ui test
```

## Android Build

```powershell
cd android
./gradlew assembleDebug
# APK at android/app/build/outputs/apk/debug/app-debug.apk
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, FastAPI, uvicorn, SQLite (WAL mode) |
| Frontend | React 19, TypeScript, Zustand, Vite |
| Desktop Shell | pywebview with WebView2 |
| Android | Kotlin, Jetpack Compose, OkHttp WebSocket |
| Browser Automation | Playwright (Edge/Chrome) |
| Speech | Wispr Flow, faster-whisper, pyttsx3 |
| Package Manager | uv (Python), npm (Node) |
| Secrets | Windows Credential Manager via keyring |

## Project Structure

```
JARVIS/
|-- src/jarvis/           # Python backend
|   |-- gateway.py        # Hub class, WebSocket server, lifecycle
|   |-- orchestrator.py   # Agent loop, tool dispatch
|   |-- providers/        # LLM provider implementations
|   |-- tools/            # 231 tools across 64 modules
|   |-- policy.py         # Tier enforcement, taint tracking
|   |-- memory.py         # Long-term memory store
|   |-- scheduler.py      # Task scheduling engine
|   |-- background_tasks.py   # Background task engine
|   |-- deep_research.py  # Research pipeline
|   |-- routines.py       # Proactive routine engine
|   |-- model_ladder.py   # Auto-escalation
|   |-- outcome_verify.py # Post-action verification
|   |-- confirmation.py   # Undo stack and confirmation gate
|   +-- ...
|-- ui/                   # React HUD
|   |-- src/
|   |   |-- App.tsx       # Main application
|   |   |-- Onboarding.tsx # First-run onboarding wizard
|   |   |-- Hud.tsx       # HUD layout and core visual
|   |   |-- Console.tsx   # Console view
|   |   |-- store.ts      # Zustand state management
|   |   +-- ...
|   +-- vite.config.ts
|-- android/              # Companion app
|   +-- app/src/main/java/com/jarvis/app/
|-- tests/                # Test suite
+-- screenshots/          # HUD screenshots
```

## Contributing

This is a personal project, but contributions are welcome. Please open an issue first to discuss what you would like to change.

## License

MIT
