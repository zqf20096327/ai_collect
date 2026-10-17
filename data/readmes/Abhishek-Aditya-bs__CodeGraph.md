<p align="center">
  <img src="docs/diagrams/banner.svg" alt="CodeGraph — turn any codebase into a queryable knowledge graph" width="100%">
</p>

<p align="center">
  <b>CodeGraph</b> turns any codebase into a Neo4j knowledge graph of its files, classes, functions and interfaces —
  then layers vector embeddings on top so you can ask it questions in plain English.<br>
  Graph traversal and semantic search answer together, through a clean Streamlit interface.
</p>

<p align="center">
  <a href="https://codegraph-website.pages.dev"><img src="https://img.shields.io/badge/Live_site-codegraph--website.pages.dev-D97757?style=flat-square" alt="Website"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-3D3D3A?style=flat-square" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Python-3.10+-3D3D3A?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Neo4j-Graph_DB-3D3D3A?style=flat-square&logo=neo4j&logoColor=white" alt="Neo4j">
  <img src="https://img.shields.io/badge/OpenAI-Embeddings-3D3D3A?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/Streamlit-UI-3D3D3A?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-Compose-3D3D3A?style=flat-square&logo=docker&logoColor=white" alt="Docker">
</p>

<p align="center">
  <a href="https://codegraph-website.pages.dev">Website</a> &nbsp;·&nbsp;
  <a href="#how-it-works">How it works</a> &nbsp;·&nbsp;
  <a href="#the-workflow">Workflow</a> &nbsp;·&nbsp;
  <a href="#quick-start">Quick start</a> &nbsp;·&nbsp;
  <a href="#usage-guide">Usage</a> &nbsp;·&nbsp;
  <a href="docs/codegraph_architecture.md">Architecture</a>
</p>

---

## Overview

Structure and meaning are different kinds of information. A call graph is topology; "what does this
module *do*" is semantics. Keyword search and plain vector search each capture only one of them.

CodeGraph keeps both and bridges them. It builds a **knowledge graph** of typed code entities and a
**semantic vector index** over the same source, stores them in a single Neo4j database, and connects
them with a bridge layer — so one natural-language question can walk relationships *and* rank by
similarity in a single pass.

- **Hybrid GraphRAG** — graph traversal combined with vector search, so structure and meaning inform every answer instead of competing.
- **One queryable database** — the knowledge graph, the 3072-dimensional vector index, and file metadata all live in Neo4j.
- **Natural-language queries** — ask in plain English and get answers grounded in real code, with the surrounding structure attached.
- **A real interface** — a Streamlit app with live connection status, a step-by-step workflow tracker, and real-time feedback, not a notebook demo.
- **Configurable models** — bring any OpenAI model for entity extraction and answers; tune chunk size, overlap, and the embedding model from configuration.
- **One-command Docker** — Compose brings the app and Neo4j up together; configure a `.env`, run, and start querying.

## Demo

<p align="center">
  <img src="assets/CodeGraphDemo.gif" alt="CodeGraph in action: from codebase ingestion to natural-language querying" width="90%">
</p>

<p align="center"><i>From codebase ingestion to intelligent querying — the full pipeline runs from the UI.</i></p>

## How it works

CodeGraph stores three layers in one Neo4j database and bridges them so a single query can use all three.

<p align="center">
  <img src="docs/diagrams/architecture.svg" alt="Three-layer GraphRAG architecture converging on a single Neo4j database" width="100%">
</p>

| Layer | What it holds | Why it matters |
|-------|---------------|----------------|
| **Structural** | A knowledge graph of typed nodes (`Class`, `Function`, `Interface`, `File`, `Package`) wired by `INHERITS`, `IMPLEMENTS`, `CALLS`, `CONTAINS`, `DEPENDS_ON`. Built by an LLM graph transformer over the parsed source. | Captures explicit relationships — the topology of the code. Answers "how is this connected?" |
| **Semantic** | `CodeChunk` nodes holding raw code plus a 3072-dimensional embedding from OpenAI `text-embedding-3-large`, indexed for cosine similarity. | Captures meaning, not just exact names. Finds relevant code even when the words differ. |
| **Bridge** | `REPRESENTS`, `CONTAINS_CHUNK`, and `PART_OF_FILE` relationships that link every chunk back to the entity it belongs to. | Lets one query traverse structure *and* rank by meaning, returning answers with context attached. |

