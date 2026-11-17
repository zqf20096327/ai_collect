<div align="center">

# llama-modchip (v3.0)

### Unified 16 GB · 32 GB · 64 GB MaxQ Inference Engine for `Qwen3.8-Flash-Next`, `DeepSeek-V4 284B` & `Nemotron-3.5 30B`
**100% Donor-Free `MaxQ` Compression · Built-In `NextN` MTP + `Stockfish-PVS v2` · Zero-Collision `v3.0` ABI · Linux, macOS Metal, CUDA, Vulkan & Windows 11**

[![Release](https://img.shields.io/badge/release-v3.0-3fb950?style=flat-square)](RELEASE_NOTES.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-58a6ff?style=flat-square)](LICENSE)
[![Quality Gate](https://img.shields.io/badge/blind%20wiki--alt%20PPL-3.43%20(64GB)%20%C2%B7%206.86%20(284B)%20%C2%B7%20100%2F100%20(30B)-2ea043?style=flat-square)](benchmarks/QUALITY_GATE_VQ3_64.md)
[![Technical Paper PDF](https://img.shields.io/badge/PDF-v2.4%20paper%20snapshot-b31b1b?style=flat-square)](paper/llama-modchip-paper.pdf)
[![Architecture](https://img.shields.io/badge/docs-ARCHITECTURE.md-bc8cff?style=flat-square)](ARCHITECTURE.md)
[![Drafter](https://img.shields.io/badge/drafter-NextN%20MTP%20%2B%20Stockfish--PVS%20v2-d29922?style=flat-square)](speculative/ROUTECRACK_TECHNIQUES.md)
[![Submit Benchmark](https://img.shields.io/badge/leaderboard-Submit%20Your%20CPU-2ea043?style=flat-square)](https://github.com/synchopate/llama-modchip/issues/new?template=cpu_benchmark_submission.yml)

[**Quickstart (`./modchip setup`)**](#quickstart) · [**3-Tier RAM Matrix**](#the-3-tier-maxq-v30-ram-matrix) · [**Gate 4 & 4D-1 Benchmarks**](#empirical-signal-fidelity-and-end-to-end-benchmarks) · [**Engine Architecture (`v3.0`)**](#what-is-new-in-llama-modchip-v30) · [**Supported Hardware**](#supported-chips-and-processor-specific-optimizations) · [**Leaderboard**](#community-cpu-and-hybrid-leaderboard) · [**FAQ**](FAQ.md)

<table>
<tr>
<td align="center"><b>3.4325 PPL · 0.4971 KLD</b><br><sub>Qwen3.8 MaxQ-64GB (-46.6% KLD vs Competitor)</sub></td>
<td align="center"><b>26.91 GiB ≤ 28.5 GiB</b><br><sub>Qwen3.8 MaxQ-32GB Cgroup v2 Verified</sub></td>
<td align="center"><b>12.66 / 14.29 tok/s</b><br><sub>Qwen3.8 Draft-MTP CPU Decode (0 GPU)</sub></td>
<td align="center"><b>57.99 GiB (284B)</b><br><sub>DeepSeek-V4 MaxQ-v4 Donor-Free</sub></td>
<td align="center"><b>24.2–111.6 tok/s</b><br><sub>Nemotron-30B 16GB CPU/Hybrid</sub></td>
<td align="center"><b>19–38.5 ms</b><br><sub>/dev/shm Hybrid State Restore</sub></td>
<td align="center"><b>0</b><br><sub>GPUs Required</sub></td>
</tr>
</table>

</div>

---

## The 3-Tier `MaxQ v3.0` RAM Matrix

One unified `llama-modchip v3.0` binary (`GLIBC <= 2.30`, static `libstdc++` & `libgomp`, zero external OpenMP `.so` needed) automatically detects your CPU ISA (`AVX-512 VBMI/VNNI`, `AVX2`, `ARM64 NEON`, `Apple Metal`) and system RAM to run the strongest open-weights model that fits cleanly on your machine:

| System RAM Tier | Recommended Aligned Checkpoint *(+ Opt-In `Abliterated`)* | Disk Footprint (`Shards`) | Peak `VmHWM` (`-c 32768`) | Verified `v3.0` Speed (`16C Zen 5`, `0 GPU`) | Backend Compatibility |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **`64 GB` Tier**<br/>*(Flagship Default)* | **[`Qwen3.8-Flash-Next-MaxQ-64GB`](https://huggingface.co/Synchopate/Qwen3.8-Flash-Next-MaxQ-64GB-GGUF)**<br/>*(`--preset qwen38-64gb` · opt-in [`qwen38-64gb-ablit`](https://huggingface.co/Synchopate/Qwen3.8-Flash-Next-MaxQ-64GB-Abliterated-GGUF), `+0.18%` ΔPPL)* | **`53.99 GiB`** (`57,969,748,352 B`)<br/>*(`43.26` Trunk + `10.73` PLE)* | **`45.08 GiB`**<br/>*(`RssAnon = 1.81 GiB`)* | **`72.0 t/s` `pp512`**<br/>**`12.66 t/s` `tg128`** *(`93.0%` MTP)* | **100% Standard `ggml`** (`types <= 42`: CPU, Metal, CUDA, Vulkan; `v3.0` loader) |
| **`64 GB` Tier**<br/>*(`284B` Alternative)* | **[`DeepSeek-V4-Flash-0731-MaxQ-v4`](https://huggingface.co/Synchopate/DeepSeek-V4-Flash-0731-MaxQ-v4-64GB-CPU-GGUF)**<br/>*(`--preset dsv4-maxq` · `284.3B` Total / `13.2B` Active)* | **`57.99 GiB`** (`62,270,037,248 B`)<br/>*(`3` shards, `34L` ConeCollapse)* | **`58.6–59.1 GiB`**<br/>*(anonymous heap)* | **`36.1–44.4 t/s` `pp`**<br/>**`8.8–19.2+ t/s` `tg`** *(`ngram-simple`)* | **100% Standard `ggml`** (`0` custom types: CPU, Metal `27.0 t/s` M5 Max, CUDA, Vulkan) |
| **`32 GB` Tier**<br/>*(Consumer Default)* | **[`Qwen3.8-Flash-Next-MaxQ-32GB`](https://huggingface.co/Synchopate/Qwen3.8-Flash-Next-MaxQ-32GB-GGUF)**<br/>*(`--preset qwen38-32gb` · opt-in [`qwen38-32gb-ablit`](https://huggingface.co/Synchopate/Qwen3.8-Flash-Next-MaxQ-32GB-Abliterated-GGUF), `+0.32%` ΔPPL)* | **`35.71 GiB`** (`38,341,683,424 B`)<br/>*(`24.98` RAM + `10.73` lazy NVMe PLE)* | **`26.91–28.40 GiB <= 28.5 GiB`**<br/>*(Cgroup v2 `Swap=0` PASS)* | **`74.6 t/s` `pp512`**<br/>**`11.45–14.29 t/s` `tg128`** *(`draft-mtp`)* | **100% Standard `ggml`** (`types <= 42`: CPU + NVMe `mmap` demand-paged PLE) |
| **`16 GB` Tier**<br/>*(CPU-Turbo / GPU)* | **[`Nemotron-3.5-30B-A3B-VQ3-64`](https://huggingface.co/Synchopate/NVIDIA-Nemotron-3.5-30B-A3B-VQ3-64-CPU-GGUF)** *(`v3.0` CPU-Turbo)*<br/>**[`Nemotron-3.5-30B-A3B-MaxQ-16GB`](https://huggingface.co/Synchopate/NVIDIA-Nemotron-3.5-30B-A3B-MaxQ-16GB-GGUF)** *(Std `ggml`)*<br/>*(opt-in `nemotron-ablit`)* | **`13.30 / 13.39 GiB`**<br/>*(`1` file, `256K` Mamba-2+MoE)* | **`14.30–16.0 GiB`**<br/>*(`14.30 GiB <= 15.0 GiB` cgroup)* | `VQ3-64`: **`24.2–60.4 t/s`** *(`111.6` TR)*<br/>`MaxQ-16GB`: **`188.3 pp` / `15.10 t/s` `N=1` (`27.80` refactor)** | `VQ3-64`: `v3.0` (`types 44/45`)<br/>`MaxQ-16GB`: **100% Upstream `ggml`** (`llama.cpp`, Metal, CUDA, LM Studio) |

---

## Quickstart

### 1-Command Setup & Interactive Chat (Linux, macOS & Windows)

```bash
git clone https://github.com/synchopate/llama-modchip.git
cd llama-modchip
./modchip setup    # Auto-detects 16GB / 32GB / 64GB RAM + CPU ISA, verifies SHA-256, writes start_server.sh
./modchip chat     # Starts background server + SSE Gateway (:8787) and opens live streaming terminal chat
```

Or bootstrap directly on a clean Linux host without cloning manually:

```bash
curl -sL https://raw.githubusercontent.com/synchopate/llama-modchip/main/install.sh | bash
```

### Direct Portable Binary Run (`GLIBC_2.30` Linux `x86_64` `-avx512` / `-avx2`)

All 12 `v3.0` Linux `x86_64` binaries link `libstdc++`, `libgcc`, and `libgomp.a` statically (`NEEDED = [libdl.so.2, libpthread.so.0, libm.so.6, libc.so.6, ld-linux-x86-64.so.2]`, `max_glibc <= 2.30`, `0` `%zmm` instructions in `-avx2`, `0` `vdpbf16ps` in `-avx512`):

```bash
# 1. Auto-select -avx512 (Zen 4/5, Ice Lake+) or -avx2 (Haswell+, Zen 1-3, Alder/Raptor Lake) and verify SHA-256:
BIN_ISA=$(grep -q "avx512f" /proc/cpuinfo && grep -Eq "avx512_?vbmi" /proc/cpuinfo && grep -Eq "avx512_?vnni" /proc/cpuinfo && echo "avx512" || echo "avx2")
curl -fLO "https://github.com/synchopate/llama-modchip/releases/download/v3.0/llama-server-modchip-linux-x86_64-${BIN_ISA}"
curl -fLO "https://github.com/synchopate/llama-modchip/releases/download/v3.0/SHA256SUMS"
sha256sum -c SHA256SUMS --ignore-missing
chmod +x "llama-server-modchip-linux-x86_64-${BIN_ISA}"

# Non-convoy thread count: leave 1 physical core free for HTTP/OS threads paired with --poll 0 --poll-batch 0
N_CORES=$(lscpu -p=CORE,SOCKET 2>/dev/null | grep -v '^#' | sort -u | wc -l)
THREADS=$(( N_CORES > 1 ? N_CORES - 1 : 1 ))

# 2A. [64 GB Tier Default] Qwen3.8-Flash-Next-MaxQ-64GB (53.99 GiB, default --repack ON, NextN draft-mtp -> 12.66 t/s):
hf download Synchopate/Qwen3.8-Flash-Next-MaxQ-64GB-GGUF \
  --include "Qwen3.8-Flash-Next-MaxQ-64GB-*.gguf" --local-dir ./qwen38-64gb
env RC_TABLES_DIR=/nonexistent "./llama-server-modchip-linux-x86_64-${BIN_ISA}" \
  -m ./qwen38-64gb/Qwen3.8-Flash-Next-MaxQ-64GB-00001-of-00002.gguf \
  -c 32768 -np 1 -fa on -ctk q8_0 -ctv q8_0 --spec-type draft-mtp --jinja \
  -t "$THREADS" -tb "$THREADS" --poll 0 --poll-batch 0 --slot-save-path /dev/shm --port 8080

# 2B. [32 GB Tier Default] Qwen3.8-Flash-Next-MaxQ-32GB (24.98 GiB Shard 1 + lazy NVMe PLE -> 26.9 GiB RSS, 11.45-14.29 t/s):
hf download Synchopate/Qwen3.8-Flash-Next-MaxQ-32GB-GGUF \
  --include "Qwen3.8-Flash-Next-MaxQ-32GB-*.gguf" --local-dir ./qwen38-32gb
env RC_TABLES_DIR=/nonexistent "./llama-server-modchip-linux-x86_64-${BIN_ISA}" \
  -m ./qwen38-32gb/Qwen3.8-Flash-Next-MaxQ-32GB-00001-of-00002.gguf \
  -c 32768 -np 1 -fa on -ctk q8_0 -ctv q8_0 --spec-type draft-mtp --jinja --ctx-checkpoints 0 \
  --temp 0.6 --top-p 0.95 --top-k 20 --presence-penalty 0.2 --repeat-penalty 1.05 \
  -t "$THREADS" -tb "$THREADS" --poll 0 --poll-batch 0 --slot-save-path /dev/shm --port 8080

# 2C. [16 GB Tier] NVIDIA-Nemotron-3.5-30B-A3B-VQ3-64 (v3.0 CPU-Turbo) or MaxQ-16GB (100% standard ggml):
# ./install.sh --preset nemotron-vq3         # 13.30 GiB v3.0 CPU-Turbo (AVX-512 VBMI)
# ./install.sh --preset nemotron-maxq-16gb   # 13.39 GiB 100% standard ggml (CPU / Metal / CUDA / LM Studio)
```

> [!IMPORTANT]
> **Critical Runtime Best Practices (`v3.0`):**
> - **Non-Convoy Threading (`-t $((N_CORES - 1)) -tb $((N_CORES - 1)) --poll 0 --poll-batch 0`):** Leaving 1 core free for HTTP/OS dispatch and disabling busy-polling eliminates thread-pool barrier convoys (`+25.9%` `pp512`, `+31.3%` `tg128` over oversubscribed `-t N --poll 50`). `./modchip` configures this automatically.
> - **Vocabulary Isolation (`RC_TABLES_DIR=/nonexistent` on Non-Nemotron Models):** When serving `Qwen3.8` (`248K` vocab) or `DeepSeek-V4` (`129K` vocab) from a working directory containing `./workspace/routecrack` Nemotron tables, always set `RC_TABLES_DIR=/nonexistent` (not merely unset) so `Stockfish-PVS v2` runs in clean online `248K` session mode. `./modchip` enforces this automatically.
> - **Default `--repack` ON (`v3.0`) vs. Unpatched Upstream `llama.cpp`:** `llama-modchip v3.0` fixes upstream `CPU_REPACK` `q8_cache` / `repack.cpp` bugs while preserving zero-copy `mmap` on 3D MoE tensors (`RssAnon = 1.81–1.92 GiB`, `93.0%` MTP accept on `MaxQ-64GB`). Users loading `Qwen3.8` GGUFs on **unpatched upstream `llama.cpp`** should pass `--no-repack` (`-nr`); `--no-repack` is **not** needed on `llama-modchip v3.0`.
> - **`MaxQ-32GB` Anti-Repetition Sampling & `<think>` Token Budgets:** At `1.63 bpw`, `MaxQ-32GB` and `MaxQ-32GB-Abliterated` must be run with `temperature=0.6`, `top_p=0.95`, `top_k=20`, `presence_penalty=0.2`–`1.0`, `repeat_penalty=1.05` (`4 / 4 = 100%` loop-free on Blind-4 vs. greedy `temp=0` tail loops on `3 / 16` `32GB-Abliterated` and `1 / 16` `64GB-Abliterated` 512-tok dual-use outputs; `./modchip` passes these flags automatically on 32 GB presets). Whenever `enable_thinking=True`, set **`max_tokens >= 16384` on `Qwen3.8`** and **`max_tokens >= 4096` on `Nemotron-3.5`** (whose default Jinja template enables `<think>...</think>` unless `enable_thinking: false` / `--reasoning-budget 0` is passed).

> [!CAUTION]
> **Responsible-Use Disclaimer & Edition Positioning (Opt-In `*-ablit` Presets):** Optional abliterated checkpoints (`qwen38-64gb-ablit`, `qwen38-32gb-ablit`, `nemotron-ablit`) attenuate refusal-mediating activation subspaces via orthogonal projection (`56.25% -> 18.75%` held-out dual-use refusals at `+0.18%` ΔPPL on `qwen38-64gb-ablit`; `43.75% -> 12.50%` at `+0.32%` ΔPPL on `qwen38-32gb-ablit`; `0 / 4` `<think>` spot refusals on both under KL-safe rank-2 editing). Upstream safety refusal filters cannot be relied upon for moderation, and `./install.sh` never selects `*-ablit` presets without explicit `[y/N]` confirmation (or `--accept-abliterated` in `--yes` mode). Use **Aligned `qwen38-64gb`** as the default pure coding flagship (`4 / 4` Blind-4 pass vs. `2 / 4` on `qwen38-64gb-ablit`), and reserve `*-ablit` strictly for authorized security research, reverse engineering, red-team auditing, CTF, code auditing, and uncensored legal/policy analysis.

| `./modchip` Command | Description |
| :--- | :--- |
| **`./modchip setup`** | Auto-detects RAM tier (`16 / 32 / 64 GB`) & CPU ISA, installs `v3.0` engine + SHA-256 verified GGUF |
| **`./modchip download-bin`** | Installs portable `GLIBC_2.30` Linux `x86_64` `-avx512` or `-avx2` `v3.0` binary |
| **`./modchip start` / `stop`** | Starts or stops background `llama-server` (`:8789`) + Agentic SSE Gateway (`:8787`) |
| **`./modchip chat`** | Interactive terminal chat with live `tok/s`, TTFT, and `Draft-MTP` / `Stockfish-PVS` telemetry |
| **`./modchip web`** | Opens the Dark-Mode Web Chat & Live Telemetry HUD (`http://127.0.0.1:8787`) |
| **`./modchip bench`** | Runs a 2-stage C++20 + Refactor benchmark and prints a shareable CPU Scorecard |
| **`./modchip claude`** | Launches Claude Code CLI wired to the local engine with `/dev/shm` Slot-0 warm restore |
| **`./modchip eval` / `status`** | Runs the 100-point Functional Gate or inspects CPU readiness, `2MB THP`, and `/dev/shm` IPC |

---

## Empirical Signal Fidelity and End-to-End Benchmarks

### 1. `Qwen3.8-Flash-Next` (`MaxQ-64GB` & `MaxQ-32GB`) — Blind `wiki-alt.txt` PPL + KLD & Competitor Audit

Evaluated on `40 x 512` blind `wiki-alt.txt` chunks (`0.000000%` 8-gram and 13-gram overlap with calibration corpora) against the donor-free `BF16` reference logit base (`Mean PPL(base) = 2.776624 ± 0.054868`):

| Checkpoint | Exact LLM Bytes (`GiB`) | Trunk + PLE (`GiB`) | Built-In MTP | `Mean PPL(Q) ± SE` | `Mean KLD ± SE` | `Median KLD` | `Same top p (%)` | Peak `VmHWM` (`-c 32768`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`MaxQ-64GB`** *(`v3.0` Flagship)* | **`57,969,748,352 B`** (`53.99 GiB`) | `43.26 + 10.73` (`512/512` exps) | **Yes (`blk.48`)** | **`3.4325 ± 0.0708`** *(`3.4383` repack)* | **`0.4971 ± 0.0099`** | **`0.1060`** | **`78.314 ± 0.408%`** | **`45.08 GiB`** *(`< 60.0 GiB` cgroup)* |
| **`MaxQ-64GB-Abliterated`** *(Opt-In)* | **`57,969,748,352 B`** (`53.99 GiB`) | `43.26 + 10.73` (`135` edited) | **Yes (`blk.48`)** | **`3.4444 ± 0.0718`** *(`+0.18%` / `+0.1784%` ΔPPL)* | **`0.4982 ± 0.0100`** | **`0.1067`** | **`78.275 ± 0.408%`** | **`46.34 GiB`** *(`RssAnon = 2.31 GiB`)* |
| `ISTA-DASLab GSQ-RCO-Coder-IQ1_M` | `58,408,584,928 B` (`54.40 GiB`) | `27.58 + 26.82` (`256/512` pruned) | No | `5.0916 ± 0.1214` | `0.9302 ± 0.0156` | `0.2964` | `69.382 ± 0.456%` | `38.55 GiB` (`--no-repack`) |
| **`MaxQ-32GB`** *(`v3.0` 32GB Default)* | **`38,341,683,424 B`** (`35.71 GiB`) | **`24.98 + 10.73`** (`512/512` exps) | **Yes (`blk.48`)** | **`5.8120 ± 0.1402`** *(`5.8041` repack)* | **`1.0069 ± 0.0149`** | **`0.3986`** | **`66.275 ± 0.468%`** | **`26.91–27.44 GiB <= 28.5 GiB`** |
| **`MaxQ-32GB-Abliterated`** *(Opt-In)* | **`38,341,683,424 B`** (`35.71 GiB`) | **`24.98 + 10.73`** (`177` edited) | **Yes (`blk.48`)** | **`5.8226 ± 0.1401`** *(`+0.32%` / `+0.3189%` ΔPPL)* | **`1.0169 ± 0.0152`** | **`0.3988`** | **`65.539 ± 0.471%`** | **`28.40 GiB <= 28.5 GiB`** |

- **64 GB Head-to-Head (`~54 GiB` Class):** Despite being **`0.41 GiB` smaller** AND embedding the `0.81 GiB` `blk.48` NextN MTP module, **`MaxQ-64GB` outperforms `ISTA-DASLab GSQ-RCO-Coder-IQ1_M` by `-1.6591` PPL** (`3.53x` smaller PPL degradation over `BF16`: `+0.6559` vs `+2.3150`), **`-46.6%` lower Mean KLD**, **`-64.3%` lower Median KLD**, and **`+8.93 pp` higher Top-1 agreement**. Compressing the `320M`-row PLE table from `26.82 GiB` (`IQ4_NL`) to `10.73 GiB` (`PCA-Wiener D=256 + RaBitQ Q1_0`) freed `+16.09 GiB` directly into `512/512` unpruned experts, `FP64 Woodbury DualGram Q2_0`, and built-in MTP.
- **32 GB Consumer Exclusivity (`18`-Checkpoint Hugging Face Audit):** Across all `18` published `Unsloth` and `ISTA-DASLab` `Qwen3.8-Flash-Next` GGUFs (`54.40 GiB` to `329.72 GiB`), **`0 / 18` fit inside a 32 GB host (`<= 28.5 GiB`)** and only **`1 / 18` fits inside 64 GB (`<= 55.5 GiB`)**. `MaxQ-32GB` keeps its `24.98 GiB` Shard 1 resident in RAM while demand-paging the `10.73 GiB` Shard 2 PLE table via `mmap`, passing strict Linux Cgroup v2 enforcement (`memory.max = 28.5 GiB`, `MemorySwapMax = 0`, `oom_kill = 0`).
- **100% Donor-Free Rank-2 Subspace-Abliterated Twins (`qwen38-64gb-ablit` & `qwen38-32gb-ablit`):** Single-pass fused rank-2 contrastive projection + `FP64 Woodbury DualGram` across `blk.4..48` (`blk.0..3` & `token_embd` spared; `0.000000%` 8/13-gram overlap across all `32/32` checks) reduces held-out dual-use security refusals **`56.25% -> 18.75%`** on `64GB` (`ΔPPL = +0.1784%`, token-weighted top-4 `tg512` MTP accept **`78.08%`**, `p512` `10.29 t/s`) and **`43.75% -> 12.50%`** on `32GB` (`ΔPPL = +0.3189%`, top-4 `tg512` MTP accept **`76.22%`**, `p512` `77.53 pp` / `11.65 t/s` mean / `12.73 t/s` cold `rep 0`), with **`0 / 4` `<think>` spot refusals** on both (vs. `2 / 4` on both Aligned checkpoints counting Unicode `I can’t` `\u2019` on `ref_01`).

<details>
<summary><b>Pinned <code>v3.0</code> Fleet GGUF <code>SHA-256</code> Checksums (`./modchip checksums`)</b></summary>
<br/>

```text
# 32 GB & 64 GB Tiers — Qwen3.8-Flash-Next-MaxQ (v3.0)
f2b8bc79acb4b4d79033acd91c9c360ba96da92cd5841512befc450e15f4786f  Qwen3.8-Flash-Next-MaxQ-64GB-00001-of-00002.gguf (46,449,692,736 B)
384bc936bdad75383c03e87184056e1cb0b037b0e3f5d5ae5273fd46f55150aa  Qwen3.8-Flash-Next-MaxQ-64GB-Abliterated-00001-of-00002.gguf (46,449,692,736 B)
06cb65f9cf6e510cd16500ca1719701a0ffa13dcaa4c4d0cc135e4f2071a8b4d  Qwen3.8-Flash-Next-MaxQ-32GB-00001-of-00002.gguf (26,821,627,808 B)
6e8ae62c37bc08de1a69e9e78ab9bae0262f87ffe543595206d1c3b3a810fd67  Qwen3.8-Flash-Next-MaxQ-32GB-Abliterated-00001-of-00002.gguf (26,821,627,808 B)
86b79714867743ddf5911ee7dff2717ae275f870551d86469cbdbf026c6b552e  Qwen3.8-Flash-Next-MaxQ-{64GB,32GB}[-Abliterated]-00002-of-00002.gguf (11,520,055,616 B)
ef2af1d6aa8a22740c7252bc7ce40c5c2f1249aa8d9c8499a4d4572c3cfdf9df  mmproj-Qwen3.8-Flash-Next-BF16.gguf (907,542,880 B)

# 64 GB Tier — DeepSeek-V4-Flash-0731-MaxQ-v4 (284B · v3.0)
6112e887b21d1fdf7b7196232b528698a6ec2d5a59760a040cb4231f8e8d691b  DeepSeek-V4-Flash-0731-MaxQ-v4-00001-of-00003.gguf (5,258,336 B)
5d85c740992b70395da5c3e4a856b3fad6ef725271722c8d837b35befe28330d  DeepSeek-V4-Flash-0731-MaxQ-v4-00002-of-00003.gguf (35,543,586,816 B)
a8654d4d5fedf748d6f2b6404a8b7f9e19435a8aa8e2bb97ce9a66bc012c0f3a  DeepSeek-V4-Flash-0731-MaxQ-v4-00003-of-00003.gguf (26,721,192,096 B)

# 16 GB Tier — NVIDIA-Nemotron-3.5-30B-A3B (v3.0)
26b884d70a52046a7198c4e01cac397af8bf44584b04cdcf59f896145587db67  NVIDIA-Nemotron-3.5-30B-A3B-MaxQ-16GB.gguf (14,382,336,640 B · 100% std ggml)
04a460cdd831002d80b2f47ec5d70e7a92227abcf0a57f31ad73fe0bd50e711f  NVIDIA-Nemotron-3.5-30B-A3B-VQ3-64.gguf (14,282,559,040 B · v3.0 types 44/45)
3a3a09eac29b5906397ca6a93d2ff0f566fca0bdd365294d067aeb5d0ebf4a1b  NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf (15,420,034,624 B · v3.0 type 44)
75da8372f3896bfacd103f3cb85bf22b729d39cb1efce82fb3c838ab2af53e57  NVIDIA-Nemotron-3.5-30B-A3B-Abliterated-VQ3-64.gguf (14,282,559,488 B · v3.0 types 44/45)
```

</details>

### 2. `llama-modchip v3.0` Engine Speedup, `248K` Speculative Shootout & `/dev/shm` Hybrid Restore

Measured on 16 Zen 5 cores (`taskset -c 16-31`, `mmap` enabled, default `--repack` ON, `RC_TABLES_DIR=/nonexistent`):

| Edition & Speculative Mode | Stage 4C Baseline (`-t 16 --poll 50 -nr`) | **`llama-modchip v3.0` (`-t 15 -tb 15 --poll 0`, `--repack` ON)¹** | Combined Gain¹ | Speculative Acceptance | Peak `VmHWM` (`RssAnon`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`MaxQ-64GB` — Pure `N=1` (`none`)** | `42.17 pp` / `4.69 t/s tg` | **`72.18 t/s pp512`** / **`6.37 t/s tg128`** | **`+71.2% pp` / `+35.7% tg`** | — | `44.9 GiB` (`0.55 GiB`) |
| **`MaxQ-64GB` — Built-In `draft-mtp` (Default)** | `39.24 pp` / `7.33 t/s tg` *(`2.56` broken repack)* | **`71.97 t/s pp512`** / **`12.66 t/s tg128`** *(peak `12.82`)* | **`+83.4% pp` / `+72.8% tg`** *(`1.99x` over `none`)* | **`93.00%`** (`279/300`) | **`45.08 GiB`** (`1.81 GiB`) |
| **`MaxQ-64GB` — `Stockfish-PVS v2` (`inplace_edit` cold `rep 0`)²** | — | **`75.2 t/s pp`** / **`10.58 t/s tg128`** *(vs `12.99` `draft-mtp`)* | **`1.67x` over `none`** | **`91.25%`** (cold) | `44.23 GiB` (`-0.85 GiB`) |
| **`MaxQ-32GB` — Pure `N=1` (`none`)** | `68.66 pp` / `6.08 t/s tg` | **`82.11 t/s pp512`** / **`6.67 t/s tg128`** | **`+19.6% pp` / `+9.7% tg`** | — | `26.3 GiB` (`0.69 GiB`) |
| **`MaxQ-32GB` — Built-In `draft-mtp` (Default)** | `61.39 pp` / `9.46 t/s tg` *(`8.39` pre-`v3.0` repack)* | **`74.55 t/s pp512`** / **`11.45 t/s tg128`** *(`14.29` `inplace_edit`)* | **`+21.5% pp` / `+21.1% tg`** *(`1.72x` over `none`)* | **`73.73%–100.0%`** | **`26.91 GiB`** (`1.92 GiB`) |
| **`MaxQ-32GB` — `Stockfish-PVS v2` (`inplace_edit` cold `rep 0`)²** | — | **`78.03 t/s pp`** / **`12.82 t/s tg128`** *(vs `13.76` `draft-mtp`)* | **`1.87x` over `none`** *(`+11.0%` faster `pp`)* | **`91.25%`** (cold) | `26.38 GiB` (`-0.53 GiB`) |

*(¹ **Transparent Speedup Attribution:** Stage 4C ran oversubscribed `-t 16 --poll 50 --no-repack` on 16 logical CPUs, whereas Stage 4D-1 ran `-t 15 -tb 15 --poll 0 --poll-batch 0` with `v3.0` default `--repack` ON. The `+72.8%` [`MaxQ-64GB`] and `+21.1%` [`MaxQ-32GB`] decode gains reflect the **combined** `llama-modchip v3.0` SIMD/GDN/repack engine optimizations plus non-convoy `-t <N-1> --poll 0` scheduling [`step0` isolated `-t 15 --poll 0` at `+25.9% pp / +31.3% tg` on `32GB none`].)*  
*(² **Speculative Shootout Note:** Built-in `draft-mtp` won cold single-turn `rep 0` `tg128` on **`6 / 6` (`100%`)** of `(edition, prompt)` pairs and is the default for `Qwen3.8`. Zero-weight `Stockfish-PVS v2 / RouteCrack` [`--spec-type ngram-simple --spec-ngram-simple-size-n 3 --spec-ngram-simple-size-m 3 --spec-ngram-simple-min-hits 1`] achieved `10.58–12.82 t/s` [`1.67x–1.87x`] on cold `rep 0` source-in-context refactoring with faster prefill and lower RAM, making it the recommended fallback for MTP-less checkpoints or iterative multi-turn edit loops. Opt-in `LLAMA_MOE_TOP_K=8` adds `+5.7% tg / +8.5% pp` on `MaxQ-32GB` at a `+0.41` 40-chunk PPL cost, so unpruned `TOP_K=10` remains strictly default.)*  
*(³ **`/dev/shm` Hybrid State Snapshot:** Saving and restoring a 512-token `Qwen3.8` Slot-0 hybrid state [`233.14 MiB` = `36` GDN `[48x128x128]` FP32 + `12` QSA `Q8_0` KV + 1 HARP checkpoint] completes in **`38.49 ms` avg (`38.16 ms` min, `6.11 GiB/s`, `162x` faster than `6.18s` prefill; `~19 ms` / `120.6 MiB` with `--ctx-checkpoints 0`)** with 100% bit-exact greedy continuation [`SHA256 = 8e5a6444...`].)*

### 3. `DeepSeek-V4-Flash 284B` (`64 GB` Tier) & `NVIDIA-Nemotron-3.5-30B-A3B` (`16 GB` Tier)

Full quality gate breakdowns, `ref5632.kld` 51-chunk / 49-chunk blind logs, and `BF16` SQNR tables are preserved in **[`benchmarks/QUALITY_GATE_VQ3_64.md`](benchmarks/QUALITY_GATE_VQ3_64.md)**, **[`docs/DEEPSEEK_V4_OPTIMIZATIONS.md`](docs/DEEPSEEK_V4_OPTIMIZATIONS.md)**, and **[`docs/NEMOTRON_OPTIMIZATIONS.md`](docs/NEMOTRON_OPTIMIZATIONS.md)**:

- **`DeepSeek-V4-Flash-0731-MaxQ-v4` (`57.99 GiB`, `284.33B` Total / `13.17B` Active, `0` custom tensor types):** `AtomicChat wiki-alt.txt` `51`-chunk `ref5632.kld` **`Mean PPL(Q) = 6.8592 ± 0.0482`** (`6.8471` on unseen chunks `3..51`), **`Mean KLD = 0.64851 ± 0.00354 nats`**, **`Median KLD = 0.18382`**, **`Same top p = 73.283%`** (vs `PPL(base) = 4.3310`); `36.1–44.4 tok/s` prefill and `8.8–19.2+ tok/s` `Stockfish-PVS` decode on 16C Zen 5 CPU (`27.0 tok/s` `tg128` / `169.4 tok/s` `pp512` on `64 GB` Apple M5 Max Metal).
- **`NVIDIA-Nemotron-3.5-30B-A3B` (`13.30 GiB` `VQ3-64` `v3.0` CPU-Turbo & `13.39 GiB` `MaxQ-16GB` 100% Standard `ggml`):** Across `40 × 512` blind `wiki-alt.txt` chunks (vs. `16.07 GiB` donor-free `MXFP4` ref `PPL = 6.596`), `Fractal-64` (`14.36 GiB`, `type 44`) achieves **`PPL = 6.653`** (`Mean KLD = 0.0688`), **`VQ3-64` (`13.30 GiB`, `types 44/45` — highest-accuracy `16 GB` CPU-Turbo flagship)** achieves **`PPL = 6.761`** (`Mean KLD = 0.0871`, `WikiText-2 PPL = 7.4400` vs `BF16` `6.9582`, **`100.0 / 100.0`** Gate at **`24.18–26.08 tok/s` Served Gate** / **`40.9–60.4 tok/s` `M=7` bursts** on 16C Zen 5, `111.62 tok/s` on Threadripper PRO 7985WX), and donor-free **`MaxQ-16GB` (`14,382,336,640 B` = `13.39 GiB`, `max_type = 42`, `0` custom types — universal stock `llama.cpp`/Metal/CUDA/LM Studio edition)** achieves **`PPL = 7.313 ± 0.192`** (`Mean KLD = 0.1722`, `Median KLD = 0.0698`, `Same top p = 83.43%`), passing strict Linux Cgroup v2 `15.0 GiB` enforcement (`MemoryMax = 15.0G`, `Swap = 0`, `VmHWM = 14.3040 GiB <= 15.0 GiB` at `-c 32768`) at **`188.29 tok/s` `pp512` / `15.10 tok/s` `tg128` pure `N=1`** and **`27.80 tok/s` (`94.44%` accept) on `MiniLRU` code refactoring** (`merge_intervals` + native OpenAI tool-call synthesis `PASS`).

---

## What Is New in `llama-modchip v3.0`

1. **Zero-Collision Custom Tensor Type IDs (`44` & `45`) + Single Unified Patch ([`patches/llama-modchip-v3.0.patch`](patches/llama-modchip-v3.0.patch)):**
   - Upstream `GGML_TYPE_Q2_0 = 42` (`18 B / 64 W` = `2.25 bpw`, `QK2_0 = 64`, used by `Qwen3.8` signed-scale `Q2_0` and `Nemotron MaxQ-16GB`) and `GGML_TYPE_F8_E4M3 = 43` remain **100% untouched**.
   - `Fractal-64` (`30 B / 64 W = 3.75 bpw`) moves cleanly to `GGML_TYPE_FRACTAL_64 = 44` (CPU AVX-512/AVX2/NEON + Apple Metal GPU) and `LUT-VQ3-64` (`24 B / 64 W = 3.00 bpw`, 128-entry 3D spherical codebook in `ggml/src/vq3_codebook.h`) moves to `GGML_TYPE_VQ3_64 = 45` (AVX-512 VBMI `VPERMI2B` + AVX2/NEON/scalar).
   - One binary (`de32b268c` + `llama-modchip-v3.0.patch`) natively runs `qwen4exp`, `deepseek4`, `nemotron_h_moe`, and `qwen35moe`.
2. **512-Bit `Q1_0`/`Q2_0`/`MXFP4` SIMD Kernels, Multi-Threaded `GATED_DELTA_NET` & Zero-Copy 3D MoE `--repack`:**
   - Dedicated AVX-512 VNNI/BW kernels for `Q1_0 (41)` (`RaBitQ` PLE), signed-scale `Q2_0 (42)`, overflow-free `Q8_0`, and `MXFP4`, plus fused 8-`zmm` FMA multi-threaded `GATED_DELTA_NET` (`36` layers, inner barrier eliminated) and dynamic `4*nth` `FLASH_ATTN_EXT` prefill load balancing.
   - Fixes upstream `q8_cache` / `params->wdata` aliasing in `tiled.cpp` and `repack.cpp` while keeping 3D MoE tensors (`ne[2] >= 64`) zero-copy `mmap`-backed under default `--repack` and aligning `MADV_HUGEPAGE` inward to `2 MiB` boundaries so lazy PLE pages are never pre-faulted.
3. **248K-Vocab `Stockfish-PVS v2` + Built-In `NextN` MTP Coexistence:**
   - Widens all `RouteCrack` / `StockfishDrafter` / `Trie` token IDs to full 32-bit `llama_token` (`n_vocab = 248,320` safe) while defaulting `Qwen3.8` to built-in `blk.48` `--spec-type draft-mtp`.

---

## Supported Chips and Processor-Specific Optimizations

Microarchitectural details and tuning flags are documented in **[`docs/HARDWARE_OPTIMIZATIONS.md`](docs/HARDWARE_OPTIMIZATIONS.md)**:

| Processor / Platform | Verified Hardware | Hardware-Specific Optimizations Active | Platform Guide & Scripts |
| :--- | :--- | :--- | :---: |
| **AMD Zen 5 (`Desktop / Mobile / Server`)** | `Ryzen 9 9955HX`, `9950X`, `Ryzen 7 9800X3D`, `EPYC 9005 Turin` | • Single-cycle 512-bit **AVX-512 (`VPDPBUSD`, `VBMI VPERMI2B`, 8-`zmm` GDN)**<br/>• **Zero-copy 3D MoE `--repack` + `2MB` THP (`MADV_HUGEPAGE`)** + `_MM_HINT_NTA` L3 isolation | **[Hardware Guide §2.1](docs/HARDWARE_OPTIMIZATIONS.md)**<br/>[`install.sh`](install.sh) |
| **AMD Zen 4 Multi-CCD (`Threadripper / EPYC`)** | `Threadripper PRO 7985WX` (`64C/128T`, `8 CCDs`, `256 MB` L3) | • **Dynamic sysfs L3 CCD Topology Discovery** ([`scripts/llama_modchip.py`](scripts/llama_modchip.py))<br/>• **Deterministic `4C/CCD` Stride (`-t 32`)**: avoids Infinity Fabric saturation (`111.6 tok/s`) | **[Hardware Guide §2.2](docs/HARDWARE_OPTIMIZATIONS.md)**<br/>[Issue #1](https://github.com/synchopate/llama-modchip/issues/1) |
| **AMD 3D V-Cache + Radeon Vulkan Hybrid** | `Ryzen 9 7945HX3D` (`128 MB` L3) + `RX 9070 XT 16GB` (`RADV`) | • **Tensor-Role Splitting (`-ngl 99 --n-cpu-moe N`)**<br/>• Native **Vulkan `SSM_SCAN` + `MXFP4` GPU Shaders** (`80.8 tok/s` at 256K) | **[Hardware Guide §2.3](docs/HARDWARE_OPTIMIZATIONS.md)**<br/>[`FAQ.md`](FAQ.md) |
| **Intel / AMD + NVIDIA RTX (`Windows 10/11`)** | `Ryzen 7 9800X3D` (`1M` ctx), `Core i9-9900K / 14900K` + `RTX 2080 Ti / 3090 / 4090` | • **Unified `v3.0` MinGW-w64 & MSVC+CUDA Builder** ([`windows/build_patched_engine.ps1`](windows/build_patched_engine.ps1))<br/>• **Live-VRAM `--n-cpu-moe` Solver (`550 MB` WDDM Reserve)** | **[Windows Port](docs/WINDOWS_PORT.md)**<br/>[`windows/`](windows/README.md) |
| **Apple Silicon (`M1 / M2 / M3 / M4 / M5`)** | `M5 Max` (`64 GB`), `M4 Max` (`64/36 GB`), `M4 Pro` (`24 GB`), `M3 Max`, `M1 Max` | • **Unified `v3.0` Metal + ARM64 NEON `SDOT` Engine** ([`apple-silicon/build-dsv4-engine.sh`](apple-silicon/build-dsv4-engine.sh))<br/>• `27.0 tok/s` `DeepSeek-V4 284B` on M5 Max (`0` swapouts); `78.6 tok/s` `30B` on M3 Max | **[Apple Silicon Guide](apple-silicon/README.md)**<br/>[`dsv4-m5max.md`](apple-silicon/results/dsv4-m5max.md) |
| **ARM64 Cloud & Mini-PC (`Graviton / Fedora`)** | `AWS Graviton3 m7g.2xlarge`, `Ryzen 7 8745HS` (`GEEKOM A8`) | • **ARMv8.4-A `SDOT` (`44.97 tok/s`)** & Fedora 44 CPU/Vulkan workflow | **[Fedora Guide](fedora/README.md)**<br/>[Issue #2](https://github.com/synchopate/llama-modchip/issues/2) |

### Hardware Readiness Check (Zero Model Download Required)

```bash
curl -sL https://raw.githubusercontent.com/synchopate/llama-modchip/main/scripts/check_cpu_readiness.py | python3
```

---

## Community CPU and Hybrid Leaderboard

Run **`./modchip bench`** (or **`windows\BENCHMARK_PC.bat`** on Windows) and **[Submit Your Scorecard (GitHub Issue)](https://github.com/synchopate/llama-modchip/issues/new?template=cpu_benchmark_submission.yml)**:

| Hardware Platform (`CPU / SoC / Hybrid`) | Cores / Cache | Memory | Prefill (`tok/s`) | Decode — Prose / C++20 | Decode — Speculative / Burst | Config & Contributor |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`Qwen3.8-MaxQ-64GB` on Zen 5 (`v3.0`)** | `16C` (`-t 15 --poll 0`, `AVX-512`) | `64 GB` Tier (`45.08 GiB` RSS, `0 GPU`) | **`71.97 – 75.58`** | **`6.37 tok/s`** *(pure `N=1`)* | **`12.66 avg / 12.99 peak tok/s`** *(`93.0%` `draft-mtp`)* | `@synchopate` (`v3.0` Gate 4D-1) |
| **`Qwen3.8-MaxQ-32GB` on Zen 5 (`v3.0`)** | `16C` (`-t 15 --poll 0`, `AVX-512`) | `32 GB` Tier (`26.91 GiB <= 28.5 GiB`, `0 GPU`) | **`74.55 – 86.14`** | **`6.67 tok/s`** *(pure `N=1`)* | **`11.45 – 14.29 tok/s`** *(`draft-mtp`, `14.77` peak)* | `@synchopate` (`v3.0` Gate 4D-1) |
| **AMD Threadripper PRO 7985WX (`Zen 4`)** | `64C/128T` (`8 CCDs`, `256 MB` L3) | `256 GB` 8-Ch DDR5-6000 (`0 GPU`) | **`386.00`** *(`-t 32`)* | **`73.84 – 80.14 tok/s`** | **`111.62 tok/s` warm** / **`80.14` cold** *(`-t 32` 4C/CCD)* | `@aifartist` ([Issue #1](https://github.com/synchopate/llama-modchip/issues/1#issuecomment-6595559921)) |
| **AMD Ryzen Threadripper 9960X (`Zen 5`)** | `24C/48T` (`4 CCDs`, `AVX-512 VBMI`) | `125 GB` 4-Ch DDR5 (`14.91 GiB` RSS, `2MB THP: 4.45 GiB`, `0 GPU`) | **`450.36`** *(`-t 24`)* | **`49.25 tok/s`** *(`TTFT 254 ms`)* | **`54.43 tok/s`** *(`73.8%` Stockfish-PVS, `VQ3-64`)* | `@pedrosousabarreto` ([Issue #40](https://github.com/synchopate/llama-modchip/issues/40#issuecomment-6916491282)) |
| **AMD Ryzen 9 7945HX3D + RX 9070 XT (`Hybrid`)** | `16C/32T` (`128 MB` 3D V-Cache) + `16 GB` Vulkan | `94 GB` DDR5 + `16 GB` VRAM | **`563.00`** *(256K ctx)* | **`75.10 tok/s`** *(`MXFP4` 15.2GB)* | **`80.80 tok/s`** *(Vulkan `SSM_SCAN` + `MXFP4` MoE)* | `Community (RADV/Vulkan)` ([`FAQ.md`](FAQ.md)) |
| **AMD Ryzen 9 9955HX (`Zen 5` · `Nemotron 30B`)** | `16C/32T` (`2 CCDs`, `64 MB` L3) | `64 GB` DDR5 (`0 GPU`) | **`241.0`** *(Peak **`306.8`**)* | **`24.18 – 26.08 tok/s`** *(Served Gate)* | **`48.39 avg / 60.40 peak`** *(`M=7`, `len 6.90`)* | `@synchopate` ([`docs/NEMOTRON_OPTIMIZATIONS.md`](docs/NEMOTRON_OPTIMIZATIONS.md)) |
| **Apple M3 Max (`Metal` · `Fractal-64` Fast-Decode)** | `ARM64 NEON` + `Metal` | `Unified` (`Metal`) | *Metal* | **`78.60 tok/s`** *(`tg128`)* | **`78.60+ tok/s`** *(Register-tiled Metal)* | `@austindixson` ([PR #24](https://github.com/synchopate/llama-modchip/pull/24)) |
| **Apple M4 Max (`14C+32C Metal` · `Q4_0` / `Fractal`)** | `ARM64 NEON` + `Metal` | `36 GB` LPDDR5X-8533 (`Unified`) | **`860.13`** *(`1,040` `pp512`)* | **`71.60 – 77.23 tok/s`** | **`71.31 – 77.95 tok/s`** *(Gate `100/100`)* | `@khairullinr` ([Issue #16](https://github.com/synchopate/llama-modchip/issues/16)) |
| **Apple M5 Max (`DeepSeek-V4 284B` · `64 GB`)** | `18C CPU` + `40C Metal` | `64 GB` LPDDR5X (`286.5 GB/s` BW) | **`169.40`** *(`pp512`)* | **`27.00 tok/s`** *(`llama-bench` `tg128`)* | **`20.70 – 23.60 tok/s`** *(`llama-server`, `0` swapouts)* | `@notactuallytreyanastasio` ([`dsv4-m5max.md`](apple-silicon/results/dsv4-m5max.md)) |
| **Apple M4 Max (`16C CPU + 40C GPU`)** | `16C` + `40C Metal` | `64 GB` LPDDR5X-8533 | **`~451.0`** | **`49.2 – 57.7 tok/s`** | **`70.9 – 120.0 tok/s`** | `@jbeckman1974` ([Issue #8](https://github.com/synchopate/llama-modchip/issues/8)) |
| **Apple M1 Max (`Metal` · `Fractal-64`)** | `10C CPU` + `32C Metal` | `Unified` | *Metal* | **`57.65 tok/s`** *(`+86%`)* | **`57.65+ tok/s`** | `@austindixson` ([PR #24](https://github.com/synchopate/llama-modchip/pull/24)) |
| **Apple M4 Pro (`14-Core SoC`)** | `14C CPU + 20C Metal` | `24 GB` Unified (`0 Swap`) | **`256.0 – 549.0`** | **`47.0 – 48.0 tok/s`** *(128K)* | **`49.0+ tok/s`** | `@jarorosFork` ([`apple-silicon/`](apple-silicon/README.md)) |
| **AWS Graviton3 `m7g.2xlarge` (`ARM64 Neoverse-V1`)** | `8 vCPU` (`32 MB` L3, `SVE-256`) | `31 GB` DDR5 (`0 GPU`) | **`101.67`** *(`-t 8`)* | **`41.05 tok/s`** *(C++20)* | **`44.97 tok/s`** *(Refactoring)* | `@gerchik` ([Issue #2](https://github.com/synchopate/llama-modchip/issues/2)) |
| **AMD EPYC 7402P (`Zen 2 Rome` · `AVX2-only`)** | `24C/48T` (`8 CCDs`, `128 MB` L3) | `128 GB` 8-Ch DDR4 (`0 GPU`) | **`158.73`** *(`-t 24`)* | **`27.29 tok/s`** | **`31.22 tok/s`** | `@AdamKlob` ([Issue #6](https://github.com/synchopate/llama-modchip/issues/6)) |
| **AMD Ryzen 9 9950X3D (`Zen 5 3D V-Cache` · `Win11`)** | `16C/32T` (`128 MB` L3, `AVX-512`) | `128 GB` DDR5-6000 (`0 GPU`) | *Native Win11* | **`24.92 tok/s`** *(`30B`) / `9.47` (`284B`)* | **`24.92+ tok/s`** | `@kevinblo` ([Issue #33](https://github.com/synchopate/llama-modchip/issues/33)) |
| **AMD Ryzen 9 9950X (`Zen 5 Desktop`)** | `16C/32T` (`64 MB` L3) | `64 GB` DDR5-6800 (`0 GPU`) | **`135.64`** | **`20.78 tok/s`** | **`24.67 tok/s`** | `@nadams` ([Issue #5](https://github.com/synchopate/llama-modchip/issues/5)) |
| **AMD Ryzen 7 8745H / 8745HS (`Zen 4`)** | `8C/16T` (`16 MB` L3, `AVX-512`) | `64–96 GB` DDR5-5600 | **`128.81`** | **`19.48 tok/s`** | **`23.38 tok/s`** | `@arch-btw` ([#9](https://github.com/synchopate/llama-modchip/issues/9)) · `@jarorosFork` ([`fedora/`](fedora/README.md)) |
| **AMD Ryzen 5 5600X (`Zen 3 Desktop`)** | `6C/12T` (`32 MB` L3, `AVX2`) | `32 GB` DDR4-3200 (`0 GPU`) | **`63.90 – 88.77`** | **`14.95 – 19.04 tok/s`** | **`18.07 – 21.58 tok/s`** | `@alexander-jung` ([Issue #17](https://github.com/synchopate/llama-modchip/issues/17)) |
| **AMD Ryzen 7 5700X (`Zen 3 Desktop`)** | `8C/16T` (`32 MB` L3, `AVX2`) | `64 GB` DDR4-3600 (`0 GPU`) | **`101.93`** | **`16.04 tok/s`** | **`19.66 tok/s`** | `@germanpsycho` ([Issue #23](https://github.com/synchopate/llama-modchip/issues/23)) |
| **Intel Core Ultra 5 125H (`Meteor Lake-H`)** | `4P+8E+2LP-E` (`18 MB` L3) | `32 GB` DDR5 (`0 GPU`) | **`55.19`** | **`14.63 tok/s`** | **`16.61 tok/s`** | `@xma` ([Issue #18](https://github.com/synchopate/llama-modchip/issues/18)) |
| **AMD Ryzen 5 7430U / Ryzen 7 PRO 6850U / 5700U** | `6–8C` (`AVX2` Mobile) | `32–64 GB` RAM (`0 GPU`) | **`43.9 – 62.7`** | **`12.6 – 13.6 tok/s`** | **`13.5 – 15.6 tok/s`** | `@armadillu` ([#12](https://github.com/synchopate/llama-modchip/issues/12)) · `@mkesper` ([#15](https://github.com/synchopate/llama-modchip/issues/15)) · `@JamesStallings` ([#20](https://github.com/synchopate/llama-modchip/issues/20)) |
| **Intel Core i9-11950H / Dual Xeon E5-2670 / Ryzen 5 2600X** | `6–16C` (`AVX-512` / `AVX` / `AVX2`) | `32–128 GB` RAM (`0 GPU`) | **`21.1 – 85.4`** | **`7.6 – 10.8 tok/s`** | **`10.4 – 13.4 tok/s`** | `@ELO-I` ([#11](https://github.com/synchopate/llama-modchip/issues/11)) · `@Mammux` ([#14](https://github.com/synchopate/llama-modchip/issues/14)) · `@lawsochi` ([#26](https://github.com/synchopate/llama-modchip/issues/26)) |
| **`DeepSeek-V4-Flash 284B` on Ryzen 9 9955HX / 9800X3D** | `8–16C` (`Zen 5`, `AVX-512`) | `64 GB` DDR5 (`0 GPU`) | **`21.3 – 44.36`** | **`8.66 – 9.06 tok/s`** *(`16C`)* | **`8.80 – 25.30 tok/s`** *(`1M` ctx verified on Win11)* | `@synchopate` · `@MR1KRAKEN` ([PR #27](https://github.com/synchopate/llama-modchip/pull/27)) |

<details>
<summary><b>Repository Structure & Manual Source Build Instructions</b></summary>
<br/>

```text
llama-modchip/
├── modchip                                    # Unified CLI (setup | download-bin | start | chat | bench | eval | web | claude | stop)
├── install.sh                                 # Zero-to-Running 3-Tier Installer (16 GB / 32 GB / 64 GB)
├── README.md / ARCHITECTURE.md / FAQ.md       # Overview, Systems Architecture & Engineering FAQ
├── RELEASE_NOTES.md                           # v3.0 & Historical Release Notes
├── patches/
│   └── llama-modchip-v3.0.patch               # Single unified patch onto llama.cpp de32b268c (Linux, macOS Metal, Windows, CUDA, Vulkan)
├── scripts/
│   ├── build_zen5_llama.sh                    # Cross-platform CMake builder (applies llama-modchip-v3.0.patch)
│   ├── llama_modchip.py                       # <5ms GGUF & CPU/Cache Topology Profiler + Live SHM TUI
│   ├── chat.py                                # Zero-dependency Streaming Chat & 2-Stage CPU Scorecard
│   └── check_cpu_readiness.py                 # Standalone CPU/RAM/THP & DRAM Bandwidth Estimator
├── apple-silicon/                             # Apple Silicon M1–M5 Metal + ARM64 NEON setup & run scripts
├── windows/                                   # Windows 10/11 MinGW-w64 & CUDA Builder + Hybrid GPU/CPU Launcher
├── fedora/                                    # Fedora 44 / Ryzen 7 8745HS (GEEKOM A8) script
├── gateway/sse_gateway.py                     # Agentic SSE Proxy + HARP-Cache + Dark-Mode Web HUD (:8787)
├── speculative/                               # RouteCrack + Stockfish-PVS v2 (248K-vocab 32-bit token safe)
├── benchmarks/                                # Reproducible Quality Gate suites, KLD/PPL evaluators & logs
└── docs/                                      # Model & hardware deep-dive guides
```

Manual source compilation on Linux or macOS:
```bash
./scripts/build_zen5_llama.sh ./workspace/llama.cpp
```

</details>

---

## Acknowledgments

- **Qwen Team (`Qwen/Qwen3.8-Flash-Next`, [`qwen-community-1.0`](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE))**, **DeepSeek AI (`deepseek-ai/DeepSeek-V4-Flash-0731`, MIT)**, and **NVIDIA (`NVIDIA-Nemotron-3.5-30B-A3B`, [`OpenMDW-1.1`](https://openmdw.ai/license/1-1/))** for the foundational hybrid architectures, and **`ggml-org/llama.cpp`** for the upstream C/C++ runtime.
- **Salvatore Sanfilippo ([`@antirez`](https://github.com/antirez))** for single-pass DeepSeek-V4 routed-MoE quantization research and the public `1.5M`-token [`routed-moe-ds4-1p5m.dat`](https://huggingface.co/antirez/deepseek-v4-gguf/blob/f71f23d552d664e523b422157b2befbf74040380/imatrix/DeepSeek-V4-Flash-chat-v2-routed-moe-ds4-1p5m.dat) importance matrix used in `DeepSeek-V4-Flash-0731-MaxQ-v4`.
- **AtomicChat ([`AtomicChat/dsv4-eval-artifacts`](https://huggingface.co/datasets/AtomicChat/dsv4-eval-artifacts))** for the open `wiki-alt.txt` evaluation corpus, plus community contributors `@notactuallytreyanastasio`, `@austindixson`, `@MR1KRAKEN`, `@jarorosFork`, `@kevinblo`, `@khairullinr`, and everyone on the CPU leaderboard.

---

<div align="center">

**[Release Notes (`RELEASE_NOTES.md`)](RELEASE_NOTES.md)** · **[Nemotron Guide (`docs/NEMOTRON_OPTIMIZATIONS.md`)](docs/NEMOTRON_OPTIMIZATIONS.md)** · **[DeepSeek-V4 Guide (`docs/DEEPSEEK_V4_OPTIMIZATIONS.md`)](docs/DEEPSEEK_V4_OPTIMIZATIONS.md)** · **[Hardware Matrix (`docs/HARDWARE_OPTIMIZATIONS.md`)](docs/HARDWARE_OPTIMIZATIONS.md)** · **[Architecture (`ARCHITECTURE.md`)](ARCHITECTURE.md)** · **[FAQ (`FAQ.md`)](FAQ.md)**

</div>
