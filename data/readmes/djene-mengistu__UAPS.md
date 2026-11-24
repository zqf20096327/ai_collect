<div align="center">

# UAPS: Uncertainty-Aware and Dynamically-Mixed Pseudo-Labels for Semi-Supervised Defect Segmentation

**Official implementation of the paper published in *Computers in Industry* (2023)**

[![Paper](https://img.shields.io/badge/Paper-Computers%20in%20Industry-blue)](https://doi.org/10.1016/j.compind.2023.103995)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.compind.2023.103995-orange)](https://doi.org/10.1016/j.compind.2023.103995)
[![GitHub stars](https://img.shields.io/github/stars/djene-mengistu/UAPS?style=social)](https://github.com/djene-mengistu/UAPS)

[**Read the Paper**](https://www.sciencedirect.com/science/article/pii/S0166361523001458) · [**Browse the Code**](https://github.com/djene-mengistu/UAPS) · [**Citation**](#citation)

</div>

---

## 📌 Overview

Accurate industrial defect segmentation often requires pixel-level annotations, which are costly and time-consuming to obtain. **UAPS** addresses this challenge through uncertainty-aware pseudo-label supervision that makes use of both labeled and unlabeled images.

UAPS employs a **shared encoder with multiple decoders**. Different perturbations of the encoder features produce diverse decoder predictions, which are **dynamically mixed** to generate pseudo-labels for unlabeled samples. Estimated prediction uncertainty is then used to guide pseudo-label supervision and regularize training, reducing the influence of unreliable predictions.

The method was evaluated on **four public defect-segmentation datasets**. In the experiments reported in the paper, UAPS outperformed the fully supervised baseline and six compared state-of-the-art semi-supervised segmentation methods. Ablation experiments further investigated the contribution of the proposed components.

### ✨ Key contributions

- **Dynamic pseudo-label mixing:** combines predictions from multiple decoders using randomly generated mixing weights.
- **Uncertainty-aware supervision:** estimates disagreement using Kullback–Leibler (KL) divergence to guide learning from unlabeled images.
- **Perturbation-based prediction diversity:** applies different perturbations to shared encoder features before decoding.
- **Experimental validation:** evaluates the method on NEU-Seg, DAGM, Magnetic Tiles, and KolektorSDD2, with ablation studies.

## 🔍 Why uncertainty matters

Not all pseudo-label predictions are equally reliable. Uncertainty estimates can help identify ambiguous regions and reduce the impact of erroneous supervision during semi-supervised training.

<p align="center">
  <img src="fig_data/uncertainty.jpg" alt="Example predictions, false-positive and false-negative errors, and estimated uncertainty" width="75%" />
</p>

<p align="center"><em>Figure 1. Network predictions, false-positive and false-negative errors, and the uncertainty map. The illustrated uncertainty is computed using KL divergence between the primary decoder prediction and the average prediction.</em></p>

## 🏗️ UAPS framework

<p align="center">
  <img src="fig_data/main-arch.jpg" alt="Overall UAPS semi-supervised learning framework" width="90%" />
</p>

<p align="center"><em>Figure 2. UAPS framework for unlabeled samples. Multiple decoders process differently perturbed encoder features. Their predictions are dynamically combined to form pseudo-labels, while prediction disagreement provides uncertainty estimates for supervision.</em></p>

### Encoder–decoder architecture and perturbations

<p align="center">
  <img src="fig_data/UNET-baseline.jpg" alt="U-Net-based baseline and perturbation modules" width="85%" />
</p>

<p align="center"><em>Figure 3. U-Net-based baseline with feature perturbation modules. The shared encoder produces features that are perturbed differently before being passed to the decoder branches.</em></p>

## 🗂️ Datasets

UAPS was evaluated on four publicly available industrial defect-segmentation datasets.

| Dataset | Domain | Dataset / reference |
|---|---|---|
| **NEU-Seg** | Steel surface defects | [Reference](https://ieeexplore.ieee.org/document/8930292) |
| **DAGM** | Industrial optical inspection | [Download](https://www.kaggle.com/datasets/mhskjelvareid/dagm-2007-competition-dataset-optical-inspection) |
| **Magnetic Tiles (MTiles)** | Magnetic tile surface defects | [Download](https://www.kaggle.com/datasets/alex000kim/magnetic-tile-surface-defects) |
| **KolektorSDD2 (KoSDD2)** | Industrial surface defects | [Dataset page](https://www.vicos.si/resources/kolektorsdd2/) |

Place the downloaded data under the `data/` directory, using the dataset directory names expected by the training scripts:

```text
data/
├── NEU_data/
├── DAGM_data/
├── MTiles_data/
└── KoSDD2_data/
```

> **Note:** The folders above represent the expected top-level layout, not a complete specification of image/mask filenames or preprocessing. Check the dataset-specific data-loading code before training.

## ⚙️ Training and evaluation

The repository organizes the proposed method and compared approaches into separate directories. Use the relevant dataset-specific directory and configure the paths and hyperparameters in the corresponding scripts.

### 1. Prepare the environment

Install the dependencies required by the Python files in your selected experiment directory. Check the repository's environment or dependency files, if provided, for compatible versions.

### 2. Configure training

Before training, review the experiment settings, including:

- Labeled-data ratio and dataset paths
- Iterations per epoch
- Consistency-loss ramp-up length
- Consistency-loss coefficients
- Model and checkpoint output paths

### 3. Train UAPS

From the directory containing the corresponding script, run:

```bash
python UAPS_train.py
```

### 4. Evaluate UAPS

Open the testing notebook and configure the trained checkpoint and dataset paths:

```text
UAPS_Testing.ipynb
```

Run the notebook cells in order to generate predictions and evaluate the trained model. Repeat the procedure with the corresponding scripts and settings for other datasets.

> **Reproducibility:** Consult the paper for the experimental protocol and hyperparameter settings. Exact environment versions, preprocessing commands, and checkpoint download links are not specified in this README; add them once confirmed from the repository.

## 🖼️ Qualitative results

### NEU-Seg

<p align="center">
  <img src="fig_data/neu-viz.jpg" alt="Qualitative defect segmentation results on NEU-Seg" width="85%" />
</p>

<p align="center"><em>Figure 4. Selected NEU-Seg segmentation results. Red dashed boxes highlight regions containing incorrect predictions.</em></p>

### Magnetic Tiles

<p align="center">
  <img src="fig_data/mt-viz.jpg" alt="Qualitative defect segmentation results on Magnetic Tiles" width="85%" />
</p>

<p align="center"><em>Figure 5. Selected segmentation results on the Magnetic Tiles dataset.</em></p>

For quantitative comparisons and ablation results, please refer to the [published paper](https://doi.org/10.1016/j.compind.2023.103995).

## 📖 Citation

If UAPS is useful in your research, please cite:

```bibtex
@article{SIME2023103995,
  title   = {Uncertainty-aware and dynamically-mixed pseudo-labels for semi-supervised defect segmentation},
  author  = {Sime, Dejene M. and Wang, Guotai and Zeng, Zhi and Peng, Bei},
  journal = {Computers in Industry},
  volume  = {152},
  pages   = {103995},
  year    = {2023},
  issn    = {0166-3615},
  doi     = {10.1016/j.compind.2023.103995},
  url     = {https://www.sciencedirect.com/science/article/pii/S0166361523001458}
}
```

## 🤝 Acknowledgments

Parts of this implementation build on code from [simEps](https://github.com/djene-mengistu/simEps). We acknowledge the contributions of the original implementation and related open-source research.

## 📬 Contact and contributions

For questions, reproducibility issues, or suggestions, please [open a GitHub issue](https://github.com/djene-mengistu/UAPS/issues) or contact **djene.mengistu@gmail.com**.

If you find this work useful, consider [⭐ starring the repository](https://github.com/djene-mengistu/UAPS) and citing the paper.
