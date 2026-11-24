## torch-population

Colocated population and ensemble wrapper for PyTorch. Parameters, buffers, and any `torch.optim.Optimizer` state live together in one flat `PopulationParameters` container.

## Install

```bash
$ pip install torch-population
```

## Usage

### Simple: noop wrapper, population & indexing

```python
import torch
from torch import nn
from torch_population import Population

net = nn.Sequential(nn.Linear(16, 32), nn.SiLU(), nn.Linear(32, 4))
x = torch.randn(8, 16)

# zero-overhead noop wrapper (exact param aliasing)

pop = Population(net)
assert pop.unwrap() is net

# turn into a vectorized population (or call pop.populate(4))

pop = Population(net, pop_size = 4)

out = pop(x)                                              # (4, 8, 4) shared input
out = pop(torch.randn(4, 8, 16), per_individual = True)   # (4, 8, 4) per-individual input

# index out an individual as a standard single nn.Module and write it back

ind = pop[0]
assert ind(x).shape == (8, 4)
pop[0] = ind
```

### Colocated optimizers (works with any `torch.optim.Optimizer`) & solo checkout

```python
# wrap any torch.optim.Optimizer class (built-in or custom)

opt = pop.optimizer(torch.optim.RMSprop, lr = 1e-3, shared = False)
# opt = pop.optimizer(AnyOptimizer, lr = 1e-3, shared = True)              # 1/P shared state
# opt = pop.optimizer(AnyOptimizer, lr = [1e-4, 3e-4, 1e-3, 3e-3])         # per-individual HPs

opt.zero_grad()
pop(x).pow(2).mean().backward()
opt.step()

# toggle state sharing across the population at runtime
# share() reduces the P separate states along the pop dim (default 'mean'; also 'max', 'min', 'sum', 'first', 'zero', member index, callable, or per-key dict)

opt.share(reduce = 'mean')                                 # or opt.share(reduce = {'square_avg': 'max', 'step': 'max'})
opt.unshare()                                              # broadcasts shared state back to P independent slots

# extract one individual + its native torch.optim.Optimizer, train solo, write both back in

ind, ind_opt = pop.extract(2)
ind_opt.zero_grad()
ind(x).pow(2).mean().backward()
ind_opt.step()
pop[2] = (ind, ind_opt)

# or with a context manager

with pop.checkout(2) as (ind, ind_opt):
    ind_opt.zero_grad()
    ind(x).pow(2).mean().backward()
    ind_opt.step()
```

### Unified `PopulationParameters`, PyTorch dicts & lifecycle

```python
pp = pop.population_parameters

pp.flat_params                       # (4, D) contiguous parameters
pp.named_optimizer_state()           # zero-copy views into colocated optimizer state

# single-individual PyTorch-compatible dict (zero-copy views; clone = True to copy)

ind_dict = pp[2]                     # {'parameters', 'named_parameters', 'buffers', 'state_dict', 'optimizer_state', ...}
pop_dict = pp.as_dict()

# shared layers, subset forward, dynamic resizing & population soup

pop = Population(net, pop_size = 4, shared = ('0.bias',))
opt = pop.optimizer(torch.optim.RMSprop, lr = 1e-3)

sub_out = pop(x, members = (0, 2))                        # (2, 8, 4)

pop.reset_(torch.tensor([True, False, False, False]))     # reinit masked params + buffers + opt state
pop.replace(3, 0, reset_opt = True)                       # copy member 0 into slot 3
pop.delete(1)                                             # P: 4 -> 3 in lockstep across params & opt state
pop.append(0)                                             # P: 3 -> 4
avg_net = pop.mean()                                      # standalone nn.Module with averaged weights
```

### Differentiable meta-learning & multi-loss gradient control (`autograd`, `functional_step`)

```python
pop = Population(net, pop_size = 4)
opt = pop.optimizer(torch.optim.RMSprop, lr = 1e-3, shared = False)
pp = pop.population_parameters
ema_pp = pp.clone(include_opt = False)

cur_pp = pp
for _ in range(2):
    inner_loss = pop(x, params = cur_pp).pow(2).mean()
    cur_pp = opt.functional_step(inner_loss, cur_pp, create_graph = True)

meta_loss = pop(x, params = cur_pp).pow(2).mean()
meta_loss.backward()                                      # gradients flow through inner optimizer updates

pp.copy_from_(cur_pp.detach())
ema_pp.lerp_(pp, 0.05)

# multi-loss / PCGrad / custom gradient lanes (works with both step() and functional_step())

g_task = pp.autograd(loss_task, retain_graph = True)      # {name: (P, ...)} scoped via names=
g_aux  = pp.autograd(loss_aux)
opt.step(grads = {k: g_task[k] + 0.5 * g_aux[k] for k in g_task})
```

### Example: train 10 MNIST networks in parallel

```bash
$ python train_pop_mnist.py
```

## Tests

```bash
$ pytest
```

## Citations

```bibtex
@inproceedings{anonymous2026continual,
    title   = {Continual Reinforcement Learning with Neuroevolution},
    author  = {Anonymous},
    booktitle = {Submitted to The Fifteenth International Conference on Learning Representations},
    year    = {2026},
    url     = {https://openreview.net/forum?id=UxsGk4on0e},
    note    = {under review}
}
```
