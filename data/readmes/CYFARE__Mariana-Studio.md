<p align="center">
  <img src="github-assets/banner.png" alt="Mariana — Into The Depths of AI's Ocean" width="100%">
</p>

<h1 align="center">Mariana Studio</h1>

<p align="center"><em>Into The Depths of AI's Ocean</em></p>

<p align="center">
  <a href="VERSION.txt"><img src="https://img.shields.io/badge/version-2.3.3-0b7285" alt="Version 2.3.3"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="License: AGPL-3.0"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-3776ab?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/devices-CUDA%20%7C%20XPU%20%7C%20MPS%20%7C%20CPU-555" alt="CUDA, XPU, MPS and CPU">
  <a href="https://github.com/CYFARE/Mariana-Studio/stargazers"><img src="https://img.shields.io/github/stars/CYFARE/Mariana-Studio?style=flat" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#backed-by-whitepapers">Whitepapers</a> ·
  <a href="#one-studio-the-whole-workflow">Workspaces</a> ·
  <a href="docs/README.md">Docs</a> ·
  <a href="https://github.com/CYFARE/Mariana-Studio/issues">Issues</a>
</p>

---

Mariana is a **one-stop research and development studio for language models**.
Train a compact byte-level hybrid diffusion–autoregressive model from scratch,
fine-tune local or Hugging Face checkpoints, chat with anything you can run,
build and schedule agents, code in an agentic IDE, evaluate, and export to GGUF,
ONNX or safetensors — from one local workspace.

Research you can run: every technique ships with a whitepaper, a runbook and
the code that implements it.

## Why Mariana

- **One workspace** — data, training, fine-tuning, chat, agents, IDE, evaluation
  and deployment behind a single local UI.
- **Research with receipts** — Sprint-DRV, SAINT, AXIOM, NCM and AML/AMP each
  have a dedicated whitepaper and runbook.
- **Small-GPU friendly** — automatic CUDA → Intel XPU → Apple MPS → CPU
  selection; measured up to 5.57× training throughput at ~61% less peak memory
  on an 8 GB consumer GPU.
- **Portable models** — lossless AR export to GGUF, ONNX and safetensors, ready
  for llama.cpp, Ollama or ONNX Runtime.
- **Local-first agents** — AML/AMP agent flows, swarms, schedules and a coding
  IDE with sandboxed abilities.

## Backed by whitepapers

| Paper | What it covers |
| --- | --- |
| [Sprint-DRV](docs/whitepapers/sprint-drv.md) | Single-pass hybrid training: one backbone forward for prefix-AR, diffusion, verifier and MTP, with the legacy two-pass baseline and measured throughput/memory. |
| [SAINT](docs/whitepapers/saint.md) | Adaptive hierarchical discrete/continuous thought memory: curricula, policy learning, ablations and honest limits. |
| [AXIOM](docs/whitepapers/axiom.md) | Connector algebra plus a domain-adaptive corpus codec: English operators, a lossless dictionary for any text and language, DNA/protein packing, an identity fallback, and the evaluation protocol. |
| [NCM](docs/whitepapers/ncm.md) | Multiscale residual VQ and parallel next-concept generation. |
| [AML and AMP](docs/whitepapers/aml-amp.md) | The portable agent document language and local HTTP/JSON runtime protocol. |

Each paper is a technical report for code in this repository; every measurement
states the hardware and protocol that produced it.

## One studio, the whole workflow

| Workspace | What it does |
| --- | --- |
| **Home** | Live GPU, memory, disk and job telemetry, recent work and quick actions. |
| **Models** | Discover and download checkpoints, GGUF/ONNX models, Hugging Face repos, Ollama and llama.cpp models, and OpenAI-compatible endpoints. |
| **Train** | Corpus inspection, Smart Options, Sprint-DRV/Legacy/NCM training, the AXIOM corpus codec, live loss, pause/save and a direct handoff to Chat. |
| **Fine-tune** | LoRA, final-layer or full fine-tuning for Mariana and Hugging Face models, with dataset discovery and a validated plan. |
| **Chat** | Persistent streaming chats with local or remote models, images and file previews, dictation, a context meter, and a leader-planned agent swarm or Solo mode. |
| **Agents** | Canvas-first AML/AMP agent designer with debugger, schedules, templates and live runs. |
| **IDE** | Agentic coding in project workspaces with skills, diagnostics, snapshots, revert and Ask/Edit/Auto modes. |
| **Deploy** | GGUF/ONNX/safetensors export, Ollama registration and an OpenAI-compatible local API. |

