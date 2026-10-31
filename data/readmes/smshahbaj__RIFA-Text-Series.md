# RIFA Text Series

### Efficient. Capable. Yours.

A **family of small language models** for text and code — open weights on Hugging Face, documentation hub on GitHub.

[![Hugging Face Collection](https://img.shields.io/badge/Hugging%20Face-Collection-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/collections/smshahbaj/rifa-text-series)
[![Models](https://img.shields.io/badge/models-5-blue)](https://huggingface.co/collections/smshahbaj/rifa-text-series)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.6084%2Fm9.figshare.33941830-blue.svg)](https://doi.org/10.6084/m9.figshare.33941830)

---

## Start here

| Resource | Link |
|----------|------|
| **All weights (collection)** | [https://huggingface.co/collections/smshahbaj/rifa-text-series](https://huggingface.co/collections/smshahbaj/rifa-text-series) |
| **Author profile** | [@smshahbaj](https://huggingface.co/smshahbaj) |
| **This docs hub** | you are here |

Weights are **not** stored in git. This repo explains the series and how to run each model.

---

## Model lineup

| Model | Params | Role | Best for | Weights |
|-------|--------|------|----------|---------|
| **[Rifa-Nano](docs/models/rifa-nano.md)** | 0.5B | Ultra-small general text | Prototyping, edge devices, lowest memory footprint | [`smshahbaj/Rifa-Nano-0.5B`](https://huggingface.co/smshahbaj/Rifa-Nano-0.5B) |
| **[RIFA-CODE](docs/models/rifa-code.md)** | 0.6B | Code-oriented small model | Completion, short scripts, code helpers on limited hardware | [`smshahbaj/RIFA-CODE-0.6B`](https://huggingface.co/smshahbaj/RIFA-CODE-0.6B) |
| **[RIFA-Edge](docs/models/rifa-edge.md)** | 0.6B | Edge / on-device friendly text | On-device or CPU-first text generation | [`smshahbaj/RIFA-Edge-0.6B`](https://huggingface.co/smshahbaj/RIFA-Edge-0.6B) |
| **[RIFA-FLASH](docs/models/rifa-flash.md)** | 1.7B | Balanced speed and quality | Interactive chat and general tasks with better quality than Nano/Edge | [`smshahbaj/RIFA-FLASH-1.7B`](https://huggingface.co/smshahbaj/RIFA-FLASH-1.7B) |
| **[RIFA-PRO](docs/models/rifa-pro.md)** | 3B | Highest quality in the series | When quality matters more than minimum latency/memory | [`smshahbaj/RIFA-PRO-3B`](https://huggingface.co/smshahbaj/RIFA-PRO-3B) |

## Which model should I use?

| If you need... | Pick |
|----------------|------|
| Smallest footprint | **Rifa-Nano** (0.5B) |
| Code-oriented help | **RIFA-CODE** (0.6B) |
| On-device / CPU-first text | **RIFA-Edge** (0.6B) |
| Balanced chat quality | **RIFA-FLASH** (1.7B) |
| Best quality in this family | **RIFA-PRO** (3B) |


---

## Quick start

```bash
pip install -r requirements-examples.txt
# or: pip install "transformers>=4.40" accelerate torch
```

**Quality default (PRO):**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "smshahbaj/RIFA-PRO-3B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else None,
)
```

**Smallest default (Nano):** `smshahbaj/Rifa-Nano-0.5B`

Runnable scripts:

```bash
python examples/list_models.py
python examples/chat.py --model smshahbaj/RIFA-PRO-3B --prompt "Explain recursion simply."
```

---

## Repository structure

```text
RIFA-Text-Series/
├── README.md                 # Series overview (this file)
├── LICENSE
├── CITATION.cff
├── requirements-examples.txt
├── docs/
│   ├── overview.md           # Series narrative
│   └── models/
│       ├── rifa-nano.md
│       ├── rifa-code.md
│       ├── rifa-edge.md
│       ├── rifa-flash.md
│       └── rifa-pro.md
├── examples/
│   ├── chat.py
│   └── list_models.py
└── .github/
    └── CODEOWNERS
```

**Design:** one series entrypoint + **one page per model** (easy to link from HF cards, tweets, papers).

---

## Design principles

| Principle | Meaning |
|-----------|---------|
| Efficient | Small parameter counts; runnable on limited hardware |
| Capable | Practical text/code behaviour for each size class |
| Yours | Open weights; clear cards; reproducible load snippets |
| Honest | Docs hub ≠ training mega-stack; scale is stated upfront |

---

## Citation

```bibtex
@misc{rifa_text_series,
  title        = {RIFA Text Series},
  author       = {smshahbaj},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/collections/smshahbaj/rifa-text-series}},
  note         = {Small language model family}
}
```

Or use [`CITATION.cff`](CITATION.cff).

---

## License

- **This repository (docs + examples):** [MIT](LICENSE)
- **Model weights:** see each Hugging Face model card

---

<div align="center">

**RIFA Text Series**

Efficient. Capable. Yours.

[Collection](https://huggingface.co/collections/smshahbaj/rifa-text-series) · [Profile](https://huggingface.co/smshahbaj)

</div>
