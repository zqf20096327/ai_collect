<div align="center">

# tiny-bayes

**Theorems, not tests.**<br>
Kernel-checked guarantees for a pretrained language model and a neural PDE solver, in Lean 4.

[Paper](https://doi.org/10.5281/zenodo.24346623) · [Pythia-14M](pythia/) · [PINNs](pinn/) · [Build](#build) · [Cite](#citation)

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24346623-blue)](https://doi.org/10.5281/zenodo.24346623)

<img src="docs/overview.png" alt="Both theorems certify from both sides" width="600">

</div>

A trained checkpoint is a finite list of numbers, and those numbers determine one mathematical function. tiny-bayes, by Hassana Labs, defines that function in Lean 4 with Mathlib and proves theorems about it. Every theorem in each folder's `Main.lean`, and every final theorem of `pythia/point/` and `pinn/poisson/`, depends only on `propext`, `Classical.choice` and `Quot.sound`.

## Pythia-14M

[EleutherAI/pythia-14m](https://huggingface.co/EleutherAI/pythia-14m) (revision `cf967c0a9a04383db6f7b1108d86b2962634b4ac`) defined exactly over ℝ: all 14,067,712 parameters as float16 bit patterns, decoded exactly, and the GPT-NeoX forward pass with exact GELU.

On a 32-token prompt, " trained" (token 10166) beats each of the other 50,303 logits by at least 2, and a perturbation of one input embedding of sup norm 37/16384 puts " dataset" (token 10895) ahead of it by at least 1/20.

```lean
theorem actual_frozen_point_pair :
    (∀ j : Fin 50304, j.val ≠ 10166 →
      (2 : ℝ) ≤ CON.logit CON.pythia14m tokens 10166 -
        CON.logit CON.pythia14m tokens j.val) ∧
    ‖witnessVector‖ = (37/16384 : ℝ) ∧
    (1/20 : ℝ) ≤
      CON.logitFrom CON.pythia14m (perturbInput witnessVector) 10895 -
        CON.logitFrom CON.pythia14m (perturbInput witnessVector) 10166
```

[`pythia/point/PointPair.lean`](pythia/point/PointPair.lean)

## Poisson PINN

A trained network N with 16 tanh units for −Δu = f on (0, 1)², with u = 0 on the boundary. For every solution u, the error |N − u| is at most `certU` on the whole closed square Q and at least `certL` at the point `witness`, with certU/certL < 2.52. For the reference solution U the two bounds are 1/30000 and 1/80000.

```lean
theorem frozen_bracket
    (u : ℝ → ℝ → ℝ)
    (hcu : ContinuousOn (fun z : ℝ × ℝ => u z.1 z.2) Q) (hdu : CoordTwoOn u)
    (hbu : ∀ z ∈ Q, Edge z → u z.1 z.2=0)
    (hpu : ∀ x y, x ∈ Ioo (0:ℝ) 1 → y ∈ Ioo (0:ℝ) 1 → -Lap u x y=forcing x y) :
    (∀ z ∈ Q, |N z.1 z.2-u z.1 z.2| ≤ certU) ∧
      certL ≤ |N witness.1 witness.2-u witness.1 witness.2|

theorem frozen_reference_accuracy :
    (∀ z ∈ Q, |N z.1 z.2-U z.1 z.2| < (1:ℝ)/30000) ∧
      (1:ℝ)/80000 ≤ |N witness.1 witness.2-U witness.1 witness.2|
```

[`pinn/poisson/FrozenComplete.lean`](pinn/poisson/FrozenComplete.lean)

## Contents

| Folder | Result | Build |
|---|---|---|
| [`pythia/point`](pythia/point) | a full-vocabulary decision and an adversarial example on a 32-token prompt | 19.5 CPU h |
| [`pythia/exact`](pythia/exact) | exact model, kernel-certified outputs, Bayesian-in-expectation results | 13 min |
| [`pythia/interval`](pythia/interval) | proved-sound interval evaluator, red/blue encoding | 9 min |
| [`pythia/induction`](pythia/induction) | `TripleCert → ¬Claim`, bound of 941 tokens; `CleanCert → ClaimAt 9` | 4 min + 40 s |
| [`pythia/collapse`](pythia/collapse) | repetition theorems for every set of weights | 35 s |
| [`pinn/poisson`](pinn/poisson) | error bound for a trained PINN on the whole unit square | 42.7 CPU h |
| [`pinn/ode`](pinn/ode) | physics-informed networks certified through their residuals | 3 min |

Statements, files and scripts for each folder are in [`pythia/README.md`](pythia/README.md) and [`pinn/README.md`](pinn/README.md). Build times are from scratch with 24 to 40 parallel Lean processes; for `point` and `poisson`, total CPU time.

## Build

Lean v4.27.0-rc1 and Mathlib `fdddb3ea` (`lean-toolchain`, `lake-manifest.json`); `lake exe cache get` fetches a prebuilt Mathlib. Set `LEAN_BIN` to the `lean` binary and `LEAN_BASE_PATH` to the output of `lake env printenv LEAN_PATH`, then:

```sh
python3 tools/project.py build pythia/collapse CE --jobs 8
```

The build command for every folder is in the two folder READMEs. `python3 tools/project.py check <NS> <dir> <tag>` rebuilds a folder from scratch in a fresh workspace, rejects `sorry`, `axiom`, `native_decide` and similar escapes, and prints each theorem of `Main.lean` with the axioms it depends on.

## Citation

```bibtex
@misc{karim2026theorems,
  title     = {Theorems, Not Tests: Kernel-Checked Guarantees for a Pretrained Language Model and a Neural PDE Solver},
  author    = {Karim, Ahmed and Chlon, Leon},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24346623},
  url       = {https://doi.org/10.5281/zenodo.24346623}
}
```

The preprint cites paths as of the tag [`preprint-v1`](https://github.com/leochlon/tiny-bayes/tree/preprint-v1). Its `point/`, `exact/`, `interval/`, `induction/` and `collapse/` are now under `pythia/`, its `poisson/` is `pinn/poisson/` and its `pinn/` is `pinn/ode/`.

## License

CC BY-NC 4.0 (`LICENSE`): free to use and adapt for non-commercial purposes, with attribution to Hassana Labs. Commercial use is not permitted. The pythia-14m parameters (the `W/` and `Bits/` folders under `pythia/`) are EleutherAI's, under Apache 2.0.
