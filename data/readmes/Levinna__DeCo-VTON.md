# DeCo-VTON: Decouple, Don't Denoise

Official PyTorch implementation of **Rethinking Garment Conditioning in Diffusion-based Virtual Try-On: Decouple, Don't Denoise**, accepted at ECCV 2026.

<a href="https://arxiv.org/abs/2511.18775"><img src="https://img.shields.io/badge/arXiv-2511.18775-b31b1b.svg"></a>
<a href="https://huggingface.co/levinna/DeCo-VTON"><img src="https://img.shields.io/badge/🤗%20HuggingFace-Model-yellow"></a>
<a href="#citation"><img src="https://img.shields.io/badge/ECCV-2026-blueviolet.svg"></a>
<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg"></a>

This work was initially released as **Re-CatVTON**. The former Hugging Face URL redirects to `levinna/DeCo-VTON`.

## 📢 News

- **[2026.06]** Accepted to ECCV 2026.
- **[2025.12.22]** Inference code and pretrained [models](https://huggingface.co/levinna/DeCo-VTON) released.
- **[2025.11.24]** The paper is available on [arXiv](https://arxiv.org/abs/2511.18775).

## 🔍 Overview

![Method Overview](assets/overview.png)

DeCo-VTON is a single-UNet virtual try-on model that separates garment conditioning from the denoising target. It builds on the Stable Diffusion 1.5 inpainting architecture without requiring a separate garment UNet.

## 🛠️ Installation
```bash
conda create -n decovton python=3.12
conda activate decovton
git clone https://github.com/Levinna/DeCo-VTON.git
cd DeCo-VTON
pip install -r requirements.txt
pip install -e .
```
We trained and tested DeCo-VTON on Python 3.12, PyTorch 2.8.0 with CUDA 12.9.

The requirements file includes the dependencies used for inference and evaluation. DressCode mask preprocessing has two additional dependencies listed below. Training code is not included in this release.

An NVIDIA GPU is required for practical inference. `requirements.txt` installs the CUDA 12.9 build of PyTorch; install the matching PyTorch build first if your system uses a different CUDA version.

## 🚀 Inference
### Data Preparation
A prepared [VITON-HD](https://github.com/shadow2496/VITON-HD) or [DressCode](https://github.com/aimagelab/dress-code) dataset is required for inference. The expected inputs are:

```text
VITON-HD/
├── test_pairs.txt
├── test_pairs_unpaired.txt (optional; falls back to test_pairs.txt)
└── test/{image,cloth,agnostic-mask}/

DressCode/
├── upper_body/{test_pairs_paired.txt,test_pairs_unpaired.txt,images,agnostic_masks}/
├── lower_body/{test_pairs_paired.txt,test_pairs_unpaired.txt,images,agnostic_masks}/
└── dresses/{test_pairs_paired.txt,test_pairs_unpaired.txt,images,agnostic_masks}/
```

### Preprocess Mask
VITON-HD inference uses the agnostic masks distributed with the prepared dataset. For DressCode, install the optional DensePose dependencies and generate masks for the test splits. The preprocessing code is adapted from CatVTON.

```bash
pip install 'git+https://github.com/facebookresearch/detectron2.git'
pip install 'git+https://github.com/facebookresearch/detectron2.git#subdirectory=projects/DensePose'

CUDA_VISIBLE_DEVICES=0 python -m thirdparty.preprocess_agnostic_mask \
    --data_root_path /path/to/DressCode \
    --pair_files test_pairs_paired.txt test_pairs_unpaired.txt
```

### Run Inference

**Option 1: Load from Hugging Face Hub**
```bash
python inference.py \
    --hf_repo levinna/DeCo-VTON \
    --dataset_name vitonhd \
    --data_root_path /path/to/VITON-HD \
    --output_dir ./output \
    --resolution 512 \
    --batch_size 1 \
    --mixed_precision bf16
```
With `--hf_repo` and no `--hf_subfolder`, the checkpoint is selected from
`--dataset_name` and `--resolution`. Set `--resolution 1024` to use the
corresponding 1024 checkpoint.

**Option 2: Load from local path**
```bash
# First, download the model
hf download levinna/DeCo-VTON \
    --include "VITON-HD-512/*" \
    --local-dir ./checkpoints

# Then run inference
python inference.py \
    --base_model_path ./checkpoints/VITON-HD-512 \
    --dataset_name vitonhd \
    --data_root_path /path/to/VITON-HD \
    --output_dir ./output \
    --resolution 512 \
    --batch_size 1 \
    --mixed_precision bf16
```
For local 1024 inference, download with `--include "VITON-HD-1024/*"`, then use
`--base_model_path ./checkpoints/VITON-HD-1024` and `--resolution 1024`. The
resolution option does not change which local checkpoint is loaded. Use the
corresponding `DressCode-1024` paths and `--dataset_name dresscode` for DressCode.

If your GPU does not support bf16, use `--mixed_precision fp16` or
`--mixed_precision no` (FP32). For a custom size, pass `--height` and `--width`
instead of `--resolution`. When loading from Hugging Face at a custom size, also
pass `--hf_subfolder` explicitly because the checkpoint resolution cannot be
inferred.

**Option 3: Use the pipeline directly in Python**
```python
import torch
from decovton import DeCoVTONPipeline

pipe = DeCoVTONPipeline.from_vton_checkpoint(
    hf_repo="levinna/DeCo-VTON",
    subfolder="VITON-HD-512/unet",
    torch_dtype=torch.bfloat16,
).to("cuda")
```

### Available Checkpoints

| Dataset | HF Subfolder | Resolution | Availability |
|---------|--------------|------------|--------------|
| VITON-HD | `VITON-HD-512/unet` | 512×384 | Available |
| DressCode | `DressCode-512/unet` | 512×384 | Available |
| VITON-HD | `VITON-HD-1024/unet` | 1024×768 | Available |
| DressCode | `DressCode-1024/unet` | 1024×768 | Available |

The 1024 checkpoints were progressively fine-tuned from the corresponding 512
models for 32,000 steps on VITON-HD and 64,000 steps on DressCode.

### Inference Options

| Argument | Default | Description |
|----------|---------|--------------|
| `--resolution` | `512` | Resolution preset: `512` or `1024` |
| `--sampler` | `ddim` | Sampler type: `ddim`, `ddpm`, `unipc`, `dpmpp` |
| `--num_inference_steps` | `50` | Number of diffusion steps |
| `--guidance_scale` | `2.5` | CFG guidance scale |
| `--enable_vae_tiling` | `False` | Reduce VAE memory usage with tiling and slicing, useful at 1024 |
| `--repaint` / `--no-repaint` | `True` | Blend result with original background |
| `--eval_pair` / `--no-eval-pair` | `True` | Evaluate on paired split (`--eval-pair` is also accepted) |

**Recommended steps per sampler:**
- `ddim`: 50 steps (main results)
- `unipc`: 30 steps
- `dpmpp`: 25 steps

## 📊 Results

| Model | FID ↓ | KID ×1000 ↓ | LPIPS ↓ | Params (M) |
|:------|:-----:|:-----:|:-------:|:----------:|
| CatVTON | 5.425 | 0.411 | 0.057 | 859.5 |
| Leffa | 4.540 | 0.050 | 0.048 | 1802.7 |
| **DeCo-VTON (Ours)** | **4.438** | **0.010** | **0.047** | **859.5** |

> *VITON-HD paired results at 512×384, from Table 1 of the [paper](https://arxiv.org/html/2511.18775v2#S5.T1). Parameter counts are from Table 3.*

## Evaluation

`evaluation.py` reports PyTorch-FID, Clean-FID, and Clean-KID. Add `--paired`
to also report PSNR, SSIM, and LPIPS. Both ground-truth and prediction folders
may contain category subdirectories, as in the DressCode output layout.

```bash
CUDA_VISIBLE_DEVICES=0 python evaluation.py \
    --gt_folder /path/to/ground-truth-images \
    --pred_folder ./output/vitonhd-512/paired \
    --paired \
    --batch_size 16 \
    --num_workers 4
```

The ground-truth folder should contain only the person images for the evaluated
split. The shell wrapper accepts the same two folders as positional arguments:

```bash
bash evaluation.sh /path/to/ground-truth-images ./output/vitonhd-512/paired
```

## 📂 Project Structure
```
DeCo-VTON/
├── decovton/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── attn_processor.py
│   ├── presets.py
│   └── utils.py
├── thirdparty/
│   ├── __init__.py
│   ├── SCHP/
│   ├── DensePose/
│   ├── cloth_masker.py
│   ├── preprocess_agnostic_mask.py
│   └── preprocess_agnostic_mask.sh
├── model/                     # deprecated stubs -> decovton (kept for compatibility)
├── assets/
├── inference.py
├── inference.sh
├── inference_recatvton.py     # deprecated stub -> inference.py
├── inference_recatvton.sh
├── vton_datasets.py
├── evaluation.py
├── evaluation.sh
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## 📄 License

- **Code:** [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Model Weights:** [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

Third-party components retain their original licenses. See
[Third-party notices](THIRD_PARTY_NOTICES.md) for sources and license texts.

**Note:** The model weights are licensed under CC BY-NC 4.0 because VITON-HD and DressCode are restricted to non-commercial use.

## 🙏 Acknowledgements

This project is built upon [Diffusers](https://github.com/huggingface/diffusers) and uses [Stable Diffusion v1.5 Inpainting](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-inpainting) as the base model.

For fair comparison, our data pipeline for inference and evaluation protocol follow those of [CatVTON](https://github.com/Zheng-Chong/CatVTON) and [Leffa](https://github.com/franciszzj/Leffa).

## Citation

If you find our work helpful, please consider citing:

```bibtex
@article{na2025rethinking,
  title={Rethinking Garment Conditioning in Diffusion-based Virtual Try-On: Decouple, Don't Denoise},
  author={Na, Kihyun and Choi, Jinyoung and Kim, Injung},
  journal={arXiv preprint arXiv:2511.18775},
  year={2025}
}
```
