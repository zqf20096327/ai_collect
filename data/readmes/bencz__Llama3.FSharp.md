# Llama3.FSharp

Inference runtime for Llama/Qwen in F#, which started from [likejazz/llama3.cuda](https://github.com/likejazz/llama3.cuda) (`llama3.cu`).
A single implementation of the transformer runs on **CPU**, **GPU (CUDA)** or **both (hybrid)**, with GPU memory planning and weight offloading.

- **CPU:** kernels selected by ISA (x86-64 AVX2/AVX-512, ARM64 NEON/DotProd, portable `Vector<T>`), with int8 integer dot products for quantized weights.
- **GPU:** kernels written in F# and compiled to PTX at runtime by [ILGPU](https://ilgpu.net). Only the **NVIDIA driver** is needed: no CUDA Toolkit, no nvcc, no cuBLAS.
- **Formats:** llama2.c checkpoints (`stories15M.bin`, parity with the original) and **GGUF** (`llama`, `qwen2`, `qwen3`, `qwen3moe`) in F32, F16, BF16, Q8_0, Q4_0, Q4_K, Q6_K.
- **Mixture of Experts** (Qwen3-30B-A3B): softmax -> top-k -> renormalised routing, expert views built once at load, batched expert matvecs.
- **Op-level and multi-GPU placement:** attention and FFN of a layer are placed independently. Layers are pipelined across any number of GPUs plus the CPU.
- **Loading (llama.cpp model):** GGUF files, including llama.cpp **splits** (`<prefix>-00001-of-0000N.gguf`), are **memory-mapped**. Tensors are zero-copy views with no 2 GiB limit, and the mapping is populated up front (`MADV_POPULATE_READ`, the equivalent of llama.cpp's `MAP_POPULATE`), so decoding never stalls on page faults. GPU uploads stream rows from the mapping through two pinned staging buffers. `--no-mmap` reads instead, with async positional I/O (`Task.parallelLimit`). Malformed files (counts, offsets, alignment, unknown types) are rejected before any allocation.
- **F# 11 / .NET 11:** ILGPU kernels are curried module functions bound with *direct delegates* (no reflection, signatures checked by the compiler).
- **Mind:** `Llama3.Mind` keeps a conversation on disk on top of the engine: episodes dated when they were said, a crash-safe journal, recall and per-model views (see [docs/13](docs/13-mind.md)).
- **Build policy:** every warning is an error: compiler, MSBuild, NuGet, plus opt-in FS1182 (unused bindings) and FS3390 (XML docs). No `#nowarn` and no `unsafe` code. SIMD goes through `ref`/`MemoryMarshal`/`LoadUnsafe`.

## Quick start

```bash
dotnet build -c Release
L="dotnet src/Hosts/Llama3.CLI/bin/Release/net11.0/llama3.dll"

$L                                              # reproduces llama3.cu: stories15M, "I have a dream", 50 steps
$L "Explain AI" -m ~/models/Qwen3-0.6B-Q8_0.gguf
$L -m ~/models/Qwen3-4B-Instruct-2507-Q4_K_M.gguf --chat          # multi-turn chat (reuses the KV cache)
$L "What is 17*23?" -m ~/models/Qwen3-0.6B-Q8_0.gguf --think     # reasoning (rendered dimmed)
$L -m ~/models/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf --ctx 2048   # MoE: attention on the GPU, experts on the CPU
$L -m model.gguf --gpu-mem 1500 --plan          # shows the placement plan only
$L -m model.gguf --gpus 0,1 --profile "..."     # pipeline over two GPUs, per-phase timing
$L --devices
```

Main options: `--mode cpu|gpu|hybrid`, `--gpus all|none|0,1,...`, `--gpu-layers N`, `--offload cpu|stream`, `--kv-cache gpu|host`,
`--gpu-mem MB` and `--gpu-reserve MB` (per GPU), `--ctx N`, `-t N`, `--cpu-isa avx512|avx2|neon|portable`, `--exact-cpu`,
`--no-mmap` (+ `--load-concurrency N`), `--profile`, `--temp/--top-k/--top-p/--min-p/--repeat-penalty/--seed` (`--help` lists everything).
Values are validated with the option's name, contradictory combinations are rejected, and `LLAMA3_DEBUG=1` prints stack traces.
`--plan` only maps the file, so planning even the 18.5 GB MoE takes about 0.5 s. `--chat "first message"` opens the conversation with the prompt.

As a library:

```fsharp
open Llama3

let options = { ModelOptions.Default with ExecutionMode = Hybrid; GpuMemoryLimitMB = Some 3000 }
use model = Llama3.load options "Qwen3-4B-Instruct-2507-Q4_K_M.gguf"
let answer = model.Generate("Explain artificial intelligence")

use chat = model.CreateChat(systemPrompt = "Answer in Portuguese.")
let r = chat.Send("Hi!", onToken = fun t -> printf "%s" t.Text)
```

## Measured results

i9-11900K (8 cores / 16 threads, AVX-512 VNNI), GTX 1050 Ti 4 GB (Pascal SM_61), greedy, tokens/s of generation.
CPU numbers are with the default autotuned int8 kernels on the physical cores.

| Model | CPU | GPU | Notes |
|---|---:|---:|---|
| stories15M (F32) | 195 | **830** | identical text to `llama3.cu` in every mode; the default 50-token run in a fresh process, where warming up the sequence engine weighs (about 530 and 930 once warm) |
| Qwen3-0.6B Q8_0 | 49.6 | **81.5** | |
| Qwen3-4B-Instruct-2507 Q4_K_M | **14.4** | **19.8** | GPU with `--ctx 1024`, everything resident. At the default 4096 context, the f32 KV cache (1.15 GB) leaves 3 layers on the CPU: 18.8 |
| Llama 3.2 3B Q4_K_M | n/a | 25.7 | `llama` arch, `rope_freqs`, Llama 3 template |
| Qwen2.5-3B Q4_K_M | n/a | 24.7 | `qwen2` arch (QKV bias) |
| **Qwen3-30B-A3B MoE Q4_K_M** (18.5 GB) | n/a | **19.4** | hybrid: attention + KV + classifier + experts of 6 layers on the 4 GB GPU, other experts on the CPU. Loads in 2.3 s from a warm page cache (mmap); 18.2 with `--no-mmap` |

`--profile` breaks a forward pass down per phase and device. On the MoE above, per token: experts on the CPU 70.7 ms,
attention on the GPU 24.3 ms, CPU<->GPU transfers 2 ms; the experts' memory reads dominate and the hybrid split costs little.

## Documentation

The documentation of the project lives in [`docs/`](docs/00-overview-and-map.md): a numbered set of
blocks (architecture and conventions, formats and loading, tokenization, the transformer and the
device abstraction, the CPU and CUDA backends, planning and execution, generation and sessions, KV
bookkeeping, the command line, testing and validation, durable storage, the mind). Start with the
[overview and map](docs/00-overview-and-map.md). Agent rules are in [`AGENTS.md`](AGENTS.md).

Licensed under the [MIT License](LICENSE). The llama2.c checkpoint and tokenizer in `models/` come from
[karpathy/llama2.c](https://github.com/karpathy/llama2.c) (MIT).
