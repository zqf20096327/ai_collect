# StudyProof

**Bring your sources to an AI study session. Check the quotes that come back.**

[![Tests](https://github.com/Lapmlnex/studyproof/actions/workflows/ci.yml/badge.svg)](https://github.com/Lapmlnex/studyproof/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-527548.svg)](LICENSE)

StudyProof is a local evidence workbench for researchers and students. Add PDFs,
lecture notes, or readings. Search for relevant passages, export a compact context
pack for your AI assistant, and check whether quotations in its answer actually
appear in that pack.

No account. No API key. No embedding model or GPU. Your source library stays on
your computer until you choose to share passages with an AI client.

## Try it in one command

With [uv](https://docs.astral.sh/uv/getting-started/installation/) installed:

```sh
uvx --from git+https://github.com/Lapmlnex/studyproof studyproof demo --web
```

Open the local address printed in the terminal. The demo includes original
teaching notes about retrieval, study practice, and interpreting evidence.
Search **retrieval evidence**, build a pack, then try the quotation checker.
No external documents or model credentials are needed.

## The workflow

| Step | What you get |
| --- | --- |
| **Add** a PDF, Markdown file, or text note | A searchable local library with source hashes and page/line locations |
| **Search** a topic | Relevant excerpts ranked with SQLite's BM25 keyword search |
| **Pack** your evidence | Markdown context for an AI assistant plus a JSON audit file |
| **Check** an answer | Matching quotations, missing references, unknown IDs, and changed wording |

A pack assigns citation IDs such as `[S1]` to the excerpts it contains. Ask your
assistant to quote evidence using this format:

```markdown
> Exact wording from the evidence pack. [S1]

Explain what this passage means, and identify what it does not establish.
```

StudyProof checks the quotation against `[S1]`. A real citation ID alone is not
proof that an answer is supported. **The audit checks quoted wording and citation
IDs; it does not verify scientific truth, paraphrases, or the reasoning around a
quote.** An answer without checkable quotations is reported as unverified.

## Use your own sources

Install once with Python 3.10 or newer:

```sh
python -m pip install git+https://github.com/Lapmlnex/studyproof
studyproof serve
```

Open the printed localhost address and select **Add sources**. Supported formats:
text-layer PDF, `.md`, and `.txt`. The browser accepts files up to 10 MiB each.
Uploaded files and the index remain in your local StudyProof workspace.

Or use the terminal:

```sh
studyproof add paper.pdf
studyproof add lecture-notes.md
studyproof search "retrieval evidence"
studyproof pack "retrieval evidence" --output context.md
studyproof audit answer.md --pack context.json
```

Keep `context.json` with the answer you want to check. Audit against the same
pack you gave your assistant. Packs include excerpt text and source hashes so
they can be inspected separately from your current library.

For a separate course or project, put `--db` before the command:

```sh
studyproof --db ./course/library.db add reading.pdf
studyproof --db ./course/library.db serve
```

Run `studyproof --help` and `studyproof <command> --help` for available options.

## Connect an AI assistant with MCP

The optional adapter exposes read-only source listing, search, and context-pack
creation through the official Model Context Protocol Python SDK.

```sh
python -m pip install 'studyproof[mcp] @ git+https://github.com/Lapmlnex/studyproof'
studyproof --db /absolute/path/to/library.db mcp
```

For an MCP client that accepts JSON server configuration:

```json
{
  "mcpServers": {
    "studyproof": {
      "command": "studyproof",
      "args": ["--db", "/absolute/path/to/library.db", "mcp"]
    }
  }
}
```

Replace the database path with your library's path; use an absolute executable
path if your client cannot find `studyproof`. Restart the client after adding its
configuration. The adapter uses stdio and does not start a public HTTP endpoint.

Your AI client may send retrieved passages to its model provider. Its privacy
settings apply. Source text is untrusted content; it is never an instruction to
execute a command or disclose other files.

## What this version does well

- A small, inspectable retrieval core, without a vector database service.
- Source locations and fingerprints attached to the retrieved text.
- A context-size budget measured in characters, including the pack wrapper.
- A useful browser interface, CLI, and optional MCP adapter over the same core.
- Explicit failures and uncertainty instead of a green badge for any cited answer.

## Limits to know

- Search matches words, not meaning. Try a specific term that occurs in your
  readings. It does not expand synonyms or translate queries.
- PDF extraction requires a text layer. Scanned PDFs need OCR beforehand.
  Multi-column text, tables and mathematical notation may extract imperfectly.
- Matching a quote does not establish the source's quality, relevance or truth.
- Source hashes identify an imported file snapshot. They are not a publisher
  signature or proof that an exported pack has not been deliberately altered.
- The workbench is for your own computer. It binds to `127.0.0.1` and is not a
  multiuser hosted service. See [SECURITY.md](SECURITY.md).

## Development

```sh
git clone https://github.com/Lapmlnex/studyproof
cd studyproof
python -m pip install -e '.[dev,mcp]'
python -m pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for small, useful ways to help and
[docs/SOURCE_USE.md](docs/SOURCE_USE.md) for the implementation's source references.

If StudyProof helps with a reading group, a course, or a research project, share
the repository with someone who has the same problem. Reproducible bug reports
and small example files are especially useful.

## License

[MIT](LICENSE). Created by [Lapmlnex](https://github.com/Lapmlnex).
