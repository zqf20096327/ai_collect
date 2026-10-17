![OpenEcho banner](./assets/readme-banner.svg)

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

# OpenEcho

**Speak once. Insert clean text anywhere.**

OpenEcho is a macOS desktop app that turns your voice into polished text, translations, answers, and structured memos — all from a single shortcut. Speech recognition runs locally on your machine, your audio never leaves your device.

![macOS](https://img.shields.io/badge/macOS-desktop-111827?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-10B981?style=flat-square)
![Whisper](https://img.shields.io/badge/speech-local%20Whisper-10B981?style=flat-square)
![LLM](https://img.shields.io/badge/LLM-optional-111827?style=flat-square)

---

## Quick Start

1. **Download** the latest `.dmg` from the [Releases](https://github.com/weenable/openecho/releases) page (Apple Silicon only)
2. **Install** — open the `.dmg`, drag OpenEcho to Applications
3. **Launch** — the setup wizard walks you through permissions, microphone test, and model download
4. **Use** — press the global shortcut, speak, done. Text appears wherever your cursor is.

> If macOS blocks the app, run: `sudo xattr -dr com.apple.quarantine /Applications/openecho.app`

---

## Why OpenEcho?

Most voice tools send your audio to the cloud, lock you into one use case, or break your workflow. OpenEcho is different:

- **Privacy first** — Whisper runs locally. Your voice stays on your Mac.
- **One shortcut, five modes** — Input, Translate, Question, Memo, Voice Generate. No app switching.
- **Works with any app** — Text is pasted directly into whatever you're working in.
- **LLM is optional** — Core voice-to-text works offline. Connect an OpenAI-compatible API for extra features when you want them.

---

## Screenshots

### Setup

Guided first-launch wizard — permissions, microphone test, model download, and optional LLM configuration.

![Setup - Preferences](./assets/setup-1.png)
![Setup - Configuration](./assets/setup-2.png)

### Voice Input

Press a shortcut, speak, and polished text is pasted wherever your cursor is.

![Voice Input](./assets/voice.png)

### Dashboard

Overview of your settings, recent transcriptions, and quick access to all features.

![Main Window](./assets/main.png)

### History

Browse, play back, copy, or delete past transcriptions. Audio recordings are saved alongside each entry.

![History](./assets/history.png)

### Voice Generate

Type text and generate speech with local or remote TTS. Preview, save, and choose from multiple languages.

![TTS](./assets/tts.png)

### Settings

Configure LLM, TTS, recognition model, shortcut, theme, and more.

![Settings](./assets/setting.png)

---

## What can it do?

### Input

Press the shortcut, speak, and the recognized text is cleaned up and pasted into your current app. Perfect for emails, messages, code comments — anywhere you type.

### Translate

Speak in your language, get text in another. Choose your target language, and OpenEcho handles the rest through your LLM endpoint.

### Question

Ask a question by voice. OpenEcho shows both your question and the AI-generated answer in a floating panel. Great for quick lookups without leaving your workflow.

### Memo

Dictate a messy thought. OpenEcho organizes it into a structured memo you can review and edit before inserting.

### Voice Generate

Type text and hear it spoken aloud. Supports local TTS (Kokoro, runs offline) or remote TTS APIs (OpenAI-compatible). Preview, save as audio file, and choose from multiple languages.

---

## How it works

```text
Global shortcut
      ↓
Microphone capture
      ↓
Local Whisper model
      ↓
  ┌─────────────────────────────────────────────────┐
  │  Input     → clean text → paste into your app   │
  │  Translate → LLM translation → paste            │
  │  Question  → LLM answer → floating Q&A panel    │
  │  Memo      → LLM organization → editable memo   │
  └─────────────────────────────────────────────────┘
```

---

## Build from source

Requires macOS, Node.js, and Rust toolchain.

```bash
npm install
npm run tauri dev       # development
npm run tauri build     # production build
```

## Release

Releases are automated via GitHub Actions. To create a new release:

```bash
git tag v0.1.0
git push origin v0.1.0
```

This will:
1. Build `.dmg` installer for Apple Silicon Mac
2. Generate a changelog from commit history since the last tag
3. Create a GitHub Release with the installers and changelog

> **Note:** The app is not code-signed. On first launch, right-click → Open, or allow it in System Settings → Privacy & Security.

## License

[MIT](./LICENSE)
