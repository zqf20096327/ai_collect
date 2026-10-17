# Handoffs in Multi-Agent Systems with LangGraph

A practical demo of multi-agent routing patterns using LangGraph, comparing **Command-based routing** vs **Conditional edge routing**.

Read the article here: https://towardsdatascience.com/how-agent-handoffs-work-in-multi-agent-systems/

## The Scenario

This project implements a **Singapore real estate assistant** as a multi-agent system:

- **Supervisor Agent**: Routes user queries to the appropriate specialist
- **Transaction History Agent**: Handles market data, sales history, and transaction trends
- **Property Profile Agent**: Provides detailed property information and specifications

The supervisor decides which agent should handle each query—demonstrating how handoffs work in multi-agent systems.

## Two Routing Approaches

| Feature | Command-based | Conditional Edges |
|---------|--------------|-------------------|
| **State Updates** | ✅ Yes (via `Command.update`) | ❌ No (message-only) |
| **Routing** | Dynamic via `Command.goto` | Pre-defined via `add_conditional_edges` |
| **Use Case** | Routing + state management | Pure routing |

- **Command-based** (`run_command_routing.py`): Combines routing AND state updates. Extracts context (e.g., property names) and passes to agents via state.
- **Conditional Edge** (`run_conditional_routing.py`): Pure routing based on message content. No state updates.

## Quick Start

```bash
# Install
pip install -r requirements.txt
pip install -e .

# Set API key
export OPENAI_API_KEY='your-key-here'  # pragma: allowlist secret

# Run examples
python run_command_routing.py "Tell me about 38 Oxley Road"
python run_conditional_routing.py "Describe the 38 Oxley Road property"
```
