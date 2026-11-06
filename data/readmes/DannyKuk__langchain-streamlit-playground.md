# LangChain × Streamlit on OpenRouter

A small hands-on project for getting to know [LangChain](https://docs.langchain.com): an interactive **playground**
that shows what LangChain adds on top of a plain API call. Each tab shows the equivalent Python code next to the live
result, so you can see what is happening and copy it into your own projects.

Models are called through [OpenRouter](https://openrouter.ai), so one API key gives you access to OpenAI, Anthropic,
Google and many other models.

![The Chat tab: model settings in the sidebar, the generated code on the left, the answer with token usage and raw response metadata on the right](example.png)

## Setup

Requirements: Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                    # create .venv and install dependencies
cp .env.example .env       # then put your OpenRouter key into .env
```

`.env` holds the configuration and is gitignored. Never commit it.

| Variable | Purpose |
| --- | --- |
| `OPENROUTER_API_BASE` | API endpoint, `https://openrouter.ai/api/v1` |
| `OPENROUTER_API_KEY` | Your key from [openrouter.ai/keys](https://openrouter.ai/keys) |
| `OPENROUTER_MODEL` | Any [OpenRouter model id](https://openrouter.ai/models), e.g. `openai/gpt-4o-mini` |

## Run

```bash
uv run langchain-streamlit
```

This is a shortcut for `uv run streamlit run src/langchain_streamlit/app.py`.

Streamlit opens the app at http://localhost:8501.

## What's inside

The sidebar controls the model settings (base URL, model, temperature, max tokens, reasoning effort) and switches each
feature tab on or off.

| Tab | What it shows |
| --- | --- |
| **Chat** | The fully explicit `ChatOpenRouter(...)` declaration, the answer, token usage and `finish_reason`. Passing `base_url` and `api_key` is optional: `ChatOpenRouter` reads them from the environment by itself. |
| **Tool calling** | An agent (`create_agent`) that decides when to call Python functions (weather, calculator, clock), with every step: model call → tool call → tool result → answer. |
| **Structured output** | `with_structured_output(PydanticModel)`: turns text into a validated Python object. Compare the `function_calling` and `json_schema` methods and see the raw model reply. |
| **Memory** | A multi-turn chat whose history is kept by a LangGraph checkpointer per `thread_id`. Switch memory off to see the model forget, and watch the input tokens grow with the history. |

## Things worth knowing

- **The model never runs your code and remembers nothing between calls.** Tools, structured output and memory all work
  the same way: LangChain sends extra context (tool descriptions, a schema, the chat history) and handles the reply.
- **Tool calling needs a model that supports it.** Check the model's page on OpenRouter.
- **Reasoning effort only affects reasoning models.** Set it to *off* for models like `gpt-4o-mini`.
- **Field descriptions are prompts.** For structured output, spell out exact formats (e.g. ISO dates) in
  `Field(description=...)`. JSON-schema hints like `"format": "date"` are usually not enforced.
- **Memory is in RAM** (`InMemorySaver`): it is lost when Streamlit restarts. Swap in `SqliteSaver` or `PostgresSaver`
  to keep it.

## Adding a feature

1. Create a module in `src/langchain_streamlit/features/` with `TITLE`, `DESCRIPTION` and
   `render(get_model, model_code)`.
2. Add it to `FEATURES` in `features/__init__.py`.

It then gets its own tab and a switch in the sidebar.

## Project layout

```
src/langchain_streamlit/
├── __init__.py             # `uv run langchain-streamlit` entry point
├── app.py                  # the playground: sidebar, Chat tab, feature tabs
└── features/
    ├── tool_calling.py
    ├── structured_output.py
    └── memory.py
```
