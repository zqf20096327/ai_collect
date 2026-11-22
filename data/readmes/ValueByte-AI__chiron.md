<div align="center">

<h1>A Foundation Model<br>to Measure and Predict Human Behaviour</h1>

<p><strong>Chiron</strong> · Psychological measurement, behavioural prediction, and population simulation</p>

<p>
<a href="https://www.alphaxiv.org/abs/2611.24830"><img src="https://img.shields.io/badge/alphaXiv-2611.24830-9A2036?logo=alphaXiv&logoColor=white" height="26" alt="alphaXiv"></a>
<a href="https://huggingface.co/chiron-group/chiron"><img src="assets/badges/model.svg" height="26" alt="Hugging Face model"></a>
<a href="https://huggingface.co/datasets/chiron-group/chiron-data"><img src="assets/badges/data.svg" height="26" alt="Hugging Face data"></a>
<a href="pyproject.toml"><img src="assets/badges/python.svg" height="26" alt="Python 3.12"></a>
<a href="pyproject.toml"><img src="assets/badges/pytorch.svg" height="26" alt="PyTorch 2.11"></a>
</p>

<p>
<a href="#overview">Overview</a> ·
<a href="#quick-start">Quick start</a> ·
<a href="#training">Training</a> ·
<a href="#evaluation">Evaluation</a> ·
<a href="#citation">Citation</a>
</p>

</div>

<p align="center">
<a href="assets/figures/headline-results.pdf"><img src="assets/figures/headline-results.png" width="1000" alt="Chiron's training and evaluation coverage, shared model, and comparisons for measurement, prediction and population simulation"></a>
</p>

<p align="center"><sub>Training and evaluation coverage and main comparisons from the manuscript.</sub></p>

## Overview

Chiron jointly learns to measure psychological attributes, predict individual behaviour and reproduce population response distributions. A shared language model represents personal evidence, while a dedicated measurement head reads construct scores from that representation.

| Task | Input | Output |
| --- | --- | --- |
| Psychological measurement | A person's records | Scores for 109 predefined constructs |
| Behavioural prediction | Personal records and a new question | Predicted responses or choices |
| Population simulation | Experimental context and questions | Sampled respondent-level answers |

<p align="center">
<a href="assets/figures/architecture.pdf"><img src="assets/figures/architecture.png" width="1000" alt="Joint training of Chiron with measurement supervision, held-out behavioural responses and population evidence"></a>
</p>

<details>
<summary><strong>A controlled example: daily records, construct scores and behavioural predictions</strong></summary>

<p align="center">
<a href="assets/figures/controlled-example.pdf"><img src="assets/figures/controlled-example.png" width="1000" alt="Four levels of structured daily habits, their construct readouts, and corresponding vocational-interest and future-orientation predictions"></a>
</p>

Changing the supplied daily-habit records produces coordinated changes in construct scores and predictions. This illustrative case concerns an intervention on model inputs; it does not establish a human causal mechanism or isolate the effect of measurement supervision.

</details>

## Quick start

