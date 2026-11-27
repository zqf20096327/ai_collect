<div align="center">

# 📄 Papyrus

**Papyrus turns documents and web pages into Markdown, chunks and images for your LLM pipeline. It runs as one Docker service, separate from your app.**

[![Version](https://img.shields.io/github/v/release/axelered/papyrus?style=for-the-badge&logo=github&logoColor=white&label=version&labelColor=18181b&color=3f3f46)](https://github.com/axelered/papyrus/releases)
[![CI](https://img.shields.io/github/actions/workflow/status/axelered/papyrus/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=ci&labelColor=18181b)](https://github.com/axelered/papyrus/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/actions/workflow/status/axelered/papyrus/release.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=release&labelColor=18181b)](https://github.com/axelered/papyrus/actions/workflows/release.yml)
[![License](https://img.shields.io/github/license/axelered/papyrus?style=for-the-badge&label=license&labelColor=18181b&color=3f3f46)](https://github.com/axelered/papyrus/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/axelered/papyrus?style=for-the-badge&logo=github&logoColor=white&label=stars&labelColor=18181b&color=3f3f46)](https://github.com/axelered/papyrus/stargazers)
[![Docs](https://img.shields.io/badge/docs-axelered.com-3f3f46?style=for-the-badge&labelColor=18181b)](https://docs.axelered.com/papyrus)

<img src="docs/assets/sticker.png" alt="Papyrus" width="100%">

[Documentation](https://docs.axelered.com/papyrus) · [Quickstart](https://docs.axelered.com/papyrus/quickstart) · [API Reference](https://docs.axelered.com/papyrus/api) · [Python SDK](https://pypi.org/project/papyrus-sdk/) · [TypeScript SDK](https://www.npmjs.com/package/@axelered/papyrus) · [HELM Chart](chart)

</div>

📦 **One service instead of a parser stack.** PDF, Word, PowerPoint, Excel, Outlook, HTML, EPUB, ZIP and images go in, Markdown or chunks sized for your embedding model come out. LibreOffice, pdfium, Chromium and the OCR clients ship inside the image, so your app needs an HTTP client and nothing else.

🛡️ **Your app never parses untrusted files.** Every document is read in a worker process inside the container, and a file that crashes or hangs a worker fails its own request while the worker is replaced. URLs pass an SSRF guard that refuses private and internal addresses, and images are checked against a pixel limit before decoding. Your developers call an API and don't have to get parser isolation and security right themselves.

🔍 **OCR on your own GPUs or through Mistral.** Point Papyrus at a Qwen VL model on vLLM, Ollama or any OpenAI compatible server and page images stay in your network, or use Mistral OCR. Switching backends is a configuration change, and callers keep the same request. Auto mode sends a document to the model only when its text layer is unusable.

The same service renders pages, makes thumbnails of documents and web pages, and takes screenshots in headless Chromium, for previews in your UI.

## 🚀 Quickstart

```shell
docker run --rm -p 8000:8000 -e PAPYRUS_API_KEY=dev ghcr.io/axelered/papyrus:latest
```

Read any file:

```shell
curl http://127.0.0.1:8000/v1/markdown -H 'Authorization: Bearer dev' -F file=@sample.pdf
```

```json
{
  "source": {"uri": "file://file", "name": "sample.pdf", "size": 18810, "mimeType": "application/pdf", "label": "pdf", "group": "document"},
  "result": {"name": "sample.md", "size": 3092, "mimeType": "text/markdown", "encoding": "utf-8", "content": "Sample PDF\nThis is a simple PDF file. Fun fun fun.\n\n…"},
  "options": {"readMode": "text"}
}
```

Send a URL instead of a file with `-d '{"source": "https://axelered.com"}'`, or add
`{"options": {"chunking": {"maxTokens": 512}}}` to get the Markdown chunked ready for RAG. See more in the
[quickstart](https://docs.axelered.com/papyrus/quickstart).

## 🧩 SDKs

Typed clients for Python and TypeScript, with retries and the same options as the API.

```python
# pip install papyrus-sdk
from pathlib import Path
from papyrus_sdk import Papyrus

with Papyrus(base_url='http://127.0.0.1:8000', api_key='dev') as client:
    doc = client.markdown(Path('report.pdf'))

print(doc.result.content)
```

```ts
// npm install @axelered/papyrus
import { openAsBlob } from 'node:fs'
import { Papyrus } from '@axelered/papyrus'

const client = new Papyrus({ baseUrl: 'http://127.0.0.1:8000', apiKey: 'dev' })
const doc = await client.markdown(await openAsBlob('report.pdf'), { filename: 'report.pdf' })
console.log(doc.result.content)
```

Guides: [Python](https://docs.axelered.com/papyrus/python), [TypeScript](https://docs.axelered.com/papyrus/typescript).

## 🤔 Why Papyrus

Reading documents looks like a small feature until it reaches production. Every format needs its own parser with its own bugs, a `.doc` from 2003 needs LibreOffice, a scanned contract needs OCR, a file named `.pdf` turns out to be a ZIP, and one upload or URL from a user can crash your process, hang it for minutes or make it fetch your cloud metadata endpoint. Each of these problems ends up in your codebase, your dependency tree and your on-call rotation.

Papyrus takes all of it out of your app. You send a file or a URL and get Markdown, chunks or an image back, in one response shape with stable error codes, whatever the input was. Everything else happens behind the API:

- Formats: Papyrus detects the real type from the content, routes it to the right engine and converts legacy Office and OpenDocument files with LibreOffice, so your code never branches on file type.
- Untrusted input: documents are read in worker processes that Papyrus replaces when a file crashes or hangs them, and that request fails with `500 processing_failed` or `504 processing_timeout` while your service keeps running. URLs, redirects and page resources go through an SSRF guard.
- OCR: scans and images are read by the backend you configure, on your own GPUs or at Mistral, and callers send the same request either way.
- Previews: page renders, thumbnails and website screenshots come from the same API, with Chromium running inside the Papyrus container, away from your app.
- Upgrades: the converters, LibreOffice, Chromium and their security fixes ship as one image, so staying current means changing an image tag.

Any language with an HTTP client gets the same results, and the Python and TypeScript SDKs add types on top.

## 📚 Supported formats

| Group           | Extensions                                                         | What you get                                                                                          |
|-----------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Documents       | `.pdf`, `.docx`, `.doc`, `.rtf`, `.odt`                            | Markdown from the text layer, or from every page with OCR. Pages render and thumbnail                 |
| Presentations   | `.pptx`, `.ppt`, `.odp`                                            | Slide text, tables and notes, or every slide with OCR, without notes. Slides render and thumbnail     |
| Spreadsheets    | `.xlsx`, `.xls`, `.ods`, `.csv`, `.tsv`                            | One Markdown table per sheet. Excel and OpenDocument sheets render and thumbnail                      |
| Web and email   | `.html`, `.htm`, `.msg`, `.epub`, `.rss`, `.atom`, `.xml`          | Headings, lists, links and tables, Outlook headers and body. HTML thumbnails are browser captures     |
| Images          | `.png`, `.jpg`, `.webp`, `.gif`, `.bmp`, `.tiff`, `.avif`          | Markdown with OCR, from every frame of a TIFF and the first frame of the others. One frame per render |
| Archives        | `.zip`                                                             | Every entry converted                                                                                 |
| Data and text   | `.json`, `.jsonl`, `.ipynb`, `.txt`, `.md`, `.rst`, `.tex`, ...    | Passed through as Markdown                                                                            |
| Code and config | `.py`, `.ts`, `.go`, `.sql`, `.yaml`, ...                          | One fenced block, for any language                                                                    |

Legacy Office and OpenDocument files are converted with LibreOffice before extraction, and every Office file goes through LibreOffice to render, which adds time to each request. Formats without pages are read as text even when a request asks for OCR, and `options.readMode` in the response says so. Screenshots take `http(s)://` URLs and capture whatever the browser shows.

Papyrus detects the format from the content with Magika and uses the extension only to refine generic matches, so a mislabeled file is processed as what it really is and reported in `source`. The [formats guide](https://docs.axelered.com/papyrus/formats) has the full table per operation.

## ☸️ Helm chart

The chart in `chart/` deploys Papyrus on Kubernetes with two replicas, a PodDisruptionBudget and a generated API key. Install it from a checkout of the repository, with the image set to a released version:
<!-- todo: switch to oci://ghcr.io/axelered/charts once the chart is published on release -->

```shell
helm install papyrus ./chart --namespace papyrus --create-namespace --set image.tag=0.3.0
```

The install notes print the commands to read the key and reach the service. Server settings go under `config` in your values file, in the same format as `config.example.yml`. Set `networkPolicy.enabled: true` to block the pods from private and cloud metadata addresses, as a second layer behind the SSRF guard. `chart/values.yaml` documents every key.

Before you expose Papyrus to a network, read the [security checklist](https://docs.axelered.com/papyrus/security). For plain Docker, see [Docker setup](https://docs.axelered.com/papyrus/docker).

## 🤝 Support and contributing

Star the repository to follow releases. If you run Papyrus in production and need support, write to [oss@axelered.com](mailto:oss@axelered.com).

To report a vulnerability, see [SECURITY.md](SECURITY.md). To build and test Papyrus locally, see [CONTRIBUTING.md](CONTRIBUTING.md).

## ⚖️ License

Apache License 2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). Copyright Axelered D.o.o. and Axelered LLC-Fz.
