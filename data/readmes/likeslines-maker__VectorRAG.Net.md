# VectorRAG.Net

High-performance embedded vector database for .NET 8.

VectorRAG.Net is an in-process vector database designed for Retrieval-Augmented Generation (RAG), semantic search, local AI assistants and low-latency applications.

Unlike external vector databases, VectorRAG.Net runs directly inside your application process.

No HTTP.

No Docker.

No external services.

No network latency.

## Features

* SIMD-optimized vector search
* LSH-based ANN indexing
* Hybrid Search (Vector + BM25)
* Automatic document chunking
* Metadata filtering
* Snapshot save/load
* Runtime metrics
* Fully embedded architecture
* .NET 8 native implementation

---

## Installation

```bash
dotnet add package VectorRAG.Net
```

---

## Quick Start

```csharp
// Get your license key: https://principium.pro/vectorrag-net/
const string licenseKey = "VECTOR-XXXX-XXXX-XXXX-XXXX";

var lshConfig = new EmbeddingLshConfig(
    Bands: 24,
    BitsPerBand: 12,
    MaxCandidates: 2048,
    Seed: 42  
);

var db = new VectorRAGDatabase(
    dimension: 1536,
    lshConfig: lshConfig,
    licenseKey: licenseKey  
);
```

---

## Add Documents

```csharp
await db.UpsertTextDocumentAsync(
    externalId: "faq_001",
    text: File.ReadAllText("faq.txt"),
    metadata: new DocumentMetadata
    {
        Department = "Support"
    },
    embeddingModel: embeddingModel
);
```

---

## Vector Search

```csharp
var queryVector =
    await embeddingModel.GenerateEmbeddingAsync(
        "How do I reset my password?"
    );

var results = db.Search(
    queryVector,
    new SearchOptions
    {
        TopK = 5
    }
);
```

---

## Hybrid Search

```csharp
var results = db.Search(
    queryVector,
    new SearchOptions
    {
        TopK = 5,
        UseHybrid = true,
        TextQuery = queryText,
        Alpha = 0.7f
    }
);
```

---

## Metadata Filtering

```csharp
var results = db.Search(
    queryVector,
    new SearchOptions
    {
        TopK = 5,
        Filter = md =>
            md.Department == "Support"
    }
);
```

---

## Save Snapshot

```csharp
await db.SaveAsync("database.vdb");
```

---

## Load Snapshot

```csharp
await db.LoadAsync("database.vdb");
```

---

## Typical Use Cases

### RAG Systems

Store embeddings locally and retrieve context without external vector services.

### Internal Knowledge Bases

Low-latency semantic search for documentation and support portals.

### Desktop AI Applications

Run completely offline without Docker, cloud services or internet access.

### Edge Computing

Vector search on embedded devices, industrial controllers and local servers.

### Corporate Offline Systems

Suitable for environments where external network access is prohibited.

---

## Performance

Example benchmark:

| Operation              | Average Time |
| ---------------------- | ------------ |
| Vector Search (TopK=5) | 15.15 μs     |
| Hybrid Search          | 116.73 μs    |

Actual performance depends on embedding dimensions, dataset size and hardware.

---

## Licensing

VectorRAG.Net is commercial software.

### Production Usage

Production use requires a commercial license.

**Price: $300 USD (one-time payment, perpetual license)**

Includes:
* Perpetual commercial license
* Unlimited production use
* Priority email support
* All future updates

Purchase your license: [https://principium.pro/vectorrag-net/](https://principium.pro/vectorrag-net/)

For licensing questions:

Email: [vipvodu@yandex.ru](mailto:vipvodu@yandex.ru)

Telegram: @vipvodu
---

## Links

NuGet:
https://www.nuget.org/packages/VectorRAG.Net

GitHub:
https://github.com/likeslines-maker/VectorRAG.Net


Benchmark results (local machine)

Environment:
OS:Windows 11 (10.0.26200.7705)
CPU:Intel Core i5-11400F (6C/12T)
.NET:8.0.23
BenchmarkDotNet:0.15.8

Workload:
Docs:10,000
Embedding dim:64 (synthetic deterministic embeddings for benchmarking)
TopK:5
Hybrid mode:Vector + BM25 (BM25 uses hashed term IDs; query-term DF cutoff enabled)
GroupByParentDocument:true

Results:

| Method | Docs | Mean | Allocated |
|---|---:|---:|---:|
| Search_VectorOnly_Top5 | 10000 | 15.15 μs | 5.69 KB |
| Search_Hybrid_Top5 | 10000 | 116.73 μs | 14.85 KB |

Notes:
Benchmarks were executed without an attached debugger (dotnet run -c Release).
Hybrid performance depends heavily on term distribution (worst-case queries with extremely common terms are intentionally mitigated).


