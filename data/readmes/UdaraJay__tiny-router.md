# tiny-router

`tiny-router` is a compact experimental multi-head text classifier for short, domain-neutral routing decisions. It predicts four label heads from `current_text` and optional interaction context, then exposes training, evaluation inference, and model export.

https://github.com/user-attachments/assets/a2b67a42-c93a-4702-86a3-dfb416ccfee6

## Outputs

```json
{
  "relation_to_previous": { "label": "correction", "confidence": 0.94 },
  "actionability": { "label": "act", "confidence": 0.97 },
  "retention": { "label": "useful", "confidence": 0.76 },
  "urgency": { "label": "medium", "confidence": 0.81 },
  "overall_confidence": 0.87
}
```

```
relation_to_previous: new | follow_up | correction | confirmation | cancellation | closure
actionability: none | review | act
retention: ephemeral | useful | remember
urgency: low | medium | high
```

The model emits four separate signals that are meant to be useful to downstream automation systems:

- `relation_to_previous`
  - tells the system whether the message starts something new or modifies prior context
  - useful for updating existing state instead of treating every message as a fresh request
- `actionability`
  - tells the system whether to do nothing, act automatically, or send the message to review
  - useful as the first routing gate in an agent or product workflow
- `retention`
  - tells the system whether the content is disposable, temporarily useful, or worth storing as longer-term memory
  - useful for memory policy and context management
- `urgency`
  - tells the system how aggressively to prioritize the message
  - useful for queue ordering, escalation, and notification policy

## Input schema

```json
{
  "current_text": "Actually next Monday",
  "interaction": {
    "previous_text": "Set a reminder for Friday",
    "previous_action": "created_reminder",
    "previous_outcome": "success",
    "recency_seconds": 45
  }
}
```

Interaction is optional. Missing interaction fields normalize to:

- `previous_text = ""`
- `previous_action = "none"`
- `previous_outcome = "unknown"`
- `recency_seconds = -1`
- `log_recency_seconds = 0.0`

Recency is clamped to `3600` by default, then transformed with `log1p`.

`previous_action` is free-form at the input layer. The raw string is preserved in the prompt, while structured features map it into a compact internal action vocabulary:

- `none`
- `create`
- `update`
- `send`
- `store`
- `route`
- `schedule`
- `dismissed`
- `clarify`
- `search`
- `notify`
- `cancel`
- `complete`
- `other`

## Model

- Default encoder: `microsoft/deberta-v3-small`
- Alternatives supported by flag: `microsoft/MiniLM-L12-H384-uncased`, `distilbert-base-uncased`, `prajjwal1/bert-tiny`, or any compatible encoder
- Text input prompt:

```text
Current: {current_text}
Previous: {previous_text}
Previous action: {previous_action}
Previous outcome: {previous_outcome}
```

- Structured features:
  - categorical embedding for canonicalized `previous_action`
  - categorical embedding for `previous_outcome`
  - learned projection over `log_recency_seconds`
- Learned attention pooling over encoder states by default
- Final representation: pooled encoder state concatenated with structured features
- Dependency-aware heads:
  - `relation_to_previous` predicts first
  - later heads receive a learned summary of earlier head predictions
  - this helps encode correlations like `correction -> act` or `closure -> none`
- Post-hoc per-head temperature scaling fitted on the validation split for calibrated probabilities

## Quickstart

```bash
uv sync
make validate-data
make dedupe-data
make split-data
make train
make eval
make export
```

## Training

Default hyperparameters:

- `max_length=256`
- `batch_size=16`
- `encoder_lr=2e-5`
- `head_lr=1e-4`
- `pooling_type=attention`
- `use_head_dependencies=true`
- `epochs=5`
- `weight_decay=0.01`
- `warmup_ratio=0.1`

Example:

```bash
uv run python -m scripts.train \
  --train-file data/synthetic/train.jsonl \
  --validation-file data/synthetic/validation.jsonl \
  --test-file data/synthetic/test.jsonl \
  --output-dir artifacts/tiny-router \
  --encoder-name microsoft/deberta-v3-small \
  --batch-size 16 \
  --device cpu \
  --epochs 5 \
  --mixed-precision
```

