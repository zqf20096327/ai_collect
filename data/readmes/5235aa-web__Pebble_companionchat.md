<div align="center">

<img src="docs/logo.svg" alt="P.C.C — Pebble Companion Chat" width="600" />

<br />

<h3>Pebble Companion Chat (P.C.C)</h3>
<p>Lightweight, focusing on multi-sensory immersive chat, customizable local &amp; cloud model-based character card chat dialogues — combining multiple conversations, multi-character group rooms, cascaded streaming voice calls, long-term memory, and an integrated picture studio.</p>

<p>
  <a href="https://github.com/5235aa-web/Pebble_companionchat/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/5235aa-web/Pebble_companionchat/ci.yml?branch=main&style=flat-square&labelColor=14110f&label=CI" alt="CI" /></a>
  <img src="https://img.shields.io/badge/Backend-FastAPI%200.136-e0a35e?style=flat-square&labelColor=14110f" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Frontend-Vue%203%20%2B%20TypeScript-c4bcae?style=flat-square&labelColor=14110f" alt="Vue 3 + TypeScript" />
  <img src="https://img.shields.io/badge/Desktop-Tauri%202-e0a35e?style=flat-square&labelColor=14110f" alt="Tauri 2" />
  <img src="https://img.shields.io/badge/Local%20Inference-llama.cpp%20%2B%20audio.cpp-a87754?style=flat-square&labelColor=14110f" alt="llama.cpp + audio.cpp" />
  <img src="https://img.shields.io/badge/UI-English%20%2F%20中文-ece5d8?style=flat-square&labelColor=14110f" alt="Bilingual UI" />
</p>

</div>

---

## 📋 Changelog

**Current Version: `v1.0.4`** — View full release notes in [CHANGELOG.md](CHANGELOG.md).

`v1.0.4` adds **Card-Aware Media Tag Protection** (preserving custom card tags like `<pimg="...">`), **Lore Panel Overhaul & Isolated Translation** (full embedded character-book import defaulting to media-only activation, per-entry toggles, true depth injection, and display-only Chinese/English translation), and **Stage HUD Affection & Portrait Fixes** (healing annotated affection values, filtering noisy multi-character assets, and syncing custom inline tags to the stage).

<details>
<summary>Previous release summary (<code>v1.0.3</code>)</summary>

`v1.0.3` adds **Group Chat Voice Input** (direct voice messages with tap-to-pick or automatic speaker routing, plus transcribe-to-draft editing and native audio/transcript fallback) and fixes **Voice Call Interruption** during AI speech playback (restoring Silero VAD barge-in, non-streaming playback interruption, and adding a manual **Interrupt** button).

</details>

---

## ✨ Overview

**Pebble Companion Chat (`P.C.C`)** is a desktop and web AI companion workspace driven by text, voice, and generated imagery. The backend is built with **FastAPI + SQLite + WebSockets**, paired with a **Vue 3 + Pinia + Vite** frontend (`frontendV2`) that can also be packaged as a lightweight **Tauri 2** desktop application (with standalone backend packaging supported via PyInstaller).

Whether running local GGUF weights, calling cloud LLM APIs, holding live voice calls, or staging multi-character scenes, all conversations, character cards, and extracted memories remain persisted locally under your control.

<p>
  <img src="docs/png0.png" alt="loading interface" width="1000">
</p>

<p align="center">
  <img src="docs/png1.png" alt="Single chat" width="49%" />
  <img src="docs/png2.png" alt="group room for 2" width="49%" />
</p>
<p align="center">
  <img src="docs/png3.png" alt="Single chat" width="49%" />
  <img src="docs/png4grouproom.png" alt="Group room detail" width="49%" />
</p>

---

## 🌟 Core Features

### 1. Single Chat & Multiple Conversations
Streaming narrative replies with candidate swipes, independent conversation threads per character card, and manual token-aware context compaction. Import SillyTavern JSONL logs directly into new branches with swipes and variables intact, or export any branch to Markdown, rich self-contained HTML, Pebble JSON, or SillyTavern JSONL.

### 2. Multi-Character Group Stage
Bring up to 3 companions onto a fanned portrait stage with `@` speaker cues, autonomous multi-turn **Relay**, isolated room memories, and a one-click **Narration Mode** to steer scenes without polluting ongoing context.

### 3. Live2D
An optional local portrait-decomposition module (`See-through`, safely skipped with zero PyTorch required) that turns static art or expression packs into interactive WebGL2 puppets with breathing, gaze tracking, TTS lip-sync, multi-outfit switching, and touch reactions.

