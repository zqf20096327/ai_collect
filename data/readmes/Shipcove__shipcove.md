# Shipcove

<p align="center">
  <img src="docs/brand/shipcove-logo.svg" alt="Shipcove logo: two sails on a wave" width="120">
</p>

<p align="center">
  <a href="https://github.com/Shipcove/shipcove/actions/workflows/ci.yml"><img src="https://github.com/Shipcove/shipcove/actions/workflows/ci.yml/badge.svg" alt="Image build status"></a>
  <a href="https://github.com/Shipcove/shipcove/tags"><img src="https://img.shields.io/github/v/tag/Shipcove/shipcove?label=version&amp;color=blue&amp;sort=semver" alt="Latest version tag"></a>
  <a href="https://github.com/orgs/Shipcove/packages"><img src="https://img.shields.io/badge/container-GHCR-2496ED?logo=docker&amp;logoColor=white" alt="Container images on GitHub Container Registry"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-orange" alt="License: AGPL v3"></a>
</p>

**A self-hosted coding agent platform for your teams.** Shipcove gives every developer an AI agent that works in an isolated, disposable sandbox: it reads, edits and tests the code, pushes its branches and opens pull requests on its own, and asks a human before anything irreversible. Models go through your own LLM gateway, secrets stay in Vault, and every conversation is saved continuously to your S3 bucket.

*Build in a safe cove. Ship with confidence.*

<table>
  <tr>
    <td width="50%" align="center"><img src="docs/images/conversation.png" alt="A Shipcove conversation: the agent's steps, a screenshot it took, an approved Git push, and the git diff of its changes" width="100%"></td>
    <td width="50%" align="center"><img src="docs/images/admin-models.png" alt="Shipcove administration: models discovered from LiteLLM, with access, default model and credit coefficients" width="100%"></td>
  </tr>
  <tr>
    <td align="center"><sub>Conversation: the agent's work, screenshots, approvals and git diff</sub></td>
    <td align="center"><sub>Administration: models, access and costs</sub></td>
  </tr>
</table>

## Why Shipcove

- **The agent works, your infrastructure stays safe.** Each conversation runs in its own hardened sandbox: unprivileged user, no route to the internet or to the backend, egress only through an allowlist proxy.
- **Git without handing out tokens.** The agent uses `git`, `gh` and `glab` as usual, but never sees a forge token: the gateway swaps in the user's OAuth token on the fly. Pushing to the default branch, merging or deleting waits for a human to approve the exact operation.
- **Nothing gets lost.** Sandbox state is checkpointed to S3 after every change. A sandbox can go to sleep or crash; the conversation picks up where it left off, and any message can be rewound.
- **Your models, your rules.** Any provider behind LiteLLM, with per-user quotas over rolling 5-hour and 7-day windows, allowlists and versioned credit costs.
- **Fits into your company.** Local accounts with TOTP, OIDC/Keycloak, SAML 2.0, LDAP/Active Directory, audit log, data retention with legal hold, French and English interface.
- **Runs where you run.** Docker Compose for a single host, a Helm chart for Kubernetes.

## Features

