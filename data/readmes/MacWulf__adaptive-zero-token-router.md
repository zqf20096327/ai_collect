# adaptive-zero-token-router

Local, zero-token intent routing for prompts that need to choose between cheap chat, tooling, coding, refactor/debugging, or planning paths.

The library runs before any LLM call. It uses deterministic routing plus optional local adaptive examples. No prompt leaves the process. No model call is required to decide the route.

## Why this exists

LLM apps often waste money by sending every turn to the strongest model. Many turns are small:

- "What does this mean?"
- "Reply OK. Do not edit files."
- "Check the logs."
- "Fix this bug."
- "Refactor this module."

Those are different execution modes. A local router can pick the right lane before tokens are spent.

This package focuses on one product-grade rule:

> Saving tokens is only useful when dangerous downroutes stay near zero.

A dangerous downroute means routing work to a weaker lane than the prompt needs, for example coding work routed to chat.

## Features

- Local only: no network call, no API key, no hosted classifier.
- Zero-token: routing happens before LLM inference.
- Negation-aware: "do not edit files" does not trigger coding.
- English and Hungarian-oriented normalization, including accent folding.
- Previous-prompt context for short follow-ups.
- Optional adaptive profile built from approved local examples.
- Eval gate with dangerous downroute, upward route, and savings counters.
- TypeScript-first API and small CLI.

## Install

```bash
npm install adaptive-zero-token-router
```

## Quick Start

```ts
import { routeIntent } from "adaptive-zero-token-router";

const result = routeIntent({
  prompt: "Reply exactly OK. Do not create, edit, delete, or move files."
});

console.log(result.route);  // "chat"
console.log(result.family); // "chat-small"
```

Positive work outside a negated clause still routes upward:

```ts
routeIntent({ prompt: "Do not explain, fix the bug." }).route;
// "coding"
```

Hungarian prompts are normalized too:

```ts
routeIntent({ prompt: "Ne irj kodot, csak valaszolj roviden." }).route;
// "chat"

routeIntent({ prompt: "Ne magyarazd tul, javitsd ki a hibat." }).route;
// "coding"
```

## Routes and Families

The router returns two levels:

| Field | Values | Meaning |
| --- | --- | --- |
| `route` | `chat`, `tooling`, `coding` | Execution lane |
| `family` | `chat-small`, `planning`, `agentic-tooling`, `code-edit`, `code-refactor`, `debugging` | More specific model/policy bucket |
| `intent` | `conversation`, `planning`, `tooling`, `coding` | User intent |

Apps can map those families to models however they want.

Example:

```ts
const modelByFamily = {
  "chat-small": "cheap-chat-model",
  planning: "strong-reasoning-model",
  "agentic-tooling": "tool-capable-model",
  "code-edit": "code-model",
  "code-refactor": "strong-code-model",
  debugging: "strong-code-model"
};
```

## Previous-Prompt Context

Short follow-ups can be ambiguous:

```ts
const previous = routeIntent({ prompt: "Refactor the router into smaller files." });

const next = routeIntent({
  prompt: "go ahead",
  previous
});

console.log(next.route); // "coding"
```

Explicit no-code/no-tool instructions still win:

```ts
routeIntent({
  prompt: "Reply OK. Do not write code or touch files.",
  previous
}).route;
// "chat"
```

## Adaptive Profile

The adaptive layer is local and opt-in. It builds simple token centroids from approved examples, then only applies them when confidence is high and the safety policy allows it.

```ts
import {
  buildAdaptiveProfile,
  createAdaptiveRouter,
  evaluateRouter
} from "adaptive-zero-token-router";

const examples = [
  {
    id: "ex-1",
    prompt: "Search the workspace and summarize the failing test.",
    expectedRoute: "tooling",
    expectedFamily: "agentic-tooling"
  },
  {
    id: "ex-2",
    prompt: "Ne irj kodot, csak mondd el roviden.",
    expectedRoute: "chat",
    expectedFamily: "chat-small"
  }
];

const profile = buildAdaptiveProfile({ examples });
const router = createAdaptiveRouter({ profile });

const report = evaluateRouter({ router, corpus: examples });
console.log(report.dangerousDownrouteCount);
```

