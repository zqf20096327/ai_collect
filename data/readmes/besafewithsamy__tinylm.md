# tinylm

A small language model built from scratch in Python and NumPy, written to be
read. The goal of this project is educational: to understand how a language
model actually works internally  tokenization, embeddings, attention,
backpropagation, optimization  instead of relying on pretrained models or
high-level frameworks.

Every layer's forward and backward pass is written and derived by hand. There
is no autograd, no PyTorch, no transformers library. The only dependency is
NumPy.

## What it does

- Builds a character-level vocabulary from any text file
- Trains a decoder-only transformer (GPT-style architecture, pre-norm) with
  multi-head causal self-attention
- Computes softmax cross-entropy loss and backpropagates through the entire
  network manually
- Updates weights with a hand-written Adam optimizer (AdamW-style decoupled
  weight decay) and gradient clipping
- Saves and loads checkpoints (`.npz` weights + `.json` metadata)
- Generates text with temperature and top-k sampling
- Provides a small interactive chat interface for sampling from a trained model

It trains on the bundled Tiny Shakespeare corpus (~1 MB), reaching
character-level structure within minutes on a regular laptop CPU. With the
default settings it learns the general shape and vocabulary of the text —
names, line breaks, speaker tags — and produces plausible-looking (if
nonsensical) Shakespeare-flavored output. This is a model measured in
hundreds of thousands of parameters, not billions; fluency is not the point,
legibility is.

## Architecture

The model is a smaller, simpler version of the transformer used by GPT:

```
token ids
   │
   ├─ token embedding (vocab, d_model)
   ├─ position embedding (block_size, d_model)
   │
   └─ x = tok_emb[id] + pos_emb[t]              (B, T, d_model)
        │
        └─ × N blocks:
             ├─ x = x + Attention(LayerNorm(x))     residual
             └─ x = x + MLP(LayerNorm(x))           residual
        │
        ├─ LayerNorm
        └─ Linear(d_model, vocab) → logits → softmax
```

Design choices worth knowing:

- **Character-level tokens.** The vocabulary is simply every distinct
  character in the training text (65 for Shakespeare). This keeps the
  embedding table tiny and the tokenizer trivial, which keeps the focus on
  the model itself.
- **Pre-norm blocks.** LayerNorm is applied before attention and before the
  MLP, with the un-normalized value passed along a residual wire. This is
  what modern GPT models do; it trains more stably than post-norm.
- **Packed QKV projection.** Query, key, and value come out of one `Linear`
  layer and are reshaped into `(batch, head, time, d_head)` so per-head
  attention falls out of plain batched matrix multiplications.
- **Causal mask.** Attention scores for future positions are set to -1e10
  before the softmax, so position `t` only attends to positions `<= t`. That
  single constraint is what makes the model autoregressive.
- **Hand-derived backward passes.** Each layer implements `backward()` from
  the analytic gradient of its `forward()`. The two non-obvious derivations —
  LayerNorm and softmax cross-entropy (whose gradient collapses to
  `probs − onehot`) — are commented where they happen.

## How training works

`train.py` runs the standard loop:

1. Sample a random batch of `(inputs, targets)` — targets are the inputs
   shifted one token to the left, which is the whole objective: predict the
   next character from everything before it
2. Forward pass → loss (mean negative log-likelihood of target characters)
3. `model.backward()` fills in gradients for every parameter
4. Clip gradients by global norm (1.0) to tame early spikes
5. Adam step, then zero the accumulated gradients

Every 100 steps it prints the running loss, and every `--sample-every` steps
it prints text generated from the current weights, so you can watch the model
go from noise to letter statistics to word shapes.

The gradient implementation is verified by `tests/test_gradients.py`, which
compares the analytic gradients against finite differences and fails loudly
if any backward pass is wrong. This test is the project's correctness
backbone — if you modify a layer, run it.

## Installation

Requires Python 3.9+ and NumPy.

```bash
git clone https://github.com/besafewithsamy/tinylm.git
cd tinylm
pip install -r requirements.txt
```

No GPU or special hardware is needed; everything here trains on CPU.

## Training

With the bundled corpus (a quick demo run, ~1 minute, CPU):

