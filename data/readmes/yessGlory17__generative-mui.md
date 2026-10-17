<div align="center">

# generative-mui

### Let the LLM build the UI — not you.

**Write a sentence — get real, working Material UI, in your own theme.**

A renderer that maps Google's [A2UI](https://github.com/google/A2UI) (v0.9.1) protocol onto **Material UI**.
The agent emits A2UI — not a nested DOM, but a **flat list of components referenced by id** plus a separate
data model bound by JSON-Pointer. The library turns it into real components inside your app's existing MUI theme.

![generative-mui demo](./promo.gif)

<sub>None of the interfaces above were hand-written — the model was prompted, emitted A2UI, and the library rendered it as MUI.</sub>

⭐ **If the idea grabs you, drop the repo a star** — it's the biggest boost for a project that takes generative UI seriously.

</div>

---

## At a glance

Chatbots return text; but a chart, a table, or a validated form often says more than a sentence.
Until now the options were weak: either hand-write a component for every scenario, or trust the model's
**raw HTML** and accept XSS and theme drift.

`generative-mui` opens a third path. The model emits **data, not code**: A2UI, a flat, schema-validated,
id-referenced UI description. The library takes that description and turns it into real MUI components
**inside the host's `<ThemeProvider>`**. No unregistered type is ever rendered; `sx`/`style`/`className`
from the agent never reach MUI.

> **Describe → the LLM emits A2UI → deterministic store → real Material UI.**

---

## What does A2UI look like? (a concrete example)

The model emits **server→client messages** streamed as JSON Lines. Here's a small, two-way-bound, validated form:

```jsonl
{"createSurface":{"surfaceId":"s1"}}
{"updateComponents":{"surfaceId":"s1","components":[
  {"id":"root","component":"Column","children":["title","name","submit"]},
  {"id":"title","component":"Text","text":"Reservation","variant":"h4"},
  {"id":"name","component":"TextField","label":"Full name","value":{"path":"/name"}},
  {"id":"submitLabel","component":"Text","text":"Confirm"},
  {"id":"submit","component":"Button","child":"submitLabel",
    "action":{"event":{"name":"confirm"}},
    "checks":[{"condition":{"call":"required","args":{"value":{"path":"/name"}}},
               "message":"Name is required"}]}
]}}
{"updateDataModel":{"surfaceId":"s1","path":"/name","value":""}}
```

Things to notice:

- **Adjacency list, not a tree.** `root` references its children **by id**. To update one component you don't
  resend the whole tree — you just put that id back through `updateComponents` (merge-by-id).
- **UI and data are separate.** `TextField.value` isn't a literal, it's a `{"path":"/name"}` binding. As the user
  types, the store's data model updates; the `required` inside `Button.checks` reads that path and **disables** the
  button while it's empty.
- **No colors/CSS.** The model only states semantics (`variant:"h4"`); pixels and palette come from the host theme.

---

## How it works — the internals

The pipeline runs through four pure layers; the first three know nothing about React/MUI:

```
JSONL ─parse─▶ messages ─reduce─▶ SurfaceStore ─resolve─▶ React/MUI tree
             (Zod safeParse)     (deterministic)         (registry + skeleton)
```

**1 · Message protocol — 4 types.** `createSurface` · `updateComponents` (add/replace by id) ·
`updateDataModel` (set/delete a JSON-Pointer path) · `deleteSurface`. Components are stored **loosely**
(`{id, component, ...passthrough}`); full per-prop validation happens lazily at render — so a **truncated
stream** or an unknown custom component degrades to a fallback instead of rejecting the whole batch.

**2 · Deterministic reducer.** The core `reduce(state, message) → state` is a pure function: it never mutates its
input and silently ignores invalid/unknown messages (streaming tolerance). The same message sequence always
yields the same state — testable, and it runs on SSR/edge.

**3 · `SurfaceStore` — live, subscribable.** Holds immutable state and is built for React's `useSyncExternalStore`:
`getState()` returns a **stable reference** until the next change (no needless renders). Key methods:

- `apply(msg | msg[] | jsonl)` — feed the stream; skips invalid lines.
- `writeLocal(surfaceId, pointer, value)` — updates the data model **without a server round-trip** when an input
  changes; this is the engine of two-way binding.
- `compact(surfaceId)` — garbage-collects components unreachable from `root` via BFS (merge-by-id never deletes,
  so ids accumulate). It's a **no-op** while the root hasn't arrived yet, so it can't drop not-yet-attached components.

