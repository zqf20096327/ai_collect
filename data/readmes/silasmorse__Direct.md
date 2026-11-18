# DIRECT

**Deep learning framework for accelerated MRI reconstruction.**

DIRECT covers the practical workflow around learned MRI reconstruction: dataset loading, model
configuration, training, evaluation and deployment. The Python package and the existing `docs/`
tree remain the reference for the full API.

## Install

```bash
pip install -e .
```

## Train

```bash
direct train --config projects/CMRxRecon/config.yaml
```

Experiment configurations live under `projects/`; the `direct` CLI is the entry point for training
and evaluation.

## Documentation

- `README.rst` - package and PyPI long description
- `docs/` - guides, tutorials and API notes
- `projects/` - reproduction configs for published experiments

## Scope

This repository is a maintained fork of the DIRECT MRI reconstruction project. The source keeps
the original training pipeline and configuration surface.
