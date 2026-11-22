# Alcyone

**W-JEPA: a joint-embedding predictive architecture whose target is a topological invariant, not a learned embedding.**

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)
[![Weights](https://img.shields.io/badge/weights-Hugging%20Face-555)](https://huggingface.co/teerthsharma/Alcyone-W)
[![Lean 4](https://img.shields.io/badge/Lean%204-1%2C818%20declarations%2C%20no%20sorry-5b3cc4)](https://huggingface.co/teerthsharma/Alcyone-W/tree/main/lemmas)
[![Data](https://img.shields.io/badge/data-CMS%20Open%20Data-0b7285)](https://opendata.cern.ch)

Teerth Sharma · [teerth.dev](https://teerth.dev) · [teerth.blog](https://teerth.blog)

<img src="assets/pipeline.svg" alt="Alcyone pipeline: event, land, hidden window, watershed" width="100%"/>

## Why I made this

Every day AI makes some new thing, and every day the water rises a little. After a while it feels like the flood is swallowing you up.

A mathematician has one reliable response to a flood: work out its watershed. Where does the water collect, which basins merge first, and which one is left standing at the end? So I built an AI whose whole job is exactly that question. If AI is going to be a flood, I want one that knows where the water goes.

## The idea

Take a proton-proton collision. Spread each particle's transverse momentum over the (η, φ) cylinder and turn the result upside down, so that energy becomes depth. You now have a landscape. Hide a window of it, and ask a network one question about the hidden part:

> *If it rained, where would the water collect?*

That is: how many basins the window contains, how long each one survives as the water level rises, and how much water each one holds. You cannot answer this by memorising pixels. You have to know the shape of the event.

## Why the target is the interesting part

Every JEPA so far (I-JEPA, V-JEPA, Graph-JEPA, Point-JEPA) minimises something like

$$\mathcal{L}(\theta) = \mathbb{E}_{x,W}\, \ell\big(g_\theta(f_\theta(x|_{W^c})),\; \bar f(x|_W)\big),$$

where $\bar f$ is itself a network, usually an EMA copy of $f_\theta$. The pair $(f, \bar f)$ then has a cheap solution: map everything to a constant. Much of the JEPA literature is the engineering that keeps the optimiser away from that point.

W-JEPA replaces $\bar f$ with a fixed function of the data,

$$T(x, W) = \Big(\beta_0(W),\; (\mathrm{pers}_1, \dots, \mathrm{pers}_8),\; (E_1, \dots, E_{\beta_0})\Big),$$

the number of basins in the window, their H0 persistences under the elder rule, and the energy each basin holds. $T$ is computed exactly by a union-find flood. Since $T$ does not move during training, there is no constant to collapse onto: a constant predictor is pinned at the majority-class rate, and the model has to beat that by looking at the event. No EMA teacher, no stop-gradient, no variance regulariser.

Collapse needs the target to cooperate. This target is a theorem, and theorems do not cooperate.

To our knowledge this is the first JEPA with a topological target (literature search, November 2026; we will credit earlier work if it turns up).

## What is proved, what is learned

> Compute what the lemmas determine; learn only what they leave open.

The flood is not a heuristic. Its rules are theorems in Lean 4:

- **The $\beta_0$ step.** Adding an edge either merges two components or changes nothing. Topologists have a Greek letter for "number of things", and they are proud of it.
- **The elder rule.** When two basins meet, the younger one dies and the elder keeps its label. This is also how most arguments at a seminar end.
- **Conservation under spill.** When two basins merge, their volumes add. Water is neither created nor destroyed, only relabelled.
- **$n - 1$ merges.** A connected graph on $n$ vertices sees exactly $n - 1$ merge events, whatever order the edges arrive in. It is the fencepost problem, now with water.
- **Graph Poincaré–Hopf.** Summing $1 - (\text{number of lower edges})$ over the vertices gives $|V| - |E| = \chi$. You cannot comb a hairy ball, and you cannot drain a landscape without the indices adding up to the Euler characteristic.

Across the libraries this comes to **1,818 built declarations with no `sorry`**, counted from build manifests, plus executable Haskell mirrors checked with QuickCheck. The source is in [`lemmas/`](https://huggingface.co/teerthsharma/Alcyone-W/tree/main/lemmas) on Hugging Face.

What remains for learning is small:

| component | parameters | status |
|---|---|---|
| W-JEPA encoder and predictor | 5,893,976 | trained |
| Galactica-6.7B | 6,657,359,872 | frozen; loaded from `facebook/galactica-6.7b`, not redistributed |
| hydraulics (union-find flood, elder rule, conservation) | 0 | the lemmas, as code |

About 6.66B parameters in total, of which 5.9M are trained.

## The construction

1. **Terrain.** Muons, electrons and jets deposit $p_T$ on a $32 \times 64$ grid over $(\eta, \phi)$, periodic in $\phi$. The Gaussian kernel conserves the total exactly. Height is $h = -\log(1 + \text{deposit})$, so energy concentrations are basins.
2. **Land.** Each object gets a plain caption, e.g. `muon, negative charge, pT 40 GeV, eta 1.0`. A frozen Galactica-6.7B embeds it (layer 24, mean-pooled), a PCA fitted on training captions reduces it to 8 dimensions, and the result is deposited with the same kernel as 8 further channels. The language model contributes geometry, not text.
3. **Mask.** A random $8 \times 16$ window is hidden. A convolutional encoder on the cylinder sees the complement.
4. **Predict.** The predictor outputs $T(x, W)$ and is scored against the exact flood of the full event.

## Results

All bars were registered before training, and all outcomes are reported.

**The training task.** Basin count of the hidden window:
- **0.945** accuracy on 512 events from a held-out source file, against **0.572** for the majority class;
- **0.936** on 4,096 fixed validation windows.

**Does the land help?** Frozen encoder, MLP probe, 3 probe seeds, 200k held-out events:

| task | Alcyone | same W-JEPA, flat land | kinematics MLP |
|---|---|---|---|
| jet multiplicity (MSE) | **0.0103** | 0.0796 | 0.0016 |
| dimuon mass, leading muon hidden (MSE) | 25,211 | 25,629 | 24,640 |
| hidden-lepton charge (accuracy) | 0.503 | 0.502 | 0.500 |

For jet multiplicity the Galactica land cuts the error by 85–87%. The effect survives every control we could think of, on all three training seeds:

| control | Alcyone's error is lower by |
|---|---|
| shuffled captions (same embeddings, wrong particles) | 84–87% |
| a smaller language model, Galactica-125m | 18–23% |
| a parameter-free caption code | 40–51% |

So the gain depends on the captions being attached to the right particles and on the size of the model reading them. Something in the geometry of a 6.7B scientific language model helps with counting jets, and nobody asked it to learn that.

**Where it stands.** The pre-registered land bars (WL1–WL5) asked for a gain on two of the three tasks, and the release has one. A plain kinematics MLP still does better on both answerable tasks; we report this the way one reports a counterexample, promptly and with mild annoyance. On charge the model scores 0.503 on a two-class problem, which is a coin, and we have checked the coin. That one is not a mystery: the terrain has no charge channel, so the information is not there to find. A separate pre-registered run (not the released checkpoint) then added a signed charge channel and a Gauss target. Charge became learnable: 0.619, against 0.539 without the Gauss target and 0.573 for a frozen random encoder, on all three probe seeds. It still falls short of the one-line Gauss rule (minus the sign of the visible charge sum), which scores 0.652 with no parameters, so bar C1 failed and we do not claim that the network reads charge topologically. The lemma beats the learner, which is what lemmas are for.

**A topology-native encoder (lab result, not the released checkpoint).** A second pre-registered run replaced the CNN with an encoder that contains no convolution. Eight pointwise height functions of energy and charge, started at the lemma filtrations h, h ± q, are flooded exactly by union-find (H0 persistence, elder rule, C kernel checked against the reference flood on 2,000 fields), and a set-function reads the persistence diagrams. With 547k encoder parameters against the CNN's 5.9M, it beats the CNN on charge (0.665 against 0.619) and on dimuon mass (3% lower error), and it is the first variant above the Gauss rule (0.665 against 0.652). It is twice as bad as the CNN on jet multiplicity. The honest caveat is bar N1: the same architecture with random weights already reaches 0.660 on charge, so the gain comes from the lemma filtrations and the exact flood, not from training. Learning the filtration helps only on jet multiplicity (8–13%). The kinematics MLP is still best on all three tasks. Its code and weights are not in this release yet.

**Text inside the topology-native encoder (lab result).** A third pre-registered run let each height function also read the eight Galactica-6.7B caption channels, so the language model's reading of each particle shapes the land that is flooded. Nothing after the input changed: no convolution, exact persistence, a set-function on the diagrams. Against the same encoder without text, jet-multiplicity error falls from 0.094 to 0.016 (3/3 probe seeds), and against the same channels attached to shuffled captions it falls from 0.063 to 0.016, so the gain comes from the text, not from extra inputs (bars X1 and X2 passed). Dimuon-mass error is 1.3–1.9% lower than without text, below the 5% bar, and 0.9% below the kinematics MLP on all three seeds; this is the first variant to edge that baseline on any task, though the comparison was not a pre-registered bar. Charge is 0.004 worse than without text and stays above the Gauss rule (X4 passed). Bar X3 failed: trained weights beat random weights only on jet multiplicity, so the other gains are not credited to training. On jet multiplicity the released CNN with text (0.011) and the kinematics MLP (0.0014) are still better. Code and weights are not in this release yet.

## Usage

```bash
git clone https://github.com/teerthsharma/Alcyone-W && cd Alcyone-W
hf download teerthsharma/Alcyone-W --local-dir .
pip install -r requirements.txt
python examples/example.py
```

The example runs on the 512 held-out CMS events that ship with the weights and needs no Galactica download for them.

```python
import sys; sys.path.insert(0, "code")
from alcyone import WatershedJEPA, exact_summary, window_mask

m = WatershedJEPA(".", galactica="facebook/galactica-6.7b")
z = m.encode(x)                       # x: (N, 15, 8) [pT, eta, phi, mass, charge, type, btag, valid]
win = window_mask(12, 24, len(x))
pred = m.predict_summary(x, win)      # basin-count probabilities, persistence, energy per basin
true = exact_summary(x, win)          # the exact flood
```

## The agent

`code/agent.py` lets you ask Alcyone questions through the frozen Galactica-6.7B, which may only answer through four deterministic tools:

| tool | function |
|---|---|
| `watershed(k)` | W-JEPA prediction beside the exact flood |
| `charge(k)` | Gauss-law readout |
| `describe(k)` | object list |
| `calc(expr)` | arithmetic |

Galactica is not instruction-tuned, so the runtime enforces the protocol: tool first, answer second, and any number no tool produced is flagged. Think of it as a referee who insists that every constant in the proof be computed, not asserted. Asked who it is, it answers from fixed text ([`ALCYONE_RULES.md`](ALCYONE_RULES.md)).

## Open problems

These are the questions we find most interesting. Start with the [introduction thread](https://github.com/teerthsharma/Alcyone-W/discussions/1), then bring questions to [Q&A](https://github.com/teerthsharma/Alcyone-W/discussions/categories/q-a), new directions to [Ideas](https://github.com/teerthsharma/Alcyone-W/discussions/categories/ideas), and things you have built to [Show and tell](https://github.com/teerthsharma/Alcyone-W/discussions/categories/show-and-tell). Bugs go in [Issues](https://github.com/teerthsharma/Alcyone-W/issues).

- **Other invariants.** $\beta_0$ of sublevel sets is the simplest choice. What about $\beta_1$, merge trees, or the full persistence diagram as the target? Lakes are $\beta_0$; islands in lakes are where it gets interesting.
- **Other spaces.** Nothing here is specific to collisions. Any data with a natural height function (images, fields, point clouds with a density, graphs with node weights) admits the same construction.
- **Leakage at the boundary.** Deposits near the window edge are partly visible from outside, so part of the target is predictable from context. What is the right notion of a clean window?
- **Why does the land help?** Shuffled captions destroy the effect and a smaller model weakens it. Which directions in Galactica's layer 24 carry it?
- **Charge.** With a charge channel the network learns charge (0.619) but stays below the parameter-free Gauss rule (0.652). Can a learned model add anything the lemma does not already give?

## Data and provenance

- **Data:** CMS Open Data (CERN Open Data portal), NanoAOD. 4M events with at least one lepton, split by source file: 2.24M train, 1.06M validation, 693k test. 512 test events ship with the weights.
- **Checkpoint:** training seed 1 of three, 38,155 steps, selected by a rule fixed in advance (lowest final masked-summary loss).
- **Freeze checks, every run:** Galactica's weight hashes are unchanged after training, no Galactica parameter requires gradients, 1,000 captions re-embed bit-identically, and the land table's hash matches its provenance.
- **Galactica:** Taylor et al., *Galactica: A Large Language Model for Science*, Meta AI, 2022.

## License

CC BY-NC 4.0. The land table and projection derive from Galactica-6.7B outputs, and Galactica is licensed CC BY-NC 4.0. Galactica's weights are not included.

---

*Alcyone is the brightest star of the Pleiades. It shares its name with another Alcyone of myth, who became a kingfisher after her husband drowned at sea. Every winter her father, the keeper of the winds, calms the storms so she can nest on the water. Those are the halcyon days. It seemed the right name for an AI that is not afraid of floods.*
