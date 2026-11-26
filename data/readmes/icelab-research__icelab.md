# Ice Lab

[![typescript sdk](https://github.com/icelab-research/icelab/actions/workflows/publish-ts-sdk.yml/badge.svg)](https://github.com/icelab-research/icelab/actions/workflows/publish-ts-sdk.yml)

Ice Lab builds models and tools for media applications. This repository holds
the SDKs, documentation and example apps for two of its products:

- [Ice Lab API](https://icelab.sh/products/api): models and infrastructure for
  media ingest, processing, generation, captions and search.
- [RaidZero](https://icelab.sh/products/raidzero): observability for media
  applications.

[Explore our work](https://icelab.sh/products) · [Meet Ice Lab](https://icelab.sh/company) · [Contact](mailto:contact@icelab.sh)

## Contents

- [Installable SDKs](#installable-sdks)
- [Observability](#observability)
- [Example apps](#example-apps)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Installable SDKs

Use the package for the language you are building in. Most examples only call
external APIs after you copy the example `.env.example` to `.env` and set
`RAIDZERO_API_KEY`. Package names follow the current manifests; if a package is
not published yet, use the linked folder as a local path dependency or build
artifact.

| language                | package                                        | how to use it                                                                                                  |
| ----------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| TypeScript / JavaScript | [`@raidzero/media`](ts/sdk)                    | `pnpm add @raidzero/media@0.2.1` or `npm install @raidzero/media@0.2.1`                                        |
| Python                  | [`raidzero-media`](python)                     | `pip install raidzero-media==0.2.1`                                                                             |
| Go                      | [`github.com/icelab-research/icelab/go`](go) | `go get github.com/icelab-research/icelab/go@v0.2.1`                                                         |
| Rust                    | [`raidzero_media`](rust)                       | `cargo add raidzero_media@0.2.1`                                                                               |
| Java                    | [`java/`](java)                                | `icu.raidzero:raidzero-media-java:0.2.1`                                                                        |
| Kotlin                  | [`kotlin/`](kotlin)                            | `icu.raidzero:raidzero-media-kotlin:0.2.1`                                                                      |
| Elixir                  | [`elixir/raidzero`](elixir/raidzero)           | add `{:raidzero, "~> 0.2.1"}` to `deps`                                                                        |

The [C++ helper](cpp) is source-only.

## Observability

Every SDK supports prefixes, monitor CRUD, paginated monitor events, and an
`alert` helper that cleans up its temporary monitor when stopped. See the
[monitor lifecycle and failure contract](docs/sdks/observability.mdx).

Go services can also export process CPU capacity to SigNoz with
[`go-signoz`](go-signoz). Its README includes the metric and alert setup.

## Example apps

Start with the full examples index in [`apps/EXAMPLES.md`](apps/EXAMPLES.md).

| language                | example                                                        | what it shows                                                |
| ----------------------- | -------------------------------------------------------------- | ------------------------------------------------------------ |
| TypeScript / JavaScript | [`apps/fifteenlabs`](apps/fifteenlabs)                         | browser ingest/search demo                                   |
| Python                  | [`apps/cohere`](apps/cohere)                                   | sync and async SDK CLI usage                                 |
| Go                      | [`apps/livecart`](apps/livecart)                               | ingest, poll, search, asset listing, and soft delete         |
| C++                     | [`apps/chips`](apps/chips)                                     | example: calling the API from C++ with CPR and nlohmann/json |
| Java                    | [`apps/raidzero/java-example`](apps/raidzero/java-example)     | Spring Boot REST proxy using the Java SDK                    |
| Kotlin                  | [`apps/raidzero/kotlin-example`](apps/raidzero/kotlin-example) | Ktor REST proxy using the Kotlin SDK                         |
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
