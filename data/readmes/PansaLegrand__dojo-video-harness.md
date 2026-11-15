# Dojo Video Harness

[![CI](https://github.com/PansaLegrand/dojo-video-harness/actions/workflows/check.yml/badge.svg)](https://github.com/PansaLegrand/dojo-video-harness/actions/workflows/check.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**An open-source video editor you run locally, with a TypeScript agent you can understand and extend.** Import your footage, edit the same timeline by hand or through chat, and export an MP4 in your browser. Ordinary validated chat edits apply directly; Compare and Undo let you inspect or reverse them.

**Want to try the hosted product? [Open DojoClip Video Edit AI](https://dojoclip.com/en/applications/video-edit-ai).** DojoClip adds managed accounts, projects, provider jobs, storage, and payments. This repository is the smaller local editor and developer foundation; it does not install the commercial SaaS.

![The local editor with a structured pending question](docs/assets/editor-question.png)

_Browser-test screenshot with synthetic model responses._

## Choose the right project

| Project                                                                | Use it for                                                                        | What you operate                                             |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **This harness**                                                       | Edit local footage, study the agent, add tools or skills                          | A single-user localhost app; your own optional provider keys |
| [Dojo Video Engine](https://github.com/PansaLegrand/dojo-video-engine) | Build scene rendering, playback, inspection, and export into your own application | TypeScript packages and browser media APIs                   |
| [DojoClip](https://dojoclip.com/en/applications/video-edit-ai)         | Use the hosted editor and managed AI services                                     | An account in the commercial product; no local server setup  |

The harness includes the shared editor UI, command validation, timeline history, captions, editable graphics, browser preview/export, and a bounded model/tool loop. It deliberately excludes commercial authentication, billing, Postgres/Prisma, Redis queues, cloud-storage configuration, production workers, and deployment credentials. Local image/video-generation adapters are not shipped; the optional BYOK music adapter is available.

No DojoClip database or commercial environment file is needed. Projects and receipts use local files; imported originals use browser IndexedDB. The UI is English-only, while media text and provider-supported captions can use other languages. See [the scope and synchronization policy](docs/open-source-scope.md).

## Run locally

Requirements: Git, Node **20.19+** (Node **22** recommended), npm, and a desktop browser with WebCodecs support. Chromium is the tested path. FFmpeg is only needed for acceptance tests.

```sh
git clone https://github.com/PansaLegrand/dojo-video-harness.git
cd dojo-video-harness
npm run launch
```

`launch` installs locked dependencies when missing, creates `.env` without overwriting an existing file, checks the environment, and starts the editor. It opens a browser from an interactive terminal; otherwise open **http://127.0.0.1:4310**. The published engine packages install automatically. No sibling repository or pnpm installation is needed.

Create a project and import a short clip. **Manual editing, subtitle import, preview, and MP4 export need no API keys.** For chat or speech recognition, open **Provider settings** and configure the relevant provider below.

```sh
npm run dev                # Start again after initial setup
npm run setup -- --install # Install updated locked dependencies after git pull
npm run doctor             # Check Node, local storage, and port availability
npm run dev -- --no-open    # Start without opening the browser
```

The launcher supports PowerShell, macOS, and Linux. Keep the same local address: browser media belongs to its origin. An occupied port produces guidance rather than silently switching addresses. To run a production build locally, use `npm run build` then `npm start`.

## Try these workflows

These examples use capabilities exercised by the repository's tests. Chat wording is a starting point: inspect the resulting edit, and use Undo or a follow-up instruction when needed. See [verification](#verification) for the distinction between scripted tests and live-model evidence.

### 1. Make a short branded clip — no keys

1. Create a project and import a video plus a PNG logo you own.
2. Trim the imported clip on the timeline. Move the imported logo to an overlay track and align its timing with the footage.
3. Add a text title or import an SRT/VTT subtitle file.
4. Preview, adjust the placement, then export MP4.

This is a local editing workflow. It needs neither an AI provider nor an account. Rendering and export run in the browser; supported media depends on browser codecs and admission limits.

### 2. Revise a title through conversation — GPT key

In an open project, choose **Whole project** scope and ask:

> Add a title saying “Hello” for the first three seconds.

Then send each follow-up separately:

> Make it red.

> Put a yellow backing behind it.

> Make the text bigger.

The title stays editable on the timeline. Ordinary local edits apply automatically; Compare and Undo remain available. The [bounded correction diagnostic](docs/conversational-corrections-2026-11-04.md) records a tested four-turn version of this workflow, including preserved object identity and rendered changes.

### 3. Caption and translate a speech clip — GPT and ASR keys

Import a short spoken clip, choose **Whole project** scope, and ask:

> Add English captions to this clip, then add Spanish translations below them. Keep the original English captions.

If transcript evidence is missing, the app requests source/provider consent before transcription and then continues the original instruction. Review timing, wording, and translated facts before export. Transcription uploads are capped at **25 MiB** and require genuine word timestamps. Already imported subtitle text can be edited manually without an ASR key.

For an explicit multi-clip workflow, import two spoken clips named `Clip A` and `Clip B` without existing linked captions, then ask:

> Join Clip A then Clip B, generate English captions, translate them to Spanish, then export.

That workflow has its own review card: approve provider access, review and apply the prepared edit, then use **Export approved workflow**. The saved export is bound to the applied revision. See [workflow behavior and evidence](docs/basic-workflows-and-music-2026-11-03.md).

### 4. Add an editable intro or ending — GPT key

With footage on the timeline, ask:

> Add a three-second 3–2–1 countdown before my footage. Move the footage after the countdown and keep its full duration.

Or:

> Add a two-second animated “Thanks for watching” ending after my footage.

These can be native grouped graphics with editable text and animation. They do not require generating another video asset. You can move, trim, split, or edit the graphic and export it with the footage. Trimming cuts animation beats; it does not automatically retime them or ripple neighboring clips. See [the intro/outro tests and limitations](docs/intro-outro-items-2026-11-04.md).

### Optional: generate background music — Kie key

Configure **Background music · Kie** in `/en/settings`, then use the Background music panel or ask through chat. The panel works without a GPT key. **Generate and insert music** approves one paid job and its displayed placement, length, and volume. The first returned track is stored locally and inserted when ready. Undo removes an edit; it does not repeat generation or refund a provider charge. See [music setup and recovery](docs/basic-workflows-and-music-2026-11-03.md).

## Configure only the providers you need

| Operation                                          | Credentials                           |
| -------------------------------------------------- | ------------------------------------- |
| Manual edits, subtitle import, preview, MP4 export | None                                  |
| Chat edits and caption translation                 | Your compatible GPT Responses API key |
| Speech transcription                               | Your ASR key, configured separately   |
| Optional instrumental music generation             | Your Kie music key                    |

Use **Provider settings** to enter the base URL, exact model ID, and matching key. Settings take effect for new requests; active jobs keep their original configuration. Advanced defaults can use [`.env.example`](.env.example), copied to your private `.env`. App settings override those defaults.

The chat adapter supports **GPT models through the Responses API with function calls and tool-result continuation**. Vercel AI Gateway is one documented provider example:

```dotenv
LLM_BASE_URL=https://ai-gateway.vercel.sh/v1
LLM_MODEL=openai/gpt-6-sol
LLM_API_KEY=your-vercel-ai-gateway-key
```

Other compatible endpoints can use the same adapter. Supply the base URL without `/responses` and a model ID in `gpt-*` or `openai/gpt-*` form. Availability and compatibility depend on your provider/account; a listed model name alone is not a compatibility guarantee. Non-GPT model families and Chat Completions are outside the shipped adapter's scope. There is no silent provider switching or automatic paid retry.

Speech recognition supports OpenAI-compatible word-timestamp endpoints and ElevenLabs Scribe. The **Use ElevenLabs** preset selects `https://api.elevenlabs.io/v1` and `scribe_v1`; enter your own ElevenLabs key. Segment-only output is rejected rather than converted into invented word timings. Music defaults are documented in `.env.example`.

Saved keys stay in the local server's private data directory and are never returned to the browser. Keep `.env` and `DATA_DIR` private and out of Git. Chat sends project context to your configured provider. Transcription sends the consented source; preview pixels require consent. Remote provider usage is billed by that provider. The local host is intended for a single user on loopback, not deployment as a public multi-user service.

## How it works and what stays synchronized

```text
Manual controls ─┐
                 ├─ validated commands → ProjectDocument → compiled Scene → engine
Chat + tools ────┘
```

Both editing paths share the document and history. The host validates scope, source evidence, locks, and revisions before applying an edit. The agent can inspect sources, read skills, ask structured questions, and prepare dependent stages. Registered browser tools support consented source sampling, candidate previews, one verified correction round, and export tied to the applied revision.

The current local profile is **local-editor-v14**, using **agent kit 0.2.9**, **loop 0.2.0**, and published **engine 1.2.3**. Older saved runs retain their original behavior and budgets. The latest shared editing behavior is reused by the commercial host through its own adapters; commercial services are not copied into this app.

- **Web → harness:** selected editor components, managed and checked by file hashes.
- **Engine → both apps:** published rendering/playback/export packages at exact versions.
- **Harness → commercial host:** portable agent loop, tool contracts, and skills.
- **Editing semantics:** some shared helpers plus separate kernels checked against the same conformance cases; there is no automatic whole-product sync. [Remaining differences](docs/open-source-scope.md#remaining-source-differences) include a bounded capability-target schema description gap.

See [the scope policy](docs/open-source-scope.md), [synchronization evidence](docs/synchronization-readiness-2026-11-08.md), and [UI sync instructions](docs/syncing-product-ui.md).

## Learn or extend the implementation

Start with [the guided walkthrough](docs/learn-the-harness.md) and [architecture](docs/architecture.md). Coding agents should read [AGENTS.md](AGENTS.md).

| Location                                             | Responsibility                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------------- |
| `packages/agent-loop/`, `packages/agent/src/loop.ts` | Bounded model → tool → observation loop and local integration       |
| `packages/agent-kit/`, `packages/agent/src/tools.ts` | Shared tool definitions, skills, and native host ports              |
| `skills/`                                            | Trusted Markdown guidance for existing tools                        |
| `packages/core/src/lib/video-project/`               | Document, validated commands, source evidence, and history          |
| `packages/adapters/src/`                             | GPT, ASR, and music transports                                      |
| `packages/ui/src/host/`                              | Local user, copy, and provider adapters                             |
| `apps/server/src/`                                   | Local files, durable runs, consent, provider settings, and receipts |

A useful first extension is a read-only tool that counts clips on a track. Or add a trusted lowercase `skills/name.md` file and restart the host. Markdown guides registered tools; it cannot install executable code or authorize spending. Follow [the extension guide](docs/extending.md).

Harness packages are source workspaces here, not a published embeddable SDK. Engine packages are published separately. Durable recovery retains completed replies and receipts; uncertain paid submissions need reconciliation. See [the current agent map](docs/agent-system.md) and [edge cases](docs/edge-cases.md) for exact limits.

## Verification

```sh
npm run check                    # OSS boundary, integrity, types, tests, build
npx playwright install chromium
npm run test:browser              # Actual browser/media tests; needs ffmpeg + ffprobe
```

The browser suite uses synthetic provider HTTP responses while exercising real UI, storage, rendering, and decoded MP4/audio. It does not spend provider credits or use `.env` keys. Test artifacts go to ignored `test-results/`.

The [readiness ledger](docs/readiness-progress.md) records version-specific local checks, public CI, separate live-model evaluations, retained failures, and remaining coverage. [The agent map](docs/agent-system.md) identifies the current build. These records do not establish universal creative quality or support for every codec, browser, provider, or arbitrarily long instruction.

Live provider probes are opt-in and incur your provider's charges; see [milestone testing](docs/agent-milestone-testing.md) before running them. The full release checklist lives in [the readiness plan](docs/harness-readiness-plan.md).

## License

MIT for the harness and extracted editor code. Engine and third-party assets retain their notices. See [THIRD_PARTY.md](THIRD_PARTY.md).
