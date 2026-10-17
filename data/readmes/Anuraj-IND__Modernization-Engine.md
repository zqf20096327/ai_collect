# Legacy Code Modernization Engine

> AI-powered pipeline that modernizes Java codebases — either to **Java 21** or **Python 3** — using context optimization, skeleton-first translation, and deterministic post-processing to minimize LLM hallucination across multi-file repositories.

---

## What It Does

This engine takes a Java repository as input and produces a fully translated output codebase. It supports three transformation paths:

- **Java 8/11/17 → Java 21/22/25** — using a local LLM (Ollama) with DAG-ordered processing
- **Java → Python 3** — using skeleton-first LLM translation with semantic context injection
- **Java 8 → Java 8/11/17** — deterministic AST patch rules with zero LLM involvement

The entire pipeline runs **locally on Ollama** using `qwen2.5-coder:14b-instruct-q4_K_M`. No cloud API, no data leaves your machine.

---

## The Problem It Solves

Enterprise Java codebases — billing systems, ERP platforms, banking applications — accumulate 10–20 years of cross-file dependencies, circular import clusters, dead code, and deprecated APIs. Feeding these repositories directly into an LLM produces output that looks correct but breaks at runtime: invented method signatures, wrong imports, broken dependency contracts, and syntax errors unique to Java-to-Python translation (labeled loops, `++` operators, Java exception names, `Enum.name()` calls).

The core issue is not model capability. It is context quality. A model asked to simultaneously understand the codebase architecture, resolve its dependency graph, detect circular imports, and translate syntax in one pass will fail at all four. This engine separates those concerns into three distinct phases.

---

## How It Works — Three Phases

### Phase 1 — IR Extraction (No LLM)

Runs deterministic static analysis on the Java repository using **tree-sitter**. Produces three JSON files that become ground truth for all downstream phases:

- `ir_registry.json` — every class, method, and data structure with stable UUIDs
- `dependency_graph.json` — all import, call, and include edges between modules
- `project_metadata.json` — entry points, language distribution, and all **circular dependency clusters** detected via DFS

No LLM is involved. No guessing. This phase runs in seconds on any repository.

### Phase 2 — Architectural RAG (Offline Ollama)

Builds a hybrid retrieval engine over the Phase 1 artifacts using **Ollama `nomic-embed-text`** embeddings. Answers six query types about the codebase — LIST, OVERVIEW, STRUCTURAL, FLOW, SMELL, HYBRID.

Key design: LIST queries (e.g. "list all classes") bypass the LLM entirely and return exact answers from the in-memory graph. HYBRID queries prepend the full module registry to every prompt so the LLM cannot hallucinate class names that do not exist.

Phase 2 also exposes a `Phase2ContextProvider` — a lightweight module that injects per-file architectural summaries (capped at 3,000 chars) into Phase 3 translation prompts without requiring Ollama.

### Phase 3 — Transformation (Three Paths)

**Case 1 — Mechanical Rules (Java 8/11/17, no LLM)**
Applies 13 version-gated AST patch rules via tree-sitter. Rules cover `StringBuffer → StringBuilder`, `Vector → ArrayList`, `Hashtable → HashMap`, `Stack → ArrayDeque`, deprecated boxed constructors, `Collections.sort()`, indexed for-loops, anonymous `Runnable`/`Comparator` → lambdas, `List.of()`, `String.isBlank()`, and pattern matching `instanceof`. Every change is logged with rule name and line number. Dry-run mode available.

**Case 2a — Java → Java 21 (LLM, DAG-ordered)**
Builds a directed acyclic graph from `dependency_graph.json` and processes files in topological order — leaf classes first, entry points last. After each successful translation, stores a **semantic stub** (method signatures, no bodies) in a knowledge base. Every subsequent file receives the stubs of its already-translated dependencies, so the LLM sees actual interfaces rather than guessing them.

**Case 2b — Java → Python (Skeleton-First LLM)**
Before calling the LLM, Phase 1 IR data is used to build a **syntactically valid Python skeleton** with the exact class name, field declarations, and method signatures locked in. The LLM is asked to fill method bodies only. It cannot rename a class, drop a method, or invent an import because those slots are already occupied.

A deterministic **postprocessor** runs on every LLM output before `ast.parse()` validation, fixing 10 categories of systematic Java-to-Python errors:

| Fix | What It Catches |
|-----|----------------|
| Labeled loops | `break OUTER` → flag variable pattern |
| Increment operators | `++i` / `--i` → `i += 1` / `i -= 1` |
| Java exceptions | `InterruptedException` → `KeyboardInterrupt` etc. |
| Enum name calls | `.name()` → `.name` (property not method) |
| Java imports | removes `java.*`, `javax.*`, `sun.*` |
| Self-imports | removes `from .ClassName import ClassName` |
| Dict context managers | `with self.m_htX:` → TODO stub |
| String compareTo | `.compareTo()` → `(a > b) - (a < b)` |
| Security manager | removes `SecurityManager` calls |
| Empty TYPE_CHECKING | removes blocks that cause `SyntaxError` |

If both LLM attempts fail validation, the engine writes the **bare skeleton with TODO comments** — always valid Python, always importable. The pipeline never writes a broken file.

**Adaptive chunking** handles files that exceed the token budget (20,000 chars for Python, 48,000 for Java 21). Files are split at method boundaries, the class header is injected into every chunk as overlap, chunks are processed separately, and outputs are merged and validated as a single file.

---

## Approach to the Problem Statement

