## Quasimetric Attention

Implementation of Quasimetric Attention in PyTorch, where query-key dot product is replaced with a learned quasimetric distance function with symmetric and asymmetric components.

## Install

```shell
$ pip install quasimetric-attention
```

## Usage

```python
import torch
from quasimetric_attention import QuasimetricAttention

attn = QuasimetricAttention(
    dim = 512,
    dim_head = 64,
    heads = 8,
    prenorm = True
)

tokens = torch.randn(2, 1024, 512)

out = attn(tokens) + tokens
assert out.shape == tokens.shape
```

By default, `mask_self = True` blocks each token from attending to its own position, `null_sink = True` adds a learned null key (symmetric and asymmetric) and null value, prepended as a no-op sink that tokens can always attend to (which also prevents `nan` when every real key is masked), and `gate = True` applies a learned per-head sigmoid gate to the values. Each can be turned off.

```python
attn = QuasimetricAttention(
    dim = 512,
    dim_head = 64,
    heads = 8,
    mask_self = False,
    null_sink = False,
    gate = False,
    prenorm = True
)
```

You can also enable a straight-through estimator (STE) on the asymmetric distance function with a smooth softplus logsumexp backwards pass (with temperature) for dense gradient propagation across all coordinate dimensions:

```python
attn = QuasimetricAttention(
    dim = 512,
    dim_head = 64,
    asym_straight_through = True,
    asym_temperature = 0.5
)
```

## Citations

```bibtex
@misc{liu2023metricresidualnetworkssample,
    title   = {Metric Residual Networks for Sample Efficient Goal-Conditioned Reinforcement Learning},
    author  = {Bo Liu and Yihao Feng and Qiang Liu and Peter Stone},
    year    = {2023},
    eprint  = {2208.08133},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url     = {https://arxiv.org/abs/2208.08133},
}
```

```bibtex
@misc{zheng2026multistepquasimetriclearningscalable,
    title   = {Multistep Quasimetric Learning for Scalable Goal-conditioned Reinforcement Learning},
    author  = {Bill Chunyuan Zheng and Vivek Myers and Benjamin Eysenbach and Sergey Levine},
    year    = {2026},
    eprint  = {2511.07730},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url     = {https://arxiv.org/abs/2511.07730},
}
```

```bibtex
@misc{wang2022improvedrepresentationasymmetricaldistances,
    title   = {Improved Representation of Asymmetrical Distances with Interval Quasimetric Embeddings},
    author  = {Tongzhou Wang and Phillip Isola},
    year    = {2022},
    eprint  = {2211.15120},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url     = {https://arxiv.org/abs/2211.15120},
}
```
