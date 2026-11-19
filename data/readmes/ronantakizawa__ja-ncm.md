# ja-NCM: A Japanese Next-Concept Foundation Model

Code I used train a Japanese Next-Concept Foundation Model from scratch, plus same-budget masked diffusion (MDLM) and autoregressive (AR) baselines to compare it with. 

- **Model weights:** https://huggingface.co/ronantakizawa/ja-ncm
- **Paper:** Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation (Khare et al., 2026), https://arxiv.org/abs/2610.14162
- **Upstream code:** HazyResearch/ncm (MIT), vendored in `ncm/`

HazyResearch released NCM checkpoints and evaluation code but not training code. This repository adds the training loops (tokenizer, generator, baselines), data preparation, evaluation and latency benchmarks. The configs reproduce ja-NCM, and the same pipeline works for other languages.

## What is an NCM?

Most language models write one token at a time, so a 128-token passage takes 128 forward passes. An NCM has two parts:

1. **A concept tokenizer**, a multiscale residual VQ-VAE. It compresses a 128-token window into 12 levels of discrete codes: level 1 is a single code for the gist of the passage, and each later level adds detail, up to 128 codes at level 12.
2. **A generator**, a transformer that predicts those codes level by level, coarse to fine, and every code within a level at once.

A passage therefore takes 12 forward passes regardless of its length. After the last level, the tokenizer's decoder turns the codes back into text.

## ja-NCM results (Japanese, one H100)

Every model was trained on the same data (FineWeb-2-Edu-Japanese, llm-jp-3 vocabulary) with the same budget (100k steps × 512 × 128 = 6.55B tokens).

| Measure | NCM (24×1024, 12 steps) | Diffusion, same size | Autoregressive |
|---|---|---|---|
| Gen-PPL at matched entropy (lower is better) | 300 | 313 at 16 steps, 121 at 128 steps | 52 (12×768) |
| ms per 128-token sequence, batch 16, CUDA graphs | 6.1 | 14.9 at 16 steps, 119 at 128 steps | 34.7 (same size) |
| en→ja COMET-22, mean of 4 test sets | 70.6 | 76.5 at 32 steps | 77.3 (12×768) |

- **Speed:** at equal quality NCM is 2.4× faster than a same-size diffusion model and 5.7× faster than a same-size AR model at batch 16. Its lead over AR shrinks as the batch grows (8.6× at batch 1, 2.0× at batch 128).
- **Quality:** under this repository's scoring, diffusion overtakes NCM at 128 steps and AR is best overall. On the paper's English LM1B setup, the NCM-vs-diffusion ranking depends on the scoring protocol (see "Evaluation" below).

## Install

```bash
python -m venv .venv
.venv/bin/pip install -e ".[ja,dev]"      # editable install: jancm needs the source tree for the vendored ncm/
.venv/bin/python -m pytest -q             # 44 CPU tests, about 10 s
```

The `ja` extra adds MeCab (fugashi) for Japanese BLEU and ROUGE. `requirements*.txt` pin the same versions if you prefer `pip install -r`. COMET runs in its own environment (`requirements-comet.txt`) because it pins older numpy and transformers.

**Docker (GPU):** the image matches the environment used for ja-NCM: Ubuntu 24.04, Python 3.12, torch 2.14.1 with CUDA 13.0, on H100s. The host needs an NVIDIA driver for CUDA 13.0 (R580 or newer) and the NVIDIA Container Toolkit.

```bash
docker build -t ja-ncm .
docker run --gpus all --ipc=host --rm -it -v $PWD/data:/work/data -v $PWD/runs:/work/runs ja-ncm
```

All trainers are multi-GPU data parallel through `torchrun`:

```bash
TR="python -m torch.distributed.run --standalone --nproc_per_node 8"   # inside the venv or the container
```

`batch_size` in a config is the global batch; gradient accumulation makes up the difference, so a config gives the same optimisation on 1, 8 or 16 GPUs. Add `--resume auto` to continue from `<out_dir>/last.pt` after an interruption.

## Train a Japanese NCM (the ja-NCM recipe)

The order matters: a new tokenizer invalidates every generator trained on it.

