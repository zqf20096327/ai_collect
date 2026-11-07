# Gemma 4 for Gufo

A [Gufo](https://github.com/gufo-org/gufo) source extension for Google's
Gemma 4 on Linux x86-64 / Strix Halo `gfx1151`:

- Gemma 4 31B (Unsloth `UD-Q4_K_XL`, `UD-Q8_K_XL`)
- Gemma 4 31B QAT (Q4_0)
- Gemma 4 26B-A4B mixture of experts (`UD-Q4_K_XL`, `UD-Q6_K_XL`, `UD-Q8_K_XL`)

with `gemma4-assistant` MTP drafting, prompt lookup, the BF16 vision sidecar,
batched sessions, native tool calls and the shared serving cache.

Maintainer: Francesco Moca ([@franzmoca](https://github.com/franzmoca)).

Report bugs and regressions in the
[issues of this repository](https://github.com/franzmoca/gemma4-gufo-extension/issues),
with the GGUF file name when a model does not load.

## Features

- `gufo serve llm`: every text endpoint, reasoning (`reasoning_content`,
  `reasoning_tokens` and reasoning budgets), native tool calls (buffered and
  streamed), image input, batched sessions, and RAM and disk prompt caching.
- `gufo prompt` and `gufo bench` through the extension's drivers.
- Provider options: `--image-tokens`, `--draft-calibration`, `--draft-trace` and
  `--prefill-weights`. MTP drafts up to 15 tokens with the calibrated policy
  unless `--draft-tokens` or `--draft-policy` say otherwise.

Benchmarks and quality reports are in the model cards:
[26B-A4B](docs/models/gemma-4-26b-a4b/README.md),
[31B](docs/models/gemma-4-31b/README.md) and
[31B QAT](docs/models/gemma-4-31b-qat/README.md).

## Validation

Compared with the `feat/gemma` engine on November 6, 2026, over HTTP with the
cards' benchmark tool, in balanced order, on Strix Halo at the
accelerator-performance profile. Single-user greedy MTP, UD-Q4_K_XL, pp2048 and
tg128, mixed and repetitive text, depths 0 and 8,192:

| Model | Prefill | Decode |
| --- | ---: | ---: |
| 31B | -0.3% to -0.5% | -0.1% to +0.3% |
| 26B-A4B | -2.1% to +2.1%, noisy | -1.2% to +2.2% |

Sampled MTP at depth 0 against the cards: 26B-A4B prefill 4,010 (card 3,898),
decode 71.8 (card 73.8 ± 2.7); 31B prefill 565 (card 561), decode 25.5 (card
22.3). The target tests pass on 31B and 26B-A4B, the Pi coding-agent replay
passes 36 of 36 on 26B-A4B, and the tool, image, cache and long-context
functional suites pass on both, apart from `image-count` below.

Not repeated on this build: QAT, and the complete functional set.

## Known limits

- The functional suites `image-detail` (it assumes Qwen's image token counts)
  and `image-count` on 26B-A4B (thinking passes that test's 256-token limit)
  fail for those test reasons.
- In-place same-slot restore and shared transfer streams (batches of 256 jobs
  instead of 16) are not upstream.
- The Python tools in `tools/` are untested here.

## Build with Gufo

The extension needs extension API 0.2.14 (upstream `main` since
[#1047](https://github.com/gufo-org/gufo/pull/1047)).

```sh
git clone https://github.com/gufo-org/gufo
cd gufo
cmake --preset release -DGUFO_EXTENSION_DIRS=/path/to/gemma4-gufo-extension
cmake --build --preset release --parallel 4
./build/release/gufo diagnose --section extensions
```

With Nix, `nix build` in this repository builds the Gufo revision pinned in
`flake.nix` with this extension. The manifest maps the `mtp` mode to
`--mtp-model`, so a server generated with Gufo's `mkGufoServe` and
`speculative = "mtp"` starts the drafter.

```sh
./build/release/gufo serve llm \
  -m gemma-4-31B-it-UD-Q4_K_XL.gguf \
  --speculative mtp --mtp-model mtp-gemma-4-31B-it-Q8_0.gguf
```

The vision sidecar `mmproj-BF16.gguf` is found beside the model, or given with
`--mmproj`.

## Tests

Test and probe executables link Gufo's public implementation targets
(`gufo_ext_core`, `gufo_ext_cache`, `gufo_ext_hip`). Model tests read
`GUFO_GEMMA4_MODEL`, `GUFO_GEMMA4_MTP_MODEL` and `GUFO_GEMMA4_MMPROJ` and are
skipped without them.

## License

The extension source is MIT licensed ([LICENSE](LICENSE)). Code copied from
Gufo (`hip/ggml/`, `hip/half_gemm.*`, `mtp_sampling.hpp`, `prompt_lookup.hpp`,
`vision/resize.*` and `DraftVocab` in `draft_vocab.hpp`; each names its
source) keeps Gufo's MIT license ([LICENSES/gufo.txt](LICENSES/gufo.txt)). Gemma 4 weights
are downloaded separately under their own license.
