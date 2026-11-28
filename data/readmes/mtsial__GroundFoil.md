# GroundFoil: deep learning for inverted airfoils in ground effect

[![Code DOI](https://zenodo.org/badge/1454795941.svg)](https://doi.org/10.5281/zenodo.24176980)
[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24424328.svg)](https://doi.org/10.5281/zenodo.24424328)

**GroundFoil** predicts the flow and the forces around **inverted airfoils in
ground effect** (F1 front wings) with neural networks trained on our own RANS
simulations. It builds on **Thuerey et al., "Deep Learning Methods for
Reynolds-Averaged Navier-Stokes Simulations of Airfoil Flows"** (*AIAA
Journal*, 2020), which we first reproduced on current software: OpenFOAM
v2606, gmsh 4 and Docker on Windows.

- **A validated dataset:** 6,988 steady RANS simulations of 1,444 airfoils
  above a moving ground, at ride heights of 0.05–0.6 chords, angles of 0–10°
  and Reynolds numbers of one to five million, checked against
  high-resolution LES, wind-tunnel tests of an F1 wing (the downforce gained
  near the ground within 4%) and finer meshes.
- **Models compared:** a U-Net predicts the whole flow around 28 airfoils it
  has not seen with a 0.99% error; small networks predict the downforce
  within 1.2% and the drag within 1.6%, in under a millisecond; a network for
  the pressure and the friction along the wing also gives the moment and
  where the flow separates. With little data a Gaussian process is the most
  accurate, and classical regressions are three to five times less accurate
  than the networks.
- **Where the downforce peaks:** the ride height of the largest downforce
  for all 1,444 airfoils, checked against 264 new simulations (within 1.4%,
  median).

Thuerey et al.'s paper: https://arxiv.org/abs/1810.08217; their code:
https://github.com/thunil/Deep-Flow-Prediction (Apache-2.0). Words used here
are explained in the [glossary](docs/glossary.md).

## Workflow

The study in nineteen steps, each with its own page:

1. **[Reproduction](docs/01-reproduction.md):** Thuerey et al.'s free-air
   study on current software, with the paper's errors.
2. **[Ground-effect setup](docs/02-ground-effect-setup.md):** the airfoil
   upside down above a moving ground; the iterations, the incoming turbulence
   and the solver settings.
3. **[Mesh study](docs/03-mesh-study.md):** a mesh on which the downforce is
   converged (GCI 0.04%), with skin friction within 7–8% of high-resolution LES.
4. **[Wind-tunnel validation](docs/04-wind-tunnel.md):** the Tyrrell 026 F1
   wing; the downforce gained near the ground within 4% of the tunnel's.
5. **[Airfoil shapes](docs/05-airfoil-shapes.md):** all airfoil files
   smoothed (1,462 used).
6. **[Parameter scan](docs/06-parameter-scan.md):** where steady RANS
   converges, and the rules for keeping a run.
7. **[The dataset](docs/07-dataset.md):** the first 4,000 runs, and 102 test
   samples on 28 airfoils kept out of training.
8. **[U-Net learning curve](docs/08-unet-learning-curve.md):** a 1.8% error
   on unseen airfoils with 789 samples (24% for the free-air model as it is).
9. **[Downforce](docs/09-downforce.md):** the downforce from the predicted
   pressure, 11% off, and 7.7% with a loss weighted next to the wing.
10. **[All the data](docs/10-all-data.md):** with 3,096 samples, downforce
    6.2% and field 1.4%, both still falling.
11. **[A new wing](docs/11-naca4412-sweep.md):** the NACA 4412, never seen:
    downforce within 5%, peak at the CFD's ride height.
12. **[The F1 wing](docs/12-tyrrell026-sweep.md):** the Tyrrell 026: the
    curve's shape right, but 10–19% too little downforce.
13. **[The exact wing shape](docs/13-distance-input.md):** the distance to
    the wing's surface as an input: downforce 3.9%, field 0.9%.
14. **[The downforce alone](docs/14-downforce-model.md):** a small network for
    the downforce beats the U-Net's: 1.6% against 3.9%.
15. **[The pressure along the wing](docs/15-surface-model.md):** a network for
    the surface pressure and friction: the downforce, the drag, the moment
    and where the flow separates.
16. **[All the data](docs/16-final-models.md):** the final models on 6,177
    samples; a Gaussian process is best with up to about 200 samples.
17. **[The drag alone](docs/17-drag-model.md):** a network for the drag,
    1.6% against 7.5% for the drag added up along the surface.
18. **[Where the downforce peaks](docs/18-ride-height-map.md):** the peak's
    ride height for all 1,444 airfoils, checked against 264 new simulations.
19. **[Classical regressions](docs/19-classical-baselines.md):** polynomial,
    random forest and support vector regression, three to five times less
    accurate than the networks.

**Data:** the simulations, the trained models, the ride-height sweeps and the
map of the peaks are on Zenodo, https://doi.org/10.5281/zenodo.24424328. All commands are in
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
| CFD checks | skin friction within 7–8% of high-resolution LES; the downforce gained near the ground within 4% of the wind tunnel (Tyrrell 026 F1 wing); numerical uncertainty of the downforce 0.04–3% | [Steps 3 and 4](docs/03-mesh-study.md) |
| Flow fields | the U-Net: 0.99% error on 28 unseen airfoils (Thuerey et al.'s error; the free-air model as it is: 24%) | [Step 16](docs/16-final-models.md) |
| Downforce | a small network on the shape, ride height, angle and speed: 1.2% off OpenFOAM's force, against 4.0% for the U-Net's; 0.65 ms per prediction, against 318 s for a simulation | [Steps 14 and 16](docs/16-final-models.md) |
| Drag | a small network of its own: 1.6%, against 7.5% for the drag added up along the surface | [Step 17](docs/17-drag-model.md) |
| Pressure along the wing | downforce 1.2%, moment 2.2%, and where the flow separates | [Steps 15 and 16](docs/16-final-models.md) |
| Little data | a Gaussian process is the most accurate with up to about 200 samples (7.4% with 97, the small network 12.4%), and says how sure it is | [Step 16](docs/16-final-models.md) |
| Classical regressions | polynomial, random forest and support vector regression: 3.8–6.9% for the downforce and 5.4–8.7% for the drag | [Step 19](docs/19-classical-baselines.md) |
| Unseen wings | at every ride height of the NACA 4412 and the Tyrrell 026 F1 wing: the U-Net within 1.9% and 3.0% of OpenFOAM's force, the small models within 0.9% | [Step 16](docs/16-final-models.md) |
| Where the downforce peaks | the peak's ride height rises with the angle (median h/c 0.107, 0.146 and 0.204 at 2°, 5° and 8°), the camber and the thickness; within 1.4% of 264 new simulations | [Step 18](docs/18-ride-height-map.md) |

All the results, with the numbers behind them: [All results](docs/results.md).
The test errors are those of all 102 test samples; two test airfoils are near
copies of training airfoils, and without their 7 samples the errors are 3–5%
higher ([step 7](docs/07-dataset.md)).

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
README.md              this page
docs/                  one page per step, all results, every file, how to run it, glossary, references
ground_effect/         the ground-effect code: simulations, checks, models and figures
scripts/               helpers of the free-air reproduction
patches/               fixes to the original code for OpenFOAM v2606
results/               figures and tables of the results
Dockerfile             OpenFOAM v2606 + gmsh + Python
Deep-Flow-Prediction/  the original code, which you clone here (see Quick start); not part of this repo
```

Every file and what it does: [Files](docs/layout.md).

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
https://doi.org/10.5281/zenodo.24176980 (all versions; v1.0.0, the version of
the final results, is https://doi.org/10.5281/zenodo.24425137; v0.1.0, under
its first title *Deep Flow Prediction on OpenFOAM v2606, extended to inverted
airfoils in ground effect*, is https://doi.org/10.5281/zenodo.24176981).
GitHub's "Cite this repository" button gives the same in other formats.

To cite the dataset and the trained models: M. T. A. Sial, *GroundFoil dataset:
RANS simulations of inverted airfoils in ground effect, and trained surrogate
models*, version 1.1, Zenodo, https://doi.org/10.5281/zenodo.24537289.

Other references used on these pages: [References](docs/references.md).

Airfoil coordinates come from the UIUC Airfoil Coordinates Database
(https://m-selig.ae.illinois.edu/ads/coord_database.html).

## License

[Apache License 2.0](LICENSE), the same license as the original
[Deep-Flow-Prediction](https://github.com/thunil/Deep-Flow-Prediction) code
that the patch in this repo modifies.
