<div align="center">
  <a href="https://youtu.be/TOWUUAqOi9E">
    <img src="https://img.youtube.com/vi/TOWUUAqOi9E/0.jpg" alt="Alibaba MNN Pocket: New 173MB Local AI Destroys ChatGPT Latency on Your Phone!">
  </a>
  <h3>📺 <a href="https://youtu.be/TOWUUAqOi9E">Watch the full tutorial on YouTube</a></h3>
</div>

# MNN-Pocket-0.3B: Ultra-Compact On-Device Language Engine

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Model Size](https://img.shields.io/badge/Parameters-300M-orange.svg)](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B)
[![INT4 Footprint](https://img.shields.io/badge/Footprint-173MB_INT4-green.svg)](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B-GGUF)
[![Throughput](https://img.shields.io/badge/Throughput-350+_Tok/s-purple.svg)](https://github.com/alibaba/MNN)
[![Context](https://img.shields.io/badge/Context-32K_Tokens-cyan.svg)](https://huggingface.co/taobao-mnn/MNN-Pocket-0.3B)

> Alibaba Taobao's 173MB on-device language transformer co-designed with the MNN inference engine to run natively offline on mobile devices, tablets, and laptops at sub-millisecond speeds.

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
|---|---|---|---|
| **Smart App-State Intent Router** | Sub-millisecond categorical intent routing and execution path dispatching | Multilingual raw mobile assistant queries | Interactive Decision Radar dashboard with target subsystem paths |
| **Local E-Commerce Receipt Normalizer** | Extracting merchant details, pricing totals, and delivery tracking from alerts | Transactional purchase alerts and shipping SMS notifications | Executive financial audit report with itemized tables & verification |
| **Micro Edge Voice Controller** | Offline voice command interpretation and low-power hardware state dispatching | Ambient smartwatch voice transcripts and device queries | Interactive wearable OS visualizer with responsive hardware toggles |

---

## 🚀 Quick Start (Windows PowerShell)

### Step 1: Setup Environment, Download Weights & Register Runtime

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install ollama huggingface_hub

hf download taobao-mnn/MNN-Pocket-0.3B-GGUF MNN-Pocket-0.3B-Instruct-Q4_1.gguf --local-dir models

ollama create mnn-pocket -f Modelfile
```

### Step 2: Run Production Pipeline

```powershell
python main.py
```

---

## 💡 Practical Use Cases

- ⚡ **Zero-Latency Mobile App Dispatching:** Route user natural language queries directly on-device to native phone settings, cameras, and navigation without paying cloud token fees or round-trip delays.
- 🛡️ **Private Offline Financial Auditing:** Parse incoming transaction confirmation SMS, bank alerts, and courier updates entirely inside local RAM with zero sensitive customer data leaving the device.
- ⌚ **Wearable & IoT Hardware Controller:** Power smartwatches, Raspberry Pi Zero boards, and ambient smart-home sensors with sub-second voice action interpretation and hardware state mutations.
- 🎮 **Offline Game NPC Dialogue:** Embed responsive, zero-latency background NPCs in mobile games with less than 200MB active memory overhead and battery-friendly CPU execution.

---

## 🗺️ Future Feature Roadmap

- 🚀 **Single-Pass Pointer Head Integration:** Direct Python bindings for the companion `MNN-Pocket-0.3B-Dec` non-autoregressive decision model for sub-10ms classification.
- 🔋 **Android / iOS Mobile Native Package:** Pre-packaged Flutter and React Native plugins leveraging Alibaba's native MNN C++ mobile runtime with Metal and OpenCL acceleration.
- 🎙️ **Streaming Whisper.cpp Voice Pipeline:** End-to-end voice-to-voice local loop integrating lightweight speech recognition with MNN-Pocket for real-time edge voice assistants.
- 🌐 **Offline Browser Automation Copilot:** Local intent-based DOM action classification for edge browser extensions handling privacy-first form auto-filling.

---

### 🏷️ Search Keywords & Tags
`mnn pocket`, `alibaba ai`, `taobao mnn`, `edge llm`, `qwen tiny`, `smollm2`, `mobile llm`, `phone ai`, `qwen mobile`, `tiny model`, `fast inference`, `llm quantization`, `edge neural`, `alibaba qwen`, `offline llm`, `mnn pocket 0.3b`, `taobao ai`, `173mb ai`, `300m model`, `on device ai`, `offline assistant`, `local llm`, `qat int4`, `w4a16`, `ollama mobile`, `llama cpp edge`, `tiny ai`, `edge transformer`, `sub 1b llm`, `intent router`, `mobile assistant`, `qwen edge`, `fast mobile ai`, `private ai`, `edge inference`, `350 tok sec`, `466 tok sec`, `gemma 3 alternative`, `smollm alternative`, `chatml model`
