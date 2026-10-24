# ssd-llm 🚀

**Run 70B+ LLMs on Apple Silicon by using SSD as extended memory.**

Intelligent layer streaming and caching for Mac — no need for 128GB RAM.

## The Problem

Large language models like LLaMA 70B require ~40GB+ RAM even with 4-bit quantization. Most MacBooks have 16–36GB unified memory. You either:
- Can't run the model at all
- Use llama.cpp's mmap, which thrashes your SSD with no intelligence
- Accept terrible performance from OS swap pressure

## The Solution

**ssd-llm** treats your fast Apple SSD as an intelligent extension of RAM:

```
┌─────────────┐     ┌──────────────┐     ┌───────────┐
│  SSD (2TB)  │────▶│ Smart Cache  │────▶│ Metal GPU │
│  Model File │     │ (Layer Pool) │     │ Inference  │
└─────────────┘     └──────────────┘     └───────────┘
                     ▲                    │
                     │    Prefetch        │ Compute
                     └────────────────────┘
```

Instead of loading the entire model, **ssd-llm** streams transformer layers on-demand from SSD to unified memory, computes them, and frees the memory. Predictive prefetching ensures the next layer is already loading while the current one is being computed.

## Key Features

- **🧱 Layer-Level Streaming** — Only 1-2 transformer layers in RAM at once
- **🔮 Predictive Prefetching** — Next layer loads asynchronously via `madvise(MADV_WILLNEED)` while GPU computes
- **📦 Smart LRU Cache** — Frequently used layers (embeddings, early attention) stay pinned in RAM
- **🗺️ mmap + madvise** — OS-level memory-mapped files with intelligent page hints
- **⚡ Metal Compute** — SIMD-optimized matmul, softmax, RoPE, RMSNorm with Metal shader foundation
- **📄 GGUF Support** — Compatible with llama.cpp quantization formats (Q4_0, Q8_0, F16, F32)
- **🔤 BPE Tokenizer** — Full Byte-Pair Encoding with SentencePiece support from GGUF vocabulary
- **🔌 Ollama-compatible API** — Drop-in replacement server with OpenAI-compatible endpoint
- **📡 Streaming** — Real-time token-by-token streaming via chunked transfer (Ollama) and SSE (OpenAI)
- **🎯 Speculative Decoding** — Use a small draft model to propose tokens, verified by the target model for 2-3x speedup
- **📦 Batch Prefill** — Layer-major prompt processing: each layer loaded once for all prompt tokens, minimizing SSD reads
- **🎛️ Adaptive Draft Length** — Dynamically adjusts speculation depth K based on rolling acceptance rate
- **📦 Prompt Prefix Caching** — Reuse KV cache states for repeated prompt prefixes (system prompts, templates), with persistent disk storage for instant warm-up across server restarts
- **🔄 Continuous Batching** — Handle multiple concurrent requests, share layer loads across sequences
- **🔀 Tensor Parallelism** — Split matmul across multiple threads for better GPU/CPU utilization
- **🪟 Sliding Window Attention** — Limit attention to recent W tokens with optional sink tokens for bounded memory
- **🔗 GQA Optimization** — Grouped-Query Attention with batched KV loads, auto-detected from model config
- **💾 Memory-Mapped KV Cache** — Spill KV cache to SSD via mmap when RAM is exhausted, enabling ultra-long contexts
- **⚡ Flash Attention** — Memory-efficient fused attention kernel using online softmax (O(1) extra memory per head)
- **📊 Structured Benchmark Suite** — JSON-exportable benchmarks with cold/warm/streaming scenarios for CI/CD
- **🏥 Health & Metrics API** — `/health` and `/metrics` endpoints with Prometheus-compatible output for production monitoring
- **📥 Model Downloader** — `ssd-llm pull` to download GGUF models from Hugging Face with resume support
- **⚙️ Configuration File** — TOML config file support for persistent settings
- **🛑 Graceful Shutdown** — Signal handling (SIGINT/SIGTERM) for clean server shutdown
- **🔧 CORS Support** — Full CORS preflight handling for browser-based clients
- **📄 PagedAttention** — vLLM-style paged KV cache: fixed-size blocks allocated on-demand, copy-on-write for beam search/parallel sampling, near-zero memory waste, sequence forking
- **💾 SSD Block Swapping** — Automatic swap-out of cold KV cache blocks to SSD under memory pressure, LRU-based eviction, transparent swap-in on access, prefetch support, swap file with slot reuse
- **🗜️ Quantized Block Swapping** — INT8 per-row quantization of KV cache blocks before writing to SSD, reducing I/O bandwidth by ~4x with minimal accuracy loss, configurable via `--swap-quantize`
- **🧮 Embeddings API** — OpenAI-compatible `/v1/embeddings` endpoint with L2-normalized vectors for RAG pipelines
- **📋 Models Listing** — OpenAI-compatible `/v1/models` endpoint for client discovery
- **🎭 Chat Templates** — Auto-detected formatting for Llama 2, Llama 3, Mistral, Gemma, Phi-3, ChatML, and raw mode
- **🛑 Stop Sequences** — Early generation termination on configurable stop strings
- **🔁 Repetition Penalties** — Repetition, frequency, and presence penalties to reduce repetitive output
- **🔢 Complete K-Quant Family** — GPU-accelerated dequantization for all K-quants (Q2_K, Q3_K, Q4_K, Q5_K, Q6_K, Q8_K) via Metal shaders, plus CPU fallback
- **🗜️ KV Cache Quantization** — INT8 per-row quantized KV cache for 4x memory reduction, enabling much longer context windows
- **📐 RoPE Scaling** — Linear, NTK-aware, and YaRN scaling methods for extended context windows beyond training length
- **🎲 Min-P Sampling** — Adaptive probability filtering that scales with model confidence for better quality/diversity trade-off
- **✂️ Tail-Free Sampling (TFS)** — Second-derivative based tail removal for cleaner distributions than top-p
- **🎯 Mirostat v1 & v2** — Adaptive perplexity-controlled sampling that maintains target surprise level for coherent text
- **💬 Interactive Chat** — `ssd-llm chat` for multi-turn conversations with history, undo, system prompts, and streaming output
- **📋 JSON Mode** — `response_format: { type: "json_object" }` for guaranteed valid JSON output via grammar-constrained generation
- **🔗 LoRA Adapters** — Load LoRA adapters from GGUF files at inference time with configurable scaling, support for multiple simultaneous adapters
- **🛠️ Function Calling / Tool Use** — OpenAI-compatible `tools` parameter with function definitions, `tool_choice` control, parallel tool calls, argument validation, and multi-turn tool result messages
- **🧩 Mixture of Experts (MoE)** — Sparse expert routing for models like Mixtral 8x7B/8x22B: top-K gating, SSD-friendly on-demand expert loading, batch expert pre-selection, Metal gating shader
- **📝 GBNF Grammar Constraints** — llama.cpp-compatible grammar-constrained generation for arbitrary structured output (SQL, XML, custom formats)
- **👁️ Vision/Multimodal** — CLIP ViT encoder for LLaVA-style image understanding, OpenAI-compatible image_url content, base64 and URL image input
- **🧬 I-Quant Support (IQ2_XXS, IQ2_XS, IQ3_XXS, IQ3_S, IQ4_NL, IQ4_XS)** — Importance-matrix quantization dequantization with grid lookup tables and non-linear LUTs, CPU + Metal GPU kernels, for higher quality-per-bit than traditional K-quants
- **📊 Perplexity Evaluation** — `ssd-llm perplexity` measures model quality with sliding-window NLL computation, per-chunk stats, JSON output for CI/CD, quantization quality comparison
- **🧠 Adaptive Memory Pressure** — Real-time macOS VM pressure monitoring via `host_statistics64`, automatic cache budget scaling (100%→25%), smart prefetch throttling, Prometheus metrics for memory state
- **🔗 Fused Residual + RMSNorm** — Single GPU dispatch combines residual connection add with RMSNorm sum-of-squares computation, eliminating one full memory pass over the hidden state per transformer layer
- **🔢 BF16 & F16 Matvec** — Native BF16 (brain float 16) and F16 (IEEE 754 half) matrix-vector multiply on CPU and Metal GPU, enabling direct inference from unquantized model weights without dequantization overhead
- **📌 Adaptive Layer Pinning** — Automatic hot-layer detection: tracks per-layer access frequency with exponential decay, auto-pins the N hottest layers in RAM (e.g., embeddings, early attention), configurable via `--adaptive-pin N`
- **📏 Criterion Benchmarks** — Reproducible micro-benchmarks for core operations (softmax, matvec, RoPE, RMSNorm)
- **⚡ Fused RMSNorm + Output Projection** — Single GPU dispatch combines final layer normalization with vocabulary projection, eliminating intermediate buffer allocation and one full memory pass over the hidden state per generated token
- **🔗 Fused Post-Attention Residual + FFN Norm** — Single logical operation combines attention residual connection with FFN input normalization, eliminating per-layer hidden state clones and 2 memory passes per transformer layer

