# <img src="docs/icons/chip.svg" width="24" height="24" align="absmiddle" alt=""/> rdna4-amd-infer: RX 9070 XT LLM Engine

**Fast local LLM inference engine for AMD Radeon RX 9070 XT (RDNA4 / `gfx1201`) built on top of Han Wang's [`hanw/amd.c`](https://github.com/hanw/amd.c), adding Windows 11 WDDM support (no system ROCm install) and 310 custom AMDGPU kernels (`217` Inkling-2-Mini with `0/0` VGPR spills and `priv=0`, `81` Saluki-27B, `12` ViT vision including `6` RDNA4 WMMA).**

Base C11 engine & verified core by [`hanw/amd.c`](https://github.com/hanw/amd.c) · Windows WDDM port + 310 custom `gfx1201` kernels + DSpark/shortlist/256K long-context/0-VRAM WMMA vision/IoRing+4T-BPE added here · Linux ROCm ready · GGUF v3 · OpenAI-compatible `ie-serve` API.

> **Upstream Credit & License Note:** The base C11 runtime, formally verified core (`engine/core/ie_core.h`), base `gfx1201` kernels, and `ie-serve` architecture come from Han Wang's [`hanw/amd.c`](https://github.com/hanw/amd.c) (and `engine/src/iq3s_grid.h` carries ggml's MIT header). Because upstream `hanw/amd.c` does not currently include a `LICENSE` file, this repository intentionally does **not** apply a separate open-source license over Han's upstream code. All credit for the base engine belongs to Han Wang; if upstream adds a license (or requests changes/removal of upstream files), this repo will follow immediately.

<p align="center">
  <a href="https://saloqt.github.io/rdna4-amd-infer/">
    <img src="docs/hero-scoreboard.svg" alt="RX 9070 XT 16GB Matched Live Benchmarks: Inkling-2-Mini 26B IQ3_XXS 189.3 tok/s snake decode and 3,792 tok/s 28.7K OMP prefill; Saluki-27B Qwen3.8 IQ2-mix 142.1 tok/s snake decode and 1,134 tok/s 23.8K OMP prefill" width="100%"/>
  </a>
</p>

**Exact quants tested above (single 16GB RX 9070 XT, Windows WDDM, streaming):**
- **Inkling-2-Mini (26B MoE):** `IQ3_XXS` GGUF (`output.weight` `Q4_K`), `Q4_K` DSpark + 0-VRAM 2-tier (`28K -> 60K + 4K`) shortlist, `f16` KV cache (default 96K ctx; up to **256K filled ctx + DSpark** with global `q4rot` KV + outer-layer SLRU MoE cache) + **0-VRAM RDNA4 WMMA ViT vision** (`28.4 - 83.8 ms`)
- **Saluki-27B (`Qwen3.8-27B`):** `IQ2-mix` GGUF, `IQ3_S` MTP7 (65K draft vocab), `q8` KV cache (128K ctx) + 0-VRAM ViT vision

