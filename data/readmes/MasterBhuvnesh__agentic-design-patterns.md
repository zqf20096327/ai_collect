<div align="center">

# Agentic Design Patterns

**21 essential patterns for building agentic AI systems.** Each one comes with a diagram, a written discussion, a runnable implementation, and a real captured run.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.5-1C3C3C?logo=langchain&logoColor=white)](https://python.langchain.com)
[![NVIDIA NIM](https://img.shields.io/badge/NVIDIA_NIM-Nemotron-76B900?logo=nvidia&logoColor=white)](https://build.nvidia.com)
[![Patterns](https://img.shields.io/badge/Patterns-21%2F21_implemented-success)](../code)

[Browse the Patterns](#the-21-patterns) · [Run the Code](#running-the-code) · [Why the Failing Runs Matter](#about-the-saved-runs)

</div>

---

## What's Inside

Every pattern is documented four ways, so you can pick whichever gets the idea across fastest.

| Format | Location | Good for |
|---|---|---|
| **Mermaid Diagrams** | [`/mermaid-diagrams`](../mermaid-diagrams) | Seeing the flow at a glance, in plain English |
| **Pattern Discussions** | [`/pattern-discussion`](../pattern-discussion) | When to use it, where it fits, pros, cons, real examples |
| **ASCII Art** | [`/ascii-art`](../ascii-art) | Pasting into Miro, terminals, or anywhere without rich graphics |
| **Runnable Code** | [`/code`](../code) | Actually seeing it work, plus a saved run for every pattern |

Each code example lives in its own folder with the run it produced:

```
code/
├── resources/                # shared LLM client, output helpers, requirements
└── prompt_chaining/
    ├── code.py               # the pattern, commented
    └── result.txt            # a real captured run, readable without an API key
```

---

## The 21 Patterns

### Core Patterns

| # | Pattern | What it does | Links |
|:--|:--|:--|:--|
| 1 | **Prompt Chaining** | Break a complex task into sequential steps | [ASCII](../ascii-art/prompt-chaining.txt) · [Diagram](../mermaid-diagrams/prompt-chaining.mmd) · [Discussion](../pattern-discussion/prompt-chaining.md) · [Code](../code/prompt_chaining/code.py) · [Run](../code/prompt_chaining/result.txt) |
| 2 | **Routing** | Direct each request to the right handler | [ASCII](../ascii-art/routing.txt) · [Diagram](../mermaid-diagrams/routing.mmd) · [Discussion](../pattern-discussion/routing.md) · [Code](../code/routing/code.py) · [Run](../code/routing/result.txt) |
| 3 | **Parallelization** | Run independent work concurrently, then merge | [ASCII](../ascii-art/parallelization.txt) · [Diagram](../mermaid-diagrams/parallelization.mmd) · [Discussion](../pattern-discussion/parallelization.md) · [Code](../code/parallelization/code.py) · [Run](../code/parallelization/result.txt) |
| 4 | **Reflection** | Critique and revise its own output | [ASCII](../ascii-art/reflection.txt) · [Diagram](../mermaid-diagrams/reflection.mmd) · [Discussion](../pattern-discussion/reflection.md) · [Code](../code/reflection/code.py) · [Run](../code/reflection/result.txt) |
| 5 | **Tool Use** | Call real functions instead of guessing | [ASCII](../ascii-art/tool-use.txt) · [Diagram](../mermaid-diagrams/tool-use.mmd) · [Discussion](../pattern-discussion/tool-use.md) · [Code](../code/tool_use/code.py) · [Run](../code/tool_use/result.txt) |

### Advanced Patterns

| # | Pattern | What it does | Links |
|:--|:--|:--|:--|
| 6 | **Planning** | Design the whole step list before executing any of it | [ASCII](../ascii-art/planning.txt) · [Diagram](../mermaid-diagrams/planning.mmd) · [Discussion](../pattern-discussion/planning.md) · [Code](../code/planning/code.py) · [Run](../code/planning/result.txt) |
| 7 | **Multi-Agent Collaboration** | Separate roles handing work to each other | [ASCII](../ascii-art/multi-agent-collaboration.txt) · [Diagram](../mermaid-diagrams/multi-agent-collaboration.mmd) · [Discussion](../pattern-discussion/multi-agent-collaboration.md) · [Code](../code/multi_agent_collaboration/code.py) · [Run](../code/multi_agent_collaboration/result.txt) |
| 8 | **Memory Management** | Decide what to keep verbatim, summarize, or never drop | [ASCII](../ascii-art/memory-management.txt) · [Diagram](../mermaid-diagrams/memory-management.mmd) · [Discussion](../pattern-discussion/memory-management.md) · [Code](../code/memory_management/code.py) · [Run](../code/memory_management/result.txt) |
| 9 | **Learning and Adaptation** | Turn mistakes into rules, without retraining | [ASCII](../ascii-art/learning-and-adaptation.txt) · [Diagram](../mermaid-diagrams/learning-and-adaptation.mmd) · [Discussion](../pattern-discussion/learning-and-adaptation.md) · [Code](../code/learning_and_adaptation/code.py) · [Run](../code/learning_and_adaptation/result.txt) |
| 10 | **Model Context Protocol** | Reach tools through a contract, not an import | [ASCII](../ascii-art/model-context-protocol.txt) · [Diagram](../mermaid-diagrams/model-context-protocol.mmd) · [Discussion](../pattern-discussion/model-context-protocol.md) · [Code](../code/model_context_protocol/code.py) · [Run](../code/model_context_protocol/result.txt) |

### System Patterns

| # | Pattern | What it does | Links |
|:--|:--|:--|:--|
| 11 | **Goal Setting and Monitoring** | Define "done" up front, then measure against it | [ASCII](../ascii-art/goal-setting-and-monitoring.txt) · [Diagram](../mermaid-diagrams/goal-setting-and-monitoring.mmd) · [Discussion](../pattern-discussion/goal-setting-and-monitoring.md) · [Code](../code/goal_setting_and_monitoring/code.py) · [Run](../code/goal_setting_and_monitoring/result.txt) |
| 12 | **Exception Handling and Recovery** | Retry, repair, or fall back, depending on the failure | [ASCII](../ascii-art/exception-handling-and-recovery.txt) · [Diagram](../mermaid-diagrams/exception-handling-and-recovery.mmd) · [Discussion](../pattern-discussion/exception-handling-and-recovery.md) · [Code](../code/exception_handling_and_recovery/code.py) · [Run](../code/exception_handling_and_recovery/result.txt) |
| 13 | **Human-in-the-Loop** | Pause for approval on the actions that deserve it | [ASCII](../ascii-art/human-in-the-loop.txt) · [Diagram](../mermaid-diagrams/human-in-the-loop.mmd) · [Discussion](../pattern-discussion/human-in-the-loop.md) · [Code](../code/human_in_the_loop/code.py) · [Run](../code/human_in_the_loop/result.txt) |
| 14 | **Knowledge Retrieval (RAG)** | Answer from fetched documents, not from memory | [ASCII](../ascii-art/knowledge-retrieval-rag.txt) · [Diagram](../mermaid-diagrams/knowledge-retrieval-rag.mmd) · [Discussion](../pattern-discussion/knowledge-retrieval-rag.md) · [Code](../code/knowledge_retrieval_rag/code.py) · [Run](../code/knowledge_retrieval_rag/result.txt) |
| 15 | **Inter-Agent Communication** | Address agents by capability over a message bus | [ASCII](../ascii-art/inter-agent-communication-a2a.txt) · [Diagram](../mermaid-diagrams/inter-agent-communication-a2a.mmd) · [Discussion](../pattern-discussion/inter-agent-communication-a2a.md) · [Code](../code/inter_agent_communication_a2a/code.py) · [Run](../code/inter_agent_communication_a2a/result.txt) |

### Optimization Patterns

| # | Pattern | What it does | Links |
|:--|:--|:--|:--|
| 16 | **Resource-Aware Optimization** | Spend tokens in proportion to the work | [ASCII](../ascii-art/resource-aware-optimization.txt) · [Diagram](../mermaid-diagrams/resource-aware-optimization.mmd) · [Discussion](../pattern-discussion/resource-aware-optimization.md) · [Code](../code/resource_aware_optimization/code.py) · [Run](../code/resource_aware_optimization/result.txt) |
| 17 | **Reasoning Techniques** | CoT, self-consistency, decomposition, and their cost | [ASCII](../ascii-art/reasoning-techniques.txt) · [Diagram](../mermaid-diagrams/reasoning-techniques.mmd) · [Discussion](../pattern-discussion/reasoning-techniques.md) · [Code](../code/reasoning_techniques/code.py) · [Run](../code/reasoning_techniques/result.txt) |
| 18 | **Guardrails / Safety** | Screen the input, then screen the output separately | [ASCII](../ascii-art/guardrails-safety-patterns.txt) · [Diagram](../mermaid-diagrams/guardrails-safety-patterns.mmd) · [Discussion](../pattern-discussion/guardrails-safety-patterns.md) · [Code](../code/guardrails_safety_patterns/code.py) · [Run](../code/guardrails_safety_patterns/result.txt) |
| 19 | **Evaluation and Monitoring** | Measure quality offline, watch proxies online | [ASCII](../ascii-art/evaluation-and-monitoring.txt) · [Diagram](../mermaid-diagrams/evaluation-and-monitoring.mmd) · [Discussion](../pattern-discussion/evaluation-and-monitoring.md) · [Code](../code/evaluation_and_monitoring/code.py) · [Run](../code/evaluation_and_monitoring/result.txt) |

### Strategic Patterns

| # | Pattern | What it does | Links |
|:--|:--|:--|:--|
| 20 | **Prioritization** | Order work by score, dependencies, and age | [ASCII](../ascii-art/prioritization.txt) · [Diagram](../mermaid-diagrams/prioritization.mmd) · [Discussion](../pattern-discussion/prioritization.md) · [Code](../code/prioritization/code.py) · [Run](../code/prioritization/result.txt) |
| 21 | **Exploration and Discovery** | Search a space of approaches instead of answering once | [ASCII](../ascii-art/exploration-and-discovery.txt) · [Diagram](../mermaid-diagrams/exploration-and-discovery.mmd) · [Discussion](../pattern-discussion/exploration-and-discovery.md) · [Code](../code/exploration_and_discovery/code.py) · [Run](../code/exploration_and_discovery/result.txt) |

---

## Running the Code

Examples use [LangChain](https://python.langchain.com) with [NVIDIA NIM](https://build.nvidia.com) endpoints.

**1. Install** from the `code/` directory:

```bash
cd code
python -m venv .venv
.venv\Scripts\activate                       # Windows
source .venv/bin/activate                    # macOS/Linux
pip install -r resources/requirements.txt
```

**2. Add your key** to `code/resources/.env`:

```env
API_KEY=your_nvidia_api_key
```

**3. Run any pattern** as a module, from inside `code/`:

```bash
python -m prompt_chaining.code
```

<details>
<summary><b>Why <code>-m</code>, and why underscored folders?</b></summary>

<br>

Running `python prompt_chaining/code.py` directly fails with `ModuleNotFoundError: resources`, because Python puts the *script's* folder on the import path rather than `code/`. The module form keeps `code/` on the path, so every example can share `resources/`.

That is also why the folders use underscores. `python -m prompt-chaining.code` is not a valid module name.

To save a run alongside the code, the way every committed `result.txt` was made:

```powershell
python -m prompt_chaining.code | Tee-Object prompt_chaining\result.txt
```

```bash
python -m prompt_chaining.code | tee prompt_chaining/result.txt
```

Piping makes stdout a non-tty, so `rich` drops colour and falls back to ASCII table borders. The content is identical.

</details>

See [`code/README.md`](../code/README.md) for the full module list and setup detail.

---

## About the Saved Runs

Every `result.txt` is **real output from the committed code**, not a hand-written illustration. Several of them record the pattern failing, plateauing, or costing more than it saved. Those runs were kept deliberately, because they teach more than a clean one does.

| Pattern | What its run actually shows |
|:--|:--|
| [Evaluation and Monitoring](../pattern-discussion/evaluation-and-monitoring.md) | The scoreboard's verdict is **wrong**. The grader marked `1` incorrect against an answer key saying `one`. A broken eval doesn't look broken, it looks like a result. |
| [Reasoning Techniques](../pattern-discussion/reasoning-techniques.md) | All four techniques tie, including the "direct" baseline. Decomposition spent 4 calls to reach what 1 call already had. |
| [Goal Setting and Monitoring](../pattern-discussion/goal-setting-and-monitoring.md) | Ends in recorded failure. Fixing the missing specs breaks the word limit, because constraint satisfaction isn't monotonic. |
| [Human-in-the-Loop](../pattern-discussion/human-in-the-loop.md) | The risk assessor gates a routine **receipt email** as irreversible. Over-gating, live. |
| [Reflection](../pattern-discussion/reflection.md) | Never converges. The critic spends three rounds on progressively more marginal objections. |
| [Exploration and Discovery](../pattern-discussion/exploration-and-discovery.md) | An earlier run produced *no* child that beat its parent. Refinement plateaus fast. |

Each pattern's discussion doc explains what its run revealed and what to do about it.

> **Note:** `temperature` is `0.7` and several examples depend on model judgement, so your output will differ in wording and token counts. The structure and conclusions should hold.

---

## Source

These patterns are distilled from research on agentic AI systems, made accessible through simple visual representations and clear explanations.

[Agentic Design Patterns (full book, PDF)](../books/Agentic_Design_Patterns_Complete.pdf)

## Contributing

Improvements and additional patterns are welcome. Open an issue or a pull request.

## License

[MIT](../LICENSE), so use these patterns freely in your projects.

<div align="center">
<br>
<sub>21 patterns · 21 runnable examples · 21 captured runs</sub>
</div>
