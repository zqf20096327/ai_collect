# CouncilEx

Multi-model LLM council workflows for Elixir.

Define a council of specialized members, run structured rounds of analysis,
and synthesize a final answer. Works against popular providers (OpenAI,
Anthropic, Gemini, Ollama, OpenRouter). Built to get richer answers from
multiple models while keeping control over the process.

Inspired by Andrej Karpathy's [karpathy/llm-council](https://github.com/karpathy/llm-council):
the multi-stage peer-review pattern that motivated this framework.

![CouncilEx](https://raw.githubusercontent.com/brewingelixir/council_ex/main/assets/council.png)

## Contents

- [Features](#features): what ships in core, ordered by abstraction layer
- [Installation](#installation): adding the dep
- [Quickstart](#quickstart): runnable OpenRouter council in 4 steps
- [Examples](#examples): index of `examples/*.exs` by topic
- [Concepts](#concepts): vocabulary used throughout the rest of the doc
- [Council forms](#council-forms): static (DSL) vs dynamic (data) councils
- [Providers](#providers): OpenAI / Anthropic / Gemini / Ollama / OpenRouter
- [Profiles](#profiles): reusable per-member capability bundles
- [Running councils](#running-councils): sync, async, Phoenix integration, retries
- [Council topologies](#council-topologies): pre-built templates (Specialist, Tournament, WeightedConsensus, JuryWithRetry, …)
- [Per-member capabilities](#per-member-capabilities): structured outputs, streaming, tools
- [Composition](#composition): sub-councils + adaptive routers
- [Auto-routing with AutoCouncil](#auto-routing-with-autocouncil): councils that pick themselves
- [Observability](#observability): PubSub events, telemetry, verbose tracer, diagrams, introspection
- [Testing](#testing): Mock provider, test helpers, capture-events
- [Deployment Considerations](#deployment-considerations): single-node / cluster / replica / ephemeral
- [Roadmap & changelog](#roadmap--changelog): shipped + planned
- [License](#license)

## Features

Ordered roughly from core primitives → execution → per-member capabilities →
reliability → observability → dev tooling.

- 🏛️ **Static & dynamic councils**: declare councils with the `use CouncilEx` DSL or build them as data via `%CouncilEx.DynamicCouncil{}` (pipeable builder, JSON ser/de, registry-by-string-name).
- 🔌 **Multi-provider adapters**: OpenAI, Anthropic, Gemini, and OpenRouter implement the `CouncilEx.Provider.Adapter` behaviour; Ollama ships as a config preset over the OpenAI adapter. All five are built in.
- 🥊 **Round library**: `:independent_analysis`, `:peer_review`, `:vote`, `:pairwise_elimination`, plus prebuilt `Councils.{Specialist,Consensus,Tournament,WeightedConsensus,JuryWithRetry}` and a custom-round behaviour.
- ⚖️ **Confidence-triggered retry**: `Councils.JuryWithRetry` runs K judges in parallel and re-samples on low average confidence (default threshold `0.7`, max `2` iterations). Judges DO NOT see each other across retries: independent re-sample, not debate. Pattern convergent across Chaos-MoA / Adjudicator / production systems; respects Wu et al. _Can LLM Agents Really Debate?_ (arXiv:2511.07784).
- ⚖️ **Reliability-weighted consensus**: `Councils.WeightedConsensus` weights member contributions by static `:weight` opts, per-member `:confidence` scores, or historical `Reliability` lookups. Inspired by Wu et al. _Council Mode_ (arXiv:2604.02923); full mapping in [`docs/COUNCIL_MODE_PAPER.md`](docs/COUNCIL_MODE_PAPER.md).
- 🎯 **Per-member confidence**: opt-in `:confidence` strategies (`:self_report`, `:logprob`) populate `%MemberResult{}.confidence` for downstream weighting.
- 🔍 **BiasDetector**: diagnostic-only `CouncilEx.BiasDetector.analyze/2` flags when member disagreement correlates with demographic axes (gender, ethnicity, religion, age, ability). Lexicon backend in core. LLM-judge and embedding-cluster backends planned.
- 📚 **Reliability store**: `CouncilEx.Reliability` (ETS default, pluggable) tracks per-member historical accuracy by query features. Feeds `WeightedConsensus` for adaptive weighting.
- ⚡ **Sync + async runs**: blocking `run/3` for short workflows, `start/3` (`GenServer.start/3` semantics: unsupervised, unlinked) and `start_link/3` (linked to caller) for async. Both return `{:ok, pid}`. Communicate with the runner via message passing, like any GenServer.
- 🛂 **Pre-run validation**: `CouncilEx.validate/1` returns structured `[%{path, code, message}]` errors for module-form _or_ `%DynamicCouncil{}` councils. `start/3` gates on it so config errors return `{:error, {:invalid_council, errs}}` before any process spawns or token is spent.
- 🌳 **Optional run grouping**: `CouncilEx.Supervisor` is a thin `DynamicSupervisor` wrapper for callers who want tenant isolation, bulk-terminate, or in-flight visibility. Library has no bundled supervisor: runs are unsupervised by default (caller's responsibility, like `GenServer.start/3`).
- 🪆 **Sub-councils**: nest a council as a member; works in static and dynamic forms (registered name, module atom, or nested `%DynamicCouncil{}`) with optional input mappers.
- 🚦 **Routers**: dynamic next-step selection between members or rounds, declared inline or registered by name.
- 🤖 **AutoCouncil**: opt-in routing layer. A council that picks itself. Pluggable strategies (`:rules`, `:cascade`, plus stub `:embedding` / `:llm_classify` / `:llm_build`) select an existing council per prompt, or synthesize a fresh `%DynamicCouncil{}` on the fly. Same `CouncilEx.run/3` entry. Routing decision surfaced in `result.metadata.auto`.
- 🛠️ **Tool calling**: parallel tool execution with concurrency + timeout knobs, multi-iteration tool-loops in both `complete/2` and `stream/3`, and `:tool_choice` (`:auto | :required | :none | "name"`).
- 📚 **RAG via tools**: council-level `add_council_tool/2` exposes a shared toolset to every member. Per-member `:tools` keeps specialist corpora private. `CouncilEx.Tools.InMemoryDocs` is a zero-dep BM25 retrieval tool baked from a compile-time corpus, useful for examples and tests. Production retrieval should wrap your real index. See [`docs/RAG.md`](docs/RAG.md).
- 📐 **Structured output**: Ecto-schema or inline JSON Schema per member, with native `responseSchema` (Gemini) and tool-shaped fallback (OpenAI/Anthropic).
- 🌊 **Streaming**: token-level streaming with sink callbacks, integrated with the tool-loop so tool-spanning turns look like one continuous response.
- 🎛️ **Profiles**: reusable per-member capability bundles (provider, model, temperature, tools, retry); 9 prebaked profiles plus user-defined `use CouncilEx.Profile` modules.
- 🔀 **Polymorphic dispatch**: `CouncilEx.run/3` and `start/3` take either a module-form council or a `%DynamicCouncil{}`; one execution path, identical semantics.
- 🛡️ **Failure handling**: per-round `failure_mode: :continue | :fail_fast`, retry policies, member timeouts, run-level `cancel/1`, and structured `%CouncilEx.Error{}`.
- 📒 **Registry**: config + runtime registration of profiles, tools, schemas, routers, rounds, sub-councils, and input mappers, all resolvable by string name.
- 📡 **PubSub events**: 10 frozen events on `"council_ex:run:#{run_id}"` (`CouncilEx.Events`); idempotent subscribe across `:pg` and Phoenix.PubSub adapters.
- 📊 **Telemetry**: `[:council_ex, :run | :round | :member | :tool, :*]` events with full parity on the modern async path; ~3µs/event overhead.
- 🔍 **Verbose tracer**: `verbose: true | :debug` opt prints a human-readable per-run timeline (member start/stop, durations, tokens, tool calls). Pure event consumer, zero production cost when off.
- 🗺️ **Diagram tooling**: `CouncilEx.Diagram.{to_ir,topology,sequence}` for both council shapes; IR is React-Flow-friendly JSON.
- 🧪 **Mock provider**: scriptable in-memory provider for tests and example fixtures (`CouncilEx.Providers.Mock.script/2`); **not for production use**.

## Installation

```elixir
def deps do
  [
    {:council_ex, "~> 0.1"}
  ]
end
```

Real LLM providers need a configured adapter + API key (e.g. `OPENAI_API_KEY`,
`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`). See
[Providers](#providers).

### Optional dependencies

The core (parallel rounds, aggregation, streaming, tools, telemetry/PubSub
observability) needs nothing beyond the dep above. Each opt-in backend pulls
its own library — add it only when you use that feature:

| Feature                                                                 | Add to `deps`                                                      | Docs                                                |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------- |
| Ecto persistence (`Recorder`/`Registry`/`Reliability.Ecto`, migrations) | `{:ecto_sql, "~> 3.13"}` + a driver, e.g. `{:postgrex, "~> 0.20"}` | [PERSISTENCE.md](docs/PERSISTENCE.md)               |
| Durable background runs                                                 | `{:oban, "~> 2.19"}`                                               | [RUNNING_WITH_OBAN.md](docs/RUNNING_WITH_OBAN.md)   |
| Redis backends (`Registry`/`Reliability.Redis`)                         | `{:redix, "~> 1.5"}`                                               | —                                                   |
| Route events through your own PubSub                                    | `{:phoenix_pubsub, "~> 2.1"}`                                      | [RUNNING_IN_PHOENIX.md](docs/RUNNING_IN_PHOENIX.md) |

These are declared `optional: true`, so they are **not** installed transitively
— including under `Mix.install` (e.g. in a Livebook). council_ex compiles fine
without them; the relevant modules are simply omitted until the dep is present.

## Quickstart

This walkthrough uses **OpenRouter** to answer the meta-question: _when
should you use an LLM council instead of a single model call?_
OpenRouter is the easiest way to start. One API key reaches every major
frontier model (`openai/gpt-4o`, `anthropic/claude-sonnet-4-6`,
`google/gemini-2.5-flash`, `meta-llama/llama-3.3-70b-instruct`, etc.), so a multi-model
council needs no extra wiring. The same council code runs against OpenAI,
Anthropic, Gemini, or Ollama directly. See [Providers](#providers).

```elixir
# 1. Configure OpenRouter. Set OPENROUTER_API_KEY in your shell.
Application.put_env(:council_ex, :providers,
  openrouter: [
    adapter: CouncilEx.Provider.Adapters.OpenRouter,
    api_key: {:system, "OPENROUTER_API_KEY"}
  ]
)

# 2. Define members (identity: role + system prompt)
defmodule MyApp.Members.Advocate do
  use CouncilEx.Member
  role "Advocate"

  system_prompt """
  You argue FOR using a multi-model LLM council. Given the user's task,
  list 3-5 concrete situations where multiple model voices outperform a
  single call (e.g. high-stakes decisions, contested judgement, weak
  ground truth, creative divergence). Be specific. No hedging.
  """
end

defmodule MyApp.Members.Skeptic do
  use CouncilEx.Member
  role "Skeptic"

  system_prompt """
  You argue AGAINST using a multi-model LLM council. Given the user's
  task, list 3-5 concrete situations where a council is overkill or
  actively harmful (latency, cost, false consensus, deterministic
  problems with a known answer). Be specific. No hedging.
  """
end

defmodule MyApp.Members.Synthesizer do
  use CouncilEx.Member
  role "Synthesizer"

  system_prompt """
  Read the Advocate's and Skeptic's lists. Produce a short decision rule
  the reader can apply to their own task: "use a council when …, skip it
  when …". Two short paragraphs max.
  """
end

# 3. Define a council (capability: provider + model)
#    Each member can run on a different frontier model. That's the
#    point. OpenRouter exposes them all under one provider.
defmodule MyApp.WhenToCouncil do
  use CouncilEx

  member :advocate, MyApp.Members.Advocate,
    provider: :openrouter, model: "openai/gpt-4o-mini"

  member :skeptic, MyApp.Members.Skeptic,
    provider: :openrouter, model: "anthropic/claude-sonnet-4-6"

  round :independent_analysis

  chair MyApp.Members.Synthesizer, id: :chair,
    provider: :openrouter, model: "openai/gpt-4o"
end

# 4. Run
{:ok, result} =
  CouncilEx.run(
    MyApp.WhenToCouncil,
    %{question: "When should I use an LLM council instead of a single LLM call?"}
  )

IO.puts(result.final.content)
```

<details>
<summary>Example run output (<code>VERBOSE=1 mix run examples/quickstart_example.exs</code>)</summary>

```
VERBOSE=1 mix run examples/quickstart_example.exs                                                                        17s 17:48:01

▶ run …Sd72NF started council=QuickstartCouncil.WhenToCouncil
  ▶ round independent_analysis (#0)
    ▶ advocate
    ▶ skeptic
    ✓ advocate 5547ms  in=90 out=361
    ✓ skeptic 5839ms  in=91 out=398
  ✓ round independent_analysis
  ▶ round synthesis (#1)
    ▶ chair
    ✓ chair 3825ms  in=918 out=156
  ✓ round synthesis
✓ run …Sd72NF ok
=== Panel members (independent_analysis round) ===

[advocate]
1. **High-Stakes Decisions**: multiple model voices minimize catastrophic-error risk …
2. **Contested Judgement**: subjective calls benefit from differing viewpoints …
   … (5 situations total)

[skeptic]
1. **Latency in Time-Sensitive Applications**: each model query adds delay …
2. **Cost-Efficiency in High-Volume Use Cases**: per-call costs multiply …
   … (5 situations total)

=== Final synthesis (chair) ===
Use a council for complex, high-stakes, or contested decisions where multiple
perspectives or weak/disputed data justify the extra cost. Skip it when the task
demands speed, cost-efficiency, or has a clear single answer.

Total duration: 15226ms
Total tokens: 2014
```

</details>

The Advocate and Skeptic run in parallel during the
`:independent_analysis` round; the Synthesizer chair sees both outputs and
produces the final answer. Inspect `result.rounds` for each member's
verdict and `result.metadata` for token + timing totals.

A runnable version of this exact council lives in
[`examples/quickstart_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/quickstart_example.exs).
Run it with `OPENROUTER_API_KEY=sk-or-v1-... mix run examples/quickstart_example.exs`.

> **Single-vendor variant:** If you only have one vendor's API key
> (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`), swap the
> provider config in step 1 for that vendor's adapter and use that
> vendor's model ids (see [Providers](#providers)). The council code is
> unchanged.

> **Karpathy-style 3-stage council:** for the
> opinions → anonymized peer review → chairman pattern from
> `karpathy/llm-council`, see
> [`docs/TUTORIAL_KARPATHY_COUNCIL.md`](docs/TUTORIAL_KARPATHY_COUNCIL.md)
> and the runnable
> [`examples/karpathy_council_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/karpathy_council_example.exs).
> Decision guide for picking between `PeerReview` and
> `AnonymizedPeerReview` lives at
> [`docs/PEER_REVIEW_PATTERNS.md`](docs/PEER_REVIEW_PATTERNS.md).

> **Mock provider:** `CouncilEx.Providers.Mock` exists for tests and
> deterministic example fixtures only. Do not use it as a stand-in for a
> real LLM in application code. See [Test helpers](#test-helpers).

## Examples

Index of `examples/*.exs`. Every example runs against a real provider
(default OpenAI or OpenRouter: see the `Run:` comment at the top of
each file for the required API key). The `Mock` provider exists for
tests only; do not run it as a stand-in for an LLM in examples.

Most examples support the `COUNCIL_FORM=static|dynamic` env switch
(see [Dual-form pattern](#dual-form-pattern)). Examples that don't
support the switch: `dynamic_council_example.exs` (already dynamic),
the prebaked `Councils.{Specialist,Consensus,Tournament}.new/1`
wrappers (`specialist`, `consensus`, `tournament`), and the
council-bypass demos (`parallel_tools`, `tool_call_events`).
`sub_council_example.exs` also supports the switch.

**Topologies & composition**

- [`parallel_panel_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/parallel_panel_example.exs): simplest panel + chair
- [`karpathy_council_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/karpathy_council_example.exs): Karpathy `llm-council` 3-stage port — opinions → `anonymized_peer_review` (`PeerRanking`) → chairman. See [`docs/TUTORIAL_KARPATHY_COUNCIL.md`](docs/TUTORIAL_KARPATHY_COUNCIL.md)
- [`debate_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/debate_example.exs): Pro/Con + chained `peer_review` rounds
- [`peer_review_manuscript_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/peer_review_manuscript_example.exs): `Councils.PeerReview.new/1` as literal scientific peer review — theorist presents → 3 distinct-lens reviewers critique → author rebuts → journal editor's decision letter
- [`specialist_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/specialist_example.exs): `Councils.Specialist.new/1`
- [`consensus_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/consensus_example.exs): `Councils.Consensus.new/1` with convergence callback
- [`tournament_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/tournament_example.exs): `Councils.Tournament.new/1`
- [`weighted_consensus_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/weighted_consensus_example.exs): `Councils.WeightedConsensus.new/1` with static `:weight` opts (Wu et al. _Council Mode_)
- [`jury_with_retry_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/jury_with_retry_example.exs): `Councils.JuryWithRetry.new/1`, K judges + confidence-triggered re-sample
- [`pr_review_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/pr_review_example.exs): **analyst → judge → chair** topology. Per-round routers split a single roster (analysts run round 1, judges vote in round 2 with `Plurality` over `Schemas.Vote`, chair synthesizes citing tally + dissent + analyst findings; chair may override plurality on critical analyst severity)
- [`confidence_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/confidence_example.exs): per-member `:self_report` confidence driving `WeightedConsensus` weights
- [`bias_detector_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/bias_detector_example.exs): `CouncilEx.BiasDetector.analyze/2` over a `ParallelPanel` on a value-laden question
- [`reliability_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/reliability_example.exs): `CouncilEx.Reliability` ETS store. Records outcomes, scores per `(member, query_features)` (no API key required)
- [`pairwise_direct_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/pairwise_direct_example.exs): raw `Iterate(PairwiseElimination)` composition
- [`router_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/router_example.exs): adaptive `CouncilEx.Router`
- [`auto_council_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/auto_council_example.exs): `CouncilEx.AutoCouncil` routing across three small councils (inline rules, registry catalog, `provider_check`, `CouncilEx.auto/1` shortcut)
- [`sub_council_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/sub_council_example.exs): hierarchical sub-council member
- [`dynamic_sub_council_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/dynamic_sub_council_example.exs): three sub-council reference shapes (inline struct, registered name, registered name + input_mapper) for `%DynamicCouncil{}`
- [`presidential_debate_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/presidential_debate_example.exs): N-member `PeerReview`: four candidates rebut across chained rounds, Pundit chair synthesizes
- [`multi_model_panel_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/multi_model_panel_example.exs): three vendors, one panel
- [`agi_debate_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/agi_debate_example.exs): **all five providers** (OpenAI / Anthropic / Gemini / Ollama / OpenRouter), one perspective each, debating AGI timing + post-AGI society + human-AI cooperation

**Profiles & dynamic councils**

- [`profile_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/profile_example.exs): `default_profile`, `profile:` overrides, inline overrides
- [`creative_judge_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/creative_judge_example.exs): `OpenAICreative` writers + `OpenAIDeterministic` judge
- [`dynamic_council_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/dynamic_council_example.exs): builder → validate → JSON round-trip → run; includes inline JSON schema member

**Custom rounds & voting**

- [`custom_round_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/custom_round_example.exs): implements four of `CouncilEx.Round`'s five callbacks (all but the optional `converged?/3`)
- [`vote_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/vote_example.exs): `:vote` round with Plurality vs WeightedMean

**Streaming & tools**

- [`streaming_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/streaming_example.exs): OpenAI token streaming
- [`anthropic_streaming_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/anthropic_streaming_example.exs): Anthropic typed-event streaming
- [`tool_calling_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/tool_calling_example.exs): full tool loop + tool error recovery
- [`tool_call_events_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/tool_call_events_example.exs): per-call PubSub events (real OpenAI provider)
- [`rag_via_tools.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/rag_via_tools.exs): RAG via council-level + per-member `InMemoryDocs` tools (real OpenRouter provider)
- [`bench/parallel_tools.exs`](bench/parallel_tools.exs): sequential vs parallel tool exec (benchmark)

**Operational concerns**

- [`error_handling_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/error_handling_example.exs): retry, `failure_mode`, `cancel/1`, `await/2` timeout
- [`verbose_tutorial_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/verbose_tutorial_example.exs): `verbose: true`/`:debug` and `verbose_io:` capture
- [`phoenix_pubsub_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/phoenix_pubsub_example.exs): pluggable PubSub backend

**Per-provider quickstarts**

- [`gemini_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/gemini_example.exs), [`ollama_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/ollama_example.exs), [`openrouter_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/openrouter_example.exs), [`anthropic_structured_output_example.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/anthropic_structured_output_example.exs), [`parallel_panel_real_provider.exs`](https://github.com/brewingelixir/council_ex/blob/main/examples/parallel_panel_real_provider.exs)

## Concepts

Vocabulary used throughout the rest of the README.

- **Council**: the workflow itself. A named ordering of members + rounds + an optional chair. Two interchangeable forms: module-form (`use CouncilEx`) or data-form (`%CouncilEx.DynamicCouncil{}`).
- **Member**: one LLM seat at the table. Defines _identity_ (`role`, `system_prompt`, optional `output_schema`). Identity is reusable; pair it with different capability stacks via Profiles.
- **Profile**: _capability_ stack (`provider`, `model`, `temperature`, `max_tokens`, `tools`, `retry`). Same Member + different Profile = same brain, different model. Resolution: inline opts > member `:profile` > council `default_profile` > app config.
- **Round**: one phase of the run. Built-in types: `:independent_analysis` (members run in parallel), `:peer_review` (members see each other's prior turn), `:vote` (each member emits a ballot, aggregator picks a winner), `:pairwise_elimination` (tournament bracket), plus `:anonymized_peer_review`, `:critique`, `:ranking`, `:synthesis`, `:iterate`, and user-defined `CouncilEx.Round` modules. A council can have any number of rounds.
- **Chair**: final synthesis member. Runs once after all rounds, sees every prior member output, and produces `%Result{}.final`. Optional. Councils without a chair return per-round results only.
- **Router**: dynamic next-step picker. Inspects state mid-run and chooses the next member or round. Inline closure or registered-by-name.
- **Sub-council**: a council used as a member of another council. Composes vertically: the outer council sees the sub-council's `final` as that member's response. Works in static + dynamic forms.
- **Run**: one execution of a council against an input. Identified by `run_id`. Sync via `run/3`, async via `start/3` + `await/2` / `cancel/1`.
- **Result**: `%CouncilEx.Result{}` returned from `run/3` and `await/2`. Carries `input`, per-round `%RoundResult{}` (with per-member `%MemberResult{}`), `final` chair response, `status`, `errors`, and `metadata` (timings + token totals).
- **Tool**: Elixir module implementing `CouncilEx.Tool` that the model can call mid-turn. Parallel execution + multi-iteration tool-loops are built in.
- **Aggregator**: function that reduces a `:vote` round's ballots into a winner. `Plurality`, `WeightedMean` ship in core; user-defined ones plug into the same interface.
- **Registry**: runtime/config table of named profiles, tools, schemas, routers, rounds, sub-councils, and input mappers. Lets data-form councils reference behaviour by string name (`"my_tool"`) instead of module atoms, required for JSON ser/de.
- **Provider adapter**: module behind a configured `provider:` key (`:openai`, `:anthropic`, …) that translates a normalized request into an HTTP call and parses the response. Implements `CouncilEx.Provider.Adapter`. OpenAI / Anthropic / Gemini / Ollama / OpenRouter ship in core.
- **Council vs ensemble**: a classical ensemble = N models in parallel + flat aggregator (one round, no roles). A council adds roles, multi-round flow, cross-member visibility, iteration, chair synthesis, sub-councils, and dynamic routing. Only the `Voting` topology reduces to ensemble shape; the other six add structure ensembles cannot express. See [`docs/COUNCILS.md`](docs/COUNCILS.md#council-vs-ensemble) for the full comparison.
- **AutoCouncil**: `%CouncilEx.AutoCouncil{}` data struct that _resolves_ to a council at run time. Holds a `:strategy` (`:rules`, `:cascade`, …), a `:catalog` of routable councils (inline list or registry-backed), and an `:on_no_match` policy. From the runner's perspective it _is_ a council. Pass it to `CouncilEx.run/3` like any other. The picked council's identity surfaces in `result.metadata.auto`. See [Auto-routing](#auto-routing-with-autocouncil).

## Council forms

CouncilEx exposes two interchangeable ways to declare a council. Both lower to the
same `%CouncilEx.Spec{}` and execute through the same runtime — behaviour,
telemetry, and `%Result{}` shape are identical.

| Pick                              | When                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| **Static** (`use CouncilEx`)      | Workflow is checked into code. Members, rounds, chair, router known at compile time. |
| **Dynamic** (`%DynamicCouncil{}`) | Workflow built at runtime, persisted to a DB as JSON, edited in a UI.                |

`CouncilEx.run/3` and `start/3` accept either form (polymorphic dispatch), so
you can switch a council from static to dynamic without touching call sites.

### Static module-form

```elixir
defmodule MyApp.MyCouncil do
  use CouncilEx

  default_profile CouncilEx.Profiles.OpenAIMini

  member :researcher, MyApp.Members.Researcher
  member :critic,     MyApp.Members.Critic
  round :peer_review
  chair MyApp.Members.Synthesizer, profile: CouncilEx.Profiles.OpenAIBalanced
end
```

Full DSL macro reference (member forms, `round`, `chair`, `router`, `default_profile`,
`output_schema`) and prebuilt `Councils.*` templates (ParallelPanel, PeerReview,
Voting, Specialist, Consensus, Tournament, WeightedConsensus, JuryWithRetry):
[`docs/COUNCILS.md`](docs/COUNCILS.md).

### Dynamic form, registry, sub-councils, hybrid

[`docs/DYNAMIC_COUNCILS.md`](docs/DYNAMIC_COUNCILS.md) covers everything runtime-configurable:

- **Dynamic data-form** — pipeable builder (`add_member/2`, `set_chair/2`, …), JSON round-trip (`to_json/2` / `from_json/1`), inline JSON Schema output, `profile_overrides`, React-Flow export (`to_flow_graph/1`).
- **Registry** — string-keyed lookup with config + runtime tiers; eight kinds (`:profile`, `:tool`, `:schema`, `:router`, `:round`, `:sub_council`, `:input_mapper`, `:council`).
- **Sub-councils** — nest any council (module, `%DynamicCouncil{}`, or registered name) as a member; `:input_mapper` projects input between layers.
- **Hybrid form** — static outer with dynamic sub-council, or dynamic outer referencing static modules; per-tenant flows and incremental migration.
- **Prebuilt dynamic variants** — `Councils.{Specialist,Consensus,Tournament,WeightedConsensus}.new_dynamic/1` return a `%DynamicCouncil{}`.
- **Dual-form pattern** — run the same topology as static or dynamic via a `COUNCIL_FORM=static|dynamic` switch.

## Providers

CouncilEx ships five provider adapters. Configure once in app config; route
members via the `provider:` opt or a `Profile`. The council DSL is provider-agnostic.

| Provider atom | Env var              | Notes                                                                      |
| ------------- | -------------------- | -------------------------------------------------------------------------- |
| `:openai`     | `OPENAI_API_KEY`     | Tool-calling, streaming, structured output.                                |
| `:anthropic`  | `ANTHROPIC_API_KEY`  | `response_schema:` and `tools:` are mutually exclusive per member.         |
| `:gemini`     | `GEMINI_API_KEY`     | Native `responseSchema`; same mutual-exclusion as Anthropic.               |
| `:ollama`     | _(none)_             | Config preset over the OpenAI adapter — not a separate adapter impl.       |
| `:openrouter` | `OPENROUTER_API_KEY` | Thin wrapper over the OpenAI adapter; reaches any model OpenRouter routes. |

See [`docs/PROVIDERS.md`](docs/PROVIDERS.md) for full config snippets, adapter quirks,
multi-provider council patterns, and the `CouncilEx.Provider.Adapter` behaviour
(7 required + 6 optional callbacks) for adding your own provider.

## Profiles

A `Profile` bundles the capability stack (provider, model, temperature,
max_tokens, tools, retry) separately from the Member's identity (role, system
prompt, output schema). Nine prebaked profiles ship in `CouncilEx.Profiles.*`:
`OpenAIBalanced`, `OpenAIMini`, `OpenAICreative`, `OpenAIDeterministic`,
`AnthropicBalanced`, `GeminiBalanced`, `OllamaLocal`, `OpenRouterAuto`,
`OpenRouterClaudeSonnet`.

Resolution order (later wins): app config default → council `default_profile`
→ member `:profile` opt → inline opts.

See [`docs/PROFILES.md`](docs/PROFILES.md) for defining custom profiles, dynamic-form
registration, `profile_overrides`, and the prebaked-profile capability table.

## Running councils

Start a run and block:

```elixir
{:ok, result} = CouncilEx.run(MyCouncil, %{question: "go or wait?"})
```

Start async, stream progress events, then await:

```elixir
{:ok, pid} = CouncilEx.start(MyCouncil, input, subscribe: true)
run_id = CouncilEx.RunServer.run_id(pid)

receive do
  {:round_completed, ^run_id, name, _rr} -> IO.puts("round done: #{name}")
end

{:ok, result} = CouncilEx.await(pid)
```

- **Core API** — async start/await, `cancel/2` (cooperative), `terminate_run/2`
  (non-cooperative), `validate/1`, `start` vs `start_link`, `pid_for/2`, run
  grouping with `CouncilEx.Supervisor`, retry policy:
  [`docs/RUNNING_COUNCILS.md`](docs/RUNNING_COUNCILS.md)
- **Phoenix / LiveView / channels**: [`docs/RUNNING_IN_PHOENIX.md`](docs/RUNNING_IN_PHOENIX.md)
- **Oban / background jobs**: [`docs/RUNNING_WITH_OBAN.md`](docs/RUNNING_WITH_OBAN.md)

## Council topologies

Nine pre-built templates (`ParallelPanel`, `PeerReview`, `Voting`,
`Specialist`, `Consensus`, `Tournament`, `Chairman`, `WeightedConsensus`,
`JuryWithRetry`), five aggregators (`Plurality`, `Borda`, `Condorcet`,
`WeightedMean`, `Median`), and the `Iterate` round wrapper for
convergence loops.

`WeightedConsensus` ports Wu et al. _Council Mode_ (arXiv:2604.02923):
heterogeneous members aggregated by `:weight` / `:confidence` /
`Reliability` lookup rather than equal-weight chair synthesis. Mapping
in [`docs/COUNCIL_MODE_PAPER.md`](docs/COUNCIL_MODE_PAPER.md).

`JuryWithRetry` runs K judges and re-samples on low average confidence
(default threshold `0.7`, max `2` iterations). Judges don't see each
other across iterations. Wu et al. _Can LLM Agents Really Debate?_
(arXiv:2511.07784) conformity mitigation. Pattern shared with
Chaos-MoA-Pipeline + Adjudicator. Full multi-paper context in
[`docs/RELATED_WORK.md`](docs/RELATED_WORK.md).

```elixir
council =
  CouncilEx.Councils.Specialist.new(
    as: MyApp.MyCouncil,
    members: [
      {:seo, MyApp.Members.Seo, [provider: :openai, model: "gpt-4o-mini"]},
      {:tech, MyApp.Members.Tech, [provider: :openai, model: "gpt-4o-mini"]}
    ],
    chair: {MyApp.Members.Synth, [provider: :openai, model: "gpt-4o"]}
  )

{:ok, result} = CouncilEx.run(council, %{topic: "..."})
```

See [`docs/COUNCILS.md`](docs/COUNCILS.md) for the full topology table,
aggregator catalog, iteration semantics, and `RoundResult.metadata.history`
shape.

## Per-member capabilities

CouncilEx members support structured outputs, streaming, and tool calling independently of one another. Full details — every default, Anthropic-specific behaviour, and PubSub event payloads — are in [`docs/PER_MEMBER_CAPABILITIES.md`](docs/PER_MEMBER_CAPABILITIES.md).

**Structured outputs** — set `output_schema` on a member to an Ecto embedded schema. `CouncilEx.Providers.Instructor` casts the LLM's JSON into that schema and runs the schema's optional `validate_changeset/2`; the member module's `validate/1` then runs for business rules. On Anthropic, CouncilEx forces a synthetic `_respond` tool whose `input_schema` mirrors your Ecto schema; structured-output and user `tools:` are mutually exclusive on the same member.

**Streaming** — add `stream true` to a member. During streaming the adapter reassembles Anthropic `partial_json` SSE fragments; subscribers receive `:member_token` PubSub events carrying `%CouncilEx.StreamChunk{content, index, finish_reason}`. The `[:council_ex, :member, :stream_chunk]` telemetry event fires per chunk.

**Tools** — a tool implements `CouncilEx.Tool` (four callbacks: `name/0`, `description/0`, `parameters_schema/0`, `execute/1`). The dispatcher runs a bounded tool-call loop (default `max_tool_iterations: 5`); exceptions are caught by `safe_execute/2` and surfaced as `{:tool_raised, exception}`. Multiple tool calls in one turn run in parallel by default (`parallel_tools: true`, strategy `:collect`, `tool_concurrency_factor: 1.0`, `tool_timeout_ms: 30_000`). `CouncilEx.Providers.Instructor.stream/3` drives the same loop across streaming round-trips; subscribe for `:tool_call_request` / `:tool_call_result` events (the synthetic `_respond` tool is excluded).

## Composition

Two ways to scale a council beyond a flat member list: nest a council inside
another (sub-councils, including dynamic `%DynamicCouncil{}` forms with
`input_mapper`), and gate which members participate per round (adaptive routers
— council-level or per-round override). Excluded members land in `RoundResult`
with `status: :skipped`.

See [`docs/COMPOSITION.md`](docs/COMPOSITION.md) for the full sub-council and
router surface (sub-run event topics, `:sub_run_id` / `:sub_result` metadata,
dynamic-form router registration, `:skipped` semantics, and a runnable two-level
example with mixed providers).

## Auto-routing with AutoCouncil

`CouncilEx.AutoCouncil` is an opt-in routing layer for callers that don't
know up-front which council fits a given prompt. Pass it to `CouncilEx.run/3`
like any other council — internally a _strategy_ picks from a _catalog_,
executes the winning council, and records the decision in `result.metadata.auto`:

```elixir
auto = CouncilEx.AutoCouncil.new(
  strategy: :rules,
  catalog:  [
    %{id: "seo",  council: MyApp.Councils.SEO,        match: ~r/seo|sitemap/i},
    %{id: "code", council: MyApp.Councils.CodeReview, match: ~r/code|PR/i}
  ]
)

{:ok, result} = CouncilEx.run(auto, %{question: "audit my SEO"})
result.metadata.auto
# => %{strategy: :rules, kind: :static, catalog_id: "seo",
#      reason: "matched ~r/seo|sitemap/i", score: nil, latency_ms: 1}
```

- **Strategies** — `:rules` (regex/fun, zero cost), `:cascade` (chain cheap→expensive), `:embedding` / `:llm_classify` / `:llm_build` (stubs, return `{:error, :not_implemented}`), or `{MyModule, opts}` for custom.
- **Catalog** — inline list or `{:registry, :council}` for hot-reloadable shared routing. `provider_check: true` drops entries whose providers aren't configured.
- **Fallback** — `on_no_match: :error` (default), `{:fallback, MyCouncil}`, or `{:fallback, "registered_id"}`.
- **Shortcut** — `CouncilEx.auto/1,2` uses `:council_ex, :auto` app config as default; per-call opts override it and `:verbose`/`:await_timeout` forward to `run/3`.

Full reference — `Strategy` behaviour, custom-strategy recipe, decision-shape
contract, telemetry events (`:decision`, `:cascade_step`, `:catalog_filtered`),
composability — in [`docs/AUTO_COUNCILS.md`](docs/AUTO_COUNCILS.md).

## Observability

Ten events fire on topic `"council_ex:run:#{run_id}"`:
`:run_started`, `:round_started`, `:member_started`, `:member_token`,
`:tool_call_request`, `:tool_call_result`, `:member_completed`,
`:round_completed`, `:run_completed`, `:run_failed`
(documented in `CouncilEx.Events`).

- **Phoenix.PubSub adapter** — route events through your own server:
  `config :council_ex, pubsub: {CouncilEx.PubSub.Phoenix, name: MyApp.PubSub}`.
  CouncilEx never starts a PubSub server itself.
- **Telemetry logger** — `CouncilEx.Telemetry.attach_default_logger/0,1` attaches
  Logger handlers (`:events` subset opt; `:exception` always logs at `:warning`;
  re-attach is idempotent); `detach_default_logger/0` removes them.
- **Verbose mode** — `verbose: true | :debug` prints a per-run timeline to stdout
  (zero cost when off; `verbose_io:` to redirect).

Full reference: [`docs/OBSERVABILITY.md`](docs/OBSERVABILITY.md).
Topology diagrams: [`docs/DIAGRAMS.md`](docs/DIAGRAMS.md).

**Introspection** — inspect a council's structure as data at runtime
(`Mod.__council__/0` → `%Spec{}`, `__providers__/0`), export it as a node/edge
graph for a UI (`CouncilEx.Diagram.to_ir/1`, both forms), or query a live run
(`CouncilEx.RunServer.state/1`, `list_active_runs/0`). See
[`docs/INTROSPECTION.md`](docs/INTROSPECTION.md).

## Testing

`import CouncilEx.Test` for three helpers: `script_council/2` (script Mock
responses for every member of a council — or nested sub-council — in one call),
`capture_events/2` (drain a run's PubSub topic until the terminal event or
timeout), and `assert_round_completed/3` (block on `:round_completed` and return
the `%RoundResult{}`). The Mock provider is `CouncilEx.Providers.Mock` (tests and
fixtures only; never production code).

See [`docs/UNIT_TESTING.md`](docs/UNIT_TESTING.md) for the full helper reference,
streaming scripts, and state inspection; [`docs/TESTING.md`](docs/TESTING.md) for
live-provider and manual testing.

## Deployment Considerations

A single `:mode` config knob picks the deployment shape: `:single_node`
(default, no config needed) uses an ETS-backed Registry, a Null reliability
store, and no Recorder; `:multi_node` flips all three to their `*.Ecto` defaults
and autowires `Recorder.Ecto` into every `CouncilEx.start/3` call. Per-key
overrides (`:reliability_store`, `:registry_backend`, `:recorder`) always win
over the mode default, so mixing backends (e.g. `Reliability.Redis` +
`Registry.Ecto` + `Recorder.Ecto`) is one line each.

See [`docs/PERSISTENCE.md`](docs/PERSISTENCE.md) for the module map, migration
setup, Redis backends, Oban durable retries, and the deployment topology matrix.

## Roadmap & changelog

### Capabilities

Topic-tagged highlights of what ships in the `0.1.0` release. See
[`CHANGELOG.md`](CHANGELOG.md) for the full release notes.

- **Paper-replication slate**: `Councils.WeightedConsensus` + `Rounds.WeightedSynthesis` (Wu et al. _Council Mode_ port, arXiv:2604.02923); per-member `:confidence` field on `%MemberResult{}` with `:self_report` and `:logprob` strategies; `CouncilEx.BiasDetector` diagnostic round (lexicon backend); `CouncilEx.Reliability` store (Null + ETS + Ecto/Postgres + Redis backends); `Councils.JuryWithRetry` with confidence-triggered re-sample (Chaos-MoA / Adjudicator pattern, Wu et al. _Can LLM Agents Really Debate?_ (arXiv:2511.07784) conformity mitigation); `bench/eval/` skeleton harness for TruthfulQA / HaluEval / BBQ; `:expose_confidence` opt on `WeightedSynthesis`. Mapping: [`docs/COUNCIL_MODE_PAPER.md`](docs/COUNCIL_MODE_PAPER.md) + [`docs/RELATED_WORK.md`](docs/RELATED_WORK.md).
- **Dynamic councils**: build / edit / validate / serialise data-form councils with sub-council composition (registered name / module / nested struct), polymorphic `run/3` + `start/3` dispatch, full run/round telemetry parity on the async path. `Profile` DSL + 9 prebaked profiles, per-run `verbose:` opt, OpenRouter adapter, diagram tooling (`CouncilEx.Diagram`), real-key-only examples, Gemini schema sanitization. `:tool_choice` member opt, atom-exhaustion DoS fix on JSON ser/de, idempotent `:pg` PubSub subscribe, cold-load tool-call adapter probe.
- **Providers**: stock OpenAI / Anthropic / Gemini / Ollama / OpenRouter adapters; pluggable `Provider.Adapter` behaviour; frozen `CouncilEx.Events` PubSub surface; `:member_completed` carries full `%MemberResult{}`.
- **Tool calling**: stream tool-loop in `CouncilEx.Providers.Instructor.stream/3`; parallel tool execution; tool-call PubSub events; Tournament Bracket round; Anthropic structured output via the tool-use API.
- **GenServer-aligned run lifecycle**: caller-owned pids via `run/3`, `start/3`, `start_link/3`; opt-in `CouncilEx.Supervisor` for tenant isolation; no auto-started supervisor (you own the pids).
- **Persistence**: optional `*.Ecto` backends for `Reliability`, `Registry`, `Recorder`, plus `*.Redis` for `Reliability` and `Registry` (Recorder is Ecto-only); `CouncilEx.Config` `:mode` knob (`:single_node` / `:multi_node`) flips all backends in one place.

### Planned

- **Nice-to-have, unscheduled**: chained multi-step tool loops where one tool call feeds the next within a single member turn (gap #11 in [`docs/FUTURE_EXAMPLES.md`](https://github.com/brewingelixir/council_ex/blob/main/docs/FUTURE_EXAMPLES.md)); ranking-parser regex fallback for cheap models (karpathy pattern); `Fairness.parity/2` metric helper (cultural_debate); persona-counterweight presets; LLM-judge / embedding-cluster backends for `BiasDetector`; logical-validity-aware aggregator (Wu 2025); deterministic pre-injection RAG ([`docs/future/RAG_PRE_INJECTION.md`](https://github.com/brewingelixir/council_ex/blob/main/docs/future/RAG_PRE_INJECTION.md)). Tracked in [`docs/RELATED_WORK.md`](docs/RELATED_WORK.md).
- **Out of scope for this repo**: durable run history, durable execution, and a LiveView dashboard. Build them in your host app against the frozen `CouncilEx.Events` PubSub surface and `Diagram.to_ir/1`.

## License

Apache-2.0. See [`LICENSE`](LICENSE).

Built by Humberto Aquino · [Brewing Elixir](https://github.com/brewingelixir) · [@brewingelixir](https://x.com/brewingelixir)

## Acknowledgements

Special thanks to Andrej Karpathy, whose [`karpathy/llm-council`](https://github.com/karpathy/llm-council) sparked the initial idea behind this project. His "models review each other before a final synthesis" experiment is what we set out to bring to Elixir as a reusable framework. See [`docs/TUTORIAL_KARPATHY_COUNCIL.md`](docs/TUTORIAL_KARPATHY_COUNCIL.md) for the Elixir port.

### References

- Wu, S., Li, X., Feng, Y., Li, Y., Wang, Z., & Wang, R. (2026). _Council Mode: A Heterogeneous Multi-Agent Consensus Framework for Reducing LLM Hallucination and Bias._ arXiv:2604.02923. [PDF](https://arxiv.org/pdf/2604.02923). Implemented as `Councils.WeightedConsensus`, per-member confidence (`MemberResult.:confidence`), `BiasDetector` (diagnostic), and `Reliability` store. Full mapping in [`docs/COUNCIL_MODE_PAPER.md`](docs/COUNCIL_MODE_PAPER.md).

For broader context on multi-agent LLM papers and projects (MAD, Adjudicator, karpathy/llm-council, Chaos-MoA-Pipeline, cultural_debate, etc.) and how each maps onto CouncilEx, see [`docs/RELATED_WORK.md`](docs/RELATED_WORK.md). The Wu et al. _Can LLM Agents Really Debate?_ (arXiv:2511.07784) finding on conformity-under-visible-majority motivated `Councils.JuryWithRetry`'s "judges don't see each other across iterations" design.
