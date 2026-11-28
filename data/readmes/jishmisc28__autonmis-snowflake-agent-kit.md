# autonmis-snowflake-agent-kit

[![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen.svg)]()
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Cloud-29B5E8.svg)]()

Production-grade Snowflake integration layer for autonomous AI agents, combining **connection-pooled query streaming** with **prefix prompt cache stabilization** via [Hearth (`hearth-ai`)](https://pypi.org/project/hearth-ai/).

Directly adapted from the production data plane powering [Autonmis](https://autonmis.com) (Enterprise AI-Native Operations & Financial Reconciliation).

---

## 1. The Core Problems in Multi-Turn Snowflake Text-to-SQL

When conversational LLM agents (LangGraph, AutoGen, CrewAI, PydanticAI) query enterprise Snowflake data warehouses, two severe operational bottlenecks emerge:

```
[Agent Turn 1] --> Fetches DDL (5,000 tokens) + Timestamp --> Cold Cache Miss (100% cost)
                                                                 New Snowflake Conn Opened
[Agent Turn 2] --> Query Error Retry + New Timestamp -------> Prefix Invalidation!
                                                                 Cold Cache Miss (100% cost)
                                                                 Warehouse Concurrency Spikes
```

1. **LLM Prefix Cache Invalidation (Token Burn):**
   - Most LLM providers (Anthropic Claude 3.5, OpenAI GPT-4o, AWS Bedrock Nova) offer prompt caching discounts (up to 90% savings) **only if the byte prefix matches identically**.
   - Naive agents inject timestamps, session IDs, or non-deterministic schema DDL order at the top of the prompt. This breaks the prefix hash on every single turn, forcing repetitive multi-thousand token billing.

2. **Snowflake Concurrency & Virtual Warehouse Credit Burn:**
   - Stateless agent executors open unmanaged connections per SQL query.
   - Under multi-turn agent loops or parallel worker swarms, connection proliferation exhausts warehouse query limits, triggering auto-scaling clusters and unnecessary Snowflake credit burn.

---

## 2. Architecture: Zero-Leak Data Plane

`autonmis-snowflake-agent-kit` solves both problems simultaneously:

```
                         +-----------------------------------------------+
                         |           Autonomous Agent Reasoning Loop      |
                         +-----------------------------------------------+
                                                |
                 +------------------------------+------------------------------+
                 |                                                             |
                 v                                                             v
+---------------------------------+                       +---------------------------------+
|  SnowflakePromptCacheEngine     |                       |    SnowflakeConnectionPool      |
|  (Hearth Prefix Stabilization)  |                       |   (Cryptographic Key Hashing)   |
+---------------------------------+                       +---------------------------------+
| * Canonical Schema DDL Sorting  |                       | * SHA-256 Credential Hashing    |
| * Deterministic Prefix Hashing  |                       | * Concurrency Ceiling (Max: 10) |
| * Volatile Tail Segregation     |                       | * Zero-Heap Streaming Iteration |
|   (Timestamps/IDs at the back)  |                       |   via `statement.streamRows()`  |
+---------------------------------+                       +---------------------------------+
                 |                                                             |
                 +------------------------------+------------------------------+
                                                |
                                                v
                         +-----------------------------------------------+
                         |         Snowflake Virtual Data Warehouse       |
                         +-----------------------------------------------+
```

---

## 3. Key Capabilities

### A. Cryptographic Connection Pooling (`agent.py`)
Directly ported from Autonmis's production TypeScript executor (`snowflakeDirectExecutor.ts`):
- **SHA-256 Config Keying:** Computes deterministic SHA-256 hashes of connection configs to safely share pools across multi-tenant sessions without leaking credentials.
- **Resource Throttling:** Caps concurrent sessions per warehouse (`max: 10`), eliminating warehouse credit spikes.
- **Streaming Results:** Memory-safe streaming with backpressure handling instead of buffering massive query result sets in Node/Python heap memory.

### B. Prompt Cache Stabilization (`caching_wrapper.py`)
- **Byte-Exact Canonical Sorting:** Automatically sorts tables and columns canonically to guarantee identical prefix hashes regardless of metadata retrieval order.
- **Volatile Tail Isolation:** Dynamically captures execution context (ephemeral UUIDs, millisecond timestamps, error retry payloads) and places them strictly into the un-cached suffix.

---

## 4. Quickstart

### Installation

```bash
git clone https://github.com/jishmisc28/autonmis-snowflake-agent-kit.git
cd autonmis-snowflake-agent-kit
pip install -r requirements.txt
```

### Running the Agent

```python
from agent import AutonmisSnowflakeAgent
from caching_wrapper import SnowflakeTableSchema

# 1. Configure Snowflake Connection
config = {
    "account": "xy12345.us-east-1",
    "user": "AUTONMIS_AGENT",
    "database": "FINANCE_PROD",
    "schema": "LEDGER",
    "warehouse": "COMPUTE_WH",
}

agent = AutonmisSnowflakeAgent(snowflake_config=config)
agent.bootstrap_catalog()

# 2. Turn 1 (Establishes warm prefix cache)
turn1 = agent.run_turn("Find all un-reconciled debit transactions", session_id="session-001")
print(f"Turn 1 Cache Hit: {turn1['cache_hit']}")  # False (Cache creation)

# 3. Turn 2 (Identical prefix hash, hits provider cache)
turn2 = agent.run_turn("Group by account code and order descending", session_id="session-001")
print(f"Turn 2 Cache Hit: {turn2['cache_hit']}")  # True (Cache hit: 90% discount)
print(f"Cumulative Savings: {turn2['metrics']['cost_savings_pct']}%")
```

---

## 5. Verification & Tests

Run the built-in test suite:

```bash
python3 -m unittest discover tests
```

Output:
```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
---

## 7. License

Licensed under the Apache License, Version 2.0.