```bash
# 1. Data (CPU). prepare_summ.py first: it writes the XL-Sum evaluation URLs that prepare_corpus.py excludes.
O=data/phase_b_v3
python scripts/prepare_summ.py   --config configs/phase_b_v3/ja_summ.yaml      --out $O/summ
python scripts/prepare_corpus.py --config configs/phase_b_v3/ja_tokenizer.yaml --out $O/corpus \
    --skip-urls $O/xlsum_eval_urls.txt --workers 40
python scripts/prepare_data.py   --config configs/phase_b_v3/en_ja.yaml --direction en-ja --out $O/en_ja

# 2. Concept tokenizer, then its gate (full-hierarchy token reconstruction >= 95%)
$TR scripts/train_tokenizer.py --config configs/phase_b_v3/ja_tokenizer.yaml
python scripts/gates.py tokenizer runs/phase_b_v3/ja_tokenizer

# 3. Unconditional generator (24x1024, about 19 h on 8x H100)
$TR scripts/train_ncm.py --config configs/phase_b_v3/ja_uncond.yaml

# 4. Fine-tunes: English->Japanese translation, and summarisation (XSum-style pre-train, distilled summaries, XL-Sum)
$TR scripts/train_ncm.py --config configs/phase_b_v3/en_ja.yaml
$TR scripts/train_ncm.py --config configs/phase_b_v3/ja_uncond_xsum.yaml
$TR scripts/train_ncm.py --config configs/phase_b_v3/ja_summ.yaml
$TR scripts/train_ncm.py --config configs/phase_b_v3/ja_summ_xlsum.yaml
```

Each config inherits from the files named in its `base:` list; `configs/phase_b/` holds the shared defaults and `configs/phase_b_v3/` the final recipe. Data preparation for the full corpus needs about 400 GB of disk and runs best with 40 workers on a 64-vCPU machine.

### Baselines

```bash
$TR scripts/train_mdlm.py --config configs/phase_b_v3/ja_uncond_mdlm_l.yaml   # diffusion, same size as NCM
$TR scripts/train_ar.py   --config configs/phase_b_v3/ja_uncond_ar.yaml       # autoregressive
$TR scripts/train_mdlm.py --config configs/phase_b_v3/en_ja_mdlm.yaml         # conditional diffusion, en->ja
$TR scripts/train_ar.py   --config configs/phase_b_v3/en_ja_ar.yaml           # and ja_summ_ar / ja_summ_xlsum_ar
```

## Train an NCM for another language

1. **Text tokenizer:** set `tokenizer.pre_tokenizer` (a Hugging Face tokenizer id with its EOS and PAD tokens) and `in_vocab_size` in a copy of `configs/phase_b_v3/_llmjp.yaml`. Measure characters per token first: a vocabulary that packs more text into each 128-token window helps.
2. **Corpus:** point `scripts/prepare_corpus.py` at your dataset. Documents are never packed together: each gets EOS and is cut into 128-token windows, so the tokenizer learns the "text, EOS, PAD" layout.
3. **Validate the loops first (recommended):** Stage 0 trains the generator on the paper's LM1B data with the released tokenizer and compares it with the released generator.

   ```bash
   hf download hazyresearch/ncm-checkpoints --include "lm1b/tokenizer.pt" --include "lm1b/small/*" --local-dir artifacts
   hf download hazyresearch/ncm-datasets --repo-type dataset --include "lm1b/*" --local-dir data/upstream
   $TR scripts/train_ncm.py --config configs/stage0/lm1b_small.yaml
   python scripts/gates.py stage0
   ```
4. **Then** run steps 2–4 of the Japanese recipe with your configs, and check the tokenizer gate before training the generator.

## Evaluation

```bash
# Unconditional quality: gen-PPL and entropy; sweep generation.temperature and compare models at matched entropy
python scripts/eval_uncond.py --model ncm  --config configs/phase_b_v3/ja_uncond.yaml --ckpt runs/phase_b_v3/ja_uncond/last.pt \
    --out results/ncm_T0.95.json generation.temperature=0.95
python scripts/eval_uncond.py --model mdlm --ckpt runs/phase_b_v3/ja_uncond_mdlm_l/last.pt --steps 128 --out results/mdlm.json
python scripts/eval_uncond.py --model data --config configs/phase_b_v3/ja_uncond.yaml --out results/data.json

# Translation and summarisation (BLEU, chrF, ROUGE with MeCab, latency); --model ncm | ar | mdlm
python scripts/evaluate.py --model ncm --ckpt runs/phase_b_v3/en_ja/last.pt --lang ja \
    --data-dir data/phase_b_v3/en_ja/test --tests flores,ntrex,kftt,alt

# Latency on one GPU: eager and whole-call CUDA-graph capture, batch 1/16/64
python scripts/bench_latency.py --ncm runs/phase_b_v3/ja_uncond/last.pt --mdlm runs/phase_b_v3/ja_uncond_mdlm_l/last.pt \
    --ar runs/phase_b_v3/ja_uncond_ar/last.pt --modes eager,capture --out results/bench.json
python scripts/check_capture.py --ncm runs/phase_b_v3/ja_uncond/last.pt --mdlm runs/phase_b_v3/ja_uncond_mdlm/last.pt \
    --mdlm-l runs/phase_b_v3/ja_uncond_mdlm_l/last.pt --ar runs/phase_b_v3/ja_uncond_ar/last.pt \
    --out results/capture_check.json   # CUDA-graph replays must match eager generation
```

