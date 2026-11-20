<p align="center">
  <img src="docs/assets/logo.png" alt="QDA" width="190">
</p>

<h3 align="center">
LLM quantization recipes, designed by an agent
</h3>

<p align="center">
| <a href="https://mit-han-lab.github.io/qda-blog"><b>Blog</b></a> | <a href="https://arxiv.org/abs/2611.23388"><b>Paper</b></a> | <a href="docs/index.md"><b>Docs</b></a> | <a href="https://huggingface.co/qda-lab"><b>Models</b></a> |
</p>

**QDA** is a system for LLM quantization in which a coding agent designs the recipe for each model and precision.
Quantizing an LLM to 4 or 3 bits makes it much cheaper to serve. The best way to do it, the *recipe* (which methods,
in which order, with which settings), differs from model to model, and finding it by hand is slow, expert work. In
QDA, the agent proposes recipes, QDA builds each one and scores it in minutes, and the best one ships as a checkpoint
that stock **vLLM** or **llama.cpp** loads with no extra code.

In the [paper](https://arxiv.org/abs/2611.23388), QDA's recipes beat the strongest public recipe on four reasoning
models by 0.9 to 2.2 accuracy points on average. On GLM-5.3-Flash at NVFP4, they keep 98.3% of the FP8 model's
accuracy, against 96.9% for the best vendor checkpoint. Builds are fast too: on 2 H100s, QDA's GPTQ runs 2.95x to
10.69x faster than llm-compressor 0.15 ([measurements](docs/reproduce.md#build-speed-against-llm-compressor)).

<p align="center">
  <img src="docs/assets/teaser.png" alt="Accuracy over the best public recipe, GLM-5.3-Flash at NVFP4, and GPTQ build speed" width="860">
</p>

## Install

You need Linux, an NVIDIA GPU and [uv](https://docs.astral.sh/uv/) (see the [driver and disk requirements](docs/install.md#requirements)):

```bash
git clone https://github.com/humanfia/qda.git && cd qda
uv venv -p 3.12 --managed-python --seed && . .venv/bin/activate
uv pip install -c constraints.txt "./packages/qda-quant[hf,gguf]" "./packages/qda-kl[vllm]" ./packages/qda-agent
vllm download-kernels   # only on L40S, RTX 4090, RTX PRO 6000, B200 or GB300, or without the CUDA compiler (nvcc)
qda doctor
```

`qda doctor` checks your setup. Anything it marks `MISS` comes with the command or setting that fixes it.

## Quantize

Try it on a small model first. This quantizes Qwen3-0.6B to W4A16 on one GPU (a 1.7 GB download, then about 46 s on an
H100):

```bash
qda build configs/quickstart.yaml
```

At the end it prints a `vllm serve` command; copy it to serve the model under the name `Qwen3-0.6B-W4A16`. The
[quickstart](docs/quickstart.md) also shows how to measure how much quality it lost.

## Search

<p align="center">
  <img src="docs/assets/loop.png" alt="The agent proposes a recipe; QDA builds it, ranks it by KL and checks long generations" width="860">
</p>

The agent proposes a recipe. QDA builds it and measures how far the quantized model's outputs drift from the
original's (the KL divergence), on prompts the agent never sees, so the agent cannot tune to the test. Promising
recipes are also checked on long generations, to catch failures such as repetition loops. The best recipe that fits
your size budget ([bits per weight](docs/search.md#budget)) wins.

**Warning:** the search agent runs without asking for approval, and every job it starts runs under your user
account. Read [agent search](docs/search.md) before running it on a shared machine.

First install and sign in to an [agent](docs/search.md#the-agent) (Claude Code by default; Codex and DeepSeek also
work). Then search a recipe for Qwen3-8B at W4A16 on 4 GPUs: `prepare` sets up the run, `search` runs the agent until
the GPU-hour budget is spent, and `eval` scores the winner on held-out prompts:

```bash
qda-agent prepare --model Qwen/Qwen3-8B --out work/q8b --format w4a16 --cards 0,1,2,3 --budget-gpu-hours 6
qda-agent search work/q8b
qda eval work/q8b/run
```

## Models

We publish 30 quantized checkpoints of 10 models in five formats (W4A16, W3A16, W4A8, W4A4, GGUF): see
[published models](docs/published.md). Each model card gives its scores, its size and the command that serves it.
The recipe that built it, with its inputs, is in the
[recipe-inputs](https://huggingface.co/datasets/qda-lab/qda-recipe-inputs) dataset, so you can rebuild it.

## Supported engines and GPUs

vLLM 0.33 serves every published checkpoint except the GGUF files, which llama.cpp serves. SGLang 0.5.23 serves the
W4A16 checkpoints of the 5 dense (non-MoE) models, plus
[Qwen3.6-35B-A3B for SGLang](https://huggingface.co/qda-lab/QDA-Qwen3.6-35B-A3B-W4A16-SGLang); on B200, add
`--quantization awq_marlin`. Which GPU runs which format: [formats](docs/formats.md#does-my-gpu-run-it).

## Acknowledgements

QDA builds on the quantization methods of [GPTQ](https://github.com/IST-DASLab/gptq),
[GPTAQ](https://github.com/Intelligent-Computing-Lab-Panda/GPTAQ), [AWQ](https://github.com/mit-han-lab/llm-awq),
[AutoRound](https://github.com/intel/auto-round), [GSQ](https://github.com/IST-DASLab/GSQ) and
[QuaRot](https://github.com/spcl/QuaRot), and writes checkpoints in the formats of
[compressed-tensors](https://github.com/vllm-project/compressed-tensors),
[llm-compressor](https://github.com/vllm-project/llm-compressor),
[NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer) and
[llama.cpp](https://github.com/ggml-org/llama.cpp)'s GGUF, so that [vLLM](https://github.com/vllm-project/vllm) and
[SGLang](https://github.com/sgl-project/sglang) can serve them. Third-party code included in QDA is listed in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Citation

```bibtex
@article{li2026qda,
  title   = {QDA: Closed-Loop LLM Quantization Design with Agents},
  author  = {Li, Xingyang and Zhao, Tianlang and Han, Song and Zhu, Ligeng},
  journal = {arXiv preprint arXiv:2611.23388},
  year    = {2026}
}
```

## License

Apache-2.0 ([LICENSE](LICENSE)).
