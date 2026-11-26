<div align="center">
  <a href="https://youtu.be/HZBvr3SJr2Y">
    <img src="https://img.youtube.com/vi/HZBvr3SJr2Y/0.jpg" alt="NVIDIA Nemotron 3.5 Bolt Just Got Vision! Run Multimodal AI on 4GB VRAM!">
  </a>
  <h3>📺 <a href="https://youtu.be/HZBvr3SJr2Y">Watch the full video tutorial on YouTube</a></h3>
</div>

---

# NVIDIA-Nemotron-3.5-Bolt-E4B-4GB (mmproj Multimodal Vision Upgrade)

[![License](https://img.shields.io/badge/License-OpenMDW--1.1-76B900.svg)](https://openmdw.ai/license/1-1/)
[![Model Architecture](https://img.shields.io/badge/Architecture-Gemma--4--E4B%20%2B%20mmproj-blue.svg)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)
[![Parameters](https://img.shields.io/badge/Parameters-8B%20Total%20%2F%204B%20Active-emerald.svg)](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf)
[![VRAM Footprint](https://img.shields.io/badge/Local%20Footprint-~4GB%20VRAM-orange.svg)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)
[![BFCL-v3 Score](https://img.shields.io/badge/BFCL--v3-67.31%25-brightgreen.svg)](https://gorilla.cs.berkeley.edu/leaderboard.html)

> *"NVIDIA-Nemotron-3.5-Bolt-E4B pairs Gemma 4's Per-Layer Embeddings architecture with pure reinforcement learning post-training. The new mmproj multimodal projector quietly unlocks native screen reading, document OCR, and desktop computer-use workflows completely offline within 4GB of VRAM."*

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
| :--- | :--- | :--- | :--- |
| **Screen & Receipt Visual Auditor** | Offline document OCR and low-token structured extraction | Commercial expense receipt photo with items and tax | Interactive financial audit dashboard with visual discrepancy highlights |
| **Slide & Architecture Deck Synthesizer** | Visual layout parsing and multi-tier architectural synthesis | Complex enterprise cloud infrastructure slide deck capture | Responsive visual executive briefing with system decision logs |
| **Dual-Mode Screen Privacy Sentinel** | Dual-mode reasoning scanner detecting credentials before screen-sharing | Desktop code workspace with exposed environment keys | Visual security audit report highlighting flagged screen zones |

---

## 🚀 Quick Start (Windows PowerShell)

### Step 1: Setup Environment, Download Weights & Register Runtime

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install ollama pillow mss requests

hf download nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB Nemotron-3.5-Bolt-E4B-Q4_K_M.gguf --local-dir models/nemotron-bolt
hf download nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB Nemotron-3.5-Bolt-E4B-mmproj-BF16.gguf --local-dir models/nemotron-bolt

ollama create nemotron-bolt-vision -f Modelfile
```

### Step 2: Run Production Pipeline

```powershell
python main.py
```

---

## 🛡️ Practical Use Cases

- 🛡️ **Pre-Broadcast Privacy Guard**: Continuously scans streaming displays, staging windows, and terminals for exposed JWTs, `.env` values, or private keys with automated alerts.
- 💳 **Offline Expense & Invoice Reconciliation**: Automatically extracts line items, tax numbers, and dates from raw receipts into structured management dashboards without third-party cloud API costs.
- ⚡ **Zero-Latency DevOps Incident Watcher**: Observes live Grafana, Datadog, or Docker dashboards, outputting succinct diagnostics only when anomaly thresholds are breached.
- 📊 **Executive Slide & Diagram Decompiler**: Converts complex multi-tier architectural slides, flowcharts, and system block diagrams into interactive briefing cards and structured documentation.

---

## 🗺️ Future Feature Roadmap

- 🌐 **Autonomous Browser-Use Action Grounding**: Native integration with local browser drivers for automated form fills and UI navigation.
- 🎙️ **Synchronized Audio-Visual Telemetry**: Multi-modal fusion utilizing the dual mmproj projector for live screen-sharing commentary.
- ✂️ **Dynamic Token Pruning Engine**: Adaptive tile resolution scaling to cut prefill latency on multi-monitor setups.
- 🩺 **Automated Health Check Monitor**: Background daemon that continuously evaluates local GPU resource headroom and KV cache allocation.

---

## 📄 License & Attribution

Released under the **OpenMDW-1.1** License. Based on [NVIDIA Nemotron 3.5 Bolt](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) and Google's [Gemma 4](https://huggingface.co/google/gemma-4-E4B-it).

---

## 🏷️ Search Tags

`qwen 3.5 4b` • `nemotron 3.5 bolt` • `nemotron 3.5 bolt e4b 4gb` • `nemotron 3.5 super vl` • `gemma 4 vs qwen` • `nemotron 3.5 bolt e4b` • `nemotron 3.5 bolt 74b` • `gemma 4 e4b` • `nemotron 3.5` • `nemotron 3.5 lightning` • `nemotron 3 ultra` • `offline document ai` • `offline document parser` • `llama.cpp vision` • `minicpm vision` • `nemotron ollama` • `nemotron vs qwen` • `nemotron gguf` • `ollama vision` • `nemotron vs gemma` • `bolt e4b` • `nemotron e4b` • `local vision agent` • `offline vision ai` • `nemotron bolt` • `nvidia nemotron`
