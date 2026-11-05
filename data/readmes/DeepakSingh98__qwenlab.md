qwenLab: Qwen runs its own ML lab
=================================

**qwenLab is an experimental model: Qwen3.5-9B with a small ML research lab compiled into it.**
It is not a plugin, a tool server or a Python sandbox. The lab is 2,382 layers appended to Qwen's own 32. None of
their weights are learned; every one is set by construction. Qwen trains, forks, evaluates and tests small transformers
through its normal tool calls, the lab layers answer every call, and Qwen reads the measured results and decides what
to try next. The host only asks the model for the next token.

[![One small transformer, made into six, put inside Qwen3.5-9B; Qwen trains them by writing commands](docs/demo.gif)](docs/demo.mp4)

*Every command, setting and score in the video comes from the recorded session in
[`results/research_r6`](results/research_r6). The per-step loss lines are the same experiments replayed in plain
PyTorch ([`video/curves.py`](video/curves.py)); the low-learning-rate runs match the session to 3-4 digits and the
high-learning-rate forks drift by a few points. Full video: [`docs/demo.mp4`](docs/demo.mp4).*

How it works
------------

### The calls

Qwen gets one tool, `city`, with one command per call. Six units, A to F, each hold a complete experiment: a
419,712-parameter transformer learning `a + b mod 97`, both Adam moments, its update counter, learning rate, weight
decay and data-stream position.

| command | what the lab does | lab ticks |
|---|---|---|
| `train U [U ...] N` | N full training updates (forward, cross-entropy, backward, AdamW) of each listed unit, side by side | 193 per update |
| `fork S D lr_scale X weight_decay Y` | copy unit S into D, then set D's learning rate and weight decay | 130 |
| `snapshot S D` | copy S into D unchanged | 130 |
| `eval U [U ...]` | validation loss and accuracy on 2,352 held-out equations | 295 |
| `test U [U ...]` | the same on a disjoint 2,353-equation test split, once at the end | 296 |

### Where the lab lives

- **Weights.** Every 128×128 weight block of every unit lives in a DeltaNet-style memory head: a 128×128 fp32 state
  you can read and write. Reading it with the activation as the query is the forward pass. Reading a transposed copy
  with the output gradient is the backward pass. AdamW reads and rewrites one row per tick, with one-hot writes,
  over 129 ticks.
- **Copies.** A head answers one query per position, so each block is stored in 2 layouts × 32 read copies: 1,686
  heads per unit, 11,892 in all.
- **Gradients** accumulate in hidden lanes that are fed back from one position to the next.
- **Data.** Batch sampling is an in-circuit Wang hash over 32 bit lanes (xor = a + b − 2ab), so the data order is
  part of the model too.
- **Language.** A grammar state machine in the lab masks Qwen's logits inside `<tool_call>` and decodes the command.
  A printer in the lab formats the results digit by digit and forces the `<tool_response>` tokens.
- **Routing.** While the lab runs a command, each position is a lab tick: Qwen's own 32 layers are skipped, so its
  caches don't grow.

### Exactness

- A float64 copy of the circuit matches textbook training math (PyTorch autograd + AdamW) to 1e-15 on loss, every
  gradient, both moments and the updated parameters.
- In fp32 the lab's gradient error is within PyTorch fp32's own error. Over 100 updates its train loss stays within
  4.3e-7 (relative) of the fp32 reference at every update.
- Forks are bitwise: an unchanged fork equals the uninterrupted run, and training a unit alongside siblings equals
  training it alone. Stopping mid-command, saving the whole lab to disk (790 MB of recurrent state), loading it into a
  fresh copy of the model and resuming gives the uninterrupted result bit for bit. These fork checks ran on a
  toy-vocabulary build of the same lab circuit.

What runs where
---------------

| work | where |
|---|---|
| learner forward, loss, full backward, AdamW, weight decay, warmup | lab layers |
| batch sampling, update counters, forks, snapshots, evaluation | lab layers |
| parsing Qwen's tool call, printing the results | lab layers |
| choosing every setting, reading the results, deciding round 2 | Qwen3.5-9B (weights unchanged) |
| host | loads weights and the initial learner state, calls the model one position at a time, samples tokens, logs |

The host never parses a command, never does learner math and never picks a setting.

Results
-------

One session, `results/research_r6` (8 minutes on one H100). The prompt fixed the protocol: train A for 200 updates,
freeze it as parent F, fork three settings of Qwen's choosing plus an unchanged control E, train each 50 updates,
evaluate, then a second round. Qwen chose every learning rate and weight decay.

