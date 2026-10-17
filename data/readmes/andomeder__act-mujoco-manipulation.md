# Action Chunking Transformers for Robot Manipulation

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

End-to-end implementation of **Action Chunking Transformers (ACT)** for imitation learning in robot manipulation tasks. Trained and evaluated in MuJoCo simulation on a pick-and-place task using the ROBOTIS FFW humanoid robot.

## Overview

This project demonstrates imitation learning for robotic manipulation using the **Action Chunking Transformer (ACT)** architecture. ACT predicts sequences of future actions (action chunks) using a conditional VAE with transformer encoders/decoders, resulting in smoother and more stable trajectories than single-step prediction methods.

### Key Features

- ✅ **Full ACT implementation** from scratch in PyTorch
- ✅ **MuJoCo simulation** with ROBOTIS FFW humanoid robot
- ✅ **Multi-GPU support** (NVIDIA CUDA, Intel Arc XPU, AMD ROCm)
- ✅ **Clean, documented codebase** with Hydra configuration
- ✅ **Evaluation pipeline** with video generation
- ✅ **WandB integration** for experiment tracking

## Architecture

```
Input Observation
├── RGB Image [3, 224, 224]
└── Robot State [15] (joint positions + velocities + gripper)
         ↓
    Vision Encoder (ResNet-18)
         ↓
    State Encoder (MLP)
         ↓
    Transformer Encoder
         ↓
    Conditional VAE
    ├── Encoder: q(z|obs, actions)
    └── Decoder: p(actions|obs, z)
         ↓
    Transformer Decoder
         ↓
Output: Action Chunk [100, 8]
(100 future actions, 8-DOF: 7 arm joints + gripper)
```

### Why ACT?

| Feature                   | ACT          | Behavior Cloning | Diffusion Policy |
| ------------------------- | ------------ | ---------------- | ---------------- |
| **Trajectory Smoothness** | ✅ Excellent | ❌ Jerky         | ✅ Excellent     |
| **Training Speed**        | ✅ Fast      | ✅ Fast          | ⚠️ Slow          |
| **Inference Speed**       | ✅ 30Hz      | ✅ 30Hz          | ⚠️ 5-10Hz        |
| **Multimodal Actions**    | ✅ Yes (VAE) | ❌ No            | ✅ Yes           |
| **Implementation**        | ⚠️ Medium    | ✅ Simple        | ❌ Complex       |

ACT offers the best balance of performance, speed, and implementation complexity for real-time robot control.

## Installation

### Prerequisites

