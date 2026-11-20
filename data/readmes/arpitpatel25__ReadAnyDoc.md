# ReadAnyDoc

<!-- mcp-name: io.github.arpitpatel25/readanydoc -->

[![GitHub stars](https://img.shields.io/github/stars/arpitpatel25/ReadAnyDoc?style=social)](https://github.com/arpitpatel25/ReadAnyDoc) [![PyPI](https://img.shields.io/pypi/v/readanydoc)](https://pypi.org/project/readanydoc/) [![Downloads](https://img.shields.io/pypi/dm/readanydoc)](https://pepy.tech/project/readanydoc) [![Tests](https://github.com/arpitpatel25/ReadAnyDoc/actions/workflows/ci.yml/badge.svg)](https://github.com/arpitpatel25/ReadAnyDoc/actions/workflows/ci.yml) [![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/LICENSE) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arpitpatel25/ReadAnyDoc/blob/main/examples/quickstart.ipynb)

Parse and extract documents with vision models, on your own machine and your own model account.
Open source, Reducto-compatible, built by Unmute. Website: https://arpitpatel25.github.io/ReadAnyDoc/

ReadAnyDoc reads every page of a PDF, scan, photo or Office file with a vision model (Claude Haiku 5.5 by default)
and returns typed blocks, tables, Markdown, or the fields of your schema, each with the place on the page it came
from. Around the model sits an engine that adds what a model alone does not give you: block types and positions,
form fields, headers and footers, table checks, word-level citations. It runs as a Python library or as a server
that speaks [Reducto](https://reducto.ai)'s HTTP API, so existing Reducto integrations work by changing one URL.

```python
import readanydoc

result = readanydoc.parse("invoice.pdf")
print(result.markdown)
```

<p align="center"><img src="https://raw.githubusercontent.com/arpitpatel25/ReadAnyDoc/main/examples/showcase/loan-estimate-citations.jpg" width="560" alt="A Loan Estimate with a citation box around every value ReadAnyDoc extracted"></p>

**A real document, unedited**: the US government's sample Loan Estimate, extracted in one call for about 1 cent.
All 11 fields are right, and every box is a citation ReadAnyDoc returned. A yes/no answer that is not printed as one
word is marked low confidence instead of pretending. A faded 1904 invoice is in the same folder:
[examples/showcase](https://github.com/arpitpatel25/ReadAnyDoc/tree/main/examples/showcase/). If it looks useful, ⭐ star the repo.

## Results

ReadAnyDoc 0.4.5 against Reducto on public benchmarks, same documents and same requests, every score from the
benchmark's own grader or from code (no AI judge). Details, per-document scores and caveats:
[BENCHMARKS.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/BENCHMARKS.md).

**Parsing**

| Benchmark | Reducto | ReadAnyDoc |
|---|---|---|
| olmOCR-bench, overall (1,403 pages) | 80.9 | **84.3** |
| OmniDocBench, text error, lower is better (1,651 pages) | 0.095 | **0.073** |
| OmniDocBench, layout: block types right | **84.6%** | 79.0% |
| RD-TableBench (1,000 tables) | 88.85 | 88.84 |
| FUNSD, form question/answer pairs (199 forms) | **78.6** | 77.4 |
| Cost per page | $0.010 | $0.003-0.005 |

**Extraction** (share of the answer key found, cost per document)

| Test set | Reducto | ReadAnyDoc |
|---|---|---|
| Long reports, table rows (LongExtract, 6 documents) | 9.1%, $1.02 | **56.4%**, $0.44 |
| 10-Q and 10-K filings (ExtractBench, 5) | 48.9%, $1.24 | **79.1%**, $0.34 |
| Research papers (ExtractBench, 3) | 49.9%, $0.33 | **68.4%**, $0.074 |
| Credit agreements, 97-218 pages (ExtractBench, 3) | 83.3%, $2.83 | 82.2%, $0.20 |
| Invoices: photos, scans, handwriting (20) | 99.8%, $0.027 | 99.8%, $0.0045 |
| Commercial contracts (CUAD, 10) | not run | 86.5%, $0.026 |

Where Reducto is ahead: page layout (about 6 points), formulas, header and footer removal, precision on 10-Q
filings (ReadAnyDoc writes more values than the answer key holds), and speed (seconds a page against 20-50 s here).

## Install

```bash
pip install "readanydoc[engine]"        # the engine: layout model and OCR run on your CPU
pip install readanydoc                  # model-only mode, no local models
```

The engine also uses [Tesseract](https://github.com/tesseract-ocr/tesseract) when it is installed
(`brew install tesseract` / `apt install tesseract-ocr`). The layout and OCR weights (about 200 MB, Apache-2.0)
are downloaded on first use, so the very first parse takes a few minutes longer; later runs start straight away. Python 3.12 or 3.13.

Set your model provider's key: `export ANTHROPIC_API_KEY=...` (or `OPENAI_API_KEY` for OpenAI models).

### Or let your coding agent set it up

Paste this into Claude Code, Codex or Cursor. It installs ReadAnyDoc, tests it on one of your files and wires it
into your project the way you choose ([what it follows](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/AGENT_SETUP.md)):

```text
Set up ReadAnyDoc in this project. Follow the instructions at
https://raw.githubusercontent.com/arpitpatel25/ReadAnyDoc/main/AGENT_SETUP.md
```

## Use

### Parse

```python
result = readanydoc.parse("statement.pdf")
result.blocks          # [Block(type="Table", content="<table>...", bbox=BoundingBox(...)), ...]
result.tables          # the Table blocks
result.markdown        # the whole document as Markdown
result.usage           # model calls, tokens, cost in USD, seconds
result.warnings        # anything that went wrong on a page
```

### Extract into your own types

```python
from pydantic import BaseModel

class Invoice(BaseModel):
    number: str
    issued: str
    total: float

out = readanydoc.extract("invoice.pdf", schema=Invoice)
out.data                      # Invoice(number="INV-2041", issued="2026-03-01", total=1575.0)
out.citations["total"]        # [Citation(content="1,575.00", bbox=BoundingBox(page=1, left=0.81, ...))]
```

The result holds your fields and nothing else; the model writes only those, so a large schema costs what the
answer costs. Opt-in: `review=True` lists values to check (not printed as returned, ambiguous dates, crossed out,
lists shorter than their table; found by code, no model call), `alternatives=True` returns other values the document
gives for a field (a special term that changes a price). See [Extract](https://arpitpatel25.github.io/ReadAnyDoc/docs/guides/extract/#extras).

A JSON Schema dict works as well as a pydantic class. `instructions=` is the system prompt for the extraction
model; `array_extract=True` processes long documents in parts and merges their lists.

### Choose the mode and the models

| Mode | What it does |
|---|---|
| `engine` (default) | The model reads each page; the engine adds layout, forms, headers/footers, table checks and citations |
| `model-only` | One model read per page and nothing else: cheapest, fastest, no structure beyond what the model writes |

Every model the pipeline uses can be chosen, with its effort level and any further request options:

```python
readanydoc.parse(
    "form.pdf",
    mode="engine",
    model="claude-haiku-5-5", effort="high",                 # page reading (the default)
    model_options={"max_tokens": 32000},                     # sent as given to the provider
    handwriting_model="claude-sonnet-5-5",                   # handwritten pages (the default); None = like any page
)

readanydoc.extract("contract.pdf", schema=Terms,
                 model="claude-haiku-5-5",                   # reads the pages
                 extract_model="claude-sonnet-5-5", extract_effort="high")   # fills the schema
```

Models: any Claude model, OpenAI models (`gpt-...`), or any OpenAI-compatible endpoint written as
`openai_compatible:<model>@<base_url>`. The benchmark numbers above are for Claude Haiku 5.5; other models work
but have not been measured here.

### Command line

```bash
readanydoc parse invoice.pdf --markdown
readanydoc parse scan.pdf --mode model-only --model claude-sonnet-5-5
readanydoc extract invoice.pdf --schema invoice.schema.json
```

### Server (Reducto-compatible API)

```bash
readanydoc serve --port 8000
# or: docker compose up
```

```python
from reducto import Reducto   # Reducto's own SDK, unchanged

client = Reducto(api_key="anything", base_url="http://127.0.0.1:8000")
upload = client.upload(file=Path("invoice.pdf"))
result = client.parse.run(input=upload.file_id)
```

Parse, extract, split, classify, edit, async jobs, webhooks and citations are implemented. Configuration,
security settings and a route-by-route compatibility table: [the documentation](https://arpitpatel25.github.io/ReadAnyDoc/docs/deploy/configuration/).

### Inside Claude, Cursor and other assistants (MCP)

```bash
pip install "readanydoc[engine,mcp]"
claude mcp add readanydoc -e ANTHROPIC_API_KEY=your-key -- readanydoc mcp
```

In Claude Code you can install the plugin instead (server plus a skill): `/plugin marketplace add arpitpatel25/ReadAnyDoc`,
then `/plugin install readanydoc@readanydoc`.

Gives the assistant two tools, `parse_document` and `extract_fields` (with citations), on files on your computer.
Setup for Claude Desktop, Cursor and others: [MCP guide](https://arpitpatel25.github.io/ReadAnyDoc/docs/get-started/mcp/).

### LangChain and LlamaIndex

```python
from readanydoc.integrations.langchain import ReadAnyDocLoader     # pip install "readanydoc[engine,langchain]"
from readanydoc.integrations.llamaindex import ReadAnyDocReader    # pip install "readanydoc[engine,llamaindex]"
```

One Markdown document per page with its page number. [Guide](https://arpitpatel25.github.io/ReadAnyDoc/docs/guides/integrations/).

### Test it against what you use now

```bash
readanydoc bench list                                                      # invoices, receipts, filings, contracts, resumes...
readanydoc bench run invoices --systems readanydoc,plain:claude-haiku-5-5,reducto --limit 10
readanydoc bench mine ./my_docs --schema schema.json --answers ./answer_keys   # your own documents
```

Your own keys, a cost estimate before anything runs, scoring by code against answer keys, and an HTML report with
every system's citations on the page. [Guide](https://arpitpatel25.github.io/ReadAnyDoc/docs/guides/testing/).

## How it works

Each page goes through a fixed sequence of stages (`readanydoc/pipeline/`): intake (file type, pages), triage
(digital or scanned, rotation), layout (an open layout model on CPU), read (the vision model; zoomed re-reads of
scanned pages where two reads must agree before a character changes; handwritten pages to a stronger model),
verify (table grids and printed totals checked without a model), ground (word and cell positions, block types,
form fields), assemble and shape (the requested output format). Nothing the model wrote is changed without
independent evidence. Design decisions and their reasons: [docs/decisions.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/docs/decisions.md).

## Limits

- Slower than Reducto: 20-50 s per page here against about 5 s.
- About 1.5-3% of pages in large public benchmarks are declined by the model provider (content filtering). Those
  pages fall back to plain OCR text at `low` confidence, or to a second model if you set
  `READANYDOC_REFUSAL_READER`; the response says so in `warnings`.
- Confidence values are tiers from how a value was found on the page, not calibrated probabilities.

## Documentation

| | |
|---|---|
| [BENCHMARKS.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/BENCHMARKS.md) | full results against Reducto, cost, method, caveats; per-document scores in [results/](https://github.com/arpitpatel25/ReadAnyDoc/tree/main/results/) |
| [docs/story.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/docs/story.md) | the whole story: the idea, how we measured, the parser, the extractor, two stages or one, what we learned |
| [docs/research/journey.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/docs/research/journey.md) | the parser research record: every stage, every experiment, what was kept and dropped and why |
| [docs/research/extraction.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/docs/research/extraction.md) | the extraction research record: structured output, caching, page parts, citations, one stage |
| [docs/decisions.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/docs/decisions.md) | every design decision with its reason |
| [Documentation](https://arpitpatel25.github.io/ReadAnyDoc/docs/) | guides, API reference, configuration, migrating from Reducto |
| [examples/](https://github.com/arpitpatel25/ReadAnyDoc/tree/main/examples/) | runnable scripts |
| [AGENTS.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/AGENTS.md), [llms.txt](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/llms.txt) | a map of the repo for AI agents; point your agent at it to ask questions |

## Community
> If ReadAnyDoc saved you time, a [star on GitHub](https://github.com/arpitpatel25/ReadAnyDoc) helps other developers find it.


Questions, ideas and what you built: [GitHub Discussions](https://github.com/arpitpatel25/ReadAnyDoc/discussions).
Bugs: [open an issue](https://github.com/arpitpatel25/ReadAnyDoc/issues/new/choose). Release news: watch the
repository (*Watch, Custom, Releases*).

## Contributing

See [CONTRIBUTING.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/CONTRIBUTING.md). Security reports: [SECURITY.md](https://github.com/arpitpatel25/ReadAnyDoc/blob/main/SECURITY.md).

## License

Apache-2.0. The layout model (Docling "heron") and the PP-OCR weights are Apache-2.0.
