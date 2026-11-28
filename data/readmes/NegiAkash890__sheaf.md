# Sheaf

![Downloads](https://img.shields.io/github/downloads/NegiAkash890/sheaf/total?label=downloads&color=285f50) ![Stars](https://img.shields.io/github/stars/NegiAkash890/sheaf?style=flat&color=285f50) ![Status](https://img.shields.io/badge/status-public%20beta-b8860b)

**Messy folders, turned into tidy collections.** Sheaf is a free Mac app that reads what is inside your files, groups the ones that belong together, and lets you find anything by person, place, thing or idea instead of by file name. You approve every move and can undo it. The AI runs on your Mac.

![Before: a messy Downloads folder in Finder. After: the same kind of folder in Sheaf, every file in a collection named for what it holds](screenshots/before-after.png)

![Sheaf sorting a messy folder: every file is placed in a collection named for what it holds](screenshots/library.png)

> **The source goes public at 100 stars.** It is private for now. When this repository reaches 100 stars, the source code is published so anyone can read it and build on it. A star is how you vote for that. Until then, [PRIVACY.md](PRIVACY.md) and [how to verify it yourself](docs/VERIFY-PRIVACY.md) list what you can check.

- **Local only.** No account, no cloud, no telemetry. The only network connection is to the model server on your own Mac.
- **Never moves anything without your approval.** Every change is journaled and can be undone.
- **Knows what kind of file it is.** A CV, a job description, an ID card, a photo of you, a trip photo, a licence file: each stays with its own kind.
- **Explains itself.** Every relationship, collection and proposed move comes with the reason.
- **Free.** No subscription, no ads.

## How it works

1. **Add a folder.** Sheaf reads it without changing anything.
2. **Sheaf reads it.** Small AI models on your Mac read text, PDFs, Word files and text inside images, link files that mean similar things, and name each collection.
3. **You review the plan.** Sheaf proposes folders and clearer names with a reason for each move. Untick what you disagree with, apply the rest, undo with one click.

| Collections | Graph |
|---|---|
| ![Collections](screenshots/collections.png) | ![Graph](screenshots/graph.png) |
| **Search by meaning** | **Organise** |
| ![Search](screenshots/search.png) | ![Organise](screenshots/organise.png) |

## Requirements and install

| | |
|---|---|
| Mac | Apple Silicon (M1 or later) |
| macOS | 14 Sonoma or later |
| Model runner | [Ollama](https://ollama.com), free. Setup installs it if you do not have it |
| Download, once | Bigger 2.4 GB or Light 1.6 GB (see below) |
| First open | Not signed by Apple yet: macOS asks you to choose **Open Anyway** |

1. Download the DMG and its `.sha256` file from [Releases](../../releases/latest). Check it: `shasum -a 256 -c Sheaf-<version>-arm64.dmg.sha256`
2. Drag Sheaf to Applications.
3. The app is **not signed or notarised yet**, so macOS blocks the first launch. Open System Settings > Privacy & Security and choose **Open Anyway**. Details in [docs/INSTALL.md](docs/INSTALL.md).
4. Open Sheaf and pick a folder. Choose a model size, and setup installs Ollama if needed and downloads the models. Reading starts as soon as the search model is in; collections are named when the writing model arrives. Meanwhile you can try every screen on sample files.

### Bigger or Light

Setup and Settings both let you choose the writing model, which names your collections. It does not decide which files belong together.

![Settings: Bigger (Recommended) and Light (Quicker)](screenshots/model-size.png)

- **Bigger (Recommended):** about 2.1 GB. More specific collection names. A little slower and uses more memory.
- **Light (Quicker):** about 1.25 GB. Smaller and faster. Collection names are more general.

You can switch any time in Settings; the other size downloads when you pick it. Both are Apache-2.0 models from IBM. See [docs/MODELS.md](docs/MODELS.md).

## Privacy

Your files and their contents never leave your Mac. See [PRIVACY.md](PRIVACY.md) for what Sheaf does on the network, and [how to verify it yourself](docs/VERIFY-PRIVACY.md).

## Documentation

- [Installing Sheaf](docs/INSTALL.md)
- [FAQ](docs/FAQ.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Models](docs/MODELS.md)
- [Roadmap](ROADMAP.md) and [Changelog](CHANGELOG.md)

## Feedback

Bugs, wrong groupings and ideas are very welcome: [open an issue](../../issues/new/choose). Describe files rather than attaching them. See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to help and [SECURITY.md](SECURITY.md) for reporting vulnerabilities privately.

Licence: [free to use](LICENSE.txt).
