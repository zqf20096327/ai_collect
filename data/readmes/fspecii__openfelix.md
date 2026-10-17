<div align="center">

<img src="assets/openfelix-logo.png" alt="OpenFelix" width="300" />

# OpenFelix 😼

**The voice-first AI agent for macOS that actually runs locally.**

> ⚠️ **Early-stage functional prototype.** Core features work — voice, tools, skills, cloud backends. Rough edges exist. We need your help to make this the best it can be.

[![License](https://img.shields.io/badge/license-Apache%202.0-amber.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%2013%2B-black.svg)](https://github.com/fspecii/openfelix)
[![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-required-orange.svg)](https://github.com/fspecii/openfelix)
[![Twitter](https://img.shields.io/badge/follow-%40openfelixai-1DA1F2.svg)](https://x.com/openfelixai)

[**Download DMG**](https://github.com/fspecii/openfelix/releases/tag/v0.1.0) · [**Watch Demo**](https://www.youtube.com/watch?v=tUmCYdsq7Sw) · [**Website**](https://openfelix.com) · [**Follow @openfelixai**](https://x.com/openfelixai)

---

*Named after a real Persian cat. Silver. Amber eyes. Always watching.*

**Created by [@AmbsdOP](https://x.com/AmbsdOP)**

</div>

---

## 🎬 Demo

[![OpenFelix Demo](https://img.youtube.com/vi/tUmCYdsq7Sw/maxresdefault.jpg)](https://www.youtube.com/watch?v=tUmCYdsq7Sw)

> **[Watch the demo on YouTube →](https://www.youtube.com/watch?v=tUmCYdsq7Sw)**

---

## What is OpenFelix?

OpenFelix is a free, open-source AI agent that lives in your Mac menu bar. Press **Option+Space** anywhere, speak or type your request, and Felix acts — reads your calendar, searches the web, sends messages, runs scheduled tasks, generates music, and talks back in a natural voice.

It's not a chatbot. It's an agent with tools, voice I/O, and a skill system that extends it to anything. It runs **fully on-device** with local MLX models, and seamlessly upgrades to Claude or any cloud model when you want the best quality.

> *"When OpenClaw meets Siri."* 😼

---

## 🙏 We Need Your Help

I'm **not a Swift developer** — I built this to prove the concept works, and it does. But to make OpenFelix the **best open-source voice assistant for macOS**, we need people who know what they're doing.

If you're a Swift developer, macOS engineer, AI/ML enthusiast, or just someone who wants a great local voice assistant on your Mac — **this project is for you**.

**This could be the best voice AI project ever built for macOS.** The foundation is here. Help us finish it.

👉 **[Open an issue](https://github.com/fspecii/openfelix/issues)** · **[Submit a PR](https://github.com/fspecii/openfelix/pulls)** · **[Star the repo ⭐](https://github.com/fspecii/openfelix)**

Areas where we especially need help:
- Swift / macOS native development
- Whisper integration for local STT
- UI/UX polish
- Skill development
- Testing across different Mac hardware

---

## Download

**Easiest way to get started:**

1. Download [`OpenFelix.dmg`](OpenFelix.dmg)
2. Open the DMG — double-click **Run Me First.command** (sets up Python + local AI engine)
3. Drag **OpenFelix.app** to your Applications folder and launch it
4. Grant **Accessibility** permission when prompted (required for global hotkey)

---

## Features

| Capability | Description |
|---|---|
| 🎙️ **Voice & Text** | Option+Space to speak, Option+T to type |
| 🧠 **Local AI** | Runs Qwen / Mistral / any MLX model on Apple Silicon — 100% on-device |
| ☁️ **Cloud Models** | Claude, GPT-4o, or any OpenAI-compatible model |
| 👁️ **Screen Vision** | Sees and analyzes anything on your screen |
| ⏰ **Cron Jobs** | Schedule tasks: `daily@09:00`, `every:30m`, `once:ISO8601` |
| 📲 **Proactive Alerts** | Sends updates to Telegram, Discord, Slack |
| 🎬 **YouTube** | Search, play, and get spoken summaries |
| 📖 **Wikipedia** | Instant spoken answers |
| 💻 **Code & Files** | Generates, reads, and runs code |
| 📅 **Calendar** | Reads and creates Apple Calendar events |
| 🔔 **Reminders** | Full Apple Reminders integration |
| 🗺️ **Maps** | Location search and directions |
| 🎵 **Music Generation** | Generates music via ACE-Step |
| 📈 **Finance** | Stock prices and market data |
| 🐦 **X / Twitter** | Read your feed and search topics |
| 🧩 **Skill System** | Extensible — skills auto-install on first run |
| 🦞 **OpenClaw Native** | Inherits all your OpenClaw skills and API keys automatically |

---

## LLM Backends

### Local (no API key needed)

Runs fully on-device via [MLX](https://github.com/ml-explore/mlx). Switch model size from the menu bar:

| Model | RAM | Tool Calling |
|-------|-----|-------------|
| Qwen 3.5 0.8B | ~1 GB | Basic — may miss tools |
| Qwen 3.5 2B *(default)* | ~2 GB | Decent for simple tasks |
| **Qwen 3.5 4B** | ~3 GB | **Recommended minimum for tools** |
| **Qwen 3.5 9B** | ~6 GB | **Best local experience** |

> **Recommendation:** Use at least a **4B–9B model** for reliable tool calling. Smaller models (0.8B–2B) can handle basic Q&A but often fail on multi-step tool use. The local models are genuinely good — but if you want consistent, production-quality results across all features, use a cloud backend.

Override the default model:
```bash
MLX_MODEL_PATH=mlx-community/Qwen2.5-7B-Instruct-4bit bash scripts/run-app.sh
```

### Cloud (strongly recommended for best experience)

For the most reliable tool calling, fastest responses, and best reasoning quality, use a cloud backend. **We especially recommend Claude** — it has excellent instruction following, strong tool use, and handles OpenFelix's structured prompts exceptionally well.

```bash
# Anthropic Claude (recommended)
export ANTHROPIC_API_KEY=sk-ant-...

# OpenAI GPT
export OPENAI_API_KEY=sk-...

# OpenRouter (access any model)
export OPENROUTER_API_KEY=sk-or-...
```

Or use [**OpenClaw**](https://openclaw.ai) — Felix reads your entire OpenClaw config automatically (models, API keys, skills). Zero duplicate configuration.

---

## OpenClaw Integration 🦞😼

OpenFelix and [OpenClaw](https://openclaw.ai) are designed to work together seamlessly — they share the same skill format, config files, and API keys. If you have OpenClaw installed, Felix picks up your entire setup with **zero additional configuration**:

- **All OpenClaw skills work in OpenFelix out of the box** — same `SKILL.md` format, same `scripts/` structure, write once run in both
- **LLM config** — same model and API keys, no re-entry
- **Notifications** — Telegram, Discord, Slack routing inherited automatically
- **API keys** — all provider keys shared between both apps
- **Two-way communication** — OpenFelix and OpenClaw can interact, share context, and hand off tasks to each other

**If you're an OpenClaw user, OpenFelix is a zero-friction addition.** You already have everything you need.

---

## Skill System

Felix ships with built-in skills that install automatically on first run:

| Skill | What it does |
|-------|-------------|
| **youtube-search** | Searches YouTube and opens the best result |
| **youtube-info** | Summarizes any YouTube video (paste a link) |
| **finance-lookup** | Stock prices and market data |
| **ace-music** | Generates music from a text prompt (requires `ACE_MUSIC_API_KEY`) |
| **bird** | Reads your X/Twitter feed (requires `npm install -g @steipete/bird` + `bird auth`) |

### Adding skills

Skills live in `~/.openfelix/skills/`. Each skill is a folder with a `SKILL.md` and a `scripts/` directory. They are fully compatible with OpenClaw skills.

### Scheduling skills

Add a `schedule:` line to any `SKILL.md` frontmatter:

```yaml
schedule: daily@09:00      # Every morning at 9
schedule: every:30m        # Every 30 minutes
schedule: once:2026-03-07T10:00  # One-time
```

---

## Build from Source

### Requirements

- macOS 13+ (Ventura or later)
- Apple Silicon (M1/M2/M3/M4)
- Xcode 15+
- Python 3.12+

```bash
git clone https://github.com/fspecii/openfelix
cd openfelix
bash scripts/setup.sh   # one-time: creates Python venv, installs mlx-lm
bash scripts/run-app.sh # build and launch
```

First launch downloads the default model (~2 GB). Subsequent launches are instant.

### Permissions

- **Accessibility** — System Settings → Privacy & Security → Accessibility → add OpenFelix (required for global hotkey suppression)
- **Microphone** — prompted automatically on first use

---

## Architecture

```
openfelix/
├── swift-test/Sources/openfelix-app/
│   ├── AppController.swift       # Core state machine + menu bar
│   ├── OpenClawBackend.swift     # Claude via OpenClaw / Anthropic API
│   ├── MLXBackend.swift          # Local MLX models
│   ├── OpenAIBackend.swift       # GPT / any OpenAI-compatible
│   ├── ToolKit.swift             # Tool calling + system prompts
│   ├── SkillLoader.swift         # Skill discovery and execution
│   ├── STTEngine.swift           # Speech-to-text (AUHAL + Apple on-device)
│   ├── TTSSpeaker.swift          # Text-to-speech
│   └── ...panels, overlay, timers
├── skills/                       # Built-in skills (auto-installed on first run)
├── scripts/
│   ├── setup.sh                  # One-time setup
│   ├── run-app.sh                # Build and launch
│   └── channel-daemon/           # Telegram / Discord / Slack daemon
└── assets/
```

---

## Status

This is a **functional prototype** — the core loop (voice → STT → LLM → tools → TTS) works well. The following are known rough edges we're actively working on:

- [ ] Whisper local STT (currently uses Apple's on-device recognizer)
- [ ] App Store release
- [ ] Skill marketplace
- [ ] Multi-language voice support
- [ ] iOS companion app
- [ ] Plugin API docs

---

## Contributing

PRs welcome. Open an issue first for major changes.

---

## License

Apache 2.0 — free to use, modify, and distribute.

---

<div align="center">

**Built with ❤️ and a Persian cat named Felix 😼**

Created by **[@AmbsdOP](https://x.com/AmbsdOP)**

[openfelix.com](https://openfelix.com) · [@openfelixai](https://x.com/openfelixai)

*I'm not a Swift developer — I just wanted a great voice assistant on my Mac.*
*Help make this the best open-source voice AI for macOS. ⭐*

</div>
