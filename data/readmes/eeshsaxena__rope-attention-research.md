# Rotary Position Embedding (RoPE) Attention Implementation

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

## Overview

This repository provides a clean, well-documented implementation of **Rotary Position Embeddings (RoPE)** integrated with Multi-Head Attention, based on the research paper:

> **"RoFormer: Enhanced Transformer with Rotary Position Embedding"**  
> Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu  
> arXiv:2104.09864 (2021)

RoPE has become a fundamental component in modern large language models including LLaMA, PaLM, and GPT-NeoX due to its superior extrapolation capabilities and relative position encoding properties.

## Key Features

- ✅ Pure PyTorch implementation of RoPE
- ✅ Multi-Head Attention with RoPE integration
- ✅ Supports variable sequence lengths
- ✅ Efficient computation using complex number representations
- ✅ Comprehensive unit tests
- ✅ Visualization tools for position embeddings
- ✅ Performance benchmarks

## Mathematical Background

RoPE encodes absolute position information with a rotation matrix and incorporates explicit relative position dependency in self-attention formulation. The key innovation is applying a rotation to query and key vectors based on their absolute positions:

```
f_q(x_m, m) = (W_q * x_m) * e^(imθ)
f_k(x_n, n) = (W_k * x_n) * e^(inθ)
```

Where the rotation angle θ varies across dimensions, enabling the model to capture both local and long-range dependencies.

## Installation

```bash
git clone https://github.com/yourusername/rope-attention-research.git
cd rope-attention-research
pip install -r requirements.txt
```

## Quick Start

```python
import torch
from rope_attention import RoPEAttention

# Initialize RoPE attention layer
attention = RoPEAttention(
    d_model=512,
    n_heads=8,
    dropout=0.1
)

# Sample input (batch_size=2, seq_len=10, d_model=512)
x = torch.randn(2, 10, 512)

# Forward pass
output = attention(x)
print(output.shape)  # torch.Size([2, 10, 512])
```

## Project Structure

```
rope-attention-research/
├── rope_attention/
│   ├── __init__.py
│   ├── rope.py              # Core RoPE implementation
│   ├── attention.py         # Multi-head attention with RoPE
│   └── utils.py             # Helper functions
├── tests/
│   ├── test_rope.py
│   └── test_attention.py
├── examples/
│   ├── basic_usage.py
│   ├── visualization.py
│   └── benchmark.py
├── docs/
│   └── theory.md
├── requirements.txt
├── setup.py
└── README.md
```

## Research Paper Reference

This implementation is based on the RoFormer paper which introduced rotary position embeddings as an alternative to traditional absolute or relative position encoding methods. The key advantages include:

1. **Better Extrapolation**: Can handle sequences longer than training length
2. **Relative Position Encoding**: Naturally encodes relative positions in attention
3. **Efficiency**: No additional parameters beyond standard attention
4. **Theoretical Soundness**: Grounded in principles of rotational invariance

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Citation

If you use this implementation in your research, please cite:

```bibtex
@article{su2021roformer,
  title={RoFormer: Enhanced Transformer with Rotary Position Embedding},
  author={Su, Jianlin and Lu, Yu and Pan, Shengfeng and Murtadha, Ahmed and Wen, Bo and Liu, Yunfeng},
  journal={arXiv preprint arXiv:2104.09864},
  year={2021}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original RoFormer paper authors
- PyTorch team for the excellent deep learning framework
- Open source community for feedback and contributions
