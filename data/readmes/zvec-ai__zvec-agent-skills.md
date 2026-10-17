# Zvec Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/node.js-16+-green.svg)](https://nodejs.org/)
[![GitHub](https://img.shields.io/badge/GitHub-zvec--ai/agent--skills-black.svg)](https://github.com/zvec-ai/agent-skills)

Official AI Agent skills for building with Zvec vector database.

Zvec Assistant is an AI Agent Skill that provides developers with complete technical guidance for the [Zvec](https://zvec.org/) vector database. It supports Python and Node.js development environments, covering comprehensive documentation from basic concepts to advanced usage.

## What is Zvec?

Zvec is an open-source, high-performance, lightweight in-process vector database built on Alibaba's Proxima engine. No server or external infrastructure required, ready to use out of the box.

**Key Features:**
- ⚡ Sub-millisecond search latency, supporting billions of vectors
- 🧩 Single package installation, zero configuration, ready to use
- ✨ Supports dense vectors + sparse vectors, native multi-vector queries
- 🎯 Hybrid search: semantic similarity + structured filtering
- 📦 Pure in-process library, runs anywhere

## Use Cases

- **RAG Systems**: Document retrieval capabilities for LLM applications
- **Semantic Search**: Intelligent search based on vector similarity
- **Recommendation Systems**: Similar product/content recommendations
- **Multimodal Search**: Joint image + text search
- **Keyword + Semantic Hybrid Search**: BM25 + vector embeddings

## Installation

### Install as AI Agent Skill


```bash
npx skills add github:zvec-ai/zvec-agent-skills --skill "zvec"
```


### Install Zvec Package

Choose installation based on your development language:

**Python:**
```bash
pip install zvec
```

**Node.js:**
```bash
npm install @zvec/zvec
```

## Quick Start

### Python

```python
import zvec

# Create Collection
schema = zvec.CollectionSchema(
    name="my_collection",
    fields=[
        zvec.FieldSchema(name="title", data_type=zvec.DataType.STRING),
    ],
    vectors=[
        zvec.VectorSchema(
            name="embedding",
            data_type=zvec.DataType.VECTOR_FP32,
            dimension=768,
            index_param=zvec.HnswIndexParam(
                metric_type=zvec.MetricType.COSINE
            ),
        ),
    ],
)

collection = zvec.create_and_open("./my_data", schema)

# Insert document
collection.upsert(zvec.Doc(
    id="doc_1",
    vectors={"embedding": [0.1] * 768},
    fields={"title": "Hello World"},
))

# Search
results = collection.query(
    vectors=zvec.VectorQuery(
        field_name="embedding",
        vector=[0.1] * 768,
    ),
    topk=10,
)
```

### Node.js

```typescript
import { ZVecCreateAndOpen, ZVecCollectionSchema, ZVecFieldSchema, ZVecVectorSchema, ZVecDataType, ZVecHnswIndexParams, ZVecMetricType } from "@zvec/zvec";

const schema = new ZVecCollectionSchema({
  name: "my_collection",
  fields: [new ZVecFieldSchema({ name: "title", dataType: ZVecDataType.STRING })],
  vectors: [new ZVecVectorSchema({
    name: "embedding",
    dataType: ZVecDataType.VECTOR_FP32,
    dimension: 768,
    indexParams: new ZVecHnswIndexParams({ metricType: ZVecMetricType.COSINE }),
  })],
});

const collection = ZVecCreateAndOpen("./my_data", schema);
```

## Project Structure

```
zvec-agent-skills/
├── skills/                       # Built skill output directory
│   └── zvec/
│       ├── SKILL.md              # Skill main document
│       ├── quick-start/          # Quick start
│       │   ├── python.md
│       │   └── typescript.md
│       ├── collection-management/# Collection management
│       ├── data-operations/      # Data operations
│       ├── vector-search/        # Vector search
│       ├── rag-system/           # RAG system
│       ├── hybrid-search/        # Hybrid search
│       ├── multimodal-search/    # Multimodal search
│       ├── data-model.md         # Data model
│       ├── api-cheatsheet.md     # API cheatsheet
│       └── troubleshooting.md    # Troubleshooting
├── src/                          # Source code directory
│   └── zvec/
│       ├── SKILL.md              # Skill main document source
│       ├── templates/            # Markdown templates
│       ├── code/                 # Code examples
│       │   ├── python/
│       │   └── typescript/
│       └── general/              # General documents
├── scripts/                      # Build scripts
│   └── build-skills.ts           # Skill build script
├── package.json                  # Project configuration
├── CLAUDE.md                     # Developer guide
└── README.md                     # Project readme
```

## Build

This project uses a build system to convert source code into distributable skills.

```bash
# Install dependencies
bun install

# Build skills
bun run build
```

The built output is located in the `skills/zvec/` directory.

## Usage Scenarios

### RAG Document Retrieval
Build intelligent document retrieval systems for LLM applications:

```
I want to build a RAG system with Python and Zvec for technical support knowledge base.
Documents are in Markdown format and need semantic search support.
```

### E-commerce Product Search
Implement semantic product search with filtering capabilities:

```
I need to implement e-commerce product search in a Node.js project:
- Support semantic search by product name and description
- Filter by price, category, and brand
- Support multimodal (image + text) search
```

### Log Troubleshooting Knowledge Base
Store and search system log failure cases:

```
I want to use Zvec to store system log failure cases and support semantic search for similar issues.
Using Python with about 100k data entries.
```

## Available Topics

### Python

- [Quick Start](./skills/zvec/quick-start/python.md) - Quick start with Zvec Python API
- [Collection Management](./skills/zvec/collection-management/python.md) - Create, open, and manage Collections
- [Data Operations](./skills/zvec/data-operations/python.md) - Insert, update, and delete documents
- [Vector Search](./skills/zvec/vector-search/python.md) - Single-vector, multi-vector, and hybrid search
- [RAG System](./skills/zvec/rag-system/python.md) - Build document retrieval system
- [Hybrid Search](./skills/zvec/hybrid-search/python.md) - Vector similarity + scalar filtering
- [Multimodal Search](./skills/zvec/multimodal-search/python.md) - Image + text joint search

### Node.js

- [Quick Start](./skills/zvec/quick-start/typescript.md) - Quick start with Zvec Node.js API
- [Collection Management](./skills/zvec/collection-management/typescript.md) - Create, open, and manage Collections
- [Data Operations](./skills/zvec/data-operations/typescript.md) - Insert, update, and delete documents
- [Vector Search](./skills/zvec/vector-search/typescript.md) - Single-vector, multi-vector, and hybrid search
- [RAG System](./skills/zvec/rag-system/typescript.md) - Build document retrieval system
- [Hybrid Search](./skills/zvec/hybrid-search/typescript.md) - Vector similarity + scalar filtering
- [Multimodal Search](./skills/zvec/multimodal-search/typescript.md) - Image + text joint search

### General

- [Data Model](./skills/zvec/data-model.md) - Zvec data model overview
- [API Cheatsheet](./skills/zvec/api-cheatsheet.md) - Python & Node.js API quick reference
- [Troubleshooting](./skills/zvec/troubleshooting.md) - Common issues and solutions

## Usage Examples

### Hybrid Search (Vector + Filter)

```python
# Search similar products while filtering by price and stock
results = collection.query(
    vectors=zvec.VectorQuery(
        field_name="description_vec",
        vector=query_vector,
    ),
    filter="price >= 100 AND price <= 500 AND in_stock == true",
    topk=10,
)
```

### Multi-Vector Search

```python
# Search using both image and text vectors
results = collection.query(
    vectors=[
        zvec.VectorQuery(field_name="image_vec", vector=image_query),
        zvec.VectorQuery(field_name="text_vec", vector=text_query),
    ],
    reranker=zvec.WeightedReRanker(
        topn=10,
        metric=zvec.MetricType.COSINE,
        weights={"image_vec": 0.7, "text_vec": 0.3},
    ),
)
```

## Best Practices

For detailed usage guidelines in Claude Code and Claude Desktop, see [CLAUDE.md](./CLAUDE.md).

### Quick Tips

- **Specify your development language** when asking questions (Python or Node.js)
- **Describe your use case** for more targeted recommendations
- **Ask for architectural advice** when designing your schema and indexing strategy

## Contributing

Contributions are welcome! Please check [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to participate.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Related Links

- [GitHub Repository](https://github.com/zvec-ai/agent-skills)
- [Zvec Official Documentation](https://zvec.org/en/docs/)
- [Zvec Python API](https://zvec.org/api-reference/python/)
- [Zvec Node.js API](https://zvec.org/api-reference/nodejs/)
- [Zvec GitHub](https://github.com/alibaba/zvec)
