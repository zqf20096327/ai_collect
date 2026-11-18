# Wafer Map Defect Classifier

**A CNN-style pipeline with no backprop, for sorting semiconductor wafer maps into defect patterns.**

ES 335 (Machine Learning) course project by **Rishi Kumar** and **Satyam Suman**.

- **Project website:** https://kernel-trojan.github.io/WaferMap-Defect-Classifier (an interactive walk-through of
  everything below)
- **Data:** [WM-811K on Kaggle](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map) (not included in this repo)
- **License:** [MIT](LICENSE)

---

## Contents

1. [At a glance](#at-a-glance)
2. [The question](#the-question)
3. [The data](#the-data)
4. [The method](#the-method)
5. [How we kept the test honest](#how-we-kept-the-test-honest)
6. [Results](#results)
7. [Limitations](#limitations)
8. [Getting started](#getting-started)
9. [Reproducing every result](#reproducing-every-result)
10. [Repository structure](#repository-structure)
11. [What each output file holds](#what-each-output-file-holds)
12. [The website](#the-website)
13. [Troubleshooting](#troubleshooting)
14. [Team, AI use and credits](#team-ai-use-and-credits)

---

## At a glance

Chip factories build hundreds of chips (*dies*) on one silicon wafer. After testing, every wafer gives a
**wafer map**: which dies passed and which failed. The *shape* of the failures (a ring at the edge, a blob in
the middle, a thin scratch) is a clue to what went wrong. We built a small model that names that shape.

| | Macro-F1 on the locked test set (95% range) |
|---|---|
| Best simple baseline (random forest on raw pixels) | 0.709 (0.688 to 0.726) |
| **Our pipeline (k-means filters + logistic regression, no backprop)** | **0.765 (0.744 to 0.783)** |
| Textbook CNN trained with backprop (post-hoc reference) | 0.829 (0.812 to 0.843) |

- **We beat every simple baseline:** +0.056 over the best one (+0.038 to +0.074).
- **Turning a wafer doesn't move our score:** 0.766 at 90°, 0.767 at 180°, 0.764 at 270°, against 0.765
  unturned.
- **A real CNN still scores higher.** We reach about 92% of its macro-F1 with 48× fewer learned numbers
  (3,242 against 155,801).

---

## The question

> **Can a one-layer, CNN-style pipeline whose filters are learned without backprop (k-means on small patches)
> sort wafer maps into their defect patterns, and keep working when a wafer comes in rotated or a little
> off-centre?**

| | |
|---|---|
| **One row (unit)** | One wafer map: a grid of dies, 0 = off the wafer, 1 = passing die, 2 = failing die |
| **Target** | One of 9 labels: Center, Donut, Edge-Loc, Edge-Ring, Loc, Near-full, Random, Scratch, none |
| **When a prediction is made** | Right after a wafer is tested, when its map exists |
| **What the model sees** | Only the map. Lot name, die size and wafer index are never features; the lot name is used only to decide which wafers go to training and which to test |
| **Main score** | Macro-F1, the plain average of the 9 per-class F1 scores, so rare patterns count as much as common ones |
| **Limits of the claim** | Labeled wafers only, one public dataset, and a class mix with far more defects than a real fab (see [Limitations](#limitations)). A pattern label is not a root cause |

---

## The data

[WM-811K](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map) (`LSWMD.pkl`, about 2 GB): 811,457 real
wafer maps from Wu, Jang and Chen, *"Wafer Map Failure Pattern Recognition and Similarity Ranking for
Large-Scale Data Sets"*, IEEE Transactions on Semiconductor Manufacturing, 2015. We don't ship the full file;
see [Getting started](#getting-started) for how to download it. The website includes a small sample of its maps
(`site/data/wafers.js`) so its examples work.

**Columns we use:** `waferMap` (the only model input), `failureType` (the label) and `lotName` (only for
splitting). `waferIndex`, `dieSize` and the dataset's own `trianTestLabel` column (typo in the original) are not
used.

What the audit (`python main.py audit`) found, and what we did about it:

| Finding | What we did |
|---|---|
| 811,457 wafers, but only 172,950 (21%) have a label | Use labeled wafers only |
| Of those, 147,431 are `none` (85%) and 25,519 have a defect pattern | Keep every defect wafer + 10,000 random `none` (seed 42) = **35,519 wafers** |
| Wafers come in lots (batches of up to 25) that share machines and conditions | Split by lot, never by single wafer |
| 107 identical maps appear in more than one lot | Lots that share an identical map are grouped together |
| 3 of those identical maps carry two different labels | Kept as-is; a sign the labels have some noise |
| The built-in train/test column is lot-safe but lopsided (88% of Edge-Ring in train, only 25% of `none`) | Not used; we built our own split |
| 338 different map sizes in our sample, 18 to 212 dies on a side | Resize everything to 32×32 by picking the nearest die (no blending) |

Class counts in our sample: Edge-Ring 9,680 · none 10,000 · Edge-Loc 5,189 · Center 4,294 · Loc 3,593 ·
Scratch 1,193 · Random 866 · Donut 555 · Near-full 149.

---

## The method

A normal CNN slides small filters over an image, keeps the strong responses, pools them and feeds a
classifier, learning everything by backprop. We keep the same **structure** but learn each part with a simple,
classic tool. The approach follows Coates, Ng and Lee (AISTATS 2011); our changes are ring pooling and trying
every filter at four rotations.

```
 raw wafer map (any size)
        │
        ▼
 1. Clean up ─── switch off failing dies with no failing neighbour; save 2 summary numbers
        │        (failing share, share removed) so scattered patterns aren't lost
        ▼
 2. Resize ───── 32×32 fail map + 32×32 wafer mask (nearest die, no blending)
        │
        ▼
 3. Patches ──── 200,000 5×5 patches from training wafers, contrast-normalised, ZCA-whitened   [learned]
        │
        ▼
 4. Filters ──── k-means, K = 32: the 32 most common little shapes (no labels, no backprop)     [learned]
        │
        ▼
 5. Convolve ─── slide every filter over the wafer, triangle activation,
        │        each filter tried at 0/90/180/270° and the strongest kept
        ▼
 6. Pool ─────── average inside 4 rings (0-25-50-75-100% of the radius) + the whole wafer
        │        → 32 filters × 5 regions = 160 numbers, + 2 summary numbers = 162 features
        ▼
 7. Classify ─── logistic regression, balanced class weights, temperature scaling             [learned]
        │
        ▼
 one of 9 labels, with an honest probability
```

| CNN part | Normal CNN | Ours | Why |
|---|---|---|---|
| Filters | backprop | k-means on 5×5 patches | finds common shapes without labels |
| Activation | ReLU | triangle (closer than average) | sparse, mostly-zero responses |
| Rotation | learned from data | each filter at 4 turns, keep the best | a scratch is a scratch at any angle |
| Pooling | max-pool into a grid | average inside rings | patterns are about distance from the centre |
| Classifier | dense layers | logistic regression + temperature | simple, fast, calibrated |
| Learned numbers | 155,801 | 3,242 | 48× fewer |

**Baselines** (`scripts/03_baselines.py`), the bar the method had to beat:

| Baseline | What it does | Validation macro-F1 |
|---|---|---|
| B0 majority | always predicts the biggest class | 0.049 |
| B0 uniform | random guess | 0.087 |
| B1 | logistic regression on one number: the failing share | 0.290 |
| B2 logistic | logistic regression on the 1,024 raw pixels | 0.579 |
| B3 | B2 logistic trained with rotated copies | 0.610 |
| **B2 random forest** | random forest on the 1,024 raw pixels | **0.696** |

---

## How we kept the test honest

- **Split by lot.** Lots that share an identical map are joined into groups (10,119 in total). 20% of the groups
  are locked away as the test set: **7,236 wafers from 2,051 lots**. The other 28,283 wafers (8,176 lots) get
  **5-fold stratified, lot-grouped cross-validation**.
- **Leak checks.** `python main.py check` runs 21 checks on the split, including one that points the checker
  at a naive random fold to prove it catches a real leak. With naive random folds, 86% of validation wafers
  would have a lot-mate in training; with ours, 0%.
- **Every learned step is fit on training data only:** patch statistics, ZCA whitening, k-means filters, the
  scaler, the classifier and its temperature.
- **All tuning happened on validation.** The final recipe was written to `experiments/final_config.json` and
  pushed (commit `9bc9713`, 04:39) *before* the test set was loaded; the results came after (`f4d5c32`,
  04:46).
- **The recipe is the default we planned, not the validation winner.** Five options scored higher on validation
  (our recipe 0.753). We kept the plan, and this is why:

  | Option | Validation macro-F1 | Why we didn't switch |
  |---|---|---|
  | Median cleanup instead of isolated-die | 0.784 | Erases 1-die-thin scratches: Scratch F1 0.373 -> 0.337 |
  | K = 64 filters | 0.778 | Twice the features, so twice the model the browser runs |
  | Random filters | 0.769 | Same score range; k-means filters can be shown and read on the site |
  | 64×64 maps | 0.766 | Four times the pixels per wafer for the browser model |
  | k-means + random forest | 0.761 | 300 trees are much bigger and slower to run in the browser than one linear layer |
- **The test set was scored once.** `scripts/05_final_test.py` refuses to run a second time. Two later looks
  are labelled post-hoc: the median-cleanup comparison and the textbook CNN.
- **Error bars** come from redrawing whole test lots 1,000 times (seed 42), because wafers from one lot look
  alike. Two models are compared on the same redraws.

---

## Results

All numbers are on the locked test set unless marked validation. Each is a row in `experiments/log.csv` or a
field in the JSON/CSV files next to it.

| Model | Macro-F1 (95% lot bootstrap) | Accuracy | Calibration error (ECE) |
|---|---|---|---|
| B2 logistic regression on pixels | 0.560 (0.535 to 0.584) | 0.682 | 0.109 |
| B2 random forest on pixels (best baseline) | 0.709 (0.688 to 0.726) | 0.794 | 0.240 |
| **Ours: k-means + logistic regression** | **0.765 (0.744 to 0.783)** | **0.820** | **0.025** |
| Ours with a linear SVM | 0.759 (0.737 to 0.778) | 0.826 | n/a |
| Textbook CNN with backprop (post-hoc) | 0.829 (0.812 to 0.843) | 0.884 | n/a |

- **Against the baselines:** +0.205 over logistic on pixels (+0.179 to +0.229) and +0.056 over the random
  forest (+0.038 to +0.074). The SVM is a tie (+0.006, range −0.008 to +0.020). The pixel baselines see raw
  pixels only (no cleanup, mask or summary numbers), so these gaps measure our whole pipeline, not the filters
  alone.
- **Per class (F1):** Edge-Ring 0.964 · Near-full 0.897 · Random 0.893 · Center 0.864 · none 0.844 ·
  Edge-Loc 0.783 · Donut 0.695 · Loc 0.560 · Scratch 0.388.
- **Rotation:** 0.764 to 0.767 at every quarter turn. In-between angles dip, to 0.673 at 45°. The pixel models
  lose 5 to 12 points at quarter turns, and the CNN 2 to 4.
- **Shift:** sliding every wafer 3 pixels costs us 0.08 (0.683). Pixel models lose 0.28 to 0.41, and the CNN
  0.20, ending below us.
- **Data needs (validation):** with 5% of the training lots we score 0.681, already above logistic regression on
  pixels trained on all of them (0.579).
- **Validation and test agree:** 0.753 on validation, 0.765 on test.
- **Calibration:** our ECE of 0.025 is at the test set's class mix. The random forest has no calibration step,
  so its 0.240 is not a like-for-like contest. At real fab shares calibration would need checking again.
- **Denoise trade-off (post-hoc):** median cleanup would score +0.033 higher (+0.016 to +0.051), but Scratch
  recall falls from 0.711 to 0.596.

**Ablations (validation macro-F1, our recipe = 0.753):** quadrants instead of rings 0.665 · no rotation 0.715 ·
K = 16 0.721 · no cleanup 0.729 · 64×64 maps 0.766 · K = 64 0.778 · median cleanup 0.784.

Figures are in `experiments/figures/`.

---

## Limitations

- **Our test set has far more defects than a real fab.** It is 27% `none`; among labeled real wafers `none` is
  85%. Replaying our error rates at real class shares drops macro-F1 from 0.765 to 0.646, and Scratch precision
  from 0.267 to 0.055 (about 1 Scratch alarm in 18 is real). 19% of clean wafers get flagged as some defect. It
  is a first-pass filter in front of a person, not full automation.
- **Scratch and Loc are weak** (F1 0.388 and 0.560). Through 5×5 windows a short scratch and a small blob look
  alike, and they are each other's most common mistake.
- **The learned filters aren't why it works.** Random 5×5 filters beat our k-means filters on validation by
  +0.015 (+0.007 to +0.023), in all 5 folds. The strength is the structure: sliding filters, four turns, ring
  pooling.
- **Rotation is nearly exact at quarter turns, not perfectly exact.** Whitening learns an average patch that
  isn't rotation-symmetric, so a 90° turn moves the score by about 0.002.
- **Label noise and unlabeled data.** 3 identical maps carry conflicting labels, and 79% of WM-811K has no label,
  so we can't say how the model behaves on that majority.
- **One dataset, one source.** We don't claim it works on another fab's maps without checking.
- **The calibration step ignores lots.** Temperature scaling picks its setting with ordinary 3-fold splits
  inside the training data (`src/models.py`), not lot-grouped ones. This only touches the calibration numbers,
  not F1, and fixing it would mean refitting the frozen recipe, so we leave it as stated.
- **The learning curve's 1% point** contains no Near-full wafers, so it understates that size.

---

## Getting started

### Requirements

- **Python 3.13 or newer** (the project has been run on 3.13 and 3.14).
- About **3 GB of free disk** for the dataset and generated files. Loading the 2 GB pickle also needs a few GB of
  RAM.
- Package versions are pinned in [`requirements.txt`](requirements.txt): numpy, pandas, matplotlib,
  scikit-learn, scipy, joblib, threadpoolctl and torch. torch is used only by the textbook CNN reference.

### 1. Clone and install

```bash
git clone https://github.com/Kernel-Trojan/WaferMap-Defect-Classifier.git
```

```bash
cd WaferMap-Defect-Classifier
```

```bash
python -m venv .venv && source .venv/bin/activate
```

On Windows, activate with `.venv\Scripts\activate` instead.

```bash
pip install -r requirements.txt
```

### 2. Get the data

Download `LSWMD.pkl` from [WM-811K on Kaggle](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map) (you
need a free Kaggle account), unzip it, and put the file at `data/LSWMD.pkl`. It is gitignored.

With the Kaggle command-line tool and an API token, this does the same:

```bash
kaggle datasets download -d qingyi/wm811k-wafer-map -p data --unzip
```

### 3. Check it loads

```bash
python main.py verify
```

This checks the file loads and has the expected row counts. The loader (`src/data_loader.py`) handles the old
Python 2 pickle format for you.

---

## Reproducing every result

Every step is one command through `main.py`. Run them in this order; each one writes its results to
`experiments/` or `splits/`.

| # | Command | What it does | Time |
|---|---|---|---|
| 1 | `python main.py verify` | Checks the dataset loads with the expected row counts | ~1 min |
| 2 | `python main.py audit` | Data audit; builds the 35,519-wafer sample (`data/project_subset.pkl`) | ~1 min |
| 3 | `python main.py splits` | Makes and freezes the lot-grouped split | ~1 min |
| 4 | `python main.py check` | 21 leak checks on the split | seconds |
| 5 | `python main.py baselines` | Baselines B0 to B3 on validation | ~2 min |
| 6 | `python main.py pipeline` | 3 filter types × 4 classifiers on validation | ~17 min |
| 7 | `python main.py tuning` | 7 one-change ablations on validation | ~40 min |
| 8 | `python main.py filter-check` | Paired k-means vs random filters, validation | ~10 min |
| 9 | `python main.py final-test` | **The one test run.** Refuses to run twice | ~2.5 min |
| 10 | `python main.py analysis` | Rotation, shift, learning curve, errors, filters | ~32 min |
| 11 | `python main.py posthoc-median` | Post-hoc median vs isolated cleanup on test | ~1.5 min |
| 12 | `python main.py reference-cnn` | Textbook CNN; training rounds picked on validation, test once | ~25 min |
| 13 | `python main.py real-world-precision` | Precision replayed at real class shares | seconds |
| 14 | `python main.py site-data` | Exports the wafers and numbers the website shows | ~4 min first time |

Times are from a laptop CPU. No GPU is required.

**Notes**

- **Run-once steps.** `final-test` and `reference-cnn` refuse to run once their results file exists. To
  reproduce from zero, delete `experiments/final_test.json` and `experiments/reference_cnn.json` first. Their
  fitted models are saved to `data/final_models.joblib` and `data/reference_cnn.pt` (gitignored).
- **Seeds** are fixed (42) everywhere. k-means and the linear algebra use several CPU threads, so a rerun can
  move a macro-F1 by about 0.001, far less than the fold-to-fold spread (0.004 to 0.014).
- **The split is committed.** `splits/project_splits.csv` holds every wafer's split, fold and group, so you can
  check our split without rerunning anything.

---

## Repository structure

```
WaferMap-Defect-Classifier/
├── main.py                          one entry point: python main.py <step>
├── requirements.txt                 pinned package versions
├── README.md
├── AI_DISCLOSURE.md                 how AI tools were used, and how their output was checked
├── LICENSE                          MIT
│
├── src/                             the reusable pipeline code
│   ├── data_loader.py               reads LSWMD.pkl (old Python 2 pickle); wafer fingerprints for duplicates
│   ├── preprocessing.py             cleanup (isolated / median / none), nearest-die resize, 2 summary numbers
│   ├── features.py                  patches, ZCA whitening, k-means / PCA / random filters, 4 turns, ring pooling
│   ├── models.py                    calibrated logistic regression, ridge, linear SVM, random forest
│   └── evaluation.py                lot bootstrap, calibration error, rotate and shift helpers
│
├── scripts/                         one numbered script per step (run through main.py)
│   ├── data_verifier.py             step "verify"
│   ├── 01_audit.py                  step "audit": the data audit and the 35,519-wafer sample
│   ├── 02_freeze_splits.py          step "splits": lot groups, locked test set, 5 folds
│   ├── check_splits.py              step "check": 21 leak checks
│   ├── 03_baselines.py              step "baselines": B0 to B3
│   ├── 03_pipeline.py               step "pipeline": filter types × classifiers grid
│   ├── 04_tuning.py                 step "tuning": the 7 ablations
│   ├── 05_final_test.py             step "final-test": the one test run
│   ├── 06_analysis.py               step "analysis": rotation, shift, learning curve, errors, filters
│   ├── 07_posthoc_median_test.py    step "posthoc-median"
│   ├── 08_reference_cnn.py          step "reference-cnn": the textbook CNN
│   ├── 09_filter_check.py           step "filter-check": k-means vs random filters
│   ├── 10_real_world_precision.py   step "real-world-precision"
│   └── 11_site_data.py              step "site-data": exports the website's data
│
├── splits/
│   ├── project_splits.csv           every wafer: split, fold, group, lot (35,519 rows)
│   └── split_summary.json           group sizes, fold class counts, duplicate-map stats
│
├── experiments/                     every logged result
│   ├── log.csv                      one row per experiment (the source of truth)
│   ├── audit_summary.json, class_counts.csv
│   ├── phase2_summary.json, phase3_summary.json, filter_check.json
│   ├── final_config.json            the frozen recipe, committed before the test
│   ├── final_test.json, final_test_predictions.csv
│   ├── phase4_analysis.json, test_denoise_comparison.*, reference_cnn*.{json,csv}
│   ├── real_world_precision.csv, site_stats.json
│   └── figures/                     PNG figures for each phase
│
├── site/                            the project website (static: HTML, CSS, JavaScript)
│   ├── index.html                   the page, sections S0 to S17
│   ├── assets/                      styles.css, core.js, story.js, model.js, results.js, bg.js, photos/
│   └── data/                        results.js, wafers.js, model.js (written by step "site-data")
│
├── .github/workflows/pages.yml      deploys site/ to GitHub Pages on every push to main
│
└── data/                            gitignored: LSWMD.pkl, project_subset.pkl, fitted models
```

---

## What each output file holds

| File | Written by | Contents |
|---|---|---|
| `experiments/log.csv` | every step | one row per experiment: split, model, parameters, macro-F1, fold spread, accuracy, notes |
| `experiments/audit_summary.json` | `audit` | row counts, class counts, lot sizes, map shapes, duplicate maps, built-in split check |
| `splits/project_splits.csv` | `splits` | the frozen split: `split`, `fold`, `group_id`, and naive `val_fold_random` folds for the leak check |
| `experiments/final_config.json` | by hand, before the test | the frozen recipe and the reasons for it |
| `experiments/final_test.json` | `final-test` | test macro-F1, accuracy, ECE, per-class F1 and PR-AUC, each with a 95% lot-bootstrap range |
| `experiments/final_test_predictions.csv` | `final-test` | every test wafer's true label and each model's prediction |
| `experiments/phase4_analysis.json` | `analysis` | rotation and shift curves, learning curve, confusion rates, most confident mistakes |
| `experiments/reference_cnn.json` | `reference-cnn` | CNN test scores, training curve, rotation and shift, learned-number counts |
| `experiments/real_world_precision.csv` | `real-world-precision` | precision and F1 at our test mix and at real class shares |
| `experiments/site_stats.json` | `site-data` | every number shown on the website |

---

## The website

`site/` is a static page with no server and no build step. It walks through the project in 19 sections with
interactive figures:

- a preprocessing stepper
- a "split it yourself" demo
- a filter explorer
- a rotation playground
- a confusion-matrix explorer
- a bootstrap demo
- a real-fab precision slider

**View it locally**

```bash
python -m http.server --directory site
```

Then open http://localhost:8000. Opening `site/index.html` directly also works.

**Regenerate its data** after changing any result:

```bash
python main.py site-data
```

This reads `experiments/` and `splits/`, writes `site/data/*.js`, and fills every number into
`site/index.html`, so no number on the page is typed by hand. The page's footer runs a self-check that
compares its JavaScript with the Python pipeline. The browser demos need a fitted model:
`site-data` uses `data/final_models.joblib` when it exists, and otherwise refits the frozen recipe on the
training lots (cached in `data/site_demo_refit.joblib`). The page labels demos that use the refit.

**Publish it on GitHub Pages**

1. In the repository on GitHub, open **Settings → Pages**. Under **Build and deployment → Source**, choose
   **GitHub Actions**. You only do this once.
2. Push to `main`. Any push that changes `site/` runs the **Deploy site to GitHub Pages** workflow
   (`.github/workflows/pages.yml`), which you can also start by hand from the **Actions** tab.
3. The site appears at `https://<owner>.github.io/<repository>/`.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `FileNotFoundError: WM-811K dataset not found` | Put `LSWMD.pkl` at `data/LSWMD.pkl` ([Get the data](#2-get-the-data)) |
| `Run python -m scripts.01_audit first` | Run the steps in order; `splits` needs the sample that `audit` writes |
| `The final test already ran … It only runs once.` | Expected. Delete `experiments/final_test.json` only if you mean to reproduce from zero |
| Scores differ in the third decimal on a rerun | Expected: multithreaded k-means; differences stay far below the fold spread |
| `pip install` fails on torch | torch is only needed for `reference-cnn`; install the CPU build for your platform from pytorch.org, or skip that step |
| Pages deploy fails at `configure-pages` with "Not Found" | Pages isn't enabled: Settings → Pages → Source → GitHub Actions, then re-run the job |
| Pages deploy says the branch is not allowed | Deploy from `main`: merge your branch first |

---

## Team, AI use and credits

**Team:** Rishi Kumar and Satyam Suman. Who built what is on the website's Team section (S17), with links to
the commits.

**AI use:** see [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

**Credits**

- Data: M.-J. Wu, J.-S. R. Jang and J.-L. Chen, "Wafer Map Failure Pattern Recognition and Similarity Ranking
  for Large-Scale Data Sets", *IEEE Transactions on Semiconductor Manufacturing*, 2015
  ([WM-811K on Kaggle](https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map)).
- Method: A. Coates, A. Ng and H. Lee, "An Analysis of Single-Layer Networks in Unsupervised Feature Learning",
  AISTATS 2011 ([paper](https://proceedings.mlr.press/v15/coates11a.html)).
- The four reference photos on the website come from Wikimedia Commons under their own licences (CC BY 2.0,
  CC BY-SA 3.0, CC BY-SA 4.0), credited under each photo.

**License:** MIT, © 2026 Satyam Suman and Rishi Kumar. See [LICENSE](LICENSE).