| round | unit | Qwen's setting (lr ×, weight decay) | val loss | val accuracy |
|---|---|---|---|---|
| 1 | E (control) | 1, 1 | 2.8987 | 15.90% |
| 1 | B | 0.5, 0 | 3.1739 | 11.99% |
| 1 | C | 2, 1 | 2.2058 | 31.93% |
| 1 | D | 4, 2 | 2.3329 | 25.30% |
| 2 | A | 8, 0.5 | 2.8254 | 11.35% |
| 2 | B | 6, 1.5 | 2.6610 | 12.84% |
| 2 | D | 3, 3 | 1.7654 | **49.53%** |
| test | D / E | | 1.7965 / 2.9022 | **49.09%** / 15.68% |

Qwen's round-2 reasoning, verbatim: "Round 1 results show unit C (lr_scale=2.0, weight_decay=1.0) is the best ...
trying higher learning rates and moderate weight decay."

Every printed number equals an independent reference evaluator applied to that unit's parameters, to all printed
digits. The session ran 59,829 lab ticks and 550 training updates in total.

Limits
------

- **Qwen is heavily modified.** The lab has its own residual stream, far wider than Qwen's 4,096, and is 2,382 layers
  against Qwen's 32. It reads Qwen's tokens and adds to Qwen's logits; Qwen's own weights are unchanged.
- **The memory heads are modified** from Qwen's Gated DeltaNet layers: fp32 state, no q/k norm, no conv, no output gate.
- **One session**, with the protocol fixed by the prompt. "Raise learning rate and weight decay to grok faster" is
  textbook, not a discovery. Qwen's closing summary also misstates that the control E got no further training; E
  trained 50 updates like the others.
- **Slow.** 0.64 s per training update inside the model, against 5.5 ms for the same update in plain PyTorch on the
  same H100. This shows it can be done; it is not a speedup.
- **Narrow interface.** Only learning rate and weight decay are exposed in the command language. There are no
  architecture changes, and counters stay below 65,536.
- **Fragile setup.** Earlier sessions failed: with thinking mode on, Qwen looped for 40k tokens; without a declared
  tool, it wrote the command in a code block. The fixes were non-thinking mode, a presence penalty and the native tool
  declaration.

Quickstart
----------

The full session needs Linux and one 80 GB GPU (peak memory 19.8 GB). It was run with torch 2.9.1+cu128 and
transformers 5.22.1.

```bash
git clone <this repo> && cd qwenlab
pip install -e .
python research.py --model Qwen/Qwen3.5-9B --revision c202236235762e1c871ad0ccb60c8ee5ba337b9a --out runs/r6
```

Checks:

```bash
python checks/smoke.py                                   # CPU, seconds: build the lab, check the data path
python checks/update_check.py --c 8 --device cpu         # one full in-model update vs float64 and fp32 references
python checks/traj_check.py --updates 100 --device cuda --graph --out traj.json
python checks/city_check.py --device cuda --graph --out city.json   # forks, isolation, save/reload/resume
python video/render.py                                   # rebuild docs/demo.mp4 from the recorded session
```

Repository
----------

| path | what it is |
|---|---|
| `rcq/ir.py` | the layer types and the tick-by-tick executor (CUDA-graph capture) |
| `rcq/engine.py`, `rcq/learner.py`, `rcq/intops.py` | the lab: learner circuit, AdamW rows, integer and hash circuits |
| `rcq/language.py` | the command grammar and the result printer |
| `rcq/qwen_trunk.py`, `rcq/session.py` | Qwen3.5-9B trunk, routing and sampling |
| `rcq/grok.py`, `rcq/reference.py` | the learner in plain PyTorch: the independent reference the lab is checked against |
| `research.py` | the research session (the prompt and protocol are at the top) |
| `checks/` | exactness, fork and resume checks |
| `results/` | receipts: update checks, trajectory, fork checks, the full session transcript and event log |
| `docs/DESIGN.md` | design and the numerical contract, written before any results |
| `docs/REPORT.md` | the full report |
| `video/render.py`, `video/curves.py` | the demo video, and the PyTorch replay behind its loss curves |

Related
-------

Part of the run of computers compiled into Qwen: a CPU (qwenputer), a GPU (qwenGPU),
[qwenFS](https://github.com/vixhal-baraiya/qwenFS) and [qwenTPU](https://github.com/Bobliuuu/qwentpu). No shared code.

License
-------

Code: MIT ([LICENSE](LICENSE)). Qwen3.5-9B weights are downloaded from Hugging Face under Qwen's Apache-2.0 license
and are not distributed here.
