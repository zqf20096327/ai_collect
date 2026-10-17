# context-kit

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

English | [中文](README_ZH.md)

> **Do the simplest thing that works.**

A minimal, framework-agnostic toolkit for Context Engineering. Not another agent framework — just pure functions and a Context dataclass.

**Built for learning** — understand Context Engineering concepts through readable, minimal code.

## 💡 Motivation

> "Most AI Agent failures are not failures of model capability, but failures of Context Engineering."

As LLMs become more powerful, the bottleneck shifts from model intelligence to **how we manage context**. Research on [context rot](https://research.trychroma.com/context-rot) shows that as context windows fill up, the model's ability to extract accurate information degrades — across all models.

**Context Engineering** is the discipline of dynamically assembling the optimal context for each reasoning step. It's not just "advanced prompting" — it's treating context as a **finite resource with diminishing marginal returns**, like memory in an operating system.

The four pillars of Context Engineering are:

| Pillar | Purpose | context-kit Module |
|--------|---------|-------------------|
| **Select** | JIT retrieval — pull information on-demand | `select` |
| **Write** | Persist information outside the context window | `memory` |
| **Compress** | Reduce context size while preserving signal | `Context.compress_*` |
| **Isolate** | Distribute context across sub-agents | Framework-level |

context-kit implements the first three pillars as pure functions, letting you compose them with any agent framework.

> [!TIP]
> 📚 **Deep Dive**: For a comprehensive guide on Context Engineering patterns, see [One Poem Suffices: Context Engineering](https://github.com/keli-wen/One-Poem-Suffices/blob/master/blogs/Context%20Engineering/README.md) and [One Poem Suffices: Just-in-Time Context](https://github.com/keli-wen/One-Poem-Suffices/blob/master/blogs/Just-in-Time%20Context/README.md).

## 📦 Why context-kit?

Context is a limited resource with diminishing returns. As context windows fill up, model performance degrades. context-kit provides the building blocks to manage context effectively:

| Module | Purpose | Key Operations |
|--------|---------|----------------|
| **Context** | Core dataclass | `compress_by_rule`, `compress_by_model`, format conversion |
| **Select** | JIT Context Retrieval | `list_dir`, `grep`, `read_file` |
| **Memory** | Context Persistence | `view`, `create`, `str_replace`, `insert`, `delete` |
| **Tools** | Agent Integration | `get_memory_tools`, `get_select_tools` |

## 🚀 Installation

### With uv (Recommended)

```bash
git clone https://github.com/keli-wen/context-kit.git
cd context-kit
uv sync                              # Install dependencies
uv run python examples/basic/00_minimal.py  # Run example
```

### Without uv

If you don't have [uv](https://docs.astral.sh/uv/) installed:

```bash
# Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use pip to build from source
git clone https://github.com/keli-wen/context-kit.git
cd context-kit
pip install -e .                     # Install in editable mode
pip install -e ".[example]"          # With example dependencies
pip install -e ".[dev]"              # With dev dependencies
```

## ⚡ Quick Example

```python
from context_kit import Context, memory, select

# 1. Create context from messages
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"},
]
ctx = Context.from_openai(messages)
print(f"Messages: {len(ctx)}, Tokens: ~{ctx.estimate_tokens()}")

# 2. Compress by clearing old tool results (Claude Context Editing API style)
ctx = ctx.compress_by_rule(keep_tool_uses=3)

# 3. Export to different formats
openai_msgs = ctx.to_openai()
anthropic_msgs, system = ctx.to_anthropic()
google_contents, system = ctx.to_google()
```

## 📚 Core Concepts

### Context: The Core Dataclass

The `Context` class manages conversation history with compression and format conversion:

```python
from context_kit import Context

# Create from various formats
ctx = Context.from_openai(messages)
ctx = Context.from_anthropic(messages, system="You are helpful.")
ctx = Context.from_google(contents, system="You are helpful.")

# Compression operations
ctx = ctx.compress_by_rule(keep_tool_uses=3)  # Clear old tool results
ctx = await ctx.compress_by_model(llm, keep_recent=3)  # LLM summarization

# Export to any format
openai_msgs = ctx.to_openai()
anthropic_msgs, system = ctx.to_anthropic()
```

> [!NOTE]
> **Thinking/Reasoning Format Support**: The `Message` class supports thinking blocks across providers (Anthropic `type: "thinking"`, OpenAI/DeepSeek `reasoning_content`, Google `thought: true`). This feature is experimental — provider APIs may change. Please [file an issue](https://github.com/keli-wen/context-kit/issues) if you encounter compatibility problems.

### compress_by_rule: Tool & Thinking Clearing

Aligned with [Claude Context Editing API](https://docs.anthropic.com/en/docs/build-with-claude/context-management). Clears old tool results and thinking blocks to reduce context size:

<p align="center">
  <img src="assets/context_editing_mix_strategy.png" width="700" alt="Context Editing Mixed Strategy">
</p>

```python
# Clear old tool results, keep only last 3
ctx = ctx.compress_by_rule(keep_tool_uses=3)

# Exclude specific tools from clearing
ctx = ctx.compress_by_rule(keep_tool_uses=3, exclude_tools=["read_file"])

# Clear thinking blocks too
ctx = ctx.compress_by_rule(
    keep_tool_uses=3,
    clear_thinking=True,
    keep_thinking_turns=1,
)

# Archive cleared content to memory (with retrieval guidance)
ctx = ctx.compress_by_rule(
    keep_tool_uses=3,
    memory_path="./agent_data",  # Same path as get_memory_tools()
)
# Placeholder: "[Tool result cleared. Use memory_read('/memories/tool_001_grep.md') to retrieve.]"
```

<details>
<summary>📊 Example Output</summary>

<p align="center">
  <img src="assets/compress_by_rule_example.png" width="500" alt="compress_by_rule Demo">
</p>

</details>

### compress_by_model: LLM Summarization

Uses an LLM to summarize older conversation turns:

```python
from context_kit.llm import from_litellm

llm = from_litellm(model="gpt-4o-mini")
ctx = await ctx.compress_by_model(
    llm,
    instruction="Preserve: key decisions, unresolved issues. Discard: exploratory attempts.",
    keep_recent=3,
)
```

### Select: JIT Context Retrieval

Progressive Disclosure pattern — start with an overview, narrow down, then load on demand:

```python
from context_kit import select

# Step 1: Understand the map (low token cost)
entries = select.list_dir("./src", max_depth=2)

# Step 2: Narrow down
matches = select.grep(r"def \w+", "./src", file_pattern="*.py")

# Step 3: Load on demand
content = select.read_file("./src/auth.py", start_line=40, end_line=60)
```

### Memory: Context Persistence

Persist information outside the context window ([Claude Memory Tool interface](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)):

```python
from context_kit import memory

memory.init(path="./agent_data")

# CRUD operations
memory.create("/memories/notes.md", "# Analysis\n\nKey findings...")
content = memory.view("/memories/notes.md")
memory.str_replace("/memories/notes.md", "old", "new")
memory.insert("/memories/notes.md", 3, "- New item")
memory.delete("/memories/notes.md")
```

### Tools: Agent Integration

Export tool definitions for agent frameworks:

```python
from context_kit import tools

# Get all tools with shared memory_path
all_tools = tools.get_all_tools(
    memory_path="./agent_data",
    select_path="./src",
)

# Or get specific tool sets
memory_tools = tools.get_memory_tools(memory_path="./agent_data")
select_tools = tools.get_select_tools(select_path="./src")
```

### LLM Adapters

Unified interface for different LLM providers:

```python
from context_kit.llm import from_openai, from_anthropic, from_litellm

# OpenAI
llm = from_openai(model="gpt-4o-mini")

# Anthropic
llm = from_anthropic(model="claude-3-haiku-20240307")

# LiteLLM (any provider)
llm = from_litellm(model="gpt-4o-mini")
```

## 🔗 Integration Example

```python
from camel.agents import ChatAgent
from camel.toolkits import FunctionTool
from context_kit import Context, tools as context_kit_tools

# Setup agent with context-kit tools
ctx_tools = [FunctionTool(f) for f in context_kit_tools.get_all_tools(
    memory_path="./agent_data",
    select_path="./src",
)]

agent = ChatAgent(
    system_message="You are a helpful assistant.",
    tools=ctx_tools,
)

# After conversation, compress context
history = agent.memory.get_context()
ctx = Context.from_openai(history)
compressed = ctx.compress_by_rule(keep_tool_uses=3, memory_path="./agent_data")
```

## 📂 Examples

See `examples/` directory:

| Example | Description |
|---------|-------------|
| `basic/00_minimal.py` | Quick start |
| `basic/01_select_tools.py` | JIT Context Retrieval |
| `basic/02_memory.py` | Memory persistence |
| `basic/03_compress_rules.py` | Tool & thinking clearing |
| `basic/04_compress_model.py` | LLM summarization |
| `integrations/camel/` | CAMEL framework integration |
| `integrations/adk/` | Google ADK integration |

## 🎯 Design Philosophy

| Principle | Description |
|-----------|-------------|
| **Minimal** | Pure functions, lightweight core |
| **Composable** | Each module independent, combine as needed |
| **Framework-agnostic** | Works with any agent framework |
| **Educational** | Code as documentation for Context Engineering |

### Design Inspiration

<p align="center">
  <img src="assets/prompt_engineering_vs_context_engineering.webp" width="700" alt="Prompt Engineering vs Context Engineering">
  <br>
  <em>Image source: <a href="https://www.anthropic.com/research/building-effective-agents">Anthropic - Building Effective Agents</a></em>
</p>

Context engineering treats context as structured blocks (docs, tools, memory, history) rather than a single prompt string. Inspired by Google ADK's "[context as a compiled view](https://developers.googleblog.com/en/agent-development-kit-context-aware-multi-agent/)" thesis:

> "Context is a compiled view over a richer stateful system... context engineering stops being prompt gymnastics and starts looking like systems engineering."

context-kit provides the primitives for this compilation: **Select** retrieves relevant blocks, **Memory** persists state, and **Compress** optimizes the final view.

### What context-kit is NOT

- Not an agent framework (use CAMEL, LangGraph, etc.)
- Not an LLM API wrapper (use LiteLLM, OpenAI SDK, etc.)
- Not a proxy server

### Isolation Pattern

For sub-agent isolation (preventing context pollution), compose existing primitives at the framework level:

```python
# Framework layer (not context-kit)
sub_ctx = Context.from_dict([{"role": "system", "content": system}])
sub_ctx = await run_sub_agent(sub_ctx, task)
summary = await sub_ctx.compress_by_model(llm, keep_recent=0)
parent_ctx = parent_ctx.add_message("assistant", summary_text)
```

## 🗺️ Roadmap

### Completed

- [x] Context dataclass with format conversion (OpenAI, Anthropic, Google)
- [x] compress_by_rule: Clear tool results & thinking blocks (Claude API aligned)
- [x] compress_by_model: LLM-based summarization
- [x] Memory module (Claude Memory Tool interface)
- [x] Select module (list_dir, grep, read_file)
- [x] LLM adapters (OpenAI, Anthropic, LiteLLM)
- [x] Tools export (get_memory_tools, get_select_tools)
- [x] Add `Context.from_dict()` convenience for thinking blocks
- [x] Support thinking/reasoning formats: Anthropic (`type: "thinking"`), OpenAI/DeepSeek (`reasoning_content`), Google (`thought: true`)

### Planned

- [ ] Add more integration examples (LangGraph, AutoGen)
- [ ] MCP server format export
- [ ] Streaming support for compress_by_model
- [ ] Semantic search with vector index for memory module (optional dependency)

## 🙏 References

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - Anthropic
- [Architecting Context-Aware Multi-Agent Framework](https://developers.googleblog.com/en/agent-development-kit-context-aware-multi-agent/) - Google ADK
- [Context Rot Research](https://research.trychroma.com/context-rot) - Chroma
- [Claude Context Management API](https://docs.anthropic.com/en/docs/build-with-claude/context-management) - Anthropic
- [Claude Memory Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) - Anthropic

## License

MIT

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.