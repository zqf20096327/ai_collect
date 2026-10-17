# BIM 2

A biologically inspired sequence learning architecture. No backpropagation. No GPU. No pretraining.

BIM 2 is the second generation of BIM (Biologically Inspired Model). BIM 1 proved one-shot sequence memorization. BIM 2 adds surprise-scaled learning, hierarchical top-down feedback, online correction, concept formation, and synaptic homeostasis.

---

## How the learning actually works

Before each token arrives, BIM predicts which sparse columns should activate next, based purely on what it has learned so far. When the real token arrives, its actual SDR is compared to that prediction using Jaccard distance:

```
surprise = 1 - |predicted columns ∩ actual columns| / |predicted columns U actual columns|
```

That surprise value directly scales the Hebbian learning rate. If BIM predicted perfectly, surprise = 0 and the learning rate is zero. Nothing changes. If BIM was completely wrong, surprise = 1.0 and full Hebbian potentiation fires. The system only updates synapses when it was wrong, and by exactly how much it was wrong.

This is the only training signal. No loss function. No optimizer. No labels. No gradients.

---

## Architecture

### Spatial Pooler
Converts token IDs into Sparse Distributed Representations. Each token maps to exactly 64 active columns out of 16,384. Tokens that appear in similar contexts drift toward overlapping SDR patterns through competitive Hebbian learning.

### Two-Layer Hierarchical Cortex
L1 (sensory) handles word-to-word sequence transitions. L2 (abstract) receives a decaying temporal pool of L1 activity with a decay factor of 0.8 per step, which lets phrase-level context persist beyond individual tokens.

Phase 7 wires top-down feedback from L2 back into L1 via apical bias. L2's predictions modulate which L1 cells stay predictive, the same direction of signal flow that exists in biological cortical layers.

### Numba JIT Learning Rules
The Hebbian potentiation and LTD loops are compiled to native LLVM machine code via `@njit(cache=True)`. When surprise = 0, the guard `if lr > 0.0:` skips the JIT call entirely. No wasted cycles on sequences the model already knows.

### Winner Cell Disambiguation (Phase 4)
When a column bursts (no prediction was active), BIM uses context to pick which cell becomes the winner. It scores each candidate cell by overlap with the previous winner cells through existing synaptic connections. Novel contexts get the least-used cell. Repeated contexts reuse the same cell. This is what allows the same token to mean different things in different sequence contexts.

### ConceptGraph
After an L2 SDR pattern repeats above a threshold, it crystallizes into a named concept. Concepts form weighted edges based on co-occurrence within a phrase. BFS traversal at depth 2 enables multi-hop inference: if A knows B and B knows C, asking about A can surface C.

### SynapticHomeostasis
Every 500 steps, if any cell's total synapse permanence exceeds 120% of the target budget, the whole cell scales down proportionally. This prevents a small set of high-permanence cells from dominating everything. It is the biological equivalent of synaptic scaling, and it runs in pure NumPy in about 2ms on 131k cells.

### Working Memory
Stores recent (input SDR, response SDR, surprise) tuples with exponential decay. Surprise scores decay by 0.95 per step. High-surprise exchanges persist longer. This is how context from earlier in a session influences later responses.

---

## Architecture overview

```
Token input
     |
Spatial Pooler (16,384 columns, sparsity = 64 active bits)
     |
L1 Sparse Cortex (8 cells/column, 256 synapses/cell)
     |  ^
     |  | apical bias (Phase 7 top-down)
     v  |
Temporal Pool (decay = 0.80 per step)
     |
L2 Abstract Cortex
     |
ConceptGraph (BFS inference, depth 2)
```

Total cells: 131,072. All on CPU.

---

## Running it

```bash
pip install numpy numba scipy
```

Start the REPL:
```bash
python main.py interact
```

Start fresh (ignore existing checkpoint):
```bash
python main.py interact --fresh
```

The REPL responds with one predicted token per input. For multi-token generation, use `generate()` directly in Python:

```python
from interaction.loop import BIMInteraction
from utils.save_load import load_checkpoint

bim = BIMInteraction()
load_checkpoint(bim)
print(bim.generate("zara directs", max_tokens=5))
```

Correct a wrong response mid-conversation:
```
You: who leads novacorp
BIM: liam
You: WRONG: liam RIGHT: zara
BIM: Corrected. (N permanences updated)
```

Check current stats:
```bash
python main.py stats
```

Run the domain knowledge benchmark:
```bash
python main.py benchmark
```

---

## The benchmark

The benchmark teaches BIM a fictional corpus about a company called NovaCorp, then tests direct recall and 2-hop inference. The corpus is fictional so there is zero chance of prior exposure.

Example facts taught:
```
zara directs novacorp
liam patents prism
zara mentors liam
liam trains maya
```

Example queries after teaching:
```
"zara directs"    -> expected: novacorp   (direct recall)
"liam trains"     -> expected: maya       (direct recall)
"zara mentors"    -> expected: liam       (1-hop chain)
```

Pass gates: direct recall >= 60%, inference >= 30%.

---

## What BIM 2 adds over BIM 1

| | BIM 1 | BIM 2 |
|--|-------|-------|
| Learning signal | Fixed Hebbian LR | Jaccard surprise-scaled LR |
| Response | Single predicted token | Single token + autoregressive generate() |
| Correction | None | WRONG/RIGHT permanence update |
| Concepts | None | ConceptGraph (crystallize, edges, BFS) |
| Context disambiguation | Cell 0 always chosen | Phase 4 winner cell selection |
| Top-down feedback | None | L2 apical bias into L1 |
| Homeostasis | None | Synaptic scaling every 500 steps |
| Working memory | None | SDR-based decaying exchange buffer |
| Reward signal | None | Scalar reward learning on prev/curr winners |
| Checkpointing | Basic | Full state (NumPy arrays + JSON) |
| Benchmarking | Throughput only | Domain knowledge + inference accuracy |

---

## Honest limitations

**Single-token REPL responses.** The interactive loop decodes one predicted token per input. For full phrase generation, call `generate()` with `max_tokens`.

**Word-level tokenizer.** Vocabulary cap is 5000 tokens. "run", "runs", and "running" are three separate unrelated tokens. BPE tokenization would give generalization across word forms.

**No open-domain knowledge.** BIM 2 knows only what it has been explicitly taught in the current session or loaded from a checkpoint. It does not hallucinate. It retrieves.

**Inference is shallow.** The ConceptGraph does BFS at depth 2. Longer chains require more edges formed through more exposure.

---

## Lineage

BIM 0 introduced the conversation loop and dialogue memory. BIM 1 proved one-shot sequence memorization at 160+ TPS on CPU. BIM 2 adds the full biological learning stack on top of BIM 1's cortex substrate.

BIM 0 is on GitHub separately. BIM 1 is in the `bim1/` directory of this repo.

---

Part of UnikAI / Nucleus AI research. Independent. No institution. No funding.
