# PINNStudio

*A no-code scientific computing environment for solving forward and inverse problems with physics-informed neural networks — from setting up the equations to training, error analysis, and visualization.*

<p align="center">
  <a href="https://pypi.org/project/pinnstudio/"><img src="https://img.shields.io/pypi/v/pinnstudio.svg" alt="PyPI version"></a>
  <a href="https://pepy.tech/project/pinnstudio"><img src="https://static.pepy.tech/badge/pinnstudio" alt="PyPI downloads"></a>
  <a href="https://pypi.org/project/pinnstudio/"><img src="https://img.shields.io/pypi/pyversions/pinnstudio.svg" alt="Python versions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/AsfandyarKhan72/PINNStudio.svg" alt="License: MIT"></a>
  <a href="https://github.com/AsfandyarKhan72/PINNStudio/stargazers"><img src="https://img.shields.io/github/stars/AsfandyarKhan72/PINNStudio?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/AsfandyarKhan72/PINNStudio/commits/main"><img src="https://img.shields.io/github/commit-activity/m/AsfandyarKhan72/PINNStudio" alt="Commit activity"></a>
</p>

<p align="center">
  <em>Three of the 60 built-in examples — Schrödinger in 1D, Allen-Cahn in 2D and heat in 3D — trained and animated in PINNStudio. Click one to see its setup and results.</em>
</p>

<table>
<tr>
<td width="33%" align="center">
<a href="#dx-schr-dinger-equation"><img src="assets/Images/Top_GIFs/1D_Schrodinger.gif" alt="PINNStudio — 1D Schrödinger PINN solution |h| animated over time" width="100%"></a>
<sub><strong>1D</strong> — <code>(x, t)</code> — <a href="#dx-schr-dinger-equation">Schrödinger</a></sub>
</td>
<td width="33%" align="center">
<a href="#2d-allen-cahn-wight--zhao"><img src="assets/Images/Top_GIFs/2D_Allen_Cahn_Wight.gif" alt="PINNStudio — 2D Allen-Cahn (Wight & Zhao) PINN solution animated over time" width="100%"></a>
<sub><strong>2D</strong> — <code>(x, y, t)</code> — <a href="#2d-allen-cahn-wight--zhao">Allen-Cahn (Wight & Zhao)</a></sub>
</td>
<td width="33%" align="center">
<a href="#3d-heat"><img src="assets/Images/Top_GIFs/3D_Heat.gif" alt="PINNStudio — 3D Heat PINN solution animated over time" width="100%"></a>
<sub><strong>3D</strong> — <code>(x, y, z, t)</code> — <a href="#3d-heat">Heat</a></sub>
</td>
</tr>
</table>

<p align="center">
  <strong><a href="https://asfandyarkhan72.github.io/PINNStudio/">Website</a></strong> &nbsp;·&nbsp;
  <strong><a href="#installation">Install</a></strong> &nbsp;·&nbsp;
  <strong><a href="#quick-start">Quick Start</a></strong> &nbsp;·&nbsp;
  <strong><a href="#examples">Examples</a></strong> &nbsp;·&nbsp;
  <strong><a href="#solving-your-own-problem">Your Own Problem</a></strong> &nbsp;·&nbsp;
  <strong><a href="https://github.com/AsfandyarKhan72/PINNStudio/discussions">Discussions</a></strong> &nbsp;·&nbsp;
  <strong><a href="#citation">Citation</a></strong>
</p>

<details>
<summary><strong>Table of contents</strong></summary>

