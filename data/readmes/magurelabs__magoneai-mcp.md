# magoneai-mcp

[![CI](https://github.com/magurelabs/magoneai-mcp/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/magurelabs/magoneai-mcp/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/magurelabs/magoneai-mcp/badge)](https://scorecard.dev/viewer/?uri=github.com/magurelabs/magoneai-mcp)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-magureai-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/u/magureai)

MCP connectors for third-party APIs, built on the [official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

Every connector here talks to somebody else's API. You supply your own credentials and your own storage, and the tool works the same whether it runs inside a platform or on your laptop. If a tool cannot do that, it does not belong in this repository.

### MagOneAI

[MagOneAI](https://www.magureinc.com/magoneai) is Magure's AI agent workflow platform: teams define agents with a persona and tools, place them in multi-step workflows, and run them from an app, chat, a schedule or an API, while the platform handles orchestration, retries, credentials and execution tracking. Its agents reach outside services through MCP servers, and this repository is those servers, published so they run anywhere, not only inside MagOneAI.

Where these docs or a tool's description say **the platform** or **the host**, they mean whatever runs the connector on a user's behalf: MagOneAI, another MCP host, or you on your laptop. A few tools accept a *file reference* (a file ID) that a host can swap for the file's bytes before the tool runs. MagOneAI does that; called directly, send the bytes inline as the tool's schema describes.

### Names

The project's short name is **`magoneai`**. The others each have a reason:

| Name | What it is |
|---|---|
| Magure Tech Middle East Ltd | the company: copyright holder and steward ([NOTICE](NOTICE), [GOVERNANCE.md](GOVERNANCE.md)) |
| MagOneAI | Magure's platform, the product these connectors were built for |
| `magoneai` | the short name: this repository (`magoneai-mcp`) |
| `magureai` | Magure's Docker Hub namespace, where each connector's image is published (`magureai/mcp-<connector>`) |
| `magurelabs` | the GitHub organisation, and so the MCP Registry namespace (`io.github.magurelabs/<connector>`), which the registry ties to it |
| `magone-mcp-core` / `magone_mcp_core` | the framework's package on PyPI, and its import name |

## What is here

- **`magone-mcp-core`** (`src/magone_mcp_core/`) - a thin layer over the SDK. It adds the handful of things a connector catalogue needs and the SDK has no opinion about, and gets out of the way otherwise.
- **`connectors/`** - one package per connector: 27 connectors, 283 tools. [`docs/TOOLS.md`](docs/TOOLS.md) lists every tool, generated from the code.
- **`scripts/`** - the gates CI runs on every pull request, each of which you can run locally.

`connectors/publication.json` records which connectors are ready to publish (18) and which are not yet (8), with the reason for each.

> **`twitter_intel` uses an unofficial provider.** It calls [twitterapi.io](https://twitterapi.io), a third-party service, not the official X API. Neither the connector nor the provider is affiliated with or endorsed by X Corp. It is blocked from publication; if you run it yourself, you are responsible for complying with the terms of X and of twitterapi.io.

## Documentation

| | |
|---|---|
| [docs/TOOLS.md](docs/TOOLS.md) | every tool in every connector, generated from the code |
| [docs/configuration.md](docs/configuration.md) | every environment variable the framework and the connectors read, with defaults |
| [docs/architecture.md](docs/architecture.md) | how `magone-mcp-core` handles a request: transport, auth modes, limits, redaction, read-only mode, annotations |
| [docs/writing-a-connector.md](docs/writing-a-connector.md) | a complete minimal connector, from an empty directory to a passing pull request |
| [CONTRIBUTING.md](CONTRIBUTING.md) | the boundary rule, running every gate locally, DCO sign-off, review |
| [SUPPORT.md](SUPPORT.md) | where to ask questions and report problems |
| [CHANGELOG.md](CHANGELOG.md), [RELEASING.md](RELEASING.md) | what changed, and how releases are versioned and published |
| [GOVERNANCE.md](GOVERNANCE.md), [MAINTAINERS.md](MAINTAINERS.md) | how decisions are made, and by whom |

## Quickstart

Requires Python 3.11 or later. The published wheel ships only `magone-mcp-core`; connectors run from a source checkout:

```bash
git clone https://github.com/magurelabs/magoneai-mcp
cd magoneai-mcp
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e .
MCP_MODE=local python -m connectors.linear
```

This starts the `linear` connector, which needs nothing but a [Linear API key](https://linear.app/settings/account/security) to make a real call. On start it logs one `[error]` line, `local_bind_clamped_to_loopback`. That is expected: `local` mode is unauthenticated, so the server refuses to listen beyond `127.0.0.1` and says so loudly.

The server speaks MCP over Streamable HTTP at `http://127.0.0.1:8000/mcp` (`PORT` changes the port). There is no stdio transport yet, so point your client at the URL. `GET /healthz` answers `{status, name, version, tools}`.

From a second terminal in the same virtualenv, list the tools and make one call with the official SDK's client:

```python
import asyncio
import os

from mcp import ClientSession
from mcp.client.streamable_http import create_mcp_http_client, streamable_http_client


async def main() -> None:
    headers = {"X-Linear-Api-Key": os.environ["LINEAR_API_KEY"]}
    async with (
        create_mcp_http_client(headers=headers) as http,
        streamable_http_client("http://127.0.0.1:8000/mcp", http_client=http) as (read, write),
        ClientSession(read, write) as session,
    ):
        await session.initialize()
        tools = await session.list_tools()
        print([tool.name for tool in tools.tools])
        result = await session.call_tool("get_viewer", {})
        print(result.structured_content or result.content)


asyncio.run(main())
```

```bash
LINEAR_API_KEY=lin_api_... python client.py
```

`get_viewer` returns the account the key belongs to. Any MCP client works the same way: point it at the URL and send the connector's credential headers.

Replace `linear` with any directory under `connectors/`. A connector that needs a third-party library declares it as an extra of the same name, for example `pip install -e ".[web_search]"`; a connector without one needs only `pip install -e .`. Several at once: `pip install -e ".[database,outlook_email]"`. Some connectors also need a service of their own: `web_search` needs a [SearXNG](https://docs.searxng.org/) instance or a Serper key (see below), and its `scrape_url` tool needs [Crawl4AI](https://docs.crawl4ai.com/) ([configuration](docs/configuration.md#web_search)).

### Credentials

Each tool declares the request headers it may receive, for example `X-Linear-Api-Key`, and gets them as a `credentials` dict. Send them as HTTP headers from your client, or, for a server you run yourself, put them in a JSON file and set `MCP_CREDENTIALS_PATH` to its path. Keys are the header name without the leading `X-`, lower-cased, with `-` replaced by `_`:

```json
{"linear_api_key": "lin_api_..."}
```

The file wins: a header cannot override a key the file sets, and can fill only keys the file leaves unset. If the file holds a secret, the host, port, URL, endpoint, connection string and allowlist keys (for example `X-Db-Host`, `X-Allowed-Mailboxes`) are never taken from a header, so a caller cannot point your secret at a server of their choosing. With no file, headers supply everything. `docs/TOOLS.md` shows how many credential headers each tool takes; the tool's `credential_headers=` in `connectors/<name>/server.py` names them.

`web_search` needs no key: it uses a SearXNG instance at `SEARXNG_URL` (default `http://localhost:8888`, JSON output enabled), or Serper when `SERPER_API_KEY` is set. It fetches pages under its own User-Agent and obeys robots.txt when crawling; you are responsible for the terms of the sites it fetches and of the search provider (see [configuration](docs/configuration.md#web_search)).

### In a container

One image builds any connector, selected at build time:

```bash
docker build --build-arg CONNECTOR=web_search \
  --build-arg SERVER_NAME=io.github.magurelabs/web-search -t magone-mcp-web-search .
docker run --rm -p 8000:8000 -e MCP_MODE=local -e MCP_ALLOW_INSECURE_BIND=1 magone-mcp-web-search
```

The connector's own extra is installed so it gets what it needs and nothing else. The image runs as uid 10001, never root, and carries `LABEL io.modelcontextprotocol.server.name` matching the connector's `server.json`. `MCP_ALLOW_INSECURE_BIND=1` is needed because a container must bind beyond loopback; only do that on a network you control, or use `platform` or `hosted` mode with authentication instead.

## Writing a connector

```python
from mcp.types import ToolAnnotations
from magone_mcp_core import ConnectorServer

server = ConnectorServer(name="example", version="0.1.0")


@server.tool(
    name="search_issues",
    description="Search issues by text.",
    annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False),
)
async def search_issues(query: str, limit: int = 20) -> dict:
    """Return matching issues."""
    return {"issues": [], "query": query}


if __name__ == "__main__":
    server.run(port=8000)
```

The schema comes from your type hints, which is the right default for a new tool. [docs/writing-a-connector.md](docs/writing-a-connector.md) walks through a complete connector with credentials, tests and every step a pull request needs.

### Declaring a tool's permission group

A connection rarely wants a connector's whole surface, so each tool names the
group it belongs to and the scopes it needs:

```python
@server.tool(
    name="deleteJiraIssue",
    description="Delete an issue.",
    annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=True),
    permission_group="write_jira",
    required_scopes=["write:jira-work"],
)
async def delete_jira_issue(credentials: dict, issueIdOrKey: str) -> dict: ...
```

A tool that declares no group falls in `default`. Both values are carried to a
client as `_meta` on the listed tool, and `scripts/permission_group_gate.py`
fails a tool whose group stayed a comment - a group that is not declared cannot
narrow anything, and the failure is silent in the direction that serves every
tool to every connection.

A group is a label a host can select on, not a permission the server enforces
on its own: see [Tool selection is a hint](#tool-selection-is-a-hint-not-a-guarantee).

### Keeping a schema exactly as written

A tool that already exists, and whose schema agents already rely on, should not have that schema regenerated. Derivation invents a `title`, adds one to every property, and drops every `description` - a silent behaviour change for any agent reading the description to decide what to pass.

`declare_schema` keeps the schema byte for byte:

```python
from magone_mcp_core import declare_schema


@server.tool(name="search_web", description="Search the web.", annotations=...)
@declare_schema(
    {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"},
        },
        "required": ["query"],
    }
)
async def search_web(query: str) -> dict: ...
```

Use it for [ported](#glossary) tools. Use type hints for new ones.

## What the framework guarantees

Each of these exists because doing it per connector meant it was done differently in each one, or not at all.

| Guarantee | What it does |
|---|---|
| **Outbound budget** | Bounds what a single tool result may return, and says so in the result when it truncates. A silently shortened list is worse than an error, because the model treats it as complete. |
| **Read-only mode** | `MCP_READ_ONLY=1` filters non-read tools out of `tools/list` *and refuses them on `tools/call`*. The call check is the control; the listing filter is a convenience. |
| **SSRF validation** | One implementation. IPv6 literals are unwrapped to the IPv4 they encode (IPv4-mapped, 6to4, Teredo, NAT64) before any membership test, because `ip in network` is False across address families. |
| **Credential-safe logging** | Tool arguments are logged by key only. Upstream error bodies are scrubbed and truncated before they reach a log line, because a vendor's 401 frequently echoes the token. |
| **Authenticated callers** | `platform` mode requires the caller's `X-Service-Token` to match `MCP_SERVICE_TOKEN`, or a token verifier; `hosted` mode requires a token verifier, which validates audience and expiry and answers 401 with an RFC 9728 challenge. A server with neither refuses to start rather than serving unauthenticated. The inbound token is never forwarded upstream. The shared service token is the [interim control](#glossary): it proves the caller holds a secret, not which tenant it is. |
| **Loopback default** | `local` mode is unauthenticated, so it will not bind beyond loopback without `MCP_ALLOW_INSECURE_BIND=1`. |
| **Host and Origin allowlist** | DNS-rebinding protection is always on. Loopback is always accepted; every other name a caller uses (a service name, an ingress host) must be listed in `MCP_ALLOWED_HOSTS`, or the request is answered `421`. |
| **Text arguments stay text** | An argument whose published schema admits a string (`"type": "string"`, a type list or `anyOf`/`oneOf` that includes one, or no type at all) reaches the handler as the string that was sent. The SDK's pre-parse would otherwise `json.loads` it whenever the annotation is not exactly `str`, turning `"null"` into `None` and `'{"a":1}'` into a dict. Object, array, number and boolean parameters keep the SDK's behaviour. |
| **Health endpoint** | `GET /healthz` answers `{status, name, version, tools}` for a container or Kubernetes probe. Hosts discover the catalogue over MCP (`server/discover`, `tools/list`), not from this endpoint. |

### Tool selection is a hint, not a guarantee

A caller can narrow one connection to part of a connector: `X-MCP-Enabled-Tools` names tools outright, `X-MCP-Enabled-Groups` names permission groups, and names win when both are sent. The server then filters `tools/list` and refuses a call outside the selection.

Those headers come from the caller, on the very request they narrow. A request that sends neither is served every tool, and nothing stops a client from leaving them out or widening them. Selection therefore restricts nothing on its own. It is only a control when a trusted intermediary you run, such as the host application or a gateway, sets the headers itself and never passes through values chosen by the end client. Do not put a connector in front of a client you do not trust and rely on these headers to limit it.

Groups also only narrow anything where a connector declares more than one. Seven do: `atlassian_confluence`, `atlassian_jira`, `csv_to_sql`, `filesystem`, `linkedin`, `trino` and `vanna`. In the other 18 every tool is in `default`, so selecting by group there is all or nothing; select by tool name instead.

The control that does restrict writes, whatever the caller sends, is `MCP_READ_ONLY=1` set on the server. Every tool not annotated `readOnlyHint=true` is dropped from `tools/list` and refused on `tools/call`, and a tool with no annotations counts as a write.

## Configuration

The variables most deployments touch. [docs/configuration.md](docs/configuration.md) lists every one, including those individual connectors read.

| Variable | Default | Meaning |
|---|---|---|
| `MCP_MODE` | `platform` | `platform`, `hosted` or `local`. An unrecognised value falls back to `platform`, so a typo cannot disable authentication. |
| `MCP_READ_ONLY` | unset | `1` refuses every tool that is not marked `readOnlyHint`. |
| `MCP_MAX_RESULT_CHARS` | `1000000` | Outbound budget per tool result. |
| `MCP_MAX_BODY_BYTES` | `10485760`, or the connector's own default | Largest request body accepted, in bytes (10 MiB). A larger one is answered `413` before it is parsed. A connector may declare a larger default (`atlassian_jira` 70 MiB, `outlook_email` 75 MiB); this overrides it. Base64 attachments are a third bigger than the file they carry. |
| `MCP_ALLOW_INSECURE_BIND` | unset | `1` lets `local` mode bind beyond loopback. |
| `MCP_ALLOWED_HOSTS` | loopback only | Comma-separated Host names callers use, e.g. `mcp-jira,mcp-jira.tools.svc.cluster.local`. A bare name is accepted with or without a port. `*` disables the check. |
| `MCP_ALLOWED_ORIGINS` | loopback only | Comma-separated browser origins allowed to call the server. A server-to-server call sends no Origin and is unaffected. |
| `MCP_SERVICE_TOKEN` | unset | `platform` mode: the shared secret every caller must send as `X-Service-Token` on `/mcp`. |
| `MCP_ALLOW_UNAUTHENTICATED` | unset | `1` lets `platform` or `hosted` mode start with no caller authentication. Only for a deployment where something in front authenticates every request. |
| `MCP_RESOURCE_URL`, `MCP_AUTH_ISSUER_URL` | unset | With a token verifier: this server's canonical URL (the audience tokens must name) and the authorization server. |
| `MCP_LOG_RAW_UPSTREAM_ERRORS` | unset | `1` logs unscrubbed upstream bodies. Honoured only in `local` mode. |

## On prompt injection

Every connector here returns text written by someone outside your trust boundary: an issue description, an email body, a scraped page. That text reaches a model that may also hold write tools.

No authorization model prevents this, because the caller is legitimately authorized for both the read and the write. A server cannot solve prompt injection and this one does not claim to.

Two things it does do. `MCP_READ_ONLY=1` makes a deployment that only needs reads incapable of writing, so it cannot be talked into one; that is the control with real blast-radius value. The provenance envelope marks third-party text so a client that wants to treat it as data has something to key on; that is a convention, not a guarantee, and wrapping text does not stop a model reading instructions inside it.

## Tests and gates

The whole suite runs with no credentials and no network:

```bash
pip install -e ".[dev,all]"
pytest tests/ connectors/ -q
```

The tests are in three groups: framework tests that need only `[dev]` (`pytest tests/ -m "not requires_connectors"`), framework tests that import every connector, and connector tests under `connectors/*/tests`. Every gate is tested by injecting the defect it exists for.

CI also runs, on every pull request: `ruff check` and `ruff format --check`; a golden-schema diff of every tool's input and output schema (`scripts/golden_schema_gate.py`); a boundary check that refuses platform reach-through (`scripts/boundary_gate.py`); the tool-contract linter (annotations, property descriptions, logged credentials); dependency, compile, code-health, credential-header, permission-group, publication, manifest and runner-label gates; and the official MCP conformance suite against every connector the change can affect. Each gate is a script under `scripts/` that runs locally the same way.

## Publication

Each of the 18 publishable connectors carries a `server.json` (schema `2025-12-11`), derived from the connector's own `SERVER_NAME` and `SERVER_VERSION` so a manifest cannot describe a server other than the one that runs. `scripts/gen_server_json.py --check` regenerates and diffs them, and `scripts/publication_gate.py` fails if a blocked connector ever gains one.

Released artifacts:

- **Container images:** one per publishable connector on Docker Hub under [`magureai`](https://hub.docker.com/u/magureai), named `magureai/mcp-<connector>`, tagged with the connector's version.
- **Python package:** the framework as [`magone-mcp-core`](https://pypi.org/project/magone-mcp-core/) on PyPI.
- **MCP Registry:** one entry per publishable connector under `io.github.magurelabs/<connector>`.

`.github/workflows/publish.yml` builds and validates all of this on every pull request that touches it, and publishes only on a manual dispatch inside the protected `release` environment, after a maintainer approves the run.

## History

The connectors originated in Magure's internal platform and are released here by Magure Tech Middle East Ltd. Code comments call that earlier framework **v1**.

Every carried-over tool's input schema is kept byte for byte with `declare_schema` and checked on every pull request, because that is the part that would silently change behaviour for an agent already running. Handler bodies were carried across unchanged; `scripts/port_status.py` counts names a body refers to that do not resolve, and fails if that number rises above zero.

Moving a connector from v1 to this framework is a **port**: a *ported* tool kept its v1 schema byte for byte, and *pre-port* means as it was in v1.

## Glossary

Terms the code, comments and docs use without stopping to define them.

| Term | Meaning |
|---|---|
| **v1**, **port**, **ported**, **pre-port** | Terms code comments use about where a connector came from; see [History](#history). |
| **gate** | A check under `scripts/` that CI runs on every pull request and fails on a specific defect, for example `boundary_gate.py`. Each runs locally the same way. |
| **golden baseline** | The recorded copy of every tool's input and output schema in `tests/golden/`. `golden_schema_gate.py` fails on any difference, so a contract change has to be approved explicitly. |
| **publication**, **ready**, **blocked** | Whether a connector may be published to the MCP Registry and as an image. `connectors/publication.json` marks each one `ready` or `blocked`, with the reason. |
| **platform** | A host that runs these connectors for many users, such as Magure's own. `platform` mode is the auth mode for that setting. |
| **interim control** | The shared `MCP_SERVICE_TOKEN` in `platform` mode: it proves the caller knows a secret, not which tenant it is. A token verifier proves both, which is why `hosted` mode requires one. |
| **playground** | Running a connector yourself with a credentials file (`MCP_CREDENTIALS_PATH`) instead of per-call headers. |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions are under the [Developer Certificate of Origin](https://developercertificate.org/) rather than a CLA: sign off each commit with `git commit -s`, and a check on every pull request verifies it. Please read the [Code of Conduct](CODE_OF_CONDUCT.md). How the project is run is in [GOVERNANCE.md](GOVERNANCE.md); questions go where [SUPPORT.md](SUPPORT.md) says.

## Security

See [SECURITY.md](SECURITY.md). Please report vulnerabilities privately, through GitHub's private vulnerability reporting or to security@magureinc.com, rather than by opening an issue.

## Licence

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

All product names and trademarks are the property of their respective owners and are used only to identify which API a connector talks to. No connector is affiliated with or endorsed by the owner of the API it wraps, and no vendor logos appear anywhere in this repository.
