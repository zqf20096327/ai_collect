# ⚡ Awesome Bare-Metal AI (2026–2027)

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Tracking: 2026-2027](https://img.shields.io/badge/Roadmap-2026--2027-blueviolet.svg)](#)

> A curated leaderboard, benchmark index, and definitive guide to **ultra-lightweight, zero-dependency, bare-metal AI engines** written in pure C, C++, Rust, Zig, and Assembly for local LLMs, edge inference, vector search, and autonomous agents.

---

## 🎯 The Bare-Metal AI Manifesto

In 2024–2025, deploying AI often meant 2GB Docker images, multi-gigabyte Python runtimes, and complex distributed clusters. 

In **2026–2027, the paradigm has shifted**:
1. **Zero-Bloat Architecture:** Production edge AI demands sub-millisecond execution, sub-100MB memory footprints, and single-binary or zero-dependency libraries.
2. **Hardware Direct Access:** Maximum performance from modern CPUs using unrolled SIMD (AVX2, AVX-512, ARM NEON) and dedicated tensor registers without heavy BLAS overhead.
3. **Local & Autonomous:** AI agents require instant local episodic memory, embedded vector indexing, and token-by-token CPU inference without cloud network latency or API bills.

---

## 📊 2026–2027 Benchmark & Footprint Leaderboard

| Category | Project | Language | Binary Footprint | Latency / Throughput | Zero External Deps? | Key Hardware Target |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **Vector Search** | [**NanoVector**](https://github.com/eminsk/nanovector) | Pure C99 | **~120 KB** | **96 µs** (2.85M vecs/s) | **Yes (0 deps)** | AVX2+FMA, ARM NEON, FASM |
| **Vector Search** | [USearch](https://github.com/unum-cloud/usearch) | C++11 | ~800 KB | ~120 µs (ANN HNSW) | Yes (Header-only) | AVX-512, NEON, SVE |
| **Vector Search** | [FAISS](https://github.com/facebookresearch/faiss) | C++ / Python | ~25 MB+ | Variable (Large batch) | No (BLAS / OpenMP) | AVX2, CUDA |
| **Vector Search** | [sqlite-vss](https://github.com/asg017/sqlite-vss) | C / C++ | ~2.5 MB | ~350 µs | Depends on SQLite | CPU |
| **GEMM / Tensors** | [**NanoGEMM**](https://github.com/eminsk/nanogemm) | Pure C99 | **~100 KB** | **Sub-microsecond** | **Yes (0 deps)** | AVX2, ARM NEON, FASM |
| **GEMM / Tensors** | [BLIS](https://github.com/flame/blis) | C99 | ~5 MB | High (Large matrix) | Yes | AVX-512, AMX, NEON |
| **LLM Inference** | [llama.cpp](https://github.com/ggml-org/llama.cpp) | C / C++ | ~15 MB | Fast (CPU/GPU GGUF) | Yes | AVX2, Metal, CUDA, Vulkan |
| **1-Bit LLM** | [bitnet.cpp](https://github.com/microsoft/BitNet) | C++ | ~10 MB | Ultra-low wattage | Yes | AVX2, AVX-512, NEON |
| **Screen Capture** | [**ScreenCapture Pro**](https://github.com/eminsk/screenvideo) | FASM / C / Py | **~190 KB** | Zero-memory pipe | Yes | Win32 x64, WASAPI, SIMD |
| **Desktop Memory** | [**NanoRecall**](https://github.com/eminsk/nanorecall) | C99 / Py | **<200 KB** | **0.28 ms** (Exact search) | **Yes (0 cloud)** | AVX2, Win32, WinRT OCR |
| **Agent JIT / Runtimes** | [**AgentJIT**](https://github.com/eminsk/agentjit) | Python / AST | **<50 KB** | **0.08 ms** (185,000x faster) | **Yes (0 deps)** | CPU, Free-Threaded (No-GIL) |
| **Speech / STT** | [whisper.cpp](https://github.com/ggerganov/whisper.cpp) | C / C++ | ~8 MB | Sub-realtime on CPU | Yes | AVX2, Metal, NEON |

---


## 🔍 Table of Contents

- [Vector Search & Episodic Agent Memory](#-vector-search--episodic-agent-memory)
- [Matrix Math & GEMM Microkernels](#-matrix-math--gemm-microkernels)
- [AI Agent JIT & Workflow Compilers](#-ai-agent-jit--workflow-compilers)
- [Local LLM & SLM Inference Engines](#-local-llm--slm-inference-engines)
- [1-Bit & Ternary Quantization Engines](#-1-bit--ternary-quantization-engines)
- [Edge Speech, Audio & Vision](#-edge-speech-audio--vision)
- [Hardware Acceleration Standards (SIMD/ISA)](#-hardware-acceleration-standards)
- [Contributing](#-contributing)

---

## 🧠 Vector Search & Episodic Agent Memory

Ultra-compact, low-latency vector indexers engineered for local RAG and long-term memory in autonomous agents:

* [**NanoVector**](https://github.com/eminsk/nanovector) — Minimalist bare-metal vector search and episodic memory engine in **~120 KB** of pure C99 with AVX2/FMA, ARM NEON, and FASM x64 optimizations. Ingests 2.85M vecs/sec, achieves 96 µs search latency on standard CPUs, single-file `.nvec` binary persistence, in-kernel metadata filtering (`$eq`, `$in`, etc.), and 1-line drop-in LangChain integration with zero external dependencies.
* [**NanoRecall**](https://github.com/eminsk/nanorecall) — 100% private, zero-cloud desktop memory and screen search engine in **<200 KB**. Open-source alternative to Microsoft Windows Recall running on standard CPUs with zero NPU or cloud required. Powered by NanoVector AVX2 engine.
* [USearch](https://github.com/unum-cloud/usearch) — Single-header HNSW and Cosine distance search library in C++11, optimized for AVX-512 and ARM SVE.
* [FAISS](https://github.com/facebookresearch/faiss) — Facebook AI Research's foundational library for dense vector clustering and approximate nearest neighbor search at massive multi-million scale.
* [sqlite-vss](https://github.com/asg017/sqlite-vss) — SQLite extension for vector search based on Faiss, enabling SQL-driven semantic retrieval.
* [Annoy](https://github.com/spotify/annoy) — Classic C++ library with Python bindings for approximate nearest neighbors with memory-mapped read-only index files.

---

## ⚡ Matrix Math & GEMM Microkernels

Bare-metal General Matrix Multiplication (GEMM) engines that eliminate BLAS dispatch overhead for latency-critical small-to-medium tensors:

* [**NanoGEMM**](https://github.com/eminsk/nanogemm) — High-performance ~100KB register-tiled GEMM microkernel in pure C and hand-crafted AVX2/FMA & ARM NEON assembly. Bypasses OpenBLAS/MKL function-call dispatch barriers, achieving up to 2.8x speedups over NumPy on small-to-medium matrices (16x16 to 128x128) essential for real-time CPU token inference and Kalman tracking.
* [BLIS](https://github.com/flame/blis) — Modular, high-performance dense linear algebra framework designed as a modern C99 alternative to conventional BLAS.
* [OpenBLAS](https://github.com/OpenMathLib/OpenBLAS) — Widely adopted, optimized open-source BLAS library with extensive architecture-specific assembly kernels.

---

## ⚡ AI Agent JIT & Workflow Compilers

Just-in-time compilers that trace dynamic, stochastic multi-step AI agent trajectories and compile them into deterministic, sub-millisecond Python code with zero token consumption:

* [**AgentJIT**](https://github.com/eminsk/agentjit) — Just-In-Time Compiler for AI Agent Trajectories. Compiles flaky, 30-second multi-step LLM workflows into **0.08 ms** deterministic Python code with zero token cost (185,000x speedup on warm paths). Features speculative input guards, automatic bailout / de-optimization runtime, and native support for free-threaded Python 3.13t/3.14t (No-GIL PEP 703) with zero external dependencies (`pip install agentjit`).

---

## 🤖 Local LLM & SLM Inference Engines

C/C++ runtimes capable of serving Large and Small Language Models directly on consumer laptops, edge gateways, and IoT devices without cloud APIs:

* [llama.cpp](https://github.com/ggml-org/llama.cpp) — The gold standard for CPU and mixed CPU/GPU LLM inference in pure C/C++ with support for GGUF quantization formats (Q4, Q8, K-quants).
* [Ollama](https://github.com/ollama/ollama) — Seamless CLI and local daemon for managing, bundling, and running GGUF models on macOS, Windows, and Linux.
* [mamba.c](https://github.com/state-spaces/mamba) / [rwkv.cpp](https://github.com/saharNooby/rwkv.cpp) — Ultra-fast linear attention and State Space Model (SSM) inference in pure C/C++ offering constant memory consumption over arbitrary context lengths.
* [vLLM](https://github.com/vllm-project/vllm) — High-throughput, memory-efficient serving engine featuring PagedAttention for production LLM deployments.

---

## 🧊 1-Bit & Ternary Quantization Engines

Next-generation sub-byte inference architectures designed for extreme wattage efficiency:

* [bitnet.cpp](https://github.com/microsoft/BitNet) — Official Microsoft inference framework for 1-bit LLMs (e.g. BitNet b1.58), featuring optimized native SIMD kernels for ternary (-1, 0, +1) weight matrix multiplication on x86 and ARM.
* [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) — Activation-aware Weight Quantization for 4-bit transformer execution without accuracy loss.

---

## 🎙️ Edge Speech, Audio & Vision

Native multimedia and telemetry suites built for real-time edge processing:

* [whisper.cpp](https://github.com/ggerganov/whisper.cpp) — High-performance port of OpenAI's Whisper automatic speech recognition model in pure C/C++ with zero external dependencies.
* [**ScreenCapture Pro**](https://github.com/eminsk/screenvideo) — High-performance desktop screen recording and screenshot suite engineered in Win32 x64 FASM Assembly and Python. Features zero-memory direct-to-disk streaming, WASAPI loopback audio, two-pass animated GIF export, and real-time mouse click ripple HUD.
* [ncnn](https://github.com/Tencent/ncnn) — Tencent's high-performance neural network inference computing framework optimized specifically for mobile and embedded CPU/GPU platforms.

---

## 📐 Hardware Acceleration Standards

| Instruction Set | Typical Vector Width | Key Capability | Representative Platforms |
| :--- | :--- | :--- | :--- |
| **x86-64 AVX2 + FMA** | 256-bit (8 × float32) | Fused multiply-add, unrolled SIMD | Modern Intel Core / AMD Ryzen CPUs |
| **x86-64 AVX-512** | 512-bit (16 × float32) | Masked vector ops, BF16/VNNI acceleration | Intel Xeon / AMD Zen 4/5 |
| **ARM NEON** | 128-bit (4 × float32) | Universal mobile and Apple Silicon vector math | Apple M-series, Cortex-A7x, Raspberry Pi 4/5 |
| **ARM SVE / SVE2** | Scalable (128–2048-bit) | Vector length agnostic HPC compute | AWS Graviton3/4, modern Neoverse cores |
| **RISC-V Vector (RVV)** | Variable | Open-standard vector extension | Edge AI microcontrollers, Kendryte K230 |

---

## 🤝 Contributing

Contributions from authors and maintainers are enthusiastically welcomed!

1. Please review [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria.
2. Projects must prioritize **minimalism, zero/low dependencies, and verifiable native performance**.
3. Submit a Pull Request with a concise description, architecture details, and benchmark metrics.

---

## 📜 License

To the extent possible under law, this work is dedicated to the public domain under the **[Creative Commons CC0 1.0 Universal License](LICENSE)**.
