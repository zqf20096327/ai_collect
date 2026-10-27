<h1 align="center">One image through a CNN</h1>

<p align="center">
  <b>Follow a single brain-MRI-style slice, layer by layer, through a convolutional neural network<br>
  written from scratch in NumPy, and see exactly how it decides "lesion".</b>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.9%2B-2a78d6">
  <img alt="Dependencies" src="https://img.shields.io/badge/deps-numpy%20%C2%B7%20matplotlib%20%C2%B7%20pillow-52514e">
  <img alt="No deep-learning framework" src="https://img.shields.io/badge/PyTorch%2FTensorFlow-not%20needed-eb6834">
  <img alt="Tests" src="https://github.com/anupbagale/cnn-one-image/actions/workflows/tests.yml/badge.svg">
</p>

<p align="center">
  <img src="assets/hero.png" alt="One MRI-like slice passing through conv, ReLU, pooling, a second conv block, a dense layer and softmax, ending in 99.6% lesion" width="100%">
</p>

Most CNN tutorials show a diagram of boxes. This repo shows **the actual numbers** inside each box for
one real input, so every step can be checked by eye. Everything runs on a laptop CPU in under half a minute.

| Step | Layer | Output shape | What it does, in one line |
|:---:|---|:---:|---|
| 1 | Input | `1 × 96 × 96` | An image is just a grid of brightness values |
| 2 | Conv 1 (4 filters, 3×3) | `4 × 96 × 96` | Slide small weight grids over the image to find edges and spots |
| 3 | ReLU | `4 × 96 × 96` | Keep positive evidence, drop the rest |
| 4 | Max-pool 2×2 | `4 × 48 × 48` | Keep the strongest response in each tile, shrink the map |
| 5 | Conv 2 (2 filters, 9×9) + ReLU + pool | `2 × 24 × 24` | Combine simple parts into bigger shapes |
| 6 | Flatten + Dense | `1,152 → 2` | Every pixel of every map casts a weighted vote |
| 7 | Softmax | `2` | Turn the votes into probabilities |

---

## 1 · An image is a grid of numbers

<img src="assets/01_pixels.png" alt="The input slice with an orange box, and the 8x8 numbers inside that box" width="100%">

The input is a synthetic axial slice: skull, brain tissue, two ventricles, scanner noise, a coil bias field,
and one bright round lesion. Inside the orange box you can see the jump from tissue (≈ 0.45) to lesion (≈ 0.75).
That jump is all the network will ever get to work with.

> [!NOTE]
> **Why synthetic?** No patient data, no licence, no download. Anyone can clone the repo and reproduce every
> figure bit-for-bit. The generator lives in [`cnn/phantom.py`](cnn/phantom.py).

## 2 · Convolution: multiply, sum, slide

<img src="assets/02_one_convolution.png" alt="A 3x3 image patch multiplied element-wise by the vertical-edge kernel, summing to one output value" width="100%">

Take a 3 × 3 patch, multiply it cell-by-cell with a 3 × 3 **kernel**, add everything up: that's one output
pixel. On the lesion's left edge (dark → bright) the negative and positive columns don't cancel, so the
answer is large. On flat tissue they cancel to ≈ 0. Now do that at every position:

<p align="center">
  <img src="assets/02_sliding_kernel.gif" alt="Animation of the 3x3 kernel sliding across the lesion and filling in the feature map" width="80%">
</p>

```python
# cnn/layers.py: every output pixel = sum(patch * kernel) + bias
patches = sliding_window_view(x_padded, (k, k), axis=(1, 2))
out = np.einsum("chwij,ocij->ohw", patches, kernels)
```

## 3 · Four filters, four questions

<img src="assets/03_conv1_feature_maps.png" alt="Four 3x3 kernels and the feature maps they produce" width="100%">

Each filter asks a different question of the same image: *Where are vertical edges? Horizontal edges? Isolated
bright dots? What's the local brightness?* Blue is a strong positive answer, red a strong negative one.

> [!TIP]
> These first-layer kernels are classic image-processing filters (Sobel, Laplacian, Gaussian), set by hand so
> they're readable. When a real CNN is trained on images, its first-layer filters usually end up looking much
> like these.

## 4 · ReLU: keep the positive evidence

<img src="assets/04_relu.png" alt="Vertical-edge map before ReLU, the ReLU curve, and the map after ReLU" width="100%">

`ReLU(x) = max(0, x)`. It's the simplest possible non-linearity, and without it stacking layers would collapse
into a single linear filter. After ReLU, the vertical-edge map only keeps dark-to-bright edges.

