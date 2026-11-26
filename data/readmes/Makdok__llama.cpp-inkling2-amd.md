# Inkling 2 Mini on AMD Radeon (ROCm/HIP): about 3000 tok/s prompt reading and 110 tok/s writing on a 24 GB card

Branch `inkling2-amd`. Measured on Radeon RX 7900 XTX, the first three rows with the h6-lbf16 file (details and method in
"Measurements"; VRAM = peak of the server, dedicated + shared):

| | prompt reading | writing after the prompt | VRAM peak |
|---|---|---|---|
| context 65536, DSpark drafter, 52 804-token prompt | 3048-3050 tok/s | 110-111 tok/s | 19.05 + 0.25 GB |
| context 131072, DSpark drafter, same prompt | 2886-2901 tok/s | 114-117 tok/s | 19.58 + 0.25 GB |
| context 262144, DSpark drafter, 249 584-token prompt | 1195 tok/s | 70 tok/s | 20.28 + 0.23 GB |
| against the Unsloth release b12568 where it fits in VRAM (context 32768, no drafter, 24 829 tokens) | 829 -> 2998-3154 tok/s (3.6-3.8x) | 42 -> 92 tok/s (2.2x) | 19.95 + 0.22 -> 17.17 + 0.14 GB |
| against the newer Unsloth release b12631 (context 32768, no drafter, 27 780 tokens) | 351 -> 3134-3146 tok/s (8.9x) | 50 -> 85 tok/s (1.7x) | 19.65 + 0.20 -> 17.17 + 0.14 GB |

> **This is not upstream llama.cpp.** This branch is the Unsloth llama.cpp release
> [b12568-mix-8eebad4](https://github.com/unslothai/llama.cpp/releases/tag/b12568-mix-8eebad4) (upstream b12568 plus the
> pull requests Unsloth merged for Inkling 2), with changes that make
> [Inkling 2 Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) fast on AMD GPUs under ROCm/HIP. It is
> experimental: it was tuned and measured on one GPU model, the Radeon RX 7900 XTX (RDNA3, gfx1100, 24 GB), and its GPU
> code paths only switch on for RDNA3.0 GPUs (gfx1100-gfx1103); every other GPU runs the stock kernels of the release
> (see "Which AMD GPUs"). It is not affiliated with ggml-org, Unsloth or Thinking Machines. A GGUF file made for this
> branch is described in its model card: `https://huggingface.co/Makdok/Inkling-2-Mini-AMD-GGUF`. With the DSpark drafter at 8192, the
> largest context where the release b12568 with the drafter stays in VRAM: prompt reading 984 -> 2448-2534 tok/s and
> writing 60 -> 129 tok/s. Image input and a gateway that loads the server on the first request: see "Images" and
> "Load on first request".
> The upstream README follows after the horizontal line.

## What it is

Inkling 2 Mini (Thinking Machines, 26.4B parameters, mixture of experts with 128 experts and 8 per token, 24 stored layers
of which layers 6-17 run three times with shared weights: 48 layer applications per token) ran in llama.cpp only with
Unsloth's merged release when this work started (2026-11-20). Built for HIP, that release is slow on RDNA3 for two
reasons:

1. Inkling 2 adds a relative-position bias per head to the attention logits. The release builds it as a dense per-head
   mask, which also takes the WMMA flash-attention kernel out of play: reading 2048 tokens at a depth of 32k runs at
   500 tok/s (llama-bench, `-ub 512`, measured on RX 7900 XTX).
2. Decoding is bound by kernel launches: about 8100 small kernels per generated token, 46.8 tok/s at depth 0.

The branch, on top of the import of the release archive:

