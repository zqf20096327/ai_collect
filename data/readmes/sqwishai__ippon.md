<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img alt="ippon, run decision models on your mac" src="assets/banner-light.svg" width="800">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/sqwishai/ippon/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/sqwishai/ippon/actions/workflows/ci.yml/badge.svg"></a>
  <img alt="macOS on Apple silicon" src="https://img.shields.io/badge/macOS-Apple%20silicon-000000?logo=apple&logoColor=white">
  <img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-3776ab?logo=python&logoColor=white">
  <a href="LICENSE"><img alt="Apache-2.0 licence" src="https://img.shields.io/badge/license-Apache--2.0-2a78d6"></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-hero-dark.svg">
    <img alt="On average over every model and workload, time to answer the same requests on the same model builds, and how much faster ippon is. ippon is 34% faster than Ollama, 55% faster than oMLX, 3.4x faster than llama.cpp and 4x faster than the creators' own code" src="docs/assets/readme-hero-light.svg" width="700">
  </picture>
</p>

<p align="center">Every runtime answers the same requests on the same model builds. Each model's chart is under <a href="#speed-">Speed</a>.</p>

**Run decision models on your Mac, blazing fast,** down to **51 ms** text (14 ms on cached context), **39 ms** audio, **179 ms** image, and **828 ms** video on M5 Pro, **4x faster** on average than creators' code and **45% less memory** than Ollama (up to 68% less), with no PyTorch, text generation, or cloud API.

### Try it with your agent

Paste this into Claude Code, Codex, Cursor, OpenCode, Pi or Hermes to install ippon and run **Kettei Core** on your Mac:

