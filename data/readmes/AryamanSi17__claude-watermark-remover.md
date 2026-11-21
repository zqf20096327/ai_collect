# claude-watermark-remover

[![CI](https://github.com/AryamanSi17/claude-watermark-remover/actions/workflows/ci.yml/badge.svg)](https://github.com/AryamanSi17/claude-watermark-remover/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Stdlib-first tool for removing AI provenance marks from text and files —
MIT-licensed, Python 3.10+.

**[→ Website](https://aryamansi17.github.io/claude-watermark-remover/)**

The name is broad on purpose (discoverability), so read this section before
anything else: it draws the line between what this tool reliably does, what
it can only attempt, and what no tool anywhere can do.

## What this actually does

This project addresses **three distinct things** that "Claude watermark
removal" could mean. They are not interchangeable, and this tool's
guarantees are different for each.

> **1. Claude's text watermark (statistical word-choice pattern) — best-effort only, never certifiable.**
> Anthropic's [own documentation](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)
> describes a statistical pattern embedded in *which words* Claude selects at
> each step, keyed to a signature only Anthropic holds. Detecting or
> "proving removed" a keyed statistical watermark from outside the vendor is
> **cryptographically impossible, not just unimplemented** — there is no
> algorithm this tool (or anyone else's) can run without that key. What this
> tool offers here (Module 2, `mark_hygiene.rewrite`) is a best-effort
> rewrite that disrupts the statistical signal by editing a small,
> synonym-rich fraction of word choices. It is never guaranteed, never
> certifiable, and it costs you prose quality. Anyone selling "guaranteed"
> or "detector-proof" text-watermark removal is selling something that
> cannot exist.
>
> **2. C2PA file provenance on images/SVGs/PDFs — reliably and verifiably removed (with one documented exception).**
> Claude's file outputs (and most other AI image/document tools) can carry a
> [C2PA](https://c2pa.org/) manifest — Anthropic's own documentation is
> careful to call this **signed metadata, not a hidden watermark**: it's a
> visible, structured record (who/what/when), not a steganographic signal.
> This tool detects it by parsing the actual manifest box structure (not
> text-matching), and removes it deterministically for PNG, JPEG, WebP, and
> most PDF embeddings. The one exception, documented in detail below: a
> PDF's manifest can be stored as a file *attachment*, which this tool
> **detects reliably but does not remove** — a scope boundary (it would
> require a full PDF object-model library), not a backlog item, and not the
> same kind of limitation as Module 2's best-effort text disruption (see
> [PDF cleaning](#pdf-cleaning-exiftool--qpdf)).
>
> **3. Generic AI-tool invisible-character and metadata marks — reliably removed.**
> Zero-width characters, bidi-override tricks, tag-character steganography,
> and file metadata (EXIF/XMP/doc-properties) that various AI tools leave
> behind, independent of any specific vendor's watermark scheme. This is
> deterministic, testable, and has no cryptographic barrier — it's just
> byte-level cleanup, and this tool does it reliably (Layer A + file
> cleaners).

If you came here expecting a tool that strips Claude's text watermark and
lets you "prove" the text is clean: that tool cannot exist for anyone
outside Anthropic. Keep reading for what actually is on offer.

## Coverage matrix

| Channel | Reliable | Best-effort | Not addressed |
| --- | --- | --- | --- |
| Invisible Unicode / bidi / tag-character / exotic-space text carriers | **Yes** — Layer A, confidence-classified, unit-tested | — | — |
| C2PA manifest — PNG, JPEG, WebP | **Yes** — structural JUMBF/UUID validation, byte-diff-tested | — | — |
| C2PA manifest — PDF (XMP reference, Info-dict, AFRelationship marker) | **Yes** — via exiftool + qpdf structural rewrite | — | — |
| C2PA manifest — PDF stored as a file *attachment* | Detection only: **yes**, structural, deterministic | — | Removal — out of scope (needs a full PDF object-model library; a documented implementation boundary, not a planned feature) |
| File metadata (EXIF/XMP/doc-properties) — PDF, PNG, JPEG, WebP, DOCX, SVG, HTML, Markdown frontmatter | **Yes** | — | — |
| DOCX `customXml/*` parts | — | — | Out of scope entirely (not detected, not removed — no reliable signal, and removal risks breaking content-control bindings; see [Supported formats](#supported-formats)) |
| Claude's statistical text watermark | No — cryptographically impossible without the vendor key | Module 2 minimal-edit rewrite (implemented), disrupts but never certifies | Certifying removal against a vendor detector |
| Pixel-domain image watermarks (e.g. SynthID-class) | — | — | Out of scope for this project |

## Install

```bash
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
```

## Quickstart

```bash
# Text: invisible Unicode carriers (Layer A)
claude-watermark-remover inspect draft.md
claude-watermark-remover inspect draft.md --json
claude-watermark-remover clean draft.md -o draft.cleaned.md
claude-watermark-remover clean draft.md -o draft.cleaned.md --aggressive --strip-pua --stats

# Files: C2PA / EXIF / XMP / doc-properties (PDF, PNG, JPEG, WebP, DOCX, SVG, HTML, Markdown)
claude-watermark-remover inspect-file photo.png
claude-watermark-remover inspect-file photo.png --json
claude-watermark-remover clean-file photo.png -o photo.cleaned.png
claude-watermark-remover clean-file doc.pdf -o doc.cleaned.pdf --stats
claude-watermark-remover clean-file post.md -o post.cleaned.md --aggressive
```

`inspect`/`inspect-file` never modify a file and exit `1` if a
`confirmed`-confidence finding is present (useful as a CI gate). `clean`/
`clean-file` write atomically (temp file + rename) and refuse to write
through a symlinked destination. Binary files are refused by the text tools
unless `--force-text` is passed, so a `.docx`/`.png` never gets silently
decoded-and-corrupted as text.

## Confirmed / probable / informational

Every finding — text codepoint or file-metadata item — gets one of three
confidence tiers instead of a flat "strip it" rule:

| Confidence | Meaning | Default behavior |
| --- | --- | --- |
| `confirmed` | Near-zero legitimate use outside AI-tool marking (zero-width space, bidi override/isolate, invisible math operators, stray tag characters, validated C2PA manifests) | Removed |
| `probable` | Has real, legitimate non-AI uses too (LRM/RLM bidi hints, French NNBSP, a static-site generator's `generator:` frontmatter key, a PDF `/AFRelationship` marker without a validated stream) | Reported only — pass `--aggressive` to remove |
| `informational` | Never removed by default (PUA codepoints used by icon fonts) | Reported only — pass `--strip-pua` to opt into PUA removal specifically |

`probable` findings are **not** auto-stripped without `--aggressive` because
blanket-stripping every "exotic" signal produces false positives: legitimate
bidi text, French typography, documents pasted from word processors, and
ordinary CMS/static-site metadata all contain marks that overlap with AI
tooling's own artifacts. Splitting confidence tiers turns "did this tool
create a false positive" into something you can actually measure, instead
of something you have to take on faith.

## PDF cleaning: exiftool + qpdf

PDF metadata cleaning shells out to two external tools:

```bash
brew install exiftool qpdf   # or your platform's equivalent
```

**ExifTool alone is not enough, and this tool refuses to pretend otherwise.**
`exiftool -all=` edits PDFs *incrementally*: it frees the old `/Info` object
and drops it from the trailer, but the original metadata bytes remain
verbatim in the file body — recoverable, and exiftool itself can undo its
own edit with `-PDF-update:all=`. If `qpdf` isn't installed, this tool still
runs the exiftool pass but **reports the finding as still present, not
removed**, and prints a loud warning. Only `qpdf --linearize`'s structural
rewrite — which re-serializes the document from its object graph and drops
now-unreferenced objects — earns a `confirmed`/removed result.

**The one documented gap**: a C2PA manifest embedded in a PDF as a file
*attachment* (via `/AF` + `/AFRelationship /C2PA_Manifest`, per the actual
C2PA-in-PDF spec).

- **Detection: reliable and structural.** This tool parses the real JUMBF
  box structure and validates the manifest UUID inside the decompressed
  stream — the same deterministic check used for PNG/JPEG/WebP, not a
  text search.
- **Removal: out of scope for this cleaner.** Neither exiftool nor qpdf
  touches file attachments. Removing one correctly means resolving the
  PDF's object graph and cross-reference structure (including compressed
  xref/object streams, which is what modern PDF 2.0 writers — exactly the
  writers producing C2PA-attached files — use by default), then rebuilding
  it with the reference and the objects gone. That's most of what a real
  PDF library does, and this project has deliberately not taken it on, for
  the same reason SVG cleaning avoids a full XML parse-and-reserialize:
  a narrow implementation that only handles simple, uncompressed-xref PDFs
  would silently mishandle exactly the files this matters for — the
  quiet-failure-on-real-input outcome this project exists to avoid, not
  a smaller but honest version of the fix.

This is a **scope boundary, not signal uncertainty** — distinct from Module
2's best-effort text-watermark disruption. Detection here is exact and
testable; the limitation is purely "this cleaner doesn't do PDF object-graph
surgery," not "we're not sure the manifest is really gone."

**A concrete leak worth knowing about in standard tooling**: if you reach
for `qpdf --list-attachments` yourself to check a file, it will report **"has
no embedded files"** on a PDF that has a real C2PA manifest attached — qpdf's
attachment listing only walks the classic `/Names /EmbeddedFiles` tree, which
C2PA's `/AF`-based embedding doesn't use. This tool's own detection doesn't
have that blind spot, but qpdf's does, and it's worth knowing if you're
verifying PDFs by hand.

When this case is detected, `clean-file` leaves the attachment in place and
prints an explicit warning rather than silently under-delivering.

## Supported formats

| Format | What's removed | Mechanism |
| --- | --- | --- |
| PDF | XMP packet, Info-dict keys, C2PA XMP/AFRelationship references | exiftool + qpdf (see above) |
| PNG | `eXIf` chunk, validated `caBX` C2PA manifest, XMP `iTXt` | stdlib chunk parser |
| JPEG | `APP1` Exif/XMP, validated `APP11` C2PA manifest | stdlib segment parser; never touches scan/pixel data |
| WebP | `EXIF`/`XMP ` chunks, validated `C2PA` chunk | stdlib RIFF parser; fixes up the RIFF size field and `VP8X` flag bits |
| DOCX | AI-vendor-named `docProps/core.xml`/`app.xml` fields, AI-provenance `docProps/custom.xml` properties | targeted ZIP-member edits; `word/document.xml` (body) and `word/media/*` (embedded images) untouched |
| SVG | `<metadata>` blocks, standalone XMP packets | regex byte-span removal (not XML re-serialization, to guarantee untouched bytes stay untouched) |
| HTML | AI-named `<meta>` tags, AI-referencing JSON-LD blocks, `data-ai-*` attributes | regex byte-span removal, same rationale as SVG |
| Markdown | AI-provenance YAML frontmatter keys | frontmatter-only; body text untouched |

C2PA detection across PDF/PNG/JPEG/WebP validates the real
[JUMBF](https://www.iso.org/standard/73604.html) box structure and the
16-byte manifest Content Type UUID — not a text search for the string
`c2pa`. That distinction matters in both directions: a PDF's manifest is
usually zlib-compressed, so the literal bytes never appear at all, and a
same-named container (PNG's `caBX`, JPEG/WebP's `APP11`/`C2PA`) can
legitimately carry non-C2PA content, which a name-only check would
misreport as `confirmed`. **C2PA has no DOCX or HTML embedding profile**,
so that channel doesn't apply to either format — DOCX/HTML detection here
is value-level (does a field/attribute/JSON-LD block name a known AI
vendor?), the same kind of signal Markdown frontmatter uses, not a
structural manifest check.

### DOCX: `customXml/*` is out of scope, and it's a different kind of gap than PDF's

DOCX's `docProps/core.xml`, `app.xml`, and `custom.xml` are cleaned the same
way as everywhere else in this project — targeted, confidence-classified,
byte-diff-tested. `customXml/*` parts are **not scanned at all**, and this
is worth distinguishing carefully from the PDF file-attachment case above,
because the two look similar but aren't:

- **PDF's gap**: detection is reliable; only removal is out of reach (a
  scope boundary — no PDF object-model library).
- **DOCX's `customXml/*` gap**: there is no reliable detection signal to
  begin with. `customXml` payloads are typically business/regulatory
  content-control data with no C2PA-grade structural marker to check
  against; keyword-matching arbitrary XML for AI vendor names here is far
  noisier than the same check against a plain doc-property value — a
  business schema legitimately mentioning "OpenAI Corp" as a partner name
  is a realistic false positive. `customXml` parts can also be
  referentially bound to `<w:sdt>` content controls in the document body by
  item ID, so deleting one without rewriting those bindings risks
  corrupting the document.

Both are honestly reported as gaps; neither is claimed as "removed."
They're just gaps for different reasons — one is an implementation
boundary, the other is an absence of a trustworthy signal.

HTML has no equivalent gap: every pattern this tool removes from HTML (a
`<meta>` tag, a `data-ai-*` attribute, a whole JSON-LD `<script>` block) is
safe to delete outright — none of them are referentially bound to anything
else in the document.

## Limitations and honest expectations

- **Light editing does not remove a statistical text watermark.** The
  signal is spread across nearly every token choice in the text. Shuffling
  paragraphs, fixing typos, or swapping a few words moves it negligibly.
- **A rewrite strong enough to meaningfully disrupt it will degrade your
  prose.** It replaces the original model's word choices with the rewriting
  model's — tone, precision, and voice flatten. This raises the honest
  question: if the plan is to rewrite Claude's output with a weaker model
  anyway, why pay for Claude's drafting at all? Generating directly with
  the weaker model is simpler and produces a comparable or better result.
  Best-effort watermark disruption only makes sense when you specifically
  want Claude's drafting and are willing to trade some quality for hygiene
  — not as a shortcut to "clean" text.
- **No tool can certify a vendor's detector will fail.** Not this one, not
  anyone else's. Any claim to the contrary about a keyed statistical
  watermark is a claim about a system the claimant doesn't control.
- **Text-watermark removal is unprovable by design**, not by omission. A
  keyless world has no way to confirm a keyed signal's absence — that's the
  entire point of keying it. This tool reports what it changed; it cannot
  report what a detector it has never seen would conclude.

## Module 2: statistical-watermark disruption (best-effort)

```bash
claude-watermark-remover rewrite draft.md                          # print-prompt (default): no model, no network
claude-watermark-remover rewrite draft.md --backend ollama --model llama3.2
claude-watermark-remover rewrite draft.md --backend openai-compatible --model gpt-4o-mini --json
```

`mark_hygiene.rewrite` is a deliberately separate package from the Layer A
text scrub and the file cleaners above — it's a different kind of tool
(model-dependent, best-effort) and the code keeps that boundary structural,
not just documented.

**What it selects, and why it's a proxy, not the watermark itself.** The
tool identifies word positions that are *synonym-rich* — spots with several
near-equivalent phrasings — and edits only those, leaving factual tokens,
named entities, numbers, code, and quoted material untouched by
construction. **Synonym-richness correlates with but is not identical to
where a watermark signal actually lives** (the model's true high-entropy
sampling positions, locatable only with the vendor's key). This tool edits
where substitution is *safe*, as a proxy for where the watermark *likely*
is — it cannot verify that overlap. Selection is a heuristic proxy, not
real model logprobs: the default backend queries no model at all, and even
chat-style Ollama/OpenAI-compatible endpoints don't reliably expose
per-position logprobs, so selection is a deterministic, backend-agnostic
text heuristic (closed-class stopword exclusion, protected-span masking
for code/quotes/URLs, and a cheap suffix-morphology proxy for
adverb/adjective-shaped words) — testable with zero model access, and
identical regardless of which backend eventually fills in the edits. By
default it targets roughly one word in eight (`--edit-fraction 0.12`);
this is a minimal-edit tool, not a paraphraser.

**Objective and candidate selection.** The backend generates N candidate
rewrites; each is scored by bigram-Jaccard divergence from the original
(how much local token-choice sequencing changed) and the highest-scoring
candidate *within a drift budget* is kept — a length-drift guard plus a
similarity floor. **The similarity floor is heuristic (word-overlap
based), not embedding-based** — this project ships no embedding model by
default, so it's a guard against gross deviation, not a proof of
meaning preservation. If no candidate clears the budget, the text is
returned unchanged rather than accepting an over-drifted rewrite.

**Backends**: `print-prompt` (default — no model, prints the constructed
prompt for you to run elsewhere), `ollama` (local, default
`http://127.0.0.1:11434`), `openai-compatible` (API key from the
`MARK_HYGIENE_REWRITE_API_KEY` environment variable only, never a CLI
flag). Both network backends refuse redirects outright (they use
`http.client` directly, which has no follow-redirect logic to begin with —
an `Authorization` header can't be replayed to a host you didn't intend),
and refuse non-loopback endpoints unless `--allow-remote` is passed.

**Default to a non-origin model.** If the configured model name suggests
it shares a vendor with Claude (contains `claude`/`anthropic`), the tool
warns explicitly: rewriting Claude-produced text with a Claude-family model
risks re-stamping the same or a related watermark scheme rather than
disrupting it.

**The report never claims removal.** Every `RewriteReport` carries a fixed
disclaimer and reports only factual, measured quantities — fraction of
tokens selected/changed, divergence achieved, whether the drift budget was
satisfied. It never says "watermark removed," "detector will fail," or
anything read as a certification, because none of that is true regardless
of the numbers.

## Intended use

This is for **privacy and hygiene on content you own or are authorized to
process** — removing incidental provenance metadata and invisible-character
artifacts before you reuse or republish your own work. It is explicitly
**not** for:

- Academic or professional fraud — passing AI-generated work off as your
  own where authorship matters.
- Passing AI-generated text off as human-written where that distinction is
  material to the reader.
- Evading transparency obligations under the EU AI Act (Article 50),
  provider disclosure requirements, platform policies, or any other
  regulation or agreement requiring AI-origin disclosure.

If the content's AI origin is a fact you're obligated to disclose to a
reader, platform, or regulator, this tool does not change that obligation —
it only changes incidental metadata and invisible characters, and (via
Module 2) makes a best-effort, quality-costing, never-certified attempt at
a statistical signal it cannot prove is gone.

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the
ground rules (stdlib-only, fixtures-first, confidence-tier discipline) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Security issues: see
[SECURITY.md](SECURITY.md) rather than a public issue.
[`CLAUDE.md`](CLAUDE.md) has orientation notes if you're working in this
repo with an AI coding agent.

## License

MIT — see [LICENSE](LICENSE).