### 4. Character Cards
Import and edit SillyTavern **PNG / JSON**, **CHARX**, and RisuAI **`.risum`** packages with automatic asset unpacking, inline media, a reactive Stage HUD, global rules, and a no-regex **Scene Rules Workshop** for plain-language or block-based customization.And it has a built-in translation function, which translates the description fields of the character cards (independently of the original text), supporting both Chinese and English.

### 5. Script Mode
Direct stories scene by scene using ordered turn budgets, a structured `<<<STATE>>>` HUD progression protocol, isolated prompts, instant scene rewind, and preserved per-scene summary cards.

### 6. Long-Term Memory & Token Engine
Automatically extract and rank durable memories using embedding-free BM25 retrieval (no vector store or extra model needed), paired with provider-aware token counting across local and cloud backends.

### 7. Cascaded Streaming Voice Calls, TTS & ASR
Hold natural spoken conversations through an interchangeable **ASR → LLM → TTS** streaming loop with Silero VAD barge-in, supporting local `audio.cpp` engines alongside OpenAI-compatible and cloud speech providers.

### 8. Picture Studio & Multimodal Attachments
Chat with images, documents, and sampled video frames (with opt-in speech transcription), and generate manual or story-triggered scene illustrations via local ComfyUI or cloud image providers into a unified gallery.

### 9. Customizable Aesthetic
Switch seamlessly between **Day / Night** themes, **7 accent palettes** (Amber, Ember, Celadon, Moon, Plum, Jade, Rose), selectable typography, and instant **English / 中文** UI localization.

---

## 🧩 Supported Providers & Engines

| Capability | Local Engines / Protocols | Cloud / External Providers |
| :--- | :--- | :--- |
| **LLM Chat** | `llama.cpp` (`llama-server` with GGUF, `mmproj` vision & MTP), Ollama, LM Studio, any local OpenAI-compatible endpoint | OpenAI, ChatGPT, DeepSeek, Qwen, Grok, Xiaomi MiMo, Volcengine, Anthropic, Gemini — every provider is called through the OpenAI-compatible `/chat/completions` protocol with a bearer key, so Anthropic and Gemini need a base URL that speaks it (their own gateway or a compatible proxy) |
| **TTS (Voice)** | `audio.cpp` (OmniVoice, DotTTS, Fish Audio, Ming 3.0 & custom GGUF specs), OpenAI-compatible HTTP endpoint | MiniMax, ElevenLabs |
| **ASR (Ears)** | `audio.cpp` (built-in Qwen3-ASR, Confucius4-R2T2 & custom GGUF specs), custom OpenAI-compatible HTTP | OpenAI-compatible STT endpoints |
| **Picture Studio** | Local ComfyUI (with custom workflow JSON import) | SiliconFlow (Kolors), Zhipu (CogView-3-Flash), Cloudflare Workers AI, AI Horde, Gemini, ModelScope, Pollinations |

## 🚀 Quick Start

### Prerequisites

- **Python** 3.10+
- **Node.js** 18+ and `npm`
- **Local Inference (Optional)**: `llama-server.exe` is **not bundled** with the app. To use the built-in managed `llama.cpp` runtime for local GGUF LLM chat, download a `llama.cpp` release for your hardware and configure its directory or executable under **Backstage → Paths → `llama.cpp runtime`** (or place it in `<modelsRoot>/llama`), and set your shared local model directory under **Backstage → Paths → `Models root`**. (The `audio.cpp` runtime for local TTS/ASR is bundled, and external local servers such as Ollama or LM Studio can be connected directly without `llama-server.exe`.)

### 1. Install Dependencies

```bash
# Core backend dependencies
pip install -r requirements.txt

# Frontend dependencies
cd frontendV2
npm install
```

#### Optional: Live2D Local Decomposition Dependencies

> Skip this step if you do not plan to use local Live2D portrait decomposition; the rest of the application does not require PyTorch.

**Windows:**

```bat
:: 1) Create & activate an isolated virtual environment (Python 3.11 / 3.12 recommended)
python -m venv "%USERPROFILE%\.pebblecompanion\inochi2d-venv"
"%USERPROFILE%\.pebblecompanion\inochi2d-venv\Scripts\activate.bat"

:: 2) Install PyTorch for your GPU (see backend/Inochi2D/requirements.txt for NVIDIA CUDA / AMD ROCm / CPU notes)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126

:: 3) Install headless Live2D inference & post-processing dependencies
pip install -r backend\Inochi2D\requirements.txt
```

