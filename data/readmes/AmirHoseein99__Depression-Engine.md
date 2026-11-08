# Depression-Engine

Speech-activity and spectrogram based depression detection on the DAIC-WOZ
corpus. This repository is a refactor of the original research notebooks into
an installable Python package with a command-line interface.

The pipeline has four stages:

1. **Manifest** – scan raw DAIC-WOZ audio/transcripts/COVAREP files and join
   them with a labels file into a single `manifest.csv`.
2. **Speech activity detection (SAD)** – train a CNN + GRU model that predicts
   voiced/unvoiced frames, using the corpus VUV annotations as labels.
3. **Silence analysis** – turn SAD predictions into per-participant silence
   statistics, compare groups with Welch t-tests and permutation tests, and fit
   a small classifier.
4. **Depression detection** – train a 2-D convolutional model on 2-second mel
   spectrogram windows and aggregate window scores per participant.

## Repository layout

```text
.
├── configs/default.yaml          # all pipeline settings
├── src/depression_engine/
│   ├── cli.py                    # argparse subcommands
│   ├── config.py                 # typed config + YAML loading/validation
│   ├── manifest.py               # raw-tree scan, labels, splits, manifest
│   ├── transcripts.py            # transcript parsing and timing features
│   ├── audio.py                  # loading, slicing, windowing, padding
│   ├── vad.py                    # VUV loading, alignment, silence statistics
│   ├── features.py               # MFCCs, mel spectrograms, scaling, caches
│   ├── models.py                 # SAD CNN-GRU, depression CNN, ensemble
│   ├── training.py               # training loops and run artifacts
│   ├── evaluation.py             # metrics, predictions, run evaluation
│   ├── analysis.py               # t-test, permutation test, classifier
│   └── plotting.py               # all figures
├── pyproject.toml
└── .github/workflows/ci.yml
```

Generated data and artifacts are ignored by Git:

```text
data/       # raw data, labels.csv, manifest.csv, feature caches
runs/       # model.keras, scaler.joblib, config.yaml, history, metrics, plots
reports/    # silence analysis outputs
```

## Dataset

This database is part of a larger corpus, the Distress Analysis Interview
Corpus (DAIC) (Gratch et al., 2014), that contains clinical interviews designed
to support the diagnosis of psychological distress conditions such as anxiety,
depression, and post-traumatic stress disorder. These interviews were collected
as part of a larger effort to create a computer agent that interviews people
and identifies verbal and nonverbal indicators of mental illness (DeVault et
al., 2014). Data collected include audio and video recordings and extensive
questionnaire responses; this part of the corpus includes the Wizard-of-Oz
interviews, conducted by an animated virtual interviewer called Ellie,
controlled by a human interviewer in another room. Data has been transcribed
and annotated for a variety of verbal and non-verbal features.

