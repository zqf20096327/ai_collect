
# Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models

[![arXiv](https://img.shields.io/badge/arXiv-Paper-red.svg)](https://arxiv.org/abs/2604.08964)    [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

This is the official implementation of **AHD (Anchor-based History-stable Decoding)**, a training-free, plug-and-play dynamic decoding strategy for Diffusion Large Language Models (dLLMs).

<p align="center">
  <img src="assets/overview.png" width="100%">
</p>

---

## 📑 Table of Contents

- [Project Structure](#-project-structure)
- [Evaluation of AHD on LLaDA & LLaDA-1.5](#-evaluation-of-ahd-on-llada--llada-15)
- [Evaluation of AHD on MMADA](#-evaluation-of-ahd-on-mmada)
- [Evaluation of AHD on DIFFA](#-evaluation-of-ahd-on-diffa)
- [Todo List](#-todo-list)
- [Citation](#-citation)
- [Acknowledgement](#-acknowledgement)

---

## 📁 Project Structure

```
open-dLLM-compress/
├── llada/                  # AHD on LLaDA-8B-Instruct
│   ├── generate_AHD_acc.py # AHD decoding implementation
│   ├── generate.py         # Baseline (Semi-AR) decoding
│   ├── eval_llada.py       # Evaluation harness wrapper
│   ├── eval_*.sh           # Evaluation scripts for each benchmark
│   └── model/              # LLaDA model definition
├── llada1.5/               # AHD on LLaDA-1.5 (same structure as llada/)
├── MMADA/                  # AHD on MMaDA (vision-language)
│   ├── models/             # MMaDA model with AHD integration
│   ├── scripts/            # Evaluation scripts
│   ├── lmms_eval/          # lmms-eval framework
│   └── generate_demo.py    # Quick demo
├── DIFFA/                  # AHD on DIFFA (audio-language)
│   ├── src/                # DIFFA model and AHD audio decoding
│   ├── inference_voicebench.py
│   └── voicebench/         # VoiceBench evaluation
├── assets/                 # Figures
├── LICENSE
└── README.md
```

---

## 🧪 Evaluation of AHD on LLaDA & LLaDA-1.5

### ⚙️ Models

| Model Name | Hugging Face Repo | Local Path |
|:--|:--|:--|
| LLaDA-8B-Instruct | [`GSAI-ML/LLaDA-8B-Instruct`](https://huggingface.co/GSAI-ML/LLaDA-8B-Instruct) | `./Models/LLaDA-8B-Instruct/` |
| LLaDA-1.5 | [`GSAI-ML/LLaDA-1.5`](https://huggingface.co/GSAI-ML/LLaDA-1.5) | `./Models/LLaDA-1.5/` |

### 📦 Dependencies

```bash
cd llada  # or cd llada1.5
conda create -n llada python=3.12
conda activate llada
pip install -r requirements.txt
```

### 🔧 Quick Demo

> Please make sure to set the correct model path in `generate_AHD_acc.py`.

```bash
python generate_AHD_acc.py
```

### 🔨 Evaluation

#### Supported Benchmarks

| Benchmark | Script | Few-shot |
|:--|:--|:--|
| BBH | `eval_bbh.sh` | 3 |
| MMLU-Pro | `eval_mmlu_pro.sh` | 0 |
| HumanEval | `eval_humaneval.sh` | 0 |
| MBPP | `eval_mbpp.sh` | 3 |
| MATH | `eval_math.sh` | 3 |
| ASDiv | `eval_asdiv.sh` | 0 |
| TruthfulQA | `eval_truthqa.sh` | 0 |

```bash
sh eval_bbh.sh
sh eval_mmlu_pro.sh
sh eval_humaneval.sh
sh eval_mbpp.sh
sh eval_math.sh
sh eval_asdiv.sh
sh eval_truthqa.sh
```

> [!TIP]
> Each script contains both **Baseline** and **AHD**. You can configure `length`, `block_length`, `num_fewshot`, and AHD-specific hyperparameters (`kl_threshold_AHD`, `history_length_AHD`, etc.) directly in the scripts.

> [!NOTE]
> HumanEval requires post-processing:
>
> ```bash
> python postprocess_code.py {samples_xxx.jsonl}
> ```

---

## 🧪 Evaluation of AHD on MMADA

### ⚙️ Models

| Model Name | Hugging Face Repo | Local Path |
|:--|:--|:--|
| MMaDA-8B-MixCoT | [`Gen-Verse/MMaDA-8B-MixCoT`](https://huggingface.co/Gen-Verse/MMaDA-8B-MixCoT) | `./Models/MMaDA-8B-MixCoT/` |

### 📦 Dependencies

```bash
cd MMADA
conda create -n mmada python=3.11
conda activate mmada
pip install -r requirements.txt
```

```bash
cd lmms_eval
uv pip install -e .
```

### 🔧 Quick Demo

> Please make sure to set the correct model path in `generate_demo.py`.

```bash
python generate_demo.py
```

### 🔑 Environment Variable Configuration

Some evaluation tasks use an LLM as a judge (e.g., GPT). Please configure the following environment variables before running evaluation:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
export API_TYPE="openai"
export OPENAI_API_URL="https://api.openai.com/v1/chat/completions"
```

### 🔨 Evaluation

#### Supported Benchmarks

| Benchmark | Task Name |
|:--|:--|
| MathVista-mini | `mathvista_testmini_mmada` |
| MathVision | `mathvision_test_mmada` |
| ScienceQA-Img | `scienceqa_img_mmada` |
| GQA | `gqa` |
| MME | `mme` |

```bash
cd ..
bash scripts/eval_baseline.sh
bash scripts/eval_AHD.sh
```

> [!TIP]
> You can configure the following hyperparameters in the scripts above: `GEN_LENGTH`, `DIFF_STEP`, `BLOCK_LENGTH`, `NGPU`.

> [!NOTE]
> The default LLM-judge model used in this paper is **gpt-4.1-mini**.

---

## 🧪 Evaluation of AHD on DIFFA

### ⚙️ Models

| Model Name | Hugging Face Repo | Local Path |
|:--|:--|:--|
| Whisper-Small | [`openai/whisper-small`](https://huggingface.co/openai/whisper-small) | `./DIFFA/whisper/` |
| DIFFA | [`zhoujiaming777/DIFFA`](https://huggingface.co/zhoujiaming777/DIFFA) | `./DIFFA/checkpoint-diffa/` |
| LLaDA-8B-Instruct | [`GSAI-ML/LLaDA-8B-Instruct`](https://huggingface.co/GSAI-ML/LLaDA-8B-Instruct) | `./DIFFA/LLaDA-8B-Instruct/` |

### 📦 Dependencies

```bash
cd DIFFA
conda create -n diffa python=3.10
conda activate diffa
pip install -r requirements.txt
```

### 🔍 Inference

```bash
python inference_voicebench.py \
    --model_path path/to/DIFFA/checkpoint-diffa \
    --whisper_path path/to/DIFFA/whisper \
    --llm_path path/to/DIFFA/LLaDA-8B-Instruct \
    --data openbookqa \
    --generation_method AHD
```

> [!TIP]
> - **Datasets**: `openbookqa`, `bbh`, `alpacaeval`, `wildvoice`, `commoneval`
> - **Methods**: `Vanilla`, `AHD`
> - **Key arguments**: `--steps`, `--block_length`, `--max_new_tokens`

### 🔨 Evaluation

Follow the evaluation method from [VoiceBench](https://github.com/MatthewCYM/VoiceBench):

```bash
cd voicebench
python evaluate.py --src_file {result.jsonl} --evaluator xx
```

---

## 📑 Todo List

- [ ] Re-architect the codebase
- [ ] Support multi-batch-size
- [ ] Support implementations of other method

---

## 🎓 Citation

If you find this work helpful for your research, please consider citing:

```bibtex
@article{zou2026ahd,
      title={Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models}, 
      author={Shun Zou and Yong Wang and Zehui Chen and Lin Chen and Chongyang Tao and Feng Zhao and Xiangxiang Chu},
      journal={arXiv preprint arXiv:2604.08964},
      year={2026}
}
```

---

## 🙏 Acknowledgement

We would like to thank the authors of the following projects for their excellent work and open-source contributions:

- [LLaDA](https://github.com/ML-GSAI/LLaDA)
- [LLaDA-1.5](https://github.com/ML-GSAI/LLaDA-1.5)
- [Fast-dLLM](https://github.com/NVlabs/Fast-dLLM)
- [MMADA](https://github.com/Gen-Verse/MMaDA)
- [DIFFA](https://github.com/NKU-HLT/DIFFA)
- [WINO](https://github.com/Feng-Hong/WINO-DLLM)
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [VoiceBench](https://github.com/MatthewCYM/VoiceBench)
- [KLASS](https://github.com/shkim0116/KLASS)
