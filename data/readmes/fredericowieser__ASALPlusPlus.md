<div align="center">

# ASAL++

### Guiding Evolution of Artificial Life Using Vision-Language Models

[Nikhil Baid](https://arxiv.org/search/?query=Baid%2C+Nikhil&searchtype=author) · [Hannah Erlebach](https://arxiv.org/search/?query=Erlebach%2C+Hannah&searchtype=author) · [Paul Hellegouarch](https://arxiv.org/search/?query=Hellegouarch%2C+Paul&searchtype=author) · [Frederico Wieser](https://fredericowieser.github.io/)

[Paper](https://doi.org/10.1162/isal.a.850) · [arXiv](https://arxiv.org/abs/2509.22447) · [ASAL paper](https://arxiv.org/abs/2412.17799) · [ASAL project](https://sakana.ai/asal/) · [Citation](#citation)

Published in **ALIFE 2025: Ciphers of Life — Proceedings of the Artificial Life Conference 2025** (MIT Press).

<img src="assets/method.png" alt="ASAL++ method: alternate CLIP-guided target optimisation with multimodal generation of the next target" width="900">

</div>

## Overview

**ASAL++** extends the supervised-target mechanism in [Automated Search for Artificial Life (ASAL)](https://github.com/SakanaAI/asal) from fixed, human-written objectives to a sequence of targets proposed by a multimodal foundation model. An inner ASAL loop uses CLIP and Sep-CMA-ES to optimise an artificial-life simulation towards a natural-language target. An outer **Evolver Model** observes the resulting video, proposes the next target, and warm-starts the next search from the previous best configuration.

The paper studies two variants in Lenia using Gemma-3-4b-it:

- **Evolved Supervised Targets (EST):** optimise only the latest generated target. EST produces larger morphological changes and higher visual novelty, but weaker continuity.
- **Evolved Temporal Targets (ETT):** optimise the complete target history at sampled rollout times. ETT produces more coherent and interpretable trajectories, but can stagnate in local minima.

The repository contains the paper experiments, ablations, branching “trees of life”, preserved outputs, exploratory notebooks, a pinned JAX ASAL fork, and an experimental PyTorch Lenia implementation.

## Contributions

| Component | ASAL baseline | ASAL++ |
| --- | --- | --- |
| Target source | Fixed prompts supplied before search | A multimodal model proposes targets from rollout history |
| Search structure | One supervised, open-endedness, or illumination search | Repeated warm-started ASAL searches in an autonomous outer loop |
| Temporal control | Human-specified target sequence | EST and ETT generated target trajectories |
| Exploration | Supervised-target, open-endedness, and illumination searches | Iterated target evolution, branching trees, and environmental prompting |
| Implementation | JAX reference implementation | JAX experiments plus experimental PyTorch Lenia/model adapters |

## Method

At outer iteration `i`:

1. Optimise substrate parameters `theta_i` against either the latest target (EST) or the target history (ETT).
2. Render the best simulation as a video rollout.
3. Sample up to `--max_images` rollout frames and pass them, with the relevant prompt history, to the Evolver Model.
4. Generate the next target `p_(i+1)`.
5. Warm-start the next Sep-CMA-ES search from `theta_i` and repeat.

The method is agnostic to the underlying artificial-life substrate provided that it exposes a parameterised simulation and a 2D rendering. The reported experiments focus on **Lenia**. The pinned JAX fork also contains inherited ASAL implementations for Boids, Particle Life, Particle Life++, Particle Lenia, discrete and continuous neural cellular automata, and Life-like cellular automata.

See [`docs/architecture.md`](docs/architecture.md) for the formal objects, interfaces, and code boundaries.

## Results

Paper-scale experiments use nine initial prompts, eight outer-loop iterations, 2,000 inner Sep-CMA-ES steps per iteration, CLIP for visual/text alignment, and Gemma-3-4b-it as the Evolver Model.

| Method | Mean visual OE score | Final − initial OE | Qualitative outcome |
| --- | ---: | ---: | --- |
| EST | `0.052 ± 0.002` | `0.009 ± 0.004` | Greater visual novelty; limited long-range continuity |
| ETT | `0.049 ± 0.002` | `0.002 ± 0.004` | More coherent trajectories; occasional repetition and convergence |

Aggregate `±` values are standard errors across the nine prompt-conditioned runs; each run’s OE summary uses the standard deviation over its eight ASAL++ iterations.

The open-endedness score is `1 − max` cosine similarity between a sampled frame and its earlier frames in CLIP image-embedding space. Higher is more visually novel. The results support **open-ended characteristics**, not indefinite open-ended evolution; the paper discusses model bias, Lenia’s radial symmetry, compute cost, vanishing activations, and limited quantitative benchmarks.

### Selected ETT trajectories

The labels below are the human-written seed prompts, not claims that the final morphology literally depicts the phrase.

<table>
  <tr>
    <th><code>a flower</code></th>
    <th><code>a monkey</code></th>
    <th><code>an extraterrestrial life</code></th>
  </tr>
  <tr>
    <td><img src="assets/examples/ett-flower.gif" width="260" alt="Lenia trajectory seeded by a flower"></td>
    <td><img src="assets/examples/ett-monkey.gif" width="260" alt="Lenia trajectory seeded by a monkey"></td>
    <td><img src="assets/examples/ett-extraterrestrial-life.gif" width="260" alt="Lenia trajectory seeded by an extraterrestrial life"></td>
  </tr>
</table>

## Installation

### Requirements

- Python 3.11 and [uv](https://docs.astral.sh/uv/);
- Git LFS and Git submodule support;
- a CUDA-capable GPU for practical paper-scale runs;
- Hugging Face access to `google/gemma-3-4b-it`;
- FFmpeg for video generation; Graphviz/Pydot for graph rendering.

```bash
git clone --recurse-submodules https://github.com/fredericowieser/ASALPlusPlus.git
cd ASALPlusPlus
bash scripts/setup.sh
source .venv/bin/activate
huggingface-cli login
```

The setup script installs the research environment from `configs/requirements.txt`, installs the `src/` packages in editable mode, and selects a CUDA-enabled JAX build when `nvcc` is available.

A dependency-free structural check is available before downloading model weights:

```bash
python scripts/verify_repository.py
```

## Quick start

The commands below reproduce the structure of one paper run. They download large foundation-model checkpoints and are not lightweight smoke tests.

```bash
# EST: optimise only the newest generated target
python scripts/main_evolutionary_prompts_last_only.py \
  --save_dir analysis/data/runs/est-microbe \
  --substrate lenia \
  --prompts "a microbe" \
  --coef_prompt 1.0 \
  --N 8 \
  --n_iters 2000 \
  --temp 0.1

# ETT: optimise the accumulated temporal target sequence
python scripts/main_evolutionary_prompts_temporal.py \
  --save_dir analysis/data/runs/ett-microbe \
  --substrate lenia \
  --prompts "a microbe" \
  --coef_prompt 1.0 \
  --coef_softmax 0.5 \
  --N 8 \
  --n_iters 2000 \
  --temp 0.1
```

For paper-scale sweeps and branching experiments, see [`docs/experiments.md`](docs/experiments.md).

## Repository layout

```text
.
├── src/                    # JAX submodule, PyTorch implementation, shared utilities
├── scripts/                # search, ablation, analysis, rendering, and setup entry points
├── configs/                # W&B sweeps, dependency list, and prompt sets
├── analysis/
│   ├── data/               # preserved runs, scores, summaries, and checkpoints
│   └── graphs/             # branching trajectories and graph visualisations
├── notebooks/              # tutorials and exploratory notebooks (Git LFS)
├── docs/                   # architecture, experiment map, and reference material
├── assets/                 # method figures and curated README animations
├── pyproject.toml
├── CITATION.cff
└── README.md
```

The committed analysis artefacts are large. Historical configuration snapshots retain the paths recorded during the original runs; current entry points use `analysis/data/` and `analysis/graphs/`. See [`analysis/README.md`](analysis/README.md) for provenance notes.

## Implementation status

- **Canonical paper path:** JAX ASAL inner loop in `src/asal/` with ASAL++ drivers in `scripts/`.
- **PyTorch path:** experimental Lenia-only implementation in `src/asal_pytorch/`. CLIP and Gemma-3 are registered; BLIP-2, CLIP4Clip, and VideoCLIP remain source-level adapters requiring further integration.
- **Notebooks:** exploratory research records; some retain Colab-specific cells and cached outputs.
- **FlowLenia sweep:** retained for provenance, but the currently pinned submodule does not expose the `flenia` identifier required by that historical configuration.

## Citation

```bibtex
@inproceedings{baid2025guiding,
  title     = {Guiding Evolution of Artificial Life Using Vision-Language Models},
  author    = {Baid, Nikhil and Erlebach, Hannah and Hellegouarch, Paul and Wieser, Frederico},
  booktitle = {ALIFE 2025: Ciphers of Life: Proceedings of the Artificial Life Conference 2025},
  publisher = {MIT Press},
  year      = {2025},
  doi       = {10.1162/isal.a.850}
}
```

This work builds on ASAL:

```bibtex
@article{kumar2024automating,
  title  = {Automating the Search for Artificial Life with Foundation Models},
  author = {Kumar, Akarsh and Lu, Chris and Kirsch, Louis and Tang, Yujin and Stanley, Kenneth O. and Isola, Phillip and Ha, David},
  year   = {2024},
  url    = {https://arxiv.org/abs/2412.17799}
}
```

## Acknowledgements and licence status

We thank Laura Ruis for supervision and guidance, Akarsh Kumar for feedback, and Catherine Bacon for editing. The JAX implementation under `src/asal/` is a pinned fork of the ASAL repository and retains its upstream licence.

The surrounding ASAL++ repository does not currently declare a top-level software licence. The paper is available from arXiv under CC BY 4.0; that paper licence does not automatically license the code.
