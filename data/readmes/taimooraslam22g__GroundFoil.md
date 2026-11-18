# GroundFoil: deep learning for inverted airfoils in ground effect

[![DOI](https://zenodo.org/badge/1454795941.svg)](https://doi.org/10.5281/zenodo.24176980)

**GroundFoil** predicts the flow around **inverted airfoils in ground effect**
(F1 front wings) with a U-Net trained on our own RANS simulations. It builds on
**Thuerey et al., "Deep Learning Methods for Reynolds-Averaged Navier-Stokes
Simulations of Airfoil Flows"** (*AIAA Journal*, 2020), which we first
reproduced on current software: OpenFOAM v2606, gmsh 4 and Docker on Windows
(about 3% test error, as in the paper). The ground-effect simulations are
checked against high-resolution LES (skin friction within 7–8%), wind-tunnel
tests of an F1 wing (downforce gain near the ground within 4%) and finer meshes
(0.04–3%).
Trained on 3,096 of these simulations, the U-Net predicts the flow around 30
airfoils it has not seen with a 0.9% error, against 20% for the free-air
model used as it is. The downforce computed from its pressure is off by
3.9%, with a loss that counts the cells next to the wing more and the
distance to the wing's surface as an extra input (9.9% with neither). On two
wings it has never seen, it predicts the downforce at every ride height
within 4% (the NACA 4412) and within 1.1% (the Tyrrell 026, the F1 wing of
the wind-tunnel tests), and puts its peak at the same ride height as the CFD.
For the downforce alone, smaller models that skip the flow do two to three
times better, and one that predicts the pressure along the wing's surface
also gives the drag, the moment and where the flow separates.

- Thuerey et al.'s paper: https://arxiv.org/abs/1810.08217
- Their code: https://github.com/thunil/Deep-Flow-Prediction (Apache-2.0)

Words used here are explained in the [glossary](docs/glossary.md).

## Workflow

The study in fifteen steps, each with its own page:

1. **[Reproduction](docs/01-reproduction.md):** we first ran the original
   free-air study on current software, to start from a working pipeline and a
   trusted model. Its pressure and velocity errors match the paper's.
2. **[Ground-effect setup and first checks](docs/02-ground-effect-setup.md):**
   the airfoil upside down above a moving ground. Single test cases set the
   number of iterations, the incoming turbulence (checked against
   high-resolution LES) and a faster solver setting.
3. **[Mesh study](docs/03-mesh-study.md):** three rounds, ending with a mesh on
   which the downforce is converged (GCI 0.04%) and skin friction matches the
   LES within 7–8%, and with a convergence test that every run must pass.
4. **[Wind-tunnel validation](docs/04-wind-tunnel.md):** the Tyrrell 026 F1
   front wing at nine ride heights. The downforce it gains near the ground
   matches the tunnel within 4%.
5. **[Airfoil shapes](docs/05-airfoil-shapes.md):** the wind-tunnel case showed
   kinks in surfaces built from sparse points, so we smoothed all the airfoil
   files (1,462 are used).
6. **[Parameter scan](docs/06-parameter-scan.md):** 200 trial runs showed where
   steady RANS converges and set the rules for keeping a run.
7. **[The dataset](docs/07-dataset.md):** 4000 runs (3,436 samples on 1,286
   airfoils), and a test set of 102 samples on 30 airfoils kept out of training.
8. **[U-Net learning curve](docs/08-unet-learning-curve.md):** with 789 samples
   the U-Net predicts airfoils it has not seen with a 1.8% error, against 24%
   for the free-air model as it is.
9. **[Downforce](docs/09-downforce.md):** the downforce from the predicted
   pressure is off by 11%, and by 7.7% with a loss that weights the cells next
   to the wing.
10. **[All the data](docs/10-all-data.md):** with all 3,096 training samples
    and the weighted loss, the downforce error falls to 6.2% and the field
    error to 1.4%. Both still fall as samples are added.
11. **[A new wing](docs/11-naca4412-sweep.md):** the NACA 4412 at 12 ride
    heights. The U-Net, which never saw it, predicts the downforce within 5%
    and puts its peak at the same height as the CFD.
12. **[The F1 wing](docs/12-tyrrell026-sweep.md):** the Tyrrell 026 at the
    tunnel's ride heights. The U-Net gets the shape of the curve but 10–19%
    too little downforce: it misses part of the suction peak.
13. **[The exact wing shape](docs/13-distance-input.md):** the distance to
    the wing's surface as an extra input. Trained from random weights, the
    downforce error falls to 3.9% and the field error to 0.9%. On the
    Tyrrell 026 the downforce is within 1.1% at every ride height. A
    distance computed from the mask does not help: the gain comes from the
    shape finer than the grid.
14. **[The downforce alone](docs/14-downforce-model.md):** a small network
    that predicts only the downforce, from the shape, the ride height, the
    angle and the speed, does better than the U-Net: 1.6% against 3.9% on the
    test airfoils (1.5% against 4.3% compared with OpenFOAM's force). On the
    F1 wing the two tie (1.2%). The U-Net's strength is the flow itself.
15. **[The pressure along the wing](docs/15-surface-model.md):** a small
    network that predicts the pressure and the friction along the wing's
    surface gets the downforce as close as step 14's (1.3%), and also the
    drag (2–3% on the two wings), the moment and where the flow separates.
    On the F1 wing its suction peak is too low, as the U-Net's was.

**Next:** four more batches of 1000 runs (about 6,200 training samples),
then the final versions of the three models with all the data, the learning
curves (with a Gaussian process for the downforce) and both sweeps again;
figures of predicted and simulated flow fields. All commands are in
[How to run it](docs/howto.md).

## What the network learns

![A ground-effect sample: the network's three inputs and the three simulated fields it learns](results/ground_first_sample.png)

*One ground-effect sample: a NACA 23012 upside down at 4°, 0.2 chords above
the moving ground, at 30 m/s. Top: what the network gets (the oncoming air,
and where the wing and the ground are). Bottom: what it learns to predict,
the simulated pressure and velocity.*

## Main results

| | Result | Details |
|---|---|---|
| Reproduction, free air | 2.96% test error with the paper's training length (paper: 2.6%); pressure and velocity errors as in the paper's best model | [Step 1](docs/01-reproduction.md) |
| CFD against high-resolution LES | NACA 4412 in free air, with the settings of the dataset: skin friction within 7.6% (suction side) and 7.3% (pressure side) on average; surface pressure also close (mean \|ΔCp\| 0.009–0.014) | [Step 3](docs/03-mesh-study.md) |
| CFD against the wind tunnel | Tyrrell 026 F1 wing: the downforce gained near the ground within 4% | [Step 4](docs/04-wind-tunnel.md) |
| Mesh study | numerical uncertainty of the downforce 0.04–3%, largest closest to the ground | [Steps 3 and 4](docs/03-mesh-study.md) |
| Airfoil shapes | 1,462 of the 1,497 UIUC files smoothed: pressure wiggles above 0.1 in 453 files before, in none after | [Step 5](docs/05-airfoil-shapes.md) |
| Where steady RANS converges | Cl becomes steady in 86% of the dataset's runs; close to the ground the flow separates, and part of the range has no steady solution | [Step 6](docs/06-parameter-scan.md) |
| U-Net in ground effect | 0.9% error on 30 unseen airfoils with 3,096 training samples and the distance input (1.4% without it; the free-air model as it is: 20%) | [Steps 8, 10 and 13](docs/13-distance-input.md) |
| Downforce from the U-Net | 3.9% error with a loss weighted next to the wing and the distance input (6.2% with the weighting alone; plain loss: 9.9%) | [Steps 9, 10 and 13](docs/13-distance-input.md) |
| Downforce from a model of its own | a small network on the shape, ride height, angle and speed: 1.6% error on the 30 test airfoils (1.5% against OpenFOAM's force, where the U-Net is 4.3%); 0.13 ms per prediction | [Step 14](docs/14-downforce-model.md) |
| Pressure along the wing | a small network for the pressure and the friction along the surface: downforce 1.3%, drag 8.7% on the test airfoils (2–3% on the two wings), moment 2.5%, the separated part of the surface within 0.3% of it on average | [Step 15](docs/15-surface-model.md) |
| Unseen wing: NACA 4412 | at 11 ride heights: downforce within 5% (within 4% with the distance input), peak at the same height as the CFD | [Steps 11 and 13](docs/11-naca4412-sweep.md) |
| Unseen wing: Tyrrell 026 (F1) | at the tunnel's 9 ride heights: downforce within 1.1% with the distance input (10–19% low without it); the suction peak still too weak | [Steps 12 and 13](docs/13-distance-input.md) |

---

## Quick start

You need Docker Desktop: OpenFOAM runs inside the container. In this folder,
in PowerShell:
```powershell
docker build -t openfoam-ml .     # OpenFOAM v2606 + gmsh + Python
git clone --config core.autocrlf=false https://github.com/thunil/Deep-Flow-Prediction.git
docker run -it --rm -v ${PWD}:/work openfoam-ml
```
Inside the container: the airfoil files, one ground-effect simulation (a few
minutes) and a picture of its sample:
```bash
cd /work/Deep-Flow-Prediction/data && bash download_airfoils.sh
cd /work/ground_effect
python3 groundGen.py --airfoil naca23012.dat --alpha 4 --h 0.2 --U 30
python3 /work/scripts/view_sample.py data/train/<file>.npz /work/results/sample.png
```
Everything else (the free-air pipeline with the fixes in `patches/`, the CFD
checks, the dataset and the training) is in [How to run it](docs/howto.md).

## Repository layout

```
README.md                   this page: summary, the steps, results, quick start
docs/                       one page per step (01-reproduction.md to 15-surface-model.md), howto.md, glossary.md, references.md
Dockerfile                  OpenFOAM v2606 + gmsh + Python environment
patches/openfoam-v2606.patch  fixes to the original code for OpenFOAM v2606
scripts/view_sample.py      plots all six channels of a training sample
scripts/plot_learning_curve.py  plots training/validation loss
scripts/run_seeds.ps1       trains + tests with several seeds, unattended
scripts/summarize_seeds.py  mean ± std table over the seed runs
ground_effect/groundGen.py        data generation: inverted airfoil above a moving ground
ground_effect/case_template/      OpenFOAM case and gmsh template for ground effect
ground_effect/plot_convergence.py Cl and Cd histories of runs
ground_effect/plot_mesh.py        draws the mesh around the wing
ground_effect/mesh_quality.py     y+ of the first cell, and cell sizes in the sampled window
ground_effect/validate_les.py     free-air runs vs LES surface pressure and skin friction
ground_effect/mesh_study.sh       runs the mesh study, round 2 (inside the container)
ground_effect/mesh_study_report.py  figures and tables of round 2
ground_effect/verification.sh     round 3: nuTilda scheme, grid convergence, domain (inside the container)
ground_effect/verification_report.py  tables and figures of round 3, including the GCI
ground_effect/sampling_test.py    checks the row-by-row sampling on finished runs (inside the container)
ground_effect/make_tyrrell026.py  Tyrrell 026 wing coordinates (Zerihan 2001, Table 2) -> airfoil files (smoothed, and as tabulated)
ground_effect/panel.py            inviscid surface pressure on the curve gmsh builds through airfoil points (panel method)
ground_effect/shape_check.py      kinks in that curve, before and after smoothing, for many airfoil files
ground_effect/smooth_airfoils.py  smooths the airfoil files for the dataset (quintic spline in sqrt(x)); leaves out files with errors
ground_effect/smoothing_test.py   tests the smoothing against stand-in airfoils whose shape is known exactly
ground_effect/validation_zerihan.sh   runs the ground-effect validation (inside the container)
ground_effect/validation_zerihan.py   compares those runs with Zerihan's experiments and CFD
ground_effect/param_scan.sh       parameter scan: 200 random runs drawn like the dataset (inside the container)
ground_effect/param_scan_report.py  sorts the runs (steady, clipped, settling, oscillating, failed) by ride height, angle and speed
ground_effect/clip_test.sh        what the nuTilda clipping changes, and whether settling runs converge (inside the container)
ground_effect/clip_test_report.py tables and figure of that test
ground_effect/clip_cells.py       finds the cells where OpenFOAM clipped nuTilda in a finished run
ground_effect/dataset.sh          makes the dataset with several runs at a time (inside the container)
ground_effect/make_dataset_zip.py zips the samples for a Kaggle dataset, after checking them against the lists of runs
ground_effect/unet.py             the U-Net of the original code (copied from DfpNet.py, unchanged)
ground_effect/unet_data.py        loads and normalises the ground-effect samples (optionally with the signed distance); the original error measure and the downforce from the pressure
ground_effect/train_unet.py       trains one U-Net (from random weights or from the free-air model) and tests it
ground_effect/learning_curve.py   trains and tests U-Nets on parts of the data, then the table and figure
ground_effect/loss_study.py       compares training losses and inputs for the downforce: table and figure
ground_effect/sweep_naca4412.sh   ride-height sweep of the NACA 4412: 12 heights and free air (inside the container)
ground_effect/sweep_tyrrell026.sh ride-height sweep of the Tyrrell 026 at the tunnel's heights and 10 m/s (inside the container)
ground_effect/sweep_report.py     table and figure of a sweep, with the U-Net's predictions
ground_effect/baseline_cl.py      comparison model: a small network that predicts only the downforce, from the shape, ride height, angle and speed
ground_effect/predict.py          the trained models for any airfoil, ride height, angle and speed, without a simulation: the U-Net's flow, the downforce network's Cl, the surface model's pressure, friction and forces
ground_effect/field_figure.py     simulated and predicted flow fields side by side, with their difference
ground_effect/downforce_report.py figure and table of the U-Net against the comparison model (step 14)
ground_effect/cl_learning_curve.py  downforce error against the amount of data: small network, Gaussian process and U-Net
ground_effect/surface_data.py     the pressure and friction along the wing at fixed points, on the mesh's own faces; Cl, Cd, Cm from them
ground_effect/surface_model.py    a small network for the pressure and the friction along the wing (step 15)
ground_effect/surface_report.py   pressure and friction along the wing: CFD against the surface model
results/                    figures and reproduction results
Deep-Flow-Prediction/       the original code, which you clone here (see Quick start); not part of this repo
```

---

## Reference

```bibtex
@article{thuerey2020deepFlowPred,
  title   = {Deep learning methods for Reynolds-averaged Navier--Stokes simulations of airfoil flows},
  author  = {Thuerey, Nils and Weissenow, Konstantin and Prantl, Lukas and Hu, Xiangyu},
  journal = {AIAA Journal},
  volume  = {58},
  number  = {1},
  pages   = {25--36},
  year    = {2020}
}
```

To cite this repository: M. T. A. Sial, *GroundFoil: deep learning for
inverted airfoils in ground effect*, Zenodo,
https://doi.org/10.5281/zenodo.24176980 (all versions; v0.1.0, under its first
title *Deep Flow Prediction on OpenFOAM v2606, extended to inverted airfoils in
ground effect*, is https://doi.org/10.5281/zenodo.24176981). GitHub's "Cite
this repository" button gives the same in other formats.

Other references used on these pages: [References](docs/references.md).

Airfoil coordinates come from the UIUC Airfoil Coordinates Database
(https://m-selig.ae.illinois.edu/ads/coord_database.html).

## License

[Apache License 2.0](LICENSE), the same license as the original
[Deep-Flow-Prediction](https://github.com/thunil/Deep-Flow-Prediction) code
that the patch in this repo modifies.
