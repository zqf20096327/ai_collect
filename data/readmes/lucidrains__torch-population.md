## torch-population

Colocated population and ensemble wrapper for PyTorch. Parameters, buffers, tracked EMAs, and any `torch.optim.Optimizer` state live together in one flat `PopulationParameters` container — scaling cleanly from a zero-overhead single-model wrapper to vectorized populations, gradient surgery, and differentiable meta-learning.

## Install

```bash
$ pip install torch-population
```

## Usage

### 1. Simple: single-model noop wrapper → vectorized population

```python
import torch
from torch import nn
from torch_population import Population

net = nn.Sequential(nn.Linear(16, 32), nn.SiLU(), nn.Linear(32, 4))
x = torch.randn(8, 16)

# zero-overhead noop wrapper (exact parameter aliasing)

pop = Population(net)
assert pop.unwrap() is net

# scale to a vectorized population (or call pop.populate(4) later)

pop = Population(net, pop_size = 4)

out = pop(x)                                            # (4, 8, 4) shared input
out = pop(torch.randn(4, 8, 16), per_individual = True) # (4, 8, 4) per-individual input

# index out any individual as a normal nn.Module and write it back

ind = pop[0]
assert ind(x).shape == (8, 4)
pop[0] = ind
```

### 2. Colocated optimizers, state sharing & individual round-trip

```python
# wrap any torch.optim.Optimizer class (built-in or custom)

opt = pop.optimizer(torch.optim.AdamW, lr = 1e-3, shared = False)
# opt = pop.optimizer(AnyOptimizer, lr = 1e-3, shared = True)              # 1/P shared opt state
# opt = pop.optimizer(AnyOptimizer, lr = [1e-4, 3e-4, 1e-3, 3e-3])         # per-individual HPs

opt.zero_grad()
pop(x).pow(2).mean().backward()
pop.clip_grad_norm_(1.0)                                # per-individual grad clipping (optional members=, names=)
opt.step()

# toggle optimizer state sharing at runtime ('mean', 'max', 'min', 'median', 'sum', 'first', 'zero', callable, or per-key dict)

opt.share(reduce = {'exp_avg': 'mean', 'exp_avg_sq': 'max', 'step': 'max'})
opt.unshare()

# insert an existing standalone module + optimizer into a population, run population ops, then extract both back out

solo = nn.Sequential(nn.Linear(16, 32), nn.SiLU(), nn.Linear(32, 4))
solo_opt = torch.optim.AdamW(solo.parameters(), lr = 1e-3)
solo(x).pow(2).mean().backward()
solo_opt.step()

pop[2] = (solo, solo_opt)                               # or pop.insert(2, solo, solo_opt)

opt.zero_grad()
pop(x).pow(2).mean().backward()
opt.step()

solo, solo_opt = pop.extract(2)                         # normal nn.Module + native torch.optim.Optimizer with updated state
solo_opt.zero_grad()
solo(x).pow(2).mean().backward()
solo_opt.step()

# or use the checkout context manager to extract, train solo, and write both back on exit

with pop.checkout(2) as (ind, ind_opt):
    ind_opt.zero_grad()
    ind(x).pow(2).mean().backward()
    ind_opt.step()
```

### 3. Shared layers, arbitrary methods, lifecycle & model soups

```python
# share a backbone (params + buffers) while keeping independent heads

pop = Population(net, pop_size = 4, shared = ('0.*',))
opt = pop.optimizer(torch.optim.AdamW, lr = 1e-3)

sub_out = pop(x, members = (0, 2))                      # (2, 8, 4) subset forward
hidden  = pop.call('encode', x)                         # vmap any method or callable(module, *args)

# parameters, buffers, tracked EMAs, and optimizer state move in lockstep

pop.reset_(torch.tensor([True, False, False, False]))   # reinit masked members
pop.replace(3, 0, reset_opt = True)                     # clone winner 0 into slot 3
pop.delete(1)                                           # P: 4 -> 3
pop.append(0)                                           # P: 3 -> 4

avg_net = pop.mean()                                    # standalone nn.Module
med_net = pop.reduce('median')                          # or 'max', 'min', callable
```

### 4. Parameter & gradient EMAs (noop & populated)

```python
# runnable target / Polyak EMA (scalar or per-member multi-timescale rates)

ema = pop.clone(include_opt = False)
ema.lerp_(pop, torch.tensor([0.001, 0.005, 0.02, 0.1]))
target_out = ema(x)

# colocated, lifecycle-synced EMAs for gradients, online Fisher, or flat parameters
# initializes without zero-bias, follows state_dict(), device moves, reset_(mask), delete/append

g = opt.autograd(pop(x).pow(2).mean(), flat = True)     # (D,) in noop, (P, D) in populated
g_ema  = opt.ema_('grad', g, decay = 0.98)              # Grokfast / smoothed gradient
fisher = opt.ema_('fisher', g.square(), decay = 0.99)   # online diagonal Fisher
p_ema  = pop.ema_('param', pop.flat_params, decay = 0.995)
ages   = pop.track_('age', torch.zeros(4, dtype = torch.long))  # dtype-agnostic lifecycle-synced metadata

out_ema = pop(x, params = p_ema)                        # run forward directly with flat EMA weights
```

### 5. Multi-loss gradient surgery, swapping & gradient penalties

