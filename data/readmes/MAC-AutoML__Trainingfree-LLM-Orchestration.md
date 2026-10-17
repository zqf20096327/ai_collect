# Training-Free Multimodal Large Language Model Orchestration

<p align="center">
  <b>Training-Free Multimodal Large Language Model Orchestration</b>
</p>

<p align="center">
  Tianyu Xie · Yuexiao Ma · Yuhang Wu · Wang Chen · Jiayi Ji · Tat-Seng Chua · Xiawu Zheng · Rongrong Ji
</p>

<p align="center">
  <b>🔥 Accepted by ICML 2026 🔥</b>
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2508.10016">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2508.10016-b31b1b.svg?logo=arxiv">
  </a>
  <a href="paper/2508.10016.pdf">
    <img alt="Paper PDF" src="https://img.shields.io/badge/Paper-PDF-red.svg">
  </a>
  <a href="https://github.com/MAC-AutoML/Trainingfree-LLM-Orchestration">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/Code-GitHub-black.svg?logo=github">
  </a>
  <a href="https://icml.cc/">
    <img alt="ICML 2026" src="https://img.shields.io/badge/ICML-2026-4B7BEC.svg">
  </a>
  <a href="https://github.com/MAC-AutoML/Trainingfree-LLM-Orchestration/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/MAC-AutoML/Trainingfree-LLM-Orchestration?style=social">
  </a>
  <br>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12+-3776AB.svg?logo=python&logoColor=white">
  <img alt="uv" src="https://img.shields.io/badge/Package%20Manager-uv-654FF0.svg">
  <img alt="Training Free" src="https://img.shields.io/badge/Training--Free-Orchestration-2ECC71.svg">
  <img alt="Multimodal" src="https://img.shields.io/badge/Omni--Modal-Assistant-F39C12.svg">
</p>

<p align="center">
  🚀 A training-free orchestration framework for building interactive omni-modal assistants by composing off-the-shelf modality experts, explicit LLM routing, text-centric cross-modal memory, and interruption-aware streaming interaction.
</p>

<p align="center">
  <a href="#highlights">Highlights</a> ·
  <a href="#method">Method</a> ·
  <a href="#results">Results</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#citation">Citation</a>
</p>

<p align="center">
  <img src="assets/figures/overview.png" width="92%" alt="Training-free orchestration overview">
</p>

## 🔥 News

- **2026**: 🔥🔥🔥 Accepted to **ICML 2026**.
- **2026-05-08**: 🚀 arXiv v3 is available.
- **2025-08-06**: 📄 Initial arXiv release.

## ✨ Highlights

- 🚀 **Training-free multimodal integration**: composes existing LLM, vision, ASR, and TTS experts without gradient-based multimodal alignment for system integration.
- 🧭 **Auditable LLM controller**: predicts user intent and emits explicit control tokens for expert selection, sequencing, speaking, listening, and interruption.
- 🧠 **Text-centric cross-modal memory**: compresses multimodal evidence into lightweight structured records for retrieval and reuse across turns.
- ⚡ **Unified interaction layer**: supports full-duplex streaming, speech interruption, live video grounding, and consistent modality transitions.
- 🧩 **Modular upgrade path**: each expert can be replaced or upgraded independently through configuration instead of retraining the full system.

## 🚀 At a Glance

| What changes | Why it matters |
| --- | --- |
| No end-to-end multimodal alignment training | Reduces integration cost and keeps the system easy to extend. |
| Explicit controller tokens | Makes routing decisions inspectable instead of hiding them inside a monolithic model. |
| Memory-backed expert reuse | Avoids repeated expert calls when prior multimodal evidence is already available. |
| Full-duplex runtime | Supports natural turn-taking, interruption, streaming response, and speech output. |

## 🧭 Method

<p align="center">
  <img src="assets/figures/pipeline.png" width="98%" alt="LLM orchestration pipeline">
</p>

## 🏗️ Framework Overview

