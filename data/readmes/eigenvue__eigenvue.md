<div align="center">

<br>

# Eigenvue

**Interactive Dissection Platform for deep learning, generative AI, and quantum algorithms**

Interactive, step-by-step visualizations with synchronized code highlighting,<br>
plain-language explanations, and educational content — in the browser and in Python.

<br>

<a href="https://pypi.org/project/eigenvue/"><img src="https://img.shields.io/pypi/v/eigenvue?color=3775A9&logo=pypi&logoColor=white&label=PyPI" alt="PyPI version" /></a>&nbsp;
<a href="https://www.npmjs.com/package/eigenvue"><img src="https://img.shields.io/npm/v/eigenvue?color=CB3837&logo=npm&logoColor=white&label=npm" alt="npm version" /></a>&nbsp;
<a href="https://github.com/eigenvue/eigenvue/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/eigenvue/eigenvue/ci.yml?branch=main&logo=github&label=CI" alt="CI status" /></a>&nbsp;
<a href="https://github.com/eigenvue/eigenvue/blob/main/LICENSE"><img src="https://img.shields.io/github/license/eigenvue/eigenvue?color=22c55e" alt="MIT License" /></a>&nbsp;
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-≥3.10-3776AB?logo=python&logoColor=white" alt="Python 3.10+" /></a>&nbsp;
<a href="https://nodejs.org/"><img src="https://img.shields.io/badge/node-≥18-339933?logo=node.js&logoColor=white" alt="Node 18+" /></a>

<br>