## The workflow

The whole pipeline runs from the Streamlit interface with a live progress tracker — point it at a
codebase and watch it ingest, build, index, and become queryable.

<p align="center">
  <img src="docs/diagrams/pipeline.svg" alt="Six-step workflow: input, ingestion, knowledge graph, vector index, query, manage" width="100%">
</p>

1. **Input** — point at a public GitHub repository or a local folder. Inputs are validated before anything runs.
2. **Ingestion** — configurable parsing walks the source and splits it into overlapping chunks, with progress tracked end to end.
3. **Knowledge graph** — an LLM extracts entities and relationships into Neo4j (classes, functions, interfaces, files).
4. **Vector index** — `text-embedding-3-large` vectors are computed and indexed for cosine similarity search.
5. **Query** — natural-language questions return answers with rich, structured context drawn from both layers.
6. **Manage** — live database statistics, health checks, and guarded cleanup; reset the UI without losing your data.

## Query processing

A question never hits just one retriever. CodeGraph runs vector search to find the most relevant code,
maps those chunks to graph entities, traverses the graph for surrounding context, and only then asks the
LLM to synthesize a grounded answer.

<p align="center">
  <img src="docs/diagrams/query-flow.svg" alt="Hybrid query flow: question to vector search to graph context to LLM synthesis to grounded answer" width="100%">
</p>

1. **Vector search** — embed the question and retrieve the top-`k` `CodeChunk` nodes by cosine similarity.
2. **Entity mapping** — follow `REPRESENTS` from those chunks to the `Class` / `Function` entities they describe.
3. **Graph traversal** — walk relationships out from those entities to gather structural context.
4. **LLM synthesis** — combine semantic matches and structural context into a grounded prompt and generate a conversational answer.
5. **Grounded answer** — return the response alongside supporting code chunks, related entities, relationships, and similarity scores.

## Data model

<p align="center">
  <img src="docs/diagrams/schema.svg" alt="Neo4j data model: nodes and the structural and bridge relationships between them" width="100%">
</p>

```cypher
// Structural layer (knowledge graph)
(Class)-[:INHERITS]->(Class)
(Class)-[:IMPLEMENTS]->(Interface)
(Function)-[:CALLS]->(Function)
(File)-[:CONTAINS]->(Class|Function|Interface)
(Package)-[:CONTAINS]->(File)

// Semantic layer (vector search)
(CodeChunk {embedding: [3072 dimensions]})
(File)-[:CONTAINS_CHUNK]->(CodeChunk)

// Bridge layer (integration)
(CodeChunk)-[:REPRESENTS]->(Class|Function)
(CodeChunk)-[:PART_OF_FILE]->(Class|Function)

// Vector index
CREATE VECTOR INDEX code_chunks_vector_index
FOR (c:CodeChunk) ON (c.embedding)
OPTIONS {indexConfig: {
    `vector.dimensions`: 3072,
    `vector.similarity_function`: 'cosine'
}}
```

## Quick start

### Docker (recommended)

The fastest path to a running instance, app and database together.

**Prerequisites:** Docker, Docker Compose, and an OpenAI API key.

1. **Clone and configure:**

```bash
git clone https://github.com/Abhishek-Aditya-bs/CodeGraph
cd CodeGraph

# Create your .env file
cat > .env << 'EOF'
NEO4J_URI=neo4j://neo4j:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_secure_password
OPENAI_API_KEY=your_openai_api_key_here
CHUNK_SIZE=500
CHUNK_OVERLAP=50
EMBEDDING_MODEL=text-embedding-3-large
LLM_MODEL=gpt-4o
EOF
```

2. **Check prerequisites and start:**

```bash
./docker/docker-prerequisite-check.sh
docker compose -f docker/docker-compose.yml up -d
```

3. **Open the application:**

- CodeGraph UI: <http://localhost:8501>
- Neo4j Browser: <http://localhost:7474>

### Local development

For development or manual control over the stack.

**Prerequisites:** Python 3.10+, Docker (for Neo4j), and an OpenAI API key.

1. **Clone and set up the environment:**