| | |
| --- | --- |
| **Conversations** | Streamed replies and tool calls, interruption (button or Esc twice), queued messages, model and reasoning effort per conversation, *Plan* mode with read-only tools, run duration, automatic titles. Rewind to the state before any message, and undo the rewind. |
| **The agent's work** | A live **plan** for complex tasks, questions asked through forms when a decision is yours, **screenshots** of the running app taken on its own, files offered for **download**, previews of web servers on a separate domain. |
| **Git** | Repositories on GitHub or GitLab (cloud or self-managed), linked through OAuth. Working-branch selector and **git diff** next to the conversation. Branches, pull/merge requests, CI and reviews handled by the agent; protected operations approved **inline in the conversation**. Commits can credit Shipcove as co-author (address set by administrators). |
| **Sandboxes** | Docker or Kubernetes, CPU/memory/process limits, idle shutdown, a **startup script** set by administrators (private registries, mirrors, tools), and backing **services** (PostgreSQL, Redis, RabbitMQ…) the agent starts on demand from an approved catalog. |
| **Extensions** | **Skills** in markdown (folders, categories, editor with preview, .zip import and export) and **MCP** servers, both global and personal, with per-tool policies. |
| **Collaboration** | Read-only sharing with named colleagues, revocable; in-app and email notifications. |
| **Identity** | Built-in accounts with TOTP MFA and revocable sessions, OIDC/Keycloak, SAML 2.0, LDAP/Active Directory, GitHub and GitLab OAuth. Accounts are never merged by email address. |
| **Models and quotas** | LiteLLM connection set from the console, automatic model discovery, default model, user allowlists, versioned coefficients, a dedicated model for titles. Personal quotas shown as percentages, with a reservation before each call. |
| **Administration** | Full web console: users and invitations, identity providers, Git forges, models, quotas, sandboxes and images, services and registry mirrors, skills and MCP, SMTP and email templates, audit export, retention. |
| **Security** | No forge token in the sandbox, secrets in Vault and redacted from outputs, a Docker guard as the only holder of the Docker socket, server-side sessions with `HttpOnly` cookies and CSRF protection, strict CSP, attachments checked by real type and, when configured, scanned by ClamAV (fail-closed). |

## Try it

The fastest way to see Shipcove is the **interactive demo**: the real interface, in your browser, with sample conversations and a simulated agent. No server needed.

```bash
pnpm install
pnpm docs:build:demo
```

This builds the documentation site with the demo inside (`apps/docs-site/dist`, demo under `demo/`). Serve that folder with any static web server and click **Try the demo**. Nothing is saved: reload to start over.

## Quick start

Requirements: Docker 24+ with Compose v2, `git` and `openssl`, and at least 4 cores, 8 GB of RAM and 30 GB of disk.