## 5 · Max-pooling: shrink, but keep what matters

<img src="assets/05_max_pool.png" alt="An 8x8 patch split into 2x2 tiles with the max of each highlighted, and the resulting 4x4 grid" width="100%">

Split the map into 2 × 2 tiles and keep only the largest value (orange). The map becomes 4× smaller, the
edge is still there, and the next layer can now "see" a wider area of the original image with the same size
kernel.

## 6 · The second layer builds shapes from parts

<img src="assets/06_conv2_feature_maps.png" alt="The input, the boundaries map and the round-blob map from conv layer 2" width="100%">

Each Conv 2 filter is a `4 × 9 × 9` cube: it reads **all four** layer-1 maps at once. One combines the two edge
maps into object **boundaries**; the other is a centre-minus-surround detector for **round bright blobs**.

The blob map lights up on the lesion (dashed circle), **but also on the skull**, which is bright too. A filter
alone can't tell them apart. That's the next layer's job.

## 7 · The decision, and where it came from

<img src="assets/07_decision.png" alt="Learned dense-layer weights for both channels, the evidence map overlaid on the input, and the softmax output" width="100%">

The dense layer is the only part that is **trained** (softmax regression, plain gradient descent, 1,000
synthetic slices). Look at what it learned (left two panels): orange weights inside the brain, nearly zero on the
skull ring. Nobody told it about anatomy; it figured out that bright blobs *inside the brain* mean lesion and
bright pixels *on the rim* mean nothing.

Multiplying each activation by its weight gives an **evidence map**: which pixels pushed the decision toward
"lesion". For this image, almost all of it comes from the lesion itself. This is the same idea behind
[CAM / Grad-CAM](https://arxiv.org/abs/1610.02391), the explanation maps used to check what medical-imaging
models are actually looking at.

## 8 · Sanity check: same anatomy, no lesion

<img src="assets/08_with_vs_without.png" alt="Side-by-side pass for the slice with and without the lesion" width="100%">

Same skull, same ventricles, lesion removed. The orange evidence disappears and the prediction flips to
**normal**. The model is responding to the lesion, not to something else in the picture.

---

## Results

| | |
|---|---|
| Training set | 1,000 synthetic slices (50% with lesion) |
| Held-out test set | 400 new slices, different random seed |
| **Test accuracy** | **98.8%** |
| This image | P(lesion) = 99.6%, and 0.0% for the same slice without the lesion |

> [!IMPORTANT]
> **Honest limitations.** The data is synthetic and far easier than real MRI. The conv filters are fixed by
> hand, so only 2,306 parameters are learned. Real lesions vary in shape, contrast and location, and scans vary
> across hospitals and scanners. The point here is to make each operation visible, not to build a clinical tool.

## How this connects to medical imaging

- **Skull stripping matters.** Step 6 shows a blob detector confusing skull with lesion. That's why real
  neuro-imaging pipelines remove the skull before analysis (e.g. with tools like FSL BET or HD-BET).
- **Explainability isn't optional.** An evidence map like step 7 is how you catch a model that "detects disease"
  by looking at a scanner label or a ruler. In clinical AI, *why* matters as much as *what*.
- **Controlled experiments.** Step 8 is a counterfactual test: change one thing, check the prediction changes
  for the right reason.

## Run it yourself

```bash
git clone https://github.com/anupbagale/cnn-one-image.git
cd cnn-one-image
pip install -r requirements.txt
python walkthrough.py        # trains the dense layer, regenerates every figure in assets/
python -m pytest -q          # checks the fast layers against slow loop versions
```

Try changing `EXAMPLE_SEED` at the top of `walkthrough.py` to follow a different slice.

## Repository layout

```
cnn-one-image/
├── cnn/
│   ├── layers.py      conv2d, relu, max_pool, dense, softmax (≈ 70 lines, NumPy only)
│   ├── model.py       TinyCNN: the filters, forward pass, training, evidence map
│   └── phantom.py     synthetic brain-MRI-like slices
├── tests/
│   └── test_layers.py every layer checked against a naive for-loop version
├── walkthrough.py     runs everything and draws every figure
└── assets/            the figures and animation shown above
```

## Ideas for next steps

- Learn the conv filters too (backpropagation through `conv2d` and `max_pool`) and compare them with the hand-set ones.
- Swap the phantom for a real public dataset slice, such as BraTS brain-tumour MRI.
- Rebuild the same network in PyTorch and confirm the outputs match these NumPy numbers.

## License

MIT, see [LICENSE](LICENSE).
