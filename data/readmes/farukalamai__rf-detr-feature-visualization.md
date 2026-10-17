# rfdetr-feature-viz

Visualize what RF-DETR's backbone sees during inference. Runs a single forward pass and saves the projector feature maps alongside the detection result.

![example output](examples/example_output.png)

Each panel shows the same image from a different stage of the backbone — from early-stage features all the way to the fused representation that gets handed to the transformer decoder. Detection boxes are overlaid on every panel.

## What you get

| Panel | What it is |
|---|---|
| Detection | Original image with predicted boxes |
| Proj 1–4 | DINOv2 intermediate outputs, resampled per FPN scale, rendered via PCA → RGB |
| Fused (P4) | The C2f-fused output fed directly into the transformer decoder |

## Setup

```bash
pip install rfdetr supervision
```

## Usage

**As a script:**

```bash
python visualize.py --image your_image.jpg
python visualize.py --image your_image.jpg --model medium --threshold 0.4
python visualize.py --image your_image.jpg --no-individual  # grid only
```

## Model options

`small` (default) · `medium` · `base` · `large`

## How it works

The script hooks into `backbone.0.projector.stages_sampling` (4 per-scale resampling layers) and `backbone.0.projector.stages.0` (the C2f fusion layer) during the forward pass. Each feature map is reduced to 3 channels via PCA and mapped to RGB — no manual channel selection, the principal components carry the most variance automatically.

Hooks are registered before inference and removed after, so the model is left unchanged.
