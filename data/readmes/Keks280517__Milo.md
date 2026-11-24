<p align="center"><img src="src-tauri/icons/128x128@2x.png" width="128" alt="Milo"></p>

# Milo

**A personal AI desktop assistant for Windows that lives in a small pill at the top of your screen, in the style of a "dynamic island".**

Milo is a small glowing cube that lives in a black pill at the top edge of your screen. Click it and the island opens into a full assistant: chat, voice, weather, files, notes, system stats, timers and a live view of what Claude Code is doing. Milo thinks with Google Gemini using your own free API key, or with a local AI that runs entirely on your PC. Everyday commands like timers, volume or opening apps run instantly on your PC, without any AI.

> 🇩🇪 Deutsche Version: [README.de.md](README.de.md)

---

## Highlights

- **Island-style UI.** A pill that stays out of your way, springs open on click, hides in fullscreen apps and lets clicks pass through around it. A glass look with refraction and a sliding lens.
- **A character with a life of its own.** Milo has moods, gestures and little adventures: a plant that grows over the days, weather from your location (rain, snow, clouds), stars and fireflies at night, and short walks across your taskbar.
- **Instant quick commands.** Timers, alarms, reminders, volume, media keys, opening apps and websites, screenshots and "what's playing?" run directly on your PC, with no AI involved (most of them even offline).
- **AI chat with tools.** Gemini (with an optional, very fast Groq model as a partner and fallback) can open and arrange apps across monitors, browse and read web pages, research the web with sources, write **Word reports**, read your files (PDF, Word, Excel, PowerPoint), manage notes and more.
- **Local AI, if you prefer.** Don't want to use Google? Milo works with [Ollama](https://ollama.com) or [LM Studio](https://lmstudio.ai) and detects a running server by itself. With your permission it checks your processor, memory and graphics card and recommends a model that fits, which it downloads with one click (percentage and time left show right in the pill) and then connects by itself. If Ollama is installed but not running, Milo starts it. Use it on its own (nothing leaves your PC) or mix it with Gemini: simple questions locally, hard ones in the cloud.
- **Voice, fully local.** Press `Ctrl + Alt + K` to talk, or use the wake word "Hey Milo". Speech recognition runs on your PC (Parakeet, optionally Whisper). Audio is never stored or sent anywhere.
- **Text tools anywhere.** Select text in any app, press `Ctrl + Alt + T` and pick Fix, More formal, More casual, Shorter, Translate, Summarize or Explain. The result replaces your selection.
- **Claude Code companion.** Live view of the file Claude is editing (with diffs), commands, task list and its last message. Approve or deny permission requests, answer Claude's questions and plans right from the island, see your 5-hour and weekly usage limits, and chat with Claude directly from Milo with `/claude`.
- **The pill as a live display.** Timer and countdown cards, upcoming calendar events, Claude status, a clock, scroll to change volume, plus hints for downloads, clipboard, battery and when your microphone or camera is in use.
- **Custom widgets.** Build small widgets with a block editor or describe them and let the AI draft them. They line up next to the island.
- **Files and downloads.** Drag files onto the island, drag them back out, follow running downloads, preview files with Windows thumbnails and move or copy them without ever overwriting anything.
- **History with undo.** Every action is logged for 30 days, and volume changes, scheduled shutdowns and file moves can be undone.
- **Workspaces.** "Save workspace as School" and later "Workspace School" reopens your apps and puts every window back in place.
- **Game mode.** Milo recognizes running games (Steam, Epic, Riot, Xbox, EA, Ubisoft, GOG, Battle.net, Rockstar, Minecraft and more) and goes to sleep, closing its own windows to use almost no resources.
- **Daily rhythm.** A short morning briefing and an evening check-in that Milo remembers.
- **Reliable shutdown.** "Shut down in 10 minutes" works without a confirmation prompt, shows a countdown you can cancel and uses a watchdog that makes sure the PC really turns off.
- **A home screen you arrange yourself.** Music, today's events, weather, timer, system, Claude, notes and more as cards. Drag them into place, pick a size or let Milo lay them out. The weather card is the live sky: drifting clouds, rain, snow, lightning, stars and shooting stars.
- **Guided start.** A welcome wizard (English or German) where you choose Google Gemini or "Without Google" and can set up the local AI right there, plus an interactive tour. And maybe you'll find a little secret while playing around with Milo.

## How Milo picks a model

Milo scores every request from 0 to 100 on your PC, instantly and without AI, and routes it:

| Request | Handled by |
|---|---|
| Quick command | Milo itself, no AI, unlimited |
| Light question, browser tasks, text tools | Gemini Flash-Lite (or Groq, if set up), or your local AI in mixed mode |
| Hard question | Gemini Flash, with automatic fallback to another model |
| Anything, in local-only mode | Your local model via Ollama or LM Studio |
| Report | Research across several searches, summarized and written as a Word file |

Milo counts its own usage per minute, per day and in tokens, so it knows ahead of time when a free quota is used up and switches models instead of running into errors. The **Usage** tab shows the current state.

## Privacy

