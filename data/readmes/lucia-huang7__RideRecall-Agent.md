# RideRecall-Agent

[![Verify](https://github.com/lucia-huang7/RideRecall-Agent/actions/workflows/verify.yml/badge.svg)](https://github.com/lucia-huang7/RideRecall-Agent/actions/workflows/verify.yml)

A stateful ride-support agent with durable memory, versioned claims and evidence-grounded replies. Python · FastAPI · Vue · SQLite · Chroma · MCP · Ollama.

[![01 Choose the charged trip; 02 Correct the account; 03 Inspect policy evidence](docs/assets/story-row-1.jpg)](docs/assets/story-row-1.jpg)

[![04 Hand off the whole case; 05 Confirm the adjustment; 06 Close the loop](docs/assets/story-row-2.jpg)](docs/assets/story-row-2.jpg)

Click either row to enlarge it. [All 25 screens](docs/interface.md).

## Architecture

[![Request processing, policy and trip lookups, case storage and adjustment confirmation](docs/assets/architecture.png)](docs/assets/architecture.svg)

- **Durable memory:** restores conversations and claim revisions while keeping rider statements separate from trip facts.
- **Evidence-grounded analysis:** policy RAG and read-only MCP supply evidence; local Qwen3 produces structured corrections and response plans.
- **Guarded case actions:** specialist handoff, explicit rider confirmation, revision checks and atomic SQLite writes with a Chroma outbox.

## Evaluation

Local Qwen3 4B · full API, memory, Chroma and MCP pipeline · 100 synthetic dialogues:

| Metric | Result |
| --- | ---: |
| Behavioral contract checks (`behavior-v2`) | 100/100 dialogues |
| Context retention | 644/644 checkpoints |
| Reply-source audit | 682/682 analyses |
| Analysis latency, P50 / P95 | 11.19 / 13.82 s |

In the frozen deterministic comparison across 2,000 dialogues, durable memory achieved **100% workflow completion vs. 67%** with four recent rider rounds. [Benchmark](datasets/ride_support/baseline.json) · [Protocols and results](docs/operations.md#local-model-validation-results).

## Run locally

Requires Python 3.11/3.12 and Node.js compatible with Vite 7. The default demo runs without an API key; local inference uses Ollama.

```bash
git clone https://github.com/lucia-huang7/RideRecall-Agent.git
cd RideRecall-Agent
bash scripts/dev/one-click.sh start --no-open
```

Open [Trips](http://127.0.0.1:5175/#/trips), or double-click [Start RideRecall-Agent.command](scripts/macos/Start%20RideRecall-Agent.command) on macOS. [Setup, tests and model configuration](docs/operations.md).

[Java backend reference](https://github.com/lucia-huang7/RideRecall-Agent/tree/reference/java-backend): Java 21, Spring Boot and LangChain4j.

Trips, policies and adjustments are simulated; evaluation scope and deployment requirements are documented in [Operations](docs/operations.md).

## License

[MIT](LICENSE).
