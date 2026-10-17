# cosmo_learn

`cosmo-learn` is a Python package for learning cosmology using a combination of statistical inference and machine learning methods applied to real and simulated cosmological observables. It supports mock data generation, model training, reconstruction, and comparison across five observational probes — all through a single unified class, `CosmoLearn`.

See the tutorial notebook [`cosmo_tutorial.ipynb`](https://github.com/reggiebernardo/cosmo_learn/blob/main/cosmo_tutorial.ipynb) or the script [`minimal_example.py`](https://github.com/reggiebernardo/cosmo_learn/blob/main/minimal_example.py) for basic usage, and [arXiv:2508.20971 [astro-ph.CO]](https://arxiv.org/abs/2508.20971) for full details.

Please cite the paper below when using `cosmo-learn`.

Tested on Linux, Mac and Windows WSL <br />
Requires: `python 3.10` <br />
Recommended installation (conda): `conda env create -f cosmo_learn.yml` <br />
Quick install: `pip install cosmo-learn`

---

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Class: CosmoLearn](#core-class-cosmolearn)
  - [Initialization](#initialization)
  - [Mock Data Generation](#mock-data-generation)
  - [Learning Methods](#learning-methods)
  - [Visualization](#visualization)
  - [Metrics and Scoring](#metrics-and-scoring)
- [Module Reference](#module-reference)
- [Upcoming](#upcoming)
- [How to cite](#how-to-cite)

---

## Overview

`cosmo-learn` provides tools to:

- **Generate mock cosmological datasets** based on a flat $w$CDM input cosmology, with realistic noise drawn from real observational uncertainties.
- **Train machine learning models** (Gaussian Processes, Bayesian Ridge Regression, Artificial Neural Networks) to reconstruct cosmological observables as functions of redshift — without assuming a cosmological model.
- **Run statistical inference** (MCMC, Genetic Algorithm + Fisher matrix) to constrain flat $w$CDM parameters.
- **Visualize** mock data, reconstructions, residuals, posterior samples, and training diagnostics.
- **Evaluate and compare** methods using a suite of quantitative metrics.

### Supported observational probes

| Key | Observable | Data source |
|-----|-----------|-------------|
| `'CosmicChronometers'` | $H(z)$ | [Hdz_2020_CConly](https://raw.githubusercontent.com/reggiebernardo/datasets/main/Hdz_2020_CConly.txt) |
| `'SuperNovae'` | $\mu(z)$ (distance modulus) | [Pantheon+SH0ES](https://github.com/PantheonPlusSH0ES/DataRelease) |
| `'BaryonAcousticOscillations'` | $D_V/r_d(z)$ | DESI DR1 (arXiv:2404.03002, default) or DESI DR2 (arXiv:2503.14738, opt-in) |
| `'RedshiftSpaceDistorsions'` | $f\sigma_8(z)$ | [Growth_tableII](https://raw.githubusercontent.com/reggiebernardo/datasets/refs/heads/main/Growth_tableII.txt) |
| `'BrightSirens'` | $d_L(z)$ | LISA bright siren simulations |

### Supported methods

| Method | Description |
|--------|-------------|
| `MCMC` | Markov Chain Monte Carlo via `emcee` |
| `GAFisher` | Genetic Algorithm best-fit + Fisher matrix covariance |
| `GP` | Gaussian Process Regression (`scikit-learn`) |
| `BRR` | Bayesian Ridge Regression with polynomial features |
| `ANN` | Artificial Neural Network via `refann` (PyTorch backend) |
| `GATO` | Genetic Algorithm reconstruction via grammatical evolution (`my_gato`) |

---

## Installation

**Recommended (conda environment):**

```bash
conda env create -f cosmo_learn.yml
conda activate cosmo-learn
```

**Quick install via pip:**

```bash
conda create -n my_env_name python=3.10
pip install cosmo-learn
```

**Test the installation:**

```bash
python minimal_example.py
```

**Run the test suite** (requires a cloned copy of the repository):

```bash
pytest
```

This runs a suite of headless smoke tests covering mock data generation, GP, BRR, ANN training, MCMC, and GA-Fisher sampling. All tests should pass within a few minutes on a standard laptop.

---

## Quick Start

```python
from cosmo_learn.cosmo_learn import CosmoLearn

# 1. Define input cosmology: [H0, Om0, w0, s8]
# (DESI Year 1 flat wCDM best-fit + Planck s8)
H0, Om0, w0, s8 = 67.74, 0.3095, -0.997, 0.834
cl = CosmoLearn([H0, Om0, w0, s8], seed=14000605)

# 2. Generate mock data for all probes
mock_keys = ['CosmicChronometers', 'SuperNovae', 'BaryonAcousticOscillations',
             'BrightSirens', 'RedshiftSpaceDistorsions']
cl.make_mock(mock_keys=mock_keys)

# 3. Train ML models
cl.train_gp()
cl.train_brr()
cl.init_ann()
cl.train_ann()

# 4. Run MCMC
prior_dict = {'H0_min': 0, 'H0_max': 100, 'Om0_min': 0, 'Om0_max': 1,
              'w0_min': -10, 'w0_max': 10, 's8_min': 0.2, 's8_max': 1.5}
rd_fid_prior = {'mu': 147.46, 'sigma': 0.28}
llprob = lambda x: cl.llprob_wcdm(x, prior_dict=prior_dict, rd_fid_prior=rd_fid_prior)
cl.get_mcmc_samples(nwalkers=15, dres=[0.05, 0.005, 0.01, 0.01, 0.005],
                    llprob=llprob, p0=[70, 0.3, -1, 0.8, 147], nburn=100, nmcmc=2000)

# 5. Visualize
import matplotlib.pyplot as plt

fig, ax = cl.show_mocks(show_input=True)
cl.show_trained_ml(ax=ax, method='GP', label='GP')
cl.show_trained_ml(ax=ax, method='BRR', color='blue', alpha=0.15, hatch='|', label='BRR')
fig.tight_layout()
plt.show()
```

---

## Core Class: CosmoLearn

```python
from cosmo_learn.cosmo_learn import CosmoLearn
```

### Initialization

```python
cl = CosmoLearn(params, de_model='no pert', rd_fid=147.46, Tcmb0=2.725, seed=None)
```

| Argument | Type | Description |
|----------|------|-------------|
| `params` | `list` | Input cosmology `[H0, Om0, w0, s8]` |
| `de_model` | `str` | Dark energy perturbation model: `'no pert'` (default), `'static'`, or `'dynamic'` |
| `rd_fid` | `float` | Fiducial sound horizon $r_d$ in Mpc (default: `147.46`) |
| `Tcmb0` | `float` | CMB temperature in K (default: `2.725`) |
| `seed` | `int` | Random seed for reproducibility |

---

### Mock Data Generation

All mock data generation methods draw Gaussian noise around the true cosmological curve evaluated at the real survey redshifts, using the real observational uncertainties.

Data is automatically split into **training** (90%) and **test** (10%) sets, accessible via `cl.mock_data[key]['train']` and `cl.mock_data[key]['test']`, each with sub-keys `'x'`, `'y'`, `'yerr'`.

#### `make_mock(mock_keys, pop_model='Pop III', years=5)`

Generate mock data for multiple probes at once.

```python
cl.make_mock(mock_keys=['CosmicChronometers', 'SuperNovae', 'BaryonAcousticOscillations',
                        'BrightSirens', 'RedshiftSpaceDistorsions'])
```

| Argument | Description |
|----------|-------------|
| `mock_keys` | List of probe keys (see table in Overview) |
| `pop_model` | LISA population model for bright sirens: `'Pop III'`, `'Delay'`, or `'No Delay'` |
| `years` | Duration of LISA observations in years (for bright sirens) |
| `bao_release` | DESI BAO release for the BAO probe: `'DR1'` (default) or `'DR2'` |

Individual generation methods are also available: `make_cosmic_chronometers_like()`, `make_pantheon_plus_like()`, `make_desi1_like(bao_release='DR1')`, `make_rsd_like()`, `make_bright_sirens_mock(years, pop_model)`.

---

### Learning Methods

#### Gaussian Process (`GP`)

```python
cl.train_gp(kernel_key='RBF', n_restarts_optimizer=10)
```

Trains one GP per probe. Available kernels (`kernel_key`): `'RBF'`, `'Matern'`, `'RationalQuadratic'`, `'ExpSineSquared'`, `'DotProduct'`. The default `'RBF'` uses a `ConstantKernel * RBF + WhiteKernel` combination.

#### Bayesian Ridge Regression (`BRR`)

```python
cl.train_brr(n_order=3)
```

Fits a polynomial of degree `n_order` with Bayesian regularization per probe.

#### Artificial Neural Network (`ANN`)

```python
cl.init_ann(mid_node=4096, hidden_layer=1, hp_model='rec_1',
            loss_func='L1', iteration=30000)
cl.train_ann()
```

Uses the `refann` (PyTorch) backend. `init_ann` configures the architecture; `train_ann` runs training and prints elapsed time per probe.

#### Genetic Algorithm reconstruction (`GATO`)

```python
cl.train_gato(grammar=['poly', 'cpl'], Nchains=10, Ngens=100, Npops=100)
```

Reconstructs each probe with GATO (`my_gato.GATO`), a genetic algorithm based on grammatical
evolution that fits a symbolic function to data points with error bars. The default grammar
`['poly', 'cpl']` combines polynomial and CPL-like basis functions. Results are stored in
`cl.GATO_dict[key]` and can be overlaid via `cl.show_trained_ml(method='GATO')`. See
[`cosmo_tutorial_other_methods.ipynb`](https://github.com/reggiebernardo/cosmo_learn/blob/main/cosmo_tutorial_other_methods.ipynb)
for a worked example. Requires `sympy`.

#### MCMC

```python
llprob = lambda x: cl.llprob_wcdm(x, prior_dict=prior_dict, rd_fid_prior=rd_fid_prior)
cl.get_mcmc_samples(nwalkers, dres, llprob, p0, nburn=100, nmcmc=500)
```

Runs `emcee` ensemble sampler. The log-posterior `llprob_wcdm` uses flat priors on `[H0, Om0, w0, s8]` and a Gaussian prior on $r_d$. The initial position is refined with a Nelder-Mead optimizer before sampling. Samples are stored in `cl.mcmc_samples`.

| `prior_dict` key | Description |
|------------------|-------------|
| `H0_min/max` | Flat prior bounds on $H_0$ |
| `Om0_min/max` | Flat prior bounds on $\Omega_{m0}$ |
| `w0_min/max` | Flat prior bounds on $w_0$ |
| `s8_min/max` | Flat prior bounds on $S_8$ |

`rd_fid_prior`: `{'mu': 147.46, 'sigma': 0.28}` — Gaussian prior on the sound horizon.

#### Genetic Algorithm + Fisher (`GA-Fisher`)

```python
fitness_func = lambda x: -2 * llprob(x)
cl.get_gaFisher_samples(fitness_func, prior_ga, llprob=llprob, nsamples=10000)
```

Finds the best-fit with a genetic algorithm, then approximates the posterior as a multivariate Gaussian using the Fisher (Hessian) information matrix. Samples are stored in `cl.gaFisher_samples`.

---

### Visualization

#### Mock data plots

```python
fig, ax = cl.show_mocks(show_input=True)
fig, ax = cl.show_mocks_and_residuals(show_input=True)
```

#### ML reconstruction overlay

```python
cl.show_trained_ml(ax=ax, method='GP', label='GP')
cl.show_trained_ml(ax=ax, method='BRR', color='blue', alpha=0.15, hatch='|', label='BRR')
cl.show_trained_ml(ax=ax, method='ANN', color='darkgreen', alpha=0.15, hatch='x', label='ANN')
```

#### Parametric reconstruction overlay

```python
cl.show_bestfit_curve(ax=ax, method='MCMC', label='MCMC', color='pink')
cl.show_bestfit_curve(ax=ax, method='GAFisher', color='orange', alpha=0.15, label='GA-Fisher')
```

#### Posterior corner plots

```python
fig_corner = cl.show_param_posterior(method='MCMC')
cl.show_param_posterior(method='GAFisher', fig=fig_corner, color='blue', show_truth=True)
```

#### ANN training loss

```python
fig, ax = cl.show_ann_loss()
```

---

### Metrics and Scoring

**`metrics.py`** provides functions to quantitatively compare reconstructed observables against test data:

| Function | Description |
|----------|-------------|
| `D0(Qi, σi, Qj, σj)` | Normalized absolute deviation (target: ≈ 0.5) |
| `D1(Qi, σi, Qj, σj)` | Tension beyond quadrature (target: high) |
| `D2(Qi, σi, Qj, σj)` | Combined absolute + excess tension (target: ≈ 1) |
| `DWstat(residuals)` | Durbin-Watson statistic (target: ≈ 2, no serial correlation) |
| `Ch2_H0(H0, errH0, refH0)` | $\chi^2$-like $H_0$ tension metric |
| `get_metrics(bgData, ptData, ...)` | Combined D0/D1/D2/DW for CC + RSD jointly |

**`rec_olympics.py`** — `OlympicsMaster` class scores methods head-to-head across multiple metrics by awarding points to the best-performing method on each metric.

---

## Module Reference

| Module | Contents |
|--------|----------|
| `cosmo_learn/cosmo_learn.py` | `CosmoLearn` class, mock data, likelihoods, training, visualization |
| `cosmo_learn/metrics.py` | `D0`, `D1`, `D2`, `DWstat`, `Ch2_H0`, `get_metrics` |
| `cosmo_learn/rec_olympics.py` | `OlympicsMaster` scoring class |
| `cosmo_learn/my_gato.py` | `GATO` genetic-algorithm reconstruction (grammatical evolution) |
| `cosmo_learn/LISA_bright.py` | LISA bright siren mock data generator (`generate`) |

---

## Upcoming

- New data sets <br />
- New methods <br />
- New models

---

## How to cite

```latex
@article{Bernardo:2025pua,
    author = "Bernardo, Reginald Christian and Grand{\'o}n, Daniela and Levi Said, Jackson and C{\'a}rdenas, V{\'\i}ctor H. and Belinario, Gene Carlo and Reyes, Reinabelle",
    title = "{Cosmo-Learn: code for learning cosmology using different methods and mock data}",
    eprint = "2508.20971",
    archivePrefix = "arXiv",
    primaryClass = "astro-ph.CO",
    month = "8",
    year = "2025"
}
```
