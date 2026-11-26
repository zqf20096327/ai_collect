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

## ✨ Overview

**Pebble Companion Chat (`P.C.C`)** is a desktop and web AI companion workspace driven by text, voice, and generated imagery. The backend is built with **FastAPI + SQLite + WebSockets**, paired with a **Vue 3 + Pinia + Vite** frontend (`frontendV2`) that can also be packaged as a lightweight **Tauri 2** desktop application (with standalone backend packaging supported via PyInstaller).

Whether running local GGUF weights, calling cloud LLM APIs, holding live voice calls, or staging multi-character scenes, all conversations, character cards, and extracted memories remain persisted locally under your control.

<p>
  <img src="docs/png0.png" alt="loading interface" width="1000">
</p>

<p align="center">
  <img src="docs/png1.png" alt="Single chat" width="49%" />
  <img src="docs/png2.png" alt="Script mode" width="49%" />
</p>
<p align="center">
  <img src="docs/png3grouproom.png" alt="Group room" width="49%" />
  <img src="docs/png4grouproom.png" alt="Group room detail" width="49%" />
</p>

---

## 🌟 Core Features

### 1. Single Chat & Multiple Conversations
- **Narrative Stage**: Streaming replies, stage-direction / narration mode, message regeneration (reroll), and multiple candidate versions.
- **Multiple Conversations**: Start a new conversation on the same card, switch, rename, or delete them, and see the active one in the side rail. A conversation is an independent thread, not a fork of an existing one.
- **Manual Context Compaction**: Fold older history into a summary on demand — segmented summarization with token-aware budgets. Nothing is compacted automatically.

### 2. Multi-Character Group Stage
- **Up to 3 Companions per Room**: Characters appear as fanned portrait cards behind a semi-transparent reading column.
- **Stage Direction & Pacing**: Mention specific speakers with `@`, click any card to cue their next line, enable multi-turn **Relay** rounds for autonomous back-and-forth, or manage room members with `/invite` and `/remove`.
- **Per-Room Context**: Configure a shared room scene, room-specific user persona notes, and isolated room memories and summaries.
- **Narration Mode (Give the conversation a break)**: One-click activation switch supporting all chat modes. In a voice-over manner, describe the behaviors and states (actions, space, psychology) of the user and character to guide the dialogue direction—affecting only the next reply without continuously contaminating surrounding context.

### 3. Live2D
- **Optional Local Decomposition**: This is an **optional** module (`backend/Inochi2D` + WebGL2 stage) and **does not affect normal usage** when skipped—core text chat, voice calls, picture generation, and built-in `2.5D Motion` work normally with zero PyTorch or GPU dependencies. When enabled, you can locally decompose a single character portrait or same-pose expression pack via `See-through` (`LayerDiff3D` + `Marigold`) across NVIDIA CUDA, AMD ROCm, or CPU fallback, with automatic blink-layer synthesis, collar/neck occlusion cleanup, and bilingual expression mapping.
- **Interactive WebGL2 Stage & Multi-Outfit**: Once built, the puppet renders purely client-side in WebGL2 with breathing and body sway, spring hair/accessory physics, soft global gaze tracking, real-time TTS audio lip-sync, cheek blush shaders, and interactive pointer gestures (head pat, cheek poke/pet, and startled chest-tap recoil). Both CHARX cards and standard PNG/JSON cards can attach expression packs or add same-pose outfits incrementally through **Character Editor → Media assets** and **Live2D → Build**.

