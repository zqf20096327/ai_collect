# Emergence and Evolution of Interpretable Concepts in Diffusion Models (NeurIPS 2025 Spotlight 🌟)
This is the official repository for the paper [Emergence and Evolution of Interpretable Concepts in Diffusion Models](https://arxiv.org/abs/2504.15473).

> [**Emergence and Evolution of Interpretable Concepts in Diffusion Models**](https://arxiv.org/abs/2504.15473),  
> Berk Tinaz<sup>\*</sup>, Zalan Fabian<sup>\*</sup>, Mahdi Soltanolkotabi  
> *NeurIPS 2025*  
> <sup>\*</sup> equal contribution

In this work, we leverage the SAE framework to probe the inner workings of Stable Diffusion v1.4, and uncover a variety of human-interpretable concepts in its activations. Interestingly, we find that even before the first reverse diffusion step is completed, the final composition of the scene can be predicted surprisingly well by looking at the spatial distribution of activated concepts.

![](assets/predict_layout.png)

Going beyond correlational analysis, we design intervention techniques aimed at manipulating image composition and style, and demonstrate that: 
(1) in early stages of diffusion image composition can be effectively controlled, 
(2) in the middle stages image composition is finalized, however stylistic interventions are effective, and
(3) in the final stages only minor textural details are subject to change.

## Installation
Follow these steps to install dependencies and download pretrained models for StableConcepts.

### 1. Clone repo and submodules
```bash
git clone https://github.com/berktinaz/stable-concepts
cd stable-concepts
```

### 2. Install packages
First, create a new conda environment.
```bash
conda create -n stable_concepts python=3.10 -y
conda activate stable_concepts
pip install --upgrade pip
```
Install torch (we tested our code with CUDA 12.4):
```bash
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/test/cu124
```
Install [Grounded-Segment-Anything](https://github.com/IDEA-Research/Grounded-Segment-Anything).
```bash
git clone https://github.com/IDEA-Research/Grounded-Segment-Anything
cd Grounded-Segment-Anything
```
and follow the installation steps under ["Install without Docker"](https://github.com/IDEA-Research/Grounded-Segment-Anything#install-without-docker). Finally, move back to the "stable-concepts" folder and install the remaining dependencies.
```bash
pip install -r requirements.txt
```

### 3. Download model checkpoints and concept dictionaries
Install model checkpoints and concept dictionaries from this link: [Download](https://drive.google.com/file/d/1H29s5Xq101R2BqrP0udWVPSKCPnU-Fqe) and unnzip it. 
```bash
unzip concept-dict_sae-ckpts.zip
```
Download Grounded-Segment-Anything related checkpoints:
```bash
mkdir GSA-ckpts
cd GSA-ckpts
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
wget https://huggingface.co/spaces/xinyu1205/Tag2Text/resolve/main/ram_swin_large_14m.pth
wget https://huggingface.co/spaces/xinyu1205/Tag2Text/resolve/main/tag2text_swin_14m.pth
```
Download Word2Vec checkpoints from this kaggle [website](https://www.kaggle.com/datasets/leadbest/googlenewsvectorsnegative300/data). Ensure you have "GoogleNews-vectors-negative300.bin" file under "word2vec-ckpt" folder.

Ensure you have "concept-dicts", "GSA-ckpts", "SD1.4-SAE-ckpts", and "word2vec-ckpt" under "stable-concepts" folder.

## Scripts (and how to use them)

Below is a quick overview of the scripts under `stable-concepts/scripts`, what each one does, and how to run them.

- `scripts/collect_latents_dataset.py` — Collect Stable Diffusion v1.4 UNet activations and generated images into WebDataset `.tar` files for later SAE training and analysis.
  - Saves per-block tar files containing activation deltas (`diff.pth`) and generation args (`gen_args.json`), plus `images.tar` with `images.npy`.
  - Key args: `--save_path`, `--start_at`, `--finish_at`, `--dataset_batch_size`, `--blocks_to_save` (comma-separated), `--timesteps_to_save` (comma-separated), `--features_to_save` (`both|cond|uncond`).
  - Example (split across GPUs):
    ```bash
    CUDA_VISIBLE_DEVICES=0 python scripts/collect_latents_dataset.py \
      --save_path ./SD1.4 \
      --start_at 0 --finish_at 25000 \
      --dataset_batch_size 1 \
      --blocks_to_save unet.down_blocks.2.attentions.1,unet.mid_block.attentions.0,unet.up_blocks.1.attentions.0 \
      --timesteps_to_save 0,500,1000 \
      --features_to_save both
    ```

- `scripts/train_sae.py` — Train Sparse Autoencoder(s) on the collected activations.
  - Configuration-driven via `SAE/config.json` (paths to latents, block name, batch size, timestep, SAE hyperparameters, logging, save intervals).
  - Saves intermediate and `final` checkpoints to the `save_path` specified in the config and logs to Weights & Biases.
  - Example:
    ```bash
    python scripts/train_sae.py
    ```

- `scripts/extract_concepts.py` — Discover concept IDs (SAE features) associated with objects found by Grounded-Segment-Anything; scores concepts per object with IoU over upsampled SAE heatmaps.
  - Requires: GSA checkpoints (`GSA-ckpts/*`), trained SAE checkpoints (`SD1.4-SAE-ckpts/*`).
  - Key args: `--save_path`, `--start_at`, `--finish_at`, `--blocks` (one block), `--timestep {0,500,1000}`, `--features_type {cond,uncond}`, `--heatmap_iou_threshold`, `--num_filter_top_cids`, `--num_save_top_cids`, `--save_figs`, `--skip_existing`, plus GSA configs/thresholds.
  - Example:
    ```bash
    CUDA_VISIBLE_DEVICES=0 python extract_concepts.py \
      --save_path outputs/down/t_0 \
      --start_at 1500000 --finish_at 1540000 \
      --blocks unet.down_blocks.2.attentions.1 \
      --timestep 0 --features_type cond \
      --heatmap_iou_threshold 0.1 \
      --save_figs False --skip_existing True
    ```

- `scripts/extract_words_for_concepts.py` — Aggregate words per concept from the per-sample `results.json` files; outputs filtered concept lists and word-count summaries.
  - Scans `--concepts_path` recursively for `results.json` and produces JSONs under `--save_path`:
    - `concepts_filtered_iou_<min_iou>.json`
    - `concepts_filtered_iou_<min_iou>_wc.json`
  - Key args: `--save_path`, `--concepts_path`, `--num_concepts` (default 5120), `--min_iou` (default 0.5; keeps entries with IoU ≤ min_iou as “matches”).
  - Examples:
    ```bash
    python scripts/extract_words_for_concepts.py --save_path outputs/down/t_0_concepts --concepts_path outputs/down/t_0
    ```

- `scripts/evaluate_seg.py` — Evaluate concept-driven semantic segmentation using word2vec embeddings to map discovered concepts to class labels.
  - Requires: GSA checkpoints, SAE checkpoints, and a word2vec binary (e.g., `GoogleNews-vectors-negative300.bin`).
  - Supports targets from the automatic tagger (`--target_source tagger`) or noun phrases from the prompt (`--target_source prompt`).
  - Produces per-sample `results.json`, optional visualizations (`prediction.png`, `seg_mask_remapped.jpg`), and `aggregated_results.json` summarizing metrics across thresholds.
  - Key args: `--save_path`, `--start_at`, `--finish_at`, `--blocks` (one block), `--timestep`, `--features_type`, `--concepts_path` (from the previous step), `--w2v_ckpt`, `--num_top_concepts`, `--num_thresholds`, `--skip_existing`, `--save_figs`, plus GSA configs/thresholds.
  - Example:
    ```bash
    CUDA_VISIBLE_DEVICES=0 python evaluate_seg.py \
      --save_path ../outputs/eval/down/t_0_tagger \
      --start_at 2000000 --finish_at 2005000 \
      --blocks unet.down_blocks.2.attentions.1 \
      --timestep 0 --features_type cond \
      --concepts_path ../concept-dicts/down/t_0_concepts_filtered_iou_0.5.json \
      --num_top_concepts 10 \
      --skip_existing False --save_figs True \
      --target_source tagger
    ```

Notes
- Make sure the following folders exist at the repo root as described above: `SD1.4-SAE-ckpts/`, `GSA-ckpts/`, and `word2vec/` (containing `GoogleNews-vectors-negative300.bin`).
- Block names follow diffusers’ UNet modules, e.g., `unet.down_blocks.2.attentions.1`.
- Timesteps typically use `{0, 500, 1000}` to represent early/mid/late diffusion steps.

## Notebooks (and how to use them)

The `notebooks/` folder contains interactive Jupyter notebooks demonstrating SAE feature visualization, concept-based interventions, and semantic segmentation prediction.

- **`visualize_features_single_image.ipynb`** — Visualize SAE concept activations for a single generated image. Load SAEs for specified UNet blocks and timesteps, generate an image from a custom prompt, extract and visualize the top-activating concept heatmaps overlaid on the generated image.

- **`predict_segmentation.ipynb`** — Predict semantic segmentation maps from SAE concept activations using word2vec embeddings. Configure block/timestep, load concept dictionary and word2vec model, generate images, extract spatial concept activations, and map them to semantic labels for segmentation visualization.

- **`global_edits_{early,mid,late}_stage.ipynb`** — Perform global concept interventions at (early,mid,late) diffusion stages. Demonstrates how amplifying or suppressing SAE concepts globally across the spatial feature map can steer image composition during reverse diffusion. 

- **`spatial_intervention_{early,mid,late}_stage.ipynb`** — Apply spatially localized concept interventions at (early,mid,late) diffusion stages. Control where objects appear in the final image by amplifying specific concept activations in targeted spatial regions (e.g., top-left, bottom-right).

## Citation

If you find our paper useful, please cite

```bibtex
@inproceedings{tinazstableconcepts,
  title={Emergence and Evolution of Interpretable Concepts in Diffusion Models},
  author={Tinaz, Berk and Fabian, Zalan and Soltanolkotabi, Mahdi},
  booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems}
}
```

## Acknowledgements and references
Model latent collection and SAE training components are based on [`surkovv/sdxl-unbox`](https://github.com/surkovv/sdxl-unbox) repository.

Our concept discovery pipeline uses RAM-Grounded-SAM pipeline from [`IDEA-Research/Grounded-Segment-Anything`](https://github.com/IDEA-Research/Grounded-Segment-Anything)
