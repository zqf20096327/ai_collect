# matriks-mask

[![PyPI](https://img.shields.io/pypi/v/matriks-mask.svg?cacheSeconds=3600)](https://pypi.org/project/matriks-mask/)
[![Python](https://img.shields.io/pypi/pyversions/matriks-mask.svg?cacheSeconds=3600)](https://pypi.org/project/matriks-mask/)
[![ci](https://github.com/MatriksData/matriks-mask/actions/workflows/ci.yml/badge.svg)](https://github.com/MatriksData/matriks-mask/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://github.com/MatriksData/matriks-mask/blob/main/LICENSE)

**English** | [Türkçe](https://github.com/MatriksData/matriks-mask/blob/main/README.tr.md)

Reversible personal data (PII) masking for Turkish text, built as a [LiteLLM](https://github.com/BerriAI/litellm)
guardrail. It supports KVKK (Turkey's personal data protection law) compliance processes.

> This plugin is a technical measure that supports KVKK compliance processes; it is not legal advice and does not by
> itself ensure compliance (see [KVKK and sector regulation](#kvkk-and-sector-regulation-not-legal-advice)). **It is not
> guaranteed that every piece of personal data in a text will be detected** (see [Known limitations](#known-limitations));
> organisations should test the masking results for their own use case.
>
> **Data controllership:** Organisations that use the plugin in their own systems are the data controllers of the
> personal data they process; Matriks is not the data controller of that data. The plugin sends no data, telemetry or
> usage information to Matriks; all processing happens in the organisation's own environment.

Before a request reaches the LLM provider, values such as Turkish ID numbers (TCKN), tax numbers (VKN), IBANs, cards,
phone numbers, names, addresses, API keys and the special categories of personal data in KVKK art. 6 are replaced with
placeholders such as `<KISI_1>` ("person") and `<TCKN_1>`. When the response comes back (streaming included), the
placeholders are restored to the original values. Original values do not reach the provider, proxy logs, spend logs,
metrics or the audit trail. Everything runs in-process: no text is sent to an external detection service.

```
User ──"Ben Ayşe Demir, TCKN 17291716060"──▶ LiteLLM proxy ──"Ben <KISI_1>, TCKN <TCKN_1>"──▶ LLM
User ◀──"Merhaba Ayşe Demir'e ilettim"────── matriks-mask ◀──"Merhaba <KISI_1>'e ilettim"───── LLM
                                             (suffix repair: 'e → 'e/'ye by vowel harmony)
```

## Highlights

- **Turkish identifiers:** TCKN, VKN, TR IBAN, Troy cards, TR licence plates, MERSİS, MKK registry numbers; validated by
  check digits and context.
- **Turkish names and inflected forms** (`Ahmet'in`, `Ayşeye`, `Ahmet YILMAZ`): name lexicon + morphology + context
  (+ optional Turkish NER).
- **Restoration in responses, streaming included,** with Turkish suffix repair by vowel harmony
  (`<KISI_1>'e` → `Kemal'e` / `Ayşe'ye`).
- **KVKK art. 6 special categories of personal data:** 12 categories, masked only when linked to a person.
- **In-process:** no text is sent to an external service for detection.
- **Low latency:** 2 KB text p50 ≈ 2.9 ms (measured on a development machine; varies with hardware;
  `pytest -m benchmark`, `python scripts/bench.py`).

## Installation

The package and the command are [**`matriks-mask`**](https://pypi.org/project/matriks-mask/). The Python module
(`matriks_pii`, LiteLLM guardrail path `matriks_pii.guardrail.TurkishPIIGuardrail`), the `MATRIKS_PII_*` environment
variables and the `matriks_pii_*` metrics keep their names, so existing configurations keep working; the old command
name `matriks-pii` is still installed as an alias. Upgrading from a git install of `matriks-pii` ≤ 0.3.3: run
`pip uninstall matriks-pii` first.

```bash
pip install "matriks-mask[fast]"                 # fast: pyahocorasick (optional, faster lexicon lookup)
pip install "matriks-mask[redis,fast,metrics]"   # production: encrypted Redis session store + Prometheus
pip install "matriks-mask[ner]"                  # optional Turkish NER (transformers + torch)
pip install "git+https://github.com/MatriksData/matriks-mask"   # latest version on main
pipx install matriks-mask                        # CLI only (`matriks-mask "…"`), isolated environment
```

For pinned production versions use [`constraints/prod.txt`](https://github.com/MatriksData/matriks-mask/blob/main/constraints/prod.txt) from the repository
(`pip install "matriks-mask[redis,fast,metrics]" -c constraints/prod.txt`).

### Try it without LiteLLM

```bash
$ matriks-mask "Ben Ayşe Demir, TCKN 17291716060"
Ben <KISI_1>, TCKN <TCKN_1>
$ echo "Ahmet Yılmaz'ın telefonu 0532 234 56 78" | matriks-mask mask --profile strict --json   # type + position, no values
```

From Python (mask → restore):

```python
from matriks_pii import MaskSession, PIIEngine, Reverter, TurkishPIIConfig

cfg = TurkishPIIConfig.build({"profile": "balanced"})
engine, session = PIIEngine(cfg), MaskSession(cfg)
masked, spans, blocked, logged = engine.mask_text("Ben Ayşe Demir, TCKN 17291716060", session)
print(masked)                                    # Ben <KISI_1>, TCKN <TCKN_1>
reverter = Reverter(session.map, session.entities, cfg)
print(reverter.revert("<KISI_1>'e ilettim", final=True))   # Ayşe Demir'e ilettim
```

`session.map` (placeholder → original value) contains personal data; do not log it or store it persistently. If
`blocked` is not empty (an entity with the BLOCK action was found), do not send the text.

### With LiteLLM

Minimum LiteLLM version is **1.106.1** (tested with 1.106.1, 1.106.5 and 1.110.2). LiteLLM `config.yaml`:

```yaml
guardrails:
  - guardrail_name: matriks-pii
    litellm_params:
      guardrail: matriks_pii.guardrail.TurkishPIIGuardrail
      mode: [pre_call, post_call]   # both REQUIRED (post_call = restoration)
      default_on: true
      profile: balanced
```

Verify the installation (prints no values; can also be used in CI and as a Kubernetes `startupProbe`):

```bash
matriks-mask selftest --config config.yaml           # config, store, 12 canonical probes, latency
matriks-mask selftest --config config.yaml --quick   # < 2 s
```

Step-by-step installation, multiple workers/replicas, verification and troubleshooting:
[`docs/LITELLM_KURULUM.md`](https://github.com/MatriksData/matriks-mask/blob/main/docs/LITELLM_KURULUM.md). Operations runbook (error codes, metrics, secret rotation,
rollback): [`docs/RUNBOOK.md`](https://github.com/MatriksData/matriks-mask/blob/main/docs/RUNBOOK.md). KVKK data category mapping (VERBİS/DPIA):
[`docs/KVKK_VERI_KATEGORILERI.md`](https://github.com/MatriksData/matriks-mask/blob/main/docs/KVKK_VERI_KATEGORILERI.md). These documents are in Turkish.

Full examples: [`examples/config.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/config.yaml), [`config.strict.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/config.strict.yaml),
[`config.redis.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/config.redis.yaml), [`config.placeholder_formats.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/config.placeholder_formats.yaml),
[`Dockerfile`](https://github.com/MatriksData/matriks-mask/blob/main/examples/Dockerfile).

With `default_on: false`, the guardrail is enabled per request with `"guardrails": ["matriks-pii"]` in the request body.
Clients cannot disable it: `disable_global_guardrails` / `opted_out_global_guardrails` are read only from admin
(key/team) metadata.

**`stream_scope` warning:** `stream_scope: non_streaming` in the LiteLLM guardrail settings skips the `post_call` hook
for streaming responses, so placeholders reach the client unrestored. Do not use it (selftest warns about it).

## Detected entities

Labels are Turkish (`KISI` = person, `TELEFON` = phone, `EPOSTA` = e-mail, `ADRES` = address …); they can be changed
per entity with `labels` (e.g. `labels: {KISI: PERSON}` → `<PERSON_1>`) and the format with `placeholder_format`.

| Label | What | How it is validated | Default |
|---|---|---|---|
| `TCKN` | Turkish ID number (incl. foreigner IDs starting with 98/99) | 11 digits + official checksum; `17.291.716.060`, spaced digits, full-width digits | MASK |
| `VKN` | Tax ID number | 10 digits + checksum **and** tax context | MASK |
| `IBAN` | TR and foreign IBAN (spaces/dashes/lower case; without `TR` if labelled) | ISO 7064 mod-97 | MASK |
| `KART` | Visa/MC/Amex/Discover/JCB/Diners/**Troy** | Luhn + BIN | MASK, only the last 4 digits restored |
| `KART_CVV`, `KART_SKT` | CVV, expiry date | context | MASK (CVV is never restored) |
| `TELEFON` | mobile, landline (real area codes), 0850, 0812 | numbering plan; record-number contexts excluded | MASK (444/0800 optional) |
| `EPOSTA`, `IP`, `MAC` | incl. e-mails obfuscated with `[at]`/`(at)` | IPv4/IPv6 validation, version numbers excluded | MASK (MAC: IGNORE) |
| `PLAKA` | licence plates `34 ABC 123`, `06-A-1234` | province code 01–81, letter/digit length rules | MASK |
| `PASAPORT`, `KIMLIK_SERI`, `EHLIYET`, `SGK`, `NUFUS_KAYIT` | identity documents (incl. old ID cards) | context required | MASK |
| `HESAP_NO`, `MUSTERI_NO`, `MKK_SICIL`, `POLICE_NO`, `MERSIS`, `ETTN`, `IMEI`, `SASI_NO`, `ADRES_KODU` | financial/corporate identifiers | context (+Luhn/VKN) | MASK |
| `TICARET_SICIL` | trade registry number | context | IGNORE (legal entity; can be enabled for sole proprietorships) |
| `KRIPTO_CUZDAN` | BTC/ETH/TRON address | format | IGNORE |
| `SIFRE` | `şifre: …`, `password=…` (value must contain digits/symbols) | context | MASK, never restored (`****` in the response); strict: **BLOCK** |
| `GIZLI_ANAHTAR` | OpenAI/Anthropic/AWS/GitHub/Slack/Google/Stripe keys, JWT, private keys, connection-string passwords, Bearer | provider prefixes | MASK, `****` in the response (strict: BLOCK) |
| `KONUM` | coordinates linked to a person or personal record | context + link to a person | MASK |
| `DOGUM_TARIHI`, `DOGUM_YERI` | date/place of birth | birth context | MASK |
| `ADRES` | neighbourhood/street/avenue/no/flat, village/locality… | ≥2 anchors or `No`/number + province/district | MASK |
| `KISI` | first name, full name, `Ahmet YILMAZ`, titled names, `Ahmetin`, `AHMET'in` | 7k first-name + 23.9k surname lexicon, context, morphology, organisation-name exclusion | MASK |
| `OZEL_SAGLIK`, `OZEL_GENETIK`, `OZEL_BIYOMETRIK`, `OZEL_CINSEL`, `OZEL_CEZA` | KVKK art. 6: health, genetic, biometric, sex life, criminal conviction | term + **link to a person** (person/ID or 1st/2nd person in the same sentence) | MASK |
| `OZEL_DIN`, `OZEL_ETNIK`, `OZEL_SIYASI`, `OZEL_FELSEFI`, `OZEL_KIYAFET`, `OZEL_UYELIK`, `OZEL_CEZA_GENIS` | KVKK art. 6: religion, ethnicity, political opinion, philosophical belief, attire, membership, broader criminal data | same | LOG (counted only) |

Actions: `MASK` (placeholder, restored in the response), `BLOCK` (HTTP 400, error without values), `LOG` (counted in
the audit trail only), `IGNORE`.

## Organisation-specific definitions

Built-in rules cover formats that are the same everywhere (TCKN, IBAN, phone, e-mail, URL encoding…). Formats that
differ between organisations (an account number in a log field, PNR, user name, order number) are added **through
configuration**; no code change is needed. `entity: KULLANICI_ADI` creates a `<KULLANICI_ADI_1>` placeholder that is
restored in the response.

| Field | When | Example |
|---|---|---|
| `extra_regex` | Organisation-specific identifiers with a known format | account no, PNR, user name |
| `deny_list` | Fixed phrases that must always be masked | project name, customer code |
| `allow_list` | Phrases that must never be masked | person names that look like product names (not applied to TCKN, VKN, IBAN, card, CVV, key, password) |

`extra_regex` fields:

| Field | Default | Description |
|---|---|---|
| `entity` | required | A new name (ASCII upper case, `_`) or an existing label (e.g. `TELEFON`; that entity's action then applies) |
| `pattern` | required | Python regex |
| `group` | — | Only this capture group (number or name) is masked: `'AccountId=([0-9]+)'` + `group: 1` → the number only |
| `score` | 0.8 | Priority when spans overlap |
| `context` | — | Regex; matches only if this phrase is within `context_window` characters of the value. Case- and Turkish-letter-insensitive (`reçete` = `RECETE`) |
| `context_window` | 60 | Distance searched for the context; if too wide, neighbouring numbers are caught too |
| `ignore_case` | `true` | For `pattern`; set `false` for upper-case codes (PNR) |
| `action` | `MASK` | `MASK`, `BLOCK`, `LOG`, `IGNORE` (new entity types only) |
| `restore` | `true` | `false`: not restored in the response (`****`) |

```yaml
extra_regex:
  - {entity: HESAP_NO, pattern: '(?:AccountId=|\|1=)([0-9]{6,12})', group: 1, score: 0.9}
  - {entity: PNR, pattern: '(?<![0-9A-Za-z])[A-Z0-9]{6}(?![0-9A-Za-z])', context: 'pnr|booking ref', context_window: 25, ignore_case: false}
deny_list:
  - {phrase: "Proje Kartal", entity: PROJE}        # → <PROJE_1>, restored in the response
allow_list: ["Can Bey"]
```

**Ready-made sector examples** ([`examples/sektor/`](https://github.com/MatriksData/matriks-mask/blob/main/examples/sektor)): finance/brokerage, airline, healthcare, insurance,
manufacturing, e-commerce/shipping, telecom and foreign formats (international phone numbers, US SSN, UK NINO). Each
file is tested in CI against its own evaluation set ([`tests/fixtures/sektor/`](https://github.com/MatriksData/matriks-mask/blob/main/tests/fixtures/sektor)). They are
starting points; narrow them to your real formats. To contribute a new sector file: [`CONTRIBUTING.md`](https://github.com/MatriksData/matriks-mask/blob/main/CONTRIBUTING.md).

**Built-in sector types:** `HESAP_NO`, `MUSTERI_NO`, `MKK_SICIL`, `POLICE_NO` are finance/insurance specific but fire
only in their own context ("hesap no", "MKK sicil", "poliçe no"), so they do not cause false positives in other sectors.

### Writing and validating rules

```bash
# 1) add the rule to the config and try a single text (no values printed; --show-values only for local debugging)
matriks-mask selftest --config config.yaml --probe "PNR: TX4K9Q yolcu Ayşe Demir"
#   probe: entity=PNR start=5 end=11 score=0.8 recognizer=extra_regex
matriks-mask mask --config config.yaml "PNR: TX4K9Q yolcu Ayşe Demir"
#   PNR: <PNR_1> yolcu <KISI_1>

# 2) measure on your own labelled set (one JSON per line; rows that must not be masked have "entities": [])
matriks-mask selftest --config config.yaml --corpus set.jsonl
```

```json
{"text": "PNR: TX4K9Q yolcu Ayşe Demir", "entities": [{"entity": "PNR", "value": "TX4K9Q"}, {"entity": "KISI", "value": "Ayşe Demir"}]}
{"text": "TK1984 seferi 14:30 kalkış, kapı B12", "entities": []}
```

> **When evaluating the product:** define your organisation-specific formats before measuring and leave out-of-scope
> types (e.g. user names, if you did not define them) out of the denominator; otherwise the result measures missing
> configuration, not the product. Measure on a separate labelled set the rules have not seen.

### Domestic / foreign coverage

The core is written for Turkey. **Outside Turkey, personal data in your own country's formats is largely not covered
out of the box.**

| Data | Turkey | Other countries |
|---|---|---|
| National ID number | TCKN, VKN | not built in (SSN, NINO: [`yurtdisi.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/sektor/yurtdisi.yaml)) |
| Phone number | detected | not built in ([`yurtdisi.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/sektor/yurtdisi.yaml)) |
| IBAN, card | detected | detected |
| Passport | with context | with context |
| E-mail, IP | detected | detected |
| Full name | lexicon + morphology | NER mode only (`ner_backend: hf`) |
| Address | detected | not detected |

## Profiles

| Profile | What it does |
|---|---|
| `balanced` (default) | The table above |
| `strict` | All `OZEL_*`, crypto, MAC, trade registry MASK; `GIZLI_ANAHTAR` BLOCK; 444 lines MASK; placeholder instruction to the LLM; scanning responses for new PII; labelled values with invalid checksums are masked too |
| `minimal` | Only TCKN, VKN, IBAN, KART, TELEFON, EPOSTA, KISI, GIZLI_ANAHTAR; `OZEL_*` LOG |

Explicit keys override the profile: `entities: {OZEL_DIN: MASK, PLAKA: IGNORE}`. Unknown entity names fail at startup.

## Key settings

| Setting | Default | Description |
|---|---|---|
| `placeholder_format` | `<{label}_{n}>` | `__{label}_{n}__`, `[{label}_{n}]`, `PII_{label}_{n}` … |
| `placeholder_id` | `sequence` | `hmac` + `hash_secret`: the same value gets the same placeholder across turns/replicas (prompt-cache friendly; numbering does not shift in a sliding window) |
| `fail_mode` | `closed` | If the guardrail fails, the request does **not** reach the LLM (HTTP 500) |
| `revert_fail_mode` | `closed` | If restoration fails **or the session is not found**, the response does not reach the client with placeholders (HTTP 500) |
| `dry_run` | `false` | Shadow mode: nothing is masked/blocked, only "would mask" counts are logged (gradual rollout) |
| `mask_logs` | `true` | Re-masks the (restored) response and the request that the proxy logs |
| `session_store` | `memory`, TTL 3600 s, 10,000 sessions | `redis`: AES-GCM encrypted; `redis_timeout_seconds` (2 s), circuit breaker, `require_tls`, `encryption_key_previous` (rotation) |
| `session_secret` | — (`MATRIKS_PII_SESSION_SECRET`) | HMAC secret for session tokens, ≥32 characters; **required** with the `redis` store, identical on all instances; `session_secret_previous` (rotation) |
| `max_text_chars`, `max_request_chars` | 2 MB, 4 MB | If exceeded, the request is cleared, HTTP 413 |
| `analysis_threads` | 4 | Dedicated thread pool for analysis/log masking (does not starve LiteLLM's executor) |
| `analysis_cache` | 2048 entries, 300 s, 200k spans | In-memory span list (with original values); `max_entries: 0` disables it; texts over 64 KB are not cached |
| `unsupported_call_types` | `mask` | For rerank/image/audio/MCP calls: `mask` (no restoration), `pass`, `block` |
| `gemini_native` | `true` | Full mask/restore on Gemini `/v1beta/models/...:generateContent` (+ stream) |
| `audit_log` | off | Value-free JSONL audit trail (who, when, how many of which entity type, score buckets) |
| `metrics_enabled` | `true` | `matriks_pii_*` counters if `prometheus_client` is installed (value-free labels) |
| `placeholder_instruction` | `none` | `system_suffix` (recommended): appends an instruction to the system message: use placeholders as if they were real values, do not mention masking, do not abbreviate |
| `label_aliases` | `PERSON→KISI, PHONE→TELEFON…` | Labels translated by the LLM (`<PERSON_1>`) are restored only in bracketed form; `{}` disables |
| `scan_response` | `false` (`strict`: on) | Masks NEW personal data generated by the LLM in the response (not restored; not applied to streams) |
| `response_json_preserve_format` | `true` | JSON text in response content is restored with its formatting (indentation, order) preserved |
| `suffix_repair` / `suffix_repair_attached` | `true` / `false` | Turkish suffix repair; suffixes attached without an apostrophe (`<KISI_1>lar` → `Demirler`) behind a flag |
| `tool_restore_policy` | `all` | `none`: tool call arguments keep placeholders |
| `mask_system_messages`, `mask_assistant_messages`, `mask_tool_messages`, `mask_embeddings` | `true` | |
| `name_detection.ner_backend` | `none` | `hf`: Turkish NER; `ner_max_chars` (sentence-based chunking), `ner_timeout_seconds`, `ner_fail_mode` (`closed`/`lexicon`), `ner_preload` |
| `checksum_policy` | `strict` (`strict` profile: `context`) | `context`: explicitly labelled values are masked even if the check digit is wrong |

Environment variables can be referenced as `os.environ/NAME` (`hash_secret: os.environ/MATRIKS_PII_HASH_SECRET`). A
warning is printed at startup if secrets are given in plain text (`MATRIKS_PII_STRICT_SECRETS=1` → error). Secrets
never enter `config_hash`, error messages or logs.

### Errors

| Situation | HTTP | `detail.error` | What happens |
|---|---|---|---|
| Blocked by policy (`BLOCK`) | 400 | `matriks_pii_blocked` | has an `entity` field, no value; the request is masked before it is logged |
| Text/request too large | 413 | `matriks_pii_text_too_large` | request cleared; independent of `fail_mode` |
| Guardrail internal error | 500 | `matriks_pii_guardrail_failure` | `fail_mode: closed` → request cleared, never reaches the provider |
| Session not found (TTL, secret mismatch, store) | 500 | `matriks_pii_session_missing` | `revert_fail_mode: closed` → response is not sent with placeholders |
| Session store unreachable | 503 | `matriks_pii_store_unavailable` | only requests containing PII are affected (no session is written for PII-free requests) |
| Restoration error | 500 | `matriks_pii_revert_failure` | `revert_fail_mode: open` → response returned with placeholders |

If an error occurs in a stream before the first chunk, LiteLLM turns it into an SSE error frame (HTTP status may
already have been sent as 200); in no case are raw values or placeholders emitted.

### Multiple workers / replicas

The pre-call and post-call hooks of a request run in the same process; a `memory` store is enough for a single pod.
Redis is recommended for Admin UI "guardrail test" (`apply_guardrail`) pairs behind many pods/replicas, for keeping
sessions across restarts and for moving the memory limit out of the process.

1. Generate secrets **once** and put them in a secret manager: `matriks-mask keys` (`--k8s` for a kubectl command).
2. `pip install "matriks-mask[redis,fast]"`.
3. [`examples/config.redis.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/config.redis.yaml):

   ```yaml
   guardrails:
     - guardrail_name: matriks-pii
       litellm_params:
         guardrail: matriks_pii.guardrail.TurkishPIIGuardrail
         mode: [pre_call, post_call]
         default_on: true
         session_secret: os.environ/MATRIKS_PII_SESSION_SECRET
         session_store:
           backend: redis
           redis_url: os.environ/MATRIKS_PII_REDIS_URL      # rediss://:password@redis:6380/0 (TLS recommended)
           encryption_key: os.environ/MATRIKS_PII_STORE_KEY
           ttl_seconds: 3600                                  # ≥ LiteLLM request_timeout
           redis_timeout_seconds: 2
           require_tls: true
   ```

`*_PREVIOUS` variables for zero-downtime secret/key rotation: [`docs/RUNBOOK.md`](https://github.com/MatriksData/matriks-mask/blob/main/docs/RUNBOOK.md#sır-ve-anahtar-rotasyonu-kesintisiz).

### Per-tenant (key/team) policy

Define several guardrail instances for different policies (`matriks-pii`, `matriks-pii-strict` …, `default_on: false`)
and add them to the key/team `guardrails` list. Session tokens are separated by guardrail name; two instances can run
together on the same request.

## Supported calls

| Endpoint | Request | Response | Streaming |
|---|---|---|---|
| `/chat/completions` | text, multi-part content, `tool_calls` JSON arguments, `name`, `reasoning_content` | content, tool calls, `reasoning_content`, `n>1` | content, reasoning, tool arguments (JSON-escaped) |
| `/completions`, `/embeddings` | `prompt`, `input` (str/list) | `choices[].text` | `/completions`: `choices[].text` chunks |
| `/responses` | `input`, `instructions`, `function_call(_output)`, `prompt.variables` | `output` | `response.*.delta/done/completed` events |
| `/v1/messages` (Anthropic) | `system`, `tool_use`, `tool_result`, `document` | `content` | raw SSE (`text_delta`, `input_json_delta`), byte-level UTF-8 safe |
| `/v1beta/models/...:generateContent` (Gemini) | `contents[].parts[]`, `systemInstruction`, `functionCall/Response` | `candidates[].content.parts[]` | raw SSE frames, per-candidate buffer |
| rerank, image, audio, MCP | text fields masked (`unsupported_call_types`) | not restored | — |

Cross-format parity is verified by the `tests/test_parity.py` matrix (5 formats × 15 features); cells that do not
apply are listed there with a reason.

Texts with JSON content (tool arguments, JSON messages, numbers and keys included) are parsed and masked leaf by leaf;
JSON content in responses is restored with its formatting preserved.

## Quality and performance

All tests: `pytest -q` (≈2.3k tests + hypothesis property tests), `pytest -m benchmark`, `pytest -m e2e` (real LiteLLM
proxy + OpenAI-compatible and Gemini echo servers), `pytest -m external`, `pytest -m ner`, `pytest -m redis_live`.

- Positive/mixed fixtures (733 detection + 76 restoration + 37 streaming + 94 hook scenarios + 52 sector-example rows) and **596 false-positive
  traps** (stock tickers, ISINs, VIOP contracts, numbers with invalid checksums, organisation names, currency pairs,
  secret-key prefixes, news sentences about special categories…): `python scripts/corpus_report.py`. In the default
  lexicon mode the false-positive count is 0.
- Two synthetic evaluation sets written by separate LLM agents (AI models) that had no access to the implementation:
  `tests/fixtures/holdout/` (results below).

| Set | Rows (PII / traps) | Measurement | P | R | F2 |
|---|---|---|---|---|---|
| holdout-1 (`holdout.jsonl`), KISI | 269 (162 / 107) | blind, before fixes | 0.947 | 0.831 | 0.852 |
| holdout-1, KISI | | after general fixes | 0.977 | 0.977 | 0.977 |
| holdout-2 (`holdout2.jsonl`), all entities, `balanced` | 345 (226 / 119) | blind, before fixes | 0.954 | 0.934 | 0.938 |
| holdout-2, all entities, `balanced` | | after general fixes | 0.991 | 0.994 | 0.993 |
| holdout-2, all entities, `strict` | | after general fixes | 0.974 | 0.994 | 0.990 |

Holdout-2 also covers the newer entities (`GIZLI_ANAHTAR`, `KONUM`, `MKK_SICIL`, `POLICE_NO`). After the blind
measurement only fixes that are not specific to the set were made; the remaining 3 rows are differences of
interpretation. Since the sets are no longer blind, `tests/test_holdout.py` only catches regressions (FP = FN = 0 for
deterministic entities; KISI R ≥ 0.95, F2 ≥ 0.95; OZEL_* recall ≥ 0.90 on holdout-2).

NER mode (`ner_backend: hf`, `akdeniz27/bert-base-turkish-cased-ner`; `python scripts/corpus_report.py --ner`):
`KISI` F2 ≈ 0.99 on the fixtures; the 512-token limit is handled by sentence-based chunking. In NER mode the negative
set is informational (the model also catches real foreign names).

**Third-party Turkish datasets** (`python scripts/external_bench.py --download`; no rows were copied into fixtures
during development, only general rules were fixed). Out-of-scope labels (nationality, salary, user name, credit
score…) are not counted:

| Dataset | Profile | P | R | F2 | Note |
|---|---|---|---|---|---|
| [cagrigungor/turkish-pii-masking-benchmark](https://huggingface.co/datasets/cagrigungor/turkish-pii-masking-benchmark) (1,000 rows, CC0) | `strict` | 0.978 | 0.944 | **0.950** | |
| same | `balanced` | 0.985 | 0.749 | 0.787 | most of the gap is special categories that are only LOGged (religion, ethnicity, union) |
| [Werea-co/Werea-KVKK-Bench](https://huggingface.co/datasets/Werea-co/Werea-KVKK-Bench) `pii_synthetic` (2,400 rows, Apache-2.0) | `strict` | **1.000** | 0.627 | 0.677 | most misses are general special-category sentences not linked to a person — intentional under KVKK art. 3/1-d |

Latency (single core, NER off, cache off; `python scripts/bench.py`):

| Input | p50 (ms) | p99 (ms) |
|---|---|---|
| 256 characters | 0.51 | 0.96 |
| 2048 characters | 2.8–3.0 | 3.3–3.5 |
| 10000 characters | 14.0 | 21.9 |
| 50000 characters | 79.9 | 93.6 |
| stream chunk (5 characters) | 0.012 | — |

Total text over 8 KB (every text when NER is on) is analysed in the dedicated thread pool; the event loop is not
blocked. Pathological inputs (100 KB digit runs, thousands of invalid IBAN candidates, long whitespace runs) are
processed in linear time.

## Operations

- **Metrics** (`pip install "matriks-mask[metrics]"`, `callbacks: ["prometheus"]` in LiteLLM): `matriks_pii_entities_total`,
  `matriks_pii_hook_seconds`, `matriks_pii_hook_total`, `matriks_pii_events_total` (session_missing, store_unavailable,
  blocked, unresolved_placeholder, ner_failed, audit_write_failed, dry_run_would_mask), `matriks_pii_scores_total`,
  `matriks_pii_sessions_open`, `matriks_pii_cache_entries`. Safe in multi-worker mode.
- **Gradual rollout:** first `dry_run: true` (staging 5 business days, production 1 week), then a per-key canary, then `default_on`.
- **Rollback:** wheel + config as a pair; in an emergency `MATRIKS_PII_IGNORE_UNKNOWN_KEYS=1`. Details: [`docs/RUNBOOK.md`](https://github.com/MatriksData/matriks-mask/blob/main/docs/RUNBOOK.md).

## KVKK and sector regulation (not legal advice)

- **Terminology:** As long as the mapping is kept in memory, this processing is not anonymisation but the use of
  codes/pseudonyms (KVKK Guide on Deletion, Destruction or Anonymisation of Personal Data; Guide on Generative AI and
  the Protection of Personal Data (in 15 Questions), 24.11.2025). For the data controller the data remains personal
  data; the exemption in art. 28/1-b cannot be relied upon.
- **Transfers abroad (art. 9, Regulation of 10.07.2024):** A request to an LLM abroad is a transfer; masking reduces
  the risk but does not remove the obligation. Standard Contract 2 must be signed and notified to the Authority within
  5 business days. Continuous API traffic is not "incidental".
- **Special categories (art. 6):** health/genetic/biometric/sex life/criminal data are MASKed by default;
  `profile: strict` masks all of them, and `BLOCK` ensures they are never sent. A criminal conviction is a final
  judgment; suspect/defendant/custody are separate (`OZEL_CEZA_GENIS`).
- **Data security (art. 12):** fail-closed defaults, value-free audit trail and metrics, masking in logs, AES-GCM in
  Redis; the mapping is never written to metadata (`store_map_in_metadata` only with `MATRIKS_PII_ALLOW_DEBUG_MAP=1`);
  API keys are masked.
- **Capital markets and banking regulation:** Organisations in these sectors are also subject to regulations such as
  the Capital Markets Board (SPK) Communiqué on Information Systems Management (VII-128.10), Banking Law No. 5411
  art. 73 (confidentiality) and the BDDK Regulation on the Sharing of Confidential Information; the plugin does not
  fulfil these obligations. Banks should assess for themselves whether the tool is suitable for de-identification
  purposes under the Confidentiality Regulation.
- **Test data:** All test fixtures in the repository are synthetic; they contain no data belonging to real persons.

Category mapping and audit trail fields: [`docs/KVKK_VERI_KATEGORILERI.md`](https://github.com/MatriksData/matriks-mask/blob/main/docs/KVKK_VERI_KATEGORILERI.md).

**Obligations outside the plugin:** SCC-2 + notification, a data processing agreement with the provider
(sub-processors, no training use, retention period), DPIA, privacy notice, VERBİS/inventory, breach response plan
(72 hours), employee training, red-team testing.

## Known limitations

- Free-text names written entirely in lower case (`ahmet yılmaz dün geldi`) are caught only in form/field context;
  NER mode is recommended. Names inside company names (`Ahmet Yılmaz Holding`) are not masked; sole-proprietorship
  names (`Mehmet Kaya Kuyumculuk`) are treated as personal data and masked.
- Foreign names (not in the lexicon) are caught in lexicon mode only with context; NER mode is recommended. Single
  names that are also common words are caught mid-sentence (`Dün Deniz aradı`), but not at the start of a sentence
  without context (`Deniz kenarında`).
- Numbers split by zero-width characters (`1729​1716060`) are not detected. Full-width digits (`１７２９…`) are detected.
- URL-encoded (`%40`, `%20`; only inside URLs/forms, Turkish percent notation such as "%40" excluded) and HTML-entity
  (`&#64;`) values, and form `+` between letters/digits (`tel=0532+123+45+67`), are decoded for scanning and the
  original encoded range is masked. Not decoded: a run containing an invalid byte (`%40%FF`), triple encoding
  (`%252540`), a single `%XX` run outside a URL/form, and other encodings such as Base64.
- Foreign phone numbers and foreign national ID numbers are not built in; see [`yurtdisi.yaml`](https://github.com/MatriksData/matriks-mask/blob/main/examples/sektor/yurtdisi.yaml).
- Personal data inside images/files (PDFs, ID card photos) is not scanned; such content reaches the provider as is.
- History kept server-side via Responses API `previous_response_id` cannot be masked.
- In Anthropic `/anthropic/*` **passthrough** streaming, LiteLLM does not call the post-call guardrail (LiteLLM #42476);
  use `/v1/messages`.
- Signed Anthropic `thinking` blocks and signed Gemini thought parts are not modified (the signature would break).
- In multi-turn conversations `sequence` numbering can shift in a sliding window; `placeholder_id: hmac` is
  recommended. A literal `<KISI_1>` sent back by the client is reserved (a new value gets `<KISI_2>`).
- With `response_json_preserve_format` on, `scan_response` also works on JSON content, but the JSON is rewritten if
  anything changes.
- Analysis is CPU-bound and runs under the Python GIL; increase the number of workers for very high concurrency.
- LiteLLM's own `--detailed_debug` prints the raw body before the guardrail runs; turn it off in production.

## Roadmap

- **Surrogate (fake value) mode — deferred to v2.** In Turkish, suffixes of a fake name (`Elif'e` ↔ `Ayşe'ye`) must be
  repaired in both directions and restoration must be proven unambiguous; the current placeholder + suffix repair
  approach does not carry these risks.
- Scanning text inside images/PDFs (OCR); Anthropic passthrough streaming (awaiting a fix in LiteLLM).

## Development

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev,fast,metrics]"
export MATRIKS_PII_HASH_SECRET=0123456789abcdef0123456789abcdef   # for the strict example config's selftest
# Windows: set PYTHONUTF8=1 && set MATRIKS_PII_HASH_SECRET=...
pytest -q && pytest -q -m benchmark && pytest -q -m e2e
python scripts/external_bench.py --download && pytest -q -m external
ruff check matriks_pii scripts tests && mypy matriks_pii --ignore-missing-imports
python scripts/corpus_report.py
matriks-mask selftest --config examples/config.yaml
# to rebuild the lexicons:
python scripts/fetch_raw.py && python scripts/build_name_lists.py && python scripts/build_common_words.py && python scripts/build_geo.py
python scripts/build_org_names.py   # optional KAP company-name list: scripts/_raw/kap_companies.txt
```

`scripts/build_fixtures.py` rewrites the generated files under `detect/revert/streaming`; hand-written files
(`*_ek.yaml`, `*_x.yaml`, `yeni_varliklar.yaml`, `sayisal_ek.yaml`) are not affected.

Data sources and licences: [`matriks_pii/data/LICENSES.md`](https://github.com/MatriksData/matriks-mask/blob/main/matriks_pii/data/LICENSES.md).

## Contributing and security

- Contribution guidelines (setup, tests, synthetic data only): [`CONTRIBUTING.md`](https://github.com/MatriksData/matriks-mask/blob/main/CONTRIBUTING.md). Issues and pull
  requests may be written in English or Turkish.
- Code of conduct: [`CODE_OF_CONDUCT.md`](https://github.com/MatriksData/matriks-mask/blob/main/CODE_OF_CONDUCT.md).
- Reporting a vulnerability (do not open a public issue): [`SECURITY.md`](https://github.com/MatriksData/matriks-mask/blob/main/SECURITY.md).

## License

The source code is licensed under the [Apache License 2.0](https://github.com/MatriksData/matriks-mask/blob/main/LICENSE), © 2026 Matriks Finansal Teknolojiler A.Ş.
(see [`NOTICE`](https://github.com/MatriksData/matriks-mask/blob/main/NOTICE)).

The package includes data files derived from third-party sources. The first-name/surname lists come from
[mkozturk/trnames](https://github.com/mkozturk/trnames) (MIT) and the province/district data from
[ubeydeozdmr/turkiye-api](https://github.com/ubeydeozdmr/turkiye-api) (MIT).
`matriks_pii/data/tr_words.txt` is derived from the OpenSubtitles 2018 Turkish word list in Hermit Dave's
[FrequencyWords](https://github.com/hermitdave/FrequencyWords) project and is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this file is not covered by the Apache-2.0 licence.
Details and licence texts: [`THIRD_PARTY_NOTICES.md`](https://github.com/MatriksData/matriks-mask/blob/main/THIRD_PARTY_NOTICES.md).

**Trademark.** The licence does not grant the right to use the "Matriks" name or logos (Apache-2.0 section 6).
Modified versions of the software must be distributed under a different name; the "Matriks" name may be used only to
indicate the origin of the software.

**Disclaimer of warranty.** The software is provided "AS IS" under sections 7 and 8 of the licence; detection of every
piece of personal data is not guaranteed.

This README is a translation of [README.tr.md](https://github.com/MatriksData/matriks-mask/blob/main/README.tr.md); in case of discrepancy the Turkish version prevails.
