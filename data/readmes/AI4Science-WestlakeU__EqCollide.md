# EqCollide: Equivariant and Collision-Aware Deformable Objects Neural Simulator (SIGKDD 2026 oral)

[![KDD 2026](https://img.shields.io/badge/KDD-2026%20AI4Science-blue)](https://kdd.org/)
[![arXiv](https://img.shields.io/badge/arXiv-2506.05797-b31b1b?logo=arxiv)](https://arxiv.org/abs/2506.05797)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Codebase](https://img.shields.io/badge/Codebase-GitHub-181717?logo=github)](https://github.com/AI4Science-WestlakeU/eqcollide-temp)

Official implementation of **EqCollide** (accepted at **KDD 2026**, AI4Science track, selected as **Oral**).

[Qianyi Chen](https://chen458438184.wixsite.com/biography)<sup>1</sup>, [Tianrun Gao](https://gaotianrun1.github.io/)<sup>2</sup>, [Chenbo Jiang](https://jiang25262.github.io/)<sup>3</sup>, [Tailin Wu](https://tailin.org/)<sup>1</sup>

<sup>1</sup> School of Engineering, Westlake University, Hangzhou, China  
<sup>2</sup> Fudan University, Shanghai, China  
<sup>3</sup> McGill University, Montreal, Canada  

---

## Overview

Simulating collisions of deformable objects is fundamental yet challenging because of solid mechanics and multi-body contact. Classical solvers (FEA, MPM, SPH) are accurate but expensive; many learning-based simulators lack **equivariance** to physical symmetries, **collision-aware** interaction modeling, or **scalability** to compact latent dynamics.

**EqCollide** is an end-to-end **equivariant neural-field simulator** for deformable-object collisions. An equivariant encoder maps Lagrangian mass points (position + velocity) to a small set of latent control points. A **collision-aware equivariant GNN-NODE** evolves those latents. An equivariant neural field decodes **continuous, resolution-independent** velocity fields at query locations. The full pipeline is SE(\(n\))-equivariant under rigid transforms of the input.

On 2D and 3D benchmarks, EqCollide achieves **24.34%–57.62%** lower rollout MSE than the best baseline, generalizes to more colliding objects and longer horizons, and remains stable under group actions on inputs.

### At a glance

| | **2D** | **3D** |
|---|--------|--------|
| **Scenarios** | 2 / 3 / 4 object collisions; comb & geo generalization | Cow collision; block combo; letter / geo generalization |
| **Code** | [`2D/experiments/fitting/`](2D/experiments/fitting/) | [`3D/experiments/fitting/`](3D/experiments/fitting/) |
| **Trajectories** | [`Google Drive/2d/`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) | [`Google Drive/3d/`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) |
| **Checkpoints** | [`eqcollide_r2`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) · [`eqcollide_se2`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) · [`eqcollide_r2_finetune`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) | [`eqcollide3d_cow`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) · [`eqcollide3d_block`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) · [`eqcollide3d_alphabet`](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing) |

---

## Installation

**Requirements:** Linux, Python 3.11, NVIDIA GPU with CUDA 12 (recommended for training and inference).


[`environment.yaml`](environment.yaml) is a full environment export from a tested Linux + CUDA 12 setup.

```bash
# From the repository root
conda env create -f environment.yaml
conda activate EQCOLLIDE
```

**Key dependencies:**

**JAX** (CUDA 12), **Flax/Optax**, **Orbax**, **PyTorch 2.6**, **Hydra**, **NumPy/SciPy/Matplotlib**, **h5py/netCDF4**, **py-pde**.

Set `logging.debug: true` in a config (or pass `logging.debug=True` on the command line) to disable swanlab during local runs.


---

## Data and checkpoints

Simulation trajectories and pretrained weights are hosted on **[Google Drive root](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing)**:



### Google Drive layout

```text
Google Drive/
├── 2d/                              # 2D simulation trajectories (archives)
│   ├── 2obj/
│   │   ├── train.tar.gz             # 2object training split
│   │   ├── test.tar.gz              # 2object test split
│   │   └── infer.tar.gz             # geo / comb inference splits
│   ├── 3obj/
│   │   └── finetune_3obj.tar.gz     # 3object trajectories
│   └── 4obj/
│       └── simulation_4obj.tar.gz   # 4object trajectories
├── 3d/                              # 3D simulation trajectories (archives)
│   ├── 3dcow.tar.gz                 # cow collision
│   ├── 3dblock.tar.gz               # block collision
│   └── 3dalphabet.tar.gz              # letter-shape generalization
└── checkpoints/                     # pretrained Orbax weights
    ├── eqcollide_r2/                # 2D 2object, R² version
    ├── eqcollide_se2/               # 2D 2object, SE(2) version
    ├── eqcollide_r2_finetune/       # 2D 3object finetune
    ├── eqcollide3d_cow/             # 3D cow collision
    ├── eqcollide3d_block/           # 3D block scenario
    └── eqcollide3d_alphabet/        # 3D alphabet generalization
```

Download the archives you need, then extract them locally. 


### Paths to configure

Edit the Hydra YAML for your scenario, or override on the command line:

| Key | When required | Meaning |
|-----|---------------|---------|
| `dataset.traj_sample_path` | Always (train & inference) | Local root of extracted trajectories (see table below) |
| `loading.load_path` | Finetune & inference | Local Orbax checkpoint directory (e.g. `./checkpoints/eqcollide_r2/`) |
| `encoder.encoder_type` | 2D train / inference | `R2` or `SE2`; must match the checkpoint |

**2D training data layout** (under `traj_sample_path`, e.g. `./data/2d/2obj/` after extracting `2d/2obj/train.tar.gz` and `2d/2obj/test.tar.gz`):

```text
train/v/   # per-trajectory velocity .npy files
train/x/   # per-trajectory position .npy files
test/v/
test/x/
```

**2D inference** expects geo / comb splits under `./data/2d/2obj/` (from `2d/2obj/infer.tar.gz`), e.g. `test/generalize_geo/` and `test/generalize_comb/`. Multi-object rollout uses `./data/2d/4obj/` (from `2d/4obj/simulation_4obj.tar.gz`), e.g. `infer/generalize_multi/` (see `experiments/fitting/datasets/pdes.py`).

---

## Training

Training is two-stage in practice: (1) fit the **encoder + equivariant NeF** on reconstruction / velocity matching; (2) train the **collision-aware latent ODE** from `training.ode.train_from_epoch`. Hydra writes runs to `outputs/${dataset.name}/...`.

Entry scripts set runtime flags (`encoder.use`, NCCL defaults, GPU memory fraction) automatically. You normally only need to point `dataset.traj_sample_path` (and `loading.load_path` for finetune).

**2D encoder:** set `encoder.encoder_type` in the Hydra config to choose the latent encoder:

| `encoder_type` | Module |
|----------------|--------|
| `R2`  | `enf/latents/pointnet.py` |
| `SE2` | `enf/latents/se2pointnet.py` |


### 2D

```bash
cd 2D
export PYTHONPATH=.

# 2object (default config)
python experiments/fitting/fit_collision_2objects_encoder.py \
  dataset.traj_sample_path=./data/2d/2obj/

# 3object / 4object finetune (load from eqcollide_r2 checkpoint)
python experiments/fitting/fit_collision_3objects_encoder.py \
  dataset.traj_sample_path=./data/2d/3obj/ \
  loading.load_path=./checkpoints/eqcollide_r2/
python experiments/fitting/fit_collision_4objects_encoder.py \
  dataset.traj_sample_path=./data/2d/4obj/ \
  loading.load_path=./checkpoints/eqcollide_r2/
```

### 3D

```bash
cd 3D
export PYTHONPATH=.

python experiments/fitting/fit_collision_2objects_encoder.py \
  dataset.traj_sample_path=./data/3d/cow/
```

3D training sets `GLOBAL_DIM = 3` and uses the cow-collision config as demo. For inference on block or alphabet scenarios, point `dataset.traj_sample_path` to `./data/3d/block/` or `./data/3d/alphabet/` and load `eqcollide3d_block/` or `eqcollide3d_alphabet/` respectively.

---

## Inference and evaluation

| Task | Script | Config |
|------|--------|--------|
| 2D rollout inference | [`2D/experiments/fitting/inference_collision_2objects.py`](2D/experiments/fitting/inference_collision_2objects.py) | `config_collision_2objects_vel_inference.yaml` |
| 3D rollout inference | [`3D/experiments/fitting/inference_collision_2objects.py`](3D/experiments/fitting/inference_collision_2objects.py) | `config_cow_2objects_vel_inference.yaml` |

**Checkpoint loading:** download the matching folder from [Google Drive/checkpoints/](https://drive.google.com/drive/folders/1OWHDqXzyQJ5J2ENAzv1JJXvYx1uML-CQ?usp=sharing), set `loading.load_checkpoint: true` and `loading.load_path` (e.g. `./checkpoints/eqcollide_r2/`). Inference scripts build inference state, load weights, then roll out with constrained latent ODE solvers. For 2D, set `encoder.encoder_type` to match the checkpoint (`R2` → `eqcollide_r2`, `SE2` → `eqcollide_se2`).

**2D inference modes** (controlled by `inference.run_geo`, `run_comb`, `run_multi` in the config):

| Mode | Flag | Dataset split | `traj_sample_path` | Use case |
|------|------|---------------|-------------------|----------|
| Geometry generalization | `run_geo: true` | `test/generalize_geo/` | `./data/2d/2obj/` | Unseen object shapes |
| Combination generalization | `run_comb: true` | `test/generalize_comb/` | `./data/2d/2obj/` | Unseen object pairings |
| Multi-object rollout | `run_multi: true` | `infer/generalize_multi/` | `./data/2d/3obj/` | multi object collisions |

**2D inference examples:**

```bash
cd 2D
export PYTHONPATH=.
python experiments/fitting/inference_collision_2objects.py \
  dataset.traj_sample_path=./data/2d/2obj/

# 3object multi-object rollout
python experiments/fitting/inference_collision_2objects.py \
  inference.run_geo=False inference.run_comb=False \
  inference.run_multi=True inference.object_num=3 \
  dataset.traj_sample_path=./data/2d/3obj/ \
  loading.load_path=./checkpoints/eqcollide_r2/

```

**Aggregate metrics** from saved rollout `.npy` files:

```bash
python experiments/fitting/evaluation.py --output-dir outputs/... --step 30
```

---

## Citation

If you use this code or build on EqCollide, please cite:

```bibtex
@inproceedings{chen2026eqcollide,
  author    = {Qianyi Chen and Tianrun Gao and Chenbo Jiang and Tailin Wu},
  title     = {{EqCollide}: Equivariant and Collision-Aware Deformable Objects Neural Simulator},
  year      = {2026},
  booktitle = {Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},
  series    = {KDD '26},
  location  = {Jeju Island, Republic of Korea},
  publisher = {Association for Computing Machinery},
  address   = {New York, NY, USA},
  doi       = {10.1145/3770855.3818862},
  url       = {https://doi.org/10.1145/3770855.3818862},
}
```

---

## Related projects

- [enf-jax](https://github.com/Dafidofff/enf-jax) — Grounding Continuous Representations in Geometry: Equivariant Neural Fields
- [enf-pde](https://github.com/david-knigge/enf-pde) — Space-Time Continuous PDE Forecasting using Equivariant Neural Fields  
