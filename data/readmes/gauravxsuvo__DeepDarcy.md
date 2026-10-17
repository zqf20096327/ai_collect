# DeepDarcy

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21318191.svg)](https://doi.org/10.5281/zenodo.21318191)

A physics-informed neural network (PINN) that predicts groundwater
depletion and infers unreported pumping rates from sparse well data,
deployed as a full-stack web application.

## What this does

Groundwater levels are usually monitored at a small number of wells, and
actual pumping records are often incomplete or unreported. This project
trains a neural network that solves the governing groundwater flow
equation directly (via automatic differentiation, not a traditional
numerical solver) and, at the same time, learns the unknown net
depletion rate from the sparse well data it does have. This is the
inverse problem that makes the project a predictor rather than just a
PDE solver demo.

The model is trained and validated on real USGS well data from the
Ogallala aquifer near Garden City, Kansas, a well-documented groundwater
depletion region. Results are reported honestly, including a real
overfitting failure that was found and fixed during development, and the
model's current holdout error, rather than only showing the best-case
numbers.

Full technical details are in `docs/design-document.md` and
`docs/model-card.md`. The model card in particular documents intended
use, training data, metrics, and known limitations, and is worth reading
before treating any prediction as more than an order-of-magnitude
estimate.

## How it helps you

If you are learning or demonstrating physics-informed machine learning,
this project is a working, end to end example of:

- Implementing a PDE residual loss with PyTorch autograd, including the
  second-order derivatives a diffusion equation needs.
- Validating a PINN against a closed-form analytical solution before
  trusting it on real data.
- Solving an inverse problem: recovering an unknown physical parameter
  (a spatially varying depletion rate) from sparse noisy observations,
  instead of only solving the forward problem.
- Catching an overfitting failure mode that standard training-loss
  monitoring did not catch, using held-out spatial validation instead.
- Serving a trained scientific model through a REST API and a mapping
  frontend, with the model's own uncertainty and limitations surfaced in
  the product itself, not just in documentation.

If you are interested in groundwater depletion specifically, the
deployed model gives an illustrative, order-of-magnitude estimate of
depletion trends for a real, well studied aquifer region. It is a
research and portfolio artifact, not a calibrated water-management tool.
See the "Intended use" and "Limitations" sections of
`docs/model-card.md` for what it should and should not be used for.

## Project layout

```
ml-engine/   PyTorch PINN core: model, training, real-data pipeline
api/         FastAPI service that serves the trained model
web/         Next.js and Leaflet frontend
infra/       Deployment configuration (not yet applied)
docs/        Design document and model card
```

Each subproject has its own README with full setup and run instructions.

## Quick start

The fastest way to see the whole thing running locally is Docker
Compose, from the repository root:

```bash
docker compose up --build
```

This builds and runs both the API and the frontend together. Once it is
up:

- Frontend: http://localhost:3000
- API docs: http://localhost:8000/docs

To run each part individually during development, see
`ml-engine/README.md`, `api/README.md`, and `web/README.md`.

## Current results

- Forward solver validated against the analytical Theis solution: 0.91
  percent relative L2 error.
- Inverse recovery of an unknown pumping rate from synthetic noisy data:
  5.15 percent relative error.
- Real-data regional model (Ogallala aquifer, Kansas): 38.3 percent
  holdout relative L2 error on wells never seen during training, after
  replacing a uniform depletion-rate assumption with a spatially varying
  one. This is a moderate, not strong, fit, and the API and frontend
  both say so on every request.

Full details, including a documented overfitting failure and how it was
caught, are in `ml-engine/README.md` and `docs/model-card.md`.

## Paper

A full writeup of this project is published on Zenodo:

> Singh, G. R. (2026). *Physics-Informed Neural Networks for Groundwater
> Depletion Inference: A Case Study on the Ogallala Aquifer*. Zenodo.
> https://doi.org/10.5281/zenodo.21318191

The LaTeX source, a Markdown copy, and the figures used are also kept in
this repo under `research-docs/`.

## Status

Phases 1 through 3 (model, API, frontend) are complete. Phase 4
(integration: Docker Compose, CI, a model card, and deployment
configuration) is mostly complete but not yet deployed to a live URL.

## License

MIT. See `LICENSE`.
