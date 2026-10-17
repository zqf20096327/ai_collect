# Multi-Scale Retrieval with RRF


This repository demonstrates a multi-scale retrieval approach for RAG (Retrieval-Augmented Generation) systems, showing that **chunk size is query-dependent** and that aggregating results across multiple chunk sizes improves retrieval robustness.

<p align="center">
  <img src="assets/multi-scale-retrieval-diagram.png" alt="Multi-Scale Retrieval with RRF Diagram" width="800">
</p>

## Overview

Instead of committing to a single chunk size, we:
1. Index the same corpus multiple times with different chunk sizes (100, 200, 500 tokens)
2. Query all indices in parallel at inference time
3. Aggregate results using **Reciprocal Rank Fusion (RRF)** to produce final document rankings

## Repository Structure

```
├── multi-window-chunk-size.ipynb   # Main notebook demonstrating the approach
├── seinfeld_trivia/
│   ├── data.json                   # Dataset with trivia questions and gold documents
│   └── documents_content/          # Markdown files for each Seinfeld episode
│       ├── S01E00.md
│       ├── S01E01.md
│       └── ...                     # 174 episode summaries
└── README.md
```

## Dataset

The `seinfeld_trivia/` directory contains:

- **`documents_content/`**: 174 markdown files, each containing a summary of a Seinfeld episode (e.g., `S05E14.md` for Season 5, Episode 14)
- **`data.json`**: A dataset of trivia questions with:
  - `query`: The trivia question
  - `targets`: The gold document(s) containing the answer
  - `answer`: The expected answer
 
  <p align="center">
  <img src="assets/seinfeld-meme.png" alt="Seinfeld RAG Benchmark Meme" width="400">
</p>

## Notebook

The `multi-window-chunk-size.ipynb` notebook demonstrates:

1. **Corpus Loading**: Reading markdown documents from the dataset
2. **Vector Store Creation**: Creating OpenAI vector stores with different chunk sizes
3. **Retrieval**: Querying each vector store and comparing results
4. **RRF Aggregation**: Combining rankings across chunk sizes

### Key Examples

The notebook includes three examples showing how different queries benefit from different chunk sizes:

| Example | Query | Best Chunk Size |
|---------|-------|-----------------|
| 1 | "What's the name for Jerry's favorite shirt?" | Small (100-200 tokens) |
| 2 | "What is Kramer's first name?" | Large (500 tokens) |
| 3 | "Where did George Costanza famously pull out a golf ball from?" | Medium (200 tokens) |

RRF aggregation consistently matches or exceeds the best individual chunk size performance.

## Requirements

```bash
pip install openai
export OPENAI_API_KEY=your_key_here
```

## Usage

1. Set your OpenAI API key as an environment variable
2. Open and run `multi-window-chunk-size.ipynb`
3. The notebook will create vector stores (or reuse existing ones) and demonstrate retrieval across different chunk sizes

## Key Takeaways

- **Chunk size is query-dependent**: Fine-grained factual queries benefit from smaller chunks; contextual queries benefit from larger chunks
- **No single size is optimal**: What works for one query may fail for another
- **RRF provides robustness**: By aggregating multiple rank signals, we typically match or exceed the best individual configuration
- **Simple implementation**: No retraining or query classification needed—just parallel retrieval and rank aggregation
