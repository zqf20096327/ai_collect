<p align="center">
  <img src="assets/Proxima_Midnight_MC_TR.webp" width="700">
</p>

<h1 align="center">
⚡ Proxima
</h1>

<p align="center">
Low-rank KV Cache Compression for vLLM

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![vLLM](https://img.shields.io/badge/vLLM-0.10.1.1-orange)
![CUDA](https://img.shields.io/badge/CUDA-12.x-green)
![Triton](https://img.shields.io/badge/Triton-Kernels-red)
![ICML](https://img.shields.io/badge/STAR--KV-ICML%202026%20Spotlight-purple)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)

</p>

An out-of-tree vLLM plugin implementing STAR-KV — low-rank KV cache compression via
learned soft-thresholding for adaptive rank control
[Bhatnagar et al., ICML 2026 Spotlight](https://arxiv.org/abs/2606.08382) .

STAR-KV replaces a transformer's full-dimension key/value cache with a per-layer low-rank
projection (head-wise decomposition for K, joint decomposition for V), calibrated offline via
short knowledge distillation, and stored in a compressed paged format. This repo reproduces
that pipeline and wires it into vLLM's V1 continuous-batching, paged-attention serving stack
via dedicated Triton kernels.

## Why

**KV-cache compression: fit more concurrent requests, and longer contexts, in the same GPU
memory.** Measured end to end on real GPU hardware (Modal L4 24GB):

| | plain vLLM | STAR-KV | delta |
|---|---|---|---|
| Max concurrent requests @ 8192 context, zero errors/timeouts | 1 | 4 | **4x** |
| Max concurrent requests @ 16384 context | 0 (refuses to boot) | 2 | boots+serves where plain can't even start |
| GPU KV-cache blocks, same memory budget (`max_model_len=4096`) | 756 | 2353 | **3.11x** |
| Max `max_model_len` this L4 can boot at | 8192 | 32768 | boots where plain refuses |

Full breakdown, methodology, and every number behind this table is in
[Measured results](#measured-results) below.

## When to use it

- You are **memory-bound**, not latency-bound: you need more concurrent sequences or longer
  contexts than stock vLLM fits on the GPU you have, and can tolerate slower per-token decode
  in exchange for not OOMing or refusing to boot.
- You are running **long-context workloads** (16k-32k+ tokens) on GPUs where plain vLLM's
  boot-time KV-cache pre-flight check refuses to start.
- You are **not** chasing single-request latency — at batch 1, STAR-KV's decode kernel is
  slower than FlashAttention-2 (launch-overhead bound, 0.36-0.87x); it crosses over to faster
  than FA2 around batch 8-16 and stays 1.2-1.46x faster at real serving batch sizes.

## Install

Not on PyPI. Install from source:

```bash
git clone https://github.com/Tenosra/Proxima
cd Proxima
pip install -e .   # pins vllm==0.10.1.1, see docs/vllm_patch_notes.md for why
```

## Quick start

```bash
# 1. Calibrate a STAR-KV checkpoint from a base HF model (offline, one-time, no vLLM involved)
python -m proxima_vllm.calibration.distill \
    --base-model lmsys/longchat-7b-v1.5-32k \
    --output ./checkpoints/longchat-7b-star-kv \
    --profiles aggressive,balanced,conservative

# 2. Serve it with vLLM
vllm serve ./checkpoints/longchat-7b-star-kv \
    --additional-config '{"proxima_vllm": {"kv_compression": "star_kv", "rank_profile": "balanced", "use_triton_kernels": true}}'
```

The reference calibrated checkpoint used for the numbers below is published (private) at
`iampoppyxx/longchat-7b-starkv-proxima` on the HF Hub.

## Measured results

Baseline is vLLM 0.10.1.1's own V1 `FlashAttentionBackend`. On L4 (sm89/Ada) vLLM falls back to
**FlashAttention-2**, not FA3 (FA3 requires Hopper) — that's what every number below is compared
against. This section keeps the headline wins; full raw sweep logs (including the messier
kernel-level tradeoffs) live in git history if you need them.

### Concurrency capacity: the core result

Same GPU, same model, distinct (non-shared-prefix) prompts per concurrent request,
`enable_prefix_caching=False`, fixed 512-token output, 120s request timeout. Capacity = serves
every request without erroring or timing out. `max_concurrency` = highest concurrency tested with
zero errors before the next doubling fails.

<p align="center">
  <img src="assets/plots/killer_concurrency_vs_context.png" width="520">
</p>

| context | plain vLLM max concurrency | STAR-KV max concurrency | delta |
|---|---|---|---|
| 8192 | 1 | **4** | **4x** |
| 16384 | 0 (boot refused) | **2** | STAR-KV serves here; plain can't boot at all |

Detail per level:

- **8192**: plain vLLM — conc=1 ok (13.1 tok/s, ttft 2.5s); conc=2 both requests time out.
  Boot log: `Available KV cache memory: 6.99 GiB`, 14,304 tokens.
  STAR-KV — conc=1/2/4 all ok (up to 20.2 tok/s, ttft 9.7s at conc=4); conc=8 all time out.
  Boot log: `Available KV cache memory: 7.05 GiB`, 44,800 tokens.
- **16384**: plain vLLM refuses to boot at every `gpu_memory_utilization` tried (0.9/0.85/0.8/0.75):
  `ValueError: ... 8.26 GiB KV cache is needed, which is larger than the available KV cache memory
  (6.99 GiB)`. STAR-KV boots (`gpu_memory_utilization=0.85`, 5.95 GiB / 37,792 tokens) and serves
  conc=1/2 ok (up to 9.8 tok/s, ttft 14.1s); conc=4 all time out.
- **32768**: plain vLLM boot-refused at every util level (known from the KV-cache-capacity numbers
  below); STAR-KV concurrency ceiling at this context not yet measured under this protocol.

### KV-cache capacity & long-context boot

`balanced` profile, same model/checkpoint, same memory budget (`max_model_len=4096`,
`gpu_memory_utilization=0.85`, block size 16):

| | GPU blocks | vs stock vLLM |
|---|---|---|
| plain vLLM | 756 | 1x |
| STAR-KV balanced | 2353 | **3.11x** |

At `max_model_len=32768`, plain vLLM's boot-time pre-flight check refuses to start at any
`gpu_memory_utilization` (needs 16.00 GiB KV cache, only ~5.45 GiB available). STAR-KV boots at
`gpu_memory_utilization=0.83` and serves real traffic — 20 concurrent requests at 178.6 tok/s.
Across the full context sweep (prompts sized to `max_model_len - 256`):

| engine | 4096 | 8192 | 16384 | 32768 |
|---|---|---|---|---|
| plain vLLM | ok | ok | **boot refused** | **boot refused** |
| STAR-KV | ok | ok | ok | ok |

Plain vLLM refuses to boot above 8192 on this L4; STAR-KV boots and serves at every context up to
the model's 32768 limit.

### Decode kernel: faster than FlashAttention-2 at real serving batch sizes

`scripts/bench/bench_attn_step.py`; 32-head MHA, head_size 128, rank 64, fp16. Speedup > 1 means
STAR-KV is faster:

<p align="center">
  <img src="assets/plots/decode_kernel_speedup.png" width="520">
</p>

| seq len | batch 1 | batch 16 | batch 64 |
|---|---|---|---|
| 1024 | 0.36x | 1.23x | 1.40x |
| 2048 | 0.57x | 1.33x | 1.43x |
| 4096 | 0.84x | 1.40x | 1.43x |
| 8192 | 0.87x | 1.44x | 1.46x |

1.2-1.46x faster than FA2 at the batch sizes real continuous-batching serving actually runs at
(>=16); the crossover point is around batch 8-16 regardless of sequence length.

### Max sustainable concurrency before saturation

`max_model_len=4096`, `gpu_memory_utilization=0.85`, sweeping `max_concurrency`:

<p align="center">
  <img src="assets/plots/throughput_vs_concurrency.png" width="520">
</p>

STAR-KV keeps admitting more concurrent decode sequences — mean batch size climbs to ~100-110
before saturating KV cache, vs plain vLLM saturating around batch ~35-47 — and output tok/s
converges to near parity (460-483 tok/s) once both are fully saturated, so the capacity win isn't
paid for in aggregate throughput at the top end.

### Long-generation latency at a context plain can't even boot

Single long-generation request(s), `concurrency=4` at `max_model_len=9216`, `concurrency=2` at
`17408`:

| engine | context | max_tokens | out tok/s | tpot p99 (ms) | kv used |
|---|---|---|---|---|---|
| plain | 9216 | 8192 | 7.6 | 525.8 | 1.00 |
| STAR-KV | 9216 | 8192 | 27.8 | 143.9 | 0.98 |
| STAR-KV | 17408 | 16384 | 12.3 | 143.8 | 0.93 |

Plain vLLM saturates KV and preempts heavily under sustained long generation at this
concurrency (tpot p99 525.8ms); STAR-KV holds steady tpot p99 (~115-144ms across all tested
lengths) including at 17408 context, which plain cannot boot at all.

## Scope

Verified end to end on `lmsys/longchat-7b-v1.5-32k`, real ShareGPT serving traffic, on Modal L4
GPU hardware. Multi-model support (Qwen/Mistral/Gemma/Llama-3) is written but not yet validated
on hardware beyond this one model.

## License

Apache-2.0. Not affiliated with the STAR-KV paper authors or the vLLM project.