Per-head loss weighting is supported:

```bash
uv run python -m scripts.train \
  --train-file data/synthetic/train.jsonl \
  --validation-file data/synthetic/validation.jsonl \
  --output-dir artifacts/tiny-router \
  --head-loss-weights '{"relation_to_previous": 1.2, "urgency": 1.1}'
```

Early stopping uses validation macro-average F1 across all four heads. After the best checkpoint is selected, the training script fits per-head temperature scaling on the validation logits and saves `temperature_scaling.json` for calibrated eval and inference.

## Evaluation

The evaluation CLI reports:

- per-head accuracy
- per-head macro F1
- per-head confusion matrix
- per-label precision/recall/F1/support
- overall exact match
- automation-safe accuracy on predictions above a confidence threshold
- confidence calibration bins and ECE
- ablations for:
  - `current_text_only`
  - `current_plus_previous_text`
  - `full_interaction`

Example:

```bash
uv run python -m scripts.eval \
  --model-dir artifacts/tiny-router \
  --data-file data/synthetic/test.jsonl \
  --output-file artifacts/tiny-router/eval.json \
  --run-ablations \
  --device cpu
```

## Inference

```bash
uv run python -m scripts.predict \
  --model-dir artifacts/tiny-router \
  --input-json '{"current_text":"Actually next Monday","interaction":{"previous_text":"Set a reminder for Friday","previous_action":"created_reminder","previous_outcome":"success","recency_seconds":45}}' \
  --device cpu \
  --pretty
```

Example output:

```json
{
  "relation_to_previous": { "label": "correction", "confidence": 0.94 },
  "actionability": { "label": "act", "confidence": 0.97 },
  "retention": { "label": "useful", "confidence": 0.76 },
  "urgency": { "label": "medium", "confidence": 0.81 },
  "overall_confidence": 0.87
}
```

ONNX inference:

```bash
uv run python -m scripts.onnx_predict \
  --model-dir artifacts/tiny-router/onnx \
  --input-json '{"current_text":"Actually next Monday","interaction":{"previous_text":"Set a reminder for Friday","previous_action":"created_reminder","previous_outcome":"success","recency_seconds":45}}' \
  --pretty \
  --show-latency
```

## ONNX export

```bash
uv run python -m scripts.export_onnx \
  --model-dir artifacts/tiny-router \
  --output-dir artifacts/tiny-router/onnx \
  --quantize
```

This exports:

- `tiny_router.onnx`
- `tiny_router.int8.onnx` when quantization is enabled
- `onnx_metadata.json`
- `temperature_scaling.json` when validation calibration is available
- tokenizer files copied from the training checkpoint
- `model_config.json` and label maps inside the checkpoint directory

## Dataset helpers

Validate labels:

```bash
uv run python -m scripts.validate_labels --input data/raw/synthetic.jsonl
```

Deduplicate:

```bash
uv run python -m scripts.dedupe_examples --input data/raw/synthetic.jsonl --output data/raw/synthetic.deduped.jsonl
```

Split train/validation/test:

```bash
uv run python -m scripts.split_dataset --input data/raw/synthetic.deduped.jsonl --output-dir data/synthetic
```

## Python inference snippet

```python
import json
import subprocess

payload = {
    "current_text": "Actually next Monday",
    "interaction": {
        "previous_text": "Set a reminder for Friday",
        "previous_action": "created_reminder",
        "previous_outcome": "success",
        "recency_seconds": 45,
    },
}

result = subprocess.check_output(
    [
        "uv",
        "run",
        "python",
        "-m",
        "scripts.predict",
        "--model-dir",
        "artifacts/tiny-router",
        "--input-json",
        json.dumps(payload),
        "--pretty",
    ],
    text=True,
)
print(result)
```

## Notes

- Calibrate the confidence threshold against production-like validation data before enabling auto-routing.
