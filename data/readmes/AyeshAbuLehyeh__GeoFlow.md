# [CVPR'26] GeoFlow: Real-Time Fine-Grained Cross-View Geolocalization via Iterative Flow Prediction

[Project Page](https://ayeshabulehyeh.github.io/geoflow_page/) · [ArXiv](https://arxiv.org/abs/2603.21943) · [Paper](https://arxiv.org/pdf/2603.21943)

<p align="center">
  <img src="assets/geoflow_architecture.png" width="900" alt="GeoFlow architecture">
</p>

GeoFlow is a lightweight framework for fine-grained cross-view geolocalization. The method formulates localization as an iterative flow refinement problem: the model extracts shared visual context once and then refines a coordinate estimate through lightweight updates.

This repository contains the training and evaluation code for both **KITTI** and **VIGOR**.

---

## Setup

### 1) Clone the repository

```bash
git clone https://github.com/AyeshAbuLehyeh/GeoFlow.git
cd GeoFlow
```

### 2) Create and activate the conda environment

```bash
conda create -n geoflow python=3.9 -y
conda activate geoflow
```

### 3) Install the requirements

```bash
pip install -r requirements.txt
```

---

## KITTI dataset preparation

Download and structure the KITTI data according to [HighlyAccurate](https://github.com/YujiaoShi/HighlyAccurate).

After downloading, update the dataset root and file-list paths to match your local setup. The evaluation scripts already expose these paths as arguments, and the defaults can also be adjusted in [kitti/data.py](kitti/data.py).

Expected list files:

- `train_files.txt`
- `test1_files.txt`
- `test2_files.txt`

If your dataset is stored in a different location, change:

- `--root-dir`
- `--test-file`
- and, if needed, the defaults in [kitti/data.py](kitti/data.py)

## VIGOR dataset preparation

Download [VIGOR](https://github.com/Jeff-Zilence/VIGOR) and keep its original layout:

```
VIGOR/
├── NewYork/      (panorama/, satellite/)
├── Seattle/
├── SanFrancisco/
├── Chicago/
└── splits/<City>/  (same_area_balanced_train.txt, same_area_balanced_test.txt, pano_label_balanced.txt)
```

Point `--root-dir` to this folder, or change the default in [vigor/data.py](vigor/data.py). To use the corrected labels from [SliceMatch](https://github.com/tudelft-iv/SliceMatch), place them in `VIGOR/splits__corrected/<City>/` and pass `--use-corrected-labels`.

---

## Repository structure

- **kitti/** — KITTI implementation with datasets, models, losses, and training/evaluation scripts
- **vigor/** — VIGOR implementation (known orientation, same-area and cross-area) with the same layout

---

## KITTI

### Training

#### 1) Non-orientation model

Uses the ground-truth (or externally provided) camera orientation and predicts only the translation correction between ground and satellite views. (Known orientation) 

```bash
python -m kitti.train \
  --train-list ./train_files.txt \
  --batch-size 128 \
  --epochs 200 \
  --backbone efficientnet_b0 \
  --d-model 128 \
  --use-augmentation
```

#### 2) Orientation-aware model

Jointly predicts both translation and camera orientation, so it can localize without assuming orientation is known beforehand. (Unknown orientation) 

```bash
python -m kitti.train_orient \
  --train-list ./train_files.txt \
  --batch-size 128 \
  --epochs 200 \
  --backbone efficientnet_b0 \
  --d-model 128
```


### Evaluation

#### Non-orientation model

```bash
python -m kitti.eval \
  --model-path checkpoints/<run_name>/best.pth \
  --test-set test2 \
  --batch-size 16 \
  --num-iterations 5 \
  --num-random-starts 10 \
  --root-dir /path/to/KITTI \
  --test-file /path/to/test2_files.txt
```

#### Orientation-aware model

```bash
python -m kitti.test_orient \
  --checkpoint-path checkpoints/<run_name>/best.pth \
  --batch-size 16 \
  --root-dir /path/to/KITTI \
  --test-file /path/to/test2_files.txt
```

Evaluation outputs are written to `inference_outputs/` as both text and JSON summaries.

---

## VIGOR

VIGOR uses the same model as the KITTI non-orientation setting, with known orientation. `--area` selects the same-area or cross-area split.

### Training

```bash
python -m vigor.train \
  --area same \
  --root-dir /path/to/VIGOR \
  --batch-size 80 \
  --epochs 200 \
  --backbone efficientnet_b0 \
  --d-model 128
```

### Evaluation

```bash
python -m vigor.eval \
  --model-path checkpoints/<run_name>/best.pth \
  --area same \
  --root-dir /path/to/VIGOR \
  --batch-size 32 \
  --num-iterations 1 \
  --num-random-starts 10
```

Errors are reported in meters using the per-city ground resolution of the satellite images.

---

## Citation

If GeoFlow is useful for your research, please cite:

```bibtex
@InProceedings{Abu_Lehyeh_2026_CVPR,
    author    = {Abu Lehyeh, Ayesh and Zhang, Xiaohan and Arrabi, Ahmad and Sultani, Waqas and Chen, Chen and Wshah, Safwan},
    title     = {GeoFlow: Real-Time Fine-Grained Cross-View Geolocalization via Iterative Flow Prediction},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2026},
    pages     = {5369-5378}
}
```

