<div align="center" style="font-family: charter;">
<h1>TFPI: Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners</br></h1>


<a href="https://arxiv.org/abs/2509.26226" target="_blank">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-TFPI-red?logo=arxiv" height="20" /></a>
<a href="https://huggingface.co/collections/xx18/tfpi" target="_blank">
    <img alt="" src="https://img.shields.io/badge/%F0%9F%A4%97%20_Models-TFPI-ffc107?color=ffc107&logoColor=white" height="20" /></a>

<div>
    <a href="https://xinxu-ustc.github.io/" target="_blank">Xin Xu</a><sup>1,</sup><sup>2,</sup>,</span>
    <a href="" target="_blank">Cliveb AI</a><sup>1</sup>,</span>
    <a href="https://github.com/yk7333" target="_blank">Kai Yang</a><sup>1,</sup>,</span>
    <a href="https://github.com/dandingsky" target="_blank">Tianhao Chen</a><sup>2,</sup>,</span>
    <a href="https://www.presidentsoffice.hku.hk/leadership/professor-yang-wang" target="_blank">Yang Wang</a><sup>3,</sup>,</span>
    <a href="https://github.com/yangsaiyong" target="_blank">Saiyong Yang</a><sup>1,</sup>,</span>
    <a href="https://sites.google.com/site/eeyangc/" target="_blank">Can Yang</a><sup>2,</sup>,</span>
</div>

<div>
    <sup>1</sup>Hunyuan LLM Department, Tencent&emsp;
    </br>
    <sup>2</sup>The Hong Kong University of Science and Techology&emsp;
    </br>
    <sup>3</sup>The University of Hong Kong&emsp;
    </br>
</div>


</div>      

## Overview

**T**hinking-**F**ree **P**olicy **I**nitialization (**TFPI**), a simple yet effective adaptation to Reinforcement Learning with Verifiable Reward (RLVR) that bridges long Chain-of-Thought (CoT) distillation and standard RLVR. TFPI employs a simple *ThinkingFree* operation, explicitly discarding the thinking content via a direct </think> append, to reduce token usage during inference. Training with *ThinkingFree*-adapted inputs improves performance and lowers token consumption, even in the original slow-thinking mode. Extensive experiments across various benchmarks have shown that TFPI accelerates RL convergence, achieves a higher performance ceiling, and yields more token-efficient reasoning models without specialized rewards or complex training designs. With TFPI only, we can train a 4B model to reach 89.0% accuracy on AIME24 and 65.5% on LiveCodeBench with extremely low training compute.



