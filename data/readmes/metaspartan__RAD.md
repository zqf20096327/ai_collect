# RAD - Inference Engine

**RAD** is a high-performance, from-scratch multimodal LLM inference engine written in **Rust**, **ROCm/HIP**, and **CUDA**, engineered for ultra-fast single-user speculative generation, 256K long-context inference, and high-throughput multi-user serving on **AMD Radeon AI PRO R9700 (RDNA4 `gfx1201`)** and **NVIDIA Blackwell (`sm_121`, 2x DGX Spark / ASUS Ascent GX10 over ConnectX-7 RoCE v2 RDMA)**.

RAD natively runs:
- **Inkling-2-Mini (ROCm/HIP, R9700 `gfx1201`):** 26B MoE, 48 looped visits, hybrid SWA + full attention, dynamic shortconv, rank-64 loop controllers, native **DFlash 2** & **DSpark** speculative decoding, and native **GPU Vision** via `mmproj-F16.gguf`.
- **DeepSeek-V4.1-Flash-1017 EXL3 (CUDA, 2x DGX Spark `sm_121`):** 40-layer 384-expert MoE (2/3/4/5/6-bit EXL3 `mul1` Tensor Core `mma.sync.aligned.m16n8k16` kernels), 4-stream FP32 mHC Sinkhorn-Knopp, CSA2 sliding-window MQA with `attn_sink` & inverse RoPE, zero-copy GPU-mapped ConnectX-7 RoCE v2 RDMA (`7 us` AllReduce), Engram conditional memory (`layers.1` & `layers.14`), native 3-layer DSpark MTP (`block_size=5`), and DSML tool-call + reasoning OpenAI API.

---

## Highlights

