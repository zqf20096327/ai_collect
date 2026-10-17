# VecPuff

VecPuff is a vector database built on top of S3, inspired by [turbopuffer](https://turbopuffer.com/docs/architecture). It's designed for learning and experimentation with scalable vector search architectures.

I have written about the thought process and journey in [this blog post](https://blog.karanjanthe.me/posts/vecpuff/).

## Architecture

VecPuff uses a log-structured architecture:

1. **WAL (Write-Ahead Log)**: All writes are batched and written to S3 as WAL files
2. **Compaction**: Background process merges WAL files into indexed segments
3. **ANN Index**: SPFresh-based approximate nearest neighbor index for fast search
4. **Local Cache**: Frequently accessed files cached locally for performance

### Building

```bash
# Build release binary
cargo build --release --bin server

# Run server
./target/release/server
```

The server will start on `http://localhost:3000` by default.

## Configuration

VecPuff uses a `config.toml` file for configuration. See `config.toml` for all available options.

### Environment Variables

- `S3_ENDPOINT`: S3 endpoint URL (default: `https://t3.storage.dev`)
- `S3_REGION`: AWS region (default: `sin` or from config)
- `LOCAL_CACHE_PATH`: Local cache directory (default: `./data/cache`)
- `RUST_LOG`: Logging level (e.g., `info`, `debug`)

### Key Configuration Sections

- **`[server]`**: HTTP server settings (timeouts, body size limits)
- **`[limits]`**: Resource limits (max dimensions, document size, etc.)
- **`[batching]`**: WAL batching configuration
- **`[indexing]`**: Compaction triggers and thresholds
- **`[storage]`**: S3 connection settings
- **`[compactor]`**: Background compaction settings

## API Reference

### Health Check

```http
GET /health
```

Returns `OK` if the server is running.

### List Namespaces

```http
GET /namespaces
```

Returns a list of all namespaces.

**Response:**

```json
{
  "namespaces": [{ "id": "my-namespace" }]
}
```

### Upsert Vectors

```http
POST /namespaces/{namespace}
```

Insert or update vectors in a namespace.

**Request Body:**

```json
{
  "distance_metric": "cosine_distance",  // optional: "cosine_distance" or "euclidean_squared"
  "upsert_rows": [
    {
      "id": "doc1",
      "vector": [0.1, 0.2, 0.3, ...],
      "text": "Sample document",
      "category": "tech",
      "score": 42
    }
  ],
  "patch_rows": [...],  // optional: partial updates
  "deletes": ["doc-id"]  // optional: delete by ID
}
```

**Response:**

```json
{
  "upserted_count": 1
}
```

**Row Format:**

- `id`: Unique document identifier (string)
- `vector`: Vector array of floats
- Additional fields: Any JSON-serializable metadata

### Query Vectors

```http
POST /namespaces/{namespace}/query
```

Search for similar vectors.

**Request Body:**

```json
{
  "query_vector": [0.1, 0.2, 0.3, ...],
  "top_k": 10
}
```

**Response:**

```json
{
  "results": [
    {
      "id": "doc1",
      "vector": [0.1, 0.2, 0.3, ...],
      "text": "Sample document",
      "category": "tech"
    }
  ],
  "total_count": 1
}
```

### Get Metadata

```http
POST /namespaces/{namespace}/metadata
```

Get namespace metadata including index status and row counts.

**Response:**

```json
{
  "approx_row_count": 1000,
  "index": {
    "status": "up_to_date",
    "indexed_row_count": 1000,
    "ann_index_file": "index/ann_index.bin"
  },
  "created_at": 1234567890,
  "updated_at": 1234567890
}
```
