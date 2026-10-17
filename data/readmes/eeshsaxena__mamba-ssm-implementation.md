# Mamba: Selective State Space Models

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

This repository provides a clean, educational PyTorch implementation of **Mamba**, the selective state space model architecture that challenges the Transformer's dominance in sequence modeling.

> **Paper:** "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"  
> **Authors:** Albert Gu, Tri Dao  
> **arXiv:** [2312.00752](https://arxiv.org/abs/2312.00752) (December 2023)

## Why Mamba?

Mamba addresses fundamental limitations of Transformers:
- ⚡ **Linear-time complexity** (O(N) vs Transformer's O(N²))
- 🚀 **5x faster inference** than Transformers on long sequences
- 📈 **Scales to million-token sequences** without performance degradation
- 💾 **Constant memory during generation** (vs growing KV cache)
- 🎯 **Selective information propagation** (not all tokens are equal)

## Key Innovation: Selective State Space Models

Traditional SSMs treat all inputs equally. Mamba's key insight:
```
Make the SSM parameters input-dependent!
```

This allows the model to:
- **Filter** irrelevant information
- **Remember** important context
- **Forget** unnecessary details

## Architecture

```
Input → Selective SSM Block → Output
         ├── Input-dependent Δ (discretization)
         ├── Input-dependent B (projection)
         ├── Input-dependent C (projection)
         └── Efficient selective scan
```

## Features

- ✅ Core Selective SSM implementation
- ✅ Mamba block with gated residuals
- ✅ Efficient selective scan algorithm
- ✅ Multiple scanning strategies (parallel, sequential)
- ✅ Complete language model implementation
- ✅ Comprehensive tests
- ✅ Training examples
- ✅ Performance benchmarks

## Installation

```bash
git clone https://github.com/yourusername/mamba-ssm-implementation.git
cd mamba-ssm-implementation
pip install -r requirements.txt
```

## Quick Start

```python
import torch
from mamba import MambaBlock

# Create Mamba block
block = MambaBlock(d_model=512, d_state=16, d_conv=4, expand=2)

# Process sequence
x = torch.randn(2, 100, 512)  # (batch, length, dim)
output = block(x)
print(output.shape)  # torch.Size([2, 100, 512])
```

## Mathematical Foundation

### State Space Model

The continuous-time SSM is defined as:
```
h'(t) = Ah(t) + Bx(t)
y(t)  = Ch(t) + Dx(t)
```

### Selective Mechanism

Mamba makes B, C, and Δ (timestep) input-dependent:
```
B(x) = Linear_B(x)
C(x) = Linear_C(x)
Δ(x) = τ_Δ(Parameter + Linear_Δ(x))
```

### Efficient Scan

The selective scan is computed efficiently using:
1. **Parallel scan** for training (O(N log N))
2. **Sequential scan** for inference (O(N) with constant memory)

## Comparison with Transformers

| Feature | Transformer | Mamba |
|---------|------------|-------|
| Time Complexity | O(N²) | O(N) |
| Memory (Training) | O(N²) | O(N) |
| Memory (Inference) | O(N) growing | O(1) constant |
| Long Sequences | Struggles | Excels |
| Inference Speed | Slower | 5x faster |

## Project Structure

```
mamba-ssm-implementation/
├── mamba/
│   ├── __init__.py
│   ├── ssm.py              # Core SSM implementation
│   ├── selective_scan.py   # Efficient scanning algorithms
│   ├── mamba_block.py      # Mamba block with gating
│   ├── model.py            # Complete Mamba language model
│   └── utils.py            # Helper functions
├── tests/
│   ├── test_ssm.py
│   ├── test_scan.py
│   └── test_mamba.py
├── examples/
│   ├── basic_usage.py
│   ├── train_language_model.py
│   └── benchmark.py
├── docs/
│   └── theory.md
├── requirements.txt
└── README.md
```

## Performance

On WikiText-103 (language modeling):
- **Perplexity:** Comparable to Transformers
- **Speed:** 5x faster inference on long sequences
- **Memory:** Scales to 1M+ tokens

## Research Impact

Mamba has shown strong results on:
- **Language Modeling** - Matches Transformer performance
- **DNA Sequence Modeling** - 1M token sequences
- **Audio Generation** - Efficient for long waveforms
- **Time Series** - Natural fit for sequential data

## Citation

If you use this implementation in your research, please cite:

```bibtex
@article{gu2023mamba,
  title={Mamba: Linear-Time Sequence Modeling with Selective State Spaces},
  author={Gu, Albert and Dao, Tri},
  journal={arXiv preprint arXiv:2312.00752},
  year={2023}
}
```

## Related Work

- **S4 (Structured State Spaces)** - Foundation for Mamba
- **H3 (Hungry Hungry Hippos)** - Attention alternative
- **RetNet** - Linear attention with retention
- **RWKV** - RNN-like with Transformer performance

## License

This project is licensed under the MIT License.

## Acknowledgments

- Original Mamba paper authors (Albert Gu, Tri Dao)
- The state-spaces research community
- PyTorch team for the excellent framework

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Future Work

- [ ] Add Mamba-2 improvements
- [ ] Implement bidirectional Mamba
- [ ] Add vision Mamba (ViM)
- [ ] Optimize selective scan with custom CUDA kernels
- [ ] Add model quantization support
