<p align="center"><img src="frontend/public/thrones.svg" width="56" alt=""></p>

<h1 align="center">Thrones</h1>

<p align="center">A private AI assistant that runs on your own PC.<br>
Open-weight models, real reasoning tools, cited web research and document Q&amp;A, in one calm interface.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue"></a>
  <img alt="Platform: Windows 10/11" src="https://img.shields.io/badge/platform-Windows%2010%2F11-informational">
  <img alt="Runs offline" src="https://img.shields.io/badge/runs-100%25%20local-success">
  <a href="https://github.com/techgptoffical/thrones/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/techgptoffical/thrones/actions/workflows/ci.yml/badge.svg"></a>
</p>

<p align="center"><img src="docs/images/chat-think-dark.png" width="860" alt="Thrones answering a loan EMI question in Think mode, with every figure computed by a calculator"></p>

---

**Thrones 1.0** is application software by TECH GPT. The language model it runs is **not** a Thrones model: by default it is **Qwen3.5 9B** by Alibaba Cloud's Qwen team (Apache-2.0), unmodified, in a community Q4_K_M quantization, executed locally by **llama.cpp**. Thrones' own trained weights are **Thrones Adapter 0.2**, a small LoRA fine-tune (61 MB) on Qwen3.5 4B: it uses the calculator reliably (also on question types it never trained on) and writes cleaner Hinglish, while general maths and code stay within noise of the base model — see its [model card](training/runs/thrones-adapter-0.2/MODEL_CARD.md). It is optional and marked Experimental; it is not a model trained from scratch. (Adapter 0.1 was withdrawn after it was found to reduce maths accuracy.)

## What it does

| | |
|---|---|
| **Chat, fully offline** | Streaming answers from a local model. Works with the network cable unplugged. No account, no telemetry. |
| **Fast / Think / Deep Research** | Three modes that change what the backend actually does. *Think* plans, solves with thinking enabled, checks arithmetic with a real calculator, then has an independent pass verify the answer and fix it if wrong. *Deep Research* searches the web, reads several pages, and writes a report whose every citation points to a page it actually fetched. |
| **Your documents** | Attach text, code, CSV, JSON, PDF or DOCX. They are indexed locally (SQLite FTS5) and quoted to the model with file and page references. |
| **Memory you control** | Save facts across chats; see, edit, disable, delete or export every one. |
| **Hindi, English, Hinglish** | Answers in the language and script you write in. |
| **Honest numbers** | Every reply carries its measured speed, latency, token counts and peak memory. |
| **Hardware-aware** | Detects your GPU/RAM, picks a profile (Lite / Balanced / High), falls back to smaller context or CPU if a load fails, unloads when idle. |

## Measured on the reference PC

RTX 5060 Ti 16 GB · Core i3-10105F · 16 GB RAM · Windows 11 · llama.cpp b12289 · 16k context. Full method and results: [`docs/MODEL_RESEARCH.md`](docs/MODEL_RESEARCH.md).

| Model | Speed | VRAM | System RAM | Hard questions (26) | Profile |
|---|---|---|---|---|---|
| **Qwen3.5 9B** Q4_K_M (default) | 50 tok/s | 5.8 GB | ~5.3 GB | 24 | High |
| Qwen3.5 4B Q4_K_M | 98 tok/s | 3.5 GB | — | 21 | Balanced |
| Thrones Adapter 0.2 (Qwen3.5 4B + LoRA) | 66 tok/s (in app) | 3.6 GB | — | 22 | Balanced, experimental |
| Qwen3.5 2B Q4_K_M | 164 tok/s | 1.6 GB | — | 19 | Lite |
| gpt-oss 20B MXFP4 (optional) | 100 tok/s | 11.7 GB | ~12 GB | 25 | needs 24 GB+ RAM |

Hard questions = our own 26-item maths / logic / code / format / Hindi set, greedy decoding, model alone. Through the app the 9B scores 23–24 in Fast and 24 in Think (Think adds checked, visible working, not extra points on this set).

## Install (Windows 10/11)

**You need:** Windows 10 or 11, [Python 3.11+](https://www.python.org/downloads/) (tick *"Add python.exe to PATH"* during install), about 10 GB of free disk space, and ideally an NVIDIA graphics card with 8 GB+ of VRAM. Without a suitable GPU, Thrones still runs on the CPU with the small Lite model, just more slowly.

### Easy install (recommended)

1. Download **`Thrones-v1.0.0-windows.zip`** from the [latest release](https://github.com/techgptoffical/thrones/releases/latest) and unzip it, for example to `C:\Thrones` or `D:\Thrones`.
2. Double-click **`Setup.bat`**. It installs everything inside that folder only (nothing system-wide) and tells you when it is done. It downloads about 600 MB, so it takes roughly 10–25 minutes depending on your internet speed.
3. Double-click **`Thrones.bat`**. Your browser opens at `http://127.0.0.1:8765`.
4. Go to **Settings → Models & hardware**, press **Download** on the model marked as recommended for your PC, and start chatting.

Closing the black Thrones window stops everything and frees the GPU.

### From source (developers)

```powershell
git clone https://github.com/techgptoffical/thrones.git Thrones
cd Thrones
powershell -ExecutionPolicy Bypass -File scripts\setup.ps1      # add -Cpu on PCs without an NVIDIA GPU
```

Building from source also needs [Node.js 20+](https://nodejs.org/) for the interface. See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow.

## Screenshots

| Welcome | Deep Research with real, dated sources |
|---|---|
| <img src="docs/images/welcome-light.png" alt="Thrones welcome screen, light theme"> | <img src="docs/images/research-dark.png" alt="A Deep Research report with six cited sources and their publication dates"> |

## Privacy

Conversations, memories, documents and settings live in `data\` on your PC. Thrones contacts the internet only when you run **Deep Research** (search queries + the pages it reads) or **download a model**. **Offline mode** blocks both. Details: [`SECURITY.md`](SECURITY.md).

## Limits — please read

- A 2–9B local model is far smaller than frontier cloud assistants. It makes more factual and reasoning errors and knows nothing after its training data. Think mode and Deep Research reduce some errors with tools and sources; they do not make the model smarter, and they do not change its weights.
- Deep Research uses DuckDuckGo through an unofficial library by default. It can be rate-limited; Brave API or your own SearXNG are supported alternatives.
- The optional Python tool is **not a sandbox** and is off by default.
- Images, voice, and external MCP tools are not supported in 1.0.
- There is no installer yet; setup uses the PowerShell script above.

Status of every feature, including what is not done: [`docs/PROGRESS.md`](docs/PROGRESS.md).

## Project documents

[Architecture](docs/ARCHITECTURE.md) · [Model research](docs/MODEL_RESEARCH.md) · [Implementation plan](docs/IMPLEMENTATION_PLAN.md) · [Training plan](docs/TRAINING_PLAN.md) · [Training pipeline](training/README.md) · [UI design spec](docs/UI_DESIGN_SPEC.md) · [Test plan](docs/TEST_PLAN.md) · [Progress](docs/PROGRESS.md) · [Security](SECURITY.md) · [Contributing](CONTRIBUTING.md)

## Licence

Thrones application code: [MIT](LICENSE). Models, the llama.cpp runtime, fonts and libraries keep their own licences: [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