- Python 3.12
- [mise](https://mise.jdx.dev/) (recommended for version management)
- GPU: NVIDIA, Intel Arc, or AMD (optional, will use CPU if not available)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/andomeder/act-mujoco-manipulation.git
cd act-mujoco-manipulation

# Install mise and Python
make setup-mise

# Install dependencies (auto-detects GPU)
make install

# Setup environment
make setup-env
```

### Manual Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements/base.txt

# Install GPU-specific dependencies
pip install -r requirements/intel.txt    # For Intel Arc
pip install -r requirements/nvidia.txt   # For NVIDIA
pip install -r requirements/amd.txt      # For AMD ROCm
```

## Usage

### 1. Data Collection

Collect demonstration data using terminal-based teleoperation:

```bash
make collect-data
```

**Controls:**

- `W/A/S/D/Q/E`: Arm movement (shoulder/elbow)
- `R/F/T/Y/U/I/O/P`: Wrist and gripper positioning
- `G`: Close gripper | `H`: Open gripper
- `J/K`: Torso lift down/up
- `X`: Save episode | `Z`: Reset episode

**Target:** Collect 10-50 episodes (6,000+ frames recommended)

### 2. Training

Train the ACT policy:

```bash
make train
```

Training will:

- Load collected demonstrations
- Train for 2,000 epochs (~3-4 hours on Intel Arc)
- Save checkpoints every 200 epochs
- Log to WandB (if enabled)

**Monitor training:**

```bash
make monitor  # Opens WandB dashboard
```

### 3. Evaluation

Evaluate trained policy and generate videos:

```bash
make eval
```

This will:

- Run 10 evaluation episodes
- Compute success rate
- Generate MP4 videos in `outputs/videos/`

## Project Structure

```
act-mujoco-manipulation/
├── src/
│   ├── policies/
│   │   └── act.py              # ACT policy implementation
│   ├── train_act.py            # Training script
│   ├── eval.py                 # Evaluation script
│   ├── collect_data.py         # Data collection interface
│   ├── envs/                   # MuJoCo environment
│   │   └── assets/             # Robot meshes and XML
│   └── utils/
│       └── gpu_utils.py        # Multi-GPU support
├── configs/
│   ├── config.yaml             # Main configuration
│   └── policy/
│       └── act.yaml            # ACT hyperparameters
├── datasets/                   # Collected demonstrations
├── outputs/                    # Checkpoints and videos
├── requirements/               # Dependencies
├── Makefile                    # Development automation
└── README.md
```

## Configuration

Key hyperparameters in `configs/policy/act.yaml`:

```yaml
# Action chunking
chunk_size: 100 # Number of future actions to predict

# Architecture
hidden_dim: 512 # Transformer hidden dimension
latent_dim: 32 # VAE latent dimension
num_encoder_layers: 4 # Transformer encoder depth
num_decoder_layers: 7 # Transformer decoder depth

# Training
batch_size: 8 # Small batches work well for ACT
lr: 1.0e-5 # Learning rate
kl_weight: 10.0 # KL divergence weight in CVAE loss
```

## Technical Details

### Conditional VAE (CVAE)

ACT uses a CVAE to handle multimodal action distributions:

**Training:**

```python
# Encoder: q(z|observation, actions)
mu, logvar = cvae_encoder(obs, actions)
z = reparameterize(mu, logvar)

# Decoder: p(actions|observation, z)
pred_actions = cvae_decoder(obs, z)

# Loss
recon_loss = MSE(pred_actions, actions)
kl_loss = KL(q(z|obs,a) || N(0,1))
total_loss = recon_loss + beta * kl_loss
```

**Inference:**

```python
# Sample from prior
z ~ N(0, 1)
actions = cvae_decoder(obs, z)
```

### Temporal Ensemble

During execution, predictions from multiple timesteps are averaged for smoother control:

```python
# At each step:
new_chunk = policy.predict(obs)
action_queue.append(new_chunk)
action = average(action_queue)  # Smooth blend
```

### Data Format

```python
{
    'observation.image': [3, 224, 224],   # RGB camera
    'observation.state': [15],             # Joint state
    'actions': [chunk_size, 8],            # Action chunk
}
```

## Multi-GPU Support

Automatically detects and configures GPU:

```bash
# Check GPU
make gpu-info

# Supported hardware:
# - NVIDIA (CUDA)
# - Intel Arc (XPU)
# - AMD (ROCm)
# - CPU (fallback)
```

## Development

```bash
# Format code
make format

# Run linting
make lint

# Run tests
make test

# Clean temporary files
make clean
```

## Citation

If you use this code, please cite the original ACT paper:

```bibtex
@inproceedings{zhao2023learning,
  title={Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware},
  author={Zhao, Tony Z. and Kumar, Vikash and Levine, Sergey and Finn, Chelsea},
  booktitle={Robotics: Science and Systems (RSS)},
  year={2023}
}
```

## Related Work

- **ACT Paper**: [arXiv:2304.13705](https://arxiv.org/abs/2304.13705)
- **Project Page**: <https://tonyzhaozh.github.io/aloha/>
- **ALOHA Hardware**: Low-cost bimanual manipulation platform
- **LeRobot**: Framework for robot learning in PyTorch

## Acknowledgments

- **Robot Assets**: ROBOTIS FFW from [robotis_mujoco_menagerie](https://github.com/ROBOTIS-GIT/robotis_mujoco_menagerie) (Apache 2.0)
- **ACT Implementation**: Based on the original paper by Zhao et al. (2023)
- **Framework**: Built with [LeRobot](https://github.com/huggingface/lerobot) and MuJoCo

## License

MIT License - see [LICENSE](LICENSE) for details.

Robot assets from ROBOTIS are licensed under Apache 2.0.

## Author

**William Obino**
Nairobi, Kenya
📧 <obinowilliam@staka.cc>
🔗 [GitHub](https://github.com/andomeder) | [LinkedIn](https://www.linkedin.com/in/williamobino/)
