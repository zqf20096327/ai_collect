# Agent Tool Result Reducer: Fit Large JSON Tool Results into an LLM Agent's Context Window

[![CI](https://github.com/AryabhattaLabs/agent-tool-result-reducer/actions/workflows/ci.yml/badge.svg)](https://github.com/AryabhattaLabs/agent-tool-result-reducer/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/agent-tool-result-reducer)](https://pypi.org/project/agent-tool-result-reducer/)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Shrink large JSON tool results for LLM agents **without silently losing data**.

**Package:** `agent-tool-result-reducer` · **Import:** `tool_result_reducer`

A zero-dependency Python library that fits an API/tool response into a
character budget by **selecting fields, dropping the widest fields, and cutting
only on whole-item boundaries** — and that always tells the model, in a
`_meta` block, exactly what it did and did not receive.

```text
Before:  [{"id":1,"name":"Acme","description":"…"},{"id":2,"name":"content delivery networ      ← cut mid-object
After:   {"items":[…25 whole items…],"_meta":{"items_included":25,"items_available":25,
          "total_reported_by_source":443,"fields_dropped":{"description":3617},…}}
```

---

## Install

```bash
pip install agent-tool-result-reducer
```

Requires Python 3.10+. No runtime dependencies.

## Quick start

```python
from tool_result_reducer import reduce_tool_result

rows = [{"id": i, "name": f"Company {i}", "description": "long text " * 400} for i in range(25)]
response = {"results": rows, "total": 443}        # a page of 25 companies, about 100,000 characters

result = reduce_tool_result(response, "crm.search", budget=4_000)

result.text        # 1,506 characters of valid JSON: this is what goes to the model
result.complete    # True: all 25 items are there; the wide `description` field was dropped
result.summary("crm.search")
# crm.search: complete, agent received 25 of 25 items (source reports 443 in total), dropped fields: description
```

The model is told what happened, in the result itself:

```json
"_meta": {"items_included": 25, "items_available": 25, "complete": true,
          "total_reported_by_source": 443,
          "total_note": "`complete` covers this response only. The source reports 443 in total; ...",
          "fields_dropped": {"description": 4017}, ...}
```

More in [Usage](#usage) and [Examples](#examples).

## Objective

Give agent builders a drop-in function that sits between **"tool returned
something"** and **"append it to the model's context"**, so that:

1. A result fits the budget you set, short of cutting a single item in half
   (cost and context-window control).
2. What the model receives is **always valid JSON** made of **whole items**.
3. When anything is left out, the model is **told explicitly**, with counts and
   a concrete way to get the rest — so it cannot report a partial result as
   complete.

## The problem

Every tool result is re-sent to the model on every later turn of an agent
loop, so large results are expensive and frameworks cap them. The usual cap
is "keep the first N characters". That causes a quiet, serious failure:

> In production, a search API returned **11 companies in 77,539 characters**.
> A 12,000-character cap kept the start and cut mid-object
> (`…"name": "content delivery networ`). The model parsed the **2** whole
> records it could see, wrote 2 rows to a spreadsheet, and **reported
> success**. Nothing indicated that 9 records had been dropped.

The cap bounded *bytes*. What matters is *what the agent consumes*: with only
the 14 fields the task needed, all 11 records fit the same budget several
times over.

## How it works

For each tool result, in order:

| Step | What happens | Why |
|---|---|---|
| 1. Pass-through | Under budget and no `select` → returned unchanged. | Zero overhead for the common case. |
| 2. Locate the collection | Finds the main list of objects in the envelope (`data`, `items`, `results`, `content`, … up to 3 levels deep; longest list wins; JSON:API `data` beats `included`). Reads server totals (`total`, `totalElements`, `count`, `page.totalElements`, …). A page `size` is not read as a total. | Works with real-world API shapes without configuration, and lets the note say "25 of 443". |
| 3. Project (`select`) | Keeps only the dot-paths requested (`id,summary.name`). Applied whenever given, not just when oversized. | Pay only for the fields you use, on every turn. |
| 4. Guard the select | A select that matches **no** field on any item is discarded (full items shown, plus the list of valid paths). When only some selected paths are found on no item, they stay `null` (a stable shape; APIs often omit empty fields) and are listed in `_meta.select_not_found` with the valid paths. A select written against the envelope (`items.id`) is repaired automatically. A field that exists but is `null` still counts as a match. | A wrong select must never produce an empty result labelled "complete", and a misspelt field must not pass silently as `null`, which reads as "value unknown". |
| 5. Auto-fit fields | Still too big → drop the **widest fields across all items** (measured, deterministic) until every item fits, down to a floor of 2 fields. | The model can't see the budget; dropping a known-expensive field beats making it guess through extra LLM turns. |
| 6. Cut on item boundaries | Still too big → keep as many **whole** items as fit. | Never broken JSON, never half a record. |
| 7. Annotate | Wrap in `{"items": [...], "_meta": {...}}` with counts, source totals, dropped fields with per-item cost, the top 3 most expensive fields, and an explicit warning when incomplete. The source's pagination fields go in `_meta.source_paging` only when every item of the page is included: values in the envelope (never in the items) whose names contain a paging word such as cursor, next, page, offset, after, more or done (`next_cursor`, `response_metadata.next_cursor`, `paging.next.after`, `pageInfo.endCursor`, `nextRecordsUrl`, …). | The model, your logs and your UI all see the same truth. A cursor points past the whole page, so following it from a partial page would skip the items left out. |
| Fallbacks | A large single object → **structure outline** (every key visible, long strings cut, nested containers summarised; still valid JSON). Non-JSON text → character cut with a clear marker. | Even non-collections degrade honestly. |

## Usage

```python
from tool_result_reducer import reduce_tool_result

raw = call_my_tool(**args)                       # dict, list or JSON string
result = reduce_tool_result(raw, "crm.search", select=args.get("select"), budget=12_000)

messages.append({"role": "tool", "content": result.text})   # goes to the model
store_full_payload(result.raw)                               # keep the original elsewhere
logger.info("tool_result_reduced", extra=result.log_fields())
if not result.complete:
    ui.warn(result.summary("crm.search"))
    # "crm.search: INCOMPLETE, agent received 7 of 25 items (source reports 443 in total)"
```

Let the model choose fields by adding an optional `select` parameter to your
tool schema, for example:

```json
"select": {
  "type": "string",
  "description": "Comma-separated dot-paths to keep from each item, e.g. id,summary.name. Omit to get all fields."
}
```

### Customising what the model is told

The text written into `_meta` is part of the agent's prompt. Defaults only
assume the model can call the tool again with `select`. If your runtime can
do better — e.g. answer a re-select from the cached response, or expose a
tool that queries the stored full payload — say so:

```python
from tool_result_reducer import Messages, reduce_tool_result

msgs = Messages(
    incomplete=(
        "You did NOT receive all items. Call this tool again with the same "
        "arguments plus `select=`; that is served from cache at no cost. "
        "Or call query_payload(ref) to read any part of the full response."
    ),
)
result = reduce_tool_result(raw, "crm.search", messages=msgs)
```

### API

| Name | Purpose |
|---|---|
| `reduce_tool_result(payload, tool_name="tool", *, select=None, budget=12000, max_overshoot=0, messages=Messages())` | Main entry point. Returns `ReducedResult`. |
| `ReducedResult` | `.text` (for the model), `.raw` (original), `.complete`, `.items_included`, `.items_available`, `.total_reported`, `.fields_dropped`, `.select_error`, `.select_not_found`, `.outlined`, `.fallback_char_cut`, `.paging` (the source's pagination fields, even when withheld from the model), `.summary()`, `.log_fields()` |
| `Messages` | Model-facing text templates (`incomplete`, `fields_dropped`, `more_at_source`, `select_not_found`, `paging`, `outline`, `char_cut`). |
| `parse_select`, `project`, `available_paths_for`, `projection_matched_nothing`, `paths_not_found`, `repair_envelope_prefix` | The building blocks, exposed for callers that project data outside an agent loop (e.g. ETL steps). |
| `locate_collection(parsed)` | Finds the main list in an API response. Returns `(items, path, total_reported)`. |
| `resolve(item, path)`, `MISSING` | Reads a dot-path from one item. Returns `MISSING` when the path is absent, and `None` when it exists and is null. |
| `available_paths(item, depth=2)` | The dot-paths that can be selected on one item. |

## Examples

Each agent-loop example runs the same task against a stand-in search tool
([`examples/demo_tool.py`](https://github.com/AryabhattaLabs/agent-tool-result-reducer/blob/main/examples/demo_tool.py)) whose result is about
108,000 characters. The reducer is a one-line change in each: the model gets
all 30 companies in about 5,600 characters, told which fields were dropped.

| File | Where the reducer goes | Install |
|---|---|---|
| [`basic.py`](https://github.com/AryabhattaLabs/agent-tool-result-reducer/blob/main/examples/basic.py) | No model: what the reducer does to a payload | nothing else |
| [`openai_tool_loop.py`](https://github.com/AryabhattaLabs/agent-tool-result-reducer/blob/main/examples/openai_tool_loop.py) | Before the `function_call_output` item, in a Responses API loop | `openai` |
| [`anthropic_tool_loop.py`](https://github.com/AryabhattaLabs/agent-tool-result-reducer/blob/main/examples/anthropic_tool_loop.py) | Before the `tool_result` block, in a Messages API loop | `anthropic` |
| [`langchain_tool.py`](https://github.com/AryabhattaLabs/agent-tool-result-reducer/blob/main/examples/langchain_tool.py) | Inside the `@tool` function, so any LangChain agent gets the reduced text | `langchain langchain-openai` |

```bash
pip install agent-tool-result-reducer openai
export OPENAI_API_KEY=...
python examples/openai_tool_loop.py
```

## Scope

**In scope**
- JSON (or JSON-serialisable) tool/API results: lists, paginated envelopes,
  JSON:API, large single objects.
- Character budgets (a proxy for tokens that needs no tokenizer).
- Deterministic, explainable reduction with model-facing and human-facing
  accounting.

**Out of scope (non-goals)**
- **Summarising with an LLM.** This is deterministic and free; run an LLM
  summariser afterwards if you want one.
- **Storing payloads or serving follow-up queries.** The library returns
  `.raw`; caching and a "query the full payload" tool belong to your runtime.
- **Token-exact budgets.** Characters are used deliberately; convert
  with your tokenizer's ratio if needed.
- **Framework adapters** in the core package. The OpenAI, Anthropic and
  LangChain [examples](#examples) show the one line each needs; the package
  stays free of dependencies.
- Non-JSON formats (XML, CSV, HTML) beyond the plain character fallback.

## Design decisions

- **Fields before items.** Twenty-five items with fewer fields lets the model
  make one informed follow-up; twenty items with all fields forces it to guess
  what it's missing.
- **Existence, not value.** `null` is an answer; a missing path is a mistake,
  so a selected path found on no item is reported, not passed silently as `null`.
- **The budget is strict by default.** At least one item is always kept, so
  the budget is exceeded only when the first item alone does not fit. A
  bounded cut of one record would be worse than a slightly larger whole one.
- **You can allow a small overshoot.** The size of the `_meta` block is
  estimated while filling, so a result sometimes lands a few dozen characters
  over, and strict mode then drops a whole item to get back under.
  `max_overshoot=200` keeps that item and accepts a result up to 200
  characters over the budget. Use it when the budget is a cost target; keep
  the default when it is a hard limit.
- **Budgets under about 1,000 characters are too small.** The `_meta` block
  itself needs several hundred characters, so the result will exceed them.
- **The cursor reaches the model only with a whole page.** When some of the
  page's items were left out, `_meta` has no cursor and the warning asks for a
  narrower call instead. Your code still gets the pagination fields on
  `ReducedResult.paging`.
- **Text is kept as written.** Non-ASCII text (Hindi, Japanese, emoji) is
  measured and returned as real characters, not as `\u` escapes.
- **No dependencies.** Standard library only, so it fits any stack.

## Compared with

| Approach | Valid JSON | Keeps whole items | Tells the model what's missing |
|---|---|---|---|
| Truncate to N chars (most frameworks' default) | ✗ | ✗ | Rarely |
| LLM summarisation of the result | n/a | ✗ (lossy) | ✗ |
| **agent-tool-result-reducer** | ✓ | ✓ | ✓ counts, totals, dropped fields |

## Status and roadmap

**v0.1 — extracted from a production agent runtime, where it handles every tool result.**

- [x] Core reducer, select projection, auto-fit, outline fallback
- [x] Configurable model-facing messages
- [x] Unit tests, including randomised checks of the invariants (valid JSON,
      whole items, budget) and non-ASCII text
- [x] CI (tests on 3.10–3.15)
- [ ] More tests: deep nesting, very wide objects
- [x] Published on PyPI
- [x] Examples for the OpenAI, Anthropic and LangChain tool loops
- [ ] Optional token-based budget via a pluggable length function

## Development

```bash
pip install -e ".[dev]"
pytest
```

## Feedback and contributing

- **Bugs and requests:** [open an issue](https://github.com/AryabhattaLabs/agent-tool-result-reducer/issues).
- **Design questions** (for example, whether the budget should be in tokens): join the
  [feedback thread](https://github.com/AryabhattaLabs/community/discussions/4), or start your own in
  [Design reviews](https://github.com/AryabhattaLabs/community/discussions/categories/design-reviews).
- **Pull requests** are welcome; see [CONTRIBUTING](https://github.com/AryabhattaLabs/.github/blob/main/CONTRIBUTING.md).

## License

MIT © Ajeet Singh Kushwaha. Built at [Aryabhatta Labs](https://aryabhattalabs.com/#developers).
