# chat_llm_cookbook - Local SLMs for WhatsApp-like chat simulation

There are not many fine-tuning pipelines for chat data, and the ones that do
exist usually focus on DMs. I wanted to test the capabilities of small language
models (SLMs), so I tried to squeeze a six-person group-chat simulation into a
non-reasoning 2B model.

The results were quite bad in terms of consistency and coherence. But when the
model captured the way we speak—our slang and our reactions—it felt genuine,
and we had a lot of fun trying the group simulation.

The repository contains the sanitized pipeline I ended up using: data
preparation, separate Qwen and Kumru MLX trainers, corrected local inference,
terminal and browser chat interfaces, and evaluation utilities. It does not
contain private conversations, participant identities, trained weights,
adapters, generated transcripts, or judge credentials.

Start with [COOKBOOK.md](COOKBOOK.md) to reproduce the pipeline. The complete
experiment record is also available as [main.pdf](main.pdf).

![An invented P1/P2/P3 conversation in the local browser interface](assets/web-ui.jpg)

*Interface preview with manually entered fictional messages; this is not model output.*

## Main results

The primary benchmark was a blind **human-anchored** test at three-turn depth.
An LLM judge received a held-out context followed by equal-message-count real
and model continuations in randomized A/B order. The number below is how often
the judge preferred the real continuation, so **lower is better**.

| Author run | Human win-rate | 95% CI | Tie rate | Pairs |
|---|---:|---:|---:|---:|
| Qwen v10, corrected MLX | 91.0% | [81.8%, 95.8%] | 1.5% | 68 |
| Kumru Base 25k, fused GGUF | 92.4% | [83.5%, 96.7%] | 2.9% | 68 |

Both systems remained far from real chat. This benchmark did not separate the
two checkpoints: each received exactly 61 human wins among 68 pairs. It is best
used to measure the remaining distance from real conversation, not to rank
models whose intervals overlap.

A separate direct comparison used 200 matched six-turn contexts:

| System | Wins | Losses | Ties | Decisive win-rate | 95% CI |
|---|---:|---:|---:|---:|---:|
| Kumru Base 25k, fused GGUF | 143 | 44 | 13 | 76.5% | [69.9%, 82.0%] |
| Qwen v10, corrected MLX | 44 | 143 | 13 | 23.5% | [18.0%, 30.1%] |

Kumru was therefore the better final system for this Turkish chat. It also
matched human message-block pacing more closely: 1.61 messages per block,
versus Qwen's 1.27 and the human reference's 1.55. This compares complete
runtime bundles, not model weights in isolation; tokenizer, quantization, and
MLX versus llama.cpp differed as well.

Kumru 25k is the quality-first recommendation. Kumru 8k is still a useful quick
or overnight run for validating the pipeline before committing to the longer
training budget. A later 50k run produced a better human-anchored point estimate
of 80.6% [69.6%, 88.3%], but its direct result against 25k was inconclusive
(104--85 with 11 ties), so 25k remains the practical default.

If you try the pipeline on another chat, run the same human-anchored comparison
and report the interval, ties, judge, prompt, depth, and pair construction. The
judge used here knew a short slang glossary but did not truly know the group's
slang, relationships, or shared history. Results from different private chats
are informative comparisons, not strictly interchangeable measurements.

## Models and languages

`settings.yaml` selects one of the two included profiles:

| Value | Language profile | Suggested starting model | Evidence scope |
|---|---|---|---|
| `tr` | Turkish fillers and stopwords | Kumru-2B-Base, MLX 8-bit | Author-tested Turkish configuration |
| `en` | English fillers and stopwords | Qwen3.5-2B, MLX 8-bit | Starting profile; no English-chat quality evaluation |

Both models were trained and evaluated on Turkish conversations. The English
profile is supplied as a starting point, not as a validated English result.
The included models and hyperparameters are suggestions based on my experiments,
not universal recommendations.

The code deliberately validates these two model/language combinations. Adding
a language requires appropriate fillers, stopwords, and prompt wording. Adding
a model family requires auditing its tokenizer, chat template, control tokens,
architecture, quantization, LoRA targets, save/reload behavior, and inference
path; it may warrant another explicit trainer.

## Repository contents

- `COOKBOOK.md`: setup, data preparation, training, inference, evaluation, and
  the practical lessons behind the pipeline.
- `prepare_data_json.py`: reply-aware, thread-split ChatML preparation.
- `train_mlx_qwen.py` and `train_mlx_kumru.py`: model-family-specific trainers.
- `inference.py` and `mlx_repetition_history.py`: corrected MLX generation and
  the audited full-prompt repetition-history handling.
- `chat_tui.py`: the full terminal client adapted to public paths and
  pseudonyms.
- `serve_chat.py` and `web/`: a localhost browser interface using the same
  inference engine.
- `benchmark/`: human-anchored evaluation and repetition/message-block
  diagnostics.
- `configs/` and `examples/`: suggested configurations and invented sample
  input.

## How to use it

Follow [COOKBOOK.md](COOKBOOK.md). It contains the model download, environment,
data-preparation, preflight, training, chat, and evaluation commands in order.
The README intentionally does not duplicate those commands, so there is one
place to keep the executable recipe current.

The broad workflow is:

1. Choose `tr` or `en` in `settings.yaml`.
2. Create the ignored local participant map and prepare an exported chat.
3. Run the matching trainer's data preparation and preflight before training.
4. Test the trained adapter through the terminal or browser, then evaluate it
   against held-out real continuations.

## Tested constraints

Training and inference were tested only on Apple Silicon macOS with MLX/Metal.
The demonstrated envelope was a 16 GB M1 Pro, a quantized 2B model, LoRA, batch
size 1, gradient accumulation 4, 512-token examples, gradient checkpointing,
and one heavy MLX job at a time. Linux, Windows, Intel Mac, CUDA, CPU-only
training, and smaller-memory machines have not been validated here.

The long-run commands use the macOS-only `caffeinate -dimsu`. Qwen's preflight
checks the static configuration, tokenizer, and prepared rows. Kumru's preflight
also performs one Metal optimizer update and a save/reload generation check.
Neither guarantees that a full 25k run will fit or finish uninterrupted.

The repository provides corrected MLX inference. It does not include GGUF
weights, llama.cpp binaries, or cross-platform packaging tools.

## Privacy boundary

Only use conversations you are entitled to process and have permission to use.
Keep participant mappings, raw and prepared chats, outputs, adapters, weights,
generation logs, credentials, and private Git history outside the repository.
Removing direct identifiers does not automatically make trained weights safe to
publish.

## License

The repository is licensed under the [Apache License 2.0](LICENSE).
