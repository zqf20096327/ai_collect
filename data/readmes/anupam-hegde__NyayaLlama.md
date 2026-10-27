# Fine-Tuning Llama on Indian Legal Text (IPC, CrPC, Constitution)

This project fine-tunes [Meta's Llama 3.2 3B Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) on a curated dataset of Indian legal question-answer pairs using QLoRA (4-bit quantization + LoRA adapters).

## Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/) and comprises curated question-answer pairs derived from key Indian legal texts:

- **Indian Penal Code (IPC)** — criminal law provisions
- **Criminal Procedure Code (CrPC)** — procedural criminal law
- **Indian Constitution** — fundamental constitutional principles

Each entry contains a clear question alongside its corresponding answer, covering fundamental concepts, key provisions, and significant legal terms.

### Intended Use Cases

- **Legal Research** — quick lookup of legal terminology and principles for lawyers, researchers, and students
- **NLP / Fine-Tuning** — train question-answering systems with domain-specific Indian legal knowledge
- **Education** — build tools and study materials for law students and practitioners

### Important Notes & Limitations

- **Educational & research use only** — this dataset must not be used for legal advice or to influence real legal decisions without proper context and verification.
- **Preprocessing recommended** — QA pairs may contain phrasing variations, redundancies, or entries that need filtering. Cleanse and normalize the data before training.
- **Law is dynamic** — legal provisions and interpretations change over time. Verify the current applicability of any concept before relying on it.
- **Credits** — if you use this dataset, provide appropriate attribution and consider sharing improvements back to the community.

## Setup

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (fast Python package manager)
- NVIDIA GPU with CUDA support (see quantization section below)

### Install

```bash
# Clone the repo
git clone <repo-url>
cd fine-tuning-legal-data

# Install dependencies with uv
uv sync
```

This creates a virtual environment and installs all packages from `pyproject.toml`:

| Package | Purpose |
|---|---|
| `torch` | Deep learning framework |
| `transformers`, `tokenizers` | Hugging Face model loading & tokenization |
| `bitsandbytes` | 4-bit quantization |
| `peft` | LoRA / QLoRA adapters |
| `trl` | Transformer Reinforcement Learning (SFT trainer) |
| `accelerate` | Multi-GPU / mixed-precision training |
| `datasets` | Hugging Face datasets library |
| `huggingface-hub` | Model upload / download |
| `safetensors` | Safe serialization format |
| `sentencepiece` | Tokenizer backend |

## Model & Quantization

**GPU**: NVIDIA RTX 4060 (8 GB VRAM)

**Base model**: [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) (3 billion parameters)

Raw FP16 inference would require **~6 GB** just for the weights — leaving almost no room for training gradients, optimizer states, and activations. Instead, this project uses **4-bit QLoRA** to make fine-tuning feasible on consumer hardware.

### 4-Bit Math

```
4 bits = 0.5 bytes
3 billion parameters × 0.5 bytes = 1.5 GB (model weights)
```

In practice, the model occupies **2–2.5 GB VRAM** once loaded. The extra ~0.5–1 GB comes from:

- **Quantization metadata** — scaling factors that `bitsandbytes` uses to preserve model quality during dequantization
- **Initial memory overhead** — CUDA kernels and buffers allocated at load time

This leaves the bulk of the **8 GB VRAM** free for the active training math — gradients, optimizer states (AdamW), and forward/backward activations.

### QLoRA Configuration

```python
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",           # NormalFloat4 — optimal for normally-distributed weights
    bnb_4bit_compute_dtype=torch.float16, # Forward/backward compute stays in FP16
    bnb_4bit_use_double_quant=True,       # Quantize the quantization constants to save extra VRAM
)
```

LoRA adapters are then attached via PEFT, so only a small fraction of parameters are trained while the base model stays frozen in 4-bit.

## Project Structure

```
├── README.md
├── pyproject.toml          # Dependencies & project metadata
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version (3.11)
├── .gitignore
├── experiment.ipynb        # Main fine-tuning notebook
├── scrape.py               # Data scraping / preprocessing utilities
└── datasets/
    ├── archive.zip          # Raw dataset archive
    └── archive/             # Extracted dataset files
```

## License

This project is for educational and research purposes. The dataset is subject to its original Kaggle license terms.
