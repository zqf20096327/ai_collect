# 🛠️ Claude Code Server Ops

**Deploy and check a Claude Code API server with systemd, health probes and end-to-end smoke tests.**

Built for **[schmarta/claude-code-openai-server](https://github.com/schmarta/claude-code-openai-server)**. This repository contains the operations tooling; install the upstream server separately.

## ⚡ What it does

- 🐧 **Service deployment** — render a systemd unit, check prerequisites and verify its configuration.
- 🔑 **Credential setup** — write a Claude CLI token into the service environment.
- 🩺 **Health checks** — test a real completion, beyond the HTTP liveness endpoint.
- 🧪 **Smoke tests** — exercise text, streaming, tool calls, images and session behaviour.
- 🔬 **Scratch instances** — run a separate server process on another port for comparison.

## 🔧 Built for operations

- **Shell scripts + Python standard library**, with no extra dependencies for the smoke suite.
- **Configurable paths and ports**, with a dry-run option for service installation.
- **Exit codes for deployment gates**, so a failed smoke check can stop a release.
- **Documented failure modes**, including expired credentials, proxy buffering and interrupted tool calls.

## 🚀 Quick start

Requires **Linux with systemd** for service installation, **Python 3.9+**, `curl`, an authenticated `claude` CLI and a working upstream server checkout.

```bash
git clone https://github.com/mazamaka/claude-code-server-ops.git
cd claude-code-server-ops

# Adjust /opt/cci and the port for your upstream installation.
sudo scripts/install-service.sh --repo /opt/cci --port 8787 --dry-run
```

After reviewing the dry run and preparing the service credentials:

```bash
sudo scripts/mint-token.sh --env-file /opt/cci/.env
sudo scripts/install-service.sh --repo /opt/cci --port 8787
python3 smoke/run_smoke.py --base http://127.0.0.1:8787
```

**[Environment template →](config/server.env.example)** · **[Usage & smoke checks →](docs/USAGE.md)** · **[Troubleshooting →](docs/GOTCHAS.md)**

## 🔐 Operational notes

- **Restrict access.** The upstream CLI runs with permission bypass and can execute code as its service user. Keep the endpoint on loopback and set `CCI_API_KEY`.
- **Probes use the model.** Deep health checks and most smoke checks make real completions; include them in your usage budget.
- **Restarts affect sessions.** Restarting the server drops in-memory conversations, including parked tool calls.
- **Verify your upstream build.** Session recovery differs between versions; the smoke suite can assert the expected behaviour.

---

**Bash · Python · systemd · HTTP · SSE**

**[MIT license](LICENSE)** · The upstream server is a separate project with its own terms.
