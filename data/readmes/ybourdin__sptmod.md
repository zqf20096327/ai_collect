# Series-Parallel Temporal Modulation (SPTMod)

This repository contains the PyTorch implementation of SPTMod used for the DAFx25 paper *Empirical Results for Adjusting Truncated Backpropagation Through Time while Training Neural Audio Effects* authored by Y. Bourdin, P. Legrand and F. Roche.

**Link to the paper:** [https://inria.hal.science/hal-05394988](https://inria.hal.science/hal-05394988)

**Sound examples and listening test:** [https://ybourdin.github.io/sptmod/](https://ybourdin.github.io/sptmod/)

## Architecture



![Figure of State prediction network (SPN) and SPTMod](attachments/sptmod25.svg) \
*Figure 1*. SPTMod, on the right, consists in two paths called the modulation and audio paths. The modulation path is a series of modulation blocks which compute modulation tensors (the $\mu_j$ tensors) applied to audio tensors ($x_j$). The initial states of the recurrent layers of the ModBlocks are computed by the State Prediction Network (SPN), on the left.

\
![Figure of ModBlock in SPTMod](attachments/sptmod25_modblock.svg) \
*Figure 2a*. Composition of the ModBlock. **An error in the ordering of the layers, present in the paper, has been corrected.**

\
![Figure of SPN Block](attachments/sptmod25_spnblock.svg) \
*Figure 2b*. Composition of an SPN block

## Training

Say we want a cumulative TBPTT length $L_c$, with $N$ sub-sequences of lengths $L_0, L_1, ..., L_{N-1}$ which sum to $L_c$.

Because we do not use padding for the first sub-sequence, the corresponding input length of this sub-sequence is $L_0^{in}$. It is computed with the `Model.set_target_length()` method.

- A list of sequences of length $L_0^{in} + L_1 + ... + L_{N-1}$ must be extracted from the training dataset using a sliding window.
- Then, before each training epoch:
    - The list of sequences is shuffled
    - The sequences are further split into sub-sequences
- We iterate through the sub-sequences in the way described in the diagram below:

![](attachments/optstrat.svg) \
*Figure 3*. Diagram of the lengths of intermediary tensors for consecutive sequence batches in our TBPTT-based approach, with 3 sub-sequences. In the first iteration, no padding is applied, so the input length incorporates the number of samples required by the temporal operations. A large additional length is used by the SPN to initialize the states of recurrent layers. In subsequent iterations, states and caches are retained, but their gradients are detached from the computational graph.

\
In the code, at every iteration (an iteration corresponding to one backpropagation pass, i.e. one sub-sequence), we need to:

- Check if the number of the current iteration is divisible by $N$
- If yes, then the first sub-sequence of a group is to be processed
    1. Compute the index intervals to slice the tensors given to different parts of the model, here the SPN, modulation path and audio path; and compute the cropping sizes of the cropping layers. This is the goal of the `Model.set_target_length()` method.
    2. Reset the model states with `Model.reset_states()`.
    3. Call `Model.forward()` with `paddingmode = CachedPadding1d.NoPadding` and `use_spn = True`.
- If not,
    1. Detach the model states with `Model.detach_states()`.
    2. Call `Model.forward()` with `paddingmode = CachedPadding1d.CachedPadding` and `use_spn = False`.

## Computing the slicing indices and the cropping sizes

The architecture of SPTMod comprises two paths containing blocks that consume some time samples (their output lengths are shorter than their input lengths) and that imply conditions over the lengths of some intermediary tensors, as represented on this diagram:

![](attachments/sptmod_indices.svg)

- $t_m(n)$, resp. $t_a(n)$, is the absolute time index of the start of the sequence received by the $(n+1)^{\text{th}}$ modulation block, resp. audio block.
- $L$ is the target output length.
- $t_a(N)$ is the absolute time index of the start of the resulting sequence. We set $t_a(N)=0$. The absolute time index of its end is thus $L$.
- $P$ is the pooling size of the modulation blocks.
- The condition (A) is that the tensor length before a pooling layer, i.e. $L - (t_m(n) + \sigma_m(n))$, must be a multiple of $P$.
- The condition (B) is that the lengths of the inputs to an add/multiply operator are equal.
- $\sigma_m(n)$, $P$ and $\sigma_a(n)$ are samples consumed by operations such as convolutions or pooling-upsampling layers.
- $c_{mm}(n)$, $c_{ma}(n)$, $c_a(n)$ are cropping sizes added to satisfy conditions (A) and (B), they must be non-negative.

### Modulation path calculations

The relationship between consecutive time indices in the modulation path is:

```math
t_m(n+1) - t_m(n) = \sigma_m(n) + P + c_{mm}(n)
```

Applying a telescoping sum from $n$ to $N-1$:

```math
t_m(N) - t_m(n) = (N-n)P + \sum_{j=n}^{N-1} (\sigma_m(j) + c_{mm}(j))
```

From this, we can express $\sum c_{mm}(j)$:

```math
\sum_{j=n}^{N-1}c_{mm}(j) = t_m(N) - t_m(n) - (N-n)P - \sum_{j=n}^{N-1} \sigma_m(j)
```

Condition (A): $L - (t_m(n) + \sigma_m(n)) = k_m(n) \cdot P$, where $k_m(n)$ is an integer.

We can then express $t_m(n)$ and substitute it in the expression of $\sum c_{mm}(j)$:

```math
\sum_{j=n}^{N-1}c_{mm}(j) = t_m(N) - (L - \sigma_m(n) - k_m(n)\cdot P) - (N-n)P - \sum_{j=n}^{N-1} \sigma_m(j)
```

```math
\sum_{j=n}^{N-1}c_{mm}(j) = t_m(N) - L + [k_m(n) - (N-n)]\cdot P - \sum_{j=n+1}^{N-1} \sigma_m(j)
```

To find an expression for $c_{mm}(n)$, we can separate the $j=n$ term from the sum:

```math
\sum_{j=n}^{n}c_{mm}(j) + \sum_{j=n+1}^{N-1}c_{mm}(j) = t_m(N) - L + [k_m(n) - (N-n)]\cdot P - \sum_{j=n+1}^{N-1} \sigma_m(j)
```

Thus, $c_{mm}(n)$ is:

```math
c_{mm}(n) = t_m(N) - L + [k_m(n) - (N-n)]\cdot P - \sum_{j=n+1}^{N-1} \sigma_m(j) - \sum_{j=n+1}^{N-1}c_{mm}(j)
```

This equation shows that $c\_{mm}(n)$ can be computed recursively, starting from $n=N-1$ (where sums from $N$ to $N-1$ are zero) and going down to $n=0$.

For $c_{mm}(n)$ to be non-negative ($c_{mm}(n) \geq 0$):

```math
[k_m(n) - (N-n)]\cdot P \geq L - t_m(N) + \sum_{j=n+1}^{N-1} \sigma_m(j) + \sum_{j=n+1}^{N-1} c_{mm}(j)
```

```math
k_m(n) \geq (N-n) + \frac{1}{P} \left[ L - t_m(N) + \sum_{j=n+1}^{N-1} \sigma_m(j) + \sum_{j=n+1}^{N-1} c_{mm}(j) \right ]
```

### Audio path calculations

The relationship between consecutive time indices in the audio path is:

```math
t_a(n+1) - t_a(n) = \sigma_a(n) + c_a(n)
```

Applying a telescoping sum from $n$ to $N-1$:

```math
t_a(N) - t_a(n) = \sum_{j=n}^{N-1} (\sigma_a(j) + c_a(j))
```

Thus:

```math
t_a(n) = t_a(N) - \sum_{j=n}^{N-1} (\sigma_a(j) + c_a(j))
```

Condition (B): $t_m(n) + \sigma_m(n) + P + c_{ma}(n) = t_a(n) + \sigma_a(n)$

Substitute the expression for $t_a(n)$:

```math
t_m(n) + \sigma_m(n) + P + c_{ma}(n) = t_a(N) - \sum_{j=n}^{N-1} (\sigma_a(j) + c_a(j)) + \sigma_a(n)
```

Next, substitute $t_m(n)$ using condition (A):

```math
(L - \sigma_m(n) - k_m(n)\cdot P) + \sigma_m(n) + P + c_{ma}(n) = t_a(N) - \sum_{j=n}^{N-1} (\sigma_a(j) + c_a(j)) + \sigma_a(n)
```

```math
L - (k_m(n) - 1)P + c_{ma}(n) = t_a(N) - \sum_{j=n+1}^{N-1} \sigma_a(j) - \sum_{j=n}^{N-1} c_a(j)
```

From this, we get the expression for $c_{ma}(n)$:

```math
c_{ma}(n) = t_a(N) - L - \sum_{j=n+1}^{N-1} \sigma_a(j) - \sum_{j=n}^{N-1} c_a(j) + (k_m(n) - 1)P
```

For $c_{ma}(n)$ to be non-negative ($c_{ma}(n) \geq 0$):

```math
(k_m(n) - 1)P \geq L - t_a(N) + \sum_{j=n+1}^{N-1} \sigma_a(j) + \sum_{j=n}^{N-1} c_a(j)
```

```math
k_m(n) \geq 1 + \frac{1}{P}\left[ L - t_a(N) + \sum_{j=n+1}^{N-1} \sigma_a(j) + \sum_{j=n}^{N-1} c_a(j) \right]
```

**Assumption on $c_a(n)$:**
There is a circular dependency between $c_a(n)$ (in the audio path) and $c_{ma}(n)$ (linking modulation to audio). To simplify, we assume $c_a(n) = 0$ for all $n$. This is likely a suboptimal choice, and an optimization algorithm could be used at this stage to find better values for $c_a(n)$.

With $c_a(j)=0$ for all $j$, the expression for $c_{ma}(n)$ becomes:

```math
c_{ma}(n) = t_a(N) - L - \sum_{j=n+1}^{N-1} \sigma_a(j) + (k_m(n) - 1)P
```

And the condition for $k_m(n)$ derived from $c_{ma}(n) \ge 0$ simplifies to:

```math
k_m(n) \geq 1 + \frac{1}{P}\left[ L - t_a(N) + \sum_{j=n+1}^{N-1} \sigma_a(j) \right]
```

### Determining $k_m(n)$, $c_{mm}(n)$, $c_{ma}(n)$, $t_m(0)$ and $t_a(0)$

To ensure both $c_{mm}(n) \ge 0$ and $c_{ma}(n) \ge 0$, $k_m(n)$ must satisfy both derived conditions. We choose the smallest integer $k_m(n)$ that satisfies a specific formulation based on these conditions, that is:
```math
k_m(n) = \max\left( (N-n) + \left\lceil \frac{L - t_m(N) + \sum_{j=n+1}^{N-1}\sigma_m(j)}{P} \right\rceil, 1 + \left\lceil \frac{L - t_a(N) + \sum_{j=n+1}^{N-1}\sigma_a(j)}{P} \right\rceil \right)
```

The compensation terms are then calculated (iteratively for $c_{mm}(n)$ from $n=N-1$ down to $0$):

```math
c_{mm}(n) = t_m(N) - L + [k_m(n) - (N-n)]\cdot P - \sum_{j=n+1}^{N-1} \sigma_m(j) - \sum_{j=n+1}^{N-1}c_{mm}(j)
```

```math
c_{ma}(n) = t_a(N) - L - \sum_{j=n+1}^{N-1} \sigma_a(j) + (k_m(n) - 1)P
```

The initial time indices are:

```math
t_m(0) = L - \sigma_m(0) - k_m(0)\cdot P
```

```math
t_a(0) = t_a(N) - \sum_{j=0}^{N-1} \sigma_a(j)
```

(Note that $t_a(N)=t_m(N)=0$)