| commit | content |
|---|---|
| 2 ports (author Daniel Han) | unslothai/llama.cpp#385 (dense bias chunked over query rows) and #386 (banded flash attention for the bias), open pull requests that are not in the release |
| ggml far mode | the relative bias evaluated inside the regular MMA/WMMA flash-attention kernel ("far" mode of `FLASH_ATTN_EXT_BANDED`), wrapped sliding-window caches read as rotated rings, fully masked K/V blocks skipped, the causal mask of a position-contiguous cache applied inside the kernel (no mask tensor), q8_0 K/V read through an F16 copy, tiles of 3 query heads for the 24 query heads over 8 K/V heads (instead of 4 with a padding column), branchless NVFP4 scale decode; for 2-8 query rows over a q8_0 cache, a kernel that serves the 3 query heads of a K/V head in one block, also with several K/V streams and with a q4_0 V beside the q8_0 K |
| llama reading path | the Inkling 2 graph on the far op (its relative-bias table as one flat product, the global cache without a mask tensor, a q8_0 global cache in groups of K/V heads with the sliding-window cache kept F16, also with a q4_0 V), KQ masks built on the device, follow-up prompts kept on the far path, sliding-window rings kept in one rotation after rejected drafts and restores, restored sliding-window states put back in the cells they were saved from (a restored conversation continues exactly like the kept one), host fills of the relative positions and of the first mask row without per-cell lookups, a graph order that lets the backend fuse; options, off by default: the drafter's full-attention cache as a window, the last layer application on the last rows only |
| ggml-cuda fusions | fused kernels for the small-op patterns of the Inkling 2 graph (also for steps of several sequences), Q8_0 mat-vec on F32 activations, grouped Q8_0 products (also over other activations of the same shape), NVFP4 MoE mat-vec tile and grid order, per layer application the row ops after the projections, the K and V convolutions and the three loop gates in one launch each, the router's top-k with the weight normalisation in one kernel: about 1215 launches per generated token instead of 8100; the loop controllers of prompt batches in three WMMA kernels; the depth mix and the short convolution with their loads held in registers (bit-identical); a relative-bias kernel for decode batches with one thread per key and token; expert products of prompt batches on FP16 WMMA instead of int8 MMQ (NVFP4 in tiles of 96 tokens, and Q8_0 / Q5_K from 256 tokens), with the SITU activation of the gate_up projection written by that kernel in FP16 and the down projection of the same experts in the same call (bit-identical), and small tiles spread over its 8 warps; an optional 2-int NVFP4 expert mat-vec for verify batches (off by default, other rounding); one kernel that uploads the staged inputs of a split |
| drafter | DSpark drafter: head computed only for the drafted positions and partly precomputed at start-up, drafted tokens picked on the device (no logits read back), target features injected from the device, compute buffer sized to its real outputs; one wait for the sampled outputs of a decode instead of one per getter |
| several slots | decode and verify steps of several conversations in one ubatch while prompts are read alone (on the far path), with the compute buffer reserved for that; no drafts while 3 or more slots generate; the drafter injections of every slot in one decode |
| scheduler input uploads | the small inputs of each split staged in pinned memory and uploaded on the GPU stream (one kernel per split) instead of one synchronous copy each; no GPU wait before a CPU split that follows a GPU split (the drafter's); a video-memory diagnostic |
| compute-buffer headroom | device compute buffers get a margin when they are (re)allocated, so that the small growths of later requests do not reallocate them (with ROCm on Windows a reallocation keeps the old block and can push the process into shared memory); allocator diagnostics |
| server prompt cache | an option, off by default (`INKLING2_CACHE_TAIL`), that also saves a slot to the RAM prompt cache when the next prompt would drop a long tail of it: for conversations that share a long prefix and take turns on one slot |
| tooling | test-backend-ops cases, batched generation and the rollback depth in llama-bench |
| docs | this section, `scripts/inkling2-amd` (build, check, and a gateway that loads the server on the first request), `.gitignore` |

## Which AMD GPUs

The GPU code paths of this branch are gated by one test, `ggml_cuda_ink2_arch_ok` (in
`ggml/src/ggml-cuda/inkling2-fused.cuh`): true on RDNA3.0 GPUs (gfx1100, gfx1101, gfx1102, gfx1103), false on every
other GPU and in CUDA builds, which then run the stock code of the release. Only gfx1100 was built and measured. The
staged input uploads of the scheduler are host code and are used on every ROCm device; only their batched upload kernel
is gated to RDNA3.0. The compute-buffer headroom, the two sliding-window cache changes, the host fills of the first mask
row and of large windows, the single wait for sampled outputs, the draft cap of the server and its prompt-cache option
are host code for every backend (table).

| change | where it runs | elsewhere |
|---|---|---|
| far mode (bias inside the flash-attention kernel, rotated rings, skip of masked K/V blocks, the bias table as one flat product, the causal mask of the global cache computed in the kernel, a q8_0 global cache read through an F16 copy), 3-head flash-attention tiles for a GQA ratio of 3 (any model with that ratio and head size 128), single-row tile kernel for decode, fused small-op kernels, relative-bias kernel of decode batches, Q8_0 mat-vec on F32 activations and grouped Q8_0 products (any model with Q8_0 weights), NVFP4 MoE mat-vec with 4 rows per block in slot-fast grid order, expert products of prompt batches on FP16 WMMA (any model with NVFP4 experts, or Q8_0 / Q5_K experts in batches of 256 tokens or more), the top-k router kernel with the weight normalisation and a rank selection (a router of 128 experts with sigmoid scores and a selection bias) | RDNA3.0 (gfx110x) | stock kernels. `GGML_CUDA_INK2_ANY_AMD=1` also enables them on the other AMD GPUs (RDNA3.5, RDNA4, RDNA1/2, GCN, CDNA): untested, the fused kernels assume 32-lane warps |
| quantized KV cache with 1 to 8 query rows (decode, verify batches) on the vector kernel, which reads it in place; for 2 to 8 rows over a q8_0 cache with head size 128 and a GQA ratio of 3, a kernel that serves the 3 query heads of a K/V head, also with several K/V streams and with a q4_0 V (any model with such a cache) | RDNA3.0 (gfx110x) | the stock choice (tile kernel with an F16 copy of the cache for some shapes) |
| shape of the stock Q8_0 mat-vec for one column | RDNA3.0 (mat-vec table `RDNA3_0`) | stock |
| branchless decode of the NVFP4 scales (same values) | RDNA3 and RDNA3.5 device code (gfx11) | stock |
| Inkling 2 attention without the far mode | ROCm devices: the dense path (the generic banded kernel of #386 was slower there); NVIDIA: the tensor-core banded kernel of #386; other backends: the path of the ports | |
| Inkling 2 graph changes (device-built masks, graph order), follow-up prompts on the far path, restore order of checkpoints, restored sliding-window states put back at position mod ring size, relative positions written in place on the host, several sequences per ubatch only for short steps and the compute-buffer reserve for it, the optional last layer on the last rows | every backend, Inkling 2 only (the restore placement also for its DSpark drafter) | |
| DSpark drafter changes, drafter injections of several slots in one decode, the optional window of the drafter's full-attention cache (`INKLING2_DRAFT_KV_WINDOW`) | every backend; the injections and the window for any drafter of the dflash architecture; target features from the device only when the first GPU is a CUDA or ROCm device; the device-side wait for the target batch only on ROCm | host copies and the host wait of the release |
| one wait for the sampled outputs of a decode instead of one per getter | every backend, every model | |
| no drafts while 3 or more slots generate (`INKLING2_SPEC_MULTI_NMAX`, default `0,3`) | llama-server, every model served with a drafter | |
| KQ mask fill of a standard sliding window of more than 4096 cells (same values) | every backend, every model with such a window (not with ALiBi) | |
| staged input uploads of the scheduler, no GPU wait before a CPU split after a GPU split | ROCm devices: one upload kernel per split on RDNA3.0, one asynchronous copy per input on the other AMD GPUs (untested there) | the synchronous copies and the wait of the release |
| headroom on device compute buffers when they are (re)allocated | every backend with device memory, every model | |
| sliding-window cache kept F16 when the KV cache is quantized; the head of a sliding-window cache after a tail removal and no restart at cell 0 there | every backend, every model with a sliding-window cache | |
| first KQ mask row of a sequence filled from the cell positions only when every used cell belongs to that sequence (same values) | every backend, every model whose KQ mask is filled on the host (not with ALiBi or M-RoPE) | |
| `INKLING2_CACHE_TAIL` (off by default): prompt-cache save and lookup when a slot would lose at least n tokens | llama-server, every backend and model, only when set | |

A build only contains kernels for the targets given at build time (`GPU_TARGETS`): build for your GPU. On an RDNA3.0
GPU other than gfx1100 run the verification below before anything else.

## Requirements

- An AMD GPU supported by ROCm/HIP with enough memory: the recommended setting below (16.4 GB file, drafter, 65536
  context) peaked at about 19.3 GB (19.05 GB dedicated + 0.25 GB shared), so a 24 GB GPU is the practical minimum to
  keep everything on the GPU (see "Context, ubatch and VRAM"). The speed-ups need an RDNA3.0 GPU (RX 7900 XTX / XT / GRE, RX 7800 XT, RX 7700 XT,
  RX 7600, Radeon PRO W7000, the Radeon 780M/760M integrated GPUs); others run at the speed of the release.
- The HIP SDK for Windows or ROCm on Linux. Measured with HIP SDK 7.2 on Windows; Linux was not tested with this branch.
- CMake and Ninja; on Windows the Visual Studio C++ build tools.
- Flash attention (`-fa 1`) and an F16 or BF16 KV cache (the default) for the fast path, or a q8_0 cache (`-ctk q8_0
  -ctv q8_0`) for long contexts (see "Context 131072"), or q8_0 K with q4_0 V (`-ctk q8_0 -ctv q4_0`, see "Contexts
  196608 and 262144"); other quantized KV caches fall back to the dense bias.

## Build

Windows (HIP SDK installed, `HIP_PATH` set by its installer), from the root of this repository:

```bat
set GPU_TARGETS=gfx1100
scripts\inkling2-amd\build-hip.cmd [build-dir]
```

Variables of the script: `GPU_TARGETS` (default gfx1100; a list such as `gfx1100;gfx1101` works), `VCVARS` (path of
`vcvars64.bat`; found with `vswhere` when unset), `INK_CMAKE` (extra configure options, e.g. `-DLLAMA_BUILD_TESTS=ON`),
`INK_TARGETS` (default `llama-server llama-bench llama-perplexity llama-cli llama-quantize`; add `test-backend-ops`
with the tests option). The build directory defaults to `build-hip` and the binaries land in `<build-dir>\bin`. The
configure step runs once per build directory. Options: `-DGGML_HIP=ON -DGGML_HIP_GRAPHS=ON -DGGML_HIP_NO_VMM=ON
-DGGML_NATIVE=ON`, the HIP SDK's clang as C and C++ compiler. `GGML_NATIVE=ON` tunes the CPU code for the build
machine: turn it off for binaries meant for other machines. With the default targets and one GPU target a full build
took about 8 minutes.

Linux (ROCm; not tested with this branch, same options except the Windows-only ones):

```sh
GPU_TARGETS=gfx1100     # your GPU: rocminfo | grep -m1 -o 'gfx[0-9a-f]*'
cmake -S . -B build-hip -G Ninja -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_HIP_COMPILER="$(hipconfig -l)/clang" -DGGML_HIP=ON -DGPU_TARGETS="$GPU_TARGETS" \
  -DGGML_HIP_GRAPHS=ON -DLLAMA_CURL=OFF
cmake --build build-hip --target llama-server llama-bench llama-perplexity llama-cli llama-quantize -j "$(nproc)"
```

## Run

```sh
MODEL=<path to Inkling-2-Mini-h6-lbf16-UD-Q4_K_M.gguf or the Unsloth file, see "Files" below>
DRAFT=<path to the DSpark drafter, see "Files" below>
llama-server -m "$MODEL" -ngl 99 -fa 1 -c 65536 -np 1 -b 2048 -ub 1024 --jinja \
  -md "$DRAFT" -ngld 99 --spec-type draft-dspark --spec-draft-n-max 3 --spec-draft-n-ubatch 512 \
  --backend-sampling --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
  --chat-template-kwargs '{"reasoning_effort":"high"}' --host 127.0.0.1 --port 8080
```

Stop it with Ctrl+C. In the Windows command prompt, end the lines with `^` instead of `\`, use `%MODEL%` and write the
JSON as `"{\"reasoning_effort\":\"high\"}"`.

- Files: unsloth/Inkling-2-Mini-GGUF now carries newer files for mainline llama.cpp under the first names (checked
  2026-11-23); they were not tested with this branch, which is built on the release b12568-mix-8eebad4. The files
  measured here are in that repository as `dspark-Inkling-2-Mini-Q8_0_Old.gguf` (the drafter, 402 278 560 bytes) and
  `Old_Support/Inkling-2-Mini-UD-Q4_K_M.gguf_file` (the Unsloth model file, 16 610 543 328 bytes; rename it to `.gguf`).
- `-ub 1024` reads prompts about 20 % faster than 512 and needs about 0.9 GB more; `-ub 2048` needed about 2 GB more
  and was not faster. The drafter reads the prompt by 512 (`--spec-draft-n-ubatch 512`); a drafter ubatch of 2048 was
  slower and used 1.5 GB more.
- `--backend-sampling` samples on the GPU: about 4 % faster writing with the drafter (four alternating A/B pairs on RX
  7900 XTX). The server turns it off by itself for requests with a grammar (tool calls), which then sample on the CPU.
- `--spec-draft-n-max 3` was the best draft length at short context and about as fast as 2 after a long prompt.
  Without a drafter, drop the `-md ... --spec-draft-n-ubatch 512` options.
- Sampling as recommended for the model (temperature 1.0, top-p 1.0, top-k 0, min-p 0). `reasoning_effort` takes none,
  minimal, low, medium, high or xhigh, or a number from 0 to 0.99.
- For a context of 131072 tokens see "Context 131072" (three options change), for 196608 and 262144 "Contexts 196608
  and 262144", for several conversations at once "Several slots", for image input "Images", and for a server that is
  loaded by the first request and stopped when idle "Load on first request".

## Context, ubatch and VRAM

Measured on RX 7900 XTX (24 GB) with the h6-lbf16 file and the command line above:

- weights: 16.44 GB file; the DSpark drafter 0.40 GB, plus about 55 MB for its precomputed head.
- KV cache: the 8 global layer applications keep a full F16 cache of 32.8 KB per token, 2 GiB per 65536 tokens (q8_0:
  17.4 KB per token, 1.06 GiB per 65536 tokens); the sliding-window cache stays small (1024-token window plus one
  ubatch) and F16.
- the whole server process (drafter on, context 65536, `-ub 1024`): a peak of 19.05 GB dedicated + 0.25 GB shared over
  a long run (2026-11-22). Memory becomes resident when it is first used: judge by the peak over a real workload, not by
  the figure at load.

Estimates, not measured: with the F16 cache each further 65536 tokens of context add about 2.1 GB, plus about 0.27 GB
for the drafter's cache; at 131072 with the drafter that is about 21.3 GB by the buffer sizes, more than a 24 GB card
leaves next to the display: use the q8_0 cache there (next section). Without the drafter about 1.5 GB less; `-ub 512`
about 0.9 GB less. Leave room for the display and other programs. On Windows an
overflow is not an error: buffers move to shared system memory and the speed collapses, so watch the shared GPU memory
of the process when the speed drops. GPUs with 16 or 20 GB cannot keep these settings on the GPU; partial offload
(`-ngl` below 99) was not measured.

## Context 131072

With the K/V cache of the 8 global layer applications in q8_0 and a drafter ubatch of 256, 131072 tokens fit on a 24 GB
card with the drafter. The command line of "Run" with `-c 131072`, `-ctk q8_0 -ctv q8_0` and
`--spec-draft-n-ubatch 256`:

```sh
llama-server -m "$MODEL" -ngl 99 -fa 1 -c 131072 -np 1 -b 2048 -ub 1024 --jinja -ctk q8_0 -ctv q8_0 \
  -md "$DRAFT" -ngld 99 --spec-type draft-dspark --spec-draft-n-max 3 --spec-draft-n-ubatch 256 \
  --backend-sampling --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
  --chat-template-kwargs '{"reasoning_effort":"high"}' --host 127.0.0.1 --port 8080
```

- Memory: the global cache takes 2.1 GiB at 131072 instead of 4 GiB in F16; the sliding-window cache and the drafter's
  cache stay F16. The far kernel reads the q8_0 cache through an F16 copy of 4 of the 8 K/V heads at a time (256 MiB at
  131072, `INKLING2_FAR_Q8_HEADS`). A drafter ubatch of 256 halves the drafter's compute buffer (about 0.15 GB less).
- Measured on RX 7900 XTX (2026-11-23), the 52 804-token prompt of "Measurements", then a 125 224-token prompt read in
  full: reading 2886-2901 tok/s and about 2190 tok/s, writing 114-117 tok/s and about 92 tok/s after them, VRAM peak
  19.58 GB dedicated + 0.25 GB shared, no growth of the compute buffers after load. At 65536 with the F16 cache the
  same prompt reads at 3048-3050 tok/s and writes at 110-111 tok/s: the q8_0 cache costs about 5 % of reading speed
  (the F16 copy per group of heads) and writes at least as fast (verify batches read it with the q8_0 kernel of "Which
  AMD GPUs").
- Quality (2026-11-22): perplexity 6.2667 against 6.2608 with the F16 cache (+0.09 %, same text and settings as the dated
  lines under the 65536 table). KL divergence of the q8_0 run against the F16 run: 0.0022, below the 0.0029 that the same F16 cache
  gives through the dense attention path instead of the far kernel, i.e. within the rounding noise of the attention
  kernels.
- Margin: measured with about 3 GB of the card held by other programs (display included). With more held elsewhere,
  watch the shared GPU memory of the process: if it moves by about 0.5 GB and writing collapses, set
  `INKLING2_FAR_Q8_HEADS=2` (128 MiB less, a 125k-token prompt reads about 15 % slower) or use `-ub 512`.

## Contexts 196608 and 262144

Two options, off by default, shrink the caches further: a 4-bit V for the 8 global layer applications (`-ctv q4_0` with
`-ctk q8_0`) and a window for the drafter's full-attention cache (`INKLING2_DRAFT_KV_WINDOW=32768`: the drafter keeps
the last 32768 positions instead of the whole context; the target checks every drafted token, so only the acceptance of
the drafts can change). At 262144 the far op also reads 2 K/V heads per group (`INKLING2_FAR_Q8_HEADS=2`):

```sh
INKLING2_DRAFT_KV_WINDOW=32768 INKLING2_FAR_Q8_HEADS=2 \
llama-server -m "$MODEL" -ngl 99 -fa 1 -c 262144 -np 1 -b 2048 -ub 1024 --jinja -ctk q8_0 -ctv q4_0 \
  -md "$DRAFT" -ngld 99 --spec-type draft-dspark --spec-draft-n-max 3 --spec-draft-n-ubatch 256 \
  --backend-sampling --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
  --chat-template-kwargs '{"reasoning_effort":"high"}' --host 127.0.0.1 --port 8080
```

For 196608: `-c 196608` and only `INKLING2_DRAFT_KV_WINDOW=32768` (4 heads per group, the default). In the Windows command
prompt set the two variables first (`set INKLING2_DRAFT_KV_WINDOW=32768`).

- Measured on RX 7900 XTX (2026-11-23) with about 2.7 GB of the card held by other programs. 262144: reading 2662 tok/s
  on the 52 804-token prompt, 1845 tok/s on a 125k-token prompt and 1195 tok/s on a 249 584-token prompt, writing 100 /
  88 / 70 tok/s after them, VRAM peak 20.28 GB dedicated + 0.23 GB shared. 196608: reading 2191 tok/s on the 125k prompt
  and 1833 tok/s on a 183.5k-token prompt, writing 88 / 86 tok/s, peak 19.59 + 0.23 GB (the peak of the 131072 setting).
- Near the memory limit of the card: with 4 K/V heads per group, 262144 sits about 0.26 GB higher and every drafter step
  takes about 6 ms more, while the shared memory of the process does not move (no visible spill). 2 heads per group
  remove that for a slower reading (-7 % at 52.8k, -15 % at 125k, -22 % at 250k). With more of the card used by other
  programs, take 196608, or 262144 without the drafter (`-ctk q8_0 -ctv q4_0`, no drafter options, no variables: 250k read
  at 1573 tok/s, written at 55 tok/s).
- Quality: against an F16 cache, the 4-bit V adds 0.0003 to 0.001 of mean KL divergence over a q8_0 V, about what
  changing the attention kernel on the same F16 cache gives. The drafter window costs acceptance when the prompt is a
  little longer than the window (52.8k: about 8 % slower writing) and almost nothing at 125k: leave it off at 65536 and
  131072.
- The 249 584-token prompt repeats a text, so acceptance and reading speed in a real conversation of that length may
  differ.

## Several slots

`-np N` gives N slots of `-c / N` cells each (a longer conversation is cut). Decode and verify steps of several slots run
as one ubatch with the fused kernels for several sequences; prompts are still read one at a time, on the far path. While
3 or more slots generate, no slot drafts (`INKLING2_SPEC_MULTI_NMAX`, default `0,3`); 2 slots keep drafting. Do not use
the unified cache (`-kvu`): it leaves the far path.

```sh
llama-server -m "$MODEL" -ngl 99 -fa 1 -c 49152 -np 4 -b 2048 -ub 1024 --jinja \
  -md "$DRAFT" -ngld 99 --spec-type draft-dspark --spec-draft-n-max 3 --spec-draft-n-ubatch 512 \
  --backend-sampling --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
  --chat-template-kwargs '{"reasoning_effort":"high"}' --host 127.0.0.1 --port 8080
```

- Measured on RX 7900 XTX (2026-11-23), 4 conversations of about 10k tokens each generated at once (greedy, 400 tokens
  each): 171-179 tok/s in total (171 with the drafter loaded, 179 without it), against about 110 tok/s for one
  conversation at a time; VRAM peak 19.44 + 0.19 GB with the drafter, 18.46 + 0.15 GB without.
- Longer conversations: `-c 131072 -ctk q8_0 -ctv q8_0 -np 4` (4 x 32768 cells), without the drafter options: 4
  conversations of about 30k tokens wrote 159-160 tok/s in total, peak 19.11 + 0.16 GB (one revision earlier). With
  `--cache-ram` (the RAM prompt cache), more conversations than slots can take turns with less prompt reading.
- One slot for a coding agent with sub-agents: the conversations take turns on the slot, and `--cache-ram 16384` with
  `INKLING2_CACHE_TAIL=2048` keeps the one that leaves the slot in system RAM. One real session of a coding agent with
  three sub-agents on the command line of "Context 131072" with `--cache-ram 16384` (2026-11-23): 94 s and about 95k
  prompt tokens read over the session without `INKLING2_CACHE_TAIL`, about 64k with it (one session each).

## Images

Inkling 2 Mini reads images through its vision projector, `mmproj-F16.gguf` of unsloth/Inkling-2-Mini-GGUF
(639 348 160 bytes, sha256 `3bff75ffeb2d6e0371ba7bd42e30d26a7d98aea681fa44b03b5a20891cfa2c5f`). Add
`--mmproj <that file> --no-mmproj-offload` to a command line above. The branch does not change the image code of the
release.

Measured on RX 7900 XTX (2026-11-23) with the h6-lbf16 file and the command line of "Context 131072", drafter loaded:

- `--no-mmproj-offload` keeps the image encoder in system RAM: the server takes 19.58 GB of the card, as without the
  projector. An image of 640x400 costs about 1 s, a 1920x1080 screenshot about 15 s. The words, numbers, shapes and
  colours of generated test images were read correctly, also the 11 pt text of a 1920x1080 screenshot, and drafting
  keeps working.
- With the encoder on the GPU (no `--no-mmproj-offload`) the server takes 20.65 GB and wrote more slowly on the same
  requests (107-125 against 122-136 tok/s).
- A large image makes the compute buffer grow once (634 to 1092 MiB at about 1300 image tokens): the server went from
  19.5 to 20.7 GB and stays there until it is restarted, so leave about 1.2 GB of the card free for it.
  `--image-max-tokens 512` (and 1024) avoided the growth, but the dense screenshot then got empty answers: no cap is
  recommended.

## Load on first request

`scripts/inkling2-amd/wake-gateway.py` (Python 3.9 or later, standard library only) keeps one port open while no model
is loaded. The first POST request starts llama-server with the command line given after `--`, later requests are
forwarded, and after `--idle-minutes` without a request the server is stopped, which frees the card:

```sh
python scripts/inkling2-amd/wake-gateway.py --listen 127.0.0.1:8080 --backend-port 8081 --idle-minutes 15 \
  --model-id inkling-2-mini -- \
  llama-server -m "$MODEL" -ngl 99 -fa 1 -c 131072 -np 1 -b 2048 -ub 1024 --jinja -ctk q8_0 -ctv q8_0 \
  -md "$DRAFT" -ngld 99 --spec-type draft-dspark --spec-draft-n-max 3 --spec-draft-n-ubatch 256 \
  --backend-sampling --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 \
  --chat-template-kwargs '{"reasoning_effort":"high"}' --host 127.0.0.1 --port 8081
```

Clients use the port of the gateway (8080 here). Environment switches set for the gateway reach the server.

- Streamed requests get the 200 status and the SSE headers at once and an SSE comment every 10 s while the model loads
  or the request waits for the slot, so that clients and relays in between keep the connection; when the client leaves,
  the request is cancelled on the server. Requests that are not streamed wait without a keep-alive.
- `GET /v1/models` and `GET /health` are answered by the gateway while no model is loaded (they do not load it);
  `GET /__wake_status` gives the state as JSON. The output of the server goes to `--server-log`.
- Only a server that the gateway started is stopped; one that already answers on the backend port is used and left
  running. The server ends with the gateway (on Windows also when the gateway is killed). To keep the gateway after the
  terminal session that started it ends, start it from a service or a logon task.
- Tested on Windows with RX 7900 XTX (2026-11-23), the command line above plus the projector options of "Images" and
  `--cache-ram 16384`: the first streamed request answered after 16 s (model load 13 s, files in the file cache of the
  system), a request without stream and an image request went through, the server was stopped after one idle minute
  (`--idle-minutes 1`; the check runs every 30 s) and the next request loaded it again in 15 s. Not tested on Linux.

## Environment switches

Everything below is off or at its fast default when unset. The switches of the first table restore the previous
behaviour of one change, for A/B tests and bisection.

| switch | default | when set |
|---|---|---|
| `GGML_CUDA_INK2_ANY_AMD=1` | off | the GPU paths of this branch on every AMD GPU, not only RDNA3.0 (untested) |
| `GGML_CUDA_INK2_FORCE_STOCK=1` | off | the stock paths on RDNA3.0 too (what other GPUs get) |
| `INKLING2_FAR=0` | on | no far mode: back to the banded or dense path of the ports |
| `INKLING2_SWA_ROT=0` | on | a wrapped sliding-window cache falls back to the dense bias |
| `INKLING2_BANDED=0` | on | the chunked dense path even where the banded op is supported |
| `INKLING2_KQ_BIAS_LOG2=n` | 23 / 29 | budget of the dense bias per attention call, 2^n elements (16..32); 23 where the far op runs, 29 elsewhere |
| `INKLING2_FAR_MIN=n` | 64 | far mode for ubatches from n tokens; lower values break the graph reuse of the verify batches and are slower |
| `INKLING2_MASK_DEV=0` | on | KQ masks filled on the host |
| `INKLING2_FAR_MASK_COPY=1` | off | one copy of the mask per far call |
| `INKLING2_FAR_CAUSAL=0` | on | the global cache in far mode gets its causal mask as a tensor again (built on the device and scanned) instead of the kernel applying it from the positions |
| `INKLING2_MASK_CLAMP_COPY=1` | off | the device-built mask is clamped into a copy (one more [n_kv, n_ubatch] tensor in the compute buffer) |
| `INKLING2_RELPOS_FAST=0` | on | the relative positions of a ubatch filled per cell and token through a temporary vector, then copied, instead of written in place into the host input from one pass over the cell positions (same values; about 0.6 ms more host time per 4-token verify batch at 125k cells) |
| `INKLING2_MASK_FAST=0` | on | the first KQ mask row of a sequence reads the sequence set of every cell even when every used cell carries that sequence (same values; about 0.1 ms more per 4-token verify batch at 125k cells); every model whose KQ mask is filled on the host |
| `INKLING2_MASK_WIN_IDX=0` | on | the KQ mask fill of a standard sliding window of more than 4096 cells (the drafter window below) records every cell of the window for the other rows of a sequence, instead of only the cells near the batch positions and near the window edge (same values; with the drafter window about 1 ms more per drafting step at 52.8k); every model with such a window |
| `INKLING2_FAR_Q8=0` | on | a q8_0 cache falls back to the dense bias instead of the far op |
| `INKLING2_FAR_Q8_HEADS=n` | 4 | K/V heads per far op with a q8_0 cache; each op reads its heads through an F16 copy (4 of 8: two ops, a 256 MiB copy at 131072; 2: 128 MiB less, about 15 % slower on a 125k-token prompt; 8: one op with a 512 MiB copy at 131072, which in an earlier revision left the process at the edge of the card's memory and made writing collapse) |
| `INKLING2_SWA_KV_F16=0` | on | with a quantized KV cache the sliding-window cache is quantized too (by default it stays F16, read in place by the far op); every model with a sliding-window cache |
| `INKLING2_SWA_HEAD_FIX=0` | on | a sliding-window cache puts the next token in the lowest freed cell after a tail removal, and can restart at cell 0 after a restore (the holes this leaves in the ring send follow-up prompts to the dense fallback); every model with a sliding-window cache |
| `GGML_ALLOC_HEADROOM_MIB=n` | 64 / quarter | extra MiB for a device compute buffer when it is (re)allocated; default 64 for buffers of 160 MiB or more, a quarter of the size below (at least 4); `=0`: none, as upstream. A device compute buffer that still grows after its first allocation is reported with a warning |
| `INKLING2_REL_SUB=1` | off | the sinks subtracted from the bias table by a separate op |
| `INKLING2_REL_FLAT=0` | on | the bias table of the far op multiplied in the form broadcast over the tokens (on ROCm one small GEMM per token, about 3x slower) |
| `INKLING2_BATCH_OPT_OFF=1` | off | previous graph layout (mix rows copied one by one, one zero-sink tensor per call, convolutions not reordered) |
| `INKLING2_RESTORE_ORDER=0` | on | the cells of a sliding-window sequence restored from a checkpoint keep their saved order (the ring then no longer reads as one rotation) |
| `INKLING2_RESTORE_MOD=0` | on | a sliding-window sequence restored from the RAM prompt cache, a slot file or a checkpoint goes back from the first free cell instead of position p to cell p mod size, where the kept sequence holds it: the same values in other cells, so every later token rounds differently from the kept sequence and at temperature 1 the text can differ; Inkling 2 and its DSpark drafter |
| `GGML_CUDA_INK2_NO_FUSE=1` | off | no fused kernel of this branch |
| `GGML_CUDA_INK2_FUSE_MASK=bits` | all | fused kinds: 1 L2 clip, 2 depth mix, 4 loop gate, 8 short-conv tail, 16 SITU activation, 32 MoE weight normalisation, 64 short-conv input and state store, 128 relative-bias chain, 256 short-conv rollback store, 512 dynamic conv, 1024 full short conv, 2048 gate tail, 4096 first maximum of a row (the drafter's token pick), 8192 SITU activation written by the FP16 expert kernel of prompt batches, 16384 the down projection of the same experts in that call (needs 8192) |
| `GGML_CUDA_INK2_CLIP_SCALED=0` | on | the multiplication by the clip weight stays a separate kernel |
| `GGML_CUDA_INK2_GATE_MT=0` | on | the first version of the loop-gate kernels |
| `GGML_CUDA_INK2_GATE_N=0` | on | the q, k and v loop gates of a looped visit in three launches of each gate kernel instead of one (same results bit for bit) |
| `GGML_CUDA_INK2_GATE_PP=0` | on | the loop controllers of prompt batches (more than 16 tokens) as generic BF16 products plus the fused tail instead of three WMMA kernels (the fused kernels keep two products in F32: rounding level) |
| `GGML_CUDA_INK2_POST=0` | on | the row ops after the projections of a layer application (q, r and k clips, v RMS norm, the products by the log-scaled positions, the K/V stores) one launch each instead of one launch in all (batches of up to 16 tokens; same results bit for bit) |
| `GGML_CUDA_INK2_SCONV_PAIR=0` | on | the K and V short convolutions of a layer in two launches instead of one (same results bit for bit) |
| `GGML_CUDA_INK2_ROUTER=0` | on | the MoE router's top-k and its weight normalisation in two launches instead of one (same results bit for bit) |
| `GGML_CUDA_INK2_TOPK_RANK=0` | on | the router's top-k by rounds of warp argmax (upstream's kernel) instead of one rank per expert (128 experts, sigmoid scores and a selection bias; same ids and weights) |
| `GGML_CUDA_INK2_MULTISEQ=0` | on | the fused short-convolution and relative-bias kernels only for steps of one sequence: steps of several slots run the generic ops (about 3090 instead of 1680 launches per step with 4 slots) |
| `GGML_CUDA_INK2_MIX_REG=0` | on | the depth mix with its element loop (one memory latency per element, each state read twice) instead of the elements of a thread held in registers (n_embd 2304; same results bit for bit) |
| `GGML_CUDA_INK2_SCONV_REG=0` | on | the short convolution with its tap loop instead of unrolled taps (3 past rows; same results bit for bit) |
| `GGML_CUDA_INK2_Q8_GROUP=0` | on | no grouping of the Q8_0 products that share their activations |
| `GGML_CUDA_INK2_Q8_GROUP_MULTI=0` | on | Q8_0 product groups only over the same activations, not also over other activations of the same shape computed before the group (same results bit for bit) |
| `GGML_CUDA_INK2_MMV_F32=0` | on | the stock Q8_0 mat-vec (activations quantized to q8_1 first) |
| `GGML_CUDA_INK2_Q8_NR`, `GGML_CUDA_INK2_Q8_WPB` | tuned | rows per warp and warps per block of that kernel, comma lists per column count (tuning) |
| `GGML_CUDA_INK2_MOE_RPB=n` | 4 | rows per block of the NVFP4 MoE mat-vec: 1, 2, 4 or 8 (upstream: 2) |
| `GGML_CUDA_INK2_MOE_SLOTFAST=0` | on | row-fast grid order of the NVFP4 MoE mat-vec (one pass over the weight rows per expert slot) instead of slot-fast |
| `GGML_CUDA_INK2_RELBIAS_KT=0` | on | the element-wise relative-bias kernel of decode / verify batches (one thread per value) instead of one thread per key and token |
| `GGML_CUDA_INK2_MOE_F16=n` | 32 | NVFP4 expert products (`MUL_MAT_ID`) of n tokens or more on FP16 WMMA, fewer tokens on MMQ; `=0`: always MMQ (int8 products on q8_1 activations) |
| `GGML_CUDA_INK2_MOE_F16_Q=n` | 256 | Q8_0 and Q5_K expert products (the last 4 layers of the UD-Q4_K_M files) of n tokens or more on the same FP16 kernel; `=0`: always MMQ |
| `GGML_CUDA_INK2_MOE_LDS1=0` | on | two shared-memory buffers in the NVFP4 FP16 expert kernel instead of one (one buffer: twice the blocks per compute unit) |
| `GGML_CUDA_INK2_MOE_TN96=0` | on | tiles of 64 tokens instead of 96 in the NVFP4 FP16 expert kernel with one shared-memory buffer (96 tokens: 31.5 KB, still two blocks per compute unit, one tile instead of two for an expert with 65 to 96 tokens; same results bit for bit) |
| `GGML_CUDA_INK2_MOE_Q_TN96=0` | on | the Q8_0 and Q5_K expert products of the FP16 expert kernel (the last 4 layers of the UD-Q4_K_M files) in tiles of 64 tokens with two shared-memory buffers instead of 96 tokens with one (same perplexity and answers) |
| `GGML_CUDA_INK2_MOE_SMALLN=0` | on | a tile of up to half the tile width (32 or 48 tokens) of the FP16 expert kernel runs on 4 of its 8 warps, as before, instead of all 8 |
| `GGML_CUDA_INK2_MOE_FFN=0` | on | the expert gate_up projection with its SITU activation and the down projection of prompt batches as two calls (the activation written in F32, then converted to FP16 by the down call, and a second expert sort) instead of one call that keeps the activation in FP16 (same results bit for bit; about 1 % faster prompt reading); same as `GGML_CUDA_INK2_FUSE_MASK` without 16384 |
| `GGML_CUDA_INK2_FA_TILE1=0` | on | a single query row with a per-head mask goes back to the vector kernel |
| `GGML_CUDA_INK2_FA_QVEC=0` | on | a quantized cache with up to 8 query rows gets the stock kernel choice again (the tile kernel copies the whole K/V view to F16 at every call) instead of the vector kernel |
| `GGML_CUDA_INK2_FA_Q8GQA=0` | on | verify batches (2 to 8 rows) over a q8_0 cache on the stock vector kernel (one block per query head) instead of the kernel shared by the 3 query heads of a K/V head |
| `GGML_CUDA_INK2_FA_Q8GQA_MS=0` | on | with several K/V streams (several slots) the q8_0 decode and verify rows go to the vector kernel instead of the 3-head q8_0 kernel |
| `GGML_CUDA_INK2_FA_Q8GQA_V4=0` | on | verify batches over a q8_0 K with a q4_0 V go to the vector kernel instead of the 3-head kernel |
| `GGML_CUDA_INK2_FA_LIVE=0` | on | no skip of the fully masked K/V blocks (`=2`: host check of the block bits, debug, needs `GGML_CUDA_DISABLE_GRAPHS=1`) |
| `GGML_CUDA_INK2_FA_GQA3=n` | 16 | queries per tile of the 3-head flash-attention tiles (batches of more than 16 tokens): `=0` back to 4 heads per tile with a padding column, `=32` tiles of 32 queries for batches of more than 32 tokens |
| `GGML_CUDA_DISABLE_BANDED_MMA=1` | off | (from #386, NVIDIA) no tensor-core banded kernel |
| `INKLING2_DSPARK_HEADC=0` | on | no precomputed drafter head: one product with the output matrix per drafted position |
| `INKLING2_DSPARK_DEV=0` | on | drafter features through host copies |
| `INKLING2_DSPARK_DEVSEL=0` | on | the drafting graph builds the logits of the drafted positions again and the host samples them (same drafts, slower) |
| `GGML_SCHED_ASYNC_INPUTS=n` | 1 | `=0`: one synchronous copy per input, as in the release; `=3`: one asynchronous copy per staged input instead of the batched upload kernel; `=2`: the staged uploads on any GPU backend with asynchronous copies, not only ROCm (untested) |
| `GGML_SCHED_CPU_SPLIT_WAIT=1` | off | the scheduler waits for the GPU again before a CPU split that follows a GPU split |
| `INKLING2_INJECT_DEVWAIT=0` | on | the drafter waits for the target batch on the host |
| `INKLING2_DSPARK_ALL=1` | off | every position of a draft block is an output |
| `INKLING2_DSPARK_ALL_ROWS=1` | off | logits for every row of large drafter ubatches |
| `INKLING2_DRAFT_RESERVE_ALL=1` | off | drafter compute buffer reserved for n_batch outputs |
| `INKLING2_SAMPLED_SYNC=0` | on | one synchronization per sampling getter (tokens, probabilities, logits, candidates) instead of one per decode outputs; every model |
| `INKLING2_MULTI_RESERVE=0` | on | with several slots (separate K/V streams), the equal split of the release (prompts of several slots in one dense ubatch) and a compute buffer reserved for that dense path (0.7-0.8 GiB more with 2 or 4 slots) |
| `INKLING2_INJECT_BATCH=0` | on | one drafter injection per slot when every slot of a step brings one row, instead of one decode for all of them |
| `INKLING2_SPEC_MULTI_NMAX=k[,n]` | 0,3 | each slot drafts at most k tokens while at least n slots (at least 2) generate; `=-1`: no cap, as in the release. Default: no drafts while 3 or more slots generate (4 slots with the drafter: 152 tok/s in all instead of 121); llama-server, every model with a drafter |

Build-time flags (`-DCMAKE_CXX_FLAGS=-D...`, not needed normally): `GGML_CUDA_INK2_UE4M3_LDEXP` (previous ldexpf
decode of the NVFP4 scales), `INK2_Q8_NWARPS` and `INK2_Q8_RPB` (shape of the stock Q8_0 mat-vec for one column, default
2 warps and 1 row), `INK2_MMVF8_BYTES` and `INK2_MMVF8_WARPS` (shape of the F32-activation Q8_0 kernel, default 16 bytes
per lane and 1 warp), `GGML_CUDA_INK2_FA_NO_SCHED` (no scheduling barriers in the 3-head flash-attention tiles; the
barriers keep the fragment loads next to their WMMA and reduce register spills), `GGML_CUDA_INK2_FA_RDNA_48` and
`GGML_CUDA_INK2_FA_RDNA_96` (configs of the 3-head tiles of 16 and 32 queries, default `96,2,64,64,64,64,1,true` and
`192,1,64,64,64,64,1,true`: threads, occupancy, nbatch_fa, nbatch_K2, nbatch_V2, nbatch_combine, nstages_target,
Q_in_reg), `GGML_CUDA_INK2_FA_RDNA_32` and `GGML_CUDA_INK2_FA_RDNA_64` (same format, override the RDNA configs of the
32- and 64-column tiles of head size 128; unset by default: tuning only), `GGML_CUDA_INK2_COST_TOOLS` (compiles in the
timing-only switches of the last table, which give wrong results, the timing-only build flag `GGML_CUDA_INK2_FA_NO_NEAR`
(no near-band relative bias in the far tiles, wrong results), and the head-mask WMMA experiment
`GGML_HIP_FATTN_WMMA_HEADMASK=n`, which can hang the GPU).

Benchmark aids: `INKLING2_N_RS_SEQ=n` (read by llama-bench only) sets the recurrent rollback depth; with `=3`, llama-bench
builds the graph that llama-server uses for the target model with a drafter of n-max 3. `LLAMA_BENCH_GEN_BATCH=B` makes
llama-bench generate in steps of B tokens, all with logits, like verify batches.

Options, off by default (not used for the measurements of this section):

| switch | when set |
|---|---|
| `INKLING2_CACHE_TAIL=n` | llama-server with `--cache-ram`: a slot is also saved to the RAM prompt cache, and the next prompt looked up there, when that prompt would drop at least n tokens of the slot (otherwise only when it keeps less than half of them). Conversations that share a long system prompt and take turns on one slot keep more than half of each other's tokens, so without it each switch reads the other conversation's tail again: two conversations of a 20k-token shared prompt and about 3.4k tokens of their own, `=2048`: 15-17 tokens read per switch instead of 3361-3753 (0.28-0.33 s with the save and the restore, instead of 1.35-1.53 s). Off by default because a client that drops the reasoning of the previous turn loses more than n tokens at every turn and would then pay a save (about 0.2-0.5 s) per turn. Every model |
| `INKLING2_DRAFT_KV_WINDOW=n` | the full-attention layer of a dflash-architecture drafter (the DSpark drafter) keeps a ring of the last n positions plus one ubatch, with the standard sliding-window rule, instead of the whole context, when the context is longer (n = 32768 at 262144: 129 MiB instead of 1 GiB). The target verifies every drafted token, so only the acceptance changes: about 8 % slower writing on a 52.8k prompt, about 1 % on 125k; meant for contexts of 196608 and more (see "Contexts 196608 and 262144") |
| `INKLING2_LAST_ROWS=n` | n >= 16, 256 recommended: when nothing reads the final features of every token (no drafter) and the outputs are the last rows of a one-sequence prompt batch of more than n tokens, the last layer application computes only its last n rows after storing the K/V of every token; other kernel shapes for those rows, so results change at rounding level; never applies with the drafter |
| `GGML_CUDA_INK2_MOE_VDR2=1` | RDNA3.0: the NVFP4 expert mat-vec of 2 to 8 tokens (verify batches) with 2 ints per thread and step instead of 4; about 0.4 ms less per 4-token verify batch, but the partial sums are grouped differently (decode-path perplexity 6.1857 against 6.1776 with 4 ints) |

Measurement switches, off (correct results, kept for A/B tests; neither paid off on RX 7900 XTX): `GGML_CUDA_INK2_Q8_BLAS=n`
sends the dense Q8_0 products of n columns or more to dequantization + hipBLAS instead of MMQ (faster for some shapes,
slower for others, FP16 accumulation: perplexity +0.1 %); `GGML_CUDA_INK2_BLAS_F32OUT=1` asks F32 output and accumulation
for the F16 / BF16 hipBLAS products (5-6x slower).

<details>
<summary>Diagnostics only (print to stderr; some synchronize the GPU after every node)</summary>

| switch | what it does |
|---|---|
| `GGML_CUDA_INK2_VERIFY=1` | runs every fused pattern with the generic ops too and prints the largest normalized error per kind at exit (with `GGML_CUDA_DISABLE_GRAPHS=1`; used by check.ps1); a comparison with a NaN shows as `max nmse nan, NaN in n comparisons` |
| `GGML_CUDA_INK2_VERIFY_POISON=1` | with the self-check: test of the check itself, the host copy of the first fused output of each kind gets a NaN and every kind must then report `max nmse nan` |
| `GGML_CUDA_INK2_VERIFY_EVERY=n` | with the self-check: also print the running result every n comparisons, with the count of multi-sequence ones (a server that is stopped runs no exit handler) |
| `GGML_CUDA_INK2_CMP=mix,sconv,moe,ffn,post,sconv2,router,gaten` | with `GGML_CUDA_DISABLE_GRAPHS=1`: the kernels named (register depth mix, unrolled short convolution, 96-token expert tiles, expert gate_up and down projection in one call, row ops after the projections in one launch, K and V convolutions in one launch, top-k with the weight normalisation, three loop gates in one launch) also run their previous form into scratch memory and the two outputs are compared bit for bit on the host; a count every 500 calls and at each call with differences (expected: 0 differing values) |
| `GGML_CUDA_INK2_MOE_HIST=1` | with `GGML_CUDA_DISABLE_GRAPHS=1`: tokens per expert of the FP16 expert calls and the tiles that widths of 32, 64, 96 and 128 tokens would run (one line every 44 calls) |
| `GGML_CUDA_INK2_TRACE=1` or `=2` | histogram of the launches of the last large graph, `=2` with a time per launch (synchronizes every node; used by check.ps1) |
| `GGML_CUDA_INK2_TRACE=3`, `GGML_CUDA_INK2_TRACE_SPIN_US=us` | with `GGML_CUDA_DISABLE_GRAPHS=1`: a one-thread kernel writes the GPU clock before every launch of the traced graphs, averaged per graph size and printed at exit; a spin kernel of `TRACE_SPIN_US` microseconds (default 40000) holds the GPU while the host queues the graph. Meaningful for decode graphs; in prompt graphs host time dominates the deltas |
| `GGML_CUDA_INK2_SEQ=start,count` | with the trace: the launches of a node range of the second large graph |
| `GGML_CUDA_INK2_TRACE_NODES=min,max` | with the trace: the graphs it looks at, by node count (default 5000 and up, the target model's graphs; a window of a few hundred nodes selects the drafter's drafting graph) |
| `GGML_CUDA_INK2_TRACE_AT=n` | with the trace: also print the histogram (with `=3` the averages) of the n-th traced graph while running (a server that is killed runs no exit handler) |
| `GGML_INK2_VIDMEM=1` | Windows: the video memory of the process as the OS accounts it (dedicated and shared usage with their budgets, from DXGI) at every device allocation of 1 MiB or more and whenever the usage moved by 2 MiB |
| `GGML_CUDA_INK2_TIMELINE=1` | one line per device interaction (graph launch and end, stream and event waits, copies, batched uploads) and per host stage of a ubatch, microsecond clock; no added synchronization, but the buffered writes add about 0.3-2 ms per decoding step, and lines still in the buffer are lost when the process is killed |
| `GGML_CUDA_INK2_DEBUG=1` or `=2` | matcher logs; `=2` also counts fused launches |
| `GGML_CUDA_INK2_RAW=start,count`, `GGML_CUDA_INK2_DUMP=start,count` | with the debug logs: the nodes of a range, all of them or the real ops with the fused patterns |
| `GGML_CUDA_INK2_TIME=1` or `=2`, `GGML_CUDA_INK2_TIME_MIN=n` | host enqueue time and GPU tail of large graphs (needs `GGML_CUDA_DISABLE_GRAPHS=1`) |
| `GGML_CUDA_INK2_RELBIAS_LOG=1` | shapes of the fused relative-bias calls |
| `GGML_CUDA_POOL_LOG=1` | every new buffer of the CUDA memory pool |
| `GGML_CUDA_MEM_TRACE=1` | nodes after which the free device memory drops (synchronizes every node) |
| `GGML_SCHED_TIME=1` | split, wait and allocation time of the scheduler |
| `GGML_ALLOC_TOP=MiB`, `GGML_ALLOC_GROWTH=1` | large tensors of a reserved graph; growth of a compute buffer after its first allocation (without it, device compute buffers still get a one-line warning per growth) |
| `INKLING2_MASK_TIME=1` | host time of the KQ mask fills |
| `INKLING2_RING_LOG=1` | why a ubatch cannot read the sliding-window ring as a rotated ring (cell runs) |
| `INKLING2_HOST_TIME=1` | host stages of each ubatch and of the drafter injections |
| `INKLING2_STEP_LOG=1` | one line per decoding step (costs about 15 % by itself) |
| `INKLING2_INJECT_TIME=1` | time of the drafter injection (serializes the two contexts) |
| `INKLING2_DRAFT_LOG=1` | the drafted tokens of every step |
| `GGML_CUDA_INK2_SKIP_KIND=bits` | builds with `GGML_CUDA_INK2_COST_TOOLS` only; wrong output, timing only: the fused kernels of these kinds are not run |
| `GGML_CUDA_INK2_SKIP_OP="KEY;KEY"` | same build only; wrong output: single nodes with these trace keys are not run |
| `GGML_CUDA_INK2_SKIP_MMVQ=type` | same build only; wrong output: mat-vec products of that weight type are not run |
| `INKLING2_NOBIAS=1` | same build only; wrong output: the relative bias is dropped |
| `INKLING2_SKIP_INJECT=1` | same build only; worse drafts: the drafter does not read the prompt |

</details>

## Verify

Run this first on any GPU, and always under a time limit: a kernel variant that is not compiled for the device prints
"no device code" and then hangs at 0 % GPU (rebuild with the right `GPU_TARGETS`).

Windows: `scripts/inkling2-amd/check.ps1` does all of it with a time guard (paths are parameters; `-Bin` defaults to
`build-hip\bin` of this repository):

```powershell
.\scripts\inkling2-amd\check.ps1 -Model $env:INKLING_MODEL
.\scripts\inkling2-amd\check.ps1 -Model $env:INKLING_MODEL -Env @{INKLING2_N_RS_SEQ='3'}
```

Linux or by hand, the same steps (`MODEL` and `BIN` set by you):

```sh
export GGML_CUDA_DISABLE_GRAPHS=1
GGML_CUDA_INK2_VERIFY=1 timeout 300 "$BIN/llama-bench" -m "$MODEL" -ngl 99 -fa 1 -p 256 -n 24 -r 1
GGML_CUDA_INK2_VERIFY=1 LLAMA_BENCH_GEN_BATCH=4 timeout 300 "$BIN/llama-bench" -m "$MODEL" -ngl 99 -fa 1 -p 0 -n 16 -d 64 -r 1
GGML_CUDA_INK2_TRACE=1 timeout 300 "$BIN/llama-bench" -m "$MODEL" -ngl 99 -fa 1 -p 0 -n 8 -r 1
unset GGML_CUDA_DISABLE_GRAPHS
for f in 1 ""; do GGML_CUDA_INK2_NO_FUSE=$f timeout 600 "$BIN/llama-bench" -m "$MODEL" -ngl 99 -fa 1 -p 2048 -n 128 -b 2048 -ub 512 -r 2; done
```

1. Self-check: every fused pattern is computed with the generic ops and with the fused kernel on the real model data.
   Expected (measured on RX 7900 XTX): one `ink2 verify <kind>` line per kind at exit with a max nmse of 0 or below
   1e-11. `sconv_full` and `sconv_in` report their patterns as not comparable: their output overwrites one of their inputs
   by design. With
   the h6-lbf16 file the loop gate of the 4-token batches shows about 5e-5, because the generic reference rounds its
   activations to BF16, and `moe_ffn` (expert gate_up, activation and down projection in one call) about 2e-10, because
   its reference takes the activation of the generic SITU op, which rounds differently (`GGML_CUDA_INK2_CMP=ffn`
   compares it with the two separate calls bit for bit); `gate_pp` (loop controllers of prompt batches) about 5e-5 too,
   because the fused kernels keep two products in F32 that the generic path rounds to BF16. A larger error means a fused kernel is wrong on that GPU: run with `GGML_CUDA_INK2_NO_FUSE=1`
   and report it. No `ink2 verify` line at all means the GPU paths are off (not an RDNA3.0 GPU).
2. Trace: about 1215 launches per generated token.
3. Speed with and without the fusions of this branch (llama-bench, pp2048 and tg128, `-ub 512`).

test-backend-ops (build with `-DLLAMA_BUILD_TESTS=ON`, run it under a time limit too): `test-backend-ops -b ROCm0 -o
FLASH_ATTN_EXT_BANDED` checks the far mode against the CPU (padding, rotations, sliding windows; on gfx1100 two random
cases with 33 792 keys sit at the 1e-3 NMSE threshold), `-o MUL_MAT` and `-o MUL_MAT_ID` cover the Q8_0 and NVFP4
mat-vec kernels and the FP16 expert kernel for NVFP4, Q8_0 and Q5_K experts (`GGML_CUDA_INK2_MOE_F16=1` and
`GGML_CUDA_INK2_MOE_F16_Q=1` take it from one token on), `-o FLASH_ATTN_EXT` includes 1 to 8 query rows over a q8_0
cache with 24 query heads over 8 K/V heads (the vector kernel and the 3-head q8_0 kernel).

Perplexity A/B on the same text (`llama-perplexity -f <text> -c 2048 --chunks 4 -ngl 99 -fa 1 -b 2048 -ub 512`) against
the stock paths (`GGML_CUDA_INK2_FORCE_STOCK=1`): expect differences of 0.1 to 0.3 % without a direction (the kernels
round differently), not more.

## Measurements

Measured on Radeon RX 7900 XTX (24 GB), Windows, HIP SDK 7.2, 2026-11-21 unless a later date is given; this branch built by
`scripts/inkling2-amd/build-hip.cmd` from the published tree; both engines with the Unsloth UD-Q4_K_M file unless said
otherwise. `llama-server`, one slot. A prompt of source code is read once, then 6 answers of up to 300 tokens are
generated after it (temperature 1.0, top-p 0.95, top-k 20, a fixed seed per answer). Reading = the server's prompt
tokens per second; writing = generated tokens per second after the prompt; VRAM = peak of the server process over the
run, dedicated + shared system memory (every run holds about 0.1-0.2 GB of shared memory from load on: pinned host
buffers, not a spill). The release runs with the `llama-server` line of Unsloth's "How to Run" guide
(`--jinja --n-gpu-layers 99 --parallel 1`, `--temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0`, and `--model-draft ...
--spec-type draft-dspark --spec-draft-n-max 3 --n-gpu-layers-draft 99` for the drafter; default flash-attention, batch
and ubatch settings; without its vision projector), this branch with the command line of "Run" (without its drafter
options in the rows without drafter), each at the context given.

### Where the release fits in VRAM

| engine, context, prompt | reading | writing | tokens per drafter step | VRAM peak |
|---|---|---|---|---|
| release, no drafter, context 32768 (Unsloth's guide), 24 829 tokens | 829 tok/s | 42.2 tok/s | | 19.95 + 0.22 GB |
| this branch, no drafter, context 32768, 24 829 tokens | 2998 / 3154 tok/s | 92.2 / 92.2 tok/s | | 17.17 + 0.14 GB |
| release, DSpark drafter, context 8192, 6 494 tokens | 984 tok/s | 60.2 tok/s | 2.65 (44.0 ms per step) | 19.07 + 0.37 GB |
| this branch, DSpark drafter, context 8192, 6 494 tokens | 2448 / 2534 tok/s | 128.6 / 128.8 tok/s | 2.63 (20.4 ms per step) | 17.16 + 0.19 GB |

The release with the drafter does not stay in dedicated memory above 8192 on this card: at 32768 it keeps 1.20 GB in
shared memory from load on (reading 766 tok/s, writing 44.1 tok/s), at 24576 2.72 GB, and at 16384 it fits at load but
grows to 2.12 GB of shared memory while it reads the prompt (reading 54 tok/s on 14 356 tokens). This branch with the
drafter: 2878 tok/s and 115.2 tok/s at 32768 (18.04 + 0.22 GB), 2890 tok/s and 117.8 tok/s at 16384 (17.45 + 0.20 GB).

The rows of this branch were measured again on 2026-11-24 with the current revision (the dev build of the same
sources, two server starts for each table row, one for 32768 and 16384 with the drafter); the rows of the release are
those of 2026-11-21. At the first publication (2026-11-21) this branch read 2103 tok/s and wrote 77.6 tok/s without the
drafter at 32768 (19.09 + 0.14 GB), and 1884 tok/s and 93.5 tok/s with it at 8192.

### Against the newer Unsloth release b12631

Unsloth's later release b12631-mix-acc0843, built for HIP with the configure options of this branch, against this
branch one revision earlier (2026-11-23): the same server options on both (`-ngl 99 -fa 1 -np 1 -b 2048 -ub 1024
--jinja --backend-sampling` and the sampling of "Run"), the same client as above, two alternated runs each.

| file, context, prompt | reading, b12631 | reading, this branch | writing, b12631 | writing, this branch | VRAM peak, b12631 / this branch |
|---|---|---|---|---|---|
| Unsloth file, no drafter, context 32768, 27 780 tokens | 351 / 352 tok/s | 3134 / 3146 tok/s | 49.7 / 49.8 tok/s | 84.5 / 84.5 tok/s | 19.65 + 0.20 / 17.17 + 0.14 GB |
| Unsloth file, no drafter, context 16384, 3 660 tokens | 783 / 816 tok/s | 2230 / 2212 tok/s | 53.1 / 53.9 tok/s | 91.9 / 92.2 tok/s | 18.31 + 0.17 / 16.66 + 0.14 GB |
| h6-lbf16 file, DSpark drafter, context 16384, 3 660 tokens | 768 / 786 tok/s | 2211 / 2330 tok/s | 74.8 / 73.9 tok/s (35.6 ms per step) | 130.7 / 130.2 tok/s (21.1 ms per step) | 19.35 + 0.27 / 17.30 + 0.20 GB |

On this card b12631 reads every prompt batch with the scalar banded attention kernel (its tensor-core paths are
enabled for NVIDIA GPUs only). At context 65536 it did not stay in dedicated memory with the 52 804-token prompt (it
grows by 2.3-2.6 GB while it reads the first batches), so there is no figure for that prompt.

### At context 65536 the release does not fit on a 24 GB card

Same text, 52 804 tokens; a second identical client run reads only the follow-up after the cached prefix. At this
context the release warns `failed to fit params to free device memory`, keeps every layer on the GPU as asked, and 4 to
6 GB of its buffers sit in shared system memory from the start: its rows measure that spill as much as the engine.
| engine, file, server options | reading | writing | tokens per drafter step | follow-up | VRAM peak |
|---|---|---|---|---|---|
| release b12568-mix-8eebad4 (HIP build), Unsloth UD-Q4_K_M, the options of Unsloth's guide, no drafter | 265 tok/s | 35.3 tok/s | | 514 tokens at 112 tok/s | 20.31 + 4.05 GB |
| same, with the DSpark drafter (n-max 3) | 261 tok/s | 25.3 / 24.9 tok/s | 2.46 / 2.43 | 514 tokens at 110 tok/s | 20.41 + 5.77 GB |
| this branch, Unsloth UD-Q4_K_M, the command line of "Run" | 1898 / 1901 tok/s | 90.3 / 90.2 tok/s | 2.66 (29.5 ms per step) | | 20.06 + 0.25 GB |
| this branch, UD-Q4_K_M-h6-lbf16, the command line of "Run" | 1943 / 1943 tok/s | 87.6 / 87.4 tok/s | 2.55 (29.1 ms per step) | 1026 tokens at 1223 tok/s | 19.90 + 0.25 GB |

- Later engine revision (2026-11-21, after the rows above: 3-head attention tiles for GQA ratio 3, NVFP4 expert products of prompt batches on FP16 WMMA), h6-lbf16 file, the command line of "Run", same 52 804-token prompt: reading 1952 -> 2381 tok/s (2442 in a second session), writing unchanged within noise (83-87 tok/s), VRAM peak 19.92 GB dedicated + 0.25 GB shared; perplexity 6.2610 against 6.2584 with the new paths off (`GGML_CUDA_INK2_FA_GQA3=0 GGML_CUDA_INK2_MOE_F16=0`; same text and settings for both, not those of the other perplexity figures here).
- Next engine revision (2026-11-21, after the line above: drafted tokens picked on the device, input uploads staged and batched on the GPU stream, no GPU wait before the drafter's CPU split), h6-lbf16 file, the command line of "Run", same 52 804-token prompt: reading 2439-2467 tok/s (was 2381-2442), writing 100-103 tok/s (was 83-87), VRAM peak unchanged at 19.92 GB dedicated + 0.25 GB shared.
- Engine revision of 2026-11-22 (after the line above: SITU activation written by the FP16 expert kernel, Q8_0 / Q5_K experts of the last 4 layers on that kernel, the relative-bias table as one flat product, one shared-memory buffer in the NVFP4 expert kernel), h6-lbf16 file, the command line of "Run", same 52 804-token prompt: reading 2593-2596 tok/s (was 2439-2467), writing 98-103 tok/s after the prompt (unchanged within noise), VRAM peak 19.62 GB dedicated + 0.25 GB shared (was 19.92 + 0.25); perplexity 6.2608 (6.2610 before, same text and settings as in the first line).
- Engine revision of 2026-11-23 (after the line above: compute buffers with headroom and sliding-window rings kept in one rotation, so that the server no longer grows into shared memory after load; the causal mask of the global layers applied inside the attention kernel; a relative-bias kernel for decode batches with one thread per key and token; small expert tiles on all 8 warps; slot-fast grid order of the expert mat-vec; a q8_0 cache for the global layers on the fast path; the depth mix and the short convolutions with their loads held in registers; expert tiles of 96 tokens; restored sliding-window states put back in the cells they were saved from; the expert gate_up projection, its activation and the down projection in one call; host fills of the relative positions and of the mask without per-cell lookups; per layer application the row ops after the projections, the K and V convolutions, the loop gates and the Q8_0 products in fewer launches, the router's top-k with its weight normalisation in one kernel, one wait for the sampled tokens; the loop controllers of prompt batches in three kernels; fused kernels and a compute-buffer reserve for several slots, no drafts while 3 or more slots generate; a 4-bit V cache and a windowed drafter cache as options for 196608 and 262144 tokens), h6-lbf16 file, the command line of "Run", same 52 804-token prompt: reading 3048-3050 tok/s (was 2593-2596), writing 110-111 tok/s after the prompt at 22.9 ms per drafter step (was 98-103), VRAM peak 19.05 GB dedicated + 0.25 GB shared (was 19.62 + 0.25); perplexity 6.2597 (was 6.2608, same text and settings as in the first line). Context 131072 with `-ctk q8_0 -ctv q8_0 --spec-draft-n-ubatch 256` (q8_0 cache for the global layers): reading 2886-2901 tok/s on the same prompt, writing 114-117 tok/s, VRAM peak 19.58 GB dedicated + 0.25 GB shared. Context 262144 with `-ctk q8_0 -ctv q4_0 --spec-draft-n-ubatch 256`, `INKLING2_DRAFT_KV_WINDOW=32768` and `INKLING2_FAR_Q8_HEADS=2`: reading 2662 tok/s on the same prompt, 1845 tok/s on a 125k-token prompt and 1195 tok/s on a 249 584-token prompt, writing 100 / 88 / 70 tok/s after them, VRAM peak 20.28 GB dedicated + 0.23 GB shared. Four slots, four conversations of about 10k tokens at once: 171-179 tok/s in total (one conversation at a time: 110 tok/s).
- Rows of this branch: two alternated runs per file (Unsloth, h6-lbf16, Unsloth, h6-lbf16). With the fixed seeds each
  file gave the same answers in both of its runs; the Unsloth file's answers happened to accept more drafts (2.66 tokens
  per step against 2.55), so its tokens per second are higher while the h6-lbf16 file is 1.2 % faster per drafter step.
  The follow-up of the h6-lbf16 row comes from a separate run of the same setting (reading 1959 tok/s, writing 88.2 /
  90.3 tok/s in that run).
- Without the drafter (same code before the drafter-head change, the command line of "Run" without the drafter options):
  writing 71.1 tok/s with `--backend-sampling`, 70.8 without; prompt reading 2022 tok/s in an earlier revision. At short
  context (8192, no drafter, three short prompts): 80 tok/s with the h6-lbf16 file, against 44 tok/s for the release with the
  Unsloth file.
- llama-bench (check.ps1: depth 0, `-ub 512`, h6-lbf16 file): pp2048 2424 tok/s and tg128 89.5 tok/s, 1840 and 53.0 with
  `GGML_CUDA_INK2_NO_FUSE=1` (the far mode stays on); the release with the Unsloth file: pp512 1606 tok/s, tg 46.8 tok/s.
- Perplexity (`-c 2048 --chunks 4 -ub 512`, start of the WikiText-2 raw test set), Unsloth UD-Q4_K_M file: 6.2387 with
  the release, 6.2364 with this branch (statistical error of the estimate: 0.23). Details: the model card.

## Limitations

- Built and measured on one GPU model (RX 7900 XTX, gfx1100) under Windows with HIP SDK 7.2. Every other GPU runs the
  stock kernels of the release (the staged input uploads of the scheduler run on every ROCm device and were measured on
  gfx1100 only); the other RDNA3.0 chips (gfx1101-gfx1103) take the same paths as gfx1100 but were not
  measured; `GGML_CUDA_INK2_ANY_AMD=1` on other AMD GPUs, Linux, and CUDA, MUSA, Vulkan, Metal or SYCL builds of this
  branch were not tested.
- Quality: checked by perplexity, the self-check and three smoke questions only (see the model card), and for the q8_0
  cache by KL divergence against the F16 cache; paths that round differently move the perplexity by 0.1 to 0.3 %. No
  task benchmark compares this branch with the release.
- Contexts from 8192 to 262144 tokens were measured (131072 only with the q8_0 cache of the global layers, 196608 and
  262144 only with q8_0 K and q4_0 V and the drafter window, prompts up to 249 584 tokens and a few follow-ups); 262144
  with the drafter fits only with about 3 GB of the card or less used elsewhere. Several slots were measured with
  generated test conversations, not with real parallel clients.
- Images: checked with a few generated test images only (text, numbers, shapes, one dense screenshot), no benchmark;
  the image path is the stock code of the release and was not made faster.
- The diagnostics listed above are still in the code (off by default, read once at start-up); the switches that give
  wrong results are compiled out unless `GGML_CUDA_INK2_COST_TOOLS` is defined.

## Attribution and license

llama.cpp: MIT, the ggml-org/llama.cpp authors (see LICENSE and AUTHORS). The release tree: Unsloth, with the pull
requests listed in the import commit. #385 and #386: Daniel Han (Unsloth). Inkling 2 Mini: Thinking Machines, Apache-2.0.
GGUF files and the DSpark drafter: Unsloth. The changes of this branch are under the MIT license of the project.

Acknowledgement: several ideas come from the Strata project (MIT, https://github.com/Niko1221/Strata): kernels for
several sequences that index the sequence of each row, kernel grouping per layer application, fused loop controllers, no
drafts under load, a windowed drafter cache and a 4-bit V cache; they were reimplemented here, no code was copied.

The changes of this branch were written with AI assistance (Anthropic's Claude models, in Claude Code) and measured on
one Radeon RX 7900 XTX.

---

# llama.cpp

![llama.cpp](https://raw.githubusercontent.com/ggml-org/llama-brand/refs/heads/master/logo/svg/cover/llama-cpp/cover-llama-cpp-dark.svg)

<div align="center">

<b>LLM inference in C/C++</b>

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/ggml-org/llama.cpp?color=brightgreen)](https://github.com/ggml-org/llama.cpp/releases?q=tag:v1)
[![Nightly](https://img.shields.io/github/v/release/ggml-org/llama.cpp?label=nightly&filter=b*&color=orange)](https://github.com/ggml-org/llama.cpp/releases?q=b)
[![Server](https://img.shields.io/github/actions/workflow/status/ggml-org/llama.cpp/server.yml?label=Server)](https://github.com/ggml-org/llama.cpp/actions/workflows/server.yml)
[![Docker](https://img.shields.io/github/actions/workflow/status/ggml-org/llama.cpp/docker.yml?label=Docker)](https://github.com/ggml-org/llama.cpp/actions/workflows/docker.yml)
[![Winget](https://img.shields.io/github/actions/workflow/status/ggml-org/llama.cpp/winget.yml?label=Winget)](https://github.com/ggml-org/llama.cpp/actions/workflows/winget.yml)

[v1.0.0](https://huggingface.co/blog/ggml-org/llama-cpp-v1) / [ggml](https://github.com/ggml-org/ggml) / [ops](https://github.com/ggml-org/llama.cpp/blob/master/docs/ops.md) / [maintainer PRs](https://github.com/ggml-org/llama.cpp/pulls?q=is%3Apr%20is%3Aopen%20draft%3AFalse%20(author%3Asanmai%20OR%20author%3Argerganov%20OR%20author%3AKitaitiMakoto%20OR%20author%3Adanbev%20OR%20author%3Aaldehir%20OR%20author%3Amax-krasnyansky%20OR%20author%3ACISC%20OR%20author%3Aggerganov%20OR%20author%3Aam17an%20OR%20author%3Ajhen0409%20OR%20author%3Abartowski1182%20OR%20author%3Anikwen%20OR%20author%3Ahipudding%20OR%20author%3Aravi9%20OR%20author%3AServeurpersoCom%20OR%20author%3Athelittlefireman%20OR%20author%3Apwilkin%20OR%20author%3Areeselevine%20OR%20author%3Angxson%20OR%20author%3Ajeffbolznv%20OR%20author%3Amarty1885%20OR%20author%3A0cc4m%20OR%20author%3ATitaniumtown%20OR%20author%3Aangt%20OR%20author%3AIMbackK%20OR%20author%3Aarthw%20OR%20author%3AJohannesGaessler%20OR%20author%3AORippler%20OR%20author%3Aruixiang63%20OR%20author%3Axctan%20OR%20author%3AmasterFoad%20OR%20author%3Aallozaur%20OR%20author%3AAndreas-Krebbel%20OR%20author%3Ayomaytk%20OR%20author%3Aaendk%20OR%20author%3Awine99%20OR%20author%3Agaugarg-nv%20OR%20author%3Ataronaeo%20OR%20author%3Aforforever73%20OR%20author%3Achaxu01%20OR%20author%3Alhez%20OR%20author%3AAlekseiNikiforovIBM%20OR%20author%3Anetrunnereve%20OR%20author%3Afairydreaming%20OR%20author%3Aynankani)%20sort%3Aupdated-desc) / [dev stats](https://github.com/ggml-org/llama.cpp-dev) / [lib llama API](https://github.com/ggml-org/llama.cpp/issues/9289) / [llama-server REST API](https://github.com/ggml-org/llama.cpp/issues/9291)

</div>

## Description

The main goal of `llama.cpp` is to enable LLM (and MLLM) inference with minimal setup and state-of-the-art performance on a wide range of hardware - locally and in the cloud.

The `llama.cpp` project is built on top of the [ggml](https://github.com/ggml-org/ggml) library.

## Quick start

A few options to get `llama.cpp` installed on your machine:

```bash
# curl
curl -LsSf https://llama.app/install.sh | sh

# powershell
irm https://llama.app/install.ps1 | iex
```

- Visit https://llama.app and follow the instructions
- Run with Docker - see our [Docker documentation](docs/docker.md)
- Download pre-built binaries from the [releases page](https://github.com/ggml-org/llama.cpp/releases)
- Build from source by cloning this repository - check out [our build guide](docs/build.md)

Once installed:

```sh
# Download and run a model directly from Hugging Face
llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF

# Launch OpenAI-compatible API server
llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF
```

<table align="center">
    <tr>
        <td align="center" width=50%>
            <img width="1310" height="888" alt="VLM session with `llama cli`" src="https://github.com/user-attachments/assets/88726b48-1713-48aa-a525-95a02e78afc4" />
            <i>VLM session with <b>llama cli</b></i>
        </td>
        <td align="center">
            <img width="1392" height="958" alt="Llama Chat, the built-in chat app, against `llama serve` running Qwen 3.6" src="https://github.com/user-attachments/assets/b402f972-2e32-4def-8771-8d849f08cf2e" />
            <i>Llama Chat, the built-in chat app, against <b>llama serve</b></i>
        </td>
    </tr>
<table>

## Documentation

#### Tools

- [cli](tools/cli/README.md)
- [completion](tools/completion/README.md)
- [server](tools/server/README.md)
- [Text-to-speech (TTS) models](docs/multimodal/tts.md)
- [GBNF grammars](grammars/README.md)

#### Development

- [How to build](docs/build.md)
- [Running on Docker](docs/docker.md)
- [Build on Android](docs/android.md)
- [Multi-GPU usage](docs/multi-gpu.md)
- [Performance troubleshooting](docs/development/token_generation_performance_tips.md)
- [GGML tips & tricks](https://github.com/ggml-org/llama.cpp/wiki/GGML-Tips-&-Tricks)
- [XCFramework](docs/xcframework.md)
- [Completions](docs/completions.md)
- [Models](docs/models.md)
- [Release process](docs/release.md)

## Contributing

- Contributors can open PRs
- Collaborators will be invited based on contributions
- Maintainers can push to branches in the `llama.cpp` repo and merge PRs into the `master` branch
- Any help with managing issues, PRs and projects is very appreciated!
- Read the [CONTRIBUTING.md](CONTRIBUTING.md) for more information

## Acknowledgements

- [yhirose/cpp-httplib](https://github.com/yhirose/cpp-httplib) - Single-header HTTP server, used by `llama-server` - MIT license
- [nothings/stb](https://github.com/nothings/stb) - Single-header image format decoder, used by multimodal subsystem - Public domain
- [nlohmann/json](https://github.com/nlohmann/json) - Single-header JSON library, used by various tools/examples - MIT License
- [mackron/miniaudio](https://github.com/mackron/miniaudio) - Single-header audio format decoder, used by multimodal subsystem - Public domain
- [sheredom/subprocess.h](https://github.com/sheredom/subprocess.h) - Single-header process launching solution for C and C++ - Public domain
