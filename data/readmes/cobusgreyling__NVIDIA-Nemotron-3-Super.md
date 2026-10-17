# NVIDIA Nemotron 3 Super — 120B Parameters, 12B Active

**A reasoning model that lets you control how much it thinks**

![Nemotron 3 Super](images/nemotron-3-super-cover.png)

---

## In Short

NVIDIA Nemotron 3 Super is a 120B parameter Large Reasoning Model with only 12B active parameters per forward pass. It uses a Mixture-of-Experts Hybrid Mamba-Transformer architecture that delivers graduate-level reasoning while running on consumer-grade hardware.

The standout feature is **controllable reasoning**. Three modes, one model.

> Nemotron 3 Super offers an exceptional tradeoff between model accuracy and efficiency.

---

## The Architecture

![MoE Architecture](images/moe-architecture.png)

Nemotron 3 Super combines three architectural breakthroughs into a single model.

**Latent Mixture-of-Experts (MoE)** — Traditional dense models activate all parameters for every token. Nemotron 3 Super routes continuous latent representations to specialised expert networks. 120B total parameters, but only 12B active per forward pass. This drastically reduces latency and memory usage.

**Multi-Token Prediction (MTP)** — Standard LLMs predict one token at a time. Nemotron 3 Super predicts multiple future tokens simultaneously in a single forward pass. This results in significantly higher tokens-per-second throughput and allows the model to better plan its reasoning trajectories.

**NVFP4 Pretraining** — The model was pre-trained using NVIDIA's 4-bit floating-point format. This doubles training throughput and reduces memory bandwidth bottlenecks compared to standard 8-bit formats. Larger dataset, richer training, no loss of gradient precision.

The hybrid Mamba-Transformer design combines:

- **Mamba layers** for efficient linear-time sequence modelling over long contexts
- **Transformer layers** for strong attention-based reasoning on complex tasks
- **MoE routing** for dynamic expert selection based on specialised knowledge

---

## Three Reasoning Modes

The model's reasoning depth is controlled via `chat_template_kwargs`. One model, three distinct behaviours.

| Mode | Parameter | Behaviour |
|------|-----------|-----------|
| **Reasoning ON** | `enable_thinking: True` | Full Large Reasoning Model. Emits thinking tokens in extended chains of thought before the final answer |
| **Reasoning OFF** | `enable_thinking: False` | Direct response. No thinking tokens. Lower latency, trades reasoning depth for speed |
| **Low Effort** | `low_effort: True` | Reduced reasoning tokens. Faster than full reasoning, more depth than reasoning off |

You can also set a `reasoning_budget` to precisely control how many thinking tokens the model generates.

```python
extra_body = {
    "reasoning_budget": 8192,
    "chat_template_kwargs": {"enable_thinking": True}
}
```

This gives fine-grained control over the tradeoff between reasoning depth and response latency.

---

## How It Looks in Practice

With **reasoning ON**, the model thinks before answering. The reasoning tokens stream first (visible in green in the notebook), followed by the final response.

Ask it "What is 2+2?" and you get a chain of thought:

> *Okay, the user asked "What is 2+2?" That's a super basic math question... The answer is definitely 4. But wait, could there be a trick? Like in some contexts (binary, modular arithmetic)? Nah, the question is phrased plainly...*

Then the clean answer:

> The answer to **2 + 2** is **4**.

With **low effort mode**, the same model produces:

> *User asks what is NVIDIA. Provide concise answer.*

Then immediately delivers a direct response. Minimal thinking overhead, fast output.

With **reasoning OFF**, no thinking tokens at all. Just the answer.

---

## Tool Calling

Nemotron 3 Super supports OpenAI-compatible function calling with streaming. The model reasons about which tool to use, emits `tool_calls` deltas with the function name and arguments, executes locally, then produces the final answer from the tool result.

```
[reasoning]  We need to compute 123+456. Use the get_math_answer tool.
[tool#0 name] get_math_answer
[tool#0 args] {"expression": "123+456"}
  get_math_answer({'expression': '123+456'}) -> 579

[reasoning]  The tool returned 579. Output just 579.
579
```

