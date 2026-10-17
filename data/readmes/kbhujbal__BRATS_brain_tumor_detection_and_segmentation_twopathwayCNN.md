# Brain Tumor Segmentation with Two-Pathway CNNs

PyTorch implementation of the paper:

> **Deep Learning based Model for Brain Tumor Detection and Segmentation using BRATS Dataset**
> Kunal Bhujbal, Dr. Pradip Mane, Ananya More
> *GRENZE International Journal of Engineering and Technology (2022) 2747-2761*
> [DOI: 01.GIJET.9.1.309](https://thegrenze.com/index.php?display=page&view=journalabstract&absid=1701&id=8)

Adapted for the **BraTS 2020** dataset (494 subjects, 4 MRI modalities).

---

## Paper Summary

The paper proposes a fully automatic brain tumor segmentation method using CNNs tailored to glioblastomas in MRI. Key contributions:

1. **Two-Pathway Architecture** — A local pathway (7x7 kernels) captures fine-grained details while a global pathway (13x13 kernels) captures broader context. Their feature maps are concatenated and fed to a convolutional output layer.

2. **Cascaded Architectures** — The output probabilities of a first TwoPathCNN are fed as additional input to a second CNN, modeling local label dependencies as an efficient alternative to CRFs. Three variants are explored:
   - **InputCascadeCNN** — concatenation at input level (best performer, Rank 2 on BRATS 2013)
   - **LocalCascadeCNN** — concatenation at local pathway's first hidden layer
   - **MFCascadeCNN** — concatenation at pre-output level (analogous to mean-field CRF inference)

3. **Two-Phase Training** — Phase 1 trains all layers with balanced label sampling (equiprobable classes). Phase 2 freezes the backbone and retrains only the output layer with the natural label distribution to calibrate probabilities.

4. **Fully-Convolutional Inference** — The output layer uses convolution instead of fully-connected layers, enabling whole-slice prediction in a single forward pass (45x speedup).

### Architecture (Fig. 2)

```
Input (4 x 33 x 33)
    ├── Local Path:  Conv7x7 → Maxout → Pool4x4 → Conv3x3 → Maxout → Pool2x2 → (64 x 21 x 21)
    └── Global Path: Conv13x13 → Maxout → (160 x 21 x 21)
                          ↓ Concatenation (224 x 21 x 21)
                          ↓ Conv21x21 → Softmax → (num_classes x 1 x 1)
```

All convolutions use **valid mode** (no padding). Max pooling uses **stride 1** to preserve per-pixel accuracy. Maxout activation with K=2 replaces traditional nonlinearities.

---

## Adaptation for BraTS 2020

| Aspect | Paper (BraTS 2013) | This Implementation (BraTS 2020) |
|---|---|---|
| Training subjects | 30 | 369 (+ 125 LGG) |
| Labels | 5 (0,1,2,3,4) | 4 (0,1,2,4 → remapped to 0,1,2,3) |
| Label 3 | Non-enhancing tumor | Merged into label 1 (NCR/NET) |
| Framework | Pylearn2 / Theano | PyTorch |
| Output classes | 5 | 4 |

Evaluation regions remain the same: **Whole Tumor** (1+2+4), **Tumor Core** (1+4), **Enhancing Tumor** (4).

---

## Project Structure

```
├── configs/config.yaml              # Hyperparameters matching the paper
├── src/
│   ├── models/
│   │   ├── layers.py                # MaxoutUnit, ConvMaxoutBlock, SoftmaxOutputLayer
│   │   ├── two_path_cnn.py          # TwoPathCNN, LocalPathCNN, GlobalPathCNN
│   │   └── cascaded.py              # InputCascadeCNN, LocalCascadeCNN, MFCascadeCNN
│   ├── data/
│   │   ├── preprocessing.py         # Intensity clipping, normalization, label remapping
│   │   ├── dataset.py               # Patch extraction with balanced/natural sampling
│   │   └── sampler.py               # Two-phase sampler
│   ├── training/trainer.py          # Two-phase training with momentum schedule
│   ├── evaluation/metrics.py        # Dice, Sensitivity, Specificity per tumor region
│   ├── inference/predictor.py       # Fully-convolutional inference + post-processing
│   └── utils/visualization.py       # Segmentation overlays, multi-view plots
├── scripts/
│   ├── train.py                     # Training entry point
│   ├── evaluate.py                  # Evaluation entry point
│   └── predict.py                   # Prediction entry point (NIfTI output)
└── tests/test_models.py             # 25 unit tests for all architectures
```

---

## Setup

```bash
# Clone and install
git clone <repo-url>
cd BRATS_brain_tumor_detection_and_segmentation_twopathwayCNN
pip install -r requirements.txt
```

### Dataset

Download **BraTS 2020** from [Kaggle](https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation) and place it under `data/`:

```
data/
└── BraTS2020_TrainingData/
    └── MICCAI_BraTS2020_TrainingData/
        ├── BraTS20_Training_001/
        │   ├── BraTS20_Training_001_flair.nii.gz
        │   ├── BraTS20_Training_001_t1.nii.gz
        │   ├── BraTS20_Training_001_t1ce.nii.gz
        │   ├── BraTS20_Training_001_t2.nii.gz
        │   └── BraTS20_Training_001_seg.nii.gz
        ├── BraTS20_Training_002/
        └── ...
```

---

## Usage

### Train TwoPathCNN

```bash
python scripts/train.py --config configs/config.yaml
```

### Train InputCascadeCNN (best performer)

First train TwoPathCNN, then use it as the pre-trained CNN1:

```bash
python scripts/train.py --config configs/config.yaml \
    --architecture InputCascadeCNN \
    --pretrained-twopathcnn checkpoints/best_final.pth
```

### Evaluate

```bash
python scripts/evaluate.py \
    --checkpoint checkpoints/best_final.pth \
    --visualize
```

### Predict on new data

```bash
python scripts/predict.py \
    --checkpoint checkpoints/best_final.pth \
    --input-dir data/BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData \
    --output-dir predictions
```

### Run tests

```bash
python -m pytest tests/ -v
```

---

## Key Hyperparameters (from the paper)

| Parameter | Value |
|---|---|
| Patch size | 33 x 33 (65 x 65 for cascaded) |
| Learning rate | 0.005, decayed by 0.1 per epoch |
| Momentum | 0.5 → 0.9 (linear schedule) |
| Maxout K | 2 |
| Dropout | 0.5 |
| Regularization | L1 + L2 (1e-5) |
| Weight clipping | ±2.0 |
| Kernel init | U(-0.005, 0.005) |
| Bias init (softmax) | log(class frequency) |

---

## Implemented Architectures

| Architecture | Paper Ref. | Params | BRATS 2013 Dice (Complete / Core / Enhancing) |
|---|---|---|---|
| TwoPathCNN* | Fig. 2, Table 1 | ~651K | 0.85 / 0.78 / 0.73 |
| InputCascadeCNN* | Fig. 3a, Table 2 | ~802K | 0.88 / 0.79 / 0.73 |
| LocalCascadeCNN* | Fig. 3b, Table 2 | ~654K | 0.88 / 0.76 / 0.72 |
| MFCascadeCNN* | Fig. 3c, Table 2 | ~662K | 0.86 / 0.77 / 0.73 |
| LocalPathCNN* | Table 1 (ablation) | — | 0.85 / 0.74 / 0.71 |
| GlobalPathCNN* | Table 1 (ablation) | — | 0.82 / 0.73 / 0.68 |

\* denotes two-phase training (reported scores from the original paper on BraTS 2013).

---

## References

```bibtex
@article{,
  title={Deep Learning based Model for Brain Tumor Detection and Segmentation using BRATS Dataset},
  author={Kunal Bhujbal, Dr. Pradip Mane, Ananya More},
  journal={GRENZE International Journal of Engineering and Technology},
  volume={9},
  pages={2747-2761},
  year={2022},
  publisher={Springer}
}
```
