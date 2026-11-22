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

### 3. Narration mode
- **Give the conversation a break**: One-click activation switch, supports all types of chats. In a voice-over manner, describe the behaviors, states (such as the user's actions, the character's actions, the space, and the psychology) of the user and the character, Guide the direction of the character's dialogue, and enable the user to control the process of the chat-playing.It only affects the content of the next reply and will not continuously contaminate the surrounding context.

### 4. Character Cards 
- **SillyTavern Ecosystem**: Import and export **PNG / JSON** character cards, with a built-in editor covering identity, dialogue fields (first message, conversation examples, advanced prompt), bound TTS voice clip/ID, system instructions, and raw JSON.
- **CHARX Containers & Bundled Assets**: Import and export **CHARX** (`.charx` / `.zip` and polyglot image+ZIP Character Card V3 packages) via streaming extraction and chunked transfer for large archives. Alongside card text and `alternate_greetings`, Pebble extracts CCv3 `data.assets` (`embeded://`, `embedded://`, `__asset:`, inline base64 data URLs), RisuAI `emotions` / `additionalAssets`, and bundled images, audio, and video into per-character storage manageable in the editor (world book / `character_book` entries and RisuAI display scripts are not imported).
- **Inline Media & Stage HUD**: Greetings and chat replies render sanitized Markdown/HTML and resolve bundled CHARX media inline — supporting `{{img::...}}`, `{{audio::...}}`, `{{bgm::...}}`, `{{video::...}}`, Markdown images, `<img src="...">`, `<video>`, and RisuAI `<img="...">` shorthand tags. For cards with bundled assets in single chat, an optional per-branch Stage HUD parses stripped `<<<STATE>>>` blocks to track mood, affection, location, and outfit while swapping stage portraits and cueing BGM/SFX automatically.
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
│   ├── api_routes.py          # Core endpoints (companions, chat, conversations, files, STT)
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
- **Local Inference (Optional)**: Configure your models root directory and `llama-server` executable under **Backstage → Paths** in the UI.

### 1. Install Dependencies

```bash
# Backend dependencies
pip install -r requirements.txt

# Frontend dependencies
cd frontendV2
npm install
```

### 2. Run in Development

#### Option A: Windows One-Click Launcher

Run the root batch script to start both the backend and frontend dev servers in separate terminals:

```bat
companion.bat
```

#### Option B: Manual Startup

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
