# Llama 3.1 8B QLoRA Fine-Tuning

QLoRA fine-tuning of **Llama 3.1 8B** (4-bit, via [Unsloth](https://github.com/unslothai/unsloth)) on a machine-translated Indonesian instruction dataset, with before/after evaluation, a GGUF export, and a direct check of how much VRAM a 4-bit 8B model actually uses.

Everything below comes from an actual Google Colab run (GPU: NVIDIA A100-SXM4-40GB). No number is estimated.

## What this does

1. Loads `unsloth/Meta-Llama-3.1-8B` in 4-bit (NF4) and attaches a LoRA adapter (r=16, all linear layers).
2. Cross-checks the LoRA parameter count against a closed-form formula computed from the model config.
3. Fine-tunes on [`rubythalib33/alpaca-cleaned-translated-id`](https://huggingface.co/datasets/rubythalib33/alpaca-cleaned-translated-id) with a held-out eval split.
4. Measures eval loss/perplexity and a small smoke test **before and after** training.
5. Saves the adapter, reloads it, and compares outputs for consistency.
6. Merges and exports the fine-tuned model to GGUF (Q4_K_M) for serving with llama.cpp.

## Results

| Metric | Value |
|---|---|
| Base model | Llama 3.1 8B (8,030,261,248 params) |
| 4-bit memory footprint (measured) | **5.86 GB** |
| LoRA trainable params | 41,943,040 (0.522%) — matches closed-form formula exactly |
| Training steps | 600 (≈0.093 epoch of the dataset) |
| Training time | 1,019 s (17.0 min) on A100-40GB |
| Peak VRAM (training) | 6.87 GB |
| Eval loss: before → after | 1.7857 → 0.8686 |
| Perplexity: before → after | 5.96 → 2.38 |
| Adapter size | 83.9 MB |
| GGUF export (Q4_K_M) | 4.92 GB (~4.90 bits/weight) |

![Training loss curve](images/loss_curve.png)

### A commonly cited compression claim doesn't hold up for this model

Bootcamp material this project is based on states that a 7B model in 4-bit uses "around 2 GB." Measured directly on this 8B model, both the raw 4-bit checkpoint and the final GGUF export come out well above that figure:

![Compression claim vs measured size](images/compression_claim_vs_measured.png)

The likely reason: NF4 quantization only replaces linear-layer weights. Embeddings, layer norms, and quantization overhead (double quantization constants) still add up, and that overhead is proportionally larger on an 8B model with a 128k-token vocabulary than the back-of-envelope "params × 4 bits" math suggests.

## Other findings

- **Reproducible code-generation regression.** Across three independent training runs, the fine-tuned model's answer to "write a factorial function" consistently mixed Indonesian keywords into otherwise-Python code (`untuk i dalam rentang(...)`, `kembali hasil` — literal translations of `for`/`in`/`range`/`return`), producing syntactically invalid code. This traces back to the training data being machine-translated, and it showed up in all three runs, not just once. The notebook checks this automatically with `ast.parse`, not just a regex match on `"def "`.
- **Individual behaviors are unstable at well under one epoch.** With only ~0.09 epoch of training, a specific smoke-test prompt (translate a short sentence to English) passed in two runs and failed in a third — the model echoed the Indonesian input back instead of translating — even though eval loss was nearly identical across runs (0.868–0.869). Aggregate loss doesn't guarantee consistent behavior on any single prompt.
- **The Fibonacci check is convention-aware.** An earlier version of the smoke test matched a literal `55` in the output, which unfairly failed a 0-indexed Fibonacci sequence (`[0, 1, 1, 2, ...]`) that is just as mathematically correct as the 1-indexed one (`[1, 1, 2, 3, ..., 55]`). The check now verifies the Fibonacci recurrence relation directly instead of one specific answer.
- **Adapter reload isn't bit-identical.** After saving and reloading the adapter, 4–5 of 6 smoke-test prompts produced identical greedy output across the three runs; the rest differed slightly in wording. This is expected — some parameters get upcast during training prep in ways that don't perfectly round-trip through a save/reload cycle.

## How to run

1. Open `notebooks/llama31_8b_qlora_unsloth.ipynb` in Google Colab.
2. Set the runtime to a GPU (a T4 works; the run here used an A100).
3. Run all cells top to bottom. A Hugging Face token is optional (only needed to avoid rate limits on the public model/dataset) — set it in Colab Secrets as `HF_TOKEN` if you have one.
4. The adapter and GGUF export are saved to Google Drive under `AI-Engineer/LLM/llama31-8b-alpaca-id/`.

Approximate total runtime: 20–40 minutes depending on GPU.

## Repo structure

```
.
├── notebooks/
│   └── llama31_8b_qlora_unsloth.ipynb
├── images/
│   ├── loss_curve.png
│   └── compression_claim_vs_measured.png
├── LICENSE
└── README.md
```

## Limitations

- Training only covers ~9% of one epoch (600 steps), by design, to keep the run short — this is a fine-tuning demonstration, not a production-quality instruction model.
- The dataset is machine-translated; translation quality was not audited beyond the code-generation issue noted above.
- The smoke test is a handful of heuristic checks (regex, AST parsing, a recurrence check), not a benchmark.

## License

MIT — see [LICENSE](LICENSE).
