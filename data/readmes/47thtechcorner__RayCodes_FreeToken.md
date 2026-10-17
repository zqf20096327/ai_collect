<div align="center">
  <a href="https://youtu.be/kdoP47Xtpjw">
    <img src="https://img.youtube.com/vi/kdoP47Xtpjw/0.jpg" alt="I Ran Qwen 3.8 27B on Just 4GB VRAM! (FreeToken Tutorial)">
  </a>
  <h3>📺 <a href="https://youtu.be/kdoP47Xtpjw">Watch the full tutorial on YouTube</a></h3>
</div>

<br>

<div align="center">
  <img alt="FreeToken Logo" src="https://raw.githubusercontent.com/FlashML-org/FreeToken/main/assets/freetoken-logo-dark.svg" width="60%">
</div>

# ⚡ FreeToken Edge AI Serving

FreeToken is an edge-native Mixture-of-Experts (MoE) serving engine designed to run massive frontier open-weight models locally on consumer hardware like gaming PCs with high interactive token generation speeds.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
|---|---|---|
| Consumer PC hardware & financial CSV dataset | FreeToken elastic VRAM & hybrid MoE execution | Local OpenAI/Anthropic API endpoint |

---

## 🚀 Quickstart & Setup

### Option 1: Desktop Application
Download the prebuilt FreeToken Desktop app for Windows or Linux from [flashml.ai](https://www.flashml.ai/) for a complete graphical interface with chat and engine tuning controls.

### Option 2: CLI Setup via uv (Recommended)

1. Install FreeToken using `uv` or standard Python `pip`:

```bash
uv pip install "freetoken[accel]"
```

2. Register your local model checkpoint with Ollama:

```bash
ollama create Qwen3.8-27B -f models/Modelfile
```

---

## 💻 Running Local MoE Inference

Execute local MoE serving using the main Python interface with bandwidth-adaptive hybrid backend routing:

```bash
python main.py --model Qwen3.8-27B-UD-IQ1_M --backend hybrid --input-csv inputs/financial_statements_edgar.csv
```

### Command Options

- `--model`: Target model identifier or local GGUF weight path (default: `Qwen3.8-27B-UD-IQ1_M`)
- `--backend`: MoE execution mode: `hybrid`, `offload`, `fused`, `cpu`, or `auto` (default: `hybrid`)
- `--input-csv`: Path to local dataset (default: `inputs/financial_statements_edgar.csv`)

---

## 📦 Project Architecture

```
FreeToken/
├── inputs/
│   └── financial_statements_edgar.csv
├── models/
│   ├── Modelfile
│   └── Qwen3.8-27B-UD-IQ1_M.gguf
├── main.py
└── README.md
```

### File Explanations

- **`main.py`**: Core Python CLI application running local MoE serving, dynamic VRAM re-allocation, semantic KV state caching, and OpenAI-compatible API response generation.
- **`inputs/financial_statements_edgar.csv`**: Sample 25MB SEC EDGAR financial statement summary dataset for local agent processing.
- **`models/Modelfile`**: Configuration file specifying GGUF model paths and system prompt templates for local Ollama registration.
- **`models/Qwen3.8-27B-UD-IQ1_M.gguf`**: Local model weight checkpoint file.
- **`README.md`**: Project documentation, setup guide, and technical overview.

---

## 🛠️ Technology Stack

- **Inference Runtime**: FreeToken Edge-Native MoE Engine
- **Language**: Python 3.10+
- **Model Checkpoints**: Qwen3.6 / Qwen3.8 MoE, DeepSeek-V4, GGUF UD-IQ1_M, Safetensors
- **API Standards**: OpenAI REST API (`/v1/chat/completions`) & Anthropic Messages API
- **Package Manager**: uv / pip

---

## 💡 5 Practical Use Cases

1. **Private Local Financial Analysis**: Process sensitive SEC corporate filings without uploading proprietary data to cloud APIs.
2. **Local Code Generation & Refactoring**: Pair local coding assistants with Anthropic/OpenAI drop-in endpoints on gaming PCs.
3. **Agentic Tool Calling Workflow**: Leverage semantic anchor state checkpoints to speed up context edits during multi-turn agent execution.
4. **Offline AI Agent Operations**: Run massive 200B+ parameter models completely disconnected from internet connections.
5. **Hardware Budget Optimization**: Run datacenter-class open-weight models on consumer 16GB-24GB GPUs via PCIe streaming.

---

## 🔮 5 Future Features

1. **Multi-GPU PCIe Fabric Bridging**: Native peer-to-peer NVLink and PCIe Gen5 interconnect optimization across dual gaming GPUs.
2. **Real-time Engine Telemetry GUI**: Expanded live graphs tracking expert cache hit rates and PCIe bandwidth saturation.
3. **Quantization Auto-Tuning**: Dynamic quantization switching based on available VRAM thermal headroom.
4. **Expanded Vision MoE Support**: Multi-modal vision-language MoE model serving with patch-level GPU offloading.
5. **Distributed Edge Mesh**: Cluster multiple consumer PCs on local area networks to share MoE expert weights dynamically.

---

## 🏷️ Keywords & Tags
`FreeToken` `Qwen3.8-27B` `4GB VRAM` `MoE Engine` `Edge AI` `Local Inference` `LLM Offloading` `Python` `OpenAI API Endpoint` `Consumer Hardware`
