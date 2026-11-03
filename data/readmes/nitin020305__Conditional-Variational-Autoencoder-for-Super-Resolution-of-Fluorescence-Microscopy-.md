# SR-VAE: 2× Fluorescence Microscopy Super-Resolution with a Conditional VAE

We reconstruct 2× super-resolved fluorescence microscopy images from widefield inputs using a conditional variational autoencoder (SR-VAE). The model is trained on the CCPs subset of [BioSR](https://www.nature.com/articles/s41592-020-01048-5), with SIM images as high-resolution targets, and follows the approach of Liu, Siu and Chan (IEEE TCSVT, 2021), adapted to single-channel microscopy data.

On our test set (135 images, 9 signal levels) SR-VAE reaches **24.48 dB PSNR / 0.896 SSIM**, compared with **17.18 dB / 0.136** for bicubic interpolation.

## Model Architecture

**Figure 1. SR-VAE architecture**

![Model Architecture](assets/architecture.png)

## Result Images

**Figure 2. Comparison, example 1**

![SR-VAE comparison, example 1](assets/results_comparison_1.png)

**Figure 3. Comparison, example 2**

![SR-VAE comparison, example 2](assets/results_comparison_2.png)

*Panels, left to right: widefield input, bicubic interpolation, SR-VAE reconstruction, SIM ground truth.*

## Quantitative Results

### Test set

Mean over all 135 test images (9 signal levels × 15 images). PSNR and SSIM are computed per image against the SIM ground truth, then averaged.

| Metric | SR-VAE | Bicubic | Gain |
|---|---:|---:|---:|
| Mean PSNR (dB) | **24.48** | 17.18 | **+7.30** |
| Mean SSIM | **0.896** | 0.136 | **+0.759** |

### Results by signal level

Every level is scored against the same 15 ground-truth images.

| Signal level | Images | SR-VAE PSNR (dB) | SR-VAE SSIM | Bicubic PSNR (dB) | Bicubic SSIM | PSNR gain (dB) |
|---|---:|---:|---:|---:|---:|---:|
| level_01 | 15 | 23.60 | 0.836 | 12.23 | 0.043 | +11.37 |
| level_02 | 15 | 24.23 | 0.898 | 16.40 | 0.067 | +7.83 |
| level_03 | 15 | 24.33 | 0.898 | 17.49 | 0.093 | +6.84 |
| level_04 | 15 | 24.44 | 0.900 | 17.85 | 0.119 | +6.59 |
| level_05 | 15 | 24.46 | 0.901 | 18.02 | 0.141 | +6.44 |
| level_06 | 15 | 24.43 | 0.900 | 18.21 | 0.171 | +6.22 |
| level_07 | 15 | 24.63 | 0.904 | 18.25 | 0.193 | +6.38 |
| level_08 | 15 | 24.91 | 0.909 | 18.20 | 0.201 | +6.71 |
| level_09 | 15 | 25.28 | 0.914 | 17.97 | 0.200 | +7.31 |
| **Mean** | **135** | **24.48** | **0.896** | **17.18** | **0.136** | **+7.30** |

SR-VAE beats bicubic at every level in both metrics. Quality is steady from level 2 to level 9 (24.2 to 25.3 dB) and drops at level_01, the noisiest input, where bicubic also falls to 12.23 dB. The gain over bicubic is largest at level_01 (+11.37 dB).

### Validation results

Best checkpoint (chosen by validation PSNR), evaluated on all 2,025 validation pairs:

| Metric | SR-VAE | Bicubic | Gain |
|---|---:|---:|---:|
| Mean PSNR (dB) | 25.5173 | 17.1787 | +8.3386 |
| Mean SSIM | 0.8960 | 0.1086 | +0.7874 |

Validation and test numbers are reported separately. During training, checkpoint selection used only 3 validation images per epoch; the table above is the full-set evaluation done afterwards.

## GPU Configuration and Model Size

| | |
|---|---|
| **GPU** | NVIDIA GeForce RTX 5080, 16 GB VRAM |
| **Driver / CUDA** | Driver 610.88, CUDA 13.3 (runtime used by PyTorch: CUDA 12.8) |
| **PyTorch** | 2.11.0 (cu128) |
| **OS** | Windows |
| **Training time** | about 10 minutes per epoch at batch size 1, roughly 17 hours for 100 epochs |
| **Trainable parameters** | **39,467,651 (≈ 39.47 M)** |
| **Frozen parameters** | 20,023,232 (VGG19 feature extractor, used only inside the training loss) |
| **Inference-only parameters** | 20,728,451 (≈ 20.73 M): the encoder is dropped at test time |

| Component | Trainable parameters |
|---|---:|
| LR-HR Encoder (training only) | 18,739,200 |
| Conditional Sampling Generator | 2,099,200 |
| SR Decoder (incl. Enhanced UBP block) | 18,629,251 |
| **Total** | **39,467,651** |

Evaluation on the test set was run on CPU; no GPU is required for inference.

---

## How It Works

Let X be the low-resolution widefield image, Y the SIM target, z a latent vector and Y′ our reconstruction.

**Conditional sampling generator G(X).** Instead of drawing noise from N(0, I) for the reparameterisation trick, we generate it from the input. G(X) average-pools the LR image to 32×32, normalises it, and passes it through two fully connected layers (ReLU in between). The output is normalised to zero mean and unit variance, so it can stand in for noise but still carries information about X.

**Posterior encoder (training only).** The encoder approximates Q(z | X, Y). It has two convolutional branches, one for the HR SIM image and one for the bicubic-upsampled LR image. Each branch has five stride-2 3×3 convolutions with 32, 64, 128, 256 and 256 channels. The branches are fused by element-wise addition and passed through fully connected layers to predict μ and log σ², with log σ² clamped to [-10, 10].

**Conditional reparameterisation.**

```
z = μ(X, Y) + σ(X, Y) ⊙ G(X)
```

**Decoder.** Two paths are fused by addition. The LR path is a three-convolution feature extractor at the input resolution. The latent path maps z through two fully connected layers to a 16×16×16 tensor, resizes it bilinearly to the LR feature size and applies a convolution. For 2× scaling, one Enhanced Up-sampling Back-Projection (UBP) block performs a learned up-projection, projects back to LR resolution, computes the LR-space residual, and uses it to correct the HR estimate. A final convolution predicts a residual that is added to the bicubic upsampling of X:

```
Y' = Bicubic(X, 2) + R(z, X)
```

**Training vs inference.** During training both X and Y are available, so the encoder supplies μ and σ. At inference there is no Y, so we skip the encoder and use `z = G(X)`. This relies on the KL term pulling the posterior towards the standard normal prior; it is the intended formulation, not a guarantee that the two match exactly.

**Loss.**

```
L = ||Y − Y'||₁ + λ · ||φ54(Y) − φ54(Y')||₁ + β · KL
```

with λ = 0.1 and β = 0.001. φ54 is a frozen VGG19 feature extractor (first 35 layers of `features`, first convolution adapted to one channel, max-pooling replaced by average pooling). KL is the standard-normal KL divergence averaged over batch and latent dimensions.

## Dataset and Preprocessing

We use the BioSR CCPs structure: 20,250 training pairs and 2,025 validation pairs (the dataset's own `training_*` and `validate_*` folders, no extra splitting). The test set has 15 ground-truth images, each captured at 9 signal levels.

- **Pairing:** widefield and SIM images are matched by filename stem. If no stems match, the loader falls back to sorted order and prints a warning, so check your filenames.
- **Formats:** `.mrc`, `.tif`/`.tiff`, `.npy`, `.png`, `.jpg`, `.bmp`.
- **Stacks:** widefield stacks are averaged over frames; for SIM stacks the first frame is used.
- **Normalisation:** each image is independently percentile-normalised to [0, 1] using the 0.03rd and 99.7th percentiles. Because LR and HR are normalised separately, absolute intensity relationships between them are not preserved.
- **Training patches:** random aligned 64×64 LR / 128×128 HR crops with the same random rotation (0°, 90°, 180°, 270°) and horizontal flip (p = 0.5) applied to both.

## Training Configuration

| Setting | Value |
|---|---|
| Structure / scale | CCPs / 2× |
| Latent dimension | 1,024 |
| Feature channels (`nf`) | 256 |
| FC hidden size | 2,048 |
| Batch size | 1 (20,250 iterations per epoch) |
| Epochs | 100 |
| Optimiser | Adam, lr 1e-4, betas (0.9, 0.999), weight decay 0 |
| Scheduler | MultiStepLR, ×0.1 at epoch 50 |
| Gradient clipping | max norm 1.0 |
| Loss weights | VGG 0.1, KL 0.001 |
| Mixed precision | not used |
| Seed | 0 |

Checkpoints are written atomically: `best.pt` (best validation PSNR), `last.pt` (full resumable state, saved every 2 epochs) and `ckpt_epNNN.pt` (kept every 10 epochs, about 300 MB each).

## Inference Details

Full images are super-resolved tile by tile: 64×64 LR tiles with an 8-pixel margin (stride 48), 32 tiles per batch. Only the central 48×48 region of each tile (96×96 at 2×) is kept, so tile-border artefacts are discarded. Inputs are reflect-padded, and the stitched output is cropped to exactly 2× the input size and clamped to [0, 1].

The bicubic baseline uses `F.interpolate(..., mode="bicubic", align_corners=False)`, clipped to [0, 1]. PSNR uses data range 1.0; SSIM uses scikit-image with data range 1.0.

---

## How to Run

### 1. Repository layout

```text
sr-vae-fluorescence-sr/
├── README.md
├── notebooks/
│   ├── Conditional_VAE.ipynb          # training + validation
│   └── srvae_test_by_level.ipynb      # testing on all signal levels
├── assets/
│   ├── architecture.png
│   ├── results_comparison_1.png
│   └── results_comparison_2.png
└── requirements.txt
```

### 2. Set up the environment

You need Python 3.10 or newer and Jupyter. A CUDA GPU is strongly recommended for training (CPU is fine for testing).

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

Install PyTorch for your CUDA version from [pytorch.org](https://pytorch.org). We used CUDA 12.8, which is needed for RTX 50-series cards:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

Then the remaining packages:

```bash
pip install numpy matplotlib scikit-image tifffile mrcfile jupyter
```

Check that PyTorch sees your GPU:

```python
import torch
print(torch.__version__, torch.cuda.is_available())
```

The training notebook downloads the ImageNet VGG19 weights through torchvision on first run, so it needs an internet connection the first time.

### 3. Prepare the data

Download the BioSR CCPs data and arrange it like this:

```text
BioSR/
└── CCPs/
    ├── training_wf/     # widefield inputs
    ├── training_gt/     # SIM targets
    ├── validate_wf/
    └── validate_gt/
```

Widefield and SIM files must share the same filename stem (for example `001.tif` in both folders).

For testing, prepare a separate folder:

```text
test/
├── test_gt/             # 001.tif ... 015.tif
└── test_wf/
    ├── level_01/        # 001.tif ... 015.tif
    ├── level_02/
    └── ...              # one folder per signal level
```

### 4. Train (`Conditional_VAE.ipynb`)

1. Open the notebook in Jupyter and edit the config cell (Section 6):

   ```python
   cfg = SimpleNamespace(
       data_root=r"path/to/BioSR",       # folder that contains CCPs/
       structure="CCPs",
       out_dir=r"path/to/runs/srvae_CCPs_run_1",   # checkpoints are saved here
       ...
   )
   ```

2. Run the cells **in order, top to bottom**: imports, data helpers, model classes, losses, tiled inference and metrics, config, data loading, then the training cell.
3. The data-loading cell should report `20250 train / 2025 val pairs`. If it reports no images or warns about sorted-order pairing, fix your paths or filenames before training.
4. The training cell prints one line per epoch with loss terms, validation PSNR/SSIM and the bicubic reference. Expect about 10 minutes per epoch on an RTX 5080.
5. To check that everything works before committing to a full run, set `cfg.epochs = 2` and run the training cell. Then set it back to 100.
6. If a session dies, set `RESUME = True` in the training cell (the default) and re-run it. Training continues from `last.pt`.
7. The final cells plot the training curves, evaluate `best.pt` on the full validation set and show a LR / bicubic / SR-VAE / ground-truth comparison.

On Windows keep `cfg.workers = 0`, which is the safest setting inside Jupyter.

### 5. Test on every signal level (`srvae_test_by_level.ipynb`)

This notebook is standalone. It needs only a checkpoint and the test folder; no training data or training code.

1. Copy `best.pt` (or `last.pt` / any `ckpt_epNNN.pt`) next to the notebook.
2. Edit the settings cell:

   ```python
   TEST_ROOT = r"path/to/test"      # contains test_gt and test_wf
   CKPT = "best.pt"
   TILE, OVERLAP = 64, 8            # keep the same as training
   ```

3. Run all cells in order. The notebook rebuilds the architecture from the arguments stored in the checkpoint, finds the `level_*` folders in natural order, and prints SR-VAE and bicubic PSNR/SSIM for each.
4. It plots PSNR and SSIM against signal level and saves `results_by_level.csv`.
5. The example cell shows one image from any level. Change `LEVEL_TO_SHOW` and `IMAGE_INDEX` to look at others.
6. The save cell writes the super-resolved images as TIFFs:

   ```text
   sr_results/
   ├── level_01/001_sr.tif, 001_bicubic.tif, ...
   ├── ...
   └── ground_truth/001.tif, ...
   ```

   Set `SAVE_AS` to `uint16` (default, opens in ImageJ and Windows Photos), `uint8` or `float32`. Set `OPEN_EXPLORER = False` on non-Windows systems.
7. The last cell writes `image_metrics_by_level.csv` with per-image metrics for SR-VAE and bicubic.

### 6. Super-resolve your own image

After training (or after loading a checkpoint) in the training notebook, run the inference section:

```python
sr_img = infer_file("my_widefield.tif", "my_sr.tif")
```

The input is averaged over frames if it is a stack, normalised, super-resolved with the tiled pipeline and saved as a TIFF in [0, 1] units.

### Common problems

| Problem | What to check |
|---|---|
| `CUDA available: False` on an RTX 50-series card | Install a CUDA 12.8 build of PyTorch (the `cu128` command above) |
| `No images found in ...` | Check `data_root` and the four folder names |
| Warning about sorted-order pairing | Widefield and SIM filename stems don't match; rename them |
| `torch.load` fails with a pickle error | Load with `weights_only=False`, as the test notebook does |
| Out of memory | Lower the tile batch size (`bs`) in `sr_full`, or train with a smaller `nf` / `z_dim` |
| Checkpoint won't load | The model classes and config must match the architecture that was trained |

---

## Limitations

- We trained and tested on the CCPs structure only. We have not measured how well the model transfers to ER, F-actin, microtubules or other microscopes and acquisition settings.
- The only baseline is bicubic interpolation. We did not benchmark deconvolution, CNN or GAN methods.
- The test set has 15 ground-truth images, and our report gives per-level means without confidence intervals.
- LR and HR images are normalised independently, so intensities are not calibrated between input and output.
- Learned super-resolution can produce structures that look plausible but are not supported by the measured signal. Do not interpret fine details quantitatively without checking against reference data.
- Per-epoch checkpoint selection used only 3 validation images, so the chosen checkpoint can be sensitive to that subset.
- A seed is set, but we did not fix deterministic backend settings or pin package versions, so exact reruns may differ slightly.

## Future Work

- Train and evaluate on all four BioSR structures.
- Add deconvolution and learned baselines (for example Richardson–Lucy, a plain CNN).
- Run ablations on the conditional generator, the UBP block, the VGG loss and the KL weight.
- Report per-image statistics with confidence intervals, and benchmark runtime and memory.
- Explore intensity-preserving normalisation and uncertainty estimates from the latent sampling.

## Built With

Python, PyTorch, torchvision (VGG19), NumPy, scikit-image, tifffile, mrcfile, Matplotlib, Jupyter.

## References

1. Liu, D., Siu, W.-C., Chan, Y. (2021). *Photo-Realistic Image Super-Resolution via Variational Autoencoders.* IEEE Transactions on Circuits and Systems for Video Technology.
2. Qiao, C., et al. (2021). *Evaluation and development of deep neural networks for image super-resolution in optical microscopy.* Nature Methods, 18, 194–202. (BioSR dataset)
3. Richardson, W. H. (1972). *Bayesian-Based Iterative Method of Image Restoration.* JOSA, 62(1), 55–59.
4. Lucy, L. B. (1974). *An Iterative Technique for the Rectification of Observed Distributions.* The Astronomical Journal, 79, 745–754.
5. Ledig, C., et al. (2017). *Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network.* CVPR.
6. Weigert, M., et al. (2018). *Content-aware image restoration: pushing the limits of fluorescence microscopy.* Nature Methods, 15, 1090–1097.
