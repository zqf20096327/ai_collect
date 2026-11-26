# TokenMS (Token Management System)

> **Local-First Code Intelligence and Context Management for AI Coding Agents**
> Compress context, prevent exploratory rediscovery loops, and bridge architectural disconnects across Python, TypeScript, Rust, and Flutter (Dart).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Version: 1.0.1](https://img.shields.io/badge/Version-1.0.1-blue.svg)](pyproject.toml)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Protocol: MCP](https://img.shields.io/badge/Protocol-MCP-green.svg)](https://modelcontextprotocol.io/)
[![Tests: Passing](https://img.shields.io/badge/Tests-174%20Passing-brightgreen.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
![GitHub forks](https://img.shields.io/github/forks/HARSHNEXX/TokenMS?style=social)

[About this project](./about.md) | [Contributing](./CONTRIBUTING.md) | [Security](./SECURITY.md)

---

## The Problem

AI coding agents waste a large portion of their token budget on file discovery rather than actual work.

A typical agent session without TokenMS looks like this:

| Without TokenMS | With TokenMS |
| :--- | :--- |
| Agent reads 8-15 whole files to find relevant code | Agent receives only the exact symbols needed |
| Repeated `grep` and exploratory reads per task | Structured AST retrieval in a single call |
| Manual relationship discovery across modules | Cross-module pathway traversal built in |
| 6,000-330,000 tokens consumed per task | 1,500-3,500 tokens per task (budget-controlled) |
| Agent loses critical context in long conversations | Persistent curated knowledge ledger across sessions |

The root cause: agents are optimized for chat, not for navigating large codebases. They read files sequentially, re-read them when context shifts, and have no way to know that `AuthService` in `auth/service.py` is the class that actually matters for the task at hand.

**TokenMS solves this at the infrastructure level**, not by prompting the agent to "be smarter."

---

## What is TokenMS?

**TMS** runs locally alongside your editor as a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) service. It parses your repository into an Abstract Syntax Tree (AST) symbol graph, maps cross-module relationships, and uses Knapsack optimization to assemble only the exact classes, functions, and interfaces required for a task into a compact token budget.

### Key Capabilities

* **Multi-Language AST Parsing:** Extracts classes, decorators, async functions, interfaces, type aliases, enums, signatures, and docstrings for Python, TypeScript, JavaScript, Rust, and Dart via Tree-sitter, with explicit syntax-error diagnostics and `unknown` return-type handling when unannotated.
* **Hybrid Multi-Modal Retrieval:** Blends SQLite FTS5 (BM25 lexical search) with phrase proximity n-grams, Personalized PageRank (PPR) graph walks, and local CPU vector embeddings.
* **Enclosing Class Context & Dependency Preservation:** Slices focal functions while preserving surrounding class headers, decorators, and essential cross-boundary dependency chains (`READS_TABLE`, `CONSTRAINED_BY`, `CALLS_API`, `GENERATED_FROM`) under tight token budgets, explicitly reporting `omitted_dependencies` and `coverage_complete` when extreme budgets evict edges.
* **Monorepo Ownership & Schema Evolution Diagnostics:** Qualifies package-scoped SQL/client/API ownership across monorepos (`AMBIGUOUS` vs `VERIFIED`/`INFERRED`), tracks `ALTER TABLE` schema migrations (`RENAME COLUMN`, `ADD`/`DROP`/`ALTER COLUMN`), inspects generated DB types (`database.types.ts`, `*.g.dart`), and surfaces stale frontend/client field warnings.
* **Production-Path Cache Freshness:** Tracks persisted `index_generation` across SQLite, FTS5, embeddings, graph adjacency, and resolution caches, purging deleted/renamed/migrated artifacts on reconciliation, edit, or buffer-overlay resets.
* **Transactional AST Patching & Outlines:** Supports TOCTOU-hardened single-symbol edits, two-phase preflight/rollback `batch_edit`, standalone zero-index `tms outline` / `tms read` CLI commands, optional PreToolUse outline-first host hooks, and optional configurable helper-delegation verification.
* **Local-First & Zero Cloud Cost:** Runs entirely on your CPU using SQLite with Write-Ahead Logging (WAL) and local Model2Vec embeddings. No external API keys or cloud dependencies required.
* **Adaptive Token Budget Controller:** Dynamically scales context from 1,200 to 4,000 tokens based on query complexity and multi-channel candidate consensus.

---

## First-Run Experience

Here is exactly what happens after installation, step by step.

### Step 1: Install TokenMS

```bash
git clone https://github.com/HARSHNEXX/TokenMS.git
cd TokenMS
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

pip install -e .
```

> **Note on the embedding model:** On the very first run, TMS downloads the [Model2Vec](https://github.com/MinishLab/model2vec) static embedding model (~30 MB) from HuggingFace. This is a one-time download; afterwards the model is cached locally and TMS operates entirely offline. No API keys are needed at any point.

### Step 2: Index your project

Run this once inside the repository you want TMS to understand:

```bash
cd /path/to/your/project
python -m tms.app index

# Verify the index is healthy
python -m tms.app status
```

TMS parses every supported source file, extracts AST symbols, computes cross-module call graphs, and stores everything in `.tms/index.sqlite`. Indexing a 50 KLOC Python project typically takes 10-30 seconds.

### Step 3: Configure your MCP client

#### Cursor

Add to `.cursor/mcp.json` or your Global Cursor Settings:

```json
{
  "mcpServers": {
    "tms": {
      "command": "python",
      "args": ["-m", "tms.app", "serve"],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

#### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tms": {
      "command": "python",
      "args": ["-m", "tms.app", "serve"],
      "cwd": "/path/to/your/project"
    }
  }
}
```

### Step 4: Agent requests task context

When your agent starts a task, it calls `resolve_task_context` with a natural language description:

```
Task: "Add retry logic to the payment processor"
```

TMS responds with the precise symbols your agent needs: the `PaymentProcessor` class signature, its `process()` method body, the `RetryPolicy` interface it depends on, and any decorators or error handlers in scope. The response is typically 1,500-3,500 tokens.

### Step 5: Agent works on focused context

Your agent reads only the symbols TMS returned, makes its edits, and calls `record_outcome` to reinforce verified symbols into the curated knowledge ledger. Future tasks on the same codebase get even more accurate context.

```
resolve_task_context("Add retry logic to the payment processor")
  -> 2,840 tokens of exactly relevant code returned
  -> Agent edits PaymentProcessor.process() with full context
  -> record_outcome() persists verified symbols to ledger
```

---

## Architecture

```text
                           AI Coding Agent
             (Claude Desktop / Cursor / VS Code)
                                  |
                        MCP Protocol (stdio)
                                  |
+-------------------------------------------------------------------+
|                            TMS Gateway                            |
|                                                                   |
| [resolve_task_context]  [query]  [batch]  [edit]  [record_outcome]|
+-------------------------------------------------------------------+
       |                          |                        |
       v                          v                        v
+----------------------+  +---------------------+  +----------------+
|  Hybrid Retrieval    |  |  AST Safe Patcher   |  | Output Parser  |
| - SQLite FTS5 (BM25) |  | - AST Fingerprints  |  | - Error traces |
| - Graph PageRank     |  | - Preconditions     |  | - Log cleaner  |
| - Local Embeddings   |  | - Live Buffer Sync  |  +----------------+
| - Knapsack Packer    |  +---------------------+
+----------------------+             |
       |                             |
       +--------------+--------------+
                      |
+-------------------------------------------------------------------+
|                    Storage & Persistence Layer                    |
|                                                                   |
| - SQLite WAL Database (.tms/index.sqlite)                         |
| - Serialized single-writer queue (avoids SQLITE_BUSY locks)       |
| - Git-versioned curated ledger (.tms/curated_knowledge.jsonl)     |
+-------------------------------------------------------------------+
```

---

## Standard MCP Tools

TMS exposes 11 standardized tools over stdio:

| Tool | Purpose | Primary Inputs |
| :--- | :--- | :--- |
| `resolve_task_context` | Primary agent entry point for evidence-backed context | `task_query`, `token_budget`, `compact`, `semantic_hints`, `target_layers`, `unsaved_buffers` |
| `query` | Targeted AST symbol and relationship inspection | `query_type` (`callers`, `symbol`, `neighbors`, `feature_files`), `target_id` |
| `batch` | Runs multiple queries in a single round-trip | `queries_json` (list of query dicts) |
| `edit` | AST-verified symbol replacement (safe buffer and disk) | `rel_path`, `symbol_name`, `new_symbol_code`, `expected_ast_fingerprint` |
| `batch_edit` | Transactional two-phase multi-symbol edit with preflight & rollback | `edits_json`, `unsaved_buffers_json`, `write_to_disk` |
| `outline` | Bounded structural outline without loading full file bodies | `file_path`, `max_symbols`, `max_tokens`, `use_cache` |
| `read_range` | Bounded follow-up read of an exact symbol or line range | `file_path`, `symbol_id` / `symbol_name` / `start_line` & `end_line` |
| `validate` | Safe test or linter execution with output compression | `test_command` (`pytest`, `npm test`, `ruff`, `mypy`, `tsc`) |
| `record_outcome` | Reinforces verified symbols and vocabulary in memory | `task_id`, `phase`, `observed_error`, `status`, `verified_files` |
| `reconcile_knowledge` | Re-indexes repository, prunes stale entries, syncs ledger | _None_ |
| `get_status` | Returns index health, file counts, and WAL stats | _None_ |

---

## Standalone Outline CLI & Host Hooks

For fast local inspection without starting SQLite or Model2Vec, TMS provides standalone CLI commands:

```bash
# Extract a bounded structural outline (JSON or text; supports multiple files or --stdin-json)
python -m tms.app outline src/tms/app.py --format text

# Read a specific symbol or bounded line range
python -m tms.app read src/tms/app.py --lines 1:40

# Evaluate a PreToolUse read payload against configurable outline-first hook policy
python -m tms.app hook pre-read < hook_payload.json
```

---

## Agent Best Practices: The 4 Execution Rules

To achieve maximum token savings, configure your agent system prompt with these 4 rules. Without them, agents can fall into the additive trap of querying TMS and reading entire files anyway.

1. **Step 0 (Resolve Context First):**
   Call `resolve_task_context` exactly once at the beginning of any coding task with the natural language query.
2. **Trust Retrieved Code:**
   Treat the AST symbols, enclosing classes, and interface contracts returned by TMS as primary context. Do not run exploratory grep or inspect unedited companion files.
3. **Strict File Read Limits:**
   Read at most 2 to 3 files that are actively being modified. Read each target file once in full rather than in micro-chunks.
4. **One-Pass Consolidated Edits:**
   Apply all imports, methods, and widget modifications in a single contiguous edit block to prevent re-reading files to verify shifted line numbers.

When agents follow these rules, cumulative session tokens drop by **40% to 50%**.

---

## Empirical Benchmark Results

Measured across 17 real-world development tasks on the TMS v1.0.1 codebase itself (139 files, 775 symbols, 10,543 relationships), spanning storage backends, cross-boundary extractors, AST parsers, caching, editing, and client-side architectures. Results below are **live-verified** by running `python -m tms.app benchmark --deep` and `python -m tms.app benchmark --workflows --budget 2500` against the live SQLite index.

### Methodology

| Parameter | Detail |
| :--- | :--- |
| **Tasks** | 17 built-in `DeepBenchmarkTask` / `EvaluationScenario` tasks across TMS subsystems |
| **Tokenizer** | char/4 approximation (~4 chars per token), consistent across all strategies |
| **Baseline: Full Repo Dump** | All source files concatenated (372,677 tokens for this repo) |
| **Baseline: Lexical / Grep** | BM25 top-5 hits per query; matched files read in full |
| **Baseline: Whole Subsystem** | Every file in the subsystem directory for the task read in full |
| **Baseline: Targeted Search + Reads** | Lexical/grep token matching followed by bounded file/range reads |
| **TMS** | Single `resolve_task_context` call per task (`ordering_mode=mmr_heuristic`, 2,500 token budget) |
| **Quality check** | File-level & entity-level Recall@5, MRR, dependency-chain coverage, and executable task checks |

### Deep Benchmark Results (`tms benchmark --deep`, `compact=True`, `budget=2500`)

| Strategy | Total Tokens (17 tasks) | Avg / Task | Savings vs Baseline |
| :--- | ---: | ---: | :--- |
| **Full Repository Dump** | 6,335,509 | 372,677 | 99.21% fewer tokens with TMS |
| **Targeted Search + Reads** | 206,326 | 12,137 | 75.85% fewer tokens with TMS |
| **Lexical Whole-Files (Grep)** | 152,163 | 8,951 | 67.25% fewer tokens with TMS |
| **Whole-Subsystem Reading** | 138,630 | 8,155 | 64.05% fewer tokens with TMS |
| **TMS Knapsack Resolution** | **49,837** | **2,932** | **2.78x compression vs subsystem** |

> **Context quality:** Across the 17 tasks, TMS achieved **0.9412 File Recall@5** (0.8529 File MRR), **0.6127 Entity Recall@5** (0.6863 Entity MRR), and **1.00 dependency-chain coverage** (compared to 0.7745 File Recall@5 for targeted search + reads).

### Multi-Arm Workflow Benchmark (`tms benchmark --workflows --budget 2500`, `compact=False`)

| Workflow Arm | Main Tokens | Total System Tokens | Avg Latency | File Recall@5 | Entity Recall@5 | MRR | Verified Task Correctness |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `targeted_search_reads` | 31,624 | 31,624 | 1,168.6 ms | 0.2843 | 0.0000 | 0.0000 | 11.76% (2/17) |
| `tms_indexed` | 49,702 | 49,702 | 1,728.8 ms | **0.9412** | **0.6127** | **0.6863** | **82.35% (14/17)** |
| `outline_only_reads` | 50,967 | 50,967 | 1,615.2 ms | 0.6078 | 0.1765 | 0.3586 | 35.29% (6/17) |
| `hook_outline_first` | 50,390 | 50,390 | 1,338.3 ms | 0.5196 | 0.0980 | 0.1992 | 29.41% (5/17) |
| `helper_deterministic` | **25,384** | 49,139 | **50.5 ms** | 0.7157 | 0.3431 | 0.4510 | 64.71% (11/17) |

### Live Per-Task Example (10 of 17 tasks, `tms benchmark --deep`)

| Task | Domain | Subsystem tokens | TMS tokens | Saving | Entity R@5 | File R@5 | File MRR |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| DB-01 | Storage & WAL | 5,748 | 2,384 | 58.5% | 0.67 | 1.00 | 1.00 |
| EDIT-02 | AST Editing | 7,392 | 2,429 | 67.1% | 1.00 | 1.00 | 1.00 |
| CB-03 | Cross Boundary | 10,094 | 3,062 | 69.7% | 0.33 | 1.00 | 0.50 |
| PARSE-04 | AST Parsing | 20,788 | 3,018 | **85.5%** | 1.00 | 1.00 | 1.00 |
| BUDGET-09 | Token Budgeting | 41,865 | 2,860 | **93.2%** | 0.67 | 0.50 | 1.00 |
| MCP-11 | Gateway & MCP | 9,790 | 3,011 | 69.2% | 0.00 | 1.00 | 1.00 |
| SEMANTIC-15 | Semantic & RRF | 7,627 | 3,092 | 59.5% | 0.33 | 1.00 | 0.50 |
| RUST-16 | Rust & Cargo | 4,313 | 3,070 | 28.8% | 0.67 | 1.00 | 1.00 |
| DART-17 | Flutter & Dart | 6,502 | 3,111 | 52.2% | 0.33 | 1.00 | 1.00 |
| DOCINGEST-13 | Unstructured Asset Ingestion | 2,799 | 2,478 | 11.5% | 1.00 | 1.00 | 1.00 |

> **Why some tasks show 0% saving:** 5 tasks have subsystems smaller than the 2,500 token budget floor (e.g., Validation = 546 tokens). There is simply nothing to compress when the source subsystem is already smaller than the target budget.

### Latency

| Metric | Value |
| :--- | :--- |
| Average cold latency (cache empty) | 1,688.0 ms |
| Cached latency (generation-validated hit) | ~9.4 ms |
| Cache speedup factor | 187.2x |
| Average compression ratio vs subsystem | 2.78x |

You can reproduce these numbers on your own repo:

```bash
python -m tms.app benchmark --deep
python -m tms.app benchmark --workflows --budget 2500
python scripts/benchmark_external_repo.py --repo-root /path/to/your/project
```

---

## Development & Testing

```bash
# Run all unit and integration tests (174 tests)
pytest

# Run specific subsystem tests
pytest tests/test_knapsack_assembly.py tests/test_pathway_engine.py tests/test_outline_and_hooks.py
```

---

## Contributing

Contributions are welcome. This project is open to forks, bug reports, feature requests, and pull requests.

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines and the [SECURITY.md](./SECURITY.md) for responsible disclosure.

---

## License

Apache License 2.0. See [LICENSE](LICENSE) for details.