**4 · Value resolution.** Every catalog prop is one of three things: a **literal**, a **`{path}` binding**, or a
**`FunctionCall`**. `resolveValue` collapses all three against the data model in one place; a `FunctionCall` has its
args resolved recursively then runs against local functions (`required`, `regex`). The same mechanism powers both
dynamic props and Button `checks`: a check whose condition is falsy disables the button and surfaces the first error
message as helper text.

---

## Streaming, resilience, and security

Agent output is **untrusted and may arrive half-formed** — the library is built for exactly that:

- 🌊 **Incremental render.** Components arrive piece by piece; not-yet-received children show a `Skeleton`. For string
  sources there's **append-only delta** detection: a growing stream never clobbers the user's local edits.
- 🧱 **Graph resilience.** An empty or root-less surface renders nothing; a **cycle** or a chain past `MAX_RENDER_DEPTH`
  degrades to a quiet placeholder instead of overflowing the stack; a **per-node error boundary** means one throwing
  renderer never unmounts the whole surface.
- 🔒 **ReDoS guard.** `regex` is local and both the pattern and the input have **length caps** (`1000` / `10,000`),
  because both the pattern and the tested text come from the untrusted agent and JS has no synchronous regex timeout —
  the cap shrinks the ReDoS blast radius without a Worker. Over-long inputs count as a non-match.
- 🛡️ **Safe by construction.** A type not in the registry **never runs arbitrary code** — it falls back safely; fields
  like `sx`/`style`/`className` never reach MUI even if the agent emits them.

---

## Architecture & boundaries

Two packages, a **one-way** dependency — and that's not a convention, it's a **compile-time rule**:

| Package | Role |
| ------- | ---- |
| `@yessglory/generative-mui-core` | Framework-neutral A2UI v0.9.1: Zod schemas, JSONL parser, JSON-Pointer (`get/set/remove`), the deterministic `SurfaceStore`, value resolution, and the agent tool schema. **Imports no React/MUI.** |
| `@yessglory/generative-mui-react` | The MUI adapter: A2UI Basic Catalog → Material UI, in a single public component: `<A2uiSurface>`. |

- **The direction `core ← react` is one-way** and enforced by `eslint-plugin-boundaries` — core leaking into
  React/MUI is a lint error. This lets the parser, store, resolution, and tool schema run **everywhere** (server,
  edge, RSC, tests).
- **Zod schemas are the single source of truth.** The Basic Catalog is a discriminated union on the `component`
  field; a **drift test** keeps these schemas locked to the vendored `catalog.json` (every component has a member,
  and no member names one the catalog doesn't define).

---

## Making an agent speak A2UI

`core` ships provider-agnostic (just data + schema) agent glue:

```ts
import { a2uiTools, a2uiExtendedTools, extractJson } from '@yessglory/generative-mui-core'

// An AI-SDK-shaped tool whose parameters ARE the A2UI adjacency list (a Zod schema).
// The model produces a render-ready surface in one shot.
const tools = a2uiExtendedTools()               // Basic + charts/table/display/input
// const { jsonSchema } = a2uiToolDefinition({ catalog: 'extended' })  // raw jsonSchema7

// If the model replied in plain prose, pull the JSON out (tolerates ``` fences / prose):
const surface = extractJson(modelReplyText)
```

Also, `describeCatalog()` / `A2UI_SHAPE_RULES` / `A2UI_BEHAVIOR_RULES` give you a **prompt block** derived from the
schemas — to embed the catalog into your system message.

---

## Install & use

```bash
pnpm add @yessglory/generative-mui-react
# core comes with react
```

```tsx
import { A2uiSurface, SurfaceStore, extendedRegistry } from '@yessglory/generative-mui-react'

const store = new SurfaceStore()
store.apply(a2uiJsonlFromYourAgent)   // JSONL / message array / single message

