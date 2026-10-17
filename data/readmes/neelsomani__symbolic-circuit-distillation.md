# Symbolic Circuit Distillation: Automatically Extracting Human-Readable Algorithms From Mechanistic Circuits

## Abstract

Mechanistic interpretability increasingly reveals small, crisp circuits that implement algorithmic behaviors inside transformers, such as delimiter matching, simple counting, or type tracking. However, converting these neuron- and channel-level circuits into faithful, human-readable explanations still requires extensive manual effort and bespoke reasoning.

We introduce Symbolic Circuit Distillation, a method for automatically converting neuron-level circuit graphs into concise, executable programs with bounded formal correctness guarantees. Given a pruned circuit extracted from a sparse model or from dense-model feature spaces (e.g., SAE features or attribution graphs), we treat the circuit as an executable teacher. We first train a small ReLU surrogate network to exactly match the circuit's behavior on a bounded token domain. We then synthesize candidate high-level programs by exhaustively instantiating a constrained, template-guided DSL designed around common transformer circuit motifs (counters, toggles, threshold detectors, small state machines). Finally, we use SMT-based bounded equivalence checking to certify whether any template-instantiated program matches the surrogate on all inputs in the bounded domain (typically 5-10 tokens), or else return a concrete counterexample.

We validate Symbolic Circuit Distillation on mechanistic behaviors studied in prior interpretability work, including string closing and bracket-depth detection, and show that the method (1) automatically recovers the algorithmic motifs identified by prior work, (2) matches pruned-circuit behavior to high fidelity, and (3) exposes subtle circuit-level failure modes difficult to detect from the raw graph. These results demonstrate that symbolic distillation can automate a core bottleneck in mechanistic interpretability: the translation from circuit graphs to clean, verified algorithms.

## 1. Introduction

Transformers exhibit a wide variety of internal algorithmic behaviors, from simple syntactic rules to multi-step reasoning processes. Recent interpretability work has shown that, with suitable inductive biases such as weight sparsity, these behaviors can be localized into small, disentangled circuits consisting of a handful of neurons, channels, and attention interactions. Yet even when a compact circuit is found, converting it into a human-understandable algorithm remains a slow, manual process requiring:

* identifying functional subcomponents,
* understanding interactions by hand,
* inferring latent state variables (e.g., depth counters),
* rewriting mechanisms into an algorithmic form, and
* validating that the explanation is faithful.

This manual pipeline does not scale.

**Our Goal.**
Enable a researcher (or an automated interpretability system) to turn a small neural circuit into a verified, executable algorithm automatically.

**Key Idea.**
Treat the pruned circuit as an executable black-box, distill it into a compact symbolic representation, and certify or refute equivalence between the circuit's computation and a synthesized program drawn from a fixed template family, returning a counterexample when equivalence fails.

This project does not attempt to interpret full-scale LLMs. Instead, we target small, well-isolated mechanistic circuits (5-20 nodes), which are the standard setting for algorithmic mechanistic interpretability benchmarks. To keep synthesis tractable and interpretable, we restrict the search to a finite template family (e.g., single-pass programs with one integer state variable and two guarded update rules).

### 1.1 Why toy algorithmic tasks?

We evaluate on tasks such as quote-type tracking and bracket-counting (canonical benchmarks in mechanistic interpretability) because they:

* have known ground-truth algorithms,
* fit within small bounded token domains,
* produce crisp circuits, and
* allow rigorous verification.

This follows the methodology of prior work (e.g., Gao et al. 2025), and serves as the ideal proving ground for automated interpretability systems.

### 1.2 Scientific Questions

This work uses symbolic circuit distillation not only as a methodology but as a lens for answering concrete scientific questions about mechanistic circuits. We focus on three questions that arise naturally in the mechanistic interpretability literature:

1. **Algorithmic Stability.**
   Do pruned transformer circuits implement stable algorithmic motifs that can be robustly recovered within a constrained symbolic program family?

2. **Faithfulness of Canonical Explanations.**
   To what extent do the canonical human explanations of circuits (e.g., toggles, depth counters) match the exact function these circuits compute over bounded domains?

3. **Hidden Failure Modes.**
   Do seemingly clean mechanistic circuits contain subtle behaviors or edge cases that are difficult to detect through attribution- or ablation-based inspection?

Our method is designed specifically to probe these scientific questions: it enables explicit hypothesis testing, formal refutation via counterexamples, and automated recovery of algorithmic structure.

