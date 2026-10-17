# LTCAttention - LTCs and GDN inspired Self Attention

![LTCAttention overview](assets/ltcattention-overview.png)

## About

LTCAttention is a compact, nanoGPT-style language model that adds an
input-conditioned, time-varying Householder-form metric to causal
self-attention. It uses positive input-conditioned time constants, following
the principle of
[Liquid Time-constant Networks (LTCs)](https://arxiv.org/abs/2006.04439), and
adaptive modal retention, following the memory-control principle of
[Gated Delta Networks (GDN)](https://arxiv.org/abs/2412.06464). Its attention
geometry provides SSM-like adaptive memory decay while retaining ordinary
softmax attention.

The repository is intentionally model-focused: every model component,
including the modal LTC gate and KV cache, lives in one documented file,
[`model.py`](model.py).

This release contains only the LTC model. It does not expose a conventional
GQA model option or an `attention_type` switch. Grouped query/key-value head
layout is retained inside the LTC layer for memory efficiency.

## Model principle

Each LTC attention layer learns `M` temporal modes for every KV head. The
unconstrained modal matrix is orthogonalized by QR, producing directions

```math
u_m^\top u_n=\delta_{mn}.
```

The first residual-stream state in the causal block, `x_0`, controls the time
constant of each mode through one linear projection:

```math
\delta=Wx_0+b,
\qquad
\tau_{h,m}(x_0)
=\frac{\tau_{\min}}
{\sigma\!\left(r_{h,m}+\delta_{h,m}\right)}
>\tau_{\min}.
```

Because `x_0` is visible to every position, this controller is causal. The
resulting time constants are fixed for the block and reused by the KV cache.

For a query at position `i` and a key at position `j <= i`, define the key age
as `Delta = i - j`. Mode `m` uses the retention coefficient

```math
\lambda_m(\Delta,x_0)
=\exp\!\left(-\frac{\Delta}{\tau_m(x_0)}\right),
```

and the time-varying Householder-form operator

```math
\mathcal{H}_m(\Delta,x_0)
=I-\left(1-\lambda_m(\Delta,x_0)\right)u_mu_m^\top.
```

This is an identity-plus-rank-one Householder-form transform. Unlike a strict
Householder reflection, it contracts the component parallel to `u_m` by
`lambda_m` instead of reflecting it. Since the modal directions are
orthonormal, their product is

```math
M_\Delta(x_0)
=\prod_{m=1}^{M}\mathcal{H}_m(\Delta,x_0)
=I+\sum_{m=1}^{M}
\left(\lambda_m(\Delta,x_0)-1\right)u_mu_m^\top.
```

LTCAttention inserts this metric directly into the causal attention score:

```math
s_{ij}
=\frac{q_i^\top M_{i-j}(x_0)k_j}{\sqrt d}.
```

The learned orthogonal complement is unchanged, while temporal mode `m`
satisfies

```math
M_\Delta(x_0)u_m
=\lambda_m(\Delta,x_0)u_m.
```

The one-token retention factor

```math
a_m(x_0)=\exp\!\left(-\frac{1}{\tau_m(x_0)}\right)
\in(0,1)
```

gives `lambda_m(Delta, x_0) = a_m(x_0)^Delta`. This is a stable diagonal
SSM-like decay law: a smaller time constant removes old information more
quickly, while a larger time constant retains it. Since the time constants
depend on `x_0`, the memory horizon adapts to the input. The LTC principle is
represented by these positive input-conditioned time constants, while the GDN
principle is represented by adaptive modal retention and erasure. The decay
acts on attention logits rather than on a recurrent state.

The metric is applied without constructing another `T x T` matrix. With a
fixed center `c`, queries and keys are factorized as

```math
q_i'=q_i+\sum_m
\left(\exp\!\left[-\frac{i-c}{\tau_m}\right]-1\right)
(q_i^\top u_m)u_m,
```

```math
k_j'=k_j+\sum_m
\left(\exp\!\left[\frac{j-c}{\tau_m}\right]-1\right)
(k_j^\top u_m)u_m,
```

so that

```math
{q_i'}^\top k_j'=q_i^\top M_{i-j}k_j.
```

The modal projection cost is linear in sequence length; scaled dot-product
attention remains the only quadratic operation.

## Model summary

The reference configuration uses:

| Setting | Value |
|---|---:|
| Transformer layers | 6 |
| Hidden width | 384 |
| Query heads / KV heads | 6 / 2 |
| Head dimension | 64 |
| LTC decay modes per KV head | 64 |
| Context length | 512 tokens |
| Parameters | 29,104,512 |
| Training tokens per run | 287,588,352 |
| Seeds | 1337, 2027, 31415 |

## Repository layout

```text
model.py                    Complete LTC model and KV-cache implementation
train.py                    nanoGPT-style trainer and evaluator
prepare_fineweb_edu.py      Streaming deduplication and GPT-2 tokenization
benchmark.py                LTC prefill and cached-decode benchmark
plot_results.py             Evaluation figure generator
config/                     Tiny and reference training configurations
data/                       Dataset metadata; token binaries are Git-ignored
results/                    Evaluation JSON and figures
docs/experiment.md          Controlled comparison protocol
tests/                      Factorization, cache, model, and data tests
uv.lock                     Fully resolved uv environment
```

## Environment setup with uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and sync
the locked environment:

```bash
uv sync --frozen --extra data --extra plot
```

This installs the model, data and plotting dependencies, and the development
test group without changing `uv.lock`.

Run the tests through the managed environment:

```bash
uv run --frozen python -m pytest
```

No manual virtual-environment activation is required.

## Using the model

### Construct the reference model

```python
import torch

from model import GPT, GPTConfig

config = GPTConfig(
    block_size=512,
    vocab_size=50_304,
    n_layer=6,
    n_head=6,
    n_kv_head=2,
    n_embd=384,
    dropout=0.0,
    bias=False,
    controller_rank=0,
    controller_hidden_size=0,
    num_decay_modes=64,
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = GPT(config).to(device)
print(f"Parameters: {model.parameter_count():,}")
```

`n_embd` must be divisible by `n_head`, and `n_head` must be divisible by
`n_kv_head`. `num_decay_modes` may range from 1 to `head_dim`. Set
`controller_rank=0` whenever more than one mode is used.
`parameter_count()` follows nanoGPT's reporting convention and excludes learned
position embeddings by default; pass `exclude_position_embeddings=False` for
the literal total.

### Compute logits and training loss

Inputs and targets have shape `[batch, time]`. Targets are the input sequence
shifted by one token.

```python
tokens = torch.randint(0, config.vocab_size, (2, 512), device=device)
inputs = tokens[:, :-1]
targets = tokens[:, 1:]

logits, loss = model(inputs, targets)
assert loss is not None
loss.backward()

print(logits.shape)
print(loss.item())
```

When targets are provided, logits are returned for every position. Without
targets, the model projects only the final position to vocabulary logits.

### Save and restore a checkpoint

```python
checkpoint = {
    "model": model.state_dict(),
    "model_config": model.config_dict(),
}
torch.save(checkpoint, "ltc-model.pt")

payload = torch.load("ltc-model.pt", map_location=device, weights_only=False)
restored = GPT(GPTConfig(**payload["model_config"])).to(device)
restored.load_state_dict(payload["model"])
restored.eval()
```

The training script writes this model configuration and state dictionary, plus
the experiment configuration and validation history, to each checkpoint.

## KV-cached inference

`GPT.generate` uses the append-only cache by default:

```python
import tiktoken

encoding = tiktoken.get_encoding("gpt2")
prompt_ids = encoding.encode("Liquid attention")
prompt = torch.tensor([prompt_ids], dtype=torch.long, device=device)

model.eval()
generated = model.generate(
    prompt,
    max_new_tokens=64,
    temperature=0.8,
    top_k=50,
    use_cache=True,
)
print(encoding.decode(generated[0].tolist()))
```

The lower-level API returns one `LayerKVCache` for each Transformer block:

```python
logits, _, cache = model(prompt, use_cache=True)
next_token = torch.argmax(logits[:, -1], dim=-1, keepdim=True)

logits, _, cache = model(
    next_token,
    past_key_values=cache,
    use_cache=True,
)
```

Each cache stores transformed keys, values, modal directions, and time
constants in compact KV-head layout. `GPT.reorder_cache` can reorder or expand
the batch axis for beam-search bookkeeping. The total prompt and generated
length cannot exceed `block_size`; sliding-window eviction is not implicit.

## Training on FineWeb-Edu

### 1. Prepare the dataset

Install the data extra through `uv sync` as shown above, then run:

```bash
uv run --frozen python prepare_fineweb_edu.py \
  --output-dir data/fineweb_edu_fullrank_29m_6layer_half \
  --train-tokens 287588353 \
  --val-tokens 2000000
```

The script streams `HuggingFaceFW/fineweb-edu` (`sample-10BT`), creates a
stable document-disjoint validation split, removes exact duplicates after
whitespace normalization, tokenizes with GPT-2 BPE, and writes raw `uint16`
files. Expected SHA-256 checksums are stored in
[`data/fineweb_edu_fullrank_29m_6layer_half/meta.json`](data/fineweb_edu_fullrank_29m_6layer_half/meta.json).

The first 287,588,352 tokens form 561,696 non-overlapping 512-token blocks.
Every run shuffles those blocks once without replacement and consumes all of
them exactly once. The resulting budget is 9.881 tokens per LTC parameter,
approximately half of the commonly cited Chinchilla ratio.

### 2. Run the reference training configuration

```bash
uv run --frozen python train.py \
  config/fullrank_fineweb_edu_29m_6layer_half_3seeds.py
```

The configuration trains seeds 1337, 2027, and 31415 independently. It uses
23,404 optimizer updates, batch size 24, BF16, AdamW, a 1,170-update warmup,
and cosine decay from `6e-4` to `6e-5`. Checkpoints are written to
`out/ltc_fineweb_edu_29m_6layer_half_3seeds/`; token binaries and checkpoints
are excluded from Git.

The result JSON is written to
`results/ltc_fineweb_edu_29m_6layer_half_3seeds.json` and contains the full
validation history, final loss and perplexity, parameter count, token budget,
and measured training throughput for every seed.

### 3. Run a short smoke test

After preparing a sufficiently large token file:

```bash
uv run --frozen python train.py config/tiny_fineweb_edu.py \
  --seeds="(1337,)" \
  --max_iters=10 \
  --eval_iters=2 \
  --eval_interval=10 \
  --save_checkpoints=False
```

Configuration values follow nanoGPT's Python-file and `--key=value` override
style. `train_data_mode="random"` samples blocks with replacement;
`train_data_mode="one_epoch"` requires the file to contain exactly the number
of non-overlapping blocks consumed by the configured training run.

## Benchmark cached inference

The benchmark measures LTC attention prefill and one-token cached decode on the
local CUDA BF16 backend:

```bash
uv run --frozen python benchmark.py \
  --hidden-size 384 \
  --query-heads 6 \
  --kv-heads 2 \
  --num-decay-modes 64 \
  --controller-rank 0 \
  --seq-lens 128 512
```

Timings depend on the GPU, PyTorch build, shapes, and SDPA backend. They should
be treated as local implementation measurements.

## Evaluation results

The checked-in study used the LTC model in a three-seed controlled
comparison. Modal LTC reached validation loss `4.07281 ± 0.01777` and mean
perplexity `58.73`. The historical baseline reached `4.13471 ± 0.02367` and
mean perplexity `62.49`; the paired loss difference was
`-0.06190 ± 0.00646` nats/token in favor of LTC. LTC was lower in all three
measured seeds, added 1.20% parameters in that comparison, and reduced recorded
eager BF16 throughput by 12.40%.

These baseline artifacts are retained only as experiment provenance. The
executable model and trainer in this release are LTC-only. See
[`docs/experiment.md`](docs/experiment.md) and [`results/README.md`](results/README.md).

![Validation-loss curves](results/figures/fullrank_6layer_loss_curves.png)

![Final validation loss](results/figures/fullrank_6layer_final_performance.png)

Three seeds and one small model scale do not establish broad scaling behavior.

## Acknowledgements

This repository uses the nanoGPT training structure, PyTorch, and
FineWeb-Edu. The attention mechanism is informed by Liquid Time-Constant
Networks and Gated Delta Networks.

## Contact

[My X account](https://x.com/peony__snow)

## About the author

### Rikka Botan

Japanese independent researcher having a shy and pampered personality >_<

Twin-tail hair is a charm point :)

Interested in natural language processing.

Usually using Python and C.

![RikkaBotan Logo](https://github.com/user-attachments/assets/92913f91-9136-4d44-8b4d-8a2120118a05)

## License and data

MIT License. Copyright (c) 2026 Rikka Botan. See [LICENSE](LICENSE).

FineWeb-Edu data is not redistributed and remains subject to its own ODC-By
license and attribution requirements.
