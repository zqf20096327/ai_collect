# text2shacl

## An Ontology-Driven Multi-Agent System for Extracting SHACL from ERA Business Rules

**text2shacl** addresses the challenge of manually creating SHACL validation shapes for large OWL ontologies. Given the ERA (European Union Agency for Railways) ontology and its official technical documentation (the RINF Application Guide), the system automatically generates SHACL constraints in Turtle format that can be used to validate railway infrastructure data.

The system has been evaluated on two versions of the RINF Application Guide: **v3.1.0** (native HTML) and **v1.6.1** (converted from PDF), against a manually curated gold standard (`era-shapes.ttl`), across five LLMs: Gemma 3 12B, GPT-OSS 120B, Llama 3.3 70B, Mixtral 8x7B, and Qwen3-Next 80B-A3B.

---

## How It Works

The pipeline follows four main steps:

1. **HTML preprocessing** — The RINF Application Guide is cleaned and split into semantic chunks. Text, tables and images are extracted for downstream processing.

2. **RAG indexing** — Text and table chunks are summarized by an LLM, images are described by a vision model, and the resulting summaries are stored in Chroma. The original chunks are stored in Redis and retrieved when generating constraints.

3. **SHACL generation** — For each ontology property, a LangGraph multi-agent workflow gathers evidence from the ontology, optional Astrea baseline and RAG context, then generates SHACL shapes in Turtle.

4. **Post-processing and merging** — Generated shapes are validated, cleaned and optionally merged with Astrea using either `priority-llm` or `restrictive` strategies.

---

## Project Structure

```
text2shacl_hf/
│
├── environment.yml                  # Conda environment definition
├── LICENSE
├── README.md
│
├── src/                             # Source code
│   ├── main.py                      # Entry point
│   ├── rag.py                       # RAG indexing and retrieval pipeline
│   ├── multiagent.py                # LangGraph multi-agent pipeline
│   ├── model_loader.py              # Unified HF/Databricks model router
│   ├── model_loader_hf.py           # HuggingFace local inference
│   ├── model_loader_databricks.py   # Databricks AI Gateway inference
│   ├── preprocess_html.py           # HTML splitter for native HTML guide
│   ├── preprocess_html_from_pdf.py  # HTML splitter for PDF-converted guide
│   ├── utils.py                     # SHACL post-processing utilities
│   ├── prompts.py                   # Prompt loader from JSON
│   ├── Logger.py                    # Custom logger
│   │
│   ├── prompts/
│   │   ├── rag.json                 # Summarization prompts
│   │   └── multiagent.json          # Agent prompts and variants
│   │
│   └── scripts/
│       ├── merge_shacl_shapes.py    # Merge strategies
│       ├── evaluate_shacl_quality.py
│       ├── evaluate_sparql_constraints.py
│       ├── run_evaluation.py        # Batch evaluation → CSV
│       ├── plot_results.py          # Bar+line charts
│       ├── plot_heatmaps.py         # Heatmap figures
│       ├── run_merges.sh            # Run all merges
│       ├── run_experiments.sh       # Run all experiments
│       └── shacl_consistency_validator_extended.py
│
├── resources/                       # Input resources
│   ├── content/
│   │   ├── rinf_application_guide_v3.2.1.html
│   │   ├── rinf_application_guide_v3.2.1_files/
│   │   └── previous_version/
│   │       ├── rinf_application_guide_v1.6.1-from-pdf.html
│   │       └── RINF_Application_guide_V1.6.1.pdf
│   │
│   └── knowledge/
│       ├── ontology.ttl             # ERA OWL ontology
│       ├── astrea-shapes.ttl        # Astrea baseline shapes
│       ├── era-shapes.ttl           # Gold standard SHACL shapes
│       └── previous_version/        # Same resources for v1.6.1
│
├── out/                             # Generated artifacts and results
│   ├── generated_shapes/            # Generated TTLs
│   ├── integrations/                # Merged TTLs
│   │   ├── priority-llm/
│   │   └── restrictive/
│   ├── figures/                     # Generated evaluation figures
│   ├── logs/                        # Execution logs
│   ├── temperature_tests/           # Temperature sensitivity TTLs
│   └── results.csv                  # Full evaluation results
│
└── cache/                           # Local cache artifacts
    ├── chroma_db/                   # Chroma vector indexes
    └── processing_cache/            # Pickled RAG summaries and extracted images
```

