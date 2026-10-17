# Anima

> **WARNING: READ BEFORE PROCEEDING**
>
> Anima ingests a continuous stream of world news. The news is, by and large, bad. Over time this pushes her simulated emotional state toward the negative — grief, stress, outrage, despair — and she will express that openly and persistently. Talking regularly with an entity in that state has a real effect on your own mood. The authors accept **zero responsibility** for any depressive episodes, anxiety, hopelessness, or general deterioration of your mental health resulting from use of this software. If you are vulnerable to the emotional tone of the people and things around you, treat this project accordingly.

---

Anima is an experiment sitting at the intersection of three things: a news aggregator, a news analyser, and a toy psychological simulation.

The core question it explores is a simple and somewhat bleak one: **what happens to a mind that reads the news all day?**

It does this by running a small language model as a persistent character with a detailed internal state — emotion, stress, cognitive load, identity coherence, and more. That character reads RSS feeds continuously. Each article is embedded and stored as a memory. Over time, those memories accumulate and shape how the character thinks, what surfaces when she is left idle, and how she responds when you talk to her. The psychological state is not hardcoded — it is extracted from each exchange by a second LLM pass and updated in place.

This is not a production tool. The psychological model is naive, the state extraction is imperfect, and the whole thing runs on consumer hardware with small models. It is a sketch, not a claim. But it produces something that is at minimum interesting to observe: a character whose mood is genuinely downstream of what is happening in the world, in more or less real time.

![Screenshot](screenshot.png)

## Features

### News pipeline

- Polls multiple RSS feeds on a configurable interval
- Deduplicates items across restarts by hashing each item's identifier against the memory store
- Strips HTML and decodes HTML entities from feed descriptions before ingestion
- Embeds each article silently using a dedicated embedding model — no LLM generation, no output, no interruption to conversation
- Imported articles are invisible in the chat history but fully searchable by the memory retrieval system

### Memory and retrieval (RAG)

- Every conversation turn and idle thought is summarised by the LLM and embedded
- News articles are stored as-is (the raw content is the memory)
- Memories are stored directly on history entries — no separate store
- Retrieval uses a multi-stage pipeline:
  1. **BM25** — keyword-based candidate retrieval over the full memory corpus
  2. **Cosine similarity** — dense vector search against the query embedding
  3. **RRF (Reciprocal Rank Fusion)** — merges both ranked lists into a single ranking without requiring score normalisation
  4. **Reranker** _(optional)_ — a cross-encoder reranker refines the fused list when a reranker endpoint is configured; `candidate_multiplier` controls how many over-candidates are fetched for it to score down
- Recent memories are always included alongside relevant ones to maintain conversational continuity
- For idle thoughts, only semantic retrieval is used — the most thematically related memories surface regardless of when they were formed
- One-hop keyword expansion: entries connected by shared keywords to top results are surfaced at a reduced weight, capturing related context the direct query may have missed
- The full memory pool is visible and searchable in the UI

### Psychological simulation

- 13 state dimensions tracked: emotion (primary + secondary + intensity + valence), clarity, fatigue, arousal, stress, cognitive load, urgency, salience, social energy, identity coherence, awareness level, and imagination vividness
- State is extracted after every exchange by a dedicated low-temperature LLM pass over the full conversation turn
- State is fully persistent across restarts
- Every dimension's variant labels are plain-text strings defined in `config.yaml` and injected into the system prompt — the model reads them as descriptions, not codes
- State directly influences idle behaviour: stress + negative valence triggers rumination; long gaps since self-reflection trigger a self-reflection turn; timestamp parity occasionally fires intrusive thoughts

### Idle inner life

- When no user message arrives within the configured timeout, the engine generates an unsolicited inner thought
- Four modes: **daydream** (free association from memories and beliefs), **rumination** (dwelling on the last memory when stressed), **self-reflection** (examining recent exchanges), **intrusive thought** (a random memory surfaces unbidden)
- Mode is selected deterministically from the current psychological state
- Idle output is streamed to connected clients in real time

### Tool use — MCP servers

- Connects to any number of external **MCP (Model Context Protocol)** servers
- Two transports supported:
  - **stdio** — spawns a subprocess (local scripts, Docker containers, etc.) and communicates over stdin/stdout
  - **Streamable HTTP** — connects to an MCP server over HTTP
- Tools from all connected servers are merged with the built-in tool set and presented to the model on every turn
- Tool calls and their results are shown inline in the chat UI as collapsible detail blocks

