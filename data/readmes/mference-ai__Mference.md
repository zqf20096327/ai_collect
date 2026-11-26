<p align="center">
  <img src="docs/assets/mference-app-icon.png" alt="Mference app icon" width="160">
</p>

<h1 align="center">Mference 2.0</h1>

<p align="center">
  <strong>Qwen 3.6 35B-A3B on Apple Silicon — with Native Ephemeral Vision &amp; Visual PDFs, Metal 4 Acceleration, Native MTP + Hybrid PLD Speculation (v5), Lossless Weight Surgery &amp; DeepSeek Harness Integration</strong><br>
  A native Swift + Metal runtime for Qwen 3.6 35B-A3B that streams routed experts from SSD in bounded memory.<br>
  <em>Forked from <a href="https://github.com/NeelM0906/Mference">NeelM0906/Mference</a>, derived from <a href="https://github.com/drumih/turbo-fieldfare">TurboFieldfare</a>.</em>
</p>

<p align="center">
  <img alt="Swift 6.1 or later" src="https://img.shields.io/badge/Swift-6.1%2B-F05138?logo=swift&logoColor=white">
  <img alt="Metal 3 or later" src="https://img.shields.io/badge/Metal-3%2B-5E5CE6">
  <img alt="macOS 15 or later" src="https://img.shields.io/badge/macOS-15%2B-000000?logo=apple&logoColor=white">
  <a href="https://github.com/mference-ai/Mference/releases/tag/v2.1.0"><img alt="Release v2.1.0" src="https://img.shields.io/badge/Release-v2.1.0-3fb950?logo=github"></a>
  <a href="https://huggingface.co/voodmany/Qwen3.6-35B-A3B-4bit-MTP-Surgery-GTurbo"><img alt="Hugging Face Model Card" src="https://img.shields.io/badge/Hugging%20Face-Model%20Card-FFD21E?logo=huggingface&logoColor=000"></a>
  <a href="https://github.com/mference-ai/Mference/discussions"><img alt="GitHub Discussions" src="https://img.shields.io/badge/Discussions-Community-8957e5?logo=github"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/License-MIT-2ea44f"></a>
</p>

<p align="center">
  <a href="#architecture">Architecture</a> ·
  <a href="#try-it">Quick start</a> ·
  <a href="MTP_WEIGHT_SURGERY_AND_ARCHITECTURE.md"><strong>Deep-Dive Spec &amp; Surgery Docs</strong></a> ·
  <a href="integrations/deepseek-harness/README.md"><strong>DeepSeek Harness Profile</strong></a> ·
  <a href="docs/OPENAI_SERVER.md">Local server</a> ·
  <a href="docs/OPEN_WEBUI.md">The UI</a> ·
  <a href="#acknowledgments">Acknowledgments</a>
</p>

> **Full Technical Reference:** See **[`MTP_WEIGHT_SURGERY_AND_ARCHITECTURE.md`](MTP_WEIGHT_SURGERY_AND_ARCHITECTURE.md)** for tensor-level specifications, surgery math, and implementation details, plus **[`integrations/deepseek-harness/README.md`](integrations/deepseek-harness/README.md)** for the DeepSeek Harness desktop profile.

---

## At a Glance — 35B MoE on a 16 GB Mac

<p align="center">
  <img src="docs/assets/mference-live-demo.svg" alt="Animated Mference 2.0 Qwen 3.6 35B-A3B live coding stream, 16 GB unified memory, and MTP+PLD demo" width="900">
</p>

<p align="center">
  <img src="docs/assets/mference-v2-benchmark.svg" alt="Qwen 3.6 35B-A3B benchmark comparison on a 16 GB Mac" width="900">
</p>

Measured on a **16 GB unified-memory Mac** (`32` expert cache slots, `temperature = 0`, `max_new_tokens = 512`) across the 8-task Artificial Analysis methodology suite ([`benchmarks/aa-scorecard-v2.json`](benchmarks/aa-scorecard-v2.json)):

