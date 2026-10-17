# HALO-Loss

A drop-in replacement for the standard Categorical Cross-Entropy (CCE) loss that forces neural networks to respect Euclidean geometry. 

What happens if classification heads cluster features using squared Euclidean distance with a built-in, zero-parameter "I don't know" origin sink, instead of an unconstrained dot product?

**Read the full deep-dive on my blog:** [Soap Bubbles and Attention Sinks: The Theory and History of the HALO-Loss](https://pisoni.ai/posts/halo/)

HALO usually matches standard CCE base accuracy while drastically improving calibration and natively catching out-of-distribution (OOD) data, slashing the False Positive Rate (FPR@95) by more than half on unseen outlier datasets like SVHN.  

## The Math Trick

At first glance, calculating the exact pairwise Euclidean distance between thousands of embeddings and class centroids sounds like a massive bottleneck compared to a highly optimized matrix multiplication. But if you expand the squared distance polynomial, you get:

$$-||x - c||^2 = -||x||^2 + 2(x \cdot c) - ||c||^2$$

In a classifier, we apply a `softmax` over the class dimension to get our probabilities. Because softmax is mathematically shift-invariant ($\text{softmax}(z + k) = \text{softmax}(z)$), the $-||x||^2$ term (which is a constant for the whole row being fed into the softmax) completely cancels out.

This leaves us with a mathematically equivalent, much simpler formulation:

$$\text{shifted\\_logit} = 2(x \cdot c) - ||c||^2$$

**What this means:** Distance-based classification is mathematically just a standard dot product, penalized by the $L_2$ norm of the class-centroid. 

## Architectural Adjustments for HALO

Switching to a distance-bounded geometry provides unique opportunities and challenges. Two main tweaks make the loss highly effective:

1. **The Origin Sink (Abstain Class)**: We create a virtual $K+1$ class with its centroid permanently bolted to the geometric origin ($c = \vec{0}$). Because our mathematical trick shifted all logits by *adding* $+||x||^2$, the shifted logit for this Abstain class perfectly cancels itself out. This gives the network a zero-parameter "I have no clue!" button to gracefully reject OOD noise.
2. **Geometric Regularizer ("Soap Bubbles")**: High-dimensional Gaussians don't look like solid spheres; due to aggressively expanding volume, they behave more similar to hollow soap bubbles. Forcing features to collapse exactly to a distance of $0.0$ wastes massive amounts of representational capacity. HALO evaluates the negative log-likelihood of the true radial distribution to act as a repulsive force, preventing representation collapse and allowing embeddings to rest comfortably on their natural $D$-dimensional shells.

## Implementation Details

Thinking of a fancy concept and then making it actually converge without agonizing hyperparameter sweeps requires a few practical engineering details under the hood:

1. **Dimensional Scaling ($\gamma$)**: High-dimensional variance causes raw squared distances to explode, instantly saturating the Softmax. We explicitly average the dot product by dividing by the embedding dimension and dynamically initialize a learnable temperature $\gamma$ to safely scale logits.
2. **The *Ideal* Abstain Bias**: Finding the right energy threshold for an Abstain Class usually turns into a brittle hyperparameter sweep. But because the shift-invariant math trick mathematically cancels out the centroid norm penalty for the origin sink, we can calculate an exact theoretical equilibrium ($t_{ideal}$) and drop an `abstain_bias` exactly one cross-entropy margin below it.
3. **Teacher-Free Self-Distillation (TFSD)**: To avoid forcing infinite separation with hard one-hot targets, HALO dynamically constructs a soft target distribution using *its own* distances to negative classes. This allows it to correct its predictions without torching the semantic "dark knowledge" and relative spatial relationships of the latent space.

## Results

I trained a ResNet-18 on CIFAR-10 and CIFAR-100 to compare standard CCE with the HALO variant. To ensure a fair test of geometry rather than capacity, HALO's embedding dimensions were strictly capped to match the dataset class count (e.g., 10 dimensions for CIFAR-10).

**CIFAR-10 Benchmark (ResNet-18)**
| Metric | Standard CCE | HALO |
| :--- | :--- | :--- |
| **ID Accuracy $(\uparrow)$** | 96.30% | **96.53%** |
| **Calibration (ECE) $(\downarrow)$** | 0.0798 | **0.0151** |
| **Far OOD (SVHN) AUROC $(\uparrow)$** | 92.51% | **98.08%** |
| **Far OOD (SVHN) FPR@95 $(\downarrow)$**| 22.08% | **10.27%** |
| **Near OOD (CIFAR-100) AUROC $(\uparrow)$**| 82.83% | **91.72%** |
| **Near OOD (CIFAR-100) FPR@95 $(\downarrow)$**| 48.94% | **37.63%** |

**CIFAR-100 Benchmark (ResNet-18)**
| Metric | Standard CCE | HALO |
| :--- | :--- | :--- |
| **ID Accuracy $(\uparrow)$** | **80.94%** | 80.80% |
| **Calibration (ECE) $(\downarrow)$** | 0.1102 | **0.0283** |
| **Far OOD (SVHN) AUROC $(\uparrow)$** | 81.01% | **86.91%** |
| **Far OOD (SVHN) FPR@95 $(\downarrow)$**| 81.00% | **63.70%** |
| **Near OOD (CIFAR-10) AUROC $(\uparrow)$**| 79.75% | **81.00%** |
| **Near OOD (CIFAR-10) FPR@95 $(\downarrow)$**| 76.77% | **75.38%** |

*(Note: Detailed evaluation reports and plots are available in the `reports/` directory).*

**Latent Space PCA Visualizations**
Standard CCE tends to produce overconfident "starburst" streaks because it forces features toward infinity. By avoiding this radial explosion, HALO pulls classes into bounded, spherical clusters that neatly orbit the origin.

*(Left: Standard CCE. Right: HALO)*  
<p align="center">
  <img src="reports/plots_cifar10_resnet18/cce_benchmark_pca.png" width="48%" alt="Standard CCE PCA"/>
  <img src="reports/plots_cifar10_resnet18/halo_benchmark_pca.png" width="48%" alt="HALO PCA"/>
</p>

*(Check out the animated PCA MP4s in the `reports/` directory for the full training evolution).*

## Try it out

The `src/losses/halo.py` file contains a clean, plug-and-play PyTorch implementation designed to act as a simple drop-in replacement.

```bash
# install dependencies
bash scripts/install.sh

# optional: download Imagenet, CIFAR-10, CIFAR-100, and SVHN datasets ahead of time
# bash scripts/download_datasets.sh

# run the full training and evaluation benchmark suite
bash scripts/run_all.sh
```


Or you can drop the halo.py file into your own code and use it like this:
```python
# your imports...
# ...
from halo import HALOModel, HALOLoss

# ...

# build and wrap the base embedding-model
base_embedding_model = build_embedding_model(...)
model = HALOModel(model=base_feature_extractor, n_classes=num_classes, embedding_dim=embedding_dim)

# init the loss
criterion = HALOLoss(emb_dims=embedding_dim, num_classes=num_classes)

# prepare centroid target ids
centroid_targets = torch.arange(num_classes, device=preds.device)

# your training loop:
for inputs, target in dataloader:
    # ...
    # compute embeddings and centroids
    embeddings, centroids = model(inputs)

    # compute loss
    loss = criterion(embeddings, target, centroids, centroid_targets)
    # ...

```

## Caveats & Next Steps

This is mostly a proof-of-concept exploring latent space geometries. A few obvious limitations and areas for exploration:
- **Scale**: ResNet-18 on CIFAR datasets is a relatively small benchmark. I haven't tested if this translates flawlessly to massive frontier representation models, but if your lab has the resources to do so, I'm looking for ML research roles and would love to connect.
- **Multi-Modal Models**: Vision-language models map text and images into a shared space using unconstrained contrastive dot products, suffering from magnitude bullying and overconfidence. HALO could provide a geometrically sound rejection threshold for unaligned image-text pairs natively during training and inference.
- **Self-Supervised Learning (SSL)**: SSL architectures constantly fight representation collapse. HALO's geometric setup and "soap-bubble" regularizer could ensure embeddings spread out uniformly across the hypersphere without heavy variance-covariance matrix computations.

If you want to try plugging this into a larger pre-training run or know how to push this further, let me know!  
Stars, Issues and PRs welcome.