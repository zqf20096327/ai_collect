# 🚀 Local RAG PDF Chatbot

A locally hosted Retrieval-Augmented Generation (RAG) application that lets users upload PDF documents and ask questions about their content using a private, self-hosted AI stack.

This project combines n8n, Qdrant, Ollama, and a local LLM to build a complete document QA pipeline without relying on paid cloud APIs.

---

## Overview

Traditional language models do not inherently know the contents of a user's private files. This system solves that by transforming uploaded PDFs into searchable embeddings and retrieving relevant context before generating a response.

The pipeline works as follows:

1. Upload a PDF through the web interface.
2. Extract text from the document.
3. Split the content into manageable chunks.
4. Generate vector embeddings for each chunk.
5. Store those embeddings in Qdrant.
6. Convert the user question into an embedding.
7. Retrieve the most relevant document chunks.
8. Pass the context to a local LLM running through Ollama.
9. Generate a grounded answer based on the document content.

In simple terms:

> Upload a PDF → Store its knowledge → Ask questions → Retrieve relevant context → Generate an answer.

---

## Architecture

```text
                         ┌──────────────────────┐
                         │      User            │
                         │                      │
                         │ Upload PDF           │
                         │ Ask Question         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Upload UI          │
                         │  HTML / JavaScript   │
                         └──────────┬───────────┘
                                    │
                                    │ HTTP POST
                                    ▼
                         ┌──────────────────────┐
                         │      n8n Webhook     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   PDF Extraction     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Text Chunking     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Ollama Embeddings  │
                         │   nomic-embed-text   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Qdrant         │
                         │  Vector Database     │
                         └──────────┬───────────┘
                                    │
                                    │ Retrieval
                                    ▼
                         ┌──────────────────────┐
                         │  Semantic Retrieval  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Ollama           │
                         │      Llama 3.1       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Answer          │
                         └──────────────────────┘
```

---

## Features

- Upload PDF documents through a lightweight browser interface
- Extract text from uploaded files
- Split long documents into semantically meaningful chunks
- Generate embeddings locally using Ollama
- Store and retrieve document vectors in Qdrant
- Answer questions grounded in the uploaded document content
- Run the full workflow locally on your own machine
- Use Docker for service orchestration and local deployment

---

## Tech Stack

| Component | Purpose |
| --- | --- |
| n8n | Workflow automation and orchestration |
| Qdrant | Vector database and semantic search |
| Ollama | Local model runtime |
| Llama 3.1 | Large language model for answer generation |
| nomic-embed-text | Text embedding model |
| PostgreSQL | Persistent service database |
| Docker Compose | Local infrastructure orchestration |
| HTML / JavaScript | Upload interface |

---

## Project Structure

```text
.
├── n8n/
│   ├── demo-data/
│   │   ├── credentials/
│   │   └── workflows/
│   └── workflow/
│       ├── RAG - Document Upload.json
│       └── RAG - Question Answering.json
├── shared/
├── assets/
│   ├── Screenshot (176).png
│   └── Screenshot (177).png
├── upload-ui/
│   └── index.html
├── docker-compose.yml
├── LICENSE
├── README.md
└── .gitignore
```

---

## Prerequisites

Before running the project, ensure you have:

- Docker and Docker Compose installed
- Ollama installed locally
- Access to the required models:
  - `llama3.1`
  - `nomic-embed-text`
- A local machine with enough resources for model inference and vector storage

---

## Getting Started

### 1. Start the Docker services

```bash
docker compose up -d
```

Check the running containers:

```bash
docker ps
```

### 2. Start Ollama and pull the required models

Make sure Ollama is running locally and that the models are available:

```bash
ollama pull llama3.1
ollama pull nomic-embed-text
```

Verify the Ollama API:

```bash
curl http://localhost:11434/api/tags
```

### 3. Open n8n

Open the n8n dashboard in your browser:

```text
http://localhost:5678
```

Import or publish the included workflows if required and confirm they are active.

### 4. Upload a PDF

Open the web upload page:

```text
upload-ui/index.html
```

Select a PDF file and click the upload button. The document is automatically sent to the n8n webhook for ingestion.

### 5. Ask questions

Once the document is indexed, use the question-answering workflow to ask questions such as:

```text
What is supervised learning?
```

```text
Explain the methodology described in this document.
```

---

## How the RAG Workflow Works

### 1. Document Upload

The user selects a PDF in the browser, which sends the file to the n8n webhook through an HTTP `POST` request.

### 2. PDF Text Extraction

The uploaded PDF is processed to extract raw text, which is then normalized for downstream tasks.

### 3. Text Chunking

Large documents are split into smaller chunks to improve retrieval quality and reduce prompt size. The project uses a recursive character text splitter with a chunk size of 1000 and overlap of 0.

### 4. Embedding Generation

Each chunk is converted into a vector embedding using `nomic-embed-text` through Ollama.

### 5. Storage in Qdrant

These embeddings are saved in the Qdrant collection named `rag_documents`, together with searchable metadata.

### 6. Semantic Retrieval

When a question is asked, the system embeds the query and searches Qdrant for the most relevant chunks.

### 7. Answer Generation

The retrieved context is then passed to Llama 3.1, which generates a grounded response based on the knowledge found in the uploaded PDF.

---

## Example Workflow

Suppose a user uploads `machine_learning.pdf`.

The application will do the following:

```text
machine_learning.pdf
        ↓
Extract text
        ↓
Create chunks
        ↓
Generate embeddings
        ↓
Store in Qdrant
```

Then the user asks:

```text
What is supervised learning?
```

The system performs:

```text
Question
   ↓
Embedding
   ↓
Qdrant search
   ↓
Relevant document chunks
   ↓
Llama 3.1
   ↓
Answer
```

---

## Why This Project Matters

This project demonstrates how to build a complete local RAG system from start to finish:

- ingest documents
- convert them into embeddings
- store them for similarity search
- retrieve relevant context
- generate grounded answers with a local LLM

The goal is to keep the entire AI pipeline private and local while still delivering useful document-based question answering.

---

## Current Limitations

This version is intentionally focused on learning and demonstrating the core RAG pipeline. A few current limitations include:

- PDF is the primary supported format
- Document deletion is not exposed through the UI
- Multiple uploaded documents are stored in the same Qdrant collection
- Authentication is not implemented for the upload webhook
- The frontend is intentionally lightweight and minimal
- The solution is designed for local and self-hosted experimentation

---

## Future Improvements

Planned enhancements include:

- Better frontend UX and conversation interface
- Document management and deletion
- Per-document metadata and identifiers
- Chat history and session memory
- Source citations in answers
- Multiple collections for different document sets
- Improved chunking and reranking strategies
- Streaming responses from the LLM
- Production-ready deployment patterns

---

## Demo

<table>
  <tr>
    <td align="center" width="50%">
      <img src="assets/Screenshot%20(176).png" alt="n8n RAG question answering workflow" width="100%" />
      <br />
      <strong>Question Answering Workflow</strong>
    </td>
    <td align="center" width="50%">
      <img src="assets/Screenshot%20(177).png" alt="n8n RAG document upload workflow" width="100%" />
      <br />
      <strong>Document Upload Workflow</strong>
    </td>
  </tr>
</table>

These screenshots show the complete local AI workflow running inside n8n, from document ingestion and vector storage to retrieval-augmented question answering.

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