### 4. Character Cards
- **SillyTavern Ecosystem**: Import and export **PNG / JSON** character cards, with a built-in editor covering identity, dialogue fields (first message, conversation examples, advanced prompt), bound TTS voice clip/ID, system instructions, and raw JSON.
- **CHARX Cards & `.risum` Modules**: Import **CHARX** (`.charx` / `.zip` Character Card V3 packages) and RisuAI **`.risum` / `module.json`** packs effortlessly—including large multi-media archives. Pebble automatically unpacks alternate greetings, character expressions, illustrations, background music, sound effects, video clips, card stylesheets, variables, and rewrite scripts into organized per-character storage that you can browse and manage right in the editor.
- **Rich Media & Stage HUD**: Greetings and chat replies render clean Markdown, styled HTML/CSS cards, decorative SVG accents, and bundled media right inline—showing character expressions, scene art, video cards, and playable audio/BGM pills with automatic typo recovery when the AI slightly misspells an asset name. For media-rich cards in single chat, an optional Stage HUD gently tracks mood, affection, location, and outfit while swapping portraits and sound cues as the story unfolds.
- **Scene Rules Workshop (No-Regex Customization)**: Click the quick button in the chat composer to slide open a **non-overlaying upward dock** synced automatically with your active character—no regex writing required:
  - **Plain-Language & Offline Blocks**: Describe formatting, cleanup, or story triggers in everyday words (compiled and auto-verified against a real sample reply), or combine offline visual blocks to restyle inner thoughts, badges, OOC cleanup, context-only history trimming, and idle/time/turn-aware behaviors.
  - **One-Click Recipes & Live Sandbox**: Toggle curated immersive presets, tweak live character variables, preview real message bubbles on the spot, or translate cryptic rules inside imported cards into plain language with one click.
- **Global Rules**: Append shared scope, behaviour, and post-history instructions across all characters without editing individual cards.

### 5. Script Mode
- **Scene-by-Scene Playthrough**: Author a script as ordered scenes, each with its own title, turn budget, and director instruction. The model advances one scene at a time instead of free-running the story.
- **Structured State Protocol**: Every reply ends with a `<<<STATE>>>` block carrying HUD fields (mood, affection, location, outfit) and a scene-done flag. A stream filter strips the block from the visible text and uses it to drive progression.
- **Rewind & Per-Scene Summaries**: Roll the session back to any earlier scene, and compact each scene into its own summary card that stays readable in the thread — unlike chat compaction, scene summaries are never merged into one.
- **Isolated Prompt Path**: The scripted prompt is built separately from the normal chat prompt, so no memory, lore or card field leaks into a scene.

### 6. Long-Term Memory & Token Engine
- **Embedding-Free Memory Retrieval**: Durable facts and relationship memories are extracted in the background, then ranked without any embedding model. Scoring is BM25 over keyword and token fields (with CJK n-gram weighting), phrase hits, importance, and use-count damping — no vector store, no extra model to download.
- **Provider-Aware Token Counting**: Prefers server-reported usage; otherwise it dispatches per provider — `llama.cpp /tokenize`, `tiktoken` for OpenAI vocabularies, or a local `tokenizer.json` — and degrades to a language-aware estimate when none is available. For Anthropic and Gemini it first tries their native counting endpoints, though those only answer if the configured base URL exposes them.

### 7. Cascaded Streaming Voice Calls, TTS & ASR
- **Cascaded Voice Loop**: The browser captures PCM through an AudioWorklet and streams it over WebSocket. The backend transcribes incrementally every 2 seconds, sends the finalized utterance down the normal LLM path, then streams the reply back as TTS audio. Listening and speaking alternate around this ASR → LLM → TTS chain — it is not a single full-duplex model — with Silero VAD barge-in so you can cut a reply mid-sentence.
- **Bring Your Own Everything**: LLM, TTS, and ASR are each independently replaceable or self-hostable — local `llama.cpp` GGUF for chat, `audio.cpp` model families, any OpenAI-compatible HTTP endpoint, or cloud providers (MiniMax, ElevenLabs) for speech, with inline voice auditioning.

### 8. Picture Studio & Multimodal Attachments
- **File & Document Parsing**: Attach images, PDFs (`pypdf`), Word documents (`python-docx`), spreadsheets (`openpyxl`), and plain-text/code files directly in chat.
- **Video Attachments**: Send video clips (`.mp4`, `.mov`, `.mkv`, `.webm`, etc.) in single and group chats. Prefers local FFmpeg (auto-detected or user-configured in Backstage Paths, with browser `<canvas>` fallback) to extract a dense chronological frame stream (up to 180 frames at 2–4 fps) injected for the active turn only, with optional opt-in speech recognition (off by default, toggleable globally or per chip), click-to-mount throttled playback, and per-session duplicate filename filtering in the media gallery.
- **Scene Illustration & Gallery**: Generate scene pictures manually or via story triggers with prompt rewriting, daily quotas, cooldowns, and a unified gallery across single and group rooms.

