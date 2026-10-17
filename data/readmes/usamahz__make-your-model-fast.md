<p align="center">
  <a href="https://ai.usamah.me">
    <img src="images/how-to-make-your-model-fast-og.png" width="100%" alt="How to Make Your Model Fast, a Systems View of Efficient Machine Learning from Silicon to Agents, by Usamah Zaheer. Beside the title, a latency budget drawn as a ruler: grey segments for the stages of one frame, cut by a line at 33 milliseconds, with the 3.6 milliseconds past the line in red.">
  </a>
</p>

# How to Make Your Model Fast

*A Systems View of Efficient Machine Learning, from Silicon to Agents*, by [Usamah Zaheer](https://www.usamah.me).

**Read it free at [ai.usamah.me](https://ai.usamah.me)**, or download it as a
[PDF](how-to-make-your-model-fast.pdf) or an [EPUB](how-to-make-your-model-fast.epub).

Most of what is written about machine learning assumes the model is the interesting part
and the machine is a detail. In practice the machine decides what you are allowed to
build. This book is about the boundary where a model meets real hardware under a real
budget for latency, memory, power and money: how to predict what that boundary will do to
you, and what to change first when it does.

By the end you should be able to pick up an unfamiliar model and an unfamiliar device
and, in about fifteen minutes with a datasheet and a calculator, say how fast the model
can possibly run there, which limit it will hit first, and what is worth trying, in what
order, to move it. It runs from the silicon upward in fourteen parts and about 90,000
words, with 48 figures and a set of worked problems at the end of every chapter.

## Contents

| Part | Chapter | What it covers |
|---:|---|---|
| 0 | [Introduction](https://ai.usamah.me) | Why the book exists, what you will be able to do by the end of it, and how to read it. |
| 1 | [Rooflines, Budgets and the Cost of a FLOP](https://ai.usamah.me/roofline) | Build the roofline model from first principles, find the ridge point, and write a defensible performance budget for a new model in fifteen minutes. |
| 2 | [Inside an Edge Accelerator](https://ai.usamah.me/hardware) | The four kinds of silicon that run ML outside a datacentre, then deep on Arm CPUs: NEON, SVE2, int8 dot products, the memory hierarchy, and datasheets. |
| 3 | [Kernels: Where the Time Actually Goes](https://ai.usamah.me/kernels) | Why the obvious matmul reaches six per cent of peak, and what tiling, a register micro-kernel and NEON int8 vectorisation recover. Four convolutions compared. |
| 4 | [Compilers, Graphs and Runtimes](https://ai.usamah.me/compilers) | How an ML compiler captures a graph, lowers it through IRs, fuses and plans memory, and why a pipeline meant to speed your model up can make it slower. |
| 5 | [Quantisation](https://ai.usamah.me/quantisation) | Affine quantisation from first principles: the int8 matmul, requantisation, number formats, granularity, calibration, QAT, and what breaks in real networks. |
| 6 | [Pruning, Sparsity and Distillation](https://ai.usamah.me/compression) | Pruning, sparsity, distillation and architecture search, with the arithmetic for when a sparse kernel finally wins and the order to pull each lever. |
| 7 | [Vision Models in the Real World](https://ai.usamah.me/vision) | Costing classification, detection and segmentation honestly: preprocessing and NMS, resolution as the abused knob, tiling large imagery, fast backbones. |
| 8 | [Transformers on Small Machines](https://ai.usamah.me/llms) | Count parameters and FLOPs in a decoder layer, derive the 2N rule, and predict a model's token rate on a phone or laptop before downloading a weight. |
| 9 | [Perception, VLMs and Robots](https://ai.usamah.me/robotics) | A robot is a control loop with a network inside it. Budget the sense-to-act chain, see why ten milliseconds can make a controller ring, and where VLMs pay. |
| 10 | [Profiling: Finding the Real Bottleneck](https://ai.usamah.me/profiling) | A method for finding what is actually slow: trustworthy benchmarks, hardware counters turned into achieved bandwidth and FLOPs/s, and a decision tree. |
| 11 | [Serving, MLOps and the Cost of Being Wrong](https://ai.usamah.me/serving) | From a latency SLO to a machine count, why utilisation above seventy percent destroys the tail, batching, placement, drift, and pricing your errors. |
| 12 | [Agents: Latency and Cost in LLM Systems](https://ai.usamah.me/agents) | An agent is a distributed system: model the latency of a call chain, the quadratic transcript cost, RAG memory, cascades and caches, and the critical path. |
| 13 | [Conclusion and Further Reading](https://ai.usamah.me/conclusion) | What the thirteen parts add up to: one reasoning procedure on one page, where it stops working, and the books and papers that taught the author most of it. |

Read [Part 1](https://ai.usamah.me/roofline) first, properly, with a pen. Everything after
it assumes you can place a workload on a roofline, and the applied chapters after that can
be read in whatever order matches what you are stuck on.

## The whole method, on one page

Part 13 reduces the book to a procedure short enough to pin above a desk:

<p align="center">
  <a href="https://ai.usamah.me/conclusion">
    <img src="images/p13-procedure.svg" width="100%" alt="The procedure from Part 13 in four steps. One: write the budget down, as three numbers for latency, memory and cost or power, and one sentence saying why the product fails if any is missed. Two: find the binding constraint, which is compute, bandwidth, latency, or not the model at all. Three: spend the cheapest thing first, from fixing the system through quantisation, compiler and kernel work, a smaller or distilled architecture and structured pruning to changing the problem. Four: measure again, then stop.">
  </a>
</p>

The other thirteen parts are about doing each of those steps honestly on real machines.

## Found an error?

There will be errors, and I would genuinely like to hear about them.
[Open an issue](https://github.com/usamahz/make-your-model-fast/issues/new) for anything
wrong or unclear: a sum that does not add up, a claim that has gone out of date, a number
your hardware disagrees with, or a paragraph you had to read three times. Unclear is a
defect too. If you would rather not use GitHub, email usamahzaheer155 [at] gmail [dot] com.

## Citing it

```bibtex
@book{make-your-model-fast,
  title        = {How to Make Your Model Fast: A Systems View of Efficient Machine Learning, from Silicon to Agents},
  author       = {Zaheer, Usamah},
  howpublished = {Online},
  url          = {https://ai.usamah.me},
  year         = {2026}
}
```

Or in prose: Usamah Zaheer, *How to Make Your Model Fast*, ai.usamah.me. Every part on the
site ends with a citation for that part alone, and GitHub's *Cite this repository* button
reads [CITATION.cff](CITATION.cff).

## Licence

The book, its figures and its cover are copyright Usamah Zaheer. You are welcome to read
them, link to them and quote them, with attribution and a link to the part you quote; for
anything beyond that, such as republishing or translating the book, please ask first.
[LICENSE](LICENSE) has the terms in full.
