<div align="center">

<img src="docs/assets/logo.svg" alt="kakemono logo" width="120" height="120">

# kakemono

**Convert PDF papers and books, Word documents, EPUB books, or arXiv papers into readable, editable formats.**

[![Release](https://img.shields.io/github/v/release/iamcaominhtien/kakemono?label=release&color=d9822b)](https://github.com/iamcaominhtien/kakemono/releases/latest)
[![CI](https://img.shields.io/github/actions/workflow/status/iamcaominhtien/kakemono/ci.yml?branch=main&label=CI&logo=githubactions&logoColor=white)](https://github.com/iamcaominhtien/kakemono/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/kakemono?logo=rust&logoColor=white)](https://crates.io/crates/kakemono)
[![PyPI](https://img.shields.io/pypi/v/kakemono?logo=python&logoColor=white)](https://pypi.org/project/kakemono/)
[![docs.rs](https://img.shields.io/docsrs/kakemono?label=docs.rs)](https://docs.rs/kakemono)
[![License: MIT](https://img.shields.io/badge/license-MIT-2f9e44)](LICENSE)

</div>

kakemono is a Rust document converter and library. It extracts reading order and structure from PDFs, Word files and EPUB books, including headings, tables, equations and figures. It can produce HTML, DOCX, Markdown, LaTeX, Typst (an article or a printed book), EPUB, editable JSON and JSONL chunks for retrieval. Word and EPUB input can also be laid out as PDF. PDF processing uses [hayro](https://github.com/LaurenzV/hayro); no Python, Poppler or MuPDF is needed for the CLI.

## Install

Download a prebuilt binary for Linux, macOS or Windows from the [latest release](https://github.com/iamcaominhtien/kakemono/releases/latest), or install with stable Rust:

```bash
cargo install kakemono
```

To build from a checkout, run `cargo build --release`. For Python, use `pip install kakemono` and see the [Python guide](python/README.md).

## Quick start

```bash
kakemono convert paper.pdf                   # paper.friendly.html
kakemono convert 1706.03762 -o paper.md      # arXiv ID → Markdown
kakemono convert report.docx -o report.pdf   # Word → PDF
kakemono convert book.epub -o book.md        # EPUB → Markdown
kakemono convert paper.pdf -o paper.epub
kakemono convert book.pdf -o book.typ        # Typst; then `typst compile book.typ`
kakemono convert paper.pdf -o paper.jsonl    # chunks for retrieval
```

Input can be a local PDF, `.docx`, `.doc` or `.epub`, an arXiv ID or an arXiv URL. The output extension selects the format; use `--format` to choose explicitly. arXiv downloads are cached in `~/.cache/kakemono` (override with `KAKEMONO_CACHE`).

For HTML, choose a layout with `--mode`:

| Mode | Layout |
| --- | --- |
| `friendly` | Responsive single-column article (default) |
| `medium` | Preserves pages and columns while reflowing text |
| `hard-95` | Page-like layout with visible HTML text |
| `hard` | Page images with a selectable text layer |

```bash
kakemono convert paper.pdf -m hard-95 -o paper.html
kakemono convert paper.pdf --all -o out/     # all four HTML modes
kakemono convert paper.pdf -o paper.md --image-dir images
kakemono convert paper.pdf -o paper.jsonl --chunk-tokens 512
```

Markdown, LaTeX, Typst and JSON write image files alongside the output by default. The Typst output is laid out as a printed book (title page, chapters on right-hand pages, running heads, footnotes on the page of their call) when the document has chapters, as an article otherwise (`--layout` to choose); its settings, such as the page size and the fonts, are at the top of the `.typ` file. See the [guide](docs/GUIDE.md#typst). See `kakemono convert --help` for image handling, table and equation options, tokenizers and other settings. `kakemono inspect paper.pdf` prints the detected structure; `kakemono fetch <arxiv-id> -o paper.pdf` downloads a paper.

## Edit extracted content

Export editable JSON, change its text, then apply it to the same input:

```bash
kakemono convert paper.pdf -o paper.json
# Edit paper.json and save it as paper.edited.json
kakemono convert paper.pdf --content paper.edited.json -o paper.edited.md
```

This JSON is distinct from the full analysis written by `--json`. Edited text is supported in PDF-derived outputs except `hard`; for Word input it does not reach page-layout outputs (PDF, `hard`, `hard-95` or `medium`). See the [editable JSON guide](docs/GUIDE.md#editable-json) for its schema and editing rules.

## Libraries

Rust: add the crate with `cargo add kakemono`, then reuse an analysis across outputs:

```rust
use kakemono::{HtmlOptions, Mode, Paper};

let paper = Paper::from_bytes(std::fs::read("paper.pdf")?)?;
let analysis = paper.analyze();
let out = paper.to_html(&analysis, &HtmlOptions { mode: Mode::Friendly, ..Default::default() });
std::fs::write("paper.html", out.html)?;
```

The [API reference](https://docs.rs/kakemono) and [library guide](docs/GUIDE.md#use-as-a-library) cover other outputs. Python bindings and examples are documented in [python/README.md](python/README.md).

## Limitations

Scanned and encrypted PDFs are not supported. Complex tables and equations may be kept as images, and unusual layouts can affect reading order. Word 6/95, RTF and password-protected Word files are not supported, nor are EPUB books protected by DRM. See the [full limitations](docs/GUIDE.md#limitations), the [Word input guide](docs/WORD-INPUT.md) and [EPUB input](docs/GUIDE.md#epub-books-as-input).

## Development

```bash
cargo test --release
```

Some real-paper tests require additional downloads; see the [testing guide](docs/GUIDE.md#testing). [CONTRIBUTING.md](CONTRIBUTING.md) explains the development workflow, and [ARCHITECTURE.md](ARCHITECTURE.md) describes the pipeline. See also the [detailed guide](docs/GUIDE.md), [benchmarks](docs/GUIDE.md#performance) and [changelog](CHANGELOG.md).

## License

[MIT](LICENSE) © Cao Minh Tiến.
