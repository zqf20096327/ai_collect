# checkpoint-forensics

**Write-up:** [English](https://01.me/en/2026/11/checkpoint-forensics/) · [中文](https://01.me/2026/11/checkpoint-forensics/) · [Discussion on X](https://x.com/bojie_li/status/2121269954876252648) · [in this repo](docs/article/ARTICLE.md)

PyTorch fills a new model's weights with random numbers using every thread the GPU has, and the thread count differs between GPU generations. Embedding rows that training never touched still hold those numbers, so a published checkpoint records the thread count of the device that initialised it. Will DePue described the method in [Checkpoint forensics](https://unemploymentlabs.com/checkpoint-forensics) (Unemployment Labs). This repository is an independent, clean-room implementation and replication of that article, extended to every open-weight LLM I could download.

A reading is a thread count. It is not a specific chip (H100, H200 and H800 share one count), it describes the device that created the weights rather than the one that trained them, and it says nothing about who owned the hardware, where it was, or whether any rule was broken. See [Limitations](#limitations).

![GPU class read from the weights of open models](docs/article/figures/00_cover.png)

**Full write-up: [docs/article/ARTICLE.md](docs/article/ARTICLE.md).** Every reading, with links to the model and its fingerprint card: [docs/article/READINGS.md](docs/article/READINGS.md).

## Headline numbers

As of 2026-11-13. Regenerate with `python3 scripts/figures_results.py stats`; everything comes from `results/summary.json`.

- 265 models scanned, 185 with a fingerprint, from 125 distinct initialisations (labs re-release weights and fine-tune each other's models).
- By GPU class: 128 Hopper (H100/H200/H800), 27 A100, 15 GB200/GB300, 10 B200/B300, 3 AMD (MI300X, MI250X), 1 V100, 1 Hopper/B200 blend (Kimi-K2.7-Code).
- 25 Blackwell-class releases: 16 initialisations by 12 developers.
- By evidence tier: 152 untouched rows, 28 trained rows, 4 sign-only rows, 1 sibling release.
- 16 fine-tunes carry another developer's initialisation.
- 80 models gave no fingerprint: 25 have no GPU layout in their rows (JAX, legacy Paddle, CPU initialisation, Huawei Ascend, or unused rows a CPU overwrote after training), 11 have no usable rows, 44 have untouched rows that no searched seed regenerates.
- Against the original article: same GPU class on 65 models, neither finds anything on 9, no contradiction. One new reading (Qwen3.8-Flash-Next), one explained difference (Qwen3-235B).

## How it works

![T threads taking turns to fill a tensor](docs/article/figures/07_dealing.png)

1. **Grid-stride layout.** To fill a tensor on a GPU, PyTorch launches `T` threads, where `T` = SMs × threads per SM: 221,184 on A100, 270,336 on H100/H200/H800, 303,104 on B200/B300, 311,296 on GB200/GB300. Thread `t` draws from its own Philox stream `(seed, t)` and writes elements `t, t+T, t+2T, ...`. The same seed on a different GPU puts the same numbers in different places.
2. **Never-trained rows.** Embedding rows of tokens that never occur in training (reserved and padding tokens) keep their initial values, at most rescaled by weight decay. `ckptforensics/preserved.py` finds them by their norm.
3. **Emulation.** `ckptforensics/kernels.cu` reimplements PyTorch's CUDA fill with `T` as a parameter, so any NVIDIA GPU can produce what any other would have written. It is tested bit for bit against real PyTorch for normal, uniform and truncated-normal fills in fp32, bf16 and fp16.
4. **Seed search.** Philox is counter-based, so a candidate (seed, offset, `T`) is checked by computing only the few values being compared. All 2³² seeds under 19 thread counts take seconds on one GPU.
5. **Verification.** The winning candidate must regenerate the untouched rows. Each result reports the cosine, σ above chance, the bit-exact fraction and the best competing thread count.
6. **Evidence tiers.** *Untouched rows*: the published values are regenerated. *Trained rows*: the rows have moved but still correlate with one candidate initialisation and no other, on two disjoint row sets. *Sign-only rows*: weight decay left only the signs, which match one candidate in >99% of positions. *Sibling release*: the reading comes from another upload of the same model.

Models split across GPUs (Megatron per-rank seeds, per-pipeline-stage seeds, sharded tensors at stream offsets) and CPU-initialised models need extra handling; the article covers both.

## Quickstart

Requirements: an NVIDIA GPU (any model; other thread counts are emulated), PyTorch with CUDA, and `nvcc` plus the cuRAND headers. The kernel compiles on first use.

```bash
git clone https://github.com/bojieli/checkpoint-forensics && cd checkpoint-forensics
pip install -U pip && pip install -e .   # editable installs need pip >= 21.3
export CUDA_HOME=/usr/local/cuda   # wherever nvcc and the cuRAND headers live
```

Public repositories need no Hugging Face token. For gated ones (Llama, Gemma and others), accept the licence on the model page and run `huggingface-cli login` or set `HF_TOKEN`.

```bash
ckptf explain                       # the mechanism, with a tiny worked example
ckptf layouts                       # thread totals of the 19 GPU classes tested
ckptf list                          # the fingerprint cards in ckptforensics/cards/
ckptf verify DeepSeek-V4-Flash      # re-derive one card from ~4 MB of public weights
ckptf verify all                    # re-derive every card
ckptf scan Qwen/Qwen2.5-7B --quick  # search a model from scratch
ckptf selftest                      # train a small model on your GPU, then recover it
```

`verify` prints the match under every thread count:

```
seed=953049583 offset=0 std=0.006 init dtype=float32; regenerating 1,888,256 values under 19 GPU layouts:

   threads    cosine  bit-exact  GPU
    303104    0.9999     96.87%  B200 / B300  <==
    233472    0.0016      0.09%  H100 PCIe / H800 PCIe
    ...
    270336   -0.0005      0.09%  H100 SXM / H100 NVL / H200 / H800 SXM / GH200

verdict: initialised with the 303,104-thread layout [B200 / B300]; 96.87% of values bit-exact; 1,374 sigma above chance; next best layout cos=0.0016
REPRODUCED
```

`scan` also takes `--revision`, `--tensor` and `--offsets`. A fingerprint card is a small JSON file: repository, tensor, row ranges, seed, offset, thread count and fill type. Cards exist for the untouched-row readings of the main scan; trained-row readings and special layouts are reproduced by scripts instead (see `results/`).

Tests:

```bash
make test-offline   # about 75 s on one GPU
make test           # adds one network test, a 30 KB range request
```

Library use:

```python
from ckptforensics import emu
w = emu.normal((129280, 4096), 0, 0.006, seed=953049583, device_threads=303104)  # what a B200 would write
hits = emu.search_seeds(positions, values, numel, device_threads=270336)          # brute-force a seed
```

## Reproducing the full results

All scripts run from the repository root with `PYTHONPATH=.` and `CUDA_HOME` set. Weights are read with HTTP range requests, so no model is downloaded whole.

```bash
# 1. Roster: roster/roster.json maps each model name to its Hugging Face repository.

# 2. Quick scan of every roster model (resumable; 8 workers share one GPU)
scripts/workers.sh start 8 --quick --outdir results/quick --offsets 0 --probes 2
scripts/workers.sh stop

# 3. Deep scan of the models the quick scan missed: tensor-parallel shards,
#    per-region search, seed bank × offsets
python3 scripts/deep_scan.py NAME [NAME ...] --skip-done                                   # -> results/deep
python3 scripts/deep_scan.py NAME [NAME ...] --regions --skip-done --outdir results/regions
python3 scripts/deep_scan.py NAME [NAME ...] --bank --skip-done --outdir results/bank

# 4. Merge everything into results/summary.json and results/SUMMARY.md
python3 scripts/summarize.py

# 5. Lineage: which fingerprinted models share trained weights (fine-tunes),
#    then summarize again so `inherits` is filled in
python3 scripts/lineage.py && python3 scripts/summarize.py

# 6. Fingerprint cards and article figures
python3 scripts/make_cards.py && python3 scripts/make_cards_extra.py
python3 scripts/article_figures.py          # cover, results-by-GPU, known answers
python3 scripts/figures_results.py all      # thread counts, coverage, timeline, DeepSeek, seeds
python3 scripts/figures_results.py stats    # the numbers quoted above and in the article
python3 scripts/readings_table.py           # docs/article/READINGS.md
```

Rough cost, measured on one RTX PRO 6000 (96 GB): the quick scan took about 7 GPU-hours in total over the roster, with a median of about 70 s per model, and fetches the end of the vocabulary plus sampled rows (5–10% of an embedding). Verifying a card needs a few MB. Trained-row readings and deep scans fetch whole embeddings, several GB each; the range-request cache (`~/.cache/ckptforensics`, or `CKPTF_CACHE`) grew to about 110 GB over the whole project.

The quick and deep scans do not find everything. Trained-row readings come from `scripts/investigations/partial_*.py` (notes in `results/partial/`), and the hardest models were worked out one by one with `scripts/investigations/unresolved_*.py` (notes in `results/unresolved/`). `summarize.py` merges those accepted readings as well.

## Results guide

- `results/SUMMARY.md`: one row per model, with the reading, seed, rows, σ, bit-exact fraction and the original article's claim.
- `results/summary.json`: the same as a list of records. Fields:
  - `name`, `repo`, `source` (which list the model came from), `article` and `article_threads` (the original article's reading, if any)
  - `status`: `fingerprint` or `no fingerprint found`
  - `threads`, `gpu`, `seed`, `offset`, `tensor`, `shape`, `rows`, `sigma`, `bit_exact`: the reading
  - `evidence`: `untouched rows`, `trained rows`, `sign-only rows` or `sibling release`
  - `init_group`: models with the same value share one initialisation (re-releases, continued training, fine-tunes)
  - `inherits`: for a fine-tune, the other developer's model whose initialisation it carries
  - `agrees`: `true` if the original article reports the same class, `null` if it has no reading; `new_vs_article` and `differs_from_article` mark the two exceptions
  - `reason_kind`, `reason`: for models without a fingerprint, `framework` (not a PyTorch GPU init), `no-rows` or `rows-present` (untouched rows, no seed found)
  - `note`, `init`, `notes` (the investigation folder), `rechecked_on_fresh_rows` (re-verified on rows the finder did not use): provenance of readings that came from the investigations below
- `results/quick/`, `deep/`, `regions/`, `bank/`, `models/`: raw scan output per model.
- `results/lineage.json`: pairwise cosine of trained rows between fingerprinted models.
- `results/partial/`: trained-row (partial survival) sweeps; `sweep.md` and `qwen.md` explain them.
- `results/unresolved/`: investigation notes for models the scans could not read. `NOTES.md` is the running log of what was tried, including negative results; each subdirectory has logs and a `REPORT.md`; `results/unresolved/README.md` explains the layout. `accepted.json` lists the readings that passed review and enter the summary.
- `results/REVIEW.md`: an adversarial review of the readings.
- `ckptforensics/cards/`: the fingerprint cards used by `verify`, one for each of 138 untouched-row readings. The other 14 untouched-row readings use shard-, column-block- or row-shift-specific inits (Megatron tensor parallelism, DTensor/FSDP, vocabulary edits) that the card format does not describe yet; their evidence is in `results/unresolved/`.

## Limitations

- **A thread count is not a chip.** H100 SXM, H200 and H800 share 270,336; B200 and B300 share 303,104; GB200 and GB300 share 311,296.
- **AMD can produce NVIDIA's numbers.** Half of an MI300X (152 of its 304 compute units) presents 311,296 threads, the GB200/GB300 count, and writes the same layout. Only a hardware disclosure separates the two.
- **It can be imitated.** Software can emulate any thread count; this repository does.
- **Initialisation is not training.** Weights can be created on one machine and trained on another.
- **Nothing about ownership, location or legality.**
- **No fingerprint means no information.** Models initialised on a CPU, by JAX or by other generators carry no PyTorch GPU layout, and the search is not exhaustive.
- The B200/B300 label has no disclosed-hardware anchor in this dataset. It rests on NVIDIA's published SM count and on the original article, whose author ran the fill on a B300.

## License

MIT. See [LICENSE](LICENSE).

## Citation

The method and the original readings are from:

> Will DePue, *Checkpoint forensics*, Unemployment Labs, 2026. https://unemploymentlabs.com/checkpoint-forensics

If you use this replication, cite the article above and this repository (Bojie Li, *checkpoint-forensics*, https://github.com/bojieli/checkpoint-forensics).