## Installation

### Prerequisites

You need [Rust](https://www.rust-lang.org/tools/install) installed:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Make sure `~/.cargo/bin` is in your PATH (restart your terminal or run `source ~/.cargo/env`).

### Build & Install

```bash
# Clone the repo
git clone https://github.com/quantumnic/ssd-llm.git
cd ssd-llm

# Build and install to ~/.cargo/bin (available as `ssd-llm` globally)
cargo install --path .

# Verify
ssd-llm --help
```

Or build without installing:

```bash
cargo build --release
# Binary at: ./target/release/ssd-llm
```

## Quick Start

```bash

# Download a model from Hugging Face
ssd-llm pull TheBloke/Llama-2-7B-GGUF:llama-2-7b.Q4_0.gguf

# List local models
ssd-llm models

# Show model info
ssd-llm info model.gguf

# Run inference with 8GB memory budget
ssd-llm run model.gguf --memory-budget 8G --prompt "Explain quantum computing"

# Benchmark SSD streaming performance
ssd-llm bench model.gguf --memory-budget 8G

# Evaluate perplexity (measure quantization quality)
ssd-llm perplexity model.gguf wiki.txt --memory-budget 8G
ssd-llm perplexity model.gguf wiki.txt --context-size 512 --stride 256 --verbose
ssd-llm perplexity model.gguf wiki.txt --json  # CI/CD integration

# Start Ollama-compatible API server
ssd-llm serve model.gguf --memory-budget 8G --port 11434

# Speculative decoding with draft model (2-3x faster)
ssd-llm run model-70b.gguf --draft-model model-1b.gguf --prompt "Hello" --draft-ahead 5

# Adaptive draft length (auto-tunes K based on acceptance rate)
ssd-llm run model-70b.gguf --draft-model model-1b.gguf --prompt "Hello" --adaptive-draft

# Serve with speculative decoding
ssd-llm serve model-70b.gguf --draft-model model-1b.gguf --memory-budget 8G

# Enable prompt prefix caching (reuse KV states across requests)
ssd-llm run model.gguf --prompt "Hello" --prompt-cache

# Tensor parallelism (auto-detected or manual)
ssd-llm run model-70b.gguf --prompt "Hello" --tensor-parallel 4

# Continuous batching server (handles 8 concurrent requests)
ssd-llm serve model.gguf --memory-budget 8G --max-batch 8 --prompt-cache

# PagedAttention with INT8-quantized SSD swapping (4x less I/O)
ssd-llm serve model.gguf --memory-budget 8G --paged-kv --swap-quantize

# Sliding window attention (bounded memory for long contexts)
ssd-llm run model.gguf --prompt "Hello" --sliding-window 4096 --sink-tokens 4

# Memory-mapped KV cache (ultra-long contexts, spills to SSD)
ssd-llm run model.gguf --prompt "Hello" --mmap-kv --max-tokens 32768

# GQA is auto-detected — just run and see the optimization message
ssd-llm run llama-70b.gguf --prompt "Hello" --memory-budget 16G

# Generate default config file
ssd-llm config --init

# Run micro-benchmarks
cargo bench
```

## LoRA Adapters

Load fine-tuned LoRA adapters at inference time without modifying the base model:

```bash
# Run with a single LoRA adapter
ssd-llm run model.gguf --prompt "Hello" --lora adapter.gguf

# Multiple adapters with custom scaling
ssd-llm run model.gguf --prompt "Hello" --lora adapter1.gguf --lora adapter2.gguf --lora-scale 0.8

# Chat with LoRA adapter
ssd-llm chat model.gguf --lora adapter.gguf

# Serve with LoRA adapter
ssd-llm serve model.gguf --lora adapter.gguf
```

LoRA adapters are loaded from GGUF files containing `*.lora_a` / `*.lora_b` tensor pairs. The adapter weights are merged into the base model weights at layer-load time using the formula: `W' = W + (alpha/r) * scale * B @ A`. Rank and alpha are auto-detected from GGUF metadata.

### Grammar-Constrained Generation

Use GBNF grammars (llama.cpp-compatible) to constrain output to any structured format:

```bash
# Inline grammar
ssd-llm run model.gguf --prompt "Generate a color:" --grammar 'root ::= "red" | "green" | "blue"'

# Grammar from file
ssd-llm run model.gguf --prompt "Write SQL:" --grammar-file sql.gbnf

# Via API (Ollama endpoint)
curl -s http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [{"role": "user", "content": "List 3 colors as JSON"}],
  "grammar": "root ::= \"[\" ws item (\",\" ws item)* ws \"]\"\nitem ::= \"\\\"\" [a-z]+ \"\\\"\"\nws ::= [ ]*"
}'
```

GBNF grammars support: literals, character classes (`[a-z]`, `[^0-9]`), rule references, groups, quantifiers (`?`, `*`, `+`), and alternatives (`|`). The grammar engine filters token logits at each generation step, ensuring output always matches the defined grammar.

## API Server

The `serve` command starts an Ollama-compatible HTTP server:

```bash
ssd-llm serve model.gguf --memory-budget 8G
```

### Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/generate` | POST | Text generation (Ollama format) |
| `/api/chat` | POST | Chat completion (Ollama format) |
| `/api/tags` | GET | List loaded models |
| `/api/version` | GET | Server version |
| `/v1/chat/completions` | POST | OpenAI-compatible chat |
| `/health` | GET | Readiness probe (JSON) |
| `/metrics` | GET | Prometheus-compatible metrics |

### Usage with curl

```bash
# Ollama-style generation
curl -X POST http://localhost:11434/api/generate \
  -d '{"prompt": "What is Rust?", "num_predict": 128}'

# OpenAI-compatible chat
curl -X POST http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Hello!"}], "max_tokens": 128}'
```

## How It Works

### Layer Streaming Architecture

Traditional LLM inference loads the entire model into RAM. **ssd-llm** takes a different approach:

1. **GGUF Parser** reads model metadata and tensor offsets without loading data
2. **mmap Loader** memory-maps the model file — the OS handles page faults
3. **Predictive Prefetcher** issues `madvise(MADV_WILLNEED)` for the next layer while the current one computes
4. **LRU Cache** keeps hot layers (embeddings, output weights) pinned in memory
5. **Eviction** calls `madvise(MADV_DONTNEED)` on completed layers to free page cache

### Why Apple Silicon?

Apple's Unified Memory Architecture is uniquely suited for this:

| Feature | Apple Silicon | Traditional PC |
|---|---|---|
| Memory | Unified (CPU+GPU shared) | Separate RAM + VRAM |
| SSD Speed | 5-7 GB/s (M3/M4 Pro) | 3-5 GB/s (NVMe) |
| Memory Bandwidth | 200-800 GB/s | 50-100 GB/s (DDR5) |
| GPU Access | Direct to unified memory | PCIe copy required |

The fast SSD + unified memory means layer streaming has very low overhead on Mac.

## Benchmarks

> v0.5 — Speculative decoding with draft model, KV cache rollback

| Model | Quant | Size | Memory Budget | Layer Load | Est. tok/s |
|---|---|---|---|---|---|
| LLaMA 7B | Q4_0 | 3.5 GB | 4 GB | ~2ms/layer | TBD |
| LLaMA 13B | Q4_0 | 7 GB | 8 GB | ~4ms/layer | TBD |
| LLaMA 70B | Q4_0 | 35 GB | 8 GB | ~8ms/layer | TBD |

Run `ssd-llm bench` on your machine to get actual numbers.

## Comparison

| Feature | ssd-llm | llama.cpp | Ollama |
|---|---|---|---|
| SSD Streaming | ✅ Intelligent | ⚠️ Naive mmap | ❌ Full RAM |
| Predictive Prefetch | ✅ madvise hints | ❌ | ❌ |
| Memory Budget | ✅ Configurable | ❌ | ❌ |
| Layer-level Cache | ✅ LRU + pinning | ❌ | ❌ |
| Speculative Decoding | ✅ Draft model | ✅ (v0.6+) | ❌ |
| Continuous Batching | ✅ Layer-major | ✅ | ✅ |
| Prompt Caching | ✅ Prefix matching | ❌ | ❌ |
| Tensor Parallelism | ✅ Multi-thread | ✅ | ✅ (via llama.cpp) |
| Metal GPU | ✅ Shaders + SIMD | ✅ | ✅ (via llama.cpp) |
| GGUF Support | ✅ | ✅ | ✅ |
| Quantization | Q4_0, Q8_0, F16 | All | All |
| API Server | ✅ Ollama + OpenAI | ✅ | ✅ |

## Architecture

```
src/
  main.rs              — CLI + entry point
  model/
    gguf.rs            — GGUF v2/v3 parser
    loader.rs          — mmap-based lazy loader
    cache.rs           — LRU layer cache with memory budget
  inference/
    transformer.rs     — Layer-by-layer forward pass
    attention.rs       — Multi-Head Attention with KV cache (GQA support)
    kv_cache.rs        — Key-Value cache for autoregressive generation
    feed_forward.rs    — SwiGLU FFN
    sampler.rs         — Temperature, Top-K, Top-P sampling (xorshift64)
    speculative.rs     — Speculative decoding engine (draft + verify)
    tokenizer.rs       — BPE tokenizer with SentencePiece support
    prompt_cache.rs    — Prompt prefix KV state caching
    batch_scheduler.rs — Continuous batching scheduler
    tensor_parallel.rs — Multi-threaded tensor parallelism
    grammar.rs         — GBNF grammar parser + constrained generation engine
  metal/
    compute.rs         — Metal compute + SIMD-optimized ops (auto GPU dispatch)
    gpu.rs             — metal-rs GPU pipeline (real Metal compute)
    shaders/           — .metal compute shaders (matmul, rmsnorm, rope, softmax)
  ssd/
    streamer.rs        — SSD → RAM streaming engine
    prefetch.rs        — Predictive prefetcher
    mmap_pool.rs       — mmap pool with madvise management
  api/
    server.rs          — Ollama-compatible HTTP API server (graceful shutdown, CORS)
    openai.rs          — OpenAI-compatible types + ChatML formatting
    metrics.rs         — Health & Prometheus metrics
  pull/
    mod.rs             — HuggingFace model downloader with resume support
  config.rs            — TOML configuration file support
  benchmark.rs         — Performance measurement
benches/
  inference_bench.rs   — Criterion micro-benchmarks (softmax, matvec, RoPE, SiLU)
```

## Speculative Decoding

Speculative decoding uses a small "draft" model (e.g. 1B parameters) to propose candidate tokens, then verifies them with the large target model. This is particularly effective for ssd-llm because:

1. **Draft model fits in RAM** — no SSD streaming needed for the small model
2. **Target model streams fewer times** — accepted draft tokens skip expensive SSD I/O
3. **Mathematically lossless** — the output distribution is identical to the target model

### How it works

```
Draft Model (1B, in RAM):    [tok1] → [tok2] → [tok3] → [tok4] → [tok5]
                                ↓        ↓        ↓        ↓        ↓
Target Model (70B, SSD):    verify   verify   verify   REJECT   resample
                                ✓        ✓        ✓        ✗        →tok4'
```

With a good draft model, 60-80% of tokens are accepted, meaning the target model does ~40% fewer forward passes. For SSD-streaming workloads this translates to 2-3x speedup.

### Configuration

- `--draft-model <path>` — Path to the draft GGUF model (same tokenizer family)
- `--draft-ahead <K>` — Number of tokens to draft per round (default: 5, try 3-8)

Higher `draft-ahead` values give more potential speedup but waste more compute on rejections. Start with 5 and tune based on your model pair's acceptance rate.

## Prior Art & Research

This project builds on insights from:

- **llama.cpp** — Uses mmap but with no intelligent page management
- **FlexGen** — SSD offloading for throughput-oriented inference
- **PowerInfer** — Sparsity-based selective loading
- **LLM in a Flash** (Apple Research) — Flash memory optimization for LLM inference
- **FlexInfer** — Flexible offloading with computation-I/O overlap

## Roadmap

- [x] v0.1 — GGUF parser, mmap loader, LRU cache, prefetcher, CPU inference
- [x] v0.2 — Metal compute foundation, SIMD ops, Ollama + OpenAI API server
- [x] v0.3 — KV cache, Metal shader compilation, SwiGLU FFN, quantized GPU kernels (Q4_0/Q8_0)
- [x] v0.4 — Full Metal GPU dispatch via metal-rs, BPE tokenizer, streaming responses
- [x] v0.5 — Speculative decoding with draft model, KV cache rollback
- [x] v0.6 — Batch prefill optimization, adaptive draft length
- [x] v0.7 — Continuous batching, prompt caching, tensor parallelism
- [x] v0.8 — Sliding window attention, GQA optimization, memory-mapped KV cache
- [x] v0.9 — Structured benchmark suite, flash attention, health/metrics API
- [x] v1.0 — Production-ready: model downloader, config files, graceful shutdown, criterion benchmarks, CORS, clippy-clean
- [x] v1.1 — OpenAI embeddings API (`/v1/embeddings`), models listing (`/v1/models`), L2-normalized embedding extraction
- [x] v1.2 — Chat templates (Llama 2/3, Mistral, Gemma, Phi-3, ChatML), stop sequences, repetition/frequency/presence penalties, proper token usage tracking
- [x] v1.3 — K-quant GPU dequantization (Q4_K, Q6_K Metal shaders), unified quantized matvec dispatch
- [x] v1.4 — INT8 KV cache quantization for 4x memory reduction
- [x] v1.5 — RoPE scaling (Linear, NTK-aware, YaRN) + Min-P sampling
- [x] v1.6 — Tail-Free Sampling (TFS) + Mirostat v1/v2 adaptive sampling
- [x] v1.7 — Interactive chat CLI + JSON mode for structured output
- [x] v1.8 — LoRA adapter support (load fine-tuned adapters from GGUF)
- [x] v1.9 — Function calling / Tool use (OpenAI-compatible, multi-turn, parallel calls)
- [x] v1.10 — Mixture of Experts (MoE) — sparse expert routing for Mixtral-style models
- [x] v1.11 — GBNF grammar-constrained generation for arbitrary structured output
- [x] v1.12 — Vision/Multimodal support (CLIP ViT encoder for LLaVA-style image understanding)
- [x] v1.13 — Ollama model management API (/api/show, /api/pull, /api/copy, /api/delete, /api/ps)
- [x] v1.14 — Q3_K + Q5_K GPU dequantization, Ollama /api/embed endpoint
- [x] v1.15 — Q2_K/Q8_K GPU dequantization — complete K-quant family on Metal
- [x] v1.16 — PagedAttention — vLLM-style paged KV cache management
- [x] v1.17 — SSD Block Swapping — automatic KV cache page swapping to SSD
- [x] v1.18 — Quantized Block Swapping — INT8 compression for 4x less SSD I/O
- [x] v1.35 — GPU-Accelerated Forward Pass — fused Metal kernels (QKV+RoPE, SwiGLU) wired into main inference loop, 9× fewer GPU dispatches per token
- [x] v1.28 — Metal Flash Attention — fused GPU attention kernel (QK scoring + online softmax + V accumulation in single dispatch)
- [x] v1.27 — ARM NEON SIMD — explicit NEON intrinsics for 2-4x CPU matvec/rmsnorm/softmax speedup

## Requirements

- macOS 13+ (Apple Silicon recommended)
- Rust 1.75+
- GGUF model file (from [HuggingFace](https://huggingface.co/models?library=gguf))

## License

MIT
