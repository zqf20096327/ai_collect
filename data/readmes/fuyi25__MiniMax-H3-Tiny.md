<div align="center">

# H3-Tiny

**Structured pruning of MiniMax H3 Ref2VA: 33B → 17B → 14B**

[![Project page](https://img.shields.io/badge/Project-Page-1f6feb)](https://fuyi25.github.io/MiniMax-H3-Tiny/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-ffcc4d)](https://huggingface.co/H3-Tiny)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Single--file%20weights-f0883e)](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-ComfyUI)
![arXiv](https://img.shields.io/badge/arXiv-coming%20soon-b31b1b)
[![Code license](https://img.shields.io/badge/Code-Apache%202.0-555)](LICENSE)

<img src="assets/teaser-v2.jpg" width="100%" alt="Samples from H3-Tiny 17B, pruned with no training, 50 steps">

<sub>Samples from <b>H3-Tiny 17B</b>: pruned with no training, 50 steps, with its own synchronized audio.</sub>

</div>

Joint video + audio generation from text and reference images, at about half the size of the original, with recovered
and few-step checkpoints.

🧩 **Using ComfyUI?** Every checkpoint also comes as a single file in
[MiniMax-H3-Tiny-ComfyUI](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-ComfyUI); see [ComfyUI](#comfyui).

<p align="center"><img src="assets/blocks.png" width="100%" alt="Block influence per block for video and audio tokens; blocks removed in the 17B"></p>

## News

- **[2026/11/22]** The checkpoints are renamed to `MiniMax-H3-Tiny-*` on Hugging Face (old links redirect), and the
  ComfyUI files to `minimax_h3_tiny_*.safetensors`.
- **[2026/11/21]** ComfyUI support: single-file checkpoints in
  [`MiniMax-H3-Tiny-ComfyUI`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-ComfyUI) load with ComfyUI's native MiniMax H3 nodes
  (17B Ref2VA, 17B FL2VA / T2VA, 14B OKD Ref2VA, and 17B FewStep with our nodes). See [ComfyUI](#comfyui).
- **[2026/11/20]** We release [`MiniMax-H3-Tiny-17B-Pruned-FL2VA`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-17B-Pruned-FL2VA),
  the H3 FL2VA / T2VA transformer pruned to 17B with no training.
- **[2026/11/19]** We release the pruning and inference code and the [project page](https://fuyi25.github.io/MiniMax-H3-Tiny/).
- **[2026/11/19]** We release three checkpoints on [Hugging Face](https://huggingface.co/H3-Tiny): `MiniMax-H3-Tiny-17B-Pruned-Ref2VA`,
  `MiniMax-H3-Tiny-17B-FewStep-Ref2VA-v0.1` and `MiniMax-H3-Tiny-14B-OKD-Ref2VA-v0.1`.

## Checkpoints

| Checkpoint | Parameters | Made by | Sampling | Released |
|---|---|---|---|:---:|
| [`MiniMax-H3-Tiny-17B-Pruned-Ref2VA`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-17B-Pruned-Ref2VA) | 17.1B | AdaLN rank 8 + 8 of 50 blocks removed, **no training** | 50 steps | ✅ |
| [`MiniMax-H3-Tiny-17B-Pruned-FL2VA`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-17B-Pruned-FL2VA) | 17.1B | Same recipe on the FL2VA / T2VA transformer (same 8 blocks removed), **no training** | 50 steps | ✅ |
| [`MiniMax-H3-Tiny-17B-FewStep-Ref2VA-v0.1`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-17B-FewStep-Ref2VA-v0.1) | 17.1B | 17B, few-step distillation | **6 steps** by default (4 or more) | ✅ |
| [`MiniMax-H3-Tiny-14B-OKD-Ref2VA-v0.1`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-14B-OKD-Ref2VA-v0.1) | 14.0B | 17B with FFNs narrowed to 9792 channels, recovered by OKD (distillation from the 33B teacher) | 50 steps | ✅ |
| `MiniMax-H3-Tiny-14B-FewStep-Ref2VA` | 14.0B | 14B OKD, then few-step distillation | **6 steps** by default (4 or more) | coming soon |

**The 17B works well straight out of pruning, with no training at all!**

This release contains the pruning code and the inference code; the recovery (OKD) and few-step training code will
follow.

## Roadmap

- [x] Pruning code: AdaLN low-rank, block removal, FFN narrowing
- [x] Inference: 50-step and few-step (6 steps by default, 4 or more)
- [x] Weights: 17B pruned, 17B few-step v0.1, 14B OKD v0.1
- [x] FL2VA / T2VA: 17B pruned
- [x] ComfyUI checkpoints
- [ ] Weights: 14B few-step
- [ ] OKD recovery training code
- [ ] Few-step distillation code

## Method

1. **AdaLN low-rank.** The per-block AdaLN projections hold 13.0B of the 33.1B parameters. Their input is a fixed
   function of the timestep, so we fit a rank-8 approximation on that input directly, with no data.
2. **Block removal.** We measure how much each block changes video and audio tokens, protect the blocks the audio
   depends on most, and remove 8 of the 50 blocks (6–11, 13 and 15), giving the 17B.
3. **FFN narrowing.** For the 14B, every FFN keeps 9792 of 14336 channels and its output projection is refit,
   followed by a short recovery training distilled from the 33B.

## Installation

```bash
pip install -e .        # torch>=2.6, torchaudio, diffusers>=0.42, safetensors, transformers
```

You also need the official MiniMax H3 checkpoint in diffusers format for the text encoder, VAEs and processors (and
the 33B transformer, to prune it yourself).

## Inference

```bash
python scripts/infer.py --weights ckpt/MiniMax-H3-Tiny-17B-FewStep-Ref2VA-v0.1 --base-model /models/MiniMax-H3 \
    --prompt "<Picture 1> ..." --references ref1.png --num-frames 124 --out outputs/
```

Prompts name the references `<Picture 1>`, `<Picture 2>`, ... in the order given. Full-step checkpoints default to 50
steps and few-step checkpoints to 6; few-step checkpoints run with 4 or more steps (`--steps 4` for speed, `--steps 8` for more detail). `--cases cases.jsonl`
runs a list of clips, sharded with `--shard` / `--num-shards`; `--offload` fits GPUs below ~110 GB. Attention runs on
FlashAttention-3 on Hopper GPUs when the `kernels` package is installed (`pip install -e .[fa3]`) and on PyTorch SDPA
otherwise; force one with `--attention fa3` or `--attention sdpa`. From Python:

```python
from h3tiny.pipeline import load_pipeline
pipe = load_pipeline("ckpt/MiniMax-H3-Tiny-17B-FewStep-Ref2VA-v0.1", "/models/MiniMax-H3", device="cuda")
```

For FL2VA (first + last frame) and T2VA (text only), use `MiniMax-H3-Tiny-17B-Pruned-FL2VA` with `--workflow`:

```bash
python scripts/infer.py --weights ckpt/MiniMax-H3-Tiny-17B-Pruned-FL2VA --base-model /models/MiniMax-H3 --workflow fl2va \
    --image first.png --last-image last.png --prompt "For the target video, at 0.00 seconds ..." --num-frames 124 --out outputs/
python scripts/infer.py --weights ckpt/MiniMax-H3-Tiny-17B-Pruned-FL2VA --base-model /models/MiniMax-H3 --workflow t2va \
    --prompt "integrated_multimodal_description: ..." --num-frames 124 --out outputs/
```

The pipeline is the official diffusers MiniMax H3 workflow with the H3-Tiny transformer and step schedule
(`h3tiny/pipeline.py`).

## ComfyUI

[`MiniMax-H3-Tiny-ComfyUI`](https://huggingface.co/H3-Tiny/MiniMax-H3-Tiny-ComfyUI) holds the checkpoints as single files for
ComfyUI's native MiniMax H3 support:

| File | Workflow node |
|---|---|
| `minimax_h3_tiny_17b_ref2va_bf16.safetensors` | MiniMax H3 Reference to Video |
| `minimax_h3_tiny_17b_fl2va_bf16.safetensors` | MiniMax H3 Image to Video (FL2VA with first / last frames, T2VA without) |
| `minimax_h3_tiny_14b_okd_ref2va_bf16.safetensors` | MiniMax H3 Reference to Video |
| `minimax_h3_tiny_17b_fewstep_ref2va_bf16.safetensors` | MiniMax H3 Reference to Video, with the H3-Tiny nodes below |

Put the file in `ComfyUI/models/diffusion_models/`, take the text encoder and VAEs from
[Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3), and select the file in **Load Diffusion Model**.
Sample with 50 steps, the `simple` scheduler and no CFG (`BasicGuider`), without the turbo LoRA.

The few-step checkpoint also needs the time-step endpoint, which stock ComfyUI does not pass. Install our nodes:

```bash
ln -s /path/to/MiniMax-H3-Tiny/comfyui ComfyUI/custom_nodes/ComfyUI-MiniMax-H3-Tiny
```

Then load the file with **H3-Tiny Few-Step Loader** instead of Load Diffusion Model, and take the sigmas from
**H3-Tiny Few-Step Sigmas** (6 steps by default, 4 or more work) into `SamplerCustomAdvanced` with the `euler` sampler
and `BasicGuider`.

To convert a diffusers checkpoint yourself:

```bash
python scripts/convert_comfyui.py --src ckpt/MiniMax-H3-Tiny-17B-Pruned-Ref2VA --out minimax_h3_tiny_17b_ref2va_bf16.safetensors
```

## Pruning

**1. Encode calibration clips.** One JSONL line per clip; the ground-truth clip must have a soundtrack:

```json
{"sample_id": "0001", "prompt": "<Picture 1> ...", "references": ["ref1.png"], "video": "gt.mp4", "num_frames": 124}
```

```bash
python scripts/prepare_samples.py --base-model /models/MiniMax-H3 --manifest calibration.jsonl --out cache/calibration
python scripts/prepare_samples.py --base-model /models/MiniMax-H3 --manifest tuning.jsonl --out cache/tuning
```

Each clip goes through the official ref2va workflow (same encoders, packing and conditioning noise as inference);
the denoising loop is replaced by a capture step that keeps the transformer inputs with the ground-truth latents as
targets (`h3tiny/data.py`). We used 24 calibration and 8 tuning clips. For the FL2VA / T2VA transformer, give each line a `"workflow": "fl2va"` or `"t2va"` field
(FL2VA uses the clip's first and last frames) and point `--base` of the pruning step at the official `transformer`
folder instead of `transformer_ref`.

**2. 33B → 17B** (one GPU with ~80 GB):

```bash
python scripts/prune_depth.py --base /models/MiniMax-H3/transformer_ref \
    --calibration cache/calibration --tuning cache/tuning --out ckpt/h3tiny-17b
# or reuse the released plan, which needs no clips:  --drop 6 7 8 9 10 11 13 15
```

**3. 17B → 14B:**

```bash
python scripts/prune_width.py --parent ckpt/h3tiny-17b \
    --calibration cache/calibration --tuning cache/tuning --out ckpt/h3tiny-14b
```

## Tests

```bash
python -m pytest tests/test_prune.py                # pruning math, CPU, no weights
python tests/smoke_pipeline.py /tmp/h3tiny-smoke    # tiny random model through both pruning scripts, CPU
```

## Citation

```bibtex
@misc{h3tiny2026,
  title        = {H3-Tiny: Structured Pruning of MiniMax H3},
  author       = {Fu, Haoshuai and Chen, Bin},
  year         = {2026},
  howpublished = {\url{https://github.com/fuyi25/MiniMax-H3-Tiny}},
  note         = {arXiv coming soon}
}
```

## Contact

Questions and bug reports: please [open an issue](https://github.com/fuyi25/MiniMax-H3-Tiny/issues). For anything else,
email Haoshuai Fu at [fohoo@outlook.com](mailto:fohoo@outlook.com).

## License

Code: [Apache 2.0](LICENSE). Model weights: [MiniMax H3 Community License Agreement](LICENSE-MiniMax-H3); see
[NOTICE](NOTICE). Use of the weights must follow that agreement, including its territorial scope and acceptable-use
policy.

*H3-Tiny is an independent project and is not affiliated with or endorsed by MiniMax. The model weights are Model
Derivatives of MiniMax H3 and are distributed under the
[MiniMax H3 Community License Agreement](LICENSE-MiniMax-H3).*