The Compose setup below is for a trusted machine (plain HTTP). Before exposing it, read [Going to production](#current-limitations) and the [TLS guide](docs/operations/tls.md).

```bash
git clone https://github.com/Shipcove/shipcove.git
cd shipcove/infrastructure/docker
cp .env.example .env              # set CAP_REGISTRY=ghcr.io/shipcove/, CAP_VERSION, CAP_SANDBOX_IMAGE, CAP_ADMIN_PASSWORD, CAP_DOCKER_GID
./scripts/init-secrets.sh         # bootstrap secrets in .secrets/ (never committed, back them up)
docker compose pull
docker pull ghcr.io/shipcove/shipcove-sandbox:0.1.0
docker compose --profile dev up -d    # the dev profile adds Mailpit and a mock LLM provider
```

1. **Sign in.** Open http://localhost:8080 with `CAP_ADMIN_EMAIL` and `CAP_ADMIN_PASSWORD`. Administrators set up TOTP on first sign-in.
2. **Add a model.** Declare models in LiteLLM (http://localhost:4000/ui, master key in `.secrets/litellm_master_key`) or connect an existing LiteLLM proxy in **Administration → Models**. Click **Reload models**, enable one and make it the default. To try without a provider, use `openai/mock-model` with `api_base` set to `http://mock-llm:4010/v1`.
3. **Connect Git (optional).** Declare a forge in **Administration → Git forges**, then link your account in **Settings → Git connections**.
4. **Start a conversation.** Write your request on the home page, and pick a repository under the input box if you want the agent to work on one.

Emails sent in development land in Mailpit at http://localhost:8025.

**Configure everything from `.env` instead (optional).** Steps 2 and 3, SSO, SMTP and platform settings can also be declared as environment variables, applied by the API at every start: models created in LiteLLM and discovered at startup, default model, OIDC / SAML / LDAP / GitHub / GitLab sign-in, Git forges, SMTP. For example:

```bash
LITELLM_MODELS='[{"model_name":"claude-sonnet","litellm_params":{"model":"anthropic/claude-sonnet-5-5","api_key":"sk-ant-…"}}]'
LITELLM_DEFAULT_MODEL=claude-sonnet
SSO_OIDC_ISSUER=https://keycloak.example.com/realms/acme
SSO_OIDC_CLIENT_ID=shipcove
SSO_OIDC_CLIENT_SECRET=…
GIT_GITLAB_HOST=gitlab.example.com
GIT_GITLAB_CLIENT_ID=…
GIT_GITLAB_CLIENT_SECRET=…
```

Every variable is optional and listed in [Configuration by environment variables](docs/operations/environment.md) (commented template at the end of `.env.example`).

## How it works

```text
Browser ── nginx (web) ──► API (NestJS, ×N) ──► PostgreSQL (state, job queues, LISTEN/NOTIFY)
                                │                Vault (secrets)   S3 / Garage (checkpoints, attachments)
                                ▼
                           Worker ──► sandboxes (agent over RPC, isolated internal network)
                                │            │  backing services on the sandbox's localhost
                                ▼            ▼
                      Gateway (LLM proxy, filtered egress, Git access) ──► LiteLLM ──► providers
                      Preview gateway (separate domain) ──► sandbox ports
```

- The **worker** starts a sandbox per conversation, restores its last checkpoint from S3, runs the startup script and drives the agent. Changes are checkpointed as they happen.
- The **gateway** is the sandbox's only way out: LLM calls (with credit reservation and billing), allowlisted egress, and Git traffic, where the run token is replaced by the user's OAuth token.
- The **API** serves the web app and streams the agent's events over SSE; several replicas can run behind the load balancer.
- PostgreSQL, Vault and an S3-compatible bucket are required. Back them up together.

| Component | Role |
| --- | --- |
| `apps/web` | Angular 22 interface (signals, zoneless) and Tailwind CSS 4, served by nginx with a strict CSP |
| `apps/api` | REST API `/api/v1` (NestJS, OpenAPI), authentication, SSE, administration |
| `apps/worker` | Agent runs, sandboxes, checkpoints, Git broker, maintenance jobs |
| `apps/gateway` | LLM proxy, filtered egress proxy, Git access for sandboxes |
| `apps/preview` | Token-protected access to sandbox ports on a separate domain |
| `packages/*` | Shared Zod contracts, Drizzle schema, Docker and Kubernetes sandbox providers, checkpoint storage, Vault client, agent runtime (built on the open-source [Pi](https://github.com/badlogic/pi-mono) engine), sandbox image |

Design decisions are recorded in [`docs/adr`](docs/adr) and the full specification is in [`SPEC.md`](SPEC.md) (both in French).

## Configuration

| Where | What |
| --- | --- |
| `infrastructure/docker/.env` | Public URL, ports, preview domain, sandbox image, API replicas, initial administrator |
| Environment variables of the API (optional) | Declarative setup applied at every start: LiteLLM connection, models (created, discovered, enabled, default), SSO providers, Git forges, SMTP, platform settings. See [`docs/operations/environment.md`](docs/operations/environment.md) |
| `infrastructure/docker/.secrets/` | Bootstrap secrets (PostgreSQL, S3, LiteLLM, Vault AppRole), generated by `init-secrets.sh` |
| Vault (`cap/…`) | Application secrets: LLM keys, SMTP, OAuth, MCP, Git tokens |
| Administration console | Everything else (and everything above that is not declared by environment variable): sign-in and MFA policy, identity providers, Git forges, models, quotas, sandboxes, images, services, skills and MCP, notifications, retention |

Before exposing Shipcove on a network, put it behind TLS (the `tls` Compose profile does it with automatic certificates), set `CAP_COOKIE_SECURE=true`, and protect `.secrets/`, which holds the Vault unseal keys.

## Documentation

| For | Read |
| --- | --- |
| Using it | The documentation site in [`apps/docs-site`](apps/docs-site), in English and French: user guide, administration, architecture (`pnpm docs:dev`) |
| Deploying it | [Docker Compose](docs/operations/docker-compose.md), [Kubernetes](docs/operations/kubernetes.md), [TLS](docs/operations/tls.md), [Vault](docs/operations/vault.md), [Configuration by environment variables](docs/operations/environment.md) |
| Connecting it | [SSO (OIDC, SAML, LDAP)](docs/operations/sso.md), [Git forges](docs/operations/git-forges.md) |
| Tuning sandboxes | [Startup script](docs/operations/sandbox-startup.md), [Backing services](docs/operations/services.md) |
| Understanding it | [Architecture decisions](docs/adr), [Specification](SPEC.md), [Implementation plan](IMPLEMENTATION_PLAN.md) |

Publishing the documentation: `pnpm docs:build` produces a static site in `apps/docs-site/dist`, ready for any web host (`DOCS_BASE=/docs/ pnpm docs:build` for a subfolder). `pnpm docs:build:demo` adds the interactive demo.

## Deploying

Images are published to GitHub Container Registry (`ghcr.io/shipcove/shipcove-web`, `-api`, `-worker`, `-gateway`, `-preview`, `-docker-guard`, `-sandbox`) for `linux/amd64`, **only when a version tag is pushed**: `vX.Y.Z` publishes `X.Y.Z`, `X.Y` and `latest`; a pre-release `vX.Y.Z-rc.N` publishes only its own tag.

```bash
git tag v0.3.0
git push origin v0.3.0
```

Pin a version in production. A Helm chart in [`infrastructure/helm/shipcove`](infrastructure/helm/shipcove) deploys the application and an isolated sandbox namespace (one Pod per sandbox and per backing service, NetworkPolicies, least-privilege worker); PostgreSQL, Vault, S3 and LiteLLM stay external. A full local setup on kind is in `infrastructure/kubernetes/dev/up.sh`.

## Development

Requires Node.js 26 and pnpm 12.18.

```bash
pnpm install
pnpm dev:infra          # PostgreSQL, Vault, Garage, LiteLLM, Mailpit, mock LLM
pnpm build              # all packages
pnpm typecheck && pnpm lint
pnpm test               # unit and integration tests (Vitest)
pnpm images:build       # build every image locally
```

End-to-end tests run against the real Compose stack: `cd tests/e2e && pnpm test`. They cover the stack, the interface (Playwright, strict CSP), Git against a real GitLab, SSO against real Keycloak and OpenLDAP, Kubernetes on kind, and resilience (API, worker, S3, LiteLLM and Vault failures). Optional test providers, from `tests/e2e`: `pnpm sso:up` (Keycloak and OpenLDAP) and `pnpm forge:up` (GitLab CE); without them, the matching suites are skipped.

The interface is translated: write UI text in French with `t('…')` and add its English translation to `apps/web/src/app/i18n/en.ts`. `pnpm lint` fails if a translation is missing. Only dependency versions published more than two weeks ago are accepted, and install scripts are blocked by default.

## Current limitations

The specified feature set is implemented and tested end to end on Docker Compose; the Helm chart is validated on a kind cluster. Before production use, plan for:

- **Internal traffic encryption** for multi-host deployments (TLS to PostgreSQL and Vault). Public TLS is provided by the `tls` profile.
- **Backup and restore tooling** for PostgreSQL, Vault and S3.
- **Observability**: metrics, OpenTelemetry tracing, alerting.
- **Kubernetes in production**: validation on a multi-node cluster with Calico or Cilium and gVisor or Kata, PodDisruptionBudgets.
- **Sandbox images**: internal registry, compliance checks, dependency caches.
- **CI, load testing and an external security audit.** An internal review has been done.

## License

Shipcove is free software under the **GNU Affero General Public License v3** ([`LICENSE`](LICENSE)), with additional terms under section 7 described in [`NOTICE`](NOTICE):

- **Attribution**: a modified version must show “Based on Shipcove — https://github.com/Shipcove/shipcove” in its interface.
- **Source code**: anyone offering a modified version to users over a network must give them access to its source code (AGPL section 13).
- **Trademark**: the license grants no rights to the Shipcove name or logo; a modified version distributed or hosted for others must use another name. See the [trademark policy](TRADEMARKS.md).
