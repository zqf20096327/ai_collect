# AG-UI Demo

**Why this exists:** nearly every [AG-UI](https://docs.ag-ui.com) example is
Next.js and CopilotKit. If you are on plain React, or on no framework at all,
you end up reading someone else's app-router setup to work out which four
handlers actually matter. This repo is the same protocol with all of that
stripped out, so you can lift the wiring straight into whatever you already
have.

A LangGraph ReAct agent talking to a browser: streaming, shared state, tool
calls, and human-in-the-loop interrupts. Two frontends that behave identically,
**React** (Vite) and **vanilla JS** (no framework, no build-time magic), both
driven by the same protocol code.

The demo itself is a flight-booking assistant called Breeze. It invents every
flight it quotes.

```
chat freely  ->  search_flights  ->  select_flight  ->  save_passenger
             ->  confirm_booking     (pauses and asks you directly)
             ->  reference issued, booking moves to the cart
```

> **⚠️ Written by an AI agent.** Not maintained by hand. A human directs and
> reviews; the code is typed by a model. Run it yourself before you trust it,
> read it before you copy it, and treat it as a reference rather than a
> dependency. All flight data is invented at runtime.

## Quick start

```bash
cd backend && cp .env.example .env && poetry install && poetry run dev
```
```bash
cd frontend && npm install && npm run dev          # :5173
```
```bash
cd frontend-vanilla && npm install && npm run dev  # :5174
```

Needs Python 3.12/3.13, Node 20+, Poetry. **No key goes in `.env`**. You paste
your own in the chat (**Add key**). Get one at
[openrouter.ai/keys](https://openrouter.ai/keys).

```bash
cd backend  && poetry run pytest    # 63 tests
cd frontend && npm test             # 43 tests
```

Neither suite needs a key or a network: everything runs against a scripted fake
model or an SSE fixture recorded from the real backend.

## Where things are

| Changing… | File |
|---|---|
| what the agent can do | `backend/src/graph.py`: tools first, prompt at the bottom |
| conversation length limits | `backend/src/middleware.py` |
| HTTP, CORS, keys, errors | `backend/src/app.py` |
| how the browser talks to the agent | `frontend/src/hooks/useAgentChat.js` ← **copy this one** |
| chat UI | `frontend/src/Chat/` + one CSS module |
| stream parsing (both frontends) | `frontend/src/lib/agentStream.js`, copied verbatim to `frontend-vanilla/src/` |
| the no-framework version | `frontend-vanilla/src/main.js`: a `state` object and four render functions |

## Things that are not obvious

**Bring your own key.** The server holds none. Each request carries the caller's
in `X-LLM-API-Key`; no key means 401. It lives in a `ContextVar` for one request,
and in page memory in the browser. Never storage, and never LangGraph's
`configurable`, which lands in checkpoint metadata that a persistent
checkpointer writes to disk.

**Interrupts.** `confirm_booking` calls `interrupt()`. The run ends with
`RUN_FINISHED { outcome: { type: "interrupt", interrupts: [{id}] } }`, and the
next send answers it:

```js
const resume = buildResumeEntries(agent.pendingInterrupts, text);
await agent.runAgent(resume ? { resume } : {}, handlers);
```

- `status` must be exactly `"resolved"`. Anything else reads as a
  cancellation, silently.
- The tool's payload sits at `metadata.langgraph.raw`, **not** the protocol's
  `value` field. `interruptPayload()` reads both.
- The legacy `on_interrupt` event is deprecated as of `ag-ui-langgraph` 0.0.43;
  the switch is `emit_interrupt_outcome` in `app.py`.

**State.** Tools return `Command(update={...})`. The panel reads
`STATE_SNAPSHOT`, the graph's real state, not a parallel copy.

**Context.** Summarised past 30 messages, cart capped, turns bounded by
`recursion_limit`. Nothing force-injects state into the prompt; the agent calls
`review_booking` when it wants to look. Cheaper per turn, at the cost of it
occasionally asking for something it already has.

**Empty replies.** A model can return nothing: the run ends clean, no error, no
text. The client detects that and says so, because nothing upstream will.

## Conventions

- **Comments say why.** Several record a bug that would otherwise come back:
  `overflow: clip` vs `hidden`, the `justify-content: flex-end` scroll trap,
  `[hidden]` losing to a class. Don't tidy them away.
- **Tests must be able to fail.** Every regression test here was checked by
  reverting its fix and watching it go red.
- **No key, no network, in tests.** Keep it that way or they stop being runnable.
- **Fixtures are recorded, not written.** Regenerate them; don't hand-edit.

## Errors you might hit

The exact messages, because these are the ones that cost an afternoon.

**`Thread has N pending interrupt(s) not addressed by resume`**
A previous run paused and you started a new one without answering it.
`@ag-ui/client` refuses rather than silently dropping the pause. Read
`agent.pendingInterrupts` and pass `resume` on the next `runAgent`.

**The interrupt fires but the payload is empty**
The value your tool passed to `interrupt()` is not on the protocol's `value`
field. The LangGraph adapter nests it at `metadata.langgraph.raw`. See
`interruptPayload()`.

**Resuming does nothing, or looks like a cancellation**
`status` has to be exactly `"resolved"`. Any other string is read as a cancel,
with no error.

**`forwardedProps.command.resume is deprecated`**
The old resume path. Send `RunAgentInput.resume[]` instead. Note the top-level
`resume` field is a *list*; an object fails validation with a 422.

**`No endpoints available matching your guardrail restrictions and data policy`**
An OpenRouter 404. Your account's privacy settings exclude every provider that
serves the model. Loosen them at
[openrouter.ai/settings/privacy](https://openrouter.ai/settings/privacy), or set
`MODEL` to one a first-party provider serves.

**`No tool call found for function call output with call_id ...`**
History trimming cut an assistant message but kept the `ToolMessage` that
answered it. Drop orphaned tool results whenever you trim.

**The run finishes and nothing appears**
The model returned an empty message. `RUN_STARTED` then `RUN_FINISHED`, no
error, no text. Nothing upstream reports it, so the client has to notice.

**Two chats at once corrupt each other**
`LangGraphAgent` keeps per-run state on the instance. Before
`ag-ui-langgraph` 0.0.20 the endpoint helper shared one across requests.
Upgrade, or build one per request.

**`404` on a bare model id like `gpt-4o-mini`**
OpenRouter namespaces by provider. Use `openai/gpt-4o-mini`.

## Deploying

Backend on Heroku (a Basic dyno never sleeps), frontend on Vercel. Because
visitors bring their own key, the dyno is the only cost. Full steps in
[DEPLOY.md](DEPLOY.md).

## Before deploying

- `MemorySaver` loses every thread on restart. Swap in
  `langgraph-checkpoint-sqlite` or `-postgres`.
- `ALLOWED_ORIGINS` defaults to `*`; set `RELOAD=false`.
- `MODEL` must support tool calling. A 404 from OpenRouter usually means the
  account's data policy excludes every provider that serves it.

## Reference

[AG-UI docs](https://docs.ag-ui.com) · [Events](https://docs.ag-ui.com/concepts/events) · [Interrupts](https://docs.ag-ui.com/concepts/interrupts)
