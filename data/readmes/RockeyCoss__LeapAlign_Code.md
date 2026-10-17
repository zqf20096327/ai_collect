## LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories<br><sub>Official PyTorch Implementation</sub>

![method](assets/images/method.webp)

> [**LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories**](https://arxiv.org/abs/2604.15311)<br>
> [Zhanhao Liang](https://github.com/RockeyCoss)<sup>1,2,&#42;</sup>, [Tao Yang](https://github.com/ThomasMrY)<sup>2,&#42;,&dagger;</sup>, [Jie Wu](https://wujie1010.github.io/)<sup>2</sup>, [Chengjian Feng](https://fcjian.github.io/)<sup>2</sup>, [Liang Zheng](https://zheng-lab-anu.github.io/)<sup>1</sup><br>
> <sup>1</sup>ANU, <sup>2</sup>ByteDance Seed<br>
> <sup>&#42;</sup>Equal contribution, <sup>&dagger;</sup>Project Lead<br>

<p align="center">
  <a href="https://arxiv.org/abs/2604.15311"><img src="https://img.shields.io/badge/Paper-arXiv-red?style=for-the-badge" alt="Paper" height="24"></a>
  &emsp;&emsp;&emsp;
  <a href="https://rockeycoss.github.io/leapalign/"><img src="https://img.shields.io/badge/Project-Page-blue?style=for-the-badge" alt="Project Page" height="24"></a>
  &emsp;&emsp;&emsp;
  <a href="https://huggingface.co/rockeycoss/LeapAlign"><img src="https://img.shields.io/badge/Hugging-Face-yellow?style=for-the-badge" alt="Hugging Face" height="24"></a>
</p>

## Overview
LeapAlign is a post-training method for aligning flow matching models with human preferences by backpropagating reward gradients through the differentiable generation process. Since backpropagation through the full sampling trajectory is memory-intensive and prone to gradient explosion, early generation steps that determine the global structure and layout of the final image are difficult to optimize. LeapAlign addresses this by constructing a two-step **leap trajectory** and backpropagating gradients through it instead of the full sampling trajectory, enabling gradient propagation to **any** generation step.

## Dependency Setup
### 1. Create the Conda environment
```bash
conda create --name leapalign python=3.11 -y
conda activate leapalign
```

### 2. Install project dependencies
```bash
./setup_env.sh
```

This script installs the Python dependencies for LeapAlign, installs `python3-tk`, and clones and installs `HPSv2`.

### 3. Download checkpoints
```bash
mkdir -p data
huggingface-cli download black-forest-labs/FLUX.1-dev --local-dir ./data/flux

mkdir -p hps_ckpt
huggingface-cli download xswu/HPSv2 HPS_v2.1_compressed.pt --local-dir ./hps_ckpt
huggingface-cli download laion/CLIP-ViT-H-14-laion2B-s32B-b79K open_clip_pytorch_model.bin --local-dir ./hps_ckpt
```

### 4. Prepare prompt embeddings
The preprocessing scripts use 8 GPUs by default.

Prepare HPDv2 prompt embeddings:
```bash
bash scripts/preprocess/preprocess_flux_hpdv2_rl_embeddings.sh
```

Prepare GenEval prompt embeddings:
```bash
bash scripts/preprocess/preprocess_flux_geneval_rl_embeddings.sh
```

## Fine-tune with LeapAlign
The provided training scripts are configured for a 2x8 setup by default, i.e., 2 nodes with 8 GPUs each.

### HPDv2
Launch on node 0:
```bash
MASTER_ADDR=<node0_host> MASTER_PORT=29500 NNODES=2 NODE_RANK=0 NPROC_PER_NODE=8 \
bash scripts/finetune/train_flux_leapalign_hpdv2_hpsv2.sh
```

Launch on node 1:
```bash
MASTER_ADDR=<node0_host> MASTER_PORT=29500 NNODES=2 NODE_RANK=1 NPROC_PER_NODE=8 \
bash scripts/finetune/train_flux_leapalign_hpdv2_hpsv2.sh
```

### GenEval
Launch on node 0:
```bash
MASTER_ADDR=<node0_host> MASTER_PORT=29500 NNODES=2 NODE_RANK=0 NPROC_PER_NODE=8 \
bash scripts/finetune/train_flux_leapalign_geneval_hpsv2.sh
```

Launch on node 1:
```bash
MASTER_ADDR=<node0_host> MASTER_PORT=29500 NNODES=2 NODE_RANK=1 NPROC_PER_NODE=8 \
bash scripts/finetune/train_flux_leapalign_geneval_hpsv2.sh
```

## Evaluation

### HPDv2
#### 1. Sample images
The example below uses 8 GPUs.

```bash
torchrun --nproc_per_node=8 fastvideo/evaluation/sample_flux_images.py \
    --model_path <path_to_finetuned_transformer> \
    --output_dir ./output/flux_leapalign_hpsv2
```

`--model_path` should point to a checkpoint directory saved during fine-tuning.

#### 2. Compute average HPSv2.1 reward
```bash
python fastvideo/evaluation/evaluate_reward_values.py \
    --results_dir ./output/flux_leapalign_hpsv2 \
    --output_dir ./output/rewards_log
```

The script prints the average HPSv2.1 score and writes `<results_dir_basename>_rewards_log.json` to `--output_dir`.

### GenEval
#### 1. Sample images
The example below uses 8 GPUs.

```bash
torchrun --nproc_per_node=8 fastvideo/evaluation/sample_flux_images_geneval.py \
    --model_path <path_to_finetuned_transformer> \
    --outdir ./output/flux_leapalign_geneval
```

#### 2. Score with the GenEval evaluator
Follow the setup and scoring instructions in the [official GenEval repo](https://github.com/djghosh13/geneval) and run their evaluator against the directory produced in step 1.

## Inference with Released Checkpoints

We release **FLUX checkpoints fine-tuned with LeapAlign** on the [Hugging Face Hub](https://huggingface.co/rockeycoss/LeapAlign). All checkpoints are trained by applying **LeapAlign** on top of **FLUX.1-dev**.

- `flux_geneval_hpsv2`: FLUX + LeapAlign + **GenEval** prompt set + **HPSv2.1** reward
- `flux_hpdv2_hpsv2`: FLUX + LeapAlign + **HPDv2** prompt set + **HPSv2.1** reward
- `flux_mjhq30k_hpsv3`: FLUX + LeapAlign + **MJHQ-30k** prompt set + **HPSv3** reward

### 1. Download checkpoints

```bash
# Download into the current directory (creates local folders)
huggingface-cli download rockeycoss/LeapAlign --local-dir . --include "flux_geneval_hpsv2/*"
huggingface-cli download rockeycoss/LeapAlign --local-dir . --include "flux_hpdv2_hpsv2/*"
huggingface-cli download rockeycoss/LeapAlign --local-dir . --include "flux_mjhq30k_hpsv3/*"
```

### 2. Run inference

```python
import torch

from diffusers import FluxPipeline, FluxTransformer2DModel

base_id = "black-forest-labs/FLUX.1-dev"
ckpt_dir = "flux_geneval_hpsv2"  # or "flux_hpdv2_hpsv2" / "flux_mjhq30k_hpsv3"

pipe = FluxPipeline.from_pretrained(
    base_id,
    torch_dtype=torch.bfloat16,
    use_safetensors=True,
)

# Load LeapAlign-aligned transformer weights from local folder
pipe.transformer = FluxTransformer2DModel.from_pretrained(
    ckpt_dir,
    torch_dtype=torch.bfloat16,
)

pipe.to("cuda")

image = pipe(
    "a very cute cat",
    guidance_scale=3.5,
    height=720,
    width=720,
    num_inference_steps=50,
    max_sequence_length=512,
).images[0]

image.save("out.png")
```

## Acknowledgments
LeapAlign builds upon several excellent open-source projects. We would like to thank the authors and contributors of:
- [DanceGRPO](https://github.com/XueZeyue/DanceGRPO/tree/main)
- [FastVideo](https://github.com/hao-ai-lab/fastvideo)
- [Diffusers](https://github.com/huggingface/diffusers)
- [MixGRPO](https://github.com/Tencent-Hunyuan/MixGRPO)
- [GenEval](https://github.com/djghosh13/geneval)
- [HPSv2](https://github.com/tgxs002/HPSv2/tree/master)

## :mailbox_with_mail: Citation
If you find this code useful in your research, please consider citing:

```
@article{liang2026leapalign,
  title={LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories},
  author={Liang, Zhanhao and Yang, Tao and Wu, Jie and Feng, Chengjian and Zheng, Liang},
  journal={arXiv preprint arXiv:2604.15311},
  year={2026}
}
```