This share includes 189 sessions of interactions ranging between 7 and 33
minutes (with an average of 16 minutes). Each session includes a transcript of
the interaction, participant audio files, and facial features. For more details
refer to the [DAIC-WOZ documentation](https://dcapswoz.ict.usc.edu/wwwutil_files/DAICWOZDepression_Documentation.pdf).

The dataset can be requested at <https://dcapswoz.ict.usc.edu/>.

**DAIC-WOZ data is not bundled with this repository.** Access, licensing, and
redistribution are the user's responsibility. Do not commit dataset files,
labels, or derived features.

## Installation

Python 3.10 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[audio,tf]"
```

Extras:

| Extra   | Provides                                      |
| ------- | --------------------------------------------- |
| `audio` | `librosa`, `soundfile` (feature extraction)   |
| `tf`    | `tensorflow>=2.15` (model training)           |
| `dev`   | `ruff`                                        |
| `all`   | all of the above                              |

The base install (no extras) supports manifest building, transcript parsing,
configuration, and CLI help. Feature extraction requires `audio`; training and
evaluation require `tf`.

## Data layout

`build-manifest` recursively scans either a nested or a flat layout:

```text
data/raw/300/300_AUDIO.wav
data/raw/300/300_TRANSCRIPT.csv
data/raw/300/300_COVAREP.csv
```

```text
data/raw/300_AUDIO.wav
data/raw/300_TRANSCRIPT.csv
data/raw/300_COVAREP.csv
```

Participant IDs are parsed from the numeric file-name prefix, never from
hardcoded path positions. Audio, transcript, and COVAREP files are matched by
suffix and by the `TRANSCRIPT`/`COVAREP` markers in the file name.

### `labels.csv`

Required columns:

```text
participant_id,PHQ8_Score,PHQ8_Binary
```

Optional column:

```text
split        # train | valid | test
```

`PHQ8_Binary` must equal `PHQ8_Score >= 10` (the threshold is configurable).
If `split` is absent, a stratified train/valid/test split is assigned from
`PHQ8_Binary` using the configured seed. Column names can be remapped under
`data.labels_columns` in the config.

### `manifest.csv`

```text
participant_id,split,PHQ8_Score,PHQ8_Binary,audio_path,transcript_path,vad_path
```

Paths are relative to the manifest file (absolute paths are also accepted).
`vad_path` points to the COVAREP file and is optional for the depression task.

## Quickstart

Run from the repository root so relative config paths resolve correctly.

```bash
# 1. Build the manifest (assigns splits when labels.csv has none)
depression-engine build-manifest \
  --raw-root data/raw \
  --labels data/labels.csv \
  --out data/manifest.csv

# 2. Speech activity detection
depression-engine extract --task sad --config configs/default.yaml
depression-engine train   --task sad --config configs/default.yaml

# 3. Silence statistics, group tests, and classifier
depression-engine analyze --task silence \
  --config configs/default.yaml \
  --sad-run runs/sad/<run>

# 4. Depression detection
depression-engine extract --task depression --config configs/default.yaml
depression-engine train   --task depression --config configs/default.yaml

# Recompute metrics for a saved run
depression-engine evaluate --task sad \
  --run-dir runs/sad/<run> --config configs/default.yaml
```

`python -m depression_engine ...` is equivalent to the `depression-engine`
console script. Every subcommand supports `--help`.

## Configuration

`configs/default.yaml` contains every setting. Relative paths are resolved
against the current working directory. The most common values can be overridden
on the command line:

```bash
depression-engine train --task sad --config configs/default.yaml \
  --seed 7 --epochs 20 --batch-size 256 --run-name quick-check
```

Key sections:

- `data` – paths, sample rate, PHQ-8 threshold, split ratios, label columns.
- `sad` – MFCC parameters, VUV column/frame rate, chunk length, model output
  (`frame` or `sequence`), training hyperparameters.
- `depression` – window/hop length, mel parameters, participant-only splicing,
  augmentation, ensemble size, training hyperparameters.
- `analysis` – permutation count, test alternative, classifier, thresholds.
- `run` – run and report roots.

## Artifacts

Each training run writes to `runs/<task>/<run-name-or-timestamp>/`:

```text
model.keras        # best checkpoint
scaler.joblib      # StandardScaler fitted on training data only
config.yaml        # resolved configuration used for the run
history.csv        # per-epoch Keras history
history.png
model_summary.png
metrics.json       # per-split metrics
predictions.csv    # per-participant predictions
roc_curve.png
confusion_matrix.png   # depression runs
```

Silence analysis writes to `reports/silence/<timestamp>/`:

```text
silence_table.csv
welch_ttests.csv
metrics.json
feature_distributions.png
permutation_<feature>.png
confusion_matrix.png
roc_curve.png
```

Feature caches live in `data/cache/sad/<participant_id>.npz` and
`data/cache/depression/<participant_id>.npz`. They record a schema version and
the feature parameters, and are recomputed automatically when the config
changes or when `--force` is passed.

## Methods

### Speech activity detection

- Input: 26 MFCCs plus their first temporal deltas (52 features per frame).
- Labels: the corpus VUV (voiced/unvoiced) column from COVAREP at 100 Hz.
- Model: two 2-D convolutions with batch normalization and ReLU, reshaped to a
  sequence, two GRU layers with dropout, and a sigmoid output.
- Default output is one probability per frame, which is required for
  frame-level AUC and silence analysis. `sad.output: sequence` reproduces the
  original global-average-pooling head.
- Training uses fixed-length chunks (30 s by default) with per-frame sample
  weights so padded frames do not contribute to the loss.

### Silence analysis

- SAD frame probabilities are thresholded into voiced/unvoiced labels.
- Unvoiced runs produce `number_of_silences`, `avg_length_of_silences`, and
  `time_of_silences`.
- Groups are compared with Welch's t-test (`equal_var=False`) and a seeded
  permutation test of the mean difference.
- A scaled logistic-regression (or SVC) pipeline classifies participants from
  the three silence features.

### Depression detection

- Participant speech is spliced from the transcript segments (configurable).
- Audio is split into 2-second windows with a 2-second hop.
- Each window becomes a 32-bin power mel spectrogram.
- Model: three `Conv2D` layers with 2x2 max pooling, flatten, and a sigmoid
  output, trained with SGD (momentum 0.9, Nesterov).
- Window probabilities are averaged per participant for participant-level
  metrics. An optional seeded ensemble averages several models.

## Historical results

The original notebooks reported the following results. They are preserved for
context only: the refactor fixes label alignment, invalid layers, and
train/test leakage, so these numbers are **not guaranteed to reproduce**.

| Metric | Train | Validation | Test |
| ------ | ----- | ---------- | ---- |
| SAD AUC | 0.9457 | 0.9432 | 0.9290 |

The depression notebook reported **0.86 recall on the test set**.

## Reproducibility and fixed defects

- Removed all notebook hosting mounts, absolute hosted paths, shell
  installs, and notebook-only globals.
- Participant IDs are parsed with a regex instead of hardcoded path indices.
- Splits are assigned at the participant level and are disjoint; scalers and
  augmentation are fitted/applied on training data only.
- SAD features and VUV labels are truncated to their common length instead of
  using the original index-slicing alignment logic.
- MFCC deltas are computed along time, not across coefficient channels.
- Invalid `Conv1D` layers on 4-D tensors were replaced with `Conv2D`.
- Hardcoded `(201, 32)` / `(401, 32)` shapes are derived from the config.
- A single mel configuration (`n_fft=400`, `win_length=400`, `n_mels=32`,
  `hop_length=160`) is used for training and inference.
- Ensemble members are built explicitly with seeded initialisation.
- Early stopping and checkpointing always monitor an existing quantity
  (`val_loss` when validation data exists, otherwise `loss`).
- Undefined notebook variables, duplicate cells, unused imports, and the
  deprecated waveform display helper were removed.
- `audiomentations` was replaced with NumPy frequency/time masking and gain
  jitter; the original `SpecChannelShuffle` was a no-op on 2-D spectrograms.

## Known limitations

- DAIC-WOZ is small (189 sessions) and class-imbalanced; results are sensitive
  to the split.
- VUV labels are a proxy for speech activity, not human-annotated silence.
- The historical results came from a single split and cannot be reproduced
  exactly.
- Participant-level splitting prevents direct leakage, but sessions from the
  same person are not deduplicated beyond the participant ID.
- Full training requires TensorFlow and the dataset; neither is included here.

## Development

```bash
pip install -e ".[audio,dev]"
ruff check .
python -m compileall -q src
python -m depression_engine --help
```

There is no automated test suite in this repository. Validate changes with the
commands above and a small synthetic manifest before running full training.

## Links

- Repository: <https://github.com/AmirHoseein99/Depression-Engine>
- DAIC-WOZ documentation: <https://dcapswoz.ict.usc.edu/wwwutil_files/DAICWOZDepression_Documentation.pdf>
- DAIC-WOZ download: <https://dcapswoz.ict.usc.edu/>
