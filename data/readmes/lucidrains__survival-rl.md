<img src="./alg1.png" width="350px"></img>

## Survival RL

Explorations into an application of [survival analysis to RL](https://arxiv.org/abs/2605.31273), proposed by Tiofack et al. of Inria earlier this year

## Install

```bash
$ pip install survival-rl
```

## Usage

`HazardCritic` takes a batch of states, actions and events, and predicts the time bin in which the event is first reached, conditioned on that event. It is trained by maximum likelihood on the predicted logits, where `reach_event_index` marks the observed time bin, and `-1` (or anything at or past `horizon_cutoff`) is treated as right censored.

```python
import torch
from survival_rl import HazardCritic

critic = HazardCritic(
    dim = 64,
    depth = 2,
    dim_state = 8,
    num_actions = 3,
    pred_time_bins = 32
)

state  = torch.randn(16, 8)
action = torch.randn(16, 3)
event  = torch.randn(16, 8)     # every state and action is conditioned on the event

reach_event_index = torch.randint(0, 32, (16,))
horizon_cutoff    = torch.full((16,), 32)

loss = critic(state, action, event, reach_event_index = reach_event_index, horizon_cutoff = horizon_cutoff)
loss.backward()
```

Once trained, a policy can be extracted for reaching the event, or avoiding it with `negate = True`, given any actor of the form `(state, event) -> action`.

```python
class Actor(torch.nn.Module):
    def __init__(self, dim_state = 8, dim_event = 8, num_actions = 3):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(dim_state + dim_event, 64),
            torch.nn.SiLU(),
            torch.nn.Linear(64, num_actions)
        )

    def forward(self, state, event):
        return self.net(torch.cat((state, event), dim = -1))

actor = Actor()

# maximize the value to reach the event

loss = -critic.extract_policy(actor, state, event).mean()
loss.backward()

# or pass `negate = True` to avoid the event instead

loss = -critic.extract_policy(actor, state, event, negate = True).mean()
loss.backward()
```

The reach indices are computed from trajectory data with `compute_first_dwell_time`, which finds the first time each trajectory dwells within `eps` of its event.

```python
import torch
from survival_rl import compute_first_dwell_time

states = torch.randn(4, 64, 8)      # (batch, time, dim)
event  = states[:, -1:]             # (batch, num_queries, dim)

# first dwell of each trajectory at its event - -1 means it was never reached,
# and is right censored at `horizon_cutoff`

reach_event_index, horizon_cutoff = compute_first_dwell_time(event, states = states, eps = 0.25)
```

To extract a policy from multiple critics, use `PolicyExtractor`. Each `ExtractionSpec` is one term in the objective. Setting `negate = True` pulls the policy away from the event instead of toward it. The actor is forwarded once and shared across specs. Each spec also accepts `weight` and `lr`. A list of critics, e.g. `ExtractionSpec([critic_a, critic_b])`, uses the pessimistic minimum.

```python
from survival_rl import PolicyExtractor, ExtractionSpec

# a second, state-only critic for crashes

crash_critic = HazardCritic(
    dim = 64,
    depth = 2,
    dim_state = 8,
    num_actions = 3,
    pred_time_bins = 32,
    condition_on_event = False
)

# (train `critic` and `crash_critic` on their respective events)

extractor = PolicyExtractor(
    actor,
    [
        ExtractionSpec(critic, name = 'goal'),                       # pull toward the goal
        ExtractionSpec(crash_critic, negate = True, name = 'crash')  # push away from crashes
    ],
    base_lr = 1e-3,
    avoid_lr_scale = 0.1   # avoid specs take smaller steps by default
)

for _ in range(1000):
    extractor.step(state, event = event)
```

For a variant where the time bins compete for a single unit of mass through a softmax, simply swap in `HazardCriticCompetitive`, which takes the same arguments.

```python
from survival_rl import HazardCriticCompetitive as HazardCritic
```

## Dwell curriculum

`DwellCurriculum` tracks observed dwell with an EMA and featurizes the dwell condition for the event.

```python
from survival_rl import DwellCurriculum

curriculum = DwellCurriculum(
    scale = 12.,
    std_fraction = 0.5   # target = mean + 0.5 * std
)

event = curriculum.featurize(goal, torch.tensor([1, 2, 3]))   # int['b'] -> goal + dwell
event = curriculum.featurize(goal)                            # null dwell, for average event prediction
event = curriculum.featurize(goal, dwell, drop_prob = 0.1)    # drop dwell during training

target = curriculum.update(dwells)
target = curriculum.above_mean(0.5)
```

Set `dwell_feature_dim = 0` to disable dwell features. Null dwells are zero features, so the critic can also produce an average event prediction.

## Citations

```bibtex
@inproceedings{Tiofack2026SVL,
    title     = {SVL: Goal-Conditioned Reinforcement Learning as Survival Learning},
    author    = {Franki Nguimatsia Tiofack and Fabian Schramm and Th{\'e}otime Le Hellard and Justin Carpentier},
    booktitle = {International Conference on Machine Learning (ICML)},
    year      = {2026},
    url       = {https://arxiv.org/abs/2604.17551}
}
```

```bibtex
@article{Tiofack2026SRL,
    title   = {Survival Reinforcement Learning: Toward Scalable Self-Supervised RL},
    author  = {Franki Nguimatsia-Tiofack and Fabian Schramm and Th{\'e}otime Le Hellard and Justin Carpentier},
    journal = {arXiv preprint arXiv:2605.31273},
    year    = {2026},
    note    = {19th European Workshop on Reinforcement Learning (EWRL), Oral},
    url     = {https://arxiv.org/abs/2605.31273}
}
```