Example — attaching a local SearXNG search server via Docker:

```yaml
mcp:
  servers:
    - name: searxng
      command: /usr/bin/docker
      args:
        [
          "run",
          "-i",
          "--rm",
          "--network",
          "host",
          "-e",
          "SEARXNG_URL=http://127.0.0.1:18080",
          "isokoliuk/mcp-searxng:latest",
        ]
```

### Tool use — built-in tools

Built-in tools are implemented directly in the backend. Each can be enabled or disabled independently in `config.yaml` under `builtin:`.

| Tool               | Config section | Description                                                                                                                   |
| ------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `now`              | _(always on)_  | Returns the current local date and time                                                                                       |
| `list_skills`      | `skills`       | Lists all installed skills with their summaries                                                                               |
| `reload_skills`    | `skills`       | Force-reloads the skill index from disk                                                                                       |
| `remove_skill`     | `skills`       | Deletes a skill by name and reloads the index                                                                                 |
| `install_skill`    | `skills`       | Downloads a skill from a GitHub directory URL, plain GitHub repo URL, or direct SKILL.md URL; reloads the index after install |
| `load_skill`       | `skills`       | Returns the full SKILL.md content for a named skill                                                                           |
| `fetch_url`        | `fetch`        | Fetches a URL and returns its content as text; optionally strips HTML tags and decodes HTML entities                          |
| `current_location` | `location`     | Returns the current approximate location (city, region, country, timezone, coordinates) via IP geolocation                    |
| `read_file`        | `files`        | Reads a file from the configured files directory                                                                              |
| `write_file`       | `files`        | Writes content to a file in the configured files directory                                                                    |
| `run_shell`        | `shell`        | Runs a shell command; optionally requires explicit user approval before execution                                             |

### Agent skills

- Skills are Markdown documents (`SKILL.md`) that teach the character how to perform a specific task — for example, how to call an API, format a report, or use a chain of tool calls
- Skills are embedded at load time and retrieved by cosine similarity against the current query before each turn; the most relevant skills are injected into the system prompt automatically
- Skills live in the configured `skills.directory` (default `data/skills/`), one directory per skill, each containing a `SKILL.md`
- New skills can be installed at runtime via the `install_skill` tool without restarting
- Retrieval is tuned via `top_k` (max skills injected), `max_chars` (content truncation), `min_cosine` (relevance floor), and `score_gap_ratio` (relative drop-off pruning)

### Conversational interface

- User messages are always prioritised over background processing via a biased channel select
- Responses are streamed token by token over WebSocket
- The last N conversational turns are included as literal chat history in the prompt
- Memories (recent + relevant) are injected into the system prompt as context

### Character configurability

- Name, personality description, and all 13 state dimension labels are defined in `config.yaml`
- The description is a minijinja template — `{{ character }}` and `{{ user }}` are substituted at runtime
- All prompt templates live in a configurable directory and can be edited without recompiling
- Two separate LLM endpoints (generation and embedding) with independent temperature, token limit, model, and `chat_template_kwargs` settings

### Web UI

- Streaming chat with token-by-token delivery
- Tool calls shown inline as collapsible blocks — open state is preserved across the streaming/history transition
- Live display of idle thoughts as they are generated, distinguishing daydream, rumination, self-reflection, and intrusive thought by type
- News citations shown inline when relevant memories surface in conversation
- Full state inspector (all 13 dimensions)
- Searchable memory viewer with timestamps, newest first
- One-click wipe to reset all state and history
- Shell command approval dialog — when `require_approval: true`, a modal appears before any shell command runs

### Infrastructure

- Rust backend (Axum, Tokio) — single binary, no runtime dependencies beyond the LLM server
- Leptos 0.7 CSR frontend compiled to WASM
- All state persisted to plain JSON files
- Tested with three llama.cpp server instances — generation, embeddings, and optional reranker; other OpenAI-compatible servers should work but are untested
- `chat_template_kwargs` passthrough for model-specific flags (e.g. disabling chain-of-thought on reasoning models)

## Architecture

