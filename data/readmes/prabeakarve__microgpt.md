# MicroGPT

**A GPT you can read end to end in one sitting â€?700 lines of NumPy, no framework, no autograd.**

MicroGPT is a decoder-only Transformer language model implemented from first principles.
Every gradient is derived by hand, every shape is annotated, and the whole thing trains on a
laptop CPU in about a minute. It exists for one reason: to make the machinery of modern
language models legible instead of magical.

```
                      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?   token ids  â”€â”€â”€â”€â”€â”€â–?â”? tok_emb[idx] + pos_emb[:T]                  â”?                      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?                                          â–?              â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?              â”? Ã— n_layer                                    â”?              â”?  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?â”?              â”?  â”?x = x + Attention(LN(x))                â”?â”?              â”?  â”?x = x + MLP(LN(x))                      â”?â”?              â”?  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?â”?              â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?                                  â–?                      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?                      â”? LN_f â†?logits = x @ Eáµ€   â”? (weight tying)
                      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”?```

## Why another tiny GPT

Most "build GPT from scratch" projects end up re-implementing an autograd engine, which hides
the interesting part behind a second abstraction. MicroGPT keeps the forward pass explicit and
writes the backward pass by hand, so the chain rule is visible in the code that uses it. The
test suite proves the backward pass correct with central finite differences against every
parameter class â€?attention projections, both layer norms, the MLP, and the tied embeddings.

## Features

- **Pure NumPy.** One dependency (`numpy`). Runs anywhere Python runs, including CI containers.
- **Hand-written backward pass.** No autograd, no `torch.autograd`, no graph object.
- **Causal multi-head self-attention** with residual connections and pre-layer-norm.
- **Weight tying** between the input embedding and the output projection.
- **Byte-level tokenizer** â€?256 symbols, no training, exact UTF-8 round-trip.
- **AdamW** with bias correction, linear warmup, and cosine decay.
- **Sampling** with temperature, top-k, and a next-token distribution inspector.
- **Checkpointing** to compressed `.npz` plus a JSON sidecar with the full config and metrics.
- **14 tests**, including a gradient check with a `2e-4` relative-error bound.
- **CLI** with `train`, `sample`, `eval`, `info`, and `next` subcommands.

## Install

```bash
git clone https://github.com/prabeakarve/microgpt.git
cd microgpt
python -m pip install -e .
```

Python 3.10+ and NumPy are the only requirements.

## Quick start

Train on the bundled corpus (about 8 KB of text, ~60 seconds on a laptop):

```bash
python -m microgpt train \
  --corpus examples/corpus.txt \
  --out checkpoints/model.npz \
  --block-size 96 --n-layer 3 --n-head 4 --n-embd 128 \
  --batch-size 16 --steps 1200 --lr 3e-3 --warmup 60
```

Sample from the checkpoint:

```bash
python -m microgpt sample --ckpt checkpoints/model.npz \
  --prompt "A language model is a probability distribution over" \
  --tokens 200 --temperature 0.7 --top-k 40
```

Inspect what the model thinks comes next:

```bash
python -m microgpt next --context "Attention is a lookup that"
```

Score a text:

```bash
python -m microgpt eval --text examples/corpus.txt
```

## Library use

```python
import numpy as np
from microgpt import GPT, ByteTokenizer, TrainConfig, train, complete, perplexity

cfg = TrainConfig(corpus="examples/corpus.txt", steps=400, n_embd=96, n_layer=2)
meta = train(cfg)                       # writes cfg.out and cfg.out + ".json"

model = GPT(vocab_size=256, block_size=64, n_layer=2, n_head=4, n_embd=96)
loss, grads = model.loss_and_grads(idx, targets)   # idx, targets: int64 (B, T)

print(complete(model, "The model learns", max_new_tokens=120))
print(perplexity(model, open("examples/corpus.txt").read()))
```

## What the numbers mean

| Symbol | Meaning |
| --- | --- |
| `B` | batch size |
| `T` | sequence length (`<= block_size`) |
| `C` | embedding width (`n_embd`) |
| `H` | number of heads, `head_dim = C / H` |
| `V` | vocabulary size (256, byte-level) |

Cross-entropy loss is reported in nats per token. `ln(256) â‰?5.545` is the loss of a model that
guesses uniformly, so any loss below that is real signal. Perplexity is `exp(loss)`.

