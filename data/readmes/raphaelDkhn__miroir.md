# Miroir 🪞

**Turn a product into an agentic RL environment.**

Miroir packages real applications into environments for training and evaluating agents.

Add a manifest and tasks to your product's Docker image. Miroir handles the rest: seeding data, resetting state between episodes, exposing APIs as tools through OpenEnv and MCP, and grading what the agent actually changed—including database rows, emails, and HTTP requests.

## Quick start

**Requirements:** Docker with buildx and [uv](https://docs.astral.sh/uv/).

### 1. Build and verify

```bash
docker buildx bake acme-crm-env
docker run --rm --network none acme-crm-env check
```

This builds Acme CRM, a sample application with Postgres, Redis, a web server, a worker, and an MCP server. The `check` command replays every task's reference run and verifies its expected outcome.

### 2. Serve the environment

```bash
docker run --rm -d -p 127.0.0.1:8000:8000 \
  -e MIROIR_TOKEN=secret acme-crm-env

curl http://127.0.0.1:8000/health
```

### 3. Run an episode

Install the Python client:

```bash
uv venv && source .venv/bin/activate
uv pip install miroir
```

Reset an episode, execute an action, and inspect its outcome:

```python
from miroir import Session

session = Session.lease(
    ["http://127.0.0.1:8000"],
    token="secret",
    wait_busy=False,
)

start = session.reset("pay-invoice")
print(start["instruction"])

step = session.step(
    "api_request",
    {"method": "POST", "path": "/invoices/4001/pay"},
)
print(step["observation"]["result"]["status"])

outcome = session.finish()
print(outcome["reward"], outcome["metadata"]["checks"])

session.close()
```

The episode receives a reward of `1` only if the invoice is paid.

## Documentation

- [Introduction](https://raphaeldkhn.github.io/miroir/)
- [How Miroir works](https://raphaeldkhn.github.io/miroir/introduction.html#how-it-works)
- [Build an environment](https://raphaeldkhn.github.io/miroir/make/image.html)
- [Train and evaluate](https://raphaeldkhn.github.io/miroir/run/serve.html)

**[Gitea example](examples/gitea)** — Unmodified Gitea with 144 tasks across 12 task families.

Build the documentation locally with `mdbook serve docs`.

## Coding agents

Use the [Miroir skill](skills/miroir/SKILL.md) to build environments, write tasks, debug checks, and run training with coding agents.

**Claude Code**
```bash
/plugin install miroir --marketplace raphaelDkhn/miroir
```

**Other agents**
```bash
npx skills add raphaelDkhn/miroir
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Report security issues privately, as
[SECURITY.md](SECURITY.md) describes.

## License

[Apache-2.0](LICENSE)