<p align="center">
  <img src="docs/brand/liyab-banner.svg" width="100%" alt="Liyab: large language models on the device in your pocket. Fast, cool to the touch, private by construction.">
</p>

<p align="center">
  <img alt="Platforms: Android, iOS, macOS, Linux" src="https://img.shields.io/badge/platforms-Android%20%C2%B7%20iOS%20%C2%B7%20macOS%20%C2%B7%20Linux-FF7A3D?labelColor=1B1420">
  <img alt="C++20" src="https://img.shields.io/badge/C%2B%2B-20-FF3D6E?labelColor=1B1420">
  <img alt="Models: GGUF" src="https://img.shields.io/badge/models-GGUF-FFC24D?labelColor=1B1420">
  <img alt="Private: on-device only" src="https://img.shields.io/badge/data-never%20leaves%20the%20device-9ED8FF?labelColor=1B1420">
  <img alt="License: Apache 2.0" src="https://img.shields.io/badge/license-Apache%202.0-EDE6EE?labelColor=1B1420">
</p>

*Liyab* is Tagalog for **flame**.

Liyab is an inference engine for GGUF language models on phones and laptops, and a private assistant built on it. It
is written in C++20 and has no cloud dependency. Our aim is to be the reference engine for running open models on
whatever device is at hand. That means models larger than the device's RAM, on any phone, without heating it up, and
without a single byte of the user's data leaving the device.

Today a 22 GB mixture-of-experts model (**Qwen3.6-35B-A3B**) answers at **~9–10.5 tokens per second** from the
command line on a Snapdragon 8 Elite phone, and at **~7.5–9.4 tok/s in the app**. Its experts are streamed from flash
storage into the 6 GiB that Android lets one app use. A model that fits in RAM, **Qwen3.5-4B**, answers at **~12 tok/s**
from the command line and **~12–16 tok/s in the app**.

