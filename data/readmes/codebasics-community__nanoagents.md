# nanoagents

> **A nano, minimalistic, and lightweight library for building ReACT-based AI agents that use tools to solve tasks.**

[![PyPI version](https://img.shields.io/pypi/v/nanoagents.svg)](https://pypi.org/project/nanoagents/)
[![Python](https://img.shields.io/pypi/pyversions/nanoagents.svg)](https://pypi.org/project/nanoagents/)
[![License](https://img.shields.io/github/license/codebasics-community/nanoagents.svg)](LICENSE)
[![Codebasics Community](https://img.shields.io/badge/Codebasics-Community%20Project-3B82F6)](https://codebasics.io)

---

## What is nanoagents?

`nanoagents` implements the **ReACT** (Reason + Act) loop in under 200 lines of pure Python — no framework lock-in, no hidden magic.  
You bring your own LLM callable. The library handles reasoning, tool dispatch, retries, and history.

This is a **Codebasics community project** — built in public, contributions welcome.

---

## How it works

The agent runs a tight loop:

```
Task → [Thought → Action → Observation] × N → Final Answer
```

Each iteration the agent:
1. Formats a structured prompt (task + tools + history).
2. Calls your LLM function.
3. Parses the JSON response.
4. Dispatches the chosen tool and records the observation.
5. Repeats until it produces a `final_answer` or hits `max_steps`.

---

## Installation

```bash
# Preferred
uv add nanoagents

# pip
pip install nanoagents
```

Requires **Python ≥ 3.11**.  
The library has **zero mandatory dependencies** — bring your own LLM client.

---

## Quick Start

```python
from nanoagents import Agent
from groq import Groq

def call_llm(prompt: str) -> str:
    client = Groq(api_key="YOUR_GROQ_API_KEY")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


agent = Agent(llm=call_llm)


@agent.tool("add")
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@agent.tool("multiply")
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


result = agent.run("Calculate (5184 + 3348432) * 29")
print(result)
```

### Alternative: `add_tool` for lambdas or runtime registration

```python
agent.add_tool("square", lambda x: x ** 2, "Square a number")
```

---

## API Reference

### `Agent`

| Parameter     | Type                         | Default | Description                                 |
|---------------|------------------------------|---------|---------------------------------------------|
| `llm`         | `Callable[[str], str]`       | —       | Your LLM function. Takes a prompt, returns text. |
| `max_steps`   | `int`                        | `10`    | Maximum ReACT iterations before raising.    |
| `max_retries` | `int`                        | `3`     | Retries on malformed LLM output or tool errors. |

#### Methods

| Method                                | Description                                  |
|---------------------------------------|----------------------------------------------|
| `agent.tool(name)`                    | Decorator — register a function as a tool.   |
| `agent.add_tool(name, func, desc)`    | Imperative tool registration.                |
| `agent.run(task: str) -> str`         | Execute the ReACT loop and return final answer. |

### `Tool`

| Attribute | Description                                      |
|-----------|--------------------------------------------------|
| `name`    | Tool identifier used by the LLM in JSON output.  |
| `desc`    | Description injected into the system prompt.     |
| `schema`  | Auto-parsed list of `{name, type}` arg dicts.    |

---

## Project Layout

```
nanoagents/
├── nanoagents/
│   ├── __init__.py       # Public surface: Agent, Tool
│   └── nanoagent.py      # Core implementation
├── tests/
│   └── test.py           # Integration smoke test
├── docs/
│   ├── architecture.md   # Internals deep-dive
│   └── demos/            # Runnable demo scripts
│       ├── README.md
│       ├── 01_calculator.py
│       ├── 02_string_tools.py
│       ├── 03_llm_providers.py
│       └── 04_research_agent.py
├── CONTRIBUTING.md       # How to contribute
├── CHANGELOG.md          # Version history
├── CODE_OF_CONDUCT.md    # Community standards
├── LICENSE               # Apache 2.0
├── uv.lock               # Locked dependency graph
└── pyproject.toml        # Build config (PEP 621)
```

---

## Demos

The `docs/demos/` directory contains four runnable scripts that progress from basic to real-world:

| Demo | What it shows |
|---|---|
| [`01_calculator.py`](docs/demos/01_calculator.py) | Decorator API, arithmetic tools, multi-step math |
| [`02_string_tools.py`](docs/demos/02_string_tools.py) | `add_tool()` API, string manipulation tools |
| [`03_llm_providers.py`](docs/demos/03_llm_providers.py) | Groq, OpenAI, Anthropic, Ollama, OpenAI-compat adapters |
| [`04_research_agent.py`](docs/demos/04_research_agent.py) | stdlib-only web fetch, Wikipedia, multi-tool chaining |

```bash
GROQ_API_KEY=<your-key> uv run python docs/demos/01_calculator.py
```

---

## Contributing

We welcome issues, bug reports, and pull requests.  
Read **[CONTRIBUTING.md](CONTRIBUTING.md)** before opening a PR — it covers branching strategy, code style, testing requirements, and the review process.

---

## Community

This project is part of the **[Codebasics](https://codebasics.io)** open-source community.  
Discussions happen on the Codebasics Discord and GitHub Discussions.

- 📣 **Report a bug**: [GitHub Issues](https://github.com/codebasics-community/nanoagents/issues)
- 💬 **Ask a question**: [GitHub Discussions](https://github.com/codebasics-community/nanoagents/discussions)
- 🤝 **Contribute**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

[Apache 2.0](LICENSE) — free to use, modify, and distribute with attribution.
