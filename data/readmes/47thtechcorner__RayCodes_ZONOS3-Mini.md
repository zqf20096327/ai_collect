<div align="center">
  <a href="https://youtu.be/mVjMSurLBB4">
    <img src="https://img.shields.io/badge/YouTube-Watch%20Video-red?style=for-the-badge&logo=youtube" alt="Zonos 3 Mini: This 100M Active AI Clones Any Voice in 80ms Locally! (Destroys ElevenLabs)">
  </a>
  <h3>📺 <a href="https://youtu.be/mVjMSurLBB4">Watch the full tutorial: Zonos 3 Mini: This 100M Active AI Clones Any Voice in 80ms Locally! (Destroys ElevenLabs)</a></h3>
</div>

# ZONOS3-Mini: 100M Active Parameter Real-Time Voice Cloning

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Model Size: 800M MoE / 100M Active](https://img.shields.io/badge/Model%20Size-800M%20Total%20%2F%20100M%20Active-green.svg)](https://huggingface.co/Zyphra/ZONOS3-Mini)
[![Latency: 80ms TTFA](https://img.shields.io/badge/Latency-80ms%20TTFA-orange.svg)](https://www.zyphra.com/our-work/zonos3-mini)
[![Languages: 43 Supported](https://img.shields.io/badge/Languages-43%20Supported-purple.svg)](https://huggingface.co/Zyphra/ZONOS3-Mini)

> **"Sub-100ms real-time voice cloning and studio-grade 44.1 kHz text-to-speech powered by a hybrid Gated DeltaNet + Attention Mixture-of-Experts architecture that runs locally on laptops, phones, and inside web browsers via WebGPU."**

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
|---|---|---|---|
| Dynamic Emotion-Steered Studio Narrator | High-fidelity zero-shot voice cloning with granular acoustic emotion and cadence steering | Studio audio reference clip and dramatic script with emotion markers | High-fidelity studio voice clone audio with excited mood conditioning |
| Multilingual Cross-Lingual Voice Agent | Sub-100ms conversational synthesis across multiple languages while preserving speaker timbre | Trilingual customer support script in English, Hindi, and Spanish | Zero-shot cross-lingual synthesized voice clip preserving natural speaker timbre |
| Sub-100ms Live Tech Commentary Deck | High-throughput streaming speech generation with rapid cadence and broadcast loudness | High-octane breaking tech release announcement script | High-speed live commentary audio stream synthesized at rapid broadcast cadence |

---

## 🚀 Quick Start (Windows PowerShell)

### Step 1: Setup Environment, Download Weights & Register Runtime

```powershell
# Create and activate Python virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install required audio and model dependencies
pip install torch torchaudio zonos

# Download official model weights and runtime files
hf download Zyphra/ZONOS3-Mini --local-dir models/ZONOS3-Mini
```

### Step 2: Run Production Pipeline

```powershell
python main.py
```

---

## 💼 Practical Use Cases

- ⚡ **Zero-Server Client-Side Voice Assistants**: Run complete voice synthesis locally inside browser tabs via WebGPU with zero cloud latency and zero recurring subscription bills.
- 🎧 **Interactive Multilingual Customer Support**: Pair real-time speech recognition with ZONOS3-Mini to stream sub-100ms voice responses across 43 languages.
- 🎮 **Dynamic Game NPC Voice Engines**: Steer emotion, cadence, and vocal texture on the fly to generate reactive character lines without shipping gigabytes of pre-recorded audio.
- 📚 **Automated Studio Audiobook Production**: Generate up to 10 minutes of continuous 44.1 kHz studio-quality narration per chapter from 10-second reference voice samples.

---

## 🗺️ Future Feature Roadmap

- 🌐 **WebGPU Single-File Standalone Runner**: Package standalone browser runtime HTML with embedded WebGPU inference for zero-install client execution.
- 🎙️ **Multi-Speaker Dialogue Synthesizer**: Support dual-speaker conversational turn-taking within a single generation pass.
- 🎛️ **Granular Phoneme-Level Prosody Tuning**: Add direct pitch-contour manipulation sliders for expressive theatrical dubbing.
- 📱 **Mobile Edge Quantization**: Optimize GGUF INT4 / INT8 runtime for on-device real-time voice agents on low-power mobile chipsets.

---

## 🏷️ Search Tags & Keywords
`Zonos3 Mini` • `Zyphra Zonos` • `Zonos voice cloning` • `real time TTS` • `browser voice AI` • `WebGPU TTS` • `local speech synthesis` • `open source voice cloning` • `multilingual TTS` • `ElevenLabs alternative` • `OpenAI voice alternative` • `Kokoro TTS alternative` • `Zonos3 tutorial` • `voice agent TTS` • `low latency speech` • `Hindi voice cloning` • `local voice cloning` • `speech synthesis AI` • `real time voice agent` • `Zonos audio model` • `Apache 2.0`
