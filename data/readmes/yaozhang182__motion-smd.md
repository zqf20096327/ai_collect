# Encoder-Free Human Motion Understanding via Structured Motion Descriptions

Yao Zhang<sup>1</sup>, Zhuchenyang Liu<sup>1</sup>, Thomas Ploetz<sup>2</sup>, Yu Xiao<sup>1</sup>
<br><sup>1</sup>Aalto University &nbsp; <sup>2</sup>Georgia Institute of Technology

**[🌐 Project page](https://yaozhang182.github.io/motion-smd/)** &nbsp;·&nbsp;
**[📄 Paper (arXiv)](https://arxiv.org/abs/2604.21668)** &nbsp;·&nbsp;
**[🗂️ Data (HF)](https://huggingface.co/datasets/zyyy12138/motion-smd-data)** &nbsp;·&nbsp;
**[🤗 Models (HF)](https://huggingface.co/zyyy12138/motion-smd-lora)**

---

This repository contains the code for converting human motion sequences into Structured Motion Descriptions (SMD) and fine-tuning LLMs with LoRA for motion question answering and captioning.

## Overview

SMD is a deterministic, rule-based conversion from joint position sequences to structured natural language text. By representing motion as text, any LLM can process it directly without learned motion encoders or alignment modules. Only lightweight LoRA fine-tuning is needed.

```
Motion Sequence (T, 22, 3)
    → Joint Angle Computation (26 biomechanical angles)
    → Temporal Segmentation (peak-valley detection)
    → Global Trajectory Extraction
    → Structured Motion Description (text, ~1K-4K tokens)
    → Any LLM + LoRA → QA Answer / Caption
```

One worked example: [`examples/example_smd.txt`](./examples/example_smd.txt).

## Project Structure

```
motion_smd/
├── README.md
├── LICENSE
├── requirements.txt
├── examples/example_smd.txt               # One real SMD sample for quick inspection
│
├── scripts/
│   ├── utils/
│   │   ├── angle_calculator.py             # Joint angle computation (26 angles from joints)
│   │   ├── angle_text_v5.py                # SMD text generation (angles → structured text)
│   │   ├── angle_to_text.py                # Body-part / angle group metadata
│   │   ├── answer_extractor.py             # QA option matching / answer extraction
│   │   ├── test_peak_valley.py             # Temporal segmentation (peak-valley, cycle detection)
│   │   └── angle_text_loader.py            # Unified data loader (JSON / directory)
│   ├── finetune/
│   │   ├── train_lora_llm.py               # Training (QA + Caption, all backbones)
│   │   ├── inference_lora_llm.py           # Inference & evaluation
│   │   ├── caption_metrics.py              # Captioning metrics (BLEU/ROUGE/CIDEr/BS/R@k/MMD)
│   │   ├── compute_filtered_metrics.py     # Re-compute metrics from saved predictions
│   │   ├── dataset_text_only.py            # QA dataset (BABEL-QA + HuMMan-QA)
│   │   ├── train_encoder_based_twostage.py # MotionGPT3-Qwen encoder baseline
│   │   └── extract_attention_v2.py         # Attention visualization (heatmap PDF)
│   ├── slurm/                              # Slurm job scripts for every task in this README
│   ├── generate_topk_angle_texts.py        # Generate Top-K joint SMD variants
│   ├── generate_no_trajectory_angle_texts.py # Generate no-trajectory SMD variant
│   └── generate_n_option_qa.py             # Standardize QA to fixed N options
│
├── captioning/
│   ├── scripts/
│   │   └── dataset_caption.py              # Caption dataset (HumanML3D)
│   ├── data/humanml3d/                     # HumanML3D subset (see Setup)
│   └── baselines/MotionGPT3/               # T2M evaluator + MotionGPT3 VAE (see Setup)
│
├── data/
│   ├── babel_qa/                           # BABEL-QA joints + questions + 10-option QA + SMDs
│   └── humman_qa/                          # HuMMan-QA joints + questions + 10-option QA + SMDs
│
├── models/                                 # LLM backbones (download separately)
├── checkpoints/                            # Trained LoRA adapters (created during training)
└── docs/                                   # Source for the GitHub Pages project site
```

## Setup

### 1. Environment

```bash
conda create -n smd python=3.10 -y
conda activate smd
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

For GLM-4-9B, additionally install:
```bash
pip install tiktoken
```

### 2. Pre-computed artifacts (recommended)

The easiest way to reproduce paper numbers is to download our pre-packaged data and adapters from HuggingFace. This lets you skip SMD generation (Step 1 below) and training (Step 3) if you only want to evaluate.

```bash
pip install huggingface_hub

# Data: SMD JSONs + preprocessed BABEL-QA / HuMMan-QA / HumanML3D subset (~5 GB total)
huggingface-cli download zyyy12138/motion-smd-data --repo-type dataset --local-dir _hf_data

# Models: all 8 LoRA adapters reported in the paper (~0.5 GB)
huggingface-cli download zyyy12138/motion-smd-lora --local-dir checkpoints
```

Then move / symlink the data into the layout the code expects:

```bash
# SMDs and motion data
ln -s $(pwd)/_hf_data/babel_qa/joints             data/babel_qa/joints
ln -s $(pwd)/_hf_data/babel_qa/questions          data/babel_qa/questions
ln -s $(pwd)/_hf_data/babel_qa/questions_10opt    data/babel_qa/questions_10opt
ln -s $(pwd)/_hf_data/humman_qa/joints            data/humman_qa/joints
ln -s $(pwd)/_hf_data/humman_qa/questions         data/humman_qa/questions
ln -s $(pwd)/_hf_data/humman_qa/questions_10opt   data/humman_qa/questions_10opt
ln -s $(pwd)/_hf_data/humanml3d                    captioning/data/humanml3d

# Pre-generated SMDs (17 variants per dataset)
ln -s $(pwd)/_hf_data/smd_texts/babel_qa/*        data/babel_qa/
ln -s $(pwd)/_hf_data/smd_texts/humman_qa/*       data/humman_qa/
ln -s $(pwd)/_hf_data/smd_texts/humanml3d/*       captioning/data/humanml3d/
```

### 3. Upstream data sources (alternative to HF download)

If you prefer to reconstruct the data from scratch:

- **BABEL-QA** and **HuMMan-QA**: Download from [IMoRe](https://github.com/LUNAProject22/IMoRe). Place motion joints (`.npy`) in `data/<dataset>/joints/` and QA files in `data/<dataset>/questions/`. Then run Step 1 and Step 2 below to regenerate SMDs and 10-option QA.
- **HumanML3D**: Download from [HumanML3D](https://github.com/EricGuo5513/HumanML3D). Place under `captioning/data/humanml3d/` (needs `new_joints/`, `texts/`, `Mean.npy`, `Std.npy`, `train.txt`, `val.txt`, `test.txt`).

**T2M Evaluator** (required for captioning R-Precision and MM-Distance):
- Download from [MotionGPT3](https://github.com/OpenMotionLab/MotionGPT3) following their instructions (`bash prepare/download_t2m_evaluators.sh`). Place under `captioning/baselines/MotionGPT3/deps/t2m/`.

**MotionGPT3 VAE** (required only for the encoder-based baseline experiment):
- Download the MotionGPT3 checkpoint from [MotionGPT3](https://github.com/OpenMotionLab/MotionGPT3). Place at `captioning/baselines/MotionGPT3/checkpoints/motiongpt3.ckpt`.

### 4. LLM Models

Download the desired LLM backbone(s) and place under `models/`:

```bash
# Default backbone
huggingface-cli download Qwen/Qwen2.5-7B-Instruct --local-dir models/qwen2.5-7b-instruct

# Additional backbones for portability experiments
huggingface-cli download Qwen/Qwen2.5-3B-Instruct   --local-dir models/qwen2.5-3b-instruct
huggingface-cli download google/gemma-3-4b-it       --local-dir models/gemma3-4b-it
huggingface-cli download Qwen/Qwen3-8B              --local-dir models/qwen3-8b
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct --local-dir models/llama-3.1-8b-instruct
huggingface-cli download THUDM/glm-4-9b-chat        --local-dir models/glm-4-9b-chat
```

## Usage

### Step 1: Generate SMD from Motion Data

Convert raw joint positions to Structured Motion Descriptions. The output is a JSON file mapping motion IDs to SMD text strings.

```bash
# Generate All-26 joint SMD (default, ~4K tokens per motion).
# Called internally by the training/eval scripts.

# Generate Top-K joint variants (shorter, ~1K tokens for Top-3)
python scripts/generate_topk_angle_texts.py --top_k 3 --dataset babel_qa
python scripts/generate_topk_angle_texts.py --top_k 3 --dataset humman_qa
python scripts/generate_topk_angle_texts.py --top_k 3 --dataset humanml3d

# Generate no-trajectory variant
python scripts/generate_no_trajectory_angle_texts.py --dataset babel_qa
```

### Step 2: Standardize QA Options

Standardize QA benchmarks to a fixed 10-option format for fair cross-method comparison:

```bash
python scripts/generate_n_option_qa.py --dataset babel_qa --max_options 10
python scripts/generate_n_option_qa.py --dataset humman_qa --max_options 10
```

### Step 3: Train with LoRA

**Motion QA** (trains jointly on BABEL-QA + HuMMan-QA):
```bash
python scripts/finetune/train_lora_llm.py \
    --task qa \
    --model_path models/qwen2.5-7b-instruct \
    --angle_texts_dir angle_texts_v5 \
    --save_dir checkpoints/lora_qwen2.5-7b_qa_v5 \
    --epochs 5 --batch_size 2 --grad_accum 4 --lr 1e-4
```

**Motion Captioning** (trains on HumanML3D):
```bash
python scripts/finetune/train_lora_llm.py \
    --task caption \
    --model_path models/qwen2.5-7b-instruct \
    --angle_texts_dir angle_texts_v5 \
    --save_dir checkpoints/lora_qwen2.5-7b_caption_v5 \
    --epochs 5 --batch_size 1 --grad_accum 8 --lr 1e-4
```

Training takes approximately 7 GPU-hours for QA and 20 GPU-hours for captioning on a single H200 GPU.

### Step 4: Evaluate

**QA Evaluation** (reports accuracy on test set):
```bash
python scripts/finetune/inference_lora_llm.py \
    --task qa --dataset babel_qa \
    --model_path models/qwen2.5-7b-instruct \
    --lora_path checkpoints/lora_qwen2.5-7b_qa_v5/best \
    --angle_texts_dir angle_texts_v5 \
    --output_dir outputs/babel_qa/qa_v5 \
    --split test

python scripts/finetune/inference_lora_llm.py \
    --task qa --dataset humman_qa \
    --model_path models/qwen2.5-7b-instruct \
    --lora_path checkpoints/lora_qwen2.5-7b_qa_v5/best \
    --angle_texts_dir angle_texts_v5 \
    --output_dir outputs/humman_qa/qa_v5 \
    --split test
```

**Caption Evaluation** (generates captions + computes all metrics):
```bash
python scripts/finetune/inference_lora_llm.py \
    --task caption \
    --model_path models/qwen2.5-7b-instruct \
    --lora_path checkpoints/lora_qwen2.5-7b_caption_v5/best \
    --data_dir captioning/data/humanml3d \
    --angle_texts_dir angle_texts_v5 \
    --output_dir captioning/outputs/caption_v5 \
    --split test
```

Captioning metrics include BLEU@1/4, ROUGE-L, CIDEr, BERTScore (text quality), and R-Precision R@1/2/3 and MM-Distance (text-motion alignment via T2M evaluator).

### Step 5: Backbone Portability

To train with a different LLM backbone, change `--model_path`. No other changes are needed:

```bash
python scripts/finetune/train_lora_llm.py \
    --task qa \
    --model_path models/gemma3-4b-it \
    --angle_texts_dir angle_texts_v5_top3 \
    --save_dir checkpoints/lora_gemma3-4b_qa_top3 \
    --epochs 5 --batch_size 2 --grad_accum 4 --lr 1e-4
```

The same SMD input, data pipeline, and training code work across all tested backbones (Qwen2.5, Qwen3, Gemma3, LLaMA-3.1, GLM-4).

### Step 6: Attention Analysis (Interpretability)

Generate attention heatmaps showing which SMD sections the model attends to:

```bash
python scripts/finetune/extract_attention_v2.py \
    --task caption --num_samples 10 \
    --model_path models/qwen2.5-7b-instruct \
    --output_dir attention_analysis
```

This produces per-character attention heatmap PDFs. Note: requires `attn_implementation="eager"` (set automatically), which uses more memory than flash attention. Using the Top-3 SMD variant (~1K tokens) is recommended to avoid OOM.

## Encoder-based Baseline (MotionGPT3-Qwen)

To replicate the MotionGPT3 encoder paradigm on Qwen2.5-7B for controlled comparison:

```bash
python scripts/finetune/train_encoder_based_twostage.py \
    --task caption --n_tokens 4 \
    --stage1_epochs 5 --stage2_epochs 5 \
    --batch_size 4 \
    --save_dir checkpoints/encoder_twostage_caption_4tok
```

This follows the two-stage LLaVA-style training protocol:
- Stage 1: Freeze LLM, train only the projection MLP (alignment)
- Stage 2: Add LoRA to LLM, train MLP + LoRA jointly

Requires the MotionGPT3 VAE checkpoint at `captioning/baselines/MotionGPT3/checkpoints/motiongpt3.ckpt` and the HumanML3D normalization statistics at `captioning/data/humanml3d/{Mean,Std}.npy`.

## Reproducing Paper Results

The pre-generated SMD files (`angle_texts_v5*.json`) are shipped via the
[HuggingFace dataset repo](https://huggingface.co/datasets/zyyy12138/motion-smd-data), so Step 1 can be skipped to directly reproduce the training and evaluation.

| Experiment | SMD variant | Train command |
|-----------|------------|---------------|
| Main table (QA) | `angle_texts_v5` | `--task qa --angle_texts_dir angle_texts_v5` |
| Main table (Caption) | `angle_texts_v5` | `--task caption --angle_texts_dir angle_texts_v5` |
| Joint count ablation | `angle_texts_v5_top{3,5,10,20}` | `--angle_texts_dir angle_texts_v5_top3` etc. |
| Trajectory ablation | `angle_texts_v4`, `angle_texts_v5_notraj` | Change `--angle_texts_dir` |
| Segmentation threshold | `angle_texts_v5_delta{3,5,10,15}` | Change `--angle_texts_dir` |
| Backbone portability | `angle_texts_v5_top3` | Change `--model_path` |
| Zero-shot | `angle_texts_v5_top3` | Run inference without LoRA |

Headline numbers:

| Benchmark | Metric | SMD + Qwen2.5-7B |
|---|---|---|
| BABEL-QA (test) | Accuracy | **66.7%** |
| HuMMan-QA (test) | Accuracy | **90.1%** |
| HumanML3D (test) | R@1 | **0.584** |
| HumanML3D (test) | CIDEr | **53.16** |

See the [paper](https://arxiv.org/abs/2604.21668) for complete tables and ablations.

## License

Code in this repository is released under the [MIT License](./LICENSE).

LoRA adapter weights and pre-computed SMD JSONs on HuggingFace follow the
licensing described in their respective repository READMEs. Upstream data
(BABEL, HuMMan, HumanML3D, AMASS) retains its original license; please
consult each upstream source before commercial or redistributive use.

## Citation

```bibtex
@article{zhang2026smd,
  title   = {Encoder-Free Human Motion Understanding via Structured Motion Descriptions},
  author  = {Zhang, Yao and Liu, Zhuchenyang and Ploetz, Thomas and Xiao, Yu},
  journal = {arXiv preprint arXiv:2604.21668},
  year    = {2026}
}
```

## Contact

Yao Zhang — `yao.1.zhang@aalto.fi`