<img src="docs/icons/chart.svg" width="15" height="15" align="absmiddle" alt=""/> **[Open Interactive 52-Round Telemetry Dashboard](https://saloqt.github.io/rdna4-amd-infer/)**: hover tooltips, frontier lines, filterable ledger, and research links for every round (`R00-R52`).

---

## Live Real-Time Demo (1x Speed, RX 9070 XT 16 GB)

Unedited 1x screen recording of `Inkling-2-Mini` (`26B IQ3_XXS`, `Q4_K` DSpark, `temp 0.6 / top_p 0.85 / top_k 20`, medium reasoning) running locally via `ie-serve` + Open WebUI on a single RX 9070 XT 16 GB (Windows WDDM, simultaneously capturing video on the same GPU): `3,882` output tokens in `35.62 s` (`109.0 tok/s`, `3.25` tok/step) generating and rendering a live 3D Rubik's Cube.

<p align="center">
  <a href="https://github.com/SaloQT/rdna4-amd-infer/releases/download/media-demo/inkling2-live-demo-1080p.mp4">
    <img src="docs/inkling2-live-demo.webp" alt="Real-time 1x speed live demo of Inkling-2-Mini 26B IQ3_XXS running on AMD Radeon RX 9070 XT 16GB via ie-serve and Open WebUI generating a 3D Rubik's Cube" width="100%"/>
  </a>
  <br/>
  <sub><i>Auto-playing 24-bit animated WebP (1280x634, 12 fps, real-time 1x) · <a href="https://github.com/SaloQT/rdna4-amd-infer/releases/download/media-demo/inkling2-live-demo-1080p.mp4">Watch / download full 1920x950 30 fps H.264 MP4 (8.6 MB)</a></i></sub>
</p>

---

<p align="center">
  <a href="https://saloqt.github.io/rdna4-amd-infer/">
    <img src="docs/progress-chart.svg" alt="AMD Radeon RX 9070 XT RDNA4 Inkling-2-Mini 26B IQ3_XXS 52-Round Optimization Benchmarks" width="100%"/>
  </a>
  <br/>
  <sub><i>Click chart to open the full-screen interactive 52-round telemetry dashboard</i></sub>
</p>

---

## <img src="docs/icons/gauge.svg" width="20" height="20" align="absmiddle" alt=""/> RX 9070 XT Benchmarks

> Single AMD Radeon RX 9070 XT 16 GB · Windows 11 WDDM · Trace-off **true host wall clock** (not GPU-event clocks). All baselines (`v0`, `Early`, `R0`, `R00`) are our own earlier `amd-infer` implementations before each round of custom kernels, not upstream builds. Click any chart for full resolution.

### 1. Inkling-2-Mini (26B `IQ3_XXS` MoE · DSpark)

<p align="center">
  <a href="docs/inkling2-benchmarks.svg">
    <img src="docs/inkling2-benchmarks.svg" alt="Inkling-2-Mini 26B IQ3_XXS GGUF Benchmarks on AMD RX 9070 XT 16GB Windows WDDM" width="100%"/>
  </a>
</p>

<details>
<summary><img src="docs/icons/table.svg" width="14" height="14" align="absmiddle" alt=""/> <b>Raw Inkling-2-Mini (`IQ3_XXS`) Numbers Table (R00-R52)</b></summary>

| Metric | First Impl (`v0` / Early) | Prior (`R00`) | **Promoted (`R51/R52`)** | Gain |
|---|---:|---:|---:|---:|
| **Matched Snake HTML (med)** | - | - | **189.3 tok/s** (`2,625` tok, `mtp 3.83`, R37 ref) | Live streaming |
| **Matched OMP Prefill (28.7K)** | - | - | **3,792 tok/s** (`7.58 s` TTFT, `0` cached, R37 ref) | 28.7K real OMP |
| **Matched OMP Decode (30-42K)** | - | - | **148.2 tok/s** avg (`178.3` @ 42K, R37 ref) | `84ms` warm TTFT |
| **4K Cold Prefill (`chunk=1024`)** | 1,118 tok/s *(v0)* | 4,644 tok/s (`882 ms`) | **6,135 tok/s** (`668 ms`) | **5.49x** vs v0 (`+32.1%` R00) |
| **16K Cold Prefill (`chunk=1024`)** | - | 4,368 tok/s (`3.75 s`) | **5,716 tok/s** (`2.87 s`; `5,721` R50) | **+30.9%** vs R00 |
| **Plain `T=1` Decode** | 90.5 tok/s | 109.2 tok/s | **126.6 tok/s** (`7.71 ms` GPU; `126.5` R52) | **+39.9%** (`+16.0%` R00) |
| **DSpark Short Code (233)** | ~230 tok/s | 281.5 tok/s | **319.3 tok/s** (`1.32 ms` draft, `19.6 ms` ver) | **+13.4%** vs R00 |
| **DSpark 16K Decode** | - | 138.6 tok/s | **170.7 tok/s** (`19.2 ms` T=8; `170.3` R52) | **+23.2%** (`-17.9%` ver) |
| **Live `ie-serve` Chat** | 118.2 tok/s | 146.7 tok/s | **169.5 tok/s** sampled *(greedy **191.2**)* | **+43.4%** (`+14.7%` greedy) |
| **Prefix-Hit TTFT** | - | 2,113 ms (`14` tok) | **226 ms** (`8,192` tok cached) | **9.35x faster** |
| **CPU Sampling + DRY** | ~0.44 ms/step | 0.399 ms/step | **0.005 ms/step** (`0.006` R51) | **80x faster** |
| **Launches / Step** | 2,222 | 1,574 | **585** (`753` R52, `0.453 ms` issue) | **-73.7%** (`-62.8%` R00) |
| **SWA Disk Cache & Resume (`20K` Q4rot)** | 357.5 MB (`2.03 s`) | 181.3 MB (`1.11 s`) | **`-40.4%` cold / `-61.1%` prewarm** (`275 -> 164 / 107 ms`, `IoRing` + H2D pipe) | **1.68x - 2.57x faster** |
| **256K Prompt BPE (`261.6K` tok)** | - | `16.93 ms` (1T) | **`3.87 ms`** (4T stack BPE + seg cache, bit-exact) | **4.37x faster** |

</details>

### 1b. Filled 128K & 256K Context + DSpark on 16 GB VRAM (Inkling-2-Mini, `R53 - R87`)

Inkling-2-Mini (`26B IQ3_XXS`) runs **filled 128K and 256K context with DSpark active inside 16 GB VRAM** on Windows WDDM without swapping or spilling past DXGI budget (`+1,731 - 2,089 MiB` DXGI reserve at 256K, `2.7x - 3.3x` above the `640 MiB` gate):
- **Global-only `Q4_0 + FWHT-128` KV + SOTA Prefill/Verify (`IE_INK_GLOB_KV=q4rot`):** Quantizes only the 8 global KV layers to 72 B/head (`2,304 MiB` exact at 256K, 4K KLD `0.004511`, `98.91%` top-1, ppl `1.2024` vs `1.2015` f16) while all 40 SWA layers stay `f16`. `R53 - R87` added dedicated `Q4_0` WMMA verify (`R59`), split-KV incremental prefill (`R60`), fast `Q4_0` prefill (`R61`), fused `sconv+vclip+q4_store` (`R65`), and `chunk=1024` guarded by DXGI clamp (`R56`) + async ping-pong H38 prefill (`R57`).
- **Ringed DSpark Global KV + Auto-16K Window + Persistent 256K SAM (`R66 - R71`):** Caps DSpark's global KV (`IE_DS_GLOB_WIN=auto16k` natively, `8192` via `serve-inkling2.ps1 -Ctx 262144`), computes RoPE on the fly (`IE_DS_ROPE_OTF=1`, `-127.5 MiB`), fuses DSpark Markov/QKV/attn/proj (`R66` + `R73` fixed `H25a`), runs 2-tier shortlist (`28K -> 60K` + `4K` dynamic tail, `R70`), lossless `T_draft=0.75` sharpening (`R69`), and a persistent 2-tier 256K prompt-suffix SAM (`R71`).
- **Outer-Layer SLRU MoE Cache + Exact-SHA Wave Repacks (`R72 - R76`):** Pins outer layers (`blk.0..5, 18..23`) in host RAM with a VRAM SLRU expert cache while keeping all 12 core looped layers (`blk.6..17`, visited 3x/token) and all 24 dense layers VRAM-resident. `R72 - R76` promoted exact-SHA `H17` loop fusion (`705 -> 585` launches/step), `H36a` zero-VRAM `IQ4_NL` wave repack (`+13.9%` 256K `T=1`) + `BM=64` prefill, `R13` exact router (`+6.5%` 4K prefill) + `R17` `FLUTE` `BM=64` worklist, and `H37` `Q8_0` core wave repack (`+17.5%` 256K `T=1` / `+15.0%` 256K DS5).
- **Wave 15 Instant Resume & Tokenization (`R78 - R83`):** Promoted Windows `IoRing`/pooled `OVERLAPPED` reader (`IE_DISK_IORING=1`) + async pipelined H2D (`IE_KV_H2D_PIPE=1`, `-40.4%` cold disk restore at `20K` Q4rot: `275 -> 164 ms`), idle background disk-to-RAM pre-warming (`IE_DISK_PREWARM=1`, `-61.1%` restart restore at `20K` Q4rot: `275 -> 107 ms`, `20/20` files from RAM), GPU `K_COPY_LIST` ephemeral stash (`IE_EPHEM_FAST=1`, `3.66x` faster at `20K` Q4rot: `32.2 -> 8.8 ms`), and 4-thread stack BPE + segment cache (`4.37x` faster at `256K`: `16.93 -> 3.87 ms` for `261,619` tokens, 100% bit-exact).

| 256K Filled Context Metric (`IQ3_XXS` · 16 GB WDDM) | `R52` (Wave 9) | **`R71 - R87` Promoted** | Gain / Notes |
|---|---:|---:|---|
| **Launches / Step (`T=1`)** | `753` (`1,574` R00) | **`585`** (`0.453 ms` issue) | **`-62.8%`** vs R00 (`-22.3%` vs R52) |
| **Real 256K (`261,632` tok) Cold Fill** | `227.0 s` | **`106 s`** (`~2,468 tok/s` avg) | **`2.14x` faster** (`chunk=1024` + `Q4` PF + `H38-ASYNC-PF`) |
| **256K `inc256` TTFT** | `600 - 630 ms` | **`236 ms`** synth / **`306 ms`** live | **`2.67x` faster** (`Q4` split-KV incremental prefill) |
| **256K Verify `T=6` / `T=8`** | `64.6 / 79.7 ms` | **`23.51 / 25.58 ms`** (`R87`) | **`2.75x - 3.12x` faster** (`Q4` WMMA + `H17` + `H36a` + `H37`) |
| **Live 256K `ie-serve` DSpark (`261.4K`, 3/3 needles)** | `54.5 tok/s` | **`107.5`** greedy / **`137.0`** sampled (`t=1.0`, R71) | **`1.97x - 2.51x` faster** (+ `H36a +13.9%` / `H37 +15.0%` R74-R76) |
| **Live 154-Req Multimodal Tool Session (`204K - 212K`)** | - | **`130 - 147 tok/s`** (peak **`219.7`** @ `156K - 180K`) | Live `1365x768` screenshots + tool calls, `3/3` needles |
| **256K Worst DXGI Reserve** | `+870 MiB` | **`+1,731 - 2,089 MiB`** (`R87`) | **`2.7x - 3.3x`** above `640 MiB` gate (`0` swap) |
| **Disk Restore (`20K` Q4rot) / Stash (`20K` Q4rot) / 256K BPE** | `275 ms` / `32.2 ms` / `16.93 ms` | **`164 ms`** cold (`107 ms` prewarm) / **`8.8 ms`** / **`3.87 ms`** | **`-40.4%` / `-61.1%`** restore (`20K`) · **`3.66x`** stash (`20K`) · **`4.37x`** BPE (`256K`) |
| **128K Filled (`130,500` tok, `ie-serve`)** | `53.7` plain | **`90.2 tok/s`** DSpark (`4.38` tok/step, `+1,997 MiB` res) | **`+68.0%` (`1.68x`)**, `405 ms` `inc256`, `3/3` needles |

```powershell
# Automatic 256K + DSpark profile (-Chunk 1024 with DXGI guard, -Draft 7 -DraftPmin 0.45, q4rot global KV, 8K DSpark ring, OTF RoPE, auto MoE SLRU):
powershell -File engine\serve-inkling2.ps1 -Ctx 262144

# Opt-in 128K + DSpark low-VRAM profile:
powershell -File engine\serve-inkling2.ps1 -Ctx 131072 -GlobKv q4rot -DsGlobWin 8192 -MoeCacheSlots auto
```

### 1c. Zero-Persistent-VRAM RDNA4 WMMA Vision (Inkling-2-Mini `inkling2v`)

Inkling-2-Mini (`OpenUncensored/Inkling-2-Mini-Uncensored`) supports native multimodal image input via 6 custom RDNA4 (`gfx1201`) WMMA vision kernels ([`engine/kernels/ie_vision_wmma_r14.inc`](engine/kernels/ie_vision_wmma_r14.inc): FP16 & Q8_0 WMMA GEMM, inline 2D Axial RoPE `hd=64` WMMA FlashAttention, fused LayerNorm, patch-prep, and 2x2 spatial merge; all 6 at `<= 94` VGPR, `0/0` spills, `4` WGs/CU):
- **Zero persistent VRAM (`0.00 MiB` delta):** Double-buffered async H2D weight streaming borrows Inkling-2's idle LLM prefill arena inside `ie-serve` (`102.8 MiB` peak at `1280x1280` `Q8_0` inside the `140.0 MiB` 256K arena; fixed 4 MiB VMM fallback standalone). Live 256K `ie-serve` DXGI stayed flat at `11.04 / 12.15 GiB` (`+1.11 GiB` reserve, `0.00 MiB` leak across mixed resolutions).
- **24.4x faster than scalar ViT (`Q8_0` default):** Download [`mmproj-Inkling-2-Mini-Q8_0.gguf`](https://huggingface.co/AtomicChat/Inkling-2-Mini-GGUF) (`346 MB`, default; `1.12x - 1.74x` faster than F16 over PCIe) or [`mmproj-Inkling-2-Mini-Uncensored-F16.gguf`](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF) (`639 MB`, fallback) into `models/`. `serve-inkling2.ps1` auto-detects it (`-Mmproj PATH` / `-NoVision` overrides).

| Resolution (`inkling2v` `Q8_0`) | Merged Tokens | WMMA Encode Latency | CPU vs GPU Cosine | Live E2E (`64K` / `256K q4rot` + DSpark) |
|---|---:|---:|---:|---|
| **`640x640`** (`16x16`) | `256` tok | **`28.4 ms`** | `0.999989` | **5/5 PASS** (OCR, spatial color/shape, bar chart, |
| **`1040x1040`** (`26x26`) | `676` tok | **`53.4 ms`** | `0.999989` | 2x2 hi-res grid, multi-turn vision+KV cache hit); |
| **`1280x1280`** (`32x32`) | `1,024` tok | **`83.8 ms`** (`24.4x` vs scalar) | `0.999985 - 0.999998` | `155 - 215 tok/s` (64K), `121 - 165 tok/s` (256K) |

### 2. Saluki-27B (`Qwen3.8 IQ2-mix` · 128K · 16GB)

<p align="center">
  <a href="docs/saluki-benchmarks.svg">
    <img src="docs/saluki-benchmarks.svg" alt="Saluki-27B Qwen3.8-27B IQ2-mix 128K Context Benchmarks on AMD RX 9070 XT 16GB" width="100%"/>
  </a>
</p>

<details>
<summary><img src="docs/icons/table.svg" width="14" height="14" align="absmiddle" alt=""/> <b>Raw Saluki-27B (`IQ2-mix`) Numbers Table</b></summary>

| Metric | First Impl (`R0`) | **Promoted (`R11`)** | Gain |
|---|---:|---:|---:|
| **Matched Snake HTML (med)** | - | **142.1 tok/s** (`1,866` tok, `mtp 5.14`) | Live streaming |
| **Matched OMP Prefill (23.8K)** | - | **1,134 tok/s** (`21.0 s` w/ ckpts; **1,242** clean) | 23.8K real OMP |
| **Matched OMP Decode (24-40K)** | - | **109.7 tok/s** avg (**166.0** file write) | `126ms` warm TTFT |
| **4.3K Cold Prefill** | 707 tok/s (`6.10 s`) | **1,177 tok/s (`3.67 s`)** | **+66.5% · -39.9% TTFT** |
| **23.3K Cold Prefill** | 685 tok/s (`33.4 s`) | **1,242 tok/s (`18.8 s`)** | **+81.3% · -43.7% TTFT** |
| **Sustained Decode** | 98.7 tok/s | **113.8 tok/s** *(peak **167.9** @ `mtp 5.79`)* | **+15.3%** |
| **Warm 23K TTFT** | 377 ms | **258-286 ms** (`23,234 / 23,312` cached) | **-31.6%** |
| **Disk Restart (26.7K)** | 22.9 s cold | **0.61 s** *(157 MB state + KV blocks)* | **37.5x faster** |
| **Rank-32 LoRA Decode** | 46-57 tok/s | **87-108 tok/s** (`IE_LORA_WAVE32=1`) | **~1.9x faster** |

</details>

---

## <img src="docs/icons/bolt.svg" width="20" height="20" align="absmiddle" alt=""/> Why It's Fast on RDNA4

1. **WDDM Launch Collapse (`2,222 -> 585`):** Fusing 4 loop controllers (`H17` exact, `-120` launches/step), single-launch QKV+sconv+KV (`H20`), router+top8+sort, K/V short-conv+vclip+store (`C1` FP16 & `Q4_0`), MoE tail, `CT=8` QKV/RelClip/Sink/Gate, `W_o+sconv`, and FLUTE `IQ3_XXS` expert paths cut Windows HIP issue time to `0.453 ms/step`.
2. **0-VRAM FLUTE SoA `IQ3_XXS` + Wave-Interleaved `IQ4_NL` & Core `Q8_0` Repacks (`R42`, `R74`, `R76`):** Load-time SoA transpose of `IQ3_XXS`, zero-persistent-VRAM wave-interleaved `IQ4_NL` (`+13.9%` 256K `T=1`), and core `blk.6..17` `Q8_0` wave repack (`+17.5%` 256K `T=1`, `+15.0%` 256K DS5) eliminate bit-unpack and bank-conflict stalls with 100% exact SHA.
3. **`chunk=1024` RDNA4 WMMA Prefill (`6,135 tok/s` @ 4K, `106 s` @ 256K):** Largest-first `BM=64` `FLUTE` + `IQ4_NL` wave worklists (`R74`, `R75`), exact `R13` router (`+6.5%`), `Q4_0` fast prefill (`R61`), async ping-pong H38 prefill (`R57`), and `chunk=1024` guarded by `gpu_chunk_clamp()` (`2.14x` faster 256K cold fill).
4. **16K-256K Attention & Outer-Layer SLRU Cache:** `T<=8` single-pass `Q4_0` WMMA global attention (`23.51 / 25.58 ms` `T=6/T=8` at 256K), split-KV `Q4_0` incremental prefill (`236 ms` `inc256`), global-only `Q4_0 + FWHT-128` KV (`2,304 MiB` at 256K), and host-backed outer-layer SLRU expert cache keep filled 256K DSpark (`107.5 - 137.0 tok/s`, `+1,731 - 2,089 MiB` DXGI reserve) inside 16 GB VRAM.
5. **0-VRAM 2-Tier Shortlist + Persistent 256K SAM + Fused DSpark (`R30`, `R66 - R73`):** Inkling-2 puts all 32K leading-space (`Ġ`) words in upper BPE band `149,860..199,997`; `id_map` shortlists (`28K -> 60K` + `4K` dynamic tail), fused DSpark QKV/Markov/attn/proj (`R66`/`R73`), lossless `T_draft=0.75` sharpening (`R69`), and a persistent 2-tier 256K prompt-suffix SAM (`R71`) accelerate speculative drafting with exact output parity.
6. **Instant Disk/RAM Resume + GPU Ephemeral Stash + 4T Stack BPE (`R78 - R83`):** Windows `IoRing`/pooled `OVERLAPPED` + async pipelined H2D (`-40.4%` cold / `-61.1%` prewarmed restore), GPU `K_COPY_LIST` ephemeral stash (`3.66x`, `8.8 ms`), 4-thread lossless-split stack BPE + segment cache (`4.37x`, `3.87 ms` for `261.6K` tokens), `IE_DEFER_CKSAVE=2`, and `IE_PACE_FIRST_FAST=1`.
7. **Zero-Waste Sampling (`0.399 -> 0.005 ms`):** Fixed unpadded-vocab `topk_prefetch` cache miss + 1-launch wave32 Top-K + `O(1)` hash-chain DRY loop penalty (auto-pauses inside `<tool_call>`).

---

## <img src="docs/icons/terminal.svg" width="20" height="20" align="absmiddle" alt=""/> Quick Start (Windows & Linux)

### Windows (No System ROCm Install)
Needs Git Bash, MinGW `gcc`/`g++`, Python 3.12, and user-space ROCm wheels in `.rocm-venv`:
```bash
pip install rocm-sdk-core rocm-sdk-libraries rocm-sdk-device-gfx1201
```

```bash
# 1. Build host engine + all 310 custom gfx1201 kernels (0 Inkling-2/vision spills)
cd engine && sh build-win.sh

# 2. Optional: shrink Inkling-2 output.weight Q8_0 -> Q4_K (-231 MB VRAM)
python ../scripts/inkling2_requant.py \
  ../models/Inkling-2-Mini-Uncensored-IQ3_XXS.gguf \
  --plan '^output\.weight$=Q4_K' \
  --out ../models/Inkling-2-Mini-Uncensored-IQ3_XXS-fast.gguf

# 3. Serve OpenAI-compatible API at http://127.0.0.1:8090/v1
powershell -File serve-inkling2.ps1              # Inkling-2-Mini (96K f16 KV + DSpark + shortlist)
powershell -File serve-inkling2.ps1 -Ctx 262144  # Inkling-2-Mini (256K q4rot global KV + DSpark)
powershell -File serve-saluki.ps1                # Saluki-27B (128K q8 KV + MTP7)
```

### Linux (ROCm + Clang 18+)
```bash
cd engine && make
./build/ie-serve ../models/MODEL.gguf \
  --backend gpu --hsaco build/ie_kernels.hsaco --port 8090
```

---

## <img src="docs/icons/folder.svg" width="20" height="20" align="absmiddle" alt=""/> Repository Structure

| Path | Contents |
|---|---|
| [`engine/src/`](engine/src) | Pure C11 engine (based on [`hanw/amd.c`](https://github.com/hanw/amd.c)): GGUF v3, HIP loader, arena planner, DSpark/MTP/DFlash, disk cache, HTTP server, ViT vision |
| [`engine/kernels/`](engine/kernels) | Base `gfx1201` kernels (`hanw/amd.c`) + **217 Inkling-2** (`0/0` spills, `priv=0`) + **81 Saluki-27B** + **12 ViT** (`6` RDNA4 WMMA + `6` Qwen3.5) custom kernels |
| [`engine/core/`](engine/core) & [`engine/laws/`](engine/laws) | Formally verified indexing/quantization core (`ie_core.h`) + law checks from [`hanw/amd.c`](https://github.com/hanw/amd.c) |
| [`engine/tools/`](engine/tools) & [`engine/tests/`](engine/tests) | Per-module build scripts, `objdump` checks, CPU unit, DRY, shortlist, vision & cache tests |
| [`engine/serve-inkling2.ps1`](engine/serve-inkling2.ps1) | Production Inkling-2-Mini launcher (`chunk=1024`, Q4\_K DSpark, 0-VRAM shortlist, 0-VRAM WMMA ViT vision, auto 256K long-context preset) |
| [`engine/serve-saluki.ps1`](engine/serve-saluki.ps1) | Production Saluki-27B launcher (128K q8 KV, MTP7, ViT vision, disk prompt cache) |
| [`data/inkling2-shortlist/`](data/inkling2-shortlist) | Portable 0-VRAM 2-tier (`28K -> 60K + 4K`) Inkling-2 Band-B frequency shortlists (`112 KB` + `240 KB`) |
| [`scripts/`](scripts) | Requantizer, shortlist builder, wall-clock harness & offline HTML dashboard generator |
| [`docs/`](docs) | Live GitHub Pages dashboard ([`index.html`](docs/index.html)), 52-round JSON ledger (`R00-R52`), SVG charts & research notes |

---

<details>
<summary><img src="docs/icons/sliders.svg" width="14" height="14" align="absmiddle" alt=""/> <b>Promoted Kernel Masks & Rollback Controls</b></summary>

- **Inkling-2 Defaults:** `IE_INK_DEFAULT_MASK = 0xfe7dfc0369c3ffff`, `IE_INK_DEFAULT_MASK2 = 0x20001c7f103d36b`, `IE_INK_DEFAULT_MASK3 = 0x3` (192-bit mask, plus promoted `R53 - R87` env-gated kernels/hooks with explicit `=0` opt-outs)
  - Disable all custom Inkling kernels: `IE_INKLING_KERNELS=0`
  - Individual opt-out toggles: `IE_INK_H17_EXACT=0`, `IE_INK_R17_DS_QKV=0`, `IE_INKLING_IQ4_REPACK=0`, `IE_INK_R17_IQ4_PF64=0`, `IE_INK_ROUTER_R13=0`, `IE_INK_R17_FLUTE_PF64=0`, `IE_INKLING_Q8_REPACK=0`, `IE_SAM_PERSIST=0`, `IE_DS_SHORTLIST=0`, `IE_DS_SHORTLIST_TIER2=0`, `IE_DS_ADAP_D=0`, `IE_SAM_LOOKUP=0`, `IE_EPHEMERAL_CACHE=0`, `IE_EPHEM_FAST=0`, `IE_DISK_IORING=0`, `IE_KV_H2D_PIPE=0`, `IE_DISK_PREWARM=0`, `IE_TOK_FAST_BPE=0`, `IE_TOK_THREADS=1`, `IE_TOK_SEG_CACHE=0`, `IE_DRY_HASH=0`, `IE_DS_PROB=0`, `IE_DS_SPLIT=0`, `IE_SNAP_HOST=0`, `IE_DEFER_CKSAVE=0`, `IE_PACE_FIRST_FAST=0`
  - Long-context 128K-256K controls (auto-enabled by `serve-inkling2.ps1` at `-Ctx > 131072`): `IE_INK_GLOB_KV=q4rot` (global-only `Q4_0 + FWHT-128` KV), `IE_DS_GLOB_WIN=8192` (or `auto16k`), `IE_DS_ROPE_OTF=1` (on-the-fly FP64 Cody-Waite DSpark RoPE, auto-on at `n_ctx >= 131072`), `IE_MOE_CACHE_SLOTS=auto` (outer-layer host-backed VRAM SLRU expert cache)
  - Opt-in experiments kept off by default: `IE_DISK_LZ4=1` + `IE_DCACHE_UNSHUF=1` (v4 byte-shuffled LZ4 disk cache + GPU unshuffle), `IE_RAM_CACHE_GB=N` (OS-guarded Host-RAM Radix L2 / RAM-only mode), `IE_INKLING_Q4K_REPACK=1`, `IE_INK_R17_FLUTE_VER=1`, `IE_INK_R17_SWA_PF=1`, `IE_INKLING_GRAPH=2` (piecewise HIP graphs), `IE_DS_TREE=1` (8-node tree verify), `IE_DS_FORESPARK=1`, `IE_DS_OVERLAP=1`, `IE_MK_INKLING=1`
- **Saluki-27B Defaults:** `IE_SALUKI_KERNEL_MASK = 0x67e8de841ffffffff` (81 compiled kernels across R0-R11: `rq128`/`rq64` raw-quant WMMA, `attn_pl_r10`, `attn_long_mp_r11`, `gdn_wy_wmma_r11`, `qkn_rope_kv_r11`, `lora_b_r11`, `topk_r11`)
  - Disable all custom Saluki kernels: `IE_SALUKI_KERNELS=0`
  - KV modes: `-Kv q8` (default, 128K), `-Kv q4` (`IE_KV_Q4=1 IE_KV_ROT=1` rotated 4-bit), `-Kv f16`
- **Re-render the Interactive Dashboard:**
  ```bash
  python scripts/render_40r_dashboard.py \
    --in docs/40round-ledger.json --out docs/index.html
  ```

</details>

<details>
<summary><img src="docs/icons/help.svg" width="14" height="14" align="absmiddle" alt=""/> <b>FAQ: Upstream Credit, License, RX 9070 XT & 16GB VRAM</b></summary>

- **What is upstream (`hanw/amd.c`) vs. what was added here?**
  The base C11 engine (`amd-infer`), formally verified core (`core/ie_core.h`), Lean laws, base `gfx1201` runtime/kernels, and base `ie-serve` HTTP server are by Han Wang ([`hanw/amd.c`](https://github.com/hanw/amd.c)). This repo adds the Windows 11 WDDM port (`build-win.sh` via user-space `rocm-sdk` wheels), native raw `IQ1_S`/`IQ1_M`/`IQ2_*`/`IQ3_XXS`/`Q2_K` quant loaders, 310 custom `gfx1201` kernels (`217` Inkling-2-Mini with `0/0` spills + `81` Saluki-27B + `12` ViT including `6` RDNA4 WMMA), FLUTE SoA `IQ3_XXS` + wave-interleaved `IQ4_NL` & `Q8_0` repacks, native DSpark + 0-VRAM 2-tier shortlist + persistent 256K SAM, filled 128K-256K global `q4rot` KV + outer-layer SLRU MoE cache, 0-VRAM Inkling-2 WMMA vision, GPU ephemeral prefix-cache immunity, Windows `IoRing` + async H2D disk cache + idle pre-warming, 4-thread stack BPE, `O(1)` hash-chain DRY loop penalty, and the telemetry dashboard.
- **Why is there no `LICENSE` file in this repo?**
  Upstream [`hanw/amd.c`](https://github.com/hanw/amd.c) does not currently declare a license, so default copyright applies to the upstream code and this repo intentionally does not place an MIT/Apache license over it. If `hanw/amd.c` adds a license, this repo will adopt matching terms (or strip down to our newly written kernel/script files if requested).
- **Do I need a system ROCm install on Windows to run LLMs on an RX 9070 XT?**
  No. `engine/build-win.sh` compiles native `gfx1201` AMDGPU `.hsaco` kernels using user-space `rocm-sdk` Python wheels (`amdclang`, `ld.lld`, `hipblas.dll`) on top of standard Windows Adrenalin drivers, with no system ROCm toolkit required.
- **How do Inkling-2-Mini (26B `IQ3_XXS`, up to 256K) and Qwen3.8-27B (`IQ2-mix`, 128K) fit inside 16 GB VRAM?**
  At 64K-96K context, Inkling-2-Mini (`IQ3_XXS` MoE + `Q4_K` output head + `Q4_K` DSpark + 0-VRAM 2-tier `28K -> 60K + 4K` shortlist) runs with **3.7-3.9 GB VRAM free** using on-demand growing `f16` KV cache. For filled **128K-256K context + DSpark**, `-Ctx 262144` switches the 8 global KV layers to 72 B/head `Q4_0 + FWHT-128` (`2,304 MiB` at 256K), rings DSpark's global KV (`8K` / `auto16k`), computes DSpark RoPE on the fly (`-127.5 MiB`), and runs an outer-layer host-backed VRAM SLRU expert cache (`+1,731 - 2,089 MiB` DXGI reserve at 256K in `R87`). Saluki-27B (`Qwen3.8-27B IQ2-mix`) uses a growing `q8` KV cache (`4.85 GB` at full 128K vs `12.1 GB` FP16, `7.8 GB` VRAM free at load) plus disk-backed prefix checkpoints and zero-VRAM ViT vision.
- **Does `ie-serve` work with Open WebUI, OpenCode, OMP, Cline, or standard OpenAI SDKs?**
  Yes. `ie-serve` exposes `/v1/chat/completions`, `/v1/models`, streaming SSE, reasoning effort (`--effort`), tool calling (`--tool-temp 0`), multimodal image inputs, and `O(1)` DRY loop-penalty protection.
- **What GPU architectures are supported?**
  The custom `310`-kernel specializations target AMD RDNA4 (`gfx1201`: Radeon RX 9070 XT / RX 9070) using native `wave32` and RDNA4 WMMA instructions. Base C11/HIP kernels can be built for other `amdgcn` targets via `GPU_ARCH=...` in `engine/Makefile`.

</details>

<details>
<summary><img src="docs/icons/book.svg" width="14" height="14" align="absmiddle" alt=""/> <b>Research Papers & Open-Source Repos Behind These Kernels</b></summary>

Full round-by-round citations are clickable inside the [Interactive Dashboard](https://saloqt.github.io/rdna4-amd-infer/) and [docs/research-summary.md](docs/research-summary.md):
- **Base Engine:** [`hanw/amd.c`](https://github.com/hanw/amd.c) (Han Wang's from-scratch C11 `gfx1201` inference engine & formally verified core)
- **ROCm & RDNA4 Kernels:** `ROCm/aiter` (`fmha_gfx1201`), `ROCm/composable_kernel`, AMD RDNA4 WMMA GEMM blogs, `ROCm/clr`
- **Inference Engines:** `vllm-project/vllm`, `sgl-project/sglang` (RadixAttention, Inkling-2-Mini loop fusion), `ggml-org/llama.cpp` (PR #9702, PR #32065, `iq3s_grid.h`), `flashinfer-ai/flashinfer`, `turboderp-org/exllamav3`, `Dao-AILab/causal-conv1d`, `LMCache/LMCache`
- **Speculative Decoding & MoE Papers:** DSpark (`arXiv:2607.05147`), Leviathan et al. (`arXiv:2211.17192`), FR-Spec (`arXiv:2502.14856`), MicroSpec (`arXiv:2605.26444`), SAM Decoding (`arXiv:2411.10666`), ForeSpark (`arXiv:2611.13442`), EAGLE-2 (`arXiv:2406.16858`), SonicMoE (`arXiv:2512.14080`), FlashInfer (`arXiv:2501.01005`), Mirage MPK (`arXiv:2512.22219`)

</details>

---

<sub>Built on Windows 11 + AMD Radeon RX 9070 XT (`gfx1201`) on top of [`hanw/amd.c`](https://github.com/hanw/amd.c). Model weights are not included: bring your own GGUFs.</sub>
