
## Make the OpenAI (or other LLM) Tools Work Better and Cheaper with a Two-Step Tool Call

I tried using OpenAI's feature for running local functions in a project with many functions. It worked well, even with lots of functions, but the cost of using OpenAI's API increased significantly. This happened because when we send function details (in JSON format) along with our main request, it counts as part of our input tokens, making it more expensive. The problem is, we often send more functions than necessary, even though the AI only needs a few of them to respond to our request.

So, I had an idea to save money and improve performace: What if we only send the details of the functions the AI actually needs? Here's how it works: First, we send a request with our main question or task, including a list of all the functions we could use, but we don't send the detailed instructions for those functions yet. We just give a brief description of each. Then, the AI tells us exactly which functions it needs to answer our question or complete our task. After that, we send another request with the detailed instructions only for those needed functions.

This method can significantly lower the cost per message because we only send the details for the functions that are necessary.
![image](https://github.com/MaurerKrisztian/two-step-llm-tool-call/assets/48491140/ce822855-5b9e-4094-96fa-89117b50bd46)
From another point of view, this method also makes the AI work faster and better. When we send too many detailed functions, we end up giving the AI too much information to handle at once. This can slow down its performance because it has to deal with a lot of extra details. However, if we only send the essential information that the AI needs, we help it stay focused and efficient. This way, we can even add more useful information without overloading it. For example, when using GPT-3 with many functions, we quickly hit the maximum amount of information it can consider at one time. By being selective about what we send, we avoid reaching this limit too soon.

Note: This code is just a demonstration currently

Read more: https://dev.to/maurerkrisztian/make-the-openai-function-calling-work-better-and-cheaper-with-a-two-step-function-call-1p96


## Results

The repo ships a benchmark (`npm run bench`) that runs identical prompts through both
strategies and compares them on real token counts. Everything below was measured against
`qwen3.5:4b` on a local Ollama, at temperature 0.

**The headline: each extra tool costs the classic approach about 165 prompt tokens on every
single request.** Two-step pays about 7.4. That ratio is what the whole method buys.

### Scaling with registry size

Three prompts (`weather`, `multi-tool`, `no-tool-needed`) run at six registry sizes:

| tools | registry chars | classic tok | 2-step tok | Δ tokens | classic prompt/req | 2-step prompt/req | classic pass | 2-step pass |
|------:|---------------:|------------:|-----------:|---------:|-------------------:|------------------:|:------------:|:-----------:|
|    11 |          4,433 |       8,403 |      4,793 |  −43.0 % |              1,527 |               571 |     3/3      |     3/3     |
|    21 |         10,973 |      16,719 |      5,191 |  −69.0 % |              3,175 |               629 |     3/3      |     3/3     |
|    41 |         24,013 |      33,098 |      6,065 |  −81.7 % |              6,460 |               737 |     3/3      |     3/3     |
|    71 |         43,573 |      57,770 |      7,322 |  −87.3 % |             11,388 |               910 |     3/3      |     3/3     |
|   111 |         69,693 |     109,139 |      8,798 |  −91.9 % |             18,004 |             1,121 |     3/3      |     3/3     |
|   161 |        102,483 |     185,696 |     21,717 |  −88.3 % |             26,356 |             1,681 |     3/3      |   2/3 ⚑     |

Reproduce with `npm run bench -- --sweep 0,10,30,60,100,150 --cases weather,multi-tool,no-tool-needed`.

### Full suite on the bare 11-tool registry

All eight cases, no padding:

| metric | classic | two-step | Δ |
|---|---:|---:|---:|
| prompt tokens | 25,054 | 13,083 | −47.8 % |
| completion tokens | 2,527 | 2,793 | +10.5 % |
| **total tokens** | **27,581** | **15,876** | **−42.4 %** |
| tool schema chars sent | 70,928 | 15,527 | −78.1 % |
| LLM round trips | 16 | 22 | +37.5 % |
| wall time | 34.4 s | 38.9 s | +13.3 % |
| cases passed | 8/8 | 8/8 | — |

Two-step already wins on tokens at the 11-tool demo registry, so break-even sits at or below
it — but note it costs **more round trips and more wall time** there. The token saving is real
from the start; the latency saving only arrives once the registry is big enough that classic's
prompts get slow to process.


## Important things to know

### Two-step is not flat — it is a 22× shallower line

The `tools_descriptor` tool lists every tool name in one flat `neededTools` enum, so the menu
grows with the registry too:

| tools | descriptor schema | share of full registry |
|------:|------------------:|-----------------------:|
|    11 |     550 chars (~138 tok) | 12.4 % |
|   161 | 4,416 chars (~1,104 tok) |  4.3 % |

At 161 tools you pay ~1,100 tokens per request for the menu alone.

### Where it breaks

At 161 tools that enum becomes its own hard problem. On the `multi-tool` case the model called
the descriptor twice and selected **nothing** both times, then gave up and called tools that had
never been unlocked — so no schema was ever on the wire. It looped until the safety limit tripped:

```
① 1 tool  → tools_descriptor unlocked: (none)
② 1 tool  → tools_descriptor unlocked: (none)
③ 1 tool  → convert_currency(…)   ✗ schema was not on the wire
④ 1 tool  → convert_currency(…)   ✗ schema was not on the wire
   … four more identical turns …
   FAIL max_calls_exceeded
```

That one run cost eight round trips and is why the last row's saving drops back to −88.3 %.
Past a few dozen tools the descriptor needs help: grouped categories, a two-level descriptor,
or retrieval over tool names rather than one flat enum.

### The benchmark ran without prompt caching

This is the biggest unmeasured hole. Ollama has no prompt caching. On providers that do, a
**static** tool block is a stable prompt prefix billed at a large discount — while two-step
changes the tool set on nearly every request and busts that prefix, paying full price. The
savings above could shrink substantially, or invert on a small registry.

Worth settling before optimising anything else: point `--base-url` / `--model` at a caching
provider and compare.

### Unlocked tools survive exactly one request

`createTwoStepToolCall` clears `options.addTools` on every recursion, so a tool the descriptor
unlocked is gone again from the next request and multi-round tasks have to re-request it. It
also means the message history can reference a tool whose schema is no longer on the wire, which
some inference servers' chat templates do not handle gracefully.

### Local Ollama and HTTP keep-alive

The benchmark disables keep-alive (`src/openai-client.ts`). Ollama drops pooled sockets between
requests and the SDK then reuses a dead one, which shows up as a deterministic `Premature close`
on the third call of a conversation — and would otherwise be scored as a strategy failure rather
than the transport artefact it is.


## Benchmark

```sh
npm run bench                       # all cases, both strategies
npm run bench -- --cases weather    # one case
npm run bench -- --pad 100          # add 100 filler tools to the registry
npm run bench -- --sweep 0,30,100   # re-run at several registry sizes and chart the scaling
npm run bench -- --repeat 3         # average over 3 runs per case
npm run bench -- --json out.json    # also write full results, including every trace event
npm run bench -- --help             # all flags
```

Defaults to a local Ollama at `http://localhost:11434/v1`. Point it anywhere OpenAI-compatible
with `--base-url` / `--model` / `--api-key`, or via `BENCH_BASE_URL`, `BENCH_MODEL`, `apikey`.

**What it compares**

| | tools on the wire |
|---|---|
| `classic` | every tool schema, on every request |
| `two-step` | only `tools_descriptor`, until the model asks for specific tools |

Both strategies share one recursion loop, one argument validator and one error path, so the only
variable is how many schemas get sent. Token counts come from the provider's own `usage` field,
not an estimate.

**What it prints**

Every round trip is one line pairing tools-sent with tokens-billed — the correlation the whole
method rests on:

```
CASE weather
  prompt: "What is the weather like in Paris right now?"
  why: single tool, one required argument
  expects: get_current_weather

  CLASSIC  (all schemas every request)
    ① 11 tools, 4,433 chars · 2 msgs → 1,446 prompt + 115 completion tok · 1.9s · tool_calls
        ↳ get_current_weather({"location":"Paris, France"}) ✓ args valid
    ② 11 tools, 4,433 chars · 4 msgs → 1,586 prompt + 186 completion tok · 2.2s · stop
        "I was able to retrieve the current weather data for Paris, France. However, the specific weathe…"
    PASS · 2 requests · 11.0 tools/request · 3,333 tokens · 8,866 schema chars · 4.0s

  TWO-STEP (schemas fetched on demand)
    ① 1 tool, 552 chars · 2 msgs → 425 prompt + 78 completion tok · 1.2s · tool_calls
        ↳ tools_descriptor unlocked: get_current_weather
    ② 2 tools, 889 chars · 4 msgs → 622 prompt + 52 completion tok · 0.9s · tool_calls
        ↳ get_current_weather({"location":"Paris, France"}) ✓ args valid
    ③ 1 tool, 552 chars · 6 msgs → 602 prompt + 171 completion tok · 2.2s · stop
        "Based on the current weather data for Paris, France, I can help you with the weather conditions…"
    PASS · 3 requests · 1.3 tools/request · 1,950 tokens · 1,993 schema chars · 4.3s
```

Then a per-case table, totals with a delta on every metric, a `TOOLS ON THE WIRE vs TOKENS
BILLED` table grouping every request by how many schemas it carried, and a breakdown of failure
reasons. A run fails for a named reason, so a cheaper-but-worse result stays visible rather than
hidden:

| reason | meaning |
|---|---|
| `missing_tool` | an expected tool was never called |
| `wrong_args` | called, schema-valid, but the values are wrong |
| `invalid_args` | arguments failed the tool's JSON Schema |
| `called_unavailable_tool` | **two-step specific** — the model called a tool before requesting it, so no schema was on the wire |
| `hallucinated_tool` | the model invented a tool name |
| `unexpected_tool` | called a tool the case does not ask for |
| `max_calls_exceeded` | the recursion limit tripped |
| `no_final_answer` | the loop ended without any text for the user |

A run only passes if every expected tool actually executed with schema-valid arguments *and* the
case's own value assertions held.

Filler tools added by `--pad` are realistic back-office schemas (`fetch_invoice_record` and
friends) that no prompt ever needs. They exist to be paid for — which is exactly the situation
the method is built for.


## Project structure

| file | role |
|---|---|
| `src/two-step-tool-call.ts` | the method — descriptor tool, recursion, tool dispatch |
| `src/classic-tool-call.ts` | the baseline it is measured against |
| `src/trace.ts` | trace events + the instrumented client that records `usage` and latency |
| `src/validate-args.ts` | AJV validation of tool arguments against `function.parameters` |
| `src/openai-client.ts` | client construction (keep-alive disabled, see above) |
| `src/schema-examples.ts` | 11 demo tools and their stub implementations |
| `src/example.ts` | interactive REPL |
| `src/benchmark/` | cases, scoring, padding generator, reporter, CLI |


## Setup

```sh
npm install
npm start
```

`npm start` runs the interactive example. It defaults to a local Ollama
(`http://localhost:11434/v1`, model `qwen3.8:latest`); override with `BENCH_BASE_URL` and
`BENCH_MODEL`. To use OpenAI instead, set your key in `.env` as `apikey` and point
`BENCH_BASE_URL` at `https://api.openai.com/v1`.