```text
Install ippon on my Mac (`curl -fsSL https://sqwish.ai/ippon/install.sh | sh`), then run `ippon pull kettei-core --dry-run`. Show me the licence link and ask before downloading with `ippon setup kettei-core --yes --accept-license` (use `kettei-core:q8` or `kettei-dot` if bf16 does not fit this Mac). Then read `ippon skills ippon`, run a sample `ippon decide` call with Kettei Core using `--server`, and show me the probabilities and warm latency.
```

## Highlights

- Faster than Ollama, oMLX and llama.cpp on the same models ([results](docs/benchmarks.md)).
- Faithful to the creators, because every build is checked against its creator's own code, with the tolerances
  published.
- Multimodal, with text, images, audio and video, each read the way the model's own code reads it.
- Made for agents, with many questions in one read, growing conversations and one model shared by all your agents.
- Our own models, Kettei Core and Kettei Dot, lead the open decision models of their size.
- Plugs in to the [Sqwish Labs SDK](https://docs.sqwish.ai/guides/sdks), the decision APIs of TypeSafe, Perplexity and
  SGLang, Claude Code, Codex, Hermes, OpenCode, Pi and MCP.
- Private and light, because nothing you send leaves your Mac and ippon uses less memory than Ollama and oMLX
  ([memory](#memory)).

<p align="center">
  <img alt="Five runtimes answer the same 41-turn chat with Clef-Flash 9B on a 48 GB M5 Pro, played at 4x and faster once ippon and Ollama finish. ippon answers all 41 turns in 8.1 s, about 140 ms a message, Ollama in 14.2 s, oMLX in 148 s, llama.cpp in 207 s and the creator's code in 559 s, the slower runtimes taking longer with every message" src="docs/assets/agent-loop.gif" width="830">
</p>

<p align="center">41-turn agent loop on Clef-Flash 9B (48 GB M5 Pro, played at 4x then faster once ippon and Ollama finish): <b>8.1 s</b> on ippon, 75% faster than Ollama (14.2 s), 18x faster than oMLX (148 s), 26x faster than llama.cpp (207 s) and 69x faster than the creator's code (559 s).</p>

## Installation

To install ippon, run this command.

```sh
curl -fsSL https://sqwish.ai/ippon/install.sh | sh
```

The installer lists the decision models with whether each fits your Mac, downloads the one you choose and asks it a
first question. In its list, the left and right arrow keys change a model's precision and show whether its answers
hold there. Esc goes back a step. A model under an open licence (Apache-2.0, MIT, BSD, the LFM Open License or the
Fastino Community License) downloads without a question. For any other licence, Kettei's included, ippon shows it
and asks you once ([licences](docs/architecture.md#pulling-and-licences)).

To upgrade, run the installer again. To remove ippon, run `ippon remove all --models`, then
`uv tool uninstall ippon`. The first command takes ippon out of your agents' settings and your login items and
stops its server. It also deletes ippon's settings, its caches, the models it downloaded and the link the installer
made to the ippon command.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-ready-dark.png">
    <img alt="ippon setup opens with Inky, Sqwish's octopus, beside ippon's name, its tagline, its version and this Mac (Apple M5 Pro, 48 GB memory, 37 GB for the GPU), then finds Kettei Core already on this Mac, sees it answer its first question in 38 ms and lists the commands to use it with" src="docs/assets/cli-ready-light.png" width="680">
  </picture>
</p>

<details>
<summary>See the interactive setup picker</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-setup-dark.png">
    <img alt="ippon setup on an M5 Pro with 48 GB lists the decision models with their precision, size, whether they fit this Mac and what they read, Kettei Core first and highlighted, every model at full precision but one at 8 bits, the largest marked tight on this Mac" src="docs/assets/cli-setup-light.png" width="680">
  </picture>
</p>

</details>

To use ippon from Python 3.11 or newer on an Apple-silicon Mac, install `ippon`:

```sh
pip install ippon                # or uv add ippon
ippon setup                      # then choose a model, download it and see it answer
```

To install from source, first install Rust's [cargo](https://rustup.rs).

```sh
pip install git+https://github.com/sqwishai/ippon
```

<details>
<summary>Or let your coding agent install it</summary>

Paste this into Claude Code, Codex, OpenCode or Pi.

```text
Set up ippon on this Mac, the runtime for local decision models at https://github.com/sqwishai/ippon.
1. Install it with: curl -fsSL https://sqwish.ai/ippon/install.sh | sh
2. ippon will download Kettei Core, or Kettei Dot on a Mac where Core does not fit as published, under the Kettei Community Model License 1.0 (https://huggingface.co/Sqwish/Kettei-Core). Show me that licence and ask me to accept it.
   Stop here if I don't.
3. Once I accept, start the setup in the background, because it downloads about 10 GB, which can take 20 minutes
   or more, longer than one shell command waits:
   nohup ippon setup --yes --accept-license --use AGENT --every-session > ~/ippon-setup.log 2>&1 &
   where AGENT is claude, codex, opencode or pi, whichever you are. Check `tail -n 3 ~/ippon-setup.log` every minute and
   tell me how far the download is, until the log shows the first answer. Setup adds ippon's MCP tools and skill to
   your settings for every session, and `ippon remove AGENT` takes them out again.
4. Read ippon's skill with `ippon skills ippon`. Then show me how my own Python code asks the model directly.
   Write ask.py that uses `from ippon import Decider, YesNo` and `Decider.load(MODEL).decide(...)`,
   where MODEL is "kettei-core" or "kettei-dot", whichever `ippon status` names, with one yes/no question about a short
   customer message. Run it with `uv run --with ippon ask.py`, and show me its answer and how sure it was.
5. Tell me to restart you, so the new tools load.
```

</details>

## Quick start

Run one decision directly from the terminal with no file setup:

```sh
ippon decide kettei-core:q8 '{"state":"Charged twice, please refund.","questions":{"refund":{"type":"noul","instructions":"Is the customer asking for a refund?"}}}'
```

To ask several questions in one read, save a `request.json` file and run `ippon decide kettei-core:q8 request.json`:

```json
{
  "state": "I was charged twice. Please refund the second charge today.",
  "questions": {
    "refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"},
    "team": {"type": "choice", "instructions": "Which team should help?", "criteria": {"billing": "Charges and refunds", "technical": "App faults"}},
    "urgency": {"type": "score", "instructions": "How urgent is the request?", "criteria": ["Can wait", "Needs help today", "Cannot continue working"]}
  }
}
```

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-decide-dark.png">
    <img alt="ippon decide kettei-core:q8 request.json: refund yes 99.1%, team billing 98.9%, urgency Needs help today 70.5%, 153 tokens read, and the model's licence" src="docs/assets/cli-decide-light.png" width="680">
  </picture>
</p>

A `noul` question asks yes or no, and its answer is the probability of yes. A `choice` answer gives each option's
probability, and a `score` answer places the message on your scale. Add `--json` to get the whole response. Add
`:q8` after a model's name to run it at 8-bit in about half the memory.

To ask from Python, in your own process, load the model with `ippon.Decider`:

```python
from ippon import Choice, Decider, YesNo

