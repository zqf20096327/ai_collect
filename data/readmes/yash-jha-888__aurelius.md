# Aurelius

Aurelius is a deep learning framework written in modern C++ from first principles.

I started this project to understand what happens underneath libraries like PyTorch instead of treating them as black boxes.

Every major building block is implemented manually, from the mathematics to the engineering, with the long-term goal of growing Aurelius into a complete deep learning framework.

One of the principles behind Aurelius is simple: every abstraction I use should be one I've implemented myself first.

Each major subsystem, including activations, weight initialization, loss functions, logging, and optimization, is designed as an independent abstraction that can be extended without modifying the rest of the framework.

---

## Features

### Neural networks
- Configurable fully connected architectures
- Forward propagation & backpropagation
- Activation functions: ReLU, Leaky ReLU
- Softmax output layer

### Training
- Mini-batch stochastic gradient descent (SGD)
- Cross-entropy loss
- Early stopping with patience
- Best-model checkpoint restoration
- Train / Validation evaluation
- Official MNIST test-set evaluation

### Framework architecture
- **Activation abstraction**: pluggable nonlinearities (`ReLU`, `LeakyReLU`)
- **Initializer abstraction**: Gaussian, `HeInitializer`, `XavierInitializer`, `LeCunInitializer`
- **Optimizer abstraction**: extensible optimizer interface (`SGD`)
- **Modular layer design**: decoupled layer forward/backward passes
- **Timestamped experiment logging**: per-run isolated artifact directories
- **CSV training metrics**: epoch-by-epoch loss, accuracy, learning rate, and timings
- **JSON sidecar run configs**: fully reproducible experiment metadata
- **Static metric visualization**: dark-themed Matplotlib + Seaborn plotting engine

### Data
- IDX dataset parser for MNIST binary format
- Official MNIST train/test split (60k train / 10k test)
- Dataset shuffling & deterministic seeding
- Configurable train/validation split

---

## Architecture

Aurelius separates each major training component behind a common interface:

- **Activation functions** (`Activation.h` / `Activation.cpp`)
- **Weight initializers** (`Initializer.h` / `Initializer.cpp`)
- **Optimizers** (`Optimizer.h` / `Optimizer.cpp`)
- **Loss functions** (`Loss.h` / `Loss.cpp`)
- **Layers** (`DenseLayer.h` / `DenseLayer.cpp`)
- **Experiment Logger** (`Logger.h` / `Logger.cpp`)

This design allows components to be swapped independently while keeping the core training pipeline unchanged.

---

## Results & Visualizations

Current benchmark on MNIST:

| Metric | Value |
|--------|------:|
| Architecture | 784 → 128 → 64 → 10 |
| Optimizer | SGD |
| Activation | LeakyReLU |
| Initializer | He |
| Batch Size | 64 |
| Learning Rate | 0.1 |
| Test Accuracy | 97.82% |

### Loss Curves (Train vs. Validation)
Tracks loss trajectories across training epochs, illustrating convergence and the overfitting threshold where early stopping checkpoints the optimal model state:

![Loss Curves](assets/loss_curve.png)

### Accuracy Curves (Train vs. Validation)
Displays learning progress and peak validation accuracy:

![Accuracy Curves](assets/accuracy_curve.png)

### Multi-Run Comparison
Overlays arbitrary $N$ runs on a single axis using metadata from JSON sidecars to highlight convergence-speed deltas (e.g. He initialization vs. alternative initializations):

![Multi-Run Overlay](assets/multi_run_overlay.png)

---

## Project Structure

```
Aurelius/
│
├── include/
│   ├── Activation.h
│   ├── Dataset.h
│   ├── DenseLayer.h
│   ├── Initializer.h
│   ├── Logger.h
│   ├── Loss.h
│   ├── Model.h
│   ├── Optimizer.h
│   └── RunConfig.h
│
├── src/
│   ├── Activation.cpp
│   ├── Dataset.cpp
│   ├── DenseLayer.cpp
│   ├── Initializer.cpp
│   ├── Logger.cpp
│   ├── Loss.cpp
│   ├── Model.cpp
│   ├── Optimizer.cpp
│   └── main.cpp
│
├── data/
│   └── mnist/
│
├── logs/
│   └── <timestamp>/
│       ├── metrics.csv
│       └── run_config.json
│
├── assets/
│   ├── loss_curve.png
│   ├── accuracy_curve.png
│   ├── multi_run_overlay.png
│   └── multi_run_accuracy.png
│
├── scripts/
│   └── plot.py
│
├── .gitignore
├── CMakeLists.txt
├── LICENSE
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Build & Run C++ Engine

```bash
mkdir build
cd build

cmake ..
cmake --build .

# Run training
./Aurelius
```

### 2. Generate Metric Visualizations

The Python plotting script reads the output CSV and JSON sidecars from `logs/` and generates static, dark-themed PNGs in `assets/`:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Automatically detect latest run and generate all plots
python scripts/plot.py

# Plot a specific run
python scripts/plot.py logs/20260813_141514

# Compare multiple specific runs
python scripts/plot.py logs/run1 logs/run2 --output-dir assets/
```

---

## Roadmap

### v0.3
- [x] Optimizer abstraction
- [x] JSON experiment metadata sidecars
- [x] Training metric visualization pipeline
- [ ] L2 regularization
- [ ] Dropout

### v0.4
- [ ] Automatic differentiation
- [ ] Convolutional layers
- [ ] Batch normalization
- [ ] Model serialization

### v0.5
- [ ] Tensor library
- [ ] CUDA backend
- [ ] Transformer implementation
