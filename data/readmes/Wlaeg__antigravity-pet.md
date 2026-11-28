# Antigravity Pet — Native Pixel-Art Desktop Companion for Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Wlaeg/antigravity-pet?style=flat-square&color=0EA5E9)](https://github.com/Wlaeg/antigravity-pet/releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11%20%7C%20macOS%2012%2B-0078D6?style=flat-square)](https://github.com/Wlaeg/antigravity-pet/releases/latest)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-10B981?style=flat-square)](#install--download)

![Antigravity Pet Showcase](assets/hero-showcase.gif)

An open-source, native pixel-art desktop companion for **Google Antigravity** on **Windows** and **macOS**. It lives quietly on your desktop, mirrors what your AI agent is doing in real time without stealing window focus, and turns long coding sessions into a lively, tactile experience.

## Why Antigravity Pet?

### 1. Live Agent Awareness Without Stealing Focus
- **Single-line live tool bubbles:** See what your agent is doing at a glance (`Reading server.mjs`, `Editing App.tsx`, `Tests passed`) right above your pet without switching windows.
- **Calm background monitoring (`🌙`):** When your foreground chat is idle while background tasks run, your pet switches to a calm resting pose with a `🌙` badge — click the stacked task bubbles to expand and jump straight to any session.
- **Non-intrusive alerts & inline approvals:** Prompts you gently when tool approval or user input is needed (with quick inline Approve / Deny actions), celebrates clean completions, and flags blocked turns.

### 2. Rich Character Ecosystem & 1-PNG Creation
- **8 built-in mascots:** Switch anytime between `cyber-fox`, `astro-bot`, `shadow-cat`, `byte-ghost`, `shiba-dog`, `pixel-dragon`, `android-bugdroid`, and `flutter-dash`.
- **Built-in Community Workshop:** Browse, search, star, and 1-click install or remove community-created pets directly inside **Settings → Community**.
- **Bring any static PNG to life:** Drop a single static PNG into **Pack Studio** (or use the `hatch-pet` skill) and the procedural animation engine generates breathing, parabolic hops, and squash-and-stretch motion automatically — or supply a full `8×11` multi-frame sprite sheet.
- **Randomized starter gear & Surprise Mode:** Each user starts with 4 randomized non-conflicting wearables drawn from `head`, `face`, `hand`, and `back` slots (`20 / 50 / 100 / 150` tasks). Reaching **200 tasks** (or starring the repo on GitHub) unlocks **Surprise Mode**, where your local Agent generates 150 additional unique pixel accessories and equips a fresh 2-slot combo every 1–5 completed tasks.

![Surprise Mode Accessories](demo/v47-surprise.gif)

### 3. Playful Desktop Interactions
- **Typing rhythm sync & dizzy easter egg:** Bounces along with your typing cadence using a frequency-only sliding window (**zero keylogging**); type faster than 5 keys/s to trigger orbiting pixel stars.
- **Autonomous wandering & naps:** Patrols your taskbar or dock, emits `?` / `♪` curiosity cues when idle, and curls up for a `Zzz` nap — any keystroke wakes it up smoothly.
- **Edge peeking & fullscreen auto-hide:** Drag it to either monitor border to peek with half its body, scale cleanly from `0.33x` to `3.00x`, and hide automatically during fullscreen apps or games.

### 4. Native Performance, Clean Controls & 11 Locales
- **Lightweight native overlay:** Compiled directly with built-in OS toolchains (`csc.exe` / `.NET Framework 4.x` on Windows; `swiftc` on macOS) with no Electron bloat or taskbar/Dock clutter (paired with Node.js 18+ for MCP, Settings, and local accessory generation).
- **Standalone Settings window:** Right-click the pet for a dedicated `460×800` Settings panel (**Characters / Behavior / Bubbles / System / Updates**) with one-click in-app self-updates.
- **11-locale full-stack localization:** Automatically matches your Antigravity language (or switch anytime) across Settings, live bubbles, counters, prompts, and context menus: `English`, `简体中文`, `繁體中文 (TW)`, `Français`, `Deutsch`, `日本語`, `한국어`, `हिन्दी`, `ไทย`, `Español (ES)`, and `Español (MX)`.

