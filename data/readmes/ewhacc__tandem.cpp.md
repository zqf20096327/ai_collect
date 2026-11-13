# tandem.cpp

tandem.cpp is a patch set for [llama.cpp](https://github.com/ggml-org/llama.cpp). It makes MoE models that don't fit in VRAM run faster in llama.cpp. It keeps the most-used experts on the GPU and lets the CPU help with the rest, for any MoE model llama.cpp supports. Single-user decode is the target.

It is an independent project, not affiliated with ggml-org. Base: llama.cpp `f5222f25c` (2026-10-28, see `BASE_COMMIT`).

Decode tok/s, one user, GSM8K questions. Each row is one model on one PC. Two numbers are greedy / the model's recommended sampling, one number is greedy.

| Model | GPU | RAM | CPU | llama.cpp | tandem.cpp | Strata |
|---|---|---|---|---|---|---|
| **Qwen3.8-Flash-Next** IQ3_S + MTP (78 GiB) | RTX 4090 24 GB | 64 GB | i5-12400F | 29.8 / 29.4 | **97.3 / 96.1** (3.3×) | 103.6 / 98.1 |
| **Qwen3.8-Flash-Next** IQ3_S + MTP (78 GiB) | RTX 5070 Ti 16 GB | **32 GB** | i5-12400F | 14.9 | **34.3** (2.3×) | 30.3 |
| **gpt-oss-120b** MXFP4 | RTX 4090 24 GB | 64 GB | i5-12400F | 27.8 / 27.7 | **51.5 / 48.0** (1.85×) | — |
| **DeepSeek-V4.1-Flash** IQ2_XS (139 GiB of experts) | RTX 5070 Ti 16 GB | 64 GB | i5-14600KF | 7.4 | **14.2** (1.9×) | 10.4 |
| **DeepSeek-V4.1-Flash** IQ2_XS | RTX 5070 Ti + 5060 Ti (32 GB) | 64 GB | i5-14600KF | — | **16.9** | — |
| **DeepSeek-V4.1-Flash** IQ2_XS | RTX 5090 32 GB | 128 GB | i5-14600KF | 11.5 | **33.1** (2.9×) | 28.0 |

The 32 GB row is a cold start from a DRAM-less PCIe 4.0 SSD; at 64 GB DeepSeek-V4.1 is about twice the RAM and is read from a PCIe 4.0 SSD.

We tuned for Qwen3.8 only, but other MoE models that do not fit in VRAM gain too: typically 1.4–2.1× (gpt-oss-120b, GLM-4.5-Air, Qwen3.6-35B-A3B, DeepSeek-V4.1), less when the model nearly fits. Prompt processing is faster as well (1.4–1.8× on a 64k-token prompt).

[Strata](https://github.com/Niko1221/Strata) is a dedicated MoE offload engine for a few models. Its default skips low-ranked experts (`STRATA_ROUTE_TAIL_SKIP`), which is faster but approximate (127.1 tok/s in the RTX 4090 Qwen3.8 row); the tables show its exact mode (`STRATA_ROUTE_TAIL_SKIP=0`, every routed expert computed, as llama.cpp and tandem.cpp do). Full tables per machine are [below](#results).

For a big card serving many concurrent streams, use [Tandem-vLLM](https://github.com/ewhacc/tandem) instead; tandem.cpp is for one user on a 16–32 GB card with the experts in RAM.

## What's new (2026-11-13)

- **Big models on small PCs are much faster.** When a model is far larger than your RAM, tandem.cpp now uses VRAM and RAM
  together as one large expert cache, so far less has to come from the SSD. It switches on by itself; nothing to set.
  - Qwen3.8 (78 GiB) on a 32 GB PC with a 16 GB card: **34 tok/s, up from 29**. That's 2.3× llama.cpp and 1.13× Strata,
    with half Strata's SSD reads and a faster first token.
  - DeepSeek-V4.1 (139 GiB of experts) on a 64 GB PC: +7–10%, and **1.8× Strata** on a budget DRAM-less SSD.
  - Models that fit in RAM run as before. 2 GiB of RAM stays free for your other programs.
  - Details in [Results](#results); `LLAMA_MOE_STORE_AUTO=0` turns it off ([Defaults](#defaults)).

## Earlier (2026-11-11)

- Models larger than RAM: prompt batches read their missed experts ahead with several threads, and misses read from the SSD
  keep the drive busy. DeepSeek-V4.1 on a 64 GB PC with a 16 GB card is now 1.9× the speed of llama.cpp and 1.4× Strata's (the earlier build was slower than llama.cpp).
- A launcher, `tandem-run.py`, that picks the flags for your machine ([Quick start](#quick-start)).
- More GPU memory for the expert cache: the default reserve is 512 MiB (was 1024), and with `LLAMA_MTP_DRAFT_VOCAB` the MTP
  head's full output layer stays in host memory (only the vocabulary subset is on the GPU).
- The CPU path times its i-quant kernels once at startup and keeps the fastest for your CPU (Qwen3.8 IQ3_S: +4.5% on an i7-8700, +1.5% on an i5-14600KF).
- The CPU/upload split leaves a little more to the CPU (factor 2.25 instead of Strata's 1.85: +2.7% on a 14600K, level elsewhere).
- Pinned copies of the experts use huge pages when the RAM allows (a fragmented host lost up to 30% before).
- Fixes from [issue #2](https://github.com/ewhacc/tandem.cpp/issues/2) (2026-11-12): the CPU-expert threads sleep when idle
  (3.3 cores busy at idle before, 0.03 now), and the auto cache size leaves room for the pooled graphs, which grow with the
  context (long prompts on a 12 GB card ran out of memory).
- The CPU threads default (`LLAMA_MOE_CPU_THREADS`) now counts physical cores within the process's CPU set: CPUs without
  SMT or with E-cores got about half before (14600K: 13 threads instead of 9, level on speed; a 6-core/12-thread CPU is unchanged).
- The RAM rules (pinned experts, the per-layer embedding table, read-ahead) also see a container's memory limit (Docker or
  Podman with cgroup v2, or cgroup v1), not only a systemd scope's.
- Qwen3.8 with MTP keeps one recurrent state and replays the accepted tokens instead of a snapshot per draft position:
  315 MiB more for the expert cache, +2.8% on a 16 GB card (exact; `LLAMA_GDN_REPLAY=0` restores the snapshots).
- Fix (Qwen3.8 with MTP): after a speculative step that rejected draft tokens, a following batch of 64 or more tokens (the
  next turn's prompt) on Ampere, Ada or Blackwell GPUs started from the recurrent state that still included the rejected tokens.

## Build

```
bash build.sh            # clones llama.cpp into ./tandem, checks out the base commit, applies tandem.patch, builds llama-server
```

or by hand:

```
git clone https://github.com/ggml-org/llama.cpp tandem && cd tandem && git checkout f5222f25c
git apply ../tandem.patch
cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build -j --target llama-server
```

Tested with CUDA 13.0–13.4 on Ubuntu 22.04 and 24.04, sm_89 (RTX 4090, RTX 6000 Ada) and sm_120 (RTX PRO 6000 Blackwell).

### AMD GPUs (ROCm)

The patch builds with HIP. We use the same code as on CUDA, but we have not tuned it for AMD:

```
git clone https://github.com/ggml-org/llama.cpp tandem && cd tandem && git checkout f5222f25c
git apply ../tandem.patch
cmake -B build -DGGML_HIP=ON -DGGML_HIP_GRAPHS=ON -DGPU_TARGETS=gfx1100 -DCMAKE_BUILD_TYPE=Release
cmake --build build -j --target llama-server
```

Set `GPU_TARGETS` to your card (gfx1100 = RX 7900 series). `-DGGML_HIP_GRAPHS=ON` matters: without graphs every layer's kernels are
launched one by one. For `-ot`, use the ROCm device name, `ROCm0`, where the examples say `CUDA0`. `tandem-run.py` supports NVIDIA only.

Tested on one PC: i7-8700 (6 cores), 64 GB DDR4, RX 7900 XTX 24 GB on PCIe 3.0, Ubuntu 26.04 with its ROCm 7.1 packages.
Qwen3.8-Flash-Next + MTP, greedy, the first 40 GSM8K questions, same day (2026-11-12), decode tok/s:

| Engine, quant | tok/s |
|---|---|
| tandem.cpp IQ3_S | 65.6 |
| Strata v0.2.9 IQ3_S | 70.4 |
| Strata's RDNA3 fork IQ3_S | 80.2 |
| Avalon IQ3_KS (its own quant) | 83.4 |

On this 6-core CPU the AMD-specific engines are ahead. Most of the gap is the CPU's work on missed experts: IQ3_S is costly to
decode on a CPU, and Avalon's own quant types decode cheaply.

## Quick start

```
bash build.sh                                  # builds llama-server (see Build above)
python3 tandem-run.py --model qwen3.8          # or: gpt-oss-120b, or --model /path/to/any-moe.gguf
```

`tandem-run.py` is one file (Python 3 standard library; Linux + NVIDIA only). It looks at your machine, picks the flags from the
[Run](#run) section for it, prints each flag with a one-line reason and the exact command, then runs `llama-server` in the
foreground. When it prints `URL: http://127.0.0.1:8080/` the OpenAI-compatible API is ready at `/v1`.

It finds `llama-server` on your `PATH`, in `$TANDEM_SERVER`, or at `--server-bin`. `qwen3.8` and `gpt-oss-120b` are built in
with their MTP head / EAGLE3 draft: if the files are missing it shows the `hf download` commands and sizes and asks before
downloading (`--yes` accepts; files go to `--models-dir`, default `~/tandem-models`). Any other GGUF gets the generic MoE rules
and the plan says so. If the model fits in VRAM the launcher leaves the expert cache out, because plain llama.cpp is faster there.

### Reading the plan

```
== Hardware ==   GPU, VRAM, PCIe, physical cores, RAM (the lower of MemTotal and the container limit), free disk, kernel
== Model ==      which file, which draft
== Plan ==       <flag>   <why>          one line per choice; "(no -lm none)" means a flag was left out on purpose
                 note: / WARNING:        things to know about this machine (below)
== Calibration == cached, or "will run on first start"
== Command ==    copy this to run it by hand
```

### Dry run

`--dry-run` prints the plan and starts nothing, downloads nothing. Use it to see what the launcher would do, or to test other
hardware (`--assume-vram-gib`, `--assume-ram-gib`, `--assume-cores` apply the rules for a smaller machine; they do not limit the
real hardware).

### Calibration

The first start for a machine, model and server build loads the model once per candidate draft count (the server cannot change it
per request), measures decode speed on three short prompts, keeps the fastest and saves it to
`~/.cache/tandem/<key>.json` (`$TANDEM_CACHE_DIR` moves it). It adds about 1-2 minutes after the first model load. Later starts reuse it.
`--calibrate` redoes it and also tries one fewer draft token; `--no-calibrate` skips it and uses the rules.

### Notes the plan may print

- **The model is larger than RAM**: the experts are read from the SSD, so speed depends on the SSD, and the first requests are slower
  while the cache warms. Below 0.6x the model size in RAM the drive sets the speed (DeepSeek-V4.1 on 64 GB: ~12 tok/s from a
  PCIe 4.0 drive, ~8 from a DRAM-less one).
- **Older kernels (before 6.1)**: they reclaim mapped model pages poorly. Expect slow loads when RAM is below the model size + 8 GiB.
- **"This build predates the low-RAM fixes"**: your tandem.cpp is older than the RAM fixes. Update it; until then the launcher sets
  `LLAMA_MOE_PIN_EXPS=0` and `LLAMA_PLE_GPU_COPY=0` when RAM is limited (a container limit is not seen by old builds).
- In a container the launcher uses the memory limit (`memory.max`), not the host's RAM.

### Other options

`--port`, `--ctx` (default 16384), `--model-path` / `--draft` (your own files, e.g. another quant), `--no-draft`, `--gpu N`,
`--extra "<llama-server flags>"` (appended last).
`--fast` adds `LLAMA_MOE_TAIL_SKIP=7`: faster but **approximate** (quality: TODO).

## Run

How it works: the experts live in host RAM, and the GPU memory left over holds a cache of recently used experts. The experts a token needs that are not in the cache are split between the CPU, which computes its share while the GPU runs the cached ones, and an upload into the cache. The split follows the measured CPU and PCIe speeds, using Strata's rule.

Any MoE model whose experts do not fit in VRAM:

```
llama-server -m model.gguf -ngl 99 -cmoe --moe-cache-mib auto -lm none -np 1 -c 16384
```

- `-cmoe` keeps every expert in host RAM. `--moe-cache-mib auto` gives the GPU memory left after the model, the KV cache and the compute buffers to the expert cache, minus `--moe-cache-margin-mib` (default 512 MiB; a draft model's GPU size is added automatically). A fixed size in MiB also works.
- `-lm none` reads the weights into RAM instead of mmapping the file.
- `-np 1 -c 16384`: one conversation with a 16k-token context. Without them llama-server opens 4 slots that share a small context, too short for a thinking model. `-c` is the total context; the KV cache comes out of the GPU memory the expert cache would get, so set it to what you need (on Qwen3.8, about 0.7 GiB per extra 16k tokens).
- The startup line `failed to fit params ... n_gpu_layers already set by user to 99, abort` is expected: `-ngl 99` turns llama.cpp's automatic placement off, and the expert cache does the placement instead.
- **Less RAM than the model** (e.g. Qwen3.8 IQ3_S, 78 GiB, on a 64 GB PC): leave out `-lm none`. The file stays mapped; the experts are copied once into pinned memory when the RAM holds them plus 10 GiB, and the rest is read from the file.
- **Much less RAM (e.g. a 16 GB PC):** also pass `--cache-ram 0`. llama-server's prompt cache otherwise takes up to 8 GiB of RAM and pushes the experts out of the page cache.
- Supported expert types for the CPU path: SwiGLU experts (fused or separate gate/up, optional clamp) and gpt-oss's SwiGLU-OAI with biases. For other types the server logs a warning and uploads every miss instead (correct, slower).

Qwen3.8-Flash-Next with its MTP head (the head as a separate GGUF). Download the model (IQ3_S, 78 GiB, two files) and the head (Q4_K):

```
hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include 'IQ3_S/*' --local-dir models
hf download ewhacc/qwen38-mtp-outq4_K-expsq4_K --include '*.gguf' --local-dir models
```

then run:

```
LLAMA_MTP_DRAFT_VOCAB=100000 llama-server -m models/IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf \
  -ngl 99 -cmoe --moe-cache-mib auto -lm none -np 1 -c 16384 \
  --spec-type draft-mtp -md models/qwen38-mtp-outq4_K-expsq4_K.gguf --spec-draft-n-max 3 --spec-draft-sampling probabilistic \
  -bs -ot '^token_embd\.weight=CUDA0'
```

- The head ([ewhacc/qwen38-mtp-outq4_K-expsq4_K](https://huggingface.co/ewhacc/qwen38-mtp-outq4_K-expsq4_K), Qwen Community License 1.0) was made with `convert_hf_to_gguf.py --mtp` on the original checkpoint (Q8_0), then its output and expert tensors to Q4_K: `llama-quantize --allow-requantize --tensor-type output=q4_K --tensor-type _exps=q4_K qwen38-mtp-q8_0.gguf qwen38-mtp.gguf Q8_0`. That takes it from 3.6 to 1.8 GiB of VRAM with the same acceptance; the freed memory goes to the expert cache.
- `--spec-draft-n-max 3` is best on 24 GB cards and 6–10 core CPUs; 4 on a 48 GB card.
- `--spec-draft-sampling probabilistic` keeps sampled output exact (rejection sampling) and acceptance high at the model's default temperature.

gpt-oss-120b with its EAGLE3 draft (`ggml-org/gpt-oss-120b-GGUF`):

```
llama-server -m gpt-oss-120b-MXFP4.gguf -ngl 99 -cmoe --moe-cache-mib auto -lm none -np 1 -c 16384 \
  --spec-type draft-eagle3 -md eagle3-gpt-oss-120b-Q8_0.gguf --spec-draft-n-max 4
```

EAGLE3 helps on 10+ core CPUs and slows things down on a 6-core one (see the consumer PC table).

## Defaults

The server applies these when the variable is unset (logged at startup); `VAR=0` turns one off, `LLAMA_MOE_NO_DEFAULTS=1` turns all off. All are exact or differ only in floating-point rounding (kernel choice); the Qwen3.8-specific ones act only on that architecture.

| Variable | Default | What |
|---|---|---|
| `LLAMA_MOE_CPU` | `auto` | CPU/GPU split for missed experts (`0..1` = fixed share uploaded) |
| `LLAMA_MOE_PREFILL_CPU` | `auto` | the split for prompt batches |
| `LLAMA_MOE_CPU_THREADS` | cores − 1 | CPU threads for missed experts |
| `LLAMA_MOE_CPU_RB`, `LLAMA_MOE_CPU_DOWN_PE` | `64`, `64` | CPU expert job work-item layout |
| `LLAMA_MOE_STORE_AUTO` | `1` | store mode (below) when the experts outside VRAM exceed 85% of the RAM and `LLAMA_MOE_ARENA_MIB` is unset |
| `LLAMA_MOE_ARENA_MIB` | unset | `auto` forces store mode: the experts outside VRAM live in one pinned block of RAM (the whole RAM less the reserve), read with direct I/O |
| `LLAMA_MOE_ARENA_RESERVE_MIB` | `2048` | store mode: RAM left free |
| `LLAMA_MOE_ARENA_EXCL` | `1` | store mode: an expert is in VRAM or in the block, not both; the VRAM victim is copied back to RAM |
| `LLAMA_MOE_ARENA_ASYNC` | `1` | store mode: decode reads from the SSD overlap the compute |
| `LLAMA_MOE_PIN_EXPS` | auto | mmap mode: copy the mapped experts to pinned memory when the RAM holds them + 10 GiB |
| `GGML_SCHED_BATCH_INPUTS` | `3` | a graph's host inputs in one packed upload |
| `GGML_CUDA_GRAPH_KEY_SHAPE` | `1` | one CUDA graph per batch shape |
| `GGML_CUDA_MMVF_MAX` | `8` | vector kernel for float weights up to 8 columns |
| `GGML_CUDA_Q8_CACHE` | `1` | reuse quantized activations across matvecs |
| `LLAMA_GRAPH_POOL` | `6` | keep allocated graphs for alternating small batch shapes; with `--moe-cache-mib auto` fewer (or none) at long contexts |
| `LLAMA_GRAPH_POOL_MIB` | `256` | VRAM those pooled graphs may take, measured at the full context and left out of the auto cache size |
| `LLAMA_SRV_USER_BREAK` | `0` | no prompt-cache checkpoint at every user message |
| `LLAMA_MTP_DEFER` | `1` | MTP catch-up decode deferred to the next draft |
| `LLAMA_HC_FUSE`, `GGML_CUDA_HC_MIX_FUSE` | `1` | hyper-connection fusions (Qwen3.8) |
| `LLAMA_GDN_DIRECT`, `LLAMA_GDN_GATES` | `1` | Qwen3.8 gated delta net |
| `LLAMA_GDN_REPLAY` | `1` | Qwen3.8 with speculative decoding, one sequence: one recurrent state plus the last step's inputs, replayed after a rollback, instead of a snapshot per draft position (450 → 135 MiB with 3 drafts) |
| `LLAMA_CONV_CONT`, `LLAMA_CONV_TAIL` | `1` | Qwen3.8 conv state |
| `LLAMA_PLE_GPU` | `1` | per-layer embeddings read by the GPU from pinned host memory |
| `LLAMA_PLE_GPU_COPY` | auto | Linux 6.8+ (file mmaps cannot be pinned): copy the table to pinned memory, only when the RAM holds the model + 8 GiB |

## Results

Single user, the first 200 GSM8K test questions (zero-shot chat, max 2048 tokens), decode tok/s. Every row gives both engines the same GPU memory and the same draft model, if any. llama.cpp is `f5222f25c` with its default placement (`-fit on`: dense layers on the GPU, then as many layers' experts as fit), with `-fitt` set to tandem.cpp's margin when a draft model is loaded. Each cell is "greedy / sampled", sampled being the model's recommended sampling (Qwen: T 1.0, top-k 20, top-p 0.95; gpt-oss: T 1.0, top-p 1.0; GLM: the server's defaults; DeepSeek: T 1.0, top-p 0.95). Accuracy is within run-to-run noise between the engines in every row. The scripts are in [`bench/`](bench/).

Models: Qwen3.8-Flash-Next [ISTA GSQ-RCO](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF) IQ3_S (78 GiB) with the Q4_K MTP head above; gpt-oss-120b MXFP4 (`ggml-org`); Qwen3.6-35B-A3B UD-Q4_K_XL and GLM-4.5-Air Q4_K_M (unsloth); DeepSeek-V4.1-Flash-1017 [ISTA GSQ-RCO](https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF) IQ2_XS (139 GiB of routed experts). We tuned for Qwen3.8 only.

### Gaming PC: i5-14600KF (6P + 8E cores), DDR4-3200 (2 channels), Samsung PM9A1 (PCIe 4.0 NVMe)

DeepSeek-V4.1-Flash-1017 IQ2_XS, no draft, greedy, the first 40 GSM8K questions (this build, 2026-11-11). At 64 GB the model is
about twice the RAM, so most experts are read from the SSD; at 128 GB it fits.

| GPU, RAM | llama.cpp | tandem.cpp | | Strata v0.2.9 exact | time to first token (llama.cpp / tandem.cpp / Strata) |
|---|---|---|---|---|---|
| RTX 5070 Ti 16 GB, 64 GB | 7.4 | 14.2 / 13.3 | 1.9× | 10.4 | 14.4 / 6.3 / 6.8 s |
| RTX 5070 Ti + RTX 5060 Ti (32 GB, `-sm layer`), 64 GB | — | 16.9 | | — | — / 4.3 / — s |
| RTX 5090 32 GB, 128 GB | 11.5 | 33.1 / 32.2 | 2.9× | 28.0 | 3.4 / 1.7 / 4.0 s |

All cells answered 39–40 of 40 correctly. Two numbers for tandem.cpp are two runs (the ratio uses the first); the 32 GB row
splits the layers over both cards (the RTX 5060 Ti sits in an x4 slot).

### Consumer PC: i5-12400F (6 cores), 64 GB DDR4 (43 GB/s), RTX 4090 24 GB, PCIe 4.0 x16

The models are larger than RAM with the OS, so both engines read them from the mapped file.

| Model, setup | llama.cpp | tandem.cpp | | Strata exact |
|---|---|---|---|---|
| Qwen3.8 IQ3_S, MTP | 29.8 / 29.4 | 97.3 / 96.1 | 3.3× / 3.3× | 103.6 / 98.1 |
| gpt-oss-120b, no draft | 27.8 / 27.7 | 51.5 / 48.0 | 1.85× / 1.73× | |
| gpt-oss-120b, EAGLE3 | 25.2 / 24.2 | 41.1 / 42.0 | 1.63× / 1.74× | |
| DeepSeek-V4.1 IQ2_XS (3× RAM, from the SSD), no draft, earlier build (2026-11-01) | 6.86 / – | 5.99 / – | 0.87× | 8.41 / – |

- Strata exact is 6% ahead greedy and 2% sampled on Qwen3.8; its default mode, which skips low-ranked experts, gives 127.1. tandem.cpp's equivalent (`LLAMA_MOE_TAIL_SKIP=7`, approximate, off by default) gives 123.6 / 124.3.
- On 6 cores EAGLE3 slows both engines down: verifying several tokens multiplies the experts the CPU must run.
- DeepSeek-V4.1 is three times this PC's RAM. That row is from the earlier build, which was slower than llama.cpp when misses had to come from the SSD; the current build reads them ahead with several threads (see the gaming-PC rows). This PC's GPU has since changed, so the row was not re-measured.


The same PC with an RTX 5070 Ti 16 GB instead of the 4090, on an MSI M450 drive (DRAM-less, PCIe 4.0), models much larger than
RAM, from a cold start (page cache dropped), greedy, two runs per engine in mirrored order (2026-11-13).

Qwen3.8-Flash-Next IQ3_S + MTP (78 GiB) at 32 GB of RAM (`mem=` boot), 8K context, the first 16 GSM8K questions:

| | decode tok/s | read from the SSD | time to first token (median) |
|---|---|---|---|
| llama.cpp `-fit on`, the same MTP head | 14.9 / 15.1 | 294 / 290 GB | 5.1 / 5.3 s |
| tandem.cpp (defaults: store mode) | **34.3 / 35.0** | 231 / 232 GB | 2.9 / 4.1 s |
| Strata v0.2.9 exact, its own low-RAM setup and MTP settings | 30.3 / 32.0 | 492 / 418 GB | 4.3 / 4.2 s |

All cells 15 of 16 correct. Strata's draft settings are its own (not the same speculative decoding as the other two rows).

DeepSeek-V4.1-Flash IQ2_XS at 64 GB, no draft, the first 8 GSM8K questions: tandem.cpp
**10.4 / 10.2** tok/s (374 / 385 GB read, first token 13.4 / 14.4 s), Strata v0.2.9 exact 5.7 / 5.7 (746 / 708 GB, 15.0 / 13.7 s):
**1.8×**. All 8/8 correct. On the gaming PC's faster drive above the gap is smaller (1.4×).

### Older workstation: i9-10900X (10 cores), 8× DDR4-2666 (78 GB/s), RTX 4090 24 GB, PCIe 3.0 x16

| Model, setup | llama.cpp | tandem.cpp | |
|---|---|---|---|
| Qwen3.8 IQ3_S, MTP | 31.1 / 31.9 | 100.9 / 100.9 | 3.2× / 3.2× |
| gpt-oss-120b, no draft | 31.2 / 30.1 | 49.6 / 49.6 | 1.59× / 1.65× |
| gpt-oss-120b, EAGLE3 | 30.3 / 28.8 | 62.5 / 61.0 | 2.06× / 2.12× |

Drafts do not speed up llama.cpp on this host (Qwen3.8 29.8 without MTP): most of its experts run from system RAM, so verifying several tokens costs nearly as much as it saves.

### Workstation: Threadripper PRO 5955WX (16 cores), DDR4 (~80 GB/s read), RTX 6000 Ada 48 GB, PCIe 4.0 x16

| Model, setup | llama.cpp | tandem.cpp | | Strata exact |
|---|---|---|---|---|
| Qwen3.8 IQ3_S, MTP, whole card | 98.6 / 97.1 | 182.5 / 180.9 | 1.85× / 1.86× | 185.9 / 169.9 |
| Qwen3.8 IQ3_S, MTP, 12 GiB expert cache | | 131.1 / 131.9 | | 129.2 / 119.4 |
| Qwen3.8 IQ3_S, MTP, 4 GiB expert cache | | 91.3 / 89.5 | | 89.3 / 83.7 |
| gpt-oss-120b, whole card | 87.9 / 86.3 | 95.3 / 90.7 | 1.08× / 1.05× | |
| gpt-oss-120b, 24 GB budget | 47.1 / 47.3 | 70.7 / 68.5 | 1.50× / 1.45× | |
| gpt-oss-120b, EAGLE3, whole card | 88.7 / 84.4 | 136.7 / 126.8 | 1.54× / 1.50× | |
| Qwen3.6-35B-A3B (22.4 GB), fits | 173.1 / 173.1 | 179.2 / 179.2 | 1.04× / 1.04× | |
| Qwen3.6-35B-A3B, 16 GB budget | 117.8 / 117.8 | 148.6 / 148.6 | 1.26× / 1.26× | |
| Qwen3.6-35B-A3B, 12 GB budget | 97.2 / 96.5 | 136.5 / 135.4 | 1.40× / 1.40× | |
| Qwen3.6-35B-A3B, 8 GB budget | 79.8 / 80.0 | 115.0 / 114.5 | 1.44× / 1.43× | |
| GLM-4.5-Air (73 GB), whole card | 31.9 / 31.9 | 54.6 / 55.1 | 1.71× / 1.73× | |
| GLM-4.5-Air, 24 GB budget | 20.1 / 20.0 | 34.7 / 34.6 | 1.73× / 1.73× | |

The cache-size rows compare against Strata at the same expert cache; a "budget" is the GPU memory both engines may use. Strata's cache rows are its exact mode as above.

Long context: a 64k-token prompt of real text in a 72k context, two planted code words found in every cell, greedy. Prefill is the prompt's tokens over the time to its first token:

| Model, setup | prefill llama.cpp | prefill tandem.cpp | | decode llama.cpp | decode tandem.cpp | |
|---|---|---|---|---|---|---|
| Qwen3.8 IQ3_S, MTP | 600 tok/s (109 s) | 860 tok/s (76 s) | 1.44× | 88.0 | 158.4 | 1.80× |
| gpt-oss-120b, no draft | 660 tok/s (100 s) | 1150 tok/s (57 s) | 1.75× | 64.9 | 75.4 | 1.16× |
| gpt-oss-120b, EAGLE3 | 560 tok/s (117 s) | 1030 tok/s (63 s) | 1.84× | 85.0 | 125.5 | 1.48× |

On the GSM8K questions (short prompts) the time to first token is 1.6–2.7× lower with tandem.cpp in the rows we checked, except the consumer-PC DeepSeek row (22 s against 12 s, the SSD issue below).

### Server: EPYC 9534 (64 cores), DDR5 (~350 GB/s), RTX PRO 6000 Blackwell 96 GB, PCIe 5.0 x16

DeepSeek-V4.1-Flash-1017 IQ2_XS (139 GiB of experts), whole card, reasoning on:

| Setup | llama.cpp | tandem.cpp | | Strata v0.2.9 |
|---|---|---|---|---|
| no draft | 51.7 / 46.0 | 89.6 / 81.0 | 1.73× / 1.76× | 84.4 / 84.0 (6 experts, no DSpark) |
| DSpark draft (3 tokens) | 63.0 / – | 132.4 / 107.2 | 2.10× | 148.9 / – (its default: DSpark, up to 5 tokens) |

tandem.cpp caches 87 GiB of the experts here (98.7% hit rate). Five draft tokens with a 0.65 confidence cut-off, Strata's default, was slower for tandem.cpp (122.3).

### Quality

Qwen3.8 Q2_0, teacher-forced KL divergence of the next-token distribution against plain llama.cpp `f5222f25c` with the whole model on the GPU, 8-token batches:

| Build | mean KLD | same top token | PPL ratio |
|---|---|---|---|
| tandem.cpp, `LLAMA_MOE_NO_DEFAULTS=1` | 0.000000 | 100% | 1.000 |
| defaults, whole model on the GPU | 0.0091 | 96.1% | 0.999 ± 0.003 |
| defaults, 4 GiB cache + CPU path | 0.0093 | 95.5% | 1.000 ± 0.003 |

With the defaults off the patch computes exactly what llama.cpp does; the defaults change only rounding (fused kernels, kernel choice), and the cache and CPU path add ≤ 0.0002.

## Limits

- Greedy output is not repeatable run to run with an expert cache: which experts are cached, and which misses the CPU computes, depends on timing, and the CPU and GPU round differently. Accuracy is unchanged. A fixed share (e.g. `LLAMA_MOE_CPU=0.2`) makes it repeatable.
- Built for one user at a time. Concurrent requests work (tested at 2 and 4, accuracy unchanged) but gain less, and with a small cache several requests together can be slower in total than one.
- Multi-GPU: only `-sm layer` (the default) works with the cache; checked for correctness on 2 GPUs, not tuned for speed.
- Linux only. Tuned and tested on NVIDIA (CUDA). AMD (ROCm) works, but it is untuned and was tested on one RX 7900 XTX ([above](#amd-gpus-rocm)).
- Qwen3.8 GGUFs converted with a current llama.cpp may be a little slower than the ISTA files we measured (one fusion does not apply to their layout).
- Known issues, to be fixed:
  - models much larger than RAM (read from the SSD) depend on the drive (see the gaming-PC rows for a PCIe 4.0 drive);
  - DeepSeek-V4.1 with `-lm none` loads very slowly (its 103 GiB Engram tables are copied page by page); run it without `-lm none`.

## Licence

MIT, see [LICENSE](LICENSE). tandem.patch modifies llama.cpp, which is MIT-licensed by the ggml authors.
