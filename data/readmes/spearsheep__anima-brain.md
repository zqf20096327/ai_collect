<p align="center">
  <a href="https://www.anima-lab.io"><img src="docs/assets/anima-icon.png" alt="Anima Lab" width="104"></a>
</p>

<h1 align="center">Anima Brain</h1>
<p align="center">
  <strong>English</strong> &nbsp; | &nbsp; <a href="README.zh-CN.md" lang="zh-CN">简体中文</a>
</p>
<p align="center"><strong>Memory and emotional continuity for AI companions.</strong></p>
<p align="center">
  Python 3.11+ &nbsp; · &nbsp; Alpha 0.6.0 &nbsp; · &nbsp; MIT-licensed code
</p>
<p align="center">
  <a href="#see-it-in-action">Demos</a> &nbsp; / &nbsp;
  <a href="#quickstart">Quickstart</a> &nbsp; / &nbsp;
  <a href="#python-sdk">SDK</a> &nbsp; / &nbsp;
  <a href="#connect-your-agent">Agent integrations</a> &nbsp; / &nbsp;
  <a href="docs/README.md">Docs</a> &nbsp; / &nbsp;
  <a href="#try-anima">Try Anima</a>
</p>

A developer toolkit for building agents with **persistent memory, character identity
and emotional continuity**. Use it from Python, plug it into an existing agent through
MCP, or connect your own frontend. Bring your own model. An optional
[Companion Studio web example](examples/showcase/README.md) lets you explore the SDK interactively.

The public project is **Anima Brain**. The Python distribution remains `companion-engine`,
imports use `companion_engine`, and the CLI is `companion`, preserving existing integrations.