## How It Works

```text
Antigravity agent ──hooks.json──▶ scripts/hook-bridge.mjs ──▶ HTTP 127.0.0.1:47821
                                                                      │
Native Overlay (app/AntigravityPet.cs | app/AntigravityPet.swift) ◀──┘
      └── Right-click Settings ──▶ Standalone Panel (sidecars/panel/server.mjs :47822)
```

- **Lifecycle hooks (`plugin.json` + `hooks.json`):** Triggers `node ./scripts/hook-bridge.mjs` across `SessionStart`, `PreInvocation`, `PreToolUse`, `PostToolUse`, `PostInvocation`, and `Stop`, mapping tool calls via `scripts/tool-label-mapper.mjs` to compact state updates on `127.0.0.1:47821`.
- **Native transparent overlay:** Lightweight OS-native window that stays always-on-top without appearing in `Alt+Tab` or your Dock/taskbar.

## Install & Download

**Runtime requirements:**
- **Desktop overlay:** Built-in `.NET Framework 4.x` on Windows 10/11 and `swiftc` (Xcode Command Line Tools) on macOS 12+.
- **Node.js 18+ (`node` in `PATH`):** **Required** for the Antigravity MCP server, Settings panel (both sidecar & standalone window), Community Workshop, GitHub Star unlock verification, and Surprise Mode accessory generation.

### For AI Agents (Quick Install)

If you are an AI coding agent installing Antigravity Pet into a user's workspace, pick the row matching the host OS, run the build/launch script once, and inform the user of the toggle shortcut:

| Platform | Plugin Path | Build & Launch Command | Toggle Shortcut |
| -------- | ----------- | ---------------------- | --------------- |
| **Windows 10/11** | `%USERPROFILE%\.gemini\config\plugins\antigravity-pet` | `.\build.ps1 -Launch` | `Win + Alt + P` |
| **macOS 12+** | `~/.gemini/config/plugins/antigravity-pet` | `chmod +x build.sh && ./build.sh --launch` | `⌥ + ⌘ + P` |

### Option 1: Download Prebuilt Release (Recommended)

#### Windows 10 / 11