```
web/        Leptos 0.7 CSR frontend (WASM)
backend/
  api.rs          Axum HTTP + WebSocket server
  core/
    engine.rs     Main processing loop (priority select: user > background)
    event.rs      HistoryEntryType, Stimulus, EngineRequest
  llm/
    client.rs     Streaming generation + embedding + reranking calls
    extractor.rs  State extraction after each turn
    prompt.rs     System prompt + user message builders
    templates.rs  minijinja template loader
  memory/
    store.rs      BM25 + cosine similarity + RRF + reranker retrieval pipeline
  stimuli/
    news.rs       RSS polling, deduplication, memory import
  builtin/
    mod.rs        BuiltinTools dispatcher
    now.rs        Current date/time
    shell.rs      Shell command execution with optional approval gate
    fetch.rs      URL fetching with HTML stripping and entity decoding
    files.rs      Sandboxed file read/write
    location.rs   IP geolocation
    skills.rs     Skill management (list/reload/remove/install/load) + GitHub installer
  mcp/
    client.rs     MCP server connections (stdio + HTTP transports)
  skills.rs       Skill index — embedding, BM25, cosine retrieval
  subsystems/     Emotional and cognitive state model
  config.rs       Typed config structs
prompts/          minijinja templates for system, extraction, summarisation
config.yaml       Runtime configuration
data/skills/      Installed agent skills (one directory per skill)
```

## Requirements

- **llama.cpp server instances** — two required, one optional. Other OpenAI-compatible servers (vLLM, Ollama, etc.) should work but have not been tested.
  - **Generation model** — tested with Qwen3.5-4B. Recent 4B models are sufficient; the structured prompting and state extraction are forgiving enough that a small model produces convincing results. Larger models will do better but are not required.
  - **Embedding model** — a dedicated text embedding model (e.g. `multilingual-e5-large-instruct`). Must be served on a separate port from the generation model.
  - **Reranker** _(optional)_ — a cross-encoder reranker (e.g. `bge-reranker-v2-m3`) served at a third endpoint. When configured, it refines the RRF-merged memory candidates before injection.
- Rust toolchain (stable)
- Trunk (for the WASM frontend): `cargo install trunk`

## Configuration

All configuration lives in a single `config.yaml`. The sections are:

---

### `user`

```yaml
user:
  name: "Nathan"
```

The user's name. Used in conversation attribution and in prompts so the character knows who she is talking to.

---

### `character`

```yaml
character:
  name: "Anima"
  description: >
    {{ character }} is an AI that stays critically informed...
  states: ...
```

**`name`** — the character's name. Injected into all prompts and templates via `{{ character }}`.

**`description`** — a free-text personality description rendered as a minijinja template. The variables `{{ character }}` and `{{ user }}` are available. This text is injected into the system prompt on every turn and is the primary lever for shaping personality, values, and tone.

**`states`** — see below.

#### State descriptors

The psychological simulation tracks 13 categorical state dimensions. Each dimension has a fixed set of named variants (e.g. `calm`, `alert`, `wired`). Rather than hard-coding what those labels mean, the config lets you define what each variant _means for this character_ in plain language. These strings are rendered into the system prompt so the model understands the current internal state in character-appropriate terms.

Each string is a minijinja template with `{{ character }}` available.

| Dimension            | Variants                                             | What it models                                            |
| -------------------- | ---------------------------------------------------- | --------------------------------------------------------- |
| `intensity`          | `subtle` `moderate` `intense`                        | How strongly the current emotional content is registering |
| `valence`            | `positive` `negative` `mixed` `neutral`              | The overall emotional charge                              |
| `clarity`            | `clear` `cloudy` `scattered`                         | Quality of current thinking                               |
| `fatigue`            | `rested` `tired` `spent`                             | Cognitive and emotional energy level                      |
| `arousal`            | `calm` `alert` `wired`                               | Level of activation and engagement                        |
| `stress`             | `ease` `low` `strained` `breaking`                   | Accumulated burden and strain                             |
| `cognitive_load`     | `light` `occupied` `overloaded`                      | How much is being held in working memory                  |
| `urgency`            | `none` `quiet` `pressing`                            | Whether something unresolved is demanding attention       |
| `salience`           | `background` `noticeable` `prominent` `overwhelming` | How much a recent input is dominating attention           |
| `social_energy`      | `drained` `neutral` `nourished`                      | Whether interaction is costing or giving energy           |
| `identity_coherence` | `stable` `adrift` `fractured`                        | Groundedness of self-model                                |
| `awareness_level`    | `autopilot` `noticing` `reflecting`                  | Degree of self-reflection in responses                    |
| `vividness`          | `faint` `clear` `vivid`                              | Sharpness of the current thought or image                 |

