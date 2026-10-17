# Off-grid Streetlight Dimming Control

[![Static repository checks](https://github.com/Galuyoo/offgrid-streetlight-dimming-control/actions/workflows/static-checks.yml/badge.svg)](https://github.com/Galuyoo/offgrid-streetlight-dimming-control/actions/workflows/static-checks.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-research%20code-orange)
![Reproducibility](https://img.shields.io/badge/reproducibility-paper%20pipeline-brightgreen)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.seta.2026.105315-blue)](https://doi.org/10.1016/j.seta.2026.105315)
![Dataset](https://img.shields.io/badge/dataset-NASA%20Battery-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/Galuyoo/offgrid-streetlight-dimming-control?color=brightgreen)
![GitHub repo size](https://img.shields.io/github/repo-size/Galuyoo/offgrid-streetlight-dimming-control?color=blueviolet)
![Jupyter Notebook](https://img.shields.io/badge/notebooks-Jupyter-orange)
![scikit--learn](https://img.shields.io/badge/ML-scikit--learn-blue)

This repository contains the reproducibility code and supporting research notebooks for the paper:

**Energy reliability and feasibility analysis for battery-constrained off-grid solar street lighting: an uncertainty-aware dimming control framework**

**Published in:** *Sustainable Energy Technologies and Assessments*, Volume 93 (2026), 105315  
**Authors:** Salaheddine Chouikh, Nouh Elmitwally, Faisal Saeed  
**DOI:** https://doi.org/10.1016/j.seta.2026.105315  
**Published online:** 12 August 2026

The repository provides the processed battery-cycle feature table, and a cleaned reproduction notebook for the main simulation pipeline. The code covers the core methodological components used in the paper:

- grouped battery-level train/test splitting
- Random Forest runtime forecasting
- residual-quantile uncertainty buffering
- phase-specific dimming policy simulation
- feasibility-bound estimation under brightness floors
- blackout rate, energy saving, and UM|BO severity metrics
- repeated-run confidence-interval analysis
- buffer ablation and severity-percentile sensitivity checks

The main entry point is:

`notebooks/03_reproduce_review_core_results.ipynb`

The cleaned notebooks in `notebooks/` are the recommended reproducibility entry points.

## Repository structure

- `notebooks/`  
  Cleaned public-facing notebooks:
  - `01_data_exploration_preprocessing.ipynb` - dataset checks and feature engineering
  - `02_model_screening.ipynb` - compact grouped model-screening analysis
  - `03_reproduce_review_core_results.ipynb` - main paper reproduction pipeline

- `data/raw/`  
  Place the downloaded NASA battery dataset here.

- `data/processed/`  
  Place or generate `engineered_metadata.csv` here.

- `outputs/tables/`  
  Generated CSV tables.

- `outputs/figures/`  
  Generated figures.

- `outputs/review_validation/`  
  Supplementary validation outputs.

- `configs/`  
  Reserved for paper configuration files.

## Dataset

The NASA battery dataset is not redistributed in this repository.

Download the dataset from the original source or Kaggle distribution:

- NASA Ames Prognostics Center of Excellence battery dataset
- Kaggle conversion: https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset

After preprocessing, the main pipeline expects:

`data/processed/engineered_metadata.csv`

See `data/README.md` for details.

## Installation

Create a Python environment and install the dependencies:

`pip install -r requirements.txt`

## Running the notebooks

The main paper reproduction entry point is:

`notebooks/03_reproduce_review_core_results.ipynb`

The two support notebooks provide preprocessing and model-screening context:

- `notebooks/01_data_exploration_preprocessing.ipynb`
- `notebooks/02_model_screening.ipynb`

The notebook expects:

`data/processed/engineered_metadata.csv`

and writes outputs under:

- `outputs/tables/`
- `outputs/figures/`
- `outputs/review_validation/`

## Notes on reproducibility

Small numerical differences may occur across environments due to package versions and stochastic model training. The notebook uses fixed split and model seeds for the reported repeated-run analyses where applicable.

## Runtime modes

The main notebook includes a `MODE` setting with several runtime options:

- `light`: quick smoke test using fewer split/model seeds and a small RF grid.
- `review_fast`: configuration used for the repeated-run analyses reported in the published paper.
- `medium`: includes optional CatBoost comparison with a moderate runtime.
- `heavy_lite`: larger RF repeated-run setting without CatBoost.
- `heavy`: extended validation setting with more split/model seeds and optional CatBoost.

For a quick check, use:

`MODE = "light"`

For published-paper repeated-run reproduction, use:

`MODE = "review_fast"`

## Citation

If you use this repository, methodology, or experiment configuration, please cite:

Chouikh, S., Elmitwally, N., & Saeed, F. (2026).  
Energy reliability and feasibility analysis for battery-constrained off-grid solar street lighting: an uncertainty-aware dimming control framework.  
*Sustainable Energy Technologies and Assessments, 93*, 105315.  
https://doi.org/10.1016/j.seta.2026.105315