with Decider.load("kettei-core:q8", accept_license=True) as model:
    result = model.decide(
        "I was charged twice. Please refund the second charge today.",
        {
            "refund": YesNo("Is the customer asking for a refund?"),
            "team": Choice("Which team should help?", ["billing", "technical"]),
        },
    )
    print(result["refund"].p_yes, result["team"].top)
```

`accept_license=True` accepts the Kettei Community Model License, which Kettei asks for once before its first
download. Every licence but an open one (Apache-2.0, MIT, BSD, the LFM Open License or the Fastino Community License)
asks the same way: confirm it in the CLI, or pass `accept_license=True` in Python.

To share one model with every app and agent on your Mac, serve it. In a terminal, `ippon serve kettei-core` prints a
line for each answer it sends, and `ippon start` runs the same server in the background.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-serve-dark.png">
    <img alt="ippon serve kettei-core shows Inky, Sqwish's octopus, beside Kettei Core, serving at http://127.0.0.1:8000, ready in 1.5 s, then prints a line for each of four answers to a client named support, with the time, 19 to 37 ms, the tokens read and each question's answer, and on the last line 24 tokens kept from an earlier reading" src="docs/assets/cli-serve-light.png" width="680">
  </picture>
</p>

```sh
curl -sS http://127.0.0.1:8000/v1/systemone -H 'Content-Type: application/json' -d @request.json
```

A client that sends the `X-Ippon-Client` header has its name on each of its lines. When a request repeats a context
that the model read before, its line shows how many tokens ippon kept from that reading.

If another program uses port 8000, `ippon start` serves on a free port and prints its URL, and `ippon status` shows
that URL too. In a terminal, `ippon status` watches live throughput, cache reuse, and per-client traffic.

<details>
<summary>See live server monitoring with <code>ippon status</code></summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-status-dark.png">
    <img alt="ippon status shows Inky beside Kettei Core, loaded in 7.6 GB, and its server watched live, 20 ms per decision, 33.5 questions answered a second, 405 answered, 21.6k tokens read with 14% from earlier requests, then 3 clients connected and a bar for each client's decisions, support 318, billing 72 and triage 15" src="docs/assets/cli-status-light.png" width="680">
  </picture>
</p>

</details>

## Features

### Agents

`ippon claude` opens Claude Code with your decision model ready for that session, and `ippon codex`,
`ippon opencode` and `ippon pi` do the same for Codex, OpenCode and Pi.

```sh
ippon claude              # or ippon codex, ippon opencode, ippon pi
```

<p align="center">
  <img alt="Claude Code runs 8 parallel subagents against one local ippon serve Kettei Core server, sorting 4,278 openai/codex issues and 5,991 comments by type, part of Codex and Windows-only bugs (30,807 questions at 70 ms median and 73% cache reuse) while ippon status shows live throughput and a bar for each subagent, then Claude Code ends on a table of the results" src="docs/assets/claude-demo.gif" width="830">
</p>

<p align="center">Claude Code spinning up 8 subagents on one local Kettei Core server, sorting 4,278 issues and 5,991 comments (30,807 questions, 70 ms median, 73% cache reuse) on a single Mac.</p>

To keep it in every session, add ippon's MCP server.

```sh
claude mcp add --transport stdio ippon -- ippon mcp kettei-core:q8
```

On Kettei Dot, `ippon serve` answers the Quick start request a second time in 0.5 ms instead of 15 ms, because it
keeps its answers by default. It returns the answer the model gave the first time, which is safe because a decision model
does not sample. Agents send the same request many times, so the saving adds up. To turn the answer cache off, use
`--answer-cache 0`.

`ippon skills` teaches your agent when a decision model is worth asking, and [Agents](docs/agents.md) covers Cursor,
Hermes and other hosts.

### Multimodal

Add an image, an audio clip or a video to a request and ask about it as you would about text. ippon
prepares each input just as the model's own code does. [examples/multimodal.py](examples/multimodal.py) asks
Liquid's d1-2B about a photo, a document image and a short video by file path. Most models read media ahead of the text,
as their creators' code does, and elephant-1 and Torchcast read each where its `<image:N>` tag sits. From the command
line, `ippon decide MODEL request.json --image photo.jpg` (or `--video`, `--audio`) adds files to a request; MCP tools
accept local file paths directly too.

```python
from ippon import Choice, Decider

with Decider.load("d1-2b:bf16") as model:
    result = model.decide(
        "The clip.",
        {"what": Choice("What happens in the video?", ["a ball rolls", "nothing moves"])},
        videos=["clip.mp4"],
    )