[**Live App**](https://eigenvue.web.app) · [**Documentation**](https://eigenvue.web.app/docs) · [**PyPI**](https://pypi.org/project/eigenvue/) · [**npm**](https://www.npmjs.com/package/eigenvue) · [**GitHub**](https://github.com/eigenvue/eigenvue)

<br>
<br>

</div>

## Why Eigenvue?

Understanding algorithms requires building **spatial and temporal intuition** that textbooks and static diagrams cannot provide. Existing tools are domain-specific — one for sorting, another for attention mechanisms, yet another for quantum circuits. None offer a unified visual language across these domains, and none bridge web-based exploration with programmatic workflows.

**Eigenvue** solves this with:

- **One platform, four domains** — classical algorithms, deep learning, generative AI, and quantum computing under a single interaction model.
- **Dual distribution** — explore in the browser at [eigenvue.web.app](https://eigenvue.web.app), or `pip install eigenvue` for Jupyter notebooks and research scripts.
- **Real code, not config** — algorithms are defined as TypeScript and Python functions, making them testable, debuggable, and contributor-friendly.

## Algorithms

<div align="center">
<table>
  <tr>
    <td>

**Classical** (12)
- Binary Search
- Bubble Sort
- Cocktail Shaker Sort
- Insertion Sort
- Linear Search
- Selection Sort
- Breadth-First Search
- Depth-First Search
- Heap Sort
- Merge Sort
- QuickSort
- Dijkstra's Shortest Path

</td>
    <td>

**Deep Learning** (5)
- Single Neuron / Perceptron
- Backpropagation
- Convolution (2D)
- Feedforward Neural Network
- Gradient Descent

</td>
  </tr>
  <tr>
    <td>

**Generative AI** (5)
- BPE Tokenization
- Self-Attention (Scaled Dot-Product)
- Token Embeddings
- Multi-Head Attention
- Transformer Block

</td>
    <td>

**Quantum Computing** (5)
- Qubit States & Bloch Sphere
- Quantum Gates & Circuits
- Superposition & Measurement
- Grover's Search Algorithm
- Quantum Teleportation

</td>
  </tr>
</table>
</div>

> **27 algorithms** with step-by-step animated visualizations, synchronized code highlighting (pseudocode, Python, JavaScript), key concepts, common pitfalls, quizzes, and further resources.
>
> Browse the full catalog: [**Algorithm Reference →**](https://eigenvue.web.app/docs/algorithms)

## Quick Start

### Web App

Explore all visualizations instantly — no installation required:

**👉 [eigenvue.web.app](https://eigenvue.web.app)**

### Python

```bash
pip install eigenvue
```

```python
import eigenvue

# List all available algorithms
eigenvue.list()

# Open an interactive visualization in your browser
eigenvue.show("binary-search")

# Get step data programmatically
steps = eigenvue.steps("self-attention")

# Use in a Jupyter notebook  (pip install eigenvue[jupyter])
eigenvue.jupyter("transformer-block")
```

### Node.js / TypeScript

```bash
npm install eigenvue
```

```typescript
import { list, steps, show } from "eigenvue";

// List all available algorithms
list();

// Get step data programmatically
const result = steps("binary-search");

// Open an interactive visualization in your browser
show("self-attention");
```

## Features

| | Feature | Description |
|---|---|---|
| ▶️ | **Step-by-Step Playback** | Play, pause, step forward/back through every algorithm state |
| 🖊️ | **Synchronized Code** | See exactly which line executes at each step — in pseudocode, Python, or JavaScript |
| 🎛️ | **Custom Inputs** | Provide your own arrays, graphs, or parameters and watch the algorithm adapt |
| 📖 | **Educational Content** | Key concepts, common pitfalls, quizzes, and curated external resources per algorithm |
| 📓 | **Jupyter Integration** | Embed interactive visualizations directly in notebooks with `eigenvue.jupyter()` |
| 🔗 | **Shareable URLs** | Every visualization state is URL-encoded — share a specific step with a link |
| ✅ | **Cross-Language Parity** | TypeScript and Python generators produce identical step sequences (CI-enforced) |
| 📦 | **Minimal Dependencies** | npm package: zero runtime deps. Python package: only Flask |

## Architecture

Eigenvue follows a clean three-layer architecture:

```
┌─────────────────────────────────────────────────────────┐
│  Generator Layer       TypeScript & Python functions     │
│                        that produce Step sequences       │
├─────────────────────────────────────────────────────────┤
│  Step Format           Universal JSON contract (v1.0.0)  │
│                        between generators & renderers    │
├─────────────────────────────────────────────────────────┤
│  Rendering Layer       Canvas 2D engine with layouts,    │
│                        animation, and playback controls  │
└─────────────────────────────────────────────────────────┘
```

Adding a new algorithm never requires modifying the rendering engine. Improving the renderer never requires touching algorithm logic. Cross-language parity is CI-enforced to ±1e-9 tolerance.

📐 [Architecture docs →](https://eigenvue.web.app/docs/architecture/overview)

## Project Structure

```
eigenvue/
├── algorithms/          # Shared algorithm definitions (meta.json per algorithm)
│   ├── classical/       # Binary Search, Bubble Sort, QuickSort, …
│   ├── deep-learning/   # Perceptron, Feedforward Network, …
│   ├── generative-ai/   # Tokenization, Self-Attention, …
│   └── quantum/         # Grover's Search, Quantum Gates, …
├── web/                 # Next.js web application (Canvas 2D, Tailwind CSS)
├── python/              # Python package (pip install eigenvue)
├── node/                # npm package (zero runtime dependencies)
├── shared/              # Shared types, schemas, and constants
├── docs/                # Documentation site (Astro / Starlight)
├── scripts/             # Build, codegen, and maintenance scripts
├── tests/               # Cross-platform integration tests
└── .github/             # CI/CD workflows
```

## Development Setup

**Prerequisites:** Node.js 22+, Python 3.10+, Git

<details>
<summary><b>Web Application</b></summary>
<br>

```bash
cd web
npm install
npm run dev          # → http://localhost:3000
```

</details>

<details>
<summary><b>Python Package</b></summary>
<br>

```bash
cd python
pip install -e ".[dev]"
pytest
```

</details>

<details>
<summary><b>Node Package</b></summary>
<br>

```bash
cd node
npm install
python ../scripts/bundle-node-data.py
npm run build
npm test
```

</details>

<details>
<summary><b>Documentation Site</b></summary>
<br>

```bash
cd docs
npm install
npm run build
```

</details>

## Documentation

Full documentation is available at **[eigenvue.web.app/docs](https://eigenvue.web.app/docs)**.

| Section | What's Inside |
|---|---|
| [Getting Started](https://eigenvue.web.app/docs/getting-started/web-app) | Web app, Python package, Jupyter integration |
| [User Guide](https://eigenvue.web.app/docs/user-guide/ui-controls) | UI controls, playback, sharing & URLs, FAQ |
| [API Reference](https://eigenvue.web.app/docs/api-reference/python-api) | Python API, TypeScript API, Step Format, Layout System |
| [Architecture](https://eigenvue.web.app/docs/architecture/overview) | System overview, design decisions, rendering engine |
| [Algorithm Reference](https://eigenvue.web.app/docs/algorithms) | All 27 algorithms with detailed documentation |
| [Contributing](https://eigenvue.web.app/docs/contributing/development-setup) | Dev setup, adding algorithms, Generator API, style guide |
| [Research & Citation](https://eigenvue.web.app/docs/research/project-overview) | Project overview, comparison, how to cite |

## Contributing

Contributions are welcome! Please read the [**Contributing Guide**](CONTRIBUTING.md) for development setup, branching strategy, and commit conventions.

**Adding a new algorithm?** Follow the step-by-step guide: [Adding an Algorithm →](https://eigenvue.web.app/docs/contributing/adding-an-algorithm)

| Resource | Link |
|---|---|
| Development Setup | [Docs →](https://eigenvue.web.app/docs/contributing/development-setup) |
| Generator API | [Docs →](https://eigenvue.web.app/docs/contributing/generator-api) |
| Step Format Spec | [Docs →](https://eigenvue.web.app/docs/api-reference/step-format) |
| Code Style Guide | [Docs →](https://eigenvue.web.app/docs/contributing/code-style) |
| Writing Tests | [Docs →](https://eigenvue.web.app/docs/contributing/writing-tests) |
| Cross-Language Parity | [Docs →](https://eigenvue.web.app/docs/contributing/cross-language-parity) |

## Tech Stack

| Layer | Technology |
|---|---|
| Web App | Next.js 15 · React 19 · Canvas 2D · Tailwind CSS 4 |
| Python Package | Python 3.10+ · Flask · hatchling |
| Node Package | TypeScript · tsup · zero runtime deps |
| Testing | Vitest · pytest · JSON Schema validation |
| CI/CD | GitHub Actions — lint, typecheck, test, build, deploy |
| Docs | Astro + Starlight |
| Hosting | Firebase |

## Citation

If you use Eigenvue in research or teaching, please cite:

```bibtex
@article{eigenvue2026,
  title   = {Eigenvue: A Visual Learning Platform for Algorithms,
             AI Architectures, and Quantum Computing},
  author  = {Mishra, Ashutosh},
  year    = {2026},
  url     = {https://eigenvue.web.app}
}
```

See the full [Citation guide →](https://eigenvue.web.app/docs/research/citation)

## License

[MIT](LICENSE) © 2026 [Ashutosh Mishra](https://github.com/eigenvue)

---

<div align="center">
  <sub>Built with care for learners, educators, and researchers.</sub>
  <br><br>
  <a href="https://eigenvue.web.app">Website</a> ·
  <a href="https://eigenvue.web.app/docs">Docs</a> ·
  <a href="https://github.com/eigenvue/eigenvue/issues">Report a Bug</a> ·
  <a href="https://github.com/eigenvue/eigenvue/issues">Request a Feature</a>
</div>
