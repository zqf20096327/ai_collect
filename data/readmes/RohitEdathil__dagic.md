# Dagic

**Typed, concurrent tool composition for LLM agents.**

Dagic is a tiny workflow language and an async execution engine that lets an LLM
compose registered tools into a **typed DAG**, instead of calling them one at a time.


It sits between traditional tool calling and full code execution: the model writes a
short program that pipes results directly between tools and runs independent branches
concurrently — without the host ever having to sandbox and execute arbitrary
model-generated code.

## Why

LLMs are good at deciding *what* should happen next, but plain tool calling makes them
responsible for shuttling every intermediate value back through the model, one call at
a time:

```
search(A) → result
search(B) → result
combine(A, B) → result
summarize(result)
```

Each arrow above is a full model round-trip, even though the model already knows the
shape of the pipeline.

The usual fix is code execution — let the model write:

```python
a = search("A")
b = search("B")
result = combine(a, b)
summarize(result)
```

That solves composition, but now the host is running arbitrary generated code, which
means sandboxing, a runtime, and a much bigger attack surface.

Dagic is the middle ground. The model writes:

```
a = search("A");
b = search("B");

result = combine(a, b);

summarize(result);
```

Dagic parses it, type-checks it, builds the DAG, and executes it — independent
branches run concurrently, and only functions the host explicitly registered can ever
be called. No arbitrary code, no manual dependency wiring.

> **Let the model describe the graph. Let the host control what can execute.**

## Results

Two experiments, both in [`experiments/`](experiments), comparing a Dagic-based agent
against a normal one-tool-per-call LangGraph agent.

### Efficiency benchmark

A math agent solves 5 JEE-Mains-level problems, run 5 times each, comparing a single
`run_dagic` tool against one LangChain tool per math operation (`add`, `multiply`,
`sqrt`, ...). Model: `deepseek-v4-flash`.

| Metric | Dagic | Per-call tools |
|---|---|---|
| Accuracy (5 runs) | 5/5 (100%) | 5/5 (100%) |
| Avg total tokens | ~33.8k | ~248.1k |
| Avg latency / problem | ~25.8s | ~82.5s |
| Avg est. cost | ~$0.0043 | ~$0.0153 |

Same accuracy, but Dagic used **~7x fewer tokens**, ran **~3x faster**, and cost
**~3.6x less**, on average. It was also far more *stable* run-to-run — per-call tools
ranged from 31s–159s and 75k–578k tokens across the 5 runs, while Dagic stayed in a
tight 17s–35s / 28k–40k band. Full per-run numbers are in the
[experiment README](experiments/efficiency/README.md).

*Caveat: the per-call baseline isn't maximally optimized — you could
hand-write a small expression parser for this specific problem to close some of the
gap. That's intentionally not done as the point here is that an agent whose tool calls naturally chain together gets faster
and cheaper for free when you let it express that chaining, instead of forcing every
intermediate value through another model turn.*

### Real task: no code execution environment needed

A harder test: *"Find the date of birth of all the actors from Avengers: Infinity
War"* — a multi-page scrape, parse, and aggregation job, the kind of thing you'd
normally reach for a code execution sandbox to do. One `web_scraper` agent, model
`kimi-k3`.

- **Succeeded**: correct DOB table for all 19 top-billed cast members (e.g. Robert
  Downey Jr. 1965-04-04, Chris Hemsworth 1983-08-11), and the agent explicitly noted
  it had left out the wider supporting cast instead of fabricating entries for them.
- ~54.9k tokens (15 model calls, 14 tool calls), ~69s wall time, ~$0.10 at kimi-k3
  rates.

A major observation from that trace is that the agent kept assuming it was writing Python and
tried invalid syntax more than once, wasting turns; Also a loop construct in Dagic would
likely cut that down further; and smaller/cheaper models struggled enough that a
larger model was needed to get a clean run. Full trace and notes in
[`experiments/real_tasks`](experiments/real_tasks).

## What Dagic provides