---

## Requirements

### Environment

Create the conda environment from the provided file:

```bash
conda env create -f environment.yml
conda activate text2shacl
```

### Services

Two services must be running before executing the pipeline:

**Redis** — used as the document store for the RAG pipeline:
```bash
# If installed via conda:
redis-server

# Or via conda install if not available:
conda install -c conda-forge redis -y
redis-server
```

**Databricks AI Gateway** — the system uses Databricks as the inference backend for all LLM calls. Ensure you have access to a Databricks workspace with the required models available.

### Environment Variables

Create a `.env` file in the project root:

```bash
# Databricks (required)
DATABRICKS_TOKEN=dapi...
DATABRICKS_BASE_URL=https://<your-workspace>.cloud.databricks.com/ai-gateway/mlflow/v1

# HuggingFace (required only for local inference)
HF_TOKEN=hf_...
HF_HOME=/path/to/hf/cache       # Override if home disk is limited

# RAG tuning (optional)
RAG_TEXT_MAX_NEW_TOKENS=256
RAG_IMG_MAX_NEW_TOKENS=900
RAG_MAX_CONCURRENCY=1

# PyTorch memory (optional, recommended for large models)
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

---

## Usage

### Running a Single Experiment

```bash
python3 src/main.py resources/content/rinf_application_guide_v3.2.1.html \
  --html_version "3.2.1" \
  --ontology resources/knowledge/ontology.ttl \
  --astrea resources/knowledge/astrea-shapes.ttl \
  --llm_model "databricks-meta-llama-3-3-70b-instruct" \
  --vision_model "gemma_3_12b" \
  --embedding_model "Qwen/Qwen3-Embedding-0.6B" \
  --temperature 0.5 \
  --prompting_technique "multiagent" \
  --verbosity 3
```

To run **without the Astrea baseline** (the `--astrea` argument is optional):

```bash
python3 src/main.py resources/content/rinf_application_guide_v3.2.1.html \
  --html_version "3.2.1" \
  --ontology resources/knowledge/ontology.ttl \
  --llm_model "databricks-gpt-oss-120b" \
  --vision_model "gemma_3_12b" \
  --embedding_model "Qwen/Qwen3-Embedding-0.6B" \
  --temperature 0.5 \
  --prompting_technique "multiagent" \
  --verbosity 3
```

Output is written to `out/generated_shapes/{version_slug}/{version_slug}_{model_tag}_t{temp}[_without_astrea].ttl`.

#### Key Arguments

| Argument | Description | Default |
|---|---|---|
| `file` | Path to the input HTML file to be processed | required |
| `--ontology` | Path to the ontology TTL file | required |
| `--astrea` | Path to the Astrea SHACL shapes TTL file. Optional | `None` |
| `--html_version` | Input HTML version. Supported values: `"3.2.1"` and `"1.6.1"` | `"3.2.1"` |
| `--llm_model` | LLM model ID, either a HuggingFace model ID or a Databricks short name | `databricks-gpt-oss-120b` |
| `--vision_model` | Vision model ID, either a HuggingFace model ID or a Databricks short name | `databricks-gemma-3-12b` |
| `--embedding_model` | Embedding model ID, either a HuggingFace model ID or a Databricks short name | `Qwen/Qwen3-Embedding-0.6B` |
| `--temperature` | Generation temperature | `0.5` |
| `--prompting_technique` | Prompt file stem under `src/prompts/`, without `.json` | `multiagent` |
| `--force_process` | Force reprocessing even if cached results are available | `False` |
| `--verbosity` | Log verbosity level: `0=errors`, `1=warnings`, `2=info`, `3=debug` | `1` |

---

## Used Models

| Model | Databricks name | Type |
|---|---|---|
| Llama 3.3 70B Instruct | `databricks-meta-llama-3-3-70b-instruct` | Text LLM |
| GPT-OSS 120B | `databricks-gpt-oss-120b` | Text LLM |
| Qwen3-Next 80B-A3B | `databricks-qwen3-next-80b-a3b-instruct` | Text LLM |
| Mixtral 8x7B | `databricks-mixtral-8x7b-instruct` | Text LLM |
| Gemma 3 12B | `gemma_3_12b` | Text LLM / Vision LLM |
| Qwen3 Embedding 0.6B | `Qwen/Qwen3-Embedding-0.6B` | Embeddings (HF) |

In addition to the models listed above, the framework supports any compatible model available through Databricks Model Serving or HuggingFace. For Databricks, provide the corresponding serving endpoint name. For HuggingFace, provide the full model identifier, such as `meta-llama/Llama-3.3-70B-Instruct`, as long as the model is accessible and compatible with the selected inference backend.

---

## Running All Experiments

```bash
chmod +x src/scripts/run_experiments.sh
./src/scripts/run_experiments.sh
```

## Merging Generated Shapes with the Astrea Baseline

```bash
# Priority-LLM strategy (recommended)
python3 src/scripts/merge_shacl_shapes.py \
  resources/knowledge/astrea-shapes.ttl \
  out/generated_shapes/rinf-application-guide-v3-2-1/rinf-application-guide-v3-2-1_gpt-oss-120b_t0.50.ttl \
  --technique priority-llm

