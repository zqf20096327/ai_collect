# organize-my-iphone

[![CI](https://github.com/pacphi/organize-my-iphone/actions/workflows/ci.yml/badge.svg)](https://github.com/pacphi/organize-my-iphone/actions/workflows/ci.yml)
![Swift 6.2 or later](https://img.shields.io/badge/Swift-6.2%2B-F05138?logo=swift&logoColor=white)
![macOS 15 or later](https://img.shields.io/badge/macOS-15%2B-000000?logo=apple&logoColor=white)
![iPhone over USB](https://img.shields.io/badge/iPhone-over%20USB-0A84FF)
![Models run locally](https://img.shields.io/badge/models-run%20locally-2EA44F)

**Website:** [pacphi.github.io/organize-my-iphone](https://pacphi.github.io/organize-my-iphone/), with a phone you can click through to try each layout.

A command-line tool for macOS that reads the apps on a connected iPhone, sorts them into categories with a model that runs on your Mac, and proposes a tidier Home Screen. You review the proposals in a browser, apply the one you like, and can put the old layout back at any time.

It offers twelve ways to organize:

| Scheme | What you get |
| --- | --- |
| `category-pages` | Apps stay loose on pages, clustered by what they do: one cluster after another, or one category per page. |
| `folder-board` | One named folder per category, gathered on as few pages as possible. |
| `alphabetical` | A to Z across pages, or one folder per letter with `--letter-folders`. |
| `most-used` | Your most-used apps on page 1, the least-used at the back. |
| `time-of-day` | A Morning page (news, health), a Work day page, an Evening page (streaming, games) and Anytime. |
| `verb-folders` | Folders named for what you do: Talk, Watch, Listen, Make, Buy, Go, Track, Read, Play, Work. |
| `rainbow` | Pages sorted by each icon's main color. |
| `thumb-reach` | Most-used apps in the bottom rows, where your thumb reaches. |
| `places` | Home, Commute, Office, Travel, Gym and Everywhere pages, ready to pair with Focus modes. |
| `new-and-review` | Newest apps on page 1 for a trial run, apps you no longer use on a Review page. |
| `essentials` | One clean page of essentials. Everything else goes in folders on pages you can hide. |
| `life-areas` | Work, Money, Health, Family, Learning, Play and Everyday pages. |

`cfgutil` cannot tell how often you use an app, when you installed it, or what its icon looks like. The layouts that need those facts read them from optional files you write (`--usage`, `--recent`, `--icon-colors`). Without the files they fall back to your current icon order or put apps under "No color data", and they say so. For icon colors there is also an opt-in shortcut: `--icon-colors-from-store` finds each icon's main color from its App Store artwork, and a color-wheel page (`colors.html`) lets you fix any match by clicking. [docs/layouts.md](docs/layouts.md) covers each layout and the file formats.

## Status

Version 0.1.0 is a first cut. The logic is covered by unit tests, and CI runs the whole pipeline against a fake iPhone. It has been run end to end (scan, apply and restore) against one real iPhone so far. The ten layouts added after 0.1.0 (alphabetical through life-areas) have so far been applied only to the fake iPhone in `make demo`; each passes the same checks before `apply` will write it. Reading the phone is low risk. Writing a layout back relies on `cfgutil set-icon-layout`, which is known to behave differently across iOS versions, so use `apply --dry-run` first and keep the backups the tool makes.

## How it works

1. **Scan.** Apple Configurator's `cfgutil` lists the installed apps and the current icon layout over USB. The layout is backed up straight away.
2. **Enrich.** Apple's public iTunes Lookup API supplies each app's App Store genre and description. Skip this with `--offline`.
3. **Classify.** Built-in rules place the apps they are sure about (Apple's own, and apps whose store genre settles it). A local model decides the rest: Ollama if it is running, otherwise Apple's on-device model. With no model, rules place everything.
4. **Plan and preview.** All twelve layouts are built, checked against iOS limits, and written to an HTML page next to your current layout.
5. **Apply.** Only when you ask. The current layout is backed up first, and `restore` puts it back.

Every step shows a live timer. The target is under 2 minutes from scan to preview for a phone with 1,000 apps, and under 5 minutes to apply; [docs/architecture.md](docs/architecture.md#performance-budget) has the budget and what it rests on.

## Requirements

- macOS 15 or later on Apple silicon or Intel
- Xcode 26 or later (Swift 6.2 or later) to build
- [Apple Configurator](https://apps.apple.com/app/apple-configurator/id1037126344) from the Mac App Store, which contains `cfgutil`
- An iPhone connected by cable, unlocked, with this Mac trusted
- Optional: [Ollama](https://ollama.com) with a chat model pulled, or macOS 26 or later with Apple Intelligence turned on

## Quick start

```sh
git clone <your-repo-url> organize-my-iphone
cd organize-my-iphone

# 1. Check the setup
swift run organize-my-iphone doctor

# 2. Scan, classify, plan and preview. Changes nothing on the phone.
swift run organize-my-iphone run --open

# 3. See exactly what would change, then apply the proposal you prefer
swift run organize-my-iphone apply folder-board --dry-run
swift run organize-my-iphone apply folder-board

# Changed your mind?
swift run organize-my-iphone restore
```

Quit the Apple Configurator app before scanning. While its window is open it holds the phone and `cfgutil` reports the device as in use.

No iPhone handy? `make demo` runs everything against a fake one.

## Commands

| Command | What it does | Touches the phone? |
| --- | --- | --- |
| `doctor` | Checks for `cfgutil`, a connected iPhone and a local model | Reads |
| `run` | Scan, enrich, classify, plan and preview in one go | Reads |
| `scan` | Reads apps and layout, backs the layout up | Reads |
| `enrich` | Looks up App Store genre and description | No |
| `classify` | Sorts apps into categories | No |
| `plan` | Builds layout proposals | No |
| `schemes` | Lists the layouts and the data each one uses | No |
| `preview` | Writes the HTML comparison page | No |
| `apply <scheme>` | Writes a proposal to the phone, after a backup and a confirmation | **Writes** |
| `restore` | Puts a backed-up layout back | **Writes** |

Full options are in [docs/usage.md](docs/usage.md), or run any command with `--help`.

## Safety

- Nothing is written to the phone except by `apply` and `restore`, and both ask first.
- Every scan and every apply saves the current layout to `~/.organize-my-iphone/backups/` in `cfgutil`'s own format.
- A proposal is refused if it would drop an icon, duplicate one, or break an iOS limit (24 icons per page, 4 in the dock, 9 per folder page, 15 pages).
- The dock is never rearranged.
- Web clips and anything the tool does not recognize are carried over, not discarded.
- No layout removes an app from the Home Screen. `essentials` keeps everything else in folders on pages you can hide in iOS.

## Privacy

- The list of apps on your phone stays on your Mac, in `~/.organize-my-iphone` by default.
- `enrich` sends bundle identifiers (for example `com.spotify.client`) to Apple's lookup service and nothing else. `--offline` skips it.
- Only if you pass `--icon-colors-from-store`, the tool also downloads each app's icon from Apple's image server (`mzstatic.com`) to find its color. The images are read on your Mac and not kept. `--offline` skips it.
- Classification runs locally. No cloud model is called.
- The `--usage`, `--recent` and `--icon-colors` files are read on your Mac and never sent anywhere.

## Project layout

```
Sources/
  OrganizeCore/        Pure logic, no I/O: models, layout codec, classification, planning, rendering
  OrganizeAdapters/    The outside world: cfgutil, App Store lookup, Ollama, Apple's model, disk
  OrganizeCLI/         The command-line front end
Tests/
  OrganizeCoreTests/       Unit tests for the logic
  OrganizeAdaptersTests/   Unit tests with faked processes and HTTP, plus one real-subprocess test
  Fixtures/fake-cfgutil    A stand-in for cfgutil, used by tests, CI and the demo script
docs/                  Usage, architecture, product requirements, personae, journey, use cases
site/                  The project website, published to GitHub Pages
examples/              A sample custom taxonomy
scripts/demo.sh        End-to-end run against the fake iPhone
Makefile               Shortcuts for building, testing and running; `make` lists them
.github/               CI on macOS runners, release and Pages workflows, Dependabot
```

## Development

Run `make` to list every shortcut. The ones you will use most:

```sh
make test      # unit tests
make demo      # the whole pipeline against a fake iPhone
make check     # lint, tests and demo: what CI runs
make format    # reformat the Swift sources
make run ARGS="run --open"   # run the tool from source
```

Each target is a thin wrapper around SwiftPM. [docs/development.md](docs/development.md) lists every target, the command behind it, and the variables you can set.

CI runs the tests and the demo on GitHub's `xcode-27` (macOS 27, Swift 6.4) and `macos-26` runners. See [docs/architecture.md](docs/architecture.md) for how the pieces fit and how to add a classifier, a device transport or a layout scheme.

## Dependencies

| Dependency | Version | Used for |
| --- | --- | --- |
| [swift-argument-parser](https://github.com/apple/swift-argument-parser) | 1.8.2 or later | Command-line parsing |
| [swift-subprocess](https://github.com/swiftlang/swift-subprocess) | 1.0.2 or later | Running `cfgutil` |
| Swift Testing | Bundled with the toolchain | Tests |
| Foundation Models | Part of macOS 26 or later | Optional on-device classification |

Dependabot keeps the Swift packages and GitHub Actions current.

## Documentation

- [Usage](docs/usage.md)
- [Layouts](docs/layouts.md) (the twelve schemes and their optional data files)
- [Development](docs/development.md) (building, testing, the Makefile, CI)
- [Architecture](docs/architecture.md)
- [Product requirements](docs/prd.md)
- [Personae](docs/personae.md)
- [User journey](docs/user-journey.md)
- [Use cases](docs/use-cases.md)

## License

No license has been chosen yet.
