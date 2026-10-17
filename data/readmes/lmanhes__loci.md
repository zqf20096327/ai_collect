# Loci

**Your personal knowledge map.** Loci transforms any document into a visual, explorable knowledge space with automatic flashcard generation and spaced repetition for long-term retention.

![Loci Overview](images/loci-overview.png)

## What is Loci?

Loci is a learning system that:

- **Ingests anything**: PDFs, markdown, text files, handwritten notes (photos), audio transcriptions, images
- **Extracts knowledge**: Automatically identifies concepts and their relationships
- **Visualizes spatially**: Displays your knowledge as an interactive honeycomb map where related concepts cluster together
- **Strengthens memory**: Generates flashcards and schedules reviews using spaced repetition (FSRS algorithm)

## Features

### Visual Knowledge Map
Navigate your knowledge like a map. Zoom from high-level categories down to individual concepts. Related ideas appear close together thanks to semantic clustering.

![Visual Knowledge Map](images/loci-select.png)

### Universal File Ingestion
Drop in any file type:
- Documents (PDF, Markdown, TXT)
- Handwritten notes (photos processed via LLM vision)
- Images with text or diagrams
- Audio transcriptions

![Upload Documents](images/loci-upload.png)

### Automatic Flashcard Generation
Each concept generates smart flashcards using two formats:
- **Cloze deletions** (easy/medium): Fill-in-the-blank with context cues
- **Q&A** (hard): Direct questions for deeper active recall

### Spaced Repetition (FSRS)
Reviews are scheduled at the optimal moment—just before you'd forget. The system tracks:
- **Stability**: How long until memory drops to 90%
- **Difficulty**: How hard the material is for you
- **Retrievability**: Current probability of recall

### Semantic Search
Find any concept instantly. Search queries match semantically, not just by keywords.

![Semantic Search](images/loci-search.png)

![Search Results](images/loci-search-results.png)

---

## How It Works

### 1. Document Processing
Files are parsed and split into meaningful chunks using LangChain text splitters. Images and handwritten notes are processed through LLM vision capabilities.

### 2. Concept Extraction
An LLM analyzes each chunk to extract:
- A clear title
- A concise summary
- The core content

### 3. Embedding Generation
Each concept is converted to a high-dimensional vector (embedding) that captures its semantic meaning. Similar concepts have similar embeddings.

### 4. Dimensionality Reduction (UMAP)
Embeddings are projected from high-dimensional space to 2D coordinates using UMAP, preserving semantic relationships. This creates the spatial layout where similar concepts appear near each other.

### 5. Clustering (HDBSCAN)
Concepts are grouped into clusters using HDBSCAN, a density-based algorithm that finds natural groupings without requiring a predefined number of clusters.

### 6. Honeycomb Visualization
The 2D coordinates are rendered as an interactive honeycomb grid. Each hexagon represents a concept. Opacity reflects learning progress—mastered concepts fade while due reviews stand out.

### 7. Flashcard Generation
For each concept, the LLM generates flashcards:
- Cloze deletions provide context cues for easier learning
- Q&A format tests deeper recall for challenging material

### 8. Spaced Repetition (FSRS)
The FSRS algorithm schedules reviews based on your performance:
- **Again**: Reset, review soon
- **Hard**: Small interval increase
- **Good**: Normal interval increase
- **Easy**: Large interval increase, decrease difficulty

---

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+ with pnpm
- Either:
  - **OpenAI** (recommended): `gpt-4.1-mini` + `text-embedding-3-small`
  - **Ollama** (local): `ministral-3:8b` + `embeddinggemma`

### Quick Start

```bash
# Clone and enter the project
git clone <repo-url>
cd loci

# Run the start script
./start.sh
```

The script will guide you through setup and start both servers.

### Manual Setup

#### Backend

```bash
cd backend

# Install dependencies with uv
uv sync

# Set your OpenAI API key
export OPENAI_API_KEY="sk-..."

# Or for local mode with Ollama:
# 1. Install Ollama: https://ollama.ai
# 2. Pull models: ollama pull ministral-3:8b && ollama pull embeddinggemma

# Start the server
uv run python main.py
```

Backend runs at `http://localhost:4224`

#### Frontend

```bash
cd frontend

# Install dependencies
pnpm install

# Start dev server
pnpm dev
```

Frontend runs at `http://localhost:3000`

---

## API Endpoints

### Documents
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/upload` | POST | Upload and process a file |
| `/concepts` | GET | List all concepts |
| `/concepts/{id}` | GET | Get concept details |
| `/search` | GET | Semantic search |

### Reviews
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/review/due` | GET | Get flashcards due for review |
| `/review/due/count` | GET | Count of due cards |
| `/review/submit` | POST | Submit review with rating (1-4) |
| `/review/grade` | POST | Grade answer using LLM |
| `/review/stats` | GET | Review statistics |

---

## Tech Stack

**Backend**: FastAPI, LangChain, SQLite + sqlite-vec, UMAP, HDBSCAN

**Frontend**: Nuxt 4, Vue 3, Honeycomb Grid, D3, Panzoom

**AI Models**:
- OpenAI: `gpt-4.1-mini` (VLM) + `text-embedding-3-small` (embeddings)
- Ollama: `ministral-3:8b` (VLM) + `embeddinggemma` (embeddings)

**Algorithm**: FSRS (Free Spaced Repetition Scheduler)

---

## License

MIT