```python
# multi-loss flat autograd & gradient projection — identical code for 1 model (D,) or P models (P, D)

g1, g2 = opt.autograd(loss_a, loss_b, flat = True)
proj = g2 - ((g1 * g2).sum(dim = -1, keepdim = True).clamp(max = 0.) / g1.square().sum(dim = -1, keepdim = True).clamp(min = 1e-8)) * g1
opt.step(grads = g1 + proj)

# optimizer-agnostic reconciliation (returns a normal scalar loss for .backward(), clip_grad_norm_, any optimizer)
# spans multiple modules with zero state_dict() pollution and keeps unused branches at grad = None

from torch_population import PopulationParameters

params = PopulationParameters((actor, obs_history, action_history))
loss = params.reconcile(loss_a, loss_b, fn = lambda g1, g2: g1 + g2)
loss.backward()

# cross-member gradient swapping / gossip mixing across a population

g = opt.autograd(loss_pop, flat = True)
opt.step(grads = g.flip(0))                             # swap grads in a population of 2 (or g.roll(1, 0) / M @ g)

# parameter-gradient penalty (or input-gradient R1 / WGAN-GP with per_individual = True)

g = opt.autograd(loss_pop, flat = True, create_graph = True, retain_graph = True)
(loss_pop + 0.1 * g.square().sum()).backward()
```

### 6. Weight-space research: SAM, Evolution Strategies, Genetic Algorithms & model soups

```python
# pass any 1D (D,) or 2D (K, D) flat parameter tensor directly into pop(x, params = ...)

# Sharpness-Aware Minimization (SAM) — works for 1 model or P models
g = opt.autograd(pop(x).pow(2).mean(), flat = True)
eps = 0.05 * g / g.norm(dim = -1, keepdim = True).clamp(min = 1e-8)
opt.step(grads = opt.autograd(pop(x, params = pop.flat_params + eps.detach()).pow(2).mean(), flat = True))

# Evolution Strategies — vmap 64 perturbations on a single noop model
single = Population(net)
noise = torch.randn(64, single.flat_params.numel())
outs = single(x, params = single.flat_params.detach() + 0.05 * noise)   # (64, 8, 4)

# Genetic Algorithm — tournament selection + weight-averaging crossover + mutation
fit = -pop(x).sub(y).pow(2).mean(dim = (-2, -1))                        # (P,) fitness
losers = fit.topk(P - elites, largest = False).indices
cand = torch.randint(P, (len(losers), 2, tourney_size))
p1, p2 = cand.gather(-1, fit[cand].argmax(-1, keepdim = True)).squeeze(-1).unbind(-1)
pop[losers] = pop[p1].lerp_(pop.view(p2), 0.5)
with torch.no_grad():
    pop.flat_params[losers] += 0.05 * torch.randn_like(pop.flat_params[losers])

# differentiable model soup & mode connectivity
soup_out = pop(x, params = pop.flat_params.mean(dim = 0))               # (8, 4), grads flow to all P members
```

### 7. Advanced: differentiable multi-optimizer meta-learning & long-term memory consolidation

```python
pop = Population(net, pop_size = 4)
ltm = pop.clone(include_opt = False)                    # long-term memory copy of the population

# attach multiple different optimizers (each has its own colocated state)

opt_sgd   = pop.optimizer(torch.optim.SGD, lr = 5e-2, momentum = 0.9, name = 'sgd')
opt_rms   = pop.optimizer(torch.optim.RMSprop, lr = 1e-2, name = 'rms')
opt_adamw = pop.optimizer(torch.optim.AdamW, lr = 1e-2, name = 'adamw')

# backprop through unrolled updates across different optimizers (or per-member via members = ...)

fast = pop.population_parameters
for step_opt in (opt_sgd, opt_rms, opt_adamw):
    inner_loss = (pop(x_tr, params = fast) - meta_target).pow(2).mean()
    fast = step_opt.functional_step(inner_loss, fast, create_graph = True, max_grad_norm = 1.0)

pop(x_val, params = fast).pow(2).mean().backward()      # meta-gradients flow through all 3 optimizers

# single-model differentiable inner-loop & per-sample vectorized fast weights via expand()
single = Population(net)
inner_opt = single.optimizer(torch.optim.SGD, lr = 1e-2)
fast = inner_opt.functional_step(single(x_tr).pow(2).mean(), create_graph = True)  # noop functional_step
fast_batch = single.expand(batch_size)                                             # differentiable (B, D) copies
fast_batch = inner_opt.functional_step(single(x_b1, params = fast_batch, per_individual = True), fast_batch)
single(x_b2, params = fast_batch, per_individual = True).mean().backward()         # grads sum into single model

# consolidate fast weights into a long-term memory version of an individual (or whole population)

ltm.view(0).lerp_(fast, 0.05)                           # Polyak EMA on individual 0
ltm.lerp_(fast, torch.tensor([0.01, 0.05, 0.1, 0.2]))   # multi-timescale LTM across all members
pop.view(0).ema_('ltm', fast.flat_params[0], decay = 0.95)  # or colocated LTM runnable via params=
```

### Examples & Research Use-Case Suite

```bash
$ python train_pop_mnist.py
$ pytest                                                # core tests + tests/use_cases/ research cookbook
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