1. Download the [latest release `.zip`](https://github.com/Wlaeg/antigravity-pet/releases/latest) and extract it to:
   ```text
   %USERPROFILE%\.gemini\config\plugins\antigravity-pet\
   ```
2. Run the one-click launcher in PowerShell:
   ```powershell
   cd "$env:USERPROFILE\.gemini\config\plugins\antigravity-pet"
   .\build.ps1 -Launch
   ```
3. Right-click the pet for **Settings**, or press **`Win + Alt + P`** anytime to show or hide it.

#### macOS 12+ (Apple Silicon & Intel)

1. Download the [latest release `.zip`](https://github.com/Wlaeg/antigravity-pet/releases/latest) (or `AntigravityPet-macOS-universal.zip`) and extract it to:
   ```text
   ~/.gemini/config/plugins/antigravity-pet/
   ```
2. Build and launch via built-in `swiftc`:
   ```bash
   cd ~/.gemini/config/plugins/antigravity-pet
   chmod +x build.sh && ./build.sh --launch
   ```
3. Press **`⌥ + ⌘ + P`** (`Option + Command + P`) to toggle visibility, or open **Desktop Pet Settings** from Antigravity's `...` menu.

### Option 2: Git Clone & Build from Source

```powershell
# Windows PowerShell
git clone https://github.com/Wlaeg/antigravity-pet.git "$env:USERPROFILE\.gemini\config\plugins\antigravity-pet"
cd "$env:USERPROFILE\.gemini\config\plugins\antigravity-pet"
.\build.ps1 -Launch
```

```bash
# macOS
git clone https://github.com/Wlaeg/antigravity-pet.git ~/.gemini/config/plugins/antigravity-pet
cd ~/.gemini/config/plugins/antigravity-pet
chmod +x build.sh && ./build.sh --launch
```

### Updating & Uninstalling

- **Update:** Open **Settings → Updates** for one-click in-app self-update, or run `git pull` followed by `.\build.ps1 -Launch` / `./build.sh --launch`.
- **Uninstall:** Close the pet from its right-click menu and remove the `antigravity-pet` folder under `.gemini/config/plugins/`.

## States & Behaviors

| State | Trigger | Visual Behavior |
| ----- | ------- | --------------- |
| `idle` | `SessionStart`, `Stop` (all tasks idle) | Gentle breathing & eye blink |
| `walk` | Autonomous patrol / cursor follow | Left/right walking frames across taskbar or dock |
| `running` | Active foreground tool / model turn | Working pose with single-line live tool bubble |
| `background_running` | Foreground idle while background tasks run | Calm lavender-blue rest pose with `🌙` badge & clickable task stack |
| `needs_input` | `PreToolUse` approval or `ask_question` | Attentive cue with quick inline Approve / Deny bubble |
| `ready` | Turn completed cleanly | Celebration hop / wave with subtle non-stealing alert |
| `blocked` | Tool failure or blocked turn | Dizzy error loop alerting you to check the session |
| `typing_sync` | Active keyboard input | Rhythmic bounce synced to typing speed (1.5s sliding window) |
| `dizzy` | Typing speed > 5 keys/s | 3 orbiting pixel stars above the pet's head |
| `bored / nap` | Extended inactivity | Wanders with `?` / `♪` cues, then curls into `Zzz` nap |
| `edge_peek` | Dragged to screen edge | Half-body peeking from left/right monitor border |

## Security & Privacy

- **Zero telemetry:** Antigravity Pet never collects analytics or phones home. Outbound HTTPS requests occur only when you explicitly browse the Community Workshop, star/download a pack, or check for updates on GitHub.
- **Zero keylogging:** Typing sync measures only a 1.5-second rolling keystroke frequency count — key codes, characters, and prompt contents are never recorded or stored.
- **Loopback-only local IPC:** The overlay (`127.0.0.1:47821`) and Settings panel (`127.0.0.1:47822`) bind strictly to localhost loopback.
- **No hidden startup entries:** By default, the pet launches and exits with Antigravity without modifying OS startup registries.
- See [SECURITY.md](SECURITY.md) for reporting security issues.

## Contributing & Community

Contributions, bug reports, new pixel mascots, and community packs are welcome:

- Read [CONTRIBUTING.md](CONTRIBUTING.md), [CUSTOM_PET_SPEC.md](CUSTOM_PET_SPEC.md), and [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) before opening a pull request.
- Open a [Bug Report](https://github.com/Wlaeg/antigravity-pet/issues/new?template=bug_report.yml), [Feature Request](https://github.com/Wlaeg/antigravity-pet/issues/new?template=feature_request.yml), or [Community Pet Submission](https://github.com/Wlaeg/antigravity-pet/issues/new?template=pet_submission.yml).
- Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Project Layout

```text
plugin.json, hooks.json         Antigravity plugin manifest & lifecycle hooks
app/                            Native Windows (C# WinForms) & macOS (Swift AppKit) overlay
sidecars/panel/                 Standalone Settings & Community Workshop UI (:47822)
scripts/                        Hook bridge, tool-label mapper, MCP server & pack validator
pets/                           8 built-in pixel-art pets
community/                      Approved community pet packs & full-body preview images
assets/                         Hero showcase GIF, logo & UI icons
skills/                         Built-in `pet` and `hatch-pet` Antigravity skills
docs/DEVELOPMENT.md             Architecture, state machine & local HTTP API reference
CUSTOM_PET_SPEC.md              Sprite sheet & community submission specification
build.ps1, build.sh             Zero-dependency Windows & macOS build/launch scripts
CHANGELOG.md                    Full release history and version notes
LICENSE                         MIT License
```

## Notes

- **Why is there no taskbar / Dock icon?** The overlay uses `WS_EX_TOOLWINDOW` (Windows) and `LSUIElement` (macOS) intentionally to stay out of your window switcher. Use `Win + Alt + P` (`⌥ + ⌘ + P` on macOS) or right-click the pet anytime.
- **Does it stay running in the background after closing Antigravity?** No — by default it follows Antigravity's lifecycle and exits automatically when Antigravity closes.
- Released under the [MIT License](LICENSE).
