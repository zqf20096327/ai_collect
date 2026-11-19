<h1 align="center">Somali-Tokenizer</h1>

<p align="center">
  <strong>A research-grade subword tokenizer for the Somali language, implemented in Rust.</strong><br>
  <em>Qalab kala-jaridda qoraalka Soomaaliga oo loogu talagalay moodallada luqadda.</em>
</p>

<p align="center">
  ByteLevel BPE · lossless round-trip · reproducible releases · Somast
</p>

---

> **Project status: implemented, not yet released.** The Rust library, CLI, and Python
> package are built and tested against the Python reference (`python-reference/`): same
> token ids, same trained vocabulary and merges, same benchmark metrics on the fixture
> corpus. The full-corpus figures quoted below were measured by the Python reference; they
> have not been re-measured by the Rust implementation yet. Nothing is published to
> crates.io or PyPI yet. The v2 artifact is on the Hugging Face Hub as
> [`somast/somali-tokenizer`](https://huggingface.co/somast/somali-tokenizer).

## Quick start

Python:

```bash
pip install somali-tokenizer        # once published; until then, see "Building" below
```

```python
from somali_tokenizer import SomaliTokenizer

tokenizer = SomaliTokenizer.v2()                     # bundled, works offline
# tokenizer = SomaliTokenizer.from_pretrained()      # from the Hub: somast/somali-tokenizer
encoding = tokenizer.encode("Soomaaliya waa dal ku yaal Geeska Afrika.")
encoding.ids       # [5446, 406, 785, 305, 1627, 4235, 1454, 29]
encoding.tokens    # ['Soomaaliya', 'Ġwaa', 'Ġdal', 'Ġku', 'Ġyaal', 'ĠGeeska', 'ĠAfrika', '.']
tokenizer.decode(encoding.ids)                       # the original text, exactly
```

The artifact is a standard `tokenizer.json`, so `transformers` loads it unchanged and gives
the same ids:

```python
from transformers import AutoTokenizer
AutoTokenizer.from_pretrained("somast/somali-tokenizer")
```

Rust:

```rust
use somali_tokenizer::SomaliTokenizer;

let tokenizer = SomaliTokenizer::v2()?;
let ids = tokenizer.encode("Soomaaliya waa dal.")?.ids;   // [5446, 406, 785, 29]
```

Command line:

```bash
cargo install --path crates/somali-tokenizer
somali-tokenizer encode "Soomaaliya waa dal."             # 5446 406 785 29
somali-tokenizer decode 5446 406 785 29
somali-tokenizer train --corpus data/final/final_so.jsonl   # streams a corpus release
somali-tokenizer benchmark --eval data/final/final_so.jsonl
somali-tokenizer stats --corpus data/final/final_so.jsonl
```

Details: [crates/somali-tokenizer/README.md](crates/somali-tokenizer/README.md) (Rust and
CLI) and [bindings/python/README.md](bindings/python/README.md) (Python).

## What this project is

Somali-Tokenizer will be a Rust library and command-line tool for **training, evaluating,
and shipping learned subword tokenizers for Somali**: the vocabulary and merge rules that
sit between raw Somali text and a language model.

It covers exactly one job: subword tokenization for language models and related NLP
systems. It is deliberately not a general Somali NLP toolkit.

## Why a Somali-specific tokenizer

A language model sees tokens, not characters. Its context window, its training cost, and
its per-request inference cost are all denominated in tokens. When a tokenizer was fitted
mostly to other languages, Somali text is split into more, smaller pieces:

```text
fixed context window
      │
      │ more tokens per Somali word
      ▼
less Somali text fits in the same window
      │
      ▼
more compute per unit of Somali content
```

On a held-out Somali evaluation set, the reference 48k Somali tokenizer needs about
**1.35** tokens per whitespace-delimited word, against **1.82** for XLM-RoBERTa-base and
**2.63** for BERT-base-uncased. On the same text, that is roughly 1.35x less fragmentation
than XLM-R and 1.94x less than BERT.

Two honest caveats, stated once here and repeated in the technical docs:

1. **Fewer tokens per word is not the same as a better model.** Tokenizer efficiency and
   downstream model quality are related but separately measured questions. Nothing in this
   repository measures downstream accuracy, and no claim about it is made.
2. **"Word" here means whitespace-delimited span.** That is the benchmark's operational
   definition, not a linguistic claim about Somali morphology. Bytes-per-token is reported
   alongside as a definition-free compression measure.

## Where this sits in the Somast Somali NLP ecosystem

```text
Somali NLP Corpus (somastllc/somali-nlp-corpus)
      │
      │ training / evaluation text (versioned corpus releases)
      ▼
Somali-Tokenizer
      │
      │ tokenizer artifacts (vocabulary + merge rules + config)
      ▼
LLMs / NLP systems
```

Separately:

```text
SomLTK
  → general-purpose Somali language processing
    (word and sentence segmentation, stemming, POS tagging, and similar)
```

| Repository | Owns |
|------------|------|
| [Somali NLP Corpus](https://github.com/somastllc/somali-nlp-corpus) | Corpus collection, cleaning, deduplication, releases |
| **Somali-Tokenizer** | Learned subword tokenization: training, encoding, decoding, benchmarking, release |
| SomLTK | General Somali NLP: linguistic word/sentence tools, morphology, tagging |

Rules of thumb for what belongs here: if it learns a vocabulary from a corpus, or encodes
and decodes text for a model, it belongs in Somali-Tokenizer. If it is a rule-based or
linguistic language tool, it belongs in SomLTK. If it produces or cleans text, it belongs
in Somali NLP Corpus.

## Reference tokenizer

The released tokenizer, **Somali ByteLevel BPE v2**, which the Rust implementation
reproduces exactly:

| Property | Value |
|----------|-------|
| Algorithm | Byte Pair Encoding (BPE) |
| Vocabulary | 48,000 (including special tokens and the byte alphabet) |
| Minimum merge frequency | 2 |
| Normalizer | Unicode NFC |
| Pre-tokenizer | ByteLevel (`add_prefix_space = false`) |
| Decoder | ByteLevel |
| Post-processor | ByteLevel (`trim_offsets = true`) |
| Initial alphabet | All 256 bytes |
| Unknown token | None; byte coverage makes one unreachable |

The design intent, and the reason for each choice, is in
[docs/TOKENIZER_DESIGN.md](docs/TOKENIZER_DESIGN.md).

## Benchmark against general-purpose tokenizers

On **FLORES-200 Somali** (2,009 sentences), the same text costs GPT-4o 1.44× as many
tokens and GPT-4 1.86× as many, with a vocabulary 2 to 5 times smaller than theirs:

| Tokenizer | Vocabulary | Tokens per word | Tokens vs this |
|---|---:|---:|---:|
| **somast-bpe-v2 (this)** | **48,000** | **1.374** | **1.00×** |
| nllb-200 | 256,204 | 1.818 | 1.32× |
| xlm-roberta | 250,002 | 1.827 | 1.33× |
| o200k_base (GPT-4o) | 200,019 | 1.975 | 1.44× |
| gemma2 | 256,000 | 2.241 | 1.63× |
| llama3-8b | 128,256 | 2.527 | 1.84× |
| cl100k_base (GPT-4) | 100,277 | 2.552 | 1.86× |
| qwen2.5 | 151,665 | 2.568 | 1.87× |

Three in four Somali words are a single token here (75.2%), against 23.4% on Llama 3. One
sentence, *Caafimaadka carruurtu waa mudnaanteenna koowaad* ("Children's health is our
first priority"):

```text
this tokenizer   7  Caafimaadka · carruurtu · waa · mudnaan · teenna · koowaad · .
GPT-4o          16  Ca · afima · adka · carr · u · urt · u · waa · mud · na · ante · enna · ko · owa · ad · .
GPT-4, Llama 3  19  Ca · af · ima · ad · ka · carr · u · urt · u · w · aa · mud · na · ante · enna · ko · owa · ad · .
```

A second test set, 2,000 Somali Wikipedia paragraphs, gives the same order (1.505 tokens
per word, against 2.060 for GPT-4o and 2.632 for GPT-4). Full tables, method, and caveats:
[docs/BENCHMARKING.md](docs/BENCHMARKING.md#against-general-purpose-tokenizers-flores-200-somali-wikipedia)
and the report
[docs/benchmarks/somast-somali-tokenizer-benchmark.pdf](docs/benchmarks/somast-somali-tokenizer-benchmark.pdf).

## Benchmark baseline (corpus holdout)

Measured by the Python reference implementation on a held-out evaluation set of
**49,424 documents / 4,933,796 words**, excluded from training:

| Metric | Somali ByteLevel BPE v2 (48k) |
|--------|------------------------------:|
| Mean tokens per word | 1.3528 |
| Median tokens per word | 1.2857 |
| P95 tokens per word | 1.8571 |
| Corpus-level tokens per word | 1.3763 |
| Bytes per token | 4.8069 |
| Round-trip fidelity | 100% |
| Documents emitting an unknown token | 0 |

Comparison tokenizers scored on the identical documents: XLM-RoBERTa-base 1.8233 mean
tokens/word, BERT-base-uncased 2.6291. These isolate tokenizer fragmentation only.

Mean tokens per word (1.3528) and corpus-level tokens per word (1.3763) differ because the
first averages per-document ratios and the second divides total tokens by total words; the
distinction is explained in [docs/BENCHMARKING.md](docs/BENCHMARKING.md).

On the fixture corpus, the Rust benchmark and statistics commands reproduce the Python
reference's numbers, and Rust training reproduces its vocabulary and merges exactly. A
full-corpus re-run is still to be done. See [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md).

## Capabilities

- Train ByteLevel BPE tokenizers on a versioned Somali NLP Corpus release, streaming, without
  loading the corpus into memory
- Encode and decode with an exact round-trip guarantee: `decode(encode(x)) == NFC(x)`
- Benchmark tokenizers on a held-out split: tokens per word, bytes per token, round-trip
  fidelity, unknown-token rate, per-source breakdown
- Run vocabulary-size sweeps and report the compression/parameter trade-off
- Use the standard Hugging Face `tokenizer.json`, so artifacts load in `transformers`
  without a bespoke loader
- Ship as a Rust library, a CLI, and a Python package
- Planned: publish versioned releases to crates.io and PyPI, and a Rust export command for
  the `transformers` companion files

## Architecture at a glance

```text
CLI
 ↓
application layer (experiment orchestration, config, reporting)
 ↓
tokenizer · training · benchmarking
 ↓
Hugging Face `tokenizers` Rust crate
 ↓
filesystem / corpus
```

It builds on the `tokenizers` Rust crate (pinned to 0.21.4, the version the reference used)
rather than reimplementing BPE, so the Rust implementation differs from the reference in as
few dimensions as possible. The reasoning, and the conditions under which that would change,
are in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Documentation

| Document | Contents |
|----------|----------|
| [PLAN.md](PLAN.md) | Phase-by-phase execution plan with acceptance criteria |
| [ROADMAP.md](ROADMAP.md) | Release direction, v0.1 through v1.0, and future research |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Intended module structure and dependency direction |
| [docs/TOKENIZER_DESIGN.md](docs/TOKENIZER_DESIGN.md) | Tokenizer specification, design rationale, invariants |
| [docs/TRAINING.md](docs/TRAINING.md) | Corpus handling, splits, and the training procedure |
| [docs/BENCHMARKING.md](docs/BENCHMARKING.md) | Metric definitions and the evaluation protocol |
| [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) | Run metadata, versioning, and artifact identity |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Rust conventions, toolchain, and dependency policy |
| [docs/FINAL_REVIEW.md](docs/FINAL_REVIEW.md) | Phase 1 completion checklist and status |
| [configs/bpe_48k.example.toml](configs/bpe_48k.example.toml) | Example experiment configuration |
| [python-reference/](python-reference/) | The Python reference implementation and its technical note (`PAPER.md`) |

## Repository layout

```text
crates/somali-tokenizer/   Rust library and CLI
bindings/python/           Python package (PyO3 + maturin)
artifacts/releases/        released tokenizer artifacts, with SHA256SUMS
python-reference/          Python reference implementation, with its Git history
tests/fixtures/            parity fixtures shared by the Rust and Python test suites
configs/  docs/            experiment configuration and documentation
```

## Building

```bash
cargo test                                  # Rust library, CLI, parity suite
cd bindings/python && uv venv && . .venv/bin/activate
uv pip install maturin pytest transformers
maturin develop && pytest                   # Python package
```

## Development status

| Area | Status |
|------|--------|
| Specification and documentation | Done |
| Rust library, CLI, training, benchmarking | Done, tested against the reference |
| Python package | Done, tested against the reference and `transformers` |
| Full-corpus parity report | Not done yet |
| Rust export of the `transformers` companion files | Not done yet |
| Published releases (crates.io, PyPI) | Not done yet |

See [PLAN.md](PLAN.md) for the phase-by-phase status.

## Known limitations

Stated up front because they shape how the numbers above should be read:

1. Training text is dominated by web crawl.
2. Latin-script Somali dominates the corpus; Arabic-script Somali is out of distribution.
3. "Word" means whitespace-delimited span.
4. Tokenizer compression efficiency is not downstream model accuracy.
5. Comparisons against BERT and XLM-R isolate fragmentation, not model quality.
6. Corpus composition materially affects which merges are learned.
7. A future, more balanced corpus may move the best vocabulary size.

Each is expanded in [docs/BENCHMARKING.md](docs/BENCHMARKING.md) and
[docs/TOKENIZER_DESIGN.md](docs/TOKENIZER_DESIGN.md).

## Contributing

Bug reports, parity findings, and Somali-language evaluation data are especially welcome.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).

Corpus data is **not** covered by this license. Somali NLP Corpus carries per-record upstream
licenses and no single corpus-wide license; anyone training on it is responsible for the
terms of each source.