- [Overview](#overview)
- [Demo Video](#demo-video)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [The Interface](#the-interface)
- [Examples](#examples)
- [Features](#features)
- [Solving Your Own Problem](#solving-your-own-problem)
- [How It Works](#how-it-works)
- [Repository Structure](#repository-structure)
- [Citation](#citation)
- [References](#references)
- [Acknowledgment](#acknowledgment)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

</details>

---

## Overview

**PINNStudio** is a scientific computing environment for solving differential equations with physics-informed neural networks (PINNs) and related scientific machine learning methods, without writing any code. You describe the problem — the equations, the domain, the boundary and initial conditions, the network and how it should be trained — and PINNStudio trains the model, tracks it while it runs, and gives back the solution, its error against reference data, plots and animations, and the trained model ready to reload.

Setting up a PINN by hand means writing a new script for every problem: the residual of the equations through automatic differentiation, the sampling of collocation points, the weighting of the loss terms, the optimizer schedule, and then the plotting and error analysis afterwards. Each of these is easy to get subtly wrong. PINNStudio puts all of it into one place, so researchers and students in science and engineering — including those new to scientific computing or machine learning — can spend their time on the physics of their problem rather than on the code around it.

**What it can solve**

- **Forward and inverse problems:** solve a known equation, or learn unknown coefficients or whole unknown fields from measured data.
- **ODEs and PDEs in 1D, 2D and 3D**, steady or time-dependent, including coupled multi-output systems, integro-differential and fractional equations, typed in a readable form such as `du_t + u*du_x - 0.01/pi*du_xx`.
- **Many kinds of domains** — intervals, rectangles, disks, polygons, cuboids, spheres, and custom shapes combined from them (e.g. a domain with a hole) — with Dirichlet, Neumann, Robin, periodic and point-data conditions, or conditions imposed exactly through the network output.

**How it trains**

- **Multi-phase training** (e.g. Adam followed by L-BFGS) with learning-rate schedules and loss weights per phase.
- **Adaptive methods:** residual-based adaptive refinement (RAR), which adds points where the error is largest; time-adaptive training, which marches through time in steps, each starting from the previous one (transfer learning); and initial-condition-guided pre-training.
- **Point resampling, early stopping, checkpointing and time budgets**, and live monitors of any output or derivative during training.
- **Parameter sweeps** over almost any setting — one at a time, all combinations, paired values, or Bayesian search — with a summary of how the error changes with each parameter.

**What you get back**

- A live training log and loss plot, and error analysis against reference data or an exact formula (relative $L_2$, MSE, maximum error).
- A history of every saved run, with any of them compared on one plot, and figures and tables that copy straight into a paper or a spreadsheet.
- Line, surface and animated solution plots, solution data export, and a saved model that can be reloaded and visualized again without retraining.
- A standalone Python script for every problem, so the work can be inspected, shared and reproduced outside PINNStudio.

**Ready-to-run examples.** PINNStudio comes with 60 worked examples, from simple ODEs to the Navier–Stokes equations in 3D, including published PINN benchmarks (Raissi et al., Wight & Zhao, Mattey & Ghosh, and others) and DeepXDE's examples. Each one loads in one click, and 58 of them come with an exact solution or reference data to compare against — see [Examples](#examples).

PINNStudio is under active development, and we are extending it with newer scientific machine learning and PINN methods, aimed at solving harder problems more accurately and faster.

## Demo Video

[![PINNStudio demo — solving PDEs with physics-informed neural networks, no code](https://img.youtube.com/vi/5ILxuutvEZw/maxresdefault.jpg)](https://youtu.be/5ILxuutvEZw)

*Click to watch the full walkthrough on YouTube: loading an example, setting up your own PDE, sketching a domain and its boundary conditions, training with live loss, error analysis, run history and parameter sweeps.*

## Installation

**Quickest way to try PINNStudio** (any operating system):

```bash
pip install pinnstudio
pinnstudio
```

<details>
<summary><strong>Command not found after <code>pip install</code>?</strong></summary>

- **<code>pip: command not found</code>?** Use <code>pip3</code> instead - many systems (macOS especially) only ship <code>pip3</code>, not a plain <code>pip</code>.
- **<code>pinnstudio: command not found</code> even though the install said it succeeded?** pip installed it into a per-user folder that is not on your shell's PATH yet. The install output actually tells you the exact folder, in a line like <code>WARNING: The script pinnstudio is installed in '.../bin' which is not on PATH.</code> Add that folder to your PATH:

```bash
echo 'export PATH="<folder from the warning above>:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

(Use <code>~/.bashrc</code> instead of <code>~/.zshrc</code> if your shell is bash.) Then <code>pinnstudio</code> should launch directly. This never comes up with <code>install.sh</code>/<code>install.bat</code>, since those use a virtual environment where the command is always found automatically.

- **The GPU fix command PINNStudio suggests fails with a <code>flit_core</code> or "Could not find a version that satisfies" error?** Your pip is too old to resolve PyTorch's package index correctly. Upgrade it first, then retry:

```bash
python -m pip install --upgrade pip
pip install torch --index-url https://download.pytorch.org/whl/cu121 --force-reinstall
```

</details>

**Have an NVIDIA GPU? Use the install script instead.** It creates its own environment and checks that the installed PyTorch can use your GPU, installing a compatible build if the default one cannot (for example with an older driver) — which plain `pip install` does not do.

<details>
<summary><strong>Before you start: open a terminal and check git and Python 3.9+</strong></summary>

- **Windows:** click the Start menu, type `PowerShell`, and open **Windows PowerShell**.
- **macOS:** press `Cmd + Space` to open Spotlight, type `Terminal`, and press Enter (or find it under Applications -> Utilities -> Terminal).
- **Linux:** open your terminal application (commonly `Ctrl + Alt + T`, or search "Terminal" in your application menu).

Then check git and Python by pasting these one at a time:

```bash
git --version
python3 --version
```

(On Windows, use `python --version` instead of `python3 --version`.)

If either command isn't recognized:

- **git missing?** Install it from [git-scm.com/downloads](https://git-scm.com/downloads). Default options are fine. On macOS, running `git --version` for the first time may itself prompt you to install Apple's Command Line Tools — accept and let it finish, then try again.
- **Python missing, or older than 3.9?** Install it from [python.org/downloads](https://www.python.org/downloads/). **On Windows, check "Add python.exe to PATH"** on the installer's first screen — this is the single most common thing people miss.

After installing either one, close your terminal window completely and open a new one before continuing, so the change takes effect.

</details>

```bash
git clone https://github.com/AsfandyarKhan72/PINNStudio.git
cd PINNStudio
```

**macOS / Linux:**
```bash
bash install.sh
./venv/bin/pinnstudio
```

**Windows:**
```
install.bat
.\venv\Scripts\pinnstudio.exe
```

Everything is installed into a virtual environment inside the `PINNStudio` folder — nothing system-wide, and deleting the folder removes it completely. The install needs an internet connection and takes a few minutes.

<details>
<summary><strong>Running PINNStudio again</strong></summary>

You only need to install once. After that, launch PINNStudio again anytime with:

**macOS / Linux**, from inside the `PINNStudio` folder:
```bash
./venv/bin/pinnstudio
```

**Windows**, from inside the `PINNStudio` folder:
```
.\venv\Scripts\pinnstudio.exe
```

That's it - no need to reinstall or recreate the virtual environment.

</details>

<details>
<summary><strong>What gets installed</strong></summary>

`install.sh` / `install.bat` set up an isolated Python virtual environment and install:

- [DeepXDE](https://github.com/lululxvi/deepxde) (PyTorch backend)
- PyTorch
- PyQt6
- NumPy (below 2.5 -- DeepXDE 1.15's Polygon/Triangle geometry breaks on NumPy 2.5+)
- Matplotlib
- Pandas

A CUDA-capable GPU is optional but recommended for larger 2D/3D problems and inverse runs.

</details>

**Something not working?** Open an issue on GitHub with the exact command you ran and the full error message — see [Contributing](#contributing).

## Quick Start

Your first result takes about a minute:

1. Start PINNStudio (`pinnstudio`, or `./venv/bin/pinnstudio` after the install script). It opens on the **Start** tab.
2. Under **Examples** on the Start tab, click **Heat 1D – Dirichlet** (or pick it from the **Examples** list in the toolbar). Every setting — equation, domain, conditions, network, training — fills in, and the model tree on the left shows each part of the problem.
3. Press **Solve** (or Ctrl+Enter). The loss is plotted as it trains (*Results → Live loss*), and the status bar shows the phase, the progress and the time left.
4. When the run finishes, the loss curve and the solution appear under *Results → Overview*, and *Results → Error analysis* lists the relative $L_2$ error against the exact solution at each reference time, with the comparison plots.

From there:
- Switch the toolbar's **Examples** list to **Inverse** and pick the same example to learn the unknown diffusivity from measured data instead.
- Browse the other examples below.
- Follow [Solving Your Own Problem](#solving-your-own-problem) to set up an equation of your own.

## The Interface

PINNStudio's window follows the layout of finite-element tools such as COMSOL: a **model tree** on the left, the **settings** of the selected part of the problem in the middle, and **graphics** on the right, with the **Training Log** and the generated **Script** below them. Every panel can be resized, and the layout is remembered (*View → Reset Layout* restores it).

<p align="center">
<img src="assets/screenshots/interface.png" alt="PINNStudio window: model tree on the left, the Equations page with the Burgers equation typeset in the middle, the loss curve and solution of the finished run on the right, Training Log below" width="100%">
</p>

- **Model tree.** Problem, Equations, Geometry, Collocation points, Initial and Boundary conditions (one node per condition), Neural network, Training, Parameter sweep and Results. A node with a setting that would stop **Solve** is marked, and the toolbar says how many there are. Right-click a node for its actions (add, duplicate or delete a boundary condition, add a training phase, fold all sections), and the **?** next to a page's title opens its part of this README.
- **Settings.** Each page is a short form whose sections fold to their titles. Equations are typeset as you type them, with a note for any name PINNStudio doesn't know.
- **Graphics.** *Start* (new problem, open, recent problems, every example), *Results*, and the domain — *Geometry* for any 2D/3D shape, or the *Sketch* when the domain is drawn.
- **Toolbar and status bar.** Examples, Open, Save, Export script, **Solve** and **Stop** are always in the toolbar; the status bar shows the run's phase, progress, loss and the time left, and the save folder.

<table>
<tr>
<td width="50%" align="center">
<img src="assets/screenshots/sketch.png" alt="Sketch: a rectangle with a circular and an elliptical hole, edges numbered and coloured by boundary condition" width="100%">
<sub><strong>Sketch</strong> — draw the domain, then click its edges to give them boundary conditions</sub>
</td>
<td width="50%" align="center">
<img src="assets/screenshots/live_loss.png" alt="Live loss: each loss term of Burgers 1D plotted during training, the L-BFGS phase marked, progress in the status bar" width="100%">
<sub><strong>Live loss</strong> — each loss term while the model trains</sub>
</td>
</tr>
<tr>
<td width="50%" align="center">
<img src="assets/screenshots/error_analysis.png" alt="Error analysis tab: relative L2 and mean absolute error at each reference time, with the comparison figures" width="100%">
<sub><strong>Error analysis</strong> — the errors at each reference time, ready to copy or export</sub>
</td>
<td width="50%" align="center">
<img src="assets/screenshots/history_compare.png" alt="History tab: runs of a parameter sweep, four compared by their loss and relative L2 error" width="100%">
<sub><strong>History</strong> — every saved run, and several compared on one plot</sub>
</td>
</tr>
</table>

<details>
<summary><strong>Keyboard shortcuts</strong></summary>

| Shortcut | Action |
|---|---|
| Ctrl+Enter or F5 | Solve |
| Shift+F5 | Stop |
| Ctrl+S / Ctrl+Shift+S | Save / Save As |
| Ctrl+O | Open a saved problem |
| Ctrl+E | Export the DeepXDE script |
| Ctrl+Z / Ctrl+Y | Undo / redo in the Sketch |

</details>

Three themes are built in — **Studio Light** (the default), **Studio Dark** and **Solarized Dark** — with an accent colour and a UI scale, under *Settings → Display Settings*.

## Examples

PINNStudio comes with 60 ready-to-run examples, all listed in the table below and loaded from the **Examples** list in the toolbar or the gallery on the Start tab. The list's category is **Forward** (every example, solving for the field) or **Inverse** (examples that learn unknown parameters or fields from data), and each list is ordered like the table, under ODE / 1D / 2D / 3D headings. Every name follows one style, *Equation Dimension – detail*. The table's **Source** column says where each example comes from:

- **PINNStudio templates** (10): our own problems; most reproduce a published PINN result, and the Source column names and links that paper (the heat and the disk/sphere Poisson templates are our own and show "—"). Each one works in both **Forward** and **Inverse** mode — picked from the Inverse list, it loads in Inverse mode with its measured-data file — and all of them ship with reference data in [`reference_data/`](reference_data), so Error Analysis is ready as soon as you load one.
- **DeepXDE examples** (40 forward, 10 inverse): the **DeepXDE** link in the Source column opens each one's script in DeepXDE's repository. These are the PINN examples from DeepXDE's documentation ([forward](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward.html), [inverse](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse.html)), set up with each script's own equation, geometry, boundary/initial conditions, network, optimizers, iteration counts and loss weights, so pressing **Solve** trains what the DeepXDE script trains. Anything that differs from the script is printed in the Training Log when the example loads, and noted in its entry below.

Loading an example fills in every setting, and you can change any of them before pressing **Solve**; if you do, the Training Log lists what you changed. Your save folder, GPU, random-seed and plot-style settings are kept when you load one.

**Error Analysis reference:** where the problem has an exact solution, Error Analysis compares against it directly (*Exact solution*). Otherwise it uses reference files computed independently of the PINN (*Generated data*): PINNStudio's own reference solutions in [`reference_data/`](reference_data), or data computed by [`tools/make_deepxde_reference_data.py`](tools/make_deepxde_reference_data.py) (no data is copied from DeepXDE's repository). Examples marked "—" have no bundled reference; you can add your own files in the Error Analysis dialog.

Every result shown below comes from one training run with the example's settings on an RTX 4090. Errors are relative $L_2$ errors from Error Analysis, and they vary a little from run to run.

The table is ordered by dimension (ODE, 1D, 2D, 3D), then steady before time-dependent and forward before inverse; examples of the same problem sit next to each other.

| # | Example | Dimension | Regime | Problem | Geometry | Error Analysis reference | Source |
|---|---|---|---|---|---|---|---|
| | **ODE (t only)** | | | | | | |
| 1 | [Integro-differential ODE](#dx-integro-differential-equation) | ODE | Time-dependent | Forward | — (t only) | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/ide.py) |
| 2 | [Integro-differential ODE – Volterra kernel](#dx-volterra-integro-differential-equation) | ODE | Time-dependent | Forward | — (t only) | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Volterra_IDE.py) |
| 3 | [Linear ODE system](#dx-ode-system) | ODE | Time-dependent | Forward | — (t only) | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/ode_system.py) |
| 4 | [Lotka-Volterra ODE](#dx-lotka-volterra-equation) | ODE | Time-dependent | Forward | — (t only) | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Lotka_Volterra.py) |
| 5 | [Second-order ODE](#dx-second-order-ode) | ODE | Time-dependent | Forward | — (t only) | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/ode_2nd.py) |
| 6 | [Lorenz ODE – unknown C₁, C₂, C₃](#dx-inverse-lorenz-system) | ODE | Time-dependent | Inverse | — (t only) | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/Lorenz_inverse.py) |
| 7 | [Lorenz ODE – unknown C₁, C₂, C₃, exogenous input](#dx-inverse-lorenz-system-with-exogenous-input) | ODE | Time-dependent | Inverse | — (t only) | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/Lorenz_inverse_forced.py) |
| | **1D** | | | | | | |
| 8 | [Euler beam 1D](#dx-euler-beam) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Euler_beam.py) |
| 9 | [Fractional Poisson 1D](#dx-fractional-poisson-equation-1d) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_Poisson_1d.py) |
| 10 | [Poisson 1D – Dirichlet](#dx-poisson-1d-dirichlet) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Dirichlet_1d.py) |
| 11 | [Poisson 1D – Dirichlet/Neumann](#dx-poisson-1d-dirichlet-neumann) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Neumann_1d.py) |
| 12 | [Poisson 1D – Dirichlet/Periodic](#dx-poisson-1d-dirichlet-periodic) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_periodic_1d.py) |
| 13 | [Poisson 1D – Dirichlet/point-set operator](#dx-poisson-1d-dirichlet-pointsetoperator) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_PointSetOperator_1d.py) |
| 14 | [Poisson 1D – Dirichlet/Robin](#dx-poisson-1d-dirichlet-robin) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Robin_1d.py) |
| 15 | [Poisson 1D – hard BCs](#dx-poisson-1d-hard-boundary-conditions) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Dirichlet_1d_exactBC.py) |
| 16 | [Poisson 1D – multi-scale Fourier features](#dx-poisson-1d-multi-scale-fourier-features) | 1D | Steady | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_multiscale_1d.py) |
| 17 | [Brinkman-Forchheimer 1D – unknown ν_e, K](#dx-inverse-brinkman-forchheimer-model) | 1D | Steady | Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/brinkman_forchheimer.py) |
| 18 | [Diffusion-reaction 1D – unknown rate field](#dx-inverse-diffusion-reaction-with-space-dependent-rate) | 1D | Steady | Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/diffusion_reaction_rate.py) |
| 19 | [Fractional Poisson 1D – unknown order α](#dx-inverse-fractional-poisson-equation-1d) | 1D | Steady | Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/fractional_Poisson_1d_inverse.py) |
| 20 | [Poisson 1D – unknown forcing field](#dx-inverse-poisson-with-unknown-forcing-field) | 1D | Steady | Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/elliptic_inverse_field.py) |
| 21 | [Poisson 1D – unknown forcing field (batches)](#dx-inverse-poisson-with-unknown-forcing-field-batches) | 1D | Steady | Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/elliptic_inverse_field_batch.py) |
| 22 | [Allen-Cahn 1D – Wight & Zhao](#1d-allen-cahn) | 1D | Time-dependent | Forward / Inverse | Interval | Generated data | [Wight & Zhao (2021)](https://doi.org/10.4208/cicp.OA-2020-0086) |
| 23 | [Allen-Cahn 1D](#dx-allen-cahn-equation) | 1D | Time-dependent | Forward | Interval | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Allen_Cahn.py) |
| 24 | [Black-Scholes 1D – American put](#dx-american-put-option) | 1D | Time-dependent | Forward | Interval | — | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/american_put.py) |
| 25 | [Black-Scholes 1D – European call](#dx-black-scholes-equation-call-option) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/black_scholes_call.py) |
| 26 | [Burgers 1D – Raissi et al.](#1d-burgers) | 1D | Time-dependent | Forward / Inverse | Interval | Generated data | [Raissi et al. (2019)](https://doi.org/10.1016/j.jcp.2018.10.045) |
| 27 | [Burgers 1D – RAR](#dx-burgers-equation-with-rar) | 1D | Time-dependent | Forward | Interval | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Burgers_RAR.py) |
| 28 | [Diffusion 1D](#dx-diffusion-equation) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_1d.py) |
| 29 | [Diffusion 1D – hard IC and BCs](#dx-diffusion-equation-with-hard-ic-and-bc) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_1d_exactBC.py) |
| 30 | [Diffusion 1D – resampling](#dx-diffusion-equation-with-resampling) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_1d_resample.py) |
| 31 | [Diffusion-reaction 1D](#dx-diffusion-reaction-equation) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_reaction.py) |
| 32 | [Fractional diffusion 1D](#dx-fractional-diffusion-equation) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_diffusion_1d.py) |
| 33 | [Heat 1D – Dirichlet](#dx-heat-equation) | 1D | Time-dependent | Forward / Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/heat.py) |
| 34 | [Heat 1D – resampling](#dx-heat-equation-with-resampling) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/heat_resample.py) |
| 35 | [Klein-Gordon 1D](#dx-klein-gordon-equation) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Klein_Gordon.py) |
| 36 | [Schrödinger 1D](#dx-schr-dinger-equation) | 1D | Time-dependent | Forward / Inverse | Interval | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Schrodinger.ipynb) |
| 37 | [Wave 1D – space-time multi-scale Fourier features](#dx-wave-propagation-space-time-multi-scale-fourier-features) | 1D | Time-dependent | Forward | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/wave_1d.py) |
| 38 | [Diffusion 1D – unknown coefficient](#dx-inverse-diffusion-equation) | 1D | Time-dependent | Inverse | Interval | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/diffusion_1d_inverse.py) |
| 39 | [Diffusion-reaction 1D – unknown k_f, D](#dx-inverse-diffusion-reaction-system) | 1D | Time-dependent | Inverse | Interval | — | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/reaction_inverse.py) |
| | **2D** | | | | | | |
| 40 | [Fractional Poisson 2D – disk](#dx-fractional-poisson-equation-2d) | 2D | Steady | Forward | Disk | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_Poisson_2d.py) |
| 41 | [Helmholtz 2D – Dirichlet](#dx-helmholtz-2d-dirichlet) | 2D | Steady | Forward | Rectangle | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Dirichlet_2d.py) |
| 42 | [Helmholtz 2D – hyperparameter search](#dx-helmholtz-2d-hyperparameter-optimization) | 2D | Steady | Forward | Rectangle | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Dirichlet_2d_HPO.py) |
| 43 | [Helmholtz 2D – sound-hard scattering](#dx-helmholtz-sound-hard-scattering-absorbing-bc) | 2D | Steady | Forward | Rectangle − Disk | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Sound_hard_ABC_2d.py) |
| 44 | [Helmholtz 2D – square with hole](#dx-helmholtz-2d-with-a-hole) | 2D | Steady | Forward | Rectangle − Disk | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Neumann_2d_hole.py) |
| 45 | [Laplace 2D – disk](#dx-laplace-equation-on-a-disk) | 2D | Steady | Forward | Rectangle in (r, θ) | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Laplace_disk.py) |
| 46 | [Linear elasticity 2D – plate](#dx-linear-elastostatic-plate) | 2D | Steady | Forward | Rectangle | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/elasticity_plate.py) |
| 47 | [Linear elasticity 2D – plate, soft BCs](#dx-linear-elastostatic-plate-soft-bcs) | 2D | Steady | Forward | Rectangle | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/elasticity_plate.py) |
| 48 | [Navier-Stokes 2D – Kovasznay flow](#dx-kovasznay-flow) | 2D | Steady | Forward | Rectangle | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Kovasznay_flow.py) |
| 49 | [Poisson 2D – disk](#2d-poisson-disk) | 2D | Steady | Forward / Inverse | Disk | Generated data | — |
| 50 | [Poisson 2D – L-shape](#dx-poisson-over-an-l-shaped-domain) | 2D | Steady | Forward | Polygon (L-shape) | Generated data | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Lshape.py) |
| 51 | [Poisson 2D – L-shape, Lu et al.](#2d-poisson-l-shape) | 2D | Steady | Forward / Inverse | Polygon (L-shape) | Generated data | [Lu et al. (2021)](https://doi.org/10.1137/19M1274067) |
| 52 | [Fractional Poisson 2D – unknown order α](#dx-inverse-fractional-poisson-equation-2d) | 2D | Steady | Inverse | Disk | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/fractional_Poisson_2d_inverse.py) |
| 53 | [Allen-Cahn 2D – Mattey & Ghosh](#2d-allen-cahn-mattey--ghosh) | 2D | Time-dependent | Forward / Inverse | Rectangle | Generated data | [Mattey & Ghosh (2022)](https://doi.org/10.1016/j.cma.2021.114474) |
| 54 | [Allen-Cahn 2D – Wight & Zhao](#2d-allen-cahn-wight--zhao) | 2D | Time-dependent | Forward / Inverse | Rectangle | Generated data | [Wight & Zhao (2021)](https://doi.org/10.4208/cicp.OA-2020-0086) |
| 55 | [Burgers 2D – Mathias et al.](#2d-burgers-mathias) | 2D | Time-dependent | Forward / Inverse | Rectangle | Generated data | [Mathias et al. (2022)](https://arxiv.org/abs/2301.07824) |
| 56 | [Heat 2D](#2d-heat) | 2D | Time-dependent | Forward / Inverse | Rectangle | Generated data | — |
| | **3D** | | | | | | |
| 57 | [Fractional Poisson 3D – sphere](#dx-fractional-poisson-equation-3d) | 3D | Steady | Forward | Sphere | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_Poisson_3d.py) |
| 58 | [Poisson 3D – sphere](#3d-poisson-sphere) | 3D | Steady | Forward / Inverse | Sphere | Generated data | — |
| 59 | [Heat 3D](#3d-heat) | 3D | Time-dependent | Forward / Inverse | Cuboid | Generated data | — |
| 60 | [Navier-Stokes 3D – Beltrami flow](#dx-beltrami-flow) | 3D | Time-dependent | Forward | Cuboid | Exact solution | [DeepXDE](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Beltrami_flow.py) |

The "unknown field" inverse examples learn the field as an extra network output from measurements given as a Point Set boundary condition, so they run in Forward mode, as in DeepXDE. To train the DeepXDE examples from the command line and print their Error Analysis results:

```bash
python tools/run_deepxde_examples.py --out deepxde_runs            # full settings
python tools/run_deepxde_examples.py --smoke --out deepxde_runs    # a few hundred iterations each
```


### ODE examples

*Click an example to expand it.*

<details id="dx-integro-differential-equation">
<summary><strong>Integro-differential ODE</strong></summary>

DeepXDE example: [`ide.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/ide.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/ide.html))

$$\Large \frac{du}{dt} + \int_0^t u(s)\ ds = 2\pi\cos(2\pi t) + \frac{\sin^2(\pi t)}{\pi}, \qquad t \in [0, 1]$$

- **Problem dimension:** ODE (t) — `du_t + integral(u) - (2*pi*cos(2*pi*t) + sin(pi*t)**2/pi)`
- **Initial condition:** $u(0) = 0$
- **Integral:** 16-point Gauss-Legendre quadrature of the network (*∫ points* 16, DeepXDE's `quad_deg`)
- **Exact solution:** $u = \sin(2\pi t)$
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Integro-differential ODE**

**Result (RTX 4090):** $L_2$ = 1.5 × 10⁻⁴

*PINN vs reference along a line*

![Integro-differential ODE — PINN vs reference along a line](assets/Images/DeepXDE/Integro_differential_equation/line_comparison.png)

</details>

<details id="dx-volterra-integro-differential-equation">
<summary><strong>Integro-differential ODE – Volterra kernel</strong></summary>

DeepXDE example: [`Volterra_IDE.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Volterra_IDE.py)

$$\Large \frac{du}{dt} + u(t) = \int_0^t e^{s - t}\ u(s)\ ds, \qquad t \in [0, 5]$$

- **Problem dimension:** ODE (t) — `du_t + u - integral(exp(s - t)*u)`, the kernel and $u$ written in the integration variable `s`
- **Initial condition:** $u(0) = 1$
- **Integral:** 20-point Gauss-Legendre quadrature; 10 uniformly spaced collocation points; L-BFGS only, as in DeepXDE's script
- **Exact solution:** $u = e^{-t}\cosh t$
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot uniform
- **Training:** L-BFGS 15,000; 10 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Integro-differential ODE – Volterra kernel**

**Result (RTX 4090):** $L_2$ = 2.5 × 10⁻³

*PINN vs reference along a line*

![Integro-differential ODE – Volterra kernel — PINN vs reference along a line](assets/Images/DeepXDE/Volterra_integro_differential_equation/line_comparison.png)

</details>

<details id="dx-ode-system">
<summary><strong>Linear ODE system</strong></summary>

DeepXDE example: [`ode_system.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/ode_system.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/ode.system.html))

$$\Large \frac{dy_1}{dt} = y_2, \qquad \frac{dy_2}{dt} = -y_1, \qquad t \in [0, 10]$$

- **Problem dimension:** ODE (t) — derivatives written `dy1_t`, `dy2_t`
- **Initial conditions:** $y_1(0) = 0$, $y_2(0) = 1$
- **Exact solution:** $y_1 = \sin t$, $y_2 = \cos t$
- **Network:** FNN [2, 50, 50, 50, 2], tanh, Glorot uniform
- **Training:** Adam 20,000; 35 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Linear ODE system**

**Result (RTX 4090):** $L_2$ = 3.6 × 10⁻³ ($y_1$), 3.1 × 10⁻³ ($y_2$)

*y1 — PINN vs reference along a line*

![Linear ODE system — PINN vs reference along a line (y1)](assets/Images/DeepXDE/ODE_system/line_comparison_y1.png)

*y2 — PINN vs reference along a line*

![Linear ODE system — PINN vs reference along a line (y2)](assets/Images/DeepXDE/ODE_system/line_comparison_y2.png)

</details>

<details id="dx-lotka-volterra-equation">
<summary><strong>Lotka-Volterra ODE</strong></summary>

DeepXDE example: [`Lotka_Volterra.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Lotka_Volterra.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/Lotka.Volterra.html))

$$\Large \frac{dr}{dt} = \frac{R}{U}\left(2Ur - 0.04U^2 rp\right), \qquad \frac{dp}{dt} = \frac{R}{U}\left(0.02U^2 rp - 1.06Up\right), \qquad t \in [0, 1]$$

- **Problem dimension:** ODE (t); populations scaled by $U = 200$ and time by $R = 20$ (constants `ub`, `rb`)
- **Initial conditions:** $r(0) = 100/U$, $p(0) = 15/U$, imposed exactly by the output transform $\hat r = r\tanh t + 100/U$, $\hat p = p\tanh t + 15/U$
- **Input features:** $(t, \sin t, \sin 2t, \ldots, \sin 6t)$ through an input-transform formula
- **Reference:** SciPy `solve_ivp` solution of the same system
- **Constants:** `ub = 200`, `rb = 20`
- **Network:** FNN [2, 64, 64, 64, 64, 64, 64, 2], tanh, Glorot normal
- **Training:** Adam 50,000 → L-BFGS 15,000; 3,000 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Lotka-Volterra ODE**

**Result (RTX 4090):** $L_2$ = 2.1 × 10⁻³ ($r$), 1.4 × 10⁻³ ($p$)

*r — PINN vs reference along a line*

![Lotka-Volterra ODE — PINN vs reference along a line (r)](assets/Images/DeepXDE/Lotka_Volterra_equation/line_comparison_r.png)

*p — PINN vs reference along a line*

![Lotka-Volterra ODE — PINN vs reference along a line (p)](assets/Images/DeepXDE/Lotka_Volterra_equation/line_comparison_p.png)

</details>

<details id="dx-second-order-ode">
<summary><strong>Second-order ODE</strong></summary>

DeepXDE example: [`ode_2nd.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/ode_2nd.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/ode.2nd.html))

$$\Large \frac{d^2u}{dt^2} - 10\frac{du}{dt} + 9u = 5t, \qquad t \in [0, 0.25]$$

- **Problem dimension:** ODE (t) — `du_tt - 10*du_t + 9*u - 5*t`
- **Initial conditions:** $u(0) = -1$ (initial condition); $u'(0) = 2$ as an Operator BC `du_t - 2` applied at the initial time
- **Loss weights:** 0.01 for the equation, 1 for both initial conditions, as in DeepXDE's script
- **Exact solution:** $u = \frac{50}{81} + \frac{5}{9}t - 2e^{t} + \frac{31}{81}e^{9t}$
- **Network:** FNN [2, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Second-order ODE**

**Result (RTX 4090):** $L_2$ = 3.2 × 10⁻⁵

*PINN vs reference along a line*

![Second-order ODE — PINN vs reference along a line](assets/Images/DeepXDE/Second_order_ODE/line_comparison.png)

</details>

<details id="dx-inverse-lorenz-system">
<summary><strong>Lorenz ODE – unknown C₁, C₂, C₃</strong></summary>

DeepXDE example: [`Lorenz_inverse.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/Lorenz_inverse.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse/Lorenz.inverse.html))

$$\Large \frac{dy_1}{dt} = C_1(y_2 - y_1), \qquad \frac{dy_2}{dt} = y_1(C_2 - y_3) - y_2, \qquad \frac{dy_3}{dt} = y_1y_2 - C_3y_3, \qquad t \in [0, 3]$$

- **Problem dimension:** ODE (t); initial conditions $y(0) = (-8, 7, 27)$
- **Unknowns:** $C_1, C_2, C_3$ (true $10, 15, 8/3$), all starting from 1
- **Data:** $y_1, y_2, y_3$ measured at 50 times (also used as anchor points), from SciPy's `solve_ivp`
- **Network:** FNN [2, 40, 40, 40, 3], tanh, Glorot uniform
- **Training:** Adam 20,000 → L-BFGS 15,000; 400 domain, 2 boundary points
- **In PINNStudio:** Examples → **Inverse** → **Lorenz ODE – unknown C₁, C₂, C₃**

**Result (RTX 4090):** $C_1$ = 9.9990, $C_2$ = 14.9997, $C_3$ = 2.66675 (true 10, 15, 8/3); $L_2$ = 1.2 × 10⁻⁴ ($y_1$), 1.2 × 10⁻⁴ ($y_2$), 6.7 × 10⁻⁵ ($y_3$)

*y1 — PINN vs reference along a line*

![Lorenz ODE – unknown C₁, C₂, C₃ — PINN vs reference along a line (y1)](assets/Images/DeepXDE/Inverse_Lorenz_system/line_comparison_y1.png)

*y3 — PINN vs reference along a line*

![Lorenz ODE – unknown C₁, C₂, C₃ — PINN vs reference along a line (y3)](assets/Images/DeepXDE/Inverse_Lorenz_system/line_comparison_y3.png)

*y1 — inferred parameters during training*

![Lorenz ODE – unknown C₁, C₂, C₃ — inferred parameters during training (y1)](assets/Images/DeepXDE/Inverse_Lorenz_system/param_plot.png)

</details>

<details id="dx-inverse-lorenz-system-with-exogenous-input">
<summary><strong>Lorenz ODE – unknown C₁, C₂, C₃, exogenous input</strong></summary>

DeepXDE example: [`Lorenz_inverse_forced.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/Lorenz_inverse_forced.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse/Lorenz.inverse.forced.html))

$$\Large \frac{dy_1}{dt} = C_1(y_2 - y_1), \qquad \frac{dy_2}{dt} = y_1(C_2 - y_3) - y_2, \qquad \frac{dy_3}{dt} = y_1y_2 - C_3y_3 + 10\sin(2\pi t)$$

- **Problem dimension:** ODE (t), $t \in [0, 3]$; initial conditions $y(0) = (-8, 7, 27)$
- **Exogenous input:** $f(t) = 10\sin(2\pi t)$, written straight into the equation
- **Unknowns:** $C_1, C_2, C_3$ (true $10, 15, 8/3$), all starting from 1
- **Data:** $y_1, y_2, y_3$ measured at 200 times, from SciPy's `solve_ivp`
- **Network:** FNN [2, 40, 40, 40, 3], tanh, Glorot uniform
- **Training:** Adam 60,000; 400 domain, 2 boundary points
- **In PINNStudio:** Examples → **Inverse** → **Lorenz ODE – unknown C₁, C₂, C₃, exogenous input**

**Result (RTX 4090):** $C_1$ = 9.987, $C_2$ = 14.998, $C_3$ = 2.6669 (true 10, 15, 8/3); $L_2$ = 7.3 × 10⁻⁴ ($y_1$), 6.6 × 10⁻⁴ ($y_2$), 2.9 × 10⁻⁴ ($y_3$)

*y1 — PINN vs reference along a line*

![Lorenz ODE – unknown C₁, C₂, C₃, exogenous input — PINN vs reference along a line (y1)](assets/Images/DeepXDE/Inverse_Lorenz_system_with_exogenous_input/line_comparison_y1.png)

*y3 — PINN vs reference along a line*

![Lorenz ODE – unknown C₁, C₂, C₃, exogenous input — PINN vs reference along a line (y3)](assets/Images/DeepXDE/Inverse_Lorenz_system_with_exogenous_input/line_comparison_y3.png)

*y1 — inferred parameters during training*

![Lorenz ODE – unknown C₁, C₂, C₃, exogenous input — inferred parameters during training (y1)](assets/Images/DeepXDE/Inverse_Lorenz_system_with_exogenous_input/param_plot.png)

</details>

### 1D examples

*Click an example to expand it.*

<details id="dx-euler-beam">
<summary><strong>Euler beam 1D</strong></summary>

DeepXDE example: [`Euler_beam.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Euler_beam.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/eulerbeam.html))

$$\Large \frac{d^4u}{dx^4} = -1, \qquad x \in [0, 1]$$

- **Boundary conditions:** $u(0) = 0$, $u'(0) = 0$ (clamped); $u''(1) = 0$, $u'''(1) = 0$ (free) — the last two as Operator BCs
- **Exact solution:** $u = -\frac{x^4}{24} + \frac{x^3}{6} - \frac{x^2}{4}$
- **Network:** FNN [1, 20, 20, 20, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 10 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Euler beam 1D**

**Result (RTX 4090):** $L_2$ = 8.4 × 10⁻³

*PINN vs reference along a line*

![Euler beam 1D — PINN vs reference along a line](assets/Images/DeepXDE/Euler_beam/line_comparison.png)

</details>

<details id="dx-fractional-poisson-equation-1d">
<summary><strong>Fractional Poisson 1D</strong></summary>

DeepXDE example: [`fractional_Poisson_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_Poisson_1d.py)

$$\Large D_{0+}^{\alpha}u + D_{1-}^{\alpha}u = f(x), \qquad x \in [0, 1],\ \alpha = 1.5$$

- **Equation in the panel:** `frac(u) - (...)`, with $f$ written out with `gamma(...)` as in DeepXDE's script; constant `alpha`
- **Fractional settings:** α `alpha`, resolution 101, static mesh (DeepXDE's FPDE, Grünwald-Letnikov)
- **Boundary conditions:** $u(0) = u(1) = 0$, imposed exactly by the output transform $\hat u = x(1-x)N$
- **Exact solution:** $u = x^3(1-x)^3$
- **Constants:** `alpha = 1.5`
- **Network:** FNN [1, 20, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 10,000; 101 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Fractional Poisson 1D**

**Result (RTX 4090):** $L_2$ = 3.7 × 10⁻²

*PINN vs reference along a line*

![Fractional Poisson 1D — PINN vs reference along a line](assets/Images/DeepXDE/Fractional_Poisson_equation_1D/line_comparison.png)

</details>

<details id="dx-poisson-1d-dirichlet">
<summary><strong>Poisson 1D – Dirichlet</strong></summary>

DeepXDE example: [`Poisson_Dirichlet_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Dirichlet_1d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/poisson.1d.dirichlet.html))

$$\Large -\frac{d^2u}{dx^2} = \pi^2\sin(\pi x), \qquad x \in [-1, 1]$$

- **Boundary conditions:** Dirichlet, $u(\pm 1) = 0$ — in the panel: Where `True` (whole boundary), Value `0`
- **Exact solution:** $u = \sin(\pi x)$
- **Network:** FNN [1, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – Dirichlet**

**Result (RTX 4090):** $L_2$ = 3.7 × 10⁻⁴

*PINN vs reference along a line*

![Poisson 1D – Dirichlet — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_Dirichlet/line_comparison.png)

</details>

<details id="dx-poisson-1d-dirichlet-neumann">
<summary><strong>Poisson 1D – Dirichlet/Neumann</strong></summary>

DeepXDE example: [`Poisson_Neumann_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Neumann_1d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/poisson.1d.neumanndirichlet.html))

$$\Large \frac{d^2u}{dx^2} = 2, \qquad x \in [-1, 1]$$

- **Boundary conditions:** Dirichlet $u(-1) = 0$ (Where `left`, Value `0`); Neumann $u'(1) = 4$ (Where `right`, Value `4` — at the right end the outward normal derivative is $du/dx$)
- **Exact solution:** $u = (x + 1)^2$
- **Network:** FNN [1, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – Dirichlet/Neumann**

**Result (RTX 4090):** $L_2$ = 2.3 × 10⁻⁴

*PINN vs reference along a line*

![Poisson 1D – Dirichlet/Neumann — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_Dirichlet_Neumann/line_comparison.png)

</details>

<details id="dx-poisson-1d-dirichlet-periodic">
<summary><strong>Poisson 1D – Dirichlet/Periodic</strong></summary>

DeepXDE example: [`Poisson_periodic_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_periodic_1d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/poisson.1d.dirichletperiodic.html))

$$\Large -\frac{d^2u}{dx^2} = \pi^2\sin(\pi x), \qquad x \in [-1, 1]$$

- **Boundary conditions:** Dirichlet $u(-1) = 0$ (Where `left`); periodic $u(-1) = u(1)$ (Where `right`)
- **Exact solution:** $u = \sin(\pi x)$
- **Network:** FNN [1, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – Dirichlet/Periodic**

**Result (RTX 4090):** $L_2$ = 1.2 × 10⁻²

*PINN vs reference along a line*

![Poisson 1D – Dirichlet/Periodic — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_Dirichlet_Periodic/line_comparison.png)

</details>

<details id="dx-poisson-1d-dirichlet-pointsetoperator">
<summary><strong>Poisson 1D – Dirichlet/point-set operator</strong></summary>

DeepXDE example: [`Poisson_PointSetOperator_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_PointSetOperator_1d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/poisson.1d.pointsetoperator.html))

$$\Large \frac{d^2u}{dx^2} = 2, \qquad x \in [-1, 1]$$

- **Boundary conditions:** Dirichlet $u(-1) = 0$ (Where `left`); point-set operator condition $u'(1) = 4$ — a Point Set Operator row with the point typed in (Points `1`, Function `du_x`, Target value `4`; no file)
- **Exact solution:** $u = (x + 1)^2$
- **Network:** FNN [1, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 20,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – Dirichlet/point-set operator**

**Result (RTX 4090):** $L_2$ = 2.6 × 10⁻⁵

*PINN vs reference along a line*

![Poisson 1D – Dirichlet/point-set operator — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_Dirichlet_PointSetOperator/line_comparison.png)

</details>

<details id="dx-poisson-1d-dirichlet-robin">
<summary><strong>Poisson 1D – Dirichlet/Robin</strong></summary>

DeepXDE example: [`Poisson_Robin_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Robin_1d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/poisson.1d.dirichletrobin.html))

$$\Large \frac{d^2u}{dx^2} = 2, \qquad x \in [-1, 1]$$

- **Boundary conditions:** Dirichlet $u(-1) = 0$ (Where `left`); Robin $u'(1) = u(1)$ (Where `right`, Value `u`)
- **Exact solution:** $u = (x + 1)^2$
- **Network:** FNN [1, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 16 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – Dirichlet/Robin**

**Result (RTX 4090):** $L_2$ = 2.4 × 10⁻⁴

*PINN vs reference along a line*

![Poisson 1D – Dirichlet/Robin — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_Dirichlet_Robin/line_comparison.png)

</details>

<details id="dx-poisson-1d-hard-boundary-conditions">
<summary><strong>Poisson 1D – hard BCs</strong></summary>

DeepXDE example: [`Poisson_Dirichlet_1d_exactBC.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_Dirichlet_1d_exactBC.py)

$$\Large -\frac{d^2u}{dx^2} = \sum_{k=1}^{4} k\sin(kx) + 8\sin(8x), \qquad x \in [0, \pi]$$

- **Boundary conditions:** $u(0) = 0$, $u(\pi) = \pi$, imposed exactly by the output transform $\hat u = x(\pi - x)\ N(x) + x$
- **Exact solution:** $u = x + \sum_{k=1}^{4}\frac{\sin(kx)}{k} + \frac{\sin(8x)}{8}$
- **Learning rate:** inverse-time decay, $10^{-4}/(1 + 0.3\ n/1000)$ at iteration $n$
- **Network:** FNN [1, 50, 50, 50, 1], tanh, Glorot uniform
- **Training:** Adam 30,000; 64 domain points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – hard BCs**

**Result (RTX 4090):** $L_2$ = 2.2 × 10⁻⁶

*PINN vs reference along a line*

![Poisson 1D – hard BCs — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_hard_boundary_conditions/line_comparison.png)

</details>

<details id="dx-poisson-1d-multi-scale-fourier-features">
<summary><strong>Poisson 1D – multi-scale Fourier features</strong></summary>

DeepXDE example: [`Poisson_multiscale_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Poisson_multiscale_1d.py)

$$\Large \frac{d^2u}{dx^2} = -(\pi A)^2\sin(\pi A x) - 0.1(\pi B)^2\sin(\pi B x), \qquad x \in [0, 1],\ A = 2,\ B = 50$$

- **Boundary conditions:** $u(0) = u(1) = 0$
- **Exact solution:** $u = \sin(2\pi x) + 0.1\sin(50\pi x)$ — a slow wave plus a fast, small one
- **Network:** a multi-scale Fourier feature network (MsFFN): the input goes through random Fourier features with scales $\sigma = 1$ and $10$, each through the same hidden layers, then combined
- **Points:** 1,280 pseudo-random collocation points, redrawn every iteration; learning rate $10^{-3}/(1 + 0.9\ n/2000)$
- **Constants:** `A = 2`, `B = 50`
- **Network:** MsFFN [1, 100, 100, 100, 1], Fourier scales σ = 1, 10, tanh, Glorot uniform
- **Training:** Adam 20,000; 1,280 domain, 2 boundary points
- **In PINNStudio:** Examples → **Forward** → **Poisson 1D – multi-scale Fourier features**

A plain network of the same size learns the slow wave and largely misses the fast one; the Fourier features at scale 10 are what let the PINN represent the sin(50πx) part.

**Result (RTX 4090):** $L_2$ = 3.9 × 10⁻³

*PINN vs reference along a line*

![Poisson 1D – multi-scale Fourier features — PINN vs reference along a line](assets/Images/DeepXDE/Poisson_1D_multi_scale_Fourier_features/line_comparison.png)

</details>

<details id="dx-inverse-brinkman-forchheimer-model">
<summary><strong>Brinkman-Forchheimer 1D – unknown ν_e, K</strong></summary>

DeepXDE example: [`brinkman_forchheimer.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/brinkman_forchheimer.py)

$$\Large -\frac{\nu_e}{\epsilon}\frac{d^2u}{dx^2} + \frac{\nu u}{K} = g, \qquad x \in [0, 1],\ \epsilon = 0.4,\ \nu = 10^{-3},\ g = 1$$

- **Unknowns:** effective viscosity $\nu_e$ and permeability $K$ (both $10^{-3}$, initial guesses 0.1)
- **Data:** 5 measurements of $u$; $u = 0$ at both walls through the output transform $\hat u = x(1-x)N$
- **Exact solution:** $u = 1 - \cosh(20(x - 0.5))/\cosh(10)$
- **Constants:** `g = 1`, `v = 1e-3`, `e = 0.4`
- **Network:** FNN [1, 20, 20, 20, 1], tanh, Glorot uniform
- **Training:** Adam 30,000; 100 domain points
- **In PINNStudio:** Examples → **Inverse** → **Brinkman-Forchheimer 1D – unknown ν_e, K**

DeepXDE's own script, run unchanged twice on the same GPU, ends with $\nu_e$ = 1.31–1.35 × 10⁻³, $K$ = 9.84 × 10⁻⁴ and an $L_2$ error of 1.8 × 10⁻²–2.0 × 10⁻² for $u$ — the same picture: $K$ is recovered closely, $\nu_e$ only to within about 30–50% from five measurements.

**Result (RTX 4090):** $\nu_e$ = 1.49 × 10⁻³, $K$ = 9.85 × 10⁻⁴ (both true 1 × 10⁻³); $L_2$ of $u$ = 2.9 × 10⁻²

*PINN vs reference along a line*

![Brinkman-Forchheimer 1D – unknown ν_e, K — PINN vs reference along a line](assets/Images/DeepXDE/Inverse_Brinkman_Forchheimer_model/line_comparison.png)

*Inferred parameters during training*

![Brinkman-Forchheimer 1D – unknown ν_e, K — inferred parameters during training](assets/Images/DeepXDE/Inverse_Brinkman_Forchheimer_model/param_plot.png)

</details>

<details id="dx-inverse-diffusion-reaction-with-space-dependent-rate">
<summary><strong>Diffusion-reaction 1D – unknown rate field</strong></summary>

DeepXDE example: [`diffusion_reaction_rate.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/diffusion_reaction_rate.py)

$$\Large \lambda\frac{d^2u}{dx^2} - k(x)\ u = \sin(2\pi x), \qquad \lambda = 0.01,\ x \in [0, 1]$$

- **Unknown:** the reaction rate $k(x)$ (true $0.1 + e^{-0.5(x - 0.5)^2/0.15^2}$), learned as a second network output
- **Data:** 100 measurements of $u$ (computed with SciPy's `solve_bvp`, as DeepXDE does), $u = 0$ at both ends
- **Constants:** `l = 0.01`
- **Network:** PFNN, a separate [20, 20] subnetwork for each of the 2 outputs, tanh, Glorot uniform
- **Training:** Adam 20,000; 50 domain, 8 boundary points
- **In PINNStudio:** Examples → **Inverse** → **Diffusion-reaction 1D – unknown rate field**

**Result (RTX 4090):** $L_2$ = 4.0 × 10⁻² ($k$)

*u — PINN vs reference along a line*

![Diffusion-reaction 1D – unknown rate field — PINN vs reference along a line (u)](assets/Images/DeepXDE/Inverse_diffusion_reaction_with_space_dependent_rate/line_comparison.png)

*u — PINN solution*

![Diffusion-reaction 1D – unknown rate field — PINN solution (u)](assets/Images/DeepXDE/Inverse_diffusion_reaction_with_space_dependent_rate/solution_plot.png)

</details>

<details id="dx-inverse-fractional-poisson-equation-1d">
<summary><strong>Fractional Poisson 1D – unknown order α</strong></summary>

DeepXDE example: [`fractional_Poisson_1d_inverse.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/fractional_Poisson_1d_inverse.py)

$$\Large \frac{D_{-1+}^{\alpha}u + D_{1-}^{\alpha}u}{2\cos(\alpha\pi/2)} = \Gamma(\alpha_0 + 2)\ x, \qquad x \in [-1, 1]$$

- **Unknown:** the order $\alpha$ (true $\alpha_0 = 1.8$, start 1.5) — an inverse variable named `alpha`, also the fractional α
- **Data:** 20 measurements of $u = x(1 - x^2)^{\alpha_0/2}$, loss weight 100
- **Fractional settings:** 100 points per unit length, dynamic mesh (rebuilt every step as α changes)
- **Constants:** `a0 = 1.8`
- **Network:** FNN [1, 20, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 10,000; 20 domain points
- **In PINNStudio:** Examples → **Inverse** → **Fractional Poisson 1D – unknown order α**

**Result (RTX 4090):** $\alpha$ = 1.792 (true 1.8); $L_2$ of $u$ = 1.3 × 10⁻²

*PINN vs reference along a line*

![Fractional Poisson 1D – unknown order α — PINN vs reference along a line](assets/Images/DeepXDE/Inverse_fractional_Poisson_equation_1D/line_comparison.png)

*Inferred parameters during training*

![Fractional Poisson 1D – unknown order α — inferred parameters during training](assets/Images/DeepXDE/Inverse_fractional_Poisson_equation_1D/param_plot.png)

</details>

<details id="dx-inverse-poisson-with-unknown-forcing-field">
<summary><strong>Poisson 1D – unknown forcing field</strong></summary>

DeepXDE example: [`elliptic_inverse_field.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/elliptic_inverse_field.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse/elliptic.inverse.field.html))

$$\Large -\frac{d^2u}{dx^2} + q(x) = 0, \qquad x \in [-1, 1]$$

- **Unknown:** the field $q(x)$ (true $-\pi^2\sin(\pi x)$), learned as a second network output
- **Data:** 100 measurements of $u$, given as a Point Set BC (and as anchor points); $u = \sin(\pi x)$ on the boundary
- **Mode:** Forward — there are no unknown constants, only an unknown field, as in DeepXDE
- **Network:** PFNN, a separate [20, 20, 20] subnetwork for each of the 2 outputs, tanh, Glorot uniform
- **Training:** Adam 20,000; 200 domain, 2 boundary points
- **In PINNStudio:** Examples → **Inverse** → **Poisson 1D – unknown forcing field**

**Result (RTX 4090):** $L_2$ = 8.3 × 10⁻⁴ ($u$), 4.3 × 10⁻² ($q$)

*u — PINN vs reference along a line*

![Poisson 1D – unknown forcing field — PINN vs reference along a line (u)](assets/Images/DeepXDE/Inverse_Poisson_with_unknown_forcing_field/line_comparison_u.png)

*q — PINN vs reference along a line*

![Poisson 1D – unknown forcing field — PINN vs reference along a line (q)](assets/Images/DeepXDE/Inverse_Poisson_with_unknown_forcing_field/line_comparison_q.png)

</details>

<details id="dx-inverse-poisson-with-unknown-forcing-field-batches">
<summary><strong>Poisson 1D – unknown forcing field (batches)</strong></summary>

DeepXDE example: [`elliptic_inverse_field_batch.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/elliptic_inverse_field_batch.py)

$$\Large -\frac{d^2u}{dx^2} + q(x) = 0, \qquad x \in [-1, 1]$$

- **Unknown:** the field $q(x)$ (true $-\pi^2\sin(\pi x)$)
- **Data:** 10,000 measurements of $u$, used 100 at a time (Point Set BC with batch size 100, redrawn every iteration)
- **Network:** PFNN, a separate [20, 20, 20] subnetwork for each of the 2 outputs, tanh, Glorot uniform
- **Training:** Adam 20,000; 200 domain, 2 boundary points
- **In PINNStudio:** Examples → **Inverse** → **Poisson 1D – unknown forcing field (batches)**

**Result (RTX 4090):** $L_2$ = 7.6 × 10⁻³ ($u$), 1.3 × 10⁻¹ ($q$)

*q — PINN vs reference along a line*

![Poisson 1D – unknown forcing field (batches) — PINN vs reference along a line (q)](assets/Images/DeepXDE/Inverse_Poisson_with_unknown_forcing_field_batches/line_comparison_q.png)

</details>

<details id="1d-allen-cahn">
<summary><strong>Allen-Cahn 1D – Wight & Zhao</strong></summary>

Benchmark problem after Wight & Zhao (2021) — see [References](#references).

$$\Large \frac{\partial u}{\partial t} = \gamma_1\frac{\partial^2 u}{\partial x^2} - \gamma_2 u^3 + \gamma_2 u, \qquad x \in [-1, 1],\ t \in [0, 1]$$

where $\gamma_1 = 0.0001$ and $\gamma_2 = 5$.

- **Initial condition:** $u(x, 0) = x^2\cos(\pi x)$
- **Boundary conditions:** Periodic
- **Geometry:** Interval
- **Time-Adaptive default:** on — $t \in [0,1]$ split into 4 steps of 0.25, L-BFGS transfer learning between steps
- **In PINNStudio:** Examples → **Forward** (or **Inverse**) → **Allen-Cahn 1D – Wight & Zhao**

**Result (RTX 4090):** $L_2$ = 1.5 × 10⁻⁴ ($t = 0$), 4.5 × 10⁻⁴ ($t = 0.25$), 1.0 × 10⁻³ ($t = 0.5$), 1.8 × 10⁻³ ($t = 0.75$), 4.8 × 10⁻³ ($t = 1$), against a Fourier pseudo-spectral solution (ETDRK4) in [`reference_data/1D/allen_cahn`](reference_data/1D/allen_cahn) (made by [`tools/make_exact_reference_data.py`](tools/make_exact_reference_data.py)). Inverse mode: $\gamma_1$ = 1.29 × 10⁻⁴ (true 1 × 10⁻⁴), $\gamma_2$ = 5.005 (true 5).

![1D Allen-Cahn — PINN vs Ground Truth, Error Analysis surface comparison](assets/Images/1D-AllenCahn/surface_comparison.png)

![1D Allen-Cahn — line comparison against reference data](assets/Images/1D-AllenCahn/line_comparison.png)

*Inverse mode* — same template, switched to **Inverse**, jointly recovering both $\gamma_1$ (diffusion) and $\gamma_2$ (reaction) as unknown parameters; the live convergence animation below shows each estimate settling onto its true value during training:

![1D Allen-Cahn inverse parameter convergence animation](assets/Images/1D-AllenCahn/param_convergence_animation.gif)

</details>

<details id="dx-allen-cahn-equation">
<summary><strong>Allen-Cahn 1D</strong></summary>

DeepXDE example: [`Allen_Cahn.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Allen_Cahn.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/allen.cahn.html))

$$\Large \frac{\partial u}{\partial t} = 0.001\frac{\partial^2 u}{\partial x^2} + 5(u - u^3), \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Initial and boundary conditions:** $u(x, 0) = x^2\cos(\pi x)$ and $u(\pm 1, t) = -1$, imposed exactly by $\hat u = x^2\cos(\pi x) + t(1 - x^2)N$
- **Reference:** computed by `tools/make_deepxde_reference_data.py` (agrees with DeepXDE's `Allen_Cahn.mat` to $5\times 10^{-4}$)
- **Constants:** `d = 0.001`
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 40,000 → L-BFGS 15,000; 8,000 domain, 400 boundary points
- **In PINNStudio:** Examples → **Forward** → **Allen-Cahn 1D**

**Result (RTX 4090):** $L_2$ = 9.5 × 10⁻⁸ ($t = 0$), 1.9 × 10⁻³ ($t = 0.25$), 5.2 × 10⁻³ ($t = 0.5$), 1.3 × 10⁻² ($t = 0.75$), 2.9 × 10⁻² ($t = 1$)

*u — PINN solution over time*

![Allen-Cahn 1D — PINN solution over time (u)](assets/Images/DeepXDE/Allen_Cahn_equation/animation.gif)

*PINN vs reference, error analysis*

![Allen-Cahn 1D — PINN vs reference, error analysis](assets/Images/DeepXDE/Allen_Cahn_equation/surface_comparison.png)

</details>

<details id="dx-american-put-option">
<summary><strong>Black-Scholes 1D – American put</strong></summary>

DeepXDE example: [`american_put.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/american_put.py)

$$\Large \min\left(-\mathcal{L}V,\ V - \max(K - S, 0)\right) = 0, \qquad \mathcal{L}V = -\frac{\partial V}{\partial \tau} + \frac{\sigma^2}{2}S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV$$

- **Domain:** $S \in [0, 4]$, $\tau \in [0, 1]$; strike $K = 1$, $r = 0.05$, $\sigma = 0.2$
- **Equations:** three residuals for one output (DeepXDE's Fischer-Burmeister form of the complementarity problem)
- **Extra points:** 1000 anchors in $S \in [0.5, 1.5]$ around the exercise boundary; point resampling every 1000 iterations
- **Reference:** none bundled (DeepXDE compares against a binomial-tree price) — add your own in Error Analysis
- **Constants:** `r = 0.05`, `sigma = 0.2`, `K = 1`
- **Network:** FNN [2, 128, 128, 128, 128, 1], tanh, Glorot normal
- **Training:** Adam 12,000 → L-BFGS 15,000; 6,000 domain, 1,500 boundary, 1,500 initial points
- **In PINNStudio:** Examples → **Forward** → **Black-Scholes 1D – American put**

**Result (RTX 4090):** trained without errors; no bundled reference to compare against

*u — PINN solution over time*

![Black-Scholes 1D – American put — PINN solution over time (u)](assets/Images/DeepXDE/American_put_option/animation.gif)

</details>

<details id="dx-black-scholes-equation-call-option">
<summary><strong>Black-Scholes 1D – European call</strong></summary>

DeepXDE example: [`black_scholes_call.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/black_scholes_call.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/black_scholes.html))

$$\Large \frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}S^2\frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV, \qquad S \in [0, 150],\ \tau \in [0, 1]$$

- **Parameters:** strike $K = 50$, rate $r = 0.05$, volatility $\sigma = 0.2$; $x$ is the stock price $S$ and $t$ the time to maturity $\tau$
- **Initial condition:** payoff $V(S, 0) = \max(S - K, 0)$; **boundary conditions:** $V(0, \tau) = 0$, $V(150, \tau) = 150 - Ke^{-r\tau}$
- **Exact solution:** the Black-Scholes formula (uses `norm_cdf` in the reference formula)
- **Constants:** `K = 50`, `r = 0.05`, `sigma = 0.2`
- **Network:** FNN [2, 28, 28, 28, 28, 1], tanh, Glorot normal
- **Training:** Adam 20,000 → L-BFGS 15,000; 2,047 domain, 63 boundary, 127 initial points
- **In PINNStudio:** Examples → **Forward** → **Black-Scholes 1D – European call**

**Result (RTX 4090):** $L_2$ = 5.7 × 10⁻⁴ ($t = 0.25$), 3.2 × 10⁻⁴ ($t = 0.5$), 4.3 × 10⁻⁴ ($t = 1$)

*u — PINN solution over time*

![Black-Scholes 1D – European call — PINN solution over time (u)](assets/Images/DeepXDE/Black_Scholes_equation_call_option/animation.gif)

*PINN vs reference, error analysis*

![Black-Scholes 1D – European call — PINN vs reference, error analysis](assets/Images/DeepXDE/Black_Scholes_equation_call_option/surface_comparison.png)

</details>

<details id="1d-burgers">
<summary><strong>Burgers 1D – Raissi et al.</strong></summary>

Exact equation, initial and boundary conditions as in Raissi, Perdikaris & Karniadakis (2019) — see [References](#references).

$$\Large \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = \frac{0.01}{\pi}\frac{\partial^2 u}{\partial x^2}, \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Initial condition:** $u(x, 0) = -\sin(\pi x)$
- **Boundary conditions:** Dirichlet, $u = 0$ at both ends
- **Geometry:** Interval
- **In PINNStudio:** Examples → **Forward** (or **Inverse**) → **Burgers 1D – Raissi et al.**

A shock forms near $x = 0$ as $t \to 1$; this template uses a larger fixed collocation count to resolve it rather than adaptive refinement.

**Result (RTX 4090):** $L_2$ = 6.0 × 10⁻⁵ ($t = 0$), 3.7 × 10⁻⁴ ($t = 0.25$), 7.2 × 10⁻⁴ ($t = 0.5$), 1.2 × 10⁻³ ($t = 0.75$), 1.3 × 10⁻³ ($t = 1$), against the exact (Cole–Hopf) solution in [`reference_data/1D/burgers`](reference_data/1D/burgers). Inverse mode: $\lambda_1$ = 0.997 (true 1), $\lambda_2$ = 0.01001 (true 0.01; the template writes the viscous term as $\frac{\lambda_2}{\pi}\frac{\partial^2 u}{\partial x^2}$, so $\lambda_2 = 0.01$ is the paper's $0.01/\pi$).

![1D Burgers — PINN vs Ground Truth, Error Analysis surface comparison](assets/Images/1D-Burgers/surface_comparison.png)

![1D Burgers — line comparison against reference data](assets/Images/1D-Burgers/line_comparison.png)

*Restore & Visualize* — the trained model restored from its saved checkpoint and re-animated without retraining:

![1D Burgers — restored solution animation](assets/Images/1D-Burgers/restored_animation.gif)

*Inverse mode* — same template, switched to **Inverse**, jointly recovering both coefficients of Raissi, Perdikaris & Karniadakis (2019)'s data-driven-discovery form of this equation, Appendix B, eq. B.1 — see [References](#references):

$$\Large \frac{\partial u}{\partial t} + \lambda_1 u\frac{\partial u}{\partial x} - \lambda_2\frac{\partial^2 u}{\partial x^2} = 0$$

with true values $\lambda_1 = 1.0$ and $\lambda_2 = 0.01/\pi$. $\lambda_1$'s initial guess starts at $0.1$ rather than $1.0$, since $1.0$ is already its true value. The live convergence animation below shows both estimates settling onto their true values during training:

![1D Burgers inverse parameter convergence animation](assets/Images/1D-Burgers/param_convergence_animation.gif)

</details>

<details id="dx-burgers-equation-with-rar">
<summary><strong>Burgers 1D – RAR</strong></summary>

DeepXDE example: [`Burgers_RAR.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Burgers_RAR.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/burgers.rar.html))

$$\Large \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = \frac{0.01}{\pi}\frac{\partial^2 u}{\partial x^2}, \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Initial / boundary conditions:** $u(x, 0) = -\sin(\pi x)$, $u(\pm 1, t) = 0$
- **Time range / reference:** $t \in [0, 1]$, compared with the exact solution at $t = 0, 0.25, 0.5, 0.75, 1$
- **Residual-based adaptive refinement:** 3 rounds, each adding the 100 points with the largest PDE residual (out of 100,000 random candidates) and retraining (Adam 10,000 → L-BFGS 15,000)
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 10,000 → L-BFGS 15,000 per RAR round; 2,500 domain, 100 boundary, 160 initial points
- **In PINNStudio:** Examples → **Forward** → **Burgers 1D – RAR**

**Why not DeepXDE's one-point refinement.** DeepXDE's script adds 1 point per round until the mean residual is below 0.005. Here, after the first training the mean residual is already about 3–4 × 10⁻³, so that loop would add a single point and stop, which shows nothing. This example therefore turns the tolerance off and runs 3 rounds of 100 points instead. The collocation-point figure below shows where they go: onto the shock at $x = 0$ once it has formed ($t \gtrsim 0.3$), the region of largest error. The $L_2$ error at $t = 1$, where the shock is steepest, falls from 2.6 × 10⁻² after round 1 to 4.0 × 10⁻³ after round 2 and 8.4 × 10⁻⁴ after round 3.

**Result (RTX 4090):** $L_2$ = 3.1 × 10⁻³ ($t = 0$), 4.6 × 10⁻³ ($t = 0.25$), 1.0 × 10⁻³ ($t = 0.5$), 1.3 × 10⁻³ ($t = 0.75$), 8.4 × 10⁻⁴ ($t = 1$)

*u — PINN solution over time*

![Burgers 1D – RAR — PINN solution over time (u)](assets/Images/DeepXDE/Burgers_equation_with_RAR/animation.gif)

*PINN vs reference, error analysis*

![Burgers 1D – RAR — PINN vs reference, error analysis](assets/Images/DeepXDE/Burgers_equation_with_RAR/surface_comparison.png)

*Collocation points after the last RAR round: original points (gray), points added in earlier rounds (orange) and in the last round (red)*

![Burgers 1D – RAR — collocation points after the last RAR round: original points (gray), points added in earlier rounds (orange) and in the last round (red)](assets/Images/DeepXDE/Burgers_equation_with_RAR/rar_collocation_points.png)

</details>

<details id="dx-diffusion-equation">
<summary><strong>Diffusion 1D</strong></summary>

DeepXDE example: [`diffusion_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_1d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/diffusion.1d.html))

$$\Large \frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} - e^{-t}\left(\sin(\pi x) - \pi^2\sin(\pi x)\right), \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Initial condition:** $u(x, 0) = \sin(\pi x)$; **boundary condition:** $u = e^{-t}\sin(\pi x)$
- **Exact solution:** $u = e^{-t}\sin(\pi x)$
- **Network:** FNN [2, 32, 32, 32, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 40 domain, 20 boundary, 10 initial points
- **In PINNStudio:** Examples → **Forward** → **Diffusion 1D**

**Result (RTX 4090):** $L_2$ = 4.8 × 10⁻³ ($t = 0$), 9.0 × 10⁻³ ($t = 0.25$), 6.4 × 10⁻³ ($t = 0.5$), 5.8 × 10⁻³ ($t = 0.75$), 3.0 × 10⁻² ($t = 1$)

*u — PINN solution over time*

![Diffusion 1D — PINN solution over time (u)](assets/Images/DeepXDE/Diffusion_equation/animation.gif)

*PINN vs reference, error analysis*

![Diffusion 1D — PINN vs reference, error analysis](assets/Images/DeepXDE/Diffusion_equation/surface_comparison.png)

</details>

<details id="dx-diffusion-equation-with-hard-ic-and-bc">
<summary><strong>Diffusion 1D – hard IC and BCs</strong></summary>

DeepXDE example: [`diffusion_1d_exactBC.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_1d_exactBC.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/diffusion.1d.exactBC.html))

$$\Large \frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} - e^{-t}\left(\sin(\pi x) - \pi^2\sin(\pi x)\right), \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Initial and boundary conditions:** imposed exactly by $\hat u = t(1 - x^2)N + \sin(\pi x)$ — no IC/BC loss terms
- **Exact solution:** $u = e^{-t}\sin(\pi x)$
- **Network:** FNN [2, 32, 32, 32, 1], tanh, Glorot uniform
- **Training:** Adam 10,000; 40 domain points
- **In PINNStudio:** Examples → **Forward** → **Diffusion 1D – hard IC and BCs**

**Result (RTX 4090):** $L_2$ = 9.4 × 10⁻⁸ ($t = 0$), 1.6 × 10⁻⁴ ($t = 0.25$), 4.6 × 10⁻⁴ ($t = 0.5$), 1.3 × 10⁻³ ($t = 0.75$), 2.8 × 10⁻³ ($t = 1$)

*u — PINN solution over time*

![Diffusion 1D – hard IC and BCs — PINN solution over time (u)](assets/Images/DeepXDE/Diffusion_equation_with_hard_IC_and_BC/animation.gif)

*PINN vs reference, error analysis*

![Diffusion 1D – hard IC and BCs — PINN vs reference, error analysis](assets/Images/DeepXDE/Diffusion_equation_with_hard_IC_and_BC/surface_comparison.png)

</details>

<details id="dx-diffusion-equation-with-resampling">
<summary><strong>Diffusion 1D – resampling</strong></summary>

DeepXDE example: [`diffusion_1d_resample.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_1d_resample.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/diffusion.1d.resample.html))

$$\Large \frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} - e^{-t}\left(\sin(\pi x) - \pi^2\sin(\pi x)\right), \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Initial / boundary conditions:** $u(x, 0) = \sin(\pi x)$, $u = e^{-t}\sin(\pi x)$ on the boundary
- **Point resampling:** pseudo-random collocation points redrawn every 100 iterations
- **Exact solution:** $u = e^{-t}\sin(\pi x)$
- **Network:** FNN [2, 32, 32, 32, 1], tanh, Glorot uniform
- **Training:** Adam 2,000; 40 domain, 20 boundary, 10 initial points
- **In PINNStudio:** Examples → **Forward** → **Diffusion 1D – resampling**

**Result (RTX 4090):** $L_2$ = 1.8 × 10⁻² ($t = 0$), 2.5 × 10⁻² ($t = 0.25$), 1.5 × 10⁻² ($t = 0.5$), 1.4 × 10⁻² ($t = 0.75$), 4.3 × 10⁻² ($t = 1$)

*u — PINN solution over time*

![Diffusion 1D – resampling — PINN solution over time (u)](assets/Images/DeepXDE/Diffusion_equation_with_resampling/animation.gif)

*PINN vs reference, error analysis*

![Diffusion 1D – resampling — PINN vs reference, error analysis](assets/Images/DeepXDE/Diffusion_equation_with_resampling/surface_comparison.png)

</details>

<details id="dx-diffusion-reaction-equation">
<summary><strong>Diffusion-reaction 1D</strong></summary>

DeepXDE example: [`diffusion_reaction.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/diffusion_reaction.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/diffusion.reaction.html))

$$\Large \frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2} + e^{-t}\left(\tfrac{3}{2}\sin 2x + \tfrac{8}{3}\sin 3x + \tfrac{15}{4}\sin 4x + \tfrac{63}{8}\sin 8x\right), \qquad x \in [-\pi, \pi],\ t \in [0, 1]$$

- **Initial and boundary conditions:** imposed exactly by $\hat u = t(\pi^2 - x^2)N + \sum_k \frac{\sin(kx)}{k}$
- **Exact solution:** $u = e^{-t}\left(\sin x + \tfrac{\sin 2x}{2} + \tfrac{\sin 3x}{3} + \tfrac{\sin 4x}{4} + \tfrac{\sin 8x}{8}\right)$
- **Network:** FNN [2, 30, 30, 30, 30, 30, 30, 1], tanh, Glorot uniform
- **Training:** Adam 20,000; 320 domain points
- **In PINNStudio:** Examples → **Forward** → **Diffusion-reaction 1D**

DeepXDE's own script, run unchanged on the same GPU, ends with a similar loss (and the same Adam loss spikes near the end of training).

**Result (RTX 4090):** $L_2$ = 9.9 × 10⁻⁸ ($t = 0$), 1.4 × 10⁻² ($t = 0.25$), 3.4 × 10⁻² ($t = 0.5$), 6.7 × 10⁻² ($t = 0.75$), 1.1 × 10⁻¹ ($t = 1$)

*u — PINN solution over time*

![Diffusion-reaction 1D — PINN solution over time (u)](assets/Images/DeepXDE/Diffusion_reaction_equation/animation.gif)

*PINN vs reference, error analysis*

![Diffusion-reaction 1D — PINN vs reference, error analysis](assets/Images/DeepXDE/Diffusion_reaction_equation/surface_comparison.png)

</details>

<details id="dx-fractional-diffusion-equation">
<summary><strong>Fractional diffusion 1D</strong></summary>

DeepXDE example: [`fractional_diffusion_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_diffusion_1d.py)

$$\Large \frac{\partial u}{\partial t} = D_{0+}^{\alpha}u + D_{1-}^{\alpha}u - e^{-t}\left(x^3(1-x)^3 + f_\alpha(x)\right), \qquad x \in [0, 1],\ t \in [0, 1],\ \alpha = 1.8$$

- **Equation in the panel:** `du_t - frac(u) + exp(-t)*(x**3*(1 - x)**3 + ...)` (DeepXDE's TimeFPDE)
- **Fractional settings:** 52-point static mesh in x at each time
- **Boundary and initial conditions:** $u(0, t) = u(1, t) = 0$, $u(x, 0) = x^3(1-x)^3$, both exact through $\hat u = x(1-x)\ t\ N + x^3(1-x)^3$
- **Exact solution:** $u = e^{-t}x^3(1-x)^3$
- **Constants:** `alpha = 1.8`
- **Network:** FNN [2, 20, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 10,000; 400 domain, 2 boundary, 2 initial points
- **In PINNStudio:** Examples → **Forward** → **Fractional diffusion 1D**

**Result (RTX 4090):** $L_2$ = 1.0 × 10⁻⁷ ($t = 0$), 1.4 × 10⁻³ ($t = 0.25$), 5.8 × 10⁻³ ($t = 0.5$), 2.4 × 10⁻³ ($t = 0.75$), 3.3 × 10⁻³ ($t = 1$)

*u — PINN solution over time*

![Fractional diffusion 1D — PINN solution over time (u)](assets/Images/DeepXDE/Fractional_diffusion_equation/animation.gif)

*PINN vs reference, error analysis*

![Fractional diffusion 1D — PINN vs reference, error analysis](assets/Images/DeepXDE/Fractional_diffusion_equation/surface_comparison.png)

</details>

<details id="dx-heat-equation">
<summary><strong>Heat 1D – Dirichlet</strong></summary>

DeepXDE example: [`heat.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/heat.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/heat.html))

$$\Large \frac{\partial u}{\partial t} = 0.4\frac{\partial^2 u}{\partial x^2}, \qquad x \in [0, 1],\ t \in [0, 1]$$

- **Initial condition:** $u(x, 0) = \sin(\pi x)$; **boundary conditions:** $u(0, t) = u(1, t) = 0$
- **Exact solution:** $u = e^{-0.4\pi^2 t}\sin(\pi x)$
- **Constants:** `a = 0.4`, `L = 1`, `n = 1`
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 20,000 → L-BFGS 15,000; 2,540 domain, 80 boundary, 160 initial points
- **In PINNStudio:** Examples → **Forward** (or **Inverse**) → **Heat 1D – Dirichlet**

The solution decays to about 2% of its initial size by $t = 1$, so the relative error grows over time even though the absolute error stays small.

**Result (RTX 4090):** $L_2$ = 4.2 × 10⁻⁴ ($t = 0$), 9.1 × 10⁻⁴ ($t = 0.25$), 2.2 × 10⁻³ ($t = 0.5$), 9.5 × 10⁻³ ($t = 0.75$), 5.0 × 10⁻² ($t = 1$)

*u — PINN solution over time*

![Heat 1D – Dirichlet — PINN solution over time (u)](assets/Images/DeepXDE/Heat_equation/animation.gif)

*PINN vs reference, error analysis*

![Heat 1D – Dirichlet — PINN vs reference, error analysis](assets/Images/DeepXDE/Heat_equation/surface_comparison.png)

*Inverse mode* — pick the example from the **Inverse** list: the diffusivity $a$ is unknown (initial guess 1, true value 0.4) and is learned together with $u$ from $u$ measured at $t = 1$ (the exact solution, [`reference_data/1D/heat/t_1.0.txt`](reference_data/1D/heat/t_1.0.txt)):

$$\Large \frac{\partial u}{\partial t} = a\ \frac{\partial^2 u}{\partial x^2}$$

**Inverse result (RTX 4090):** $a$ = 0.3984 (true 0.4); $L_2$ = 1.0 × 10⁻³ ($t = 0$), 3.2 × 10⁻³ ($t = 0.25$), 1.2 × 10⁻² ($t = 0.5$), 1.5 × 10⁻² ($t = 0.75$), 2.7 × 10⁻³ ($t = 1$)

*Inverse mode — inferred parameter during training*

![Heat 1D – Dirichlet inverse mode — inferred parameter during training](assets/Images/DeepXDE/Heat_equation/inverse_param_convergence_animation.gif)

</details>

<details id="dx-heat-equation-with-resampling">
<summary><strong>Heat 1D – resampling</strong></summary>

DeepXDE example: [`heat_resample.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/heat_resample.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/heat.resample.html))

$$\Large \frac{\partial u}{\partial t} = 0.4\frac{\partial^2 u}{\partial x^2}, \qquad x \in [0, 1],\ t \in [0, 1]$$

- **Initial / boundary conditions:** $u(x, 0) = \sin(\pi x)$, $u(0, t) = u(1, t) = 0$
- **Point resampling:** the collocation points are redrawn every 10 iterations (DeepXDE's `PDEPointResampler`)
- **Exact solution:** $u = e^{-0.4\pi^2 t}\sin(\pi x)$
- **Constants:** `a = 0.4`, `L = 1`, `n = 1`
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 200,000 → L-BFGS 15,000; 2,540 domain, 80 boundary, 160 initial points
- **In PINNStudio:** Examples → **Forward** → **Heat 1D – resampling**

**Result (RTX 4090):** $L_2$ = 1.6 × 10⁻⁴ ($t = 0$), 4.6 × 10⁻⁴ ($t = 0.25$), 5.8 × 10⁻⁴ ($t = 0.5$), 4.1 × 10⁻³ ($t = 0.75$), 1.4 × 10⁻² ($t = 1$)

*u — PINN solution over time*

![Heat 1D – resampling — PINN solution over time (u)](assets/Images/DeepXDE/Heat_equation_with_resampling/animation.gif)

*PINN vs reference, error analysis*

![Heat 1D – resampling — PINN vs reference, error analysis](assets/Images/DeepXDE/Heat_equation_with_resampling/surface_comparison.png)

</details>

<details id="dx-klein-gordon-equation">
<summary><strong>Klein-Gordon 1D</strong></summary>

DeepXDE example: [`Klein_Gordon.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Klein_Gordon.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/klein.gordon.html))

$$\Large \frac{\partial^2 u}{\partial t^2} - \frac{\partial^2 u}{\partial x^2} + u^2 = -x\cos t + x^2\cos^2 t, \qquad x \in [-1, 1],\ t \in [0, 10]$$

- **Initial conditions:** $u(x, 0) = x$ and $\partial u/\partial t\ (x, 0) = 0$ (the second as an Operator BC applied at the initial time)
- **Boundary condition:** $u = x\cos t$
- **Training:** Adam with inverse-time decay ($10^{-3}$, steps 3000, rate 0.9), then L-BFGS
- **Exact solution:** $u = x\cos t$
- **Constants:** `alpha = -1`, `beta = 0`, `gamma = 1`, `k = 2`
- **Network:** FNN [2, 40, 40, 1], tanh, Glorot uniform
- **Training:** Adam 20,000 → L-BFGS 15,000; 30,000 domain, 1,500 boundary, 1,500 initial points
- **In PINNStudio:** Examples → **Forward** → **Klein-Gordon 1D**

**Result (RTX 4090):** $L_2$ = 1.4 × 10⁻³ ($t = 0$), 1.6 × 10⁻² ($t = 2.5$), 8.5 × 10⁻² ($t = 5$), 6.5 × 10⁻² ($t = 7.5$), 8.1 × 10⁻² ($t = 10$)

*u — PINN solution over time*

![Klein-Gordon 1D — PINN solution over time (u)](assets/Images/DeepXDE/Klein_Gordon_equation/animation.gif)

*PINN vs reference, error analysis*

![Klein-Gordon 1D — PINN vs reference, error analysis](assets/Images/DeepXDE/Klein_Gordon_equation/surface_comparison.png)

</details>

<details id="dx-schr-dinger-equation">
<summary><strong>Schrödinger 1D</strong></summary>

DeepXDE example: [`Schrodinger.ipynb`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Schrodinger.ipynb)

$$\Large i\frac{\partial h}{\partial t} + \frac{1}{2}\frac{\partial^2 h}{\partial x^2} + |h|^2 h = 0, \qquad x \in [-5, 5],\ t \in [0, \pi/2]$$

$$\Large \frac{\partial u}{\partial t} + 0.5\frac{\partial^2 v}{\partial x^2} + (u^2 + v^2)\ v = 0$$

$$\Large \frac{\partial v}{\partial t} - 0.5\frac{\partial^2 u}{\partial x^2} - (u^2 + v^2)\ u = 0$$

- **Solved as:** two real outputs, $h = u + iv$: the second and third equations above are the real and imaginary parts, entered in PINNStudio as PDE 1 (`du_t + 0.5*dv_xx + (u**2 + v**2)*v`) and PDE 2 (`dv_t - 0.5*du_xx - (u**2 + v**2)*u`)
- **Initial condition:** $h(x, 0) = 2\ \mathrm{sech}(x)$; **boundary conditions:** periodic in $u$, $v$ and their $x$-derivatives
- **Compared:** $|h| = \sqrt{u^2 + v^2}$ against a Fourier pseudo-spectral (split-step) solution in [`reference_data/1D/schrodinger`](reference_data/1D/schrodinger), made by [`tools/make_exact_reference_data.py`](tools/make_exact_reference_data.py)
- **Network:** FNN [2, 100, 100, 100, 100, 2], tanh, Glorot normal
- **Training:** Adam 10,000 → L-BFGS 10,000; 10,000 domain, 20 boundary, 200 initial points
- **In PINNStudio:** Examples → **Forward** (or **Inverse**) → **Schrödinger 1D**

**Result (RTX 4090):** $L_2$ of $|h|$ = 1.5 × 10⁻³ ($t = 0$), 1.1 × 10⁻³ ($t = 0.25$), 1.1 × 10⁻³ ($t = 0.5$), 1.4 × 10⁻³ ($t = 0.75$), 1.4 × 10⁻³ ($t = 1$), 1.1 × 10⁻³ ($t = 1.25$), 1.7 × 10⁻³ ($t = 1.5$)

*|h| — PINN solution over time*

![Schrödinger 1D — PINN solution over time (|h|)](assets/Images/DeepXDE/Schr_dinger_equation/animation.gif)

*|h| — PINN vs reference, error analysis*

![Schrödinger 1D — PINN vs reference, error analysis (|h|)](assets/Images/DeepXDE/Schr_dinger_equation/surface_comparison.png)

*Inverse mode* — pick the example from the **Inverse** list: the coefficient $c$ of the second-derivative terms (0.5 above; initial guess 1) is unknown and is learned from $|h| = \sqrt{u^2 + v^2}$ measured at $t = 0.75$, with the same training as above:

$$\Large \frac{\partial u}{\partial t} + c\frac{\partial^2 v}{\partial x^2} + (u^2 + v^2) v = 0, \qquad \frac{\partial v}{\partial t} - c\frac{\partial^2 u}{\partial x^2} - (u^2 + v^2) u = 0$$

**Why $t = 0.75$.** Measured at $t = 1.5$ only, $|h|$ does not determine $c$: solving the equation with $c = 1.95$ gives an $|h|$ at $t = 1.5$ within 1% of the one for $c = 0.5$, and training from the guess $c = 1$ converges to 1.95, fitting the data at $t = 1.5$ while missing every other time by 27–60%. At $t = 0.75$ (or $0.5$) $|h|$ changes with $c$ in one direction only, and the true value is recovered.

**Inverse result (RTX 4090):** $c$ = 0.50017 (true 0.5); $L_2$ of $|h|$ = 1.3 × 10⁻³ ($t = 0$), 9.7 × 10⁻⁴ ($t = 0.25$), 1.4 × 10⁻³ ($t = 0.5$), 2.2 × 10⁻⁴ ($t = 0.75$), 8.4 × 10⁻⁴ ($t = 1$), 1.3 × 10⁻³ ($t = 1.25$), 1.5 × 10⁻³ ($t = 1.5$)

*Inverse mode — inferred parameter during training*

![Schrödinger 1D inverse mode — inferred parameter during training](assets/Images/DeepXDE/Schr_dinger_equation/inverse_param_convergence_animation.gif)

</details>

<details id="dx-wave-propagation-space-time-multi-scale-fourier-features">
<summary><strong>Wave 1D – space-time multi-scale Fourier features</strong></summary>

DeepXDE example: [`wave_1d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/wave_1d.py)

$$\Large \frac{\partial^2 u}{\partial t^2} = C^2\frac{\partial^2 u}{\partial x^2}, \qquad x \in [0, 1],\ t \in [0, 1],\ C = 10$$

- **Boundary conditions:** $u(0, t) = u(1, t) = 0$
- **Initial conditions:** $u(x, 0) = \sin(\pi x) + \sin(A\pi x)$ ($A = 2$); $\partial u/\partial t(x, 0) = 0$ as an Operator BC `du_t` applied at the initial time
- **Exact solution:** $u = \sin(\pi x)\cos(C\pi t) + \sin(A\pi x)\cos(AC\pi t)$ — ten and twenty oscillations in time
- **Network:** space-time multi-scale Fourier features (STMsFFN): space scale $\sigma_x = 1$, time scales $\sigma_t = 1, 10$; inputs rescaled to zero mean, unit variance by the input-transform formula `(x - 0.5)*2*sqrt(3); (t - 0.5)*2*sqrt(3)`
- **Loss weights:** set from the initial losses, $w_i = 5 / L_i(0)$ (*Scale by initial losses*); learning rate $10^{-3}/(1 + 0.9\ n/2000)$; collocation points redrawn every iteration
- **Constants:** `A = 2`, `C = 10`
- **Network:** STMsFFN [2, 100, 100, 100, 1], Fourier scales σ = 1, time scales 1, 10, tanh, Glorot uniform
- **Training:** Adam 10,000; 360 domain, 360 boundary, 360 initial points
- **In PINNStudio:** Examples → **Forward** → **Wave 1D – space-time multi-scale Fourier features**

Collocation points are redrawn every iteration from a pseudo-random distribution. DeepXDE's script keeps the default Hammersley distribution, which is deterministic, so its resampler redraws the same 360 points: run that way, the network fits them (training loss 4 × 10⁻⁵) but not the wave in between (test loss near 1, $L_2$ ≈ 1 for t > 0). This is a hard problem in 10,000 iterations — the error grows with t; longer training improves it.

**Result (RTX 4090):** $L_2$ = 7.7 × 10⁻⁴ ($t = 0$), 4.5 × 10⁻² ($t = 0.25$), 9.8 × 10⁻² ($t = 0.5$), 1.0 × 10⁻¹ ($t = 0.75$), 1.4 × 10⁻¹ ($t = 1$)

*u — PINN solution over time*

![Wave 1D – space-time multi-scale Fourier features — PINN solution over time (u)](assets/Images/DeepXDE/Wave_propagation_space_time_multi_scale_Fourier_features/animation.gif)

*PINN vs reference, error analysis*

![Wave 1D – space-time multi-scale Fourier features — PINN vs reference, error analysis](assets/Images/DeepXDE/Wave_propagation_space_time_multi_scale_Fourier_features/surface_comparison.png)

</details>

<details id="dx-inverse-diffusion-equation">
<summary><strong>Diffusion 1D – unknown coefficient</strong></summary>

DeepXDE example: [`diffusion_1d_inverse.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/diffusion_1d_inverse.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse/diffusion.1d.inverse.html))

$$\Large \frac{\partial u}{\partial t} = C\frac{\partial^2 u}{\partial x^2} - e^{-t}\left(\sin(\pi x) - \pi^2\sin(\pi x)\right), \qquad x \in [-1, 1],\ t \in [0, 1]$$

- **Unknown:** $C$ (true value 1, initial guess 2)
- **Data:** 10 measurements of $u$ at $t = 1$, plus the initial and boundary conditions
- **Exact solution:** $u = e^{-t}\sin(\pi x)$
- **Network:** FNN [2, 32, 32, 32, 1], tanh, Glorot uniform
- **Training:** Adam 50,000; 40 domain, 20 boundary, 10 initial points
- **In PINNStudio:** Examples → **Inverse** → **Diffusion 1D – unknown coefficient**

**Result (RTX 4090):** $C$ = 0.9988 (true 1); $L_2$ = 1.2 × 10⁻³ ($t = 0$), 1.8 × 10⁻³ ($t = 0.25$), 1.9 × 10⁻³ ($t = 0.5$), 2.8 × 10⁻³ ($t = 0.75$), 3.1 × 10⁻³ ($t = 1$)

*u — PINN solution over time*

![Diffusion 1D – unknown coefficient — PINN solution over time (u)](assets/Images/DeepXDE/Inverse_diffusion_equation/animation.gif)

*PINN vs reference, error analysis*

![Diffusion 1D – unknown coefficient — PINN vs reference, error analysis](assets/Images/DeepXDE/Inverse_diffusion_equation/surface_comparison.png)

*Inferred parameters during training*

![Diffusion 1D – unknown coefficient — inferred parameters during training](assets/Images/DeepXDE/Inverse_diffusion_equation/param_plot.png)

</details>

<details id="dx-inverse-diffusion-reaction-system">
<summary><strong>Diffusion-reaction 1D – unknown k_f, D</strong></summary>

DeepXDE example: [`reaction_inverse.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_inverse/reaction_inverse.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse/reaction.inverse.html))

$$\Large \frac{\partial C_A}{\partial t} = D\frac{\partial^2 C_A}{\partial x^2} - k_f C_A C_B^2, \qquad \frac{\partial C_B}{\partial t} = D\frac{\partial^2 C_B}{\partial x^2} - 2k_f C_A C_B^2$$

- **Domain:** $x \in [0, 1]$, $t \in [0, 10]$; $C_A = C_B = e^{-20x}$ at $t = 0$, $C_A = C_B = 1 - x$ on the boundary
- **Unknowns:** $k_f$ (true 0.1) and $D$ (true $2\times 10^{-3}$, written as $10^{-3}D$ with $D = 2$)
- **Data:** $C_A$ and $C_B$ on a space-time grid, computed by `tools/make_deepxde_reference_data.py`
- **Network:** FNN [2, 20, 20, 20, 2], tanh, Glorot uniform
- **Training:** Adam 80,000; 2,000 domain, 100 boundary, 100 initial points
- **In PINNStudio:** Examples → **Inverse** → **Diffusion-reaction 1D – unknown k_f, D**

**Result (RTX 4090):** $k_f$ = 0.0992 (true 0.1), $D$ = 1.995 (true 2)

*ca — PINN solution over time*

![Diffusion-reaction 1D – unknown k_f, D — PINN solution over time (ca)](assets/Images/DeepXDE/Inverse_diffusion_reaction_system/animation.gif)

*ca — inferred parameters during training*

![Diffusion-reaction 1D – unknown k_f, D — inferred parameters during training (ca)](assets/Images/DeepXDE/Inverse_diffusion_reaction_system/param_plot.png)

</details>

### 2D examples

*Click an example to expand it.*

<details id="dx-fractional-poisson-equation-2d">
<summary><strong>Fractional Poisson 2D – disk</strong></summary>

DeepXDE example: [`fractional_Poisson_2d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/fractional_Poisson_2d.py)

$$\Large -(-\Delta)^{\alpha/2}u = 2^{\alpha}\Gamma(2 + \tfrac{\alpha}{2})\Gamma(1 + \tfrac{\alpha}{2})\left(1 - (1 + \tfrac{\alpha}{2})|x|^2\right), \qquad |x| < 1,\ \alpha = 1.8$$

- **Equation in the panel:** `frac(u)*gamma((1 - alpha)/2)*gamma((2 + alpha)/2)/(2*pi**1.5) - ...` — `frac(u)` times $C(\alpha, 2)$ is $-(-\Delta)^{\alpha/2}u$
- **Fractional settings:** 8 directions, 100 Grünwald-Letnikov points per unit length, dynamic mesh
- **Geometry:** unit disk; $u = 0$ on the circle through $\hat u = (1 - x^2 - y^2)N$
- **Exact solution:** $u = (1 - |x|^2)^{1 + \alpha/2}$
- **Constants:** `alpha = 1.8`
- **Network:** FNN [2, 20, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 20,000; 100 domain points
- **In PINNStudio:** Examples → **Forward** → **Fractional Poisson 2D – disk**

**Result (RTX 4090):** $L_2$ = 3.4 × 10⁻³ to 4.2 × 10⁻³ over repeated runs (the fractional operator's sums on the GPU are not bit-for-bit repeatable)

*PINN vs reference, error analysis*

![Fractional Poisson 2D – disk — PINN vs reference, error analysis](assets/Images/DeepXDE/Fractional_Poisson_equation_2D/surface_comparison.png)

</details>

<details id="dx-helmholtz-2d-dirichlet">
<summary><strong>Helmholtz 2D – Dirichlet</strong></summary>

DeepXDE example: [`Helmholtz_Dirichlet_2d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Dirichlet_2d.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/helmholtz.2d.dirichlet.html))

$$\Large -\nabla^2 u - k_0^2 u = k_0^2\sin(k_0 x)\sin(k_0 y), \qquad k_0 = 4\pi,\ (x, y) \in [0, 1]^2$$

- **Boundary conditions:** $u = 0$ on the boundary, imposed exactly by $\hat u = x(1-x)y(1-y)N$
- **Exact solution:** $u = \sin(k_0 x)\sin(k_0 y)$
- **Constants:** `n = 2`, `k0 = 2*pi*n`
- **Network:** FNN [2, 150, 150, 150, 1], sin, Glorot uniform
- **Training:** Adam 5,000; 400 domain, 80 boundary points
- **In PINNStudio:** Examples → **Forward** → **Helmholtz 2D – Dirichlet**

**Result (RTX 4090):** $L_2$ = 1.9 × 10⁻³

*PINN vs reference, error analysis*

![Helmholtz 2D – Dirichlet — PINN vs reference, error analysis](assets/Images/DeepXDE/Helmholtz_2D_Dirichlet/surface_comparison.png)

</details>

<details id="dx-helmholtz-2d-hyperparameter-optimization">
<summary><strong>Helmholtz 2D – hyperparameter search</strong></summary>

DeepXDE example: [`Helmholtz_Dirichlet_2d_HPO.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Dirichlet_2d_HPO.py)

$$\Large -\nabla^2 u - k_0^2 u = k_0^2\sin(k_0 x)\sin(k_0 y), \qquad k_0 = 4\pi,\ (x, y) \in [0, 1]^2$$

- **Same problem** as Helmholtz 2D (Dirichlet), with $\hat u = x(1-x)y(1-y)N$
- **Parameter Sweep, mode Bayesian search:** learning rate $10^{-4}$–$5\times10^{-2}$ (log), hidden layers 1–10, neurons per layer 5–500, activation sin / sigmoid / tanh
- **Budget:** 50 runs of 10,000 Adam iterations each — the baseline (lr $10^{-3}$, 4 × 50, sin), 10 random runs, then 39 chosen by the Gaussian-process model, minimizing the final loss
- **Output:** one folder per run, `bayes_search.csv` and `bayes_convergence.png`; the best run is printed at the end of the Training Log
- **Constants:** `n = 2`, `k0 = 2*pi*n`
- **Network:** FNN [2, 50, 50, 50, 50, 1], sin, Glorot uniform
- **Training:** Adam 10,000; 400 domain, 80 boundary points
- **In PINNStudio:** Examples → **Forward** → **Helmholtz 2D – hyperparameter search**

**Result (RTX 4090):** the baseline (lr $10^{-3}$, 4 × 50, sin) ends at final loss 5.7 ($L_2$ = 3.3 × 10⁻¹); the best of the 50 runs — lr $1.5\times10^{-3}$, 3 hidden layers of 87, sin — reaches final loss 0.020 and **$L_2$ = 1.3 × 10⁻³** (about 40 minutes for all 50 runs)

*PINN vs reference, error analysis*

![Helmholtz 2D – hyperparameter search — PINN vs reference, error analysis](assets/Images/DeepXDE/Helmholtz_2D_hyperparameter_optimization/surface_comparison.png)

*Bayesian search: final loss of every run and the best so far*

![Helmholtz 2D – hyperparameter search — Bayesian search: final loss of every run and the best so far](assets/Images/DeepXDE/Helmholtz_2D_hyperparameter_optimization/bayes_convergence.png)

</details>

<details id="dx-helmholtz-sound-hard-scattering-absorbing-bc">
<summary><strong>Helmholtz 2D – sound-hard scattering</strong></summary>

DeepXDE example: [`Helmholtz_Sound_hard_ABC_2d.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Sound_hard_ABC_2d.py)

$$\Large -\nabla^2 u - k_0^2 u = 0, \qquad u = u_{re} + i\ u_{im},\ k_0 = 2$$

- **Geometry:** Custom — the square $[-\pi, \pi]^2$ minus a disk of radius $R = \pi/4$
- **Scattered field** of the plane wave $e^{ik_0x}$ off a sound-hard disk: two outputs `u_re`, `u_im`, one equation each
- **On the disk** (Neumann): $\partial u/\partial n = -\partial e^{ik_0x}/\partial n$, i.e. `-k0*x*sin(k0*x)/R` and `k0*x*cos(k0*x)/R`
- **On the outer square** (absorbing, Robin): $\partial u/\partial n = ik_0u$, i.e. `-k0*u_im` on the `u_re` row and `k0*u_re` on the `u_im` row
- **Reference:** the Bessel/Hankel series solution of DeepXDE's script
- **Constants:** `k0 = 2`, `R = pi/4`
- **Network:** FNN [2, 350, 350, 350, 2], tanh, Glorot uniform
- **Training:** Adam 10,000; 1,600 domain, 320 boundary points
- **In PINNStudio:** Examples → **Forward** → **Helmholtz 2D – sound-hard scattering**

**Result (RTX 4090):** $L_2$ = 7.8 × 10⁻² ($u_{re}$), 6.7 × 10⁻² ($u_{im}$) — DeepXDE's own script, run unchanged on the same GPU, ends at 9.1 × 10⁻² (best 7.1 × 10⁻²)

*u_re — PINN vs reference, error analysis*

![Helmholtz 2D – sound-hard scattering — PINN vs reference, error analysis (u_re)](assets/Images/DeepXDE/Helmholtz_sound_hard_scattering_absorbing_BC/surface_comparison_u_re.png)

*u_im — PINN vs reference, error analysis*

![Helmholtz 2D – sound-hard scattering — PINN vs reference, error analysis (u_im)](assets/Images/DeepXDE/Helmholtz_sound_hard_scattering_absorbing_BC/surface_comparison_u_im.png)

</details>

<details id="dx-helmholtz-2d-with-a-hole">
<summary><strong>Helmholtz 2D – square with hole</strong></summary>

DeepXDE example: [`Helmholtz_Neumann_2d_hole.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Helmholtz_Neumann_2d_hole.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/helmholtz.2d.neumann.hole.html))

$$\Large -\nabla^2 u - k_0^2 u = k_0^2\sin(k_0 x)\sin(k_0 y), \qquad k_0 = 2\pi$$

- **Geometry:** Custom — the square $[-0.5, 0.5]^2$ minus a disk of radius 0.25
- **Boundary conditions:** Dirichlet (exact solution) on the outer square; Neumann (exact normal derivative) on the hole
- **Exact solution:** $u = \sin(k_0 x)\sin(k_0 y)$
- **Constants:** `n = 1`, `k0 = 2*pi*n`, `R = 1/4`
- **Network:** FNN [2, 350, 350, 350, 1], sin, Glorot uniform
- **Training:** Adam 5,000; 225 domain, 240 boundary points
- **In PINNStudio:** Examples → **Forward** → **Helmholtz 2D – square with hole**

**Result (RTX 4090):** $L_2$ = 4.6 × 10⁻²

*PINN vs reference, error analysis*

![Helmholtz 2D – square with hole — PINN vs reference, error analysis](assets/Images/DeepXDE/Helmholtz_2D_with_a_hole/surface_comparison.png)

</details>

<details id="dx-laplace-equation-on-a-disk">
<summary><strong>Laplace 2D – disk</strong></summary>

DeepXDE example: [`Laplace_disk.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/Laplace_disk.py) ([documentation](https://deepxde.readthedocs.io/en/latest/demos/pinn_forward/laplace.disk.html))

$$\Large r\frac{\partial u}{\partial r} + r^2\frac{\partial^2 u}{\partial r^2} + \frac{\partial^2 u}{\partial \theta^2} = 0, \qquad r \in [0, 1],\ \theta \in [0, 2\pi]$$

- **Boundary condition:** $u(1, \theta) = \cos\theta$
- **Input features:** $(r\sin\theta,\ r\cos\theta)$ through an input-transform formula, which makes the solution periodic in $\theta$
- **Exact solution:** $u = r\cos\theta$
- **In PINNStudio:** $x$ plays $r$ and $y$ plays $\theta$, so the plots show the $(r, \theta)$ rectangle
- **Network:** FNN [2, 20, 20, 20, 1], tanh, Glorot normal
- **Training:** Adam 15,000; 2,540 domain, 80 boundary points
- **In PINNStudio:** Examples → **Forward** → **Laplace 2D – disk**

**Result (RTX 4090):** $L_2$ = 1.1 × 10⁻³

*PINN vs reference, error analysis*

![Laplace 2D – disk — PINN vs reference, error analysis](assets/Images/DeepXDE/Laplace_equation_on_a_disk/surface_comparison.png)

</details>

<details id="dx-linear-elastostatic-plate">
<summary><strong>Linear elasticity 2D – plate</strong></summary>

DeepXDE example: [`elasticity_plate.py`](https://github.com/lululxvi/deepxde/blob/master/examples/pinn_forward/elasticity_plate.py) ([documentation](