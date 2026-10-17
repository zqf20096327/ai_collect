<p align="center">
  <img src="assets/banner.png" alt="Awesome Mac mini Home Server - Turn an Apple Silicon Mac mini into a 24/7 agentic AI home server" width="100%">
</p>

<h1 align="center">Awesome Mac mini Home Server</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/momenbasel/awesome-mac-mini-homeserver"><img src="https://img.shields.io/github/stars/momenbasel/awesome-mac-mini-homeserver?style=flat&logo=github&color=yellow" alt="Stars"></a>
  <a href="https://github.com/momenbasel/awesome-mac-mini-homeserver/network/members"><img src="https://img.shields.io/github/forks/momenbasel/awesome-mac-mini-homeserver?style=flat&logo=github&color=blue" alt="Forks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg?style=flat" alt="License"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat" alt="PRs Welcome"></a>
  <a href="https://momenbasel.github.io/awesome-mac-mini-homeserver/"><img src="https://img.shields.io/badge/website-live-22d3ee?style=flat&logo=github" alt="Website"></a>
</p>

<p align="center"><strong>A curated list of tools, guides, and projects for running an Apple Silicon Mac mini as a 24/7 home server, with agentic AI as the headline focus.</strong></p>

<p align="center">
  <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fmomenbasel%2Fawesome-mac-mini-homeserver&text=Turn%20your%20Mac%20mini%20into%20a%2024%2F7%20agentic%20AI%20home%20server.%20400%2B%20curated%20tools%2C%20one-command%20installer.&hashtags=MacMini%2CSelfHosted%2CLocalLLM%2CAgenticAI">
    <img alt="Share on Twitter" src="https://img.shields.io/badge/Share_on-Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white">
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2Fmomenbasel%2Fawesome-mac-mini-homeserver">
    <img alt="Share on LinkedIn" src="https://img.shields.io/badge/Share_on-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
  <a href="https://www.reddit.com/submit?url=https%3A%2F%2Fgithub.com%2Fmomenbasel%2Fawesome-mac-mini-homeserver&title=Awesome%20Mac%20mini%20Home%20Server%20-%20400%2B%20curated%20tools%20for%20agentic%20AI%20on%20Apple%20Silicon">
    <img alt="Share on Reddit" src="https://img.shields.io/badge/Share_on-Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white">
  </a>
  <a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2Fmomenbasel%2Fawesome-mac-mini-homeserver&t=Awesome%20Mac%20mini%20Home%20Server">
    <img alt="Share on Hacker News" src="https://img.shields.io/badge/Share_on-HN-FF6600?style=for-the-badge&logo=ycombinator&logoColor=white">
  </a>
  <a href="https://github.com/momenbasel/awesome-mac-mini-homeserver/discussions">
    <img alt="Join Discussions" src="https://img.shields.io/badge/Join-Discussions-0969DA?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>

<p align="center">
  <em>If this list saves you time, please <a href="https://github.com/momenbasel/awesome-mac-mini-homeserver">star the repo</a> - it genuinely helps other Mac mini owners discover it.</em>
</p>

## What is this, in plain English?

You buy a Mac mini. You stick it in a closet. It quietly runs, forever, doing useful things for you:

- **Your personal AI.** It runs ChatGPT-style assistants locally, so your prompts never leave your home.
- **Your photo library.** Like iCloud, but you own it.
- **Your password vault.** Like 1Password, but you own it.
- **Your media server.** Like Netflix, with your own shows.
- **Your smart home brain.** Home Assistant, HomeKit, Matter - all in one place.
- **Your personal automation.** Tell it "every morning at 8am, read my emails and summarize them" - it does that.

This list is the map. It tells you **which tools are good**, **what they do**, and gives you a **one-command installer** to get started.