```

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-media-dark.png">
    <img alt="A photo of the Wright brothers' first flight, page 1 of the US Constitution and a 3-second clip of a rolling ball, with d1-2B's answers, an aircraft 99.8%, a law or charter 93.6%, a ball rolls 98.7%" src="docs/assets/cli-media-light.png" width="680">
  </picture>
</p>

### SDKs and HTTP

In your own Python process, `ippon.Decider` runs any model directly via `.decide()`, `.systemone()`, or `.sqwish()`.
From another process, language, or the [Sqwish Labs SDK](https://docs.sqwish.ai/guides/sdks), `ippon serve` answers the
same decide API over HTTP at `POST /v1/decide`.

```sh
ippon serve kettei-core:q8 --port 8000
curl -s http://127.0.0.1:8000/v1/decide -H 'Content-Type: application/json' -d '{
  "context": "I was charged twice and the app crashes when I open my invoices.",
  "decisions": [{"id": "refund", "question": "Should this customer get a refund?", "kind": "binary"}]
}'
```

Kettei Core and Dot read the prompts the SDK writes token for token, and every other model ippon runs answers the same
request. ippon also serves these other decision APIs.

- [TypeSafe's System One](https://docs.typesafe.ai/api/system-one) at `POST /v1/systemone`, which TypeSafe's
  [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) sends. The SDK adds `/v1/systemone` itself, so
  give it the server's address with no `/v1` (`base_url="http://127.0.0.1:8000"`).
- [Perplexity's Decisions API](https://docs.perplexity.ai/docs/decisions/quickstart) and
  [SGLang](https://docs.sglang.io/docs/supported-models/decision_models) at `POST /v1/decisions`.

### Answers you can trust

ippon checks every model it supports against its creator's own code. It runs a fixed set of requests and compares
each probability with the creator's, within a tolerance published for each model. A near tie can change the top
answer and still pass. Two probabilities inside the tolerance can also fall on opposite sides of your app's cutoff,
for example when it blocks a command at 85%.

Before you rely on a cutoff, see how closely each build matches the creator's probabilities in
[Accuracy](docs/accuracy.md). Then test your threshold on your own examples. `ippon verify MODEL` repeats the
creator check on your Mac. `ippon eval examples.jsonl --model MODEL` scores the model on your labelled examples. It then picks a
threshold for each yes/no question and checks it on examples held out from that choice. If a build is past its
tolerance, [Models](docs/models.md) marks it and gives the reason.

## Models

ippon supports the decision models that are practical on a Mac, from creators who publish their weights and
reference code. Kettei Core and Kettei Dot sit first, and each section orders the rest by public benchmark score
per gigabyte of memory (highest value per GB first; models without a public board score sit at the end). Each name
downloads the build that `ippon pull --list` marks with a star. Add `:q8` after any name to run it at 8-bit
(`kettei-core:q8`). If the creator publishes a verified 8-bit build, `:q8` takes that build (`d1-2b:q8` is Liquid's
own Q8_0 file). If you already have a model, give its folder, its GGUF file or `ollama://TAG` in place of the name.

**Text**

