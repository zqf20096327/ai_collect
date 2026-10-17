<div align="center">

<img src="assets/branding/app-icon-128.png" alt="Majik's Music Studio" width="128" height="128">

# Majik's Music Studio

**Open-source AI music generation on your desktop.**
**Powered by [ACE-Step 1.5](https://github.com/ace-step/ACE-Step).**

Describe the music in your head — get a full song with vocals, lyrics,
and stems in minutes. Runs locally on your machine. No cloud. No account.
No limits on what you create.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/macOS-14%2B-black?logo=apple)](macos/)
[![Linux](https://img.shields.io/badge/Linux-AppImage%20%7C%20.deb%20%7C%20.rpm-orange?logo=linux)](desktop/)
[![Tracks Made](https://img.shields.io/badge/Tracks%20Made-800%2B-green)](https://majiks.online)

[Download for Mac](https://majiks.studio) · [Listen to 800+ tracks](https://majiks.online) · [Pro Suite](https://majiks.studio/pricing) · [Demo Video](https://youtu.be/LAVmhfazBHM)

</div>

---

## What It Does

<div align="center">

![Chat Interface — describe your song and Majik creates it](assets/screenshots/hero.jpg)

</div>

Chat with an AI producer. Describe the vibe, genre, mood, lyrics — and get a full song with vocals back in minutes. Everything runs locally on your machine.

### Chat-Driven Creation

![Chat interface showing a conversation with the AI producer](assets/screenshots/chat-interface.png)

Describe what you want in natural language. The AI understands genre, mood, BPM, key, instrumentation, and lyrics. Refine through conversation until it's right.

### Studio Session

![Studio session with generation controls and audio waveform](assets/screenshots/studio-session.png)

Fine-tune every parameter: BPM, musical key, duration, lyrics with structure tags, genre and style tags. Generate variants and pick the best one.

### Library Management

![Library browser showing organized tracks with metadata](assets/screenshots/library-browser.png)

Organize your catalog with metadata, album art, and tags. Browse by album, artist, genre, or search. Everything stored locally.

---

## Features

- **Full song generation** — vocals, instruments, lyrics, all from a text description
- **ACE-Step 1.5** — turbo, base, and SFT model variants
- **Export** — WAV, FLAC, MP3, M4A
- **Stem separation** — isolate vocals, drums, bass, and other instruments (via Demucs)
- **AI chat** — Ollama, OpenRouter, Anthropic, OpenAI, DeepSeek, Gemini, and any OpenAI-compatible endpoint
- **Full parameter controls** — BPM, key, duration, lyrics, genre/style tags
- **Library management** — organize, tag, search your catalog
- **100% offline** after model download — your music never leaves your machine

---

## Platforms

| Platform | Status | Stack | Directory |
|----------|--------|-------|-----------|
| **macOS** (native) | Production v2.0.0 | Swift 6, SwiftUI, Python | [`macos/`](macos/) |
| **Linux** | Release-ready | Tauri 2, Svelte 5, Rust, Python | [`desktop/`](desktop/) |
| **Windows** | Coming soon | Tauri 2, Svelte 5, Rust, Python | [`desktop/`](desktop/) |
| **macOS** (Tauri) | Coming soon | Same as Linux | [`desktop/`](desktop/) |
| **Web** | Beta | [studio.magicunicorn.dev](https://studio.magicunicorn.dev) | — |
| **Mobile** | v1 complete | Flutter | — |

### Quick Start

**macOS (native):**
```bash
cd macos/
# See macos/README.md for prerequisites
swift build
swift test  # 84 tests
```

**Linux / Cross-platform (Tauri):**
```bash
cd desktop/
pnpm install
pnpm dev:studio
# See desktop/README.md for prerequisites
cargo test  # 143 Rust tests
```

---

## Pro Suite

The open-source core handles music generation, export, library management, and stem separation — everything you need to create and own your music.

The **Pro Suite** ($29.99 one-time) adds tools for the full creative workflow:

| App | What it does |
|-----|-------------|
| **Publisher** | Publish to [majiks.online](https://majiks.online) or any compatible server. ISRC codes, artist profiles, provenance certificates, sales dashboard. |
| **Songwriter** | Turn conversations, memories, and news into songs. 21 songwriting strategies, knowledge graph, MIDI/MusicXML export. |
| **Art Studio** | AI-generated album covers and artist visuals. |
| **Broadcaster** | Live audio streaming with real-time Rust DSP processing. |
| **Player** | Multiroom audio with AI room correction. |
| **DJ** | Two-deck mixing with effects and MIDI support (coming soon). |

One license key unlocks everything, on every platform. [Get Pro Suite →](https://majiks.studio/pricing)

---

## The Platform

[majiks.online](https://majiks.online) is the companion streaming and buy-to-own music platform. 800+ tracks across 25+ genres from 22 artists — all created with these tools.

- **Free streaming** — no account, no ads
- **Buy to own** — DRM-free downloads (FLAC, WAV, MP3, M4A)
- **100%** of personal license revenue goes to the creator
- Every track has an **ISRC** — real music industry identifiers
- Registered with **SoundExchange** and **The MLC** for royalties

---

## Built With

- [ACE-Step 1.5](https://github.com/ace-step/ACE-Step) — music generation model
- [Tauri 2](https://v2.tauri.app/) — cross-platform desktop framework
- [Svelte 5](https://svelte.dev/) — reactive UI
- [Swift 6](https://swift.org/) / SwiftUI — macOS native
- Rust — DSP, IPC, audio processing
- Python — ML services, model management
- [Demucs](https://github.com/adefossez/demucs) — stem separation

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                 Majik's Music Studio                 │
├──────────────────────┬──────────────────────────────┤
│   macos/ (native)    │   desktop/ (cross-platform)  │
│   Swift 6 / SwiftUI  │   Tauri 2 + Svelte 5         │
│   CryptoKit          │   Rust crates                │
│   macOS 14+          │   Linux / Windows / macOS    │
├──────────────────────┴──────────────────────────────┤
│              Shared Python Backend                   │
│   majiks-music (ACE-Step 1.5)                       │
│   majiks-agent (LLM chat — 7+ providers)            │
│   majiks-ml-core (GPU detection, model management)  │
└─────────────────────────────────────────────────────┘
```

Both builds share the same Python ML backend. The macOS native app communicates via JSON-RPC over stdin/stdout. The Tauri app communicates via FastAPI on localhost.

---

## Tests

| Suite | Tests | Status |
|-------|------:|--------|
| macOS native (Swift) | 84 | Passing |
| Rust crates (cross-platform) | 143 | Passing |
| Python packages | 207 | Passing (6 skipped) |
| **Total** | **434** | **All green** |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for build instructions, code conventions, and how to submit changes.

We welcome contributions to the open-source core. Bug fixes, platform ports, documentation improvements, and new features are all appreciated.

---

## Trademark

"Majik's Music Studio" and the Majiks logo are trademarks of Magic Unicorn Unconventional Technology & Stuff Inc. If you fork this project, you must use a different name and branding. See [TRADEMARK.md](TRADEMARK.md) for details.

---

## License

Apache 2.0 — see [LICENSE](LICENSE) for the full text.

The source code is free to use, modify, and distribute. Logos and visual branding are copyrighted and not covered by the Apache 2.0 license — see [TRADEMARK.md](TRADEMARK.md).

---

<div align="center">

**Built by [Magic Unicorn Inc](https://magicunicorn.tech) in Charleston, SC**

[majiks.studio](https://majiks.studio) · [majiks.online](https://majiks.online) · [magicunicorn.tech](https://magicunicorn.tech)

</div>
