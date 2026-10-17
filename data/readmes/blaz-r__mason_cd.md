<div align="center">
<h1>MaSoN - Make Some Noise</h1>
<h2>Unsupervised Remote Sensing Change Detection Using Latent Space Perturbations</h2>
<h3>IEEE Transactions on Geoscience and Remote Sensing 2026</h3>

[Blaž Rolih](https://scholar.google.com/citations?user=Qs-k2PkAAAAJ),
[Matic Fučka](https://scholar.google.com/citations?user=2kdcuAkAAAAJ),
[Filip Wolf](https://scholar.google.com/citations?user=1i7eNmwAAAAJ),
[Luka Čehovin Zajc](https://scholar.google.com/citations?hl=en&user=XKc1wdcAAAAJ)

University of Ljubljana, Faculty of Computer and Information Science

[![TGRS](https://img.shields.io/badge/TGRS-paper-00629B.svg)](https://doi.org/10.1109/TGRS.2026.3730181)
[![arXiv](https://img.shields.io/badge/arXiv-2602.19881-b31b1b.svg)](https://arxiv.org/abs/2602.19881)
[![Project](https://img.shields.io/badge/Project-page-00629B.svg)](https://blaz-r.github.io/mason_ucd/)

[![Model on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/collections/blaz-r/mason-change-detection)
[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-md.svg)](https://huggingface.co/spaces/blaz-r/MaSoN-CD-demo)

</div>
Train a remote sensing change detector without annotated change masks. MaSoN synthesises relevant changes and irrelevant variations in the latent space of a frozen foundation model, using noise calibrated to your target data.

- **Data-adaptive training**: synthesise changes directly from target-domain feature statistics.
- **Strong benchmark results**: best results on four of five evaluated datasets, with a 14.1 percentage-point improvement in average F1 over the prior methods compared in the paper.
- **Ready to explore**: a browser demo, pretrained checkpoints, and training and evaluation code.

<p align="center">
    <img src="assets/title.svg" alt="image showing improved generalisation">
</p>

[Quickstart](#quickstart) | [Checkpoints](#pretrained-checkpoints) | [Training](#train-on-your-target-domain) | [Data](#data) | [How it works](#how-it-works) | [Citation](#citation) | [Questions](#questions)

## Quickstart

### Install

```bash
git clone https://github.com/blaz-r/mason_cd.git
cd mason_cd

conda create -n mason_env python=3.12
conda activate mason_env
pip install -r requirements.txt
```

### Enable backbone access:

The default configuration loads DINOv3 ViT-L/16. Request access on its [model page](https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m/tree/main) and authenticate with an account that has access:
```
hf auth login
```

Frozen DINOv3 weights are loaded separately from Meta's repository; they are omitted from MaSoN checkpoints saved by this code. Backbone access is therefore required for local training and evaluation.

### Evaluate a pretrained checkpoint

```bash
python train.py --config configs/mason.yaml \
  --data.dataset oscd96 \
  --eval_only --ckpt_path blaz-r/mason_oscd96
```

This downloads the OSCD dataset and MaSoN checkpoint, runs benchmark evaluation, and writes metrics to `res.csv` under `./results`. The first run also downloads the backbone. 

This command evaluates a dataset, use the browser demo to try an individual image pair: 

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/blaz-r/MaSoN-CD-demo)

## Pretrained checkpoints

Choose the checkpoint for your use case:

| Use case | Checkpoint |
| --- | --- |
| Zero-shot Sentinel-2 RGB inference | [MaSoN trained on SSL4EO](https://huggingface.co/blaz-r/mason_ssl4eo-0shot) · [Demo](https://huggingface.co/spaces/blaz-r/MaSoN-CD-demo) |
| Paper benchmark evaluation | Dataset-specific checkpoints below |

F1 values below are percentages. Released checkpoints are individual runs; the paper reports averages across seeds.

| Dataset argument | Hugging Face checkpoint | Released checkpoint F1 | Paper mean F1 |
| --- | --- | ---: | ---: |
| `oscd96` | [mason_oscd96](https://huggingface.co/blaz-r/mason_oscd96) | 44.05 | 43.5 |
| `levir` | [mason_levir](https://huggingface.co/blaz-r/mason_levir) | 39.37 | 38.9 |
| `sysu` | [mason_sysu](https://huggingface.co/blaz-r/mason_sysu) | 62.14 | 60.6 |
| `clcd` | [mason_clcd](https://huggingface.co/blaz-r/mason_clcd) | 56.05 | 54.3 |
| `gvlm` | [mason_gvlm](https://huggingface.co/blaz-r/mason_gvlm) | 58.26 | 55.4 |

Set **both** `--data.dataset` and `--ckpt_path` when switching benchmarks. For example:

```bash
python train.py --config configs/mason.yaml \
  --data.dataset clcd \
  --eval_only --ckpt_path blaz-r/mason_clcd
```

Checkpoints are also available on [Google Drive](https://drive.google.com/drive/folders/1qAuiTWABBb2rVtalVrzXItrcMa9pPtPT?usp=sharing). To evaluate a downloaded checkpoint:

```bash
python train.py --config configs/mason.yaml \
  --data.dataset clcd \
  --eval_only --ckpt_path checkpoints/clcd.ckpt
```

## Train on your target domain

Train and then evaluate on one of the integrated datasets:

```bash
python train.py --config configs/mason.yaml --data.dataset oscd96
```

The default configuration trains for **1,000 steps**, keeps the encoder frozen, and saves checkpoints under `./checkpoints`. Synthetic masks supervise training; real change masks are used for evaluation.

See [configs/mason.yaml](configs/mason.yaml) for the encoder, decoder, noise settings and optimiser. Override configuration values from the command line:

```bash
python train.py --config configs/mason.yaml \
  --data.dataset clcd --data.batch_size 4 --seed 42
```

List available arguments with `python train.py -h`.

## Data

Integrated datasets (`oscd96`, `levir`, `sysu`, `clcd`, `gvlm`) are downloaded from Hugging Face and cached under `./datasets` by default.

### RGB input preparation

The default pipeline expects **RGB values in `[0, 255]`**. It resizes images to `256 × 256`, scales them to `[0, 1]`, and applies ImageNet normalisation with mean `(0.485, 0.456, 0.406)` and standard deviation `(0.229, 0.224, 0.225)`. Supply unnormalised images to this pipeline to avoid applying normalisation twice.

Image pairs should cover the same area and be spatially aligned. Binary label images use **0 for unchanged and 255 for changed**; the loader converts them to `[0, 1]`.

### Local datasets

Set `--data.use_hf false`, choose a dataset name, and point `--data.data_path` to its parent directory:

```bash
python train.py --config configs/mason.yaml \
  --data.use_hf false --data.dataset my_dataset --data.data_path ./datasets
```

The current dataset loader expects paired images and label files, including during training, although the training objective uses synthetic change masks.

<details>
<summary><strong>Directory and HDF5 formats</strong></summary>

Directory layout (matching PNG filenames in `A`, `B` and `label`):

```text
data_root/
  dataset_name/
    train/
      A/
      B/
      label/
    test/
      A/
      B/
      label/
    val/
      A/
      B/
      label/
```

By default, images are read from disk on demand. Set `--data.load_in_mem direct` to load the directory dataset into RAM.

For HDF5, set `--data.load_in_mem hdf5` and use:

```text
data_root/
  dataset_name/
    train.h5
    test.h5
    val.h5
```

Each split must contain `imageA`, `imageB`, `label`, and `img_idx`. Image arrays use `N × H × W × C`; label arrays use `N × H × W`. HDF5 splits are loaded into RAM.

</details>

## How it works

1. Extract features with a frozen encoder.
2. During training, add data-adaptive latent perturbations (Gaussian noise) to simulate relevant changes and irrelevant variations, with synthetic masks as supervision.
3. Train a decoder to detect changes from feature differences. At inference, compare the features of the actual image pair without adding perturbations.

<p align="center">
  <img src="assets/arch.svg" alt="MaSoN architecture: frozen encoder, latent change synthesis during training, feature subtraction, and mask decoder" width="100%">
</p>

See the [paper](https://arxiv.org/abs/2602.19881) and [project page](https://blaz-r.github.io/mason_ucd/) for the perturbation analysis, ablations, and qualitative results. Performance depends on the encoder's representations; transferring to a new domain or modality may require adaptation.

## Citation

If you found this work useful, consider citing our paper and giving this repo a ⭐ 😃
```bibtex
@article{rolih2026mason,
  title={Make Some Noise: Unsupervised Remote Sensing Change Detection Using Latent Space Perturbations},
  author={Rolih, Blaž and Fučka, Matic and Wolf, Filip and Čehovin Zajc, Luka},
  journal={IEEE Transactions on Geoscience and Remote Sensing},
  year={2026},
  doi={10.1109/TGRS.2026.3730181},
}
```

## Questions

For issues or questions, please open a GitHub [issue](https://github.com/blaz-r/mason_cd/issues) or email me.
