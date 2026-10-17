# BrightCut: Localizing Visual Splices

## Project Overview

BrightCut is an end-to-end research toolkit for identifying tampered regions within composite imagery. It couples convolutional backbones with refinement heads to deliver high-resolution localization masks that highlight suspected edits.

![image](https://user-images.githubusercontent.com/4397546/43671765-04b292c2-97db-11e8-8709-e4097092302c.png)

## Feature Highlights

- Joint global and local reasoning for precise mask generation.
- Modular data preparation scripts supporting patch-based and full-resolution workflows.
- Checkpointed training utilities with resume-friendly logging.
- Visualization helpers for side-by-side label, prediction, and ground-truth comparisons.

![image](https://user-images.githubusercontent.com/4397546/43671759-e8b2874e-97da-11e8-9f42-e2d0afe229bf.png)

## Quickstart

```shell
pip install -r requirements.txt
python hybird.py --help
```

The first command installs dependencies. The second displays all configurable hyperparameters exposed by the training driver.

## Dataset Preparation

This project supports the Columbia splicing dataset, available through the official request form. After obtaining the data, generate training patches and resized images:

```shell
python tools/make_dataset_colmbia.py /path/to/dataset
```

Adjust output locations inside the script or via command-line arguments to match your storage layout. The resulting structure separates training, validation, and testing splits for both patches and full images.

## Training Workflow

Use `train_local.sh` as a template for launching experiments. Key flags include `--epochs`, `--arch`, `--train-batch`, `--data`, and `--base-dir`. Update paths before execution to point at your prepared dataset. Models and logs are stored under `checkpoint/local` by default.

## Monitoring Progress

Training produces scalar summaries and segmentation previews. Point your preferred visualization tool at the `checkpoint` directory to monitor loss curves, accuracy trends, and qualitative mask outputs over time.

## Evaluation and Results

Sample outputs provided below demonstrate label predictions, predicted masks, and ground-truth annotations. Use `scripts/utils/evaluation.py` to compute metrics such as pixel accuracy and mean IoU on your validation split.

![image](https://user-images.githubusercontent.com/4397546/43671725-4487e1fa-97da-11e8-8dad-e083ed1a9181.png)

Validation statistics including loss curves and segmentation accuracy are logged automatically during training.

![image](https://user-images.githubusercontent.com/4397546/43671741-a03c7e20-97da-11e8-86b4-c6df5cb1b3c1.png)

## Credits

This repository consolidates research code exploring semi-global strategies for splice localization. Cite the project if it aids your work and share improvements via pull requests.
