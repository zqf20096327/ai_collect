# FCCL

<img src="docs/images/logo-fccl-dark.png" alt="FCCL" width="132" align="right">

**Vendor-neutral cross-process collective communication over PCIe + host shared memory.**

Run one model across an AMD card and an NVIDIA card in the same box — **tensor parallel** over
PCIe and host memory, **no NVLink, no RDMA, no compilation**.

Core is roughly **2.5k lines of Python** (~1.7k excluding comments and blank lines) — torch + numpy only.

[![version](https://img.shields.io/badge/version-1.4.0-blue)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)
[![python](https://img.shields.io/badge/python-3.9%2B-blue)](pyproject.toml)

[简体中文 →](README.zh-CN.md) · [Benchmarks](benchmarks/README.md) · [Docs](docs/en/) · [CHANGELOG](CHANGELOG.md)

---

## Why this exists

Sold out, marked up, or shipped only as a matched set. When one card is not enough, the reflex is
to buy a second one of the same model — which means waiting for stock, accepting whatever the price
is today, and staying inside a single vendor's ecosystem for good. And the moment you pick a
different brand to cover what that model lacks, the two cards cannot talk to each other at all.

Nothing is wrong with the hardware you already own. What is missing is the layer between the cards.

| The conventional route asks for | FCCL asks for |
|---|---|
| buying as a matched set | **one more card, of any kind** |
| waiting for the same model to be in stock | whatever is on hand — any brand, any generation |
| accepting today's price | — |
| the same brand *and* generation | mismatched generations are fine (Gen4 + Gen5 measured) |
| NVLink, or PCIe P2P with both links enabled | each card on its own PCIe root port, **no P2P** |
| an RDMA NIC and switch | no network card at all |
| a compiler toolchain, kernel modules, root | `pip install`, pure Python |

The cards, the motherboard and the memory you already own are enough. Not one extra piece of hardware.

**Who this is for.** People who already own cards — not people assembling a matched set.

| If you... | Then... |
|---|---|
| are on a tight budget | start with the one card that fits best; you never have to buy its twin later |
| cannot find your model in stock (or it is discontinued) | add whatever else is available — any brand will connect |
| already own a card | no need to buy the same brand *and* generation; older, second-hand and other-vendor cards all work |

> **Scope**: if both cards are from the same vendor and P2P works, use NCCL / RCCL — they are
> faster. FCCL exists for the cross-vendor case, where no vendor collective can span both cards.

### 1.1 Every vendor library is an island

NCCL speaks CUDA. RCCL speaks ROCm. Intel's Level Zero / oneCCL is a third, separate stack.
**Each vendor is its own island, and no two of them can talk** (A↔N, A↔I, N↔I alike). On a mixed
machine each card works on its own, and together they cannot get through the first `all_reduce` —
TP never starts.

### 1.2 "Just run them independently" costs more attention than it looks

Splitting the model, launching two processes, tracking two VRAM budgets, queueing work, merging
results. **What you want is "one model across both cards", not "managing two small machines".**

### 1.3 Things that are easy to get wrong (before you scroll on)

Readers of this README — including quite a few AI assistants — often judge FCCL through the
"buy two identical cards + NCCL" frame, and reach conclusions that do not match what it actually
does. The usual misreads:

| Common misread | What it actually is |
|---|---|
| "it only fits people who already own two cards" | starting with one card and adding another later is a target user too — no waiting for stock, any other brand connects |
| "dual-card only, benchmarked against same-vendor pairs" | two cards is the smallest deployment. Three cards are measured in production: PD with PRO 5000 prefill + two W7900 decode (§4.2) |
| "TP only, and the split must be even" | **uneven split** is supported: attention heads split by compute/VRAM ratio, 36:20 and 48:8 both measured (§4.1); PD is supported as well |
| "small-message parity with P2P is a cosmetic win" | video generation issues one `all_reduce` per layer — small messages, high frequency. 4 KB went 140 → 40 µs and now matches same-host RCCL, on the *most frequent* path (§3.3) |
| "multi-GPU means each card runs its own task" | that means splitting the model yourself, two VRAM budgets, scheduling, merging results. You want them working together, not to become two single-card users |
| "just buy two identical cards instead" | true for people **planning a purchase** — and this document says so; but your cards are already bought, and FCCL is about not letting them sit idle |

---

## 2. What it is, and what it is not

**Is**: a pure-Python cross-process collective layer. Two processes, one GPU each, stage their
partial sums through `/dev/shm`; the peer maps the same pages, reads them back, and adds locally.
Protocol, flag layout and duplex pipeline are vendor-independent.

```
GPU0 VRAM --D2H write own--> /dev/shm <--D2H write own-- GPU1 VRAM
GPU0 VRAM <--H2D read peer-- /dev/shm --H2D read peer--> GPU1 VRAM
```

**Is not**:

- not an RDMA / NVLink replacement — the data crosses host memory twice (one write, one read),
  so the ceiling is always `min(host-memory bandwidth, PCIe bandwidth)`;
- not a performance winner — with same-vendor P2P, use the vendor library;
- not "any accelerator card, zero work" — a card must meet four conditions (§9.1), though the
  protocol itself is vendor-neutral.

**Is**: the layer that turns TP from 0 into 1 on a machine where no official library can span both cards.

| Backend | Path | Status |
|---|---|---|
| NVIDIA | CUDA streams + D2H/H2D | implemented, measured on RTX 5880 / RTX PRO 5000 |
| AMD | ROCm/HIP (hip-as-cuda) | implemented, measured on W7900 / R9700 |
| Intel | XPU + Level Zero DMA (`l0_dma.py`) | implemented; 2× Arc Pro B60, and Arc Pro B70 ↔ R9700 measured |
| **Any other PCIe accelerator** (domestic/custom compute card, FPGA, DSP…) | implement async "pinned host ↔ device" copy | **protocol-equivalent**: one vendor branch in `detect.py` plus one copy wrapper; the protocol does not change. Porting steps: [`docs/en/porting-new-vendor.md`](docs/en/porting-new-vendor.md) |

**A card qualifies when it meets four conditions:** ① its own device memory that can act as a DMA
source and destination (this rules out block devices such as SSDs); ② the ability to compute on
the card (each rank produces its own partial sum); ③ a usable driver/runtime; ④ asynchronous
D2H/H2D copy with completion signalling (`cudaHostRegister` / `hipHostRegister` / `mlock` plus the
vendor equivalent).

> FCCL never uses an inter-GPU link — each card talks to the host over its own root port — so
> **the two ends may run different PCIe generations**. On this machine the W7900 is Gen4 and the
> RTX PRO 5000 is Gen5. "Link parity" is not one of the four conditions.

---

## 3. Measured: how fast is it, really (1.4.0)

Platform: WRX90, AMD W7900 (ROCm, Gen4 x16) ↔ NVIDIA RTX PRO 5000 (CUDA, Gen5 x16), each card on
its own root port. Every number comes from the repo's own `tests/run_full.sh` (8 groups, 144 rows);
raw data in [`benchmarks/1.4.0/`](benchmarks/1.4.0/).

### 3.1 In one line

**1.4.0 vs 1.3.1: 4 MB 379 → 320 µs (−15%, 60% → 71% of same-host RCCL), 8 MB −15%, 16 MB −11%.**
The 4 MB dip is gone — it was the single worst point on the curve. The block-level handshake now
lives inside the GPU stream (`WriteValue32`/`WaitValue32`), so the CPU waits only once per message.

### 3.2 Main table

All numbers re-measured on 2026-11-25 (126 rows, 0 failures):

| Metric | **FCCL 1.4.0** |
|---|---|
| **`all_reduce` 4 KB** | **39–40 µs** |
| 1 MB | **131 µs** |
| 4 MB | **320 µs** |
| 8 MB | 540 µs |
| 16 MB | **955 µs** |
| 32 MB | 1.74 ms |
| 64 MB | 3.31 ms |
| 128 MB | 6.37 ms |
| 192 MB | 9.38 ms |
| 256 MB | 12.43 ms |
| 512 MB | 24.88 ms |
| **1 GiB duplex** | **50.34 ms / 42.66 GB/s** |
| 1 GiB single-block | 84.42 ms / 25.44 GB/s |
| 1500-iteration soak (1 GiB) | p99 **50.44 ms** |
| `bcast` 1 KB | **2 µs** |
| `all_to_all_single` (Ulysses 7685×56×128 bf16) | 4.50 ms / 49.1 GB/s |
| Full sweep | **126/126 `ok=True`** |

<img src="docs/images/latency-vs-size-en.png" alt="latency vs message size: 1.3.1 vs 1.4.0" width="100%">

### 3.3 Against same-host RCCL P2P (same-vendor reference)

| Message | **FCCL 1.4.0** | RCCL (2× W7900, P2P) | FCCL vs RCCL |
|---|---:|---:|---:|
| **4 KB** | **40 µs** | **40 µs** | **100%** |
| 1 MB | 131 µs | 92 µs | 70% |
| **4 MB** | **320 µs** | 227 µs | **71%** |
| 16 MB | **955 µs** | 768 µs | **80%** |
| 32 MB | **1.74 ms** | 1.50 ms | **86%** |
| 64 MB | **3.31 ms** | 2.96 ms | **89%** |
| 128 MB | 6.37 ms | 5.90 ms | 93% |
| 256 MB | 12.43 ms | 11.77 ms | 95% |
| 512 MB | 24.88 ms | 23.62 ms | 95% |
| 1 GiB | 50.34 ms | 47.32 ms | **94%** |

RCCL talks GPU-to-GPU over P2P; FCCL crosses host memory twice — that is the whole remaining gap.

> **Bandwidth convention**: `busbw = 2 × message_bytes / time` (one send + one receive), applied
> identically to FCCL, RCCL and NCCL in §3.3/§3.4 — the three are directly comparable. The 2×
> caveat only applies when a library reports `algbw` (1 × bytes / time); don't mix the two.

<img src="docs/images/fcc-vs-rccl-en.png" alt="FCCL vs same-host RCCL P2P: parity at 4 KB, 60-72% mid, 94% at 1 GiB" width="100%">

### 3.4 Cross-platform (1 GiB all_reduce)

| Platform | Backend | Time | Note |
|---|---|---|---|
| W7900 + PRO 5000 (WRX90) | **FCCL 1.4.0** duplex | **50.34 ms / 42.66 GB/s** | this README's reference box, both x16 |
| 2× W7900 | RCCL P2P | **47.32 ms / 45.38 GB/s** | same-vendor reference |
| PRO 5000 + RTX 5880 | NCCL (no P2P, host path) | 60.26 ms | FCCL's host path ~19% faster |
| **R9700 + Arc Pro B70 (B850)** | **FCCL 1.4.0** single-block + 2 MiB pages | **93.5 ms / 22.96 GB/s** | both ends Gen5 x8 |

**Intel pair (B70 ↔ R9700)**: both ends run Gen5 **x8** — the AMD root port only trains 8 lanes.
Single-direction pinned DMA measures **H2D 28.7 / D2H 22.7 GB/s**, i.e. 91% / 72% of the x8
ceiling (31.5 GB/s), so the link is saturated. What caps `all_reduce` is Intel's **two bcs copy
engines serialising** ahead of the PCIe port — bidirectional total 31.5 GB/s versus AMD's 44.5.
Required config: huge pages + `FCCL_DUPLEX=0` + explicit block size (§7).

| Message | FCCL 1.4.0 (B70 ↔ R9700) | busbw |
|---|---:|---:|
| 4 KB | **35 µs** | 0.23 GB/s |
| 16 KB | **35 µs** | 0.94 GB/s |
| 64 KB | **56 µs** | 2.36 GB/s |
| 256 KB | **77 µs** | 6.82 GB/s |
| 1 MB | **172 µs** | 12.18 GB/s |
| 4 MB | **786 µs** | 10.67 GB/s |
| 16 MB | **1.748 ms** | 19.19 GB/s |
| 64 MB | **6.10 ms** | 22.00 GB/s |
| 256 MB | **23.56 ms** | 22.79 GB/s |
| **1 GiB** | **93.5 ms** | **22.96 GB/s** |

<img src="docs/images/three-way-1gib-dark.png" alt="1 GiB all_reduce: FCCL vs RCCL vs NCCL" width="100%">

---

## 4. Two real workloads: what it is actually used for

Microbenchmarks say how fast the pipe is. This section says whether it pays off.

### 4.1 Video generation: cross-vendor TP2 with uneven split

Same model (ComfyUI MiniMax-H3, int8 ConvRot), two cross-vendor pairs.

**R9700 + Arc Pro B70** (1.68× compute gap, 1344×768 / 294 frames / 6 steps). An even 28:28 split
leaves the R9700 idle every step; splitting the 56 attention heads **36:20** in inverse proportion
makes both ends finish together:

| Configuration | End-to-end | Per step | vs fastest solo |
|---|---:|---:|---:|
| R9700 solo | 814 s | 100.9 s | 1.00× |
| TP2 even 28:28 | 676 s | 92.4 s | 1.20× |
| **TP2 uneven 36:20** | **563 s** | **71.0 s** | **1.45×** |

Both ends agree at 45.57 dB PSNR.

<img src="docs/images/tp2-split-a-dark.png" alt="R9700 + B70: solo vs even vs uneven TP2" width="100%">

**W7900 + RTX PRO 5000** (3.8× compute gap, 8 steps, 3 LoRAs bypassed):

| Configuration | End-to-end | Per step |
|---|---:|---:|
| TP2 even 28:28 | 1053 s | 125.2 s |
| **TP2 uneven 48:8** | **547 s** | **52.3 s** |
| 52:4 (further) | — | 56.3 s ↑ |

Uneven is 48% faster than even<img src="docs/images/tp2-split-b-dark.png" alt="W7900 + PRO 5000: even vs uneven" width="100%">

 — **but it only ties the PRO 5000 running alone.** Pushing to 52:4
gets slower: once the slow card no longer sets the pace, the fast one becomes the bottleneck.

> **Uneven splitting recovers wasted time, not the compute gap itself.** When the two cards differ
> by more than ~3×, even an optimal split only matches the fastest card — use that card alone and
> skip TP. Measure each card in single-end mode first; it takes half an hour and saves days of
> tuning. Details: [`docs/en/uneven-split.md`](docs/en/uneven-split.md).

### 4.2 LLM inference: cross-vendor PD disaggregation (three cards)

PD splits inference into two stages, each on the hardware that suits it — **compute-bound prefill
on the FP8 NVIDIA card, memory-bound decode on the AMD cards**. That split is the real cross-vendor
value: **no single vendor can build it with this pair** — the AMD card here (W7900, RDNA3) has no
FP8 tensor cores (58% slower prefill, no 256K), and the NVIDIA card here (48 GB) lacks the VRAM for
a 256K decode pool.

<img src="docs/images/pd-prefill-dark.png" alt="prefill throughput: NVIDIA FP8 vs AMD W4A16" width="100%">

| Stage | Wants | Better card | Measured |
|---|---|---|---|
| prefill | compute | RTX PRO 5000 + FP8 | **5451 tok/s** (8K), **58% faster** than AMD W4A16's 3446; at 256K only FP8 fits (1757 tok/s) |
| decode | VRAM + bandwidth | 2× W7900 + W4A16 | 48G each, **252K** KV pool, 199 tok/s (math), 256K context (250,047 tokens measured) |

The cost is just as clear: the KV has to cross host memory. An 8K request moves 788 MB in 41 ms —
**2.7%** of TTFT (D2H 15.7 ms @ 50 GB/s, H2D 25.2 ms @ 15.6 GB/s per rank). Same-vendor P2P/NVLink
would be lower.

<img src="docs/images/pd-ttft-dark.png" alt="8K request TTFT breakdown: prefill 1492 ms + transfer 41 ms" width="100%">

**vLLM speaks only NIXL**: on a host without P2P its default falls back to TCP (842 MB/s here), and
across vendors it has no path at all. FCCL's vLLM connector moves the same 208.5 MB per request in
**17.5 ms (same-vendor) / 23.8 ms (cross-vendor)** — **10–14× the default NIXL path**.

Do not extrapolate: NIXL reaches 16.5 GB/s with a host buffer and 82–230 GB/s with NVLink + IMEX.
**Both of those high-bandwidth paths cost money**: the 16.5 GB/s host-buffer path needs the same
host-memory bandwidth as FCCL (same bar, §5); the 82–230 GB/s path needs NVLink / IB NICs plus the
whole IMEX stack. On the two cards you already own, neither exists. **FCCL's 17.5 / 23.8 ms is
what this hardware does with zero extra spend** — and cross-vendor is the part NIXL cannot do at all.

Runnable scripts: [`examples/sglang-pd/`](examples/sglang-pd/),
[`examples/vllm-pd/`](examples/vllm-pd/); full data and pitfalls:
[`docs/en/pd-disaggregation.md`](docs/en/pd-disaggregation.md),
[`benchmarks/pd-crossvendor/`](benchmarks/pd-crossvendor/).

---

## 5. The real bottleneck: host memory (the bar scales with PCIe)

### 5.1 The formula

The path is **device → host memory → device**, so a 1 GiB all_reduce moves:

```
per rank : write 1 GiB (D2H) + read 1 GiB (H2D)
two ranks: 4 × 1 GiB = 4.29 GB
```

In the ideal duplex case `T ≈ 1 GiB ÷ B` (B = one-way PCIe bandwidth), so:

```
required host simultaneous R+W = 4.29 GB ÷ T = 4 × B
```

**In one line: the host needs about 4 × the one-way PCIe bandwidth.**
There is no universal "85 GB/s bar" — 85 is just the Gen4 x16 number.

> **That is the condition for saturating PCIe, not a usability threshold.** When host bandwidth is
> short, FCCL does not stop working — throughput simply drops in proportion: less bandwidth, slower
> transfer, roughly linearly. The 72 GB/s R9700 machine below (needed ~177) still gets 1.09× duplex,
> which is plenty for individual video generation and small-team inference (§5.4).

### 5.2 How much host-memory bandwidth each PCIe generation needs (x16)

> **Three assumptions**: ① both GPUs and the pinned buffers sit on the **same NUMA node**
> (crossing UPI / Infinity Fabric roughly doubles the pressure); ② the message is **much larger
> than the CPU's L3** (e.g. >64 MB) — a 4 KB message hits cache and never needs this DRAM
> throughput; ③ the 85% already accounts for 128b/130b encoding plus TLP, DLLP and ACK/NAK overhead.

| PCIe | One-way theoretical | One-way measured (~85%) | **Required host R+W** | Typical memory on that generation | Verdict |
|---|---|---|---|---|---|
| **3.0 x16** | 15.75 GB/s | ~13 GB/s | **~52 GB/s** | 4× DDR4-3200 (~50) | just enough, no headroom |
| **4.0 x16** | 31.5 GB/s | ~26 GB/s | **~104 GB/s** | 4× DDR4 (~50) / 8× DDR4 (~90) | 4 DIMMs short, 8 marginal |
| **5.0 x16** | 63 GB/s | ~44–54 GB/s | **~177–214 GB/s** | 8× DDR5-6000 (~180) | OK; 4 DDR5 DIMMs far short |

**x8 machines** (many consumer/workstation boards wire only x8 to the GPU) need half:

| PCIe | One-way measured | Host R+W needed | Typical memory on that generation | Verdict |
|---|---|---|---|---|
| 3.0 x8 | ~7 GB/s | ~28 GB/s | dual-channel DDR4 (~25) | ✅ plenty |
| 4.0 x8 | ~13 GB/s | ~52 GB/s | 4× DDR4-3200 (~50) | ✅ just enough |
| 5.0 x8 | ~27 GB/s | ~107 GB/s | 4× DDR5-6000 (~90) | ⚠️ slightly short, 8 DIMMs needed |

<img src="docs/images/host-mem-en.png" alt="host-memory R+W needed vs typical memory per PCIe generation" width="100%">

### 5.3 Two measured platforms

| Platform | PCIe | Host memory | R+W measured | Needed | Outcome |
|---|---|---|---|---|---|
| W7900 + PRO 5000 | 4.0 x16 | 8×32G DDR5-6000 (8ch) | ~**324 GB/s** | ~104 | not the limit; duplex **1.67×** |
| 2× R9700 (ASRock W790) | 5.0 x16 | 4×32G DDR5-4800 (4ch) | **72 GB/s** | ~177 | memory-bound; still **1.09×** duplex, usable |

### 5.4 Decision rule (compute per platform, never carry it across)

| supply ÷ requirement | Consequence |
|---|---|
| ≥ 1.3 | ideal: host is not the limit, PCIe saturates (1.67× on Gen4) |
| 0.8–1.3 | near saturation: host and PCIe trade places, performance dips slightly |
| 0.5–0.8 | host bandwidth is the limit, throughput drops proportionally — still usable, the 1.09× duplex gain is still there |
| < 0.5 | clearly held back: consider adding DIMMs; without them it still runs, just slower |

**There is no "cannot run" row** — the worst row is only slower. Missing bandwidth costs speed in
proportion, and for individual video generation or small-team inference that is usually fine.

### 5.5 In a real application: the impact is smaller than you think

The numbers above are a "move 1 GiB at once" raw-bandwidth view. In real workloads, communication
is one small slice of the end-to-end time:

- **Video generation**: TP2 issues a per-layer `all_reduce`, but one sampling step is ~8.4 s and
  communication is about 7% of it. Halve the host bandwidth and the end-to-end run is a few minutes
  longer — you do not feel it day to day. Not "unusable", just "slower".
- **LLM inference (PD)**: an 8K request has a 1533 ms TTFT, of which KV transfer is 41 ms — 2.7%.
  Cut bandwidth in half and TTFT grows by ~20 ms. Chat experience does not change.
- What host memory really limits is the "move 40+ GB/s" raw benchmark, not producing a video or
  answering a chat.

**In one line: enough bandwidth buys full performance; not enough buys a slower but completely
usable system.** For individuals and small teams, that slowdown usually sits well within budget.

### 5.6 Tuning order

1. compute **`4 × one-way PCIe`** to get the "saturating" requirement;
2. measure the actual host R+W; when requirement > supply, estimate the proportional loss first, and **add DIMMs only if that speed is not enough**;
3. PCIe 3.0 machines (x16 or x8) usually need no memory work — go straight to block-size tuning (§6.4, `FCCL_DUPLEX_BLOCK_MB`);
4. do not treat block-size tuning as the cure for a host-memory bottleneck.

---

## 6. Install and quick start

**One line to install, two processes to run.** No compilation, no root, nothing beyond torch and numpy.

### 6.1 Four ways to get it

| Way | Command / entry | Best for |
|---|---|---|
| **Download a release** | [Releases](https://github.com/Fcys11/fccl/releases) → `fccl-1.3.1-py3-none-any.whl` | pinned version, offline machine |
| **pip from git** | `pip install "git+https://github.com/Fcys11/fccl"` | tracking main |
| **Clone** | `git clone https://github.com/Fcys11/fccl` | editing code / reading all benchmarks |
| **No install** | add the repo's `src/` to `sys.path` | leaving the environment alone |

```bash
# ① straight from GitHub (easiest; needs git and network access)
pip install "git+https://github.com/Fcys11/fccl"

# ② or a downloaded wheel
pip install fccl-1.3.1-py3-none-any.whl

# ③ or the sdist
pip install fccl-1.3.1.tar.gz
```

> ⚠️ **Do not rename the .whl.** pip parses the package name, version and platform from the
> filename; saving it as `fccl.whl` fails with `Invalid wheel filename`.

> ⚠️ `pyproject.toml` **deliberately declares no torch dependency**: CUDA, ROCm and IPEX torch
> builds are not interchangeable, so letting pip resolve one would very likely install the wrong
> one. Install the vendor torch matching your cards first, then FCCL. You may also need
> `pip install numpy`.

### 6.2 Minimal usage

```python
import fccl

print(fccl.describe())          # which devices are visible, recommended mode

# automatic mode selection
ar = fccl.auto(nbytes=1200 << 20, rank=0, session="job42", world=2)
ar.all_reduce(t)                # in-place sum, same as dist.all_reduce(t)
ar.all_reduce_max(t)            # in-place max
ar.bcast_bytes(b"...")          # rank0 → others, small objects
ar.all_to_all_single(out, send, [128], [128])   # Ulysses axis swap (1.2.6)
ar.all_gather(out, send)                        # gather every rank's block (1.2.6)
ar.broadcast_tensor(t, root=0)                  # asymmetric broadcast (1.2.6)
```

Run the two ranks as two processes (each process sees one card):

```bash
# rank 0 (NVIDIA)
TP_SESSION=job42 CUDA_VISIBLE_DEVICES=GPU-xxxx python your_train.py --rank 0
# rank 1 (AMD)
TP_SESSION=job42 ROCR_VISIBLE_DEVICES=GPU-yyyy python your_train.py --rank 1
```

Current release: **1.3.1**. Details of the public API: [`docs/en/architecture.md`](docs/en/architecture.md).

### 6.3 Prerequisites

| Item | Requirement |
|---|---|
| GPU | ≥2 devices (any vendor mix) |
| Driver | CUDA / ROCm / Level Zero stack matching your torch build |
| torch | ≥2.0 |
| numpy | any version — `pip install numpy` if the venv lacks it (FCCL declares no install-time dependency, so pip pulls neither torch nor numpy) |
| `/dev/shm` | ≥2× buffer size free (`TP_SHM_MB=1200` → 2.4 GB) |
| pinned host memory | `cudaHostRegister` / `hipHostRegister` available |

### 6.4 Environment variables

| Variable | Default | Meaning |
|---|---|---|
| `FCCL_DUPLEX` | 1 | 1 = block-pipelined duplex, 0 = single-block |
| `FCCL_DUPLEX_BLOCK_MB` | 16 | block size; values >16 are clamped to 16 |
| `FCCL_DUPLEX_MAX_MB` | 0 | 0 = unlimited; above this size use single-block |
| `FCCL_DUPLEX_SYNC` | 0 | 1 = global sync per block (debug, slow) |
| `FCCL_DUPLEX_TRACE` | 0 | 1 = print first-round block trace |
| `FCCL_TRACE` | 0 | 1 = print seq/shape/bytes |
| `FCCL_GPUSIG_MAX_KB` | 1024 | upper bound of the fast path (1 MB); 0 disables it (1.2.7 behaviour) |
| `FCCL_GSIG` | 1 | **master switch for GPU-side flags**; 0 = never use GPU write/wait on flags (4 KB returns to ~63 µs). Use this after a driver upgrade instead of downgrading |
| `B1_GSIG` | 1 | disables only the 1.4.0 **block-level** flags (4 MB/16 MB fall back to CPU-spin, slightly slower) |
| `FCCL_RELAY_MAX_KB` | 1024 | XPU small-message relay threshold (Intel cards only), clamped to the 1 MB relay buffer; 0 disables |

Full table and the H3-side variables: [`docs/en/architecture.md`](docs/en/architecture.md).

---

## 7. Reproducing the benchmarks

```bash
# isolated copy, so an installed/pinned package cannot shadow the tree
mkdir -p /tmp/fccltest && cp -a src/fccl /tmp/fccltest/ && cd /tmp/fccltest
rm -f /dev/shm/xbrtp_*

# terminal 1 (rank 0), terminal 2 (rank 1)
TP_SESSION=bench CUDA_VISIBLE_DEVICES=GPU-xxxx python fccl/tests/bench_sweep.py --rank 0 --mode msg --mb 1200 --sizes 1g
TP_SESSION=bench ROCR_VISIBLE_DEVICES=GPU-yyyy python fccl/tests/bench_sweep.py --rank 1 --mode msg --mb 1200 --sizes 1g
```

`src/fccl/tests/run_full.sh` orchestrates the full 8-group, 104-row sweep (~12 min) and writes
`results.csv`. Raw evidence for every number in this README lives in
[`benchmarks/1.4.0/`](benchmarks/1.4.0/).

---

## 8. Known pitfalls

9. **The fast path depends on driver symbols.** GPU-side flags use
   `hipStreamWriteValue32` / `cuStreamWriteValue32_v2` resolved via ctypes. A renamed or
   removed symbol falls back to the blocking path automatically (4 KB ~63 µs instead of 40,
   logged, no error) — but a **signature** change can make the self-test segfault. After a
   driver upgrade run a 4 KB bench; if it reads ~63 µs, set `FCCL_GSIG=0` explicitly; to drop
   the fast-path code entirely, downgrade to `v1.2.7` (**the whole TP group must downgrade**).

1. **Two copies of the library.** In the reference deployment the library is imported via
   `sys.path`; editing one copy does not change behaviour of the other. Verify with
   `fccl.__version__` at the import site.
2. **Cross-stream dependency.** The duplex path must
   `stream.wait_event(record(current_stream))` before D2H, otherwise it reads a tensor that
   is still being produced → NaN (fixed in 1.2.3, do not revert).
3. **Non-contiguous tensors.** After `t.contiguous()` the result must be copied back to the
   original tensor, otherwise `all_reduce` silently does nothing (fixed in 1.2.3).
4. **A green benchmark does not prove correctness.** `fill_`-style uniform data and contiguous
   tensors hide both defects above. End-to-end PSNR is the gate.
5. **KMAX truncation.** Up to 1.2.3, more than 80 blocks were silently truncated; 1.2.4 processes
   them in batches without changing the flag layout.
6. **Stale `/dev/shm` segments** make `cudaHostRegister` fail → silent bad data. Clear
   `/dev/shm/xbrtp_*` before every run.
7. **Single-ended submission** to a two-process collective deadlocks. Always start both.
8. **Every process in the TP group must upgrade together.**
   From 1.3.0 the handshake reports the platform type in slots 502/503: mixing with a
   1.2.7-or-earlier peer exits with an error in ~3 s instead of deadlocking for 60 s
   (set `FCCL_ALLOW_LEGACY_PEER=1` to restore the old behaviour for same-vendor, non-XPU peers).
   From **1.3.1** the block policy is reported in slot 500 as well (`1000 + MB` means "block
   adapts to the message size"): mixing 1.3.1 with 1.3.0 or earlier now fails fast on the first
   message above 1 MB with "block policy mismatch" instead of silently exchanging mismatched
   block counts. Note this guard **only fires when duplex is enabled** — a mixed A+I machine
   degrades to single-block and never touches slot 500, so cross-version mixing won't error there.
   Either way (A+I, A+N, same-vendor) we recommend upgrading the whole group at once.

---

## 9. Contributing

**FCCL is a community project.** The protocol, the flag layout and the duplex pipeline are all
documented; anyone can change them, extend them, or port a new card without asking. There is no
"the author decides" gate — send a PR.

### 9.1 Porting a new card (three steps)

1. **Detect** — add a vendor branch in `detect.py`, returning device name, memory, and
   `can_device_access_peer`.
2. **Copy wrapper** — implement async pinned-host ↔ device D2H/H2D. Use `l0_dma.py` for
   Level Zero, or torch `copy_(non_blocking=True)`.
3. **Verify** — `tests/bench_sweep.py` over 4 KB–1 GiB must report `ok=True`, then a
   1 GiB × 1500-iteration soak.

### 9.2 Submitting benchmark data

Follow the `benchmarks/1.3.1/` layout: `results.csv` + raw logs + platform description
(CPU, DIMM configuration, PCIe generation/width, driver versions). **Data without a complete
platform description cannot be reproduced and will not be merged.**

### 9.3 Discussions and issues

| What you want | Where |
|---|---|
| Ask "will card X work?" | [Discussions](https://github.com/Fcys11/fccl/discussions) |
| Report a bug | Issue with `fccl.__version__`, both card models, `results.csv`, full log |
| Change code / add a feature | PR directly, no need to ask first |
| Contribute your measurements | PR against `benchmarks/`, laid out as in §9.2 |

**The only merge criterion is reproducibility**, not who submitted it.

---

## 10. Citation and license

```bibtex
@software{fccl2026,
  title        = {FCCL: Vendor-Neutral Cross-Process Collective Communication
                  over PCIe and Host Shared Memory},
  author       = {Fcys11},
  year         = {2026},
  version      = {1.3.1},
  url          = {https://github.com/Fcys11/fccl},
  note         = {Vendor-neutral all_reduce over PCIe + host shared memory; any PCIe device able to do pinned-host async copy}
}
```

**License: Apache-2.0** — see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
Commercial use, modification and redistribution under the same terms are permitted.