Notes on comparing models fairly:

- **Matched entropy:** lower temperature lowers gen-PPL while making text less varied, so compare models at the same sample entropy (character entropy across different text tokenizers), interpolating gen-PPL between temperatures.
- **Scoring protocol:** gen-PPL rankings depend on the protocol. `scripts/eval_uncond.py` averages per-sample perplexity with every model sampled plainly. The paper's pipeline (`ncm/scripts/eval_shard.py`, `eval_merge.py`; reproduced for LM1B by `scripts/lm1b_paper_protocol.py`) computes corpus-level perplexity and reads out NCM's tokens with frequency and adjacency penalties. On LM1B, the released NCM scores 93.5 under the paper's protocol (paper: 93.1).
- **Averaged weights:** MDLM checkpoints store both raw and EMA weights. `--mdlm-weights auto` uses EMA only after it has warmed up (step × (1 − decay) ≥ 5). NCM and AR keep no EMA.
- **Same-size baselines:** compare against MDLM and AR models of the generator's size. `scripts/bench_ar_shape.py` times a same-shape AR model with random weights, since decoding time does not depend on the weights.
- **Conditional MDLM:** use MDLM's random reveal order (`generation.mdlm_order: random`, the default). Confidence ordering truncates summaries.

## Layout

| Path | Contents |
|---|---|
| `ncm/` | Vendored HazyResearch/ncm (MIT) with small patches (multi-level reconstruction fix, KV-cache masking, safe checkpoint loading, CUDA-graph-friendly masks) |
| `jancm/` | Training objectives (tokenizer and generator corruption, self-correction), data loading, DDP and preemption helpers, MDLM and AR baselines, inference, Japanese metrics |
| `scripts/prepare_*.py` | Corpus windows, summarisation data and translation pairs, with decontamination against the test sets |
| `scripts/train_tokenizer.py`, `train_ncm.py`, `train_mdlm.py`, `train_ar.py` | Trainers (all `torchrun`) |
| `scripts/eval_uncond.py`, `evaluate.py`, `score_comet.py`, `eval_external.py` | Unconditional and conditional evaluation |
| `scripts/bench_latency.py`, `bench_ar_shape.py`, `check_capture.py` | Latency benchmarks and replay checks |
| `scripts/gates.py`, `stage0_reference.py`, `check_tokenizer.py`, `lm1b_paper_protocol.py` | Validation against the released checkpoints, tokenizer gate, paper-protocol scoring |
| `scripts/translate.py`, `record_trajectories.py` | Generation, including the coarse-to-fine trajectory after each level |
| `scripts/hf_upload.py` | Uploads a checkpoint to a private Hugging Face repo (configs are scrubbed of machine-specific settings) |
| `configs/` | `phase_b_v3/`: the ja-NCM recipe. `phase_b/`: shared defaults. `stage0/`: LM1B validation. `ja_en_*.yaml`: fine-tuning the released WMT14 NCM on ja→en |
| `tests/` | CPU tests, including a 2-process DDP check |

## Known limitations

- The NCM training loop is a reimplementation; HazyResearch's training code is unreleased. On LM1B it matches the released generator under this repository's scoring (1.01×) and is 1.28× worse under the paper's protocol.
- The ja-NCM results come from one training run per model.
- Japanese evaluation uses llm-jp-3-1.8b as the only gen-PPL scorer.

## Data licences

FineWeb-2-Edu-Japanese (ODC-By), llm-jp-3 tokenizer vocabulary (LLM-jp), JapaneseSummarization-FW2EduJa-Distill (Apache-2.0), XL-Sum ja (CC BY-NC-SA 4.0), KFTT (CC BY-SA 3.0), Mitsua Wikidata (CC0), Tatoeba (CC BY 2.0 FR), ALT (CC BY 4.0); FLORES+ and NTREX-128 for evaluation. Models trained on share-alike or non-commercial data inherit those terms.

## License

MIT (see `LICENSE`). `ncm/` is HazyResearch/ncm, also MIT (`ncm/LICENSE`).