The full flow — reasoning, tool selection, execution, final answer — streams in a single interaction.

---

## API Access

Nemotron 3 Super uses the NVIDIA NIM endpoint with the OpenAI-compatible API.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY"),
)

completion = client.chat.completions.create(
    model="private/nvidia/nemotron-3-super-120b-a12b",
    messages=[{"role": "user", "content": "hello"}],
    temperature=1.0,
    top_p=0.95,
    max_tokens=8192,
    stream=True,
    extra_body={
        "chat_template_kwargs": {"enable_thinking": True}
    },
)
```

Recommended settings: `temperature=1.0`, `top_p=0.95` for all modes.

---

## Notebook Results

All cells tested successfully against the live API:

| Cell | Mode | Result | Time |
|------|------|--------|------|
| 3 | Reasoning ON | Thinking tokens (green) → answer "2+2=4" | 1.4s |
| 5 | Low Effort | Minimal thinking → concise NVIDIA description | 2.6s |
| 6 | Tool Calling | Reasoning → `get_math_answer(123+456)` → 579 | 2.9s |
| 7 | Reasoning OFF | No thinking tokens, direct quantum computing answer | 1.6s |

The [walkthrough notebook](nemotron_3_super_walkthrough.ipynb) in this repo demonstrates all features:

1. **Reasoning ON** — full chain-of-thought with streaming
2. **Reasoning ON with budget** — controlled reasoning depth
3. **Low Effort** — fast responses with minimal thinking
4. **Tool calling** — function calling with streaming + reasoning
5. **Reasoning OFF** — direct response, no thinking tokens
6. **Side-by-side comparison** — same prompt across all three modes with timing

---

## The Bigger Picture

The controllable reasoning mechanism is what makes Nemotron 3 Super interesting from an application design perspective. You do not need to choose between a fast model and a reasoning model. One model handles both.

For simple queries, turn reasoning off. For complex multi-step problems, turn it on with a generous budget. For everything in between, low effort mode finds the middle ground.

The MoE architecture means you get 120B parameters of knowledge with 12B parameters of compute cost. The Mamba layers handle long contexts efficiently. The Transformer layers handle complex reasoning. The routing layer decides which experts to activate per token.

> Intelligence is in the routing, not just the weights.

---

## Reasoning Budget Sweep

**How much thinking does a model actually need?**

The [`budget-sweep/`](budget-sweep/) directory contains an experiment that runs a fixed math olympiad problem at seven reasoning budgets (256, 512, 1024, 2048, 4096, 8192, 16384) and measures reasoning tokens, content tokens, and latency.

Key findings:
- All 7 budgets produced the **correct answer**
- Reasoning tokens scale with budget, but the model does not fill the full budget
- Content tokens **decrease** as reasoning increases — the model writes less when it thinks more
- The **sweet spot is ~1024** tokens for multi-step math
- Latency grows **4x** from budget 256 (10.7s) to 16384 (44.7s)

| Budget | Reasoning | Content | Time |
|--------|-----------|---------|------|
| 256 | 123 | 156 | 10.7s |
| 512 | 229 | 196 | 16.9s |
| 1024 | 355 | 206 | 22.8s |
| 2048 | 400 | 235 | 29.2s |
| 4096 | 551 | 186 | 23.2s |
| 8192 | 508 | 161 | 37.0s |
| 16384 | 801 | 137 | 44.7s |

**Contents:**
- [`budget-sweep/blog.md`](budget-sweep/blog.md) — Full write-up with analysis
- [`budget-sweep/app.py`](budget-sweep/app.py) — Gradio visual demo (port 7866)
- [`budget-sweep/run_sweep.py`](budget-sweep/run_sweep.py) — Experiment script
- [`budget-sweep/results.json`](budget-sweep/results.json) — Raw results with full reasoning traces

> Set the budget to match the problem, not the model's maximum.

---

## Adaptive Reasoning Router

**One model, three modes, zero manual switching.**

The [`adaptive-router/`](adaptive-router/) directory contains a query classifier that automatically selects the right reasoning mode and budget per query. No user-facing toggles.

The router classifies incoming queries into five categories:

| Category | Reasoning Mode | Budget | Typical queries |
|----------|---------------|--------|-----------------|
| Simple Fact | OFF | — | Definitions, capitals, dates |
| Moderate | Low Effort | — | Summaries, comparisons, short explanations |
| Multi-Step | ON | 2048 | Word problems, multi-part questions |
| Code Generation | ON | 4096 | Write functions, debug, algorithms |
| Complex Reasoning | ON | 8192 | Proofs, optimisation, formal derivations |

Classification is rule-based (no LLM call required) using signal words, question structure, and code markers.

**Contents:**
- [`adaptive-router/blog.md`](adaptive-router/blog.md) — Full write-up on the design pattern
- [`adaptive-router/app.py`](adaptive-router/app.py) — Gradio demo with live classification (port 7867)
- [`adaptive-router/feedback.py`](adaptive-router/feedback.py) — Router learning loop with user corrections

> The smartest model is the one that knows how hard to think.

---

## FastAPI Server

A REST API server that exposes Nemotron 3 Super via OpenAI-compatible endpoints with SSE streaming support.

```bash
python api_server.py
# Server runs on http://localhost:8000
```

**Endpoints:**

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/models` | List available models |
| POST | `/v1/chat` | Single chat completion (any reasoning mode) |
| POST | `/v1/chat/stream` | Streaming chat via Server-Sent Events |
| POST | `/v1/compare` | Run the same prompt across all 3 reasoning modes |

