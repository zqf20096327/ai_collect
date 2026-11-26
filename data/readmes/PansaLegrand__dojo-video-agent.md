# Dojo Video Agent

[![CI](https://github.com/PansaLegrand/dojo-video-agent/actions/workflows/check.yml/badge.svg)](https://github.com/PansaLegrand/dojo-video-agent/actions/workflows/check.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**An open-source video editor where you and an AI agent work on the same timeline.** Run locally, bring your own model keys, and extend the TypeScript agent. Import footage, edit by hand or through chat, and export an MP4 in your browser. Ordinary validated chat edits apply directly; Compare and Undo let you inspect or reverse them.

**Want to try the hosted product? [Open DojoClip Video Edit AI](https://dojoclip.com/en/applications/video-edit-ai).** DojoClip adds managed accounts, projects, provider jobs, storage, and payments. This repository is the smaller local editor and developer foundation; it does not install the commercial SaaS.

## Make it your own

<!-- dojo-demo-gallery:start -->

### North Studio · a chart becomes a portrait film

[![Animated portrait chart with a coral peak, mint Week one label and North Studio logo ending](docs/assets/showcase/north-studio/preview.gif)](docs/assets/showcase/north-studio/portrait.mp4)

Ten seconds of editable data storytelling: a measured chart reveal, a highlighted peak and a matching brand ending. Made with Dojo Video Agent and rendered by Dojo Video Engine. The model-authored layout used saved-result and command-syntax recovery.

[Watch the portrait MP4](docs/assets/showcase/north-studio/portrait.mp4) · [Production notes](docs/creative-qualification-r36-2026-11-22.md)

### Night Garden · one brief, two cuts

[![Eight-second animated comparison: a lilac flower opens in Nocturne while two ink layers align into a moth in Ink Press](docs/assets/showcase/night-garden/compare.gif)](docs/assets/showcase/night-garden/compare.mp4)

[Watch Nocturne](docs/assets/showcase/night-garden/nocturne.mp4) · [Watch Ink Press](docs/assets/showcase/night-garden/press.mp4) · [Edit either film](examples/art-direction/README.md) · [Type and color guide](guides/type-and-color.md)

### Open Assembly · editable 3D instrument study

[![A watch separates into a dial, gears and case beside the editable Open Assembly title](docs/assets/showcase/open-assembly/poster.jpg)](docs/assets/showcase/open-assembly/preview.mp4)

The eight-second cut opens with a studio imprint, then reveals the watch in layers. Open it in the running local editor with `node examples/art-direction/import.mjs examples/art-direction open-assembly`. The text, timing and 3D objects stay editable. [Download the MP4](docs/assets/showcase/open-assembly/preview.mp4)

### Creative directions

https://github.com/user-attachments/assets/99fa44aa-1e46-4594-9938-7b8cfe312223

Illustrated stories, animated data, portrait typography, cinematic titles and 3D branding.

### 3D and vector detail

https://github.com/user-attachments/assets/59f7b7d2-bb9c-442a-808c-8935aeec4de0

A miniature city, an exploded mechanical timepiece and layered kinetic vector art.

### Real-world scenarios

https://github.com/user-attachments/assets/088f91fb-d8a0-47d6-85c9-9e7665a116e9

Sports broadcast graphics, a software workflow and a colorful drink campaign.

### Lottie and animated lettering

https://github.com/user-attachments/assets/32125d51-061f-4a0f-b0ab-e15f79edb770

An original Lottie story, handwriting drawn stroke by stroke, and expressive editable text.

<details>
<summary>Watch all 19 individual films</summary>

| Film                                                                      | Creative direction              |
| ------------------------------------------------------------------------- | ------------------------------- |
| [North Studio](docs/assets/showcase/north-studio/portrait.mp4)            | Portrait chart and brand ending |
| [Night Garden · Nocturne](docs/assets/showcase/night-garden/nocturne.mp4) | Botanical motion identity       |
| [Night Garden · Ink Press](docs/assets/showcase/night-garden/press.mp4)   | Print-inspired motion identity  |
| [Open Assembly](docs/assets/showcase/open-assembly/preview.mp4)           | Editable 3D instrument study    |
| [Night Train](docs/assets/showcase/journey.mp4)                           | Illustrated story               |
| [Field Notes](docs/assets/showcase/data-story.mp4)                        | Data and reports                |
| [Type in Motion](docs/assets/showcase/kinetic.mp4)                        | Portrait motion poster          |
| [Deep Field](docs/assets/showcase/cinema.mp4)                             | Cinematic titles                |
| [After Hours](docs/assets/showcase/festival.mp4)                          | Festive 3D                      |
| [Orbit](docs/assets/showcase/company.mp4)                                 | Company launch                  |
| [Little Worlds](docs/assets/showcase/city.mp4)                            | Miniature worlds                |
| [Precision / P–01](docs/assets/showcase/precision.mp4)                    | Exploded assembly               |
| [Chroma Bloom](docs/assets/showcase/bloom.mp4)                            | Kinetic vector art              |
| [Night League](docs/assets/showcase/sports.mp4)                           | Sports broadcast                |
| [Flow](docs/assets/showcase/software.mp4)                                 | Software product demo           |
| [Squeeze](docs/assets/showcase/citrus.mp4)                                | Food and drink campaign         |
| [Special Delivery](docs/assets/showcase/lottie.mp4)                       | Lottie vector story             |
| [Make Magic](docs/assets/showcase/handwriting.mp4)                        | Handwritten lettering           |
| [Letter / Form](docs/assets/showcase/type-motion.mp4)                     | Expressive typography           |

Full reels: [Creative directions](docs/assets/showcase/gallery.mp4) · [3D and vector detail](docs/assets/showcase/showoff.mp4) · [Real-world scenarios](docs/assets/showcase/scenarios.mp4) · [Lottie and lettering](docs/assets/showcase/lettering.mp4)

</details>

**[Explore the editable examples and make them yours →](examples/creative-showcase/README.md)**
The original scenes stay editable; no API keys are needed to render them.

<!-- dojo-demo-gallery:end -->

Formerly **Dojo Video Harness** (`dojo-video-harness`). The repository name changed; package names, saved projects, and runtime profiles remain compatible. See [the rename record](docs/project-rename-2026-11-17.md).

## Choose the right project

| Project                                                                | Use it for                                                                        | What you operate                                             |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Dojo Video Agent**                                                   | Edit local footage, study the agent, add tools or skills                          | A single-user localhost app; your own optional provider keys |
| [Dojo Video Engine](https://github.com/PansaLegrand/dojo-video-engine) | Build scene rendering, playback, inspection, and export into your own application | TypeScript packages and browser media APIs                   |
| [DojoClip](https://dojoclip.com/en/applications/video-edit-ai)         | Use the hosted editor and managed AI services                                     | An account in the commercial product; no local server setup  |

Dojo Video Agent includes the shared editor UI, command validation, timeline history, captions, editable graphics, browser preview/export, and a bounded model/tool loop. It deliberately excludes commercial authentication, billing, Postgres/Prisma, Redis queues, cloud-storage configuration, production workers, and deployment credentials. Local image/video-generation adapters are not shipped; the optional BYOK music adapter is available.

No DojoClip database or commercial environment file is needed. Projects and receipts use local files; imported originals use browser IndexedDB. The UI is English-only, while media text and provider-supported captions can use other languages. See [the scope and synchronization policy](docs/open-source-scope.md).

## Run locally

Requirements: Git, Node **20.19+** (Node **22** recommended), npm, and a desktop browser with WebCodecs support. Chromium is the tested path. FFmpeg is only needed for acceptance tests.

```sh
git clone https://github.com/PansaLegrand/dojo-video-agent.git
cd dojo-video-agent
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

## Open the showcase projects

With the local editor running, use another terminal at the repository root:

```sh
node examples/creative-showcase/import.mjs journey
node examples/creative-showcase/import.mjs data-story
node examples/creative-showcase/import.mjs kinetic
node examples/creative-showcase/import.mjs cinema
```

Each command creates a fresh project and prints its editor link. Play it, select
a graphic, make it yours and export. [Source, customization and rendering details](examples/creative-showcase/README.md).

![After Hours open in the local editor with editable 3D controls and timeline layers](docs/assets/showcase/editor-festival.png)

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

The stable source default is **local-editor-v14**, using **agent kit 0.2.10**, **loop 0.2.0**, and published **engine 1.3.1**. Brand Kits or `DOJO_VISUAL_REVIEW=1` select the 0.2.12 candidate. New local runs retain explicit authoring/visibility policies; saved runs keep their original policies. Older saved runs retain their original behavior and budgets. The latest shared editing behavior is reused by the commercial host through its own adapters; commercial services are not copied into this app.

- **Web → agent:** selected editor components, managed and checked by file hashes.
- **Engine → both apps:** published rendering/playback/export packages at exact versions.
- **Agent → commercial host:** portable agent loop, tool contracts, and skills.
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

The **0.2.10 development candidate** adds seven visual skill packs: branded
endings, charts, festival motion, kinetic typography, presentation motion,
product walkthroughs and 3D scenes. Each has motion guidance and a reference
board, loaded when selected. Try short briefs such as “Animate MAKE EVERY FRAME
COUNT” or “Explain Plan, Build, Launch as a motion slide.” See the
[skill catalog](docs/extending.md#a-skill) and
[validation status](docs/creative-skill-expansion-2026-11-18.md); the four newest
packs still await real-model visual qualification.

For new local candidate runs, start the server with
`DOJO_FOCUSED_GRAPHICS_DISCOVERY=1 npm run dev` to expose `clip`, `mask`, and
`effect` lookups through `inspect_graphics_schema`. Each reply contains only
that feature’s installed fields and a native node example. Existing runs retain
their original tool contract when resumed.

A useful first extension is a read-only tool that counts clips on a track. Or add a trusted lowercase `skills/name.md` file and restart the host. Markdown guides registered tools; it cannot install executable code or authorize spending. Follow [the extension guide](docs/extending.md).

Agent packages are source workspaces here, not a published embeddable SDK. Engine packages are published separately. Durable recovery retains completed replies and receipts; uncertain paid submissions need reconciliation. See [the current agent map](docs/agent-system.md) and [edge cases](docs/edge-cases.md) for exact limits.

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

MIT for the agent and extracted editor code. Engine and third-party assets retain their notices. See [THIRD_PARTY.md](THIRD_PARTY.md).

### Portable projects

Use **Project package** to export an editable `.dojoproject` file with media and registered fonts. Restore it into an empty project in a fresh browser. The package excludes provider accounts/jobs and verified transcript authority; captions remain editable and new speech cuts need fresh transcription. Limits and evidence are in the readiness ledger.

### External coding agents

Use **Copy for Agent** and the opt-in local MCP bridge to continue the same project from another agent. See [setup, tools and browser consent](docs/external-agent-mcp.md).
