<div align="center">

<img src="assets/reflector-icon.png" width="112" alt="Reflector logo"/>

<img src="assets/reflector-wordmark.png" width="300" alt="Reflector"/>

**Arrangement-aware harmonic retrieval for sample-based composition**

[Manual](https://austinrockman.com/reflector/manual.html) · [Paper](https://austinrockman.com/research/reflector) · [Download the app](https://github.com/austinrockman/reflector/releases/tag/v1.0.0)

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache_2.0-6AAF92.svg)](LICENSE)

<br/>

<img src="assets/reflector-demo.gif" width="720" alt="Reflector in action: querying a sample library, arranging results on the timeline, and exploring saved sessions in the galaxy view"/>

</div>

---

Reflector is an interactive audio workstation that automates and inspires the process of sample-based composition by
learning the harmonic structure of a sound library and corresponding arrangements. To put the breadth
of the system into perspective: a folder of a thousand samples holds half a million pairs, and every pair would blend
differently under twelve transpositions. Meaning, there are six million potential harmonic relationships,
sleeping in that hypothetical folder. Reflector exposes this latent structure to the producer, allowing for
real-time retrieval as compositions start to take form.

Commercial platforms increasingly treat retrieval as compositional. Splice's Create and
Output's Co-Producer both suggest complementary sounds for an arrangement in progress: your own audio can
seed the search, and the suggestions come from each platform's catalog. Their methodologies are proprietary
and unpublished. Reflector is an experimental take on the same idea for your personal library: it searches
the samples you already own, it is free, and its method is public end to end, from the training data to the
weights that ship in the app.

## What Reflector listens for

Reflector hears pitch. It reads the harmonic content of a sound, which makes it built for tonal
and textural material: pads, keys, strings, synths, guitars, vocals, field recordings with a tonal
center, sound design that carries harmony. Reflector does not currently analyze rhythm or "beat match",
so bring your melodic and textural sounds because there is a universe of potential inside of them.

## Download and documentation

Reflector runs entirely on your machine as a free, signed macOS application. 
You do not need to know anything about machine learning to use it, and I would encourage every 
user to start with the manual to get oriented. For the technically curious, a paper describes the model, 
the training pipeline, and a characterization of the system's retrieval behavior.

Reflector is currently for Apple Silicon machines only. 

