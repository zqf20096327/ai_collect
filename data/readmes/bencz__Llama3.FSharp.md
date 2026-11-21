# Llama3.FSharp

Inference runtime for Llama/Qwen in F#, which started as a port of [likejazz/llama3.cuda](https://github.com/likejazz/llama3.cuda) (`llama3.cu`).
A single implementation of the transformer runs on **CPU**, **GPU (CUDA)** or **both (hybrid)**, with GPU memory planning and weight offloading.

- **CPU:** kernels selected by ISA (x86-64 AVX2/AVX-512, ARM64 NEON/DotProd, portable `Vector<T>`), with int8 integer dot products for quantized weights.
- **GPU:** kernels written in F# and compiled to PTX at runtime by [ILGPU](https://ilgpu.net). Only the **NVIDIA driver** is needed: no CUDA Toolkit, no nvcc, no cuBLAS.
- **Formats:** llama2.c checkpoints (`stories15M.bin`, parity with the original) and **GGUF** (`llama`, `qwen2`, `qwen3`, `qwen3moe`) in F32, F16, BF16, Q8_0, Q4_0, Q4_K, Q6_K.
- **Mixture of Experts** (Qwen3-30B-A3B): softmax -> top-k -> renormalised routing, expert views built once at load, batched expert matvecs.
- **Op-level and multi-GPU placement:** attention and FFN of a layer are placed independently. Layers are pipelined across any number of GPUs plus the CPU.
- **Loading (llama.cpp model):** GGUF files, including llama.cpp **splits** (`<prefix>-00001-of-0000N.gguf`), are **memory-mapped**. Tensors are zero-copy views with no 2 GiB limit, and the mapping is populated up front (`MADV_POPULATE_READ`, the equivalent of llama.cpp's `MAP_POPULATE`), so decoding never stalls on page faults. GPU uploads stream rows from the mapping through two pinned staging buffers. `--no-mmap` reads instead, with async positional I/O (`Task.parallelLimit`). Malformed files (counts, offsets, alignment, unknown types) are rejected before any allocation.
- **F# 11 / .NET 11:** ILGPU kernels are curried module functions bound with *direct delegates* (no reflection, signatures checked by the compiler).
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
| stories15M (F32) | 285 | **930** | identical text to `llama3.cu` in every mode |
| Qwen3-0.6B Q8_0 | 40 | **81.5** | |
| Qwen3-4B-Instruct-2507 Q4_K_M | **13.5** | **19.8** | GPU with `--ctx 1024`, everything resident. At the default 4096 context, the f32 KV cache (1.15 GB) pushes 6 layers to streaming: 14.4 |
| Llama 3.2 3B Q4_K_M | n/a | 25.7 | `llama` arch, `rope_freqs`, Llama 3 template |
| Qwen2.5-3B Q4_K_M | n/a | 24.7 | `qwen2` arch (QKV bias) |
| **Qwen3-30B-A3B MoE Q4_K_M** (18.5 GB) | n/a | **19.4** | hybrid: attention + KV + classifier + experts of 6 layers on the 4 GB GPU, other experts on the CPU. Loads in 2.3 s from a warm page cache (mmap); 18.2 with `--no-mmap` |

`--profile` breaks a forward pass down per phase and device. On the MoE above the breakdown was: experts on the CPU 70.7 ms,
attention on the GPU 24.3 ms, CPU<->GPU transfers 2 ms. The hybrid split costs almost nothing, and the experts' memory reads dominate.

## Architecture

```
Llama3.CLI --> Llama3.Runtime --> Llama3.Backend.CPU   -+
                    |         +--> Llama3.Backend.CUDA -+--> Llama3.Core
                    +-----------------------------------+
```

| Project | Folders | Responsibility |
|---|---|---|
| **Llama3.Core** | `Numerics` `Storage` `Tensors` `Model` `Formats` `Tokenization` `Loading` `Sampling` `Compute` `Inference` | memory-mapped storage (`MappedFile`, `TensorStorage`), formats (GGUF incl. splits, llama2.c), dequantization, tokenizers (SentencePiece, byte-level BPE), chat templates, sampler, **device abstraction** (`IComputeBackend`, `IKvCache`, `ILayerSource`) and the **device-agnostic transformer** |
| **Llama3.Backend.CPU** | `Platform` `Isa/{Contracts,Portable,X86,Arm}` `Kernels` | `ICpuKernels` per ISA (portable `Vector<T>`, AVX2, AVX-512 VNNI `vpdpbusd`, NEON + DotProd), all taking weight rows as spans (mapped or managed). `Autotune` measures the candidates per format on a DRAM-sized working set with the real thread count, using a deterministic 10% margin. `CpuWorkerPool` is a persistent fork-join pool (atomic chunk counter, spin-then-sleep, protocol safe on weakly ordered CPUs) that replaces `Parallel.For`. `CpuTopology` counts the **physical** cores the process may use (affinity/cpusets on Linux, `GetLogicalProcessorInformationEx` on Windows, `hw.physicalcpu` on macOS). |
| **Llama3.Backend.CUDA** | `Kernels` `Memory` | ILGPU kernels (`MatVecKernels`, `AttentionKernels`, `ElementwiseKernels`, `DeviceMath`), padded device layouts (`GpuLayout`), buffers/KV, weight streaming |
| **Llama3.Runtime** | `Configuration` `Devices` `Planning` `Execution` `Generation` | `DeviceManager` (discovery), `MemoryManager` (estimate per component), `Scheduler` (placement plan), `ExecutionEngine` (materializes the plan), generation/chat, public API `Llama3.load` |
| **Llama3.CLI** | `Cli` | arguments, console rendering |

### How the hybrid runtime works

1. **The `Transformer` knows nothing about CUDA.** It runs a pipeline of `LayerStage`s, each with
   `Compute` (backend), `Weights` (`ILayerSource`), `KvBackend` and `Cache`. The activation stays on a device
   while consecutive stages run there; at each boundary only `dim` floats cross over.
2. **The `Scheduler` decides placement before allocating anything**, from the free VRAM minus a reserve
   (`GpuReserveMB`, default max(256 MiB, 1/64 of the device)) and `GpuMemoryLimitMB`:
   - `Hybrid` + `CpuCompute`: the **last** layers and the classifier go to the GPU. The embedding lives on the host,
     so the activation crosses PCIe only **once** per token.
   - `GpuOnly` or `Hybrid` + `StreamWeights`: everything computes on the GPU. Layers that don't fit stay in
     **pinned** memory and are copied into **2 device slots** (double buffering): layer *i+1* is copied on a
     separate stream while layer *i* computes.
   - `KvCache = HostMemory`: the KV cache stays in RAM and only attention runs on the CPU (q/k/v cross over, a few KB),
     freeing VRAM for weights (the equivalent of llama.cpp's `--no-kv-offload`).
   - No GPU (or GPU too small) + `UseCpuFallback`: everything on the CPU, with a note in the plan.
   - **MoE:** attention + KV of every layer and the classifier go to the GPUs first, because they are small and used every token,
     in contiguous segments **proportional to each GPU's room** (so no GPU is left idle). Experts then join their own attention GPU while
     budget remains, and leftovers use any other GPU with room (one activation round trip) before falling back to the CPU. Experts are
     never streamed.
   - **Several GPUs:** a model that fits is split proportionally to the GPUs' room. Otherwise each GPU takes a contiguous segment filled
     backwards: the last GPU holds the tail and the classifier, which maximises the layers on GPUs for a contiguous pipeline
     (CPU -> GPU0 -> ... -> GPUn).
   - **Forced `GpuLayers = k`:** 0 means everything on the CPU. Layers beyond the budget are streamed with `StreamWeights` on one GPU;
     otherwise they over-commit the GPU with the most room, and the excess shows up in `GpuBytes` and in the plan's notes. Every `CudaBackend` binds its CUDA context
     before each driver call, so any number of accelerators can be driven from one thread. Weight streaming is single-GPU for now.
3. **A new device** (ROCm/HIP, OpenCL, Metal) means implementing `IComputeBackend` (and optionally
   `IWeightStreaming`) and registering it in `DeviceManager`. The transformer and scheduler don't change.
   ILGPU's kernels are already portable to its OpenCL backend.

### Quantization

- **CPU:** activations are quantized to int8 in blocks of 32, with per-16 sums. Q8_0/Q4_K/Q6_K use integer dot products
  (`vpmaddubsw`/`vpmaddwd` on x86; `sdot` or `smull+sadalp` on ARM). Q4_K mins and Q6_K's -32 offset
  are corrected in a single FMA using the precomputed sums. `--exact-cpu` switches to the float path
  (exact decoding + float dot).
- **GPU:** Q8_0 (34 B) and Q6_K (210 B) blocks are **padded to 4 bytes** at upload (36/212 B), so every
  lane reads whole `uint32` words. `x` is staged in shared memory once per block, and warps walk the rows with a
  grid-stride loop. Q4_K reads its 3 scale words into registers and extracts only the 2 scale/min pairs it needs.

## Numerical validation (215 tests, `dotnet test --solution Llama3.FSharp.slnx`)

- **Placements:** synthetic dense and MoE models (Q8_0/Q4_K) are compared with an independent float64 reference forward pass
  (`tests/Shared/ReferenceModel.fs`) under 9 placements: CPU, GPU, attention-GPU/FFN-CPU, the reverse, alternating layers, KV on host,
  streaming, a 2-GPU pipeline, and attention and FFN of one layer on different GPUs. The 2-GPU cases run on a single card by opening two
  independent CUDA contexts. Architecture variants are also checked against the reference on CPU, GPU, split and streamed placements:
  Llama 3.1 (interleaved RoPE + `rope_freqs`), Qwen2 (QKV bias + tied classifier), and 5-layer models whose streamed layers wrap around
  the two slots. `LLAMA3_SLOW_TESTS=1` adds an end-to-end Qwen3-30B-A3B test, and `LLAMA3_REQUIRE_ALL=1` turns missing GPUs or models
  into failures instead of skips.
- **Loader:** a GGUF writer (`tests/Shared/GgufWriter.fs`) serializes synthetic dense and MoE models, with tokenizer and ChatML
  template, as single files and as 3-way splits. Loading through mmap and through buffered reads must yield byte-identical
  payloads and the reference logits. Malformed files (huge strings/arrays, bad alignment, unknown types, truncation, data
  past EOF) must be rejected.
- **Sessions:** end to end on a synthetic GGUF, greedy decoding. A turn cancelled before or *during* its prompt leaves the session
  exactly as it was, and the conversation then continues token for token like an uninterrupted one. Interleaved sessions
  replay correctly. A sampled stop token is replaced by the template's end of turn. An oversized prompt raises
  `ContextOverflowException` without side effects. Streamed pieces (including the final UTF-8 flush) reassemble the result.

- **Golden:** `stories15M` reproduces **byte for byte** the README output of `llama3.cu` in 7 configurations
  (CPU, CPU-portable, GPU, hybrid 3+3, KV on host, full streaming, mixed streaming).
- **Independent reference:** `tools/reference/qwen3_reference.py` is a NumPy float64 forward pass for Qwen3 with its own
  GGUF reader and Hugging Face semantics (`rotate_half`). It shares no code with the runtime. Qwen3-0.6B matches
  the reference (top-1 at every position, top-10 logits within 2e-3) on CPU, GPU and hybrid.
- **Tokenizer:** byte-level BPE ids identical to `llama-tokenize` (accents, CJK, emoji, digits, contractions,
  specials). Special-token markup in user text is never interpreted as control tokens.
- **Kernels:** every CPU ISA available on the machine against exact references, plus BF16 rows, the worker pool (3000 back-to-back
  jobs, failure propagation) and MoE routing with NaN logits. Each GPU kernel against float64/CPU (6 formats incl. BF16; shapes with
  row tails, Q8_0 block tails and rows beyond shared memory; norms, RoPE with and without factors, GQA at several positions).
- **Chat:** incremental continuation (KV reuse) equals replaying the conversation from scratch.
- **ARM64:** `tools/test-arm64.sh` publishes the CPU suite and the CLI for linux-arm64 and runs them in an arm64 container through
  qemu-user, using the real ARM64 JIT on an emulated CPU with `asimddp`, SVE and SVE2. All 96 CPU tests pass there (the ISA
  theories expand to Portable + NEON), and the `stories15M` golden is byte-identical with `--cpu-isa neon` and `--cpu-isa portable`.
  On Qwen3-0.6B Q8_0, NEON with `--exact-cpu` produces the same text as x86.
- **Known limitation, documented in the tests:** the int8 activation path (default on the CPU) deviates from the exact float path
  because of the attention sink's *massive activations* (~8e3 at position 0). Measured on Qwen3-0.6B: up to 37% relative logit error
  at position 0 and 2-4% afterwards, the same envelope for every ISA. Greedy continuations can therefore differ between ISAs where the
  exact path itself is nearly tied. Example: after "Paris. The capital of", "France" leads "Italy" by only 0.069 logits; AVX2 and NEON
  keep "France", while Portable and AVX-512 VNNI pick "Italy". llama.cpp's Q8 path behaves the same way. `--exact-cpu` removes it.

## Intentional differences from the original

- UTF-8 output is reassembled correctly. The original's `safe_printf` turned `0xC3`/`0xC2` sequences into Latin-1 and
  dropped lone bytes >= 0x80. ASCII control bytes are still filtered.
- The `prompt_tokens[1] == 306 -> 76` monkey patch only applies in `GenerationSettings.Legacy` (default for llama2.c checkpoints).
- The original copied the embedding with `cudaMemcpyHostToDevice` from a device pointer. Here the embedding lives on the host
  and only the token's row is uploaded.

## Roadmap

- **GPU performance:** remove the 4-way shared-memory bank conflicts in the `x` reads (permute bytes in the padded layout),
  batched prefill (GEMM instead of GEMV per prompt token), tiled/flash attention for long contexts, F16 KV cache.
- **Architectures:** Gemma 3 (GeGLU, sliding window, extra norms), and later MLA, Gated DeltaNet/hybrid layers, partial and
  multimodal RoPE.
- **Thinking/introspection:** channels already exist (`TokenChannel.Thinking`), as do the hooks (`IForwardObserver`: hidden state per layer,
  MoE routing decisions, logits), plus the per-phase profiler (`ForwardProfile`).
- **Cache:** `IKvCache` isolates the layout (paged, reduced precision, prefix cache) from the rest of the runtime.
- **Big machines (validation on multi-GPU pods planned):** GPU->GPU transfers over P2P/NVLink (currently through host memory), weight
  streaming per GPU, NUMA-aware CPU workers and weight placement on multi-socket hosts, adaptive KV capacity on large GPUs.
- **MoE:** batched prefill over experts (group prompt tokens by expert), and a fused routing kernel to avoid the per-layer router download.
- **CPU:** AVX-VNNI (256-bit, client cores without AVX-512), AMX on Sapphire Rapids+, SVE/SVE2 on ARM servers, outlier-aware
  mixed precision for int8 activations, and NUMA-aware worker pinning.
- **ARM64 hardware:** the NEON/DotProd kernels are validated under qemu (see below). Remaining work is performance tuning on real
  cores (Graviton, Ampere, Apple) and SVE/SVE2 kernels.

## Structure

```
src/Engine/    Llama3.Core (formats, model, device abstraction, transformer), Llama3.Runtime (planning, execution, generation)
src/Backends/  Llama3.Backend.CPU, Llama3.Backend.CUDA
src/Hosts/     Llama3.CLI (and the upcoming OpenAI-compatible server)
tests/      CpuTests, CudaTests, NumericalParityTests (+ data/ with the NumPy reference), Shared/
tools/      reference/qwen3_reference.py, test-arm64.sh (CPU suite + golden on linux-arm64 via qemu)
models/     stories15M.bin + tokenizer.bin (llama2.c checkpoint used by the golden; GGUF models in ~/models or $LLAMA3_MODELS_DIR)
```

License of the original code: MIT (llama3.cuda / llama2.c).
