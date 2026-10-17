# RoboMP<sup>2</sup>: A Robotic Multimodal Perception-Planning Framework with Multimodal Large Language Models

> **[ICML 2024]** A robotic multimodal perception-planning framework that combines retrieval-augmented prompting, multimodal code generation, and executable manipulation primitives for robotic tasks.

## Authors

[**Qi Lv**](https://aopolin-lv.github.io/)<sup>1,2</sup>, [**Hao Li**](https://openreview.net/profile?id=~Hao_Li59)<sup>1</sup>, [**Xiang Deng**](https://xiang-deng-dl.github.io/)<sup>1</sup>\*, [**Rui Shao**](https://rshaojimmy.github.io/)<sup>1</sup>, [**Michael Yu Wang**](https://scholar.google.com/citations?user=Oo7c22wAAAAJ&hl=zh-CN)<sup>2</sup>, [**Liqiang Nie**](https://liqiangnie.github.io/)<sup>1</sup>\*

<sup>1</sup> Harbin Institute of Technology, Shenzhen  
<sup>2</sup> Great Bay University  
\* Corresponding authors

## Links

- **Paper**: [`arXiv`](https://arxiv.org/abs/2404.04929)
- **Project Page**: [`Website`](https://aopolin-lv.github.io/RoboMP2.github.io/)
- **Code Repository**: [`GitHub`](https://github.com/iLearn-Lab/ICML25-RoboMP2)

---

## Table of Contents

- [Updates](#updates)
- [Introduction](#introduction)
- [Highlights](#highlights)
- [Method / Framework](#method--framework)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Tasks / Evaluation Setting](#tasks--evaluation-setting)
- [Usage](#usage)
- [Results](#results)
- [Citation](#citation)
- [Acknowledgement](#acknowledgement)
- [License](#license)

---

## Updates

- [05/2024] RoboMP<sup>2</sup> was presented at ICML 2024

---

## Introduction

RoboMP<sup>2</sup> is a robotic multimodal perception-planning framework for manipulation tasks. This repository contains the project code used to transform VIMABench task descriptions and scene observations into executable action programs with multimodal large language models.

From the current codebase, the main inference pipeline consists of:

1. **Prompt Grounding**: Convert VIMABench prompts and prompt assets into language descriptions or visual templates.
2. **Instruction Rewriting**: Rewrite the task instruction to improve retrieval robustness.
3. **Example / API Retrieval**: Rank relevant demonstrations and APIs with coarse- and fine-grained retrieval.
4. **Program Generation**: Query GPT-4V with the current scene image and retrieved context to generate executable code.
5. **Robot Execution**: Parse the generated code into manipulation primitives and execute it in the simulator.

This repository provides:
- Evaluation and rollout scripts on VIMABench
- Retrieval modules for example and API selection
- Prompt rewriting and code post-processing utilities
- Robotic action primitives and perception-planning helpers

---

## Highlights

- Multimodal perception-planning framework for robotic manipulation with multimodal large language models
- Retrieval-augmented prompting with instruction rewriting plus coarse/fine-grained ranking
- GPT-4V-based executable code generation grounded on current scene observations
- Built-in robotic primitives such as `PickPlace`, `DistractorActions`, `RearrangeActions`, and `RotateAll`
- Strong performance against end-to-end models and MLLM planners, reaching **82.4** average score in the reported benchmark

---

## Method / Framework

The repository implements a perception-planning loop centered around `eval.py`, `retrieval/`, and `engine_robotic.py`:

![RoboMP2 Framework](./assets/robomp2.png)

**Figure 1.** Overall framework of RoboMP<sup>2</sup>.

1. **Task Preparation**
   `utils/data_prepare.py` turns VIMABench prompt placeholders into either natural-language object descriptions or visual templates extracted from prompt assets.

2. **Retrieval-Augmented Prompt Construction**
   `retrieval/rewrite.py` rewrites the task instruction, and `retrieval/sort.py` ranks relevant examples from `data/codebase/all_codebase.json` using TF-IDF and Sentence-BERT scoring.

3. **Multimodal Program Synthesis**
   `data_process/gptutils.py` sends the assembled prompt together with the current top-view observation to GPT-4V (`gpt-4-vision-preview`) and receives executable program text.

4. **Program Parsing and Execution**
   `data_process/utils.py` filters task-specific code snippets, and `engine_robotic.py` executes the resulting manipulation actions in VIMABench with perception, geometry, and control helpers.

The code also includes a local MLLM wrapper in `model/custom_model.py`, which is used by the execution engine for object grounding and scene reasoning.

---

## Project Structure

```text
.
├── assets/
│   └── robomp2.png                        # Framework figure
├── data/
│   ├── codebase/
│   │   ├── all_codebase.json              # Retrieved example codebase
│   │   ├── apibase.json                   # API prompt resources
│   │   └── method_apibase.json            # Method-level API resources
│   ├── prompt_base/
│   │   ├── first_level.ini                # Prompt templates
│   │   ├── second_level.ini
│   │   ├── third_level.ini
│   │   └── instruction.ini
│   └── rewrite.txt                        # Instruction rewriting prompt
├── data_process/
│   ├── gptutils.py                        # OpenAI / GPT-4V API wrappers
│   ├── utils.py                           # Result parsing and helper utilities
│   └── __init__.py
├── model/
│   ├── custom_model.py                    # Local MLLM loading and wrapper
│   ├── InstructModel.py                   # Model definition
│   └── utils.py
├── retrieval/
│   ├── rewrite.py                         # Instruction rewriting
│   ├── similarity_retrieval.py            # Sentence-BERT / BM25 / TF-IDF retrieval
│   ├── sort.py                            # Coarse and fine-grained ranking
│   ├── utils.py
│   └── __init__.py
├── utils/
│   ├── common_utils.py                    # Shared utilities and logging
│   └── data_prepare.py                    # Prompt and template construction
├── engine_robotic.py                      # Robot execution primitives and helpers
├── eval.py                                # Main evaluation / rollout entry
├── environment.yaml                       # Conda environment definition
├── requirements.txt                       # Pip dependency list
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/iLearn-Lab/ICML25-RoboMP2.git
cd ICML25-RoboMP2
```

### 2. Create environment

The repository provides both a full Conda environment file and a lighter `requirements.txt`.

Recommended:

```bash
conda env create -f environment.yaml
conda activate vima
```

Alternative:

```bash
conda create -n robomp2 python=3.9
conda activate robomp2
pip install -r requirements.txt
```

### 3. Install VIMABench

This project depends on `vima_bench`, which should be installed separately:

```bash
git clone https://github.com/vimalabs/VIMABench.git
cd VIMABench
pip install -e .
```

### 4. Optional gym fix

If `gym==0.21.0` fails during installation, try:

```bash
pip install setuptools==65.5.0
pip install wheel==0.38.0
```

---

## Tasks / Evaluation Setting

The default evaluation loop in `eval.py` covers four VIMABench generalization partitions:

- `placement_generalization`
- `combinatorial_generalization`
- `novel_object_generalization`
- `novel_task_generalization`

The default task list includes:

- `rearrange_then_restore`
- `scene_understanding`
- `novel_adj`
- `novel_noun`
- `twist`
- `follow_order`
- `sweep_without_exceeding`
- `same_shape`
- `manipulate_old_neighbor`
- `pick_in_order_then_restore`
- `novel_adj_and_noun`
- `follow_motion`
- `same_texture`

By default, results are written to:

```text
./visual_programming_prompt/save_demo_output/
```

---

## Usage

### Step 1: Configure external services and local model paths

Before running the evaluation, update the following files:

- `data_process/gptutils.py`: set `base_url` and `api_key` for GPT-4 / GPT-4V access
- `retrieval/similarity_retrieval.py`: set `SENTENCEBERT_PATH`
- `model/custom_model.py`: set the local checkpoint path for the MLLM and processor

The current implementation expects:

- Instruction rewriting via `gpt-4-1106-preview`
- Multimodal program generation via `gpt-4-vision-preview`
- Retrieved examples from `data/codebase/all_codebase.json`

### Step 2: Adjust the evaluation configuration

Edit the configuration values near the bottom of `eval.py` if needed:

- `tasks`
- `partitions`
- `prompt_modal`
- `save_dir`
- `hide_arm`
- `seed`

### Step 3: Run evaluation

```bash
python eval.py
```

### Step 4: Inspect outputs

The script saves:

- JSON rollout results under `save_dir/<partition>/<task>/<prompt_modal>/`
- Log files under `save_dir/`
- Failure or debug images under `save_dir/.../imgs/`

---

## Results

Here we report the performance comparison between RoboMP<sup>2</sup> and representative baseline models.

### Main Results

| Model | L1 | L2 | L3 | L4 | Avg. |
|---|---:|---:|---:|---:|---:|
| *End-to-end models* |  |  |  |  |  |
| Gato<sup>&dagger;</sup> | 58.1 | 53.2 | 43.5 | 12.4 | 41.8 |
| Flamingo<sup>&dagger;</sup> | 47.5 | 46.0 | 40.8 | 12.1 | 36.6 |
| VIMA<sup>&dagger;</sup> | 81.6 | 81.5 | 79.0 | 48.9 | 72.7 |
| RT-2 | 72.8 | 70.3 | 66.8 | 47.0 | 64.2 |
| *MLLM planners* |  |  |  |  |  |
| CaP | 71.2 | 70.0 | 42.8 | 44.7 | 57.2 |
| VisualProg | 49.7 | 47.7 | 69.9 | 52.2 | 54.9 |
| I2A<sup>&dagger;</sup> | 77.0 | 76.2 | 66.6 | 49.8 | 65.0 |
| **RoboMP<sup>2</sup> (Ours)** | **89.0** | **85.9** | **86.8** | **68.0** | **82.4** |

---

## Citation

If you find this project useful, please consider citing:

```bibtex
@InProceedings{pmlr-v235-lv24a,
  title = 	 {{R}obo{MP}$^2$: A Robotic Multimodal Perception-Planning Framework with Multimodal Large Language Models},
  author =       {Lv, Qi and Li, Hao and Deng, Xiang and Shao, Rui and Wang, Michael Y and Nie, Liqiang},
  booktitle = 	 {Proceedings of the 41st International Conference on Machine Learning},
  pages = 	 {33558--33574},
  year = 	 {2024},
  editor = 	 {Salakhutdinov, Ruslan and Kolter, Zico and Heller, Katherine and Weller, Adrian and Oliver, Nuria and Scarlett, Jonathan and Berkenkamp, Felix},
  volume = 	 {235},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {21--27 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://raw.githubusercontent.com/mlresearch/v235/main/assets/lv24a/lv24a.pdf},
  url = 	 {https://proceedings.mlr.press/v235/lv24a.html},
}
```

---

## Acknowledgement

- [VIMABench](https://github.com/vimalabs/VIMABench) for the robotic manipulation benchmark environment
- [OpenAI API](https://platform.openai.com/docs/) for GPT-4 / GPT-4V based program generation
- [Sentence-Transformers](https://www.sbert.net/) and [FAISS](https://github.com/facebookresearch/faiss) for retrieval
- [OpenCLIP](https://github.com/mlfoundations/open_clip) and InstructBLIP-related components for multimodal perception utilities

---

## License

This project is released under the Apache License 2.0.
