# IsItAI — Self-Hostable AI Text Detector

A self-hostable, **bring-your-own-calibration** AI text detector based on the [Fast-DetectGPT](https://arxiv.org/abs/2310.05130) algorithm. Unlike hosted services, IsItAI lets you plug in any HuggingFace causal LM, calibrate on your own domain data, and run inference locally or on a Modal GPU — all with no data leaving your infrastructure.

It splits text into sentence-aligned chunks, scores each chunk using a language model's log-probability discrepancy, and aggregates the results into an overall AI probability.

> **Key idea:** AI-generated text tends to sit near local maxima of a language model's probability surface. The *discrepancy score* — the difference between the original token sequence's log-probability and the average log-probability of random samples — captures this signal. Run calibration on your own human/AI dataset to fit the detector to your domain and model.

---

## Contents

- [Project structure](#project-structure)
- [Installation](#installation)
- [Workflow overview](#workflow-overview)
- [Step 1 — Prepare your dataset](#step-1--prepare-your-dataset)
- [Step 2 — Calibrate locally](#step-2--calibrate-locally)
- [Step 3 — Run the local detector](#step-3--run-the-local-detector)
- [Modal deployment (GPU inference)](#modal-deployment-gpu-inference)
- [Dataset format reference](#dataset-format-reference)
- [Samples](#samples)
- [Calibration explained](#calibration-explained)
- [Tuning chunker settings](#tuning-chunker-settings)
- [Best practices](#best-practices)
- [Limitations](#limitations)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Project structure

```
isitai/
├── pyproject.toml              # uv project file
├── chunker.py                  # shared sentence splitter and chunker
├── models.py                   # Pydantic result models
├── prepare_dataset.py          # CLI — chunk a raw JSON dataset
├── ai_detector.py              # local CPU/GPU inference
├── calibrate_local.py          # calibration — local machine
├── samples/                    # example JSON files (see [Samples](#samples))
│   ├── sample_dataset.json
│   ├── sample_dataset_chunked.json
│   └── sample_calibration_results.json
└── modal_deployment/
    ├── ai_detector_modal.py    # Modal GPU inference endpoint
    └── calibrate_modal.py      # calibration — Modal GPU
```

---

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Clone the repo
git clone https://github.com/Croups/isitai
cd isitai

# Create a virtual environment and install dependencies
uv sync

# Activate the environment
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```

PyTorch is included in the dependencies. If you need a specific CUDA version, install it manually before running `uv sync`:

```bash
# Example: CUDA 12.1
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

Modal is included in the default dependencies and is installed automatically by `uv sync`. No extra step is needed.

---

## Workflow overview

```
1. Collect dataset
   human_texts + ai_texts  (raw JSON)
         │
         ▼
2. prepare_dataset.py
   Chunks every entry into 15-50 word pieces
         │
         ▼
3. calibrate_local.py  OR  calibrate_modal.py
   Scores chunks with your model, fits Gaussian distributions
         │
         ▼
4. Paste CALIBRATION dict
   into ai_detector.py  OR  ai_detector_modal.py
         │
         ▼
5. Run the detector
   detect_full("your text...")  →  ai_score, prediction, chunks
```

The **calibration step is essential** — the default `CALIBRATION` values in the code are placeholders. Without calibration on data that matches your model and domain, the detector will produce unreliable predictions.

---

## Step 1 — Prepare your dataset

Prepare a raw dataset JSON file with the following structure (see [Dataset format reference](#dataset-format-reference) for details), then chunk it:

```bash
python prepare_dataset.py \
    --input my_dataset.json \
    --output my_dataset_chunked.json
```

Available flags:

| Flag | Default | Description |
|---|---|---|
| `--input` | required | Path to raw dataset JSON |
| `--output` | required | Path to write chunked dataset |
| `--min-words` | `15` | Minimum words per chunk |
| `--max-words` | `50` | Maximum words per chunk |
| `--min-sentence-words` | `3` | Drop sentences shorter than this |

The chunker uses sentence boundaries to build natural-sounding chunks. Tune `--min-words` and `--max-words` to match the average paragraph length in your target domain. **Use the same values during calibration and inference.**

---

## Step 2 — Calibrate locally

```bash
python calibrate_local.py \
    --model Qwen/Qwen2.5-3B \
    --dataset my_dataset_chunked.json \
    --output calibration_results.json
```

Available flags:

| Flag | Default | Description |
|---|---|---|
| `--model` | `Qwen/Qwen2.5-3B` | HuggingFace model name |
| `--dataset` | required | Path to chunked dataset JSON |
| `--output` | `calibration_results.json` | Where to save full results |
| `--max-samples` | `200` | Max texts per class (use more for a better fit) |
| `--n-samples` | `5` | Token samples per text |
| `--max-length` | `512` | Tokeniser truncation limit |
| `--seed` | `42` | Random seed for subsampling |

When finished, the script prints a `DEFAULT_CALIBRATION` dict. Copy it into `ai_detector.py`:

```python
# ai_detector.py
DEFAULT_CALIBRATION: Dict[str, float] = {
    "mu0":    -0.023,   # <-- your value
    "sigma0":  0.041,   # <-- your value
    "mu1":     0.087,   # <-- your value
    "sigma1":  0.038,   # <-- your value
}
```

---

## Step 3 — Run the local detector

### As a library

```python
from ai_detector import AIDetector

detector = AIDetector()  # lazy-loads model on first call

result = detector.detect_full("Paste your essay or article here...")

print(f"AI score  : {result.ai_score:.1f}%")
print(f"Prediction: {result.prediction}")   # 'AI', 'Human', or 'Mixed'

for chunk in result.chunks:
    print(f"  Chunk {chunk.chunk_index + 1}: {chunk.prediction} ({chunk.ai_probability:.0%})  — {chunk.text[:60]}...")
```

Pass a custom calibration or chunker config:

```python
from ai_detector import AIDetector
from chunker import ChunkerConfig

detector = AIDetector(
    model_name="Qwen/Qwen2.5-3B",
    calibration={
        "mu0": -0.023, "sigma0": 0.041,
        "mu1":  0.087, "sigma1": 0.038,
    },
    chunker_config=ChunkerConfig(min_chunk_words=20, max_chunk_words=60),
)
```

### From the command line

```bash
# Analyse a string
python ai_detector.py "The quick brown fox jumps over the lazy dog."

# Analyse a file
python ai_detector.py --file essay.txt

# JSON output (pipe-friendly)
python ai_detector.py --json essay.txt
```

---

## Modal deployment (GPU inference)

Modal lets you run inference on a GPU without managing any infrastructure. The container stays warm between requests, so cold-start latency is rare after the first call.

### 1. Install and authenticate

```bash
modal setup
```

`modal setup` will open a browser window. Create a free account at [modal.com](https://modal.com) — new accounts receive a **$5 free credit**, which is enough to run dozens of calibration and inference jobs on a T4 GPU. Once you sign up, authorize the CLI in the browser and you're ready to go.

### 2. Configure

Open `modal_deployment/ai_detector_modal.py` and edit the constants at the top:

```python
MODEL_NAME       = "Qwen/Qwen2.5-3B"   # HuggingFace model
GPU_TYPE         = "T4"                  # T4 / L4 / A10G / A100 / H100
SCALEDOWN_WINDOW = 300                   # seconds to keep container warm
N_SAMPLES        = 5                     # samples per chunk

CALIBRATION = {
    "mu0":    ...,   # paste your calibrate_modal.py output here
    "sigma0": ...,
    "mu1":    ...,
    "sigma1": ...,
}
```

### 3. Calibrate on GPU

Run calibration on the same GPU type you will use for inference so the score distribution matches exactly:

```bash
modal run modal_deployment/calibrate_modal.py \
    --gpu T4 \
    --model Qwen/Qwen2.5-3B \
    --dataset my_dataset_chunked.json \
    --output calibration_results.json
```

Available flags:

| Flag | Default | Description |
|---|---|---|
| `--model` | `Qwen/Qwen2.5-3B` | HuggingFace model name |
| `--gpu` | `T4` | Modal GPU type (`T4`, `L4`, `A10G`, `A100`, `H100`) |
| `--dataset` | required | Path to chunked dataset JSON |
| `--output` | `calibration_results.json` | Local path for results |
| `--max-samples` | `400` | Max texts per class |
| `--n-samples` | `5` | Token samples per text |
| `--max-length` | `512` | Tokeniser truncation limit |

Copy the printed `CALIBRATION` dict into `ai_detector_modal.py`.

### 4. Deploy

```bash
# Deploy permanently
modal deploy modal_deployment/ai_detector_modal.py

# Hot-reload for development (stops when you Ctrl-C)
modal serve modal_deployment/ai_detector_modal.py
```

Modal prints the endpoint URL after deployment.

### 5. Call the endpoint

```bash
curl -X POST https://your-modal-endpoint.modal.run \
     -H "Content-Type: application/json" \
     -d '{"text": "Your text here...", "include_chunks": true}'
```

Response:

```json
{
  "ai_score": 82.3,
  "prediction": "AI",
  "confidence": 0.74,
  "raw_score": 0.091,
  "total_chunks": 6,
  "ai_chunk_count": 5,
  "human_chunk_count": 1,
  "total_words": 248,
  "chunks": [...]
}
```

---

## Dataset format reference

Both `prepare_dataset.py` and the calibration scripts expect this format:

```json
{
  "human_texts": [
    {
      "id": "unique-identifier",
      "text": "Full text of the document...",
      "source": "optional label, e.g. ASAP_2.0"
    }
  ],
  "ai_texts": [
    {
      "id": "unique-identifier",
      "text": "Full text of the document...",
      "source": "optional label, e.g. gpt-4o"
    }
  ]
}
```

- `id` — any unique string; used to name the resulting chunks (`{id}_chunk_1`, etc.)
- `text` — the full document text; `prepare_dataset.py` will split it into chunks
- `source` — optional metadata, preserved in the chunked output

**Recommended dataset size:** at least 100 texts per class for calibration. More is better — 500+ per class gives a reliable Gaussian fit and stable AUROC.

---

## Samples

The `samples/` directory contains example files you can copy or inspect:

| File | Purpose |
|------|---------|
| `sample_dataset.json` | Raw dataset in the [expected format](#dataset-format-reference) (`human_texts` / `ai_texts`). Use as `prepare_dataset.py --input`. |
| `sample_dataset_chunked.json` | Chunked output of `prepare_dataset.py` — same shape as `calibrate_local.py` / `calibrate_modal.py` `--dataset`. |
| `sample_calibration_results.json` | Example output of `calibrate_local.py` (or Modal calibration): calibration parameters plus per-text scores. |

These are for documentation and local testing only; replace them with your own data for real calibration.

---

## Calibration explained

The detector classifies each chunk using Bayesian inference over two Gaussian distributions:

```
p(AI  | score) ∝ N(score ; mu1, sigma1)   — AI distribution
p(Human | score) ∝ N(score ; mu0, sigma0) — Human distribution
```

The four parameters you calibrate:

| Parameter | Meaning |
|---|---|
| `mu0` | Mean discrepancy score for human-written text |
| `sigma0` | Standard deviation of discrepancy scores for human text |
| `mu1` | Mean discrepancy score for AI-generated text |
| `sigma1` | Standard deviation of discrepancy scores for AI text |

**`mu1` must be greater than `mu0`** for the detector to work correctly. If this is not the case, your dataset labels may be swapped, or the model may not discriminate well between the two classes.

**AUROC** (Area Under the ROC Curve) measures how well the raw scores separate human from AI text before applying Gaussian classification:

- `1.0` — perfect separation
- `0.5` — random (the model cannot distinguish)
- `> 0.8` — good enough for practical use

**Important:** Calibration is model- and domain-specific. If you switch models or move to a different domain (e.g. from news articles to academic essays), re-run calibration.

---

## Tuning chunker settings

The chunker splits text at sentence boundaries and groups sentences into chunks within the configured word-count window. Smaller chunks are more sensitive to local edits (useful for detecting partially AI-written text); larger chunks are more stable for short inputs.

```python
from chunker import ChunkerConfig

config = ChunkerConfig(
    min_chunk_words=15,   # merge chunks smaller than this
    max_chunk_words=50,   # start a new chunk when this would be exceeded
    min_sentence_words=3, # drop very short sentences before chunking
)
```

**Always use the same `ChunkerConfig` values during calibration and inference.** The discrepancy score distribution shifts when chunk sizes change, which invalidates the calibration parameters.

---

## Best practices

### Choosing a model

The scoring model is the single most important factor in detection quality. A few guidelines:

- **Larger models discriminate better.** A 7B model will typically produce a higher AUROC than a 3B model on the same dataset, because it has a sharper probability surface and is more sensitive to the stylistic patterns of AI-generated text. If your AUROC is below 0.75, try upgrading the model before investing in more calibration data.
- **Match the model family to your use case.** If the texts you want to detect were generated by a GPT-4-class instruction-tuned model, a similarly capable base LM (e.g. `Qwen2.5-7B`, `Mistral-7B`) will score them more reliably than a small 1–3B model.
- **Use a base model, not an instruction-tuned one.** Base models have a smoother token probability distribution, which makes the discrepancy signal cleaner. Instruction-tuned models apply RLHF shaping that can compress or distort log-probabilities and reduce separation.
- **Keep the model consistent.** Calibration parameters are tied to the model that produced them. If you swap models, re-run calibration from scratch — the raw score distributions will be completely different.

### Interpreting AUROC

AUROC measures how often the model correctly ranks a random AI chunk above a random human chunk, before any Gaussian classification is applied. It is the most honest single-number summary of detector quality.

| AUROC | Interpretation |
|---|---|
| `> 0.90` | Excellent — suitable for high-stakes use |
| `0.80 – 0.90` | Good — reliable for most practical purposes |
| `0.70 – 0.80` | Acceptable — useful but expect some errors |
| `0.60 – 0.70` | Weak — reconsider model or dataset quality |
| `< 0.60` | Poor — close to random, do not rely on results |

If your AUROC is unexpectedly low, check these common causes in order:
1. **Swapped labels** — confirm that `mu1 > mu0`; if not, your `human_texts` and `ai_texts` may be switched.
2. **Domain mismatch** — calibration data should closely match the texts you will run the detector on in production. A model calibrated on news articles will perform poorly on academic essays.
3. **Model too small** — upgrade to a larger model (see above).
4. **Insufficient data** — fewer than ~200 samples per class leads to an unstable Gaussian fit. Use 500+ per class when possible.

### Building a high-quality calibration dataset

The calibration dataset directly determines how well the detector performs in your target domain. Poor calibration data is the most common reason for a low AUROC.

- **Match the domain.** Human texts and AI texts should both come from the same domain, writing style, and average length as the texts you will detect in production. A mismatch between calibration and inference domain is the leading cause of unreliable predictions.
- **Use realistic AI texts.** Generate AI texts with the same model, temperature, and prompt style that you expect to encounter. Texts generated at very low temperature (near-deterministic) are easier to detect; texts at higher temperature are harder. Calibrate for the harder case.
- **Balance your classes.** Use roughly equal numbers of human and AI samples. Imbalanced datasets can skew the Gaussian fit and inflate or deflate the AUROC.
- **Diversify.** Avoid repeated prompts or boilerplate AI outputs. Diversity in both human and AI samples produces a more robust Gaussian fit.
- **Minimum recommended sizes:**

| Dataset size (per class) | Expected fit quality |
|---|---|
| 50–100 | Rough estimate, high variance |
| 200–500 | Reliable for most use cases |
| 500+ | Stable fit, recommended for production |

### Chunk size tuning

Chunk size interacts directly with score variance. Smaller chunks are noisier (fewer tokens → higher variance per chunk) but catch localised AI edits in otherwise human text. Larger chunks are more stable but may dilute short AI passages.

- **Short inputs (< 100 words):** use `max_chunk_words=100` to avoid over-splitting.
- **Mixed human/AI documents:** use smaller chunks (`max_chunk_words=30–40`) to increase spatial resolution.
- **Long, uniformly-written texts:** default settings (`min=15`, `max=50`) work well.
- Whatever you choose, **use identical settings during calibration and inference**.

### Thresholds

The default decision thresholds (`> 70%` → AI, `40–70%` → Mixed, `< 40%` → Human) are conservative starting points. Adjust them based on your tolerance for false positives vs false negatives:

- Raising the AI threshold (e.g. to 80%) reduces false positives at the cost of more missed detections.
- Lowering it (e.g. to 60%) catches more AI text but flags more human text as suspicious.
- For high-stakes decisions, always treat "Mixed" as requiring human review rather than automated action.

---

## Limitations

IsItAI is a research-grade tool. Be aware of its constraints before using it in production:

- **Not a ground truth.** No statistical detector is perfect. IsItAI produces a probability, not a verdict. False positives (human text flagged as AI) and false negatives (AI text missed) will occur, especially near the decision boundary.
- **Calibration drift.** Calibration parameters are tied to a specific model, chunk size, and text domain. If any of these change — new LLM versions, different writing styles, different languages — performance will degrade until you recalibrate.
- **Short texts are unreliable.** Texts shorter than ~100 words produce very few chunks, which increases variance and makes the aggregated score unstable. Treat results on short inputs with extra caution.
- **Adversarial text.** A writer who is aware of how log-probability detectors work can paraphrase or lightly edit AI-generated text to lower its discrepancy score. IsItAI is not robust against deliberate evasion.
- **Language.** The detector's performance depends on how well the scoring model handles the input language. It works best on English text; results on other languages will vary with the model's multilingual capability.
- **Not a replacement for human judgment.** Automated AI detection should be one signal among many, not a sole basis for decisions with real consequences (academic integrity cases, hiring, content moderation, etc.).

---

## License

MIT — free to use, modify, and distribute for any purpose. See [LICENSE](LICENSE).

---

## Acknowledgements

IsItAI is built on the **Fast-DetectGPT** algorithm introduced in:

> Bao, G., Zhao, Y., Teng, Z., Yang, L., & Zhang, Y. (2023).  
> *Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.*  
> [arXiv:2310.05130](https://arxiv.org/abs/2310.05130)

The original implementation of fast-detectgpt is available at [github.com/baoguangsheng/fast-detect-gpt](https://github.com/baoguangsheng/fast-detect-gpt).

---

## Contact

Built by [Enes Koşar](https://www.linkedin.com/in/enes-koşar). Feel free to reach out for questions, feedback, or collaboration.
