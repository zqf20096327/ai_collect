# Illegal Waste Dumping Detection (IWDD)

Research code for the [IWDD contest](https://mivia.unisa.it/iwddcontest2026/). It includes VideoMAE and X-CLIP fine-tuning, sliding-window video preprocessing, and YOLO detectors used to draw object bounding boxes on input frames. Single-model and ensemble inference scripts are included, with implementation limitations described below.

## Requirements

- **Python 3.11+**
- **uv package manager** - https://docs.astral.sh/uv/getting-started/installation/

## Quick Start

### 1. Setup

```bash
# Clone the repository
git clone https://github.com/00200200/Video-Waste-Dumping-Detection---IWDD.git
cd Video-Waste-Dumping-Detection---IWDD

# Install dependencies
uv sync
```

Before training, provide the following files; the dataset and trained weights are not included:

- MP4 videos in `data/raw/videos/` and matching `<video_stem>.json` annotations in `data/raw/labels/`. The loader reads `Dumping` and, for positive examples, `DumpingDetails.Timestamp` in seconds.
- Trash-detector weights at `runs/yolov8n_trash_detector/weights/best.pt` and general-detector weights at `yolov8m.pt`. The training entry point enables both YOLO detectors. See the [YOLO dataset preparation guide](docs/YOLO.md) and `src/scripts/train_yolo.py`.
- Access to the pretrained model and processor configured in `config/models_config.yaml`, either through Hugging Face downloads or a local cache.

Run the commands below from the repository root.

### 2. Training

**Basic training with default parameters:**

```bash
# Train default model (VideoMAE-SSv2)
uv run -m src.scripts.train

# Train specific model
uv run -m src.scripts.train --model videomae_ssv2 --lr 1e-5 --epochs 10 --batch-size 8 --unfreeze-layers 1 --clip-duration 3 --stride 1 --accelerator cuda
uv run -m src.scripts.train --model videomae_ssv2
uv run -m src.scripts.train --model xclip
uv run -m src.scripts.train --model videomae_kinetics
```

**Configured model keys:** `videomae_ssv2`, `videmoae_ssv2_short`, `videomae_kinetics`, `xclip` (in `config/models_config.yaml`). The spelling `videmoae_ssv2_short` is the current configuration key; the corresponding pretrained model must be accessible to use it.

**CLI arguments:**

```bash
--model              # Model name (default: videomae_ssv2)
--epochs             # Number of epochs (default: 10)
--batch-size         # Batch size (default: 1)
--lr                 # Learning rate (default: 1e-5)
--unfreeze-layers    # Final encoder layers to unfreeze (default: 1; 0 trains only the classifier for VideoMAE)
--clip-duration      # Clip duration in seconds (default: 3)
--stride             # Sliding window stride (default: 1)
--accelerator        # Device: auto/cuda/mps/cpu (default: auto)
--yolo-conf          # Trash-detector confidence threshold (default: 0.3)
--yolo-general-conf  # General-detector confidence threshold (default: 0.5)
--checkpoint         # Checkpoint path for resuming training or testing
--test-only          # Skip training and test; supply --checkpoint to evaluate trained weights
```

**Selected settings from `src/scripts/train.py`:**

```python
# Model loaded from config
model_config = get_model_config(args.model)

model = VideoClassificationModel(
    model_config=model_config,        # Config from YAML
    learning_rate=1e-5,               # Learning rate
    num_unfreeze_layers=1,            # Number of layers to unfreeze
)

# Data parameters
data = IWDDDataModule(
    model_config=model_config,        # Same config
    videos_dir="data/raw/videos",     # Path to videos
    annotations_dir="data/raw/labels", # Path to annotations
    batch_size=1,                      # Default batch size
    num_workers=0,                     # Number of data loading workers
    persistent_workers=False,
    clip_duration=3,                   # Clip duration in seconds
    stride=1,                          # Stride for sliding window
    num_frames=16,                     # Number of frames per clip
    train_split=0.1,                   # Fraction of clips used for training
    val_split=0.15,                    # Fraction of clips used for validation
    use_yolo=True,
    yolo_model_path=Path("runs/yolov8n_trash_detector/weights/best.pt"),
    yolo_general_model_path=Path("yolov8m.pt"),
    yolo_trash_conf=0.3,
    yolo_general_conf=0.5,
)

# Trainer parameters
trainer = L.Trainer(
    max_epochs=10,           # Number of epochs
    accelerator="auto",      # Accelerator
    log_every_n_steps=1,     # Logging frequency
    limit_test_batches=0.1,  # Test only 10% of test batches
    deterministic=True,
    callbacks=[ModelCheckpoint(monitor="val_loss", filename="best_model-{epoch:02d}-{val_loss:.2f}")],
    logger=CSVLogger("logs", name="test_results"),
)
```

### 3. Monitor Training

The entry point uses `CSVLogger`. Metrics are written to `logs/test_results/version_<n>/metrics.csv`, with training progress also shown in the terminal.

To use TensorBoard instead, configure a `TensorBoardLogger` in `src/scripts/train.py`, then point TensorBoard at that logger's output directory. For example, with `TensorBoardLogger("lightning_logs")`:

```bash
uv run tensorboard --logdir lightning_logs/
```

Open http://localhost:6006 in your browser to view the TensorBoard logs. The default CSV logs are not TensorBoard event files.

### 4. Checkpoints

With the current logger, checkpoints are saved to `logs/test_results/version_<n>/checkpoints/` based on validation loss (`val_loss`). Use `--checkpoint <path>` to resume training, or add `--test-only` to evaluate that checkpoint.

## Current Limitations

- `train.py` uses 10% of clips for training, 15% for validation, and the remainder for testing. `--test-only` evaluates only 10% of test batches. These settings are hard-coded in the script.
- The data module randomly splits clips, so overlapping clips from the same video can appear in different splits. Metrics from this setup do not establish performance on unseen videos; that requires splitting by video before generating clips.
- The inference scripts need fixes before use. `load_processor()` expects a `processor_class` field absent from the model configuration, and `predict_video()` passes a tensor where the model expects an input dictionary. The ensemble code also uses an uninitialized `confidence` variable and reads a `positive_votes` key it never stores. Their presence does not establish a working end-to-end ensemble.

## Project Structure

```
Video-Waste-Dumping-Detection---IWDD/
├── src/
│ ├── data/
│ │ └── dataset.py # Dataset and DataModule
│ ├── model/
│ │ └── model.py # model definition
│ ├── inference/ # Single-model and ensemble scripts (see limitations)
│ ├── scripts/
│ │ └── train.py # Training script
│ └── utils/
│ ├── metrics.py # Evaluation metrics
│ └── utils.py # Utility functions
├── data/
│ └── raw/ # Dataset directory
├── docs/ # Documentation
│ └── YOLO.md # YOLO training guide
├── config/models_config.yaml # Pretrained model configuration
├── logs/test_results/ # CSV metrics and checkpoints generated by train.py
└── README.md
```

## Documentation

- **[YOLO Training Guide](docs/YOLO.md)** - Instructions for training YOLO models with multiple datasets