```bash
curl -X POST http://localhost:8000/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain TCP vs UDP", "reasoning_mode": "ON", "reasoning_budget": 4096}'
```

---

## Tool Calling Demo

Interactive Gradio demo showing function calling with reasoning trace. The model reasons about which tool to use, streams `tool_calls`, executes them locally, then produces the final answer.

Three built-in tools:
- **calculate** — evaluate math expressions (safe eval with `sqrt`, `sin`, `cos`, `log`)
- **get_weather** — simulated weather data for major cities
- **search_knowledge** — search a built-in knowledge base about Nemotron architecture

```bash
cd tool-calling && python app.py
# Runs on http://localhost:7865
```

The UI shows the full execution trace: reasoning → tool call → result → final answer.

---

## Model Comparison

Side-by-side comparison of the same prompt across different NIM models.

| Model | ID |
|-------|----|
| Nemotron 3 Super (120B/12B) | `private/nvidia/nemotron-3-super-120b-a12b` |
| Nemotron Super 49B | `nvidia/nemotron-super-49b-v1` |
| Llama 3.3 70B | `meta/llama-3.3-70b-instruct` |
| Llama 3.1 8B | `meta/llama-3.1-8b-instruct` |
| Mistral Large 2 | `mistralai/mistral-large-2-instruct` |

```bash
cd model-comparison && python app.py
# Runs on http://localhost:7868
```

Select two models, enter a prompt, and compare reasoning tokens, content tokens, and latency side by side.

---

## Batch Benchmark

CLI tool that runs a prompt suite across all three reasoning modes and generates structured reports.

```bash
python batch_benchmark.py
python batch_benchmark.py --prompts custom_prompts.json --output results/
```

Default suite: 8 prompts × 3 modes = 24 API calls. Categories: Simple, Moderate, Multi-Step, Code, Complex.

Outputs:
- **JSON report** with full reasoning traces and token counts
- **Markdown summary** table with reasoning/content/time per prompt per mode

---

## System Prompt Library

Pre-built prompt templates for different use cases. 12 templates included:

| Key | Name | Suggested Mode |
|-----|------|---------------|
| `default` | Default Assistant | ON |
| `coder` | Senior Developer | ON |
| `analyst` | Data Analyst | ON |
| `concise` | Concise Responder | OFF |
| `teacher` | Patient Teacher | ON |
| `creative` | Creative Writer | Low Effort |
| `reviewer` | Code Reviewer | ON |
| `debugger` | Debugging Expert | ON |
| `architect` | System Architect | ON |
| `interviewer` | Technical Interviewer | Low Effort |
| `summarizer` | Summarizer | OFF |
| `researcher` | Research Assistant | ON |

