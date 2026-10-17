<p align="center">
  <img src="docs/assets/hero_banner.png" alt="Bird's Nest — 100% Local AI" width="600">
</p>

<h1 align="center">🪹 Bird's Nest</h1>

<h3 align="center">The First Local AI Manager for Non-Transformer Models</h3>

<p align="center">
  Run RWKV, Mamba, xLSTM, and StripedHyena locally on your Mac.<br>
  No cloud. No API keys. No transformers.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.11+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/platform-macOS-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/architecture-RNN%20%7C%20SSM%20%7C%20LSTM-purple.svg" alt="Architecture">
  <img src="https://img.shields.io/badge/100%25-Local-red.svg" alt="100% Local">
</p>

---

## Why Bird's Nest?

Every local AI tool — **Ollama**, **LM Studio**, **GPT4All** — is built for transformers. We built for **what comes next**.

| | Transformer Tools | Bird's Nest |
|---|---|---|
| **Architecture** | Attention-based (GPT, LLaMA, Mistral) | **RNN, SSM, LSTM** (RWKV, Mamba, xLSTM) |
| **Memory** | KV cache grows with context | **Constant memory** |
| **Scaling** | O(n²) attention | **O(1) per token** |
| **Context** | Fixed window (4K–128K) | **Infinite context** |
| **RAM for 7B** | 16GB+ recommended | **8GB capable** |

---

## Screenshots

<p align="center">
  <img src="docs/assets/screenshot_chat.png" alt="Chat Interface" width="800">
  <br><em>Chat with RWKV models — streaming responses at 11.5 tok/s</em>
</p>

<p align="center">
  <img src="docs/assets/screenshot_tools.png" alt="25+ Built-in Tools" width="800">
  <br><em>25+ tools your local AI can call — web search, image gen, music, YouTube, and more</em>
</p>

<p align="center">
  <img src="docs/assets/screenshot_models.png" alt="Model Library" width="800">
  <br><em>One-click model management — download, load, and switch between architectures</em>
</p>

<p align="center">
  <img src="docs/assets/screenshot_imagegen.png" alt="Image Generation" width="800">
  <br><em>On-device image generation — your RNN calls tools mid-conversation to create images locally</em>
</p>

---

## Features

### 🧠 Multi-Architecture AI Engine
Run **19 text models** across 4 non-transformer architectures — all from one app:

| Family | Models | Parameters | Architecture |
|--------|--------|-----------|--------------|
| **RWKV-7 GooseOne** | 7 variants | 0.1B – 13.3B | Linear Attention RNN |
| **RWKV-7 World** | 4 variants | 0.1B – 2.9B | Multilingual RNN |
| **RWKV-6 Finch** | 4 variants | 1.6B – 14B | Previous Gen RNN |
| **Mamba** | 2 variants | 1.4B – 2.8B | Selective State Space |
| **xLSTM** | 1 variant | 7B | Extended LSTM |
| **StripedHyena** | 1 variant | 7B | Hybrid Architecture |

### 🎨 Image Generation
**8 image models** with per-model quantization (Q4/Q8) and TeaCache acceleration:
- **SDXL Lightning** — 4-step instant generation
- **FLUX.2 Klein** — 4B and 9B variants
- **FLUX.1 Dev** — 12B with LoRA and ControlNet
- **Qwen Image 20B** — best prompt understanding
- **Z-Image Turbo** — photorealism specialist
- **FLUX.1 Kontext** — style transfer and editing
- **SeedVR2** — 1-step upscaler

### 🔧 25+ Built-in Tools
Your local RNN can **call tools mid-conversation** — no cloud APIs needed:

| Tool | Description |
|------|------------|
| 🔍 Web Search | DuckDuckGo search with inline results |
| 🖼️ Image Search | Find and display images |
| 📺 YouTube | Search and embed videos inline |
| 🌐 Fetch URL | Read and summarize web pages |
| 🎨 Image Gen | Generate images from text prompts |
| 🎵 Music Gen | Create music with Stable Audio / Riffusion |
| 🔄 Translate | 50+ language pairs |
| 📚 RAG | Search local documents |
| 🔢 Calculator | Math and conversions |
| 🌤️ Weather | Current conditions |
| 📝 Todos | Task management |
| 🐍 Python | Run code inline |
| 📁 File Search | Search local files |
| 🖥️ System | System monitoring |
| ...and more | Screenshot, Clipboard, Shell, Database, Upscale, Edit Image |

### 🎵 Music Generation
- **Stable Audio Open** — up to 47s of high-quality audio
- **Riffusion** — real-time music from text prompts

### 🔒 100% Local
- **Zero cloud dependencies** — everything runs on your machine
- **Zero telemetry** — no analytics, no tracking, no phone-home
- **Zero API keys** — download models from HuggingFace and go
- **Your data stays yours** — chat history, images, everything is local

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Dappit-io/birdsnest.git
cd birdsnest

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch Bird's Nest
python -m birdsnest.server
```

Open **http://localhost:7861** in your browser. That's it.

### First Run
1. Click any model in the **Model Library** panel
2. Click **Download** — models auto-download from HuggingFace
3. Once downloaded, click the model to **Load** it
4. Start chatting!

---

## System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| **OS** | macOS 12+ | macOS 14+ |
| **CPU** | Any (Intel/Apple Silicon) | Apple Silicon (M1+) |
| **RAM** | 8 GB | 32 GB |
| **Python** | 3.11 | 3.12+ |
| **Disk** | 5 GB (smallest model) | 50 GB (full catalog) |

> 💡 **Apple Silicon users** get Metal acceleration for image generation via MLX. Intel Macs work fine for text models.

---

## Architecture

```
Browser (localhost:7861)
    │
    ├── WebSocket /ws/chat ──► Streaming token generation
    │
    └── REST API
         ├── /api/models ──────► Model download, load, switch
         ├── /api/image-models ─► Image model management
         ├── /api/image-library ► Generated image gallery
         ├── /api/music-models ─► Music model management
         └── /api/tools ────────► Tool execution pipeline

Server (FastAPI + Uvicorn)
    │
    ├── engines/
    │    ├── rwkv_engine.py ───► RWKV v6 & v7 inference
    │    ├── mamba_engine.py ──► Mamba SSM inference
    │    └── hf_engine.py ────► xLSTM, StripedHyena (HuggingFace)
    │
    ├── image_engine.py ──────► mflux + diffusers (8 models)
    ├── tools.py ─────────────► 25+ built-in tool implementations
    ├── rag.py ───────────────► Local RAG with sentence embeddings
    └── models.py ────────────► Model catalog definitions
```

---

## Data Storage

| Data | Location |
|------|----------|
| Models | `~/birdsnest_models/` |
| Generated images | `~/birdsnest_workspace/images/` |
| Chat history | `~/birdsnest_workspace/.birdsnest_history.json` |
| Config | `~/birdsnest_workspace/.birdsnest_*` |

---

## Contributing

Pull requests welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, development setup, and how to add new models and tools.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

[MIT](LICENSE) — use it, fork it, build on it.

---

<p align="center">
  <strong>Built by <a href="https://dappit.io">Dappit</a></strong> — The First Web3 Vibe Coding Platform<br>
  <sub>Build, deploy, and ship decentralized apps with AI — no setup required.</sub><br><br>
  <a href="https://dappit.io">dappit.io</a> · <a href="https://github.com/Dappit-io">GitHub</a>
</p>
