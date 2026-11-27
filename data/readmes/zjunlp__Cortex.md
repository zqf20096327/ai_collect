<h1 align="center">🧠 Cortex</h1>
<p align="center"><b>Consolidating Context into Parametric Memory</b></p>

<p align="center">
  <a href="https://arxiv.org/abs/2610.20399">📄 arXiv</a> ·
  <a href="https://huggingface.co/papers/2610.20399">🤗 HF Paper</a> ·
  <a href="https://huggingface.co/collections/zjunlp/cortex">🤗 HF Collection</a> ·
  <a href="https://x.com/zxlzr/status/2110619174917534034">𝕏 Announcement</a>
</p>

Cortex turns context into model memory. It generates supervision from knowledge, instructions, or agent experience, consolidates that supervision into model parameters, and evaluates both the learned capability and the capabilities to retain.

The Python package, **`mc`**, connects experience data, consolidation methods, model backends, and evaluators through a common workflow.

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Experience Data](#experience-data)
- [Evaluation](#evaluation)
- [Continual Consolidation](#continual-consolidation)
- [Data Preparation](#data-preparation)
- [Citation](#citation)

## Overview

<p align="center">
  <img src="assets/figure1.png" alt="Figure 1: biological systems consolidation and memory consolidation in language models." width="100%">
</p>

*Figure 1. Biological inspiration and the memory consolidation objective.*

1. **Prepare an experience.** Supply the context to learn, optional training tasks, and references to target (`q_plus`) and retention (`q_minus`) evaluations.
2. **Consolidate the context.** Cortex generates questions and answers or collects agent rollouts, then trains an adapter with cross-entropy, logit distillation, or hidden-state matching. Each update can use one experience or a batch; repeated updates on the same method support continual learning.
3. **Evaluate the updated model.** Pass `method.backend()` and the experiences to `evaluate()`. Each evaluator runs its tasks and scores the results, using an agent for chat or environment interaction.

## Installation

Create a Python 3.11+ environment and install the training dependencies:

```bash
git clone https://github.com/zjunlp/cortex.git
cd cortex

conda create -n cortex python=3.11 -y
conda activate cortex
pip install torch transformers accelerate safetensors openai
pip install git+https://github.com/huggingface/peft.git
```

Run the following Python examples from the repository root. For Code evaluation, install the task's Python package in the execution environment. ALFWorld and Tau2 use their respective SDKs and environment data.

## Quick Start

This example consolidates one factual edit from the bundled ZsRE experiences into a Qwen model using LoRA.

```python
from peft import LoraConfig
from transformers import TrainingArguments

from mc import consolidate, load_experiences
from mc.methods.cortex import CortexMethod, LossConfig

model_name = "Qwen/Qwen3-4B-Thinking-2507"
experiences = load_experiences("data/experiences/zsre/experiences.jsonl")[:1]

method = CortexMethod(
    model_name,
    device="cuda",
    dtype="bfloat16",
    work_dir="outputs/zsre",
    adapter_config=LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["gate_proj", "up_proj", "down_proj"],
        task_type="CAUSAL_LM",
    ),
    loss=LossConfig(kl_weight=1.0, mse_weight=1.0),
    training_args=TrainingArguments(
        output_dir="outputs/zsre/train",
        learning_rate=5e-4,
        num_train_epochs=1,
        per_device_train_batch_size=1,
        bf16=True,
        report_to="none",
    ),
    question_task="zsre",
    num_questions=8,
    generation={"max_new_tokens": 2048, "temperature": 0.7},
)

consolidate(method, experiences)
method.save("outputs/zsre/saved")

reply = method.backend().generate(
    [{"role": "user", "content": "When was Karstadt founded?"}],
    config={"max_new_tokens": 2048, "temperature": 0},
)
print(reply["content"])
method.close()
```

`consolidate()` prepares the method input from each Experience and runs the update. Use `method.backend()` for inference and evaluation. Set `model_path` and `tokenizer_path` when using local model files.

Load a saved method to continue inference or consolidation:

```python
from mc.methods.cortex import CortexMethod

method = CortexMethod.load("outputs/zsre/saved", device="cuda")
backend = method.backend()
```

## Experience Data

Store experiences as JSONL, with one context per line. Evaluation questions and reference answers live in separate task files.

For example, a record in `data/experiences/zsre/experiences.jsonl` has this structure:

```json
{
  "id": "edit/000",
  "context": "Karstadt came into being in 1902.",
  "q_plus": [{
    "evaluator": "zsre",
    "source": "target.jsonl",
    "ids": ["edit/000/src", "edit/000/rephrase", "edit/000/portability"]
  }],
  "q_minus": [
    {"evaluator": "zsre", "source": "locality.jsonl", "ids": ["edit/000/locality"]},
    {"evaluator": "mmlu", "source": "../../tasks/mmlu.jsonl"}
  ],
  "meta": {"subject": "Karstadt"}
}
```

| Field | Description |
|---|---|
| `id` | A unique identifier within the experiment. |
| `context` | The knowledge, instructions, or experience to consolidate. |
| `support` | Optional training tasks or environment tasks, selected from the `train` split. |
| `q_dev` | Optional development evaluations, selected from the `dev` split. |
| `q_plus` | Target evaluations on the `test` split. |
| `q_minus` | Retention evaluations on the `test` split. |
| `model_names` | Optional list of base models the experience applies to. |
| `meta` | Additional information available to the method, such as a package name or subject. |

Each task reference chooses an `evaluator`, an optional data `source`, optional task `ids`, and evaluator `options`. Relative sources are resolved from the experience file's directory. Omitting `ids` selects every task in the requested split. Several experiences can share the same retention dataset through their `q_minus` references.

The method receives `id`, `context`, `support`, and `meta`; the evaluator receives the evaluation references. Custom experiences can also be created directly:

```python
from mc import Experience

experience = Experience(
    id="my-experience",
    context="Your knowledge or instructions to consolidate.",
    meta={"generation_task": "general"},
)
```

Bundled experience domains include **Code, ZsRE, Steering, RWKU, ALFWorld, and Tau2**. Shared evaluation data includes **MMLU, SimpleQA, GSM8K, MATH500, and AIME26**.

Data is organized into two directories:

- [`data/experiences/`](data/experiences/): domain contexts and their associated target and retention tasks. Each `experiences.jsonl` stores multiple experiences; `experiences.<model>.jsonl` stores model-specific contexts.
- [`data/tasks/`](data/tasks/): shared evaluation datasets that any experience can reference.

RWKU, ALFWorld, and Tau2 include model-specific contexts. Select the experience file for the base model being consolidated; `model_names` records that compatibility. Code, ZsRE, and Steering provide shared contexts.

Each task file uses JSONL with `id`, `split`, `input`, `reference`, and optional `meta`. For example:

```json
{
  "id": "addition/001",
  "split": "test",
  "input": {
    "messages": [{"role": "user", "content": "What is 2 + 3?"}]
  },
  "reference": {"answer": "5"}
}
```

The evaluator defines the contents of `input` and `reference`. Chat inputs contain messages; environment inputs contain an `input.native` task description used by the agent's SDK. Reference answers remain on the scoring side. The bundled tasks use the `test` split; add separate `train` or `dev` records for support or development evaluation.

Validate the data and references with `python scripts/check_data.py`.

## Evaluation

`evaluate()` reads an Experience's Q+ and Q− references, runs their evaluators, and returns a report. Generation settings, batch size, and repeated runs are configured with `EvalConfig`.

For the ZsRE example, configure `JUDGE_MODEL`, `JUDGE_BASE_URL`, and `JUDGE_API_KEY` for an OpenAI-compatible judge service, then evaluate the loaded method:

```python
import json
import os

from mc import evaluate, load_experiences
from mc.backends import OpenAIBackend
from mc.evaluators import EvalConfig

experiences = load_experiences("data/experiences/zsre/experiences.jsonl")[:1]
judge = OpenAIBackend(
    model_name=os.environ["JUDGE_MODEL"],
    base_url=os.environ["JUDGE_BASE_URL"],
    api_key=os.environ["JUDGE_API_KEY"],
    generation={"temperature": 0, "max_tokens": 128},
)

report = evaluate(
    method.backend(),
    experiences,
    config=EvalConfig(
        generation={"max_new_tokens": 2048, "temperature": 0},
        batch_size=4,
        repeat=1,
        seed=42,
    ),
    evaluator_options={"zsre": {"judge": judge}},
    out_dir="outputs/zsre/evaluation",
)
print(json.dumps(report["summary"], indent=2))
judge.close()
method.close()
```

Results are saved to **`outputs/zsre/evaluation/report.json`**:

- `config`: model and evaluation settings.
- `summary`: metrics for each experience, evaluation role, and task reference.
- `records`: individual responses or trajectories and their scores.

Use `phase="dev"` to evaluate `q_dev`. For repeated sampling, increase `repeat` and set the sampling parameters in `generation`.

| Task family | Evaluators |
|---|---|
| Knowledge and reasoning | MMLU, SimpleQA, GSM8K, MATH500, AIME26, BBH, TriviaQA, TruthfulQA |
| Knowledge editing and forgetting | ZsRE, RWKU |
| Behavioral steering | PowerSeeking, Psychopathy |
| Code | Generated Python programs scored against task tests |
| Agent environments | ALFWorld, Tau2 |

Evaluators select the agent and scoring procedure. Chat tasks use `ChatAgent`; ALFWorld manages game interaction; Tau2 uses the official SDK's agent and orchestrator. A custom evaluator can be referenced as `"my_package.evaluation:MyEvaluator"`.

### Base and context baselines

Use a `TransformersBackend` for the base model, or wrap it in `PromptMethod` to evaluate with the experience context in the prompt:

```python
from mc import consolidate
from mc.backends import TransformersBackend
from mc.methods import PromptMethod

base = TransformersBackend(model_name, device="cuda", dtype="bfloat16")
prompt = PromptMethod(base)
consolidate(prompt, experiences)

base_backend = base
context_backend = prompt.backend()
```

Pass either backend to `evaluate()` with the same experiences and scoring configuration. After evaluation, close `prompt` and `base`.

## Continual Consolidation

Keep the same method instance across updates. Each call accepts a batch of experiences, so successive batches can have different sizes:

```python
from peft import LoraConfig
from mc import consolidate, load_experiences
from mc.methods.cortex import CortexMethod

experiences = load_experiences("data/experiences/zsre/experiences.jsonl")[:5]
method = CortexMethod(
    "Qwen/Qwen3-4B-Thinking-2507",
    device="cuda",
    dtype="bfloat16",
    work_dir="outputs/continual",
    adapter_config=LoraConfig(
        r=8, lora_alpha=16,
        target_modules=["gate_proj", "up_proj", "down_proj"],
        task_type="CAUSAL_LM",
    ),
    question_task="zsre",
    reuse_adapter=False,
)

for step, batch in enumerate([experiences[:2], experiences[2:]]):
    consolidate(method, batch)
    method.save(f"outputs/continual/step-{step}")

method.close()
```

`reuse_adapter=True` updates the existing adapter. `False` adds one adapter per call while keeping earlier adapters active and frozen. `teacher_source="base"` prepares supervision with the base model; `"current"` uses the model after its previous updates. Evaluate each saved stage on the experiences accumulated so far to measure learning and retention.

## Data Preparation

Data preparation and training can run separately:

```python
from mc import load_experiences
from mc.methods.cortex import CortexMethod

method = CortexMethod.load("outputs/zsre/saved", device="cuda")
experiences = load_experiences("data/experiences/zsre/experiences.jsonl")[:1]
inputs = [
    exp.to_consolidation_input(model_name=method.model_name)
    for exp in experiences
]
prepared_dir = method.prepare(inputs)
training_report = method.train(prepared_dir)
method.close()
```

The prepared directory stores raw records, filtering decisions, aligned training tokens, and teacher targets. Calling `train(prepared_dir)` reuses those targets.

For existing question-answer pairs or agent rollouts, pass `records="path/to/records.jsonl"` to `prepare()`. These records use [`TrainingRecord`](mc/methods/cortex/data.py). Agent support tasks are rolled out through their evaluator's training split; the agent handles the environment and conversation loop.

Customize collection with `generator(inputs, teacher, *, generation, seed) -> GeneratedData`, and filtering with `checker(records, result) -> bool`. Both are ordinary Python callables passed to `CortexMethod`. The provided teacher records model calls and their generated token IDs. Task-specific question prompts live in [`prompts.py`](mc/methods/cortex/prompts.py); `question_backend` can supply a separate model for generating questions.

## Citation

If you use Cortex in your research, please cite our [paper](https://arxiv.org/abs/2610.20399):

```bibtex
@misc{zhang2026cortex,
  title         = {Cortex: Consolidating Context into Parametric Memory},
  author        = {Jintian Zhang and Feng He and Xinnian Liang and Ziwen Xu and
                   Haoming Xu and Haojing Huang and Shuangzhi Wu and Ningyu Zhang},
  year          = {2026},
  eprint        = {2610.20399},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2610.20399}
}
```
