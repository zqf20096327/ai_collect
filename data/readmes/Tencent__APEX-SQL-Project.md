# APEX-SQL

**APEX-SQL** is an agentic Text-to-SQL framework that shifts the paradigm from *passive schema perception* to *agentic exploration*. Central to our approach is a **Hypothesis-Verification (H-V) loop**, where the agent formulates logical assumptions based on the user question and validates them by executing exploratory SQLs against actual data. This transforms Text-to-SQL from a static translation task into an interactive reasoning task grounded in database reality.

📄 **Paper**: [APEX-SQL: Talking to the data via Agentic Exploration for Text-to-SQL](https://arxiv.org/pdf/2602.16720)

---

## Repository Structure

```
APEX-SQL/
├── BIRD/          # Implementation for the BIRD benchmark (SQLite)
└── Spider2/       # Implementation for the Spider 2.0-Snow benchmark (Snowflake)
```

---

## Framework Overview

APEX-SQL applies agentic exploration to two sequential stages: **Schema Linking** and **SQL Generation**.

### Stage 1 — Agentic Exploration for Schema Linking

Given massive industrial databases with ambiguous naming conventions, APEX-SQL navigates the schema through the H-V loop:

1. **Logical Planning** (`schema_linking.py`)  
   Generates a *schema-agnostic* logical plan that verbalizes the question's computational steps and latent constraints, deliberately isolating high-level reasoning from the noise of concrete table/column names. Multiple reasoning paths are aggregated into a unified master plan via a consensus-based synthesis strategy.

2. **Dual-Pathway Pruning** (`schema_linking.py`)  
   Simultaneously executes a *negative pass* (deletion) to remove obvious noise and a *positive pass* (selection) to identify relevant columns, then fuses both results. This prevents standard selection from missing subtle foreign keys while avoiding aggressive deletion of structural dependencies.

3. **Parallel Data Profiling** (`schema_linking.py`)  
   Assigns independent agents to each table to dynamically generate exploratory SQL queries grounded in the hypothesized column roles, validating data patterns against real data.

4. **Global Synthesis** (`schema_linking.py`)  
   Integrates all empirical observations to make the final decision on the sufficient schema subgraph, ensuring topological connectivity across verified elements.

### Stage 2 — Agentic Exploration for SQL Generation

5. **Macro Plan Aggregation** (`preprocess_macro_plans.py`)  
   Aggregates the per-question logical plans generated during Schema Linking into a unified macro plan corpus, consolidating multiple reasoning paths via a consensus-based synthesis strategy to produce a single master plan per question.

6. **Deterministic Guidance Retrieval** (`preprocess_select_tips.py`)
   Leverages the logical plan to infer potential SQL realization paths for each logical step, then applies a rule engine to extract operational keywords and match them against a predefined library of SQL best practices. This deterministic keyword mapping transforms the logical plan from a passive blueprint into an executable verification guide.

7. **Agentic Exploration** (`run.py` → `agent.py`)
   Guided by the retrieved directives, the agent navigates a flexible action space through the H-V loop:
   - **Profiling**: Autonomously generates exploratory queries to resolve uncertainties about value distributions and data formats.
   - **Consolidation**: Periodically compresses interaction history to prevent context saturation and maintain logical coherence.
   - **SQL Synthesis**: Synthesizes a candidate SQL query grounded in empirical evidence, with execution-guided self-correction on errors.
   - **Confirmation**: Performs a final semantic fidelity check to verify that the SQL logic aligns with user requirements and accumulated observations.

   Multiple candidates are sampled per question. For BIRD, the final answer is selected via a **reward model**; for Spider 2.0-Snow, **result-based majority voting** with model-selection as a tie-breaker is used.

8. **Evaluation** (`eval.py` / `evaluate_from_dir.py`)
   Evaluates generated SQL against ground-truth answers (Execution Accuracy, Pass@K).

---

## Workflow Diagram

```
                    ┌──────────────────────────────────────────────────┐
                    │              Schema Linking                      │
                    │                                                  │
                    │  1. Logical Planning (schema-agnostic H-V plan)  │
                    │         ↓                                        │
                    │  2. Dual-Pathway Pruning (delete + select)       │
                    │         ↓                                        │
                    │  3. Parallel Data Profiling (per-table agents)   │
                    │         ↓                                        │
                    │  4. Global Synthesis (topological connectivity)  │
                    └──────────────────┬───────────────────────────────┘
                                       │  sufficient schema subgraph D*
                    ┌──────────────────▼───────────────────────────────┐
                    │              SQL Generation                      │
                    │                                                  │
                    │  5. Macro Plan Aggregation                       │
                    │         ↓                                        │
                    │  6. Deterministic Guidance Retrieval             │
                    │         ↓                                        │
                    │  7. Agentic Exploration (H-V loop)               │
                    │       ├─ Profiling                               │
                    │       ├─ Consolidation                           │
                    │       ├─ SQL Synthesis + self-correction         │
                    │       └─ Confirmation                            │
                    │         ↓                                        │
                    │  8. Multi-sample voting / Reward model selection │
                    └──────────────────┬───────────────────────────────┘
                                       │
                    ┌──────────────────▼───────────────────────────────┐
                    │              Evaluation                          │
                    │  eval.py / evaluate_from_dir.py                  │
                    └──────────────────────────────────────────────────┘
```

---

## Results

| Benchmark | Metric | Score |
|-----------|--------|-------|
| BIRD-Dev | Execution Accuracy | **70.7%** |
| Spider 2.0-Snow | Execution Accuracy | **53.4%** |
| Spider 2.0-Snow | Pass@8 | **68.4%** |

---

## Benchmarks

| Benchmark | Description | Directory |
|-----------|-------------|-----------|
| [BIRD](https://bird-bench.github.io/) | Large-scale cross-domain Text-to-SQL benchmark (SQLite) | `BIRD/` |
| [Spider 2.0](https://spider2-sql.github.io/) | Enterprise-level benchmark with Snowflake cloud databases, averaging 800+ columns per database | `Spider2/` |

See the README in each subdirectory for quick start instructions.
