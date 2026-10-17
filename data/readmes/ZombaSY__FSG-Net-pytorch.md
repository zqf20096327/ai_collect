# 🩺 FSG-Net: Full-scale Representation Guided Network for Retinal Vessel Segmentation

<div align="center">

**Official PyTorch Implementation**

[![Paper](https://img.shields.io/badge/arXiv-2501.18921-red?style=flat-square)](https://arxiv.org/abs/2501.18921)
[![GitHub](https://img.shields.io/badge/GitHub-Releases-blue?style=flat-square)](https://github.com/ZombaSY/FSG-Net-pytorch/releases/tag/1.1.0)

![Qualitative Results](images/Qualitative_evaluation.png)

</div>

---

## 📋 Table of Contents
- [Environment Setup](#-environment-setup)
- [Performance Results](#-performance-results)
- [Pretrained Models](#-pretrained-models)
- [Dataset Preparation](#-dataset-preparation)
- [Training](#-training)
- [Inference](#-inference)
- [Citation](#-citation)

---

## 🖥️ Environment Setup

| Component | Version |
|-----------|---------|
| **OS** | Ubuntu 22.04 LTS |
| **GPU** | RTX 4090 (24GB) |
| **GPU Driver** | 550.54.14 |
| **CUDA** | 12.4 |
| **PyTorch** | 2.4.1 |

---

## 🎯 Performance Results

Comprehensive evaluation across multiple retinal vessel segmentation datasets:

| Dataset | mIoU | F1 Score | Accuracy | AUC | Sensitivity | MCC |
|---------|------|----------|----------|-----|-------------|-----|
| **DRIVE** | 84.068 | 83.229 | 97.042 | 98.235 | 84.207 | 81.731 |
| **STARE** | 86.118 | 85.100 | 97.746 | 98.967 | 86.608 | 83.958 |
| **CHASE_DB1** | 82.680 | 81.019 | 97.515 | 99.378 | 85.995 | 79.889 |
| **HRF** | 83.088 | 81.567 | 97.106 | 98.744 | 83.616 | 80.121 |

---

## 📦 Pretrained Models

Pre-trained models for each dataset are available in the [releases](https://github.com/ZombaSY/FSG-Net-pytorch/releases/tag/1.1.0) page.

**Download and extract** the models corresponding to your target dataset before inference.

---

## 📊 Dataset Preparation

### Configuration
Edit the dataset paths in [`configs/train.yml`](configs/train.yml):
- Update `train_x_path` with your input data directory
- Update corresponding label paths

### Important Requirements
- ✋ Input and label files **must be sorted by name**
- ✋ Ensure one-to-one correspondence between inputs and labels

### Download Datasets
Datasets can be obtained from:
- Public repositories
- [GitHub Releases](https://github.com/ZombaSY/FSG-Net-pytorch/releases/tag/1.1.0)

---

## 🚀 Training

### Step 1: Configure Training
Edit [`configs/train.yml`](configs/train.yml) with your:
- Dataset paths
- Hyperparameters
- Training settings

### Step 2: Setup Monitoring (Optional)
**With WandB:**
```bash
wandb login  # Login with your credentials
```

**Without WandB:**
Set `wandb: false` in [`configs/train.yml`](configs/train.yml)

### Step 3: Start Training
```bash
bash bash_train.sh
```

---

## 🔍 Inference

### Step 1: Configure Inference
Edit [`configs/inference.yml`](configs/inference.yml):
- Set `model_path` to your pretrained model location
- Specify input image directory
- Configure output paths

### Step 2: Run Inference
```bash
bash bash_inference.sh
```

### Expected Results
When using official pretrained models, results should closely match the performance metrics above.

---

## 📖 Citation

If you find this work helpful, please cite:

```bibtex
@article{seo2025fullscalerepresentationguidednetwork,
  title   = {Full-scale Representation Guided Network for Retinal Vessel Segmentation},
  author  = {Sunyong Seo, Sangwook Yoo, Huisu Yoon},
  journal = {arXiv preprint arXiv:2501.18921},
  year    = {2025}
}
```

---

<div align="center">

**⭐ If you find this repository useful, please consider giving it a star!**

</div>
