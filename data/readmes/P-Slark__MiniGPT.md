<p align="center">
  <img alt="LLM step by step" src="docs/logo.png" width="55%">
</p>

<h3 align="center">
What worked, what didn't, and why — a small LLM, end-to-end
</h3>

<p align="center">
| <a href="./JOURNEY.md"><b>Journey</b></a> |
<a href="https://stanford-cs336.github.io/"><b>CS336 (curriculum)</b></a> |
<a href="https://github.com/P-Slark/LLM-Step-by-Step/issues"><b>Issues</b></a> |
</p>

<p align="center">
<a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
<a href="https://www.python.org/"><img alt="Python 3.12+" src="https://img.shields.io/badge/python-3.12+-blue.svg"></a>
<a href="https://pytorch.org/"><img alt="PyTorch ~2.11" src="https://img.shields.io/badge/PyTorch-~2.11-red.svg"></a>
<img alt="Status: WIP" src="https://img.shields.io/badge/status-work%20in%20progress-yellow.svg">
</p>


## 👉 Two things to read

<table>
<tr>
<td width="50%" valign="top">

### 📖 [JOURNEY.md](./JOURNEY.md)

**The writing.** A chapter-by-chapter narrative of *what I tried, what was slow, and what each round of optimization actually bought me.* Each chapter maps to a commit. Most "build an LLM" tutorials show you the final code — this one shows the path.

If you only read **one** thing in this repo, read this.

</td>
<td width="50%" valign="top">

### 💻 [`cs336_basics/`](./cs336_basics/)

**The code.** Clean, dependency-light implementations of every piece: BPE tokenizer, RMSNorm/RoPE/SwiGLU/MHA, AdamW, cosine LR schedule, gradient clipping, training loop, sampling.

Read alongside JOURNEY.md. Each module is short and meant to be read top-to-bottom.

</td>
</tr>
</table>

Everything else in the repo (`scripts/`, `tests/`, fixtures, the assignment PDF) is scaffolding around those two things.

---

The curriculum is borrowed from Stanford's [CS336](https://stanford-cs336.github.io/)
("Language Models from Scratch").

## About

- **🧱 Built from PyTorch primitives, not framework abstractions.** No `torch.nn.Transformer`, no HuggingFace, no `transformers` library, no pre-trained weights. Every layer, optimizer, and training step is written from scratch in this repo — autograd and tensor ops are the only things borrowed.
- **📖 A step-by-step journey, not just code.** [JOURNEY.md](./JOURNEY.md) walks through *what was tried, what was slow, and what each round of optimization actually bought* — chapter by chapter, commit by commit. Most "build an LLM" repos hand you the final code. This one shows the path.

## What's in here

| Part | Topic | Code | Journey chapter |
|---|---|---|---|
| I  | BPE tokenizer (train + encode/decode, parallel + incremental) | `cs336_basics/bpe.py`, `tokenizer.py` | [Iterations 1–4](./JOURNEY.md#iteration-1) |
| II | Transformer model (RMSNorm, RoPE, SwiGLU, MHA, tied embeddings) | `cs336_basics/model.py` | [Part II](./JOURNEY.md#part-ii--transformer-building-blocks) |
| III | Training building blocks (cross-entropy, AdamW, cosine LR, grad clip) | `cs336_basics/optim.py`, `training.py`, `nn_utils.py` | [Part III](./JOURNEY.md#part-iii--training) |
| IV | Training loop (data loader, checkpointing, `scripts/train.py`) | `cs336_basics/data.py`, `scripts/` | [Part IV](./JOURNEY.md#part-iv--training-loop) |
| V  | Text generation (temperature, top-k, top-p, EOS stopping) | `cs336_basics/decoding.py`, `scripts/generate.py` | [Part V](./JOURNEY.md#part-v--text-generation) |

## Quickstart

```sh
# Install (uses uv for env management)
pip install uv
uv sync

# Run the unit tests
uv run pytest

# Download TinyStories
mkdir -p data && cd data
wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-train.txt
wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-valid.txt
cd ..

# Train a BPE tokenizer, encode the corpus, train a small model, generate text
# (see JOURNEY.md for the full pipeline)
uv run scripts/encode_corpus.py --help
uv run scripts/train.py --help
uv run scripts/generate.py --help
```


## Credits & honest scope

The curriculum, the spec, and the test fixtures all come from Stanford's
CS336 ("Language Models from Scratch"), which generously publishes its
materials online. All the implementations and the writing in JOURNEY.md
are mine. If you're a current CS336 student, please respect your course's
collaboration policy — this repo is a learning log, not a copy-paste solution.

The original assignment scaffolding (handout PDF, test adapters,
submission script) lives under [`assignment/`](./assignment/).