- **Download the app:** [Reflector v1.0.0](https://github.com/austinrockman/reflector/releases/tag/v1.0.0)
- **Manual:** [austinrockman.com/reflector/manual.html](https://austinrockman.com/reflector/manual.html)
- **Paper:** [austinrockman.com/research/reflector](https://austinrockman.com/research/reflector)

## Contact 

Reflector is independent and experimental software. If something breaks, if something confuses you, 
or if you have an idea for what it should do next, write to me: [research@austinrockman.com](mailto:research@austinrockman.com)

## An ethical note to users

Modern AI has been trained on the personal data of creators. Reflector uses synthetic audio
for training: everything was generated via synthesis and configured to the needs of the
application. **At no point in this architecture is any copyrighted audio used, and at no point
will it ever be.** The same commitment carries into the app itself: all features run locally, 
and your audio and usage data stay private on your machine, forever.

---

Everything below is the technical account of the training pipeline. You do not need any of this to 
use Reflector. Head over to the download link and the manual to get started.  

## How it works

1. **The oracle.** A hand-designed 12×12 interval-class kernel `K` scores how the pitch-class
   content of two sounds combines when layered: a bilinear form evaluated frame by frame and
   taken best-over-twelve-transpositions. The oracle lives in `trajectory_generator.py`.

2. **Synthetic data (Stage A).** A pitch-class grammar (`theory.py`) generates paired
   chroma-like trajectories, and the oracle labels each pair with a compatibility score and its
   full twelve-way transposition profile.

3. **Rendered audio (Stage B).** Each Stage A trajectory is rendered to audio via additive
   synthesis with randomized effects (`audio_render.py`), then folded back to CQT chroma
   (`chroma_extract.py`), so the encoder learns to recover the oracle's judgment from realistic,
   audio-derived features.

4. **Distillation.** A shared two-tower encoder is trained to approximate the oracle. Stage A supervises 
   with MSE on the score plus a forward-KL term on the transposition profile; Stage B fine-tunes the retrieval 
   geometry directly with InfoNCE, anchored lightly to the oracle. After Stage B the encoder is **frozen**; at retrieval 
   time a dot product between two embeddings stands in for the oracle at interactive speed.

**Representation.** Chroma is a constant-Q transform folded to 12 pitch classes (6 octaves,
36 bins/octave, `fmin` = C1 ≈ 32.7 Hz), power-law compressed (exponent 0.7), at 50 fps over
3-second, 150-frame windows. Training and the app share exactly these settings.

## Repository layout

```
reflector/
├── theory.py                     musical vocabulary: pitch-class sets and chord shapes
├── trajectory_generator.py       the oracle (kernel K) and the paired trajectory generator
├── chroma_extract.py             CQT → 12-D chroma front end (shared by training and the app)
├── audio_render.py               additive synthesis + effects: trajectories → audio (Stage B)
│
├── generate_stage_a_dataset.py   Stage A data: trajectories + oracle labels        → .npz shards
├── generate_stage_b_dataset.py   Stage B data: render Stage A → audio → re-chroma   → .npz shards
│
├── train_stage_a_baseline.py     Stage A: distill the oracle into the encoder (MSE + KL)
├── train_stage_b_retrieval.py    Stage B: retrieval fine-tune on audio chroma (InfoNCE)
│
├── weights/
│   └── checkpoint_best.pt        the frozen encoder shipped in the app (Stage B output)
│
├── requirements.txt
├── THIRD_PARTY_LICENSES
├── LICENSE                       Apache-2.0
├── NOTICE                        attribution carried into derivative works
└── assets/                       README icon + wordmark (not Apache-2.0)
```

### How the pieces connect

```text
theory.py                     pitch-class vocabulary
      │
      ▼
trajectory_generator.py       oracle (kernel K) labels every pair
      │
      ▼
generate_stage_a_dataset.py   → stage_a/   synthetic trajectories + labels (.npz)
      │
      ├───────────────▶ train_stage_a_baseline.py   MSE + KL  → Stage A checkpoint
      │                                                              │
      ▼                                                              │
generate_stage_b_dataset.py   render (audio_render.py) +            │
      │                       re-extract chroma (chroma_extract.py) │
      │                       → stage_b/   audio-derived chroma      │
      ▼                                                              │
train_stage_b_retrieval.py    InfoNCE, initialized from Stage A ◀───┘
      │
      ▼
weights/checkpoint_best.pt    frozen encoder → loaded by the Reflector app
```

## Install

Python 3.11 recommended.

```
pip install -r requirements.txt
```

Stage B audio rendering additionally uses `pedalboard` (GPL-3.0), which is optional and not
installed by default. Run `pip install pedalboard` to enable effect rendering; without it,
Stage B still runs but skips the effects. See [THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES).

## Quickstart

Reproduce the encoder from scratch. `--device` accepts `mps` (Apple Silicon), `cuda`, or `cpu`.

```bash
# 1 — Stage A: synthetic pitch-class trajectories + oracle labels
python generate_stage_a_dataset.py --out stage_a --train 50000 --valid 5000 --test 5000

# 2 — Stage A training: distill the oracle into the encoder (MSE + KL)
python train_stage_a_baseline.py --data stage_a --device mps --epochs 8 --save-dir runs/stage_a

# 3 — Stage B: render trajectories to audio, re-extract CQT chroma
python generate_stage_b_dataset.py --stage-a stage_a --out stage_b --intensity mix

# 4 — Stage B training: retrieval fine-tune (InfoNCE), initialized from Stage A
python train_stage_b_retrieval.py --data stage_b \
    --init-ckpt runs/stage_a/checkpoint_best.pt \
    --device mps --epochs 3 --temperature 0.2 --lambda-compat-mse 0.05 \
    --save-dir runs/stage_b
```

Pass `--help` to any script for the full set of options (dataset sizes, temperatures, loss weights, augmentation, and more).

## Weights

`weights/checkpoint_best.pt` is the frozen encoder that ships in Reflector. It embeds a `(150, 12)` chroma window into a 
128-dimensional unit vector.

## License

Code in this repository is licensed under Apache-2.0. See [LICENSE](LICENSE) for the full terms
and [NOTICE](NOTICE) for the attribution that Apache-2.0 §4(d) carries forward into derivative
works: if you build on this code, keep the contents of NOTICE with it.

The trained checkpoint (`weights/checkpoint_best.pt`) is model output and is distributed under
this repository's license.

**Name and brand assets.** "Reflector", the Reflector wordmark, and the application icon
(`assets/`) are excluded from the Apache-2.0 grant. They appear here so this README can display
them, and they remain the property of Austin Rockman. Section 6 of Apache-2.0 grants no
trademark rights. Forks are welcome and should carry their own name.

**Scope.** This repository is the training pipeline and the encoder it produces. The Reflector
application is separate work and is not published here.

Third-party notices, including the optional GPL-3.0 `pedalboard` dependency, are in
[THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES).

## Citation

```bibtex
@misc{rockman2026reflector,
  title  = {Reflector: Arrangement-Aware Harmonic Retrieval for Sample-Based Composition},
  author = {Rockman, Austin},
  year   = {2026},
  eprint = {2607.22413},
  archivePrefix = {arXiv}
}
```
