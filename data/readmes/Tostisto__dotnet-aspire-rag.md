# Aspire RAG demo

A small .NET 10 demo of retrieval-augmented generation with an AI agent, orchestrated by Aspire and built with Clean Architecture. It indexes Markdown documentation into Qdrant and answers questions about it with a local Ollama model, citing the pages it used.

The sample documentation is the [VS Code wiki](https://github.com/microsoft/vscode/wiki), included as a git submodule in `refs/`. Any folder of Markdown files can be added under `Documents:Folders` in `src/AspireRag.AppHost/appsettings.json`.

## How it works

On startup the ingestion worker splits every page into chunks, embeds them with `nomic-embed-text` and stores them in Qdrant. When it finishes, the API starts. Each question goes to an agent (Microsoft Agent Framework with `llama3.2:3b`) that searches Qdrant and answers only from the results.

## Projects

- `Domain`: documents, chunks, questions and answers.
- `Application`: use cases and the interfaces they depend on. No AI or vendor packages.
- `Infrastructure`: Qdrant, Ollama, the agent and the Markdown reader.
- `Api` and `IngestionWorker`: the two hosts.
- `AppHost` and `ServiceDefaults`: Aspire orchestration and shared telemetry.

## Run

Requires the .NET 10 SDK, Docker, Ollama and the Aspire CLI.

```bash
./scripts/refs.sh   # fetch the documentation submodule
aspire run
```

Open the Scalar link of the `api` resource in the dashboard, or use `src/AspireRag.Api/AspireRag.Api.http`. `POST /api/ask` takes a question and a `mode`: `Always` searches before every answer, `OnDemand` lets the agent decide when to search. `GET /api/search` shows the raw search results.

## Test

```bash
dotnet test --solution AspireRag.slnx --filter-not-trait "Category=Integration"
dotnet test --project tests/AspireRag.IntegrationTests
```

The unit tests cover the layers and their dependency rules. The integration tests start the whole app, so stop `aspire run` first.
