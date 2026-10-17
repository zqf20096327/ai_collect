# jevtok

Exact token counting and request-cost prediction for [Jev](https://typesafe.ai), TypeSafe's System One decision model. A `tiktoken`-style encoder for a model that ships no tokenizer.

Jev bills per input token, but its tokenizer is not any public one: it uses GPT-4o's `o200k_base` vocabulary with a different encoder that produces more tokens than `tiktoken` on most real text (`evidence` is 3 tokens, `2024` is 4, `SessionManager` is 5). `jevtok` reproduces it bit for bit, reconstructed from the API's own `usage.input_tokens`.

```
$ jevtok count "The tokenization of evidence"
7
$ jevtok encode --pieces "SessionManager"
'S' 'ess' 'ion' 'Man' 'ager'
```

Verified: 0 mismatches on 20,034 strings / 5.6M tokens across 30 languages and 21 code formats, and on every one of the 546,057 strings measured while building it. Request-cost prediction: exact on 403 / 403 requests. Model version `jev-1.13-20260917`.

## Install

```bash
uv add git+https://github.com/LabGuy94/jevtok            # in a project
uvx --from git+https://github.com/LabGuy94/jevtok jevtok count "hello"   # one-off CLI
pip install git+https://github.com/LabGuy94/jevtok        # plain pip
```

Requires Python 3.10+. Dependencies: `tiktoken`, `regex`.

## Use

Same shape as `tiktoken`:

```python
import jevtok

enc = jevtok.get_encoding("jev-1.13")      # aliases: "jev-latest", "typesafe/jev-1.13"
enc.count("The tokenization of evidence")  # 7
enc.encode("evidence")                     # [68, 1429, 1082]  (o200k_base ids)
enc.decode([68, 1429, 1082])               # 'evidence'
enc.encode_pieces("evidence")              # [b'ev', b'id', b'ence']
enc.n_vocab                                # 200019
```

Predict what a whole request will be billed, before sending it:

```python
questions = {
    "is_sponsor": {"type": "noul", "instructions": "Does the message ask to sponsor the site?"},
    "category": {
        "type": "choice",
        "instructions": "What kind of product is described?",
        "criteria": {"dev_tool": "Developer tools or hosting", "course": "Courses or books", "other": None},
    },
}
jevtok.estimate_request_tokens({"name": "Managed Postgres", "text": "..."}, questions)
# -> input_tokens the API will report; raises jevtok.ContextLimitExceeded if it would be rejected
```

Structured (`dict` / `list`) states are handled the way the API handles them, which is not `json.dumps` and then tokenize; see [docs/METHOD.md](docs/METHOD.md#request-cost).

CLI:

```
jevtok count [text | -f file]          token count
jevtok encode [--pieces] [text]        ids or pieces
jevtok estimate request.json           input_tokens for {"state": ..., "questions": ...}
jevtok verify "text" | -f strings.txt  compare with the live API, print an issue-ready report on mismatch
```

## How it works

```
text ─ NFC ─ pretokenize ─┬─ pretoken in LOOKUP (144,710 tokens) ──────────────► 1 token
                          └─ else byte BPE, o200k rank order, merges limited ──► tokens
                             to results in FORMED (53,820 tokens)
```

1. **NFC normalization** (not NFKC: `ＡＢＣ` stays 3 tokens, `e` + U+0301 becomes `é`).
2. **Pretokenizer**: cl100k's regex, except every digit is its own pretoken, letter runs include combining marks, marks never join punctuation, and punctuation absorbs trailing newlines.
3. **Whole-pretoken lookup** against a 145k-token subset of `o200k_base`. `idence` alone is 1 token; inside `idenceq` it is not.
4. **Restricted BPE** for everything else: `o200k_base` merge ranks, but only ~54k tokens can ever be formed by merging (99% of 3-byte tokens, 43% of 5-byte, none of 7+). Compounds get shredded: `evidence` → `e|vid|ence`.
5. **Request cost**: `259 + state + Σ(7 + question body)` with per-type extras; a per-question cap of `state + question ≤ 32,736`.

Token ids are `o200k_base` ranks. Special tokens such as `<|endoftext|>` are ordinary text to Jev.

The full derivation, every probe class, and the evidence tables are in [docs/METHOD.md](docs/METHOD.md).

## Found a mismatch? Have an idea?

```bash
export OPENROUTER_API_KEY=...          # the endpoint jevtok was measured against
jevtok verify "the string in question"
```

If the counts differ it prints a JSON block; open a [mismatch issue](../../issues/new?template=mismatch.yml) and paste it. That is the whole process. Bulk: `jevtok verify -f strings.txt -q --report out.json`. TypeSafe's first-party endpoint is also wired up (`--endpoint typesafe`, `TYPESAFE_API_KEY`) but has not been tested.

Ideas, probe classes you think would break it, or questions about the method go in an [idea issue](../../issues/new?template=idea.yml). See [CONTRIBUTING.md](CONTRIBUTING.md) for how a mismatch becomes a fix.

## Scope

- Matches `jev-1.13-20260917`. New Jev versions may keep or change the encoder; `jevtok verify -f tests/fixtures/strings.txt` on a release tells you in a minute.
- Counts and pieces are exact; token ids are the natural `o200k_base` ranks, which is the only id space observable from outside.
- Lone surrogates are rejected by the API (HTTP 400) and raise in `jevtok`.

## License

MIT