> **This README describes the code as it is.** Every feature listed here is implemented and tested; everything that
> is not lives in the [Roadmap](#roadmap). Numbers are measured on real hardware. Where a number comes from a single
> run, a hot phone or a different setup, the text says so.

---

## Contents

* [Why Liyab](#why-liyab)
* [Design principles](#design-principles)
* [What it does today](#what-it-does-today)
* [Quick start](#quick-start): host, Android, iOS, [Windows](#windows-x64), CMake options
* [Architecture](#architecture)
* [Supported models](#supported-models)
* [Models larger than RAM](#models-larger-than-ram)
* [Context, memory and serving](#context-memory-and-serving)
* [Heat and power](#heat-and-power)
* [Speculative decoding](#speculative-decoding)
* [Embeddings and reranking](#embeddings-and-reranking)
* [LoRA adapters](#lora-adapters)
* [Using the engine](#using-the-engine): C++, C ABI, Kotlin, Swift, command line
* [The Liyab app](#the-liyab-app): assistant, agent tools, local OpenAI / Anthropic / gRPC API
* [Look and feel](#look-and-feel): the living flame, colours, type
* [Measured results](#measured-results)
* [Experimental modules](#experimental-modules)
* [Testing](#testing)
* [Roadmap](#roadmap)
* [Known limitations](#known-limitations)
* [Project layout](#project-layout)
* [Contributing](#contributing)
* [License](#license)

---

## Why Liyab

Cloud assistants are capable, but they cannot read your messages, your calendar or your files without sending them
somewhere else. A model running on the phone can. That only works if the device can run a *strong* model, and do it
in a way people will tolerate: no waiting minutes for an answer, no phone burning in the hand, no battery gone by
lunch.

Phones are not small servers. Their memory is shared with everything else and capped per app (6 GiB on HyperOS). The
fast storage reads at ~4.4 GB/s, but only when the reads are large and concurrent. Sustained load hits thermal limits
within minutes. Every SoC has a different mix of CPU cores, GPU and NPU, and every model architecture stresses them
differently.

Liyab is built around those constraints:

* **Models larger than RAM are the normal case.** Dense blocks and MoE experts stream from flash, with direct I/O
  sized to what the storage likes. The expert cache predicts the next block's experts from the router and overlaps
  reads with compute. Memory is planned against the budget the OS really allows.
* **Heat is part of scheduling.** The engine reads the OS's thermal-headroom forecast. As pressure builds, it paces
  tokens and asks the governor for lower clocks, so the same tokens cost fewer watts. It does not run flat out and
  then collapse.
* **Serving a single user well.** Context is reused across turns, including the recurrent state of hybrid models.
  A prefix cache of KV chunks brings back earlier conversations, keeps a shared system prompt once and outlives a
  restart. Prefill can be cancelled and resumed. Structured output covers
  tool calls. A local OpenAI, Anthropic Messages and gRPC API lets other apps on the device use the same model.
* **A private agent on top.** The Liyab app replaces the system assistant. It answers questions about your day from
  your own calendar, notifications, messages and calls, and nothing leaves the phone.

## Design principles

These rules decide what goes into the code:

1. **Generic and self-calibrating.** No optimization is tied to one SoC or one model. Thread counts, draft
   lengths, expert prefetch depth, context length, memory plans and thermal bands are measured or derived on the
   device the engine runs on.
2. **Kernels per instruction set, policy per platform.** Compute kernels target ISAs: ARM64 NEON with dot product
   and i8mm, x86-64 AVX2, Metal, Vulkan. Differences between operating systems (thermal APIs, performance hints, memory limits)
   live behind a thin adaptive layer, never in the kernels.
3. **Lossless by default.** Every speed-up that changes the output (fewer experts, requantization, skipping) is
   opt-in, labelled lossy, and measured with `liyab-kl` against the lossless path.
4. **Measured, not assumed.** Changes are judged by alternating A/B runs on a real phone. Ideas that did not pay off
   are documented, so nobody has to try them again blind.
5. **Private by construction.** The engine never touches the network. The app uses the network only to download
   models from Hugging Face.

---

## What it does today

| Area | Status |
| :--- | :--- |
| GGUF v2/v3 loader: `mmap`, zero-copy, validated against malformed files; split models (`-00001-of-0000N.gguf`) | ✅ |
| Architectures: `llama`, `mistral`, `qwen2`, `qwen3`, `qwen35` (hybrid Gated DeltaNet + attention), `qwen3moe`, `qwen35moe`, `hunyuan-dense`, `gemma2`, `gemma3`, `phi3`, `deepseek2` (multi-head latent attention) | ✅ cross-checked against llama.cpp or Hugging Face transformers |
| Every GGML tensor format (F32/F16/BF16, legacy Q4–Q8, K-quants, I-quants, TQ1_0/TQ2_0, MXFP4, NVFP4) | ✅ bit-exact against llama.cpp's reference decoder |
| Tokenizers: SentencePiece and byte-level BPE, pre-tokenizers as data (Qwen, Llama 3, GPT-2, DeepSeek, Hunyuan, Phi, Gemma, Mistral-Nemo, SmolLM2, Youtu-LLM) | ✅ token-identical to each model's Hugging Face tokenizer |
| Chat templates: the GGUF's Jinja template rendered by Liyab's own interpreter; layout of turns and prefix stability for context reuse | ✅ byte-identical to transformers' `apply_chat_template` |
| Models larger than RAM: dense blocks streamed by parallel `O_DIRECT` reads; MoE experts streamed into an LFU cache with router-predicted prefetch | ✅ automatic |
| Memory planning: per-app budget, automatic requantization only when the expert cache would be too small, recommended budget reported | ✅ |
| CPU backend: NEON + SDOT; i8mm (SMMLA) layouts for Q4_K/Q5_K/Q6_K/Q8_0; WFE-waiting thread pool with chunks claimed on demand | ✅ |
| CPU backend on x86-64: AVX2 + FMA + F16C kernels chosen at run time by CPUID, scalar fallback in the same binary | 🟡 tested under Rosetta 2 only |
| Windows x64 port of the engine, `liyab-cli`, the tests and tools: file mapping, unbuffered direct reads, processor groups and hybrid cores, UTF-8 paths and console; MSVC or clang-cl | 🟡 written, not yet compiled or run on Windows ([Windows](#windows-x64)) |
| GPU backends: Metal (zero-copy on unified memory), Vulkan (Adreno/Mali; native kernels for 23 formats on GPU-shared memory) | ✅ |
| Paged KV cache (F16 / Q8_0 / Q4_0 / Q4_1) laid out per block (windowed blocks keep only their window), with per-channel key scaling, sliding window with attention sinks, grouped-query attention over spans, latent rows for multi-head latent attention, read in the absorbed form or, for long prefills, the expanded one (chosen by a threshold measured once per device) | ✅ |
| Context kept between turns, recurrent-state snapshots for hybrid models, save/restore to disk | ✅ |
| Several sequences decoded together: one pass over every sequence's rows, each sequence's own context, adapter and priority, each output what it gives alone | ✅ CPU and Metal backends |
| Automatic context length from the KV cache's cost; cancellable, resumable chunked prefill | ✅ |
| Prefix cache across conversations: a content-addressed store of KV chunks (shared prefixes kept once), in RAM and on storage across runs, capped, LRU | ✅ |
| Segment reuse: marked parts of a prompt (documents, tool results) reused wherever they appear, keys turned to their new positions, a share calibrated per model processed again; attention-only models | ✅ opt-in, lossy |
| Speculative decoding: draft model, n-gram lookup or suffix drafts from this and earlier conversations (their continuation tree verified in one pass), adaptive draft count, hybrid models included | ✅ |
| Structured output: grammar-constrained decoding (JSON Schema, grammar text; tool calls in the app and the local API) and forced continuations | ✅ |
| Embeddings and reranking: decoder embedding models and rerankers as their GGUF declares them (last-token or mean pooling, ranking heads, or LM-head labels), shared prefixes computed once | ✅ cross-checked against Hugging Face transformers |
| LoRA adapters: several GGUF adapters loaded next to one model within a memory cap, selected per generation, computed beside the base matmuls (never merged); dense, hybrid and MoE models (per-expert adapters); contexts kept apart by adapter | ✅ |
| Heat and power: OS headroom forecast, adaptive pacing, ADPF performance hints, emergency guards, power profiles | ✅ |
| SoC detection (Snapdragon, Dimensity, Tensor, Exynos, Apple) and backend ranking | ✅ |
| Qualcomm QNN (Hexagon NPU), MediaTek NeuroPilot | 🟡 detected at runtime; compute falls back to GPU/CPU |
| Liyab app (Flutter): chat, model library with Hugging Face downloads, activity meters, settings, system assistant sheet (phone) or command bar (computer) | ✅ Android · ✅ macOS (Apple silicon) · 🟡 iOS app not built yet (the engine builds for iOS) |
| Agent tools: calendar, notifications (chats, email previews), SMS, calls, contacts, clipboard on Android; calendar, Apple Mail, Messages, calls, contacts, clipboard on macOS; each source opt-in | ✅ |
| Local API for other apps on the device: OpenAI, Anthropic Messages, gRPC; loopback only, token-protected, off by default; tools and JSON answers by constrained decoding | ✅ text (no images) |
| Voice, actions (alarms, events, replies), local memory/RAG | 🔜 [Roadmap](#roadmap) |
| Experimental: early exit, head pruning, EGLS, 2:4 sparsity, JIT unpacker, persistent KV prefix files, io_uring | 🧪 `LIYAB_ENABLE_EXPERIMENTAL` |

---

## Quick start

Requirements: CMake ≥ 3.22, a C++20 compiler (Clang 17+ / Apple Clang 15+), Ninja recommended. Android: NDK r26+.
iOS: Xcode 15+. Windows: Visual Studio 2022 with its C++ tools (MSVC, or its clang-cl). The app: Flutter 3.x,
Android SDK platform 36, JDK 17.

```bash
# Build and test on the host (macOS / Linux)
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release   # add -DLIYAB_ENABLE_EXPERIMENTAL=ON for experimental modules
cmake --build build
ctest --test-dir build --output-on-failure

# x86-64 build on an Apple-silicon Mac, run under Rosetta 2. Rosetta executes AVX2 but reports it in CPUID only
# with ROSETTA_ADVERTISE_AVX=1; without it the scalar kernels run
cmake -S . -B build-x86 -G Ninja -DCMAKE_OSX_ARCHITECTURES=x86_64 -DCMAKE_BUILD_TYPE=Release
cmake --build build-x86
ROSETTA_ADVERTISE_AVX=1 ctest --test-dir build-x86 --output-on-failure

# Run a model
./build/liyab-cli -m model.gguf -p "Explain unified memory in one paragraph." -n 128
./build/liyab-cli --device                                 # what Liyab sees: SoC, accelerators, backend ranking
```

```bash
# Android (arm64-v8a): libliyab.so, liyab-cli and the tests in build/android/arm64-v8a
scripts/build_android.sh                     # --experimental, --abi, --api, --ndk, --no-vulkan, ... (see --help)

# iOS: build/ios/Liyab.xcframework (device arm64 + simulator arm64/x86_64), importable from Swift as `Liyab`
scripts/build_ios.sh

# The Liyab app: builds libliyab first, then the release APK; --install waits while the app is in use
scripts/build_flutter_app.sh --install

# The Liyab app for macOS (Apple silicon): app/build/macos/Build/Products/Release/Liyab.app
scripts/build_flutter_app.sh --macos
```

The Android NDK is located from `--ndk`, `$ANDROID_NDK_HOME`, or the newest NDK in the usual SDK locations. The
`.so` is linked with 16 KB page alignment, which Android 15+ devices with 16 KB pages require. If `xcodebuild`
reports missing components, run `sudo xcodebuild -runFirstLaunch` once.

### Windows (x64)

The engine library (`liyab.dll`), `liyab-cli`, the tests and the tools are ported to Windows x64. The port has not
been compiled or run on Windows yet (see [Known limitations](#known-limitations)). In an "x64 Native Tools Command
Prompt for VS 2022":

```bat
rem clang-cl (Visual Studio's "C++ Clang tools"); leave out the two compiler options to build with cl.exe
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DLIYAB_ENABLE_EXPERIMENTAL=ON -DCMAKE_C_COMPILER=clang-cl -DCMAKE_CXX_COMPILER=clang-cl
cmake --build build
ctest --test-dir build --output-on-failure
build\liyab-cli.exe --device
```

What the port does differently from the POSIX platforms:

* **Mapping.** The GGUF is mapped with `CreateFileMappingW` / `MapViewOfFile` as one view. `PrefetchVirtualMemory`
  and `VirtualUnlock` (which takes unlocked pages out of the working set) stand in for `madvise`'s `WILLNEED` and
  `DONTNEED`; a mapped view has no `SEQUENTIAL` or `RANDOM` hint. The file stays deletable while it is mapped.
* **Direct reads.** `DirectFile` opens with `FILE_FLAG_NO_BUFFERING` (offsets, lengths and buffers in 4 KiB
  multiples, as with `O_DIRECT`) and reads with overlapped `ReadFile`, one event per request: requests made through
  a synchronous handle would run one after another. A volume that refuses an unbuffered read of the first block gets
  buffered reads.
* **Threads.** The pool's default size counts the physical cores of the highest efficiency class (an Intel hybrid's
  P-cores; every core of a homogeneous CPU), SMT siblings excluded. On machines with more than 64 logical
  processors, which Windows splits into processor groups, each worker is moved to a group so that the pool spreads
  over them. Workers wait with `PAUSE` and are named with `SetThreadDescription`.
* **Device.** The CPU name comes from the registry, memory from `GlobalMemoryStatusEx`, AVX2/FMA/F16C from
  `__cpuidex` / `_xgetbv` under MSVC and clang-cl.
* **Text.** Every path is UTF-8, as on the other platforms: the library converts paths to UTF-16 for Windows.
  `liyab-cli` reads its UTF-16 command line and switches the console to UTF-8 while it runs; the executables
  declare UTF-8 as their code page in their manifest (Windows 10 1903 and later).
* **Linking.** `liyab.dll` exports the C and the C++ API; CMake's `liyab` target defines `LIYAB_DLL_IMPORT` for the
  code that links it. An app that loads the DLL at run time (FFI) only needs the C API's exported names.
* **Not available on Windows:** the GPU and NPU backends (`LIYAB_USE_VULKAN`, `LIYAB_USE_QNN`,
  `LIYAB_USE_NEUROPILOT` stop the configuration), thermal readings (Windows has no thermal status, headroom forecast
  or sensor zones Liyab reads, so the steering of [Heat and power](#heat-and-power) stays idle while the profiles'
  rate caps and core shares still apply), and locking the expert cache in RAM (`VirtualLock` is capped by the
  working-set minimum).

### CMake options

| Option | Default | Effect |
| :--- | :--- | :--- |
| `LIYAB_USE_NEON` | ON on arm64 | NEON intrinsics kernels |
| `LIYAB_ARM_DOTPROD` | ON on arm64 | `-march=armv8.2-a+dotprod+fp16` on Android/iOS/Linux (SDOT) |
| `LIYAB_USE_AVX2` | ON on x86-64 | AVX2 + FMA + F16C kernels, used when CPUID reports them (the library itself keeps the x86-64 baseline) |
| `LIYAB_USE_METAL` | ON on Apple | Metal GPU backend |
| `LIYAB_USE_VULKAN` | ON on Android | Vulkan GPU backend and probe (loader opened with `dlopen`; shaders need `glslc` from the NDK or the Vulkan SDK); not available on Windows |
| `LIYAB_USE_QNN` / `LIYAB_USE_NEUROPILOT` | ON on Android | NPU runtime probes (no SDK needed); not available on Windows |
| `LIYAB_ENABLE_EXPERIMENTAL` | OFF | [Experimental modules](#experimental-modules) and `test_experimental` |
| `LIYAB_BUILD_SHARED` | ON | Shared (`.so`/`.dylib`/`.dll`) or static library |
| `LIYAB_BUILD_TESTS` / `LIYAB_BUILD_CLI` | ON | Unit tests, benchmarks and `liyab-cli` |

---

## Architecture

```
   Liyab app (Flutter, dart:ffi) · Kotlin (JNI) · Swift · C++ · other apps via the local API
                                     │
                         liyab_c_api.h  (stable C ABI)
                                     │
  ┌──────────────────────────────────▼──────────────────────────────────────────┐
  │ Engine                                                                      │
  │  ├─ Context manager ── turn-to-turn reuse, state snapshots, prefix cache,   │
  │  │                     cancellable chunked prefill, save/restore            │
  │  ├─ Generation ─────── sampler, grammars, forced text, speculative decoding │
  │  ├─ PowerManager ───── headroom forecast, pacing, performance hints, guards │
  │  ├─ DeviceDetect ───── SoC + accelerator probes → backend ranking           │
  │  └─ Transformer ────── per block: mixer (attention | Gated DeltaNet)        │
  │                        + FFN (dense | MoE), paged KV cache, recurrent state │
  └──────────┬───────────────────────────────────────────┬──────────────────────┘
             │ weights                                   │ matmuls (per-op route)
  ┌──────────▼─────────────────────────────┐   ┌─────────▼────────────────────────────┐
  │ MmapLoader      zero-copy GGUF, splits │   │ CPU   NEON · SDOT · i8mm · AVX2 ✅   │
  │ DirectFile      parallel O_DIRECT      │   │ GPU   Metal ✅ · Vulkan ✅            │
  │ TripleBuffer    streamed dense blocks  │   │ NPU   QNN · NeuroPilot (probe) 🟡    │
  │ ExpertStore     MoE expert cache:      │   │ fallback per matmul: NPU → GPU → CPU │
  │   LFU, prediction, size classes,       │   │ GPU-shared memory: the GPU reads     │
  │   repack on read, hot-list warmup      │   │ weights where storage wrote them     │
  └────────────────────────────────────────┘   └──────────────────────────────────────┘
```

* **Zero-copy weights.** `MmapLoader` maps the GGUF file read-only. Every tensor is a view into the mapping, and the
  CPU kernels read quantized blocks in place. On Apple Silicon each tensor is wrapped in an `MTLBuffer` with
  `newBufferWithBytesNoCopy`, so the GPU reads the page cache directly.
* **One forward pass for every architecture.** The transformer is not written per model. For each block the loader
  picks the token mixer from the tensors present (`ssm_conv1d` → Gated DeltaNet, `attn_kv_a_mqa` → multi-head latent
  attention, otherwise softmax attention) and detects optional pieces (QKV biases, Q/K norms, an attention output
  gate, the pre-FFN norm, norms after the attention and the FFN). The facts the tensors cannot tell are one row per
  architecture: whether Q/K norms come before or after RoPE, the FFN's activation (SwiGLU or GeGLU), whether
  embeddings are scaled, which blocks attend through a sliding window and with which RoPE base. The FFN is a mixture
  of experts when the block has a router. Scalars a model states in its file (RoPE scaling, soft caps, the q·k
  scale) are read from it. See [Supported models](#supported-models).
* **Per-operation routing.** Attention projections can go to the GPU and the FFN to the NPU. A backend that reports
  `Unsupported` for a matmul falls back to the next one for that matmul only.
* **Vulkan on phones.** Mobile drivers lack `VK_EXT_external_memory_host` (Adreno 830 included), so mapped weights
  cannot be wrapped in place. Liyab has two paths:
  * Streamed models: weights are placed in host-visible, device-local, coherent and cached memory. On Adreno that
    is the same RAM, and direct reads from storage land there. Native kernels (`shaders/matvec_native.comp`, 23
    formats) decode the GGUF blocks in place.
  * Models that fit: each tensor is copied once into GPU memory and repacked (`shaders/matvec.comp`).

  Kernels are compiled with `glslc` and embedded at build time. Matmuls that share an input go out in one submission,
  and a dispatch costs 0.055 ms.
* **Paged KV cache.** Fixed 64-token pages come from a pool on demand through page tables. Memory follows the
  positions actually used, and freed pages are reused exactly. Sliding windows keep the first `kv_sink_tokens`
  positions (attention sinks, default 8) plus the last *N*. Multi-head latent attention caches one row per position
  and block, its RoPE key and its latent, and reads the values from the latent channels of that row
  ([Supported models](#supported-models)). Attention scores a KV head's whole query
  group at once, and each V row is dequantized once per group. On a 2,812-token context this cut attention from 67.6
  to 44.4 ms per token on the 35B. Each token's visible positions are cut into up to 84 equal spans of at least 32
  positions, merged in order with log-sum-exp. While decoding, the spans of the one token are the tasks every
  thread shares (168 on two KV heads, an even split for 1 to 4 and 6 to 8 threads). The cut follows the token's own
  position, never the batch or the threads, so its attention is the same bits however the prompt was split.
* **KV laid out per block.** Blocks the model itself windows (Gemma 2's and 3's local layers, Phi-3's) see only
  their last *W* positions, so they keep only those rows. Layers are grouped by window: the blocks that see every
  position form one group, the windowed ones another, and each group maps its own pages. A windowed group lets go
  of every page no query can see any more, after a rollback of up to 64 positions (speculative verification), so
  its memory stays at its window whatever the context; the other group grows with the context. Every page still
  has one size and comes from one pool: a pool page holds 64 positions of *U* layers, *U* dividing each group's
  layer count (all the layers when no block is windowed), so a page one group frees is reused by the other,
  without fragmentation. Pages are zeroed when mapped. A model without windowed blocks keeps the single-table
  layout, byte for byte, with the same memory, and every model's logits are the same bits as before (golden
  hashes unchanged, Gemma 2 and 3 included). A context returns to an earlier position only where the window before
  it is still kept: inside the rollback margin, and at the state snapshots the engine takes (the end of each
  prompt, the oldest one), whose window pages are pinned instead of copied (the live window usually holds them
  anyway). With `segment_reuse` on, windowed blocks keep every position as before (a reused segment needs every
  block's rows). [Measurements](#per-block-kv).
* **Key scaling for quantized KV caches.** A quantized cache stores each key row in blocks of 32 values that share
  one scale, set by the block's largest value. Some model families carry a few key channels far larger than the
  rest and nearly constant across tokens: about −130 where the others are about 1 on Qwen2.5, up to ~300 on Qwen3.
  The small values sharing their block were then rounded with a step a hundred times too coarse, and almost all of
  a Q8_0 cache's error came from there. Attention only needs q·k, and q·k = (q∘t)·(k/t) for any positive
  per-channel t, so keys are stored divided by t and queries multiplied by it. Each channel then has the same range
  on both sides and the products are unchanged.
  * **Measured once per model**, on a short fixed text (about 45 tokens: prose, code, numbers, several scripts).
    For each channel, t takes the largest value the keys and queries reach at any position up to 32,768: RoPE turns
    each pair of channels by a known angle per position, so that range is exact even though the text covers only a
    few positions. Ranges are floored at a quarter of their head's median and t is bounded, so a channel the text
    barely reached cannot get an extreme factor. A model whose tokenizer cannot encode text (a pre-tokenizer
    Liyab does not have) cannot be measured: it loads with its keys as computed, and the log and `describe()`
    (a `Keys:` line) say so. On a model with large key channels that costs a quantized cache the accuracy above;
    an F16 cache loses nothing.
  * **Only where it helps.** A model is scaled when some head's largest key channel reaches 12 times its median
    channel: Qwen3-0.6B 107×, Qwen3-4B 87×, Qwen2.5-0.5B 52×. Below that (Qwen3.5-0.8B 10.5×, the Qwen3.6-35B
    MoE 7.4×, Qwen3.5-4B 7.5×, Llama 3.2 6.3×) scaling moved the KL against F16 only within noise, sometimes up,
    so those models keep their keys as computed, bit for bit. The first 12 tokens decide for most models; the
    rest of the text is processed only for those that need factors.
  * **Cost.** On the phone: 0.27 s for Qwen3.5-4B, 1.4 s for the 35B MoE (its experts are read from storage), 7.4
    s for a dense 27B larger than RAM, 1.4 s for Qwen3-4B, which is scaled. `EngineConfig::cache_dir` keeps the
    result (a few KB per model, the 16 most recently used models), so only a model's first load pays for it. The
    factors depend only on the model, the cache format and the kernel set, never on the backends or the configured
    context, so a prompt gets the same reply in every process. With the factors kept, speed is unchanged (A/B on
    the phone, 35B: decode 10.2 vs 10.0 tok/s, first token 5.8 vs 6.0 s).
  * **Saved contexts** carry the factors their keys were stored with; one saved with others (or before key scaling
    existed) is converted when loaded instead of being processed again.

  Measured against F16 ([Correctness](#correctness)): Q8_0 keys went from a mean KL of 0.070 to 0.0018 on
  Qwen2.5, 0.051 to 0.0021 on Qwen3-0.6B and 0.015 to 0.0063 on Qwen3-4B, with the same memory and kernels.
* **x86-64 kernels.** One binary runs on any x86-64 CPU. The library is compiled for the x86-64 baseline; the AVX2
  kernels (`src/core/quant_x86.cpp`) carry a per-function `target("avx2,fma,f16c")` attribute and run only when
  CPUID reports AVX2, FMA and F16C and the OS saves the 256-bit registers (Intel Haswell and AMD Zen onwards).
  The choice is made once per process; `LIYAB_KERNELS=scalar` forces the scalar set and `quant::kernel_isa()`
  reports `avx2` or `scalar`. They cover Q8_0 (single and multi-row), Q4_0, Q4_1, Q5_0, Q5_1, IQ4_NL and MXFP4
  against Q8_0 activations; Q4_K, Q5_K, Q6_K (1 to 4 rows per weight decode) and IQ4_XS against Q8_K; F32, F16
  and BF16 dots; Q8_0 / Q8_K activation quantization; F16 encoding and the F16, BF16, Q8_0, Q4_0, Q4_1 decodes
  of the KV cache and embeddings. The int8 products use `VPMADDUBSW` (|w| times x with w's sign, which cannot
  saturate because activations stay in [-127, 127]) and `VPMADDWD` against the sub-block scale, so a K-quant
  super-block accumulates exactly in int32. Q8_0 and the K-quants then apply the same float epilogues as the NEON
  kernels in the same order, so a row's result does not depend on the batch, and activation quantization and
  decoding give the scalar code's bits.
* **Thread pool.** Workers wait for the next job in `WFE` on ARM64: the core sleeps until the job word changes, with
  no instructions issued, instead of spinning at full clock; on x86-64 they spin with `PAUSE`. They block on a
  condition variable after 300 µs idle. A job is split into 4 chunks per thread, claimed on demand, so a preempted
  core does not hold up a whole matmul. Matmuls that share an input run as one group, and MoE experts run in waves:
  two fork/joins per wave instead of two per expert.

---

## Supported models

* **Format:** GGUF v2/v3, a single file or split with `gguf-split`. Open part 1; the other parts must sit next to it
  under their original names.
* **Architectures:**
  * `llama` (Llama 1/2/3.x, Mistral, TinyLlama…), `mistral`, `qwen2`, `qwen3`;
  * `qwen35`: Qwen3.5 / Qwen3.8 hybrids, with three Gated DeltaNet blocks per gated-attention block. The
    multi-token-prediction head is skipped;
  * mixture-of-experts: `qwen3moe` (Qwen3-30B-A3B…) and `qwen35moe` (Qwen3.5/3.6-35B-A3B…);
  * `hunyuan-dense` (Hunyuan-MT-7B, Hunyuan 0.5B–7B): Q/K norms after RoPE. Its dynamic-NTK "alpha" RoPE scaling
    is already folded into `rope.freq_base` by the GGUF converter. Its `hunyuan` / `hunyuan-dense` pre-tokenizers
    are table rows (below). A prompt must start with its BOS token, which the GGUF does not ask the tokenizer to
    add;
  * `gemma2` (Gemma 2): embeddings scaled by √d, GeGLU, norms after the attention and the FFN, every other block
    (the even ones) through the sliding window, and soft caps on the attention scores and the logits
    (cap · tanh(x / cap), from the file's `attn_logit_softcapping` and `final_logit_softcapping`; tanh is the
    engine's own (`core/portable_math.h`, within 1.32 ulp), because the C library's differs between Apple and
    Android in the last bits and the Mac and the phone gave Gemma 2 different logits; the logits' cap runs in
    chunks on the thread pool, the same bits for any
    thread count: 0.34 ms per token on one thread, 0.05 ms on eight, over a 256k vocabulary on an M-series Mac);
  * `gemma3` (Gemma 3 text models): embeddings scaled by √d, GeGLU, norms after the attention and the FFN, Q/K
    norms, five sliding-window blocks (RoPE base 10,000) per global block (the file's base and scaling). The GGUF
    stores its RMSNorm weights as 1 + w already, for Gemma 2 too;
  * `phi3` (Phi-3, Phi-3.5, Phi-4-mini): fused `attn_qkv` and `[gate | up]` projections, partial rotation, LongRoPE;
  * `ernie4_5` (ERNIE 4.5 dense: ERNIE-4.5-0.3B): a pre-norm block with SwiGLU, RoPE on adjacent pairs; the row was
    proposed and gated by `tools/describe_model.py` ([docs/model-descriptions.md](docs/model-descriptions.md)).
    The published GGUFs (unsloth, bartowski and mradermacher were checked) ask for a BOS token
    (`tokenizer.ggml.add_bos_token` true, or absent, which for a SentencePiece vocabulary means true) and, by
    leaving `tokenizer.ggml.add_space_prefix` out, for a space before the text, while the model's own tokenizer
    adds neither. Liyab reads the file as written, so such a file encodes text unlike the model's tokenizer from the
    first token on (the forward pass itself matches the reference). Fix a copy once; the tensors are copied as
    they are:

    ```bash
    tools/gguf_set_keys.py ERNIE-4.5-0.3B-PT-F16.gguf ERNIE-4.5-0.3B-PT-F16-fixed.gguf \
        --bool tokenizer.ggml.add_bos_token=false --bool tokenizer.ggml.add_space_prefix=false
    ```
  * `deepseek2` (DeepSeek-V2-Lite, DeepSeek-V3-structured models with one expert group, and the models converted to
    their architecture, such as Youtu-LLM-2B): multi-head latent attention, queries from one projection or a
    low-rank pair with its norm, dense FFNs in the leading blocks and MoE with shared experts in the others (from
    the tensors), YaRN with its log multiplier. The cache holds one row per position and block, `[k_pe | latent]`
    (576 values on DeepSeek-V2-Lite instead of the 5,120 of per-head keys and values), whose latent channels are the
    values. Attention reads it in one of two forms, chosen per forward pass:
    * absorbed (always for decoding): each head's query is projected onto the latent once (`attn_k_b`), so all
      heads attend over the cached rows themselves; the weighted latent is then expanded per head (`attn_v_b`). Per
      position and head that scores 576 channels and accumulates 512;
    * expanded (prefill batches): per-head keys `[W_kb c | k_pe]` and values `W_vb c` are expanded from the cached
      latents of the positions the batch sees, a tile of at most 256 positions at a time (5 MiB on
      DeepSeek-V2-Lite, plus 8 MiB of the decoded `attn_k_b` and `attn_v_b` of the block being run; never the
      whole context: the cache keeps latents only), and the batch attends over them: 192 channels scored and 128
      accumulated per position and head, for the cost of expanding each position once per pass instead of
      projecting each token's query. Tiles have absolute bounds and are merged in order, so a token's result is the
      same however its prompt was split into passes and however many threads run.

    The form is chosen from measured cost, measured once: each form's work is counted per pass from its batch size
    and context, and the ratio of what a multiply-add costs in each form on this device sets the threshold, so it is
    the device's own instead of a constant. The engine times both forms of one block on a synthetic pass at load
    (256 tokens after 768 cached positions, best of 3 each; 0.18 s on Youtu-LLM-2B on the Mac, ratio 0.595), rounds
    the ratio to 1/8 octave and keeps it in `EngineConfig::cache_dir` next to the key scales (measured again when
    the file is missing or damaged; without a `cache_dir`, kept in memory for the process only, and two processes
    may measure a step apart: 0.595 and 0.648 in three runs there). It is never re-measured on
    the fly: from then on a pass's form follows from its shape alone, so the same prompt gives the same bits on that
    device in every run, whatever else loads it. Another device (or another kernel set) may set another threshold
    and round a long prompt differently. The engine prefills these models in passes of 512 tokens (64 for other models, 1,024 with streamed
    experts): a pass of 64 tokens deep in a context does not repay expanding every position it sees, and stays
    absorbed. Both forms compute the same function and round differently: outputs are not bit-identical across
    forms (each form on its own is, and `test_golden` pins both); against transformers both give a mean KL of
    0.00000 with an F16 cache, and the expanded form is the closer with a Q8_0 one ([Correctness](#correctness)).
    `TransformerOptions::latent_form` / `EngineConfig::latent_form` pin one form. Queries are scaled for the
    per-head width the model was trained with (1/√192 there). Key scaling covers the latent too: the absorbed form
    multiplies the attention output back, the expanded one the latents before it expands them. Files converted
    before `attn_kv_b` was split into `attn_k_b` and `attn_v_b` are refused with a request to convert them again,
    and so is group-limited expert routing
    (`expert_group_count` > 1: DeepSeek-V2 236B, V3 and R1).

  Linear RoPE scaling, Llama 3.x `rope_freqs`, LongRoPE and YaRN are supported, and windowed blocks can rotate with
  a RoPE base of their own. LongRoPE picks its factors once, from the configured context: the short ones up to the
  model's original context (4,096 on Phi-3.5), where the result is the reference's, and the long ones beyond it from
  the first position on (the reference switches when the sequence grows past it, rotating earlier keys again).
  YaRN is read from the file's `rope.scaling.*` keys (factor, original context, `yarn_beta_fast` / `yarn_beta_slow`,
  `yarn_ext_factor`, `yarn_truncate`, `yarn_attn_factor`, `yarn_log_multiplier`): each rotary pair's frequency is
  blended between its own and the one divided by the factor along the reference's ramp, and queries and keys get
  its attention factor (0.1 ln factor + 1 unless the file states one). It does not depend on the context length,
  so one table serves every position. The q·k scale is the file's `attention.scale` when it has one, else 1/√head_dim.
  `liyab_supported_architectures()` lists what a build runs, so front ends can filter downloads.
* **Embedding models and rerankers** built on these architectures (Qwen3-Embedding, Qwen3-Reranker) run as their
  GGUF declares them: see [Embeddings and reranking](#embeddings-and-reranking). Encoder-only models (BERT, XLM-R)
  are not supported.
* **MoE details:**
  * softmax or sigmoid gating, optional selection bias, top-k, renormalization and scale from the metadata;
  * an optional shared expert with a sigmoid gate;
  * each expert's gate and up projections as two tensors or as one `[gate | up]` tensor (`ffn_gate_up_exps`,
    written by converters that fuse them); the fused rows are the split ones, so the logits are the same bits;
  * the tokens of a batch are grouped per expert, so each expert is read once.
* **Hybrid models:** DeltaNet blocks keep a recurrent state: conv history plus one 128×128 matrix per value head.
  These models can roll back only:
  * inside a window of state checkpoints (used by speculative decoding), or
  * to one of four state snapshots (the oldest, the end of the last prompt, and the two newest others).
* **Tensor types:** every format llama.cpp writes, mixed freely per tensor:
  * F32, F16, BF16;
  * Q4_0/Q4_1/Q5_0/Q5_1/Q8_0;
  * Q2_K…Q6_K (and the S/M/L mixes);
  * IQ1_S/M, IQ2_XXS/XS/S, IQ3_XXS/S, IQ4_NL/XS;
  * TQ1_0/TQ2_0, MXFP4, NVFP4.

  Decoders are ported from llama.cpp's gguf-py reference, and `test_engine` checks all 24 formats bit-exactly against
  `tests/data/quant_vectors.bin`.
* **Kernels:**
  * Q4_0/Q4_1/Q5_0/Q5_1/Q8_0 have NEON + SDOT kernels that unpack bits in registers.
  * K-quants, TQ2_0 and I-quants use NEON kernels adapted from llama.cpp (`src/core/quant_lowbit.cpp`) against
    Q8_K activations, so a whole super-block accumulates in int32.
  * IQ4_NL and MXFP4 use table lookups.
  * With i8mm, resident Q4_K/Q5_K/Q6_K/Q8_0 matrices are rearranged losslessly at load into 8-row (4-row for Q8_0)
    interleaved layouts. One SMMLA then multiplies 8 weight rows by 4 activation rows.
  * Every kernel of a format ends each block the same way: exact integer sums, then the same fused multiply-adds in
    the same order. That holds on the file's layout or repacked, for one activation row or several. A row's result
    is then the same bits whichever kernel computed it, so logits depend neither on the batch size nor on the layout
    (tested for every format).
* **Tokenizers:** SentencePiece (`llama`: Llama 2, Mistral, Gemma, Phi-3) and byte-level BPE (`gpt2`).
  * **Pre-tokenizers are data.** Before merging, a byte-level BPE tokenizer cuts the text into pieces with regular
    expressions. Each scheme is one row of a table keyed by the GGUF's `tokenizer.ggml.pre`
    (`src/core/pre_tokenizer.cpp`): the patterns of the model's own `tokenizer.json`, NFC normalization where it
    asks for it (Qwen), and whole-piece vocabulary lookup before merging (Llama 3, Hunyuan, Tekken). Rows:
    `default` / `gpt-2` / `gpt2` / `phi-2`, `llama-bpe` / `llama3`, `qwen2` / `deepseek-r1-qwen`, `qwen35`,
    `hunyuan`, `hunyuan-dense` / `deepseek-v3`, `deepseek-llm`, `gpt-4o` (Phi-4-mini), `smollm` (SmolLM2: every
    digit alone, then GPT-2's split), `tekken` (Mistral-Nemo) and `youtu` (Youtu-LLM: Hangul, CJK punctuation,
    Bopomofo and Han/kana runs first; its `\p{Hangul}` is written out as the script's code-point ranges, since the
    regex engine has categories, not scripts). A GGUF without the key uses `default`. Any other value is an error
    naming it and the supported list; the model still loads and runs on token ids, with a quantized KV cache too
    (its keys then unscaled, see [key scaling](#architecture)).
  * **Liyab's own regex engine** (`src/core/regex.cpp`) runs the patterns: Unicode general categories (`\p{L}`,
    `\p{Lu}`, `\P{N}`…), classes, alternation, greedy, lazy and possessive quantifiers, case-insensitive groups,
    lookahead and atomic groups. It decodes the text once into code points with a category key each, so a class
    test is a bit lookup. The Unicode data (categories, NFC tables) is generated into `src/core/unicode_tables.inc`
    by `tools/gen_unicode_tables.py`.
  * **Special tokens** written in the text map to their ids, found in one pass over the text. Those of the Phi-3
    family (Phi-3/3.5, Phi-4-mini) swallow the white space after them, as their Hugging Face tokenizer does. A
    byte a vocabulary lacks (Hunyuan's dense models have no `\r`) is left out before merging, as there.
  * **Checked token for token** against each model's Hugging Face tokenizer, special tokens, contractions,
    digits, white-space runs, composed and decomposed accents, CJK, emoji and right-to-left text included
    ([Correctness](#correctness)).
  * **Speed.** Tokenizing sits on the typing path (prompts are encoded while the user writes). Merges compare token
    ids through a heap, never strings, so a long piece costs O(n log n). On an Apple M4 Pro a 68 KB text encodes in
    2.4–3.6 ms (19–28 MB/s, Qwen3, Qwen3.5, Llama 3.2) and an 80 KB conversation full of special tokens in 2.5–3.2 ms.
* **Chat templates from the model.** Every GGUF carries the Jinja chat template of its Hugging Face tokenizer
  (`tokenizer.chat_template`). Liyab's own Jinja interpreter (`src/core/chat_template.cpp`) renders it the way
  transformers' `apply_chat_template` does: the same whitespace rules, Python's printing, `tojson`,
  `raise_exception`, `strftime_now`, loops with `loop.previtem` / `nextitem`, macros, namespaces, string methods and
  the usual filters and tests, and the sandbox's refusal of methods that change a list or dict.
  * `Engine::render_chat` (C: `liyab_engine_render_chat`) takes the request as JSON: `messages`, optional `tools`
    and `add_generation_prompt`, and any template variable such as `enable_thinking`. A text that starts with the
    BOS token's own text (Llama 3, Gemma) gets no second BOS when tokenized.
  * `Engine::chat_format` (C: `liyab_engine_chat_format`) renders probe conversations and reports how the template
    lays out turns: the system block, what opens and closes a user turn, the generation prompt and what ends a
    reply. It also says whether the template is **prefix-stable**: rendering *n* turns, then the reply, must be the
    start of rendering *n* + 1 turns, which context reuse across turns needs. Llama 3, Qwen2.5, Gemma 3, Phi-3.5,
    Phi-4-mini, Hunyuan-MT, DeepSeek V3.1, and Qwen3.6 with `preserve_thinking`, are. Qwen3 and Qwen3.5 are not:
    they drop the reasoning of earlier replies once the conversation goes on. The load log says which.
  * Checked byte for byte against transformers on 14 conversations per template (system, user, assistant and tool
    turns, tools, inline and separate reasoning, thinking on and off, no system message, non-ASCII and white space
    at the edges), for Qwen2.5, Qwen3, Qwen3.5, Qwen3.6, Llama 3.2, Gemma 3, Phi-3.5, Phi-4-mini, Hunyuan-MT,
    Hunyuan-0.5B, Hunyuan-A13B and DeepSeek V3.1: 165 renders identical, and the 3 conversations transformers
    refuses refused too (`tests/data/chat_templates.json`, written by `tools/chat_template_reference.py`). The
    templates the GGUFs themselves carry gave the same 168 results.
* **Prompts are used as given** by `generate()` and `prefill()`: render them with the template first (the app does).

---

## Models larger than RAM

Streaming switches on automatically when a model does not fit, that is, when the file is larger than 80% of the
available memory or of `memory_budget_mb`.

* **Storage that is fast only when used right.** UFS 4 reaches ~4.4 GB/s with 2–4 direct requests of ≥ 256 KiB in
  flight, random or sequential alike, but stays under 1.2 GB/s with 16 KiB requests (see the
  [flash chart](#charts)).
  * `DirectFile` reads with `O_DIRECT` (`F_NOCACHE` on Apple, `FILE_FLAG_NO_BUFFERING` on Windows), so there is no
    page-cache copy and resident weights are not evicted. It splits large reads into concurrent 4 MiB requests.
  * On FUSE (Android's `/storage/emulated`), direct reads were seen to return success without the file's bytes, so
    Liyab never uses them there, and it self-tests direct against buffered reads before trusting any file.
* **Dense models.** As many blocks as fit stay resident. The others stream through a 3-slot pipeline (fetch →
  prepare → execute), spread evenly through the stack so storage keeps reading while resident blocks compute. With
  Vulkan, slots and resident blocks live in GPU-shared memory, where the native kernels decode them in place.
* **Mixture-of-experts models.** Everything but the routed experts stays resident. Experts go through the
  `ExpertStore`:
  * **A RAM cache sized by the memory plan.** It holds one entry per expert (gate/up/down) in slot size classes per
    matrix layout. Eviction is LFU with periodic halving. A freshly loaded expert is not evicted before the block it
    was loaded for has used it.
  * **Prediction one block ahead.** After a block's mixer, the next block's router is applied to the residual stream
    and the experts it picks are prefetched, ordered by rank and only while that rank's guesses pay off. On
    Qwen3.6-35B-A3B about 79–83% of guesses are chosen. Wrong guesses are settled as soon as the real router
    chooses: queued ones are dropped, and ones already read become the next to evict.
  * **Reads shaped for flash.** Four I/O threads read the experts. The thread that starts an expert reads its gate
    matrix and hands up and down to idle threads, so a waiting forward pass gets its expert after one matrix's read
    instead of three. A fused `[gate | up]` matrix is contiguous per expert: one read, then down, two in all.
  * **Compute that overlaps I/O.** Experts already in RAM run first, in one batched pass (gate/up, then down). The
    shared expert runs while the routed ones wait for a read.
  * **Batch-aware.** For a multi-token pass (prefill), experts are rearranged into the i8mm layouts on the I/O
    thread as they arrive. Prefill runs in passes of 1,024 tokens, each reading the union of its tokens' experts
    once. Such passes give the experts no LFU credit, so a long prompt does not evict the experts a conversation
    keeps using. A pass of [several sequences](#context-memory-and-serving)' decoding steps, one token each, is
    decoding: their experts are read in the file's layout and credited as a single sequence's are (served as a
    prefill, two sequences on Qwen3-30B-A3B decoded at 0.60x the speed of taking turns; as decoding, 0.96x).
  * **Deterministic.** Each token's expert outputs are added in router order, whatever order they arrived in, and a
    repacked expert rounds like one in the file's layout. Results therefore depend neither on I/O timing nor on what
    the cache held: streamed and in-place experts give bit-identical logits (tested).
* **Memory plan.** `Engine::memory_plan()` reports the resident bytes, the experts' bytes, the expert cache and the
  budget at which 15% of the experts would be cached, so a front end can tell the user when a budget is too small.
  With `requant_bits = -1` (the app's default), resident Q8_0 matrices are converted to Q5_K or Q4_K at load **only**
  when the expert cache would otherwise hold under 10% of the experts. That is the point where nearly every token
  would wait on storage.
* **Optional lossy trade-offs**, all measured with `liyab-kl` (see [results](#qwen36-35b-a3b-a-22-gb-moe-on-a-phone)):
  * `requant_bits` 4/5: fewer resident bytes;
  * `moe_expert_mass`: run only the top experts covering a share of the router weight;
  * `moe_max_experts`: cap the experts per token;
  * `moe_skip_slow`: skip a light expert that is not in RAM yet instead of waiting for it (replies then depend on
    I/O timing).

---

## Context, memory and serving

A phone serves one user, but that user switches conversations, types, leaves the app and comes back. Liyab treats
each of those as a scheduling problem.

* **Context reuse across turns.** When a prompt continues the text the engine already processed (the previous prompt
  plus its reply, which is how a chat grows), that text keeps the tokens it was processed as. Only the rest is
  computed, recurrent DeltaNet states included. Re-encoding a reply need not reproduce the generated tokens (around
  `</think>`, for example), and that no longer forces a restart. The engine keeps knowing which text its tokens
  encode through work that is cancelled or cut short (a prefill typed ahead, a reply stopped while its prompt is
  processed), through rewinds and through `save_state()`. A prompt that leaves that text partway (a draft edited, a
  message prepared ahead then typed over) keeps its tokens up to where the texts part. When that text ends inside a
  character (a model may write one in two byte-level tokens), the tokens step back to the last whole character
  instead of the prompt being encoded again. Otherwise the longest common
  token prefix is kept: any length on attention-only models, and back to the nearest state snapshot on hybrid ones;
  the log says at which token a prompt left the context. On the 35B, follow-up turns start in ~1.1–1.6 s instead of
  reprocessing the conversation.
* **State snapshots for hybrid models.** Four are kept: the oldest one, the end of the last prompt (pinned, so
  background drafts cannot evict it), and the two newest others (a draft's words and the whole draft after them).
  They are set aside from the expert cache's budget (62.8 MiB each on the 35B).
* **Prefix cache across conversations** (`prefix_cache_mb`, `prefix_cache_dir`). A context that another prompt
  replaces (or an embedding call) is set aside in a content-addressed store of KV chunks. A prompt replaces it when
  it shares less than half of it, or leaves it before the end of its last prompt and rewinding would process at
  least 128 tokens again: another chat after a long shared system prompt, an edited message (on a hybrid model,
  rewinding goes back to the nearest state snapshot). A draft typed ahead and edited after the last reply keeps
  using the context's own snapshots instead. Whenever a prompt leaves the context, the store is asked for more of
  it than the context keeps. A chunk is a whole number of pages of the paged KV cache, about 2 MiB and at most
  256 tokens (each is a file on storage, and creating one costs about as much as writing a megabyte), keyed by a
  hash chained over every token before it and rooted in what its bytes depend on (the model file, cache layout and
  type, key scales, kernels and backends, a latent-attention model's prefill form, and the
  [LoRA adapter](#lora-adapters) selected with its scale, if any). A prefix that several
  conversations share (the system prompt, the tool block, the start of a conversation) is therefore stored once,
  and setting a conversation aside again writes only its new chunks. A later prompt is restored up to the longest
  prefix the store holds, chunk by chunk, then cut to where the two diverge, even when its earlier replies would
  encode to other tokens: the store keeps the text each context encodes. The rows the live context already holds
  for the same tokens stay where they are. Recurrent states cannot be cut into chunks, so a hybrid model keeps them
  as images at the positions the prefix cache always kept (the end of the context, the end of its last prompt and
  the oldest snapshot). Each image is attached to a chunk holding its prefix and moves to another such chunk when
  that one goes; a prompt restores up to the deepest one it reaches. Windowed blocks (Gemma 2 and 3, Phi-3) keep
  only their window, so their rows are not in the chunks (which hold the other blocks' rows): they go to the store
  page by page, each window page keyed by the prefix ending at its page's end (or at the context's end or a
  snapshot inside a page), so they are shared between contexts as chunks are. A context set aside keeps the window
  pages its cache still holds (the window before its end and before its snapshots), and a prompt restores to the
  deepest position whose own window page is stored along with every page of the window before it; the snapshots
  below it come back with their windows. The output equals that of a context never interrupted (tested on
  attention-only, hybrid and windowed models, in RAM, on storage and in a later engine).
  * **Tiers and caps.** RAM (`prefix_cache_mb`) holds the most recently used chunks. It comes out of the memory
    budget; on a MoE whose experts stream, only as far as the expert cache can spare above 10% of the experts, so
    it never causes a requantization. What RAM cannot hold goes to storage (`prefix_cache_dir`,
    `prefix_cache_disk_mb`), which costs no RAM at all. What storage cannot hold goes, least recently used first:
    a chunk with every chunk after it, a state image on its own. Room is made before anything is written, so
    neither tier is ever above its cap. A 2,000-token conversation on the 35B costs ~21 MiB of chunks plus
    62.8 MiB per state image.
  * **Across runs.** The storage tier outlives the engine. When destroyed, the engine sets its context aside
    there too, and a later engine or process with the same model and settings restores from it: a system prompt
    or a conversation comes back after a restart without being processed again. Other models' chunks stay and
    count against the cap. Files are written to a temporary name and renamed. When it opens the directory, the
    engine removes interrupted writes, damaged files, other format versions, broken chains and the files of
    builds before the store; a chunk whose payload hash does not match when read is removed and the prompt
    processed. One engine at a time uses a directory (an OS lock); another one runs without the storage tier.
  * **Compressed on storage, only where it pays.** What fills the storage cap is the KV rows, so a chunk can be
    written compressed (`src/core/kv_codec.cpp`) and decoded when read back; RAM keeps rows as they are, and every
    cap counts the bytes written. Measured on real pages of Qwen3-0.6B, Qwen3.5-0.8B and Llama 3.2 1B, KV bytes are
    close to random except the exponents of 16-bit floats, which stay near the largest one their channel takes in
    the page. The lossless encoding therefore stores each 16-bit float (F16 values, Q8_0 block scales) as its low
    byte plus a symbol for its high byte relative to its channel's largest exponent, and codes those symbols with
    our own static rANS coder (12-bit tables per plane, 4 interleaved states, branchless refills). Q8_0 quants are
    coded too, a key channel that changes less from one position to the next than it is large (the slowly turning
    RoPE pairs) as those differences. Pages are encoded one by one and decoded straight into the cache's pages,
    layers in parallel on the engine's threads. With every stream coded (`liyab-kl --store-codec`, 2,047
    positions, every logit identical; decode and encode on the Mac's chunk files, M4 Pro, best of 3):

    | Cache | Stored / raw | Contexts per 512 MB (2,000 tokens) | Decode, 1 thread / 10 | Encode, 10 threads |
    | :--- | ---: | ---: | ---: | ---: |
    | F16 (Qwen3-0.6B, Qwen3.5-0.8B, Llama 3.2 1B) | 1 / 1.168–1.177 | Qwen3-0.6B 2.34 → 2.74 | 0.65–0.89 / 0.11–0.16 ms per MiB | 0.34–0.55 ms per MiB |
    | Q8_0 (same) | 1 / 1.11–1.13 | Qwen3-0.6B 4.41 → 4.90 | 0.83–1.7 / 0.13–0.4 ms per MiB | 0.5–0.8 ms per MiB |

    Restores come first, so a stream is coded only when the read time its smaller size saves exceeds the time
    decoding it takes, on this device: once per storage directory, cache layout and thread count, the store
    writes an 8 MiB probe file next to its chunks, reads it back uncached (`O_DIRECT` / `F_NOCACHE`) and through
    its own buffered, hashed read (a read costs the slower of the two), and decodes a synthetic chunk of the
    layout on the pool. The result is kept in `cache_dir` (`kv-costs-*.bin`, 16 sets at most), so what is coded
    is fixed afterwards; where reads cannot be measured uncached, nothing is coded. A coded stream saves less than
    its own size, so where decoding a symbol costs at least as much as reading a byte nothing can pay: chunks are
    then written raw without trying, and set-asides and restores are exactly those of raw chunks. While a
    compressed chunk decodes, the next one's file is read on a thread of its own (`KvStore::read_ahead()`).
    On the Mac (M4 Pro: reads 8.4–8.8 GB/s, decoding 0.23–0.46 ns per symbol on 10 threads) nothing pays,
    and restores equal the raw store's (alternating runs, 5 each; "coded" forces every stream coded):

    | Context | Raw store | This build (raw chosen) | Coded | Storage, raw → coded |
    | :--- | ---: | ---: | ---: | ---: |
    | Qwen3.5-0.8B Q8_0, 27.9k tokens | 36.3–40.3 ms | 36.3–37.8 ms | 156–192 ms | 213 → 194 MiB |
    | Qwen3.5-0.8B F16, 27.9k tokens | 59.8–61.5 ms | 60.0–62.2 ms | 84.6–86.8 ms | 367 → 320 MiB |
    | Qwen3-0.6B Q8_0, 8.3k tokens | 73.2–75.1 ms | 73.1–75.1 ms | 155–161 ms | 480 → 430 MiB |
    | Qwen3-0.6B F16, 8.3k tokens | 137–141 ms | 134–140 ms | 192–201 ms | 903 → 772 MiB |

    Old raw chunk files stay readable; a build that does not know an encoding removes its files when it opens the
    directory. Recurrent state images are stored raw: their 32-bit floats would code ~13% smaller (Qwen3.5-0.8B),
    which on such storage would not pay either.
  * **Lossy, opt-in** (`prefix_cache_lossy`, `--prefix-cache-lossy`): chunks re-quantized to 4 bits on their way
    to storage. Keys channel by channel, each (layer, KV head, channel) with its own minimum and step over the
    chunk's 64 positions, so the few large, nearly constant key channels of some models keep their own range
    (key scaling, from the chunk itself); values in 32-channel blocks of one position (Q4_1). They come back in
    the cache's type. 3.37× smaller than F16 rows, 1.79× than Q8_0 (Qwen3-0.6B F16: 2.34 → 7.9 contexts of
    2,000 tokens per 512 MB). Cost, `liyab-kl` against the uncompressed restore (every page after the first
    attended to as decoded), 2,047 positions:

    | Model | Cache | KL mean / median | Top-1 agreement | Perplexity |
    | :--- | :--- | ---: | ---: | ---: |
    | Qwen3-0.6B | F16 | 0.0061 / 0.0023 | 96.34% | 14.475 → 14.518 |
    | Qwen3-0.6B | Q8_0 | 0.0063 / 0.0026 | 96.14% | 14.472 → 14.584 |
    | Qwen3.5-0.8B | F16 | 0.0017 / 0.0007 | 97.95% | 10.424 → 10.424 |
    | Qwen3.5-0.8B | Q8_0 | 0.0019 / 0.0007 | 97.85% | 10.428 → 10.414 |
    | Llama 3.2 1B | F16 | 0.0070 / 0.0032 | 95.51% | 13.981 → 14.224 |
    | Llama 3.2 1B | Q8_0 | 0.0078 / 0.0034 | 95.70% | 14.005 → 14.192 |

    A lossy engine keys its chunks apart (its store's seed differs): they are never restored by an engine that
    did not opt in, and a lossy chunk under a lossless engine's own key is removed as untrusted. Q4_0 / Q4_1
    caches are already 4-bit: they are stored lossless.
  * **Measured on the Mac** (8 threads; the app's configuration: storage only, 512 MiB) with a scripted workload: a
    1,392-token system and tool block, seven chats with 160-token replies, four of them resumed (two twice), three
    abandoned, then a restart that resumes the first. Every reply equals that of a context never interrupted, with
    this cache and with the earlier per-context one.
    * Qwen3-0.6B: 91.1% of prompt tokens reused, against 84.4%. The earlier cache set nothing aside (each chat was
      shorter than the system block), so a resumed chat processed its turns again: 1.8–3.8 s to the first token,
      against 0.19–0.25 s. A set-aside took 3–24 ms and wrote only the chat's own chunks, 10–13 MiB (91 MiB for the
      first context), where the earlier cache wrote the whole context each time; a restore took 1–4 ms, the system
      block's rows staying in place. Storage peaked at 208 MiB. After the restart the first chat came back from
      storage: 0.17 s to the first token instead of 14.5 s.
    * Qwen3.5-0.8B (hybrid): 44.5% reused, against nothing (rewinding went back to the start, the nearest state
      snapshot). Every resumed turn was restored: 0.19–0.30 s to the first token against 12–18 s. New chats still
      process the system block, whose end has no state snapshot when it is not prepared on its own. A set-aside
      wrote 1–2 chunks of 4 pages and 2 state images, ~40 MiB, in 9–11 ms; storage peaked at 312 MiB (352 MiB once
      the engine set its context aside when destroyed). After the restart: 0.17 s to the first token instead of
      18.4 s.
    * Throughput, Qwen3.5-0.8B with a 25.8k-token context and three state images (218.6 MiB), alternating runs:
      set aside in 43–49 ms (4.7–5.3 GB/s) and restored in 28–31 ms (7.5–8.3 GB/s), where the earlier cache wrote
      its one file in 23–25 ms and read it back in 41–47 ms. State images are read into the model's states and the
      snapshots' own buffers, and written from them, with no copy in between; each 1 MiB block is hashed while it
      is in cache (xxHash64 runs at ~25 GB/s, reading from the page cache at ~17).
    * Decoding is as fast as before (alternating runs, best of 3: 68.6, 67.9, 62.9 tok/s before; 68.9, 68.6,
      63.3 after).
  * On the phone (Snapdragon 8 Elite, Qwen3.6-35B-A3B, the app's 512 MiB on storage), a chat of 1,355 tokens
    that a local-API request replaced was set aside in 73 ms (2 of its 8 chunks new, its 2 state images: 127.7
    MiB written) and restored in 151 ms when the next message came, which then processed 17 new tokens and
    gave its first token 1.66 s after sending. The same chat set aside again one message later wrote 1 new
    chunk and its 2 state images (126.0 MiB) in 87 ms and came back in 127 ms. Most of what is written is the
    DeltaNet state images (62.8 MiB each), which change with every turn; the KV chunks are written once. The
    store's files outlived an update of the app: the next load kept 9 chunks and 2 contexts. (With the earlier
    per-context cache, a 4,907-token chat (114 MiB) was set aside in 81 ms and restored in 95 ms, where
    processing a 4,009-token one again had taken 163 s.)
* **Segment reuse: KV reused away from its prefix** (`segment_reuse`; opt-in and lossy). An agent's prompts carry
  documents, memory snippets and tool results in the middle, and a change before them forced everything after them
  to be processed again. A request can mark parts of its prompt (`GenerateOptions::segments`,
  `liyab_engine_generate_segmented`, `prefill()` with segments: byte ranges of a system block, tools, documents,
  tool results, turns). With segment reuse on, the KV of each marked part is kept, and a later prompt that holds the
  same part anywhere takes it from there instead of processing it again.
  * **Exact reuse first.** What the live context or the prefix cache holds of a prompt is kept or restored as
    before, losslessly; segments are reused only after it. A request that marks nothing never sees a reused row: a
    context holding some is processed again from the first one, the prefix cache keeps only the rows before it,
    and `save_state()` records where they start.
  * **Kept in the prefix cache's store.** A segment is kept once a prompt marking it has been processed, as a
    context of its own whose tokens sit between two ids no vocabulary has, the first naming the position it was
    computed at. So it gets the store's tiers, caps, LRU order and files, and no prompt's chain ever reaches it
    (its rows are exact only after what preceded it there). It is kept once, as first computed, and reused from
    there wherever it appears. Text a segment holds is encoded on its own, so its tokens are the same wherever
    it appears (with a SentencePiece vocabulary, wherever it follows the same kind of token), and segments
    shorter than 16 tokens are processed as usual.
  * **Turned to its new positions.** RoPE turns each key by an angle proportional to its position, so a stored key
    is turned back by its old angle and on by its new one, with each block's own table: both pairings, partial
    rotation, `rope_freqs`, linear scaling, LongRoPE, YaRN, the windowed blocks' own base, latent attention's RoPE
    key. Key scales and Q/K norms after RoPE are taken out first and put back after; only the quantized blocks
    that hold rotated channels are rounded again, and values, latents and keys moved by 0 keep their bits.
    Measured with `liyab-reuse --shift` (a context's rows moved 300 or 3,000 positions away and back, so rounded
    twice), against the unmoved context: KL 0.0003–0.0004 on Qwen3-0.6B and 0.0006–0.0007 on Llama 3.2 1B with
    a Q8_0 cache, under 0.000001 with F16, 0.02–0.03 with Q4_0. Segments are therefore kept in the cache's own
    format: an F16 copy would take nearly twice the memory of a Q8_0 one to remove a difference two orders of
    magnitude below what reuse itself changes, and an INT4 cache's extra rounding is part of what the
    calibration measures. A move takes ~4 µs per position across all the blocks of a 1B model on the Mac.
  * **Partly processed again.** Reused rows lack attention to what now precedes them. Every reused token runs the
    first two blocks again with the tokens around it; the share whose keys and values moved most there runs
    through the rest of the model, the others keep their reused rows. The whole span from the end of the exact
    prefix to the last reused token goes block by block, in passes in order, so each token sees every position
    before it. The share is not a constant: the engine measures it per model on prompts shaped like real ones,
    the documents of the corpus below in the model's own chat template: three prompts store them, four others
    arrange 3 to 5 of them in other orders, each followed in turn by three questions about them. For each share
    of 5, 10, 15, 20, 30 and 45% it takes the mean KL of the answers against processing the whole prompt, and a
    bound above it (1.645 standard errors of the 12 questions' own means); it keeps the smallest share whose
    bound, and every larger share's, is within `segment_reuse_max_kl` (default 0.03). With none, the model is
    refused. `Engine::segment_reuse()` gives the share and the calibration's KL, bound and top-1,
    `GenerationStats` and `PrefixCacheStats` what was reused.
  * **Calibrated in the background.** Loading does not wait for the measurement: it runs once the engine has
    been idle for 2 s, a stage (a few passes over one prompt's documents) at a time, on a context of its own
    swapped in for the stage, so the conversation's context stays as it was. A call arriving meanwhile stops
    the stage between two blocks, waiting a fraction of a second instead of getting `Busy`, and the stage runs
    again at the next idle time. Until the measurement ends segment reuse is off: marked prompts are processed as
    usual, and `Engine::segment_reuse()` reports `Busy` with its progress. The result is kept in `cache_dir`, so
    the next engine has it at once (without one, every load measures again).
  * **Measured on the Mac** (`liyab-reuse`; CPU, Q8_0 cache with key scaling; on a Mac other jobs loaded heavily,
    so times are compared within each run). 8 prompts per model: the system prompt of a small company's
    assistant, 3–5 of its 12 documents in random order (77–80% of ~555 tokens) and a question, through the
    model's chat template, after warm-up prompts had stored the documents in other orders. (The calibration
    draws on the same corpus, in other arrangements.) Quality against
    processing the whole prompt, at the first answer token and each next one up to the end of the greedy answer
    (at most 33); the first token's time against the lossless path, the part before the first document restored
    from the prefix cache and the rest processed:

    | Model | Processed again | Mean KL | Median KL | Top-1 | Same greedy answer | First token sooner |
    | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
    | Qwen3-0.6B | 0% | 0.049 | 0.0013 | 95.7% | 2 of 8 | 5.5× |
    | | 10% | 0.041 | 0.0012 | 96.2% | 3 of 8 | 3.7× |
    | | 20% | 0.030 | 0.0008 | 95.7% | 1 of 8 | 2.8× |
    | | 30% | 0.026 | 0.0006 | 98.3% | 4 of 8 | 2.5× |
    | Llama 3.2 1B | 0% | 0.027 | 0.0034 | 96.5% | 3 of 8 | 4.2× |
    | | 10% | 0.020 | 0.0025 | 97.2% | 4 of 8 | 3.2× |
    | | 20% | 0.013 | 0.0021 | 98.0% | 4 of 8 | 2.7× |
    | | 30% | 0.011 | 0.0015 | 98.4% | 4 of 8 | 2.2× |

    The first token comes as much sooner as the work left predicts: the selection runs 2 of Qwen3-0.6B's 28
    blocks (2 of Llama's 16) for every reused token, the share processed again all of them. The mean KL is a
    few answer tokens' doing: the median is 6 (Llama) to 48 (Qwen3) times lower, the largest single token's KL
    0.3–1.9. A reused document costs the store its rows, ~60 KiB per token on Qwen3-0.6B and ~17 KiB on Llama
    3.2 1B. Documents kept from prompts that had themselves reused others, as the engine keeps them
    (`--warm-up-reuse`, at 10% on Qwen3-0.6B and 5% on Llama), give the same KL within 0.0006: copies made after
    reused rows add no measurable error of their own.
  * **Which tokens are processed again matters**, at equal work too. Mean KL on Qwen3-0.6B at 10, 20 and 30%:
    the deviation criterion 0.041, 0.030, 0.026; random tokens 0.045, 0.043, 0.039; each document's first ones
    0.052, 0.041, 0.056; ranked by the attention the prompt's last tokens pay them (the question taken into the
    pass) 0.037, 0.038, 0.034, and by that attention times their deviation 0.042, 0.037, 0.026; the deviation
    with each document's first 8 tokens added 0.046 and 0.036 (10 and 20%), compared at block 3 instead of
    block 1 0.039 and 0.037. On Llama 3.2 1B random tokens give 0.025, 0.022, 0.018. Random needs no selection
    pass, yet with it counted the deviation still leads: at 20% it costs 26% of the documents' work on
    Qwen3-0.6B and 30% on Llama, and gives 0.030 and 0.013 where random tokens at 30% give 0.039 and 0.018.
    So the deviation at block 1 is the default (`liyab-reuse --criterion`, `--select-block` and `--first-tokens`
    measure the others).
  * **The calibration against the measurement.** The share the calibration keeps holds on the prompts measured
    above (`liyab-reuse --calibrate 0.03` runs both), or the model is refused:

    | Model | Kept at the default target (0.03) | Calibration: mean KL (bound) | Measured above at that share | First token sooner |
    | :--- | ---: | ---: | ---: | ---: |
    | Llama 3.2 1B | 15% | 0.0219 (0.0280) | 0.0162 | 3.0× |
    | Qwen3-0.6B | refused (45%, the largest) | 0.0364 (0.0543) | 0.0180 | |
    | Qwen3.5-0.8B | refused: hybrid | | | |

    Its prompts ask more than the measured ones. From 5 to 45% Llama's calibration gives 0.035, 0.027, 0.022,
    0.019, 0.019 and 0.012 (bounds 0.045 to 0.016), where the measured prompts give 0.020 at 10% and 0.013 at
    20%. Qwen3-0.6B's stays at 0.036–0.042 whatever the share, carried by a few of its 12 questions (at 45%,
    0.14 and 0.07 for two of them, under 0.022 for seven), while the measured prompts fall to 0.018 at 45%. So
    the share kept errs on the safe side: at a target of 0.02 Llama 3.2 1B kept 45% and got its first token
    1.8× sooner, where 20% (2.7×) would have stayed within 0.02 on the measured prompts; the default is 0.03,
    where it keeps 15% (3.0×) and measures 0.016. Earlier, with plain-text prompts, four
    documents and one or three questions, the calibration was the gentler one (Llama 3.2 1B: 0.0097 at 5%
    against 0.027 at 0% and 0.020 at 10% measured), which is why it now uses the model's chat template, the
    corpus's numbered documents and a bound. It took 205 s of background work on Llama 3.2 1B and 90 s on
    Qwen3-0.6B (BF16 weights on the Mac's CPU), about as much as processing 15,000 tokens, once per model and
    cache format.
  * **Hybrid models are refused**, with the reason in `Engine::segment_reuse()`: their recurrent blocks must run
    over the whole prompt in order, so every token still goes through every block, and reusing the attention
    blocks' keys and values would skip only their key and value projections (1.3% of a prompt token's matrix work
    on Qwen3.5-0.8B). Marked prompts are then processed as usual. Windowed blocks (Gemma) take part like global
    ones, each turned with its own RoPE table, a recomputed token seeing its window: a reused segment needs every
    block's rows wherever it lies, so with `segment_reuse` on the windowed blocks keep every position (full
    attention's KV memory, a shorter automatic context) instead of only their window. With the engine's own
    sliding window there is no prefix cache, so no segment reuse.
  * **Off, nothing changes.** The forward pass, split into the steps this reuse runs block by block at scattered
    positions, gives the same bits (golden logits, arm64 and x86) at the same speed: alternating runs on the Mac
    before and after, a 520-token prompt and 96 tokens, prefill median 5.59 and 5.61 s, decoding 72.2 and 72.1
    tok/s on Qwen3-0.6B, 9.49 and 9.53 s, 42.0 and 43.7 tok/s on Llama 3.2 1B, the same replies.
* **Cancellable, resumable prefill.** `cancel_prefill()` stops a background prefill between blocks, within a fraction
  of a second even inside a 1,024-token pass, and keeps the work done. The next prompt continues from there. A user
  request therefore never waits behind background work.
* **Several sequences decoded together** (`max_sequences`, `Engine::open_sequence()`). The chat, a request from
  another app through the local API and a background agent no longer queue behind each other: each one runs on a
  sequence of its own, with its own context (KV pages as it uses them, recurrent states and snapshots, the text its
  tokens encode, its LoRA adapter), sharing the weights, the threads, the expert cache and the prefix cache. Calls on
  different sequences run at once, each on its caller's thread, and their forward passes run together: whichever
  waiting thread leads takes every sequence's next tokens into one pass
  (`Transformer::forward_batch()`), whose matmuls go over all of their rows, so each weight is read once for all
  of them (a mixture of experts reads the union of the experts they choose), while each sequence attends to its own
  cache at its own positions, continues its own DeltaNet states, applies its own adapter and, with latent attention,
  attends in the form its pass alone would take. The rest stays on each caller's thread: sampling, grammars,
  callbacks, stopping.
  * **Each sequence's output is its own.** A row's matmul gives the same bits whatever rows share its batch, and
    attention depends on a token's own position only, so on the CPU backend every sequence's logits are the bits
    it gets alone: greedy output is token for token, sampling draws the same tokens from the same seed. Tested on
    dense, gated, windowed (Gemma 2/3, Phi-3), hybrid, MoE (in place and streamed), latent (both forms, mixed in one
    pass) and LoRA models (`tests/test_sequences.cpp`). The GPU kernels compute each row on its own too: on Metal,
    replies together equal replies alone (`liyab-seq-bench --backend metal`). With the experimental lossy hooks on,
    sequences take turns instead of sharing passes, so that holds there too.
  * **Alone, nothing changes.** A call that runs while no other sequence has one runs exactly as a single
    conversation always has: the same passes, speculative drafts, pacing per token. Alternating runs on the Mac
    against the engine before sequences (CPU, 8 threads, 128 tokens, medians) decoded at 57.6 and 57.0 tok/s on
    Qwen3-0.6B BF16 (63.7 and 64.2 with drafts), 26.8 and 26.3 on Llama 3.2 1B, 48.3 and 48.1 on Qwen3.5-0.8B,
    238.6 and 235.5 on Qwen2.5-0.5B Q8_0 (11 runs each, prefill 180 ms both), the same replies. While several
    run, their steps are plain (one token each, no drafts): the shared pass is the batch drafts would otherwise
    fill. Passes of a prompt are cut to `max_batch` tokens while others decode, since a pass's time is what their
    next token waits for (latent attention keeps its own pass sizes: each pass's form follows from its size).
  * **What it gains.** `liyab-seq-bench` on the Mac (M4 Pro, 8 threads, 128 tokens per sequence, greedy, medians of
    3 paired runs): every token generated together over the wall time, against the same generations one after
    another. Every reply together was its reply alone.

    | Model | 2 sequences | 3 | 4 | Each of 2, alone |
    |---|---|---|---|---|
    | Qwen2.5-0.5B Q8_0, CPU | 1.37x | 1.75x | 2.28x | 144 tok/s, 287 |
    | Qwen2.5-0.5B Q8_0, Metal | 1.90x | | 3.26x | 44.3 tok/s, 46.5 |
    | Qwen3.5-0.8B BF16 (hybrid), CPU | 1.23x | 1.29x | 1.27x | 23.1 tok/s, 39.2 |
    | Qwen2.5-0.5B F16, CPU | 1.14x | 1.20x | 1.24x | 38.1 tok/s, 69.9 |
    | Qwen3-0.6B BF16, CPU | 1.10x | 1.21x | 1.29x | 30.3 tok/s, 55.3 |
    | Llama 3.2 1B BF16, CPU | 1.11x | 1.18x | 1.18x | 14.3 tok/s, 25.6 |
    | Qwen3-30B-A3B Q4_K_M, experts streamed (2 GiB cache), CPU | 0.96x | | 1.01x | 7.7 tok/s, 17.9 |

    Quantized weights gain most: their kernels decode a block of weights once for four rows. F16 and BF16 weights
    are dotted row by row, so a row more costs almost a row's time ([next](#roadmap)). On the GPU a pass's fixed
    cost dominates and is paid once for all. A MoE whose experts stream from storage reads the union of the
    experts its sequences choose, and with 8 of 128 per token they have few in common: a shared pass (64 tokens
    per sequence there) costs about as much as the passes it replaces, a draw. Each sequence decodes slower than alone, since a pass of more
    rows takes longer: the reason background steps join the user's passes only when that costs little. Drafts or a
    shared pass: with `lookup_drafts` on new text, the same generations in turns went no faster (Qwen2.5 Q8_0:
    222 tok/s with drafts, 223 without), and two sequences together gave 1.42x over the turns with drafts; drafts pay on repeated text
    (`liyab-spec-bench`), so a sequence alone keeps them, and sequences together share plain steps.
  * **The user first** (`SequencePriority`). Foreground sequences are the user's turn; background ones yield: their
    passes run when no foreground request waits, a pass of a background prompt is stopped between two blocks when
    foreground work arrives (its work kept, the pass run again later), and a background decoding step joins a
    foreground pass only while a pass of one more sequence measured at most 1.25 times as long: on a model in RAM
    a row more costs little, while a MoE whose experts stream from storage would make the user's step wait for the
    background step's expert reads. One step in 64 that would be kept out joins anyway, so the estimate follows
    the expert cache warming up and the device's load (at most 1/64 of the difference on the user's steps). A leader waits for the sequences about to submit (sampling, calling back) for
    at most half a pass, so a slow callback costs the others little.
  * **Per sequence.** Cancellation (`Sequence::cancel()`, `cancel_prefill()`), adapters (`set_adapter()`), the
    prefix cache's restores and set-asides (a context one sequence set aside, any other restores), and the Busy
    rule: one call at a time per sequence. `embed()`, `rerank()`, `save_state()`, `load_state()` and segment reuse
    stay on the default sequence; the others' passes wait while they run.
  * **Memory, only while a sequence is open.** `max_sequences` is a ceiling and reserves nothing: the model loads
    with the memory plan of a single conversation whatever it allows (the same expert cache, the same decision to
    requantize, the same bits out), so an engine with no sequence open is the engine of one sequence. Each
    sequence keeps its own KV pages as it uses them, up to `context_length()` positions. On hybrid models it also
    holds its recurrent states, rollback checkpoints and up to four snapshots (62.8 MiB of state each on the 35B,
    five of them): with streamed experts, `open_sequence()` takes that much out of the expert cache before
    allocating it (slots at the end of each size class, their experts evicted, their pages returned to the OS) and
    closing the sequence gives it back. Reserving it at load for every sequence allowed shrank the 35B's cache from
    2286 to about 1970 MiB with the app's API on, below the line where the resident Q8_0 matrices are requantized
    to 4 bits: other replies, 15.9 s to load instead of 3.7 s, an 11% higher peak, for a sequence that was never
    opened. A cache that cannot spare a sequence's memory without going below its minimum (a block's top-k and the
    reads in flight) refuses the open (`OutOfMemory`) instead of overcommitting; nothing is requantized after load.
    Not with a draft model, whose cache follows one sequence.
* **Automatic context length.** With `context_length = 0`, the context is what 256 MiB of KV holds: 4,096 to 32,768
  positions, at most the training context. That is ~24k on Qwen3.6-35B-A3B (only 10 of 40 blocks have a KV cache)
  and 4,096 on a dense 4B. Windowed blocks count for what they keep: their window plus the rollback margin is set
  aside once, and the rest of the budget goes to the blocks that keep every position, at their own cost per
  position ([Per-block KV](#per-block-kv)).
* **Save and restore.** `save_state()` / `load_state()` write the context to a file (KV pages, recurrent states, and
  the tokens and text they encode) and restore it in a later process. This works only for the same model file and
  cache layout, which a fingerprint checks. A long system prompt is processed once, not after every start. On hybrid
  models the file also keeps two state snapshots, the oldest and the last prompt's end (62.8 MiB each on the 35B), so
  a restored context rewinds where the live one would. The next prompt re-sends the last reply as text, which may
  encode differently from the tokens generated; without that snapshot the whole conversation was processed again
  (a 1,436-token chat: 60 s to the first token). The file also records the key scales its KV pages were stored with;
  a context saved with other scales, or before key scaling existed, has its keys converted when loaded, so an
  upgrade does not process saved conversations again. With windowed blocks (format version 4) the pages hold the
  blocks that keep every position, and the windowed blocks' rows of the window before the end (and before each
  kept snapshot) follow; the file records the per-block layout, and a file of another layout (another context
  length, `segment_reuse` changed) is refused with that reason. Files written before the per-block layout (every
  block's rows of every position in one table) load converted: the windowed blocks keep the window before the end.
* **Giving memory back.** `trim_memory()` empties the expert cache while idle, and drops constrained decoding's
  caches (rebuilt on the next constrained generation); the model and its context stay loaded. Its hot list survives: `warm_memory()` refills the cache in one background pass of large reads (~0.7 s for
  2.4 GB), and `save_expert_profile()` / `load_expert_profile()` carry the list to a later process.
* **Structured output.** `generate()` takes an optional `ForceCallback`. After each piece it sees the output so far
  and may return text the output must continue with. The engine runs that text through the model in one batched
  pass, like a short prefill, and emits it as output. That pass also gives the logits of the token after the forced
  text, which is sampled from them, so forced text costs no decoding step of its own (the CPU backend computes a row
  the same bits in any batch, so the output is the same as with a separate step). Constrained decoding (below)
  forces a grammar's fixed text through the same pass: the syntax and names of tool calls. It works with speculative
  decoding too: the callback is asked after every token, and tokens a step verified past a forced point are rolled
  back. Forced text that ends inside a character is emitted up to it, the rest with the token that completes it.
  Forced tokens are counted apart from sampled ones, with the time their passes took, and
  `GenerationStats::decode_passes` counts the model's passes while decoding. On the 35B with streamed experts, a tool call's 9 forced tokens took 1.52 s against ~1.66 s to
  sample them: a batched pass reads the union of its tokens' experts, so what forcing buys there is a call that
  always parses, not speed.
* **Constrained decoding.** `generate()` also takes `GenerateOptions`: a grammar the whole output must match, or a
  `ContinuationCallback` that forces text and opens constrained spans where it chooses (a tool call's arguments,
  between forced syntax). While a grammar is active, every token whose bytes it cannot accept is masked before
  sampling, so the output always matches. Grammars come from a JSON Schema (the subset tool parameters and response
  formats use: objects, required and optional properties, enums, `$ref`, integer and number ranges, string lengths
  and formats; see `include/liyab/grammar.h`), any JSON, or grammar text in a GBNF-like syntax with `%json`,
  `%schema`, `%string` and `%until`. A schema keyword Liyab cannot enforce (`pattern`, `uniqueItems`...) is refused
  with an error naming it and where it is, never ignored.
  * **How.** Liyab's own grammar engine lowers rules to a byte-level pushdown automaton: UTF-8 classes become byte
    sequences, so a token may end inside a character, and a matched text is always valid UTF-8. The set of parse
    stacks the output allows is interned as a state, and byte transitions between states are cached: inside a
    string a transition is one table lookup. The vocabulary is a trie in depth-first order; a state's mask is one
    pass over it that skips every subtree whose prefix the state rejects, and is cached per state. Greedy and top-k
    sampling skip the mask altogether: the likeliest tokens are checked one by one until the k best allowed ones
    are found, which leaves exactly what masking then keeping the top k would.
  * **Forced, not sampled.** Text every continuation shares (keys, separators, brackets, the rest of the only enum
    value that fits) is forced in one batched pass, as forced continuations are. JSON is laid out as `json.dumps`
    writes it (`", "` and `": "`) by default, so the model samples only values and choices; any white space is an
    option. End-of-generation tokens are allowed only where the grammar accepts, and a whole-output grammar ends the
    generation as soon as its match is complete.
  * **Token healing.** Forced text ends where the grammar offers a choice, and its last token can be the start of a
    longer token the model writes there: Qwen writes ` {"` after `"arguments":` and `</` before `function>`. Forced
    alone, ` {` or `<` makes the model go on from a token boundary it never saw in training, which skews its choice.
    Through the app's tool calls, Qwen3-0.6B then mostly wrote `{}` and left out its optional arguments (a date in
    10 of 50 replies, against 30 when it wrote that token itself), and Qwen3.5-0.8B added a parameter it did not
    need. So when a longer token the grammar allows starts with the forced text's last token, that token is left
    to the model, which samples it or the longer one under the mask; the batched pass only gets shorter, so it
    costs no step. With it, Qwen3-0.6B gave a date in 30 of 50 replies again, and Qwen3.5-0.8B's greedy calls are
    the ones it writes when only their syntax and names are forced.
  * **Cost.** On an M4 Pro (Qwen3-0.6B, Qwen3.5-0.8B, Llama 3.2 1B, Qwen2.5-0.5B), constrained decoding cost
    0.14–0.24 ms per token greedy, 0.25–0.62 ms with top-k sampling, and 0.09–0.12 ms with whole masks once a
    state's mask is cached, against decode steps of 18–92 ms. A state's first whole mask takes 1.5–2.7 ms (inside a
    string, where nearly every token is allowed). The vocabulary trie is built on the first constrained token:
    333,000 nodes in ~30 ms for Qwen3's 151,000 tokens, 592,000 nodes in ~45 ms for Qwen3.5's 248,000. The engine
    keeps the states and masks of the 16 grammars used last (32 MiB per grammar, 64 MiB together), so a request with
    the same tools does not pay for them again. `GenerationStats::constrained_tokens` and `grammar_ms` report the
    cost of each generation, and `test_grammar` measures it on any GGUF (`LIYAB_GRAMMAR_MODEL`), together with a
    tool call made the way the local API makes one: Qwen3-0.6B (JSON calls) and Qwen3.5-0.8B (XML calls) wrote
    valid calls in every run.
  * **Speculative decoding** is off while a grammar is active (drafts would need a mask at every verified position);
    the unconstrained parts of the same generation use it.

---

## Heat and power

A phone that gets hot slows down by itself, and gets slower still once the OS steps in. Liyab steers before that
happens.

* **Forecast, not reaction.** While the engine processes a prompt or generates, a polling thread reads the
  following once a second:
  * the OS thermal status (Android `AThermal_*`, Apple `NSProcessInfo.thermalState`);
  * Android's thermal-headroom forecast 10 s ahead (Android 12+, smoothed);
  * the sysfs skin and SoC zones.

  Idle, it reads nothing. One reading costs ~10 ms of CPU and ~25 wakeups on a Snapdragon 8 Elite, which a loaded
  but unused model would otherwise pay every second (about 1% of a core, the screen off included).

  The forecast becomes a pressure from 0 to 1 over a band set by the power profile: Performance 0.75–0.95, Balanced
  0.65–0.90, LowPower 0.35–0.60. A cooler profile reacts earlier.
* **Same tokens, fewer watts.** From a pressure of 0.1, the engine sheds cores (down to half). It also paces tokens
  at up to twice their full-speed work time, learned while running unslowed. On Android 13+ the decode threads report
  each token's work time to a performance-hint session (ADPF) with the token period as target, so the governor runs
  just fast enough instead of sprinting and sleeping. Unpaced decoding opens no session. Below 0.1 nothing is paced:
  a hint asking for the current pace had been holding the clocks there.
* **Guards for emergencies only.** These trigger a throttle (GPU work rerouted, half the threads, half the rate):
  * pressure 1;
  * the profile's OS-status limit;
  * the skin threshold. With a forecast this applies only 8 °C above the threshold, because on many phones the
    "skin" sensor is a board thermistor that reads 45–50 °C under load;
  * a smoothed SoC reading past 95 °C. Single samples spike by 25–30 °C, and 85–90 °C is normal under load.
* **Duty cycling.** Profiles can cap output at a reading-speed rate (Balanced 12 tok/s, LowPower 6 tok/s; `--tps` to
  override), so the SoC idles between tokens.
* **Live counters.** `Engine::counters()` reports GPU busy time, bytes streamed and tokens generated, and is safe to
  call while a generation runs. The app's Activity page adds battery watts and J/token on battery.

---

## Speculative decoding

A small draft model proposes *k* tokens, or, with `lookup_drafts`, the text itself does, with no extra weights and
for any model. Two drafters:

* **Suffix drafts** (the default, `suffix_drafts`): the longest suffix of the conversation (2…32 tokens) that
  occurred before, in this conversation or in earlier ones of the same engine, and how its occurrences continue:
  their continuation tree, which branches where the occurrences part.
  Earlier conversations are kept with a suffix array each, so finding a match is a binary search. They are set
  aside when a prompt stops continuing them (a new conversation, a regenerated reply) and are bounded: 262,144
  tokens (~2 MiB) in at most 64 of them, least recently used out first. A conversation taken up again replaces its
  stored copy, so no text is counted twice. Each drafted token carries an acceptance probability, calibrated on
  the device from what verification accepted, by match length, by how many occurrences agree and by whether the
  conversation itself supports it; a token's probability is the product along its branch. A step verifies the
  tree's likeliest nodes, as many as give the most expected tokens per millisecond at the measured cost of a step
  per draft count. A confident draft is verified at full length (`draft_tokens` at most) and a doubtful one not at
  all.
* **Context lookup** (`suffix_drafts = false`): the tokens that followed the most recent earlier occurrence of the
  last 4…2 tokens of the conversation.

The target verifies the drafts in one batched pass, reading its weights once for *k* + 1 tokens.

**Tree verification** (suffix drafts, `draft_tree`, on by default). Where earlier occurrences of the matched text
continue differently (a list whose items differ, a JSON field whose values do), the drafter offers both
continuations, and one pass verifies them together:

* **Which drafts.** The *k* likeliest nodes of the continuation tree, taken best first: a node's children become
  candidates once it is taken, so any first *j* of them form a tree. Siblings are exclusive (the target picks one
  token), so their probabilities are scaled to sum to at most 1. The expected tokens of a step are 1 + the sum of
  the nodes' probabilities; the draft budget weighs them against the measured cost of a pass of *k* + 1 tokens,
  which is the same whether they form a branch or a tree (on a MoE that streams its experts, the union of the
  tokens' experts either way).
* **One pass.** The batch is the last token, then the drafts depth first with the likeliest child first, so the
  likeliest branch is the batch's first tokens. Every token is computed at its branch's position (the context's
  length plus its depth), attending to the context and its own ancestors only, through the same visible positions
  and spans as a linear pass over its branch. So its row of logits has that pass's bits. Each token's keys and
  values go to a slot of their own. Windowed blocks see their window over the branch; latent attention runs in the
  absorbed form, as decoding does; an active LoRA adapter applies as in any pass.
* **Hybrid models branch their recurrent state.** A token whose parent is not the token before it continues from
  the state after its parent, which the pass keeps for every token (in the rollback checkpoints, *k* + 1 of them
  as before). Every token's state is copied once, as a linear pass of *k* + 1 tokens copies it.
* **Kept branch.** From the last token down, each row is sampled once, as plain decoding samples it, and the child
  holding the sampled token is kept. The kept branch's rows move to their positions (none when it is the likeliest
  branch), its recurrent states become the rollback checkpoints, and the rest of the tree is dropped: the context
  is exactly the one a linear pass over that branch leaves. A tree that is a single branch runs as a linear pass.
  `draft_tree = false` verifies only the best branch.

* **Exact.** Acceptance follows Leviathan et al. (2023), so the output keeps the target's distribution. With greedy
  sampling it is token-for-token identical to plain decoding (tested). Suffix drafts are kept while they equal the
  token plain decoding samples from the same row, on a branch or in a tree. With temperature, their output is
  therefore plain decoding's own tokens for a seed, whatever was drafted (tested on the CPU backend). The one
  exception is the tokens after a forced continuation cut a step short.
* **Hybrid models included.** Both models keep copies of their recurrent states for the last *k* + 1 tokens, so
  rejected tokens roll back exactly.
* **Self-tuning.** How many drafts to verify is learned on the device. With a draft model or context lookup, it is
  the draft count with the most tokens per millisecond, and losing counts are retried after a doubling wait. With
  suffix drafts, it is chosen for each draft from its acceptance probabilities and each count's step time (the
  median of its last 8 steps). Counts are tried upwards, one more draft at a time.
* **When it pays.** It pays on dense models with i8mm tiles, where 4 rows cost ~1.7× one row. Qwen3-4B on the
  phone went from 11.2 to 12.6 tok/s on a code edit, with 65% of drafts accepted. It does not pay on a MoE whose
  experts stream from flash, because a pass reads the union of its tokens' experts. That is why it is off by
  default.

### Host measurements: suffix drafts and context lookup

Measured with `liyab-spec-bench` on an Apple M4 Pro with the CPU backend, 6 threads, greedy decoding and replies of up to
256 tokens. The default of 3 drafts per step was used, and the draft count was learned. Each cell gives the decode
speed-up over plain decoding (median of 2 runs) and, in parentheses, the tokens produced per verification pass. The
tasks are a code edit (a 50-line module rewritten with one rename), a summary of a pasted text, two turns that each
carry the same tool output (the second asks for it in full), free chat, and that tool conversation again as a new
conversation. Every reply was identical to plain decoding's.

| Model | Drafter | Code edit | Summary | Tool output | Free chat | Tool chat again |
|---|---|---|---|---|---|---|
| Qwen2.5-0.5B Q8_0 | lookup | 2.60× (3.44) | 1.42× (1.51) | 1.71× (1.92) | 1.06× (1.09) | 1.69× (1.81) |
| | suffix | 2.96× (3.61) | 1.40× (1.56) | 1.63× (1.94) | 1.15× (1.05) | 2.59× (3.83) |
| Qwen3-0.6B BF16 | lookup | 1.25× (2.69) | 0.98× (1.04) | 0.98× (1.06) | 1.04× (1.01) | 0.98× (1.06) |
| | suffix | 1.28× (3.26) | 0.99× (1.16) | 1.00× (1.24) | 1.01× (1.00) | 1.33× (3.62) |
| Qwen3.5-0.8B BF16 (hybrid) | lookup | 1.18× (2.28) | 0.93× (1.02) | 0.99× (1.02) | 0.96× (1.00) | 0.95× (1.01) |
| | suffix | 1.18× (2.19) | 0.97× (1.13) | 0.98× (1.18) | 0.97× (1.01) | 1.30× (3.91) |
| Llama-3.2-1B BF16 (best run) | lookup | 0.94× (2.33) | 0.89× (1.03) | 1.10× (0.99) | 0.96× (1.00) | 1.13× (1.02) |
| | suffix | 0.98× (2.60) | 0.93× (1.04) | 0.93× (1.00) | 1.00× (1.01) | 1.36× (3.01) |

* **Acceptance.** Of the drafts verified, suffix drafts had 92–98% accepted on the code edit, 42–62% on the summary,
  26–77% on the tool output, 0–35% in free chat and 100% on the conversation seen before. Lookup had 86–97%,
  24–55%, 0–64%, 0–29% and 29–60%.
* **The same drafts where the text occurs once.** With every draft verified (`suffix:K:fixed`), both drafters
  give nearly the same tokens per pass on the code edit and the summary (3.71 for 3 drafts, 7.11 for 8 on Qwen2.5).
  On the repeated conversation, suffix drafts give 3.90–3.96 tokens per pass for 3 drafts and 8.53–8.67 for 8.
  Lookup gives 1.15–2.01 and 1.16–2.42, because it sees only the conversation in progress.
* **Doubtful drafts are not verified.** Suffix drafts size each draft from its acceptance probabilities, so they
  stay within 7% of plain decoding where drafting cannot pay. With 8 drafts per step, lookup lost up to 20% on
  the same tasks (Llama summary 0.80×, Qwen3 summary 0.84×), and suffix drafts lost at most 5%.
  Suffix drafts reached 1.24–2.85× on the repeated conversation, with 6.1–7.8 tokens per pass.
* **Why the BF16 models gain less.** On this CPU a pass over 4 tokens costs about 3× one token on the BF16
  models, against ~1.5× on Q8_0 (from the tokens per pass and speed-ups above). Only near-certain drafts pay there.
* The Llama runs shared the host with other heavy work. Their speed-ups are the least disturbed run's; tokens per
  pass and acceptance do not depend on timing.

### Host measurements: tree verification against the best branch

The same tasks and host (CPU backend, 6 threads, greedy, replies of up to 256 tokens), each suffix-draft mode with
its tree (`suffix`, the default) and with its best branch only (`suffix:linear`). Every reply of every mode was
identical to plain decoding's, the hybrid model's included. Tokens per verification pass with every draft verified
(`suffix:8:fixed` against `suffix:8:fixed:linear`; these do not depend on timing):

| Model | Code edit | Summary | Tool output | Free chat | Tool chat again |
|---|---|---|---|---|---|
| Qwen2.5-0.5B Q8_0 | 7.11 / 7.11 | 1.82 / 1.82 | 2.53 / 2.50 | 1.12 / 1.11 | 8.53 / 8.53 |
| Qwen3-0.6B BF16 | 6.74 / 6.74 | 1.36 / 1.37 | 1.77 / 1.77 | 1.02 / 1.02 | 8.67 / 8.67 |
| Qwen3.5-0.8B BF16 (hybrid) | 4.20 / 4.20 | 1.34 / 1.34 | 1.46 / 1.45 | 1.02 / 1.02 | 8.56 / 8.56 |
| Llama-3.2-1B BF16 | 7.11 / 7.11 | 1.19 / 1.18 | 1.21 / 1.20 | 1.03 / 1.03 | 8.42 / 8.42 |

(tree / best branch.) With the learned draft count on Qwen2.5-0.5B Q8_0 (median of 3 runs), the tree and the best
branch gave 3.52 / 3.57, 1.55 / 1.53, 1.64 / 1.75, 1.03 / 1.03 and 3.89 / 3.85 tokens per pass for 3 drafts per
step, and speed-ups over plain decoding of 2.02× / 2.10×, 1.17× / 1.11×, 1.49× / 1.37×, 1.00× / 1.02× and
2.28× / 2.06×: equal within the run-to-run spread of this shared host.

* **On these tasks a tree verifies what the best branch does.** Where a draft is rejected, the target almost always
  writes a token that no earlier occurrence of the matched text continued with, so no sibling could have been
  right; where the occurrences part, the likeliest one is mostly the right one. A tree gains where earlier text
  continues the same words several ways and the target takes a less frequent one: the tests build such text and
  check that the sibling is kept.
* **It costs what the branch costs.** A tree pas