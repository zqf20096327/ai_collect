# modelXare: a decentralized AI model platform

**A few labs run the world's AI.** Every question you ask it, every document you paste in and every
idea you work through goes to their data centers, runs on their terms and at their prices, and may
train their next model. What people know is being poured into AI that a handful of companies own.

**It doesn't have to work that way.** Picture thousands of small models instead of one giant one,
each the best at one job and published by the people who know that job: a nurse, a translator, a
teacher, an engineer. A fast System 1 router sends every request to the right ones, and they run on
your own laptop or in a browser tab. Every new model widens what the whole catalog can do. The goal
is a global community of contributors covering every scenario, until together they match what
frontier models do: built by everyone, owned by no one.

**modelXare, by weXare, is where that starts.** Anyone can publish a model, or teach one what they
know, and anyone can find it, check where it came from and run it on their own device. No lab, no
account, no central registry, and what you type stays with you.

**Under the hood**, models are published as signed Nostr releases, stored on IPFS, torrents and
HTTP mirrors, collected by independent indexers into signed catalog snapshots, then searched,
verified and run on the person's own device: entirely inside the browser, or natively behind a
local OpenAI-compatible API. All of it runs end to end today;
[Known limitations](#known-limitations) lists what comes next.

- **Publish.** A CLI writes a manifest for real model files, signs a NIP-94 release event, and publishes it to two relays. Each relay's acknowledgment is reported separately.
- **Collect.** A restartable indexer watches several relays and deduplicates. It never claims coverage it did not get.
- **Archive.** A builder freezes the collected signed events into a ZIP, signs an announcement, and distributes it over IPFS, an HTTP mirror and a WebRTC-capable torrent.
- **Discover.** The browser app reads relays directly (Live), imports archives (Archives), or both (Combined), into SQLite WASM + FTS5 on OPFS. Searches stay on the device.
- **Run.** The browser downloads model files with source fallback, verifies every byte against the signed manifest, and runs GGUF models locally with wllama. It composes classification → summarization, and can apply a LoRA adapter at runtime.
- **Route.** In the simple app, a System 1 router works out every task a request asks for, and sends each step to a model on the device. The router is [Laya](https://github.com/wexare-ai/browser-laya), itself a signed catalog release. If the person adds their own API key, steps no local model can do go to an online model.
- **Run natively.** `pnpm modelxare` runs the same releases on your own machine with native llama.cpp and ONNX Runtime, with no browser memory limits. It serves them behind an OpenAI-compatible API (`http://127.0.0.1:8796/v1`) for agents and apps such as OpenCode, Hermes Agent and OpenClaw. Its `auto` model puts the System 1 router in front of the catalog's models: [Run models on your own machine](#run-models-on-your-own-machine).

There is no central registry, account or search API, and no remote inference unless a person turns on
online help with their own key. Anyone can run all of it:

- **On one machine**, with local relays, IPFS nodes and a file mirror in Docker: [Quick start](#quick-start).
- **On the internet, with your own domains**: the app on any static host, your releases on public
  Nostr relays, and later your own relay, IPFS gateway and file mirror on one server:
  [docs/deployment.md](docs/deployment.md).
- **On your laptop, for agents and apps**: the catalog's models behind a local OpenAI-compatible
  API, reading the public catalog, with no Docker: [Run models on your own machine](#run-models-on-your-own-machine).

See [docs/protocol.md](docs/protocol.md) for the data contract and [docs/acceptance.md](docs/acceptance.md)
for what has been verified, and how.

![The publisher, catalog operator and browser exchange signed metadata through Nostr relays and bytes through storage](docs/architecture.svg)

## Prerequisites

- Node.js 22.12 or later, below 23 (`.nvmrc` pins 22.22.2), and pnpm 11 (`corepack enable`). With
  nvm, run `nvm install && nvm use` in the repository. Newer Node versions print an "Unsupported
  engine" warning and are untested.
- Docker with Compose v2, for the two strfry relays, two Kubo nodes and the tracker of the local
  demo. It must be running before `pnpm infra:up`. The local runtime with the public catalog
  ([Run models on your own machine](#run-models-on-your-own-machine)) doesn't need it.
  - macOS: Docker Desktop, OrbStack or Colima. The pinned images support Apple Silicon.
  - Ubuntu: `sudo apt-get install -y docker.io docker-compose-v2 && sudo usermod -aG docker $USER`.
    The infra script falls back to `sg docker` until you log in again.
- About 10 GB of free disk for the demo. The pinned model fixtures total 1.87 GB, including the
  904 MB router, and they are copied into IPFS, the mirror and the browser. `pnpm install` also
  brings the local runtime's prebuilt llama.cpp and ONNX Runtime binaries: about 1 GB on Linux x64,
  where the CUDA and Vulkan builds are included, and less elsewhere.
- Network access the first time, to download the pinned fixtures from Hugging Face. No accounts are needed.
- Chrome or Chromium for the app; other browsers are untested. `pnpm --filter @wexare/tests exec playwright install chromium` provides one for tests.

## Quick start

```sh
pnpm install
pnpm infra:up          # relays A/B, Kubo A/B, tracker (docker compose; data volumes persist)
pnpm demo:prepare      # keys, fixture download + verification, releases, IPFS pins, torrents, synthetic catalog
pnpm dev               # developer app :5173, simple app :5174, indexer (operator A) :8791, artifacts mirror/seeder :8790
pnpm demo:publish      # in another terminal: publish to both relays, per-relay outcomes
pnpm catalog:build     # freeze operator A's indexer into a signed, seeded snapshot
```

Open <http://localhost:5173>, the developer app (`apps/web`). Releases appear under **Discover → Live**. To import the snapshot, go to
**Sources & diagnostics** and paste the announcement JSON that `catalog:build` printed (saved under
`.data/operators/a/archives/`), or look it up by event ID. To run the classification → summarization
workflow, use **Playground**. [docs/demo-script.md](docs/demo-script.md) walks through the full
demonstration, including relay failure, offline reload and a second operator.

For people without a technical background, open <http://localhost:5174> instead. That app
(`apps/simple`), shown as **modelXare by weXare** in the weXare brand, opens on a front page
that shows what modelXare is for: a before and after played by scrolling, from a few labs' data
centers to small models on everyone's own laptop, then one request played through System 1 (the
router decides) and System 2 (language models do the work) in the browser. **Try modelXare**
(`#/try`) lists models by what they
do, in the words their releases use (Summarize, Sort by topic, Continue the text, Write a git command). Opening a model gives you a text box and one button. The first
press downloads and checks the model, then it runs on the device. It uses the same engine as the
developer app but hides keys, hashes, relays and storage. It is a separate site, so it keeps its own
downloads. Its **What do you need?** box sends a request through the System 1 router; see
[Routing with System 1](#routing-with-system-1). **Xare your model**, next to the catalog, shows
how to publish a model of your own, with a starter file to fill in. Its first step is a visual guide
to training one: spec, data, LoRA/QLoRA training, eval, fuse, GGUF export, quantization, a tokenizer
check and a browser test, with common tools for each stage.

Models download when they are first needed, without a question. They stay saved until a new model
needs room, and then the ones used longest ago are removed first. They download again if needed
later. Room is made in two ways:

- **Before a download**, so that saved models stay within the space for models (4 GB by default,
  changeable in **Settings**) and within the space the browser says the site has left.
- **When the browser refuses the bytes anyway.** Some browsers, and private windows, misreport their
  space, so a download is always tried. If the browser runs out of space partway, the app takes how
  much it stored before refusing as the real room, removes models used longest ago to match, and
  retries once. Only then does it report that there isn't enough space, saying how much the browser
  really allowed.

The files of the model about to run, and the router's files during a request, are never removed.
Nothing is removed while another tab holds storage. The rule is `planEviction` in `@wexare/storage`.

The first `demo:prepare` downloads 1.87 GB and signs 10,000 synthetic records, which takes a few minutes.
Later runs reuse everything: unchanged manifests keep their signed events.

`pnpm dev` does not start the docker services. If the indexer logs `connection failed (is the relay
running? pnpm infra:up)`, start Docker, then run `pnpm infra:up`. It is safe to repeat, and it
prints a ✓ for each service once it answers. Relay and IPFS data live in docker volumes, so events
you published earlier are still there after a restart.

## Run models on your own machine

`pnpm modelxare` ([`apps/local`](apps/local)) runs the catalog's models natively, without the
browser's memory limits, and serves them behind an OpenAI-compatible API. It needs neither Docker nor
the demo services: with weXare's public settings it reads the public catalog and downloads the files
from Hugging Face.

```sh
pnpm install
pnpm modelxare --env infra/deploy/app.env.example list        # the catalog, and what is downloaded
pnpm modelxare --env infra/deploy/app.env.example pull auto   # the router and every model, about 1.9 GB
pnpm modelxare --env infra/deploy/app.env.example run auto "Categorize and summarize this message: Hi Sam, because of a storm your flight to Lisbon on Friday will leave two hours late, at 16:40. Your seat and bags stay the same."
pnpm modelxare --env infra/deploy/app.env.example serve       # http://127.0.0.1:8796/v1
```

- **Same trust as the apps.** It reads the same signed releases, lists only approved publishers
  (`infra/publishers.json`), and checks every file against its signed SHA-256: when it is
  downloaded, and again when a server first loads it. Without `--env` or `WEXARE_*` variables, it
  reads the local development relays and shows every validly signed release, like the apps.
- **Native engines.**
  - The GGUF models run on llama.cpp ([node-llama-cpp](https://node-llama-cpp.withcat.ai)), using
    Metal, CUDA or Vulkan when there is a GPU, else the CPU. Each model gets its full trained
    context, up to 32,768 tokens.
  - The System 1 router runs on native ONNX Runtime, with the browser build's request rendering and
    calibration.
- **The API.**
  - `GET /v1/models`.
  - `POST /v1/chat/completions`: streaming with usage, tools, and `json_object` or `json_schema`
    output.
  - `POST /v1/completions`.

  Model ids are the releases' `model_id`s (`community-assistant`, `tiny-summarizer`, `story-base`,
  `shakespeare-lora`, `git-commands`, `ffmpeg-commands`, `imagemagick-commands`), plus `auto`.
- **`auto`: System 1 + System 2 behind one model id.**
  - The router reads the last message, as in [Routing with System 1](#routing-with-system-1), and hands
    each task it asks for to the catalog model that does it.
  - There is no person to ask, so a task without a specialist, or a request the router isn't sure
    about, goes to a general chat model instead.
  - A `modelxare` field in the response says which path was taken.
- **Agents.** Point any OpenAI-compatible client at the base URL. [docs/local.md](docs/local.md)
  has settings for OpenCode, Hermes Agent and OpenClaw.
  - The catalog's models are small (15 to 500 million parameters). They are good for titles,
    summaries, sorting and simple tool calls, not as a coding agent's main model.
  - Hermes requires 64K tokens of context for its main model, so they fit only its auxiliary slots.
- **Safe defaults.**
  - It listens on `127.0.0.1`; any other address needs `--api-key`.
  - Requests from web pages on other sites are refused unless allowed with `--cors-origin`: bodies
    must be JSON, and only localhost `Host` names are accepted.
  - Requests and answers are never logged.

Models and releases are kept in `~/.local/share/modelxare` (Linux),
`~/Library/Application Support/modelxare` (macOS) or `%LOCALAPPDATA%\modelxare` (Windows), or
wherever `--home` says.
[docs/local.md](docs/local.md) has every command and option, the full API, how `auto` decides, and
measured speed and memory.

## Routing with System 1

**Try modelXare** (`#/try`) in the simple app opens with one box: **What do you need?** What a request
can ask for comes from the catalog, never from the app's code: every task the approved publishers'
models offer, described in each release's own words (its operations' `title` and `when`, see
[docs/protocol.md](docs/protocol.md#routing)). A release with a new task or category is routed to as
soon as it arrives. A request such as "Categorize and summarize this message: …" is handled like this:

1. The router (System 1) answers one multiple-choice question over those tasks, plus three general
   requests no model is assumed to do (answer a question, translate, draft a reply), so that "none of
   the models here" is a possible answer. It returns probabilities rather than text. With more than
   10 tasks, they compete in groups and the winners in a final question, because the router is
   calibrated for up to 10 options.
2. An instruction at the start (the part before a colon, or a first sentence that is a question with
   more text after it) that names several tasks is read part by part: "Categorize this message" and
   "summarize this message". One choice finds one task, and the router's yes/no and "what else?"
   questions proved unreliable for a second. A part of one or two words counts only at 90 %, so "the
   pros and cons" doesn't leave a task called "cons". Only the instruction is read, so a message that
   mentions other tasks ("Can you translate the notice?") doesn't add them.
3. A request without an instruction, or with no clear part, is read whole. A task at 50 % or more
   becomes a step; if none is, the person picks from the likeliest three. At most three steps run,
   the first ones asked for.
4. When several models offer a task in different words, the router also picks the one that fits the
   request best; otherwise a model already downloaded comes first, then the smallest. Add-ons run
   their own prompt on their base's weights, so the git, ffmpeg and ImageMagick command writers, each
   about 6 MB, share the Message assistant's 491 MB model. Each release's prompt decides what its
   model reads: the whole request, or the text after the instruction.
5. A model that answers that a request is outside what it does (its `decline`, such as
   `UNSUPPORTED`) hands the step to the next likeliest task, then to online help. Online help gets
   the whole request, which may name a language, and is used only for steps no local model can do,
   and only when the person has turned it on. Otherwise the step is reported as unavailable, in
   plain words.
6. **How this was decided** lists what the router read, what it took each part for and how sure it
   was, and which model it picked when there was a choice.

Against the real router release, with the sample releases in the catalog (the command add-ons
included), this plans all 39 requests in `tests/integration/router-laya.test.ts` correctly, multi-step
ones included.

Releases share a task ID when their models can stand in for each other: any summarizer will do, so
a downloaded one or the smallest runs, unless their `when` sentences differ and the router prefers
one for the request. Models that can't stand in for each other take different IDs: the git, ffmpeg
and ImageMagick command writers are `git-command`, `ffmpeg-command` and `imagemagick-command`, each
described by its own `when`.

The router is a catalog release like any model: `fixtures/releases/laya-router.json` publishes the
ONNX export of Laya (`wexare/laya-onnx`, pinned revision) with `runtime.family: "laya"` and the
`intent-routing` capability. Its four files (weights, tokenizer, tokenizer config, calibration) are
downloaded the first time a request needs them, verified, and checked again before loading, like
every model file. Clients that don't bundle `@wexare/laya-web`, such as the developer app, list it as
unsupported. `modelxare` runs the same release with native ONNX Runtime.

**Online help** (Settings) takes any OpenAI-compatible service: OpenRouter, OpenAI, or a custom
address. The API key is kept in this browser's local storage only and sent only to that service.
The app says on screen when online help is on, and each answer shows which model produced it and
where.

## Commands

| Command | What it does |
| --- | --- |
| `pnpm install` | Install the pinned workspace dependencies |
| `pnpm infra:up` / `pnpm infra:down` | Start, or stop, the docker services. `down` keeps volumes. |
| `pnpm demo:prepare` | Generate demo keys, fetch and verify fixtures, and populate the mirror, IPFS (with replicas on Kubo B) and torrents |
| `pnpm dev` | Web app, simple app, indexer and artifacts mirror/seeder, with live logs |
| `pnpm demo:publish` | Publish every fixture release (and the negative fixture) to both relays |
| `pnpm catalog:build` | Build, sign, publish and seed a snapshot from operator A's indexer database |
| `pnpm test` | Fast unit tests: protocol, catalog and golden queries, storage, runtime, orchestrator, router, collector, the local runtime's API |
| `pnpm test:e2e` | Browser and service acceptance tests against the real services (see below) |
| `pnpm test:models` | Opt-in real-model browser tests. They download about 0.9 GB into the browser. |
| `pnpm build` | Static web builds (`apps/web/dist`, `apps/simple/dist`) and bundled programs (`apps/*/dist`, including `apps/local/dist/main.js`, the `modelxare` command) |
| `pnpm demo:reset --force` | Delete the demo data under `.data/`. `--volumes` also deletes relay and IPFS data, and `--downloads` the fixture models. Without `--force` it only lists what it would delete. |
| `pnpm cli <args>` | The publisher/builder CLI (`wexare --help`) |
| `pnpm modelxare <args>` | The local runtime: `list`, `pull`, `run`, `serve` (the OpenAI-compatible API) and `rm`. See [Run models on your own machine](#run-models-on-your-own-machine) |

### Tests

- `pnpm test` needs nothing running.
- `pnpm test:e2e` and `pnpm test:models` need `pnpm infra:up` and `pnpm demo:prepare`. Playwright
  starts the artifacts server (reusing one on :8790) and a production build served by `vite preview`
  on :4173, with the service worker. Tests start their own indexers on :8793 to :8795, with data under
  `.data/e2e/<run>/`. Evidence is written as JSON to `tests/results/<ID>.json`, where the ID is one
  of the checks listed in [docs/acceptance.md](docs/acceptance.md). The e2e run stops and restarts the
  relay containers for the relay-failure check (A16), and publishes labeled synthetic records to both
  relays for the bounded-collection check (A17).
- `pnpm vitest run --project integration` runs the Node-side checks against the same services. The
  mirror and torrent checks also need the artifacts server on :8790, which `pnpm dev` starts.
  `WEXARE_TEST_ARWEAVE=1` adds the public Arweave gateway test, which needs internet access.
- `WEXARE_TEST_LOCAL=<data folder>` runs `apps/local/test/real-models.test.ts`: the local runtime's
  API with the real models already pulled into that folder (`pnpm modelxare pull auto`). It needs
  about 4 GB of free memory.
- `WEXARE_TEST_LAYA=1` turns on the checks that load the real router:
  `tests/integration/router-laya.test.ts` (routing decisions, Node) and `tests/models/router.spec.ts`
  (the Ask box end to end). They need about 4 to 5 GB of free memory, so they are off by default.
  `WEXARE_TEST_LAYA=native` runs the routing decisions on the local runtime's native router instead:
  about 2.5 GB, and no running services, only the router release and files `pnpm demo:prepare` put
  in `.data/`.

## Repository layout

| Path | Contents |
| --- | --- |
| `packages/protocol` | Schemas, canonical JSON, event and manifest verification, tag rules, operation output shapes, test vectors |
| `packages/catalog` | Shared SQLite schema, FTS5 queries, source membership, archive build/read, operator state |
| `packages/storage` | Source resolution, verified downloads (Node and browser), IPFS client, mirror layout, torrents |
| `packages/runtime` | Capability detection, wllama runtime wrapper (including the LoRA adapter path), GGUF header reader |
| `packages/orchestrator` | Release selection, two-stage workflow planning and execution, LoRA dependency resolution |
| `packages/router` | System 1 routing: the catalog's tasks, the step-by-step loop, local-first routes, online help, router release selection |
| `apps/cli` | `wexare`: keys, `release prepare/publish`, `archive build/verify/publish`, `demo …` |
| `apps/indexer` | Persistent multi-relay collector with a read-only status endpoint |
| `apps/artifacts` | Static HTTP mirror (range, CORS, immutable caching) and WebRTC torrent seeder |
| `apps/web` | The developer app: Discover, Model library, Playground, Sources & diagnostics, with every key, hash and source on screen |
| `apps/simple` | The plain-language app: find a model by task and use it, built on the `apps/web` engine |
| `apps/local` | `modelxare`: catalog models on native llama.cpp and ONNX Runtime, behind an OpenAI-compatible API, with `auto` (System 1 + System 2) |
| `infra/` | Docker Compose for strfry ×2, Kubo ×2 and the WebSocket tracker, with images pinned by digest |
| `fixtures/` | Pinned upstream model fixtures, release definitions, sample messages, the Arweave fixture |
| `tests/` | Playwright acceptance (`e2e/`, `models/`), integration tests, the runtime compatibility spike |
| `docs/` | Protocol, deployment guide, local runtime and API guide, demo script, acceptance checklist, runtime compatibility report |

## Running components separately

Every component reads its endpoints from flags. The defaults are in `infra/dev-endpoints.json`, and
none of them is required by the protocol.

- **Developer app only:** run `pnpm --filter @wexare/web build` and serve `apps/web/dist` from any static host
  that sends `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy:
  require-corp`; those headers enable multithreaded inference. Relays, gateways, trackers and
  trusted catalog builders are configured in **Sources & diagnostics** and can be exported or imported
  as public JSON.
- **Simple app only:** run `pnpm --filter @wexare/simple build` and serve `apps/simple/dist` with the
  same two headers. Its addresses are built in. With no `WEXARE_*` variables, it uses the local
  services in `infra/dev-endpoints.json` and shows every validly signed release. A deployment sets its
  own addresses in environment variables (`infra/deploy/app.env.example`) and shows only the
  publishers approved in `infra/publishers.json` (weXare's key, for weXare's deployment; yours lists
  your own); the build stops if a setting is wrong.
- **Publisher CLI only:** `pnpm cli keygen --out my.key.json`, then `pnpm cli release prepare --definition
  def.json --key my.key.json --out out/ --ipfs-api http://… --mirror-url https://…`, then
  `pnpm cli release publish --event out/event.json --relay wss://…`.
- **Indexer only:** `node apps/indexer/dist/main.js run --data /srv/wexare/op --name my-operator
  --relay wss://… --port 8791`.
- **Archive build only:** `pnpm cli archive build --indexer-db /srv/wexare/op/indexer.sqlite --builder-key
  builder.key.json --relay wss://… --out archives/`, then optionally `pnpm cli archive publish --zip …`.
  `--events <file>` builds from preserved signed event files, with no indexer.
- **Mirror and seeder only:** `node apps/artifacts/dist/main.js --roots-dir /srv/wexare/artifacts --port
  8790` (add `--no-seed` for HTTP only).
- **Local runtime only:** after `pnpm --filter @wexare/local build`, run `node apps/local/dist/main.js
  --env <settings file> serve` (the same commands as `pnpm modelxare`). It reads the same `WEXARE_*`
  settings as a deployed app, plus its own `WEXARE_LOCAL_*` ones (`HOME`, `HOST`, `PORT`, `API_KEY`
  and more; see [docs/local.md](docs/local.md)).

## Ports (local demo)

| Service | Port |
| --- | --- |
| Relay A (strfry, limit 500) / relay B (strfry, limit 50) | 7777 / 7778 |
| Kubo A API / gateway | 5001 / 8080 |
| Kubo B API / gateway | 5002 / 8081 |
| WebSocket tracker | 8000 |
| Artifacts mirror + seeder | 8790 |
| Indexer operator A / B (status only) | 8791 / 8792 |
| Web app (dev / preview) | 5173 / 4173 |
| Simple app (dev / preview) | 5174 / 4174 |
| Local runtime API (`pnpm modelxare serve`) | 8796 |

## Data and keys

All runtime state is under `.data/`, which is ignored by git. That covers keys (mode 0600), fixture
models, published releases, artifact roots, indexer databases, archives and synthetic data. Model
binaries, private keys, archives and databases never belong in the repository. The demo keys are
disposable. Private keys stay in the CLI and never reach the browser.

The local runtime keeps its own data outside the repository, in the folder given in
[Run models on your own machine](#run-models-on-your-own-machine): `releases.json` (signed release
events, verified again whenever they are read) and `files/sha256/<hash>`. It holds no keys.

## Known limitations

- Only one tab at a time uses the local catalog, because the OPFS SQLite VFS holds exclusive
  handles. Opening the app in a new tab moves the catalog there, and the previous tab offers **Use
  here**. If storage still can't be opened, the app says why, falls back to an in-memory catalog, and
  offers **Reset local data**.
- The indexer resumes from a `created_at` cursor. A running indexer receives every new event, but if
  an event signed long before it is published arrives while the indexer is stopped, only a rescan
  collects it: `curl -X POST http://127.0.0.1:8791/rescan`.
- Peers-first torrent transfer needs a seeder that has finished hashing. The HTTP web-seed fallback,
  4 s by default and configurable, keeps imports usable meanwhile.
- Runtime LoRA execution relies on a wllama 3.8.1 internal. Any other version shows "Adapter execution
  unavailable in this runtime"; see [docs/runtime-compatibility.md](docs/runtime-compatibility.md).
- Gateway availability, storage retention and browser P2P connectivity are separate concerns. A pinned
  CID or a seeded torrent says nothing about whether a particular gateway or peer is reachable.
- The router (Laya fp16) is English only. Loading it takes about 3 GB of memory on top of the page.
  Its routing decisions were checked with native ONNX Runtime (and run natively by `modelxare`), but
  not yet in the browser: the 8 GB test machine could not load it there safely. Run the `WEXARE_TEST_LAYA=1` checks on a larger machine.
- The simple app's offline cache includes the router's 28 MB WebAssembly runtime, even if routing is
  never used.
- The local runtime runs one request at a time; the others wait their turn. It doesn't load models
  split into several GGUF files yet, and downloads over https, IPFS and Arweave but not torrents. It
  was checked on Linux x64 with 4 cores, 8 GB of memory and no GPU; macOS, Windows and GPUs are
  untested.
  The agent settings in [docs/local.md](docs/local.md) follow each project's documentation, but only
  raw HTTP and the official OpenAI SDK were run against the server.
- Not implemented yet: Arweave uploads (only `ar://` resolution is implemented),
  incremental or sharded catalogs, and browser publishing with a Nostr signer.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) to set up, test and send changes. Report vulnerabilities
privately as described in [SECURITY.md](SECURITY.md). Contact: hello@wexare.com.

## License

Copyright 2026 weXare. Licensed under [Apache-2.0](LICENSE); see [NOTICE](NOTICE).

The license doesn't cover the weXare and modelXare names or logos: a fork or product built from
this code may say it is based on modelXare, but uses its own name and logo. Model fixtures keep
their upstream licenses; see `fixtures/models.json`.
