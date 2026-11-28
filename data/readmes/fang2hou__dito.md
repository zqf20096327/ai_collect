<p align="center">
  <img src="assets/readme/header.png" alt="Dito" width="440">
</p>

<p align="center">
  <strong>A local-first voice assistant for macOS</strong>
</p>

<p align="center">
  Language: <strong>English</strong> / <a href="README.ja.md">日本語</a> / <a href="README.zh-CN.md">简体中文</a> / <a href="README.ko.md">한국어</a>
</p>

Dictation, polishing, rewriting, translation, summaries, replies, Q&A, and meeting transcription for macOS.  
Dito runs local models by default, so your history, audio, and models stay on your Mac.  
You can also connect cloud models and customize prompts when needed.

https://github.com/user-attachments/assets/831d9d6f-c7f4-43d9-8620-2d760d91b9c2

> [!NOTE]
> Dito is in active early development and does not publish prebuilt binaries yet. Build and install it from source with the single script below.

## Install

Requires an Apple Silicon Mac with macOS 13 or later (macOS 14.6 or later for system audio capture).

### Prerequisites

> [!TIP]
> If the tools below aren't installed yet, install [Homebrew](https://brew.sh/) and run the install script; it will walk you through installing anything missing.

1. [Rust](https://www.rust-lang.org/learn/get-started) 1.98 or later
2. CMake
3. [Apple Command Line Tools](https://developer.apple.com/xcode/features/) (if shader compilation reports a missing Metal toolchain, run `bash scripts/setup-macos.sh`)

### Build and install

From the repository root, run:

```bash
bash scripts/install-local.sh
```

## Features

### 1. Dictation

Press your shortcut, speak, and press it again. Dito transcribes your speech and inserts the polished text at the cursor.

Configure the speech model, text model, wordbook, and prompts, including per-app polish rules.  
You can also extract domain terms from existing documents into your wordbook to improve recognition accuracy.

<p align="center"><img src="assets/readme/dictation-en.webp" alt="The HUD listens, transcribes, polishes, and the sentence appears at the cursor" width="720"></p>

### 2. Commands

Select text in any app, press your shortcut, and speak an instruction: polish, rewrite, translate, summarize, reply, or ask a question.

A classifier fitted to small local models routes your instruction offline.  
When you prefer not to speak, hover over the HUD to type the instruction instead.

<p align="center"><img src="assets/readme/command-en.webp" alt="A selected sentence is rewritten by voice and replaced in place" width="720"></p>

### 3. Meeting Transcription

From the Tools window, record system audio, your microphone, or both and get a live transcript. When recording stops, Dito polishes each paragraph in context and generates a title. Paragraphs can be edited in place or copied as text.

<p align="center"><img src="assets/readme/meeting-en.webp" alt="A meeting is transcribed live in the Tools window and polished after it stops" width="720"></p>

### 4. Chat and Local API

Chat uses your selected text model, supports attaching files or completed meeting transcripts, and streams replies with Markdown, code, and tables. With a local model selected, conversations never leave your Mac. Enable the Local API to let other apps on your Mac use the models Dito is set to: the OpenAI-compatible HTTP endpoint offers text generation and speech transcription, and MCP offers text generation and the model list. With a cloud model selected, those requests go to that provider.

<p align="center"><img src="assets/readme/chat-en.webp" alt="A question about the next meeting is answered by a local model, streaming as a list" width="720"></p>

### More features

| | |
| --- | --- |
| **Per-app polish rules** | Layer app-specific rules and writing examples on top of common rules per language |
| **Wordbook** | Import and export hotwords, or extract candidate terms from pasted text, files, or another AI's output |
| **Local and cloud per stage** | Choose a local model or a cloud configuration independently for speech recognition and text processing |
| **History and reruns** | Falls back to the raw transcript if polishing fails; keeps every result and recording in History so you can re-transcribe or re-polish with another model |
| **Stats and 7 UI languages** | Tracks time saved, character count, and speaking speed; UI available in Japanese, English, Simplified Chinese, Traditional Chinese, Korean, Mongolian, and French |
| **Local storage** | History, audio, and models stay on your Mac; cloud API keys are stored in the macOS Keychain, never in config files |

## Models

> [!NOTE]
> Local models are downloaded and managed on demand inside Dito, with resumable downloads and SHA-256 verification.

- Speech recognition (ASR)
  - Local models
    - Qwen3-ASR 1.7B (default)
    - Qwen3-ASR 0.6B
    - SenseVoice Small
    - Haas-ja v1.0
    - Confucius4-R2T2
    - Fun-ASR-MLT-Nano-2512
    - Whisper large-v3
    - Whisper large-v3-turbo
    - Nemotron 3.5 Transcribe 30B-A4B
  - Cloud
    - FunASR
    - Qwen ASR
    - OpenRouter
    - Custom HTTP requests (configured in the built-in JSON editor)
- Text processing (polish, commands, chat)
  - Local models
    - Qwen3.5 Instruct 2B
    - Qwen3.5 Instruct 4B
    - Qwen3.5 Instruct 9B (default)
    - Qwen3.8 27B
    - Ternary Bonsai 2.5 27B
  - Cloud
    - Azure OpenAI
    - Amazon Bedrock
    - Any OpenAI-compatible API
- Speech detection (meetings)
  - Local models
    - Silero VAD

## Development

```bash
mise install                 # Rust, Python, uv, and ruff at the pinned versions
mise run dev:mock            # whole app with mock cloud, microphone, and data
mise run dev                 # real microphone, models, and providers
mise run check               # format check and fast tests
mise run lint:rust           # clippy, also with the mock and screenshots features
mise run readme:assets       # regenerate the README animations (build the screenshot binary first)
```

Dito is a Rust workspace built on [GPUI](https://www.gpui.rs/). UI design in `design/dito.figcraft` leads, and the code follows it.

| Goal | Read |
| --- | --- |
| Build, run with mocks, test | [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) |
| Run locally, flags, diagnose a problem | [docs/DEBUGGING.md](docs/DEBUGGING.md) |
| Architecture and decisions | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [ADRs](docs/adr/README.md) |
| Terms and where each concept lives | [docs/GLOSSARY.md](docs/GLOSSARY.md) |
| What the app does and why | [design/features.md](design/features.md) |
| UI and motion design | [design/README.md](design/README.md) |
| Work with an AI coding agent | [AGENTS.md](AGENTS.md) |

## License

[MIT](LICENSE)
