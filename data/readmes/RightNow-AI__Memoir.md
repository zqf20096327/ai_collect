# Memoir

A transformer has two timescales. Weights freeze when pretraining ends, and the
context window empties when the session does. Everything the model learns while
you talk to it is thrown away.

Memoir is an architecture with weights that keep moving. We are building it in
the open and publishing what we find, including the parts that do not work.

![Memoir architecture](figures/png/model.png)

## The idea

Four pieces, meant to work as one system.

**Weight tiers.** Four sets of weights on different clocks. Fast weights update
on every forward pass. Episodic weights update once per session. Slow weights
consolidate rarely. A frozen core never changes at all, which is what keeps a
self modifying model anchored.

![Weight tiers across timescales](figures/png/tiers.png)

**A pondering core.** A small recurrent block that runs a variable number of
steps and decides for itself when to stop. Reasoning depth stops being tied to
parameter count.

**A world model signal.** One objective for every tier. Predict the next latent
state, score it with an energy head. Low energy means coherent. High energy
means think longer or refuse to answer.

**Discovered update rules.** The update rules are small networks found by
meta optimization instead of written by hand.

The novel part was supposed to be the join between the first two. Every
pondering step writes into the fast weights, so thinking reinforces the paths it
uses. Nobody had built that.

## What we found

We built it and tried to kill it first. Two arms, same parameter count, same
FLOPs, same seeds. Arm A writes to fast weights while pondering. Arm B reads
them but only writes between forward passes, which is the ordinary approach.

On a task easy enough that both arms hit 100 percent, they tied, and the harness
happily reported a verdict. That number was worthless. A ceiling cannot separate
two models. We raised the difficulty and ran it again.

![Falsification result](figures/png/recall.png)

At 240 training steps, twelve seeds:

| | writes while pondering | read only |
|---|---|---|
| mean recall | 0.5203 | **0.6557** |
| 95 percent interval | [0.4522, 0.5883] | [0.5953, 0.7160] |

The plain version wins by 13.5 points. Both arms carry 81,738 parameters and
matched forward FLOPs, so neither wins on budget. The arms are paired seed for
seed, starting from identical weights on identical batches, so the honest test is
on the per seed differences: paired t of 3.23 on 11 degrees of freedom, a 95
percent interval of [0.0431, 0.2277] that excludes zero, and read only winning on
10 of 12 seeds.

One thing this does not show. Arm A writes the fast tier about seven times more
often than Arm B, and the task is built so that extra writes hurt. So we have
shown the coupled setup learns slower, not that the timing of the writes is what
caused it. The arm that would separate those, same writes applied between passes,
is not run yet.

Then a reviewer asked the obvious question we had not answered: both arms were
still improving at step 240, so is this a real penalty or just slower start? We
trained four times longer to find out.

| | writes while pondering | read only |
|---|---|---|
| recall at 960 steps | 1.0000 | 1.0000 |

The gap closes completely. Every seed of both arms solves the task. So the
coupling does not break the model, it just makes it learn slower, and the honest
claim is a speed penalty at a fixed budget rather than a capability penalty. The
960 step run saturates, so it cannot tell us whether any difference survives at
convergence on a harder task. That is still unmeasured.

The same reviewer predicted a different failure, that the model would learn to
lower energy by rewriting memory until it agreed with itself. That did not
happen. The energy margin grew and held.

![Energy margin through training](figures/png/margin.png)

So the most interesting thing in this architecture currently pays no rent. That
is worth knowing after two days instead of after six months, which is the whole
reason we ran the experiment before building on top of it.

Details and caveats are in `experiments/falsify/FINDINGS.md`.

## Running it

```
py -m pip install -e ".[dev]"
py -m pytest -q
```

Reproduce the experiment:

```
py -m experiments.falsify.run --num-values 64 --distractors 16 \
    --interference 0.85 --train-steps 240
py experiments/falsify/analyze.py
```

Needs PyTorch with CUDA. Built against torch 2.11 and CUDA 12.8. Everything here
runs on one GPU.

## Layout

```
memoir/spec.py     the interface every module binds to, read this first
memoir/tiers/      weight tiers, delta rule, consolidation
memoir/ponder/     recurrent block, halting, tier coupling
memoir/energy/     latent prediction, energy head, abstention
memoir/meta/       discovered update rules
memoir/bench/      continual learning benchmark
experiments/       the falsification runs
bench/             performance profiling and the scaling story
figures/           figure sources and rendered images
docs/              architecture, results, limitations
```

Start with `docs/`. `docs/results.md` is the whole experiment told end to end,
and `docs/limitations.md` is the honest list of what this does not show.

## On the numbers

Every number here comes from `results/falsify/summary.json`. Nothing about this
model gets quoted until it has been run, and the raw per seed scores are written
for every run.

The benchmark is ours, which is a conflict of interest, so the protocol is
written to be checked by someone assuming bad faith. Every metric documents what
would make it look good for the wrong reason.

## Status

Early. 81k to 236k parameters. One task family. None of this transfers to a
large model by argument alone, and we do not claim it does.

## Sponsor this project

Everything above ran on one laptop GPU. We are looking for anyone willing to
sponsor this project with compute.

The next experiments are already named and scoped: the third arm that separates
write timing from write volume, a sweep over write strength, a task family that
stays below ceiling at convergence, and then the question that actually matters,
whether any of this holds at 1B parameters. We cannot fund a full training run
ourselves, and we would rather say that plainly than pretend otherwise.

What a sponsor gets is the way we work. Every number traceable to a run, claims
gated behind pre-registered tests, and negative results published with the same
care as positive ones. Write to jaber@rightnowai.co.

## License

Apache 2.0. See `LICENSE`.


