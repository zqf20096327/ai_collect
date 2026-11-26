# MNIST Neural Network from Scratch Using Only NumPy

A modular neural network built from scratch using only NumPy. No PyTorch, no TensorFlow, no scikit-learn or any other external libraries. Every gradient was derived by hand and implemented as a layer with its own `forward` and `backward`, and verified numerically with gradient checking. The final model reaches **98.05% test accuracy** on MNIST.

## Highlights

- **No ML libraries.** Layers, loss, optimizer, training loop and data loading (parsing the raw IDX files byte by byte) are all written with NumPy.
- **Hand-derived backpropagation.** Each formula was derived on paper, starting from a single neuron and generalizing to matrix form.
- **Numerically verified.** A gradient check compares every analytic gradient with a central-difference estimate; the largest relative error is below 4 × 10⁻⁹.
- **Tested.** Unit tests for the loss layer and the full gradient check run with `pytest`.
- **Reproducible.** Fixed seeds, a train / validation / test split, experiment results saved to JSON and plots generated from them.
- **Reusable weights.** The trained model is saved as a 408 KB `float32` file and can be reloaded without retraining.

## Architecture

```
784 → Dense(128) → ReLU → Dense(10) → Softmax + Cross-Entropy
```

| Hyperparameter | Value |
|---|---|
| Learning rate | 0.5 |
| Batch size | 64 |
| Epochs | 20 |
| Optimizer | Mini-batch SGD |
| Weight initialization | He (`randn · √(2 / fan_in)`) |
| Data split | 50,000 train / 10,000 validation / 10,000 test |

Inputs are scaled to [0, 1] by dividing by 255; labels are one-hot encoded.

## The Math

Notation: a batch has $m$ examples. $X$ is $(m \times \text{in})$, $W$ is $(\text{in} \times \text{out})$, $b$ is $(1 \times \text{out})$. For any quantity $A$, $dA$ means $\partial J / \partial A$, the gradient of the cost with respect to $A$; it always has the same shape as $A$.

### Dense

Forward:

$$Z = XW + b$$

Backward, given $dZ$ from the next layer:

$$dW = X^\top dZ \qquad db = \sum_{i=1}^{m} dZ_{i,:} \qquad dX = dZ\, W^\top$$

$W$ and $b$ are shared by every example in the batch, so each example's contribution is **summed** into $dW$ and $db$. Each row of $X$ belongs to a single example, so $dX$ involves no sum over the batch. The layer stores $X$ during the forward pass because $dW$ needs it.

### ReLU

$$A = \max(0, Z) \qquad dZ = dA \odot \mathbb{1}[Z > 0]$$

ReLU acts on each element independently, so its Jacobian is diagonal and the backward pass reduces to an element-wise mask: active units pass the gradient through, inactive ones block it.

### Softmax + Cross-Entropy

$$\hat{y}_{ic} = \frac{e^{z_{ic}}}{\sum_{k} e^{z_{ik}}} \qquad J = -\frac{1}{m} \sum_{i=1}^{m} \sum_{c} y_{ic} \log \hat{y}_{ic}$$

The two are implemented as a single layer because their combined gradient simplifies to

$$dZ = \frac{\hat{y} - y}{m}$$

The $1/m$ comes from averaging the loss over the batch. Because it is applied once, at the start of the backward pass, every gradient downstream is automatically an average and no other layer needs to divide by $m$.

## Numerical Stability

- **Overflow / underflow in softmax.** `exp(1000)` overflows to `inf`, while subtracting one global maximum from the whole batch can push other rows to `exp(-1000) = 0`. Subtracting **each row's own maximum** keeps the largest exponent in every row at exactly `e⁰ = 1`, so the denominator is always ≥ 1. This does not change the result, since the constant cancels between numerator and denominator.
- **`log(0)`.** Even a stable softmax can output an exact 0. With one-hot labels this gives `0 · log(0) = 0 · (−∞) = nan`, which then spreads to every weight, even when the prediction is correct. Probabilities are clipped to `[1e-12, 1]` before the log.

## Verification

The backward pass is checked against a numerical derivative computed only from the forward pass:

$$\frac{\partial J}{\partial w} \approx \frac{J(w + \varepsilon) - J(w - \varepsilon)}{2\varepsilon}, \qquad \varepsilon = 10^{-5}$$

The central difference has error $O(\varepsilon^2)$ instead of $O(\varepsilon)$, and $\varepsilon = 10^{-5}$ balances that approximation error against floating-point rounding. The check runs on a small 4 → 5 → 3 network for every element of every parameter. Because $dW_1$ sits at the start of the chain, it can only be correct if the backward passes of the loss, both Dense layers and ReLU are all correct.

| Parameter | Max relative error |
|---|---|
| W1 | 3.6 × 10⁻⁹ |
| b1 | 5.7 × 10⁻¹⁰ |
| W2 | 2.8 × 10⁻⁹ |
| b2 | 2.7 × 10⁻¹⁰ |

