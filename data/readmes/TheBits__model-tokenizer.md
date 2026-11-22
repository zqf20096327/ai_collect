# model-tokenizer

**Token-accurate support for text splitters.** Use it when you need exact
token counts for a context window. The same text uses different numbers of
tokens depending on the language, and splitting by characters makes the
context window hard to fill. Embedding models have limited context,
so splitting by tokens fills it as fully as possible. Small language models on
devices may also be limited to a 4k or 8k context window.

The package lets [`langchain-text-splitters`](https://python.langchain.com/docs/concepts/text_splitters/) and
[`semantic-text-splitter`](https://github.com/benbrandt/text-splitter) count
and split text by the tokens of a real **llama.cpp** or **vLLM** model, using
the `/tokenize` and `/detokenize` endpoints.

Works with a plain `llama-server` and with routers such as llama-swap or
LiteLLM (`model` is sent in the body and query string so the right backend is
selected; a plain server ignores it).

## Installation

```bash
uv add model-tokenizer
# or
pip install model-tokenizer
```

## langchain-text-splitters

Token-based splitting has two useful forms. `ModelTokenizer` supports both;
no adapter is needed.

### 1. Pure token windows: `split_text_on_tokens`

LangChain's generic seam is the `Tokenizer` dataclass. Build it from
`ModelTokenizer.encode` / `decode`:

```python
from langchain_text_splitters import Tokenizer, split_text_on_tokens
from modeltokenizer import LlamaCppHttpTransport, ModelTokenizer

tokenizer = ModelTokenizer(
    transport=LlamaCppHttpTransport(
        base_url="http://127.0.0.1:9931",
        model_name="my-model",
    ),
)

langchain_tokenizer = Tokenizer(
    chunk_overlap=32,
    tokens_per_chunk=512,
    encode=tokenizer.encode,
    decode=tokenizer.decode,
)

chunks = split_text_on_tokens(text=document, tokenizer=langchain_tokenizer)
```

The document is tokenized once (`POST /tokenize`), then each window is decoded
with `POST /detokenize`, one round trip per emitted chunk.

Pure token windows give a hard token guarantee, but boundaries are token
indices, not word or sentence boundaries, so a chunk can start or end
mid-word. Overlap is exact in token units.

### 2. Token-measured semantic splitting: `length_function`

LangChain's character/recursive splitters accept a custom length function, so
they can keep their paragraph/sentence/word boundaries while measuring size in
server tokens:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    length_function=tokenizer,   # chunk_size and chunk_overlap are now in tokens
    chunk_size=512,
    chunk_overlap=64,
)
chunks = splitter.split_text(document)
```

Trade-offs:

- **Many more requests**: every candidate split or merge calls `tokenizer(text)`,
  so expect one `POST /tokenize` per probe. Token windows tokenize the document
  only once.
- **Not a hard guarantee**: if a single separator unit is larger than
  `chunk_size`, LangChain can emit it anyway and logs a warning.
- **Overlap is not exact token overlap**: LangChain keeps whole separator
  units, so the actual overlap can differ from `chunk_overlap`.

### 3. Note on `TokenTextSplitter`

`langchain_text_splitters.TokenTextSplitter` is hard-wired to tiktoken: it
imports `tiktoken` and loads an OpenAI encoding by name. It has no seam for a
remote tokenizer. Use `split_text_on_tokens` instead.

### Recommendation

- Need exact token windows: `split_text_on_tokens`.
- Need semantic boundaries measured in tokens:
  `RecursiveCharacterTextSplitter(length_function=tokenizer, ...)`.
- Need `Document` objects or `split_documents`:
  `RecursiveCharacterTextSplitter`; `split_text_on_tokens` is only a text
  function.

See `examples/langchain_splitter.py`.

## semantic-text-splitter

`semantic-text-splitter` can only integrate with this client through
`from_callback`: `ModelTokenizer` implements `Callable[[str], int]`, and
every size probe becomes one `POST /tokenize` request. The
`from_huggingface_tokenizer` and `from_tiktoken_model` constructors do not
accept a remote tokenizer object, so they cannot use `ModelTokenizer`.

```python
from semantic_text_splitter import TextSplitter

splitter = TextSplitter.from_callback(tokenizer, (256, 512))
chunks = splitter.chunks(document)
```

The same `from_callback` pattern works with `MarkdownSplitter` and
`CodeSplitter`. See `examples/semantic_splitter.py`.

### MarkdownSplitter

```python
from semantic_text_splitter import MarkdownSplitter

splitter = MarkdownSplitter.from_callback(tokenizer, (256, 512))
chunks = splitter.chunks(markdown_document)
```

### CodeSplitter

`CodeSplitter` also needs a tree-sitter language grammar. Install the grammar
for your language separately (for example, `tree-sitter-python`):

```python
import tree_sitter_python
from semantic_text_splitter import CodeSplitter

splitter = CodeSplitter.from_callback(
    tree_sitter_python.language(),
    tokenizer,
    (256, 512),
)
chunks = splitter.chunks(source_code)
```

For all three splitters, `capacity` is in the server's tokens, and `overlap`
and `trim` behave exactly as they do with `from_callback` on any other sizing
callback.

## How to use

Examples for both libraries are in the `examples/` directory.

```python
from modeltokenizer import LlamaCppHttpTransport, ModelTokenizer

tokenizer = ModelTokenizer(
    transport=LlamaCppHttpTransport(
        base_url="http://127.0.0.1:9931",
        model_name="my-model",          # router model name
        api_key="...",                  # optional Bearer token
        timeout=7200,                   # optional timeout
    ),
)

tokenizer("Hello world!")                # -> 3
tokenizer.encode("Hello world!")         # -> [9906, 1917, 0]
tokenizer.decode([9906, 1917, 0])        # -> "Hello world!"
```

## Development

```bash
uv run python -m unittest discover -s tests -v
ruff check src tests
ruff format --check src tests
```

MIT License