```bash
python3 train.py --steps 300 --d-model 64 --n-layers 2 --n-heads 2 \
                 --block-size 64 --batch-size 16 --sample-every 300
```

A more serious run (roughly half an hour on a laptop CPU):

```bash
python3 train.py --steps 3000
```

Useful flags — all defaults live in `tinylm/config.py`:

| Flag | Meaning | Default |
|---|---|---|
| `--data` | training text file | `data/input.txt` |
| `--steps` | optimizer steps | 1000 |
| `--batch-size` | sequences per step | 32 |
| `--lr` | Adam learning rate | 3e-4 |
| `--d-model` | embedding / residual width | 96 |
| `--n-layers` | transformer blocks | 3 |
| `--n-heads` | attention heads | 4 |
| `--block-size` | context length | 128 |
| `--save` | checkpoint prefix | `checkpoints/model` |

Checkpoints are written as two files: `model.npz` (parameter arrays) and
`model.json` (architecture, vocabulary, training metadata), which is
everything needed to reload the model later.

## Chat

The interactive interface samples from a trained checkpoint:

```bash
python3 chat.py
```

Commands inside a session: `/temp 0.8` (temperature), `/topk 20` (top-k
sampling), `/reset` (clear context), `/quit`. Fair warning: a character-level
model of this size does not hold a conversation. It continues your prompt in
the statistical style of its training text, which is the fun part.

## Custom training data

Point `--data` at any UTF-8 text file:

```bash
python3 train.py --data path/to/your.txt --steps 2000
```

The vocabulary is built automatically from whatever characters appear in the
file, so any language or text style works without configuration. ASCII-heavy
text of a few hundred kilobytes or more trains fastest; the bundled
`data/input.txt` (Tiny Shakespeare, public domain) is a good size reference.
Note that the vocabulary and architecture are saved with the checkpoint, so a
checkpoint is only compatible with itself — each trained model carries its
own tokenizer.

## Tests

```bash
python3 tests/test_gradients.py   # finite-difference gradient check
python3 tests/test_smoke.py       # tiny model must learn a repeating corpus
```

The gradient check perturbs individual parameters, recomputes the loss
numerically, and compares against the backward pass (agreement to ~1e-6
relative error). The smoke test asserts loss falls sharply on a predictable
corpus — if either fails after your changes, your math broke somewhere, and
the failing parameter tells you which layer.

## Project structure

```
tinylm/
├── data/input.txt            # training corpus (Tiny Shakespeare)
├── tinylm/
│   ├── config.py             # hyperparameter defaults, one screenful
│   ├── tokenizer.py          # character vocabulary, encode/decode
│   ├── layers.py             # Linear, Embedding, LayerNorm (+ backward)
│   ├── model.py              # attention, MLP, blocks, loss, sampling
│   ├── optimizer.py          # Adam with decoupled weight decay
│   ├── dataset.py            # random (inputs, targets) batch sampler
│   └── checkpoint.py         # save/load .npz + .json
├── tests/
│   ├── test_gradients.py     # analytic vs. numerical gradients
│   └── test_smoke.py         # end-to-end "does it learn"
├── train.py                  # training entry point
├── chat.py                   # interactive sampling interface
└── requirements.txt
```

The intended reading order is roughly the order above: `config` →
`tokenizer` → `layers` → `model` → `optimizer` → `dataset`. Each file fits
on a screen or two, and `model.py`'s `forward`/`backward` mirror each other
line by line, which is the clearest way to see what backpropagation actually
computes.

## Ideas for experiments

- Increase `--steps` and watch samples evolve from noise to words to names
- Change the corpus (your own writing, code, another language) and watch the
  vocabulary and style change
- Break something on purpose: remove the causal mask in `model.py` and see
  what the model can and cannot learn
- Add a learning-rate warmup or cosine decay in `train.py`
- Implement top-p (nucleus) sampling next to top-k in `TransformerLM.sample`
- Compare hand-written Adam in `optimizer.py` against plain SGD — the
  difference at this scale is dramatic and instructive

## License

The code in this repository is released under the MIT license. The bundled
`data/input.txt` is Tiny Shakespeare (public domain, originally compiled by
Andrej Karpathy).
