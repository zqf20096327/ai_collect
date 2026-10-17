# Deep Learning Lectures

Educational deep learning notebooks — from first principles to frontier architectures.

Each module is a self-contained Jupyter notebook that builds intuition through code, math, and visualizations. No wrappers, no magic: raw PyTorch throughout.

## Roadmap

| # | Topic | Notebook | Status |
|---|-------|----------|--------|
| 1 | **Feed-Forward Neural Networks** | `feed_forward/` | planned |
| 2 | **Vision Transformer (ViT)** | [`vision_transformer/`](vision_transformer/vision_transformer.ipynb) | available |
| 3 | **Large Language Models** | [`large_language_model/`](large_language_model/gemma_Inference_samples.ipynb) | available |
| 4 | **Vision-Language Models (VLMs)** | `vlm/` | planned |
| 5 | **Flow Matching** | `flow_matching/` | planned |
| 6 | **World Models** | `world_models/` | planned |

## What's inside

**Vision Transformer** — Patch embedding, positional encoding, multi-head self-attention, forward pass mechanics, CIFAR-10 training, attention weight and positional embedding visualization.

**LLM Inference (Gemma 2B)** — Loading and running inference with Google's Gemma, exploring generation behavior on curated prompts.

## Setup

```bash
# requires Python ≥ 3.13
uv sync
```

## License

MIT
