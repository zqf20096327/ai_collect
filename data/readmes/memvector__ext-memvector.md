# MemVector: Local Vector API, Storage & Embedding Engine for PHP

A high-performance PHP extension that brings local AI infrastructure and AI API to PHP developers and optimized for AI workload. Vector similarity search, text embedding, and cross-encoder reranking — all running directly in your PHP process. Built in C++17 with AVX2 SIMD acceleration. No external vector database, no embedding API, no network round-trips. Embed, store, search, and rerank in under 10 ms.

Works best with **small, specialized local GGUF models** (embedding + reranker, 24-636 MB) that run efficiently on CPU, and with **long-lived PHP runtimes** ([OpenSwoole](https://openswoole.com), [ReactPHP](https://reactphp.org), [RoadRunner](https://roadrunner.dev), [FrankenPHP](https://frankenphp.dev)) where persistent workers keep models loaded in memory across requests — giving you single-digit millisecond latency for the entire embed → search → rerank pipeline with zero external dependencies.

## Quick Start

```php
// Semantic search with local embeddings (requires --with-llama)
$emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf');
$store = new MemVectorStore(null, ['dimensions' => $emb->dimensions()]);

$store->set('php',     $emb->embed('PHP is a server-side scripting language'),     'lang');
$store->set('python',  $emb->embed('Python is used for machine learning'),         'lang');
$store->set('gravity', $emb->embed('Gravity pulls objects toward the earth'),      'science');
$store->set('dna',     $emb->embed('DNA encodes genetic information'),             'science');

$results = $store->search($emb->embed('programming languages'), 2);
// [['key' => 'php', 'score' => 0.82, 'metadata' => 'lang'],
//  ['key' => 'python', 'score' => 0.79, 'metadata' => 'lang']]
```

```php
// Two-stage retrieval: vector search + cross-encoder rerank (requires --with-llama)
$rr = new MemVectorReranker('/models/bge-reranker-v2-m3-Q8_0.gguf');
$candidates = $store->search($emb->embed('programming languages'), 50);
$results = $rr->rerank('programming languages', $candidates, 5);
```

```php
// Or bring your own vectors (no llama.cpp needed)
$store = new MemVectorStore('/data/vectors', ['dimensions' => 1536]);
$store->set('doc_1', $openai_embedding, '{"title": "Introduction"}');
$results = $store->search($query_embedding, 10);
```

## Features

- **Key-value API** — `set(key, vector)`, `get(key)`, `delete(key)`, `batchSet()` with upsert semantics
- **Text embeddings** — optional [llama.cpp](https://github.com/ggerganov/llama.cpp) integration for local GGUF model inference
- **Cross-encoder reranking** — two-stage retrieval: fast vector search → accurate cross-encoder rerank
- **Three storage modes** — memory, disk (mmap), shared memory (cross-process)
- **HNSW index** — auto-builds transparently during search for fast approximate nearest neighbor
- **Vector quantization** — F16, Int8 (scalar), binary, and product quantization (PQ)
- **Four distance metrics** — cosine, dot product, euclidean, manhattan
- **Lock-free concurrency** — reads/writes via `std::atomic`
- **AVX2 SIMD** — accelerated cosine/dot distance computation
- **Multi-segment architecture** — auto-grows with fixed-capacity segments
- **JSONL import/export** — `dump()` and `load()` for backup, migration, and interop
- **Memory limits** — cap total mmap usage across segments

## Performance

MemVector runs entirely in-process — no network calls, no serialization, no external services. This eliminates the latency and cost of external APIs and vector databases.

### Embedding generation

| Approach | Latency per call | Cost |
|----------|-----------------|------|
| OpenAI API (`text-embedding-3-small`) | 50-200 ms (network round-trip) | $0.02 / 1M tokens |
| Cohere API (`embed-english-v3.0`) | 50-200 ms (network round-trip) | $0.10 / 1M tokens |
| **MemVector + local GGUF model** | **5-15 ms** (in-process) | **Free** |

Local embedding with MemVector is 10-40x faster than API calls and has zero per-token cost. The model runs inside the PHP process via llama.cpp — no HTTP overhead, no API keys, no rate limits.

### Vector search

| Approach | Latency per query | Notes |
|----------|------------------|-------|
| Pinecone / Qdrant / Weaviate (cloud) | 10-50 ms (network) | Managed service, per-vector pricing |
| Pinecone / Qdrant / Weaviate (self-hosted) | 5-20 ms (network) | Separate process, TCP/gRPC overhead |
| PostgreSQL + pgvector | 5-50 ms (query + network) | Shared DB, connection pooling overhead |
| **MemVector (in-process)** | **0.1-5 ms** | **No network, no serialization** |

MemVector searches vectors directly in the PHP process memory (or mmap'd files). There is no serialization, no socket, no protocol parsing. HNSW index + AVX2 SIMD keeps search under 1 ms for most workloads up to millions of vectors.

### Full RAG pipeline (embed + search + rerank)

| Approach | Total latency | Components |
|----------|--------------|------------|
| OpenAI embed + Pinecone search | 100-400 ms | 2 network round-trips |
| OpenAI embed + Pinecone search + Cohere rerank | 200-600 ms | 3 network round-trips |
| **MemVector (all in-process)** | **10-30 ms** | **0 network round-trips** |

A complete two-stage retrieval pipeline (embed query → vector search → cross-encoder rerank) runs in a single PHP process with no external dependencies.

### Memory footprint

| Component | RSS |
|-----------|-----|
| MemVector extension (no model) | ~1 MB |
| + embedding model (all-MiniLM-L6-v2, 24 MB GGUF) | ~33 MB |
| + reranker model (bge-reranker-v2-m3, 636 MB GGUF) | ~200 MB |
| + 100K vectors (384 dim, f32) | ~150 MB |
| + 100K vectors (384 dim, int8 quantized) | ~40 MB |

Model weights are `mmap()`'d and shared across php-fpm/OpenSwoole workers by the OS page cache.

### Why small models + OpenSwoole

MemVector is designed for **small, task-specific models** — not large generative LLMs. Embedding models (24-138 MB) and reranker models (366-636 MB) are compact enough to run on CPU with low latency and fit comfortably in server memory. These models do one thing well: convert text to vectors or score relevance — tasks where small specialized models match or exceed large API-hosted models in quality.

Combined with **OpenSwoole**, where each worker process loads the model once and reuses it across thousands of requests, you get a fully self-contained semantic search stack:

- **No API costs** — models run locally, no per-token billing
- **No network latency** — embed, search, and rerank happen in-process
- **No external services** — no vector database, no embedding API, no reranker API to deploy and maintain
- **Predictable performance** — no cold starts, no rate limits, no variance from shared infrastructure

A single OpenSwoole worker with a 24 MB embedding model + MemVector store handles embed + search in under 10 ms per request using ~50 MB of RAM.

## Requirements

- PHP 8.1+
- C++17 compiler (GCC 7+ or Clang 5+)
- Optional: [llama.cpp](https://github.com/ggerganov/llama.cpp) for text embeddings and cross-encoder reranking

## Install via PIE

[PIE](https://github.com/php/pie) is the official PHP installer for extensions.

```bash
pie install memvector/ext-memvector
```

To enable llama.cpp support (embeddings & reranking):

```bash
pie install memvector/ext-memvector --with-llama=/usr/local
```

## Build from Source

```bash
phpize
./configure --enable-memvector
make
make test
```

### Install llama.cpp (optional, for embeddings & reranking)

**macOS (Homebrew):**

```bash
brew install llama.cpp
```

**Linux (build from source):**

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
cmake -B build -DBUILD_SHARED_LIBS=ON -DGGML_CUDA=OFF
cmake --build build --config Release -j$(nproc)
sudo cmake --install build --prefix /usr/local
sudo ldconfig  # refresh shared library cache
```

For GPU acceleration, replace `-DGGML_CUDA=OFF` with `-DGGML_CUDA=ON` (requires CUDA toolkit).

### Build with llama.cpp support (embeddings & reranking)

```bash
phpize
./configure --enable-memvector --with-llama=/usr/local
make
make test
```

Pass `--with-llama=DIR` if llama.cpp is installed in a non-standard location.

### Download models

**Embedding models** — any GGUF embedding model works. Recommended starter (24 MB, 384 dimensions):

```bash
curl -L -o all-MiniLM-L6-v2-Q8_0.gguf \
  https://huggingface.co/leliuga/all-MiniLM-L6-v2-GGUF/resolve/main/all-MiniLM-L6-v2.Q8_0.gguf
```

| Model | Dimensions | Size | Download |
|-------|-----------|------|----------|
| all-MiniLM-L6-v2 (Q8) | 384 | 24 MB | [HuggingFace](https://huggingface.co/leliuga/all-MiniLM-L6-v2-GGUF) |
| nomic-embed-text-v1.5 (Q8) | 768 | 138 MB | [HuggingFace](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF) |
| bge-small-en-v1.5 (F16) | 384 | 67 MB | [HuggingFace](https://huggingface.co/CompendiumLabs/bge-small-en-v1.5-gguf) |

**Reranker models** — GGUF cross-encoder models for two-stage retrieval:

```bash
curl -L -o bge-reranker-v2-m3-Q8_0.gguf \
  https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF/resolve/main/bge-reranker-v2-m3-Q8_0.gguf
```

| Model | Size | Download |
|-------|------|----------|
| bge-reranker-v2-m3 (Q8) | 636 MB | [HuggingFace](https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF) |
| bge-reranker-v2-m3 (Q2) | 366 MB | [HuggingFace](https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF) |

### Configure options

| Flag | Description |
|------|-------------|
| `--enable-memvector` | Enable the extension (required) |
| `--enable-memvector-avx2` | AVX2 SIMD (`auto` by default, auto-detected) |
| `--with-llama[=DIR]` | Enable llama.cpp support (embeddings & reranking) |

## Feature Detection

Optional features can be detected at runtime via constants:

```php
if (defined('MEMVECTOR_SHM')) {
    // Shared memory mode available
    $store = new MemVectorStore('mystore', ['storage' => 'shm', 'dimensions' => 128]);
}

if (defined('MEMVECTOR_LLAMA')) {
    // llama.cpp support compiled in (embeddings & reranking)
    $emb = new MemVectorEmbedding('/path/to/embedding-model.gguf');
    $rr  = new MemVectorReranker('/path/to/reranker-model.gguf');
}
```

## PHP API

### Class: `MemVectorStore`

#### `__construct(?string $dir = null, ?array $options = null)`

Create or open a vector store.

```php
// Memory mode (ephemeral, single-process)
$store = new MemVectorStore();
$store = new MemVectorStore(null, ['dimensions' => 128]);

// Disk mode (persistent, file-backed mmap)
$store = new MemVectorStore('/path/to/dir', ['dimensions' => 128]);

// Shared memory mode (persistent, cross-process)
$store = new MemVectorStore('mystore', ['storage' => 'shm', 'dimensions' => 128]);
```

**Options** (all string values are case-insensitive):

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `storage` | string | auto | `'disk'`, `'memory'`, or `'shm'` |
| `dimensions` | int | 1536 | Vector dimensionality (1-4096) |
| `distance` | string | `'cosine'` | `'cosine'`, `'dot'`, `'euclidean'`, `'manhattan'` |
| `quantization` | string | `'none'` | `'none'`, `'f16'`, `'int8'`, `'binary'`, `'pq'` |
| `segment_size` | int | 10M (disk/shm), 4096 (memory) | Max records per segment |
| `writable` | bool | true | Open in read-only mode (shm mode) |
| `memory_limit` | int\|string | 0 | Max total mmap bytes (`'1G'`, `'512M'`, `'128K'`). 0 = unlimited |

---

#### `set(string $key, array $vector, ?string $metadata = null): bool`

Insert or replace a vector by key (upsert semantics).

```php
$store->set('doc_42', $vector);
$store->set('doc_42', $new_vector, '{"category": "science"}'); // replaces previous
```

- `$key` — Unique string key (max 63 chars)
- `$vector` — Float array matching the store's `dimensions`
- `$metadata` — Optional metadata string (max 4096 bytes)

---

#### `batchSet(array $batch): int`

Insert or replace multiple vectors in one call. Returns the count of items inserted.

```php
$count = $store->batchSet([
    ['key' => 'doc_1', 'vector' => $vec1],
    ['key' => 'doc_2', 'vector' => $vec2, 'metadata' => '{"tag": "a"}'],
]);
```

---

#### `search(array $vector, int $topK = 10, float $precision = 50): array`

Search for the nearest neighbors of a query vector.

```php
$results = $store->search($query_vector, 5);
$results = $store->search($query_vector, 5, 100); // higher precision
$results = $store->search($query_vector, 5, 0);   // force brute-force
```

- `$topK` — Number of results (max 1000)
- `$precision` — HNSW beam width. Higher = better recall, slower. `0` = brute-force.

The HNSW index auto-builds when `precision > 0` and vector count reaches `auto_index_threshold`.

Returns results sorted by score (highest first):

```php
[
    ['key' => 'doc_42', 'score' => 0.95, 'metadata' => '{"category": "science"}'],
    ['key' => 'doc_7',  'score' => 0.89, 'metadata' => null],
]
```

Score meaning by distance metric:
- **Cosine**: similarity (0 to 1, higher = more similar)
- **Dot**: raw dot product (higher = more similar)
- **Euclidean/Manhattan**: negated distance (higher = closer)

---

#### `get(string $key): ?array`

Retrieve a record by key. Returns `null` if not found.

```php
$record = $store->get('doc_42');
// ['key' => 'doc_42', 'vector' => [0.1, ...], 'metadata' => '...']
```

---

#### `delete(string $key): bool`

Soft-delete a record by key. Returns `true` if found and deleted.

---

#### `count(): int`

Return the total number of live records.

---

#### `stats(): array`

Return store statistics.

| Key | Type | Description |
|-----|------|-------------|
| `storage` | string | `"memory"`, `"disk"`, or `"shm"` |
| `total_count` | int | Total records across all segments |
| `segment_count` | int | Number of segments |
| `dimensions` | int | Vector dimensionality |
| `distance` | string | `"cosine"`, `"dot"`, `"euclidean"`, or `"manhattan"` |
| `quantization` | string | `"none"`, `"f16"`, `"int8"`, `"binary"`, or `"pq"` |
| `bytes_per_vector` | int | Storage bytes per vector |
| `index_status` | string | `"none"` or `"ready"` |
| `unindexed_count` | int | Records not yet in the HNSW index |
| `memory_mb` | float | Total memory/mmap usage in MB |

---

#### `dump(?string $path = null): string|int`

Export all records as JSONL. Each line: `{"key":"...","vector":[...],"metadata":"..."}`

```php
$jsonl = $store->dump();                        // returns string
$count = $store->dump('/backup/vectors.jsonl');  // streams to file, returns count
```

---

#### `load(string $path): int`

Import records from a JSONL file (inverse of `dump()`). Returns the number of records loaded. Uses upsert semantics.

```php
$count = $store->load('/backup/vectors.jsonl');
```

---

#### `clear(): bool`

Remove all records. Memory and shm modes only.

---

#### `snapshot(string $dir): bool`

Persist a memory or shm store to disk. Can be reloaded with `'storage' => 'memory'`:

```php
$store->snapshot('/data/snapshot');
// Later:
$store = new MemVectorStore('/data/snapshot', ['storage' => 'memory', 'dimensions' => 128]);
```

---

#### `close(): void`

Close the store and release resources. Called automatically on GC. Safe to call multiple times.

---

#### `static destroy(string $name): bool`

Unlink a shared memory store. Requires `MEMVECTOR_SHM`.

---

### Class: `MemVectorEmbedding`

Requires `--with-llama` at build time. Detect with `defined('MEMVECTOR_LLAMA')`.

#### `__construct(string $model_path, ?array $options = null)`

Load a GGUF embedding model.

```php
$emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf', [
    'context_size' => 512,
    'gpu_layers'   => 0,
    'normalize'    => true,
]);
```

**Options:**

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `context_size` | int | 512 | Max tokens per text input |
| `gpu_layers` | int | 0 | Number of layers to offload to GPU |
| `normalize` | bool | true | L2 normalize output vectors |

Throws `MemVectorException` if the model file cannot be loaded.

---

#### `embed(string $text): array`

Generate an embedding vector for a single text. Returns `float[]` of size `dimensions()`.

```php
$vector = $emb->embed("The quick brown fox");
```

---

#### `embedBatch(array $texts): array`

Generate embeddings for multiple texts. Returns `float[][]`.

```php
$vectors = $emb->embedBatch(["Hello", "World", "Test"]);
// count($vectors) === 3, count($vectors[0]) === $emb->dimensions()
```

---

#### `dimensions(): int`

Return the model's embedding dimensionality.

---

#### `close(): void`

Free the model and context. Called automatically on GC. Safe to call multiple times.

---

### Class: `MemVectorReranker`

Cross-encoder reranker for two-stage retrieval. Requires `--with-llama` at build time. Detect with `defined('MEMVECTOR_LLAMA')`.

#### `__construct(string $model_path, ?array $options = null)`

Load a GGUF cross-encoder reranker model.

```php
$rr = new MemVectorReranker('/models/bge-reranker-v2-m3-Q8_0.gguf', [
    'context_size' => 512,
    'gpu_layers'   => 0,
]);
```

**Options:**

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `context_size` | int | 512 | Max tokens per query+document pair |
| `gpu_layers` | int | 0 | Number of layers to offload to GPU |

Throws `MemVectorException` if the model file cannot be loaded.

**Recommended model:** [bge-reranker-v2-m3](https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF) (Q8_0 ~1 GB)

---

#### `score(string $query, array $texts): array`

Score each text against the query using the cross-encoder. Returns `[['index' => int, 'score' => float], ...]` sorted descending by score.

```php
$scores = $rr->score("What is PHP?", [
    "PHP is a scripting language.",
    "The weather is sunny.",
]);
// → [['index' => 0, 'score' => 0.87], ['index' => 1, 'score' => -3.2]]
```

---

#### `rerank(string $query, array $candidates, int $topK = 0): array`

Rerank search results from `MemVectorStore::search()`. Scores each candidate's `metadata` field against the query. Returns `[['key' => string, 'score' => float, 'metadata' => string], ...]` sorted descending. `$topK = 0` returns all candidates.

```php
$candidates = $store->search($emb->embed($query), 50);
$reranked = $rr->rerank($query, $candidates, 5);
```

---

#### `close(): void`

Free the model and context. Called automatically on GC. Safe to call multiple times.

---

#### Two-Stage Retrieval Example

```php
$emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf');
$rr  = new MemVectorReranker('/models/bge-reranker-v2-m3-Q8_0.gguf');
$store = new MemVectorStore(null, ['dimensions' => $emb->dimensions()]);

// Index documents
foreach ($docs as $key => $text) {
    $store->set($key, $emb->embed($text), $text);
}

// Stage 1: Fast vector search (broad recall)
$candidates = $store->search($emb->embed($query), 50, 0);

// Stage 2: Accurate cross-encoder rerank (high precision)
$results = $rr->rerank($query, $candidates, 5);
```

---

### Exception Class: `MemVectorException`

All errors throw `MemVectorException` (extends `\Exception`).

```php
try {
    $store->set('x', [0.1]); // wrong dimension
} catch (MemVectorException $e) {
    echo $e->getMessage(); // "Vector dim mismatch: expected 128"
}
```

---

### INI Settings

| Directive | Default | Description |
|-----------|---------|-------------|
| `memvector.default_dir` | `/tmp/memvector` | Default directory for disk stores |
| `memvector.default_dim` | 1536 | Default vector dimension |
| `memvector.default_storage` | 0 | Default storage mode |
| `memvector.mem_initial_capacity` | 4096 | Initial memory-mode capacity |
| `memvector.hnsw_max_connections` | 16 | HNSW max connections per node |
| `memvector.hnsw_construction_ef` | 200 | HNSW build beam width |
| `memvector.hnsw_ef_search` | 50 | HNSW search beam width |
| `memvector.auto_index_threshold` | 100 | Min vectors before HNSW auto-builds (0 = disable) |
| `memvector.pq_subvectors` | 0 | PQ sub-vector count (required for `quantization = 'pq'`) |
| `memvector.pq_training_size` | 256 | Vectors to buffer before PQ codebook auto-trains |
| `memvector.use_avx2` | 1 | Enable AVX2 SIMD (if compiled with support) |
| `memvector.model_cache` | 1 | Cache llama.cpp models per-process (PHP_INI_SYSTEM). Requires `--with-llama` |

---

## Usage Examples

### Semantic Search with Embeddings

```php
$emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf');
$store = new MemVectorStore(null, ['dimensions' => $emb->dimensions()]);

// Index a knowledge base
$articles = [
    'relativity'  => 'Einstein published the theory of general relativity in 1915',
    'evolution'   => 'Darwin proposed natural selection as the mechanism of evolution',
    'computing'   => 'Turing described a theoretical machine that could compute anything',
    'genetics'    => 'Watson and Crick discovered the double helix structure of DNA',
    'quantum'     => 'Heisenberg formulated the uncertainty principle in quantum mechanics',
];

foreach ($articles as $key => $text) {
    $store->set($key, $emb->embed($text), json_encode(['text' => $text]));
}

// Semantic search — finds related articles, not just keyword matches
$results = $store->search($emb->embed('biology and heredity'), 3);
foreach ($results as $r) {
    $meta = json_decode($r['metadata'], true);
    printf("  [%.2f] %s: %s\n", $r['score'], $r['key'], $meta['text']);
}
// Output:
//   [0.67] genetics: Watson and Crick discovered the double helix...
//   [0.51] evolution: Darwin proposed natural selection...
//   [0.24] quantum: Heisenberg formulated the uncertainty...
```

### RAG Pipeline (Retrieval-Augmented Generation)

```php
// 1. Build index from documents
$emb = new MemVectorEmbedding('/models/nomic-embed-text-v1.5.Q8_0.gguf');
$store = new MemVectorStore('/data/knowledge', ['dimensions' => $emb->dimensions()]);

foreach ($documents as $doc) {
    // Chunk long documents and index each chunk
    foreach (chunk_text($doc->content, 512) as $i => $chunk) {
        $store->set("{$doc->id}_chunk_{$i}", $emb->embed($chunk), json_encode([
            'doc_id' => $doc->id,
            'title'  => $doc->title,
            'chunk'  => $chunk,
        ]));
    }
}

// 2. Retrieve relevant context for a user query
$query = "How does photosynthesis work?";
$results = $store->search($emb->embed($query), 5, 100);

$context = implode("\n\n", array_map(function ($r) {
    return json_decode($r['metadata'], true)['chunk'];
}, $results));

// 3. Send to LLM with retrieved context
$prompt = "Context:\n{$context}\n\nQuestion: {$query}\nAnswer:";
// $answer = $llm->complete($prompt);
```

### Two-Stage Retrieval with Reranking

```php
$emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf');
$rr  = new MemVectorReranker('/models/bge-reranker-v2-m3-Q8_0.gguf');
$store = new MemVectorStore(null, ['dimensions' => $emb->dimensions()]);

// Index documents (store text as metadata for reranking)
$docs = [
    'php-web'     => 'PHP is widely used for building dynamic web applications and APIs.',
    'python-ml'   => 'Python is the dominant language for machine learning and data science.',
    'php-history' => 'PHP was originally created by Rasmus Lerdorf in 1994.',
    'weather'     => 'The weather forecast predicts rain for the upcoming weekend.',
];

foreach ($docs as $key => $text) {
    $store->set($key, $emb->embed($text), $text);
}

// Stage 1: Fast vector search — broad recall (top 50)
$query = "Tell me about PHP";
$candidates = $store->search($emb->embed($query), 50, 0);

// Stage 2: Cross-encoder rerank — high precision (top 3)
$results = $rr->rerank($query, $candidates, 3);

foreach ($results as $r) {
    printf("  [%.4f] %s: %s\n", $r['score'], $r['key'], $r['metadata']);
}
// PHP-related documents rank at the top, weather at the bottom
```

### Persistent Disk Store with HNSW

```php
$store = new MemVectorStore('/var/data/vectors', [
    'dimensions'   => 768,
    'distance'     => 'cosine',
    'segment_size' => 100000,
]);

// Index vectors — HNSW auto-builds on first search
foreach ($documents as $doc) {
    $store->set($doc->id, $doc->embedding, json_encode($doc->metadata));
}

// Fast approximate search
$results = $store->search($query, 10, 100);
$store->close();

// Data and index persist — reopen anytime
$store = new MemVectorStore('/var/data/vectors', ['dimensions' => 768]);
$results = $store->search($query, 10, 100);
```

### Quantized Store (F16 — half memory)

```php
$store = new MemVectorStore(null, [
    'dimensions'   => 768,
    'quantization' => 'f16',  // 2 bytes/dim instead of 4
]);

$store->set('doc_1', $embedding);
$results = $store->search($query, 10);
```

### Product Quantization (PQ — extreme compression)

```php
ini_set('memvector.pq_subvectors', 96);      // 96 sub-vectors of 8 dims each
ini_set('memvector.pq_training_size', 1000); // auto-train after 1000 vectors

$store = new MemVectorStore(null, [
    'dimensions'   => 768,
    'quantization' => 'pq',
]);

// First 1000 vectors are buffered for codebook training
for ($i = 0; $i < 5000; $i++) {
    $store->set("vec_$i", $embeddings[$i]);
}
// After training: 96 bytes/vector instead of 3072 (32x compression)
```

### JSONL Backup & Restore

```php
$store = new MemVectorStore('/data/vectors', ['dimensions' => 768]);

// Export
$count = $store->dump('/backup/vectors.jsonl');
echo "Exported $count records\n";

// Import into a new store
$newStore = new MemVectorStore('/data/vectors_v2', ['dimensions' => 768]);
$loaded = $newStore->load('/backup/vectors.jsonl');
echo "Imported $loaded records\n";
```

### Snapshot & Reload in Memory Mode

```php
$store = new MemVectorStore(null, ['dimensions' => 128]);
// ... add vectors ...

$store->snapshot('/data/snapshot');
$store->close();

// Reload entirely in memory (fast startup, no disk I/O after load)
$store = new MemVectorStore('/data/snapshot', ['storage' => 'memory', 'dimensions' => 128]);
```

### Shared Memory with OpenSwoole Workers

```php
// Master: create and populate
$store = new MemVectorStore('search_index', [
    'storage'    => 'shm',
    'dimensions' => 1536,
]);
foreach ($documents as $doc) {
    $store->set($doc->id, $doc->embedding, $doc->title);
}
$store->close();

// Workers: attach read-only (zero-copy, cross-process)
$store = new MemVectorStore('search_index', [
    'storage'    => 'shm',
    'dimensions' => 1536,
    'writable'   => false,
]);
$results = $store->search($query_vector, 10, 100);
$store->close();

// Cleanup
MemVectorStore::destroy('search_index');
```

### Memory-Limited Store

```php
$store = new MemVectorStore(null, [
    'dimensions'   => 128,
    'segment_size' => 10000,
    'memory_limit' => '256M',
]);
// Throws MemVectorException when adding would exceed the limit
```

---

### Model Cache (php-fpm)

When `memvector.model_cache=1` (default), `MemVectorEmbedding` and `MemVectorReranker` cache loaded GGUF models per worker process. The first construction loads the model from disk; subsequent constructions with the same file path reuse the cached model and only create a lightweight context. This avoids re-parsing weights on every request. Disable with `memvector.model_cache=0` in `php.ini` (PHP_INI_SYSTEM — cannot be changed at runtime).

**Latency impact** — construction time per request:

| Model | Size | Without cache | With cache | Speedup |
|-------|------|---------------|------------|---------|
| all-MiniLM-L6-v2 (Q8) | 24 MB | ~60 ms | ~1.5 ms | ~40x |
| nomic-embed-text-v1.5 (Q8) | 138 MB | ~300 ms | ~1.5 ms | ~200x |
| bge-reranker-v2-m3 (Q8) | 636 MB | ~1500 ms | ~1.5 ms | ~1000x |

Embed/score inference time is the same with or without the cache (~5-15 ms per call depending on model and text length).

**Memory impact** — per worker process:

| Model | Size | Cache RSS per worker | Context per request |
|-------|------|----------------------|---------------------|
| all-MiniLM-L6-v2 (Q8) | 24 MB | ~22 MB | ~1 MB |
| nomic-embed-text-v1.5 (Q8) | 138 MB | ~60 MB | ~2 MB |
| bge-reranker-v2-m3 (Q8) | 636 MB | ~200 MB | ~5 MB |

Model weights are loaded via `mmap()`, so the OS shares physical pages across all workers through the page cache. The per-worker private cost is mainly model metadata (vocab, tensor descriptors). For example, 10 php-fpm workers with a 24 MB model use ~24 MB shared + 10 x 8 MB private = ~104 MB total physical RAM, not 10 x 48 MB.

### Long-Lived PHP Runtimes

The model cache is designed for php-fpm's per-request lifecycle. For long-lived PHP runtimes — where worker processes persist across requests — the cache is unnecessary. Load the model once at startup and reuse the same object across all requests. This avoids both model loading **and** context creation overhead, giving the best possible performance.

This applies to any long-lived PHP framework or library:

- **[OpenSwoole](https://openswoole.com)** — async event-driven server
- **[ReactPHP](https://reactphp.org)** — event loop for non-blocking I/O
- **[AMPHP](https://amphp.org)** — async PHP framework
- **[Workerman](https://www.workerman.net)** — high-performance PHP socket server
- **[RoadRunner](https://roadrunner.dev)** — Go-powered PHP application server
- **[FrankenPHP](https://frankenphp.dev)** — modern PHP app server (worker mode)
- Any long-running CLI script or daemon

**OpenSwoole example:**

```php
$server->on('workerStart', function ($server, $workerId) {
    $server->emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf');
    $server->store = new MemVectorStore('/data/vectors', [
        'dimensions' => $server->emb->dimensions(),
    ]);
});
$server->on('request', function ($request, $response) use ($server) {
    $vec = $server->emb->embed($request->post['text']);
    $results = $server->store->search($vec, 5);
    $response->end(json_encode($results));
});
```

**ReactPHP example:**

```php
$emb = new MemVectorEmbedding('/models/all-MiniLM-L6-v2.Q8_0.gguf');
$store = new MemVectorStore('/data/vectors', ['dimensions' => $emb->dimensions()]);

$http = new React\Http\HttpServer(function (Psr\Http\Message\ServerRequestInterface $request) use ($emb, $store) {
    $body = json_decode((string) $request->getBody(), true);
    $vec = $emb->embed($body['text']);
    $results = $store->search($vec, 5);
    return React\Http\Message\Response::json($results);
});
```

In all cases, the `MemVectorEmbedding`, `MemVectorReranker`, and `MemVectorStore` objects stay in memory for the lifetime of the worker — zero overhead per request beyond the actual embed/search computation.
