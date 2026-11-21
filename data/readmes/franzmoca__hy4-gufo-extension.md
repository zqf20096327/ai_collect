# Hy4 Flash for Gufo

An experimental Gufo source extension for Tencent's
[Hy4 Flash](https://huggingface.co/tencent/Hy4-flash) (`hy_v4_flash`) on
Linux x86-64 / Strix Halo `gfx1151`.

**Status:** experimental. `gufo serve llm` serves chat, tool calls, reasoning,
image input and the prompt cache (RAM and disk), and drafts with Tencent's
DFly2. One user decodes at 18.8 tok/s, 24 to 28 tok/s with DFly2 on mixed text
and 62 to 68 on repetitive text, with identical replies; prompts prefill at 740
to 870 tok/s. Concurrent requests decode together: eight users get 85 tok/s in
all. See [docs/BENCHMARKS.md](docs/BENCHMARKS.md),
[docs/QUALITY.md](docs/QUALITY.md), [docs/EXPERIMENTS.md](docs/EXPERIMENTS.md)
and the design in [docs/PLAN.md](docs/PLAN.md).

Maintainer: Francesco Moca ([@franzmoca](https://github.com/franzmoca)).

## Model files

The target build is the
[Xylolabs Q4_K_M](https://huggingface.co/Xylolabs/Hy4-flash-GGUF): a 97.8 GB
trunk kept resident, plus the 63.4 GB FP8 Engram shard read from disk. The
DFly2 drafter comes from Tencent's checkpoint
(`model-00148-of-00148.safetensors`), and the vision tower is the Xylolabs
repository's `mmproj-Hy4-flash-BF16.gguf`.

## Build with Gufo

```sh
nix build                    # Gufo with this extension: ./result/bin/gufo
./result/bin/gufo diagnose --section extensions
```

Without Nix, from a Gufo checkout at the revision pinned in `flake.lock`:

```sh
cmake --preset release -DGUFO_EXTENSION_DIRS=/path/to/hy4-gufo-extension
cmake --build --preset release --parallel 4
```

## Serve

```sh
gufo serve llm -m Hy4-flash-Q4_K_M-00001-of-00002.gguf \
  --mmproj mmproj-Hy4-flash-BF16.gguf \
  --dfly-model /path/to/tencent-dfly2   # optional: DFly2 speculative decoding
```

The second GGUF shard (the Engram table) must sit beside the first. Without
`--context` a session holds 32,768 tokens; the model's full 1,048,576 tokens
fit on a 128 GB Strix Halo beside DFly2 and vision. `--dfly-model` takes the drafter's
safetensors file or the directory holding it. By default it drafts until its
confidence head predicts acceptance below 0.45, up to 7 tokens;
`--dfly-draft-tokens` (1 to 7) fixes the count instead. Without `--mmproj`, a single
`mmproj*.gguf` beside the model enables image input. An image takes
(h/32)·(w/32 + 1) tokens after resizing to 4K to 4M pixels (`detail: low`: at
most 512²), so a 2048² image takes 4,160.