```python
from system_prompts import get_prompt_text, list_prompts
prompt = get_prompt_text("coder")
```

---

## CLI Tool

Run Nemotron 3 Super from the command line. No UI required.

```bash
# Basic usage
python cli.py "What is the capital of France?"

# Full reasoning with custom budget
python cli.py --mode on --budget 4096 "Prove sqrt(2) is irrational"

# Low effort mode
python cli.py --mode low-effort "Explain TCP vs UDP"

# JSON output (includes reasoning, tokens, cost)
python cli.py --json "Write a Python sort function"

# Batch processing
python cli.py --batch prompts.txt --json > results.json

# Custom system prompt
python cli.py --system "You are a math tutor" "Solve x^2 + 5x + 6 = 0"
```

Features:
- Streaming output with green reasoning traces (ANSI colours)
- Token counting and cost estimation
- Automatic retries with exponential backoff
- Batch mode for processing multiple prompts
- JSON output for piping to other tools

---

## Mode Comparison

Side-by-side comparison of all three reasoning modes on the same prompt.

```bash
python comparison.py   # port 7869
```

Sends the same query through Reasoning ON, Low Effort, and Reasoning OFF simultaneously. Displays results in three columns with token counts, latency, and cost for each mode.

---

## Multi-Problem Budget Sweep

The original budget sweep used a single math problem. The expanded sweep tests across 6 diverse problem categories.

```bash
# Run all 6 problems across 7 budgets
python budget-sweep/run_multi_sweep.py

# Run a single problem
python budget-sweep/run_multi_sweep.py --problem code
```

Problem categories: math (hard), code (medium), logic (medium), factual (easy), creative (medium), proof (hard).

Answers the question: **Does the sweet spot change by problem type?**

---

## Prompt Templates

Pre-built templates with optimised mode and budget presets.

```
templates/prompts.json — 8 templates:
├── code-review        → ON, budget 4096
├── math-tutor         → ON, budget 8192
├── doc-writer         → Low Effort
├── quick-answer       → OFF
├── debug-helper       → ON, budget 4096
├── explain-concept    → Low Effort
├── security-audit     → ON, budget 8192
└── data-analysis      → ON, budget 4096
```

Each template includes a system prompt, a parameterised template string, and recommended reasoning settings.

---

## Conversation Persistence

Chat history saved to SQLite. Sessions survive page reloads. Export to JSON or Markdown.

```python
from persistence import ChatDB

db = ChatDB()
conv_id = db.create_conversation("Debug session")
db.save_message(conv_id, "user", "Why is my code slow?")
db.save_message(conv_id, "assistant", "...", reasoning_tokens=450, content_tokens=120, elapsed=8.2)

# Export
print(db.export_conversation(conv_id, format="markdown"))

# Usage stats
stats = db.get_usage_stats()
# → total_conversations, total_tokens, total_cost, avg_response_time
```

---

## Conversation Export

Save and load chat histories in JSON or Markdown format.

```python
from conversation_export import Conversation

conv = Conversation(title="My Chat", model="nemotron-3-super")
conv.add_message("user", "Hello")
conv.add_message("assistant", "Hi!", reasoning="User greeted me", mode="ON")

conv.save("conversations", fmt="json")
conv.save("conversations", fmt="markdown")
```

Supports `from_gradio_history()` for direct integration with the Gradio chat demos.

---

## Shared Module

Common code extracted into `shared/` to eliminate duplication across all Gradio apps:

- **`shared/theme.py`** — NVIDIA dark theme and base CSS
- **`shared/client.py`** — Centralized OpenAI client with `.env` support
- **`shared/helpers.py`** — `esc()`, `approx_token_count()`, `format_reasoning_html()`, `build_extra_body()`, and more

All new demos import from `shared/` instead of duplicating theme and helper code.

---

## Docker

Run the full suite with Docker Compose:

```bash
cp .env.example .env
# Edit .env with your NVIDIA_API_KEY

docker compose up
```

