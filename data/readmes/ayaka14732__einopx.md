# einopx

`einopx` is a unified, JAX-native array pattern API for shape and sharding checks, reshape, rearrange, reshard, and einsum contractions.

The project is in early development and has not yet been published to PyPI.

## Authors

- Codex 5.6 Sol
- Ayaka Mikazuki
- Shin
- Sangandol

## Related projects

- Native JAX operations
- [google-deepmind/einshape](https://github.com/google-deepmind/einshape)
- [arogozhnikov/einops](https://github.com/arogozhnikov/einops)
- [yixiaoer/einshard](https://github.com/yixiaoer/einshard)

## What problem does einopx solve?

### A single logical operation is scattered across multiple APIs

A single logical array operation in a JAX model often has to go through several tools that know nothing about each other: hand-written assertions to check shapes, `NamedSharding` or `PartitionSpec` to check sharding, `einops.rearrange` to split, merge, or transpose axes, and `jax.numpy.einsum` to perform the contraction. Users end up repeating axis names and introducing extra temporary variables along the way. These APIs frequently use incompatible syntax, adding maintenance overhead — even though shape, layout, sharding, and contraction together describe a single operation, they end up being expressed multiple times, creating redundancy. `einopx` unifies all of this information into a single API.

```python
query = einop(hidden, weight, "B* S* D, (Hq Dh)/N D -> B* S* Hq/N Dh")
```

This one line simultaneously specifies: the logical axes of `hidden` are `B S D`; the first physical axis of `weight` is composed of `Hq Dh` and sharded along `N`; `D` is the contraction axis; and the output should split the composite axis back into `Hq Dh`, with the final sharding landing on `Hq`.

### Plain einsum labels aren't enough to carry a model's shape contract

Traditional einsum strings typically rely on single-letter labels, which are fine for expressing algebraic relationships but poorly suited to carrying model semantics directly. Modern large models often call for more descriptive symbols — names like `Hq`, `Hkv`, `Dh`, and `Ktop` are much easier to read than `a`, `b`, `c`.

Separately, batch size and sequence length are usually only known at call time, while dimensions like hidden size and head count should strictly match the configuration. `einopx` uses `D` to denote axes that must be checked against a fixed configuration, and `B*` to denote axes that skip the fixed-size lookup but are still bound to the actual length observed at that call. For composite dynamic axes like `(B* S*)` that cannot be uniquely factored back out, you can supply the minimum necessary extra information via `axes={"B": ...}`.

### General-purpose einops libraries don't support JAX-specific function arguments

einops' einsum implementation can't accept JAX-specific arguments like `optimize`, `precision`, and `preferred_element_type`, forcing a fallback to the native JAX API. In `einopx`, these arguments are passed straight through, so there's no need to switch to the native JAX call.

### Output sharding shouldn't be determined by both the pattern and a separate argument

If the pattern describes one output layout while the caller also passes a separate `out_sharding`, the two could disagree, and it's unclear which one is authoritative. `einopx` does not accept a separate `out_sharding` argument: the output pattern is the single source of truth for both output shape and sharding. The wrapper constructs explicit JAX output sharding for both the internal reshape and the final contraction.

## Installation

Until a PyPI package is published, install from a Git checkout:

```bash
git clone https://github.com/ayaka14732/einopx.git
cd einopx
python -m pip install -e .
```

## Quick start

```python
import jax
import jax.numpy as jnp
from jax.sharding import NamedSharding, PartitionSpec as P

from einopx import make_einop

mesh = jax.make_mesh((len(jax.devices()),), ("device_x",), devices=jax.devices())
named = lambda spec: NamedSharding(mesh, spec)
device_count = mesh.shape["device_x"]
head_count = 2 * device_count
head_dim = 8
hidden_size = 32

einop = make_einop(
    {
        "D": hidden_size,
        "Hq": head_count,
        "Dh": head_dim,
        "N": device_count,
    },
    partition_rules={"N": "device_x"},
)

hidden = jax.device_put(jnp.ones((1, 4, hidden_size)), named(P()))
weight = jax.device_put(jnp.ones((head_count * head_dim, hidden_size)), named(P("device_x", None)))

query = einop(hidden, weight, "B* S* D, (Hq Dh)/N D -> B* S* Hq/N Dh")
```

The result has shape `(1, 4, head_count, head_dim)` and sharding `PartitionSpec(None, None, "device_x", None)`.

## Pattern syntax

Physical axes are separated by whitespace. Logical axes inside one pair of parentheses form one physical array dimension:

```python
einop(x, "B* S* D")
einop(x, "B* S* D -> (B* S*) D")
einop(x, weight, "B* S* D, V/N D -> B* S* V/N")
```

The syntax rules are as follows:

- `B`, `Hq`, and `head_dim` are logical axis names. Names may contain multiple letters, and digits or underscores after the first character.
- `B*` binds the observed length of `B` but skips the fixed-size mapping lookup. Every subsequent occurrence of `B*` must have the same length.
- `2D` denotes twice the configured length of `D`.
- `(B* S*)` denotes a physical dimension that is the product of logical axes `B` and `S`.
- `Hq/N` denotes a physical `Hq` dimension using the sharding alias `N`.
- `(Hq Dh)/N` denotes that the entire composite physical dimension uses the alias `N`. The suffix belongs to the physical axis, not to any individual logical factor.
- `""` is a check-only pattern for scalars.

Sharding syntax within composite axes is intentionally kept unambiguous: `(Hq Dh)/N` is valid, while `(Hq/N Dh)` and `(Hq Dh/N)` are rejected. Once a composite axis is expanded internally, physical sharding is attributed to the first logical factor, so `(Hq Dh)/N` can produce `Hq/N Dh` in the output.

If a composite input dimension contains more than one unknown dynamic factor, its factorization is not unique. In that case you need to explicitly bind enough dimensions:

```python
flat = einop(x, "B* S* D -> (B* S*) D")
restored = einop(flat, "(B* S*) D -> B* S* D", axes={"B": x.shape[0]})
```

Both the pattern and `axes` are static Python data at trace time; runtime-dynamic rank is not currently supported.

## Operation dispatch

`einop` selects an operation based on the pattern:

- No `->`: checks a single input and returns it unchanged.
- Single input, with identical logical axes on both sides of the arrow: performs a rearrange via transpose and reshape.
- Any other pattern with an arrow: performs a contraction via `jax.numpy.einsum`, then realizes the specified physical output axes.

Contraction options are keyword-only arguments:

```python
output = einop(
    context,
    projection,
    "B* S* Q/N, D Q/N -> B* S* D",
    precision=jax.lax.Precision.HIGH,
    preferred_element_type=jnp.float32,
)
```

`einopx` does not accept a separate `out_sharding` argument. The output pattern is the single source of truth for output sharding.

## Sharding model

Create a callable with fixed logical dimensions and optional sharding aliases:

```python
einop = make_einop(
    {"D": 2048, "N": 4},
    partition_rules={"N": "device_x"},
)
```

An alias can map to a single mesh axis or to a tuple of multiple mesh axes. Its fixed value must equal the corresponding mesh partition count. Every operand must use `NamedSharding` on the explicit mesh axes, share a compatible mesh and memory kind, and match exactly the physical sharding declared by the expression. Any physical dimension without an annotation must be replicated.

The wrapper passes explicit output sharding to both the JAX reshape and the contraction. This prevents incidental sharding inference from becoming part of the API contract, but it does not guarantee the elimination of every layout-changing copy or reshard. When performance depends on a specific physical layout, inspect the lowered StableHLO or a compiler profile.

## Numerical behavior

`einopx` recognizes composite free axes that belong to a single input and are preserved contiguously in the output, and keeps them collapsed during contraction, splitting them only after the contraction completes.

## Development

Run the CPU-compatible test suite from the repository root:

```bash
python -m unittest discover -s tests -v
python -m mypy src tests
```

TPU validation should additionally inspect representative lowered StableHLO to confirm that composite free axes remain flat through the intended dot, and that no undeclared reshard or all-gather is introduced.

## Roadmap

- Ellipsis support
- Adding new axes / repeating axes
- Reductions beyond einsum summation
- Diagonal extraction via repeated labels within a single input