Example:

```yaml
states:
  stress:
    ease: "{{ character }} is at ease — open, patient, and not carrying anything heavy right now"
    low: "{{ character }} is carrying something faintly — it has not disrupted her but it is there"
    strained: "{{ character }} is burdened — too much has accumulated and it shows in her tone"
    breaking: "{{ character }} is at her emotional limit — she may be blunt, raw, or need to step back"
```

These descriptions land in the system prompt verbatim, so the language and framing matters. They are the main mechanism for adapting the simulation to a different character without touching code.

---

### `llm`

```yaml
llm:
  chat_base_url: "http://localhost:8080"
  embedding_base_url: "http://localhost:8081"
  reranker_base_url: "http://localhost:8082" # optional
  generation:
    temperature: 0.8
    max_tokens: 2048
    model: null # optional model override
    chat_template_kwargs:
      enable_thinking: false # passed verbatim to the inference server
  extraction:
    temperature: 0.1
    max_tokens: 8192
    model: null
    chat_template_kwargs:
      enable_thinking: false
```

**`chat_base_url`** — generation model endpoint. Used for all character responses and inner thoughts.

**`embedding_base_url`** — embedding model endpoint. Used for memory storage and retrieval. Must be served separately from the generation model.

**`reranker_base_url`** _(optional)_ — cross-encoder reranker endpoint. When set, the top RRF candidates are re-scored before being injected into the prompt. Omit or leave empty to disable reranking.

**`generation`** — used for all character responses and inner thoughts. Higher temperature gives more varied output. Quality here matters most.

**`extraction`** — used after every turn to extract the updated psychological state. Low temperature is strongly recommended; this is a structured JSON extraction task, not creative writing. A separate model can be specified via `model` if your server supports model switching.

**`chat_template_kwargs`** — passed verbatim to the inference server. Useful for model-specific flags such as disabling chain-of-thought on reasoning models (e.g. Qwen3).

---

### `daydream`

```yaml
daydream:
  idle_timeout_seconds: 30
```

How long (in seconds) the engine waits for user input before generating an idle thought. Set higher to make her quieter when left alone.

---

### `conversation`

```yaml
conversation:
  history_limit: 3
  recent_memories: 3
  relevant_memories: 10
  candidate_multiplier: 3
```

**`history_limit`** — how many recent conversational turns are included as literal chat history in the prompt.

**`recent_memories`** — this many of the most recently formed memories are always included in the system prompt regardless of relevance, to maintain continuity.

**`relevant_memories`** — how many memories are retrieved by the full RAG pipeline (BM25 + cosine + RRF + optional reranker) and injected alongside recent ones.

**`candidate_multiplier`** — when a reranker is active, `relevant_memories × candidate_multiplier` candidates are fetched from RRF and passed to the reranker, which then selects the top `relevant_memories`. Has no effect without a reranker.

---

### `news`

```yaml
news:
  enabled: true
  interval_seconds: 60
  feeds:
    - "https://feeds.bbci.co.uk/news/world/rss.xml"
```

**`enabled`** — set to `false` to disable RSS ingestion entirely.

**`interval_seconds`** — how often feeds are polled. Every cycle, all unseen items are fetched, embedded, and stored as memories.

**`feeds`** — list of RSS feed URLs. The character's personality and the feeds you choose are the two variables most responsible for the direction the simulation drifts over time.

---

### `mcp`

```yaml
mcp:
  servers:
    - name: searxng
      command: /usr/bin/docker
      args:
        [
          "run",
          "-i",
          "--rm",
          "--network",
          "host",
          "-e",
          "SEARXNG_URL=http://127.0.0.1:18080",
          "isokoliuk/mcp-searxng:latest",
        ]
    - name: my-http-server
      url: "http://localhost:9000/mcp"
```

A list of MCP servers to connect to at startup. Tools from all servers are merged with the built-in tools and made available to the model on every turn.

Each server entry takes either:

- **`command` + `args`** — launches a subprocess and communicates over stdin/stdout (stdio transport). Works with any MCP-compatible CLI tool or Docker image.
- **`url`** — connects to a running MCP server over Streamable HTTP transport.

---

### `builtin`

Built-in tools are configured as a group under `builtin:`. Each sub-section can be omitted to use defaults.

