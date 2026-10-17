# grok-bot-0.18-original

Untouched runtime code from Grok Bot 0.18.0 (`com.anysphere.sand`, built 2026-08-13), mechanically split into a per-module file tree. Reassembling the splits reproduces the official bundle byte-for-byte.

## Where the code comes from

The official installer ships its Electron runtime bundles unminified. esbuild output retains original class and function names, comments, and module path annotations, so the code reads close to source. `tools/split-bundles.mjs` slices the bundles at those module-path annotations into the `split/` tree; `split-manifest.json` records each segment's declared path, byte offset, and length.

There are no source maps involved, on any side:

- macOS DMG full tree (1296 files) and Windows `app.asar` (726 files) contain **0 `.map` files**
- All runtime bundles and renderer chunks contain **0 `sourceMappingURL` references** (including inline data URIs)
- The `sourceMap` strings inside bundles are OpenTelemetry/protobuf field names, unrelated to JS source maps

The renderer (frontend) is minified without maps and is not recoverable; it is not included here. The reorganized reconstruction with added features (inference router, Docker sandbox, usage tracking) is a separate repo: [grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed). What it adds over this archive is listed in [BN-NETT-ADDITIONS.md](BN-NETT-ADDITIONS.md).

## Contents

```
bundles-verbatim/   runtime bundles as they ship in the official asar
split/              file tree split at esbuild module path annotations
split-manifest.json per-segment declared path, byte offset, length
tools/split-bundles.mjs  deterministic splitter with lossless reassembly assertion
VERIFICATION.md     SHA-256 chain and reproduction steps
BN-NETT-ADDITIONS.md    what the reconstructed repo adds over this archive
```

13 bundles, 6561 module slices: 2357 first-party modules across 32 monorepo packages (`agent-core`, `agent-exec`, `mcp-core`, `prompt-jsx`, `shell-exec`, `redaction`, `redacted-protos`, …), 4204 third-party dependencies.

## Reading entry points

- `split/dist/node-agent-coordinator/main.cjs/packages/constants/dist/sand-box.js` — sandbox image tags, noVNC ports (6080/6081), websockify paths
- `split/dist/host/host-main.cjs/packages/agent/dist/prompts/claude-helpers.js` and `…/self-summary/anthropic-compaction-handler.js` — per-model prompt and compaction handling
- Model IDs visible via tree-wide grep: `cursor-0226`, `cursor-agent`, `claude-4.5-sonnet`, `claude-opus-4-8`, `grok-4.5`, `gpt-5`, `gemini-3.1-pro`
- `declaredPath` in `split-manifest.json` preserves Cursor CI build-machine paths (Buildkite job IDs, `pnpm-virtual-store`, `sand-release-build-*`)

## Verification

See [VERIFICATION.md](VERIFICATION.md) for the DMG → app.asar → bundle SHA-256 chain and the commands to reproduce this repo's contents from the official installer.

## Copyright

All code under `bundles-verbatim/` and `split/` is copyright **Anysphere, Inc.** This repository is an unmodified archival split of shipped binaries, for study only; it grants no rights to the code. Will be removed upon rights-holder request.
