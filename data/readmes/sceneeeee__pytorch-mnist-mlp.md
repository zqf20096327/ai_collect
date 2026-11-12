# PyTorch MNIST Classifier

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch 2.x](https://img.shields.io/badge/PyTorch-2.x-ee4c2c)
![CPU](https://img.shields.io/badge/Device-CPU-green)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A beginner PyTorch project that trains a small multilayer perceptron (MLP) to classify handwritten digits from the MNIST dataset.

## Project Structure

```text
model.py         Defines the MLP model
inspect_data.py  Downloads and inspects MNIST samples and batches
train.py         Trains, tests, and saves the model parameters
evaluate.py      Loads the saved model, tests it, and displays a prediction
requirements.txt Lists the Python dependencies
assets/prediction_example.png  Example model prediction image
data/            Downloaded MNIST data (created automatically)
checkpoints/     Saved model parameters (created by train.py)
LICENSE          MIT License text
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

For a CPU-only PyTorch installation, use:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Then install the remaining project dependencies:

```bash
pip install matplotlib numpy
```

Alternatively, install all dependencies from the requirements file with `pip install -r requirements.txt`.

## Model

MNIST images arrive in batches with shape `[batch, 1, 28, 28]`. The network consists of:

```text
[batch, 1, 28, 28]
  -> Flatten              [batch, 784]
  -> Linear(784, 128)     [batch, 128]
  -> ReLU                 [batch, 128]
  -> Linear(128, 10)      [batch, 10]
```

The 10 output values are **logits**, or unnormalized class scores. The class with the largest logit is the prediction. `CrossEntropyLoss` compares these logits with the correct digit labels; it applies the required probability calculation internally, so the model does not include a softmax layer. SGD updates the model parameters using the gradients produced by backpropagation.

## Usage

Inspect the dataset and display a sample:

```bash
python inspect_data.py
```

Train for five epochs, evaluate on the test set, and save a checkpoint:

```bash
python train.py
```

Load the checkpoint, evaluate it, and display one prediction:

```bash
python evaluate.py
```

`model.train()` enables training behavior, while `model.eval()` switches the model to evaluation behavior. This model has no dropout or batch normalization, but using these modes is still the correct PyTorch pattern. `torch.no_grad()` disables gradient tracking during evaluation, reducing unnecessary work.

Training saves `model.state_dict()` to `checkpoints/mnist_mlp.pth`. A `state_dict` contains the learned parameter tensors. Evaluation creates the same `MNISTModel`, reads the checkpoint with `torch.load(..., map_location="cpu")`, and restores the parameters with `model.load_state_dict(...)`.

## Example Prediction

![MNIST prediction example](assets/prediction_example.png)

## Results

| Setting | Value |
| --- | --- |
| Epochs | 5 |
| Batch size | 32 |
| Optimizer | SGD |
| Learning rate | 0.01 |
| Final training accuracy | Approximately 92.6% |
| Test accuracy | Approximately 93% |

After five epochs, training accuracy is approximately **92.6%** and test accuracy is approximately **93%**, with minor variation between runs.

Results may vary slightly between runs because the model uses random parameter initialization and the training data is shuffled.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.