This project adapts the memory and brain architecture behind [Anima Lab](https://www.anima-lab.io)
into a standalone Python implementation. It carries over selected designs and logic,
with local storage, configurable providers and developer-facing APIs. **It is a separate
adaptation with different defaults and capability coverage, not the complete Anima app
backend or a promise of identical behavior.** See [what was adapted](docs/architecture.md#source-provenance-and-non-parity).

## What it gives your agent

| Capability | In this SDK |
| --- | --- |
| **Grounded memory** | Original messages, source-backed facts, corrections, contextual notes and linked evidence. |
| **Retrieval and continuity** | Local lexical search, optional embeddings, bounded follow-up lookup, cited core and episode summaries. |
| **Character and response guidance** | Persona, expression preferences, emotional-attunement records and optional fictional relationship state. |
| **Multimodal operations** | Vision observations, image generation and reference edits, speech and transcription through separately configured providers. |
| **Live calls** | Streaming Doubao ASR + the same brain + character speech; optional Vidu S2 animated video over managed RTC. |
| **Application control** | Typed results, memory review, context budgets, usage receipts and request replay. |

The engine runs locally with SQLite + FTS5. It requires no Anima account or Convex
backend. The **Python package stays headless**. The optional
[web showcase](examples/showcase/README.md) is a separate React application in `examples/showcase/`,
with character chat, memory editing and context inspection. Optional MCP cards expose
memory controls and voice playback inside compatible hosts.

## See it in action

Three short English demos from the local showcase and Python SDK. **Click a preview to watch with sound.**

| Voice messages · 6.5s | Live audio call · 5.9s | Animated video call · 6.6s |
| --- | --- | --- |
| [![Play the English SDK voice sample](docs/assets/demos/voice-message.jpg)](https://spearsheep.github.io/anima-brain-demos/#voice-message) | [![Play the English voice-call demo](docs/assets/demos/audio-call.jpg)](https://spearsheep.github.io/anima-brain-demos/#audio-call) | [![Play the English animated video-call demo](docs/assets/demos/video-call.jpg)](https://spearsheep.github.io/anima-brain-demos/#video-call) |
| Character speech generated through the SDK | Spoken input → brain → character speech | S2 avatar and speech captured together over RTC |

[Watch all three](https://spearsheep.github.io/anima-brain-demos/) · [Download the 4K clips](https://github.com/spearsheep/anima-brain/releases/tag/demo-media-2026-11) · [Recording details and setup](docs/demos.md)

These use configured external providers. The voice-call UI was re-recorded around the
actual call response; the video-call audio and picture come from the same RTC capture.
The 4K presentation contains the provider's native-resolution avatar stream.

## Quickstart

With Python 3.11+ and SQLite FTS5, clone the repository and run the offline example:

```bash
git clone https://github.com/spearsheep/anima-brain.git
cd anima-brain
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python examples/offline_demo.py
```

The offline example uses synthetic data and makes no model calls. To chat with a real
provider, configure a Chat Completions-compatible model supporting JSON-object output:

```bash
export COMPANION_BASE_URL='https://your-provider.example/v1'
export COMPANION_MODEL='your-model-id'
# Bash: enter the key without putting its value in shell history.
read -s -p 'API key: ' COMPANION_API_KEY
export COMPANION_API_KEY
python examples/chat.py
```

Provider calls use your account. No provider or model is selected implicitly.
The terminal example retrieves memory without extra planning calls by default;
`python examples/chat.py --help` lists optional lookup, history and memory controls.

## Optional web showcase

[![Companion Studio: Anima-style local companion interface](docs/assets/companion-studio.png)](examples/showcase/README.md)

A responsive local studio with Anima’s paper-and-ink design, character portraits and
subtle motion. It uses the real engine for chat, memory, review and source inspection.

```bash
python -m pip install -e '.[http,calls]'
npm ci --prefix examples/showcase
npm run build --prefix examples/showcase
python examples/showcase/serve.py --open
```

Configure your model in the studio, or add `--demo` for a clearly labeled offline preview.
See [setup, capabilities and storage](examples/showcase/README.md). This is a local,
single-owner example with [live voice and animated video calls](docs/live-calls.md).
Public multi-user hosting requires your own authentication and deployment layer.

## Inside the brain

[![Original evidence, semantic and episodic memory, consolidation, retrieval and emotional continuity](docs/assets/brain-flow.svg)](docs/assets/brain-flow.svg)

[Open the full-size SVG](docs/assets/brain-flow.svg) · [Animated walkthrough](docs/assets/brain-flow.gif) · **[Explore the Brain Atlas](docs/brain-flow.md)**:
semantic vs episodic memory, the cited consolidation cycle, retrieval formulas and
emotional continuity. Four animated views follow the implemented Python paths.
Start the showcase and open [`?view=architecture`](http://127.0.0.1:8787/?view=architecture)
to play or step through them, adjust recency/importance inputs, and explore PAD vs tension
decay. RRF relevance and time-aware follow-up priority are shown separately. The page
supports reduced motion, makes no model calls and reads no private conversations.
Use **English / 简体中文** in the atlas header to switch languages. The
[Chinese README](README.zh-CN.md#这套大脑怎么工作) includes a localized SVG and animation.
The README uses a larger-type vector layout for readability; the atlas shares the same node
labels and mechanisms, with its own interactive layout.

Live calls use this same path. The SDK exposes `brain.call(character_id, CallOptions(...))`
with streaming audio, transcripts, interrupt/mute controls and saved delivery receipts.
See [provider setup, SDK example and lifecycle](docs/live-calls.md).

## Python SDK

With your provider configured:

```python
import asyncio
from companion_engine import CompanionBrain, Settings

async def main():
    async with CompanionBrain(
        storage="./output/brain.sqlite3",
        user_id="alice",
        settings=Settings.from_env(),
    ) as brain:
        if not any(c.id == "mika" for c in brain.characters()):
            brain.create_character(
                character_id="mika",
                name="Mika",
                persona="Direct, playful, caring without empty reassurance.",
            )

        reply = await brain.chat(
            "mika", "Please remember I prefer tea.", request_id="message-1",
        )
        print(reply.text)
        print(reply.memory_ids)

asyncio.run(main())
```

Reopen the same database and user ID to continue. Use a stable request ID for retries
and a new ID for each new message. Synchronous applications can use `chat_sync()`.

`Settings` selects providers and model limits. `BrainConfig` controls memory retrieval,
recent history, context budgets and response instructions. Character settings control
memory writes and relationship behavior. Creating a character makes no model or
image-generation call. New SDK characters enable provider-configured indexing, reconciliation
and summaries; explicit existing off policies stay off. These jobs use additional model calls.
See [memory architecture and defaults](docs/memory-parity.md).

→ [SDK guide](docs/sdk.md) · [Memory, vision and media arguments](docs/sdk-capabilities.md)

## How it works

```text
Your app or agent host
        │
        ▼
  Prepare context ─── character + recent conversation + retrieved evidence
        │
        ▼
  Generate reply ──── SDK calls your model, or the MCP host writes the reply
        │
        ▼
  Validate & commit ─ original messages + grounded proposals + optional state
        │
        ▼
  Local SQLite ────── available to the next conversation
```

Memory writes can be automatic, reviewed or off. Disabling fact writes still stores
conversation history; reading, writing and retention are separate concerns.
Quote validation checks provenance, not the truth of every model interpretation.

The Python adaptation shares Anima's emphasis on memory and continuity. It includes
optional voice-call and animated-video adapters, but does not include Anima's full
consumer application, hosted infrastructure, billing or autonomous outreach.
[Architecture and implementation boundaries](docs/architecture.md).

## Connect your agent

For Claude Code, Claude Desktop and DeepSeek Harness:

```bash
python -m pip install -e '.[mcp]'
companion --db ./output/host/brain.sqlite3 host-package ./output/hosts
```

Follow the generated `START-HERE.md`. It contains paths for your checkout, so generate
it on the machine where the engine will run. The host uses its own reply model.

MCP makes tools available; the host must call them to retrieve context and save turns.
It does not automatically capture every conversation. See
[host integrations](docs/host-integrations.md) and [connection modes, including ChatGPT](docs/connections.md).

For programmatic loopback HTTP/MCP, install `.[http]` and run `companion http`.
A separate `companion settings` command opens only a private provider-configuration
form when needed. Neither starts a chat application.

## Try Anima

Want a ready-to-use companion instead of building an integration? Use **Anima Lab**:

**[Website & web app](https://www.anima-lab.io) · [iPhone / iPad](https://apps.apple.com/app/id6776954266) · [Android download](https://www.anima-lab.io/download)**

<p align="center">
  <a href="https://www.anima-lab.io"><img src="docs/assets/rina.jpg" alt="Rina, an Anima Lab companion, at an aquarium" height="240"></a>
  &nbsp;
  <a href="https://www.anima-lab.io"><img src="docs/assets/sean.jpg" alt="Sean, an Anima Lab companion" height="240"></a>
</p>

*Rina and Sean from Anima Lab's public website. These images show the consumer product's
characters, not preinstalled SDK characters or features. Android is distributed as a
direct APK through the official download page.*

## Documentation

| Start here | For |
| --- | --- |
| [SDK guide](docs/sdk.md) | Chat, configuration, memory review and recovery |
| [SDK capabilities](docs/sdk-capabilities.md) | Memory limits, vision, images, speech and transcription |
| [Host integrations](docs/host-integrations.md) | Claude and DeepSeek Harness setup |
| [Feature reference](docs/features.md) | MCP tools, CLI and lower-level APIs |
| [Architecture](docs/architecture.md) | Anima adaptation, retrieval, persistence and limits |
| [Memory maintenance](docs/memory-automation.md) | Optional indexing and summary work |
| [Contributing](CONTRIBUTING.md) | Development, testing and release checks |

[Full documentation index](docs/README.md) · [Verification](docs/verification.md) · [Changelog](CHANGELOG.md)

## Status and license

Alpha, installed from source. Protocol and persistence tests are separate from real-model
quality evaluation. Emotional state is fictional simulation, not a psychological assessment.
Local storage does not mean local inference: configured providers receive submitted context.
Owner IDs are namespaces, not authentication. Read [Security](SECURITY.md) before deployment.

Code is [MIT licensed](LICENSE). Anima branding and character artwork have separate
[asset terms](docs/assets/README.md); they are not runtime dependencies.

## Authors

Anima Brain is built by [Jun Yu Chen (@spearsheep)](https://github.com/spearsheep) and
[@kayllla](https://github.com/kayllla).
