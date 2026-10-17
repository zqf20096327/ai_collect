# zephyr

![Version 0.0.22](https://img.shields.io/badge/version-0.0.22-green)

**Zephyr** makes writing functional code in JAX for neural networks and machine learning a breeze. No subclassing, no **call**, no hidden state, just `f(params, x)`.

- Minimal library, minimal learning curve; zephyr solves the frustration working in pure JAX :: parameter creation and handling
- Near zero boilerplate, readable, aligns with JAX-style
- Full separation of state(params) and structure

# Core Idea

A neural network, like what it mathematically is, is just a function. Literally, just a function.

```python
def model(params, x):
    x = nets.linear(params["l1"], x, 256)
    x = jax.nn.relu(x)
    x = nets.linear(params["l2"], x, 10)
    return x
```

Zephyr takes care of initializing `params` via its `trace` function.

```python
key = jax.random.PRNGKey(0)
x   = jnp.ones([32, 784])

params     = trace(model, key, x)   # runs model once to infer all shapes

fast_model = jit(model)
logits     = fast_model(params, x)
```

# Installation

```bash
pip install-U  z-zephyr
```

# Motivation and Inspiration<a id="motivation"></a>

This library is heavily inspired by [Haiku](https://github.com/google-deepmind/dm-haiku)'s `transform` function which eventually
converts impure functions/class-method-calls into a pure function paired with an initilized `params` PyTree. This is my favorite
approach so far because it is closest to pure functional programming. Zephyr tries to push this to the simplest and make neural networks
simply just a function.

This library is also inspired by other frameworks I have tried in the past: Tensorflow -> PyTorch -> Flax, -> Equinox -> and Haiku (in this order). Tensorflow's shape inference. PyTorch's intuitive use with the right audience. Flax's `@compact` decorator before it was deprecated. Equinox's native interoptability with JAX. Lastly, Haiku's simplicity.
