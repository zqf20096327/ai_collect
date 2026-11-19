<div align="center">

# Oxideon

**A fast, Hackable Deep Learning & Tensor Library in Rust — with a PyTorch-friendly Python API.**

[![Version](https://img.shields.io/badge/version-v0.0.1-blue.svg)](https://github.com/voidstackloop/oxideon/releases/tag/v0.0.1)
[![Python](https://img.shields.io/badge/python-3.9%20%E2%80%93%203.13%20(abi3)-blue.svg)](pyproject.toml)
[![Rust](https://img.shields.io/badge/rust-2024%20(1.85%2B)-orange.svg)](https://www.rust-lang.org)
[![Clippy](https://img.shields.io/badge/clippy-0%20warnings-brightgreen.svg)]()
[![License](https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-blue.svg)](LICENSE-MIT)

[Why Oxideon?](#why-oxideon) · [Getting Started](#getting-started) · [Quick Tour](#quick-tour) · [PyTorch Cheat Sheet](#pytorch-cheat-sheet) · [Interop](#ecosystem-interop) · [Architecture](#how-its-organized) · [Docs](docs/)

</div>

---

## Why Oxideon?

Most deep learning stacks force a trade-off: either you use Python on top of a massive C++ runtime that's hard to inspect or embed, or you write everything in Rust and give up the ergonomics of NumPy and PyTorch.

**Oxideon** tries to give you both:
- **A clean Rust core (`oxideon-core`)** with multi-dtype tensors (`f32`, `f64`, `f16`, `bf16`, `fp8`, `c64`, `c128`, `i64`, `bool`), zero-copy strided views, higher-order autograd, blocked GEMM, and a caching buffer pool.
- **Native GPU & JIT execution** via `wgpu` (Vulkan / DX12 / Metal) and dynamic NVIDIA CUDA Driver PTX loading (`nvcuda`), plus an SSA graph compiler with operator fusion and WGSL/PTX codegen.
- **Familiar Python bindings (`PyO3` `abi3`)** — one wheel works across Python 3.9–3.13, releases the GIL during heavy compute, and talks zero-copy with NumPy and PyTorch via DLPack.
- **Batteries included for modern ML** — `nn.Module`, `AdamW`/schedule-free/2nd-order optimizers, SafeTensors & ONNX import/export, GGUF & 1.58-bit/4-bit quantization, PagedAttention & speculative decoding, DoRA/LoRA+, DPO/ORPO, and TCP/in-process distributed training (DDP + FSDP).

---

## Getting Started

### Build from source (Python + Rust)

```bash
git clone https://github.com/voidstackloop/oxideon.git
cd oxideon

# Create a virtualenv and install maturin
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install maturin numpy pytest

# Build and install the optimized Python extension
maturin develop --release
```

### Use from Rust

Add `oxideon-core` to your `Cargo.toml` or run the built-in tests and examples directly:

```bash
cargo test -p oxideon-core --lib
cargo run --release --example showcase
```

---

## Quick Tour

### 1. Tensors & Zero-Copy Strided Views

Oxideon tensors use signed `isize` strides, so transposes, flips, and stepped slices share underlying memory with zero copies:

```python
import oxideon as ox

x = ox.Tensor.arange(0.0, 24.0, 1.0).reshape([2, 3, 4])
v = x.transpose(0, 2)
assert v.shares_storage(x)

flipped = x[:, ::2, ::-1]
y = (x * 2.0 + 1.0).sum(dim=1)
```

### 2. Higher-Order Autograd

Need 1st, 2nd, or 3rd derivatives, Jacobians, or Hessians? Just set `create_graph=True`:

```python
import oxideon as ox

x = ox.Tensor.from_slice([3.0], [1], requires_grad=True)
y = x.powf(4.0)

dy  = ox.grad([y], [x], create_graph=True)[0]   # 4x^3  = 108.0
d2y = ox.grad([dy], [x], create_graph=True)[0]  # 12x^2 = 108.0
d3y = ox.grad([d2y], [x])[0]                    # 24x   = 72.0
```

### 3. Neural Networks (`ox.nn`) & Training

If you've ever written a PyTorch training loop, you already know how to write one in Oxideon:

```python
import oxideon as ox
import oxideon.nn as nn
import oxideon.optim as optim

class MLP(nn.Module):
    def __init__(self, d_in: int, d_hidden: int, d_out: int):
        super().__init__()
        self.fc1 = nn.Linear(d_in, d_hidden)
        self.act = nn.GELU()
        self.norm = nn.LayerNorm(d_hidden)
        self.fc2 = nn.Linear(d_hidden, d_out)

    def forward(self, x):
        return self.fc2(self.norm(self.act(self.fc1(x))))

model = MLP(16, 64, 4)
opt = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)

x = ox.randn([32, 16])
target = ox.randn([32, 4])

loss = ((model(x) - target) ** 2).mean()
opt.zero_grad()
loss.backward()
opt.step()
```

### 4. LLM Inference, Quantization & PEFT

Oxideon ships first-class primitives for running and fine-tuning language models:

```python
import oxideon as ox

# Paged KV cache (16-token blocks)
kv = ox.PagedKVCache(num_blocks=128, block_size=16, num_heads=8, head_dim=64)
table = kv.allocate(num_tokens=24)

# DoRA adapter fine-tuning that merges back into a plain Linear for inference
dora = ox.DoRALinear(in_features=256, out_features=256, r=8, lora_alpha=16.0)
out = dora.forward(ox.randn([16, 256]))
dora.merge()
```

You also get `FlashAttention-2` tiled online softmax, `SpeculativeDraftDecoder`, `Q4_0`/`Q8_0`/K-quants/GGUF loading, `BitLinear` 1.58-bit ternary layers, and alignment losses (`DPOLoss`, `ORPOLoss`, `KTOLoss`).

### 5. Distributed Training (DDP & FSDP)

Run multi-rank collectives over TCP or in-process threads with `NativeProcessGroup` and `FullyShardedParam` (`ox.distributed`), or launch with `RANK` / `WORLD_SIZE` / `MASTER_ADDR` / `MASTER_PORT` via `ProcessGroup.from_env()`:

```python
import oxideon as ox
import oxideon.distributed as dist

pg = dist.NativeProcessGroup.from_env()
w = ox.randn([1024, 1024])
sharded = dist.FullyShardedParam.from_tensor(w, pg)
full_w = sharded.gather(pg)
```

---

## PyTorch Cheat Sheet

| PyTorch (`torch`) | Oxideon (`ox`) |
|---|---|
| `torch.randn(3, 4)` | `ox.randn([3, 4])` |
| `torch.arange(0, 10)` | `ox.Tensor.arange(0.0, 10.0, 1.0)` |
| `x.transpose(0, 1)` / `x.t()` | `x.transpose(0, 1)` / `x.t()` |
| `y.backward()` | `y.backward()` |
| `torch.autograd.grad(y, x, create_graph=True)` | `ox.grad([y], [x], create_graph=True)` |
| `torch.nn.Module` / `Linear` | `ox.nn.Module` / `ox.nn.Linear` |
| `torch.optim.AdamW` | `ox.optim.AdamW` |
| `torch.cuda.is_available()` | `ox.cuda.is_available()` |
| `safetensors.save_file` | `ox.save_file` / `ox.load_file` |

---

## Ecosystem Interop

Oxideon plays nicely with the libraries you already use:

- **NumPy**: `ox.from_numpy(arr)`, `t.numpy()`, `np.asarray(t)` (`__array__` protocol)
- **PyTorch**: `ox.from_torch(t)`, `t.to_torch()`, zero-copy CPU DLPack (`__dlpack__`), and bidirectional `state_dict` helpers
- **SafeTensors & ONNX**: zero-copy SafeTensors I/O and ONNX export (both sequential models and compiled SSA graphs)
- **Data & Science**: Pandas, Polars, Apache Arrow, SciPy sparse matrices (`CSRMatrix`), Pillow (`from_pil` / `to_pil`), NetworkX, SymPy, and JAX

---

## How It's Organized

```text
oxideon/
├── crates/
│   ├── oxideon-core/      # Tensors, autograd, nn, optim, quant, JIT, compiler, CUDA/wgpu backends
│   └── oxideon-engines/   # Scientific, physics, PDE, and domain simulation engines
├── python/oxideon/        # High-level Python package (nn, optim, distributed, cuda, evals, vision, ...)
├── src/                   # PyO3 native extension bindings
├── examples/              # Runnable Python and Rust showcases
├── docs/                  # Architecture, tutorials, benchmarks, API stability & reference guides
└── tests/                 # Python test suite
```

---

## Running Tests

```bash
# Rust core tests
cargo test -p oxideon-core --lib

# Workspace lint (zero warnings)
cargo clippy --workspace --all-targets -- -D warnings

# Python tests
pytest tests/ -q
```

---

## Note on Cryptography Modules

The `crypto` / `quantum` modules included in the scientific engines are **educational and complexity-estimation utilities only**. Do not use them to protect sensitive production data.

---

## License

Dual-licensed under either of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE))
- MIT License ([LICENSE-MIT](LICENSE-MIT))

at your option.