```bash
git clone https://github.com/Abhishek-Aditya-bs/CodeGraph
cd CodeGraph

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Create the configuration:**

```bash
cat > .env << 'EOF'
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password
OPENAI_API_KEY=your_openai_api_key_here
CHUNK_SIZE=500
CHUNK_OVERLAP=50
EMBEDDING_MODEL=text-embedding-3-large
LLM_MODEL=gpt-4o
EOF
```

3. **Start Neo4j:**

```bash
docker run -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  -e NEO4J_PLUGINS='["apoc"]' \
  -e NEO4J_apoc_export_file_enabled=true \
  -e NEO4J_apoc_import_file_enabled=true \
  -e NEO4J_dbms_security_procedures_unrestricted='apoc.*' \
  -e NEO4J_dbms_security_procedures_allowlist='apoc.*' \
  neo4j:latest
```

4. **Launch CodeGraph:**

```bash
streamlit run app/main.py
```

## Usage guide

### System status (sidebar)

- **Neo4j connection** — live status of the database connection.
- **OpenAI API key** — confirms the key is configured.
- **Vector index** — indicates the system is ready for semantic queries.
- **Live metrics** — real-time node and relationship counts.

### Workflow tabs

| Tab | What you do |
|-----|-------------|
| **Codebase input** | Provide a GitHub URL (HTTPS or SSH) for one-click cloning, or an absolute local folder path. Inputs are validated and summarized. |
| **Ingestion** | Configure chunk size (100–2000 chars), overlap (0–200 chars), and file extensions. Parsing is tracked with real-time progress. |
| **Knowledge graph** | Run LLM-powered entity extraction into Neo4j, with API-call progress and statistics about the graph elements created. |
| **Vector index** | Generate `text-embedding-3-large` embeddings, store them in Neo4j with a cosine-similarity index, and initialize the query processor. |
| **Query** | Ask natural-language questions, tune result count and graph context, and read rich responses with syntax-highlighted code chunks and similarity scores. |
| **Database** | View live statistics and node/relationship breakdowns; clear data (two-step confirmation), reset the UI without losing data, or re-sync UI state. |

### Working with existing data

CodeGraph detects existing data on startup and synchronizes the session with the database, so your work
survives a page refresh. Use **Sync with Database** in the Database tab to re-synchronize manually.

## Example queries

**Architecture and design**

```text
What is the overall architecture and how are the components connected?
What design patterns are used in this codebase?
What are the main classes and their relationships?
How is the database schema structured?
```

**End-to-end flows**

```text
How does creating a new record work from API request to database storage?
Show me the complete flow for user registration and authentication.
How does the service layer interact with the repository layer?
```

**Implementation details**

```text
How is authentication and authorization implemented across the application?
How does the application handle errors and what custom exceptions are defined?
How is data validated when creating new records?
What REST endpoints are available and what operations do they perform?
```

A ready-to-run query set for a sample Spring Boot repository lives in [`demo/questions.md`](demo/questions.md).

## Configuration

### Environment variables

| Variable | Required | Default | Description |
|----------|:--------:|---------|-------------|
| `NEO4J_URI` | Yes | — | Neo4j connection URI |
| `NEO4J_USERNAME` | Yes | — | Neo4j username |
| `NEO4J_PASSWORD` | Yes | — | Neo4j password |
| `OPENAI_API_KEY` | Yes | — | OpenAI key for embeddings and the LLM |
| `CHUNK_SIZE` | No | `500` | Code chunk size for processing |
| `CHUNK_OVERLAP` | No | `50` | Overlap between code chunks |
| `EMBEDDING_MODEL` | No | `text-embedding-3-large` | OpenAI embedding model |
| `LLM_MODEL` | No | `gpt-4o` | OpenAI model for entity extraction and answers |

For **Docker**, use the Compose service name so containers can reach the database:

```env
NEO4J_URI=neo4j://neo4j:7687
```

For **local development**, point at localhost:

```env
NEO4J_URI=neo4j://localhost:7687
```

## Project structure

```text
CodeGraph/
├── app/
│   ├── main.py              # Streamlit UI and end-to-end workflow
│   ├── config.py            # Environment and configuration loading
│   ├── database.py          # Singleton Neo4j connection manager
│   ├── ingestion.py         # Repository cloning, parsing, and chunking
│   ├── graph_builder.py     # Knowledge graph, vector index, and bridges
│   ├── query_processor.py   # Hybrid GraphRAG query processing
│   └── utilities/           # File, folder, Git, LLM, and Neo4j helpers
├── docker/
│   ├── Dockerfile                    # Container image definition
│   ├── docker-compose.yml            # App + Neo4j orchestration
│   └── docker-prerequisite-check.sh  # Environment validation
├── docs/
│   ├── codegraph_architecture.md     # Detailed architecture guide
│   └── diagrams/                     # SVG architecture and flow diagrams
├── tests/
│   ├── core/                # Core unit tests
│   ├── integration/         # Integration tests
│   └── fixtures/            # Self-contained test data
├── assets/                  # Demo media
├── requirements.txt         # Python dependencies
├── run_tests.py             # Test runner with selectable modes
└── README.md
```

## Testing

CodeGraph ships with self-contained test data — no external repositories required for the core suite.

```bash
# Run the full suite
python -m pytest tests/ -v

