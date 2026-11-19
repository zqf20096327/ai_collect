# kalkan 🛡️

**English** · [Türkçe](README.tr.md)

[![test](https://github.com/CelkMehmett/kalkan/actions/workflows/ci.yml/badge.svg)](https://github.com/CelkMehmett/kalkan/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/kalkan.svg)](https://crates.io/crates/kalkan)
[![PyPI](https://img.shields.io/pypi/v/kalkan.svg)](https://pypi.org/project/kalkan/)
[![docs.rs](https://img.shields.io/docsrs/kalkan)](https://docs.rs/kalkan)
[![license](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#contributing-and-license)

**A PII shield for Turkish text: masks personal data before it reaches an LLM and restores it in the reply.**
Built for KVKK (Turkey's data protection law, the local counterpart of GDPR). Written in Rust;
the same engine runs in Rust, Python (`pip install kalkan`) and the browser (WebAssembly) with
identical results.

```text
User         : Ben Ayşe Kaya, TC 10000000146. İadeyi TR33 0006 1005 1978 6457 8413 26 hesabıma yapın.
Sent to LLM  : Ben [AD_SOYAD_1], TC [TCKN_1]. İadeyi [IBAN_1] hesabıma yapın.
LLM reply    : Merhaba [AD_SOYAD_1], iadeniz [IBAN_1] hesabına yapılacak.
Shown to user: Merhaba Ayşe Kaya, iadeniz TR33 0006 1005 1978 6457 8413 26 hesabına yapılacak.
```

**Live demo:** [celkmehmett.github.io/kalkan](https://celkmehmett.github.io/kalkan/). Masking
happens entirely in your browser; no data leaves the page. The demo loads no external fonts,
CDNs or analytics.

## Contents

- [Why?](#why)
- [Features](#features)
- [Installation](#installation)
- [Python](#python)
- [Rust](#rust)
- [Integrations: OpenAI, LiteLLM, LangChain](#integrations)
- [Browser (WebAssembly)](#browser-webassembly)
- [Strategies](#strategies)
- [Command line](#command-line)
- [API contract](#api-contract)
- [Benchmarks](#benchmarks)
- [Security model](#security-model)
- [Limitations](#limitations)
- [Testing](#testing)
- [Contributing and license](#contributing-and-license)

## Why?

Companies want to use ChatGPT, Claude or Gemini, but sending a customer's national ID number,
IBAN or phone number to a server abroad is a KVKK/GDPR risk. General-purpose PII tools are
mostly English-centric: they don't know Turkish ID checksums, Turkish phone formats, Turkish
suffixes (`Yılmaz'ın`) or the dotted/dotless `İ/ı`. `kalkan` replaces this data with placeholders
before the request leaves, and puts the real values back when the reply arrives.

kalkan is not a product but an **embeddable engine**: put it inside your own LLM gateway, Python
service, browser extension or batch anonymization job.

## Features

| | |
|---|---|
| **14 entity types** | Turkish ID (TCKN), tax ID (VKN), IBAN, phone, card, e-mail, licence plate, person name, postal address, social-security (SGK) number, IP, date of birth, passport, custom terms |
| **Checksum validation** | TCKN, VKN, IBAN (mod-97), card (Luhn); dates, prices, order numbers and version strings are not flagged |
| **Restore** | Per-session vault; different spellings of the same value get the same token |
| **Streaming** | Restores correctly even when a placeholder is split across chunks (`"[TC"` + `"KN_1]"`) |
| **Fake but valid** | `Synthetic` mode emits checksum-valid fake TCKN/IBAN/cards and documentation-range IPs |
| **Leak audit** | Detects new PII produced by the model and hallucinated placeholders |
| **Custom terms** | Customer, project and product names; Turkish-aware case folding (`IŞIK` ↔ `ışık`) |
| **Turkish-aware** | `Yılmaz'ın` → only the name is masked, the suffix `'ın` stays |
| **Zero dependencies** | Core has no `unsafe`; the C ABI is only enabled with the `ffi` feature |

## Installation

| Target | Install | Note |
|---|---|---|
| Rust | `cargo add kalkan` | MSRV 1.82; dependency-free core |
| Python | `pip install kalkan` | CPython ≥ 3.9, abi3 wheels |
| CLI | `cargo install kalkan` | `mask`, `detect`, `audit`, `restore` |
| Browser | `wasm/build.sh` → `wasm/dist/index.html` | Single-file demo |

From source:

```bash
git clone https://github.com/CelkMehmett/kalkan kalkan && cd kalkan
cargo test --workspace --exclude kalkan-py
```

### Detected entity types

Labels are Turkish because they appear in prompts sent to the LLM; the meaning is given below.

| Type | Label | How |
|---|---|---|
| Turkish national ID | `TCKN` | Two check digits; fake patterns such as `11111111110` are rejected |
| Tax ID | `VKN` | Revenue Administration checksum **and** a nearby "vergi/VKN" keyword |
| IBAN | `IBAN` | TR + 24 digits, mod-97; spaced or contiguous |
| Phone | `TELEFON` | Mobile, landline, 0850/0800; `+90`, `0090`, `(0532)`, `532.123.45.67` |
| Card | `KART` | Luhn + card network prefix |
| E-mail | `EPOSTA` | Structural check |
| Licence plate | `PLAKA` | Province code 01–81, letter/digit rules; units like `12 TL 500` get low confidence |
| Person name | `AD_SOYAD` | Titles (`Sayın`, `Prof. Dr.`), honorifics (`Bey`, `Hanım`), form labels (`Ad Soyad:`), common-name dictionary |
| IP | `IP` | IPv4 (octet ≤ 255) and IPv6; times (`14:30:00`), MACs and versions are rejected |
| Date of birth | `DOGUM_TARIHI` | `05.03.1990`, `1990-03-05`, `5 Mart 1990`; only with "doğum" context, calendar-validated |
| Passport | `PASAPORT` | Letter + 7–8 digits, only with "pasaport" context |
| Postal address | `ADRES` | Neighbourhood/street anchor (`Mah.`, `Cad.`, `Sok.`, `Blv.`) preceded by a name or number, plus `No:`, floor/flat, postal code, `District/Province`; a bare street name (`Bağdat Caddesi`) is not masked |
| SGK number | `SGK` | 6–13 digits, only with "SGK/SSK/Bağ-Kur" context; a valid TCKN stays `TCKN` |
| Custom term | `OZEL` | Your own list |

## Python

```python
import kalkan

k = kalkan.Kalkan(terms=["Proje Atlas"])
s = k.session()                        # one session per conversation

prompt = s.mask("Ayşe Kaya Hanım, TC 10000000146, Proje Atlas bütçesi")
# "[AD_SOYAD_1] Hanım, TC [TCKN_1], [OZEL_1] bütçesi"

reply = llm(prompt)
report = s.audit(reply)                # did the model produce new PII?
if not report:
    log.warning(report)
print(s.restore(reply))

# Streaming
stream = s.stream()
for chunk in llm_stream(prompt):
    send(stream.push(chunk))
send(stream.finish())

# Batch anonymization: all cores, GIL released
clean = kalkan.Kalkan(strategy="label").mask_batch(millions_of_records)
```

`start`/`end` in `detect()` results are character indices: `text[e.start:e.end]` works directly.
The vault is available as a dict via `s.vault` and can be loaded in another process with `import_vault`.

## Rust

```rust
use kalkan::{Kalkan, Strategy};

let kalkan = Kalkan::builder()
    .strategy(Strategy::Token)
    .terms(["Proje Atlas"])
    .build();
let mut session = kalkan.session();

let prompt = session.mask("Müşteri TC 10000000146, tel 0532 123 45 67");
// "Müşteri TC [TCKN_1], tel [TELEFON_1]"

let reply = call_llm(&prompt);
assert!(session.audit(&reply).is_clean());
let for_user = session.restore(&reply);

// Streaming: StreamRestorer is independent of the session and can move to another task.
let mut stream = session.stream();
for chunk in llm_stream { send(&stream.push(&chunk)); }
send(&stream.finish());
```

Runnable example: `cargo run --example llm_akisi`

## Integrations

Ready-made adapters mask the prompt and restore the reply (including streaming, with
placeholders split across chunks) so you don't have to wire sessions yourself. Every call gets
its own session; the vault stays in process memory.

**OpenAI-style messages (no dependencies)** — works with the OpenAI SDK or any `messages` list:

```python
from kalkan.messages import mask_messages

s = kalkan.Kalkan().session()
reply = client.chat.completions.create(model="gpt-4o", messages=mask_messages(s, messages))
print(s.restore(reply.choices[0].message.content))
```

Text parts and tool-call arguments are handled; arguments are parsed as JSON so restored values
never break the JSON.

**LiteLLM** (`pip install "kalkan[litellm]"`) — drop-in for `litellm.completion`/`acompletion`:

```python
from kalkan.integrations.litellm import completion

r = completion(model="gpt-4o", messages=[{"role": "user", "content": "TC 10000000146"}])
for chunk in completion(model="gpt-4o", messages=..., stream=True): ...
```

or as a **LiteLLM Proxy guardrail** in `config.yaml`, protecting every app behind the gateway:

```yaml
guardrails:
  - guardrail_name: kalkan
    litellm_params:
      guardrail: kalkan.integrations.litellm.KalkanGuardrail
      mode: [pre_call, post_call]
      default_on: true
      # optional: strategy, terms, kinds, exclude, min_confidence
```

The vault is never written to request metadata or LiteLLM logs (only an opaque id is). Note that
with `--detailed_debug` the proxy itself logs the incoming request before guardrails run.

**LangChain** (`pip install "kalkan[langchain]"`) — wraps any Runnable or chat model:

```python
from kalkan.integrations.langchain import with_kalkan

model = with_kalkan(ChatOpenAI(model="gpt-4o"), on_leak=lambda report: log.warning(report))
chain = prompt | model | StrOutputParser()
chain.invoke({"question": "Ben Ayşe Kaya, TC 10000000146 ..."})
```

`invoke`, `ainvoke`, `stream` and `astream` are supported; tool-call arguments are restored too.
`on_leak` is called with the `audit` report if the model produces new personal data.
Tested with LiteLLM 1.110 (SDK and a real proxy) and langchain-core 1.7.

## Browser (WebAssembly)

```js
import { kalkanYukle } from "./kalkan.js";
const engine = await kalkanYukle("./kalkan.wasm");
const session = engine.oturum({ strateji: "token", terimler: ["Proje Atlas"] });
session.maskele("TC 10000000146");       // "TC [TCKN_1]"
session.tespit(text);                    // offsets are JS string indices (correct for emoji)
const stream = session.akis();           // streaming restorer
```

Build and single-file demo: `./wasm/build.sh` → `wasm/dist/index.html`.
`.github/workflows/demo.yml` does this on every push to `main` and publishes to GitHub Pages.

## Strategies

| Strategy | `10000000146` → | Restorable? | When |
|---|---|---|---|
| `Token` (default) | `[TCKN_1]` | Yes | General use |
| `Synthetic` | `91176921220` (valid fake) | Yes | Tool calls that validate formats, realistic test data |
| `Partial` | `*********46` | No | Logs, screenshots |
| `Label` | `[TCKN]` | No | Training-data anonymization |

## Command line

```bash
cargo install --path .

kalkan detect < document.txt
kalkan mask -s partial -t "Proje Atlas,Acme Holding" < document.txt
kalkan mask -v vault.tsv < prompt.txt | llm-cli > reply.txt
kalkan audit -v vault.tsv < reply.txt      # exit code 1 if anything is found
kalkan restore -v vault.tsv < reply.txt
```

## API contract

| Layer | `start`/`end` unit | Vault transport |
|---|---|---|
| Rust (`Match.span`), CLI (`detect --json`) | **bytes** (always on a UTF-8 boundary) | `Session::vault` / `import_vault` |
| Python (`Entity.start/end`) | **characters** (matches Python slicing) | `session.vault` dict |
| WASM/JS (`tespit()`) | **UTF-16 code units** (matches `String.slice`) | `kasa()` object |

Don't mix the three units: `&text[m.span]` works in Rust, `text[e.start:e.end]` in Python and
`text.slice(e.start, e.end)` in JS. Never pass byte offsets to a JS or Python string.

A `Session` vault is **single-use**: open a new session for every conversation/request.
Different spellings of the same value get the same placeholder and are restored with the first
spelling seen. Call `audit` on the raw LLM reply, then `restore`/`stream`.

## Benchmarks

A 5 MB corpus of 11,617 synthetic Turkish customer-support messages (generated by
`bench/gen_corpus.py`, with known gold labels). Compared against
[kvkk-pii](https://pypi.org/project/kvkk-pii/) using **only its regex layer** (no model; a
person-name rule was added for fairness). Machine: 2-core Intel Xeon 2.1 GHz VM. The 12 kalkan
types of v0.2 enabled (the address and SGK detectors added in v0.3 cost about 14% more detection time).

| | kalkan | kvkk-pii (regex) |
|---|---|---|
| Detect, from Rust | **8 µs/message** | 105 µs/message |
| Mask, from Python (single core) | **12 µs/message** | 104 µs/message |
| Mask, Python `mask_batch` (2 cores) | **8 µs/message** | — |
| Recall | 100% | 79% |
| Precision | 100% | 99.8% |

The accuracy gap comes mainly from spaced IBANs (the competitor catches 30% and sometimes
mistakes the 16 middle digits for a card number) and names without titles (`Merhaba, ben Emre Yılmaz`).

```bash
python3 bench/gen_corpus.py corpus.txt 5
cargo run --release --example bench -- corpus.txt kalkan.jsonl
pip install kvkk-pii && python3 bench/karsilastir.py corpus.txt kalkan.jsonl
python3 bench/python_hiz.py corpus.txt
```

> ⚠️ **Read these numbers carefully.** The corpus is synthetic and its templates are limited;
> names were drawn from kalkan's own dictionary. 100% recall is therefore **not** real-world
> recall. The speed comparison is solid: both libraries process the same text. kvkk-pii's NER and
> GLiNER layers (addresses, sensitive categories such as health data) are not part of this
> comparison; those layers find things kalkan does not cover. In a chat app the LLM takes
> seconds anyway, so the speed difference matters mostly for **batch jobs** (logs, call
> transcripts, training-data cleaning).

## Security model

kalkan masks data **locally, before sending**; the vault only lives in your process. It is a
tool that **supports** the claim "personal data did not leave the country"; it is not a legal
compliance guarantee on its own.

- Real values are kept only in the `Session` vault; writing it to disk (`--vault`, `vault`) is
  your explicit choice, and you are responsible for file permissions.
- Generation in `Synthetic` mode is **not cryptographic**; keep `secret` private and don't log
  generated fake values as if they were real.
- `audit` **reports**, it does not block: decide what to do before showing a flagged reply to
  the user (the CLI `audit` exits with code 1 in that case).
- Undetected data cannot be masked; never assume 100% coverage. In critical flows combine kalkan
  with an NER layer and an output filter.
- The FFI output buffer is process-wide: with concurrent calls, only read the output of the most
  recently completed call.

To report a vulnerability see [SECURITY.md](SECURITY.md).

## Limitations

> **Important:** kalkan is a helper, not a legal compliance guarantee. Detection is not 100%;
> using kalkan alone does not make you KVKK or GDPR compliant. Audit outputs with `audit` in
> sensitive flows and do your own legal assessment. The software is provided "as is", without
> warranty of any kind, as stated in the licenses.

- **Names are heuristic.** Without a title, honorific, form label, or a dictionary first name +
  surname, a name can be missed (e.g. `Gülizar Tunç geldi`). Use an NER model alongside for high
  recall on free text.
- **Addresses are heuristic.** Addresses without a `Mah./Cad./Sok./Blv.` anchor (e.g. `Kadıköy'de
  oturuyorum`, village addresses) are missed. SGK numbers have no checksum and need context.
- **No sensitive categories (health, religion, …).**
- In `Synthetic` mode, if the model reformats the fake value (e.g. strips spaces) restore will
  not recognise it. Use `Token` in critical flows.
- Different spellings of the same value (`0532 123 45 67` / `+905321234567`, `ACME` / `Acme`)
  intentionally share a token and are restored with the first spelling seen.
- Scanning slows down linearly with very many custom terms (hundreds).

## Testing

```bash
cargo test --workspace --exclude kalkan-py   # unit + integration + doctests
cargo test --features ffi --lib              # + C ABI tests
cd python && maturin develop && pytest
cargo build --release --features ffi && cd wasm && bun install && bun test
```

- **Fuzz:** 20,000 random inputs: no panics, spans on UTF-8 boundaries and non-overlapping,
  `restore(mask(x)) == x`.
- **Streaming:** replies are verified when split at every possible byte and into 1–12 character
  chunks; on the JS side including splits in the middle of an emoji (UTF-16 surrogate pair).
- **JS wrapper and demo page:** the same C ABI is loaded natively via `bun:ffi`; the demo page is
  run in happy-dom against the real engine, including HTML-injection tests.
- **CI:** `.github/workflows/ci.yml` runs all three languages on every push; `wheels.yml`
  uploads Linux/macOS/Windows wheels to PyPI when a tag is pushed.

## Contributing and license

Contributions are welcome in English or Turkish. See [CONTRIBUTING.md](CONTRIBUTING.md),
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [CHANGELOG.md](CHANGELOG.md) and
[SECURITY.md](SECURITY.md). Issues labelled
[`good first issue`](https://github.com/CelkMehmett/kalkan/labels/good%20first%20issue) are a
good place to start; new detectors (addresses, SGK numbers) are especially welcome.

Licensed under either of [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE) at your option.