## 2. Contributions

Our contributions are:

1. **A pipeline for automatically converting mechanistic circuits into executable algorithms.**
   Given a pruned circuit (from sparse models, SAEs, or feature-based circuit tracing), we distill it into compact, human-readable code.

2. **A surrogate modeling technique enabling formal reasoning.**
   We train a small ReLU network that exactly matches circuit behavior on a bounded domain and can be symbolically encoded for SMT.

3. **SMT-based formal equivalence checking on a bounded domain.**
   We provide bounded correctness guarantees by certifying when a template-instantiated program is equivalent to the surrogate (and thus the circuit) for all in-domain inputs.

4. **A constrained, template-guided DSL capturing common transformer circuit motifs.**
   Our DSL includes counters, toggles, linear accumulators, gating predicates, and simple state machines. For each task, we define a finite template family with fixed control flow and a discrete parameter grid.

5. **Automatic algorithm synthesis and code generation.**
   We exhaustively enumerate all instantiations of the template family, filter by circuit agreement, and formally verify surviving candidates before rewriting them into Python-like code.

6. **Empirical validation of correctness and insight.**
   On tasks such as quote classification and bracket counting, the system recovers known motifs, reveals subtle failure modes (e.g., averaging behavior), and matches circuit outputs with high fidelity.

## 3. Background

### 3.1 Pruned Circuits as Mechanistic Artifacts

Prior work has shown that pruning (or using sparse autoencoders) can isolate the minimal set of neurons, channels, and attention interactions responsible for specific behaviors. These pruned circuits behave deterministically on bounded token domains and form ideal subjects for algorithmic extraction.

### 3.2 Why Distillation?

Raw circuits are difficult for humans to parse:

* hundreds of small scalar weights,
* polysemantic interactions,
* implicit state carried in activation magnitudes.

Distillation compresses this complexity into structured programs with explicit state.

## 4. Methods

### 4.1 Circuit to Surrogate Distillation

We treat the pruned circuit as a deterministic function:

$$f_\text{circuit}: X \to Y$$

where $X$ is a bounded token domain (e.g., all sequences up to length 8) and $Y$ is a task-specific output (e.g., logits or binary decisions).

We train a small ReLU network. This surrogate is piecewise linear, symbolically encodable,  and dramatically simpler than the circuit. The surrogate serves as the bridge to formal verification.

### 4.2 SMT-Based Formal Equivalence Checking

To encode the surrogate, each ReLU unit introduces a piecewise-linear constraint:

$$y = \max(0, Wx + b)$$

Flattening this across layers gives a symbolic encoding suitable for an SMT solver (Z3). Piecewise-linear regions are represented via standard ReLU-SMT constraints.

Candidate DSL programs are translated into symbolic constraints on input-output behavior.

Finally, we query whether there exists any input in the bounded domain where the surrogate and program disagree:

$$\exists x \in X: g_\theta(x) \neq P(x)$$

* Unsat: The program is provably equivalent on-domain.
* Sat: The solver returns a concrete counterexample, which we use to refine synthesis.

This creates a tight verification loop.

### 4.3 Template-Guided Program Synthesis

We define a small DSL containing:

* integer counters with inc/dec
* boolean toggles
* comparisons and token predicates
* structured update rules

The system searches over templates such as:

```
state = INIT
for tok in input:
    if predicate(tok):
         state = update(state)
return output_fn(state)
```

or:

```
depth += (tok == "[") - (tok == "]")
```

The template instantiation that best matches the circuit across all training examples is passed to formal verification. Our synthesis is complete only over the task-specific template family. We do not enumerate all programs expressible in the full DSL.

### 4.4 Human-Readable Algorithm Extraction

Once a program is verified, we pretty-print it into Python-like code:

```
depth = 0
for tok in input:
    if tok == "[":
        depth += 1
return depth > 1
```

This gives clear, interpretable descriptions of neural circuits without manual intervention.

## 5. Experimental Setup

### 5.1 Metrics

We evaluate on tasks commonly used to study mechanistic circuits: quote closing (single vs double) and bracket counting (flat vs nested). Circuits were extracted using pruning from weight-sparse models.

Measured results:

| Task  | DSL vs. Gao circuit (Gao dataset) | Surrogate vs. Gao circuit (finite domain) |
|-------|----------------------------------|-------------------------------------------|
| Quote | 100%                             | 100%                                      |
| Bracket | 100%                           | 100%                                      |

