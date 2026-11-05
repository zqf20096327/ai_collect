# PINNForge
[![PyPI version](https://badge.fury.io/py/pinnforge.svg)](https://pypi.org/project/pinnforge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\
**Solve partial differential equations in 3 lines of code.**

![PINNForge demo](docs/demo.gif)

PINNForge is a lightweight wrapper around PyTorch that handles the boilerplate code of Physics-Informed Neural Networks so you can focus on the physics.

## Install

```bash
pip install pinnforge
```

## Quick Start

```python
from pinnforge import solve_pde

result = solve_pde("heat", epochs=5000)
print(f"Relative L2 error: {result['metrics']['relative_l2_error']:.2e}")
# Relative L2 error: 3.42e-02
```

The library automatically builds the network, generates training points, trains, validates, and returns metrics.

## Why PINNForge?

Setting up a PINN in the standard tooling requires 25+ lines of boilerplate before you see your first result. PINNForge does it in 3.

### Side-by-side: solving the 1D Heat equation

<table>
<tr>
<th width="50%">PINNForge (3 lines)</th>
<th width="50%">DeepXDE (~25 lines)</th>
</tr>
<tr>
<td>

```python
from pinnforge import solve_pde

result = solve_pde("heat", epochs=5000)
print(result['metrics']['relative_l2_error'])
```

Everything else is handled by the library.

</td>
<td>

```python
import deepxde as dde
import numpy as np

def pde(x, y):
    dy_t = dde.grad.jacobian(y, x, i=0, j=1)
    dy_xx = dde.grad.hessian(y, x, i=0, j=0)
    return dy_t - dy_xx

geom = dde.geometry.Interval(0, 1)
timedomain = dde.geometry.TimeDomain(0, 1)
geomtime = dde.geometry.GeometryXTime(geom, timedomain)

def boundary(x, on_boundary):
    return on_boundary

def initial(x):
    return np.sin(np.pi * x[:, 0:1])

bc = dde.icbc.DirichletBC(geomtime, lambda x: 0, boundary)
ic = dde.icbc.IC(geomtime, initial, lambda _, on_initial: on_initial)

data = dde.data.TimePDE(
    geomtime, pde, [bc, ic],
    num_domain=2000, num_boundary=100, num_initial=100,
)

net = dde.nn.FNN([2] + [64] * 3 + [1], "tanh", "Glorot normal")
model = dde.Model(data, net)
model.compile("adam", lr=1e-3)
model.train(epochs=15000)
model.compile("L-BFGS")
losshistory, train_state = model.train()

# Then write validation and plotting code yourself
```

The setup is 9x longer and you still need to write your own validation and plots after training.

</td>
</tr>
</table>

### Feature comparison

Features that PINNForge has that DeepXDE and PINNs-Torch do not:\
&nbsp;&nbsp;&nbsp;&nbsp;-One-line solve API\
&nbsp;&nbsp;&nbsp;&nbsp;-Symbolic PDE definition (SymPy)\
&nbsp;&nbsp;&nbsp;&nbsp;-Automatically generated validation metrics and plots\
&nbsp;&nbsp;&nbsp;&nbsp;-Built in numerical solvers

However, DeepXDE is multi-backend, is better for 3D+ problem, and tested since 2019 which are advantages over PINNForge. PINNForge trades depth for ease of use and time-to-result. If you need complex PDEs or 3D problems, use DeepXDE. If you want to try an idea in 5 minutes with minimal code, use PINNForge.

## What's Included

- **`solve_pde()`**: one-line API for common PDEs (Heat and Burgers, wave is on the list)
- **`AutoPINN`**: configurable solver with auto-selected hyperparameters
- **`PINN`**: the underlying neural network module
- **`SymbolicPDE`**: define custom PDEs using SymPy math notation
- **`NumericalSolver`**: finite-difference reference solutions
- **`ExperimentLogger`**: automatic training metrics and checkpoint logging

## Custom PDEs with SymPy

For problems not in the built-in registry, define them symbolically:

```python
import sympy as sp
from pinnforge import AutoPINN

x, t = sp.symbols('x t')
u = sp.Function('u')(x, t)
equation = sp.diff(u, t) + u * sp.diff(u, x) - 0.01 * sp.diff(u, x, 2)

solver = AutoPINN.from_symbolic(equation, [x, t], u)
result = solver.solve()
```

`u` has to be a `sp.Function` of x and t. A plain symbol has no derivatives, so `sp.diff` would quietly return 0. Only `u_t`, `u_x` and `u_xx` can show up in the equation, and the initial condition defaults to `sin(pi x)` with zero boundaries unless you pass your own to `SymbolicPDE`.

Metrics only come back when there is something to compare against, so custom PDEs return an empty dict.

## Validation

`solve_pde` checks the result on a grid after training. Heat is compared to its exact solution. Burgers has no closed form for this setup, so it is compared to a finite difference reference (implicit, on a fine grid). Custom symbolic PDEs skip validation.

## Known Limitations (v0.2.1)

- **Wave equation does not run.** The residual needs `u_tt` and `PINN.loss_pde` only computes first derivatives in time, so `WaveEquation.residual` raises `NotImplementedError` for now.
- **Fourier features were rewritten in v0.2.1 but are still off by default.** The old version only used 2 random frequencies for a 2D input and threw away the raw coordinates, which is the likely reason training collapsed in [#1](https://github.com/ved-rl/pinnforge/issues/1). It now uses 64 by default and keeps x and t. I have not benchmarked it against the plain network yet, so it stays opt-in.
- **Adaptive loss weighting is off by default.** The weights are now balanced from gradient sizes and no longer trained by the optimizer (they were before, which defeated the point). Needs benchmarking too.
- **Adaptive activation (SA-PINN) is off by default.**
- **`precision` in `AutoConfig` is not applied yet.** Everything runs in float32.
- **Only 1D problems are supported.** Multi-dimensional PDEs are planned.
- **No CLI yet.** Everything is Python-only.

See `CHANGELOG.md` for what changed in each version.

## Contributing

This is a new project and there are several tasks that would help a lot. If you're looking for a place to contribute to SciML tooling, help is greatly appreciated

### Good First Issues

| Task | Difficulty | Description |
|------|------------|-------------|
| **Wave equation** | Medium | Compute `u_tt` in `PINN.loss_pde` (or pass it to the residual) and write a real `WaveEquation.residual` with a test against the d'Alembert solution. |
| **Add a quickstart notebook** | Easy | Create `examples/quickstart.ipynb` that walks through the 3-line API and shows results inline. |
| **Improve error messages** | Easy | Several places raise generic errors. Add context-specific messages for common failure modes. |

### Larger Contributions Welcome

| Task | Difficulty | Description |
|------|------------|-------------|
| **Benchmark Fourier features** | Medium | The mapping was rewritten in v0.2.1. Run Burgers and Heat with and without it over a few seeds and scales and post the errors on [#1](https://github.com/ved-rl/pinnforge/issues/1). |
| **L-BFGS fine-tuning** | Medium | Adding L-BFGS as a second-stage optimizer like DeepXDE does would improve final accuracy by 10x. |
| **2D PDE support** | Hard | Currently limited to 1D spatial domains. Requires changes to `pdes.py`, `data.py`, and the `PINN` class. |
| **JAX backend** | Hard | Optional JAX backend for 5-10x faster training. See `jinns` for reference. |
| **Adaptive sampling (RAR)** | Medium | Residual-based adaptive refinement. Sample new collocation points where the PDE residual is highest. |

### How to Contribute

1. Fork the repo
2. Create a feature branch (`git checkout -b fix-fourier-features`)
3. Make your changes
4. Run `pytest tests/ -v` and make sure everything passes
5. Open a Pull Request

See `CONTRIBUTING.md` for the full guide. First-time contributors are very welcome — if you're unsure where to start, open an issue and ask.

## Tech Stack

- Python 3.8+
- PyTorch 
- SymPy
- NumPy / SciPy 

## License

MIT — see `LICENSE`.

## Acknowledgments

Built on the original Physics-Informed Neural Networks formulation by Raissi, Perikaris, and Karniadakis (2019). Inspired by the usability goals of DeepXDE but with a focus on time-to-first-result.
