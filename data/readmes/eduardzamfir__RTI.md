# Elastic Token Compression for Pixel-Space Diffusion Transformers

#### [Eduard Zamfir<sup>1</sup>](https://eduardzamfir.github.io), [Christian Reisswig<sup>2</sup>](https://scholar.google.com/citations?user=zwrN9NoAAAAJ), [Zongwei Wu<sup>1</sup>](https://sites.google.com/view/zwwu/accueil), [Yongqin Xian<sup>2</sup>](https://xianyongqin.github.io/), [Radu Timofte<sup>1</sup>](https://www.informatik.uni-wuerzburg.de/computervision/)

#### <sup>1</sup>University of Würzburg &nbsp;&nbsp; <sup>2</sup>Google

[![arXiv](https://img.shields.io/badge/arXiv%20paper-2608.29281-b31b1b.svg)](https://arxiv.org/abs/2608.29281)&nbsp;
[![Project Page](https://img.shields.io/badge/Project%20Page-RTI-blue)](https://eduardzamfir.github.io/rti)&nbsp;

<p align="center">
  <img src="assets/teaser.jpg" width="100%">
</p>

---

## Latest

- **[2026-09-10]** Code and checkpoints released.
- **[2026-08-29]** Paper on [arXiv](https://arxiv.org/abs/2608.29281).

---

## Method

> Natural images concentrate their detail in a small fraction of the frame, yet diffusion
> models spend a full token on every patch, in every layer and at every timestep. The waste
> is largest in pixel-space models, with no autoencoder to absorb low-level redundancy
> first. Probing a pretrained pixel text-to-image transformer, we find its middle-block
> tokens redundant wherever the image is flat. The redundancy occupies connected,
> content-shaped regions, and exploiting it requires tokens with the same geometry. Cutting
> a Hilbert ordering of the patches provides them. Consecutive positions are always image
> neighbours, so any contiguous run is a connected region whose size and shape follow the
> content, and grouping in two dimensions becomes a cut in one. Existing reductions each
> lose part of this. Similarity merging scatters its groups, latent bottlenecks discard
> position, and skipping deletes what it should summarize. We cut where the model's
> features change most and pool each run into one region token. Our Region Token Interface
> (RTI) adapts a diffusion model to these tokens, with the region count drawn at random
> during fine-tuning so one checkpoint serves every budget. RTI leads prior reduction
> methods at matched budgets, matches dense quality at 2.0× the speed, and stays close at
> 2.6×.

<p align="center">
  <img src="assets/method.jpg" width="100%">
</p>

A frozen MiniT2I backbone runs its middle blocks on `R ≪ N` region tokens:

```
prelude (dense) → cut → Read (soft pool) → core on R tokens → Write (scatter back) → coda (dense)
```

The cut orders patches along a Hilbert curve and splits at the `R-1` largest adjacent
feature distances, so every region is a contiguous run of the curve and therefore a
connected, content-shaped image region. `Read` soft-pools each run into one token; `Write`
gives every member its own delta from its region's delta. Only LoRA on the frozen trunk
and the small interface are trained, and **`R` is drawn per step during fine-tuning, so a
single checkpoint serves every budget** — pass `--budget` at inference to move along the
quality/compute curve.

---

## Results

GenEval, 553 prompts × 4 samples, cfg 5.0, 100 steps (`N = 1024` tokens is dense):

| backbone | method | R | GenEval | CLIP | Pick | IR | speedup |
|---|---|---|---|---|---|---|---|
| **B/16** | dense | 1024 | 87.2 | 28.23 | 22.45 | 1.18 | 1.00× |
| | Token Skip | 576* | 82.3 | 28.08 | 21.93 | 1.06 | 1.19× |
| | Feat Sim | 512 | 84.7 | 28.04 | 22.04 | 1.07 | 1.84× |
| | **RTI** | 512 | **87.8** | 28.09 | 22.30 | 1.11 | 1.84× |
| | Feat Sim | 256 | 80.5 | 27.73 | 21.57 | 0.93 | 2.15× |
| | Latent Array | 256 | 45.7 | 23.30 | 19.78 | −0.65 | 2.15× |
| | **RTI** | 256 | **84.7** | 28.04 | 22.06 | 1.06 | 2.15× |
| **L/16** | dense | 1024 | 88.1 | 28.50 | 22.75 | 1.23 | 1.00× |
| | Feat Sim | 512 | 83.1 | 28.80 | 22.34 | 1.16 | 2.11× |
| | **RTI** | 512 | **87.5** | 28.58 | 22.63 | 1.20 | 2.11× |
| | Feat Sim | 256 | 76.5 | 28.31 | 21.76 | 1.01 | 2.59× |
| | **RTI** | 256 | **86.3** | 28.52 | 22.37 | 1.17 | 2.59× |

<sub>*Token Skip sets a capacity, not a budget; 576 is the derived mean image tokens per core block.</sub>

### Reproduced with this codebase

| arm | GenEval | CLIP | PickScore | ImageReward |
|---|---|---|---|---|
| | paper / here | paper / here | paper / here | paper / here |
| B/16, R=512 | 87.8 / 87.30 | 28.09 / 28.06 | 22.30 / 22.30 | 1.11 / 1.10 |
| B/16, R=256 | 84.7 / 85.18 | 28.04 / 27.99 | 22.06 / 22.07 | 1.06 / 1.06 |
| L/16, R=512 | 87.5 / 87.52 | 28.58 / 28.65 | 22.63 / 22.64 | 1.20 / 1.20 |
| L/16, R=256 | 86.3 / 85.93 | 28.52 / 28.53 | 22.37 / 22.38 | 1.17 / 1.17 |

Per-task breakdowns and raw scorer output: [`results/reproduction/`](results/reproduction/).

MJHQ-30K FID (L/16, 30 000 prompts, cfg 5.0, clean-fid):

| arm | FID ↓ | speedup |
|---|---|---|
| dense | **9.07** | 1.00× |
| RTI, R=512 | **11.43** | 2.11× |
| Feat Sim, R=512 | 19.99 | 2.11× |
| RTI, R=256 | **14.71** | 2.59× |
| Feat Sim, R=256 | 28.02 | 2.59× |

---

## Installation

```bash
git clone https://github.com/eduardzamfir/RTI.git
cd RTI
conda create -n rti python=3.10 -y
conda activate rti
pip install -r requirements.txt
```

The MiniT2I backbone is downloaded from the Hugging Face release on first use; this
repository ships adapters only.

---

## Pretrained models

| model | span | budgets | link |
|---|---|---|---|
| RTI-B/16 | 3–13 | 64 – 1024 | [`eduardzamfir/RTI`](https://huggingface.co/eduardzamfir/RTI) → `rti_b16_40k.pt` |
| RTI-L/16 | 3–19 | 64 – 1024 | [`eduardzamfir/RTI`](https://huggingface.co/eduardzamfir/RTI) → `rti_l16_40k.pt` |

Each checkpoint holds LoRA and interface tensors only — 62 MB for B/16, 137 MB for
L/16 — and serves **every** budget in the range.

---

## Usage

### Sampling

```bash
python sample.py --ckpt rti_b16.pt --variant MiniT2I-B/16 \
    --prompt "a red panda wearing a scarf, studio photo" \
    --budget 1024 512 256 128 64 --steps 100 --cfg 5.0
```

Passing several budgets writes a grid so the compute dial is visible on one image.

### Evaluation

```bash
# GenEval
torchrun --nproc_per_node=4 -m eval.generate \
    --ckpt rti_b16.pt --variant MiniT2I-B/16 --budget 256 \
    --metadata eval/prompts/geneval.jsonl --outdir $TMPDIR/geneval_r256 \
    --samples-per-prompt 4 --cfg 5.0 --steps 100
python eval/geneval/evaluate_images.py $TMPDIR/geneval_r256 \
    --outfile results/geneval.jsonl --model-path <mask2former-weights>
python eval/geneval/summary_scores.py results/geneval.jsonl results/geneval.json

# PartiPrompts (CLIP / PickScore / ImageReward)
torchrun --nproc_per_node=4 -m eval.generate \
    --ckpt rti_b16.pt --budget 256 --metadata eval/prompts/partiprompts.jsonl \
    --outdir $TMPDIR/parti_r256 --samples-per-prompt 1
python -m eval.imscore --imgdir $TMPDIR/parti_r256 --scorers clip,pickscore,imagereward

# MJHQ-30K FID (fetch the prompt list from the MJHQ-30K release first)
torchrun --nproc_per_node=8 -m eval.generate \
    --ckpt rti_l16.pt --variant MiniT2I-L/16 --budget 512 \
    --metadata mjhq30k.jsonl --outdir $TMPDIR/mjhq_r512 --samples-per-prompt 1
python -m eval.fid --imgdir $TMPDIR/mjhq_r512 --dataset mjhq30k
```

A Slurm launcher that does all three stages in one job is in `scripts/`.

### Training

Prepare the fine-tuning corpus once (image/caption WebDataset shards):

```bash
python prepare_data.py --out /path/to/minit2i_ft
```

then fine-tune the interface and LoRA on the frozen backbone:

```bash
torchrun --nproc_per_node=8 train.py \
    --data-root /path/to/minit2i_ft --variant MiniT2I-B/16 --span 3,13 \
    --micro-batch 16 --grad-accum 2 --num-steps 40000 --lr 1e-4 \
    --budget-tiers 64,128,256,512 --out-dir runs/rti_b16
```

The released B/16 checkpoint used exactly this command; L/16 used `--span 3,19
--micro-batch 8 --grad-accum 8`.

---

## Citation

```bibtex
@article{zamfir2026rti,
  title   = {Elastic Token Compression for Pixel-Space Diffusion Transformers},
  author  = {Zamfir, Eduard and Reisswig, Christian and Wu, Zongwei and
             Xian, Yongqin and Timofte, Radu},
  journal = {arXiv preprint arXiv:2608.29281},
  year    = {2026}
}
```

---

## Acknowledgements

Built on [MiniT2I](https://huggingface.co/MiniT2I/MiniT2I) and the
[JiT](https://github.com/LTH14/JiT) line of pixel-space diffusion transformers. Evaluation
uses [GenEval](https://github.com/djghosh13/geneval), PartiPrompts, MJHQ-30K and
[clean-fid](https://github.com/GaParmar/clean-fid). The released checkpoints are adapters
over the MiniT2I backbone, which keeps its own licence; the evaluation sets and the
fine-tuning corpus keep theirs.

---

## License

[MIT](LICENSE), matching the MiniT2I backbone this builds on.

This covers the code and the released adapter weights. It does **not** cover the MiniT2I
backbone, its fine-tuning corpus, or any evaluation set (GenEval, PartiPrompts,
MJHQ-30K) — each keeps its own terms.
