# VidRouteBench

**A benchmark for budgeted text-to-video routing, OPMU (one probe set for many utilities), and a finding:
sampling a weak model several times can beat calling a strong model once.**

[![arXiv](https://img.shields.io/badge/arXiv-2611.28099-b31b1b.svg)](https://arxiv.org/abs/2611.28099)
[![License](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
![status](https://img.shields.io/badge/release-v0.2%20preview-orange.svg)

> **Preview release (v0.2).** Adds the multi-seed sample data, the independent-seed protocol and two runnable
> examples for the new section "Routing over samples" of the paper (arXiv v2). Everything from v0.1 is
> unchanged: `reproduce/reproduce_v1.py` still checks every arXiv v1 number. Videos, the generation/scoring
> pipeline and a leaderboard will follow (see [Roadmap](#roadmap)).

Text-to-video generators differ by two orders of magnitude in price, and a cheap configuration of a strong
model is often good enough for a given prompt. VidRouteBench makes routing across such **arms**
(model x sampling configuration) measurable:

- **16 arms from 7 open families**, measured cost from $0.0025 to $0.298 per clip (121x).
- **1,625 grouped prompts** from VBench, VBench-2.0 and TA-Hard, with 26,928 labelled (prompt, arm, seed) clips.
- **A frozen quality target**, calibrated against human pairwise preferences (68.7% CV accuracy vs 66.2%
  for the best single scorer), plus per-clip scores on 12 raw / 9 identifiable quality dimensions.
- **Repeated seeds** for noise estimation, an **encrypted test split**, and a sealed newest family
  (HunyuanVideo 1.5) for cold-start evaluation.
- **An evaluator that compares a router with the best prompt-agnostic mixture of arms** (the upper convex
  hull of single arms), not with the best single arm.

**No GPU needed.** All clips are already generated and scored. Developing and evaluating a router or a
cold-start method runs on a CPU in seconds to minutes.

![overview](assets/fig_overview.png)

## Finding: sample before you upgrade

Seed-to-seed variation of one (prompt, arm) pair (s.d. 0.42 on the frozen target) is larger than what perfect
per-prompt model choice buys (+0.38). So instead of paying for a bigger model, draw several samples from a
cheaper one and let a small judge (VideoReward, 2B, about $0.0006 per clip) keep the best:

![example](assets/example_sample_vs_switch.png)

*One panel prompt: four samples of Wan2.1-1.3B (50 steps), the one VideoReward prefers is kept, versus one
sample of Wan2.2-A14B at the same price (we show the A14B sample closest to its own 4-seed mean, so the strong
model is not represented by an unlucky seed). One prompt is an illustration, not evidence: over 333 panel
prompts the judge-kept 1.3B sample beats the A14B 4-seed mean on 59% of prompts, and the averages are below.*

| at matched cost (about $0.30 per prompt) | quality (frozen target) | predicted human win rate vs. A14B x1 |
|---|---:|---:|
| Wan2.2-A14B, 1 sample ($0.298) | -0.105 | 50.0% |
| Wan2.1-1.3B, best of 4 ($0.296) | **+0.001** | **52.7%** |

Over budgets $0.01-0.30 the frontier of all (arm, k) points lies +0.058 above the one-sample model frontier
and reaches the same quality for 23.8% less money on average (31.2% less at the quality of the best single arm).

![sampling frontier](assets/fig_sampling.png)

**Routing over (arm, number of samples).** Letting the router choose both, and training it on best-of-k
targets instead of single-sample means, adds up with prompt routing (87 panel dev prompts, evaluation seeds
all different from the training seed; budget shared by all prompts):

| policy | reads prompt | gain over prompt-agnostic hull | predicted win rate |
|---|---|---:|---:|
| prompt-agnostic resampling | no | +0.049 | 51.2% |
| router, one sample | yes | +0.111 | 52.8% |
| router + per-arm best-of-k gain | yes | +0.137 | 53.4% |
| router + predicted per-prompt spread | yes | +0.151 | 53.8% |
| **router trained on best-of-k targets** | yes | **+0.160** | **54.0%** |
| oracle | - | +0.793 | 68.9% |

The mean gain is the same for budget groups of 5, 10, 20 or 40 prompts (+0.152 to +0.160); small groups are
noisier (40% of 5-prompt groups lose to plain resampling, 13% of 40-prompt groups). Drafting at 5-8 denoising
steps to pick a seed and re-rendering it at full steps does **not** pay: every draft-then-refine policy lies
below the plain best-of-k frontier.

```bash
python examples/sample_vs_switch.py                    # per-arm best-of-k table and the matched-cost comparison
python examples/sample_vs_switch.py --prompt p00352    # the prompt in the figure: every arm, every seed
python examples/route_over_samples.py                  # the routing table above, groups of 5/10/20/40/all (CPU, ~3 min)
```

> **Seeds matter for evaluation.** Generating every prompt with the same seed index starts all prompts of an arm
> from the same initial latent, and a router learns that shared perturbation. Trained on seed 0 and evaluated
> on seed 0 the full-label routing gain is 0.224; on independent per-prompt seeds it is 0.155. The examples
> above therefore evaluate on seeds that differ from the training seed; `data/samples/` holds the
> independent-seed clips (seed >= 100 means a per-prompt seed).

## Quickstart

```bash
git clone https://github.com/dayuwang401/VidRouteBench && cd VidRouteBench
python -m venv .venv && . .venv/bin/activate      # Python 3.12 tested
pip install -r requirements.txt

cd harness
python run.py --method profile --cv 5 --no-log     # cold-start recovery of the profile baseline
cd .. && python reproduce/reproduce_v1.py          # all v1 tables, checked against the paper
```

## Tasks

**1. Budgeted routing.** Predict quality for every (prompt, arm), route with
`argmax_a (q_hat - lambda * c_a)`, sweep `lambda`, and report the gain of the routed cost-quality frontier
over the single-arm hull, averaged over 8 budgets.

**2. Cold start.** Each arm in turn becomes the *new* arm. It is labelled on only K in {10, 20, 50} probe
prompts chosen by the method; the other arms keep their labels. We report
`recovery = (gain - gain_excl) / (gain_full - gain_excl)` and the probe cost K x price.

**3. Many utilities.** Scenarios are utility directions `w` over the 9 identifiable quality dimensions
(6 named scenarios, 9 single-dimension corners, 200 Dirichlet samples, `configs/scenarios.json`). A method
should Pareto-dominate the prompt-agnostic hull for as many directions as possible.

## Writing a method

A method is one file in `harness/methods/` with three functions (see `harness/methods/base.py`):

```python
from methods.base import Method as Base

class Method(Base):
    def fit_known(self, ctx):                 # (n_eval, n_known) quality of the known arms on eval prompts
        ...
    def select_probes(self, ctx, k, rng):     # which <= k train prompts to label for the new arm
        ...
    def predict_star(self, ctx, probe, y, d): # (n_eval,) quality of the new arm from its probe labels
        ...
```

Then `cd harness && python run.py --method <name> --cv 5`. The protocol in `harness/protocol.py` and
`harness/run.py` is frozen; methods only see what is in `ctx` plus the probe labels.

## Results in arXiv v1 (and what changed in v2)

Cold start with the router held fixed (Table 4; 5-fold CV is the decision criterion):

| method | recovery, 5-fold | recovery, dev |
|---|---:|---:|
| `mean`: credit the new arm with its probe average | -3.32 | -0.66 |
| `ridge_k`: fit prompt -> quality on the K probes | -2.44 | -0.52 |
| `profile`: regress on known arms' quality | **+0.04** | +0.21 |
| `dimprofile`: per-dimension profile (rejected) | -0.23 | +0.25 |

OPMU over 200 Dirichlet utility directions (Table 5):

| utilities | rule | gain | dominance | dHV |
|---|---|---:|---:|---:|
| oracle (upper bound) | linear | +0.382 | 100% | +0.680 |
| OPMU (multi-output, scalarise afterwards) | linear | **+0.050** | **94%** | +0.110 |
| per-scenario router | linear | +0.045 | 90% | +0.103 |
| OPMU | Chebyshev | +0.043 | 85% | +0.092 |

`python reproduce/reproduce_v1.py` regenerates these and the other tables and writes
`results/v1_reproduction.md`.

**v2 update (full 1,625-prompt matrix):** OPMU 79% dominance (+0.031), per-scenario router 78% (+0.032),
Chebyshev 71% (+0.029), oracle 100% (+0.370). OPMU now matches per-scenario routers rather than beating them;
its advantage is that a new scenario needs no retraining.

> **Note on v1 numbers.** The v1 tables were computed while generation was still running, from three states
> of the same append-only label file: Table 2 (gate) on the first 8 arms, Table 5 on 899 prompts, Tables 1,
> 3 and 4 on the data shipped in `data/gen/`. `reproduce/v1/` holds the row manifests of the two earlier
> states, so each table is reproduced exactly. Re-running the analyses on the full data changes some
> numbers; these updates will appear in v2 together with the corresponding paper revision.

## Repository layout

```
harness/            frozen protocol (protocol.py), evaluation driver (run.py), methods/ (one file per baseline)
scripts/            gate_check.py (Table 2), pareto_eval.py (Table 5, OPMU)
configs/            target.json (frozen quality target + calibration record), utility_basis.json,
                    scenarios.json (215 utility directions), cost.json (GPU price used for $/clip)
data/gen/           VidRouteBench: prompts.csv, arms.csv, labels.csv, features/emb_qwen3.npy
data/rb_human/      VideoGen-RewardBench human labels (12 closed models), used as a human-labelled control
data/test/          encrypted test prompts (test.csv.enc) and their SHA-256; sealed until v2
reproduce/          reproduce_v1.py and the v1 row manifests
examples/           sample_vs_switch.py (weak model x k vs. strong model x 1), route_over_samples.py (routing over (arm, k))
data/samples/       all scored clips over all seeds, the 400-prompt aligned-seed panel, SigLIP2 text embeddings
```

## Data

| file | content |
|---|---|
| `data/gen/prompts.csv` | `prompt_id, split (train 1,220 / dev 405), text, source (vbench / vbench2 / tahard), dims, group` |
| `data/gen/arms.csv` | `arm, family, config (JSON sampling config), usd_per_clip, heldout` |
| `data/gen/labels.csv` | one row per clip: `prompt_id, arm, seed, target, dim_*` (12 raw quality dimensions) |
| `data/gen/features/emb_qwen3.npy` | Qwen3-Embedding-0.6B prompt embeddings, rows aligned with `prompts.csv` |
| `data/samples/labels_multiseed.csv.gz` | every scored clip, all seeds: `prompt_id, arm, seed, target, vr_overall`; seed >= 100 is an independent per-prompt seed; includes three 5-8-step draft arms |
| `data/samples/noise_panel.csv` | 400 prompts (300 train / 100 dev) on which all 16 arms have seeds 0/2/3/4 |
| `data/samples/emb_siglip_text.npy` | SigLIP2-so400m text embeddings, rows aligned with `prompts.csv` (kept out of `data/gen/features/` so v1 results stay bit-identical) |

Prices are our own measured A800 GPU-seconds at $1.5 per GPU-hour, not vendor prices. Prompts are split
by semantic group, so near-duplicate prompts never straddle train and dev.

**Sources and licenses.** Prompt texts come from [VBench](https://github.com/Vchitect/VBench) and
[VBench-2.0](https://github.com/Vchitect/VBench) and from TA-Hard; `data/rb_human` is derived from
[VideoGen-RewardBench](https://huggingface.co/datasets/KlingTeam/VideoGen-RewardBench) (Apache-2.0).
The clips were generated with CogVideoX, Wan 2.1/2.2, LTX-Video, Kandinsky 5 and HunyuanVideo 1.5,
each under its own model license; the clips themselves are not part of this preview.

## Roadmap

- [x] v0.1 preview: data, frozen evaluator, baselines, exact reproduction of arXiv v1
- [x] v0.2 preview: multi-seed samples, independent-seed protocol, routing over (arm, k), runnable examples
- [ ] full v2 tables on independent seeds (gate, router, cold start)
- [ ] human check of judge-selected vs. random samples
- [ ] generated clips on the Hugging Face Hub
- [ ] generation and scoring pipeline (diffusers + VideoReward + SigLIP2), calibration script
- [ ] test-split leaderboard and the sealed HunyuanVideo 1.5 family

## Citation

```bibtex
@article{wang2026vidroutebench,
  title   = {VidRouteBench: A Benchmark for Budgeted Video-Generation Routing},
  author  = {Wang, Dayu},
  journal = {arXiv preprint arXiv:2611.28099},
  year    = {2026}
}
```

## License

Code: [Apache-2.0](LICENSE). Data: see [Sources and licenses](#data).