Use Linux x86-64, Python 3.12 and [uv](https://docs.astral.sh/uv/getting-started/installation/) 0.11 or later, with sufficient GPU memory for the 35B base model. Python is selected by `.python-version`; package versions and sources are recorded in `uv.lock`.

```bash
git clone https://github.com/ValueByte-AI/chiron.git
cd chiron
uv python install 3.12
export UV_PROJECT_ENVIRONMENT=.venv-inference
uv sync --locked --extra inference
```

`uv sync` installs Python packages, not model weights. The first `Chiron.from_pretrained("chiron-group/chiron")` call downloads the Chiron adapter and measurement head, then loads the base model named in the adapter configuration: `Qwen/Qwen3.6-35B-A3B`. Its weights and tokenizer are downloaded if they are not already cached. Subsequent calls reuse cached files for the same model revision.

If a Hugging Face repository requires access, authenticate with `uv run --locked --extra inference hf auth login`. Run Python scripts through `uv run --locked --extra inference python`.

```python
from chiron import Chiron

model = Chiron.from_pretrained("chiron-group/chiron")
records = [
    "I make a plan before starting a project and keep track of its deadlines.",
    "When a task becomes difficult, I usually keep working until it is finished.",
]
print(model.measure(records, constructs=["conscientiousness"]))
```

`measure` returns a dictionary of construct scores. Omit `constructs` to return all 109; `model.constructs` lists their names. The head is trained against targets on −1 to 1, and its predictions can extend beyond that range.

### Behavioural prediction

Prediction and population sampling use the vLLM service described under [Serving](#serving).
After starting it, connect from the inference environment. A single-question example:

```python
from chiron import Chiron

model = Chiron.from_server("http://127.0.0.1:8000/v1")
records = [
    "I make a plan before starting a project and keep track of its deadlines.",
    "When a task becomes difficult, I usually keep working until it is finished.",
]
record_context = "Below are records describing this person."
questions = [
    'How would this person rate "I finish tasks on time"?\n'
    "Option 1: Disagree\nOption 2: Neither agree nor disagree\nOption 3: Agree"
]
print(model.predict(
    record_context=record_context,
    observations=records,
    questions=questions,
))
```

`predict` returns generated answer text. Its fixed template presents `record_context`, `observations` and `questions` in that order. Generation uses temperature 0, thinking disabled and a default answer limit of 128 tokens. The service accepts up to 8,192 tokens including the answer.

Multiple questions can share a response scale, as in this shortened IPIP-FFM evaluation example:

```python
# Shortened IPIP-FFM evaluation example: two targets sharing one response scale.
record_context = (
    "Below are self-report questionnaire responses from one respondent on the IPIP-FFM scale."
)
observations = [
    "Item: I worry about things | Response: Agree",
    "Item: I start conversations | Response: Agree",
    "Item: I don't mind being the center of attention | Response: Neutral",
    "Item: I take time out for others | Response: Agree",
]
questions = (
    "Use this response scale for every question below:\n"
    "Option 1: Disagree\nOption 2: Slightly disagree\nOption 3: Neutral\n"
    "Option 4: Slightly agree\nOption 5: Agree\n\n"
    "Rate each statement for this person:\n"
    'Q1. "I am not interested in abstract ideas"\n'
    'Q2. "I get irritated easily"'
)
print(model.predict(
    record_context=record_context,
    observations=observations,
    questions=questions,
))
```

The model returns one completion with answers numbered `Q1`, `Q2`, and so on, in question order. Lists receive automatic question numbering; a string preserves an already formatted question block.

Transformers/PyTorch generation is also supported: load with `Chiron.from_pretrained(...)` and use the same `predict` and `simulate_population` arguments.

To use existing local weights:

```python
model = Chiron.from_pretrained(
    "models/chiron",
    base_model="models/qwen3.6-35b-a3b",
)
```

Run measurement locally, or run the prediction examples after starting the vLLM service:

```bash
uv run --locked --extra inference python examples/measurement.py
uv run --locked --extra inference python examples/prediction.py
```

### Population simulation

[examples/population.py](examples/population.py) runs the two company-hierarchy conditions from study OBHDP_10_1b, using the experimental wording, three items, seven response options, and 103 and 99 respondents used in the paper.

```bash
uv run --locked --extra inference python examples/population.py
```

Connect with `Chiron.from_server(...)`. `simulate_population` accepts `participant_context`, `experimental_setting`, `questions` and `n_respondents`. Each question contains `text` and an ordered list of `options`. vLLM generates all respondents for a condition in one request, using temperature 1, top-p 1, top-k disabled, thinking disabled and constrained `Q1: Option …` responses. The default token budget is `8 * len(questions) + 16`. Results contain `raw_output` and one-based `option_ids`, ordered by respondent index.

`seed` is the condition-level random seed. The example uses 20261154 and 20261155 for conditions A and B, matching the evaluation. The default is 20260902; the paper adds each condition's original evaluation index. Transformers uses the same prompt and sampling rules, with respondents generated sequentially. Random samples can differ between backends.

## Training

Use a separate shell and environment for training. The training profile uses CUDA 12.8 PyTorch wheels and the bundled LLaMA-Factory source. Building FlashAttention requires a CUDA 12.8 development toolkit and a C++ compiler; make `nvcc` available on `PATH` or set `CUDA_HOME` to the toolkit installation. uv supplies the GPU extensions' build dependencies and matches their build-time PyTorch to the training runtime.

Run commands from the repository root:

```bash
export UV_PROJECT_ENVIRONMENT=.venv-train
uv sync --locked --extra train
uv run --locked --extra train hf download chiron-group/chiron-data --repo-type dataset --local-dir chiron-data
uv run --locked --extra train hf download Qwen/Qwen3.6-35B-A3B --local-dir models/qwen3.6-35b-a3b
```

Prepare the source datasets following the [data instructions](https://huggingface.co/datasets/chiron-group/chiron-data/tree/main/data/raw). The complete training mixture requires locally obtained restricted sources; the distributed subset alone is insufficient. Each source retains its own licence and access requirements.

Data preparation uses the dataset repository's own `requirements.txt`, separately from the model environment:

```bash
uv run --no-project --python 3.12 --with-requirements chiron-data/requirements.txt \
  python chiron-data/code/prediction/build_prediction.py
uv run --no-project --python 3.12 --with-requirements chiron-data/requirements.txt \
  python chiron-data/code/measurement/build_human_gold.py
uv run --no-project --python 3.12 --with-requirements chiron-data/requirements.txt \
  python chiron-data/code/build_joint_training.py
uv run --locked --extra train torchrun --nproc_per_node=4 scripts/train_joint.py
```

The two-epoch recipe is in [configs/train_joint.yaml](configs/train_joint.yaml); checkpoints are saved to `outputs/joint/`. The measurement head saves its centring mean for inference. `chiron_person_mean_ema.pt` also stores the update count and rate for training resumption. The customized backend is included in [LLaMA-Factory/](LLaMA-Factory/) under its Apache-2.0 licence.

## Evaluation

The manuscript evaluates psychological measurement, prediction across 29 behavioural domains and population simulation across 15 held-out studies. The [data repository](https://huggingface.co/datasets/chiron-group/chiron-data#evaluation) provides frozen evaluation inputs, source instructions and reconstruction scripts.

Distributed evaluation files omit restricted-domain records. Their subset scores should not be compared directly with the paper's full-set aggregates. Follow the source-specific instructions to reconstruct the complete evaluation locally. Paper-specific evaluation outputs, baseline and reporting scripts are available upon request.

## Serving

<details>
<summary><strong>vLLM prediction and population server</strong></summary>

Use a separate shell and environment for vLLM. Its official 0.21.0 wheels target CUDA 13.0, so the serving profile selects matching PyTorch, TorchVision and TorchAudio wheels. A compatible NVIDIA driver is required. Inference and training use CUDA 12.8; `serve` cannot be combined with either extra.

```bash
export UV_PROJECT_ENVIRONMENT=.venv-serve
uv sync --locked --extra serve
uv run --locked --extra serve hf download Qwen/Qwen3.6-35B-A3B --local-dir models/qwen3.6-35b-a3b
uv run --locked --extra serve hf download chiron-group/chiron --local-dir models/chiron
CUDA_VISIBLE_DEVICES=0,1 uv run --locked --extra serve python scripts/serve.py
```

The server applies the LoRA update in FP32 while loading the base weights, then runs BF16 inference. This is the loading path used in the prediction and population experiments. `--base-model`, `--checkpoint` and `--port` can select existing local weights or a different port.

In a separate inference shell, connect with `Chiron.from_server("http://127.0.0.1:8000/v1")`. The public methods fill the fixed prompts and request settings. Measurement continues to use `Chiron.from_pretrained(...).measure(...)` through Transformers/PyTorch; run it separately or allocate distinct GPUs.

</details>

## Development

The tests cover both the inference package and training backend. Use the compatible training and inference extras together, with the test dependency group:

```bash
export UV_PROJECT_ENVIRONMENT=.venv-train
uv sync --locked --extra train --extra inference --group test
uv run --locked --extra train --extra inference --group test pytest -q
uv lock --check
uv build --wheel --no-sources
```

After changing dependencies in `pyproject.toml`, run `uv lock` and commit both files. Keep the selected extras on `uv run` commands so that uv synchronizes the intended profile. Model checkpoints are managed separately by Hugging Face and are not pinned by the Python lockfile.

## Repository layout

| Path | Contents |
| --- | --- |
| `chiron/inference.py` | Model loading, fixed prompts and inference |
| `chiron/sitecustomize.py` | Adapter loading for the vLLM server |
| `examples/` | Measurement, prediction and population examples |
| `scripts/train_joint.py` | Joint training entry point |
| `scripts/serve.py` | vLLM prediction and population server |
| `configs/` | Training settings |
| `pyproject.toml`, `uv.lock`, `.python-version` | Environment profiles, locked dependencies and Python version |
| `LLaMA-Factory/` | Customized training backend |
| `assets/figures/` | Paper figures, web previews and source hashes |

## Citation

If you use Chiron in your research, please cite:

```bibtex
@misc{ye2026foundationmodelmeasurepredict,
      title={A Foundation Model to Measure and Predict Human Behaviour},
      author={Haoran Ye and Tianrui Huo and Hangzhen Li and Xin Zhang and Guojie Song},
      year={2026},
      eprint={2611.24830},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2611.24830},
}
```
