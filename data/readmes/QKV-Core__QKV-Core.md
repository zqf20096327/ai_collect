# QKV Core: Breaking the 4GB VRAM Barrier 🚀

> **Run modern 7B LLMs (like Qwen 2.5, Llama 3) on legacy 4GB GPUs (GTX 1050/1650) without crashing.**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Experimental-orange)
[![Medium](https://img.shields.io/badge/Medium-Read%20the%20Series-black?style=flat&logo=medium&logoColor=white)](https://medium.com/@broxytr/qkv-core-series-part-1-0ca4fa89bfd1)

## 📰 In the Media & Articles

> Read the engineering story behind QKV Core:

* [**Part 1: Breaking the 4GB VRAM Barrier**](https://medium.com/@broxytr/qkv-core-series-part-1-0ca4fa89bfd1) - *How I ran 7B LLMs on a GTX 1050 without crashing.*
* **Part 2: Inside the Architecture** - *(Coming Soon)*

## 🧐 The Problem: It's Not Size, It's Fragmentation

Millions of developers are stuck on "GPU Poor" hardware like the **NVIDIA GTX 1050 (4GB)**.
When you try to load a standard quantized 7B model (e.g., Q4_K_M ~4.3GB or even smaller), you often hit the "OOM Cliff":
## 🚀 Features

- **Transformer Architecture**: Full implementation of GPT-style transformer models
- **Training & Fine-tuning**: Support for full training, incremental training, and fine-tuning
- **Parameter-Efficient Methods**: LoRA and QLoRA for efficient fine-tuning
- **RLHF & DPO**: Reinforcement Learning from Human Feedback and Direct Preference Optimization
- **Model Formats**: Support for PyTorch (.pt) and GGUF formats
- **Hugging Face Integration**: Download and convert models from Hugging Face Hub
- **Web UI**: Comprehensive Gradio-based interface for all operations
- **CLI Interface**: Command-line tools for training and inference
- **Research Features**: Implementation of cutting-edge techniques (FlashAttention, Mamba SSM, etc.)

## 📦 Installation

### Prerequisites

- Python 3.10+ (3.10, 3.11, or 3.12 recommended)
- PyTorch 2.0+
- CUDA Toolkit (optional, for GPU acceleration)

### Quick Install

```bash
# Clone the repository
git clone https://github.com/QKV-Core/QKV-Core.git
cd QKV-Core

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install GGUF support (optional, for GGUF models)
# See GGUF_INSTALL.md for platform-specific instructions
```

## 🎯 Quick Start

### Web Interface

```bash
python launch_web_ui.py
```

Then open your browser to `http://localhost:7861`

### Command Line Interface

```bash
# Train a tokenizer
python cli/run.py train-tokenizer --corpus data/sample_corpus.txt --output tokenizer/my_tokenizer.pkl

# Train a model
python cli/run.py train --data data/sample_corpus.txt --tokenizer tokenizer/my_tokenizer.pkl

# Chat with a model
python debug_chat.py
```

## 📚 Documentation

- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Comprehensive contribution guidelines
- **[GGUF_INSTALL.md](GGUF_INSTALL.md)**: GGUF model installation guide
- **[docs/RESEARCH_IMPLEMENTATIONS.md](docs/RESEARCH_IMPLEMENTATIONS.md)**: Research paper implementations

## 🏗️ Project Structure

```
QKV-Core/
├── core/              # Core transformer implementation
├── models/            # Inference engines
├── training/          # Training implementations
├── web_ui/            # Gradio web interface
├── cli/               # Command-line interface
├── utils/             # Utility modules
└── docs/              # Documentation
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built on the fundamental Query-Key-Value attention mechanism that powers transformer architectures. QKV Core brings production-grade AI capabilities to your fingertips.

---

**QKV Core - Where Query, Key, and Value Create Intelligence** 🚀

## Running on 4GB Pascal GPU (Pascal 4GB BitNet flow) ⚙️

This project includes features and helper scripts to support running a hybrid BitNet model on limited GPUs (4GB Pascal-class). Key options:

- Use the model factory to create a smaller model for development: `create_transformer_model(config, mode='small')`.
- Enable accelerate offload by setting env var `USE_ACCELERATE=1` and optionally use bitsandbytes quantization with `USE_BNB=1`.
- If you encounter fragmentation OOM, try setting `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` in the environment.

Quick example (POSIX shell):

```bash
# Optional: install offload/quantization libraries
pip install accelerate bitsandbytes

# Run the BitNet hybrid runner with accelerate offload enabled
USE_ACCELERATE=1 USE_BNB=0 python -m qkv_core.run_bitnet_hybrid

# For development / testing on a machine without GPU (fast fallback)
python -m qkv_core.run_bitnet_hybrid
```

Notes:
- Offload/dispatch behavior depends on `accelerate` version and available system resources.
- `bitsandbytes` is Linux-focused and may not be available on Windows; the code will skip quantization if not available.


<br>
<hr>
<div align="right">
  <sub>Built with ❤️ for the Open Source AI Community by <a href="https://github.com/broxytr">Hüseyin Kama</a></sub>
</div>
