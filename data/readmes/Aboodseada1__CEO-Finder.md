# CEO Finder

Command-line tool that identifies the CEO, president, founder or owner of a company from public web search results. It runs several targeted searches through a self-hosted SearXNG instance, then asks an LLM to extract a single name from the result snippets and return it as structured JSON.

## Problem

Company records often lack a current executive name. Finding it by hand means running several searches and cross-checking snippets. This tool automates that loop for one company at a time.

## How it works

1. Takes a company name or domain as input and normalizes it.
2. Runs seven search queries against SearXNG (for example `"<company>" CEO official name`, `"<company>" founder OR president OR owner`, and a LinkedIn-scoped query), collecting up to two result pages each.
3. Builds a prompt from the top 15 titles, URLs and snippets. The prompt asks the model to prefer CEO over President, Founder and Owner, to favor names that appear consistently, and to return `null` when nothing is clear.
4. Calls the selected LLM provider and parses the JSON reply, stripping code fences if present. Output looks like `{"ceo_name": "Full Name"}` or `{"ceo_name": null}`.

## Stack

- Python 3, `requests`
- SearXNG for search (self-hosted)
- LLM providers: Google Gemini, OpenAI, Groq, Ollama (local). Optional model override, with a fallback list per provider.

## Usage

```bash
pip install -r requirements.txt

python standalone_ceo_finder.py "Example Corp" \
  --searx-url http://localhost:8080 \
  --llm-provider ollama \
  --llm-model llama3
```

Options: `--llm-provider {gemini,openai,groq,ollama}`, `--llm-model`, `--llm-api-key` (needed for Gemini, OpenAI and Groq), `--log-level`.

## Limits

- Accuracy depends on what search returns and on the model. Treat the result as a lead to verify, not a confirmed fact.
- One company per run. There is no batching or caching.

## Responsible use

The tool reads only public search results. Follow the terms of your search provider and LLM provider, and the data protection rules that apply to you when you store or use personal names.

## License

MIT. See `LICENSE`.
