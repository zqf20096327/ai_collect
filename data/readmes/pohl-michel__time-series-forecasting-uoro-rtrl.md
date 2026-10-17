# Multivariate respiratory-motion time-series forecasting using RNNs trained with UORO and RTRL

> **Note**: This repository contains the original code associated with my paper on unbiased online recurrent optimization (UORO) published in 2022 (see ["References"](#references) section). A newer consolidated implementation is available in the [`Time_series_forecasting folder`](https://github.com/pohl-michel/2D-MR-image-prediction/blob/main/Time_series_forecasting/README.md) of the `2D-MR-image-prediction` repository, which covers additional online learning algorithms for recurrent neural networks (RNNs), namely decoupled neural interfaces (DNI) and sparse one-step approximation (SnAp-1), transformer models, and more general evaluation settings.


## Overview

This repository contains MATLAB code for forecasting multivariate time-series data. Specifically, it implements vanilla RNNs trained online with UORO or real-time recurrent learning (RTRL), together with least mean squares (LMS) and ordinary least-squares linear autoregressive baselines. For RNNs and LMS, input signals are standardized using the training-set mean and standard deviation, and gradient clipping is applied to improve numerical stability.

The figure below shows an example of irregular respiratory-motion forecasting using UORO.

<p align="center"> <img src="prediction_UORO.png" width="70%" alt="External-marker respiratory-motion forecast using UORO"> </p>

<p align="center"> <em>Comparison of the ground-truth position of an external thoraco-abdominal marker moving due to breathing and its forecast using UORO. The horizon is set to 2.0 s and the sampling rate is 10 Hz. Prediction used the x-, y-, and z-coordinates of three markers as input, but only the z-coordinate of one marker, corresponding approximately to the spine axis, is displayed.</em> </p>


## Time-series data

The input time-series data are located in `1. Input time series sequences`. They consist of the 3D positions of three external markers placed on the chest and abdomen of healthy individuals lying supine during breathing. The sampling rate is 10 Hz, and sequence durations range from 73 s to 222 s.

The sequences processed by `prediction_main.m` and `hyperparameter_optimization_main.m` can be selected in `load_path_parameters.m` by commenting or uncommenting the corresponding entries in `path_par.time_series_dir_tab`.

**Data curation.** This repository also includes the script `convert_csv_to_mat.m`, which converts the original marker-position `.csv` files in `Original data` into MATLAB `.mat` files. The generated files are saved in `Original data` as `sequence_1.mat`, `sequence_2.mat`, etc.; these correspond to the `data.mat` files used in the input-sequence subfolders. These marker-position `.csv` files were provided by Krilavicius et al.; see the [References](#references) section.


## How to run the time-series forecasting code

**Inference with specified parameters.** Time-series forecasting with a specified algorithm, sequence, and set of parameters can be run by executing `prediction_main.m` in MATLAB from the repository root.

**Hyperparameter optimization.** Grid-search-based hyperparameter optimization can be run by executing `hyperparameter_optimization_main.m` in MATLAB from the repository root. For each horizon, the script selects hyperparameters on the validation set, reports test-set performance obtained with the selected hyperparameters, and records how validation performance changes when individual hyperparameter values are varied. 

**Expected outputs.** Prediction figures are saved in `2. Prediction results (figures)` and `3. Prediction results (images)`, while numerical performance logs are written to `5. Log txt files`. In addition, forecast values, loss values, and inference-time measurements are saved as `.mat` files in `4. RNN variables (temp)`. These folders are created automatically if they do not exist.

>**Note:** The forecasting algorithms can be applied to generic multivariate time series, but the implemented evaluation metrics assume that the signal represents the 3D coordinates of multiple tracked markers or objects. See Pohl et al., 2022 in the [References](#references) section for the metric definitions.

## Configuration parameters

Sequence-specific forecasting parameters, including the horizon, signal-history length, and method-specific settings, can be configured in the `pred_par.xlsx` file inside the subfolders of `1. Input time series sequences`. Each subfolder corresponds to one input time-series sequence.

Other parameters can be specified using files located at the repository root:

| File                         | Parameters                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| `disp_par.xlsx`              | Display and plotting parameters.                                                   |
| `load_pred_par.m`            | Method-specific forecasting settings, overriding the sequence-specific ones defined in `pred_par.xlsx`.                    |
| `load_hyperpar_cv_info.m`    | Hyperparameter grids and forecasting horizons used for grid search on the validation set. |
| `load_behavior_parameters.m` | Workflow flags for training, evaluation, saving, and GPU computation.              |
| `load_path_parameters.m`     | Input-sequence selection, path configuration, and output-folder names.             |

Specifically, the following fields of `pred_par` can be specified or modified in `load_pred_par.m`, among others:

| Field of `pred_par` | Meaning |
|---|---|
| `tmax_training` | Last time-step index of the initial training/normalization segment. In grid-search validation, `tmax_training + 1` is the first validation time step; final test-set evaluation starts at `tmax_cv + 1`.|
| `NORMALIZE_DATA` | Set to `true` to standardize input data using the training-set mean and standard deviation. |
| `GRAD_CLIPPING` | Set to `true` to clip the gradient norm using the threshold specified in `grad_threshold`. |
| `grad_threshold` | Gradient-norm clipping threshold. |
| `update_meth` | Gradient-based update method; `1` selects stochastic gradient descent and `2` selects ADAM. |

## Requirements

Grid-search-based hyperparameter optimization in MATLAB uses `parfor` loops and therefore requires MATLAB's Parallel Computing Toolbox, unless the `parfor` loops are manually replaced with `for` loops, which increases processing time.

RNN calculations can use the GPU by setting `beh_par.GPU_COMPUTING` to `true`. This requires MATLAB's Parallel Computing Toolbox. In previous tests, GPU computation was faster when using RTRL with a relatively high number of hidden units.


## References

This code supports the claims in the following research article:

 - Michel Pohl, Mitsuru Uesaka, Hiroyuki Takahashi, Kazuyuki Demachi, Ritu Bhusal Chhatkuli, "Prediction of the Position of External Markers Using a Recurrent Neural Network Trained With Unbiased Online Recurrent Optimization for Safe Lung Cancer Radiotherapy", Computer Methods and Programs in Biomedicine (2022): 106908 [[Published version]](https://doi.org/10.1016/j.cmpb.2022.106908) [[arXiv]](https://doi.org/10.48550/arXiv.2106.01100).

The UORO algorithm was introduced in:

 - Corentin Tallec and Yann Ollivier, "Unbiased Online Recurrent Optimization," International Conference On Learning Representation (ICLR), 2018 [[arXiv]](https://doi.org/10.48550/arXiv.1702.05043).

The marker-position data used in this repository were originally introduced in:

 - Tomas Krilavicius et al., "Predicting Respiratory Motion for Real-Time Tumour Tracking in Radiotherapy", arXiv preprint, 2015 [[arXiv]](https://doi.org/10.48550/arXiv.1508.00749).

Please cite the relevant article(s) if you use this code in your research. An accessible summary of this work is available as a Towards Data Science Editors’ Pick article, also mirrored on my personal blog:

 - Michel Pohl, "Predicting respiratory motion using online learning of recurrent neural networks for safer lung radiotherapy", Towards Data Science (2022) [[Medium]](https://medium.com/towards-data-science/forecasting-respiratory-motion-using-online-learning-of-rnns-for-safe-radiotherapy-bdf4947ad22f) [[Personal blog]](https://pohl-michel.github.io/blog/articles/predicting-respiratory-motion-online-learning-rnn/article.html).


## License

This repository is released under the BSD-3-Clause license.
