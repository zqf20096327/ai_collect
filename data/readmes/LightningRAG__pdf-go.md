# pdf-go

**[简体中文说明 → README_zh.md](README_zh.md)**

**pdf-go** is a **pure Go** library for **reading and writing PDF** documents. Import path: **`github.com/lightningrag/pdf-go/pdf`**.

- **Go 1.20+**
- **Standard library only** at runtime (no third-party runtime dependencies)
- **ISO 32000–oriented** APIs for common document, page, stream, and writer workflows

Full API notes: **[`docs/API.md`](docs/API.md)**. Design notes: **[`DESIGN.md`](DESIGN.md)**.

---

## Features (high level)

| Area | What you can do |
|------|------------------|
| **Open & parse** | `OpenFile`, `NewPdfReader` (seekable streams); xref / trailer / catalog; object lookup; stream decode (Flate, LZW, ASCIIHex/85, RunLength, pass-through image filters, PNG predictors) |
| **Pages** | Flattened page list, `Page(i)`, page boxes (`MediaBox`, `CropBox`, …), rotation, resources, annotations, links |
| **Text** | `ExtractText()` (lightweight heuristic) and `ExtractTextAdvanced()` (ToUnicode / CMap / Form XObject paths, options) |
| **Document info** | Trailer `/Info`, metadata helpers, XMP bytes, outlines, page labels, named destinations, embedded files |
| **Encryption (metadata)** | Detect `/Encrypt`, optional open policy (`RejectEncrypted` vs `AllowEncryptedOpen`); **no password decryption** of content |
| **Write & merge** | `PdfWriter`: add/insert/remove pages, append pages from a reader, merge documents, catalog fields, attachments, outlines, forms helpers, content merge/transform utilities |
| **Low-level** | `pdf/generic` types (`Dict`, `Array`, `Stream`, …), filter helpers under **`pdf/filters`** |

**Not in scope today:** full crypto (RC4/AES decrypt), raster image decode to pixels, incremental updates/signatures, layout engine–grade text extraction. See **`docs/API.md` → Scope**.

---

## Install

```bash
go get github.com/lightningrag/pdf-go/pdf
```

In your module:

```go
import "github.com/lightningrag/pdf-go/pdf"
```

---

## Quick start (`ExtractTextAdvanced`, like `examples/readtextadvanced`)

```go
package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/lightningrag/pdf-go/pdf"
)

func main() {
	r, err := pdf.OpenFile("document.pdf", false)
	if err != nil {
		log.Fatal(err)
	}
	n, err := r.NumPages()
	if err != nil {
		log.Fatal(err)
	}

	opts := pdf.ExtractTextOptions{}
	for i := 0; i < n; i++ {
		p, err := r.Page(i)
		if err != nil {
			log.Fatalf("page %d: %v", i, err)
		}
		txt, err := p.ExtractTextAdvanced(opts)
		if err != nil {
			fmt.Printf("--- page %d ---\n(error: %v)\n\n", i, err)
			continue
		}
		body := strings.TrimSpace(txt)
		if body == "" {
			body = "(empty)"
		}
		fmt.Printf("--- page %d ---\n%s\n\n", i, body)
	}
}
```

Encrypted PDFs: by default **`OpenFile`** returns **`pdf.ErrEncrypted`** when the trailer contains **`/Encrypt`**. Use **`OpenFileWithPolicy`** with **`pdf.AllowEncryptedOpen`** only if you need structural inspection without decrypting streams. Details: **`docs/API.md`**.

---

## CLI in this repository

The repo root includes a tiny demo that prints page count and library version:

```bash
go run . ./assets/example.pdf
```

---

## Examples

Runnable programs live under **`examples/`** (inspect, read text, merge, outlines, links, docinfo, encrypt check, page ranges, etc.). Run them from the **repository root** so **`assets/example.pdf`** resolves.

```bash
go run ./examples/inspect
go run ./examples/readtext
go run ./examples/readtextadvanced
```

See **[`examples/README.md`](examples/README.md)** for every command, flags, and the optional **`PDF_GO_EXAMPLE`** environment variable.

---

## Documentation layout

| Path | Purpose |
|------|---------|
| [`docs/API.md`](docs/API.md) | API overview, `ExtractText` vs `ExtractTextAdvanced`, writer rules, errors |
| [`docs/TESTING.md`](docs/TESTING.md) | Optional corpus / manifest notes (if you add external fixtures) |
| [`docs/SAMPLE_FILES_TESTING.md`](docs/SAMPLE_FILES_TESTING.md) | Manifest-driven sample-file testing notes |
| [`DESIGN.md`](DESIGN.md) | Design and implementation notes |

---

## Repository layout (short)

```
pdf/           # library package (import github.com/lightningrag/pdf-go/pdf)
pdf/filters/   # stream filters
pdf/generic/   # PDF object model and syntax helpers
examples/      # example programs
docs/          # human-readable API and testing notes
assets/        # sample PDF for examples
main.go        # minimal CLI demo at repo root
```

---

## Contributing & support

Issues and PRs are welcome on the upstream GitHub project. When reporting bugs, attach a **minimal PDF** (or describe generator + version) and the **Go code** that reproduces the issue.
