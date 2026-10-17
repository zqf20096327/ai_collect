# One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation

A PyTorch implementation replicating the core logic of FAE (Feature Auto-Encoder) from the paper "One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation" (arXiv:2512.07829).

## Overview

This project demonstrates how pretrained visual representations (like DINOv3) can be adapted for image generation using minimal architecture: a single attention layer compression followed by coupled decoders. The key insight is that understanding-oriented features can be compressed into generation-friendly latent spaces without complex architectural modifications.

## Motivation

Visual generative models traditionally operate in compressed latent spaces to balance efficiency and quality. However, adapting pretrained visual representations remains challenging due to fundamental mismatches:

- **Representation encoders** benefit from high-dimensional latents that capture diverse hypotheses for masked regions
- **Generative models** favor low-dimensional latents that must faithfully preserve injected noise during denoising

This implementation addresses the discrepancy by using a simple compression framework that retains sufficient information for both reconstruction and generation.

## Architecture

### Core Components

1. **DeepAdapter**: Compresses pretrained features from 1024-dim to 64-dim using:
   - Linear compression layer
   - Multi-head attention layers (3 transformer encoder layers)
   - Linear expansion back to feature space

2. **Feature Refiner**: A frozen transformer encoder (2 layers) that acts as a mathematical anchor to stabilize reconstructed features

3. **Pixel Decoder**: Converts refined features back to RGB images using:
   - Initial convolution from feature dimension to 512 channels
   - 5 bilinear upsampling stages (7x7 → 224x224)
   - Progressive channel reduction (512 → 256 → 128 → 64 → 32 → 16 → 3)

4. **PatchGAN Discriminator**: Provides adversarial training signal with spectral normalization for stability

5. **SimpleDiT (Diffusion Transformer)**: Operates in the compressed 64-dim latent space using:
   - Sinusoidal positional embeddings for time conditioning
   - 6-layer transformer encoder
   - Rectified flow formulation for efficient sampling

## Training Pipeline

### Phase 1: Feature Alignment (5,000 steps)

Train the adapter to compress and reconstruct pretrained DINOv3 features:

```
Input Features [B, 50, 1024] → Adapter → Latents [B, 50, 64]
Latents [B, 50, 64] → Expand → Raw Features [B, 50, 1024]
Raw Features → Refiner → Reconstructed Features [B, 50, 1024]
```

- Objective: MSE loss between reconstructed and original features
- Learning rate: 5e-4
- Optimizer: AdamW

### Phase 1.5: Decoder Stabilization (2,000 steps)

Pretrain the pixel decoder with noise augmentation:

```
Features + Gaussian Noise → Pixel Decoder → RGB Images
```

- Objective: MSE + LPIPS perceptual loss
- Noise augmentation: σ = 0.5
- Learning rate: 5e-4

### Phase 2: GAN Training (10,000 steps)

Joint training of adapter and pixel decoder with adversarial loss:

- **Generator Loss**:
  - L1 reconstruction: 5.0x weight (structural preservation)
  - LPIPS perceptual: 1.0x weight (perceptual quality)
  - Adversarial: 0.1x weight (texture realism)

- **Discriminator Loss**: Hinge loss with spectral normalization

- **Key Design Decisions**:
  - Adapter: Unfrozen (learns compression for generation)
  - Refiner: Frozen (prevents gradient explosion)
  - Decoder: Unfrozen (learns pixel synthesis)
  - Gradient clipping: 1.0 max norm

### Phase 3: Flow Matching (20,000 steps)

Train diffusion transformer in the compressed latent space:

```
z_t = (1 - t) * noise + t * latent
velocity = latent - noise
```

- Objective: MSE between predicted and true velocity
- Sampler: Euler method with 50-100 steps
- Learning rate: 1e-4

## Data Pipeline

The implementation uses a disk-based caching system for scalability:

1. **Preprocessing**: Extract DINOv3 features from COCO dataset
2. **Storage**: Memory-mapped files (float16) for features and images
3. **Normalization**: Online statistics (mean/std) computed during caching
4. **Loading**: Streaming from disk with multiprocessing (4 workers)

Configuration:
- Dataset: COCO 2017 (25,000 samples)
- Image size: 224x224
- Batch size: 128
- Feature dimension: 1024 (DINOv3)
- Sequence length: 50 tokens

## Key Insights from Implementation

### Why Single Attention Layer?

The adaptation task is substantially weaker than original self-supervised pretraining. For unmasked inputs, modeling diverse distributions is unnecessary. A minimal design maintains closer distance to pretrained embeddings, leading to higher reconstruction quality.

### Why Frozen Refiner?

The feature refiner acts as a mathematical anchor during GAN training. Freezing it prevents gradient explosion while allowing the adapter to learn generation-specific compressions.

### Why Low-Dimensional Latents?

Compact latent spaces (64-dim vs 1024-dim) make diffusion trajectories smoother and more stable. The dual encoding of noised input and clean target becomes less resource-demanding, enabling faster convergence.

## Generation

```python
def generate_images(n_samples=4, steps=50):
    # Start from pure noise in 64-dim space
    x = torch.randn(n_samples, 50, 64)
    
    # Euler integration
    dt = 1.0 / steps
    for i in range(steps):
        t = i * dt
        velocity = dit_model(x, t)
        x = x + velocity * dt
    
    # Decode to pixels
    features = adapter.decode_features(x)
    features = feature_refiner(features)
    images = pixel_decoder(features)
    
    return images
```

## Requirements

```
torch
transformers
datasets
wandb
lpips
timm
torchmetrics
diffusers
accelerate
requests
pillow
matplotlib
tqdm
```

## Usage

1. **Setup WandB and HuggingFace authentication** (Cell 0-1)
2. **Cache dataset features** (Cell 3, first run only)
3. **Load cached data** (Cell 4, subsequent runs)
4. **Train Phase 1**: Feature alignment (Cell 6)
5. **Train Phase 1.5**: Decoder stabilization (Cell 7)
6. **Train Phase 2**: GAN training (Cell 8)
7. **Train Phase 3**: Flow matching (Cell 9)
8. **Generate images** (Cell 10)

## Differences from Original Paper

This implementation simplifies certain aspects while maintaining core principles:

- Uses DINOv3-ConvNeXt instead of DINOv2 or SigLIP
- Employs bilinear upsampling instead of transposed convolutions
- Trains on COCO instead of ImageNet
- Uses 64-dim latents (paper tests 32-dim and 64-dim)
- Implements rectified flow instead of full diffusion formulation
- Single-stage training instead of multi-scale progressive training

## Results

The model generates 224x224 images from pure noise by:
1. Sampling in compressed 64-dim latent space (100 steps)
2. Decoding to 1024-dim DINOv3 feature space
3. Refining features with frozen transformer
4. Reconstructing pixels with upsampling decoder

See `assets/` directory for example outputs.

## Citation

Original paper:
```
@article{gao2024onelayer,
  title={One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation},
  author={Gao, Yuan and Chen, Chen and Chen, Tianrong and Gu, Jiatao},
  journal={arXiv preprint arXiv:2512.07829},
  year={2024}
}
```

## License

Research purposes only. Pretrained models (DINOv3, LPIPS) maintain their original licenses.

