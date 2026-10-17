# WebSearchFree

**Free open-source Tavily alternative** — keyless web search + content extraction for AI agents, RAG, LangChain, MCP, and LLM tools.

Self-host a local **web search API for AI** with **no API key**, **no quota**, and **no per-query bill**. Drop-in style JSON similar to [Tavily](https://tavily.com), without paying for [Serper](https://serper.dev), [Exa](https://exa.ai), [Linkup](https://www.linkup.so), [Brave Search API](https://brave.com/search/api/), [SerpAPI](https://serpapi.com), or [Firecrawl](https://www.firecrawl.dev) search credits.

> Looking for a **free Tavily**, **open source web search for RAG**, or a **self-hosted AI search API**? This repo is that.

No accounts. No telemetry. Outbound HTTPS only to public search engines and pages.

```mermaid
flowchart TB
  subgraph clients [Your stack]
    UI[Embedded UI]
    CLI[CLI]
    CPP[C++ library]
    PY[Python]
    HTTP[Local HTTP]
    MCP[MCP]
    LC[LangChain]
  end

  subgraph core [wsf_core]
    Search[search plus status]
    Extract[multi extract]
    Rank[merge and rank]
  end

  subgraph engines [Keyless engines]
    DDG[DuckDuckGo]
    Brave[Brave]
    Wiki[Wikipedia]
    News[DDG news]
    Searx[SearXNG optional]
  end

  UI --> Search
  CLI --> Search
  CPP --> Search
  PY --> Search
  HTTP --> Search
  MCP --> HTTP
  LC --> HTTP
  Search --> DDG
  Search --> Brave
  Search --> Wiki
  Search --> News
  Search --> Searx
  DDG --> Rank
  Brave --> Rank
  Wiki --> Rank
  News --> Rank
  Searx --> Rank
  Rank --> Extract
  Extract --> Out[JSON for RAG or agents]
```

## Free alternative to paid AI web search APIs

| Need | Paid options | WebSearchFree |
|------|----------------|---------------|
| Agent / RAG live web results | Tavily, Linkup, Exa, You.com | Yes, local |
| SERP-style search JSON | Serper, SerpAPI, Bing Search API | Yes, metasearch |
| Page → clean text for LLMs | Firecrawl, Tavily extract | Static HTML extract (not JS/anti-bot scrape) |
| API key / monthly credits | Required | **None** |
| Data leaves your machine for the vendor | Usually yes | **No vendor cloud** — binary is local; queries still go to public engines (DDG/Brave/Wikipedia) |

## Features (v0.5)

- **Plug and play**: Docker / GHCR, one-line install scripts, GitHub Release binaries
- **Self-update**: `wsf update` (SHA256-verified GitHub Releases); 24h nudge; `/health` reports `update_available`
- **In-process MCP**: `wsf mcp` — tools `web_search`, `web_search_multi`, `web_extract`
- **Metasearch** across DuckDuckGo HTML, Brave Search HTML, Wikipedia, optional SearXNG, and DDG news
- **Agent / RAG knobs**: `include_domains` / `exclude_domains`, `search_depth` (`basic`|`advanced` = auto-extract, not crawl), `topic`, `time_range`, `max_tokens` + `context_tokens`
- **Multi-query**: `POST /search/batch`, CLI `--queries q1||q2`, MCP `web_search_multi`
- **Trust ranking + goggles**: boost/bury via `goggles.yaml`; official-docs heuristics
- **Injection scrub** on extract (`sanitized` flag when scrubbing occurred)
- **Adaptive engine failover** + durable search disk cache (`WSF_SEARCH_CACHE_TTL`)
- **Extractive `answer`**: sentences from top snippets/raw text (not an LLM)
- **Honest status**: per-engine `ok` / `error`, `warning_details`, real `response_time`
- MIT licensed

### vs Tavily / Exa / Firecrawl / SearXNG

| | WebSearchFree | Tavily / Exa | Firecrawl | SearXNG |
|--|---------------|--------------|-----------|---------|
| Keys / bill | None | Required | Required | Self-host ops |
| Agent JSON + MCP | Built-in | SaaS | Scrape-first | DIY wrappers |
| Token-budget context | `max_tokens` | Vendor packs | N/A | DIY |
| Multi-query fan-out | Native | Linkup-like paid | N/A | Manual |
| JS render / deep crawl | No (static HTML) | Varies | Yes | No |
| LLM research answers | No (extractive only) | Yes (paid) | N/A | No |

### Non-goals (honest)

- `answer` is **extractive**, not an LLM-generated summary
- `search_depth: advanced` means **auto-extract**, not crawl depth
- Extract is **static HTML**, not a Firecrawl-style JS browser farm
- Queries **leave your machine** to public engines (there is no private web index)
- No image search or `follow_up_questions` (still null/empty)
- Result quality depends on upstream HTML/APIs; not Google-quality SERP fidelity

## Plug and play (no C++ build required)

Pick one path. Every path exposes the same local API at `http://127.0.0.1:8080`.

| Path | Command |
|------|---------|
| **Docker (any OS)** | `docker run --rm -p 8080:8080 ghcr.io/drmikecrypto/websearchfree:latest` |
| **Compose (this repo)** | `docker compose up --build` |
| **Windows one-liner** | `irm https://raw.githubusercontent.com/drmikecrypto/WebSearchFree/main/scripts/install.ps1 \| iex` |
| **Linux one-liner** | `curl -fsSL https://raw.githubusercontent.com/drmikecrypto/WebSearchFree/main/scripts/install.sh \| bash` |

Then open [http://127.0.0.1:8080](http://127.0.0.1:8080) or call the API:

```bash
curl -s -X POST http://127.0.0.1:8080/search \
  -H "Content-Type: application/json" \
  -d '{"query":"open source metasearch","max_results":5,"search_depth":"basic","topic":"general","include_answer":true}'
```

Release binaries are self-contained (static MSVC CRT on Windows; no MinGW DLL hell). Tag `v*` to publish via GitHub Actions → Releases + GHCR.

### Drop into another project

1. Run WebSearchFree (Docker/binary above).
2. Copy one client:

| Your stack | Drop-in |
|------------|---------|
| Any language / HTTP | `POST /search`, `POST /extract` — see `/openapi.json` |
| Python (stdlib) | copy [`integrations/http/client.py`](integrations/http/client.py) |
| OpenAI tool calling | [`examples/openai_tools.json`](examples/openai_tools.json) + [`examples/drop_in_agent.py`](examples/drop_in_agent.py) |
| LangChain | [`integrations/langchain/wsf_tool.py`](integrations/langchain/wsf_tool.py) |
| Cursor / Claude MCP | [`integrations/mcp/server.py`](integrations/mcp/server.py) |

```python
# anywhere — stdlib only
import sys
sys.path.insert(0, "path/to/WebSearchFree/integrations/http")
from client import WebSearchFree

wsf = WebSearchFree()  # or WebSearchFree("http://127.0.0.1:8080")
print(wsf.search("open source metasearch", max_results=5))
print(wsf.extract(["https://example.com"]))
```

Set `WSF_BASE_URL` if the server is not on localhost:8080. Optional `.env` keys: see [`.env.example`](.env.example).

## Quick start (build from source)

### Docker (local build)

```bash
docker compose up --build
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080) for the UI. API: `POST /search`, `POST /search/batch`, `POST /extract`, `GET /health`, `GET /openapi.json`.

### Build (Windows / MinGW or MSVC)

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -G "MinGW Makefiles" -DCMAKE_CXX_COMPILER=C:/mingw64/bin/g++.exe
cmake --build build -j
ctest --test-dir build --output-on-failure
```

Binary: `build/wsf.exe` (or `build/wsf`). MinGW builds link `-static`; MSVC builds use static CRT — you should not need extra compiler DLLs next to the exe.

### Search (no keys)

```bash
./build/wsf search "open source metasearch" --max 5 --json
```

### Extract a URL

```bash
./build/wsf extract https://example.com --json
```

### Local HTTP — Tavily-compatible shape for agents

```bash
./build/wsf serve --host 127.0.0.1 --port 8080
```

```bash
curl -s -X POST http://127.0.0.1:8080/search \
  -H "Content-Type: application/json" \
  -d '{"query":"open source metasearch","max_results":5,"search_depth":"advanced","topic":"news","time_range":"week","max_tokens":2000,"include_domains":["wikipedia.org"],"include_answer":true}'
```

```bash
curl -s -X POST http://127.0.0.1:8080/search/batch \
  -H "Content-Type: application/json" \
  -d '{"queries":["metasearch open source","keyless web search API"],"max_results":8,"max_tokens":1500}'
```

```bash
curl -s -X POST http://127.0.0.1:8080/extract \
  -H "Content-Type: application/json" \
  -d '{"urls":["https://example.com","https://example.org"]}'
```

No `Authorization` header required.

### MCP (Cursor / Claude Desktop)

Preferred (in-process, no HTTP server):

```json
{
  "mcpServers": {
    "websearchfree": {
      "command": "wsf",
      "args": ["mcp"]
    }
  }
}
```

HTTP fallback: start `wsf serve --port 8080`, then point Python [`integrations/mcp/server.py`](integrations/mcp/server.py) at `WSF_BASE_URL`.

Tools: `web_search`, `web_search_multi`, `web_extract`.

### Self-update

```bash
wsf update --check
wsf update
# Installers verify SHA256; pin with WSF_VERSION=v0.5.0
# Opt out of the daily nudge: WSF_NO_UPDATE_CHECK=1
# Auto-apply (non-serve): WSF_AUTO_UPDATE=1
```

Docker: `docker pull ghcr.io/drmikecrypto/websearchfree:latest` (self-update does not rewrite container images).

### LangChain

```bash
pip install langchain-core
# with wsf serve running:
```

```python
import sys
sys.path.insert(0, ".")
from integrations.langchain.wsf_tool import WebSearchFreeTool

tool = WebSearchFreeTool(base_url="http://127.0.0.1:8080")
print(tool.invoke({"query": "open source metasearch", "max_results": 5}))
```

### C++

```cpp
#include "wsf/wsf.hpp"

wsf::Options opt;
opt.include_domains = {"wikipedia.org"};
opt.search_depth = "advanced";  // attaches raw_content
opt.topic = "news";
opt.include_answer = true;      // extractive, not LLM
auto resp = wsf::search("open source metasearch", opt);
for (const auto& r : resp.results) {
  // r.title, r.url, r.content, r.score, r.raw_content
}
// resp.answer, resp.engines, resp.warnings, resp.response_time
```

### Python

```bash
cmake -S . -B build -DWSF_BUILD_PYTHON=ON ...
# or call the CLI via bindings/python/wsf/__init__.py fallback
```

```python
import sys
sys.path.insert(0, "bindings/python")
import wsf
print(wsf.search("open source metasearch", max_results=5))
print(wsf.extract_one("https://example.com"))
```

## How it works

```mermaid
sequenceDiagram
  participant App as Your app
  participant WSF as WebSearchFree
  participant Engines as Public engines
  participant Pages as Result pages

  App->>WSF: search(query)
  par Fan-out
    WSF->>Engines: DuckDuckGo HTML
    WSF->>Engines: Brave HTML
    WSF->>Engines: Wikipedia API
    WSF->>Engines: SearXNG JSON optional
    WSF->>Engines: DDG news HTML if topic=news
  end
  Engines-->>WSF: titles, urls, snippets plus status
  WSF->>WSF: dedupe and score
  opt include_raw_content
    WSF->>Pages: fetch top URLs
    Pages-->>WSF: HTML
    WSF->>WSF: extract main text
  end
  WSF-->>App: JSON results plus warnings
```

This is **metasearch**, not a sovereign web index. For personal and small-team RAG this is usually enough; it is not a hosted SaaS SLA.

Related: [SearXNG](https://github.com/searxng/searxng). Point WebSearchFree at your instance with `WSF_SEARX_URL` or `--searx-url` and include `searx` in `--engines`.

## Engines

| Name | Source | Key |
|------|--------|-----|
| `ddg` | DuckDuckGo HTML | none |
| `brave` | Brave Search HTML | none |
| `wikipedia` | MediaWiki opensearch | none |
| `searx` | Your SearXNG (`format=json`) | none (needs URL) |
| `ddg_news` | DuckDuckGo news HTML (`iar=news`) | none |

```bash
wsf search "query" --engines ddg,wikipedia
wsf search "query" --engines ddg,searx --searx-url http://127.0.0.1:8888
wsf search "query" --topic news --depth advanced --include-domain wikipedia.org
# or: export WSF_SEARX_URL=http://127.0.0.1:8888
```

## Adoption paths

```mermaid
flowchart TB
  Need[Need live web for an agent?] --> Choice{How do you integrate?}
  Choice -->|Browser| UI[wsf serve UI]
  Choice -->|Shell or scripts| CLI[wsf search]
  Choice -->|C++ project| Lib[link wsf_core]
  Choice -->|Python| Py[import wsf]
  Choice -->|LangChain| LC[integrations/langchain]
  Choice -->|Cursor or Claude| MCP[integrations/mcp]
  Choice -->|Any HTTP tool| Srv[localhost API]
```

## FAQ

**Is WebSearchFree a free Tavily alternative?**  
Yes for search + extract without keys. It does not generate AI answers or images.

**Do I need Serper, SerpAPI, Bing, or Google Programmable Search?**  
No for the built-in engines. Optional SearXNG is also keyless if you self-host it.

**Is it the same as SearXNG?**  
Same family (metasearch), different packaging: WebSearchFree is an embeddable agent-oriented binary with Tavily-shaped JSON. You can also use SearXNG as a backend engine.

**Does it phone home or require signup?**  
No.

## Project layout

```
include/wsf/              Public C++ API
src/                      Core: HTTP, engines, extract, rank
apps/wsf_cli/             CLI + HTTP server + embedded UI
bindings/python/          pybind11 module + CLI wrapper
integrations/http/        Stdlib Python HTTP client (drop-in)
integrations/mcp/         Stdio MCP server
integrations/langchain/   LangChain tools
scripts/install.*         One-line binary installers
examples/                 curl, OpenAI tools, drop-in agent
Dockerfile / compose      Production image + healthcheck
.github/workflows/        CI + Release (binaries + GHCR)
```

## Keywords

`free tavily alternative` · `open source web search api for ai` · `self hosted rag search` · `keyless serp for llm` · `langchain web search free` · `mcp web search` · `tavily open source` · `serper alternative free` · `exa alternative self host` · `ai agent web search no api key`

## License

MIT — see [LICENSE](LICENSE).

Maintained by [drmikecrypto](https://github.com/drmikecrypto).