For quote closing, no program in the (restricted) template family is formally equivalent to the circuit on the bounded domain. The solver returns a concrete counterexample:

```
[QUOTE] formal equivalence: False
[QUOTE] counterexample (abstract domain): [2, 0, 2]
[QUOTE] counterexample (actual tokens): [0, 1, 0]
[QUOTE] counterexample (rendered): ['!', '"', '!']
[QUOTE] outputs (actual tokens) -> teacher: 6, program: 1, surrogate: 6
[QUOTE] outputs (rendered) -> teacher: ', program: ", surrogate: '
```

For bracket counting, the synthesized program matches the circuit and surrogate on all inputs in the bounded abstract domain, and the solver confirms equivalence:

```
[BRACKET] program vs teacher (Gao dataset): accuracy 1.0 disagreements 0
[BRACKET] program vs teacher (abstract domain): accuracy 1.0 disagreements 0
[BRACKET] surrogate vs teacher (abstract domain): accuracy 1.0 disagreements 0
[BRACKET] formal equivalence: True
```

The pipeline can be applied to additional mechanistic behaviors to populate:

* Surrogate accuracy vs circuit
* Template-instantiated program accuracy vs circuit
* Solver result (SAT/UNSAT)
* Counterexamples (if any)
* Fidelity on adversarial or extended sequences

### 5.2 Scientific Findings

#### Evidence for Algorithmic Stability (Q1)

For quote-type tracking, symbolic distillation recovers the same high-level motifs described in prior mechanistic analyses (e.g., toggles and additive counters). This supports the view that small pruned circuits consistently implement stable algorithmic patterns that can be rediscovered through constrained program synthesis.

#### Deviations from Canonical Explanations (Q2)

For the quote-closing circuit, no program instantiation within the template family is formally equivalent on the bounded domain. The SMT solver returns concrete counterexamples illustrating behaviors inconsistent with the standard "toggle" interpretation. This provides direct evidence that canonical explanations can omit subtle but systematic deviations in the underlying circuit logic.

#### Discovery of Hidden Failure Modes (Q3)

The solver-generated counterexamples expose input sequences where the circuit behaves differently from any succinct template program, despite appearing clean under standard pruning- and attribution-based inspection. These discrepancies reveal latent failure modes that are difficult to detect from raw circuit graphs, illustrating the value of formal verification for mechanistic analysis.

## 6. Environment & Usage

### 6.1 Run Instructions

We use the following environment:

- Python version 3.11.8 (using venv)
- Set the environment flag `GAO_ONLINE=1` to allow loading Gao artifacts and teachers

You can run unit tests with `pytest`. To run the full end-to-end program search, surrogate fitting, and equivalence demo, run:

```
GAO_ONLINE=1 python scripts/run_equivalence_demo.py --quote --save
```

Alternatively, you can pass `--bracket` or omit flags to run both demos. The `--save` flag writes artifacts to `results/`.

### 6.2 Artifacts & Metrics

- Distilled programs (serialized DSL): `results/best_quote_program.json`, `results/best_bracket_program.json`.
- Rendered Python: `results/best_quote_program.py`, `results/best_bracket_program.py`.
- Surrogate IRs: `results/surrogate_quote_ir.json`, `results/surrogate_bracket_ir.json`.
- Metrics + counterexamples: `results/quote_metrics.json`, `results/bracket_metrics.json`

## 7. Limitations

Our guarantees are bounded and do not extend to arbitrary-length sequences. Surrogates and SMT encodings scale poorly with increasing circuit size.

The DSL includes the handful of algorithmic primitives (counters, toggles, thresholding, simple state transitions) that characterize the pruned circuits in prior mechanistic interpretability benchmarks. Our method certifies equivalence only within the chosen template family. It does not rule out the existence of more complex equivalent programs outside this family. 

Full-model interpretability remains out of scope.

## 8. References

This work builds directly on the sparse-circuit methodology introduced in:

* Gao et al. (2025). *Weight-sparse transformers have interpretable circuits.*
  Source code and models available at `openai/circuit_sparsity`.

We also draw on prior work in mechanistic interpretability and sparse feature extraction, including:

* Olsson et al. (2022). *In-context Learning and Induction Heads.*
* Nanda et al. (2023). *Progress measures for grokking via mechanistic interpretability.*

In our experiments, all pruned circuits, masks, and synthetic teachers are derived from the Gao et al. (2025) artifacts. Users applying our pipeline to their own work should also cite Gao et al.