| Metric | Raw INT4 Baseline | Mference 2.0 (Surgery + Adaptive MTP) | Impact |
| :--- | ---: | ---: | :--- |
| **Pass@1 Accuracy** | `25.0%` (`2/8`) | **`100.0%` (`8/8`)** | **`+75.0 pts`** — eliminates `<think>` loops |
| **Decode Speed** | `15.96 tok/s` | **`16.47 tok/s` avg** | Up to **`18.36 tok/s`** (Swift) / **`17.88 tok/s`** (AIME) |
| **MTP Acceptance** | `79.1%` static `K=2` | **`83.1%` adaptive hybrid** | **`2.55`** tokens/round (up to **`94.3%`** on AIME) |
| **Avg Time per Task** | `32.14s` | **`25.31s`** | **`-21.3%`** (`13.11s` avg TTFAT) |
| **Thinking Waste** | `413.4` avg tokens | **`126.1` avg tokens** | **`-69.5%`** wasted reasoning tokens |

```bash
git clone https://github.com/mference-ai/Mference.git && cd Mference-2.0
./mference-ui.sh install qwen36-mtp   # Qwen 3.6 35B-A3B + 19-tensor MTP shard + lossless surgery
./mference-ui.sh                      # MferenceServer (:8080) + Open WebUI (:3000)
```
*(Or package the native macOS desktop app at `~/Applications/Mference.app` via `./Scripts/build-app.sh` — see [Try it](#try-it) for full CLI and DeepSeek Harness setup.)*

### Why It Works
1. **Lossless INT4 Resident Weight Surgery:** Scales `BF16` affine `scale`/`bias` tables ($\alpha w = (\alpha s)q + (\alpha b)$) and `BF16` norms directly inside `model_weights.bin` with automatic MTP co-adaptation and manifest provenance checks — fixing quantized reasoning collapse with **zero nibble re-quantization**.
2. **Native 19-Tensor MoE MTP + 6-Gram Hybrid PLD:** Combines an async-pipelined `commitAcceptPass`, a 4-slot Gated-DeltaNet rollback arena (plus SSD-spilled GDN checkpoint ring), lossless `topK = 6` draft expert pruning, exact within-block top-2 EVICT margin truncation, lossless sampled speculative decoding (`top-k` 1...64 via 64-TG GPU softmax), and single-pass 6/5/4/3-gram prompt lookup for tool/code spans.
3. **Bounded-Memory NVMe Expert Streaming (`16 GB` Safe):** Streams `256` routed experts per layer on demand via `PreadExpertStreamer` with Phase-1/Phase-2 hit/miss verify pipelining, I/O-first ordering, prefill-tail warm start, `POSIX_MADV_RANDOM` slab-only MTP mapping, and a 2-slot LRU `ServerPromptCache` (`PrefixSnapshot`).
4. **Native Ephemeral Vision &amp; Visual PDFs (`vision_weights.bin` + Metal 4):** `MferenceRepack --attach-vision` streams all `333` BF16 `vision_tower.*` tensors via HTTP Range requests into an ephemeral sidecar without altering `model_weights.bin` or MTP/surgery state. `Qwen36VisionEncoder` runs the 27-layer ViT + `2×2` spatial merger on lazy-loaded Metal 4 `matmul2d` kernels (`vision.metal`) with automatic Accelerate AMX (`cblas_sgemm`) fallback, caches compact `[N_vis, 2048]` FP16 embeddings, and immediately `munmap`s `vision_weights.bin` before the 40-layer MoE trunk prefill — zero startup cost and zero idle RAM overhead for text sessions. Works with images and multi-page PDFs across `Mference.app`, OpenAI `/v1/chat/completions` (`image_url` / `file`), and `MferenceCLI` (`--image` / `--pdf`).

---

## Architecture

**Mference 2.0** is built around **[Qwen 3.6 35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** (`40` layers in a 3:1 hybrid Gated-DeltaNet linear-attention + full-attention layout, `256` routed experts per layer with `top-8` routing + scalar-gated shared expert, and a `19`-tensor MTP speculative draft sidecar). Rather than loading all 35B parameters into RAM, it keeps resident core weights, linear GDN state, and KV cache in unified memory while streaming routed experts on demand from NVMe SSD.

### End-to-End Runtime Stack

```mermaid
flowchart LR
    subgraph Frontends["Front-Ends & Clients"]
        App["Mference.app (MferenceMac -> MferenceDecodeService IPC)"]
        Server["MferenceServer (SwiftNIO OpenAI HTTP/SSE :8080)"]
        WebUI["mference-ui.sh / Open WebUI (:3000)"]
        CLI["MferenceCLI"]
        DSH["DeepSeek Harness (cordis.patch.yml)"]
        WebUI --> Server
        DSH --> Server
        App -. "Start OpenAI Server" .-> Server
    end

    subgraph Orchestration["Alignment, Tokenization & Prompt Cache"]
        Aligner["ServerIntentAligner (.zeroThinkFastPath, memory K cap)"]
        Tokenizer["MFTokenizer (ChatML / Jinja, QwenToolCallParser)"]
        Cache["ServerPromptCache (2-slot LRU) + PrefixSnapshot"]
        Loop["RawCompletion + Sampler + RepetitionLoopDetector"]
    end

    subgraph Execution["Forward Runner, Vision & v5 Speculation"]
        Runner["RealForwardRunner (40-layer GDN + Full Attn, 4-slot GDN arena)"]
        Vision["Qwen36VisionEncoder (Ephemeral 27-layer ViT + 2x2 Merger + mRoPE)"]
        Spec["Qwen36MTPSpeculator (MTP + Hybrid PLD + Adaptive K + EVICT)"]
        KV["KVCacheManager + GDNStateManager"]
        Vision --> Runner
        Runner <--> Spec
        Runner --> KV
    end

    subgraph GPU_Storage["Metal 3/4 Kernels & .gturbo Storage"]
        Metal["Metal Kernels (MoE topK 4/6/8 & Slot-Map, Attention, GDN, Prefill TensorOps2D, Vision matmul2d, LMHeadChainInt4)"]
        Resident["mmap model_weights.bin + ephemeral vision_weights.bin"]
        Stream["PreadExpertStreamer (hit/miss slot cache) + ResidentExpertStreamer (MTP slab)"]
    end

    Frontends --> Orchestration --> Execution --> GPU_Storage
```

### SwiftPM Modules & Targets

Defined in [`Package.swift`](Package.swift):

- **`Mference`** — Core runtime library: Metal compute shaders (`MoE`, `Attention`, `GDN`, `Prefill`, `Vision`, `Fusions`, `Sampling`), `RealForwardRunner`, `Qwen36VisionEncoder`, `Qwen36VisionImageStore`, `Qwen36MTPSpeculator`, `KVCacheManager`, `GDNStateManager`, `PreadExpertStreamer`, `ResidentExpertStreamer`, `MFTokenizer`, `StructuredAssistantDecoder`, and `QwenToolCallParser`.
- **`MferenceRepackCore` / `MferenceRepack`** — Streaming Hugging Face installer and `.gturbo` packager (`MTPAttachTool` for attaching the 19-tensor MTP shard + lossless resident weight surgery, and `VisionAttachTool` for attaching Qwen 3.6's `vision_weights.bin` sidecar).
- **`MferenceServerCore` / `MferenceServer`** — SwiftNIO OpenAI-compatible HTTP/SSE server (`HTTPServer`, `ServerIntentAligner`, 2-slot LRU `ServerPromptCache`, multimodal `image_url`/`file` parts, `ServerModelDiscovery`).
- **`MferenceCLICore` / `MferenceCLI`** — Terminal chat and raw-completion executable.
- **`MferenceAppCore` / `MferenceDecodeProtocol` / `MferenceDecodeService` / `MferenceMacPresentation` / `MferenceMac`** — Native SwiftUI macOS app isolating model execution inside `MferenceDecodeService` over length-framed IPC (`OpenAIServerManager` also manages the local server process).
- **`Scripts/install-qwen36-mtp.sh` / `Scripts/build-app.sh`** — One-command Qwen 3.6 + MTP + weight surgery installer and signed `~/Applications/Mference.app` desktop bundle packager.
- **`integrations/deepseek-harness/`** — DeepSeek Harness profile patch (`cordis.patch.yml`) configuring the `mference` provider (`timeoutMs: 600000`, `streamIdleTimeoutMs: 600000`, `defaultContextWindow: 32768`, `defaultMaxTokens: 16384`), bounded tool output/pruning (`spill-policy`, `tool-fs`, `tool-result-pruner`), and fast macOS `persona` rules.

### Core Mechanisms

1. **On-Disk `.gturbo` Layout & Bounded-Memory Streaming**
   ```text
   scratch/qwen36-mtp.gturbo/
     manifest.json                 # ArchConfig, sidecars.mtp, sidecars.vision, SHA-256 map
     verified-install.json         # Install integrity receipt
     model_weights.bin             # 16 KiB-aligned index + mmap resident weights & 17 mtp.* tensors
     vision_weights.bin            # Optional ephemeral BF16 sidecar (333 vision_tower.* tensors)
     packed_experts/               # Trunk routed experts (256 experts/layer, page-aligned)
       layout.json & layer_XX.bin  # Streamed on demand via pread into LFU/LRU slot cache
     packed_experts_mtp/           # MTP auxiliary routed expert pool
       layer_00.bin                # 256 page-aligned INT4 experts (~453 MB, .mapped slab)
     tokenizer/                    # config.json, tokenizer.json, chat_template.jinja
   ```
   - `PreadExpertStreamer` keeps a fixed per-layer wired slot budget (`16` memory-first, `32–48` on 16 GiB hosts, `96` on 24 GiB+ hosts), fetches only the `top-8` active experts per token with zero-syscall `F_NOCACHE` tracking, and splits verify batches into Phase-1 resident hits + I/O-first Phase-2 misses.
   - Prefill-tail expert warm start (`v5`) and hybrid MPP grouped MoE prefill minimize SSD stalls across large prompts and decode step 1.

2. **Native MTP + Hybrid PLD Speculation (`v5`)**
   - **Async-Pipelined Seed & Verify/Rollback:** `RealForwardRunner` batches `[bonus] + drafts[0..<K]` through zero-spill templated batched slot-map MoE verify kernels (`moe.metal`), fused multi-token GDN verify + tail updates (`gdn.metal`), and `LMHeadGreedyMultiX`. It rewinds `KVCacheManager`, restores linear-attention state from a **4-slot GDN rollback arena** (plus an SSD-spilled GDN checkpoint ring in `GDNStateManager`), and overlaps `commitAcceptPass` asynchronously with CPU detokenization and SSE streaming.
   - **Zero-Blit MTP Execution:** Draft and accept passes write `k_proj`/`v_proj` directly into `mtpK`/`mtpV`, batch accept-pass per-head norms + NeoX RoPE via `PrefillQKVEpilogue`, deduplicate final `RMSNorm` into `mtp.lastHiddenBuf`, and use `POSIX_MADV_RANDOM` slab-only mapping for `packed_experts_mtp/layer_00.bin`.
   - **Phase-Aware Adaptive `K`:** `Qwen36MTPSpeculator` tracks `<think>`, visible prose, and `<tool_call>`/code-fence token transitions via `notifyTokens` with per-position acceptance EMAs, calibrating adaptive depth throttling for SSD-streaming caches and capping `K` under 16 GiB RAM/context pressure.
   - **Lossless Draft Expert Pruning (`moe.metal`):** Draft steps use `router_topk_select_k4_par` / `k6_par` (`draftTopK = 6` by default) while trunk verification always evaluates full `topK = 8`.
   - **Exact Within-Block EVICT Truncation & Sampled MTP (`logit.metal`):** `lm_head_greedy_int4_rows_chunk_raw` tracks within-8-row runner-up logits (`kLMHeadSingleRowSummaryStride = 3`) so `lastTop1Margin = top1 - top2` is exact across the vocabulary, while 64-TG GPU softmax (`LogitSoftcapSoftmax`) enables lossless sampled speculative decoding (`temperature > 0`, `top-k` `1...64`).
   - **Hybrid PLD + MTP (`v5`):** Runs a zero-allocation single-pass backward scan checking 6/5/4/3-grams over `tokenHistory` during `<tool_call>` and fenced code spans (disambiguating repeated 4-grams with 5/6-gram context) to populate `draft[1..]` without extra sequential MTP neural passes.
   - **Dynamic Greedy / Sampled Mode Switching:** Dynamically switches between fused greedy MTP and full sampled MTP verification without reloading weights.

3. **Lossless Resident Weight Surgery (`MTPAttachTool`)**
   - Group-64 affine quantized weights satisfy $w = s \cdot q + b$, so scaling by $\alpha$ transforms linearly into $(\alpha \cdot s) \cdot q + (\alpha \cdot b)$ on `BF16` scale/bias tables and `BF16` norm vectors staged atomically via a `.surgery.tmp` clone before swapping over `model_weights.bin` — **never unpacking or re-quantizing `INT4`/`INT8` nibbles**.
   - Supports optional late Gated-DeltaNet residual calibration (`--surgery-late-linear-residual`), finite/positive parameter validation, automatically co-adapts `mtp.norm.weight`, `mtp.layers.0.self_attn.{q_norm,k_norm,o_proj}`, `mtp.layers.0.mlp.gate`, and `mtp.layers.0.mlp.shared_expert.down_proj` (`coAdaptMTP`), records provenance under `manifest.json["surgery"]` to prevent accidental double-application, refreshes SHA-256 digests, and regenerates `verified-install.json`.

4. **Multi-Slot LRU Prompt Cache & Agentic Guards (`v5`)**
   - `ServerPromptCache` manages up to `2` LRU prefix slots (shrinking automatically to `1` under memory pressure), saving and restoring linear KV cache, GDN recurrent states, and MTP `tokenHistory` via `PrefixSnapshot` when switching between interleaved conversations.
   - `ServerIntentAligner`, `RawCompletion`, `RepetitionLoopDetector`, `StructuredAssistantDecoder`, and `QwenToolCallParser` handle `.zeroThinkFastPath` injection, clause-aware soft-landing `</think>`, repetition cycle breaking, and quantized tool-call JSON repair.

5. **Native Ephemeral Vision & Visual PDF Pipeline (`VisionAttachTool` + `vision.metal`)**
   - **Zero-Idle-Overhead Sidecar:** `MferenceRepack --attach-vision --output <model.gturbo>` fetches the `333` BF16 `vision_tower.*` tensors via coalesced HTTP Range requests into `vision_weights.bin`, updates `manifest.json` (`sidecars.vision`) and `verified-install.json`, and keeps pure-text sessions completely untouched.
   - **Ephemeral Metal 4 + AMX ViT Encoder:** `Qwen36VisionEncoder` maps `vision_weights.bin` read-only with `F_NOCACHE` and double-buffered contiguous `pread` staging only when uncached visual inputs appear, executes the 27-layer ViT + `2×2` spatial merger on Metal 4 `matmul2d` Neural Accelerator kernels (`mpp_vision_bf16_gemm_f32`, `vision_layernorm_f32`, `vision_rope_2d_f32`, `vision_attention_f32`) with automatic Accelerate AMX (`cblas_sgemm`) fallback, caches compact `[N_vis, 2048]` FP16 embeddings, and `munmap`s `vision_weights.bin` immediately before trunk prefill + 3D mRoPE indexing.
   - **Images & Multi-Page PDFs Everywhere:** `Qwen36VisionImageStore` applies Qwen3-VL `smart_resize` (`factor = 32`, `defaultMaxPixels = 384×384`), renders multi-page PDFs (`defaultMaxPDFPages = 8`, up to `64`), and shares a bounded `.vpatch` disk cache across `Mference.app` (`PromptComposerView`), OpenAI `/v1/chat/completions` (`image_url`, `input_image`, `file`), and `MferenceCLI` (`--image` / `--pdf`).

---

## Try it

Prebuilt binaries for Apple Silicon Macs (`arm64`, macOS 15+, Metal 3/4) are available on the **[v2.1.0 Releases page](https://github.com/mference-ai/Mference/releases/tag/v2.1.0)** (`Mference.app` + CLI/Server/Repack binaries), or you can build from source with Swift 6.1+. Install [`uv`](https://github.com/astral-sh/uv) (`brew install uv`) only if you want the Open WebUI browser UI; CLI, `Mference.app`, `MferenceServer`, and DeepSeek Harness need no Python.

```bash
git clone https://github.com/mference-ai/Mference.git
cd Mference-2.0
./mference-ui.sh doctor               # check prerequisites without downloading or changing settings
swift build -c release

# Install Qwen 3.6 35B-A3B + guru87 MTP shard + lossless weight surgery
./mference-ui.sh install qwen36-mtp   # (or: ./Scripts/install-qwen36-mtp.sh)

# Launch MferenceServer + Open WebUI at http://127.0.0.1:3000
./mference-ui.sh

# Optional: package the native macOS desktop app at ~/Applications/Mference.app
./Scripts/build-app.sh
```

> **Important:** `./mference-ui.sh install qwen36` installs only the unmodified base [`mlx-community/Qwen3.6-35B-A3B-4bit`](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-4bit) checkpoint without MTP or weight surgery. Use **`./mference-ui.sh install qwen36-mtp`** (or [`Scripts/install-qwen36-mtp.sh`](Scripts/install-qwen36-mtp.sh)) to get the complete Mference 2.0 setup (resumable with `--resume`).

### DeepSeek Harness Setup

```bash
mkdir -p ~/.dsh/profiles/desktop
cp integrations/deepseek-harness/cordis.patch.yml ~/.dsh/profiles/desktop/cordis.patch.yml
```

See [`integrations/deepseek-harness/README.md`](integrations/deepseek-harness/README.md) for profile options.

### Command-Line Usage (without UI)

```bash
# Interactive chat
swift run -c release MferenceCLI --model scratch/qwen36-mtp.gturbo --chat

# Optional: attach Qwen 3.6 native vision + visual PDF sidecar (333 BF16 tensors)
.build/release/MferenceRepack --attach-vision --output scratch/qwen36-mtp.gturbo

# Single-turn image or PDF query via CLI (--image / --pdf are repeatable)
swift run -c release MferenceCLI --model scratch/qwen36-mtp.gturbo --image screenshot.png --prompt "Describe this UI"
swift run -c release MferenceCLI --model scratch/qwen36-mtp.gturbo --pdf paper.pdf --prompt "Summarize the figures"

# OpenAI-compatible server (http://127.0.0.1:8080/v1)
.build/release/MferenceServer \
  --model scratch/qwen36-mtp.gturbo \
  --port 8080 \
  --bind loopback \
  --model-id qwen3.6-35b-a3b \
  --max-context 32768 \
  --prefill-chunk 2048 \
  --prompt-cache-mode single-prefix \
  --expert-cache-slots 48 \
  --verify trusted-receipt
```

See [docs/OPENAI_SERVER.md](docs/OPENAI_SERVER.md) and [docs/OPEN_WEBUI.md](docs/OPEN_WEBUI.md) for server flags and UI options.

---

## Acknowledgments

**Mference 2.0** builds directly upon **[Mference](https://github.com/NeelM0906/Mference)**
by [NeelM0906](https://github.com/NeelM0906), which itself is heavily inspired by
— and its foundation derived from —
**[TurboFieldfare](https://github.com/drumih/turbo-fieldfare)** by Andrey
Mikhaylov (which pioneered running MoE models in bounded memory on Apple Silicon
and documented over a hundred experiments behind its design). Those derived
portions are licensed under the [Apache License 2.0](LICENSE-APACHE); see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for details. New Mference
code is [MIT-licensed](LICENSE).

Model weights and sidecars remain subject to their own terms: the
[Qwen license](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/main/LICENSE)
for [Qwen 3.6 35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
([`mlx-community/Qwen3.6-35B-A3B-4bit`](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-4bit))
and [`guru87/Qwen3.6-35B-A3B-MTP`](https://huggingface.co/guru87/Qwen3.6-35B-A3B-MTP)
for the MTP draft shard. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
