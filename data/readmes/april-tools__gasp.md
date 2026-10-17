# GASP!
[![Python package](https://github.com/april-tools/gasp/actions/workflows/python-package.yml/badge.svg)](https://github.com/april-tools/gasp/actions/workflows/python-package.yml)

This repository is the implementation of GASP!, the GPU Accelerated Simplical Integrator, as a stand-alone drop-in backend for wmi-pa.

GASP! is a high-performance WMI-integration backend that that can replace LATTE and can achieve one to two magnitude performance improvements, even more if many monomials must be integrated separately in parallel.

![gasp_vs_latte](imgs/scatter.png)

## Install

Install via git:

```python
pip install git+https://github.com/april-tools/gasp.git@master
```

## Usage

The main usage is via `NumericalSymbIntegratorPA`, which hooks into the `wmipa` API.

## Citation

```
@inproceedings{kurscheidt2025probabilistic,
  title={A Probabilistic Neuro-symbolic Layer for Algebraic Constraint Satisfaction},
  author={Kurscheidt, Leander and Morettin, Paolo and Sebastiani, Roberto and Passerini, Andrea and Vergari, Antonio},
  booktitle={Conference on Uncertainty in Artificial Intelligence},
  pages={2431--2471},
  year={2025},
  organization={PMLR}
}
```
