# Efficient Unrolled Networks for Large Scale 3D Inverse Problems (CVPR'2026 - Oral)

[![arXiv](https://img.shields.io/badge/arXiv-Efficient%20Unrolling-b31b1b.svg)](https://arxiv.org/abs/2601.02141)
[![Code](https://img.shields.io/badge/GitHub-Code-blue.svg)](https://github.com/romainvo/efficient-unrolling)
[![Project](https://img.shields.io/badge/Web-Project-ff69b4.svg)](https://romainvo.github.io/efficient-unrolling/)

This repository contains the official code for the paper: <a href="https://arxiv.org/abs/2601.02141">**Efficient Unrolled Networks for Large Scale 3D Inverse Problems**</a> by <a href="https://romainvo.github.io">Romain Vo</a> and <a href="https://tachella.github.io">Julian Tachella</a>, 2026.  

We extend the <a href="https://deepinv.github.io/deepinv/">DeepInverse</a> library with a `PartitionedReconstructor` and `DiagCirculantWrapper` features to make *3D reconstruction* practical at clinical resolutions by:

- **Partitioning the global inverse problem** into overlapping patch-focused subproblems, while keeping a consistent 3D physical forward model. 
- **Approximating expensive normal operators** $A^\top A$ with efficient **diagonal–circulant operators**.  

This README focuses on these core components and on how to run the provided training and approximation scripts. Please refer to  [DATA.md](DATA.md) for details on the expected data layout and on how to prepare the datasets.

**Check out our self-contained notebook [demo_walnut.ipynb](demo_walnut.ipynb) for a quick demo of the core functionalities !** Data and weights are available by pulling data on-the-fly from [huggingface](https://huggingface.co/datasets/romainvo/efficient-unrolling/tree/main).

You can also check out:
- the  [Quick Usage](#quick-usage) section below for instructions on how to run the training and approximation scripts
- the [Core Functionality](#core-functionality) section for more details on the `PartitionedReconstructor` and `DiagCirculantWrapper` features.

## Requirements

[![DeepInverse](https://img.shields.io/github/stars/deepinv/deepinv?label=DeepInverse)](https://deepinv.github.io/deepinv)

All the requirements are listed in [requirements.txt](requirements.txt). We recommend using conda and installing the requirements with:

```bash
conda create --name efficient-unrolling --file requirements.txt
conda activate efficient-unrolling
```

## Core Functionality

### Partitioned Reconstruction

<!-- The **partitioned reconstruction** idea is implemented in [physics/crop.py](physics/crop.py) via `PartitionedReconstructor`, and used by the training scripts. -->

In the paper, we **apply the** `PartitionedReconstructor` to a PGD reconstructor, but the design is generic: you can wrap optimization-based Reconstructor implemented in deepinv (e.g. ADMM, DRS, FISTA) as long as it obeys the standard `forward(y, physics, init=None)`.

Conceptually, for a global inverse problem

$$ y = A x + \varepsilon, $$

we choose a patch extraction operator $S$ and define the partitioned problem:

$$ \tilde y = y - A S_\perp S_\perp^\top x, \quad \tilde A = A S^\top, $$

so that we reconstruct **patches of x** while still using the 3D forward model $\tilde{A}$ consistent with the global operator $A$.

#### Minimal example: wrapping a deepinv reconstructor

This simplified example shows how to construct a `PartitionedReconstructor` around any deepinv reconstructor.

```python
import deepinv as dinv
from physics.crop import PartitionedReconstructor

# Base physics (any deepinv LinearPhysics)
base_physics = dinv.physics.TomographyWithAstra(
  img_size=(501, 501, 501),
  num_angles=100,
  num_detectors=(972, 768),
  geometry_type="conebeam",
  geometry_vectors=traj,  # user-provided
  normalize=False,
)

# Base reconstructor (here PGD with a denoising prior)
denoiser = dinv.models.DRUNet(in_channels=1, out_channels=1, pretrained="download_2d", dim=3)
prior = dinv.optim.prior.PnP(denoiser=denoiser)
base_rec = dinv.optim.PGD(
  stepsize=0.99,
  sigma_denoiser=3e-2,
  trainable_params=[],
  data_fidelity=dinv.optim.data_fidelity.L2(),
  max_iter=3,
  prior=prior,
  unfold=True,
)

patch_size = (8, 128, 128)
img_size = (501, 501, 501)
stride = tuple(max(1, s // 2) for s in patch_size)  # half-overlap

partitioner = PartitionedReconstructor(
  base_reconstructor=base_rec,
  img_size=img_size,
  patch_size=patch_size,
  stride=stride,
  pad_mode="constant",
  init_tiling=False,
)
```
At train time, the partitioner can be used with `partitioner.local_forward(y, physics, patch_indices=patch_indices, context=x)` to train your model to reconstruct patches of the image, where `y`, `x` and `physics`.

At test time, you can use `partitioner.forward(y, physics)` to reconstruct the full image from measurements `y` without needing to specify patch indices, the `context` is computed under the hood if not provided.

You can adapt it to any other deepinv physics class by swapping `base_physics` and the underlying reconstructor (see [train_cbct.py](train_cbct.py) and
[train_mri.py](train_mri.py) for end-to-end examples)

### Diagonal–Circulant Approximation of $A^\top A$

`DiagCirculantWrapper` wraps any `deepinv.physics.LinearPhysics` instance
and replaces expensive calls to $A^\top A$ by a diagonal–circulant
approximation learned from data (internally using
`DiagCirculantOperator`). 

Features:
- Supports **2D and 3D** inputs.  
- Works with both real and complex-valued signals.  
- Can be used in **patch mode** together with `PartitionedReconstructor`.



```python
from physics.structured import DiagCirculantWrapper
from physics.crop import PartitionedReconstructor

# base_physics: any deepinv LinearPhysics (e.g. MultiCoilMRI, TomographyWithAstra)
physics = base_physics.to(device)
reconstructor = PartitionedReconstructor(...)

# operator_norm can be 1.0 for already-normalized operators (e.g. MRI)
operator_norm = 1.0

wrapped_physics = DiagCirculantWrapper(
  physics=physics,
  img_size=physics.img_size,
  scaling=operator_norm,
  device=device,
)

# Optionally enable patch mode if you use patch-wise reconstruction
wrapped_physics.patch(patch_size=patch_size)

# In the training loop, pass learned parameters from the dataset
pred = reconstructor.local_forward(
  y=measurements,
  physics=wrapped_physics,
  init=init,
  patch_indices=patch_indices,
  x_context=x_context,
  fourier_filter=batch["learned_filter"].to(device),
  spatial_mask=batch["learned_mask"].to(device),
)
```

The parameters of the approximations themselves can be produced by
[fit_mcmri_approx.py](fit_mcmri_approx.py) and
[fit_cbct_approx.py](fit_cbct_approx.py).

## Quick Usage

### Training with run_train.py

[run_train.py](run_train.py) is a small CLI wrapper that loads a YAML config and forwards arguments to the appropriate training script. 

To use the *diagonal circulant wrapper* functionality, make sure to set `use_diag_wrapper: true` in the YAML config. You will need to fit the approximations beforehand using the approximation scripts described below.

- MRI (Calgary-Campinas):

    ```bash
    python run_train.py \
    --config configs/partitioned_unrolled_mcmri.yaml \
    --setup mcmri \
    --input_dir /path/to/CC359/Raw-data/Multi-channel/12-channel \
    --mask_dir /path/to/masks \
    --log_dir /path/to/logs \
    --exp_name mri_unr_patch
    ```

- CBCT (Walnut):

    ```bash
    python run_train.py \
    --config configs/partitioned_unrolled_cbct.yaml \
    --setup cbct \
    --input_dir /path/to/Walnut-CBCT \
    --log_dir /path/to/logs \
    --exp_name cbct_unr_patch
    ```

Command-line arguments override values in the YAML config.

### Fitting diagonal–circulant approximations (approximation scripts)

To use the `DiagCirculantWrapper`, you need to fit the approximations beforehand using the provided approximation scripts. These scripts read the raw data, compute the normal operator $A^\top A$ for each sample, and fit a diagonal–circulant approximation to it. 

Once done, you can use `--use_diag_wrapper` in the training scripts and provide the approximation directory `--approx_dir` to automatically load and use these approximations.

- MRI (Calgary-Campinas):

  ```bash
  python fit_mcmri_approx.py \
    --input_dir /path/to/CC359/Raw-data/Multi-channel/12-channel \
    --mask_dir /path/to/masks \
    --output_dir /path/to/mri_approximations \
    --acceleration_rates 5 10
  ```

  This creates per-volume approximations in subfolders like
  `output_dir/Train/approx_R5/` and `output_dir/Val/approx_R5/`, which
  are later consumed via `approx_dir` in [train_mri.py](train_mri.py).

- CBCT (Walnut):

  ```bash
  python fit_cbct_approx.py \
    --input_dir /path/to/Walnut-CBCT \
    --output_dir /path/to/cbct_approximations \
    --num_projs 30 50 100
  ```

  This creates subfolders like `output_dir/approx_30/`, one per
  projection configuration, which are then read by the Walnut dataset
  and [train_cbct.py](train_cbct.py) when `--use_diag_wrapper` is enabled.



## License and Citation

If you use this code or ideas from the paper in your work, please consider citing:

```text
@article{vo2026efficient,
  title   = {Efficient Unrolling for Large Scale 3D Inverse Problems},
  author  = {Romain Vo and Julián Tachella},
  journal = {arXiv preprint arXiv:2601.02141},
  year    = {2026}
}
```