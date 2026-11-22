# lfm3-cpt

Continued pre-training (CPT) of [LiquidAI LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) on raw Turkish text with
TRL + LoRA, turned from the Liquid cookbook notebook into a CLI project. It has a live Rich training dashboard,
metric logging, before/after evaluation, hardware profiles and tests.

The recipe is the notebook's. You train on Turkish Wikipedia. Perplexity is measured on held-out Wikipedia and on
out-of-distribution FineWeb-2 web pages. Grammar is checked with the TurBLiMP minimal-pair benchmark, before and after
training. At the end the adapter is merged into a standalone checkpoint.

An optional **second stage** then instruction-tunes the CPT model on Turkish conversations (SFT), so it not only
knows more Turkish but also answers in it. See [Stage 2](#stage-2-optional-turkish-instruction-tuning-sft).

**Other languages and periods.** Turkish is the default, not a limit. Stage 1 can train on your own text files
instead of Wikipedia, with:
- whole-file evaluation holdout and weighted mixing of related languages
- Unicode normalization and stripping of niqqud, cantillation, harakat or macrons
- a grammar test from your own minimal pairs
- a tokenizer coverage check
- a `rank` command that scores candidate restorations of a lacuna

An `export` command builds large mixed corpora from Hub datasets. Worked setups for Modern Hebrew (a Wikipedia + web + English-replay mix), Classical Latin and Targumic/Samaritan Aramaic are in
[docs/LANGUAGES.md](docs/LANGUAGES.md) and `examples/`.

**→ [QUICKSTART.md](QUICKSTART.md) has the exact commands for every case.**

## Install

Install PyTorch for your GPU **first**, then this package (torch is not pinned to a build in `pyproject.toml`).

**NVIDIA (RTX 3090):**

```bash
python -m venv .venv && . .venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/cu128   # or the CUDA build you use
pip install -e ".[dev]"
```

**AMD Strix Halo (gfx1151, ROCm):** install the ROCm PyTorch build that already works on your machine (an
official `rocm*` wheel or AMD's gfx1151 nightlies), then `pip install -e ".[dev]"`. Before training, check that
`lfm3-cpt info` reports `backend ROCM`, `bf16 True`, and the amount of GPU-visible memory you expect. On an APU that
amount depends on your BIOS/kernel memory split.

## Quick start

```bash
lfm3-cpt info                              # backend, GPU, versions, suggested profile
lfm3-cpt -p rtx3090 prepare                # stream + cache the corpora in data/tr (once)
lfm3-cpt -p rtx3090 train --merge          # baseline eval → train → final eval → merge
lfm3-cpt report runs/lfm3-1.7b-cpt-tr      # before/after table again, any time

# optional stage 2
lfm3-cpt -p rtx3090 sft --merge            # Turkish SFT on top of the CPT model
lfm3-cpt chat                              # talk to the result
```

Or both stages in one go: `lfm3-cpt -p rtx3090 train --sft --merge`.

On the Strix Halo use `-p strix-halo`. For a smoke test on any machine, use
`-p cpu-debug --set model_id=<small local model>`.

## Commands

| command | what it does |
|---|---|
| `info` | CUDA/ROCm detection, memory, bf16/TF32, library versions, suggested profile |
| `show-config [--toml]` | resolved config; `--toml` output can be saved and passed back with `-c` |
| `prepare [--sft]` | prepares and caches stage-1 data (Hub or your files), minimal pairs, SFT data; checks the tokenizer |
| `train` | full pipeline with live dashboard; `--resume`, `--merge`, `--sft`, `--skip-baseline`, `--max-steps`, … |
| `evaluate [MODEL]` | held-out/OOD perplexity + minimal pairs for a base, adapter or merged model; `--json-out` |
| `merge ADAPTER` | exact merge into a fresh bf16 base (CPU by default); `--push-to-hub REPO` |
| `generate [MODEL]` | continue prompts (`--prompt`) for a qualitative check; `--chat` uses the chat template |
| `sft` | stage 2: Turkish instruction tuning on top of the CPT model (or `--from base` / a path) |
| `chat [MODEL]` | interactive multi-turn chat; defaults to the run's SFT model, else its CPT model |
| `export [DATASET]` | stream a Hub dataset (or raw files) into budgeted train/eval JSONL for `train_files`; `--inspect` shows its fields |
| `distill PROMPTS` | have the original model answer prompts (Hub dataset, file, or .txt) and save them as SFT data for `sft_mix` |
| `multiblimp LANG` | minimal pairs for 101 languages (MultiBLiMP, subject-verb agreement) for `grammar_files` |
| `cloze build` / `cloze score` | gap-filling benchmark: restore a masked word among plausible alternatives; build once, score many models on the same items |
| `restore` | propose and rank fillers for a lacuna: letter count, legible letters (`נ??עין`), model proposals and corpus words, ranked with the text on both sides |
| `sft-source taco` / `parallel` | raw data → chat examples: TaCo-translated Alpaca (target-language answer only), translation requests from a parallel corpus |
| `languages` | right answer language per data source (judged by the reference), for one or more SFT runs |
| `clean` | remove OCR garbage, boilerplate and ruined documents from JSONL corpora (any language); `--dry-run` reports with examples |
| `pairs` | minimal pairs from any held-out text, for languages without a benchmark |
| `sefaria` | Rabbinic Hebrew from Sefaria's library: one cleaned edition per book, chapters, whole tractates held out, optional minimal pairs ([docs/RABBINIC.md](docs/RABBINIC.md)) |
| `tokenizer-check [FILES]` | how well the tokenizer covers your text, compared with English, with a recommendation |
| `rank [MODEL]` | rank candidate fillers of a gap (`___`) by model probability: lacunae, conjectures, variants |
| `report RUN…` | summary of one or several finished runs (both stages for a run directory) |

Every config key can be set from any level: `defaults < --profile < -c file.toml < --set key=value < command options`.

```bash
lfm3-cpt -p strix-halo -s train_articles=20000 -s lora_gate_proj=true train --lr 1e-4
lfm3-cpt -p rtx3090 show-config --toml > my-run.toml   # edit, then: lfm3-cpt -c my-run.toml train
```

## Stage 2 (optional): Turkish instruction tuning (SFT)

CPT teaches the model the language; it does not teach it to *answer* in that language. After CPT the model may
still reply in English, or continue your message instead of answering it. A short SFT pass on Turkish
conversations fixes that. The stage follows Liquid's SFT notebook, with the extraction task swapped for chat:
prompt-completion data, loss on the answer only, LoRA r=16 / alpha=32 / dropout 0.05, effective batch 16,
LFM3's non-reasoning mode (`enable_thinking=False`), greedy evaluation with `repetition_penalty=1.1`.

One deliberate difference: 1 epoch at learning rate 1e-4, not the notebook's 2e-4. On Turkish, 2 epochs at
2e-4 made the model *answer* some facts worse than the original did. Ranking showed it still knew them, but its
answers no longer reached them. 1 epoch at 1e-4 got the same gains (answers finished on their own: 23% → 91%)
and left the stage-1 metrics unchanged.

```bash
lfm3-cpt -p rtx3090 sft                         # start from this run's CPT model
lfm3-cpt -p rtx3090 sft --from base -o runs/sft-only   # control: the same SFT without CPT
lfm3-cpt report runs/lfm3-1.7b-cpt-tr runs/sft-only
```

**Where it starts.** `--from cpt` (default) uses `<run>/merged`, merging `<run>/adapter` first (bf16, CPU) if
needed. SFT then trains a fresh adapter on a standalone model instead of stacking adapters. The SFT adapter
records the merged CPT model as its base, so `lfm3-cpt merge <run>/sft/adapter` works. Running `--from base`
into another output dir is the experiment that shows what CPT actually adds.

**Data.** The default is the Turkish part of the [Aya dataset](https://huggingface.co/datasets/CohereLabs/aya_dataset)
(`language_code == "tur"`): about 4,000 human-written prompt/answer pairs, Apache-2.0, with its own test split.
Because it is human-written rather than machine-translated, it is a good fit for teaching *natural* Turkish. Any
other Hub dataset works if it uses one of the common layouts, which are detected automatically: `messages`,
ShareGPT `conversations`, Aya `inputs`/`targets`, Alpaca `instruction`/`input`/`output`, or prompt/response-style
pairs. Otherwise, name the columns with `-s sft_user_column=… -s sft_assistant_column=…`. Multi-turn
conversations are trained on their last assistant turn. Conversations longer than `sft_max_length` are dropped
rather than truncated, exact duplicates are removed, and eval examples that also appear in train are removed.
For a larger, synthetic corpus, try `--dataset turkish-nlp-suite/InstrucTurca --filter "" --max-train 20000`
(CC-BY-SA-4.0, about 2.5M rows; the full file is downloaded once).

**Metrics** (before → after, on held-out conversations):

| metric | what it tells you |
|---|---|
| answer perplexity | how well the model predicts the reference answers (the SFT loss, token-weighted) |
| answers in Turkish / English | language of the generated answers (a dependency-free stopword + letter heuristic) |
| answers finished (EOS) | answers that end on their own before the token limit (vs. rambling or loops) |
| chrF vs reference | rough character-level similarity to the reference; free-form answers can differ and still be good |
| perplexity (Wikipedia, web), TurBLiMP | the stage-1 metrics again: a **forgetting check**, did SFT undo CPT? |

Every answer is written to `sft/generations.jsonl` (prompt, reference, answer before, answer after, detected
languages). Reading 20 of them tells you more than any of the numbers.

SFT keys (all settable with `-s`): `sft_dataset`, `sft_filter_column`/`sft_filter_value`, `sft_system_prompt`,
`sft_max_train`, `sft_num_train_epochs` (1), `sft_learning_rate` (1e-4), `sft_lora_r`,
`sft_max_length`, `sft_gen_samples`, `sft_max_new_tokens`, … (`lfm3-cpt show-config` lists them all). The
hardware profiles set the SFT batch sizes too. There is no default system prompt, so the model learns to answer
in Turkish without being told to.

## Profiles

| profile | rows × accum | eval batch | checkpointing | notes |
|---|---|---|---|---|
| `t4` | 2 × 4 | 2 | on | the original notebook (fp16) |
| `rtx3090` | 4 × 2 | 4 | on | bf16 + TF32 for the fp32 LoRA matmuls |
| `strix-halo` | 8 × 1 | 8 | **off** | plenty of memory, modest compute: trade memory for speed; no pinned memory on an APU |
| `cpu-debug` | 1 × 1 | 1 | on | tiny, 2 steps, fp32 |

All GPU profiles keep the notebook's effective batch of 8 rows × 2,048 tokens per optimizer step, so the
hyper-parameters and results are comparable across machines. If the Strix Halo runs out of GPU-visible memory, use
`-s gradient_checkpointing=true` or a smaller batch.

## Outputs (`runs/lfm3-1.7b-cpt-tr/`)

- `config.toml`: the exact resolved config of the run
- `metrics.jsonl`: every Trainer log line, with perplexities and peak memory
- `baseline.json`: the pre-training evaluation, cached, so `--resume` does not recompute it
- `checkpoints/`: adapter checkpoints every `save_steps` (the last `save_total_limit` are kept)
- `adapter/`: the final LoRA adapter + tokenizer
- `results.json`: config, device, data stats, baseline/final metrics, grammar flips, training stats
- `merged/`: standalone model (with `--merge`)
- `sft/`: stage 2, same layout (`adapter/`, `checkpoints/`, `metrics.jsonl`, `results.json`, `merged/`) plus
  `generations.jsonl`

## Changes from the notebook

- **Exact merge in bf16.** The notebook merged into the model it had trained. On a T4 that model was loaded in
  fp16, so the "merged" checkpoint silently became fp16. `merge` loads a fresh bf16 copy of the base model (on CPU,
  so it never competes with the GPU) and merges with `safe_merge=True`.
- **Crash in the examples loop.** `next(...)` raised `StopIteration` whenever one of the 4 "most improved"
  phenomena had no wrong→right pair, for example when it had not improved at all. `compare_grammar` skips those
  phenomena and also counts pairs that training *broke*.
- **Token-weighted perplexity.** The Trainer's `eval_loss` is an average of per-batch means. Before/after
  perplexity now uses the exact total NLL divided by the total number of tokens, over the same wrapped 2,048-token
  rows as training.
- **OOD tracked during training.** Wikipedia and web pages are both passed as eval sets, so `metrics.jsonl` shows
  both curves, not just before/after.
- **The grammar test leaves the tokenizer alone.** The notebook set `tokenizer.padding_side = "right"` globally.
  Padding is now done by hand, on the right. That matters for LFM3: its causal short convolutions are only safe with
  right padding. Sentences are also sorted by length, so batches carry less padding.
- **LoRA targets are checked** against the model's real module names. Missing ones are reported, instead of
  failing deep inside PEFT.
- **Checkpoints and resume** (`--resume`). The notebook had `save_strategy="no"`.
- **Non-reentrant gradient checkpointing**, the recommended mode with PEFT.
- **Optional `--train-embeddings`.** This is the notebook's "next step" for a new language: the (tied) input
  embedding is fully trained via `modules_to_save` with `ensure_weight_tying`. It adds about 130M trainable
  parameters, so consider a lower `--lr` with it.
- **Cached, reproducible data.** Corpora are stored without EOS (it is added at use time), with a signature of the
  data settings in `metadata.json`. Changing only training settings does not trigger a re-download.

The model, LoRA rank/alpha, target modules, learning rate, schedule, wrapped packing and data sizes match the
notebook by default.

## Tests

```bash
pytest                 # well under a minute on CPU, fully offline (a tiny Llama + BPE tokenizer is built on the fly)
pytest -m "not slow"   # skip the end-to-end training/CLI tests
```

The end-to-end tests run the real pipeline: prepare, baseline, a few LoRA steps, checkpoints, resume, final eval,
merge, and then the `evaluate`/`merge`/`generate`/`report` commands on the result. The stage-2 tests run CPT
without merging, then SFT from the CPT adapter (exercising the automatic merge), resume, the `--from base`
control, `report`, `chat` and merging the SFT adapter. The language tests cover normalization, local corpora
(holdout, upsampling, cache invalidation), minimal-pair files, the tokenizer check, answer-language detection,
local SFT files, and a full local-corpus run followed by `tokenizer-check`, `rank`, `generate` and `evaluate`.
