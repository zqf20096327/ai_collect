<div align="center">
  <img src="./assets/images/logo.svg" width="400"/>
</div>

<div align="center">

<h1>Labeling Neural Representations with Inverse Recognition</h1>
<h6>Accepted at 37th Conference on Neural Information Processing Systems (NeurIPS 2023)</h6>
<a href="https://arxiv.org/abs/2311.13594">Paper link</a>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lapalap/invert/blob/main/hello_invert.ipynb)

<hr />
<br> 
</div>

<div align="center">
<img src="./assets/images/about.svg" height="40"/>
</div>
<br>

<div align="center">
<img src="./assets/images/invert.svg" height="200"/>
</div>
<br>

<div align="center">
Inverse Recognition (INVERT) is a method designed to enhance our understanding of the representations learned by Deep Neural Networks (DNNs). It aims to bridge the gap between these complex, hierarchical data representations and human-understandable concepts. Unlike existing global explainability methods, INVERT is more scalable and less reliant on resources such as segmentation masks. It also offers an interpretable metric that measures the alignment between the representation and its explanation, providing a degree of statistical significance.
</div>

<br> 
<div align="center">
<img src="./assets/images/installation.svg" height="40"/>
</div>
<br> 

You can it via pip as shown below:
```
! git clone https://github.com/lapalap/invert.git --quiet
! pip install git+file:///content/invert --quiet
```
<br> 
<div align="center">
<img src="./assets/images/gettingstarted.svg" height="40"/>
</div>
<br> 

You can get started with the following [colab notebook](https://colab.research.google.com/github/lapalap/invert/blob/main/hello_invert.ipynb).

<br> 
<div align="center">
<img src="./assets/images/updates.svg" height="40"/>
</div>
<br> 

## Version 1.2

This release brings a major speed-up path for INVERT via **HDF5-based, batched explanations**—ideal for large layers and datasets.

### Highlights
- **New appendable HDF5 dataset:** `invertH5Dataset`
  - Stores a single dataset `Y` of shape **[N, D]** (float32), where each row is a flattened activation vector.
  - Simple streaming API: `.update(batch)` appends batched activations (PyTorch or NumPy); activations are flattened automatically.
  - Designed for high-throughput writes with chunking; great for long inference runs.
- **New fast explainer:** `Invert.explain_from_h5(...)`
  - Reads activations directly from an HDF5 file (dataset `Y`) and performs **fully vectorized** explanation search.
  - Computes AUROC for many concepts and features at once using **rank-based** formulas with proper tie handling.
  - Efficient **feature batching** (`feature_batch_size`) and no per-candidate loops: conjunctions/disjunctions use inclusion–exclusion algebra for sums and counts.
  - Supports the same knobs as the classic API: `L`, `B`, `limit_search`, `min_fraction`, `max_fraction`, `mode`, `memorize_states`.

### What’s improved
- **Speed & scalability:** Large, layered activations can be labeled significantly faster by avoiding repeated per-neuron passes and by computing metrics in bulk.
- **Memory efficiency:** Processes features in column-batches; no need to load the entire `[N, D]` activation matrix into GPU memory at once.
- **Backwards compatible:** The existing `explain_representation(...)` API is unchanged and still works with a single activation vector per unit.

### Minimal usage

Collect activations once (streaming) and save to HDF5:
```python
from invert_h5_dataset import invertH5Dataset

# Create (or append to) an H5 file with a single dataset "Y" of shape [N, D]
ds = invertH5Dataset("runs/acts.h5", d_dim=D, mode="a")

for imgs in loader:
    with torch.no_grad():
        acts = model(imgs.to(device))   # [B, ..., D]
        ds.update(acts)                 # appends B rows; flattens automatically

ds.close()
```

Run the fast explainer:

```
from invert.explainer import Invert

inv = Invert(device="cuda")
inv.load_concept_labels(labels_path="labels.pt",
                        description_path="labels.json")

results = inv.explain_from_h5(
    h5_path="runs/acts.h5",
    L=3, B=5,
    limit_search=None,
    min_fraction=0.0,
    max_fraction=0.5,
    mode="positive",
    memorize_states=False,
    feature_batch_size=512,   # tune for your memory
)

# results: Dict[int, List[Explanation]] keyed by feature (unit) index
```

## Version 1.1
The latest update brings several enhancements to our software:

- Improved Interface: We’ve introduced a fresh, user-friendly interface that enhances your experience.
- Speed Boost: Explanation generation is now faster, allowing you to get insights more swiftly.
- Memory Optimization: We’ve fine-tuned memory usage for better efficiency.

Specifically:

- The Phi class now supports `sympytorch`, streamlining the explanation generation process.
- Our new interface enables the `explain_representation` method to work seamlessly with individual activation tensors from a single unit.


<br> 
<div align="center">
<img src="./assets/images/citation.svg" height="40"/>
</div>
<br> 

```bibtex
@article{bykov2024labeling,
  title={Labeling neural representations with inverse recognition},
  author={Bykov, Kirill and Kopf, Laura and Nakajima, Shinichi and Kloft, Marius and H{\"o}hne, Marina},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}
```