**macOS / Linux (Experimental — untested):**

```bash
# 1) Create & activate the isolated virtual environment
python3 -m venv ~/.pebblecompanion/inochi2d-venv
source ~/.pebblecompanion/inochi2d-venv/bin/activate

# 2) Install PyTorch for your platform (CUDA 12.x on Linux; use --index-url .../whl/rocm6.3 for Linux ROCm, or plain install for macOS MPS / CPU)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126

# 3) Install headless Live2D inference & post-processing dependencies
pip install -r backend/Inochi2D/requirements.txt
```

Download the two `See-through` model repositories into your `Models root` directory (`seethroughv0.0.2_layerdiff3d` and `seethroughv0.0.1_marigold`):

- **LayerDiff3D**: <https://huggingface.co/layerdifforg/seethroughv0.0.2_layerdiff3d> → `<modelsRoot>/seethroughv0.0.2_layerdiff3d`
- **Marigold Depth**: <https://huggingface.co/24yearsold/seethroughv0.0.1_marigold> → `<modelsRoot>/seethroughv0.0.1_marigold`

```bash
# Optional quick download via huggingface_hub inside your inochi2d-venv
python -c "from huggingface_hub import snapshot_download; snapshot_download('layerdifforg/seethroughv0.0.2_layerdiff3d', local_dir='<modelsRoot>/seethroughv0.0.2_layerdiff3d'); snapshot_download('24yearsold/seethroughv0.0.1_marigold', local_dir='<modelsRoot>/seethroughv0.0.1_marigold')"
```

Both source runs and packaged desktop builds share `~/.pebblecompanion/inochi2d-venv` automatically, and you can also point **Backstage → Paths → `Live2D Python`** to any existing `venv` or `conda` environment.

### 2. Run in Development

#### Option A: Windows One-Click Launcher

Run the root batch script to start both the backend and frontend dev servers in separate terminals:

```bat
companion.bat
```

#### Option B: macOS / Linux Launcher (Web UI)

Run the root shell script to start both the backend (`8002`) and frontend dev server (`5176`) in one terminal (press `Ctrl+C` to stop both; use `./frontendv2.sh` to start the frontend alone):

```bash
chmod +x companion.sh frontendv2.sh
./companion.sh
```

#### Option C: Manual Startup

```bash
# Terminal 1: Start the FastAPI backend (http://localhost:8002)
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8002

# Terminal 2: Start the Vite dev server (http://localhost:5176)
cd frontendV2
npm run dev
```

Open `http://localhost:5176` in your browser to get started:

1. **Import a character**: Open **Cast** in the top bar and import your character card (`PNG` / `JSON` / `CHARX` / `.risum`).
2. **Import chat history (optional)**: To bring over an existing SillyTavern conversation for that character, open the **Branches** menu in the top bar and select **+ import JSONL**.
3. **Configure your model & chat**: Open **Backstage** (`Model` tab) to set up a local LLM (`llama.cpp`, Ollama, LM Studio, etc.) or enter a cloud API key (along with optional Voice, Ears, Paths, and Pictures settings), then start chatting right away!

### 3. Desktop Build (Tauri 2)

> **Windows Users:** You can skip building from source and download the pre-built Tauri desktop installer directly from the [Latest Release](https://github.com/5235aa-web/Pebble_companionchat/releases/latest) page (always redirects to the newest release).

To build from source with the Rust toolchain installed, run inside `frontendV2`:

```bash
cd frontendV2

# Desktop development mode
npm run tauri:dev

# Build desktop installer (Windows NSIS)
npm run tauri:build
```

---

## ⚙️ Data Directory & Environment Variables

To keep conversations and settings safe across rebuilds or upgrades, all writable user data is stored under `~/.pebblecompanion` by default (including `companions.db`, `uploads/`, `config/`, and `voice/` reference clips).

You can override default locations with environment variables:

- `PEBBLE_DATA_ROOT` — Override the root directory for writable user data and config files.
- `PEBBLE_MODELS_ROOT` — Override the default root directory for local model weights (also configurable via **Backstage → Paths**).

---

## 💬 Support & Feedback

If you happen to be using it and find it enjoyable, a **Star** is a great way to support the author; and if you run into issues or have suggestions, feel free to open an **Issue** anytime!
