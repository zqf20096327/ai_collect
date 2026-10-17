# Embedding Fingerprints

Given an embedding vector, identify which model produced it.

[Live Demo](https://embedding-inversion-demo.jina.ai) | [Blog Post](https://jina.ai/news/embedding-fingerprints)

> **See also:** [Embedding Inversion](https://github.com/jina-ai/embedding-inversion-demo) -- reconstruct original text from embedding vectors using conditional masked diffusion.

## How it works

Each float in the embedding is formatted as `%.4f`, then decomposed into
individual characters. A vocabulary of 15 tokens maps digits (0-9), minus
sign, decimal point, separator, CLS, and PAD. A CLS token is prepended to the
sequence, and a small transformer classifies the CLS output into one of N
embedding model classes.

This works because different models leave characteristic numerical patterns
in their output distributions -- digit frequencies, value ranges, and
positional correlations act as fingerprints.

## Quick start

Generate training data (requires GPU and embedding model weights):

```bash
pip install -e ".[generate]"
python generate.py --data texts.txt --output ./data/
```

Train:

```bash
pip install -e .
python train.py --data ./data/ --output ./checkpoints/
```

Plot training curves:

```bash
python plot.py --metrics checkpoints/train_metrics.jsonl --output ./plots/
```

## Architecture

| Parameter       | Value   |
|-----------------|---------|
| Vocab size      | 15      |
| Dimension       | 128     |
| Layers          | 4       |
| Heads           | 4       |
| FF hidden       | 344     |
| Total params    | ~800K   |
| Attention       | SDPA    |
| Position        | RoPE    |
| Normalization   | RMSNorm |
| FFN             | SwiGLU  |

Layer count is configurable via `--num-layers`. The default (4 layers, ~800K
params) is sufficient for the current class count. Training with 12 layers
(~2.4M params) gives marginally better accuracy on larger class sets.

## Tokenizer

```
"0.1234" -> [CLS, 0, 11, 1, 2, 3, 4]
"-0.5678 0.9012" -> [CLS, 10, 0, 11, 5, 6, 7, 8, 12, 0, 11, 9, 0, 1, 2]
```

Token IDs: 0-9 = digits, 10 = minus, 11 = dot, 12 = SEP (space), 13 = CLS, 14 = PAD.

## Current results

- 68 classes (25+ embedding models, multiple task prefixes per model)
- ~86% validation accuracy (4 layers, 128d)
- 10K samples per class (7000 train / 3000 val)
- Training data: multilingual text embeddings from diverse models

## Data format

Each `.npz` file in the data directory contains an `embeddings` key with shape
`(N, D)` float32 array. The filename (minus `.npz`) becomes the class name.
