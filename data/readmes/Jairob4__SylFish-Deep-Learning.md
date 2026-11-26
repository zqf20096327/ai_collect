# sylfish-dl

Fish classification and segmentation with deep learning on the SylFishBD dataset. This is the final project for Artificial Intelligence (Universidad del Magdalena, 2026-2). Due date: Saturday, November 21, 2026.

The system takes a photograph of a fish and answers two questions: which species it is, with what confidence, and where the fish is. The demo is a Gradio interface run in Colab (`share=True`, temporary public link): you upload an image and get back the image with the fish outline and a caption with the species and the confidence percentage, plus a summary with the fish area.

## How it works

```
               ┌─► CNN (EfficientNetB0)  ─► species + confidence ─┐
fish photo  ───┤                                                   ├─► image with outline and caption
               └─► U-Net v2 (binary)     ─► fish/background mask ──┘
```

These are two independent models that only meet in the demo. They are trained, validated and saved separately, so a failure in one does not contaminate the other and each has its own metrics.

## Data

SylFishBD has 9075 color JPG photographs of 500×500 pixels. The only annotation is the class, given by the folder; there are no segmentation masks. The classes follow this order:

| boal | ilish | kalibaush | katla | koi | mrigel | pabda | rui | telapia | Total |
|---|---|---|---|---|---|---|---|---|---|
| 885 | 789 | 525 | 1133 | 592 | 1293 | 862 | 1670 | 1326 | 9075 |