| Service | Port | Description |
|---------|------|-------------|
| chat | 7864 | Main chat demo |
| api | 8000 | FastAPI REST server |
| tool-calling | 7865 | Tool calling demo |
| budget-sweep | 7866 | Budget sweep visualizer |
| adaptive-router | 7867 | Adaptive reasoning router |

Or build and run individually:

```bash
docker build -t nemotron-demo .
docker run -e NVIDIA_API_KEY=nvapi-xxx -p 7864:7864 nemotron-demo python app.py
```

---

## Token Efficiency Dashboard

Analytics dashboard showing historical usage patterns.

```bash
python dashboard.py   # port 7868
```

- Usage overview: total conversations, messages, tokens, cost
- Token distribution: reasoning vs content ratio per conversation
- Cost tracker: per-conversation breakdown
- Mode distribution: ON vs Low Effort vs OFF usage frequency
- Trends: last 20 responses with colour-coded metrics

---

## Router Learning Loop

The adaptive router now accepts user feedback. When the classifier gets it wrong, users can correct it. Corrections are stored and analysed to suggest weight adjustments.

```python
from adaptive_router.feedback import RouterFeedback

fb = RouterFeedback()
fb.record_feedback("Compare Python and Go", classified_category="code", correct_category="moderate")

print(fb.get_accuracy())           # Overall and per-category accuracy
print(fb.get_confusion_matrix())   # Misclassification patterns
print(fb.suggest_weight_adjustments())  # Which categories need tuning
```

---

## Retry & Resilience

All API calls use the resilience layer with:
- Exponential backoff with jitter (1s, 2s, 4s, 8s...)
- Catches rate limits, timeouts, connection errors, server errors
- Rate limit header detection
- Cost estimation

```python
from resilience import resilient_client, estimate_cost

client = resilient_client(base_url, api_key, max_retries=3)
cost = estimate_cost(input_tokens=1000, output_tokens=500)
# → $0.0045
```

---

## Tests & CI

```bash
# Run all tests
python -m pytest tests/ -v

# Tests cover:
# - Adaptive router classifier (20 tests)
# - Resilience module (5 tests)
# - Persistence layer (8 tests)
```

GitHub Actions runs tests on every push and PR to main.

---

## Project Structure

```
nemotron-3-super/
├── app.py                          ← Interactive chat UI (port 7864)
├── cli.py                          ← Headless CLI tool
├── comparison.py                   ← Side-by-side mode comparison (port 7869)
├── dashboard.py                    ← Token efficiency dashboard (port 7868)
├── persistence.py                  ← SQLite conversation storage
├── resilience.py                   ← Retry & cost estimation
├── blog.md                         ← Main blog post
├── nemotron_3_super_walkthrough.ipynb  ← Jupyter notebook
├── budget-sweep/
│   ├── app.py                      ← Visual demo (port 7866)
│   ├── blog.md
│   ├── run_sweep.py                ← Single-problem sweep
│   ├── run_multi_sweep.py          ← Multi-problem sweep
│   ├── problems.json               ← 6 diverse test problems
│   └── results.json                ← Pre-computed results
├── adaptive-router/
│   ├── app.py                      ← Adaptive routing demo (port 7867)
│   ├── blog.md
│   └── feedback.py                 ← Router learning loop
├── templates/
│   └── prompts.json                ← 8 prompt templates
├── tests/
│   ├── test_classifier.py          ← Router tests (20)
│   ├── test_resilience.py          ← Resilience tests (5)
│   └── test_persistence.py         ← Persistence tests (8)
├── images/                         ← Visual assets
└── .github/workflows/test.yml      ← CI pipeline
```

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/cobusgreyling/NVIDIA-Nemotron-3-Super.git
cd NVIDIA-Nemotron-3-Super

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
cp .env.example .env
# Edit .env with your NVIDIA_API_KEY

# 4. Run any demo
python app.py                    # Main chat (port 7864)
python cli.py "Hello"            # CLI tool
python comparison.py             # Mode comparison (port 7869)
python dashboard.py              # Token dashboard (port 7868)
python api_server.py             # REST API (port 8000)
cd tool-calling && python app.py # Tool calling (port 7865)
```

---

## Author

Cobus Greyling