Adaptation should be gated before release. Do not accept a profile only because accuracy increased. Reject it if dangerous downroutes appear.

## CLI

Evaluate a JSONL corpus:

```bash
aztr eval examples/corpus.jsonl
```

Each JSONL line:

```json
{"id":"case-1","prompt":"Fix the failing login test.","expectedRoute":"coding","expectedFamily":"debugging"}
```

Route one prompt:

```bash
aztr route "Do not edit files, just explain the error."
```

## Safety Model

This library is conservative by design.

- Negated action words are removed from action scoring.
- Explicit chat/no-action requests can suppress previous coding/tooling context.
- Adaptive profile cannot downgrade a deterministic coding/tooling result to chat.
- Eval reports count dangerous downroutes separately from safer upward routes.

Known limitation: this is not a semantic LLM classifier. It is a fast local router. Use a strong fallback route for high-risk tasks.

## Metrics

`evaluateRouter` reports:

- route accuracy
- family accuracy
- dangerous downroutes
- upward routes
- sideways mismatches
- estimated savings units
- quality-adjusted savings units

Savings units are relative, not provider pricing. Use them to compare router configs, not to estimate a cloud bill.

## Measured Results

This repository currently includes a small synthetic smoke corpus. It is meant to prove installability and core behavior, not to claim broad benchmark coverage.

Current public smoke corpus:

| Metric | Result |
| --- | ---: |
| Cases | 6 |
| Route accuracy | 100% |
| Family accuracy | 100% |
| Dangerous downroutes | 0 |
| Upward routes | 0 |
| Sideways mismatches | 0 |
| Relative savings | 43.8% |

The original extraction source was also tested on a larger internal English/Hungarian routing corpus before this public package was created:

| Metric | Result |
| --- | ---: |
| General eval cases | 108 |
| General route accuracy | 100% |
| General family accuracy | 100% |
| Hungarian hard cases | 40 |
| Hungarian hard route accuracy | 100% |
| Hungarian hard family accuracy | 100% |
| Dangerous downroutes | 0 |
| Unsafe downgrades | 0 |
| Relative savings, general corpus | 46.3% |
| Relative savings, Hungarian cases | 46.7% |
| Relative savings, English cases | 45.8% |
| Relative savings, mixed-language cases | 45.8% |
| Relative savings, Hungarian hard corpus | 47.5% |

Those internal cases were reviewed and generalized during extraction. They are not bundled here because public corpora must avoid private project context and user-specific transcripts.

## Expected Savings

For traffic similar to the evaluated corpora, expect roughly **40-50% relative model-cost reduction** compared with sending every turn to a strongest-model baseline.

This is not a provider price guarantee. Actual bill savings depend on:

- which model each app maps to `chat-small`, `planning`, `agentic-tooling`, `code-edit`, `code-refactor`, and `debugging`
- traffic mix
- prompt and completion token sizes
- whether high-risk tasks intentionally route upward
- whether the adaptive profile is enabled or deterministic-only mode is used

The router itself adds no LLM call, so its routing cost is CPU time only.

## Speed

Routing is designed to be cheaper than asking another model which model to use.

Measured runtime on a Windows development machine during extraction:

| Measurement | Result |
| --- | ---: |
| Cold first decision | 128.36 ms |
| Warm average decision | 0.68 ms |
| Warm median decision | 0.43 ms |
| Warm p95 decision | 0.68 ms |

These numbers measure local routing only. They do not include LLM inference, network latency, tool execution, or app UI work.

## Privacy

The package does not include private training data. Example prompts are synthetic and generic.

When building your own adaptive profile:

- store examples locally unless users opt in
- redact paths, names, email addresses, secrets, tickets, and company-specific terms
- keep raw transcripts out of public corpora
- publish only reviewed, generalized examples

## Status

Early public extraction. API may change before `1.0`.

Good fit:

- local-first desktop apps
- model selection before LLM calls
- routing between chat/tool/coding lanes
- multilingual apps that need cheap deterministic safeguards

Bad fit:

- replacing a full semantic classifier
- autonomous safety decisions
- routing where one wrong downgrade is unacceptable without a strong fallback

## Development

```bash
npm install
npm run check
```

## License

MIT