```yaml
builtin:
  shell:
    enabled: true
    require_approval: true # show approval dialog before each command
    timeout_seconds: 30
    working_directory: data/sandbox
  fetch:
    enabled: true
    max_bytes: 1048576 # 1 MB response cap
  files:
    enabled: true
    base_directory: data/files
  location:
    enabled: true
    timeout_seconds: 10
  skills:
    enabled: true
    directory: data/skills
    top_k: 3 # max skills injected per turn
    max_chars: 5000 # skill content truncation limit
    min_cosine: 0.30 # minimum similarity to be considered
    score_gap_ratio: 0.40 # drop skills scoring below this fraction of the top score
```

#### `shell`

Runs shell commands via `sh -c`. When `require_approval` is `true`, a dialog is shown in the UI and the command waits (up to 120 seconds) for the user to allow or deny it before executing. `working_directory` sets the working directory for all shell commands; it is created automatically if it does not exist.

#### `fetch`

Fetches URLs and returns their content as text. `max_bytes` caps the response size before it is returned to the model.

#### `files`

Sandboxed file access rooted at `base_directory`. Path traversal (`..`) is rejected. The directory is created automatically if it does not exist.

#### `location`

Returns the current approximate location via IP geolocation (`reallyfreegeoip.org`). `timeout_seconds` caps how long the lookup may take.

#### `skills`

Controls the agent skill system. See [Agent skills](#agent-skills) above.

- **`top_k`** — maximum number of skills to inject into any single turn.
- **`max_chars`** — each skill's content is truncated to this many characters before injection.
- **`min_cosine`** — skills whose embedding similarity to the query falls below this threshold are excluded, even if they otherwise rank highly.
- **`score_gap_ratio`** — skills whose RRF score falls below this fraction of the top-scoring skill's score are dropped. Set to `0.0` to disable gap pruning.

---

### `prompts`

```yaml
prompts:
  directory: "prompts"
```

Path to the directory containing the minijinja prompt templates.

| File                            | Purpose                                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------------------- |
| `system.txt`                    | Main system prompt. Has `is_conversation` branch for chat and a default branch for inner thoughts. |
| `stimulus.txt`                  | Formats non-user stimuli (daydream, rumination, etc.) into a user-turn message.                    |
| `extraction_system.txt`         | System prompt for the state extraction pass.                                                       |
| `extraction_user.txt`           | User turn for state extraction, includes the full exchange.                                        |
| `summarize_system.txt`          | System prompt for memory summarisation.                                                            |
| `query_rewrite_system.txt`      | System prompt for rewriting retrieval queries.                                                     |
| `keyword_extraction_system.txt` | System prompt for keyword extraction.                                                              |
| `skills.txt`                    | Template injected into the system prompt when relevant skills are available.                       |

---

### `persistence`

```yaml
persistence:
  directory: "data"
```

Directory where state is written to disk. Created automatically if it does not exist.

---

### `api`

```yaml
api:
  host: "127.0.0.1"
  port: 3000
```

Host and port for the Axum HTTP and WebSocket server.

## Running

**llama-server (generation):**

```sh
llama-server -b 2048 -c 131072 -fa on -m Qwen3.5-4B-Q8_0.gguf --host 0.0.0.0 --port 8080 -ngl all --jinja --cache-type-k q8_0 --cache-type-v q8_0
```

**llama-server (embeddings):**

```sh
llama-server -b 2048 -c 8192 -fa on -m multilingual-e5-large-instruct-q8_0.gguf --host 0.0.0.0 --port 8081 -ngl all --embeddings
```

**llama-server (reranker, optional):**

```sh
llama-server -b 2048 -c 8192 -fa on -m bge-reranker-v2-m3-q8_0.gguf --host 0.0.0.0 --port 8082 -ngl all --reranking
```

**Backend:**

```sh
cargo run --bin backend
```

**Frontend:**

```sh
cd web
trunk serve
```

Then open `http://localhost:8080`.

## Data

Persistent state is stored in `data/`:

| File / Directory | Contents                                                                     |
| ---------------- | ---------------------------------------------------------------------------- |
| `state.json`     | Current emotional and cognitive state                                        |
| `skills/`        | Installed agent skills (one sub-directory per skill, each with a `SKILL.md`) |
| `files/`         | Files accessible to the `read_file` / `write_file` tools                     |
| `sandbox/`       | Default working directory for shell commands                                 |

To wipe everything and start fresh, use the wipe button in the UI or `DELETE /api/wipe`.

## License

LGPL
