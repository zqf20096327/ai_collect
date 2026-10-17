# Auris

<p align="center">
  <img src="./documentation/icon.svg" alt="Auris" width="120" height="120" />
</p>

Domain-agnostic retrieval-augmented generation engine delivered as a TypeScript monorepo with an HTTP API.

Teams need retrieval, guardrails, and observability to stay coherent as vendors change; Auris isolates every external system behind ports and wires concrete adapters in one place. It answers questions by retrieving grounded chunks with dense plus sparse search, optional reranking, and an LLM over a packed context. Configuration lives in YAML and environment variables, pipelines emit tracing spans per step, and you can replace vector stores, sparse engines, or LLMs without rewriting core logic.

## Features

| Feature                                            | Status         |
| -------------------------------------------------- | -------------- |
| Hexagonal ports and adapters for external services | ✓              |
| Hybrid dense and sparse retrieval with RRF fusion  | ✓              |
| HyDE and multi-query expansion                     | ✓              |
| Cross-encoder reranking (Cohere)                   | ⚙ Configurable |
| Input and output guardrails                        | ✓              |
| Pluggable chunking strategies                      | ✓              |
| ChromaDB vector store client                       | ✓              |
| Elasticsearch or Typesense sparse search           | ✓              |
| Filesystem prompt templates                        | ✓              |
| Index fingerprinting and content-hash skips        | ✓              |
| REST API (`/v1/query`, `/v1/index`, `/v1/health`)  | ✓              |
| Golden-set assets for evaluation                   | ✓              |
| Docker Compose for Chroma and Elasticsearch        | ✓              |
| Extension-based local file ingestion               | ✓              |
| Scheduled incremental sync worker                  | 🔜 Planned     |
| Additional vector stores (Weaviate, pgvector)      | 🔜 Planned     |

## Stack

| Component       | Default / Alternatives                                                 |
| --------------- | ---------------------------------------------------------------------- |
| Runtime         | Node.js 20+                                                            |
| Package manager | pnpm 9.15.0                                                            |
| API             | Express                                                                |
| Language        | TypeScript 5.7                                                         |
| Embeddings      | OpenAI `text-embedding-3-large` (stub without API key)                 |
| Vector store    | ChromaDB HTTP client                                                   |
| Sparse search   | Elasticsearch 8.x, Typesense, or noop                                  |
| Fusion          | Reciprocal rank fusion (weighted merge in config)                      |
| Reranker        | Cohere rerank v3 or noop                                               |
| LLM             | OpenAI GPT-4o family (stubs for other enums)                           |
| Guardrails      | Composite heuristic provider                                           |
| Tracing         | Console spans with optional vendor tags (Langfuse, LangSmith, Phoenix) |
| Orchestration   | Custom Node pipelines                                                  |
| Configuration   | `config/default.yaml` merged with `AURIS_*` environment variables      |

## Quick start

1. `git clone https://github.com/ftonato/auris.git`
2. `cd auris`
3. `corepack enable && corepack prepare pnpm@9.15.0 --activate`
4. `pnpm install`
5. `pnpm docker:up`
6. `cp .env.example .env`
7. `${EDITOR:-vi} .env`
8. `pnpm data:seed`
9. `pnpm dev`
10. `curl -s -X POST http://127.0.0.1:3000/v1/query -H 'content-type: application/json' -d '{"query":"How to protect plants from cutworms?"}'`

```json
{
  "answer": "string",
  "citations": [{ "chunkId": "string", "score": 0, "source": "string" }],
  "confidence": 0,
  "traceId": "string",
  "pipeline": {
    "expansionUsed": true,
    "fusion": "rrf",
    "rerankerSkipped": false
  }
}
```

## How to run

### Prerequisites

- Node.js **>=20.0.0** (see root `package.json` `engines.node`)
- **pnpm 9.15.0** (see root `packageManager`)
- **Docker Engine 24+** with the Compose v2 plugin

### Development

1. `pnpm install`
2. `pnpm docker:up`
3. `cp .env.example .env`
4. `pnpm data:seed`
5. `pnpm dev`
6. `pnpm test`

Required `.env` keys are listed in [CONTRIBUTING.md](./CONTRIBUTING.md#running-locally).

### Scripts reference

| Script             | What it does                                    |
| ------------------ | ----------------------------------------------- |
| `pnpm dev`         | Start the HTTP API in watch mode                |
| `pnpm docker:up`   | Start local ChromaDB and Elasticsearch          |
| `pnpm data:seed`   | Build shared types and run the indexing worker  |
| `pnpm types:check` | Typecheck every workspace package               |
| `pnpm test`        | Run unit tests                                  |
| `pnpm lint`        | Run ESLint in all packages                      |
| `pnpm repo:setup`  | Install, start Compose, then `pnpm types:check` |

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full script catalog (formatting, coverage, evaluation, and Docker helpers).

## Links

→ [ARCHITECTURE.md](./ARCHITECTURE.md)  
→ [CONTRIBUTING.md](./CONTRIBUTING.md)  
→ [CHANGELOG.md](./CHANGELOG.md)

## License

This project is licensed under the [MIT License](LICENSE).
