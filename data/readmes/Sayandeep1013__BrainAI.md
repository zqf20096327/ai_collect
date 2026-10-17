# BrainAI

Turn one sentence into a planning tree, then compile it into a folder of files a coding agent can actually build from — on your machine, with your own keys.

[![Next.js](https://img.shields.io/badge/Next.js-15.5-%23000000?logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-%2361dafb?logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-%233178c6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![xyflow](https://img.shields.io/badge/xyflow-12-%23ff0072)](https://reactflow.dev/)
[![Zod](https://img.shields.io/badge/Zod-3-%233068b7)](https://zod.dev/)
[![Tavily](https://img.shields.io/badge/Tavily-live%20search-%236366f1)](https://tavily.com/)
[![Vitest](https://img.shields.io/badge/Vitest-56%20tests-%236e9f18?logo=vitest&logoColor=white)](https://vitest.dev/)
[![License](https://img.shields.io/badge/license-MIT-%23bb9af7)](LICENSE)

![The workspace mid-run](docs/assets/02-growing.png)

## Idea

You have an idea and an agent that will build it. The gap between the two is a
planning problem, and it is the part everyone skips: you either hand the agent a
one-paragraph prompt and get a plausible-looking mess, or you spend a day writing a
PRD, a schema, an architecture note and a task list by hand.

BrainAI closes that gap by growing the plan as a tree and then compiling the tree
into the pack. You type a sentence. It proposes root sections, runs real web
research, takes the reversible forks itself, keeps filling gaps until every file in
the pack map has evidence behind it, and stops when it needs a human or runs out of
budget. Then it writes 45 files into a folder you name.

Two constraints shaped almost every decision in here:

1. **The autonomy has to be visible, or it isn't trusted.** A machine that thinks for
   forty seconds behind a spinner is indistinguishable from a machine that has
   crashed. So the planner's reply is parsed incrementally and each child is drawn as
   a dashed draft the moment its JSON object closes; the run narrates itself in a
   log; and when it stops, it says which of six things stopped it — and keeps saying
   so after the run ends.
2. **A pack with a hole in it is worse than no pack.** Compile is gated on a coverage
   matrix, not on a file count. Every key in the pack map has to point at a node with
   real evidence before a single file is written, and the compiler writes to a temp
   directory and secret-scans it before anything touches your folder.

## What it does

| | |
| --- | --- |
| ![Home](docs/assets/01-home.png) | **Start from a sentence.** Optionally name the folder and set the node, depth and search budgets before the first wave — the run begins the moment the project exists. |
| ![The tree](docs/assets/03-tree.png) | **The tree writes itself.** Sections, research, decisions and artifacts, laid out left-to-right with dagre. Every card says what it is, what it needs, and which pack files it becomes. |
| ![A decision](docs/assets/04-decision.png) | **It decides for you, and says so.** Reversible forks are taken on the recommended option and marked `auto-decided` with a gold edge. Override one and it records what autopilot had picked. |
| ![Coverage](docs/assets/05-coverage.png) | **Compile is a gate, not a button.** Every blocking coverage key with the reason it's blocking and its own *Grow this gap*, plus the budgets that stopped the run. |
| ![The pack](docs/assets/06-pack.png) | **Take delivery.** Every written file, grouped and sized, readable in place, with the folder path and a button that opens it. |

## How it works

**The wave is an autonomous run loop, not one pass.** `src/server/orchestrator/wave.ts`
walks seed → sections → breadth-first expansion → Tavily research → auto-accept
non-critical decisions → gap-fill until coverage closes → optional auto-compile. A
`POST` returns **202** and the work runs on the Node server; SSE only subscribes.
That split exists because a full run is minutes of sequential model calls and a
route handler that `await`s it dies on the first client navigation.

**Streamed previews are parsed out of half-received JSON.** `src/server/llm/stream.ts`
walks the `children` array of a partial reply, string-aware and escape-aware, and
announces each child the instant its object closes. The canvas draws those as dashed
ghosts that are replaced in place by real nodes. The offline planner replays the
same path so the effect is not a live-only luxury.

**Coverage is keys, not a file list.** `TECH/schema/pack-map.json` declares 34
coverage keys; some accept variants (`schema.sql` *or* `schema.prisma`), some demand
a minimum file count under a prefix, and two carry rules — `product.market` needs a
live citation, the legal files need named facts. A node lists several `packTargets`,
so a 17-node tree can close a 45-file pack.

**The model adapter assumes the gateway will fail.** Seven failure kinds
(`waf | auth | model_denied | pool_exhausted | rate_limit | network | parse`), a
model fallback chain where per-model failures advance and WAF/auth stop it dead,
retry-on-the-same-model before switching, and a `truncated` kind that doubles the
token budget rather than switching voice mid-pack. All of it measured against the
live gateway, not guessed — see `PRODUCT/decisions/ADR-003.md`.

**Compile is transactional.** Files are written to `.brainai/compile-tmp/`,
secret-scanned in memory, and only then copied into place. A failed scan deletes the
temp directory and leaves the previous pack exactly as it was.

## Stack

| Layer | Choice | Why this one |
| --- | --- | --- |
| App | Next.js 15 App Router | Route handlers and `node:fs` in one local process |
| Canvas | xyflow + dagre | An infinite tree that lays itself out; no hand-placed coordinates |
| Validation | Zod | `graph.json` is the source of truth, so it is parsed, not trusted |
| Planner | Any OpenAI-compatible endpoint | Bring your own; default is AgentRouter |
| Search | Tavily `basic`, 5 results | Live URLs, budgeted, counted per HTTP attempt |
| Jobs | In-process registry + SSE | No queue, no database, no second service to run |
| State | JSON files on disk | The pack is the product; the graph is a file you can read |
| Tests | Vitest, 56 across 10 files | Four are end-to-end runs of the real orchestrator |

## Run it

```bash
npm install
npm run dev          # http://localhost:3000
```

Then open **Settings**. Either paste an OpenAI-compatible base URL, key and model, or
pick **Offline (no key)** — a deterministic local planner that builds a real tree and
a real pack shape with nothing researched or reasoned. It is labelled in the top bar,
in Settings, and stamped into every file it writes. It is a harness for exercising
the machine, never a shipping path.

```bash
npm run typecheck
npm run lint
npm test
```

Keys live in `data/settings.json` and `.env.local`, both gitignored, and the compiler
refuses to write a pack containing anything matching `sk-[A-Za-z0-9]{16,}` or
`tvly-[A-Za-z0-9_-]{8,}`.

## Spec

This repository was specified before it was built, and the specification is still the
source of truth.

| Document | What's in it |
| --- | --- |
| [`PRODUCT/prd.md`](./PRODUCT/prd.md) | 38 numbered requirements and their acceptance checks |
| [`PRODUCT/decisions/`](./PRODUCT/decisions/) | 13 ADRs — the locked calls, with the reasoning |
| [`PLAN/FLOW-SPEC.md`](./PLAN/FLOW-SPEC.md) | The user flow, stage by stage, and what each stage was missing |
| [`PLAN/BLOCKERS.md`](./PLAN/BLOCKERS.md) | Every landmine hit, measured, with the required handling |
| [`PLAN/PROGRESS.md`](./PLAN/PROGRESS.md) | Dated log of what was built and why |
| [`TECH/schema/pack-map.json`](./TECH/schema/pack-map.json) | The 34 coverage keys and the files they demand |
| [`DESIGN/microcopy.md`](./DESIGN/microcopy.md) | Every string that ships |

## State

**34 of 38 requirements done, 12 of 14 tasks complete.** What is not:

- **`T-013`** — root CI. Template parked at `OPS/.github/workflows/ci.yml`.
- **`T-014`** — asks for a UI rating ≥ 8/10. Two independent critic rounds scored
  **6/10**; a third batch of fixes went in unscored. By its own bar, open.
- **REQ-006** — a `paused` critical node is not sealed: *Go deeper* still grows
  children under a fork that is waiting on you.
- **REQ-014** — `minFiles` is enforced on the coverage gate but not at write time.
- **REQ-020** — wireframe `ext: html` is not enforced on model-supplied targets.
- **REQ-025** — unexpanded branches never reach `backlog.md`.

Recent verification has been offline; AgentRouter rations Claude in two daily
batches, so live runs wait on the window.

## Run it in a browser

**<https://sayandeep1013.github.io/BrainAI/>** is the real app, not a showcase.
Same interface, same planning engine, bring your own keys.

There is no server and no account. The engine talks to a small `Vfs` interface
instead of `node:fs`, so the hosted build runs it against IndexedDB in your own
browser: your keys and every project you plan stay on your machine, and a
compiled pack leaves as a `.zip`, or straight into a folder you pick where the
browser supports it. One conformance suite runs the same assertions against both
filesystems, so the two cannot drift.

**No key?** Press *Try it offline instead*. You get the whole structure — every
folder, every file, every heading, an archetype picked from your idea and specs
named after your own problems — built deterministically with no model involved.
Every file says so in its own text. It is the honest way to see the machine work
before deciding whether to point a key at it.

### Which gateway to use

Your key goes straight from your browser to the provider. Most gateways accept
that; one does not.

| Gateway | Works in the browser | Note |
| --- | --- | --- |
| OpenRouter | yes | Reaches Claude and most other models on one key. The default. |
| DeepSeek | yes | Cheap and unrationed. |
| Groq | yes | Very fast, generous free tier. |
| AgentRouter | **no** | Needs a relay — see below. |
| Tavily (search) | yes | No relay, ever. |

AgentRouter fingerprints its clients and rejects any request carrying a browser
`User-Agent` with `401 unauthorized_client_error`. `User-Agent` is a [forbidden
header][forbidden] that a page is not allowed to set, so this is not something
the app can work around. Measured against the live gateway on 2026-09-11: the
same request with a CLI `User-Agent` — Origin, Referer and `Sec-Fetch-*` headers
and all — is accepted. That one header is the whole problem.

`relay/` holds a ~120-line stateless worker that rewrites it and forwards
nothing else. It is allowlisted rather than open, and it never stores your key.
Deploy it free in about two minutes (`cd relay && npx wrangler deploy`) and paste
the URL into Settings. Or skip it: pick a gateway from the table above, or run
BrainAI locally, where AgentRouter works directly and no relay exists.

[forbidden]: https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header

### Local is still the primary way to run it

`npm run dev` gives you the app in `## Run it` above: projects are real folders,
`graph.json` is a real file, and the compiled pack lands on disk. That is
`ADR-001` and it has not changed. `npm run build:static` produces the hosted
build into `docs/`.

## License

MIT — see [LICENSE](./LICENSE).
