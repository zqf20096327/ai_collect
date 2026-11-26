# finetune-anywhere

Fine-tune a small open model and run it on your own machine. Colab, Kaggle, NVIDIA, Mac, CPU, or cloud GPU.

**2/10 → 7/10 exact matches in 80 seconds of training on a Colab T4.** The JSON extractor learned from 40 examples and was evaluated on 10 held-out requests.

> Please supply a dozen insulated lunch bags for the field team. Delivery next week is fine.

**Before**
```json
{"item": "lunch bags", "quantity": null, "priority": "normal"}
```

**After**
```json
{"item": "insulated lunch bags", "quantity": 12, "priority": "normal"}
```

[See all ten real before/after answers, settings and remaining errors](recipes/json-extractor/results/2026-11-21-t4/).

[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/junaiddshaukat/finetune-anywhere)](https://github.com/junaiddshaukat/finetune-anywhere/stargazers)
[![Contributors](https://img.shields.io/github/contributors/junaiddshaukat/finetune-anywhere)](https://github.com/junaiddshaukat/finetune-anywhere/graphs/contributors)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/junaiddshaukat/finetune-anywhere/blob/main/paths/colab/finetune_unsloth_colab.ipynb)
[![Open in Kaggle](https://img.shields.io/badge/Open_in-Kaggle-20BEFF)](https://www.kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/junaiddshaukat/finetune-anywhere/main/paths/kaggle/finetune_unsloth_kaggle.ipynb)

## Hackathon participants: start here

Start with [Colab and the JSON extractor](paths/colab/): choose a T4 GPU, keep the default recipe, and run the cells in order. Download your evidence ZIP and GGUF, then follow the local inference instructions. After the first run, use the final notebook section to train on your own data.

Read the [event rules and submission steps](showcase/qwen-local-hackathon-2026/).

## Pick your path

| Your hardware | Start here | Tool | Plan for |
| --- | --- | --- | --- |
| No GPU, free notebook | [Colab](paths/colab/) | Unsloth | An afternoon |
| Kaggle account | [Kaggle](paths/kaggle/) | Unsloth | An afternoon |
| NVIDIA on Linux or Windows/WSL | [Your GPU](paths/nvidia-gpu/) | Unsloth | An afternoon including setup |
| Apple Silicon Mac | [Mac](paths/apple-silicon/) | MLX-LM | An afternoon including downloads |
| CPU laptop | [Cloud training, local inference](paths/cpu-only/) | Ollama or llama.cpp | An afternoon plus cloud training |
| Rented GPU | [Cloud GPU](paths/cloud-gpu/) | Unsloth | Setup plus training; stop billing afterward |

[Start here](guides/00-start-here.md) if these tools are new to you. The defaults are Apache-2.0 Qwen3 text models.

## The seven steps

1. [Pick a model](guides/01-pick-a-model.md). Start small enough to iterate.
2. [Make a dataset](guides/02-make-a-dataset.md). Teach one task with clean examples.
3. [Train](guides/03-train.md). Save a small LoRA adapter.
4. [Evaluate](guides/04-evaluate.md). Compare against the base on unseen prompts.
5. [Quantize](guides/05-quantize.md). Make the model smaller.
6. [Run locally](guides/06-run-locally.md). Use your laptop or a local API.
7. [Share](guides/07-share-your-model.md). Publish the model, evidence and instructions.

## Will it run on my machine?

Weights only, in decimal GB. Parameter counts come from the [model registry](configs/models.yaml).

| Alias | Parameters | 16 bit | 8 bit | 4 bit |
| --- | ---: | ---: | ---: | ---: |
| tiny | 0.6B | 1.20 GB | 0.60 GB | 0.33 GB |
| starter | 1.7B | 3.40 GB | 1.70 GB | 0.94 GB |
| larger | 4.0B | 8.00 GB | 4.00 GB | 2.20 GB |

Formula: parameters × bytes per parameter. Use 2 bytes for 16 bit, 1 for 8 bit, about 0.55 for 4 bit including quantization metadata. Context adds KV cache. Runtime, activations and the operating system need more memory. Training needs more than inference. Discrete GPU VRAM is separate from RAM.

```bash
python scripts/memory_calc.py --params 1.7 --bits 4 --context 4096
python scripts/memory_calc.py --params 1.7 --bits 4 --context 2048 --train
```

## Choose your tool

| Tool | Choose it for |
| --- | --- |
| [Unsloth](paths/nvidia-gpu/) | The default NVIDIA and free-notebook training path |
| [MLX-LM](paths/apple-silicon/) | Training and inference on Apple Silicon |
| [LLaMA-Factory](tools/llama-factory/) | A training web UI or configurable CLI |
| [ms-swift](tools/ms-swift/) | Qwen workflows and the ModelScope ecosystem |
| [Axolotl](tools/axolotl/) | YAML-driven GPU training |
| [TRL + PEFT](tools/trl-peft/) | Learning the Python training pieces |
| [Ollama, llama.cpp, LM Studio](guides/06-run-locally.md) | Running your exported model locally |
| [vLLM](guides/06-run-locally.md) | Serving on a GPU machine |

See the [decision tree and comparison](guides/choose-your-tool.md).

## Recipes

| Recipe | Task |
| --- | --- |
| [Commit message writer](recipes/commit-message-writer/) | Turn a diff into a short conventional commit |
| [JSON extractor](recipes/json-extractor/) | Extract typed fields from a request |
| [SQL generator](recipes/sql-generator/) | Write a read-only query for a supplied schema |
| [Support bot from docs](recipes/support-bot-from-docs/) | Answer from a policy and abstain when it is silent |

Each includes 60 original MIT-licensed examples: 40 for training, 10 for validation and 10 for held-out evaluation.

## Community showcase

<!-- SHOWCASE:START -->

No submissions yet. Be the first to share a model you trained and ran locally.

<!-- SHOWCASE:END -->

[All community models](showcase/README.md). Fine-tuned something? [Add it to the showcase](showcase/README.md#submit-your-model).

## Qwen Local Hackathon 2026

A free online build week organized by **Qwen Pakistan**, 23 to 29 November 2026. Kickoff: Monday 23 November on Microsoft Teams. Fine-tune, quantize, or run a small Qwen model locally. Any one counts.

**Submit by Saturday 28 November, 23:59 PKT (18:59 UTC).** Results: Sunday 29 November. [Rules, judging and submission steps](showcase/qwen-local-hackathon-2026/).

## Contributors

<!-- ALL-CONTRIBUTORS:START - Do not remove or modify this section -->
[M Junaid](https://github.com/junaiddshaukat) maintains this project. Contributions include code, recipes, documentation, testing and community models. [Join in](CONTRIBUTING.md).
<!-- ALL-CONTRIBUTORS:END -->

## Credits

Built for the community by M Junaid, Qwen Ambassador and organizer of **Qwen Pakistan**. An independent community resource.

Thanks to [Qwen](https://github.com/QwenLM), [Unsloth](https://github.com/unslothai/unsloth), [MLX](https://github.com/ml-explore/mlx-lm), [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory), [ms-swift](https://github.com/modelscope/ms-swift), [Axolotl](https://github.com/axolotl-ai-cloud/axolotl), [TRL](https://github.com/huggingface/trl), [PEFT](https://github.com/huggingface/peft), [llama.cpp](https://github.com/ggml-org/llama.cpp), [Ollama](https://github.com/ollama/ollama), [LM Studio](https://lmstudio.ai/) and [vLLM](https://github.com/vllm-project/vllm).

If this helped you train your first model, a star helps other people find it.

[Work and testing report](PROJECT_REPORT.md) · [Maintainer notes](MAINTAINER_NOTES.md)