## Design notes

**Why pre-layer-norm.** Normalizing before each sub-block keeps the residual stream's scale
stable, which is what makes deep stacks trainable without learning-rate tricks. The residual
path is a clean identity from the embedding to the final norm.

**Why scale the output projections.** `wo` and `w2` are multiplied by `1/sqrt(2 * n_layer)` at
initialization. Residual branches accumulate variance with depth; this keeps the stream's
magnitude roughly constant and prevents the first few dozen steps from diverging.

**Why the mask is applied before the softmax.** Setting masked scores to `-inf` makes their
post-softmax probability exactly zero, so no future token can influence the present. Applying a
mask afterwards would break the normalization.

**Why byte-level tokens.** A learned subword vocabulary is a second thing to train, version, and
get wrong. Bytes cost sequence length but remove an entire class of bugs, and they let the model
round-trip any UTF-8 text exactly â€?including text it has never seen.

## Project layout

```
microgpt/
  model.py        # Transformer: forward pass, hand-written backward pass, sampling
  optim.py        # AdamW and the warmup + cosine schedule
  train.py        # batching, training loop, checkpoint save/load
  generate.py     # completion, perplexity, next-token inspection
  tokenizer.py    # byte-level tokenizer
  __main__.py     # CLI
examples/
  corpus.txt      # ~8 KB training corpus
tests/
  test_microgpt.py
```

## Testing

```bash
python -m unittest discover -s tests -v
```

The gradient check compares analytic gradients against central differences for the token
embedding, positional embedding, query projection, output projection, both MLP matrices, and
both layer norms. A relative error above `2e-4` fails the build.

## ä¸­æ–‡è¯´æ˜Ž

MicroGPT æ˜¯ä¸€ä¸?*åªç”¨ NumPy ä»Žé›¶å®žçŽ°**çš?GPT è¯­è¨€æ¨¡åž‹ï¼šæ‰‹å†™å‰å‘ä¸Žåå‘ä¼ æ’­ï¼Œä¸ä¾èµ–ä»»ä½•æ·±åº¦å­¦ä¹ æ¡†æž¶ã€?
- **ç»“æž„**ï¼šå­—èŠ‚çº§åˆ†è¯ï¼?56 è¯è¡¨ï¼? å¤šå¤´å› æžœè‡ªæ³¨æ„åŠ› + æ®‹å·® + Pre-LayerNorm + 4 å€æ‰©å±?FFNï¼Œè¾“å…¥è¾“å‡ºåµŒå…¥æƒé‡å…±äº«ã€?- **è®­ç»ƒ**ï¼šäº¤å‰ç†µæŸå¤±ï¼ŒAdamW ä¼˜åŒ–å™¨ï¼Œçº¿æ€?warmup + ä½™å¼¦é€€ç«ï¼Œæ¢¯åº¦ç”¨ä¸­å¿ƒå·®åˆ†é€å‚æ•°æ ¡éªŒã€?- **æŽ¨ç†**ï¼šæ¸©åº¦é‡‡æ ·ã€top-k æˆªæ–­ã€å›°æƒ‘åº¦è¯„ä¼°ã€ä¸‹ä¸€ä¸?token æ¦‚çŽ‡åˆ†å¸ƒæŸ¥çœ‹ã€?- **ä¸Šæ‰‹**ï¼š`pip install -e .` åŽæ‰§è¡?`python -m microgpt train`ï¼Œä¸€åˆ†é’Ÿå†…å¯åœ¨ç¬”è®°æœ¬ CPU ä¸Šå®Œæˆè®­ç»ƒã€?
```bash
python -m microgpt train --steps 1200 --n-embd 128 --n-layer 3
python -m microgpt sample --prompt "A language model is" --tokens 200
```

é€‚åˆç”¨æ¥ç†è§£æ³¨æ„åŠ›ã€åå‘ä¼ æ’­ã€ä¼˜åŒ–å™¨å’Œé‡‡æ ·ç­–ç•¥åˆ°åº•åœ¨åšä»€ä¹ˆâ€”â€”ä»£ç é‡å°åˆ°å¯ä»¥ä¸€ä¸ªä¸‹åˆè¯»å®Œã€?
## License

MIT Â© 2026 prabeakarve
