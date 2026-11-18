<p align="center">
  <img alt="astro-weights logo: astronaut with a gold visor and a violet chest patch" src="https://raw.githubusercontent.com/astro-weights/astro-weights/main/docs/assets/logo.svg" width="120" height="120">
</p>

<h1 align="center">astro-weights</h1>

<p align="center"><b>Small course corrections for open LLMs.</b><br>Agent-driven weight edits. Democratizing AI for all.</p>

<p align="center">
  <a href="https://pypi.org/project/astro-weights/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/astro-weights"></a>
  <a href="https://pypi.org/project/astro-weights/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/astro-weights"></a>
  <a href="https://github.com/astro-weights/astro-weights/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/astro-weights/astro-weights/actions/workflows/ci.yml/badge.svg"></a>
</p>

<p align="center">
  <a href="https://astro-weights.dev/docs/">Docs</a> ·
  <a href="https://pypi.org/project/astro-weights/">PyPI</a> ·
  <a href="https://github.com/astro-weights/astro-weights/blob/main/CHANGELOG.md">Changelog</a> ·
  <a href="https://github.com/astro-weights/astro-weights/blob/main/CONTRIBUTING.md">Contributing</a>
</p>

The goal is an agent that proposes small, targeted low-rank edits to a model's weights and keeps the ones that hold up under paired tests, saved as plain PEFT LoRA adapters. The agent loop is not here yet. What the library ships today is the toolkit that loop needs:

- Edits: build low-rank edits from numpy recipes, rebuild one from a recipe file (`astro-weights build`), or convert a dense update with `from_dense`.
- Export: save and load edits as hash-checked LoRA adapters, write a GGUF adapter for llama.cpp, and write a Hugging Face model card.
- Runners: apply edits to transformers models and remove them again, and generate eval records from a local model or an OpenAI-compatible endpoint.
- Directions: difference-of-means directions with a split-half gate.
- Eval: graders and paired comparison of a base arm and an edit arm.

LoRA is the output format because every serving stack already loads it (transformers, PEFT, vLLM, llama.cpp and the rest), so an edit needs no custom runtime: ship the adapter, load it like any other, and drop it to get the base model back.

> **Status: pre-alpha.** The API will change without notice until 1.0.

## Install

```bash
pip install astro-weights
```

To apply edits to transformers models, add the `hf` extra (pulls in torch, transformers and peft):

```bash
pip install "astro-weights[hf]"
```

## Quick look

Build a rank-1 edit with numpy and save it as a LoRA adapter:

```python
import numpy as np
from astro_weights.edits import Edit, masked_rank1
from astro_weights.export import save_peft

W0 = np.random.default_rng(0).standard_normal((16, 48), dtype=np.float32)
u = np.eye(16, dtype=np.float32)[0]
mask = np.ones(48, dtype=np.float32)
delta = masked_rank1("model.layers.1.mlp.down_proj", W0, u, mask, alpha=0.5)
save_peft(Edit(deltas=(delta,), base_model="org/name"), "my-edit")
```

Summarize and verify the saved adapter:

```bash
astro-weights inspect my-edit
```

To apply an edit to a real model, build it from that model's own weights; the edit above is random and 16x48, so it matches no real model. [Tutorial: first edit](https://astro-weights.dev/docs/tutorials/first-edit/) does this end to end on a small model that runs on CPU. Once you have an adapter built for your base model, apply and remove it like this (`hf` extra):

```python
from transformers import AutoModelForCausalLM

from astro_weights.export import load_peft
from astro_weights.runners.hf import apply, remove

edit = load_peft("my-adapter")  # an adapter built for its base model
model = AutoModelForCausalLM.from_pretrained(edit.base_model)
peft_model = apply(model, edit)
model = remove(peft_model)  # base weights were never modified
```

`apply` also finds layers named differently, as in text-only and multimodal loads of one checkpoint: see [How-to: apply across model classes](https://astro-weights.dev/docs/how-to/apply-across-model-classes/).

## Agent over MCP (0.2)

The agent loop is new in 0.2 (`pip install "astro-weights[mcp,hf]"`). `astro-weights mcp RUN_DIR` serves the agent tools over stdio MCP, with a budget and an OS sandbox, to Claude Code or any MCP client (the Codex setup is documented but not tested). `astro-weights run CONFIG` runs a whole edit session with a built-in editor: scripted, a local model or Claude on your own key. Start with [Tutorial: first agent run](https://astro-weights.dev/docs/tutorials/first-agent-run/).

## Development

```bash
git clone https://github.com/astro-weights/astro-weights
cd astro-weights
uv sync
uv run pytest
```

See [CONTRIBUTING.md](https://github.com/astro-weights/astro-weights/blob/main/CONTRIBUTING.md) for the full set of checks and how to send a pull request.

## Citation

If you use astro-weights in your work, please cite it. The metadata is in [CITATION.cff](https://github.com/astro-weights/astro-weights/blob/main/CITATION.cff); on GitHub, use **Cite this repository** in the sidebar.

## License

[Apache-2.0](https://github.com/astro-weights/astro-weights/blob/main/LICENSE).

The logo is based on the Noto Emoji "person astronaut" glyph, Copyright Google LLC, Apache-2.0. See [docs/assets/LOGO-LICENSE.md](https://github.com/astro-weights/astro-weights/blob/main/docs/assets/LOGO-LICENSE.md).
