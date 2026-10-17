# Twins: Learn to Predict Unified Representations with Focal Loss

> [**Twins: Learn to Predict Unified Representations with Focal Loss**](https://openreview.net/pdf?id=UvWZFnG1Np)<br>
> [Kaixiong Gong, Xin Cai, Bin Lin, Hao Wang, Yunlong Lin, Mingzhe Zheng, Bohao Li, Jian-Wei Zhang, Miles Yang, Zhao Zhong, Liefeng Bo, Xiangyu Yue](https://openreview.net/pdf?id=UvWZFnG1Np)

Twins learns to predict a **unified representation** for multimodal understanding and
generation, using a **focal loss** to better model continuous representation targets.

This repository releases the generation experiment from the paper: a Stage-2 latent
**Diffusion Transformer** trained on the latent space of a **SigLIP2 + Flux-VAE**
Representation Autoencoder ([RAE](https://github.com/bytetriper/RAE)) with a focal/MSE
objective. It contains a single Stage-2 training config, its sampling configs, and the
minimal source needed to train, sample, and evaluate it.

## Overview

- **Stage 1 (frozen):** `RAESiglipVAE` — a SigLIP2-base encoder paired with a
  Flux VAE. Image patches are encoded into an `[896, 16, 16]` latent.
- **Stage 2 (trained):** `DiTwDDTHead` (DiT<sup>DH</sup>-XL) — a dual-head
  diffusion transformer trained on the SigLIP-VAE latents with a focal/MSE loss.
- **Sampling:** ODE (Euler) with classifier-free guidance or autoguidance.

## Environment

```bash
conda create -n <env> python=3.10 -y
conda activate <env>

# PyTorch (CUDA 12.8)
pip install torch==2.9.0 torchvision==0.24.0 torchaudio --index-url https://download.pytorch.org/whl/cu128

# Other dependencies
pip install -r requirements.txt
```

## Data & Model Preparation

1. **ImageNet-1k.** Download and lay out the training split in the standard
   `ImageFolder` format. Point the training script to it via `DATA_PATH`.

2. **Flux VAE.** The SigLIP-VAE encoder loads a Flux VAE through `diffusers`.
   Provide it via the `FLUX_VAE_PATH` environment variable (a local path or a
   HuggingFace repo id); it defaults to `models/flux2-dev`:

   ```bash
   export FLUX_VAE_PATH=/path/to/flux-vae   # contains a `vae/` subfolder
   ```

3. **Latent normalization stats.** The configs reference two stat files:

   ```
   models/stats/flux2vae/imagenet1k/stat.pt
   models/stats/siglip2/base_p16_i256/ImageNet1k/stat.pt
   ```

   Place them at those paths (the `models/` directory is git-ignored).

## Training

```bash
# Single node (8 GPUs by default)
DATA_PATH=/path/to/imagenet/train bash scripts/train.sh
```

Multi-node — set the rendezvous variables per node:

```bash
NNODES=4 NODE_RANK=0 MASTER_ADDR=<chief-ip> MASTER_PORT=29519 \
DATA_PATH=/path/to/imagenet/train bash scripts/train.sh
```

Checkpoints and logs are written under `results/stage2/` (configurable via
`RESULTS_DIR`). To enable Weights & Biases, export `WANDB_KEY` / `WANDB_ENTITY`
/ `WANDB_PROJECT` and add `--wandb` in `scripts/train.sh`.

Key config: `configs/stage2/training/ImageNet256/DiTDH-XL_twins.yaml`.

### Variant: DiT on pure Flux-VAE latents

To instead train the DiT on a frozen Flux VAE latent space (no SigLIP branch),
use the Flux-VAE entrypoint:

```bash
DATA_PATH=/path/to/imagenet/train bash scripts/train_fluxvae.sh
```

Key config: `configs/stage2/training/ImageNet256/DiTDH-XL_fluxvae.yaml`. Sample
it with `CONFIG=configs/stage2/sampling/ImageNet256/DiTDH-XL_fluxvae.yaml bash scripts/sample.sh`.

## Sampling

Set the trained checkpoint in the sampling config's `ckpt:` field, then:

```bash
# Classifier-free guidance
bash scripts/sample.sh

# Autoguidance (set both ckpts in the _AG config)
CONFIG=configs/stage2/sampling/ImageNet256/DiTDH-XL_siglip_vae_fixed_zero_focal_mse_AG.yaml \
  bash scripts/sample.sh
```

`--label-sampling equal` is used by default (exactly 50 images/class for FID-50k).

## Evaluation (FID)

1. Pack the generated images into a single `.npz`:

   ```bash
   python scripts/compress_samples_to_npz.py --sample_dir samples/final
   ```

2. Score with the [ADM evaluation suite](https://github.com/openai/guided-diffusion)
   in a separate environment:

   ```bash
   wget https://openaipublic.blob.core.windows.net/diffusion/jul-2021/ref_batches/imagenet/256/VIRTUAL_imagenet256_labeled.npz
   python evaluator.py VIRTUAL_imagenet256_labeled.npz samples/final.npz
   ```

## Configuration

Everything is driven by OmegaConf YAML. A config describes the Stage-1
autoencoder (`stage_1`), the Stage-2 diffusion transformer (`stage_2`), the
`transport` / `sampler` / `guidance` settings, shared `misc` shapes, and
`training` hyperparameters. See the provided configs for the exact schema.

## License & Acknowledgement

Released under the [MIT License](LICENSE). If you use this code, please cite
[Twins](https://openreview.net/pdf?id=UvWZFnG1Np):

```bibtex
@inproceedings{gongtwins,
  title={Twins: Learn to Predict Unified Representations with Focal Loss},
  author={Gong, Kaixiong and Cai, Xin and Lin, Bin and Wang, Hao and Lin, Yunlong and Zheng, Mingzhe and Li, Bohao and Zhang, Jian-Wei and Yang, Miles and Zhong, Zhao and others},
  booktitle={Forty-third International Conference on Machine Learning}
}
```

Built upon:

- [RAE](https://github.com/bytetriper/RAE) — Diffusion Transformers with Representation Autoencoders

- [SiT](https://github.com/willisma/sit) — diffusion implementation and training codebase
- [DDT](https://github.com/MCG-NJU/DDT) — parts of the DiT<sup>DH</sup> implementation
- [LightningDiT](https://github.com/hustvl/LightningDiT/) — Lightning-based DiT implementation
- [MAE](https://github.com/facebookresearch/mae) — ViT decoder architecture
