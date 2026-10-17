# Sparse Identification of Nonlinear Dynamics

This repository is a clean, reproducible implementation of the core idea from:

Steven L. Brunton, Joshua L. Proctor, and J. Nathan Kutz, "Discovering governing equations from data: Sparse identification of nonlinear dynamical systems", arXiv:1509.03580.

The project focuses on Sparse Identification of Nonlinear Dynamics (SINDy): given measurements of a dynamical system, build a library of candidate nonlinear terms and use sparse regression to identify the few terms that govern the dynamics.

## What Is Included

- A compact SINDy implementation in `src/sindy_piml/`
- Polynomial feature libraries for candidate dynamics
- Finite-difference derivative estimation
- Sequential thresholded least squares (STLSQ)
- Reproducible examples for a linear system and the Lorenz system
- Paper-faithful examples for the cubic oscillator, logistic map, Hopf normal form, noisy data, and threshold selection
- Tests that verify coefficient recovery on known systems
- A notebook walkthrough that demonstrates data generation, library construction, sparse regression, simulation, and threshold selection

No external data files are required for the main examples. The examples generate synthetic data from known systems.

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m unittest discover -s tests
python examples\linear_system.py
python examples\lorenz_system.py
python examples\cubic_oscillator.py
python examples\logistic_map.py
python examples\hopf_normal_form.py
python examples\threshold_sweep.py
```

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests
python examples/linear_system.py
python examples/lorenz_system.py
python examples/cubic_oscillator.py
python examples/logistic_map.py
python examples/hopf_normal_form.py
python examples/threshold_sweep.py
```

## Project Layout

```text
.
|-- README.md
|-- pyproject.toml
|-- requirements.txt
|-- src/
|   `-- sindy_piml/
|       |-- differentiation.py
|       |-- features.py
|       |-- model.py
|       |-- optimizers.py
|       `-- systems.py
|-- examples/
|   |-- cubic_oscillator.py
|   |-- hopf_normal_form.py
|   |-- linear_system.py
|   |-- logistic_map.py
|   |-- lorenz_system.py
|   |-- noisy_linear_system.py
|   `-- threshold_sweep.py
|-- notebooks/
|   `-- 01_sindy_linear_system.ipynb
|-- tests/
|   |-- test_features.py
|   `-- test_model.py
`-- docs/
    |-- paper-notes.md
    `-- legacy-notebooks.md
```

## SINDy Workflow

1. Collect state measurements `X(t)`.
2. Estimate or provide derivatives `dX/dt`.
3. Build a candidate library `Theta(X)` containing possible terms such as `1`, `x`, `y`, `x^2`, `xy`, and so on.
4. Solve the sparse regression problem

   ```text
   dX/dt = Theta(X) Xi
   ```

5. Interpret the nonzero coefficients in `Xi` as the discovered governing equations.

Start with `notebooks/01_sindy_linear_system.ipynb` if you want the narrated version of that workflow.

## Example Output

For the synthetic system

```text
x' = -2x
y' = y
```

the linear example recovers:

```text
x' = -2.000*x
y' = 1.000*y
```

For Lorenz data, the quadratic example recovers the expected sparse structure:

```text
x' = -10*x + 10*y
y' = 28*x - y - x*z
z' = x*y - 2.667*z
```

Small numerical differences are expected because the examples use simulated data and regression.

## Paper Coverage

| Paper topic | Repo coverage |
| --- | --- |
| Sequential thresholded least squares | `src/sindy_piml/optimizers.py` |
| Polynomial candidate library | `src/sindy_piml/features.py` |
| Linear damped oscillator | `examples/cubic_oscillator.py` |
| Cubic damped oscillator | `examples/cubic_oscillator.py` |
| Chaotic Lorenz system | `examples/lorenz_system.py` |
| Threshold/Pareto tradeoff | `examples/threshold_sweep.py` and `src/sindy_piml/selection.py` |
| Noisy derivative caution | `examples/noisy_linear_system.py` |
| Discrete-time logistic map | `examples/logistic_map.py` and `SINDyMap` |
| Parameterized Hopf normal form | `examples/hopf_normal_form.py` |
| Cylinder wake/POD | Documented as future work; omitted because the dataset is not included |

## Notes On The Previous Notebooks

The original notebooks mixed SINDy, PINNs, Colab upload cells, missing `.mat` files, and TensorFlow 1 APIs. They are valuable as research history, but they were not a reproducible project as-is. The cleaned repo keeps the core SINDy paper connection as the primary, runnable path. See `docs/legacy-notebooks.md` for migration notes.

## Citation

```bibtex
@article{brunton2016discovering,
  title={Discovering governing equations from data by sparse identification of nonlinear dynamical systems},
  author={Brunton, Steven L. and Proctor, Joshua L. and Kutz, J. Nathan},
  journal={Proceedings of the National Academy of Sciences},
  volume={113},
  number={15},
  pages={3932--3937},
  year={2016},
  doi={10.1073/pnas.1517384113}
}
```
