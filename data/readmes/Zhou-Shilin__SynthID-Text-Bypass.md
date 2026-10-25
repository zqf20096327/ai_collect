# SynthID Text Bypass

A research demo of a **scrubbing attack** against generative text watermarks
(such as **SynthID-Text**): for every sliding window of **H** tokens, one
token is masked and re-filled by a masked language model (MLM), producing
fluent text whose meaning is preserved while the watermark's statistical
signature is perturbed.

> ⚠️ **For research and education only.** Removing watermarks from AI-generated
> content may violate the terms of service of the service that produced it and
> may be illegal in some jurisdictions. Use responsibly.

## Background

[SynthID-Text](https://www.nature.com/articles/s41586-024-08025-4) (Dathathri et al.,
*Nature*, 2024) embeds a statistical signature into the token stream of
generated text via its *tournament sampling* algorithm. A detector later
re-measures that signature to decide whether the text was machine-generated.

The paper's own **Limitations** section states that generative watermarks
*"are weakened by edits to the text"* and are vulnerable to *"stealing,
spoofing and scrubbing attacks."* This project implements exactly such a
scrub: a **minimal-edit attack** that swaps about `1/H` of the tokens for
near-equivalent ones, so the text stays fluent while the measured statistic
changes.

## How it works

```
Input text ──► tokenize ──► slide window of H tokens
                                   │
                                   ▼
                 every eligible token of the window is masked in turn
                                   │
                                   ▼
                 MLM scores each position; the original token is
                 EXCLUDED from the candidate set (an MLM's top-1 is
                 usually the original itself, so "top-1 != original"
                 would waste most windows):
                     y_i = argmax_{v != x_i} P(v | context)
                                   │
                                   ▼
          a replacement is accepted only if it preserves meaning:
            • P(y)/P(x) ≥ min. ratio        (relative plausibility)
            • cos(E(x), E(y)) ≥ min. sim    (contextual embeddings)
            • original ranks ≤ max rank     (weak plausibility guard)
            • candidate is a plain word of the same script —
              proper nouns & acronyms are never touched
              (Android → Java is "contextually probable", not
               semantically interchangeable)
                                   │
                                   ▼
                 edit the best position of the window (highest Q),
                 mark the neighbourhood as covered, rebuild text
```

