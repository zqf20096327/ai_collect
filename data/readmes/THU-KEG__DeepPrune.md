
---

# 🌿 ACL 2026 Findings | DeepPrune: Parallel Scaling without Inter-trace Redundancy

<p align="center">
     📃 <a href="https://arxiv.org/pdf/2510.08483" target="_blank">Paper</a>  • ✈️ <a href="https://deepprune.github.io/" target="_blank">Project Page</a> • 🤗 <a href="https://huggingface.co/THU-KEG/DeepPrune-Judge-4B" target="_blank">Model</a>  • 🤗 <a href="https://huggingface.co/datasets/THU-KEG/DeepPrune" target="_blank">Data</a>
</p>

<p align="center">
     <strong>Accepted to ACL 2026 Findings</strong>
</p>

> **Efficient reasoning at scale by pruning redundant reasoning traces—without sacrificing accuracy.**

---

## 📌 Overview

Large language models (LLMs) often generate multiple reasoning traces in parallel to improve answer reliability. However, these traces frequently exhibit **severe inter-trace redundancy**, leading to wasted computation and inflated inference costs.  

**DeepPrune** addresses this by learning to identify and prune semantically redundant traces *before* full execution—enabling **cost-effective parallel reasoning** while preserving performance.

**More details can be found in our [website](https://deepprune.github.io/)**

### Results

![1776689362331](figs/image.png)

---

## 📦Dependencies
```
cd DeepPrune  
pip install -r requirements.txt
```

⚠️ We use `Llama-Factory` for model fine-tuning and inference and we have provided the version we used in `Llama-Factory` folder. Here we modify it to support Focal Loss. Please refer to the [GitHub issue](https://github.com/hiyouga/LLaMA-Factory/pull/9077) if you want to clone `LLaMA-Factory` by yourself.

⚠️ We use `Qwen/Qwen3-4B-Instruct-2507` as the backbone LLM for DeepPrune. You can download it from [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507). You can also use other open-source LLMs.

---

## 🧾 Dataset

### ⚠️ The dataset provided here is not complete because of the size! ! ! Please refer to [Dataset](https://huggingface.co/datasets/THU-KEG/DeepPrune) for the full dataset.

To understand how to use the dataset, please refer to `DeepPrune_data/README.md`. [Click here](DeepPrune_data/README.md)

---

## 🧪 Preliminaries

To understand the motivation behind DeepPrune, explore the preliminary analysis in:

📁 `Preliminaries/Preliminary experiment.ipynb`

This notebook includes:

- 📊 **Distribution of answer agreement**:  
  Most trace pairs yield the *same answer*, revealing significant redundancy in parallel reasoning.
  
- 📈 **ROC curves for redundancy detection**:
  - **Sentence-BERT (shallow similarity)**: AUROC = 0.58 → limited discriminative power.  
  - **Qwen3-4B-Instruct (zero-shot LLM comparison)**: AUROC = 0.66 → moderate improvement, but still suboptimal.

> 🔧 To reproduce the zero-shot Qwen3-4B-Instruct results:  
> 1. Prepare the evaluation dataset using `DeepPrune/Offline/Ablation_Study.ipynb`  
> 2. Run `Preliminaries/zero_shot_exp.py`

---

## 🛠️ DeepPrune Pipeline

### ⚙️ Prerequisites

- Install [`Llama-Factory`](https://github.com/hiyouga/LLaMA-Factory)  
- ⚠️ **Patch required**: Modify the codebase to support **Focal Loss** (see GitHub issue for guidance).

---

### 1️⃣ Prepare Finetuning Dataset

Generate the supervised training data for DeepPrune:

```bash
jupyter notebook DeepPrune/finetuning/build_finetune_dataset.ipynb
```

This constructs pairwise trace comparisons labeled by answer equivalence.

---

### 2️⃣ Offline Training

Train the DeepPrune model using supervised fine-tuning:

- Config: `LLaMA-Factory/examples/train_full/Qwen3_full_sft.yaml`
- Framework: Llama-Factory

After training:

1. Generate test data: `DeepPrune/Offline/Ablation_Study.ipynb`  
2. Evaluate performance:  
   ```bash
   python DeepPrune/Offline/offline_exp.py
   ```
3. Visualize results: `DeepPrune/Offline/check_model_output.ipynb`

✅ Expect significant gains over shallow similarity baselines (AUROC > 0.83 in our experiments).

---

### 3️⃣ Online Pruning

Deploy DeepPrune for real-time trace pruning during inference:

1. **Establish baselines**:  
   Run `DeepPrune/Online/check_pass_k.ipynb` to compute:
   - `pass@1`: Accuracy with single trace
   - `cons@512`: Consensus accuracy with 512 traces

2. **Apply DeepPrune**:  
   ```bash
   python DeepPrune/Online/greedy_cluster_threshold.py
   ```
   This performs greedy clustering of traces using DeepPrune’s similarity scores and prunes redundant ones.

3. **Trade-off control**:  
   Adjust the similarity **threshold** to balance:
   - 💰 **Cost reduction** (fewer traces executed)
   - 🎯 **Performance retention** (maintained consensus accuracy)

---
## 🙏 Acknowledgement

This code repository is developed based on [Llama-Factory](https://github.com/hiyouga/LLaMA-Factory), [vllm](https://github.com/vllm-project/vllm), [DeepScaleR](https://github.com/agentica-project/rllm) and [DeepConf](https://github.com/facebookresearch/deepconf).

Thanks for their great work!

---
## 📜 Citation

If you use DeepPrune in your research, please cite our work. This paper was accepted to **ACL 2026 Findings**.

```
@article{tu2025deepprune,
  title={DeepPrune: Parallel Scaling without Inter-trace Redundancy}, 
  author={Shangqing Tu, Yaxuan Li, Yushi Bai, Lei Hou, Juanzi Li},
  journal={arXiv preprint arXiv:2510.08483},
  year={2025}
}
```