The challenge required handling multi-file dependencies without exceeding context windows and minimizing hallucination caused by distracting code comments or dead code. The approach taken:

**Context Optimization** — instead of feeding entire files or whole repositories to the LLM, each translation call receives only: the translation rules, a 3,000-char architectural summary from Phase 2, the method stubs of direct dependencies from the knowledge base, the source file itself (chunked if oversized), and the pre-built skeleton. Irrelevant classes, unrelated Javadoc, and dead code never enter the prompt.

**Dependency-aware ordering** — the DAG ensures every file's dependencies are translated before it is. The LLM never has to guess what a dependency looks like because the actual translated stub is already in the knowledge base.

**Determinism where possible** — anything that can be done without an LLM is done without one. Phase 1 is pure static analysis. Case 1 transformations use AST rules. LIST queries use graph traversal. The postprocessor uses regex and AST patching. The LLM is called only for what requires genuine code generation.

**Resilience** — per-file status tracking (pending / in_progress / done / needs_revision / blocked) means a 200-file job can be interrupted and resumed without reprocessing successful files. `--retry-failed` resets only failed files.

---

## Web Interface

The engine ships with a full-stack web UI served by the FastAPI backend at `/`. No separate frontend server, no build step.

- **Transform tab** — zip upload or GitHub URL clone, Phase 1 extraction, mode selector, real-time log terminal via SSE
- **Explore tab** — side-by-side Java and translated output with syntax highlighting
- **Chat tab** — ask questions about the codebase; backed by Ollama when running, falls back to graph-based IR search when offline
- **Download tab** — download the entire transformed codebase as a zip(upcoming feature)

---

## Running on Kaggle (Free T4 GPU)

```bash
# Cell 1 — install Ollama
!curl -fsSL https://ollama.com/install.sh | sh

# Cell 2 — pull models
!ollama pull qwen2.5-coder:14b-instruct-q4_K_M
!ollama pull nomic-embed-text

# Cell 3 — start server with ngrok tunnel
!pip install fastapi uvicorn pyngrok python-multipart -q
import os, threading, subprocess
from kaggle_secrets import UserSecretsClient
os.environ["NGROK_TOKEN"] = UserSecretsClient().get_secret("NGROK_TOKEN")
threading.Thread(
    target=lambda: subprocess.run(["python", "app.py"], cwd="/kaggle/working/project"),
    daemon=True
).start()
# prints public ngrok URL — open in browser
```

---

## Running Locally

```bash
# Requirements: Python 3.10+, Ollama installed and running

pip install -r requirements.txt
pip install -r requirements_phase2.txt

# Pull models
ollama pull qwen2.5-coder:14b-instruct-q4_K_M
ollama pull nomic-embed-text

# Java to Python
python run_phase3.py \
  --repo   ./your-java-project \
  --source java \
  --target python \
  --model  qwen2.5-coder:14b-instruct-q4_K_M

# Java to Java 21
python run_phase3.py \
  --repo        ./your-java-project \
  --target-java 21 \
  --model       qwen2.5-coder:14b-instruct-q4_K_M

# Dry-run (shows what would change, writes nothing)
python run_phase3.py --repo ./your-java-project --target-java 17 --dry-run

# Resume an interrupted run
python run_phase3.py --repo ./your-java-project --source java --target python --retry-failed
```

---

## Project Structure

```
project/
├── run_phase3.py                        # CLI entry point
├── app.py                               # FastAPI web server
├── frontend/
│   └── index.html                       # Single-page UI
├── engine/
│   └── phase1_runner.py                 # IR extraction entry point
├── phase3/
│   ├── transformers/                    # Case 1 — AST rules
│   │   ├── java_modernizer.py
│   │   ├── rule_base.py
│   │   └── output_writer.py
│   ├── same_language/                   # Case 2a — Java → Java 21
│   │   ├── dag/
│   │   │   ├── dag_builder.py
│   │   │   ├── status_tracker.py
│   │   │   └── knowledge_base.py
│   │   └── llm/
│   │       ├── prompt_assembler.py
│   │       ├── llm_transformer.py
│   │       └── java21_rules.py
│   └── cross_language/                  # Case 2b — Java → Python
│       └── java_to_python/
│           └── llm/
│               ├── prompt_assembler.py
│               ├── llm_transformer.py
│               ├── python_postprocessor.py
│               ├── java_to_python_rules.py
│               └── knowledge_base.py
├── phase2/                              # Phase 2 — Architectural RAG
│   ├── phase2_runner.py                 # RAG engine entry point
│   ├── builders/                        # Module + system doc builders
│   ├── graph/                           # GraphIndex — dependency traversal
│   ├── indexing/                        # Vector index builder (LlamaIndex)
│   ├── loaders/                         # IR, dependency, metadata loaders
│   ├── query/                           # Query engine — 6 typed handlers
│   └── retrieval/                       # HybridRetriever + ContextAssembler
└── phase2_context_provider.py           # Lightweight context bridge (no Ollama needed)
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Static analysis | tree-sitter, tree-sitter-java |
| LLM inference | Ollama (`qwen2.5-coder:14b-instruct-q4_K_M`) |
| Embeddings | Ollama (`nomic-embed-text`) |
| Vector index | LlamaIndex (512-token chunks, top-k=3) |
| Backend | FastAPI, uvicorn |
| Frontend | Vanilla JS, highlight.js |
| Tunnel (Kaggle) | pyngrok |
| Syntax validation | ast.parse() (Python), tree-sitter (Java) |