## Quick start

```bash
git clone https://github.com/CYFARE/Mariana-Studio.git && cd Mariana-Studio
python mariana.py setup                    # pyenv + .venv + PyTorch/NumPy, on any OS
# PERFORM SOURCE VENV ACTIVATE BEFORE RUNNING BELOW COMMANDS!
python mariana.py studio                   # open the studio
python mariana.py                          # smoke-test train on the built-in demo corpus
python -m mariana train --data corpus.txt  # train on your own text
python mariana.py update                   # update from the latest GitHub release
```

`setup` prefers [pyenv](https://github.com/pyenv/pyenv) (installing the
requested CPython line when it is missing) and always installs inside a virtual
environment, never into the system interpreter — so distributions that mark
Python as externally managed keep working. The `mariana.py` wrapper selects
`.venv` automatically, so activation is only needed for direct `pip`/`pytest`
commands (or set `MARIANA_NO_VENV=1` to keep the current interpreter). Use
`--device cpu|cuda|xpu` to pick a requirements profile and
`--extras export,data,finetune` for optional tool groups; every flag is
documented in [docs/setup.md](docs/setup.md).

Device selection is automatic — **CUDA → Intel XPU → Apple MPS → CPU** — with
per-device mixed precision; `--device cuda|xpu|mps|cpu` overrides. Smaller
CPU-only and Intel Arc installs use `requirements-cpu.txt` and
`requirements-xpu.txt`. **No checkpoints ship with the repository**;
`trained-model/` is created on demand and is git-ignored.

## Export

```bash
pip install -r requirements-export.txt
python -m mariana export --checkpoint trained-model/mariana.pt --format all --out exports
```

One command writes a LLaMA-architecture GGUF, an Ollama `Modelfile`, an ONNX
model and LLaMA-format safetensors. The AR path is lossless by construction and
verified by a numeric parity test. Runner commands and caveats are in
[docs/export.md](docs/export.md).

## Go deeper

| Topic | Read |
| --- | --- |
| Set up a new machine | [docs/setup.md](docs/setup.md) |
| Train, fine-tune or distill | [README_training.md](README_training.md) · [docs/distillation.md](docs/distillation.md) |
| Fine-tune on a 6-8 GB GPU | [docs/low-vram-finetuning.md](docs/low-vram-finetuning.md) |
| Sprint-DRV, SAINT, AXIOM and NCM runbooks | [docs/fast-training.md](docs/fast-training.md) · [docs/latent-language.md](docs/latent-language.md) · [docs/axiom.md](docs/axiom.md) · [docs/ncm.md](docs/ncm.md) |
| Agents and the coding IDE | [docs/agentic.md](docs/agentic.md) · [docs/ide.md](docs/ide.md) |
| Export and serve | [docs/export.md](docs/export.md) |
| Update the checkout | [docs/update.md](docs/update.md) |
| MoE + MTP + SAINT on a small GPU | [docs/low-vram.md](docs/low-vram.md) |
| Architecture and engineering standard | [architecture.txt](architecture.txt) · [AGENTS.md](AGENTS.md) |

The full index is [docs/README.md](docs/README.md).

## Tests

```bash
python -m pytest -q                 # complete CPU suite
python -m pyflakes mariana tests    # unused imports and undefined names
```

Optional backends skip cleanly when their packages are not installed.

## License and citation

Mariana is licensed under **AGPL-3.0**; see [LICENSE](LICENSE). If you use it in
your work, cite [CITATION.cff](CITATION.cff). Contributions follow
[CONTRIBUTING.md](CONTRIBUTING.md); security reports follow
[SECURITY.md](SECURITY.md).