| Model | Creator | Size | Pull | Weights | Licence |
|---|---|---:|---|---:|---|
| [Kettei Core](https://huggingface.co/Sqwish/Kettei-Core) | Sqwish Labs | 3.7B | `kettei-core` | 10.1 GB (7.6 GB resident) | Kettei Community Model License 1.0 |
| [Kettei Dot](https://huggingface.co/Sqwish/Kettei-Dot) | Sqwish Labs | 0.9B | `kettei-dot` | 2.2 GB (1.8 GB resident) | Kettei Community Model License 1.0 |
| [GLiDE 2B](https://huggingface.co/fastino/GLiDE-2B) | Fastino | 2B | `glide-2b` | 3.8 GB | Fastino Community License |
| [Strands-Decider-E2B](https://huggingface.co/StrandsAgents/strands-decider-E2B-gemma4-v2-2611) | StrandsAgents | 2B active | `strands-e2b` | 10.3 GB (3.8 GB resident) | Apache-2.0 |
| [Kev 0.8B](https://huggingface.co/jaredpalmer/kev-0.8b) | Jared Palmer | 0.8B | `kev-0.8b` | 1.8 GB with its base | Apache-2.0 |
| [Strands-Decider-E4B](https://huggingface.co/StrandsAgents/strands-decider-E4B-gemma4-v2-2611) | StrandsAgents | 4B active | `strands-e4b` | 16.0 GB (8.0 GB resident) | Apache-2.0 |
| [Jeff-1.1-Qwen-4B](https://huggingface.co/jgeuter/Jeff-1.1-Qwen-4B) | Jonathan Geuter | 4B | `jeff-qwen-4b` | 9.1 GB | CC BY-NC 4.0 |
| [GLiDE 9B](https://huggingface.co/fastino/GLiDE-9B) | Fastino | 9B | `glide-9b` | 15.9 GB | Fastino Community License |
| [Kev 4B](https://huggingface.co/jaredpalmer/kev-4b) | Jared Palmer | 4B | `kev-4b` | 9.5 GB with its base | Apache-2.0 |
| [Strands-Decider-12B](https://huggingface.co/StrandsAgents/strands-decider-12B-gemma4-v2-2611) | StrandsAgents | 12B | `strands-12b` | 23.9 GB (21.8 GB resident) | Apache-2.0 |
| [Jeff-1.1-Medium](https://huggingface.co/jgeuter/Jeff-1.1-Medium) | Jonathan Geuter | 12B | `jeff` | 25.4 GB | CC BY-NC 4.0 |
| [Kev 9B](https://huggingface.co/jaredpalmer/kev-9b) | Jared Palmer | 9B | `kev-9b` | 19.5 GB with its base | Apache-2.0 |
| [AutoTrust-Decider-Mini-9B](https://huggingface.co/autotrust/AutoTrust-Decider-Mini-9B) | AutoTrust | 9B | `autotrust-mini-9b` | 18.1 GB | Apache-2.0 |

**Text and images**

| Model | Creator | Size | Pull | Weights | Licence |
|---|---|---:|---|---:|---|
| [H2O-Lightning-4B](https://huggingface.co/h2oai/h2o-lightning-4b) | H2O.ai | 4B | `h2o` | 9.3 GB | Apache-2.0 |
| [pplx-decider flash v1.3](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.3) | Perplexity | 4B | `pplx-flash` | 9.1 GB | Apache-2.0 |
| [Torchcast Decision 4B](https://huggingface.co/torchcast-ai/torchcast-decision-4b) | Torchcast AI | 4B | `torchcast` | 10.4 GB | Apache-2.0 |
| [Clef-Flash 9B](https://huggingface.co/Cloudflare/clef-flash) | Cloudflare | 9B | `clef-flash` | 10.7 GB, MLX 8-bit | Apache-2.0 |
| [elephant-1](https://huggingface.co/baselabs/elephant-1) | Base Labs | 9B | `elephant` | 18.8 GB | MIT |

**Text, images and video**

| Model | Creator | Size | Pull | Weights | Licence |
|---|---|---:|---|---:|---|
| [d1-2B](https://huggingface.co/LiquidAI/d1-2B) | Liquid AI | 2B | `d1-2b` | 3.8 GB | LFM Open License v1.0 |
| [d3-mini](https://huggingface.co/vllm-sr/d3-mini) | vllm-sr | 4B | `d3-mini` | 9.1 GB | Apache-2.0 |
| [d3-flash](https://huggingface.co/vllm-sr/d3-flash) | vllm-sr | 9B | `d3-flash` | 16.8 GB | Apache-2.0 |

**Text, images, video and audio**

| Model | Creator | Size | Pull | Weights | Licence |
|---|---|---:|---|---:|---|
| [d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) | Liquid AI | 2B | `d1-omni-2b` | 4.3 GB | LFM Open License v1.0 |

`d1-2b:q8` pulls Liquid's own [Q8_0 file](https://huggingface.co/LiquidAI/d1-2B-GGUF) instead. It is 2.0 GB with
its image encoder, which reads images and video too, a little further from Liquid's answers than the full model
([accuracy](docs/accuracy.md)). ippon runs models at full precision or 8-bit unless you ask
for fewer bits. If you do, it warns how far the model drifts from its creator's answers
([formats](docs/formats.md)). Weights keep their creators' licences, and Jeff's do not allow commercial use.
[Models](docs/models.md) lists every build and what was checked of it.

Our largest models, Kettei Chub and Kettei Fat, run on [console.sqwish.ai](https://console.sqwish.ai), where Kettei
Fat leads every listed decision model on the public Decision Index and JevBench. There you can also fine-tune Kettei
on your own labelled data and call it through the [Sqwish Labs SDK](https://docs.sqwish.ai/guides/sdks) or the OneHot API.

## Speed ⚡

Each model has one chart, in the section for the inputs it was timed on. Open a model to see ippon beside every
runtime that runs the same build, each in its own server and answering the same requests. Beside each model's
name is ippon's time for a typical call, about 500 tokens with 3 questions, and how much faster that is than the
model's other runtimes.
[Benchmarks](docs/benchmarks.md) has the method and the raw results.

### Text only

Per-model timings for typical calls, repeated contexts, growing agent conversations (see the 41-turn recording under
[Highlights](#highlights)), and 16 concurrent clients.

<!-- text charts: benchmarks/kit/summarize.py --readme -->

| Model | Typical call | Same context again | Context grown | 16 clients at once |
|---|---:|---:|---:|---:|
| Kettei Core | 183 ms | 44 ms | 48 ms | 12.0 req/s |
| Kettei Dot | 51 ms | 14 ms | 16 ms | 46.4 req/s |

<details>
<summary><b>Jeff-1.1-Medium</b> ~1,615 ms, 69% faster than Jonathan Geuter's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-jeff-1-1-medium-dark.svg">
  <img alt="Jeff-1.1-Medium: ippon beside Jonathan Geuter's server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-jeff-1-1-medium-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>elephant-1</b> ~412 ms, 5x faster than Base Labs' runtime</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-elephant-1-dark.svg">
  <img alt="elephant-1: ippon beside Base Labs' runtime on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-elephant-1-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>Clef-Flash 9B</b> ~437 ms, up to 2x faster than Cloudflare's code, Ollama, llama.cpp and oMLX</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-clef-flash-9b-dark.svg">
  <img alt="Clef-Flash 9B: ippon beside Cloudflare's code, Ollama, llama.cpp and oMLX on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-clef-flash-9b-light.svg" width="830">
</picture>

With 16 clients at once, llama.cpp's median wait is lower than ippon's, at 759 ms against 3,986 ms. It answers some clients at once and makes others wait, so its 90th-percentile wait is 33,003 ms against ippon's 4,192 ms. It answers 2.64 requests per second, and ippon answers 4.00.

</details>

<details>
<summary><b>GLiDE 9B</b> ~1,255 ms, 4.8x faster than Fastino's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-glide-9b-dark.svg">
  <img alt="GLiDE 9B: ippon beside Fastino's server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-glide-9b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>GLiDE 2B</b> ~199 ms, 7x faster than Fastino's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-glide-2b-dark.svg">
  <img alt="GLiDE 2B: ippon beside Fastino's server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-glide-2b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>Jeff-1.1-Qwen-4B</b> ~549 ms, 7.4x faster than Jonathan Geuter's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-jeff-1-1-qwen-4b-dark.svg">
  <img alt="Jeff-1.1-Qwen-4B: ippon beside Jonathan Geuter's server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-jeff-1-1-qwen-4b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>Kev-9B</b> ~322 ms, 52% faster than Jared Palmer's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-kev-9b-dark.svg">
  <img alt="Kev-9B: ippon beside Jared Palmer's server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-kev-9b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>Kev-4B</b> ~187 ms, 44% faster than Jared Palmer's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-kev-4b-dark.svg">
  <img alt="Kev-4B: ippon beside Jared Palmer's server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-kev-4b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>Strands-Decider-12B</b> ~677 ms, 34% faster than AWS Strands' server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-strands-decider-12b-dark.svg">
  <img alt="Strands-Decider-12B: ippon beside AWS Strands' server on the same builds, for typical call, same context again and 16 clients at once" src="docs/assets/readme-strands-decider-12b-light.svg" width="830">
</picture>

On the 48 GB Apple M5 Pro, with a growing context, AWS Strands' server returned errors on 2 of its 20 requests, while ippon answered every request.

</details>

<details>
<summary><b>Strands-Decider-E4B</b> ~191 ms, 2x faster than AWS Strands' server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-strands-decider-e4b-dark.svg">
  <img alt="Strands-Decider-E4B: ippon beside AWS Strands' server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-strands-decider-e4b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>Strands-Decider-E2B</b> ~75 ms, 2.9x faster than AWS Strands' server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-strands-decider-e2b-dark.svg">
  <img alt="Strands-Decider-E2B: ippon beside AWS Strands' server on the same builds, for typical call, same context again, context grown and 16 clients at once" src="docs/assets/readme-strands-decider-e2b-light.svg" width="830">
</picture>

</details>
<!-- /text charts -->

### Both text and images

When a request sends the images of the request before it plus one more, ippon reads only the new image. On a 4B
vision decision model, each request stays near 450 ms however many images came before. On the same file, llama.cpp
reads every image again, takes 5 s by the eighth image and refuses a ninth
([the round](benchmarks/results/m5pro-2026-11-17-pictures)).

A model that reads images both ways, such as d1-2B or d1-Omni-2B, must read the earlier images again, but ippon still
keeps the encoding of each image. With 8 images, the model answers in 820 to 910 ms on ippon. Ollama takes 1.5 s on
its own MLX build, and llama.cpp takes 2.1 s on the same Q8_0 file. On d3-mini, oMLX takes 3.6 s and ippon takes
2.2 s on the same checkpoint. From the sixth image, Ollama's d3 runner stopped instead of answering or refusing the
request ([the round](benchmarks/results/m5pro-2026-11-18-pictures),
[oMLX's](benchmarks/results/m5pro-2026-11-18-pictures-omlx)).

<!-- text-images charts: benchmarks/kit/summarize.py --readme -->
<details>
<summary><b>Torchcast Decision 4B</b> ~488 ms, 2.9x faster than Torchcast's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-torchcast-decision-4b-dark.svg">
  <img alt="Torchcast Decision 4B: ippon beside Torchcast's server on the same builds, for typical call, same context again, context grown, 16 clients at once, an image and same image again" src="docs/assets/readme-torchcast-decision-4b-light.svg" width="830">
</picture>

</details>

<details>
<summary><b>pplx-decider flash v1.3</b> ~507 ms, 7.6x faster than Perplexity's package</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-pplx-decider-flash-v1-3-dark.svg">
  <img alt="pplx-decider flash v1.3: ippon beside Perplexity's package on the same builds, for typical call, same context again, context grown, an image, growing images and same image again" src="docs/assets/readme-pplx-decider-flash-v1-3-light.svg" width="830">
</picture>

These timings use the full BF16 checkpoint. Perplexity publishes no GGUF or MLX build of flash v1.3, so its own package is the other runtime.

</details>

<details>
<summary><b>H2O-Lightning-4B</b> ~229 ms, 89% faster than llama.cpp</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-h2o-lightning-4b-dark.svg">
  <img alt="H2O-Lightning-4B: ippon beside llama.cpp on the same builds, for typical call, same context again, context grown, 16 clients at once, an image, growing images and same image again" src="docs/assets/readme-h2o-lightning-4b-light.svg" width="830">
</picture>

</details>
<!-- /text-images charts -->

### Text, images and video

Each model is timed beside its creator's own code and every other runtime that reads its video, with 3 questions
about a new 4-second 720p clip ([the round](benchmarks/results/m5pro-2026-11-18-video),
[oMLX and llama.cpp](benchmarks/results/m5pro-2026-11-19-video-rivals)). oMLX reads video for d3, llama.cpp reads it
for d1, and Ollama refuses video for every decision model.

<!-- text-images-video charts: benchmarks/kit/summarize.py --readme -->
<details>
<summary><b>d3-mini</b> ~513 ms, up to 7.6x faster than Ollama, oMLX and vllm-sr's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-d3-mini-dark.svg">
  <img alt="d3-mini: ippon beside Ollama, oMLX and vllm-sr's server on the same builds, for typical call, same context again, context grown, 16 clients at once, an image, a video, growing images, same image again and same video again" src="docs/assets/readme-d3-mini-light.svg" width="830">
</picture>

On the 48 GB Apple M5 Pro, with growing images, Ollama returned errors on 5 of its 7 requests, while ippon answered every request.

</details>

<details>
<summary><b>d3-flash</b> ~920 ms, up to 4.8x faster than Ollama, oMLX and vllm-sr's server</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-d3-flash-dark.svg">
  <img alt="d3-flash: ippon beside Ollama, oMLX and vllm-sr's server on the same builds, for typical call, same context again, context grown, 16 clients at once, an image, a video, growing images, same image again and same video again" src="docs/assets/readme-d3-flash-light.svg" width="830">
</picture>

On the 48 GB Apple M5 Pro, with growing images, Ollama returned errors on 6 of its 8 requests, while ippon answered every request.

</details>

<details>
<summary><b>d1-2B</b> ~67 ms, up to 4.3x faster than Liquid's code, Ollama and llama.cpp</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-d1-2b-dark.svg">
  <img alt="d1-2B: ippon beside Liquid's code, Ollama and llama.cpp on the same builds, for typical call, same context again, context grown, 16 clients at once, an image, a video, growing images, same image again and same video again" src="docs/assets/readme-d1-2b-light.svg" width="830">
</picture>

With 16 clients at once, llama.cpp's median wait is lower than ippon's, at 121 ms against 515 ms. It answers some clients at once and makes others wait, so its 90th-percentile wait is 5,278 ms against ippon's 518 ms. It answers 16.5 requests per second, and ippon answers 31.0.

</details>
<!-- /text-images-video charts -->

### Text, images, video and audio

A question about 10 seconds of audio takes d1-Omni-2B 39 ms on ippon. It takes 70 ms in Liquid's code on the same
checkpoint and 76 ms on llama.cpp with the same Q8_0 file.

<!-- text-images-video-audio charts: benchmarks/kit/summarize.py --readme -->
<details>
<summary><b>d1-Omni-2B</b> ~67 ms, up to 4.4x faster than Liquid's code, Ollama and llama.cpp</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-d1-omni-2b-dark.svg">
  <img alt="d1-Omni-2B: ippon beside Liquid's code, Ollama and llama.cpp on the same builds, for typical call, same context again, context grown, 16 clients at once, an image, a video, an audio clip, growing images, same image again and same video again" src="docs/assets/readme-d1-omni-2b-light.svg" width="830">
</picture>

With 16 clients at once, llama.cpp's median wait is lower than ippon's, at 122 ms against 513 ms. It answers some clients at once and makes others wait, so its 90th-percentile wait is 5,286 ms against ippon's 517 ms. It answers 16.5 requests per second, and ippon answers 31.2.

</details>
<!-- /text-images-video-audio charts -->

## Memory

A decision model runs beside your agent, its editor and a browser full of tabs. On the same builds, Ollama needs 80%
more memory than ippon at its peak while answering. oMLX, which runs the same MLX checkpoints as ippon, needs 10% more.
ippon's peak includes the contexts it keeps to answer the next call sooner.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-memory-dark.svg">
  <img alt="On average, the most memory used while answering, relative to ippon on the same builds. Ollama needs 80% more" src="docs/assets/readme-memory-light.svg" width="830">
</picture>

Ollama's bar averages its highest memory on each build it shares with ippon, over the typical, repeat, grow,
16-client and image-again workloads ([details](docs/benchmarks.md#memory-beside-other-runtimes)).

## Getting help

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cli-help-dark.png">
    <img alt="ippon --help lists every command with one line on what it does, and 3 to start with, ippon setup, ippon claude and ippon start" src="docs/assets/cli-help-light.png" width="760">
  </picture>
</p>

- `ippon --help` lists the main commands, and `ippon COMMAND --help` explains one and ends with examples.
- `ippon doctor` checks your Mac's setup and says what stands between it and full speed.
- `ippon skills` teaches your agent to use ippon.
- To report a bug or ask for a model, [open an issue](https://github.com/sqwishai/ippon/issues/new/choose).
- Report security problems as [SECURITY.md](SECURITY.md) describes, never in a public issue.

## Documentation

- [Choosing and evaluating](docs/evaluating.md) - pick a model and measure it on your own examples.
- [Models](docs/models.md) - every build, what it reads and what was checked of it.
- [Agents](docs/agents.md) - MCP, the shared server and the errors an agent can get.
- [Accuracy](docs/accuracy.md) - the references, the tolerances and every result.
- [Benchmarks](docs/benchmarks.md) - how each timing was taken, with the raw results.
- [Architecture](docs/architecture.md) - the command line, HTTP and Python reference, and how a request runs.
- [Kernels](docs/kernels.md) and [Packed formats](docs/formats.md) - what runs on your Mac's GPU, and the files it reads.
- [Bring your own](docs/bring-your-own.md) and [Adding a model](docs/adding-a-model.md) - run another model.
- [Errors](docs/errors.md) - exit codes, HTTP statuses and what to retry.
- [Contributing](CONTRIBUTING.md) - prepare, check and measure a change.

ippon is licensed under [Apache-2.0](LICENSE). See [NOTICE](NOTICE) for attribution and [SECURITY.md](SECURITY.md) to report a
vulnerability. Model weights keep their creators' licences and are downloaded separately.

<br>

<p align="center">
  <a href="https://sqwish.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/sqwish-labs-dark.png">
      <img alt="Made by Sqwish Labs" src="assets/sqwish-labs-light.png" width="212">
    </picture>
  </a>
</p>
