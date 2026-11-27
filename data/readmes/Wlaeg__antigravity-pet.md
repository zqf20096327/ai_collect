# Antigravity Pet — a free, open-source pixel desktop pet for Google Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v4.6.0-0EA5E9?style=flat-square)](https://github.com/Wlaeg/antigravity-pet/releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11%20%7C%20macOS%2012%2B-0078D6?style=flat-square)](https://github.com/Wlaeg/antigravity-pet/releases/latest)
[![Runtime](https://img.shields.io/badge/Runtime-Zero%20External%20Dependencies-10B981?style=flat-square)](#install--download)

![Antigravity Pet Showcase](assets/hero-showcase.gif)

Antigravity Pet is a free, open-source pixel desktop pet for **Google Antigravity**. It lives on your **Windows** or **macOS** desktop and shows what your AI agent is doing in real time — which file it is reading, which test it is running, whether it needs your input or is stuck — so you can tell at a glance without switching windows. It is a native app with zero external runtime dependencies, so there is nothing extra to install and nothing running in the background beyond the pet itself.

**New in v4.6.0:** a Community Workshop where anyone can submit a pet pack through a GitHub issue — approved packs publish themselves with no server involved — plus community-wide stars and download counts synced from GitHub every 30 minutes.

- **Live tool status & calm `BackgroundRunning` (`🌙`):** Shows single-line live action bubbles (`Reading server.mjs`, `Editing App.tsx`, `Tests passed`) directly above your pet. When the foreground chat is idle while background tasks run, the pet switches to a calm lavender-blue resting pose with a `🌙` badge — click stacked task bubbles to expand the list and jump straight to any session.
- **8 built-in mascots + Community Workshop:** Switch between 8 built-in pixel companions (`cyber-fox`, `astro-bot`, `shadow-cat`, `byte-ghost`, `shiba-dog`, `pixel-dragon`, `android-bugdroid`, `flutter-dash`) or install community packs (`gemini-chan`, `cyber-panda`, `pixel-octopus`, `coffee-slime`, `star-hamster`) in one click inside the Settings panel.
- **1 static PNG comes alive:** Drop a single static PNG into the built-in **Pack Studio** (or use the `hatch-pet` skill), and the procedural animation engine brings it to life with breathing, parabolic hops, and squash-and-stretch bounces — or supply a full `1536×2288` (`8×11`) v3 multi-frame sprite sheet.
- **Playful typing sync & tiered boredom:** Bounces with your typing cadence (frequency-only sliding window — **zero keylogging**); type faster than 5 keys/s and watch dizzy stars orbit its head. Leave it idle and it wanders with `?` / `♪` cues before curling up for a `Zzz` nap — one keystroke wakes it in 0.3s.
- **Standalone Settings window & edge peeking:** Right-click the pet for a clean `460×800` standalone Settings window (**Characters / Behavior / Bubbles / System / Updates**), smooth `0.33x–3.00x` scaling, half-body screen-edge peeking, fullscreen auto-hide, and one-click in-app self-updates.
- **11-locale full-stack localization:** Automatically follows your Antigravity locale (or switch anytime) across the Settings UI, live tool bubbles, background counters, approval prompts, and context menu: `English`, `简体中文`, `繁體中文 (TW)`, `Français`, `Deutsch`, `日本語`, `한국어`, `हिन्दी`, `ไทย`, `Español (ES)`, and `Español (MX)`.

## How it works

```text
Antigravity agent ──hooks.json──▶ scripts/hook-bridge.mjs ──▶ HTTP 127.0.0.1:47821
                                                                      │
Native Overlay (app/AntigravityPet.cs | app/AntigravityPet.swift) ◀──┘
      └── Right-click Settings ──▶ Standalone Panel (sidecars/panel/server.mjs :47822)
```

- **Lifecycle hooks (`plugin.json` + `hooks.json`):** Triggers `node ./scripts/hook-bridge.mjs` across `SessionStart`, `PreInvocation`, `PreToolUse`, `PostToolUse`, `PostInvocation`, and `Stop`, mapping tool calls via `scripts/tool-label-mapper.mjs` and pushing compact state updates to `127.0.0.1:47821`.
- **Native transparent overlay:** Compiled directly with built-in OS toolchains (`csc.exe` / `.NET Framework 4.x` on Windows; `swiftc` on macOS) — no Electron, no Python runtime, and no extra SDK required.

## Install & Download

**Runtime requirements:** Zero extra dependencies. Uses built-in `.NET Framework 4.x` on Windows 10/11 and built-in `swiftc` on macOS 12+.

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

## Built-in Pets & Community Workshop

- **8 Built-in Pets:** `cyber-fox`, `astro-bot`, `shadow-cat`, `byte-ghost`, `shiba-dog`, `pixel-dragon`, `android-bugdroid`, `flutter-dash`
- **Community Workshop:** Browse, star, and 1-click install community packs directly inside **Settings → Community** (including `gemini-chan`, `cyber-panda`, `pixel-octopus`, `coffee-slime`, `star-hamster`).
- **Unlockable Accessories:** Earn frame-synced accessories as your completed task count grows (**Glasses**, **Dev Cap**, **Coffee Cup**, **Gold Crown**).
- **Create & Submit Your Own:** Drop a single PNG into **Pack Studio** or build a full `1536×2288` (`8×11`) v3 pack following [CUSTOM_PET_SPEC.md](CUSTOM_PET_SPEC.md), then submit via the [Community Pet Submission](https://github.com/Wlaeg/antigravity-pet/issues/new?template=pet_submission.yml) form.

## Security & Privacy

- **Zero telemetry:** Antigravity Pet never collects analytics or phones home. Outbound HTTPS requests occur only when you explicitly browse the Community Workshop, star a pack, or check for updates on GitHub.
- **Zero keylogging:** Typing sync measures only a 1.5-second rolling keystroke frequency count — key codes, characters, and prompt contents are never recorded or stored.
- **Loopback-only local IPC:** The overlay (`127.0.0.1:47821`) and Settings panel (`127.0.0.1:47822`) bind strictly to localhost loopback.
- **No hidden startup entries:** By default, the pet launches and exits with Antigravity without modifying OS startup registries.
- See [SECURITY.md](SECURITY.md) for reporting security issues.

## Contributing & Community

Contributions, bug reports, new pixel mascots, and community packs are welcome:

- Read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) before opening a pull request.
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
CUSTOM_PET_SPEC.md              v3 sprite sheet & community submission specification
build.ps1, build.sh             Zero-dependency Windows & macOS build/launch scripts
CHANGELOG.md                    Full release history (v3.0.0 – v4.6.0)
LICENSE                         MIT License
```

## FAQ

- **What is Antigravity Pet?** A free, open-source pixel desktop pet for Google Antigravity. It sits on your desktop and mirrors your AI agent's status live, so you always know whether your agent is working, waiting on you, or done — without keeping the Antigravity window in front of you.
- **How do I install Antigravity Pet?** Download the latest release, extract it into your Antigravity plugins folder, and run the one-click launcher — see [Install & Download](#install--download). No extra runtime, account, or setup step is required.
- **Does Antigravity Pet work on Windows and Mac?** Yes — native apps for Windows 10/11 and macOS 12+, built with each operating system's own toolchains.
- **Is Antigravity Pet free?** Yes, free and open source under the [MIT License](LICENSE).
- **How is it different from other Antigravity pets?** It lives on your desktop instead of inside the app window, shows the agent's live tool activity instead of just a status name, lets you send work with a double-click and approve risky commands in the bubble, gives background tasks their own moon state, and has a community workshop for sharing pet packs. It also gets bored and falls asleep if you ignore it.
- **Why is there no taskbar / Dock icon?** The overlay uses `WS_EX_TOOLWINDOW` (Windows) and `LSUIElement` (macOS) intentionally to stay out of your window switcher. Use `Win + Alt + P` (`⌥ + ⌘ + P` on macOS) or right-click the pet anytime.
- **Does it stay running in the background after closing Antigravity?** No — by default it follows Antigravity's lifecycle and exits automatically when Antigravity closes.
- Released under the [MIT License](LICENSE).