## 📝 News
- [2026/01/26] Our paper is accepted to ICLR 2026.
- [2025/12/22] We released the codes.
- [2025/11/7] We released the [model checkpoints](https://huggingface.co/collections/xx18/tfpi).
- [2025/9/30] We released the [paper](https://arxiv.org/abs/2509.26226)!



## 🚀 Quick Start

### Installation

#### 1. Environment setup
```bash
conda create -n TFPI python=3.10 -y
conda activate TFPI
```

#### 2. Requirements installation
```bash
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
pip install vllm==0.8.5.post1
pip install -e .
pip install vertexai
pip install sentence_transformers
pip install flash-attn==2.7.4.post1 --no-build-isolation
```



### Run Training
The training dataset is the training prompts in [Polaris-53K](https://huggingface.co/datasets/POLARIS-Project/Polaris-Dataset-53K).

First, download and transform the format of training data using the following Python script:

```bash
python scripts/download_train.py
```

The training data is saved in `./data/train/tfpi-polaris53k.parquet`


Next, adapt the training script in `"./scripts/train/qwen3-4b-tfpi.sh"` by setting the WandB key, model path and dataset path.

Finally, run the following commands at the master node:
```bash
bash ./scripts/ray_start.sh # start ray
bash ./scripts/train/qwen3-4b-tfpi.sh # submit training
```

### Run Evaluation

First, download the evaluation datasets using
```bash
hf download xx18/TFPI-EVA --repo-type=dataset --local-dir ./data/eval
```

All test datasets are downloaded to the folder `data/eval`.

for evaluation, use:
```bash
bash ./scripts/ray_start.sh # start ray, use pssh to run on multiple nodes if necessary
bash scripts/eval/start_generate.sh
```

The resulted metrics and evaluation outputs will be saved under the folder `your_model_path/eval_results`

For `IFEval`, please refer to the official repo [IFEval evaluation](https://github.com/google-research/google-research/tree/master/instruction_following_eval).

## 🤗 Datasets and Models

we are open-sourcing our complete codes, and training details for the research community. All our resulted checkpoints can be found in [TFPI Collection](https://huggingface.co/collections/xx18/tfpi).

| Name | Link | Remarks | 
| - | - | - |
| Evaluation Sets | [TFPI-EVA](https://huggingface.co/datasets/xx18/TFPI-EVA) | All evaluation datasets used in the TFPI paper, including AIME24, AIME25, BeyondAIME, LiveCodeBench, GPQA, and IFEval |
| Training set | [Polaris-53K](https://huggingface.co/datasets/POLARIS-Project/Polaris-Dataset-53K) | - |
| 1.5B TFPI Stage 1 | [TFPI-DeepSeek-Qwen-1.5B-Stage1](https://huggingface.co/xx18/TFPI-DeepSeek-Qwen-1.5B-Stage1) | Results in Table 1; Training Response Length 2048 |
| 1.5B TFPI Stage 2 | [TFPI-DeepSeek-Qwen-1.5B-Stage2](https://huggingface.co/xx18/TFPI-DeepSeek-Qwen-1.5B-Stage2) | Results in Table 1; Training Response Length 4096 |
| 1.5B TFPI Stage 3 | [TFPI-DeepSeek-Qwen-1.5B-Stage3](https://huggingface.co/xx18/TFPI-DeepSeek-Qwen-1.5B-Stage3) | Results in Table 1; Training Response Length 8192 |
| 1.5B TFPI Stage 3 + DAPO | [TFPI-DeepSeek-Qwen-1.5B-Stage3_then_RL](https://huggingface.co/xx18/TFPI-DeepSeek-Qwen-1.5B-Stage3_then_RL) | Results in Table 7; Training Response Length 16K; |
| 1.5B Direct RL checkpoint 1 | [DirectRL_DeepSeek-Qwen-1.5B_baseline1](https://huggingface.co/xx18/DirectRL_DeepSeek-Qwen-1.5B_baseline1) | Results in Table 1; Training Response Length 16K; Traning Time = 3 stages of TFPI | 
| 1.5B Direct RL checkpoint 2 | [DirectRL_DeepSeek-Qwen-1.5B_baseline2](https://huggingface.co/xx18/DirectRL_DeepSeek-Qwen-1.5B_baseline2) | Results in Table 7; Training Response Length 16K; Traning Time = ''TFPI+RL'' | 
| Qwen3-4B TFPI Stage 1 | [TFPI-Qwen3-4B-Stage1](https://huggingface.co/xx18/TFPI-Qwen3-4B-Stage1) | Results in Table 1; Training Response Length 4096 | 
| Qwen3-4B TFPI Stage 2 | [TFPI-Qwen3-4B-Stage2](https://huggingface.co/xx18/TFPI-Qwen3-4B-Stage2) | Results in Table 1; Training Response Length 8192 | 
| Qwen3-4B TFPI Stage 3 | [TFPI-Qwen3-4B-Stage3](https://huggingface.co/xx18/TFPI-Qwen3-4B-Stage3) | Results in Table 1; Training Response Length 16K | 
| Qwen3-4B TFPI Stage 3 + DAPO | [TFPI-Qwen3-4B-Stage3_then_RL](https://huggingface.co/xx18/TFPI-Qwen3-4B-Stage3_then_RL) | Results in Table 2; Training Response Length 32K |
| Qwen3-4B Direct RL checkpoint 1 | [DirectRL_Qwen3-4B_baseline1](https://huggingface.co/xx18/DirectRL_Qwen3-4B_baseline1) | Results in Table 1; Training Response Length 32K; Traning Time = 3 stages of TFPI |
| Qwen3-4B Direct RL checkpoint 2 | [DirectRL_Qwen3-4B_baseline2](https://huggingface.co/xx18/DirectRL_Qwen3-4B_baseline2) | Results in Table 2; Training Response Length 32K; Traning Time = ''TFPI+RL'' |
| Qwen3-4B-Thinking-2507 Stage 3 | [TFPI-Qwen3-4B-Thinking-2507-Stage3](https://huggingface.co/xx18/TFPI-Qwen3-4B-Thinking-2507-Stage3) | Results in Table 2; Training Response Length 16K |





## 🤝 Acknowledgement

We are deeply grateful for the following GitHub repositories, as their valuable code and efforts have been incredibly helpful:

* [DeepScaler](https://github.com/agentica-project/rllm)
* [VeRL](https://github.com/volcengine/verl)


## ✏️ Citation

### Bib
If you find TFPI useful for your research and applications, please cite using this BibTeX:
```
@article{xu2025tfpi,
  title={Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners},
  author={Xu, Xin and AI, Cliveb and Yang, Kai and Chen, Tianhao and Wang, Yang and Yang, Saiyong and Yang, Can},
  journal={arXiv preprint arXiv:2509.26226},
  year={2025}
}
```
