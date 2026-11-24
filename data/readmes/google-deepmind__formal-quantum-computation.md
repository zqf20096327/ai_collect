# QuantumComputation

[![arXiv](https://img.shields.io/badge/arXiv-2611.09822-b31b1b.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2611.09822)

A [Lean 4](https://leanprover.github.io/lean4/doc/whatIsLean.html) library for formally specifying and verifying quantum programs, grounded in quantum Hoare logic with classical variables.

## Overview

The repository is organized into two Lean libraries:

* **[`QuantumComputation`](./QuantumComputation/)** is the core library covering the foundations of quantum computation (circuits, gates, registers, and underlying mathematics), the formalization of quantum Hoare logic with classical variables, the resource counting framework, and the verification of key quantum algorithms.
* **[`QuantumComputationSpecs`](./QuantumComputationSpecs/)** is a separate library of specifications and benchmark challenges for automated theorem proving and AI-assisted quantum program discovery.

The quantum programs discovered and described in the paper are in the `discoveries` branch of the repository (in order to enable depending on the framework itself in a more lightweight manner). See [the `QuantumComputationDiscoveries` README](https://github.com/google-deepmind/formal-quantum-computation/tree/discoveries/QuantumComputationDiscoveries/README.md) for information on these.

This repository is under active development, with explicit models for costing classical computation and control flow as the next planned milestone.

## Usage

This is a Lean 4 project managed with `lake`. You first need to [install `elan`, `lake`, and `lean`](https://leanprover-community.github.io/get_started.html), and then run:

```bash
lake exe cache get
lake build 
```

## Dependencies

The project builds on the standard Lean 4 libraries for mathematics and quantum information [Mathlib4](https://github.com/leanprover-community/mathlib4) and [QuantumInfo](https://github.com/leanprover-community/physlib/tree/master/QuantumInfo) (part of [Physlib](https://github.com/leanprover-community/physlib)). 

The `lake build` command above handles fetching these automatically.

## Versioning

This repository tracks tagged releases of Mathlib and Physlib (which provides QuantumInfo) rather than their `master` branches. It currently uses Lean, Mathlib, and Physlib, pinned in [`lean-toolchain`](./lean-toolchain) and [`lakefile.toml`](./lakefile.toml).

## Citing

If you use this repository in your work, please cite [Discovering formally verified quantum programs with AI](https://arxiv.org/abs/2611.09822):

```bibtex
@misc{shirobokov2026discoveringformallyverifiedquantum,
      title={Discovering formally verified quantum programs with {AI}}, 
      author={Sergey Shirobokov and Ben Jaderberg and Katerina Hristova and George Tsoukalas and Johannes Bausch and Eric Wieser and Francisco J. H. Heras and Nicholas C. Rubin and Guang Hao Low and Sébastien Racanière and Nenad Tomašev and Lei M. Zhang and James D. Watson and Tanuj Khattar and Aws Albarghouthi and Stavan Jain and Harun Khan and Leopoldo Sarra and Andrew W. Senior and Michael Broughton and Hussain Masoom and Sergio Boixo and Ryan Babbush and Swarat Chaudhuri and Pushmeet Kohli},
      year={2026},
      eprint={2611.09822},
      archivePrefix={arXiv},
      primaryClass={quant-ph},
      url={https://arxiv.org/abs/2611.09822}, 
}
```

## License and disclaimer

Copyright 2026 Google LLC

All software is licensed under the Apache License, Version 2.0 (Apache 2.0);
you may not use this file except in compliance with the Apache 2.0 license.
You may obtain a copy of the Apache 2.0 license at:
https://www.apache.org/licenses/LICENSE-2.0

All other materials are licensed under the Creative Commons Attribution 4.0
International License (CC-BY). You may obtain a copy of the CC-BY license at:
https://creativecommons.org/licenses/by/4.0/legalcode

Unless required by applicable law or agreed to in writing, all software and
materials distributed here under the Apache 2.0 or CC-BY licenses are
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the licenses for the specific language governing
permissions and limitations under those licenses.

This is not an official Google product.
