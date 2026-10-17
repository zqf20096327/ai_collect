# wgpu-llm

> A minimalist Llama inference engine written in Rust and WGSL.  
> Runs locally on **any GPU** — no CUDA required.

---
![wgpu-llm generating 24 tokens/sec natively on Snapdragon Adreno](assets/demo.webp)

## What Is This?

A from-scratch LLM inference engine that uses [wgpu v29](https://docs.rs/wgpu) to dispatch WGSL compute shaders for the full Transformer forward pass. No CUDA. No Python. No framework dependencies. Just Rust, raw shaders, and your GPU.

**Target architecture:** Llama (TinyLlama, Llama 2/3, and compatible fine-tunes).  
**Tested with:** [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

### Benchmarks (TinyLlama 1.1B, 256 tokens, default sampling)

| GPU | Mode | VRAM (weights) | tok/s |
|---|---|---|---|
| **RTX 3090** (Vulkan) | f16-weights | ~2.05 GiB | **66+** |
| **Adreno X1-85** (Vulkan) | INT8-b64 | 1.27 GiB | **32.8** |
| **Adreno X1-85** (Vulkan) | f16-weights | 2.05 GiB | **25.5** |

## Why?

- **The Copilot+ Hardware Gap** — I recently got a Snapdragon X Elite Copilot+ laptop and quickly realized my GPU was effectively a paperweight for local AI. Standard tools like LM Studio and the massive PyTorch ecosystem didn't support the integrated Adreno GPU, forcing everything onto the CPU. I didn't want to wait for the ecosystem to catch up, so I bypassed it entirely.
- **Portability** — runs on Windows, macOS, Linux, and anything with a Vulkan/Metal/DX12 driver.
- **Educational** — every layer of the Transformer is visible as a standalone WGSL shader. No framework magic.
- **Hackable** — small codebase, clear data flow, easy to experiment with.

## How It Was Built

`wgpu-llm` is an experiment in highly leveraged, AI-accelerated engineering. Starting from a detailed, human-designed architectural blueprint, the engine was scaffolded into working code in under 16 hours using a custom LLM orchestration pipeline with a human-in-the-loop approach.

To ensure the AI could write complex, low-level code without hallucinating or losing track of the architecture, the orchestrator was augmented with my own open-source tools:
* **[MCP_WGSL_Docs](https://github.com/Beledarian/MCP_WGSL_Docs):** Fed the LLM the exact, up-to-date WGSL specification so it could accurately implement features like tiled GEMM and compile-time f32/f16 switching across 12 standalone compute shaders.
* **[mcp-local-memory](https://github.com/Beledarian/mcp-local-memory):** Maintained persistent, strict architectural context across the entire 16-hour development sprint, ensuring the Rust host code and WGSL shaders stayed perfectly aligned.


## Installation

**Prerequisites:** [Rust and Cargo](https://rustup.rs) + a GPU with Vulkan, Metal, or DX12 support.

### Install from crates.io

```bash
cargo install wgpu-llm
```

### Build from source

```bash
git clone https://github.com/Beledarian/wgpu-llm.git
cd wgpu-llm
cargo build --release
```

## Quick Start

Download a compatible model (e.g., [TinyLlama-1.1B-Chat](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)) — the model directory needs `config.json`, `tokenizer.json`, and `*.safetensors`.

```bash
# If installed via cargo install:
wgpu-llm --model-dir /path/to/model --prompt "The overarching philosophy of stoicism teaches us" --max-tokens 256 --f16-weights

# If built from source:
cargo run --release --bin wgpu-llm -- --model-dir /path/to/model --prompt "The overarching philosophy of stoicism teaches us" --max-tokens 256 --f16-weights
```

The engine auto-detects your GPU capabilities, loads weights, and streams generated text to stdout. After generation it prints a telemetry summary (VRAM breakdown, tok/s, timing).

**INT8 mode** (~2× VRAM reduction):
```bash
# 1. Quantize your model (one-time step, requires Python + safetensors)
python scripts/quantize_int8.py /path/to/model /path/to/model-int8 --block-size 64

# 2. Run with quantized weights
wgpu-llm --model-dir /path/to/model-int8 --prompt "..." --max-tokens 256 --gemm-int8-block-size 64
```

For the full list of CLI flags (sampling, INT8 GEMM, KV spill, memory budget, dry-run), see the [CLI Reference](docs/cli-reference.md).

## Current Limitations

- **Alpha quality** — functional but not production-hardened
- **Decode-only** — prompt tokens are processed sequentially (no batched prefill yet)
- **Single-sequence** — no batching or concurrent requests
- **INT8 lightly tested** — verified with TinyLlama 1.1B; quality may vary with larger models
- **CPU-side sampling** — logits read back to CPU for top-k/top-p/temperature; fast enough for single-sequence but not optimal
- **No chat template** — raw text completion only; no multi-turn conversation support yet
- **Timing is wall-clock** — reported tok/s includes CPU overhead, not isolated GPU kernel time

## Architecture at a Glance

```
Text → Tokenizer → Embedding → [N × Transformer Layers] → Logits → Sampler → Token
                                       │
                                  ┌────┴────┐
                                  │  Attn   │ ← KV Cache (paged)
                                  │  FFN    │
                                  └─────────┘
```

Each box is one or more **WGSL compute shader dispatches** orchestrated by Rust.  
See [`docs/architecture.md`](docs/architecture.md) for the full system design.

## Key Design Decisions

| Decision | Detail |
|---|---|
| 12 WGSL compute shaders | Every Transformer op is a standalone shader (GEMM, MATVEC, RMSNorm, RoPE, SiLU, softmax, etc.) |
| f32/f16 compile-time switching | WGSL string injection — no runtime branching |
| Paged KV Cache | Lazy GPU page allocation with per-page sequence-offset writes |
| Single CommandEncoder | All dispatches per token in one GPU submission — no mid-pipeline sync |
| CPU-side sampling | Temperature → top-k → top-p → softmax → weighted sample; GPU argmax at temp=0 |
| Row-sharding | Large embedding/LM-head tensors auto-split to fit `max_storage_buffer_binding_size` |
| GQA support | Grouped-Query Attention for Llama 3 models |

## Future Roadmap

- **Batched prompt prefill** — process all prompt tokens in one dispatch
- **GPU timestamp queries** — accurate kernel-level timing
- **7B+ model support** — optimize for Llama 3.1 8B and larger
- ~~**INT8 GEMM activation**~~ ✅ — ~2× VRAM reduction via `scripts/quantize_int8.py` + `--gemm-int8-block-size`
- ~~**Streaming output**~~ ✅ — tokens are emitted as generated
- **Multi-turn chat** — KV cache reuse with chat template wrapper

See [`docs/plan.html`](docs/plan.html) for the full interactive roadmap.

## Documentation

| Document | Purpose |
|---|---|
| [Architecture](docs/architecture.md) | System design, data flow, buffer layouts |
| [CLI Reference](docs/cli-reference.md) | All flags, sampling config, advanced modes |
| [Roadmap](docs/plan.html) | Interactive implementation plan |
| [Doc Maintenance](docs/DOC_MAINTENANCE.md) | Documentation rules for contributors |
| [Guides](docs/guides/) | wgpu & WGSL pitfalls and best practices |
| [Contributing](CONTRIBUTING.md) | How to contribute |

## License

Dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE) at your option.
