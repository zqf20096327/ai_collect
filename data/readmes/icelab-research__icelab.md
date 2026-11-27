# Ice Lab

[![Ice Lab](docs/logos/ice-lab-banner.png)](https://icelab.sh)

Ice Lab makes your videos searchable through one API. This repository holds
the SDKs, documentation and example apps for the Ice Lab API:

- [Ice Lab API](https://icelab.sh/products/api): models and infrastructure for
  media ingest, processing, generation, captions and search.

[Explore our work](https://icelab.sh/products) · [Meet Ice Lab](https://icelab.sh/company) · [Contact](mailto:contact@icelab.sh)

## Contents

- [Installable SDKs](#installable-sdks)
- [Example apps](#example-apps)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Installable SDKs

Use the Ice Lab SDK for your language to ingest media and search it. Follow
its installation guide for the current package name and setup. For examples,
copy `.env.example` to `.env` and configure the API key as documented there.

| language | SDK | installation |
| --- | --- | --- |
| TypeScript / JavaScript | [Ice Lab TypeScript SDK](ts/sdk) | [Installation guide](ts/sdk/README.md) |
| Python | [Ice Lab Python SDK](python) | [Installation guide](python/README.md) |
| Go | [Ice Lab Go SDK](go) | [Installation guide](go/README.md) |
| Rust | [Ice Lab Rust SDK](rust) | [Installation guide](rust/README.md) |
| Java | [Ice Lab Java SDK](java) | [Installation guide](java/README.md) |
| Kotlin | [Ice Lab Kotlin SDK](kotlin) | [Installation guide](kotlin/README.md) |
| Elixir | [Ice Lab Elixir SDK](elixir/icelab) | [Installation guide](elixir/icelab/README.md) |

The [C++ helper](cpp) is source-only.

## Example apps

Start with the full examples index in [`apps/EXAMPLES.md`](apps/EXAMPLES.md).

| language                | example                                                        | what it shows                                                |
| ----------------------- | -------------------------------------------------------------- | ------------------------------------------------------------ |
| TypeScript / JavaScript | [`apps/fifteenlabs`](apps/fifteenlabs)                         | browser ingest/search demo                                   |
| Python                  | [`apps/cohere`](apps/cohere)                                   | sync and async SDK CLI usage                                 |
| Go                      | [`apps/livecart`](apps/livecart)                               | ingest, poll, search, asset listing, and soft delete         |
| C++                     | [`apps/chips`](apps/chips)                                     | example: calling the API from C++ with CPR and nlohmann/json |
| Java                    | [Ice Lab Java example](apps/icelab/java-example)     | Spring Boot REST proxy using the Java SDK                    |
| Kotlin                  | [Ice Lab Kotlin example](apps/icelab/kotlin-example) | Ktor REST proxy using the Kotlin SDK                         |
| Elixir                  | [`apps/resto_booking_app`](apps/resto_booking_app)             | Phoenix restaurant booking app for The Seasons               |
| Elixir                  | [`apps/ellie_ai`](apps/ellie_ai)                               | voice AI that answers the booking line for that app          |
| Rust                    | [`rust`](rust)                                                 | SDK source package; no standalone app example yet            |

## Documentation

Start with the [quickstart](docs/quickstart.mdx) or the
[SDK overview](docs/sdks/overview.mdx). Each SDK directory contains its API,
installation, and build instructions.

## Contributing

This repository is maintained through an automated source export. Open issues
and pull requests here; accepted changes are included in a subsequent export.
