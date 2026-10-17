# PromptCast Game

> *Inscribe the sigil. Cross the threshold. Duel by prompt.*

PromptCast is a browser-based, peer-to-peer 3D spell duel where players cast in **natural language**. A local LLM (loaded entirely in-browser via [`@sipphq/sipp`](https://www.sipp.sh)) interprets each prompt into a structured, validated spell — VFX, physics, audio, and balance bake out into a runnable scene the engine fires across the network.

Project site: **https://www.sipp.sh**

---

## Table of Contents

- [The Game](#the-game)
- [Tech Stack](#tech-stack)
- [The `@sipphq/sipp` Package](#the-sipphqsipp-package)
- [Quick Start](#quick-start)
- [Environment Variables](#environment-variables)
- [Secrets & Security](#secrets--security)
- [Project Structure](#project-structure)
- [Multiplayer & Networking](#multiplayer--networking)
- [Debugging & Developer Tools](#debugging--developer-tools)
- [Build & Deploy](#build--deploy)
- [Contributing](#contributing)
- [Links](#links)

---

## The Game

**Lore-flavored pitch.** Two wizards meet at the threshold. One inscribes a sigil; the other speaks it. Inside the arena they trade incantations — the words you write *are* the spell. The Sage (the model) listens, weighs your intent, and shapes a working incantation in the world.

**Technical pitch.** PromptCast is an AI-driven 1v1 spell battler built on Next.js + React Three Fiber + Rapier. Players type free-form prompts; a constrained, multi-call LLM pipeline produces a JSON spell (concept → balance) validated against a Zod schema, then handed to the runtime to drive VFX (three.quarks), rigid-body projectiles (Rapier), and audio (ElevenLabs). Multiplayer is P2P over WebRTC via PeerJS, with the host as authority for player list and room state.

Match flow: **Lobby → Inscribe Sigil → Cross Threshold → Begin Duel → Cast Spells → Resolve.**

---

## Tech Stack

| Domain | Library |
| --- | --- |
| Framework | Next.js (App Router), React 19, TypeScript |
| 3D / Rendering | three, `@react-three/fiber`, `@react-three/drei`, `@react-three/postprocessing`, `three.quarks` |
| Physics | `@dimforge/rapier3d-compat` (pinned `0.19.2`), `@react-three/rapier` |
| Networking | `peerjs` (WebRTC) |
| State | `zustand` |
| Validation | `zod` |
| AI | `@sipphq/sipp` (in-browser LLM, GGUF via OPFS) |
| Audio | ElevenLabs (server route) |
| IDs | `nanoid` |

---

## The `@sipphq/sipp` Package

[`@sipphq/sipp`](https://www.sipp.sh) is the in-browser LLM client this project uses to turn natural-language prompts into structured spells. The client runs in a worker, downloads a pinned GGUF model into OPFS on first load, and exposes a streaming, grammar-constrained query API.

**How PromptCast uses it:**

- `src/game/ai/sippSpellGenerator.ts` — owns the `SippClient` singleton, OPFS model loading/caching, progress fan-out to the loader UI, and observability subscription. The pinned model is `LFM2.5-1.2B-Instruct-Q4_K_M.gguf` (see `MODEL_URL` in `src/game/ai/sippSpellGenerator.ts`).
- `src/game/ai/pipeline/` — multi-call pipeline that streams a spell through stages (`conceptCall.ts`, `balanceCall.ts`) using `callRunner.ts`. Each stage emits `PipelineProgress` events the UI renders live.
- `src/game/ai/grammar/` — JSON grammar definitions used to constrain model output to valid spell shapes.
- `src/game/spells/spellSchema.ts` — Zod schema the pipeline output is validated against before reaching the runtime.
- `src/game/ai/spellLog.ts` — stage-tagged logger for inspecting pipeline runs.
- `src/game/ai/spellGenerationError.ts` — typed error wrapper exposing `stage` + `canRepair` so the UI can offer a Repair retry.

**Browser requirements (inferred from the loader):**

- Secure context with WebAssembly + Worker support
- OPFS (`navigator.storage.getDirectory`) for model caching
- Plenty of free disk space for the GGUF (~700MB+ depending on quant)
- Cross-origin isolation may be required depending on Sipp's worker mode

See [sipp.sh](https://www.sipp.sh) for SDK docs and the canonical API.

---

## Quick Start

**Prerequisites**

- Node.js (LTS recommended)
- npm or yarn
- A Chromium-based browser for full feature support (OPFS, WebRTC, optional WebGPU)

**Install & run**

```bash
npm install
cp .env.local.example .env.local   # then fill in keys (see below)
npm run dev                        # http://localhost:3000
```

**Scripts**

| Script | Purpose |
| --- | --- |
| `npm run dev` | Next dev server on `localhost` |
| `npm run dev:network` | Next dev server bound to `0.0.0.0` for LAN multiplayer testing |
| `npm run build` | Production build |
| `npm run start` | Run the production build |
| `npm run lint` | ESLint |
| `npm run typecheck` | `tsc --noEmit` |

---

## Environment Variables

Create a `.env.local` at the repo root. Variables prefixed with `NEXT_PUBLIC_` are exposed to the browser; everything else is server-only.

**Server-side**

| Variable | Purpose |
| --- | --- |
| `ELEVENLABS_API_KEY` | ElevenLabs TTS / audio API key (used by server routes only) |

**Client-side (optional PeerJS overrides)**

| Variable | Purpose |
| --- | --- |
| `NEXT_PUBLIC_PEER_HOST` | Self-hosted PeerJS broker host |
| `NEXT_PUBLIC_PEER_PORT` | Broker port |
| `NEXT_PUBLIC_PEER_PATH` | Broker path (e.g. `/`) |
| `NEXT_PUBLIC_PEER_SECURE` | `true` / `false` |
| `NEXT_PUBLIC_PEER_DEBUG` | PeerJS debug level `0`–`3` |
| `NEXT_PUBLIC_MULTIPLAYER_DEBUG` | Force-enable the multiplayer debug panel |

**Client-side (optional Sipp debug)**

| Variable / Flag | Purpose |
| --- | --- |
| `?debugSipp=1` (URL) | Enable verbose `[SippLoad]` console logging |
| `localStorage.setItem("promptcast.sippDebug", "1")` | Persistent equivalent of the URL flag |

> Sipp-specific configuration (API keys, endpoints, model overrides) — see [sipp.sh](https://www.sipp.sh) for the current SDK contract. The current integration uses the in-browser worker engine and does not require a server-side key.

---

## Secrets & Security

**Never commit `.env.local` or any file containing API keys.**

- `.env.local` must remain gitignored. Verify with `git check-ignore .env.local` before committing.
- Treat any key that lands in a tracked file (or in your shell history, screenshots, or chat logs) as **leaked** and rotate it immediately at the provider.
- Server-only secrets must **not** be prefixed with `NEXT_PUBLIC_` — that prefix ships them to the browser.
- ElevenLabs and any future provider keys belong only in environment variables consumed by server routes / serverless functions.
- Audit `git log -p -- .env*` periodically to catch accidental commits.

---

## Project Structure

```
src/
  app/                       # Next.js App Router
    page.tsx                 # Lobby (sigil inscription / threshold)
    game/                    # Match route
    dev/                     # Developer tool routes (see below)
    layout.tsx, globals.css

  components/game/           # React 3D + UI components

  game/
    ai/
      sippSpellGenerator.ts     # Sipp client + model loader + progress
      pipeline/                # concept → balance call pipeline
      grammar/                 # JSON grammars constraining model output
      spellLog.ts              # stage-tagged pipeline logger
      spellGenerationError.ts  # typed errors with `canRepair`
    arena/                   # Arena scene + props
    audio/                   # Audio engine, ElevenLabs hooks
    config/                  # Tunables
    math/                    # Vector / curve helpers
    networking/
      peerSession.ts           # PeerJS host/client session, auth, debug
      usePeerSession.ts        # React bindings
      messages.ts              # Network message types + parser
    physics/                 # Rapier wrappers
    spells/
      spellSchema.ts           # Zod schema for generated spells
      runtime/                 # Spell execution engine
      modules/                 # Reusable spell building blocks
      vfx/                     # VFX module library
      sceneNode.ts             # Scene graph helpers
      balance.ts               # Balance pass utilities
    state/                   # Zustand stores
    playerProfile.ts         # Local player identity
    types.ts                 # Shared types

public/
  audio/, textures/, models  # Static game assets
```

---

## Multiplayer & Networking

PromptCast multiplayer is peer-to-peer over WebRTC using PeerJS. The host's PeerJS id is derived deterministically from the room code (`promptcast-<lowercase-code>`), so a sigil string *is* the address — clients connect by name, no signaling lookup needed beyond the public PeerJS broker (or your own — see env vars). The host is authoritative for the player list and room state; clients send intents, host validates and rebroadcasts. See `src/game/networking/peerSession.ts:81` for the session implementation.

### Local Multiplayer Debugging

1. Run `npm run dev` for same-machine browser testing, or `npm run dev:network` to expose the Next dev server on the local network.
2. Open `/` in browser A and click **Inscribe Sigil**.
3. Copy the generated sigil.
4. Open `/` in browser B or an incognito window, enter the sigil, and click **Cross the Threshold**.
5. The host can click **Begin the Duel**; clients auto-route on match start or can click **Step Through** once data-ready.

The multiplayer debug panel is available in development builds and with `?debugNetwork=1`. It shows PeerJS state, lobby/store player ids, message events, drops, and debug actions.

Optional PeerJS client config:

```text
NEXT_PUBLIC_PEER_HOST=localhost
NEXT_PUBLIC_PEER_PORT=9000
NEXT_PUBLIC_PEER_PATH=/
NEXT_PUBLIC_PEER_SECURE=false
NEXT_PUBLIC_PEER_DEBUG=1
NEXT_PUBLIC_MULTIPLAYER_DEBUG=1
```

Direct `/game?mode=host&room=...` URLs only set local game mode; they do not create or rejoin PeerJS sessions. Start from the lobby for real multiplayer sessions.

### Common Networking Issues

| Symptom | Likely cause |
| --- | --- |
| Client times out connecting | Host's PeerJS id never opened; check broker reachability, NAT/firewall, or `NEXT_PUBLIC_PEER_*` overrides |
| `actor_mismatch` drops in debug panel | Client tried to send a message claiming another player's id; check authorization in `peerSession.ts:401` |
| `client_sent_host_authority_message` drops | A client attempted to send `player_list`, `room_state`, `pickup_state`, etc. — those are host-only |
| `invalid_payload` drops | Message failed `parseNetworkMessage` — bump the schema in `src/game/networking/messages.ts` |
| Host connection closed before opening | Connection settled before the data channel opened; check console for PeerJS error |

---

## Debugging & Developer Tools

### Debug panels & flags

| Where | What it does |
| --- | --- |
| `?debugNetwork=1` or dev build | Multiplayer debug panel: PeerJS state, lobby/store player ids, message in/out/drop events, debug actions |
| `?debugSipp=1` or `localStorage.setItem("promptcast.sippDebug", "1")` | Verbose `[SippLoad]` console logs covering client create, Sipp model caching, and model load progress |
| `window.__promptcastSippDiagnostics` | Last ~80 Sipp diagnostic entries (also persisted to `localStorage.promptcast.sippDiagnostics`) |
| `spellLog` (`src/game/ai/spellLog.ts`) | Stage-tagged pipeline log — inspect concept/balance call traces and failure causes |

### Developer tool routes

Mounted under `src/app/dev/`:

| Route | Purpose |
| --- | --- |
| `/dev/audio-library` | Browse and audition audio assets used by spells |
| `/dev/vfx-preview` | Live VFX module preview harness |
| `/dev/vfx-textures` | Inspect VFX textures (also see `public/textures/vfx/README.md`) |

### Typical debugging workflow

1. **Pipeline failure?** Open the console, look for `[spellLog]` / `[SippLoad]` lines, and inspect the `SpellGenerationError`'s `stage` + `cause`. The UI offers a Repair retry when `canRepair` is true.
2. **Model won't load?** Set `?debugSipp=1`, hard-reload, and read the `client:create:*` and `model:*` events. Check OPFS quota and that the page is in a secure context.
3. **Networking issue?** Open `?debugNetwork=1`, watch the live event feed, and cross-reference dropped messages against the table above.
4. **Visuals look wrong?** Use `/dev/vfx-preview` to isolate a module away from the full match.

---

## Build & Deploy

```bash
npm run build
npm run start
```

Production deployment requires:

- `ELEVENLABS_API_KEY` set as a server-side secret
- Hosting that supports Next.js App Router (Vercel works out of the box)
- A reachable PeerJS broker — the public broker works for casual testing; production should self-host (set `NEXT_PUBLIC_PEER_*`)

---

## Contributing

- `npm run lint` and `npm run typecheck` must pass before you push.
- Keep Sipp pipeline changes localized to `src/game/ai/`; runtime changes localized to `src/game/spells/runtime/`. Cross-cutting changes deserve a design note.
- Don't widen the network message schema without updating both `messages.ts` and the host authority list in `peerSession.ts:authorizeMessage`.
- Never commit secrets — see [Secrets & Security](#secrets--security).

---

## Links

- Project / SDK site: https://www.sipp.sh
- `@sipphq/sipp` package: https://www.sipp.sh
- Next.js: https://nextjs.org
- React Three Fiber: https://r3f.docs.pmnd.rs
- Rapier: https://rapier.rs
- PeerJS: https://peerjs.com
