# Null AI

**The open-source AI pentester.** Null AI plans the test, runs real security tools in a sealed sandbox, proves what it finds, and writes the report. It runs on your computer, with your model.

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-yellow.svg)](LICENSE)
![Runs with Docker](https://img.shields.io/badge/runs%20with-docker%20compose-black.svg)
![Node.js 22](https://img.shields.io/badge/node-22-black.svg)

![Null AI home: choose Pentest, Compliance or Code Review and start a run on a verified target](docs/images/home.png)

[Quick start](#quick-start) · [Connect a model](#connect-a-model) · [Your first test](#your-first-test) · [How it works](#how-it-works) · [Safety](#safety)

## What it does

- **Pentest.** Maps the attack surface, then tests it the way a person would: recon, enumeration, then the weaknesses that fit what it found. A finding counts only once a separate validation step proves it.
- **Code review.** Reads your code from a folder on this computer or a public git URL, pinned to one commit. Give a pentest the code too and it tests whitebox.
- **Compliance.** Readiness reviews for SOC 2, ISO 27001, NIST CSF, PCI DSS, HIPAA and GDPR, from the evidence you give it.
- **Reports.** Every finding keeps its proof. Reports render to PDF on your computer.

The agent works with 55 tools in its sandbox (nmap, nuclei, sqlmap, ffuf, semgrep, trivy, a real browser and more) and 108 skills: the know-how for JWT attacks, IDOR, request smuggling, GraphQL, OAuth, cloud, Kubernetes and the frameworks it meets.

## Quick start

You need [Docker](https://docs.docker.com/get-docker/) (Engine 28.1 or later, or a current Docker Desktop) and git.

```sh
git clone https://github.com/Null-Square/null-agent.git
cd null-agent
docker compose --profile lab up -d
docker compose logs backend | grep '#key='
```

Open the link it prints, `http://localhost:8080/#key=…`. It signs this browser in as you, so keep it to yourself. The first start builds the images; the sandbox image takes the longest.

Setup asks for four things: your model, your organization, your website, and your authorization to test it.

`--profile lab` also starts [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), a deliberately vulnerable app to practise on. Leave it out once you test your own sites.

## Connect a model

![Settings, Model: Continue with ChatGPT, Claude with an API key, or another provider](docs/images/model.png)

Pick one in setup, or later in **Settings → Model**:

| Option | What you need |
| --- | --- |
| **Continue with ChatGPT** | Your ChatGPT plan. You sign in at OpenAI. A workspace admin may have to allow third-party apps first. |
| **Claude** | A [Claude API key](https://platform.claude.com/docs/en/get-api-key). |
| **Another provider** | An API key for OpenAI, DeepSeek, Qwen or Moonshot. The model list comes from the provider's own catalog. |

Anything else, such as Ollama or your own gateway, goes in [`services/backend/config/seeds/models.seed.json`](services/backend/config/seeds/README.md). A key in `.env` (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, and so on, see [`.env.example`](.env.example)) connects on start.

Your provider receives what the agent sends it. Nothing else leaves your computer by itself.

## Your first test

![A scope for Juice Shop: verified, with its code connected for a whitebox test](docs/images/scope.png)

1. In setup, enter `juice-shop.lab` as the website and choose **Verify & start discovery**. It passes at once, as a practice target.
2. Optional: in the scope's **Code**, add `https://github.com/juice-shop/juice-shop.git`. The test becomes whitebox, and **Code review** can read it.
3. On **Home**, choose **Pentest** and **Start**. Follow the run under **Assessments**, then open what it proved under **Risks**.

For a real site, Null AI first checks that it is yours: a DNS TXT record or a file on the site. Test only what you own or have written permission to test.

## How it works

```
 you ── objective ──▶ planner ──▶ executors ──▶ validation ──▶ findings ──▶ report
                          │            │
                          ▼            ▼
                       skills    sandbox (tools, browser)
```

- The **planner** breaks your objective into steps. **Executors** carry them out with the tools in the sandbox and record what they find: assets, services, leads.
- A lead becomes a **finding** only when a separate validation step proves it. Each finding keeps its evidence.
- **Rules of engagement** on each scope say what must not be tested and how far a proof may go.
- Everything is stored in Postgres on your computer. Runs, traces and workspaces go to local S3-compatible storage.

## Safety

- **Only you.** The app answers on `127.0.0.1` only, and only to a browser holding your owner key.
- **A sealed sandbox.** Each sandbox reaches the internet and the lab, never your database, the app, your computer's own services or your network.
- **Verified targets only.** The agent tests what you proved is yours, within the scope's rules.

[SECURITY.md](SECURITY.md) has the details and how to report a vulnerability.

## Develop

You need Node.js 22.18 or later and Docker.

```sh
npm ci
npm run dev
```

`npm run dev` starts Postgres, storage and the sandbox gateway in Docker, then runs the backend and the app from source. Open the link the backend prints. Before a pull request, run `npm run typecheck` and `npm test`. See [CONTRIBUTING.md](CONTRIBUTING.md).

| Path | What it is |
| --- | --- |
| `services/backend` | The API, the agent, the sandbox control and the database |
| `services/frontend` | The app |
| `services/sandbox` | The image the agent's tools run in |
| `services/shell-server` | The private runner's bridge, which the sandbox image runs |
| `packages/contracts`, `packages/design-tokens` | Shared types and UI |

## Credits

Null AI is the platform [NullSquare](https://nullsquare.net) built, released for one person to run on their own computer. Some skills and prompt lines are adapted from [Strix](https://github.com/usestrix/strix); [NOTICE](NOTICE) lists every credit and licence.

Licensed under [Apache 2.0](LICENSE).