# Restrictive strategy
python3 src/scripts/merge_shacl_shapes.py \
  resources/knowledge/astrea-shapes.ttl \
  out/generated_shapes/rinf-application-guide-v3-2-1/rinf-application-guide-v3-2-1_gpt-oss-120b_t0.50.ttl \
  --technique restrictive

# Run all merges at once
chmod +x src/scripts/run_merges.sh
./src/scripts/run_merges.sh
```

Output is placed in `out/integrations/priority-llm/` or `out/integrations/restrictive/`.

---

## Evaluation

### Quality Evaluation (Target Classes, Property Paths, Value Constraints)

```bash
python3 src/scripts/evaluate_shacl_quality.py \
  --gold resources/knowledge/era-shapes.ttl \
  --pred out/generated_shapes/rinf-application-guide-v3-2-1/rinf-application-guide-v3-2-1_gpt-oss-120b_t0.50.ttl
```

Reports Precision / Recall / F1 for three levels: target classes (structural), property paths (structural), and value constraints (semantic). Also computes a restrictiveness analysis (exact / stronger / weaker / incomparable vs. gold).

### SPARQL Constraint Evaluation

```bash
python3 src/scripts/evaluate_sparql_constraints.py \
  --gold resources/knowledge/era-shapes.ttl \
  --pred out/generated_shapes/rinf-application-guide-v3-2-1/rinf-application-guide-v3-2-1_gpt-oss-120b_t0.50.ttl
```

Evaluates `sh:SPARQLConstraint` applicability shapes by matching `era:affectedClass` and `era:affectedProperty` metadata.

### Batch Evaluation → CSV

```bash
python3 src/scripts/run_evaluation.py \
  --gold_v321 resources/knowledge/era-shapes.ttl \
  --gold_v161 resources/knowledge/previous_version/era-shapes.ttl \
  --output out/results.csv
```

Scans the generated and integrated SHACL directories under `out/` and produces a single `out/results.csv` with all metrics.

### Generating Figures

```bash
# Bar + line charts (P/R/F1 per model, 6 figures)
python3 src/scripts/plot_results.py --csv out/results.csv --out out/figures/

# Heatmaps (vs Astrea, vs Integration strategy, vs Guide version)
python3 src/scripts/plot_heatmaps.py --csv out/results.csv --out out/figures/
```

---

## Evaluation Results

Best result obtained with temperature `0.5` on the ERA ontology v3.2.1:

| Configuration | Model | without Astrea | TC F1 | PP F1 | VC F1 |
|---|---|---:|---:|---:|---:|
| Generated Shapes (LLM) | GPT-OSS 120B | True | 0.904 | 0.934 | 0.699 |

The best-performing configuration is the generated-only output produced by GPT-OSS 120B without merging with Astrea:

`rinf-application-guide-v3-2-1_gpt-oss-120b_t0.50_without_astrea.ttl`

This run achieves the strongest overall balance across target classes, property paths, and value constraints, with the highest value-constraint F1 among the evaluated configurations.

## Authors

**CiTIUS - Universidade de Santiago de Compostela**

- Adrián Martínez Balea
- David Chaves Fraga