Design choices follow the scrubbing-attack literature: excluding the original
token from the candidate set is SimKey's approach
([arXiv:2510.12828](https://arxiv.org/html/2510.12828v2)), and scoring every
eligible token of the window before editing one is the
synonym-eligible-word-first strategy analysed for SynthID robustness
([arXiv:2508.20228](https://arxiv.org/html/2508.20228v1)).

### Parameters

| Parameter | Meaning |
| --------- | ------- |
| `window_size` (`H`) | Window length in tokens; **one** token per window may be replaced. Larger `H` = fewer edits, smaller `H` = stronger scrubbing. |
| `stride` | Window advance. `H` (default) = non-overlapping windows; `1` = fully sliding. |
| `mode` | `best` (default): score every eligible token of the window and edit the best one. `middle` / `random` fix the position instead. |
| `min_ratio` | Meaning guard: the replacement must have at least this probability *relative to the original*, `P(y)/P(x) ≥ min_ratio`. Alternatives are naturally rarer than the original, so absolute thresholds reject too much. |
| `min_similarity` | Meaning guard: cosine similarity between the model's contextual representation of the original and of the replacement. |
| `max_orig_rank` | Weak plausibility guard: the original token must rank within the MLM's top-N predictions. |

### Models

| Model | Scripts | Notes |
| ----- | ------- | ----- |
| `answerdotai/ModernBERT-base` | English + code | default for latin text |
| `jhu-clsp/mmBERT-base` | 1800+ languages | default for CJK text |
| `FacebookAI/xlm-roberta-base` | 100 languages | optional |
| `google-bert/bert-base-multilingual-cased` | 104 languages | optional |
| `google-bert/bert-base-chinese` | Chinese | optional |

The Gradio UI and the CLI select the model **automatically** from the input
text's script (CJK → multilingual, otherwise English-optimized).

## Installation

Requires Python ≥ 3.10.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The first run downloads the selected MLM (~600 MB – 1.2 GB) from the Hugging
Face Hub.

### Using a local model (offline)

Drop a complete Hugging Face checkpoint into `models/<name>/` (e.g.
`models/ModernBERT-base/` with `config.json`, `tokenizer.json`,
`tokenizer_config.json`, `special_tokens_map.json`, `model.safetensors`) and
the code will automatically use it instead of downloading — fully offline:

```bash
# example: manual download via huggingface-cli
huggingface-cli download answerdotai/ModernBERT-base --local-dir models/ModernBERT-base

python app.py          # resolves answerdotai/ModernBERT-base -> models/ModernBERT-base
```

`models/` is git-ignored; it is meant for pre-downloaded checkpoints, not for
committing model weights.

## Usage

### Gradio web UI

```bash
python app.py            # http://127.0.0.1:7860
python app.py --share    # public link via Gradio
```

Paste AI-generated text, adjust **H** (and the other parameters), click
**Scrub Text**. The UI shows the scrubbed text, a token-level diff, the
applied edits table (with replacement probability, similarity and original
rank), and scrubbing statistics including the guard rejection breakdown.

### Command line

```bash
# scrub a string (model auto-selected from the text's script)
python -m synthid_bypass.cli --text "Your AI generated text here." --window 10

# scrub a file, machine-readable output, force a model
python -m synthid_bypass.cli --input text.txt --window 8 --mode random \
    --model jhu-clsp/mmBERT-base --json

# from stdin
cat text.txt | python -m synthid_bypass.cli --window 12
```

### As a library

```python
from synthid_bypass import TokenScrubber

scrubber = TokenScrubber()                      # auto-resolves local models/
result = scrubber.scrub(text, window_size=10)   # H = 10
print(result.scrubbed_text)
print(result.stats())
for edit in result.edits:
    print(edit.original_word, "->", edit.replacement_word,
          edit.probability, edit.similarity)
```

## Tests

```bash
pytest -q
```

The unit tests run offline with a fake tokenizer/model and cover script
detection, token eligibility (proper nouns, fragments, CJK), windowing,
candidate evaluation (original exclusion, ratio/plausibility/no-op guards),
and the full pipeline.

## Evaluating the detection-rate drop

The actual SynthID-Text detector is not public (it requires the watermarking
key/seed scheme of the production system). To measure the effect of this
attack on detection, use an open statistical watermark detector as a proxy,
e.g. the [watermarking-toolbox](https://github.com/gworks-wm-lab/watermarking-toolbox)
(KGW / Unigram / Exponential watermarks) and compare its detection AUC
before vs. after scrubbing. General rule of thumb: the smaller `H`, the more
edits and the lower the detection rate — at the cost of slightly more visible
changes.

## Limitations

- **Human observers** can still spot occasional replacements; this is not a
  paraphrase-level rewrite, it is a *minimal-edit* attack.
- Meaning preservation is heuristic (probability ratio + contextual-embedding
  cosine); occasional imperfect swaps are possible — the guard thresholds are
  exposed as sliders for a reason.
- Tokenizer round-trips can normalize whitespace/newlines (especially for
  CJK text), so the scrubbed text may differ cosmetically from the input.
- Only single-token swaps; phrases with multi-token idioms are left intact.
- Detection is probabilistic — scrubbing reduces the detection rate, it does
  not guarantee evasion.

## References

- Dathathri et al., *Scalable watermarking for identifying large language
  model outputs* (SynthID-Text), Nature 634, 819–826 (2024).
  https://doi.org/10.1038/s41586-024-08025-4
- Han et al., robustness analysis of SynthID-style watermarks under
  synonym-based editing: https://arxiv.org/html/2508.20228v1
- SimKey, minimal-edit scrubbing with BERT-style replacements:
  https://arxiv.org/html/2510.12828v2
- Answer.AI / LightOn, *ModernBERT*: https://huggingface.co/answerdotai/ModernBERT-base
- JHU CLSP, *mmBERT*: https://huggingface.co/jhu-clsp/mmBERT-base

## License

[MIT](LICENSE)
