# BitMamba-2: Efficient Scaling of 1.58-bit State Space Models (JAX/Flax)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/Paper-Zenodo-00649C.svg)](https://doi.org/10.5281/zenodo.18394665)
[![Hugging Face 1B](https://img.shields.io/badge/%F0%9F%A4%97%20Weights-1B%20Model-FFD21E)](https://huggingface.co/Zhayr1/BitMamba-2-1B)
[![Hugging Face 255M](https://img.shields.io/badge/%F0%9F%A4%97%20Weights-255M%20Model-FFD21E)](https://huggingface.co/Zhayr1/BitMamba-2-0.25B)
[![TPU Supported](https://img.shields.io/badge/Hardware-Google%20Cloud%20TPU-blue)](https://cloud.google.com/tpu)

**BitMamba-2** introduces a scalable, hybrid architecture that integrates **1.58-bit ternary quantization** (BitNet) into the **Mamba-2** state space model framework. This repository contains the **JAX/Flax source code** used to pre-train the models from scratch on Google Cloud TPUs.

We provide the training scripts for two scales:

- **BitMamba-2-255M:** A lightweight baseline trained on 400B tokens.
- **BitMamba-2-1B:** A scaled-up model trained on 150B tokens demonstrating strong reasoning capabilities.

### 📊 Benchmark Results

Scaling from 255M to 1B parameters yields consistent improvements in reasoning capabilities and language modeling fluency. Evaluation performed zero-shot.

| Benchmark      |          Metric           | BitMamba-2-255M | BitMamba-2-1B | Improvement |
| :------------- | :-----------------------: | :-------------: | :-----------: | :---------: |
| **ARC-Easy**   |         Accuracy          |     55.51%      |  **63.30%**   |    +7.8%    |
| **PIQA**       |         Accuracy          |     64.42%      |  **68.77%**   |    +4.4%    |
| **BoolQ**      |         Accuracy          |     59.30%      |  **62.35%**   |    +3.1%    |
| **HellaSwag**  |         Acc Norm          |     35.22%      |  **45.59%**   |   +10.4%    |
| **Winogrande** |         Accuracy          |        -        |  **52.80%**   |      -      |
| **WikiText-2** | Perplexity ($\downarrow$) |      51.69      |   **29.62**   |  **-22.1**  |

### 🚀 Efficiency & Speed (C++ Inference)

Inference benchmarked on an **Intel Core i3-12100F** using our standalone C++ engine.

| Model               | Params | Quantization | Model Size | RAM Usage  |     Speed      |
| :------------------ | :----: | :----------: | :--------: | :--------: | :------------: |
| **BitMamba-2-255M** |  255M  |   1.58-bit   | **247 MB** | **252 MB** | **~146 tok/s** |
| **BitMamba-2-1B**   |   1B   |   1.58-bit   | **614 MB** | **621 MB** | **~53 tok/s**  |

> **Note:** For the standalone C++ inference engine (`bitmamba.cpp`) optimized for edge devices, please visit our [Inference Repository](https://github.com/Zhayr1/bitmamba.cpp).

---

## 📂 Project Structure

```text
BitMamba-2/
├── requirements.txt      # Python dependencies (jax, flax, optax, etc.)
├── src/
│   ├── model.py          # BitMamba2LM architecture definition & BitLinear layers
│   ├── train_255m.py     # Training script for the 255M model
│   └── train_1b.py       # Training script for the 1B model
├── README.md
└── LICENSE
```

## 🛠️ Setup & Requirements

### 1. Hardware Environment

These scripts are explicitly designed to run on **Google Cloud TPU VMs** (e.g., TPU v4-8, v5e, or v6e). They leverage JAX's `pmap` and sharding for efficient distributed training across TPU cores.

### 2. Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Zhayr1/BitMamba-2.git
cd BitMamba-2
pip install -r src/requirements.txt
```

## 🚀 Training

### Configuration (Crucial Step)

Before running any script, you must configure your storage and authentication credentials directly inside the training files (`src/train_255m.py` and `src/train_1b.py`).

Open the scripts and locate the configuration block at the top:

```python
# --- USER CONFIGURATION ---

HF_TOKEN = "your_hf_token" # Your Hugging Face Write Token (to load datasets)
GCS_BUCKET_NAME = "your_bucket" # Your Google Cloud Storage Bucket (to push checkpoints)
```

- **HF_TOKEN**: Required to load the datasets from Hugging Face.
- **GCS_BUCKET_NAME**: Required to push the checkpoints to Google Cloud Storage.

### Running the Training

Once configured, launch the training process directly on the TPU VM:

**To train the 255M Model:**

```bash
python src/train_255m.py
```

**To train the 1B Model:**

```bash
python src/train_1b.py
```

The scripts handle:

- Model initialization (random weights).
- Dataset streaming (FineWeb-Edu, Cosmopedia, Stack-Dedup).
- Distributed training loop with gradient accumulation.
- Periodic checkpointing to Hugging Face / GCS.

## 🔮 Inference

We provide a standalone, high-performance C++ inference engine optimized for consumer CPUs (AVX2), as well as Python scripts for PyTorch inference.

- **Fast Inference (C++)**: Running on pure CPU with 1.58-bit optimized kernels.
- **Python Inference**: Scripts for running the model with PyTorch.

👉 **Access the Inference Repository here:** [Zhayr1/bitmamba.cpp](https://github.com/Zhayr1/bitmamba.cpp)

## 📊 Datasets

The models are trained on a high-quality mix designed for reasoning and coding:

- **FineWeb-Edu** (60%)
- **Cosmopedia** (20%)
- **The Stack-Dedup** (20%)

> **Note:** The dataloading logic in `train_*.py` expects this distribution. Ensure you have access to these datasets via Hugging Face.

## 📜 Citation

If you find this work useful, please cite our paper via Zenodo:

```bibtex
@misc{salazar2026bitmamba2,
  author       = {Salazar, Jesus},
  title        = {{BitMamba}-2: Efficient Scaling of 1.58-bit State Space Models},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18394665},
  url          = {https://doi.org/10.5281/zenodo.18394665}
}
```

## 🙏 Acknowledgments

We explicitly thank the **Google TPU Research Cloud (TRC)** program for providing access to the Cloud TPU v6e accelerators used in this work. Research supported with Cloud TPUs from Google's tpu research cloud (TRC).
