# Glance Engine

**Ask a vision model 32 questions about an image and get 32 typed answers in 49 ms.** Glance Engine serves decision
models: it reads an image once, answers every question in one forward pass with readout heads instead of generated
text, and scans one question across hundreds of cached images in about 100 ms.

![python](https://img.shields.io/badge/python-3.11%20%7C%203.12-3776ab)
[![license](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![model](https://img.shields.io/badge/%F0%9F%A4%97%20model-Glance--4B--preview-ffcc4d)](https://huggingface.co/Vision-Decision/Glance-4B-preview)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/engine-hero-dark.svg">
  <img width="100%" alt="Top lane: a generative server (vLLM, SGLang) prefills the image, then every one of 32 questions decodes its box as text, one token per forward step: 334.0 ms with vLLM BF16, 658.0 ms with SGLang BF16. Bottom lane: Glance Engine runs the image prefix and all 32 question blocks in one forward pass and heads read out a box with P(present) and P(IoU at least 0.5), P(yes), or a probability per option: 48.9 ms. Source: outputs/engine_opt/CEILING.md, final-state table, one image box Q=32." src="assets/engine-hero-light.svg">
</picture>

<sub>A generative server must decode each answer token by token; Glance answers every question from one forward pass.
Times: one image (≤640 visual tokens), 32 box questions, warm median on one RTX PRO 6000; the fastest vLLM setup,
FP8 weights with speculative decoding, takes 229.2 ms
([CEILING.md](outputs/engine_opt/CEILING.md#final-state-frozen-at-8bc7d58)).</sub>

<table>
<tr>
<td align="center" width="33%"><h2>6.8×</h2>faster than vLLM at the same precision (BF16) on 32 questions about one image<br><sub>48.9 vs 334.0 ms; 4.7× vs the fastest vLLM, FP8+MTP</sub></td>
<td align="center" width="33%"><h2>32.6×</h2>faster than vLLM BF16 scanning one question over 256 cached images<br><sub>96.7 vs 3,151.6 ms; 27.6× vs FP8+MTP</sub></td>
<td align="center" width="33%"><h2>65 / 65</h2>workloads faster than vLLM and SGLang in BF16<br><sub>23 of 24 matched cells against lossy vLLM FP8+MTP</sub></td>
</tr>
</table>

## Install

```bash
git clone https://github.com/Vision-Decision/glance-engine.git && cd glance-engine
pip install -e '.[gpu,serve]'      # CPU only: pip install -e '.[serve]'
```

pip also installs [glance-core](https://github.com/Vision-Decision/glance-core), the model package, from GitHub. On a
CPU-only Linux machine, install the CPU torch wheel first
(`pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu`). Real checkpoints run in BF16 on
CUDA. **No GPU?** Replace `Glance.from_pretrained(...)` with `Glance.tiny()`: a random tiny model that runs the same
code on CPU with meaningless answers.

## Quickstart

**Ask several questions about one image.**

```python
from glance_engine import Box, Choice, Glance, YesNo

glance = Glance.from_pretrained("Vision-Decision/Glance-4B-preview")   # BF16 on CUDA
image_id = glance.add_image("demo/data/search_large/211069.jpg")       # vision tower + prefill, once

answers = glance.ask(image_id, [
    Box("the giraffe on the right"),
    YesNo("Is this photo taken outdoors?"),
    Choice("How many giraffes are there?", ["one", "two", "three or more"]),
])
for answer in answers:
    print(answer)    # BoxAnswer(question=…, p_present=…, box=[x1, y1, x2, y2], p_iou50=…, box_px=[…])
                     # YesNoAnswer(question=…, p_yes=…)  ChoiceAnswer(question=…, probs={"one": …, "two": …, …})
```

Answers are temperature-calibrated probabilities. Asking about `image_id` again reuses the cached prefix: on a G4 a
follow-up of 3 questions took 10.5 ms. The first call of each new shape spends seconds capturing CUDA graphs
([smoke test](docs/smoke_g4.md)).

**Scan one question across many cached images** (same `glance`).

```python
import glob
from PIL import Image

images = [Image.open(p).convert("RGB") for p in sorted(glob.glob("demo/data/search_large/*.jpg"))]
scanner = glance.scanner(max_vis=640)        # visual tokens per image, as in the benchmarks
result = scanner.scan("a giraffe", images)    # first call encodes the bank, then answers
result = scanner.scan("a toaster", images)    # same list: only the new question runs
print(result["set"]["any"], result["images"][0], result["latency_ms"])
```

`scanner.calibrate(negative_scans)` adds `result["set"]["none_conformal"]`, a "not in any of these" verdict whose
false-alarm rate is bounded. [Scanner API](docs/api.md#scanner-scanapipy)

**Serve over HTTP.**

```bash
glance-serve --port 8002 &        # add --tiny to try it on CPU
IMG=$(base64 < demo/data/search_large/211069.jpg | tr -d '\n')
curl -s localhost:8002/v1/decisions -H 'content-type: application/json' -d '{
  "image": "'"$IMG"'", "cache": true,
  "questions": [{"type": "box", "text": "the giraffe on the right"},
                {"type": "noul", "instr": "Is this photo taken outdoors?"}]}'
```

The reply has one result per question and an `image_ids` entry; send `{"image_ids": [...], "questions": [...]}` to
ask follow-ups without resending pixels. [HTTP API](docs/api.md#http) · [More examples](examples/)

## See it run

The animations replay separate demo runs, so their times differ slightly from the benchmark table below.

<p align="center"><img src="demo/glance_vs_vllm.gif" width="820" alt="Glance answers 32 box questions about one image at once in 49.6 ms; vLLM FP8+MTP returns boxes one by one and finishes at 242.3 ms"></p>

<p align="center"><b>32 questions about one image.</b> Glance 49.6 ms; vLLM 242.3 ms with FP8 weights and multi-token-prediction (MTP) speculative decoding, the fastest vLLM setup we measured. Median of 50 calls, replayed at 10× slow motion.</p>

<p align="center"><img src="demo/search_256.gif" width="820" alt="One question over 256 cached images: Glance answers in 95.9 ms with a calibrated verdict; vLLM FP8+MTP takes 2.6 s"></p>

<p align="center"><b>One question over 256 cached images.</b> Glance 95.9 ms; vLLM FP8+MTP 2,646 ms. Real time. Glance first encodes each image into a reusable <i>bank</i> entry (120.5 ms per image, once).</p>

<sub>Both animations replay measured runs on one RTX PRO 6000 ([method and raw timelines](demo/README.md)); they compare speed only. Photos: COCO val2017, CC BY 2.0 or no known copyright restrictions ([credits](demo/data/credits.csv)).</sub>

## Results

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/engine-latency-dark.svg">
  <img width="100%" alt="Dot plot on a log latency axis for six workloads. Glance vs fastest baseline: one image with 32 box questions 48.9 ms (4.7x faster than vLLM FP8+MTP at 229.2); follow-up on a cached image 19.6 ms (10.8x vs 211.8); video 64 frames 587.7 ms (1.18x vs 695.7); cached scan over 256 images 96.7 ms (27.6x vs 2,672.2); 64 concurrent clients 1,424.3 ms (1.28x vs vLLM BF16 1,828.0); GUI screenshot of 4,096 tokens with one question 277.9 ms, where vLLM FP8+MTP wins at 262.4 ms. Source: outputs/engine_opt/CEILING.md final-state table." src="assets/engine-latency-light.svg">
</picture>

<sub><b>Fastest on five of the six headline workloads, against every vLLM and SGLang setup we ran.</b> The ratio on the
right is against the fastest baseline in any precision, including lossy FP8 weights with speculative decoding. The one
loss is a 4,096-token screenshot with a single question, where almost all the time is prefill.</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/engine-all-cells-dark.svg">
  <img width="100%" alt="Strip plot of per-workload speedups (baseline ms / Glance ms) for all 65 measured cells. Against vLLM BF16: faster in 65 of 65, from 1.03x to 38x. Against SGLang BF16: faster in 65 of 65, from 1.24x to 80x. Against vLLM FP8+MTP (24 matched cells): faster in 23 of 24, from 0.94x to 30x; the one loss is the GUI 4,096-token, 1-question cell (Glance 277.9 ms, vLLM 262.4 ms). Source: outputs/engine_opt/CEILING.md final-state table." src="assets/engine-all-cells-light.svg">
</picture>

<sub><b>Every cell we measured, not a selection.</b> One dot per workload cell (single image, GUI, video, cached and fresh
scans, follow-ups, 1 to 64 concurrent clients). The smallest lead is 3% on prefill-bound fresh scans; the largest is on
cached scans, where Glance skips the vision tower and prefill entirely.
Plot data and script: [`assets/engine_charts.py`](assets/engine_charts.py).</sub>


Warm median latency in milliseconds on one NVIDIA RTX PRO 6000 Blackwell. Glance runs the BF16 Glance model; the
servers run Qwen3.5-4B, the generative model it is fine-tuned from, on the same pixels and questions, with prefix
caching and CUDA graphs.

| Workload | Glance | vLLM BF16 | SGLang BF16 | Best vLLM FP8+MTP |
|---|---:|---:|---:|---:|
| One image, 32 box questions | **48.9** | 334.0 | 658.0 | 229.2 |
| Follow-up on a cached image, 32 box questions | **19.6** | 316.9 | 606.5 | 211.8 |
| GUI screenshot (4,096 tokens), 1 box question | 277.9 | 353.7 | 489.0 | **262.4** |
| Video, 64 frames × 1 box question | **587.7** | 928.1 | 1,052.0 | 695.7 |
| Cached scan: 1 box question × 256 images | **96.7** | 3,151.6 | 7,732.9 | 2,672.2 |
| 64 concurrent clients, one cold box question each | **1,424.3** | 1,828.0 | 2,330.0 | — |

Across all 65 measured workloads Glance is faster than vLLM and SGLang in BF16, by 3% on prefill-bound work up to
38× on cached scans. Against lossy vLLM FP8+MTP it loses one of 24 matched workloads: a 4,096-token screenshot with
a single question, which is almost all prefill. [All 65 workloads](outputs/engine_opt/CEILING.md#final-state-frozen-at-8bc7d58) ·
[How to read the numbers](docs/performance.md)

Answers match the reference forward to FP32 rounding on CPU and stay within calibrated BF16 gates on GPU. One known
limit: when two image patches nearly tie, BF16 noise can switch which one a box is centred on.
[Exactness](docs/exactness.md)

## How it works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/architecture-dark.svg">
  <img width="100%" alt="Scheduler batches requests; each image runs the vision tower and a shared prefix prefill once; question blocks branch from the shared state; heads read out answers without decoding; retained prefixes form a bank for cached scans." src="docs/assets/architecture-light.svg">
</picture>

One packed variable-length prefill per batch, Gated DeltaNet kernels that continue many question branches from one
read-only recurrent state, a byte-bounded cache of image prefixes, and banks of cached prefixes for scans.
Details: [docs/architecture.md](docs/architecture.md).

## What is where

| Path | Contents |
|---|---|
| `glance_engine/` | Public API (`Glance`, typed questions), checkpoint loading, the `glance-serve` server |
| `speed/` | Single-image engine, kernels, scheduler, HTTP server, single-image and serving benchmarks |
| `scan/` | Scan engine, image banks, packed prefill for new images, set-level answers, scan benchmarks and the exactness suite |
| `tests/` | CPU test suite (`pytest`) |
| `examples/` | Runnable quickstart, cached scan and HTTP client |
| `docs/` | Architecture, exactness, performance, benchmarks, API, FAQ, development |
| `outputs/` | Raw timings and equivalence logs behind every number |
| `demo/` | The two animations, their measured timelines and image credits |

How the engine works (one prefill, branched questions, banks, kernels): [docs/architecture.md](docs/architecture.md).

## Reproducing the benchmarks

Every number comes from one documented command on a single RTX PRO 6000 (Colab G4) with torch 2.14.1+cu130,
transformers 5.23.0 and flash-linear-attention 0.6.0, against vLLM 0.34.0 and SGLang 0.5.23 in their own
environments. The single-image rows, for example:

```bash
CKPT=ckpt_final.pt   # training-format v1 checkpoint (see below)
python -m speed.bench_glance --modes eng_fused --parts lat,mixed,followup --ckpt $CKPT --out speed.json
/content/vllm_env/bin/python -m speed.bench_serve --backend vllm --async_sched --spec mtp --spec_k 2 --quant fp8 \
    --parts lat,mixed,followup,tput,video,gui --out vllm_fp8mtp.json
```

The benchmark scripts load the training-format checkpoint of the v1 weights (`ckpt_final.pt`: config, LoRA and heads
in one file). It holds the same weights as the public
[Glance-4B-preview](https://huggingface.co/Vision-Decision/Glance-4B-preview) release, but it is not public yet; the
Python API and `glance-serve` load the public release directly. One command per workload, baseline flags and setup:
[docs/benchmarks.md](docs/benchmarks.md). The CPU test suite is
`pip install -e '.[test]' && pytest`; the GPU exactness gates are in [docs/exactness.md](docs/exactness.md#running-the-gates).

## Glance-X models

The engine also serves the [Glance-X](docs/glance-x.md) series (X-4B, X2, X-Lite). These are box models with one
backbone and three reading directions: `image_first`, `text_first` and `joint`. They use the same API and server:
`Glance.from_pretrained("Vision-Decision/Glance-X-Lite")`, then `ask(..., direction=...)`. The answers add every target
from the multi-box head. Install with `pip install -e '.[gpu,serve,x]'`.

[Exactness gates and latency](docs/glance-x.md#exactness-and-speed-h200-bf16): with `exact=True` the engine matches
glancex's reference bit for bit. On H200 it is faster than glancex's own CUDA-graph path, for example 61.6 vs 90.1 ms
for 32 requests about one image on X-4B.

## Status and limitations

- Serves Glance and Glance-X models. The v1 engine is tuned and measured on one GPU class (RTX PRO 6000, SM120), and its
  optional kernels fall back to reference paths elsewhere. The X backend is measured on H200.
- BF16 box centres can switch between adjacent patches near a tie; an FP32 backbone fixes this at 3.12× the latency
  and is not yet an engine mode.
- The HTTP server returns raw (uncalibrated) head probabilities; the Python API applies the checkpoint's
  temperatures.
- In progress: in-block zoom for small targets, per-request LoRA scale, and a port to a public hybrid GDN/attention
  model.

The research history (the original engine, scan experiments and raw benchmark files) is on the
[`main`](https://github.com/Vision-Decision/glance-engine/tree/main) branch.

## Related repositories

| Repository | Contents |
|---|---|
| [glance-core](https://github.com/Vision-Decision/glance-core) | The Glance model (`dv` package): architecture, training, evaluation |
| [glance-video](https://github.com/Vision-Decision/glance-video) | Glance-Video, the clip-level model, and its agent-facing scan tools |
| [Glance-4B-preview](https://huggingface.co/Vision-Decision/Glance-4B-preview) | Public model weights and model card |
| [glancex](https://github.com/Vision-Decision/Glance-X-MLX) | The Glance-X model package; weights: [X-4B](https://huggingface.co/Vision-Decision/Glance-X-4B), [X-Lite](https://huggingface.co/Vision-Decision/Glance-X-Lite) |

## License

Apache-2.0 ([LICENSE](LICENSE)). Vendored third-party code keeps its own license: SpecPilot (Apache-2.0) and a FlashAttention header (BSD-3-Clause); see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [NOTICE](NOTICE). Model weights follow their model cards;
Glance-4B-preview is CC BY-NC 4.0.