Run all tests:

```bash
pytest
```

## Experiments

Each experiment changes **one** hyperparameter from the baseline (lr = 0.1, hidden = 128, batch = 64, 10 epochs) and is measured on the validation set. The test set was not used for any of these decisions.

### Learning rate

![Learning rate](figures/exp_learning_rate.png)

| Learning rate | Val. accuracy (epoch 10) |
|---|---|
| 0.01 | 92.64% |
| 0.05 | 96.18% |
| 0.1 | 96.95% |
| 0.5 | 97.73% |

With 0.01 the steps are so small that the model is still far from converged after 10 epochs; it would get there with much longer training. 0.5 gives the best accuracy but also the least stable curve: the drop at epoch 3 is the model overshooting the minimum and recovering. Much larger rates would overshoot repeatedly and fail to converge.

### Hidden layer size

![Hidden size](figures/exp_hidden_size.png)

| Hidden units | Parameters | Val. accuracy (epoch 10) | Training time |
|---|---|---|---|
| 32 | 25,450 | 95.83% | 2.3 s |
| 128 | 101,770 | 96.95% | ~4.8 s |
| 512 | 407,050 | 97.47% | 14.9 s |

More hidden units give more learned features and higher accuracy, with diminishing returns: 512 units add about 0.5 points over 128 for about three times the training time and four times the weights. Training time grows with the number of parameters, but less than proportionally, because part of each step (shuffling, slicing, the loss) is a fixed cost.

### Long training (30 epochs)

![30 epochs](figures/exp_30_epochs.png)

The training loss keeps falling for all 30 epochs, but the validation loss stops improving around epoch 21: the model starts to fit the training set more closely than it generalizes, a mild form of overfitting. Interestingly, validation **accuracy** still creeps up slowly after that point. Accuracy only checks whether the highest probability is on the right class, while the loss also measures confidence. The model keeps fixing a few borderline examples (accuracy up) while becoming over-confident on the ones it gets wrong (loss up), and the two effects roughly cancel.

## Results

The final configuration (lr = 0.5, hidden = 128, 20 epochs) was chosen on the validation set. A learning rate of 0.5 performed best in the learning-rate experiment, and in a 30-epoch run with this rate the validation accuracy peaked around epoch 19, so training stops at 20 epochs instead of continuing into the overfitting regime. 128 hidden units were kept over 512 because the gain was small and the weight file stays four times smaller.

The test set was evaluated **once**, after all choices were made.

| Split | Accuracy   |
|---|------------|
| Validation | **97.89%** |
| Test | **98.05%** |

The weights are saved in `weights/model.npz` as `float32` (408 KB). Reloading them into a fresh model reproduces the original logits to within 1.2 × 10⁻⁶.

## Limitations & Next Steps

- **No translation invariance.** Every weight in the first Dense layer is tied to one pixel position, so a digit shifted by a few pixels looks like a completely different input. A convolutional layer fixes this; adding `Conv` and `Pooling` layers to this engine is the natural next step.
- **Plain SGD.** Momentum and Adam would make training faster and less sensitive to the learning rate.
- **No regularization.** Dropout or weight decay could reduce the overfitting seen in long training; BatchNorm could stabilize larger learning rates.
- **Single seed.** All results come from one run. Reporting mean ± std over several seeds would make the comparisons more reliable.
- **Demo.** A browser demo where you draw a digit and the model predicts it, using the saved weights.

## Project Structure

```
nn/               Layers, loss, optimizer and model
  dense.py
  relu.py
  softmax_cross_entropy.py
  sgd.py
  model.py
tests/            Unit tests and gradient check
experiments/      Small learning scripts (finite differences, toy SGD)
figures/          Experiment plots
weights/          Trained weights (float32)
data_loader.py    Reads the raw MNIST IDX files, normalizes, one-hot encodes, splits
train.py          Runs the experiments and saves results.json
evaluate.py       Trains the final model, evaluates on the test set, saves the weights
plot_results.py   Draws the figures from results.json
```

## How to Run

```bash
pip install -r requirements.txt
```

Download the four MNIST files (original page: [yann.lecun.com/exdb/mnist](http://yann.lecun.com/exdb/mnist/), mirror used here: [mkolod/MNIST](https://github.com/mkolod/MNIST)) and place them in a `data/` folder in the project root:

```
data/
  train-images-idx3-ubyte.gz
  train-labels-idx1-ubyte.gz
  t10k-images-idx3-ubyte.gz
  t10k-labels-idx1-ubyte.gz
```

Then, from the project root:

```bash
python train.py          # run the hyperparameter experiments, write results.json
python plot_results.py   # draw the figures in figures/
python evaluate.py       # train the final model, report test accuracy, save the weights
pytest                   # run the unit tests and the gradient check
```

## License

MIT