The ratio between the largest and the smallest class is $1670/525\approx3.18$. There are exact and near-duplicate copies, so the split is made **by groups of duplicates** (MD5 and dHash with Hamming distance $\le 5$), 70/15/15 with seed 42: a photo and its copies never end up in different sets. This leaves 8975 images (train 6246, val 1359, test 1370); 100 were excluded for label noise. The images, masks, `.npz` files and models are not in this repository: they live on Drive ([Drive folder](https://drive.google.com/drive/folders/1taTrSyyyjND9iM3SYT313Oj7lgGljFiC?hl=es)). Dataset reference: [dataset reference to be completed].

## Segmentation: SAM 2 masks and U-Net v2 (module 05)

**Problem.** Since the dataset has no masks, the first version of the U-Net (`unet_v1`) was trained with GrabCut (OpenCV) pseudo-masks. GrabCut left 640 empty masks and its quality control discarded 1857 of 8975 (20.7 %), mostly plate, bucket or table scenes; only 7118 masks were usable.

**Idea.** Use **SAM 2** (Segment Anything Model 2, by Meta) as an **offline labeling** tool: it generates new masks once and is not part of the delivered system. The U-Net is retrained from scratch with those masks.

**Pipeline** (notebooks `05_preparacion_mascaras_sam2_{A_prompts,B_sam2,C_unet_v2}`):

1. **A (TensorFlow).** `unet_v1` predicts one box and one centroid per image; these are the SAM 2 prompts. A sample of 30 val images is drawn for visual review.
2. **B (PyTorch).** Visual pilot with two prompts (P1: fixed box; P3: the v1 box enlarged by 5 % plus a positive point at the centroid). P3 was right on 27 of 30 images (by eye) and was applied to the full batch of 8975 images (34 min on a T4). OpenCV post-processing (largest connected component and hole filling) and a quality control recalibrated on val only: $0.02 \le$ area $\le 0.35$ and border band $\le 0.08$.
3. **C (TensorFlow).** The **U-Net v2** is trained with the same architecture, hyperparameters and seed as v1 (1,946,993 parameters, BCE + Dice, Adam $10^{-3}$, batch size 16, seed 42); only the labels change. $\tau$ is chosen on val and the test set is evaluated only once.

**Quality control result.** Retention rises from 7118 to 8702 of 8975 images (79.3 % to 97.0 %). By class, `boal` goes from 63.3 % to 94.3 % and `ilish` from 62.6 % to 93.9 %.

**Final model.** After evaluating the SAM 2 option, the selected segmentation model is **`unet_v2`** (`models/unet_v2.keras`, `models/unet_v2_umbral.json`, $\tau = 0.6$). It was chosen by direct visual judgment: v2 was right on 27 of 30 val images (by eye) and SAM 2 was better than GrabCut on all 30 compared; v1 was not graded and the advantage rule set in advance was not evaluated. `unet_v1` is kept as a fallback.

| Model | Reference labels | Per-image mIoU (val) | Per-image mIoU (test) | Images evaluated (test) |
|---|---|---|---|---|
| `unet_v1` | GrabCut | 0.8334 | 0.8344 | 1119 |
| **`unet_v2`** (final) | SAM 2 | 0.8962 | 0.8944 | 1335 |

**These two rows are not comparable:** each mIoU is measured against the masks the model was trained on (GrabCut or SAM 2) and on a different set of images (`qc_ok` 7118 versus `sam2_qc_ok` 8702). The evidence that v2 is better is visual and from a single person, not a number.

## Evaluation

All decisions (architecture, threshold $\tau$, prompt, quality-control thresholds, model selection) are made on validation. The test set is evaluated only once, with the model frozen. The test set had already been evaluated with `unet_v1` before v2 was trained, and this is declared. The U-Net is evaluated with per-image IoU (mean and median) and, for v1, also with global Dice and a pixel confusion matrix.

## Segmentation limitations

- The SAM 2 masks are still pseudo-masks, not ground truth; the v1/v2 comparison is visual, on 30 val images and graded by one person.
- With prompt P3, v2 inherits where v1 located the fish (partial circularity); P1 was not graded image by image.
- In an eyeball audit, 2 of 12 approved masks were contaminated (plate or extra stain) and 2 of 12 discarded ones were large, well-segmented fish that the area threshold removes.
- The v2 training reached the cap of 40 epochs (best epoch 37) and was a single run.
- The decision to adopt v2 was made after seeing the grids, by direct visual judgment and without applying the rule set beforehand.
- SAM 2 runs on PyTorch, outside the Keras pipeline; it is used only for offline labeling.
- Switching the demo to `unet_v2` and testing it with external photos are still pending.

The full detail, with decisions, figures and glossary, is in `05_SAM2.md`.

## Repository structure

```text
sylfish-dl/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_preparacion_datos/         notebook, GUIA.md and 01_PREPARACION_DATOS.md
│   ├── 02_cnn/                       notebook, GUIA.md and 02_CNN.md
│   ├── 03_unet/                      notebook, GUIA.md and 03_UNET.md
│   ├── 04_demo/                      notebook, GUIA.md and 04_DEMO.md
│   └── 05_experimentacion_sam2/      notebooks A, B and C and 05_SAM2.md
└── reports/
    ├── figures/                      report figures
    └── tables/                       result tables (.csv, .json)
```

Folder and file names are kept in Spanish, as in the code. The repository contains only the notebooks, their guides and the results. The data and models are in the [Drive folder](https://drive.google.com/drive/folders/1taTrSyyyjND9iM3SYT313Oj7lgGljFiC?hl=es). The notebooks in 05 require PyTorch and SAM 2 (notebook B) in addition to TensorFlow, in separate Colab sessions; those dependencies are documented apart from `requirements.txt`.

## How to run

Copy the Drive folder to `MyDrive/sylfish/` and mount it in Colab. Open modules 01 to 04 in order; 01 leaves `splits.csv`, the masks and the `.npz` files on Drive. Module 05 is run afterwards, in three new Colab sessions with a T4 GPU (A, B and C, in that order), and leaves `unet_v2.keras` and `unet_v2_umbral.json` in `models/`. The demo uses U-Net v2: it loads `unet_v2.keras` and `unet_v2_umbral.json`, with the same input preprocessing as v1 (RGB 256×256, `INTER_AREA`, divided by 255).
