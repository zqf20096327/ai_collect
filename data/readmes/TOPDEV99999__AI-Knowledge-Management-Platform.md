# Agentic Documents Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

The *Agentic Documents Assistant* is an LLM-powered assistant that allows users to answer complex questions from business documents through natural conversations.

It supports answering factual questions by retrieving relevant information directly from documents using semantic search based on the RAG (Retrieval-Augmented Generation) design pattern.

Additionally, it can answer analytical questions such as *which contracts will expire in the next 3 months?* by converting user questions into SQL queries and executing them against a database containing structured entities extracted from documents through batch processing.

The assistant can also solve complex multi-step questions by combining document retrieval, analytical reasoning, and external tools through an LLM agent architecture.

## Key Features

- Semantic search to enhance responses with relevant document information
- Structured metadata and entity extraction from documents
- SQL-based analytical reasoning over extracted document data
- LLM agent using the Reason and Act (ReAct) approach
- Intelligent decision-making between search, SQL queries, and available tools
- Conversational interface for enterprise document analysis

## Architecture Overview

The solution follows an agentic AI architecture that combines:

- Document ingestion and processing pipelines
- Semantic search with vector-based retrieval
- Entity extraction and structured data storage
- SQL query generation for analytical questions
- LLM-powered reasoning agents
- Secure frontend and backend communication

## Project Structure

| Folder | Description |
| ----------- | ----------- |
| `backend` | Backend services and infrastructure configuration |
| `frontend` | Frontend deployment and application infrastructure |
| `frontend/chat-app` | Next.js application with authentication and secured backend connectivity |
| `data-pipelines` | Data processing notebooks and pipelines for document ingestion |
| `experiments` | Research experiments and standalone modules for development |

## Getting Started

### Prerequisites

Before running the project, ensure you have:

- An AI model provider configured
- Required API credentials
- Backend and frontend development environments installed
- Database and vector storage configured

### Installation

1. Clone this repository.

2. Install backend dependencies:

```bash
cd backend
npm install