# Core component tests only
python -m pytest tests/core/ -v
```

The test runner offers selectable modes:

```bash
python run_tests.py --unit          # Fast unit tests only
python run_tests.py --core          # Core functionality tests
python run_tests.py --integration   # Full integration tests
```

Expensive tests are skipped by default during development:

```bash
export SKIP_INTEGRATION_TESTS=true
export SKIP_API_COST_TESTS=true
export SKIP_SLOW_TESTS=true
```

To run the complete suite including API-cost tests, provide the Java design-patterns repository as a fixture:

```bash
mkdir -p cloned_repos
cd cloned_repos
git clone https://github.com/iluwatar/java-design-patterns.git
cd ..

export SKIP_API_COST_TESTS=false
python -m pytest tests/ -v
```

Without that fixture, API-cost tests are skipped automatically and the core suite still passes.

## Docker operations

```bash
# Start services
docker compose -f docker/docker-compose.yml up -d

# View logs
docker compose -f docker/docker-compose.yml logs -f codegraph
docker compose -f docker/docker-compose.yml logs -f neo4j

# Stop services
docker compose -f docker/docker-compose.yml down

# Rebuild and restart
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up -d --build
```

### Public deployment (EC2 / VPS)

```bash
# Install Docker on the server
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Deploy
git clone https://github.com/Abhishek-Aditya-bs/CodeGraph
cd CodeGraph
# Create the .env file with your configuration
./docker/docker-prerequisite-check.sh
docker compose -f docker/docker-compose.yml up -d
```

Then reach the app at `http://YOUR_SERVER_IP:8501`. The image uses a multi-stage build, runs as a
non-root user, exposes health checks, and persists data on volumes across restarts.

## Troubleshooting

| Symptom | Resolution |
|---------|------------|
| **Neo4j connection failed** | Confirm Neo4j is running on the expected port, check the credentials in `.env`, and verify firewall settings. |
| **OpenAI API error** | Verify the API key in `.env`, confirm available account credits, and check network connectivity. |
| **"Complete workflow first" after refresh** | Use **Sync with Database** in the Database tab, and confirm data exists in the Neo4j Browser. |
| **Docker issues** | Run `./docker/docker-prerequisite-check.sh`, inspect `docker compose logs`, and ensure `.env` is in the project root. |

## Performance tuning

- **Chunk size:** 500–1000 characters balances context and cost.
- **Overlap:** 50–100 characters preserves context across chunk boundaries.
- **Result count:** 5–10 results keeps queries fast and focused.
- **File extensions:** limit ingestion to the languages you care about.
- **Database hygiene:** clear the database before processing a different codebase, and review node and relationship counts in the sidebar.

Approximate footprint: each code chunk stores a 3072-dimensional vector (~12 KB). Vector search
typically returns in well under 100 ms, and graph traversal in tens of milliseconds, on most codebases.

## Tech stack

Built with **Python**, **Neo4j**, **LangChain**, **OpenAI** embeddings and models, **Streamlit**, and **Docker**.

CodeGraph supports a wide range of languages out of the box, including Python, Java, JavaScript,
TypeScript, C, C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, and Scala.

For a deeper dive into the layers, schema, and query internals, see
[`docs/codegraph_architecture.md`](docs/codegraph_architecture.md).

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Make your changes and add tests where applicable.
4. Ensure the suite passes: `python run_tests.py`.
5. Open a pull request.

Please follow PEP 8, add docstrings to new functions, and update documentation as needed.

## License

Released under the [MIT License](LICENSE).

## Acknowledgments

- **Neo4j** — graph database and native vector index.
- **OpenAI** — embeddings and language models.
- **LangChain** — graph-transformer and RAG building blocks.
- **Streamlit** — the interactive interface.
