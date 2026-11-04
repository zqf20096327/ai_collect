# TinyRL: Real-Time Deep RL That Fits in Small Devices

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-blue.svg)](https://en.cppreference.com/w/cpp/17)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Docs](https://img.shields.io/badge/docs-latest-brightgreen)](https://mohmdelsayed.github.io/TinyRL/)
[![Header-only](https://img.shields.io/badge/header--only-yes-green)](https://github.com/mohmdelsayed/TinyRL)

<p align="center">
  <img src="assets/esp32s3.jpg" alt="ESP32-S3 board running TinyRL" width="50%" style="max-width: 640px">
</p>
<p align="center"><em>Real-time reinforcement learning on the ESP32-S3 microcontroller.</em></p>

**TinyRL** is a lightweight, header-only C++ deep learning framework designed for real-time reinforcement learning on microcontrollers and embedded systems.

### Core Components

| Component | Description |
|-----------|-------------|
| **Autograd Core** | Tensors, reverse-mode automatic differentiation, neural network layers, and optimizers |
| **Stream-X** | Streaming deep RL algorithms: StreamAC (Actor-Critic), StreamQ (Q-learning with discrete/Atari variants), and StreamSARSA |

---
## 🗂️ Project Structure

```
TinyRL/
├── src/                       # Core C++ headers (autograd, layers, optimizer)
├── examples/
│   ├── cpp/                   # C++ examples (MLP, CNN, operations)
│   ├── python/                # Python examples (MNIST, CIFAR-10, spiral)
│   ├── stream_x/              # Streaming deep RL (StreamAC, StreamQ, StreamSARSA)
│   └── stream_x_esp32/        # ESP32 embedded RL example
├── bindings/                  # pybind11 Python bindings
├── tests/                     # Comprehensive test suite
├── docs/                      # MkDocs documentation
└── website/                   # Landing page
```

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🔧 **Header-only** | Zero dependencies—just include and compile |
| 🚀 **Autograd** | Reverse-mode automatic differentiation with dynamic graphs |
| 🧠 **Neural Networks** | Linear, Conv2D, LayerNorm, ReLU, Tanh, Softmax, and more |
| 📊 **N-D Tensors** | 2D and 4D tensor operations with broadcasting |
| 🐍 **Python Bindings** | Full pybind11 interface for rapid prototyping |
| 🎯 **Optimizers** | SGD, RMSProp, and ObGD (Stream-X) |
| ⚡ **SIMD Acceleration** | Vectorized operations for SSE/NEON |
| 🛡️ **Error Handling** | Comprehensive validation with descriptive messages |
| 🧪 **Well-tested** | Extensive test suite with gradient checking |
| 🪶 **Embedded Ready** | Runs on ESP32-S3 with minimal memory footprint |

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [Installation](#-installation)
3. [Basic Usage](#-basic-usage)
4. [Core Components](#core-components)
5. [Examples](#-examples)
6. [Building from Source](#-building-from-source)
7. [Numeric Precision](#numeric-precision)
8. [Streaming RL](#reinforcement-learning)
9. [Embedded / ESP32-S3](#embedded-esp32-s3)
10. [Documentation](#-documentation)
11. [Contributing](#-contributing)
12. [License](#-license)

## 🚀 Quick Start

### Prerequisites

- **C++17** compatible compiler (GCC 13+, Clang 16+, or recent MSVC)
- **CMake 3.14+**
- **Python 3.8+** (for Python bindings)
- **pybind11** (for Python bindings)

### Installation

#### Option 1: Header-only Library (Recommended)
```bash
git clone https://github.com/mohmdelsayed/TinyRL.git
cd TinyRL
```

Include the headers in your project:
```cpp
#include "autograd.h"
#include "layers.h"
#include "optimizer.h"
```

#### Option 2: CMake Integration
```bash
# Build and install TinyRL
mkdir build && cd build
cmake .. -DAUTOGRAD_BUILD_EXAMPLES=ON -DAUTOGRAD_BUILD_TESTS=ON
cmake --build . --target install -j

# In your project's CMakeLists.txt
find_package(AutoGrad REQUIRED)
target_link_libraries(your_target PRIVATE AutoGrad::autograd)
```

#### Option 3: Python Bindings
```bash
# Build from source (no PyPI release yet)
./install.sh --with-bindings

# Or manual build
cd bindings && mkdir build && cd build
cmake .. && cmake --build . -j
```

## 💻 Basic Usage

### C++ Example
```cpp
#include "autograd.h"
#include "layers.h"
#include "module.h"
#include "optimizer.h"

int main() {
    ag::manual_seed(42);

    nn::Sequential model;
    model.add(nn::Linear(10, 5));
    ag::SGD optimizer(0.01f);
    optimizer.add_parameters(model.layers());

    // Random input (batch 32 x features 10) 
    // and dummy target (batch 32 x 5 to match output)
    int batch_size = 32;
    ag::Tensor x(ag::Matrix::Random(batch_size, 10), true, "x");
    ag::Tensor y(ag::Matrix::Random(batch_size, 5), false, "y");

    ag::Tensor out = model.forward(x);
    ag::Tensor loss = ag::sum(ag::pow(out - y, 2.0f)) / batch_size;
    optimizer.zero_grad();
    loss.backward();
    optimizer.step();
    return 0;
}
```

### Python Example
```python
import autograd
import numpy as np

# Create tensors
x = autograd.Tensor(np.random.rand(32, 10), requires_grad=True)
y = autograd.Tensor(np.random.rand(32, 1), requires_grad=False)

# Build model
model = autograd.Sequential()
model.add(autograd.Linear(10, 1))
opt = autograd.SGD(0.01)
opt.add_parameters(model.layers())

# Forward/backward
out = model.forward(x)
loss = autograd.sum(autograd.pow(out - y, 2.0))
opt.zero_grad()
loss.backward()
opt.step()
```

---

## 🧩 Core Components

### 1. Tensor Operations (`matrix.h`)
- N-dimensional tensor support with bounds checking
- Basic arithmetic operations with broadcasting
- Matrix operations (matmul, transpose)
- Element-wise operations with SIMD optimization
- Convolution operations

### 2. Automatic Differentiation (`autograd.h`)
- Reverse-mode automatic differentiation
- Dynamic computational graph construction
- Gradient computation and memory management
- Graph visualization tools
- Enhanced error handling and validation

### 3. Neural Network Layers (`layers.h`)
- **Linear (Dense) layers**
- **Convolutional layers** (Conv2D)
- **Activation functions** (ReLU, LeakyReLU, Tanh, Softmax, Softplus)
- **Normalization layers** (LayerNorm) with efficient fused operations
- **Sequential model** support

### 4. Optimizers (`optimizer.h`)
- **SGD** (Stochastic Gradient Descent)
- **RMSProp** (Root Mean Square Propagation with adaptive learning rates)
- **ObGD** (Overshooting-bounded Gradient Descent) for streaming deep RL

### 5. Utilities
- Random number generation (`rng.h`)
- Computational graph visualization (`draw_graph.h`)
- Weight initialization (`initialize.h`) with LeCun and sparse methods
- Lightweight logging macro (`log.h`) via `AG_LOG` (printf on embedded)
- Build scripts and comprehensive test suites
- Python bindings

---

## 📚 Examples

### C++ Examples
```bash
cd examples/cpp
mkdir build && cd build
cmake .. && make
./minimal_operations
./minimal_network_mlp
./minimal_network_cnn
```

### Python Examples
```bash
cd bindings && mkdir build && cd build
cmake .. && make
cd ../../examples/python
python minimal_operations.py
python full_training_mnist.py
```

### Available Examples
- **Basic Operations**: Tensor creation, arithmetic, and gradients
- **MLP Training**: Multi-layer perceptron with MNIST
- **CNN Training**: Convolutional networks with CIFAR-10
- **Reinforcement Learning**: Stream-X examples (StreamAC algorithm in continuous/discrete variants, StreamQ algorithm, StreamSARSA algorithm for discrete actions)

---

## 🔧 Building from Source

### Quick Build
```bash
./install.sh
```

### Custom Build Options
```bash
mkdir build && cd build
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DAUTOGRAD_BUILD_EXAMPLES=ON \
    -DAUTOGRAD_BUILD_TESTS=ON \
    -DAUTOGRAD_BUILD_BINDINGS=OFF
make -j$(nproc)
```

### Build Options
| Option | Description | Default |
|--------|-------------|---------|
| `AUTOGRAD_BUILD_EXAMPLES` | Build example programs | ON |
| `AUTOGRAD_BUILD_TESTS` | Build test suite | ON |
| `AUTOGRAD_BUILD_BINDINGS` | Build Python bindings | OFF |
| `AUTOGRAD_BUILD_STREAM_X` | Build Stream-X RL module | OFF |
| `AUTOGRAD_ENABLE_SIMD` | Enable SIMD optimizations | ON |
| `AUTOGRAD_EMBEDDED` | Enable embedded-friendly mode (defines `AG_EMBEDDED`) | OFF |
| `AUTOGRAD_FAST_MATH` | Enable `-ffast-math` in Release builds | ON |
| `AUTOGRAD_USE_DOUBLE` | Use double precision (`AG_USE_DOUBLE`) | OFF |

---

## 🔢 Numeric Precision

TinyRL uses **float32** (`Float` type) by default for all computations, providing optimal balance of performance and memory efficiency for embedded systems and real-time applications.

To use **float64** (double precision), define `AG_USE_DOUBLE` before including TinyRL headers:
```cpp
#define AG_USE_DOUBLE
#include "autograd.h"
```

Or via CMake:
```bash
cmake .. -DAUTOGRAD_USE_DOUBLE=ON
```

Or via the install script:
```bash
./install.sh --use-double
```

---

## 🎯 Reinforcement Learning

The Stream-X module lives in `examples/stream_x` and includes the StreamAC algorithm (continuous and discrete Actor‑Critic variants), the StreamQ algorithm (discrete Q‑learning), and the StreamSARSA algorithm (on-policy discrete TD learning).

### Build Stream‑X
```bash
./install.sh --with-stream-x
```

Or directly via CMake: `-DAUTOGRAD_BUILD_STREAM_X=ON`.

### Usage Examples

- StreamAC algorithm — Continuous actions
```cpp
#include "stream_x/stream_ac_continuous.h"
int obs_dim = 11;
int act_dim = 1;
int hidden = 128;

ContinuousStreamAC ac_cont(obs_dim, 1.0f, 0.99f, 0.8f, 2.0f, 2.0f);

nn::Sequential actor_backbone;
actor_backbone.add(nn::Linear(obs_dim, hidden));
actor_backbone.add(nn::ReLU());

nn::Sequential mu_head;
mu_head.add(nn::Linear(hidden, act_dim));

nn::Sequential std_head;
std_head.add(nn::Linear(hidden, act_dim));
std_head.add(nn::Softplus());

nn::Sequential critic;
critic.add(nn::Linear(obs_dim, hidden));
critic.add(nn::ReLU());
critic.add(nn::Linear(hidden, 1));

ac_cont.set_model(actor_backbone, mu_head, std_head, critic);

ag::Matrix norm_s = ac_cont.normalize_observation(state);
ag::Matrix norm_sn = ac_cont.normalize_observation(next_state);
ag::Tensor s(norm_s, false);
ag::Tensor sn(norm_sn, false);
ag::Tensor a_cont = ac_cont.sample_action(s);
ag::Float scaled_r = ac_cont.scale_reward(reward, done);
ag::Tensor r(ag::Matrix::Constant(1, 1, scaled_r), false);
ac_cont.update(s, a_cont, r, sn, done);
```

- StreamAC algorithm — Discrete actions
```cpp
#include "stream_x/stream_ac_discrete.h"
int obs_dim = 11;
int n_actions = 2;
int hidden = 128;

DiscreteStreamAC ac_disc(obs_dim, n_actions, 1.0f, 0.99f, 0.8f, 2.0f, 2.0f);

nn::Sequential actor;
actor.add(nn::Linear(obs_dim, hidden));
actor.add(nn::ReLU());
actor.add(nn::Linear(hidden, n_actions));
actor.add(nn::Softmax());

nn::Sequential critic;
critic.add(nn::Linear(obs_dim, hidden));
critic.add(nn::ReLU());
critic.add(nn::Linear(hidden, 1));

ac_disc.set_model(actor, critic);

ag::Matrix norm_s = ac_disc.normalize_observation(state);
ag::Matrix norm_sn = ac_disc.normalize_observation(next_state);
ag::Tensor s(norm_s, false);
ag::Tensor sn(norm_sn, false);
ag::Tensor a_idx = ac_disc.sample_action(s);  // action index (scalar tensor)
ag::Float scaled_r = ac_disc.scale_reward(reward, done);
ag::Tensor r(ag::Matrix::Constant(1, 1, scaled_r), false);
ac_disc.update(s, a_idx, r, sn, done);
```

- StreamQ algorithm — Discrete Q-learning
```cpp
#include "stream_x/stream_q.h"

// Define a simple Q network (1xA output)
nn::Sequential qnet;
qnet.add(nn::Linear(11, 64));
qnet.add(nn::ReLU());
qnet.add(nn::Linear(64, 2));

StreamQ q_agent(/*n_obs=*/11, /*n_actions=*/2, /*lr=*/1.0f, /*gamma=*/0.99f,
                        /*lambda=*/0.8f, /*kappa=*/2.0f);
q_agent.set_model(qnet);

ag::Matrix norm_s = q_agent.normalize_observation(state);
ag::Matrix norm_sn = q_agent.normalize_observation(next_state);
ag::Tensor s(norm_s, false);
ag::Tensor sn(norm_sn, false);
auto [act, is_nongreedy] = q_agent.sample_action(s);
ag::Float scaled_r = q_agent.scale_reward(reward, done);
q_agent.update(s, act, scaled_r, sn, done, is_nongreedy);
```

---

## 🛠️ Embedded / ESP32-S3

An on-device reinforcement learning example is provided in `examples/stream_x_esp32/` using PlatformIO/Arduino.

### Features
- Header-only integration (no dynamic library needed)
- Compile with: `-DAG_EMBEDDED -DAG_ENABLE_SIMD=OFF`
- Replaces iostream logging with `printf` via `AG_LOG`
- Manual unrolled math loops for Xtensa
 - Enable via CMake: `-DAUTOGRAD_EMBEDDED=ON` (adds `AG_EMBEDDED` define automatically)

### Quick Host Simulation
```bash
c++ -std=c++17 -DAG_EMBEDDED \
    -I src -I examples/stream_x/src \
  examples/stream_x_esp32/src/stream_ac_continuous.cpp -o esp32_sim
./esp32_sim
```

### PlatformIO Setup
```bash
cd examples/stream_x_esp32
platformio run --target upload
platformio device monitor
```

For detailed instructions, see `examples/stream_x_esp32/README.md`.

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Quick test (standalone)
cd tests
sh compile_tests.sh && sh run_tests.sh

# Full project test with new build system
./install.sh --build-type Debug

# Run specific test categories
cd build
./test_error_handling    # Error handling validation
./test_operations        # Basic operations
./test_mlps             # Neural network tests
./test_cnns             # Convolutional network tests
```

### Test Coverage
- **Error Handling**: Comprehensive validation of all error conditions
- **Functionality**: Complete testing of all features and optimizers
- **Edge Cases**: Boundary conditions and error state testing

---

## 📖 Documentation

Visit the project documentation: **https://mohmdelsayed.github.io/TinyRL/**

The documentation includes:
- 📋 **API Reference**: Complete class and method documentation
- 📚 **Tutorials**: Step-by-step guides
- 💡 **Examples**: Practical code examples
- 🛠️ **Installation Guide**: Setup instructions
- 🧠 **Architecture Overview**: System design and components

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Setup
```bash
git clone https://github.com/mohmdelsayed/TinyRL.git
cd TinyRL
./install.sh --build-type Debug --with-bindings
# Make your changes
cd build && ctest  # Run tests
```

---

## 📖 Citation

If you use TinyRL in your research, please cite:

```bibtex
@software{TinyRL2026,
  author       = {Elsayed, Mohamed},
  title        = {{TinyRL: Real-Time Deep RL That Fits in Small Devices}},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/mohmdelsayed/TinyRL},
}
```

---

## 📝 License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- TinyRL's autograd design is inspired by TinyGrad/PyTorch's automatic differentiation systems
- Stream-X algorithms are based on [Streaming Deep Reinforcement Learning](https://arxiv.org/abs/2410.14606)
- We thank Khurram Javed, Adrian Orenstein, and Kris De Asis for testing an early version of the library and for providing helpful feedback.