LLM Orchestration separates multimodal assistant construction into three coordinated layers:

| Layer | Role |
| --- | --- |
| **LLM Controller** | Interprets the dialogue state, chooses modality experts, and emits protocol-constrained control tokens. |
| **Cross-modal Memory** | Stores dialogue history and compressed multimodal evidence for retrieval in later turns. |
| **Interaction Runtime** | Executes ASR, video capture, LLM calls, TTS playback, streaming responses, and interruption handling. |

This repository provides a runnable reference implementation with GUI and CLI entry points.

## 📊 Results

The figures below summarize the paper's reported gains from orchestration and memory reuse.

<p align="center">
  <img src="assets/figures/model_improvements.png" width="92%" alt="Model improvement comparison">
</p>

<p align="center">
  <img src="assets/figures/efficiency.png" width="78%" alt="Efficiency analysis">
</p>

## 📁 Repository Structure

```text
.
├── assets/       # README figures and visual assets
├── asr/          # ASR, VAD, and microphone input processing
├── dialogue/     # Main dialogue orchestration loop
├── gui/          # PyQt interface
├── llm/          # LLM controller, prompts, and model manager
├── memory/       # Dialogue and cross-modal memory records
├── paper/        # Local paper PDF
├── tts/          # TTS engines and audio playback
├── utils/        # Configuration and file utilities
├── video/        # Camera capture and visual processing
├── main.py       # CLI / GUI entry point
└── pyproject.toml
```

## 🛠️ Installation

This project is managed with `uv`.

```bash
git clone https://github.com/MAC-AutoML/Trainingfree-LLM-Orchestration.git
cd Trainingfree-LLM-Orchestration
uv sync
```

Create a local environment file:

```bash
cp .env.template .env
```

Then edit `.env` with the API endpoints and keys for the experts you want to use.

## ⚡ Quick Start

Run the GUI:

```bash
uv run python main.py --mode gui
```

Run the CLI:

```bash
uv run python main.py --mode cli
```

The runtime will initialize the configured ASR service, camera capture, LLM experts, memory manager, and TTS engine. Hardware devices and third-party APIs must be available according to your `.env` configuration.

## 🔧 Configuration

Most runtime behavior is configured through `.env`.

| Area | Example variables |
| --- | --- |
| Main dialogue LLM | `MAIN_LLM_MODEL`, `MAIN_LLM_API_BASE`, `MAIN_LLM_API_KEY` |
| Vision LLM | `VISION_LLM_MODEL`, `VISION_LLM_API_BASE`, `VISION_LLM_API_KEY` |
| Visual reasoning LLM | `QVQ_LLM_MODEL`, `QVQ_LLM_API_BASE`, `QVQ_LLM_API_KEY` |
| ASR | `ASR_API_URL`, `ASR_API_KEY`, `ASR_MODEL`, `ASR_GAIN` |
| TTS | `TTS_ENGINE`, `TTS_VOICE`, `COSY_API_BASE`, `GPUSTACK_API_BASE` |
| Runtime | `DEBUG`, `VAD_SENSITIVITY`, `USE_STREAMING` |

See [.env.template](.env.template) for the full list.

## 📄 Paper

- arXiv: [https://arxiv.org/abs/2508.10016](https://arxiv.org/abs/2508.10016)
- Local PDF: [paper/2508.10016.pdf](paper/2508.10016.pdf)

## 📚 Citation

If this work is useful for your research, please cite:

```bibtex
@article{xie2025trainingfree,
  title   = {Training-Free Multimodal Large Language Model Orchestration},
  author  = {Xie, Tianyu and Ma, Yuexiao and Wu, Yuhang and Chen, Wang and Ji, Jiayi and Chua, Tat-Seng and Zheng, Xiawu and Ji, Rongrong},
  journal = {arXiv preprint arXiv:2508.10016},
  year    = {2025}
}
```

The citation will be updated when the official ICML 2026 proceedings entry is available.