If a tag like `[D]` confuses you, check the [Legend](#legend). If you just want to get going, jump to [Quick Start](#quick-start).

<div align="center">

**[Agentic AI](#agentic-ai)**  ·  **[Self-Hosted Apps](#self-hosted-apps)**  ·  **[Media Servers](#media-servers)**  ·  **[Smart Home](#smart-home)**  ·  **[Quick Start](#quick-start)**

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Lint](https://github.com/momenbasel/awesome-mac-mini-homeserver/actions/workflows/lint.yml/badge.svg)](https://github.com/momenbasel/awesome-mac-mini-homeserver/actions/workflows/lint.yml)
[![Last Commit](https://img.shields.io/github/last-commit/momenbasel/awesome-mac-mini-homeserver)](https://github.com/momenbasel/awesome-mac-mini-homeserver/commits/main)

</div>

---

## Why a Mac mini?

Apple Silicon Mac mini is the highest performance-per-watt home server you can buy. Unified memory, Metal and ANE acceleration, silent fans, and native macOS daemons make it the ideal always-on host for local agents, self-hosted services, and home automation.

| Metric | Mac mini M4 | Typical x86 SFF |
|---|---|---|
| Idle power | 4-7 W | 15-35 W |
| Peak power | 65 W | 120-200 W |
| Unified memory ceiling | 64 GB | 64-128 GB (discrete, slow GPU path) |
| LLM inference (70B Q4) | Runs on 64 GB tier | Needs dedicated GPU |
| Fan noise at idle | Inaudible | Audible |
| Form factor | 5 x 5 x 2 in | Typically 8+ in |
| Built-in server daemons | SMB, AFP, HomeKit, Time Machine, AirPlay | None |

---

## Architecture at a glance

```mermaid
flowchart LR
    subgraph Mini["Mac mini (24/7 host)"]
        direction TB
        O[Ollama / MLX / llama.cpp]
        C[Claude Code / Aider]
        MCP[MCP servers]
        L[launchd + cron]
        D[Docker / OrbStack]
        HA[Home Assistant]
        TM[Time Machine server]
        O --> C
        C --> MCP
        L --> C
        D --> HA
    end
    Phone[iPhone / iPad] -->|Shortcuts| L
    Chat[Telegram / Slack] -->|Bridge| C
    Macs[Other Macs] -->|Tailscale| Mini
    Mini -->|HomeKit| IoT[IoT devices]
    Mini -->|SMB| NAS[External storage]
```

---

## Quick Start

Install a curated stack with the included CLI. Pick Agentic AI, Media Server, or Self-Hosted Productivity:

```bash
curl -fsSL https://raw.githubusercontent.com/momenbasel/awesome-mac-mini-homeserver/main/install.sh -o install.sh
chmod +x install.sh
./install.sh
```

Review [`install.sh`](install.sh) before running. Idempotent: safe to re-run. See [docs/agentic-quickstart.md](docs/agentic-quickstart.md) for the opinionated agentic build.

### See it in action

<p align="center">
  <img src="assets/screenshots/01-menu.png" alt="install.sh main menu - Apple Silicon detected, Homebrew confirmed, three numbered stack options (Agentic AI, Media Server, Self-Hosted Apps)" width="820">
  <br><em>Pick a stack. One command. Idempotent.</em>
</p>

<p align="center">
  <img src="assets/screenshots/02-agentic-running.png" alt="install.sh running the Agentic AI stack - Homebrew installs Ollama, Whisper.cpp, LM Studio, Jan, Msty, then pipx installs Aider, pulls llama3.2:3b model, and docker-compose spins up Open WebUI + Langfuse" width="820">
  <br><em>Running <code>./install.sh agentic</code> - brew + pipx + ollama pull + docker compose, all handled.</em>
</p>

<p align="center">
  <img src="assets/screenshots/03-done.png" alt="install.sh completion screen - lists reachable URLs for Ollama, Open WebUI, Langfuse, and reminder commands for Claude Code and Aider" width="820">
  <br><em>Done - your agents are live at these URLs.</em>
</p>

Non-interactive: `./install.sh agentic` / `media` / `selfhosted` / `all`.

### Time Machine server for the whole household

Turn the mini's external drive into a shared Time Machine destination every Mac on the LAN can back up to:

```bash
sudo ./scripts/time-machine-server.sh /Volumes/YourExternalDrive
```

One command. APFS/HFS+ aware. SMB + Bonjour discovery. Optional per-Mac quota via `QUOTA_GB=500`.

### Stack components at a glance

**Agentic AI**
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Claude](https://img.shields.io/badge/Claude_Code-D97706?style=for-the-badge&logo=anthropic&logoColor=white)
![OpenWebUI](https://img.shields.io/badge/Open_WebUI-000000?style=for-the-badge&logo=openai&logoColor=white)
![Langfuse](https://img.shields.io/badge/Langfuse-0A0A0A?style=for-the-badge)
![Whisper](https://img.shields.io/badge/whisper.cpp-412991?style=for-the-badge&logo=openai&logoColor=white)

**Media Server**
![Jellyfin](https://img.shields.io/badge/Jellyfin-00A4DC?style=for-the-badge&logo=jellyfin&logoColor=white)
![Sonarr](https://img.shields.io/badge/Sonarr-2596BE?style=for-the-badge)
![Radarr](https://img.shields.io/badge/Radarr-FFCA28?style=for-the-badge)
![Prowlarr](https://img.shields.io/badge/Prowlarr-E37100?style=for-the-badge)
![qBittorrent](https://img.shields.io/badge/qBittorrent-2F67BA?style=for-the-badge&logo=qbittorrent&logoColor=white)

**Self-Hosted Apps**
![Vaultwarden](https://img.shields.io/badge/Vaultwarden-175DDC?style=for-the-badge&logo=bitwarden&logoColor=white)
![Paperless](https://img.shields.io/badge/Paperless-17541F?style=for-the-badge)
![Gitea](https://img.shields.io/badge/Gitea-609926?style=for-the-badge&logo=gitea&logoColor=white)
![Homepage](https://img.shields.io/badge/Homepage-0F172A?style=for-the-badge)

---

## Legend

Each entry carries one or more badges so you can see at a glance what it runs on and how it ships.

| Badge | Meaning |
|---|---|
| ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) | Runs only on Apple Silicon (M1/M2/M3/M4). Not compatible with Intel Macs. |
| ![Intel](https://img.shields.io/badge/Intel-0071C5?style=flat-square&logo=intel&logoColor=white) | Intel Mac only. |
| ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) | Universal binary - works on both Apple Silicon and Intel. |
| ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) | Ships as a native macOS app or CLI (Homebrew, `.app`, or signed binary). |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) | Runs in a Docker container (use OrbStack, Colima, or Docker Desktop). |
| ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square) | Paid or freemium - free tier may exist but full use often needs a license. |

---

## Contents

- [Agentic AI](#agentic-ai)
  - [Apple Silicon optimized (MLX / CoreML / ANE)](#apple-silicon-optimized-mlx--coreml--ane)
  - [Local LLM runtimes](#local-llm-runtimes)
  - [Agentic frameworks](#agentic-frameworks)
  - [Coding agents and AI IDEs](#coding-agents-and-ai-ides)
  - [Agent sandboxes](#agent-sandboxes)
  - [MCP servers](#mcp-servers)
  - [Agent gateways and LLMOps](#agent-gateways-and-llmops)
  - [Tool and integration platforms](#tool-and-integration-platforms)
  - [Document ingestion](#document-ingestion)
  - [Agent memory and RAG](#agent-memory-and-rag)
  - [Vector databases](#vector-databases)
  - [Browser and computer-use agents](#browser-and-computer-use-agents)
  - [Voice and multimodal agents](#voice-and-multimodal-agents)
  - [Agent UIs](#agent-uis)
  - [Orchestration and eventing](#orchestration-and-eventing)
  - [Observability](#observability)
  - [Image and video agents](#image-and-video-agents)
  - [Agent bridges](#agent-bridges)
- [Hardware](#hardware)
- [OS and base setup](#os-and-base-setup)
- [Remote access](#remote-access)
- [Containers and virtualization](#containers-and-virtualization)
- [Media servers](#media-servers)
- [Storage and NAS](#storage-and-nas)
- [Self-hosted apps](#self-hosted-apps)
- [Smart home](#smart-home)
- [Ad blocking and DNS](#ad-blocking-and-dns)
- [Reverse proxy and TLS](#reverse-proxy-and-tls)
- [Monitoring and observability](#monitoring-and-observability)
- [Automation and scheduling](#automation-and-scheduling)
- [Development environments](#development-environments)
- [Backup](#backup)
- [Security](#security)
- [Audio and AirPlay](#audio-and-airplay)
- [Game streaming](#game-streaming)
- [Torrents, Usenet, and archiving](#torrents-usenet-and-archiving)
- [Photo and video](#photo-and-video)
- [Databases](#databases)
- [Dashboards](#dashboards)
- [Power and thermals](#power-and-thermals)
- [Bootstrap and dotfiles](#bootstrap-and-dotfiles)
- [CI/CD and build farms](#cicd-and-build-farms)
- [Networking](#networking)
- [Sleep, wake, and persistence](#sleep-wake-and-persistence)
- [CLI power tools](#cli-power-tools)
- [File transfer](#file-transfer)
- [Reference lists](#reference-lists)
- [Contributing](#contributing)

---

## Agentic AI ![](https://img.shields.io/badge/_-AGENTIC-22d3ee?style=flat-square&logo=openai&logoColor=white)
Mac mini is the ideal 24/7 host for local agents. Unified memory runs large models natively. Metal accelerates inference. `launchd` turns any script into an always-on worker. See [docs/ram-sizing-llm.md](docs/ram-sizing-llm.md) for model sizing per memory tier.

### Apple Silicon optimized (MLX / CoreML / ANE)

Tools that exploit the Mac mini's unique hardware - Neural Engine, Metal Performance Shaders, and unified memory - for the fastest or lowest-power inference possible.

- [CoreML Tools](https://github.com/apple/coremltools) - Convert PyTorch, TensorFlow, and ONNX models to CoreML for ANE and Metal execution. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/apple/coremltools?style=social&label=)
- [DiffusionKit](https://github.com/argmaxinc/DiffusionKit) - Argmax's on-device Stable Diffusion with MLX and CoreML. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/argmaxinc/DiffusionKit?style=social&label=)
- [exo](https://github.com/exo-explore/exo) - Run a unified LLM cluster across multiple Apple devices at home. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/exo-explore/exo?style=social&label=)
- [FastMLX](https://github.com/Blaizzy/fastmlx) - OpenAI-compatible high-performance server for MLX models. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/Blaizzy/fastmlx?style=social&label=)
- [llamafile](https://github.com/Mozilla-Ocho/llamafile) - Single-binary LLM distribution with Apple Silicon acceleration. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/Mozilla-Ocho/llamafile?style=social&label=)
- [ml-ane-transformers](https://github.com/apple/ml-ane-transformers) - Apple's reference transformer implementation optimized for the Neural Engine. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/apple/ml-ane-transformers?style=social&label=)
- [MLX](https://github.com/ml-explore/mlx) - Apple's array framework for Apple Silicon unified memory. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/ml-explore/mlx?style=social&label=)
- [MLX-Audio](https://github.com/Blaizzy/mlx-audio) - TTS, STT, and speech-to-speech for MLX. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/Blaizzy/mlx-audio?style=social&label=)
- [MLX-LM](https://github.com/ml-explore/mlx-lm) - Run Llama, Mistral, Qwen, Phi via MLX with 4 and 8-bit quantization. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/ml-explore/mlx-lm?style=social&label=)
- [mlx-vlm](https://github.com/Blaizzy/mlx-vlm) - Vision-language models on MLX (LLaVA, Qwen-VL, Pixtral). ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/Blaizzy/mlx-vlm?style=social&label=)
- [mlx-whisper](https://pypi.org/project/mlx-whisper/) - OpenAI Whisper ported to MLX for Apple Silicon native speed. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [swift-transformers](https://github.com/huggingface/swift-transformers) - Hugging Face Swift library for CoreML model inference. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/huggingface/swift-transformers?style=social&label=)
- [WhisperKit](https://github.com/argmaxinc/WhisperKit) - Argmax's CoreML-optimized Whisper with ANE acceleration. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/argmaxinc/WhisperKit?style=social&label=)

### Local LLM runtimes

- [GPUStack](https://github.com/gpustack/gpustack) - GPU cluster manager that auto-configures vLLM and SGLang workers across heterogeneous nodes. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/gpustack/gpustack?style=social&label=)
- [Jan](https://jan.ai) - Offline local AI chat with a polished native UI. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [llama-swap](https://github.com/mostlygeek/llama-swap) - Go proxy that hot-swaps llama.cpp or any OpenAI-compatible backend on demand. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/mostlygeek/llama-swap?style=social&label=)
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - C/C++ inference engine with first-class Metal backend. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=social&label=)
- [LM Studio](https://lmstudio.ai) - GUI for GGUF models with an OpenAI-compatible headless server. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [LocalAI](https://github.com/mudler/LocalAI) - OpenAI-compatible drop-in API for local models. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/mudler/LocalAI?style=social&label=)
- [Ollama](https://ollama.com) - One-command local LLM server, Metal-accelerated by default. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [SGLang](https://github.com/sgl-project/sglang) - High-performance serving framework with structured-output and radix-cache scheduling. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/sgl-project/sglang?style=social&label=)
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput inference server, runs via Docker on Apple Silicon. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/vllm-project/vllm?style=social&label=)

### Agentic frameworks

- [AgentScope](https://github.com/modelscope/agentscope) - Production-oriented multi-agent framework from Alibaba with built-in tool, memory, and voice abstractions. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/modelscope/agentscope?style=social&label=)
- [Agno](https://github.com/agno-agi/agno) - Python runtime and AgentOS control plane for building, deploying, and operating agentic systems at scale. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/agno-agi/agno?style=social&label=)
- [Aider](https://aider.chat) - Terminal-native AI pair programmer with git-aware edits. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent conversation framework from Microsoft. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/microsoft/autogen?style=social&label=)
- [Claude Code](https://docs.claude.com/en/docs/claude-code) - Anthropic's terminal coding agent, scriptable via stdin and launchd. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [Cline](https://cline.bot) - Autonomous coding agent for VS Code. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Continue](https://continue.dev) - Open-source AI code assistant for IDEs. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [CrewAI](https://www.crewai.com) - Role-based multi-agent orchestration framework. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [DSPy](https://github.com/stanfordnlp/dspy) - Stanford framework for programming (not prompting) LMs via compiled modules and optimizers. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/stanfordnlp/dspy?style=social&label=)
- [Fabric](https://github.com/danielmiessler/fabric) - Go CLI that applies reusable AI patterns to stdin for summarization, code review, and research. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/danielmiessler/fabric?style=social&label=)
- [Goose](https://block.github.io/goose/) - Open-source on-machine AI agent by Block. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [Inngest AgentKit](https://github.com/inngest/agent-kit) - TypeScript toolkit for building multi-agent networks on Inngest's durable runtime. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/inngest/agent-kit?style=social&label=)
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful multi-actor agent graphs. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social&label=)
- [Mastra](https://github.com/mastra-ai/mastra) - TypeScript agent framework with workflows, RAG, and evals for shipping production agents. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/mastra-ai/mastra?style=social&label=)
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) - Python framework for composing agents purely out of MCP servers. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social&label=)
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Enterprise successor to AutoGen with Python and .NET SDKs for multi-agent workflows. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/microsoft/agent-framework?style=social&label=)
- [Open Interpreter](https://www.openinterpreter.com) - Natural language interface that executes code locally. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Lightweight multi-agent orchestration SDK that succeeds Swarm, works with any OpenAI-compatible provider. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/openai/openai-agents-python?style=social&label=)
- [OpenClaw](https://github.com/openclaw/openclaw) - Open-source always-on personal AI assistant controllable via WhatsApp, Telegram, Discord, and Slack with persistent memory and 50+ integrations. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/openclaw/openclaw?style=social&label=)
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Autonomous software engineer agent platform. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=social&label=)
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe Python agent framework from the Pydantic team. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social&label=)
- [smolagents](https://github.com/huggingface/smolagents) - Minimal agent library from Hugging Face. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/huggingface/smolagents?style=social&label=)
- [VoltAgent](https://github.com/VoltAgent/voltagent) - TypeScript agent-engineering framework with optional cloud console for observability. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square) ![⭐](https://img.shields.io/github/stars/VoltAgent/voltagent?style=social&label=)

### Coding agents and AI IDEs

- [Bolt.diy](https://github.com/stackblitz-labs/bolt.diy) - Community fork of StackBlitz Bolt for full-stack web app generation against any LLM. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/stackblitz-labs/bolt.diy?style=social&label=)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) - Anthropic SDK for building custom agents on top of Claude Code with hooks and custom tools. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/anthropics/claude-agent-sdk-python?style=social&label=)
- [Crush](https://github.com/charmbracelet/crush) - Charm's multi-model terminal coding agent with LSP and MCP support. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/charmbracelet/crush?style=social&label=)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Open-source Google agent that brings Gemini or local models into the terminal with extensible tools. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=social&label=)
- [Kilo Code](https://github.com/Kilo-Org/kilocode) - All-in-one agentic engineering platform available as VS Code extension and CLI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/Kilo-Org/kilocode?style=social&label=)
- [OpenAI Codex CLI](https://github.com/openai/codex) - Lightweight terminal coding agent from OpenAI, works with local OpenAI-compatible endpoints. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/openai/codex?style=social&label=)
- [OpenCode](https://github.com/anomalyco/opencode) - Provider-agnostic open-source terminal coding agent with a client/server core you can drive remotely. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/anomalyco/opencode?style=social&label=)
- [Roo Code](https://github.com/RooCodeInc/Roo-Code) - VS Code extension with autonomous architect, code, debug, and custom agent modes. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/RooCodeInc/Roo-Code?style=social&label=)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Princeton/Stanford framework for LM agents that autonomously fix GitHub issues. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=social&label=)
- [Void](https://github.com/voideditor/void) - Open-source Cursor alternative built on VS Code with agentic editing and any-model support. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/voideditor/void?style=social&label=)
- [Zed](https://github.com/zed-industries/zed) - High-performance native macOS editor with first-class agent panel, MCP, and Metal-accelerated UI. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/zed-industries/zed?style=social&label=)

### Agent sandboxes

- [Daytona](https://github.com/daytonaio/daytona) - Elastic runtime that spins up isolated dev-container sandboxes for agent code execution. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/daytonaio/daytona?style=social&label=)
- [E2B](https://github.com/e2b-dev/E2B) - Open-source secure cloud sandboxes for running AI-generated code, self-hostable. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/e2b-dev/E2B?style=social&label=)

### MCP servers

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - Community-curated catalog of MCP servers, the canonical discovery index. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=social&label=)
- [FastMCP](https://github.com/jlowin/fastmcp) - Pythonic framework for building MCP servers and clients with auto-generated schemas. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/jlowin/fastmcp?style=social&label=)
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - GitHub's official MCP server for repos, issues, PRs, and Actions. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/github/github-mcp-server?style=social&label=)
- [GitMCP](https://github.com/idosal/git-mcp) - Remote MCP server that grounds assistants in any public GitHub repo's docs and code. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/idosal/git-mcp?style=social&label=)
- [Glama MCP Registry](https://glama.ai/mcp/servers) - Directory of 20k+ MCP servers filterable by language, transport, and category. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [MCP Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - Official filesystem MCP server. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social&label=)
- [MCP reference servers](https://github.com/modelcontextprotocol/servers) - Official reference implementations (filesystem, git, fetch, memory, sequential-thinking). ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=social&label=)
- [mcp.run](https://www.mcp.run) - Registry and runtime for portable MCP servlets. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - Browser automation for agents via structured accessibility snapshots. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/microsoft/playwright-mcp?style=social&label=)
- [Smithery](https://smithery.ai) - Largest open marketplace of MCP servers with one-command install into MCP clients. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Toolhive](https://github.com/stacklok/toolhive) - Secure MCP server manager. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/stacklok/toolhive?style=social&label=)

### Agent gateways and LLMOps

- [LiteLLM](https://github.com/BerriAI/litellm) - Unified OpenAI-compatible gateway and Python SDK fronting 100+ providers and local engines. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/BerriAI/litellm?style=social&label=)
- [OpenLLM](https://github.com/bentoml/OpenLLM) - BentoML project for serving open-source LLMs behind an OpenAI-compatible API. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/bentoml/OpenLLM?style=social&label=)
- [Portkey AI Gateway](https://github.com/Portkey-AI/gateway) - High-performance edge gateway that routes to 200+ LLMs with guardrails and fallbacks. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social&label=)
- [promptfoo](https://github.com/promptfoo/promptfoo) - CLI and library for evaluating and red-teaming LLM apps with side-by-side comparisons. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social&label=)
- [TensorZero](https://github.com/tensorzero/tensorzero) - Rust-based LLMOps stack unifying gateway, observability, evals, and optimization. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/tensorzero/tensorzero?style=social&label=)
- [Weave](https://github.com/wandb/weave) - W&B's developer toolkit for tracing, evaluating, and debugging GenAI applications. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square) ![⭐](https://img.shields.io/github/stars/wandb/weave?style=social&label=)

### Tool and integration platforms

- [Composio](https://github.com/ComposioHQ/composio) - SDK providing 1000+ authenticated tool integrations and a sandboxed workbench for any agent framework. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square) ![⭐](https://img.shields.io/github/stars/ComposioHQ/composio?style=social&label=)

### Document ingestion

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Open-source web crawler and scraper that emits LLM-ready Markdown for RAG. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social&label=)
- [Docling](https://github.com/docling-project/docling) - IBM-led document processor that converts PDFs, DOCX, PPTX, and images into structured layouts. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/docling-project/docling?style=social&label=)
- [MarkItDown](https://github.com/microsoft/markitdown) - Microsoft utility that converts arbitrary files to clean Markdown for LLM pipelines. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/microsoft/markitdown?style=social&label=)
- [Scrapling](https://github.com/D4Vinci/Scrapling) - Adaptive Python web scraping framework with stealth, anti-bot bypass, and full-crawl support. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/D4Vinci/Scrapling?style=social&label=)

### Agent memory and RAG

- [Cognee](https://github.com/topoteretes/cognee) - Knowledge engine giving agents persistent memory via combined vector and graph stores. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/topoteretes/cognee?style=social&label=)
- [Graphiti](https://github.com/getzep/graphiti) - Temporal knowledge-graph framework for tracking how facts change over time with provenance. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/getzep/graphiti?style=social&label=)
- [Kotaemon](https://github.com/Cinnamon/kotaemon) - Open-source document-chat UI with advanced citation and multi-modal retrieval. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/Cinnamon/kotaemon?style=social&label=)
- [LangChain](https://github.com/langchain-ai/langchain) - LLM application framework. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/langchain-ai/langchain?style=social&label=)
- [Letta](https://github.com/letta-ai/letta) - Stateful agents with long-term memory, formerly MemGPT. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/letta-ai/letta?style=social&label=)
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for LLM applications. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/run-llama/llama_index?style=social&label=)
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI agents. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/mem0ai/mem0?style=social&label=)
- [Onyx](https://github.com/onyx-dot-app/onyx) - Self-hostable enterprise chat with agentic RAG, web search, and code execution over your data. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/onyx-dot-app/onyx?style=social&label=)
- [PaperQA](https://github.com/Future-House/paper-qa) - High-accuracy agentic RAG for scientific PDFs with iterative search and in-text citations. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/Future-House/paper-qa?style=social&label=)
- [RAGFlow](https://github.com/infiniflow/ragflow) - RAG engine with deep document parsing, intelligent chunking, and grounded citations. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/infiniflow/ragflow?style=social&label=)
- [Zep](https://www.getzep.com) - Long-term memory for AI agents. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Vector databases

- [Chroma](https://www.trychroma.com) - Open-source embedding database. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [LanceDB](https://lancedb.github.io/lancedb/) - Serverless vector database with native Metal support. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [pgvector](https://github.com/pgvector/pgvector) - Vector similarity search extension for Postgres. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/pgvector/pgvector?style=social&label=)
- [Qdrant](https://qdrant.tech) - Vector search engine with Docker support on Apple Silicon. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Weaviate](https://weaviate.io) - Open-source vector database with hybrid search. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Browser and computer-use agents

- [Anthropic Computer Use](https://docs.claude.com/en/docs/build-with-claude/computer-use) - Claude API for controlling the desktop. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [browser-use](https://github.com/browser-use/browser-use) - Make websites accessible for AI agents. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/browser-use/browser-use?style=social&label=)
- [Camoufox](https://github.com/daijro/camoufox) - Stealth Firefox fork for undetected automation. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/daijro/camoufox?style=social&label=)
- [OmniParser](https://github.com/microsoft/OmniParser) - Screen parsing for GUI agents. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/microsoft/OmniParser?style=social&label=)
- [Playwright](https://playwright.dev) - Cross-browser automation library. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [Skyvern](https://github.com/Skyvern-AI/skyvern) - Automate browser workflows with LLMs. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/Skyvern-AI/skyvern?style=social&label=)
- [Stagehand](https://github.com/browserbase/stagehand) - AI web browsing framework. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/browserbase/stagehand?style=social&label=)

### Voice and multimodal agents

- [Dia](https://github.com/nari-labs/dia) - 1.6B dialogue TTS with speaker control and emotion conditioning for multi-voice scenes. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/nari-labs/dia?style=social&label=)
- [Kokoro TTS](https://github.com/hexgrad/kokoro) - 82M-parameter open-weight TTS that hits top TTS-Arena quality while running fast on Apple Silicon. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/hexgrad/kokoro?style=social&label=)
- [Moshi](https://github.com/kyutai-labs/moshi) - Kyutai's real-time full-duplex speech-text foundation model. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/kyutai-labs/moshi?style=social&label=)
- [OpenVoice](https://github.com/myshell-ai/OpenVoice) - Instant voice cloning. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/myshell-ai/OpenVoice?style=social&label=)
- [Parakeet](https://github.com/NVIDIA/NeMo) - NVIDIA ASR model, convertible to CoreML. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/NVIDIA/NeMo?style=social&label=)
- [Piper](https://github.com/rhasspy/piper) - Fast neural text-to-speech. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/rhasspy/piper?style=social&label=)
- [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) - Multilingual speech understanding. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/FunAudioLLM/SenseVoice?style=social&label=)
- [Sesame CSM](https://github.com/SesameAILabs/csm) - Conversational speech model that produces RVQ audio codes from text and audio with a Llama backbone. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/SesameAILabs/csm?style=social&label=)
- [Ultravox](https://github.com/fixie-ai/ultravox) - Real-time speech-to-speech LLM. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/fixie-ai/ultravox?style=social&label=)
- [Whisper.cpp](https://github.com/ggerganov/whisper.cpp) - C/C++ port of Whisper with Metal acceleration. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/ggerganov/whisper.cpp?style=social&label=)
- [WhisperX](https://github.com/m-bain/whisperX) - Whisper with speaker diarization. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/m-bain/whisperX?style=social&label=)

### Agent UIs

- [AnythingLLM](https://anythingllm.com) - Full-stack RAG application for any LLM. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - Cross-platform native desktop client with 300+ preconfigured assistants. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/CherryHQ/cherry-studio?style=social&label=)
- [Enchanted](https://github.com/gluonfield/enchanted) - Native macOS UI for Ollama. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/gluonfield/enchanted?style=social&label=)
- [LibreChat](https://www.librechat.ai) - Enhanced ChatGPT clone with multi-provider support. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [LobeChat](https://github.com/lobehub/lobehub) - Feature-rich self-hosted AI workspace with plugins, knowledge base, and multi-provider support. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/lobehub/lobehub?style=social&label=)
- [Msty](https://msty.app) - Native chat UI for local and remote models. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [NextChat](https://github.com/ChatGPTNextWeb/NextChat) - Lightweight cross-platform chat client with plugin and MCP support. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/ChatGPTNextWeb/NextChat?style=social&label=)
- [Open WebUI](https://openwebui.com) - Extensible self-hosted AI interface. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) - Locally installed unified frontend for many LLM APIs with deep customization. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/SillyTavern/SillyTavern?style=social&label=)
- [Vane](https://github.com/ItzCrazyKns/Vane) - Privacy-focused self-hosted answering engine (ex-Perplexica) with web source citations. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/ItzCrazyKns/Vane?style=social&label=)

### Orchestration and eventing

- [Activepieces](https://www.activepieces.com) - Open-source Zapier alternative. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Dagu](https://github.com/dagu-org/dagu) - Single-binary DAG-based cron replacement with web UI and YAML workflows. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/dagu-org/dagu?style=social&label=)
- [Dify](https://github.com/langgenius/dify) - Production LLM app platform with visual workflows, RAG pipelines, and an agent builder. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/langgenius/dify?style=social&label=)
- [Flowise](https://github.com/FlowiseAI/Flowise) - Drag-and-drop visual builder for agents and LLM flows. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social&label=)
- [Huginn](https://github.com/huginn/huginn) - Build agents that perform automated tasks. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/huginn/huginn?style=social&label=)
- [Kestra](https://github.com/kestra-io/kestra) - Event-driven orchestration platform for scheduled and triggered workflows with 600+ plugins. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/kestra-io/kestra?style=social&label=)
- [Langflow](https://github.com/langflow-ai/langflow) - Visual IDE for composing and deploying agentic workflows as APIs or MCP servers. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/langflow-ai/langflow?style=social&label=)
- [n8n](https://n8n.io) - Fair-code workflow automation with LLM nodes. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Temporal](https://temporal.io) - Durable execution workflow engine. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Trigger.dev](https://trigger.dev) - Open-source background job framework. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Windmill](https://www.windmill.dev) - Developer platform for internal tools and workflows. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Observability

- [Helicone](https://github.com/Helicone/helicone) - Self-hosted LLM observability. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/Helicone/helicone?style=social&label=)
- [Langfuse](https://langfuse.com) - Open-source LLM engineering platform. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry for LLM apps. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/traceloop/openllmetry?style=social&label=)
- [Phoenix](https://phoenix.arize.com) - ML observability from Arize. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Image and video agents

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Node-based Stable Diffusion UI with Metal support. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/comfyanonymous/ComfyUI?style=social&label=)
- [Draw Things](https://drawthings.ai) - Apple Silicon native Stable Diffusion app with CLI. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [Fooocus](https://github.com/lllyasviel/Fooocus) - Simplified SDXL generation UI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/lllyasviel/Fooocus?style=social&label=)
- [InvokeAI](https://invoke-ai.github.io/InvokeAI/) - Professional Stable Diffusion platform. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)

### Agent bridges

- [claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) - Telegram bridge for Claude Code. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/RichardAtCT/claude-code-telegram?style=social&label=)
- [matterbridge](https://github.com/42wim/matterbridge) - Bridge between chat protocols. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/42wim/matterbridge?style=social&label=)

---

## Hardware ![](https://img.shields.io/badge/_-HARDWARE-64748b?style=flat-square&logo=apple&logoColor=white)
Pick the right mini. Unified memory is not upgradeable, choose generously.

| Model | Year | Min RAM | Max RAM | Max storage | Notes |
|---|---|---|---|---|---|
| Mac mini M1 | 2020 | 8 GB | 16 GB | 2 TB | Great bargain, limited for 13B+ models |
| Mac mini M2 / M2 Pro | 2023 | 8 / 16 GB | 24 / 32 GB | 8 TB | Sweet spot for most home servers |
| Mac mini M4 / M4 Pro | 2024 | 16 / 24 GB | 32 / 64 GB | 8 TB | Best for agentic workloads and 70B models |

- [Macs Fan Control](https://crystalidea.com/macs-fan-control) - Monitor and override fan curves. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [Network UPS Tools](https://networkupstools.org) - NUT client for safe shutdown with a UPS. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [OWC Thunderbolt docks](https://eshop.macsales.com/shop/docks) - Quality hubs for storage and display expansion. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Satechi stands](https://satechi.net) - Aluminum stands with USB-C passthrough. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)

See [docs/hardware.md](docs/hardware.md) for detailed picks and sizing.

---

## OS and base setup ![](https://img.shields.io/badge/_-macOS-000000?style=flat-square&logo=apple&logoColor=white)
- [Asahi Linux](https://asahilinux.org) - Fedora-based Linux for Apple Silicon if you prefer a Linux server OS (M1/M2 series supported, M3/M4 not yet). ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white)
- [Auto-Login Settings](https://support.apple.com/guide/mac-help/set-your-mac-to-log-in-automatically-mh27627/mac) - Required for headless post-reboot startup. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [BetterDisplay](https://github.com/waydabber/BetterDisplay) - Virtual display for headless Apple Silicon Macs. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/waydabber/BetterDisplay?style=social&label=)
- [caffeinate(8)](https://ss64.com/osx/caffeinate.html) - Prevent sleep for a process or timeframe. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [defaults(1)](https://ss64.com/osx/defaults.html) - Scriptable access to macOS preferences. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [OpenCore Legacy Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher) - Run current macOS on unsupported Intel minis to keep old hardware serving. ![Intel](https://img.shields.io/badge/Intel-0071C5?style=flat-square&logo=intel&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/dortania/OpenCore-Legacy-Patcher?style=social&label=)
- [sharing(1)](https://ss64.com/osx/sharing.html) - Configure SMB, AFP, and Time Machine shares from CLI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)

---

## Remote access ![](https://img.shields.io/badge/_-REMOTE-3b82f6?style=flat-square&logo=tailscale&logoColor=white)
- [Blink Shell](https://blink.sh) - Best-in-class SSH/mosh client for iOS and iPadOS. ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) - Expose local services without opening ports via `cloudflared`. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [mosh](https://mosh.org) - Mobile shell, survives roaming and sleep. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [RustDesk](https://github.com/rustdesk/rustdesk) - Open-source remote desktop with an optional self-hosted relay server. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/rustdesk/rustdesk?style=social&label=)
- [Screens 5](https://apps.apple.com/us/app/screens-5-vnc-remote-desktop/id1663047912) - Polished VNC client for managing the mini from Mac, iPhone, and iPad. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Tailscale](https://tailscale.com) - WireGuard-based mesh VPN with SSH, Funnel, and Serve. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [WireGuard](https://www.wireguard.com) - Fast modern VPN, use `wg-quick` via launchd. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [wush](https://github.com/coder/wush) - Ad-hoc P2P SSH and rsync over WireGuard using Tailscale DERP without a tailnet. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/coder/wush?style=social&label=)
- [ZeroTier](https://zerotier.com) - Peer-to-peer virtual LAN that puts the mini and all your devices on one flat network. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)

---

## Containers and virtualization ![](https://img.shields.io/badge/_-CONTAINERS-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Apple Container](https://github.com/apple/container) - Apple's Swift-native Linux container runtime using lightweight VMs, optimized for Apple Silicon. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/apple/container?style=social&label=)
- [Arcane](https://github.com/ofkm/arcane) - Modern Go/Svelte Docker management UI covering images, volumes, networks, and Compose stacks. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/ofkm/arcane?style=social&label=)
- [CapRover](https://caprover.com) - One-click self-hosted PaaS on Docker Swarm with Nginx and Let's Encrypt. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Cilicon](https://github.com/traderepublic/Cilicon) - Self-hosted ephemeral macOS CI runner that clones APFS VM bundles for GitHub Actions and Buildkite. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/traderepublic/Cilicon?style=social&label=)
- [Colima](https://github.com/abiosoft/colima) - Container runtimes on Lima, fast Docker replacement. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/abiosoft/colima?style=social&label=)
- [Coolify](https://coolify.io) - Self-hostable Heroku/Vercel alternative deploying apps and 280+ services over SSH. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - Mainstream Docker on macOS with GUI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Dockge](https://github.com/louislam/dockge) - Reactive web UI dedicated to managing Docker Compose stacks. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/louislam/dockge?style=social&label=)
- [Lima](https://github.com/lima-vm/lima) - Linux VMs with automatic file sharing and port forwarding. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/lima-vm/lima?style=social&label=)
- [OrbStack](https://orbstack.dev) - Fast, light Docker and Linux VMs for macOS. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Parallels Desktop](https://www.parallels.com/products/desktop/) - Full commercial VM suite with server mode. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Portainer CE](https://www.portainer.io) - Web UI for managing Docker, Compose, Swarm, and Kubernetes containers. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Rancher Desktop](https://rancherdesktop.io) - Kubernetes and container management on the desktop. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Runtipi](https://github.com/runtipi/runtipi) - Personal home-server orchestrator with a one-click app store built on Docker Compose. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/runtipi/runtipi?style=social&label=)
- [Tart](https://github.com/cirruslabs/tart) - Native Apple Silicon VMs for macOS and Linux guests. ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/cirruslabs/tart?style=social&label=)
- [UTM](https://mac.getutm.app) - QEMU-based VMs with a native UI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)

---

## Media servers ![](https://img.shields.io/badge/_-MEDIA-00A4DC?style=flat-square&logo=jellyfin&logoColor=white)
- [Audiobookshelf](https://audiobookshelf.org) - Self-hosted audiobook and podcast server with mobile apps. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Channels DVR](https://getchannels.com) - DVR server for live TV. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Emby](https://emby.media) - Media server fork of MediaBrowser. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Ente](https://github.com/ente-io/ente) - End-to-end-encrypted self-hostable photos, auth, and locker. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/ente-io/ente?style=social&label=)
- [Jellyfin](https://jellyfin.org) - Free and open source media server. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Jellyseerr](https://seerr.dev) - Unified request and discovery manager for Jellyfin, Plex, and Emby. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Komga](https://www.komga.org) - Self-hosted media server for comics, manga, and eBooks. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Navidrome](https://navidrome.org) - Lightweight Subsonic/OpenSubsonic-compatible self-hosted music streaming. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Plex Media Server](https://www.plex.tv) - The original streaming-first media server. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [RomM](https://romm.app) - Self-hosted ROM manager with EmulatorJS and 400+ platforms. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Tautulli](https://www.tautulli.com) - Python monitoring and analytics companion for Plex. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

---

## Storage and NAS ![](https://img.shields.io/badge/_-STORAGE-6366f1?style=flat-square&logo=synology&logoColor=white)
- [Mountain Duck](https://mountainduck.io) - Mount S3/SFTP/WebDAV volumes in Finder. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [OpenZFS on OS X](https://openzfsonosx.org) - ZFS filesystem for external storage pools. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [rclone](https://rclone.org) - Rsync for cloud storage, 70+ backends. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [Resilio Sync](https://www.resilio.com/individuals/) - P2P file sync without a cloud. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Syncthing](https://syncthing.net) - Continuous file sync across devices. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)

---

## Self-hosted apps ![](https://img.shields.io/badge/_-SELF--HOSTED-10b981?style=flat-square)
### Productivity and notes

- [Actual Budget](https://actualbudget.org) - Envelope-budgeting personal finance app. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [AFFiNE](https://github.com/toeverything/AFFiNE) - Local-first open-source Notion/Miro alternative unifying docs, whiteboards, and databases. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/toeverything/AFFiNE?style=social&label=)
- [AppFlowy](https://appflowy.com) - Open-source local-first Notion alternative with docs, wikis, tasks, and AI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white)
- [BookStack](https://www.bookstackapp.com) - Self-hosted wiki organized into Books, Chapters, and Pages with WYSIWYG editing. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Docmost](https://docmost.com) - Confluence/Notion alternative with MCP support and diagramming. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Firefly III](https://firefly-iii.org) - Self-hosted double-entry personal finance manager with budgets, rules, and API. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [HedgeDoc](https://hedgedoc.org) - Real-time collaborative markdown editor, formerly CodiMD. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Huly](https://github.com/hcengineering/platform) - All-in-one Linear, Jira, Slack, and Notion alternative with native arm64 containers. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/hcengineering/platform?style=social&label=)
- [Khoj](https://github.com/khoj-ai/khoj) - Self-hostable personal AI that answers across your notes, docs, and the web. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/khoj-ai/khoj?style=social&label=)
- [Logseq](https://logseq.com) - Privacy-first local-first outliner and knowledge graph for daily notes and backlinks. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Apple Silicon](https://img.shields.io/badge/Apple%20Silicon-000000?style=flat-square&logo=apple&logoColor=white)
- [Mealie](https://mealie.io) - Recipe manager and meal planner with URL scraping and shopping lists. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Memos](https://usememos.com) - Self-hosted timeline for quick markdown notes, daily logs, and snippets. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [NocoDB](https://nocodb.com) - No-code Airtable alternative turning Postgres/MySQL into a spreadsheet UI. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Outline](https://www.getoutline.com) - Team knowledge base with real-time collaboration and AI search. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [SilverBullet](https://silverbullet.md) - Programmable browser-based markdown PKM platform with Lua scripting. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [ToolJet](https://github.com/ToolJet/ToolJet) - Open-source low-code builder for internal tools and dashboards with 80+ data sources. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/ToolJet/ToolJet?style=social&label=)
- [Trilium Next](https://github.com/TriliumNext/Notes) - Hierarchical self-hosted knowledge base with scripting, relations, and local-first sync. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/TriliumNext/Notes?style=social&label=)
- [Vikunja](https://vikunja.io) - Open-source task manager with list, kanban, Gantt, and table views. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)

### Files and documents

- [CryptPad](https://cryptpad.org) - End-to-end-encrypted collaborative office suite (docs, sheets, slides, kanban). ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Etherpad](https://etherpad.org) - Real-time collaborative plain-text editor with 290+ plugins. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Filebrowser](https://github.com/filebrowser/filebrowser) - Single-binary web file manager for uploading, editing, and sharing files. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/filebrowser/filebrowser?style=social&label=)
- [Forgejo](https://forgejo.org) - Community Gitea fork for self-hosted git. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Gitea](https://gitea.io) - Lightweight self-hosted git service. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Gitleaks](https://github.com/gitleaks/gitleaks) - Single-binary secret scanner for git history and working trees. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![⭐](https://img.shields.io/github/stars/gitleaks/gitleaks?style=social&label=)
- [Immich](https://immich.app) - Google Photos replacement with ML. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Nextcloud](https://nextcloud.com) - Full self-hosted cloud suite. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Paperless-ngx](https://docs.paperless-ngx.com) - Document management with OCR. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Stirling PDF](https://www.stirlingpdf.com) - 60+ PDF tools for merging, signing, converting, and OCR. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - Lightweight Bitwarden server in Rust. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/dani-garcia/vaultwarden?style=social&label=)
- [Zoekt](https://github.com/sourcegraph/zoekt) - Trigram-indexed source code search with symbol-aware ranking. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/sourcegraph/zoekt?style=social&label=)

### Reading and feeds

- [ArchiveBox](https://archivebox.io) - Self-hosted web archive preserving pages as HTML, PDF, PNG, and WARC. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [FreshRSS](https://freshrss.org) - Scalable self-hosted RSS/Atom aggregator with WebSub and mobile sync. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Karakeep](https://karakeep.app) - AI-powered bookmark and read-it-later app. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Miniflux](https://miniflux.app) - Minimalist RSS reader. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Readeck](https://codeberg.org/readeck/readeck) - Single-binary Go read-it-later and bookmark manager with article extraction and full-text search. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Shiori](https://github.com/go-shiori/shiori) - Single-binary Go bookmark manager with content archival and Pocket import. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/go-shiori/shiori?style=social&label=)
- [Wallabag](https://wallabag.org) - Self-hosted read-it-later app for saving, syncing, and reading web articles. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Analytics and monitoring

- [changedetection.io](https://changedetection.io) - Website change monitor with CSS/xPath filters and 85+ notification channels. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Medama](https://github.com/medama-io/medama) - Sub-1 KB cookieless analytics tracker delivered as a single Go binary. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/medama-io/medama?style=social&label=)
- [Plausible CE](https://plausible.io) - Cookieless, privacy-friendly web analytics. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [PostHog](https://posthog.com) - Product analytics, session replay, feature flags, and experiments platform. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Rybbit](https://rybbit.com) - Modern cookieless analytics with session replay, funnels, and web vitals. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Umami](https://umami.is) - Simple, privacy-focused self-hosted web analytics. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Vince](https://github.com/vinceanalytics/vince) - Plausible-style privacy analytics as one dependency-free Go binary with automatic TLS. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/vinceanalytics/vince?style=social&label=)

### Mail, comms, and push

- [Apprise](https://github.com/caronc/apprise) - One CLI to push notifications to 100+ services including ntfy, Telegram, Discord, and email. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/caronc/apprise?style=social&label=)
- [Conduit](https://conduit.rs) - Simple single-binary Rust Matrix homeserver with embedded RocksDB. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [docker-mailserver](https://github.com/docker-mailserver/docker-mailserver) - Production-ready containerized full mail stack. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/docker-mailserver/docker-mailserver?style=social&label=)
- [Gotify](https://gotify.net) - Self-hosted push-notification server with REST API and Android client. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Listmonk](https://github.com/knadh/listmonk) - Single-binary self-hosted newsletter and mailing-list manager backed by Postgres. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/knadh/listmonk?style=social&label=)
- [ntfy](https://ntfy.sh) - HTTP-based pub/sub push notification service, free public and self-hostable. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Stalwart](https://stalw.art) - All-in-one Rust mail and collaboration server with SMTP, IMAP, JMAP, and CalDAV. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Synapse](https://github.com/element-hq/synapse) - Reference Python implementation of the Matrix homeserver. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/element-hq/synapse?style=social&label=)

### Network tunnels and zero-trust

- [Headscale](https://github.com/juanfont/headscale) - Self-hosted open-source implementation of the Tailscale coordination server. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/juanfont/headscale?style=social&label=)
- [NetBird](https://netbird.io) - WireGuard-based zero-trust mesh VPN with SSO and policies. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square)
- [Pangolin](https://github.com/fosrl/pangolin) - WireGuard-based identity-aware reverse proxy and remote-access platform with RBAC. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Paid](https://img.shields.io/badge/Paid-DAA520?style=flat-square) ![⭐](https://img.shields.io/github/stars/fosrl/pangolin?style=social&label=)
- [zrok](https://zrok.io) - OpenZiti-based peer-to-peer sharing and secure tunneling alternative to ngrok. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### Privacy front-ends and search

- [Invidious](https://invidious.io) - Privacy-respecting alternative front-end for YouTube with RSS and API. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [SearXNG](https://docs.searxng.org) - Privacy-respecting metasearch engine aggregating up to 251 sources. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

---

## Smart home ![](https://img.shields.io/badge/_-SMART%20HOME-41BDF5?style=flat-square&logo=homeassistant&logoColor=white)
- [ESPHome](https://esphome.io) - DIY firmware for ESP-based smart devices. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square)
- [Frigate](https://frigate.video) - Local AI-driven NVR with real-time object detection and Home Assistant integration. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Home Assistant](https://www.home-assistant.io) - Leading open-source home automation platform. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Homebridge](https://homebridge.io) - Bridge non-HomeKit accessories into Apple Home. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white)
- [HOOBS](https://hoobs.org) - Homebridge distribution with a web UI. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Matterbridge](https://github.com/Luligu/matterbridge) - Node-based Matter plugin manager that bridges devices into Apple Home, Google, and Alexa. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/Luligu/matterbridge?style=social&label=)
- [Node-RED](https://nodered.org) - Flow-based programming for automation. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [python-matter-server](https://github.com/home-assistant-libs/python-matter-server) - Reference Matter controller WebSocket server used by Home Assistant. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/home-assistant-libs/python-matter-server?style=social&label=)
- [RuView](https://github.com/ruvnet/RuView) - WiFi DensePose: camera-free human pose, presence, and vital-sign monitoring over commodity WiFi. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![⭐](https://img.shields.io/github/stars/ruvnet/RuView?style=social&label=)
- [Scrypted](https://scrypted.app) - HomeKit Secure Video bridge for existing cameras. ![Universal](https://img.shields.io/badge/Universal-636363?style=flat-square) ![Native](https://img.shields.io/badge/Native-111111?style=flat-square&logo=apple&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- [Viseron](https://github.com/roflcoopter/viseron) - Self-hosted local-only NVR with object detection, motion detection, and face recognition. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/roflcoopter/viseron?style=social&label=)
- [Z-Wave JS UI](https://github.com/zwave-js/zwave-js-ui) - Z-Wave controller UI. ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![⭐](https://img.shields.io/github/stars/zwave-js/zwave-js-ui?style=social&label=)

---

## Ad blocking and DNS ![](https://img.shields.io/badge/_-DNS-68217A?style=flat-square&logo=adguard&logoColor=white)