# Forecasting Crude Oil Option Prices

This repository contains code, data files, figures, and experiment outputs related to the paper:

- **Title:** Forecasting crude oil option prices with dynamic factors using integrated machine learning models
- **Authors:** Kexin Yu, Xin-Jiang He, Xiaoyang Han, Xin Luo, and Sha Lin
- **Journal:** Communications in Nonlinear Science and Numerical Simulation
- **Volume / Article:** Vol. 147, Article 108879
- **Publication Date:** August 2025
- **DOI:** https://doi.org/10.1016/j.cnsns.2025.108879

## Project Overview

Crude oil options are important derivative instruments for hedging energy-market risk, but their prices are difficult to forecast because they are affected by nonlinear market dynamics, volatility changes, and multiple interacting financial factors. This project provides supporting materials for research on forecasting crude oil option prices with dynamic factors and integrated machine learning models.

The repository includes datasets, feature construction files, model scripts, prediction results, and visualization outputs. It is organized around experiments that compare traditional machine learning methods and deep learning models for option-price forecasting. The included implementations cover models such as SVR, BP neural networks, MLP, CNN, RNN, GRU, and LSTM, with both TensorFlow and PyTorch versions provided for part of the experiments.

A central idea of the related study is to combine dynamic market factors with machine learning models in order to improve forecasting performance for crude oil option prices. The code and data files in this repository support the empirical workflow, including data preprocessing, dimensionality-reduction or factor-related processing, model training, prediction generation, and result visualization.

## Repository Structure

```text
.
├── codes/                  # Main model and data-processing scripts
├── data/                   # Dataset files
├── fig/                    # Figures and visualization outputs
├── option_data/            # Option-related input and processed data
├── pytorch_version/        # PyTorch model implementation
├── tensorflow_version/     # TensorFlow model implementation
├── old_code/               # Earlier experiment scripts and archived outputs
├── Predict/                # Prediction result files
├── res/                    # Serialized result outputs
└── *.xlsx / *.py / *.ipynb # Additional datasets, scripts, and notebooks
```

## Methods

The repository includes forecasting experiments using traditional machine learning and deep learning approaches, including:

- Support Vector Regression (SVR)
- Back Propagation neural network (BP)
- Multilayer Perceptron (MLP)
- Convolutional Neural Network (CNN)
- Recurrent Neural Network (RNN)
- Gated Recurrent Unit (GRU)
- Long Short-Term Memory network (LSTM)

## Notes

The files are organized as supporting materials for the paper linked above. Please verify dataset licensing and publication permissions before making the repository public.