- **Stays on your PC:** speech recognition, memory and notes, copies of your files, quick commands, and everything the local AI does. Audio is never saved or sent.
- **Sent to Google (Gemini):** your question, the last 8 turns of the conversation and whatever Milo reads to answer it (for example a file you give it, or a screenshot when you ask for one). Milo asks for consent once, and you can turn on "ask before every send". A log of everything sent is available in the settings.
- **API keys** are stored only in the Windows Credential Manager, never in a file.
- **Other services** only receive what they need: your location for the weather (Open-Meteo), search terms for research (DuckDuckGo, Wikipedia).
- **Claude Code:** Milo only reads what Claude Code reports through its own hooks, status line and session log. It never approves anything on its own, only when you click.

## Getting started

### Requirements

- Windows 11 (WebView2 is included)
- A free **Gemini API key** from [Google AI Studio](https://aistudio.google.com/apikey), **or** a local AI with [Ollama](https://ollama.com/download/windows) or [LM Studio](https://lmstudio.ai) (without either, only quick commands work)
- About Gemini: you use your own API key and accept [Google's Gemini API terms](https://aistudio.google.com/docs/terms), which require you to be **18 or older**. On the free tier, Google may use your requests to improve its products and people may review them, so don't send sensitive or personal information. If you'd rather keep everything on your PC, use the local AI instead.
- Optional: a free **Groq API key** from [console.groq.com/keys](https://console.groq.com/keys)
- Optional: the speech models (Parakeet, Whisper, wake word) for voice input

### Install

Run the installer `Milo_<version>_x64-setup.exe`. It installs for your user only and **does not need administrator rights**. On first launch the island opens by itself and the welcome wizard asks for your language, an optional name and whether Milo should think with Google Gemini or with a local AI, then shows you around. Every step can be skipped and done later in the settings.

### Build from source

You need [Rust](https://www.rust-lang.org/tools/install), [Node.js](https://nodejs.org/) and the Visual Studio Build Tools.

```bash
npm install
npm run tauri dev     # development mode
npm run tauri build   # release build with installer
```

The installer ends up in `src-tauri/target/release/bundle/nsis/`.

### Browser extension (optional)

"Milo for the browser" lets Milo click, type, scroll and read pages more reliably in Chrome, Edge, Brave and other Chromium browsers. Load `src-tauri/browser-extension/` as an unpacked extension. Without it, Milo falls back to Windows UI Automation.

## Tech stack

- [Tauri 2](https://tauri.app/) with a **Rust** backend
- **Svelte 5** + SvelteKit (static) + TypeScript + Vite for the UI
- Google Gemini and Groq (OpenAI-compatible) as cloud AI, Ollama and LM Studio as local AI
- Local speech recognition (Parakeet / Whisper) and wake-word detection

## Project structure

| Path | Contents |
|---|---|
| `src-tauri/src` | Rust backend: `agent` (conversation and tool rounds), `gemini`, `groq`, `local` (local AI), `router` (request scoring), `limits` (quota counter), `tools`, `quick` (offline commands), `browser` / `browser_bridge`, `screens`, `power`, `claude` / `claudechat`, `voice`, `tts`, `widgets`, `actionlog`, `workspaces`, `gamemode`, `pulse`, and more |
| `src/lib` | Svelte UI: `Island.svelte`, `Chat.svelte`, `character/` (Milo and the scenery), `views/` (tabs), `cards/`, `widgets/`, `theme.css` (design tokens) |
| `src/routes` | Extra windows: settings, widgets, desktop layer |
| `src-tauri/browser-extension` | The "Milo for the browser" extension (Manifest V3) |
| `scripts/` | Claude Code hook and status line, dev and test helpers, a Gemini mock server |

## Status and known limitations

Milo is a personal project under active development and is **Windows only**.

- Without an internet connection, only quick commands (and the local AI) work.
- The wake word "Hey Milo" can be fooled by TV audio or other voices. Sensitivity is adjustable.
- The island and its walks only appear on the primary monitor. Multi-monitor window placement and display scaling other than 100% are not fully tested.
- Claude usage limits come from Claude Code's status line and need a Pro or Max plan.
- Old `.doc` / `.xls` files and scanned PDFs cannot be read.
- Twitch live checks and web research rely on public web pages and may break if those pages change.

## Security

Found a security problem? Please report it privately, see [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE)

Milo uses open-source components under their own licenses (MIT, Apache-2.0, MPL-2.0 and others), listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Voice input uses [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) with NVIDIA's Parakeet model (CC-BY-4.0) and optionally OpenAI's Whisper (MIT); the models are not part of this repository.

## Disclaimer

Milo is an independent hobby project. It is not affiliated with, endorsed by or sponsored by Apple, Google, Anthropic, Microsoft, Netflix, Twitch or any other company mentioned here. All product names, logos and trademarks belong to their respective owners and are used only to describe what Milo works with. The island design is inspired by, not copied from, existing designs.

Milo is provided "as is", without warranty of any kind (see [LICENSE](LICENSE)). When you let Milo control websites, you are responsible for following those websites' terms of use. Using cloud AI services (such as Google Gemini or Groq) with your own API key is subject to their terms and pricing.
