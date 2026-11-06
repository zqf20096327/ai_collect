# pageindex

**Local-first, vectorless, reasoning-based RAG in Rust.**

[![crates.io](https://img.shields.io/crates/v/pageindex.svg)](https://crates.io/crates/pageindex)
[![docs.rs](https://docs.rs/pageindex/badge.svg)](https://docs.rs/pageindex)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Vector RAG retrieves by *similarity*. pageindex retrieves by *reasoning*. Each document is
indexed into a hierarchical **tree**: a table of contents with page ranges and summaries. At
question time, an LLM agent navigates that tree the way a person reads a long report: it
scans the outline, opens the relevant section, reads the pages and cites them. There are no
embeddings, no vector database and no chunking.

This is an unofficial Rust port of the local mode of
[PageIndex](https://github.com/VectifyAI/PageIndex) (Python, by Vectify AI). It keeps the
same algorithms and prompts, runs entirely on your machine, and makes network calls only to
the model endpoints you configure. Those can be local too: Ollama, llama.cpp, vLLM or
LM Studio.

- **Pure Rust.** PDF parsing is built in, so there is no PDFium, Python or other native library to install.
- **Fast.** Layout-based indexing of a 758-page textbook takes about 1 s (upstream: 16 s).
- **Faithful.** Outlines match the Python implementation exactly on all of its example documents.
- **Any model.** Ollama (native API), OpenAI-compatible servers (OpenAI, llama.cpp, vLLM, LM Studio, OpenRouter), the Anthropic API, or your own `LanguageModel` implementation.
- **Library and CLI.** Streaming chat, citations, multi-turn history, and retrieval tools you can plug into your own agent.

## Quick start

```toml
[dependencies]
pageindex = "0.1"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

```rust
use pageindex::llm::ReasoningEffort;
use pageindex::{IndexOptions, PageIndex};

#[tokio::main]
async fn main() -> pageindex::Result<()> {
    let client = PageIndex::builder()
        .index_model("ollama/qwen3.5:4b") // builds the tree: a small model is enough
        .chat_model("ollama/qwen3.5:9b")  // navigates the tree: use the best you can run
        // Summaries don't need a thinking model to think first.
        .index_options(IndexOptions::new().reasoning_effort(ReasoningEffort::None))
        .build()?;

    let doc = client.index("annual-report.pdf").await?;
    let answer = client.chat("What was the 2023 operating margin?").doc(&doc.id).citations(true).send().await?;

    println!("{answer}");
    for c in &answer.citations {
        println!("  {} p.{}", c.document, c.page);
    }
    Ok(())
}
```

Documents are stored under `./.pageindex` (change it with `.storage_dir(...)`), so each file
is indexed once and queried many times.

### Command line

```sh
cargo install pageindex-cli

export PAGEINDEX_INDEX_MODEL=ollama/qwen3.5:4b PAGEINDEX_CHAT_MODEL=ollama/qwen3.5:9b
export PAGEINDEX_INDEX_REASONING=none   # skip the thinking phase while indexing
pageindex index annual-report.pdf notes.md
pageindex ls
pageindex tree annual-report.pdf --summaries
pageindex chat -d annual-report.pdf "What was the 2023 operating margin?" --cite
pageindex chat                        # interactive, keeps conversation history
pageindex outline paper.pdf           # table of contents only: no model, no store
```

## How it works

```
PDF ──▶ spans ──▶ layout outline ──▶ refined tree + summaries ──▶ store ──▶ chat agent
        (pageindex-pdf)  (pageindex-flash)   (index model)                 (chat model + tools)
```

1. **Parse.** `pageindex-pdf` interprets each page's content stream (fonts, encodings,
   CMaps, Type 3 and CID fonts, form XObjects) into positioned text spans. It also reads
   the PDF's bookmarks.
2. **Outline.** `pageindex-flash` builds the table of contents from layout statistics alone:
   font sizes and weights, numbering, spacing, columns, repeated headers and footers,
   captions, and bookmarks when they can be trusted. No model is involved.
3. **Refine.** The index model merges thin sections, expands oversized ones, and writes a
   summary for each node plus a one-line description of the document.
4. **Answer.** The chat model gets tools to browse documents, read a tree and read page
   ranges. It walks down the tree to the pages it needs and answers with page citations.

### Indexing modes

| Mode | Input | Structure from | Model calls |
|---|---|---|---|
| `Flash` (default for PDFs) | PDF | layout analysis | optional: summaries, refinement, description |
| `Standard` | PDF | the model reads the pages and any printed table of contents | many |
| `Markdown` (default for `.md`) | Markdown | headings | optional: summaries |

```rust
use pageindex::{IndexMode, IndexOptions, Optimize};

// No model calls at all: layout outline plus deterministic merging.
client.index_with("report.pdf", IndexOptions::offline()).await?;

// Standard mode for PDFs whose layout carries no usable hierarchy.
client.index_with("brochure.pdf", IndexOptions::new().mode(IndexMode::Standard)).await?;

// Tune the flash pipeline.
let options = IndexOptions::new().optimize(Optimize::Merge).summary_max_words(80).concurrency(8);
```

## Models

Models are named with `provider/model` strings, or passed as values:

| Spelling | Backend | Configuration |
|---|---|---|
| `ollama/qwen3.5:9b` | Ollama, native API | `OLLAMA_HOST` (default `http://localhost:11434`), `OLLAMA_CONTEXT_LENGTH` (default 32768) |
| `gpt-5-mini` or `openai/gpt-5-mini` | OpenAI | `OPENAI_API_KEY`, optional `OPENAI_BASE_URL` |
| `anthropic/claude-sonnet-5` | Anthropic | `ANTHROPIC_API_KEY` |
| `lmstudio/<model>` | LM Studio | `LMSTUDIO_BASE_URL` (default `http://localhost:1234/v1`) |
| `openai-compatible/<model>` | llama.cpp, vLLM, OpenRouter, ... | `OPENAI_BASE_URL`, optional `OPENAI_API_KEY` |

```rust
use pageindex::llm::{Anthropic, Ollama, OpenAi};

// A llama.cpp server for indexing, Ollama with a custom context window for chat.
let local = PageIndex::builder()
    .index_model(OpenAi::compatible("http://localhost:8080/v1", "qwen3.5-4b"))
    .chat_model(Ollama::new("qwen3.5:9b").with_num_ctx(24_576))
    .build()?;

// Claude with extended thinking for chat.
let hosted = PageIndex::builder()
    .chat_model(Anthropic::from_env("claude-sonnet-5")?.with_thinking_budget(4096))
    .build()?;
```

Implement [`LanguageModel`](https://docs.rs/pageindex/latest/pageindex/llm/trait.LanguageModel.html)
to use anything else.

### Choosing local models

A basic model is enough for indexing. For chat, use the strongest model your GPU can hold with
room for context. Tested on an RTX 3080 (10 GB) with Ollama:

| Role | Model | Result |
|---|---|---|
| Indexing | `qwen3.5:4b`, reasoning `none` | 53-page PDF indexed with summaries in 82 s |
| Chat | `qwen3.5:9b`, 32K context | correct, cited answers in 20–60 s |

Two settings matter for local models:

- **Turn reasoning off for indexing.** Thinking models such as Qwen 3.5 reason for thousands of
  tokens before each one-paragraph summary. With default settings the same PDF took more than
  10 minutes. Use `IndexOptions::reasoning_effort(ReasoningEffort::None)`,
  `--index-reasoning none` or `PAGEINDEX_INDEX_REASONING=none`.
- **Give chat a large context window.** A document tree returned by a tool can run to
  25K tokens. The `ollama/` backend uses Ollama's native API and requests a 32K window
  (`OLLAMA_CONTEXT_LENGTH` or `Ollama::with_num_ctx` to change it). Ollama's
  OpenAI-compatible endpoint can't do this: it silently cuts long prompts to the server
  default, often 8K tokens, dropping the question itself.

Very small models (around 2B and below) tend to answer from summaries without opening the
pages, and they often mangle citations.

## Chat

```rust
use futures::StreamExt;
use pageindex::ChatEvent;

// Stream tokens as they arrive.
let mut events = client.chat("Summarize the risk factors").doc(&doc.id).stream();
while let Some(event) = events.next().await {
    match event? {
        ChatEvent::TextDelta(text) => print!("{text}"),
        ChatEvent::ToolCall(call) => eprintln!("[{}] {}", call.name, call.arguments),
        ChatEvent::Done(answer) => eprintln!("\n{} turns, {:?}", answer.turns, answer.usage),
        _ => {}
    }
}

// Multi-turn: pass the previous transcript back.
let first = client.chat("What was revenue in 2023?").doc(&doc.id).send().await?;
let follow_up = client.chat("And in 2022?").doc(&doc.id).history(first.messages).send().await?;
```

Leave out `.doc(...)` to let the agent browse every stored document. Other options include
`.docs([...])`, `.instructions(...)`, `.max_turns(n)`, `.temperature(t)`,
`.reasoning_effort(...)` and `.model(...)`.

## Bring your own agent

The retrieval tools are available on their own, with JSON schemas, for any agent framework:

```rust
let tools = client.tools().scoped_to([&doc.id]);
let openai_json = tools.to_openai_tools();       // or tools.to_anthropic_tools()
let system_prompt = tools.instructions();
let result = tools.call("get_document_structure", serde_json::json!({"doc_name": doc.name})).await;
```

The tools are `browse_documents`, `get_document`, `get_document_structure`,
`get_page_content`, and `remove_document` when enabled with `.with_management(true)`.
`call` never fails: errors come back as a JSON envelope the model can read.
[`examples/custom_agent.rs`](crates/pageindex/examples/custom_agent.rs) shows a complete loop.

## Crates

| Crate | What it is |
|---|---|
| [`pageindex`](crates/pageindex) | The client: indexing, storage, LLM backends, chat agent and tools. Re-exports the two below. |
| [`pageindex-pdf`](crates/pageindex-pdf) | Pure-Rust PDF text-span extraction and bookmark reading. |
| [`pageindex-flash`](crates/pageindex-flash) | LLM-free outline extraction from PDF layout. |
| [`pageindex-cli`](crates/pageindex-cli) | The `pageindex` command-line tool. |

Optional feature: `pageindex/tiktoken` for exact token counts (o200k) instead of the
built-in approximation.

## Fidelity to upstream

The port is tested against output recorded from the Python implementation (PageIndex 0.2.10)
on its nine example PDFs, from 12 to 758 pages:

- **Outlines:** identical trees for all nine, both with bookmarks and with layout detection only.
- **PDF text:** 99.99–100% of upstream's span text, and 99.55–100% of spans with the same boxes and font sizes.
- **Model pipelines:** byte-identical prompts and identical resulting trees when replaying recorded model responses for flash refinement, summaries, standard mode and Markdown.

Deliberate differences from upstream:

- The cloud service, folders, the MCP bridge and the Python agent-SDK adapters are not included.
- A few upstream crash paths return errors instead.
- CJK PDFs without ToUnicode maps that use predefined CMaps other than Identity are decoded as raw CIDs.

Run the parity suites with `PAGEINDEX_GOLDEN_SPANS=<dir> cargo test`. `testdata/README.md`
describes the fixtures.

## Development

```sh
cargo test --workspace
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo run -p pageindex --example outline -- testdata/pdfs/four-lectures.pdf
```

## License

MIT, for both this port and the upstream project it is derived from. See [LICENSE](LICENSE).
Test PDFs in `testdata/` come from the upstream repository. Bundled Adobe font metrics and
glyph lists carry their own permissive notices in `crates/pageindex-pdf/data/`.
