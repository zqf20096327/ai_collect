<div align="center">

# sentinel-reverse

### AI-Powered Autonomous Binary Reverse Engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Apple Silicon](https://img.shields.io/badge/Apple_Silicon-Optimized-black.svg?style=for-the-badge&logo=apple&logoColor=white)](#requirements)
[![MLX](https://img.shields.io/badge/MLX-Framework-orange.svg?style=for-the-badge)](#mlx-engine)
[![PyTorch MPS](https://img.shields.io/badge/PyTorch-MPS_GPU-red.svg?style=for-the-badge&logo=pytorch&logoColor=white)](#mps-accelerator)

**The native AI reverse engineering engine from [Innora-Sentinel](https://innora.ai)**

*Zero API cost · Full data privacy · GPU-accelerated · Iterative analysis*

[English](README.md) · [中文](docs/README_ZH.md) · [日本語](docs/README_JA.md) · [한국어](docs/README_KO.md) · [Tiếng Việt](docs/README_VI.md) · [Español](docs/README_ES.md) · [Français](docs/README_FR.md) · [Deutsch](docs/README_DE.md) · [Português](docs/README_PT.md)

---

<img src="docs/assets/pipeline.svg" alt="sentinel-reverse pipeline" width="700">

</div>

## Why sentinel-reverse?

Traditional reverse engineering tools (IDA Pro, Ghidra, radare2, Binary Ninja) require **manual effort** for every function — reading assembly, inferring logic, naming variables, and detecting vulnerabilities. For a binary with 500+ functions, this takes **days to weeks** of expert time.

**sentinel-reverse** automates this by combining:

| Feature | Traditional Tools | sentinel-reverse |
|---------|------------------|------------------|
| Function decompilation | Manual reading | **AI-driven** with iterative refinement |
| Variable naming | Manual guessing | **LLM semantic inference** |
| Vulnerability detection | Pattern matching | **Context-aware AI analysis** |
| Function similarity | Signature-based | **GPU-accelerated embeddings** |
| Analysis throughput | 5-10 functions/hour | **50-200 functions/hour** |
| Cost per analysis | $500+ (IDA Pro license) | **$0** (local inference) |
| Data privacy | Cloud-dependent tools | **100% local** — nothing leaves your machine |

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    sentinel-reverse CLI                       │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Phase 1  │ Phase 2  │ Phase 3  │ Phase 4  │    Phase 5      │
│ r2pipe   │ Format   │ MPS GPU  │ MLX AI   │    Report       │
│ Extract  │ Specific │ Embed    │ Iterate  │    Generate     │
│          │          │          │          │                 │
│ radare2  │ .NET     │ PyTorch  │ Local    │ Markdown        │
│ analysis │ bundle   │ Metal    │ LLM      │ + JSON          │
│          │ APK      │ Accel.   │ Inference│                 │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
                           │              │
                    ┌──────┴──────┐ ┌─────┴──────┐
                    │ MPS Accel.  │ │ MLX Engine │
                    │ - Embedding │ │ - Decompile│
                    │ - Similarity│ │ - Vuln Det.│
                    │ - Predict   │ │ - Algo Det.│
                    └─────────────┘ └────────────┘
```

### Core Components

| Module | Description |
|--------|-------------|
| **MLX Engine** | Local LLM inference via Apple MLX — 6 task-specific prompt templates, LRU cache, dual-layer fallback |
| **MPS Accelerator** | PyTorch Metal GPU — Transformer-based binary code embeddings, cosine similarity search, function name prediction |
| **Iterative Analyzer** | Multi-round confidence-driven analysis — 4 strategies (full_reverse, quick_decompile, security_audit, algorithm_recovery) |
| **Model Voter** | Multi-model voting — majority, weighted confidence, best-of strategies; local + cloud hybrid |
| **Checkpoint Manager** | Per-phase incremental saving — interrupt anytime, resume with `--resume` |

## Quick Start

### Requirements

- **macOS** with Apple Silicon (M1/M2/M3/M4) — *recommended*
- **Python 3.10+**
- **radare2** — binary analysis framework
- A local **MLX-compatible LLM** model (any instruction-tuned model in MLX format)

### Installation

```bash
# Install radare2
brew install radare2

# Install sentinel-reverse
pip install sentinel-reverse

# Or install from source
git clone https://github.com/sgInnora/sentinel-reverse.git
cd sentinel-reverse
pip install -e ".[all]"
```

### Download a Model

sentinel-reverse works with **any MLX-format instruction-tuned model**. Popular choices:

```bash
# Using mlx-community models (recommended)
pip install huggingface-hub
huggingface-cli download mlx-community/Qwen2.5-Coder-32B-Instruct-4bit --local-dir ~/models/qwen2.5-coder-32b-4bit

# Or any other MLX model
huggingface-cli download mlx-community/Llama-3.3-70B-Instruct-4bit --local-dir ~/models/llama-3.3-70b-4bit
```

### Usage

```bash
# Standard analysis (auto-discovers local models)
sentinel-reverse /path/to/binary

# Exhaustive mode — maximum GPU utilization, up to 15 iterative rounds
sentinel-reverse /path/to/binary -m exhaustive

# Security audit — focused on vulnerabilities and crypto
sentinel-reverse /path/to/binary -m security

# Quick scan — fast overview in ~2 rounds
sentinel-reverse /path/to/binary -m quick

# Specify model explicitly
sentinel-reverse /path/to/binary --model ~/models/my-model

# Resume from checkpoint after interruption
sentinel-reverse /path/to/binary --resume

# Detect binary format only
sentinel-reverse --detect /path/to/binary

# List available local models
sentinel-reverse --list-models

# Custom parameters
sentinel-reverse /path/to/binary --confidence 0.95 --max-rounds 20 --max-functions 100
```

### Analysis Modes

| Mode | Rounds | Confidence | Functions | Use Case |
|------|--------|------------|-----------|----------|
| `quick` | 2 | 0.70 | 50 | Fast triage, CTF challenges |
| `standard` | 5 | 0.80 | 200 | General reverse engineering |
| `exhaustive` | 15 | 0.92 | 9999 | Deep malware analysis, full binary RE |
| `security` | 8 | 0.85 | 500 | Vulnerability research, crypto auditing |

## Python API

```python
import asyncio
from sentinel_reverse import (
    MLXReverseEngine, FunctionContext, AnalysisTask,
    IterativeAnalyzer, MPSAccelerator,
)

async def analyze():
    # Initialize engine with your local model
    engine = MLXReverseEngine(
        model_path="~/models/your-mlx-model",
        max_tokens=4096,
        temperature=0.2,
    )
    engine.load_model()

    # Create function context from disassembly
    func = FunctionContext(
        address=0x401000,
        name="target_func",
        assembly="push rbp\nmov rbp, rsp\nsub rsp, 0x20\n...",
        size=256,
    )

    # Single-shot analysis
    result = engine.analyze(func, task=AnalysisTask.DECOMPILE)
    print(f"Decompiled: {result.output}")
    print(f"Confidence: {result.confidence}")

    # Iterative analysis (multi-round refinement)
    analyzer = IterativeAnalyzer(
        engine=engine,
        confidence_threshold=0.85,
        max_rounds=10,
    )
    iter_result = await analyzer.analyze(func, strategy="full_reverse")
    print(f"Final confidence: {iter_result.final_confidence}")
    print(f"Rounds: {iter_result.total_rounds}")
    print(f"Stop reason: {iter_result.stop_reason}")

    # GPU-accelerated embeddings
    accel = MPSAccelerator(embedding_dim=256)
    embedding = accel.compute_embedding(func.assembly, func.address)
    print(f"Embedding dim: {embedding.dimension}")

    engine.unload_model()

asyncio.run(analyze())
```

## Supported Binary Formats

| Format | Detection | Full Analysis |
|--------|-----------|---------------|
| ELF (Linux) | ✅ | ✅ |
| PE / PE32+ (Windows) | ✅ | ✅ |
| Mach-O (macOS/iOS) | ✅ | ✅ |
| .NET Single-File Bundle | ✅ | ✅ (embedded DLL extraction) |
| APK (Android) | ✅ | ✅ |
| DEX (Dalvik) | ✅ | ✅ |
| JAR/AAR (Java) | ✅ | ✅ |
| Universal Binary (Fat) | ✅ | ✅ |

## GPU Memory Management

> **Critical for Apple Silicon unified memory systems.**

sentinel-reverse uses **staged GPU memory management** to prevent system freezes:

```
Phase 3 (MPS): PyTorch loads Transformer encoder → computes embeddings
    ↓ torch.mps.empty_cache() + gc.collect()
Phase 4 (MLX): MLX loads LLM → runs iterative inference
    ↓ mx.clear_memory_cache() + model unload
```

MPS and MLX **cannot safely coexist** in unified memory simultaneously with large models. The pipeline automatically handles the transition.

## Output

Each analysis produces:

1. **Markdown report** — human-readable with tables, code blocks, and statistics
2. **JSON data** — machine-parseable with full analysis results and metadata

```
reverse_results/
├── target_reverse_20260205_143000.md    # Markdown report
├── target_reverse_20260205_143000.json  # JSON data
└── .checkpoint_target.json              # Auto-deleted on completion
```

## Performance

Benchmarked on Apple M3 Max (128GB unified memory):

| Metric | Value |
|--------|-------|
| Embedding computation (per function) | ~2-5ms (MPS GPU) |
| LLM inference (per round) | ~3-15s (model-dependent) |
| Functions per hour (standard mode) | ~80-150 |
| Functions per hour (quick mode) | ~200-400 |
| GPU memory usage | ~20-25GB (32B model, 6-bit) |
| Checkpoint overhead | <1% of analysis time |

## Project Origin

**sentinel-reverse** is the open-source extraction of the AI reverse engineering engine from [**Innora-Sentinel**](https://innora.ai), an enterprise-grade security analysis platform. It has been used in production for:

- Malware triage and deep analysis
- Vulnerability research on commercial software
- CTF competition automation
- Binary firmware reverse engineering
- .NET/Android application security auditing

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Development setup
git clone https://github.com/sgInnora/sentinel-reverse.git
cd sentinel-reverse
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Lint
ruff check sentinel_reverse/
```

## Related Projects

- [**InNora_Ares**](https://github.com/sgInnora/InNora_Ares) — Innora's AI-powered threat intelligence platform
- [**Innora-Sentinel**](https://innora.ai) — Enterprise security analysis platform (full product)

## License

[MIT License](LICENSE) — Free for commercial and non-commercial use.

This project is the **native AI reverse engine** from the **Innora-Sentinel** security platform, open-sourced by [Innora AI](https://innora.ai).

## Contact

| Channel | Contact |
|---------|---------|
| Website | [innora.ai](https://innora.ai) |
| Security | [security@innora.ai](mailto:security@innora.ai) |
| Sales | [sales@innora.ai](mailto:sales@innora.ai) |
| Support | [support@innora.ai](mailto:support@innora.ai) |
| Partnerships | [partnerships@innora.ai](mailto:partnerships@innora.ai) |
| Licensing | [licensing@innora.ai](mailto:licensing@innora.ai) |
| LinkedIn | [Feng Ning](https://www.linkedin.com/in/fengningarchitect) |
| Twitter/X | [@met3or](https://twitter.com/met3or) |

---

<div align="center">

**Built with ❤️ by [Innora AI](https://innora.ai)**

*Making binary reverse engineering accessible to everyone.*

</div>