- **Composition** — chain multiple tools into a single workflow.
- **Parallelism** — independent branches execute concurrently, automatically.
- **Static type checking** — incompatible tool arguments are rejected before
  execution, not mid-run.
- **Controlled execution** — only functions the host registers can be called. No
  arbitrary code.
- **Tiny language** — deliberately limited to what's needed to express a DAG.
- **Async execution** — built on Python's `asyncio`.

## Installation

Requires Python 3.10+.

```
pip install dagic
```

## Syntax

A Dagic program is just assignments and function calls:

```
result = add(create("1"), create("2"));

store(result);
```

Slightly more interesting:

```
a = fetch("A");
b = fetch("B");

combined = combine(a, b);

store(combined);
```

The graph is implicit in the data flow:

```
fetch("A") ──┐
              ├── combine ── store
fetch("B") ──┘
```

- Functions are nodes.
- Function arguments are edges.
- Assignments name intermediate values.
- Calls returning `None` are terminal nodes.
- Independent branches execute concurrently — no explicit parallel syntax needed.

## Types

Dagic type-checks the program at compile time, before anything runs.

Two built-in types:
- **Strings** — `"Hello, World!"`
- **Arrays** — `["Hello", "World!"]`

Every other type comes from the host. If a function expects a `float`:

```python
def add(a: float, b: float) -> float:
    return a + b
```

then passing anything else is rejected before execution — including array element
types (`List[float]` and `List[int]` are distinct).

This makes a Dagic program a **verifiable execution plan**, not an unchecked sequence
of tool calls.

## Defining tools

Tools are plain Python functions, registered with a `Module`:

```python
from dagic import Module

math = Module(name="math", desc="Basic arithmetic.")


@math.register
def create(value: str) -> float:
    """Create a float from a string."""
    return float(value)


@math.register
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
```

Registered functions must:
- annotate every parameter and the return value
- have no `*args` / `**kwargs`
- have no default or keyword-only parameters

Functions returning `None` are terminals; everything else produces a value that
downstream calls can consume.

## Execution

```
Source → Parse → Type-check → Build DAG → Execute concurrently
```

Execution starts at terminal nodes and resolves dependencies backwards. In the
`fetch`/`combine`/`store` example above, the two `fetch` calls have no dependency on
each other, so they run concurrently while `combine` waits on both.

A program needs at least one terminal node; unused named subgraphs are rejected at
compile time.

## Built-in modules

A small `float_math` module ships with the package: `create`, `add`, `subtract`,
`multiply`, `divide`, `power`, `modulus`, `floor_divide`, `absolute`, `negate`. It
composes with your own modules directly:

```python
import asyncio
from dagic import Dagic, Module
from dagic.builtins import float_math

sink = []
io = Module(name="io", desc="I/O helpers.")


@io.register
def store(value: float) -> None:
    sink.append(value)


async def main():
    dagic = Dagic([float_math.float_math, io])
    await dagic.run('result = add(create("1"), create("2")); store(result);')
    print(sink)  # [3.0]


asyncio.run(main())
```

`Dagic.run()` compiles the source against the registered modules, builds the DAG, and
executes it — all async.

## Dagic vs. the alternatives

| | Tool calling | Dagic | Code execution |
|---|---|---|---|
| Multi-step composition | Limited | ✓ | ✓ |
| Parallel execution | Agent-managed | ✓ | ✓ |
| Static type checking | Usually limited | ✓ | Depends |
| Arbitrary code execution | ✗ | ✗ | ✓ |
| Host-controlled operations | ✓ | ✓ | Harder |

Dagic isn't trying to replace general-purpose workflow engines or full code execution.
It's aimed at a narrower question:

> How can an LLM compose multiple *trusted* operations into a single, verifiable,
> concurrent workflow — without the host needing to run arbitrary code?

## Examples

See [`examples/`](examples) for the math agent and web-scraper agent used in the
experiments above.

## Development

```
make test    # run the test suite
make format  # format with ruff
```

## License

MIT.