function Chat() {
  return (
    <A2uiSurface
      source={store}                    // live store → streaming + two-way binding
      registry={extendedRegistry}       // enable charts too (optional; @mui/x-charts)
      onAction={(a) => sendToAgent(a)}  // action.event goes back to the agent
    />
  )
}
```

- **Two-way binding**: inputs bound to `{"path":"/field"}` read/write the data model.
- **Actions**: `action.event` → `onAction({ surfaceId, name, context })`; `action.functionCall` (e.g. `openUrl`) runs locally.
- **Host-overridable**: `registry={{ MyType: MyRenderer }}` extends or replaces any mapping.
- **Theme**: it has no theme of its own; it inherits the host palette/typography — switch the theme and the UI re-skins top to bottom.

---

## Catalog → MUI

All **18 Basic-Catalog components** map one-to-one:

| A2UI | MUI | A2UI | MUI |
| ---- | --- | ---- | --- |
| `Text` | `Typography` | `Button` | `Button` (+ `checks`→disabled) |
| `Image` | `Box img` | `TextField` | `TextField` |
| `Row`/`Column` | `Stack` | `CheckBox` | `Checkbox` |
| `List` | `List` | `ChoicePicker` | `RadioGroup` / checkbox group |
| `Card` | `Card` | `Slider` | `Slider` |
| `Tabs` | `Tabs` | `DateTimeInput` | `TextField[type=date]` |
| `Divider` | `Divider` | `Modal` | `Dialog` |

**Extended Catalog** (opt-in, `extendedRegistry`): `LineChart` · `BarChart` · `PieChart` · `ScatterChart` ·
`SparkLineChart` · `Gauge` · `Table` · `Alert` · `Chip` · `Badge` · `Accordion` · `Progress` · `Stepper` · `Switch` ·
`Rating` · `Autocomplete`. The schemas live in the React-free `core` (so validation works everywhere); only the
renderers are opt-in, so the `@mui/x-charts` dependency stays optional. Use `a2uiExtendedTools()` to have the agent
emit these too.

---

## Add your own component

Overriding an existing type just needs `registry`. For a genuinely **new** type, `registerComponent` gives you
schema + renderer in one call — without editing the core:

```tsx
import { A2uiSurface, registerComponent, useResolved } from '@yessglory/generative-mui-react'
import { z } from 'zod'

// A brand-new "StarBar" type that shows a score with ★
const StarBar = registerComponent(
  'StarBar',
  { value: z.union([z.number(), z.object({ path: z.string() })]), max: z.number().optional() },
  ({ node }) => {
    const value = Number(useResolved(node.value)) || 0     // literal or {path} binding
    return <span>{'★'.repeat(value).padEnd(node.max ?? 5, '☆')}</span>
  },
)

<A2uiSurface source={store} components={[StarBar]} />
```

The schema is enforced **before** the renderer runs, so a custom type is as safe as a built-in one (invalid props →
skeleton, never a throw). For more — overriding renderers, adding permanently to the core catalog, and advertising
the type to the agent's tool schema → **[`docs/`](./docs)**
([overriding renderers](./docs/08-overriding-renderers.md) · [new types](./docs/09-custom-components.md)).

---

## Examples

The same generative-UI chatbot, in three setups:

| Example | Stack | Notes |
| ------- | ----- | ----- |
| [`examples/gemini-chat`](./examples/gemini-chat) | Vite + React SPA | Gemini call in the browser (demo) |
| [`examples/gemini-chat-next`](./examples/gemini-chat-next) | Next.js App Router | Gemini call in a server Route Handler (the key never ships to the client) |
| [`examples/mui-x-chat`](./examples/mui-x-chat) | Vite + [`@mui/x-chat`](https://www.npmjs.com/package/@mui/x-chat) | Uses MUI's chat component as the shell; generative-mui renders each reply's content via a `data-a2ui` part renderer — no per-component wiring. Includes a [**before/after**](./examples/mui-x-chat#before--after) of the same prompt with and without generative-mui |

```bash
pnpm --filter @yessglory/example-gemini-chat dev        # Vite
pnpm --filter @yessglory/example-gemini-chat-next dev   # Next.js
pnpm --filter @yessglory/example-mui-x-chat dev         # @mui/x-chat + generative-mui
```

All three run out of the box in demo mode, no API key needed.

---

## Development

```bash
pnpm install
pnpm test        # vitest (all packages)
pnpm typecheck   # tsc --noEmit per package
pnpm build       # tsup per package
pnpm lint        # eslint + boundaries
```

**Test surface** — `core`: JSON-Pointer round-trip (property-tested), `SurfaceStore` determinism +
incremental/JSONL replay, drift against `catalog.json`, and the agent tool schema. `react`: render, two-way binding,
`required`-check disabling, action dispatch, streaming skeletons, and **zero axe violations**.

---

<div align="center">

### Like it?

`generative-mui` takes seriously that LLMs shouldn't just talk — they should **build validated, safe, themed UI**.
If you like the idea ⭐ **star it**, watch it, try it — your feedback steers where it goes.

**built by [yessGlory17](https://github.com/yessGlory17)**

</div>
