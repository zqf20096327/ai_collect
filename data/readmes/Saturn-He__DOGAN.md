<div align="center">

# DOGAN

### DINO-Based Optical-Prior-Driven GAN<br>for SAR-to-Optical Image Translation

**IEEE Transactions on Geoscience and Remote Sensing · 2025**

Jingfei He<sup>†</sup>, Liang Chen<sup>†</sup>, Hao Shi, Yuhang Chen, Jingyi Yang, Wei Li

<sub>† Equal contribution</sub>

[![Paper](https://img.shields.io/badge/IEEE_TGRS-Paper-00629B)](https://doi.org/10.1109/TGRS.2025.3606979)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](#-setup)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1-EE4C2C?logo=pytorch&logoColor=white)](#-setup)

[Overview](#-overview) · [Visual Results](#-visual-results) · [Setup](#-setup) · [Training & Inference](#data-and-commands) · [Evaluation](#-evaluation) · [Citation](#-citation)

</div>

## 🔍 Overview

**DOGAN transfers optical priors from a pretrained DINO model into a SAR-to-optical translation GAN.** During training, a frozen DINO backbone and lightweight adapters provide multiscale optical features that guide the generator through domain alignment. At inference, the trained generator translates SAR images into optical-like images.

<p align="center">
  <a href="assets/Overview_1.png"><img src="assets/Overview_1.png" width="100%" alt="DOGAN training framework: generator, DINO optical-prior extraction, SOA adapters, and multiscale domain alignment"></a>
</p>

**Training framework.** Optical priors guide the generator at multiple feature scales.

| Component | Role |
| :--- | :--- |
| **DOE** — DINO-based Optical-prior Extraction | Extracts multiscale optical priors from a pretrained DINO backbone. |
| **SOA** — Stacked Optical-Aware adapter | Adapts optical representations to remote sensing while keeping DINO frozen. |
| **SO-MDA** — SAR-optical Multi-scale Domain Alignment | Aligns optical and translation features using L1 and MK-MMD losses. |

<p align="center">
  <a href="assets/Overview_2.png"><img src="assets/Overview_2.png" width="100%" alt="DOGAN inference framework: SAR image to translated optical image through the trained generator"></a>
</p>

**Inference framework.** The generator performs SAR-to-optical translation without the optical-prior extraction branch.

## 🖼️ Visual Results

Qualitative comparisons from the paper on **SAR2Opt** and **SEN1-2**. Click each figure to inspect the original resolution. These are the paper's results, not outputs of a new run of this release.

### SAR2Opt

[![Qualitative comparison on SAR2Opt](assets/SAR2Opt_comparative_results.jpg)](assets/SAR2Opt_comparative_results.jpg)

<details>
<summary><strong>SEN1-2 — expand the qualitative comparison</strong></summary>

[![Qualitative comparison on SEN1-2](assets/SEN12_comparative_results.jpg)](assets/SEN12_comparative_results.jpg)

</details>

This repository provides training, inference, and image-quality evaluation code.

## 🛠️ Setup

Use Python 3.10. Install PyTorch 2.1 and torchvision 0.16 for your CUDA version, then run:

```bash
pip install -r requirements.txt
```

Download the [DINO ViT-S/16 weights](https://dl.fbaipublicfiles.com/dino/dino_deitsmall16_pretrain/dino_deitsmall16_pretrain.pth) to `pretrained_dino/dino_deitsmall16_pretrain.pth` for training. The training code can download the torchvision ResNet-50 weights on first use. For inference supply a trained generator checkpoint under `checkpoints/DOGAN/200_net_G_trans.pth`, or use the checkpoint produced by the training command below.

## Data and commands

Provide your own paired SAR and optical images. Put SAR images in `trainA/` and `testA/`, and optical targets in `trainB/` and `testB/`. Paired images must have matching relative filenames.

```text
paired_dataset/
├── trainA/   # SAR training images
├── trainB/   # Paired optical training images
├── testA/    # SAR test images
└── testB/    # Paired optical test images
```


```bash
python scripts/run_dogan.py --mode train --dataroot /path/to/paired_dataset
python scripts/run_dogan.py --mode test --dataroot /path/to/paired_dataset
```

Run from the repository root. By default, training uses 256-pixel crops and testing processes all pairs in the supplied test folders. Use `--num_test` to set an optional test limit. To use the 512-pixel preprocessing profile, pass `--config configs/crop512.json` to both commands and use the corresponding `DOGAN_512` checkpoint and output folders.

## 📊 Evaluation

Inference writes images under `results/DOGAN/test_200/images/`. Run the six paper image-quality metrics separately:

```bash
python evaluate.py --gt /path/to/paired_dataset/testB \
  --pred results/DOGAN/test_200/images \
  --output results/DOGAN/metrics.json
```

The evaluator matches GT and predictions by stem after removing `_fake_B` from the prediction name. Set `--pred-suffix ""` if the stems already match. Use `--check-pairs` to check alignment. By default it evaluates at the native resolution. Set `--resize WIDTH HEIGHT` for image pairs requiring common dimensions.

The evaluator reports PSNR, SSIM, CW-SSIM, RMSE, LPIPS and SAM. PSNR defaults to the legacy PIL luminance convention. Select `--psnr-color rgb` to measure RGB PSNR. SSIM and RMSE operate on RGB at an intensity range of 0–255. CW-SSIM uses pyssim 0.7. LPIPS uses AlexNet with spatial averaging, and SAM uses the legacy image-similarity-measures implementation. Resizing applies to all six metrics when requested. Scores on historical splits depend on the exact files, preprocessing and checkpoint used.

## 📖 Citation

If you use DOGAN in your research, please cite our paper:

> J. He, L. Chen, H. Shi, Y. Chen, J. Yang, and W. Li, “DOGAN: DINO-Based Optical-Prior-Driven GAN for SAR-to-Optical Image Translation,” *IEEE Transactions on Geoscience and Remote Sensing*, vol. 63, pp. 1–16, 2025. DOI: [10.1109/TGRS.2025.3606979](https://doi.org/10.1109/TGRS.2025.3606979).

### BibTeX

Copy the entry below into your LaTeX bibliography, or download [DOGAN.bib](DOGAN.bib). Cite it with `\cite{he2025dogan}`.

```bibtex
@article{he2025dogan,
  author  = {He, Jingfei and Chen, Liang and Shi, Hao and Chen, Yuhang and Yang, Jingyi and Li, Wei},
  title   = {{DOGAN}: {DINO}-Based Optical-Prior-Driven {GAN} for {SAR}-to-Optical Image Translation},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  year    = {2025},
  volume  = {63},
  pages   = {1--16},
  doi     = {10.1109/TGRS.2025.3606979},
  url     = {https://doi.org/10.1109/TGRS.2025.3606979}
}
```

## Acknowledgments

The implementation builds on [Parallel-GAN](https://doi.org/10.1109/TGRS.2022.3200996), [CycleGAN and pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix), and [DINOv2](https://github.com/facebookresearch/dinov2). See the upstream projects for their terms and notices.

We thank the authors for making their code publicly available.

## 🔗 Our Related Projects

Explore our related work on optical priors, colour control, and cross-tile consistency in SAR-to-optical image translation. Click an overview to view the full-size figure.

### [ColorS2O](https://github.com/Saturn-He/ColorS2O)

**Controllable SAR-to-Optical Image Translation with Sparse Colour Anchors**

<p>
  <a href="https://github.com/Saturn-He/ColorS2O/blob/main/assets/framework.png">
    <img src="https://raw.githubusercontent.com/Saturn-He/ColorS2O/main/assets/framework.png" width="360" alt="ColorS2O framework overview">
  </a>
</p>

ColorS2O uses sparse colour anchors from an optical observation to control the colours of translated images.

### [XTile-S2O](https://github.com/Saturn-He/XTile-S2O)

**Cross-Tile Coherent Full-Scene SAR-to-Optical Image Translation**

<p>
  <a href="https://github.com/Saturn-He/XTile-S2O/blob/main/assets/figures/overview.png">
    <img src="https://raw.githubusercontent.com/Saturn-He/XTile-S2O/main/assets/figures/overview.png" width="360" alt="XTile-S2O framework overview">
  </a>
</p>

XTile-S2O shares context across neighbouring tiles to improve spatial consistency in full-scene SAR-to-optical translation.

### [SADBM](https://github.com/AproZC/SADBM)

**Structure-Aware Diffusion Bridge Model for SAR-to-Optical Image Translation**

<p>
  <a href="https://github.com/Saturn-He/DOGAN/blob/main/assets/sadbm-teaser.jpg">
    <img src="https://raw.githubusercontent.com/Saturn-He/DOGAN/main/assets/sadbm-teaser.jpg" width="360" alt="SADBM comparison with conditional diffusion models and GANs">
  </a>
</p>

SADBM uses an edge-enhanced SAR image as the starting point of a diffusion bridge to preserve scene structure in SAR-to-optical image translation.