### 9. Customizable Aesthetic
- **Day / Night** themes, **7 accent palettes** (Amber, Ember, Celadon, Moon, Plum, Jade, Rose), selectable typography, and instant **English / 中文** UI switching.

---

## 🧩 Supported Providers & Engines

| Capability | Local Engines / Protocols | Cloud / External Providers |
| :--- | :--- | :--- |
| **LLM Chat** | `llama.cpp` (`llama-server` with GGUF, `mmproj` vision & MTP), Ollama, LM Studio, any local OpenAI-compatible endpoint | OpenAI, ChatGPT, DeepSeek, Qwen, Grok, Xiaomi MiMo, Volcengine, Anthropic, Gemini — every provider is called through the OpenAI-compatible `/chat/completions` protocol with a bearer key, so Anthropic and Gemini need a base URL that speaks it (their own gateway or a compatible proxy) |
| **TTS (Voice)** | `audio.cpp` (OmniVoice, DotTTS, Fish Audio, Ming 3.0 & custom GGUF specs), OpenAI-compatible HTTP endpoint | MiniMax, ElevenLabs |
| **ASR (Ears)** | `audio.cpp` (built-in Qwen3-ASR, Confucius4-R2T2 & custom GGUF specs), custom OpenAI-compatible HTTP | OpenAI-compatible STT endpoints |
| **Picture Studio** | Local ComfyUI (with custom workflow JSON import) | SiliconFlow (Kolors), Zhipu (CogView-3-Flash), Cloudflare Workers AI, AI Horde, Gemini, ModelScope, Pollinations |

---

## 📁 Project Structure

```text
companionchat/
├── backend/                   # FastAPI backend
│   ├── main.py                # Standalone backend entrypoint (default port 8002)
│   ├── api_routes.py          # Core endpoints (companions, conversations, files, STT)
│   ├── api_routesV2.py        # Text chat streaming endpoints mounted onto api_routes
│   ├── paths.py               # Data root & model path resolution
│   ├── companion.py           # Chat orchestration & prompt assembly
│   ├── compaction.py          # Conversation summarization & compaction
│   ├── memory_engine.py       # Long-term memory extraction & retrieval
│   ├── world_book_engine.py   # Optional keyword-matching module (backend only, no UI)
│   ├── script_mode.py         # Script mode prompt builder & HUD state filter
│   ├── tavern_importer.py     # PNG / JSON character card importer
│   ├── tavern_exporter.py     # PNG / JSON character card exporter
│   ├── tts_service.py         # TTS engine routing & management
│   ├── stt_registry.py        # ASR engine registry & hot-switching
│   ├── llama_server_engine.py # llama.cpp local server lifecycle
│   ├── ws_call.py             # Real-time voice call WebSocket handler
│   ├── group_sessions/        # Group chat rooms (routes, memory, compaction, turns)
│   └── picturesys/            # Picture Studio (providers, ComfyUI, gallery store)
├── frontendV2/                # Active frontend (Vue 3 + TypeScript + Vite)
│   ├── src/
│   │   ├── components/        # Chat, GroupStage, BackstagePanel, CharacterEditor, Gallery, etc.
│   │   ├── stores/            # Pinia stores (session, chat, llm, tts, stt, call, pictures, script)
│   │   ├── api/               # REST & WebSocket clients
│   │   ├── i18n/              # Locale dictionaries (en.ts / zh.ts)
│   │   └── styles/            # Design tokens & stylesheets
│   └── src-tauri/             # Tauri 2 desktop wrapper & NSIS bundle config
├── docs/                      # Documentation & brand assets (including logo.svg)
├── scripts/                   # Maintenance scripts
├── requirements.txt           # Python dependencies
├── companion.bat              # Windows launcher for both backend and frontendV2
└── frontendv2.bat             # Windows launcher for frontendV2 dev server
```

---

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

Open `http://localhost:5176` in your browser and open **Backstage** to configure your LLM, Voice (TTS), Ears (ASR), Paths, and Pictures settings.

### 3. Desktop Build (Tauri 2)

With the Rust toolchain installed, run inside `frontendV2`:

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
