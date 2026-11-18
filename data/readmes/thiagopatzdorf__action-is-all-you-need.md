# Action Is All You Need

Small transformers trained from scratch on nothing but records of agents acting, and measured on one thing: do they
emit the right action. Working paper by Thiago Patzdorf and James (Genesis Innovation), 12 November 2026.

**Read the paper: [PAPER.md](PAPER.md).**

| Model | Parameters | Right tool | Right tool and all arguments | Chance |
|---|---|---|---|---|
| A-126 | 125.8 M | 88.2% | 55.4% | 31.5% |
| A-286 | 286.3 M | 90.8% | 63.1% | 31.5% |
| A-537 | 536.9 M | 94.0% | 68.5% | 31.5% |
| A-897 (larger corpus, see below) | 896.5 M | 95.2% | 72.0% | 31.5% |

Held-out trajectories that offer two or more tools; first tool call; greedy decoding; exact string match. Total GPU cost
of the three runs: about US$ 25 on one rented card.

**Update, 14 November 2026.** A fourth model (A-897) finished. It was trained on a larger corpus, so size and data changed
together and it is not a clean fourth point on the curve; the control run has not been done. A new multi-step scorer
(`scripts/regua_passos.py`) scores every call of a trajectory with gold history: A-897 writes the whole call exactly in
61.5% of 579 calls (A-537: 56.7%), and 65% of the calls do not fit in the 2,048-token context at all. Details in section 7
of the paper.

On those same 579 calls we also ran a production general-purpose model and a pair (the small model answers; the general
model answers only when the small one is unsure):

| Who answers | Right tool | Whole call right | Seconds per call |
|---|---|---|---|
| A-897 alone | 95.0% | 61.7% | 0.20 |
| General model alone | 91.9% | 59.8% | 1.03 |
| Pair (general model on 27.6% of the calls) | n/a | 64.8% | n/a |

Differences of two or three points here are within noise, and the format is the small model's home format. The fair
reading is "comparable, five times faster, complementary", not "better". Scripts: `scripts/passos_conf.py`,
`scripts/braco_b.py`, `scripts/pontuar.py`; numbers in `results/pair-*.json`.

## What this is, and what it is not

- A scaling experiment: same data, same recipe, three sizes. Every size improved every measure.
- The models are next-token predictors over agent trajectories. They are not chat models and were never instruction-tuned.
- The test is narrow. It scores the first action only, reads one of the two call formats present in the data, uses 314
  examples, and draws them from the same sources as training. Section 4 of the paper lists every limit.
- Research artifacts. Not evaluated for safety or for production use.

## What is in this repository

| Path | What |
|---|---|
| `PAPER.md` | The paper |
| `results/results.json` | The numbers in the table, machine-readable |
| `logs/` | Raw output of the scorer for each model |
| `scripts/regua_b.py` | The scorer ("régua") |
| `scripts/prep-acao.sh`, `scripts/baixar.sh` | Download and conversion of the corpus |
| `scripts/b4.sh`, `scripts/b5.sh` | Shuffle, training and scoring of the three models |
| `scripts/baixar2.sh`, `scripts/conv2.py`, `scripts/b6.sh` | The fourth run (larger corpus, 896.5 M parameters) |
| `scripts/regua_passos.py` | The multi-step scorer (gold history) |
| `nanochat-commit.txt` | The commit of the nanochat codebase the runs used |

Script comments are in Portuguese. Paths assume a `/workspace` directory on the training machine.

## Data

Toucan-1.5M (Apache-2.0) and SWE-smith trajectories (MIT). The fourth model adds resolved trajectories from
Open-SWE-Traces and SWE-rebench. Nothing proprietary was used.

## Weights

The four checkpoints and the tokenizer are on Hugging Face: https://huggingface.co/jamessleman/action-is-all-you-need

## License

Code and weights: Apache-2.0 (see `LICENSE`). Paper text: CC BY 4.0.

## Citation

```
@misc{patzdorf2026action,
  title  = {Action Is All You Need},
  author = {Patzdorf, Thiago and James},
  year   = {2026},
  note   = {Genesis Innovation working paper}
}
```