- **Single-R9700 Speed Records:** **`1,224.9 tok/s`** peak single-user decode (`>1,000 tok/s` across `2K–64K`, **`881.6 tok/s`** @ 128K, **`674.4 tok/s`** @ 256K), **`1,074.8 tok/s`** live `/v1/chat/completions` SSE (`1,073.4 tok/s` at `temp=0.2`), **`4,103.8 agg tok/s`** multi-user (`256.5/user` at `B=16`, `3,867.1` / `483.4/user` at `B=8`, `3,011.4` / `752.8/user` at `B=4`, `791.0` / `98.9/user` pure DFlash 2 at `B=8`), **`3,306.5 agg tok/s`** (`413.5/user`) live 8-user HTTP SSE at `temp=0.2`, and **`4,435.3 tok/s`** `pp2048` prefill (**`2,046.4 tok/s`** @ 256K, **`5.79×`** `llama.cpp`) with **`1.84 s`** cold load at 256K.
- **RDNA4 (`gfx1201`) Custom HIP Kernels:** Hand-written Wave32 WMMA `Q4_0_SOA × Q8_1` GEMM/MoE with bank-conflict-free LDS tiling & coalesced epilogues, Split-KV WMMA FlashAttention-2 (single & multi-user), INT8 full-attention KV cache, and HIP graph capture (`B=1`, `K=8..128` verify, and multi-user Flash verify).
- **Native Speculative Decoding:** Zero-copy [`incoai/Inkling-2-Mini-DFlash2`](https://huggingface.co/incoai/Inkling-2-Mini-DFlash2) + DSpark + hybrid `K=128` longest-prefix lookup (single-user & multi-user, **100.00% bit-exact** parity vs no-spec at `temp=0.0`, greedy & GPU top-64 sampled).
- **Agentic & Multimodal Ready:** Native Inkling-2-Mini tool calling, multi-turn prefix caching (`98.9–100.0%` hit rate up to 249K context & across reformatted tool-call JSON via verbatim `tool_call_id` replay, `21–82 ms` cached TTFT/E2E), JSON grammar constraints, and built-in GPU Vision (`mmproj-F16.gguf`).
- **Full OpenAI, Anthropic, vLLM, SGLang & llama.cpp API Server:** Continuous batching (`B<=128`), Paged KV, chunked prefill, 64 MB body limit, `--gpus 0,1` data-parallel serving with prefix-aware routing, Prometheus `/metrics`, API auth, `/v1/chat/completions`, `/v1/completions` (SSE), `/v1/responses` (HTTP/SSE/WS), `/v1/messages` + `/v1/messages/count_tokens` (Anthropic SSE), `/v1/models`, `/tokenize`, `/detokenize`, `/props`, `/slots`, `/version`, `/health`, `/ping`, `/ready`, `/live` on port **`6733`**.

---

## Benchmarks (AMD Radeon AI PRO R9700, `gfx1201`, ROCm 7.14)

### Single-User Decode & Prefill (RAD vs. Stock `llama.cpp` & RTX PRO 6000 Blackwell)

![RAD vs Stock llama.cpp and RTX PRO 6000 Blackwell](assets/rad_benchmark.svg)

Measured end-to-end on the **same AMD Radeon AI PRO R9700 (32 GB, ~\$1,250)**, **same GGUF (`Inkling-2-Mini-UD-Q4_K_XL-v2.gguf`)**, and **same `B=1` / `pp2048` / `tg128`** (`rad bench` 3-run `mean ± stddev`, on-GPU `Q4_0_SOA` weight repacking, **INT8 full-attention KV cache + FP16 SWA KV**), achieving **4.29×–17.37× faster decode** and **5.79× faster `pp2048` prefill** than stock `llama.cpp`, and outperforming Unsloth's claimed **125 tok/s** on an **NVIDIA RTX PRO 6000 Blackwell (96 GB, ~\$8,500)** by **2.42×–9.80×**:

| Engine / Hardware | Decode (`tok/s`) | `pp2048` Prefill (`tok/s`) | Notes |
| --- | --- | --- | --- |
| **Stock `llama.cpp` (R9700 + DSpark)** | `70.5 tok/s` | `765.5 tok/s` | `-fa on -ctk q8_0 -ctv q8_0 --spec-type draft-dspark` |
| **RAD (R9700, No-Spec `hipGraph`)** | **`110.8 ± 0.7 tok/s`** (`1.57×`) | **`4,435.3 ± 3.0 tok/s`** (**`5.79×`**) | `tg128 @ d=2048 = 102.2 tok/s`; `pp512 = 3,562.7 ± 4.0 tok/s` |
| **Unsloth RTX PRO 6000 Blackwell** | `125.0 tok/s` *(claimed)* | - | 96 GB workstation GPU (~\$8,500) |
| **RAD (R9700 + DSpark `K=6`)** | **`148.2 tok/s`** (`2.10×`) | **`4,435.3 tok/s`** (**`5.79×`**) | `verify=23.7 ms`, `avg_emit=4.27` |
| **RAD (R9700 + DFlash 2 `K=8`, Pure Gen)** | **`302.2 tok/s`** (**`4.29×`**) | **`4,370.2 ± 3.2 tok/s`** (**`5.71×`**) | **2.42× vs. RTX PRO 6000 Blackwell**, `Math=271.4 tok/s`, `2K Pure Gen=244.7 tok/s`, `Prose=110.9 tok/s` |
| **RAD (Hybrid DFlash 2 + `K=128`, 2K–256K)** | **`1,224.9 tok/s`** (**`17.37×`**) | **`4,228.1 tok/s`** (**`5.52×`**) | **9.80× vs. RTX PRO 6000 Blackwell**; **`>1,000 tok/s` across 2K–64K**, **`881.6 tok/s`** at 128K, **`674.4 tok/s`** at 256K |

### Long-Context Decode & Prefill (`2K → 256K`, Single 32 GB R9700)

![RAD Long-Context 2K to 256K Scaling on Single R9700](assets/rad_longctx.svg)

Measured via `rad bench --ctx 262144 --max-seqs 1` on a single AMD Radeon AI PRO R9700 (32 GB) with INT8 full-attention KV cache, WMMA SWA FlashAttention (`B >= 16`), live-`pos0` dynamic split-KV (`eff_splits >= 16`), and hybrid DFlash 2 + longest-prefix `K=128` prompt-lookup speculation (`1.84 s` cold load at 256K):

| Context Depth | Prompt Tokens | Prefill (`tok/s`) | Prefill Time | Decode (`tok/s`) | Avg Emit / Round |
| --- | --- | --- | --- | --- | --- |
| **2K** | 1,984 | **4,156.1 tok/s** | 0.48 s | **1,160.2 tok/s** | 86.8 |
| **4K** | 4,074 | **4,161.2 tok/s** | 0.98 s | **1,224.9 tok/s** | 104.0 |
| **8K** | 8,064 | **3,977.5 tok/s** | 1.84 s | **1,147.3 tok/s** | 86.8 |
| **16K** | 16,234 | **3,826.6 tok/s** | 4.24 s | **1,088.7 tok/s** | 86.8 |
| **32K** | 32,764 | **3,621.3 tok/s** | 9.05 s | **1,029.5 tok/s** | 96.5 |
| **64K** | 65,444 | **3,255.7 tok/s** | 20.10 s | **1,009.2 tok/s** | 104.0 |
| **128K** | 130,994 | **2,717.2 tok/s** | 48.21 s | **881.6 tok/s** | 104.0 |
| **256K** | 261,334 | **2,046.4 tok/s** | 127.71 s | **674.4 tok/s** | 96.5 |

### Multi-User Continuous Batching & Batched Speculative Decoding

![RAD Multi-User Scaling on Single R9700](assets/rad_multiuser.svg)

| Workload | Throughput / Latency | Notes |
| --- | --- | --- |
| **Cold Load (`ctx=262144`, DFlash 2)** | **1.80 s** | On-GPU `Q4_0_SOA` + `Q8_0` conversion & `hipGraph` capture |
| **Short Prompt TTFT (`24 tok`, `B=1`)** | **32.7 ± 0.0 ms** | 3-run mean; 8-warp LDS WMMA + high-occupancy `sink_dyn_bf16_smallb_k` |
| **8-User Concurrent Burst TTFT (`B=8`, live SSE)** | **107.2 ms avg** | `106.5–107.7 ms` across all 8 users (`3.2×` faster via batched multi-user prefill) |
| **Prefix-Cached TTFT (`1,645 tok`, `1,639` cached)** | **21.2 ms** | Prefix-cache affinity hit + GQA 3:1 Split-KV FlashAttention |
| **Multi-User Decode (`B=4`, Batched DFlash 2 `K=8`)** | **538.1 agg tok/s** | **`134.5 tok/s/user`** (`ITL 7.4 ms`, 32-tok `exp2f` SWA + single-launch `grid.z` WMMA) |
| **Multi-User Decode (`B=4`, Hybrid DFlash 2 + `K=128`)** | **3,011.4 agg tok/s** | **`752.8 tok/s/user`** (`ITL 1.3 ms`, bank-free WMMA + padded `sm_vt` + 32-tok `exp2f` Q8KV FlashAttention) |
| **Multi-User Decode (`B=8`, no-spec)** | **643.6 agg tok/s** | **`80.4 tok/s/user`** (`ITL 12.4 ms`, `hipGraph` + GQA-3:1 INT8 KV + `loop_ctrl_down_nt_k<8>`) |
| **Multi-User Decode (`B=8`, Batched DFlash 2 `K=8`)** | **791.0 agg tok/s** | **`98.9 tok/s/user`** (`ITL 10.1 ms`; Split-KV multi-user `K<=16` Q8KV + `exp2f` DFlash 2 + SWA FlashAttention) |
| **Multi-User Decode (`B=8`, Hybrid DFlash 2 + `K=128`)** | **3,867.1 agg tok/s** | **`483.4 tok/s/user`** (`ITL 2.1 ms`, bank-free WMMA + padded `sm_vt` + L2 grid tiling + `1,024`-tok verify) |
| **Multi-User Decode (`B=16`, no-spec)** | **926.3 agg tok/s** | **`57.9 tok/s/user`** (`ITL 17.3 ms`, unrolled `nt == 8` MoE + GQA-3:1 INT8 KV) |
| **Multi-User Decode (`B=16`, Batched DFlash 2 `K=8`)** | **1,174.4 agg tok/s** | **`73.4 tok/s/user`** (`ITL 13.6 ms`, 32-tok `exp2f` SWA + `grid.z` WMMA FlashAttention) |
| **Multi-User Decode (`B=16`, Hybrid DFlash 2 + `K=64`)** | **4,103.8 agg tok/s** | **`256.5 tok/s/user`** (`ITL 3.9 ms`, bank-free WMMA + padded `sm_vt` + L2 grid tiling, **92.5% of `pp2048` compute**) |
| **Multi-User Decode (`B=32`, no-spec)** | **1,277.8 agg tok/s** | **`39.9 tok/s/user`** (`ITL 25.0 ms`; +47% via `blockIdx.z` hot-expert splitting & `fused_rg B<=64`) |
| **Multi-User Decode (`B=64`, no-spec)** | **1,162.2 agg tok/s** | `18.2 tok/s/user` (8-warp `128×64` LDS WMMA MoE) |
| **Multi-User Decode (`B=128`, no-spec)** | **1,856.0 agg tok/s** | **`14.5 tok/s/user`** (fused WMMA MoE-to-`Q8_1` + `float4` slot reduction) |
| **Live SSE API (`/v1/chat/completions`, real code edit)** | **1,074.8 tok/s** | Live HTTP SSE streaming `2,048` Python tokens in `1.91 s` (**`1,073.4 tok/s`** at `temp=0.2` via GPU top-64 sampling) |
| **Multi-Turn Agentic E2E (`exec` + `write_file` + `read_file`)** | **98.9–99.5% prefix cache** | Verbatim `tool_call_id` replay survives client JSON reformatting (`77.3 ms` T2 E2E), stop-token speculative rewind |
| **DFlash 2 Hybrid vs No-Spec Accuracy Parity (`temp=0.0`)** | **100.00% bit-exact** | Identical token-for-token outputs across math (`1.97×`), code (`2.54×`), and hybrid edits (`4.54×`) |
| **256K Long-Context Agentic Project E2E (7 turns, live SSE)** | **100.0% cache @ 249K** | Builds & tests multi-file Python project across `443 -> 43K -> 92K -> 182K -> 249K` tok (**`235.6 ms` TTFT**, **`96.2 tok/s`** decode @ 249K, exact Turn-1 recall) |
| **Multi-User 17.5K Long-Context E2E (`B=8`, 2 turns, live SSE)** | **99.8% cache / 222.6 ms TTFT** | Split-KV multi-user `K<=16` FlashAttention + exact `max_tokens` rewind (**`283.2 tok/s`** T1 pure DFlash 2, **`399.1 tok/s`** T2 cached Hybrid) |
| **Live SSE API (8-User Concurrent, Hybrid `K=128`, `temp=0.2`)** | **3,306.5 agg tok/s** | **`413.5 tok/s/user`** avg (**`413.3–413.7 tok/s/user`** across all 8 users, `3,307.0` overlap; pure-gen `B=8` SSE **`315.3 tok/s`**) |
| **Cybara Multi-Turn Agentic E2E (Live Desktop -> RAD R9700)** | **6-turn + 4-turn concurrent** | 10KB Rust analysis (`5,572` chars) + 3-file Python engine (`16/16` tests) + concurrent 80-entry needle haystack (`5,011`-char parser + exact recall), `0` looping |
| **Live SSE API (4-Turn Website Build & Iterate, 6,400 tok)** | **345.1 tok/s avg** | **`1,006.3 tok/s`** T2 / **`867.0 tok/s`** T4 / **`154.4 tok/s`** T1 fresh HTML+CSS+JS (`72.8–115.2 ms` TTFT); **`B=4`** concurrent 2-turn web coding: **`337.5 agg tok/s`** (`9,594` tok in `28.42s`) |
| **Live SSE API (8-User Independent File Edits, `B=8`)** | **2,342.3 agg tok/s** | `9,295` tokens across 8 distinct edits in `3.97 s` (**`289–324 tok/s/user`**, avg `296 tok/s/user`, all 8 users finishing within `0.32 s`) |

### Live Recorded Demo Videos

- **RAD Chat Plain CLI Live Demo (Non-TUI, `Inkling-2-Mini · Q4_K_XL · DFlash 2` + 2x DGX Spark `DeepSeek-V4.1-Flash-1017 · EXL3 2.9bpw`, 1x Real-Time):** [assets/rad_chat_cli.mp4](assets/rad_chat_cli.mp4)
- **RAD Chat TUI Live Demo (`Inkling-2-Mini · Q4_K_XL · DFlash 2` @ `326.4 tok/s` + 2x DGX Spark `DeepSeek-V4.1-Flash-1017 · EXL3 2.9bpw` @ `216.9 tok/s`, 1x Real-Time with Live Metrics & Sparkline):** [assets/rad_chat_tui.mp4](assets/rad_chat_tui.mp4)
- **8-User Concurrent Live SSE Serving (`9,295` tok in `3.97 s`, `2,342 tok/s` full / `296 tok/s/user` avg, up to `324/user`):** [assets/rad_multiuser_x.mp4](assets/rad_multiuser_x.mp4)
- **Single-User Live SSE Serving (`1,075 tok/s` live HTTP SSE code edit):** [assets/rad_promo_x.mp4](assets/rad_promo_x.mp4)

<video src="https://raw.githubusercontent.com/metaspartan/RAD/main/assets/rad_chat_cli.mp4" controls width="100%"></video>

<video src="https://raw.githubusercontent.com/metaspartan/RAD/main/assets/rad_chat_tui.mp4" controls width="100%"></video>

<video src="https://raw.githubusercontent.com/metaspartan/RAD/main/assets/rad_multiuser_x.mp4" controls width="100%"></video>

<video src="https://raw.githubusercontent.com/metaspartan/RAD/main/assets/rad_promo_x.mp4" controls width="100%"></video>

---

## Benchmarks (2x NVIDIA DGX Spark / ASUS Ascent GX10, `sm_121`, CUDA)

First CUDA backend (`rad-cuda` + `rad-dsv41`) running **DeepSeek-V4.1-Flash-1017 EXL3** (40 layers, 384 experts, 2/3/4/5/6-bit EXL3 `mul1` weights, 4-stream FP32 mHC Sinkhorn-Knopp, CSA2 sliding-window MQA with `attn_sink` & inverse RoPE, Engram conditional memory, native 3-layer DSpark MTP) across **2x NVIDIA GB10 Blackwell (`sm_121`)** nodes over **ConnectX-7 RoCE v2 RDMA (`rocep1s0f1`)**:

| Component / Workload | Measured Performance | Notes |
| --- | --- | --- |
| **EXL3 `mul1` Tensor Core GEMV (`M=1`, 4-bit)** | **269.9 GB/s** (**98.9% peak**) | `mma.sync.aligned.m16n8k16` (`rad_exl3_mma.cu`), verified `<2e-5` rel_err across 2/3/4/5/6-bit |
| **EXL3 `mul1` Tensor Core Prefill (`M=16..64`)** | **21.02 TFLOPS** | Fused WHT-128 + `mul1` `0x83DCD12D` Tensor Core MMA |
| **Fused Batched `wo_a` EXL3 MMA (`8x 1024x512`, 5b)** | **14.2 us** (`184.5 GB/s`, **8.3x**) | Single-launch 8-group `exl3_batched_group_mma_m16_mul1_k` (`12.7 us` / `205.9 GB/s` at `M=1`, zero gather/scatter) |
| **Tensor Core MQA+CSA2 FlashAttention (`M>=1`, Split-KV)** | **5.59 ms/layer** (**8.2x** @ 4K) | Bank-free `s_kv[16][520]` `mqa_flash_mma16_f16_k` (`exp2f` softmax) + 48-SM `mqa_flash_mma16_splitkv_f16_k` (`M<=16, ctx>=1K`, zero extra VRAM) |
| **ConnectX-7 RoCE v2 RDMA AllReduce & Argmax** | **7 us** (**134x** vs TCP) | Zero-copy `cudaHostAllocMapped` + `libibverbs` (`32 MB` RDMA ring for `M=2048` prefill) + `IBV_SEND_INLINE` RDMA `all_reduce_argmax` |
| **Tensor Core MoE Router (`384` exp) & `float4` mHC** | **~35 us** router / **~180 us** mHC | `moe_gate_logits_mma_f16_k` (50x prefill speedup) + single-pass `mhc_coeff_proj_24_k` (8x) + `float4`-vectorized `mhc_sinkhorn_mix` & `mhc_pre_mix` |
| **GPU-Grouped MoE Tensor Core MMA (`M=2..2048`)** | **200 GB/s** (`M=128`) / `m64` prefill | 128-bit `uint4` trellis loads, modulo-free indexing, 256-thread `moe_build_groups_k`, `exl3_moe_mma_grouped_m64_mul1_k` (`M>=512`), fused `w3 + clamped_swiglu` post-pass, **100% bit-exact** parity |
| **Live 40-Layer TP=2 RDMA Long-Context Prefill & TTFT (`65K` ctx)** | **640.4 tok/s** (`2K`) / **609.7 tok/s** (`5.5K`) / **507.0 tok/s** (`12K`) | Single-pass `step_batch_last` prefill cuts cold TTFT to **`132.5 ms`** (**`2.0x`** faster than `267.2 ms` vLLM, **`73.7–210 ms`** multi-turn cached), `M=2048` + early-chunk MTP skip + `m64` MoE + FlashMQA |
| **Live 40-Layer TP=2 RDMA Pure Gen (`DSpark MTP` + CUDA Graphs)** | **63.3 tok/s** code (**86.6 tok/s** peak) | `Math=55.0 tok/s`, `Prose=29.2 tok/s`; Tensor Core `mqa_flash_mma16_dspark_f16_k` MTP attention (`16x` fewer KV reads), fused `rad_cuda_markov_argmax_f16`, `split_k=2` wave-balanced MoE `M=6`, `M=1/6/16/32/64/128/512/1024/2048` CUDA Graphs |
| **Live 40-Layer TP=2 RDMA Hybrid (`K=128` Edit, 6.4K Web & Cybara 37K)** | **212.6–269.5 tok/s** (`116.1 tok/s` 6.4K web avg) | `700` chunks in `3.29 s` (`212.6 tok/s`); 4-turn `6,400`-tok live website coding (`21K` chars): **`50.1` -> `229.7` -> `269.5` -> `239.4 tok/s`** (`200–236 ms` cached TTFT, **+48.3%** vs `78.3`); live Cybara 37K ctx: **`99.4 tok/s`** (`8,625` tok, `96.2–98.6%` cache) |

### Supported Models & Weights

| Model | Format / Quants | HuggingFace Weights |
| --- | --- | --- |
| **Inkling-2-Mini** (R9700, ROCm/HIP) | GGUF (`Q4_K_XL` / `Q8_0`) + DFlash 2 + Vision | [Inkling-2-Mini-GGUF](https://huggingface.co/incoai/Inkling-2-Mini-GGUF) · [Inkling-2-Mini-DFlash2](https://huggingface.co/incoai/Inkling-2-Mini-DFlash2) |
| **DeepSeek-V4.1-Flash-1017 (Regular)** (2x DGX Spark, CUDA) | EXL3 `mul1` 2.90 bpw (39 shards, DSpark MTP included) | [LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw](https://huggingface.co/LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw) |
| **DeepSeek-V4.1-Flash-1017 (Abliterated / EAQ v1)** (2x DGX Spark, CUDA) | EXL3 `mul1` 2.90 bpw (39 shards, 4-bit MTP) | `deepseek-ai/DeepSeek-V4.1-Flash-1017` EAQ v1 EXL3 2.90 bpw (`--model <exl3_dir>`) |
| **DeepSeek-V4.1-Flash-1017 Engram Tables** (Optional) | Native FP8 E4M3 (shards 47 & 48, ~190 GiB) | [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) (`--engram-dir <dir>`) |

---

## Repository Structure

```text
RAD/
├── Cargo.toml                 Workspace manifest
├── kernels/
│   ├── build.sh               Backend kernel build dispatcher
│   ├── rocm/                  ROCm/HIP kernels (gfx1201, all modules < 2K LOC)
│   │   ├── build.sh           Builds kernels/rocm/librad_ops.so via hipcc
│   │   ├── rad_ops*.hip       Core decode, RMSNorm, shortconv, attention, loop-ctrl kernels
│   │   ├── rad_batch*.hip     Batched prefill, router & multi-user kernels
│   │   ├── rad_sudot4*.hip    Q4_0_SOA / Q8_1 / NVFP4 sudot4, MoE & fused B=1 kernels
│   │   ├── rad_wmma*.hip      RDNA4 Wave32 WMMA INT8 GEMM, MoE & FP16 FlashAttention-2
│   │   ├── rad_q8kv*.hip      INT8 KV cache store & GQA-3:1 Split-KV WMMA FlashAttention
│   │   ├── rad_dflash2.hip    DFlash 2 grouped dynamic conv, top-16 & path selector kernels
│   │   ├── rad_dspark.hip     DSpark speculative drafter kernels
│   │   └── rad_vision.hip     ViT FP16 GEMM, LayerNorm, GELU, LayerScale, bidirectional attn & 2x2 merge
│   └── cuda/                  NVIDIA Blackwell CUDA kernels (sm_121, all modules < 2K LOC)
│       ├── build.sh           Builds kernels/cuda/librad_cuda_ops.so via nvcc + libibverbs
│       ├── rad_exl3.cu        EXL3 mul1 (0x83DCD12D, __dp4a) WHT-128 & GEMV kernels
│       ├── rad_exl3_mma.cu    Blackwell Tensor Core mma.sync.aligned.m16n8k16 EXL3 GEMM & EP=2 MoE MMA
│       ├── rad_dsv41_ops.cu   FP32 mHC Sinkhorn, YaRN + inverse RoPE, MQA attn_sink, Engram gate & MTP fusion
│       ├── rad_dsv41_router.cu Vectorized half2 MoE sqrtsoftplus router, parallel 256-thread top-K & argmax
│       └── rad_rdma.cu        Zero-copy cudaHostAllocMapped ConnectX-7 RoCE v2 RDMA (libibverbs)
├── crates/
│   ├── rad-http/              Shared OpenAI/Prometheus HTTP helpers, auth, CORS, reasoning & cycle detection
│   ├── rad-chat/              Cross-platform Rust CLI & `ratatui` TUI (`rad-chat`) with live streaming metrics & sparkline
│   ├── rad-gguf/              Zero-copy mmap GGUF reader
│   ├── rad-hip/               Minimal ROCm/HIP FFI, RAII DevBuf, P2P & CapturedGraph
│   ├── rad-core/              InklingEngine (model/{mod,decode,multi,profile}), DFlash 2 & DSpark, Paged KV, VisionEncoder
│   ├── rad-serve/             `rad` CLI + Axum server (main, types, prompt, scheduler, handlers, grammar, metrics, bench)
│   ├── rad-cuda/              Minimal CUDA FFI, RAII CudaBuf, CudaCapturedGraph & ConnectX-7 TP=2 RDMA/TCP comm
│   └── rad-dsv41/             DeepSeek-V4.1-Flash EXL3 TP=2 engine (`rad-dsv41`: weights, engine, engram, mtp, server)
├── assets/
│   ├── rad_benchmark.svg      Single-user decode & prefill comparison chart
│   ├── rad_longctx.svg        Long-context 2K–256K decode & prefill scaling chart
│   ├── rad_multiuser.svg      Multi-user throughput scaling chart
│   ├── rad_chat_cli.mp4       Live 1x real-time plain non-TUI `rad-chat --cli` demo across R9700 & 2x DGX Spark
│   ├── rad_chat_tui.mp4       Live 1x real-time `rad-chat` TUI demo across R9700 & 2x DGX Spark
│   ├── rad_multiuser_x.mp4    Live recorded 8-user concurrent SSE demo video
│   └── rad_promo_x.mp4        Live recorded single-user SSE code-edit demo video
└── scripts/
    ├── test_serve.py          End-to-end HTTP, SSE, batch, and WebSocket test suite
    ├── test_e2e_realworld.py          Real-world 10-test multi-user SSE, Anthropic/OpenAI/compat API, prefix cache & grammar suite
    ├── test_e2e_edge_cases.py         11-test production edge-case suite (401 auth, ctx overflow, SSE cancel, streaming stops, top_k/min_p, mixed TTFT)
    ├── test_e2e_longctx_agent.py      Real-world 7-turn 256K long-context agentic project-building E2E test
    ├── test_e2e_multiuser_longctx.py  Multi-user B=8 17.5K long-context multi-turn prefix-cache & SSE E2E test
    └── test_accuracy_spec_parity.py   DFlash 2 Hybrid vs No-Spec bit-exact token-parity & accuracy verification
```

---

## Quickstart

### Interactive Chat CLI / TUI (`rad-chat`, Windows / Linux / macOS, no GPU required)

```bash
# Build cross-platform TUI client (zero GPU dependencies)
cargo build --release -p rad-chat

# Launch plain non-TUI interactive chat CLI (clean streaming terminal REPL)
./target/release/rad-chat --cli --url http://127.0.0.1:6733

# Launch interactive full-screen TUI with live streaming tok/s, TTFT, sparkline & /metrics telemetry
./target/release/rad-chat --url http://127.0.0.1:6733

# Connect to 2x DGX Spark DeepSeek-V4.1-Flash with custom header badge & thinking enabled
./target/release/rad-chat --url http://192.168.1.149:8888 --api-key <key> --display-name "DeepSeek-V4.1-Flash-1017 · EXL3 2.9bpw" --think

# One-shot streaming CLI mode
./target/release/rad-chat --url http://127.0.0.1:6733 --prompt "Write a fast Rust binary search."
```

Slash commands inside the TUI: `/clear`, `/model [name]`, `/url <http://...>`, `/think`, `/effort <low|medium|high>`, `/temp <f>`, `/stats`, `/exit`.

### Prerequisites & Model Weights

- Linux with **ROCm 6.x / 7.x** (`hipcc`, `libamdhip64`, `libhipblas`, `librocblas`)
- **Rust** toolchain (`cargo`, edition 2021)
- **Inkling-2-Mini GGUF & Vision (`mmproj-F16.gguf`):** [unsloth/Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF) (`Inkling-2-Mini-UD-Q4_K_XL.gguf`, `mmproj-F16.gguf`, and `tokenizer.json`)
- **DFlash 2 Speculative Drafter (Recommended):** [incoai/Inkling-2-Mini-DFlash2](https://huggingface.co/incoai/Inkling-2-Mini-DFlash2) (`model.safetensors` + `config.json`)

```bash
huggingface-cli download unsloth/Inkling-2-Mini-GGUF \
  Inkling-2-Mini-UD-Q4_K_XL.gguf mmproj-F16.gguf \
  --local-dir ./models/inkling2

huggingface-cli download incoai/Inkling-2-Mini-DFlash2 \
  --local-dir ./models/inkling2-dflash2
```

### 1. Build HIP Kernels

```bash
RAD_ARCH=gfx1201 bash kernels/rocm/build.sh
```

### 2. Build RAD

`crates/rad-core/build.rs` and `crates/rad-serve/build.rs` automatically link `kernels/rocm/librad_ops.so` with `-Wl,-rpath`, so no manual `RUSTFLAGS` or `LD_LIBRARY_PATH` is required:

```bash
cargo build --release
```

### 3. Run the CLI (`rad`)

`rad` automatically detects sibling `tokenizer.json`, **DFlash 2** (`../inkling2-dflash2/model.safetensors`, preferred over DSpark), **DSpark** (`dspark-Inkling-2-Mini-Q8_0.gguf`), and **Vision** (`mmproj-F16.gguf`, enabled by default):

```bash
./target/release/rad serve -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf --port 6733

./target/release/rad serve -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf --gpus 0,1 --port 6733

./target/release/rad serve -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf --ctx 131072 --max-seqs 2 --port 6733

./target/release/rad run "Show me a Python quicksort function." -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf

./target/release/rad run "Describe this image." --image /path/to/photo.png -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf

./target/release/rad info -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf
```

### 4. Run Built-In Benchmarks (`rad bench`)

Includes Cold Load, TTFT, `pp512`/`pp2048` Prefill, Single-User Code/Math/Prose, Multi-User `B=4/8/16`, and **2K–256K Long-Context Scaling**:

```bash
./target/release/rad bench -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf --ctx 4096 --max-seqs 16

./target/release/rad bench -m /path/to/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf --ctx 262144 --max-seqs 1

python3 scripts/test_serve.py
```

### 5. Build & Run CUDA Backend (2x NVIDIA DGX Spark, `sm_121`)

Requires **CUDA 12.x / 13.x** (`nvcc`), `libibverbs-dev` (for ConnectX-7 RoCE v2 RDMA), and **Rust**:

```bash
bash kernels/cuda/build.sh
cargo build --release --manifest-path crates/rad-dsv41/Cargo.toml

./crates/rad-dsv41/target/release/rad-dsv41 \
  --model-dir /path/to/deepseek-v4.1-flash-1017-exl3 \
  --rank 0 --world-size 2 --peer-addr 10.100.232.1:29500 \
  --rdma-dev rocep1s0f1 --port 8888

./crates/rad-dsv41/target/release/rad-dsv41 \
  --rank 1 --world-size 2 --peer-addr 10.100.232.1:29500 \
  --rdma-dev rocep1s0f1
```

Rank 0 streams Hadamard-128 aligned TP=2/EP=2 shards to Rank 1 over ConnectX-7 at startup, so Rank 1 requires zero local model storage.

### 6. Install & Deploy (Docker, `.deb`, Homebrew, Flatpak)

- **Docker with AMD ROCm GPU Passthrough:**
  ```bash
  RAD_MODELS_DIR=/path/to/models docker compose up -d
  ```
  Or directly:
  ```bash
  docker run --rm -p 6733:6733 \
    --device=/dev/kfd --device=/dev/dri \
    --group-add video --group-add render \
    --security-opt seccomp=unconfined --ipc=host \
    -v /path/to/models:/models:ro \
    ghcr.io/metaspartan/rad:latest serve -m /models/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf --port 6733
  ```
- **Debian / Ubuntu (`.deb`):**
  Download `rad_<version>_amd64.deb` from GitHub Releases or build locally:
  ```bash
  bash packaging/deb/build_deb.sh 0.17.0
  sudo dpkg -i dist/rad_0.17.0_amd64.deb
  ```
- **Homebrew (Linuxbrew):**
  ```bash
  brew install --build-from-source packaging/homebrew/rad.rb
  ```
- **Flatpak:**
  ```bash
  flatpak-builder --user --install --force-clean build-dir packaging/flatpak/io.github.metaspartan.RAD.yml
  ```

---

## Configuration

| Environment Variable | Default | Description |
| --- | --- | --- |
| `RAD_MODEL` | `./models/Inkling-2-Mini-UD-Q4_K_XL-v2.gguf` | Target model GGUF path |
| `RAD_TOKENIZER` | *(auto-detected)* | HuggingFace `tokenizer.json` path |
| `RAD_DFLASH2` | *(auto-detected)* | Optional DFlash 2 safetensors dir/file (preferred over DSpark) |
| `RAD_DSPARK` | *(auto-detected)* | Optional DSpark drafter GGUF path |
| `RAD_MMPROJ` | *(auto-detected)* | Optional vision `mmproj-F16.gguf` path |
| `RAD_SPEC` | `1` | Enable (`1`) or disable (`0`) speculative decoding |
| `RAD_VISION` | `1` | Enable (`1`) or disable (`0`) GPU vision encoder |
| `RAD_CTX` | `8192` | Per-sequence KV context length (tested up to `262144`) |
| `RAD_MAX_SEQS` | `32` | Maximum concurrent sequences in KV pool |
| `RAD_PORT` | `6733` | HTTP/WebSocket bind port |
| `RAD_GPUS` | `0` | Comma-separated HIP GPU IDs (`0,1`) or `auto` for multi-GPU data-parallel serving |
| `RAD_API_KEY` | *(empty)* | Optional comma-separated Bearer / `X-API-Key` tokens (disabled if empty) |
| `RAD_ARCH` | `gfx1201` | Target GPU architecture for `kernels/build.sh` |

---

## API Reference

All endpoints are served on `--port` (default `6733`). When `--api-key` / `RAD_API_KEY` is set, pass either `Authorization: Bearer <key>` or `x-api-key: <key>` (health probes are always unauthenticated; `/metrics` is unauthenticated unless `--metrics-auth` is passed). Request body limit is `64 MB`.

### Inference & Agentic Endpoints

| Method | Endpoint | Protocol / Compatibility | Features |
| --- | --- | --- | --- |
| `POST` | `/v1/chat/completions` | OpenAI Chat Completions (sync & SSE) | Continuous batching, vision (`image_url`), native tool calling (`tools`, `tool_choice`), `response_format` (`json_object` / `json_schema`), `stream_options.include_usage`, `stop`, `temperature`, `top_p`, `top_k`, `min_p`, `repetition_penalty`, `presence_penalty`, `frequency_penalty`, `seed`, `chat_template_kwargs.enable_thinking`, prefix-cache `cached_tokens`, immediate GPU slot cancellation on SSE disconnect |
| `POST` | `/v1/completions` | OpenAI Legacy Completions (sync & SSE) | Single string or batched `prompt: [...]`, SSE streaming with `include_usage`, `stop`, `temperature`, `top_p`, `top_k`, `min_p` |
| `POST` | `/v1/responses` | OpenAI Responses API (sync & SSE) | Structured `input` / `instructions`, tool calls (`function_call` / `function_call_output`), `reasoning`, `max_output_tokens`, `cached_tokens` |
| `GET` | `/v1/responses` | OpenAI Responses API (WebSocket) | Persistent WebSocket streaming (`?api_key=` or auth header) |
| `POST` | `/v1/messages` | Anthropic Messages API (sync & SSE) | System prompts, `thinking` blocks, `tools` / `tool_use` / `tool_result`, `stop_sequences` (sync & SSE), `temperature`, `top_p`, `top_k`, `min_p`, `cache_read_input_tokens` |
| `POST` | `/v1/messages/count_tokens` | Anthropic Token Counting | Exact tokenizer input token count for Anthropic message payloads |

### Tokenization, Models & Introspection

| Method | Endpoint | Compatibility | Description |
| --- | --- | --- | --- |
| `POST` | `/tokenize`, `/v1/tokenize` | vLLM / SGLang / `llama.cpp` | Tokenize `prompt`, `text`, or `content` into token IDs and count |
| `POST` | `/detokenize`, `/v1/detokenize` | vLLM / SGLang / `llama.cpp` | Detokenize `tokens` array back into `text` / `content` |
| `GET` | `/v1/models`, `/models` | OpenAI / `llama.cpp` | List served models and context/capability metadata |
| `GET` | `/v1/models/:id` | OpenAI | Retrieve single model object by ID |
| `GET` | `/props` | `llama.cpp` | Server properties (`n_ctx`, `total_slots`, model & spec configuration) |
| `GET` | `/slots` | `llama.cpp` | Live continuous-batching slot & Paged KV block status (`active`, `prefilling`, `queued`, `kv_blocks_used`) |
| `GET` | `/version` | vLLM / SGLang | Engine version, spec mode, and GPU architecture |
| `GET` | `/metrics` | Prometheus | Request counts, TTFT/decode histograms, prefix-cache hits & tokens saved, KV utilization |
| `GET` | `/health`, `/ping`, `/ready`, `/live` | Kubernetes / vLLM / SGLang / `llama.cpp` | Liveness and readiness probes (`200 OK`) |

---

## License

MIT — Copyright (c) 2026 Carsen Klock. See [LICENSE](LICENSE).
