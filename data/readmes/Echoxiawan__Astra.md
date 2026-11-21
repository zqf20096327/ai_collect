<div align="center">

<img src="frontend/public/logo.svg" width="300" alt="Astra">

# Astra

_AI-powered UI automation testing for real Android and iOS devices_

[![License](https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue](https://img.shields.io/badge/Vue-2.7-4FC08D?style=flat-square&logo=vue.js&logoColor=white)](https://vuejs.org/)
[![Appium](https://img.shields.io/badge/Appium-2-662D91?style=flat-square)](https://appium.io/)
[![Platform](https://img.shields.io/badge/device-Android%20%7C%20iOS-lightgrey?style=flat-square)]()
[![Docker](https://img.shields.io/badge/deploy-Docker%20Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](./docker-compose.yml)

English · [简体中文](./README.zh-CN.md) · [User Guide](./docs/user-guide.md) · [Contributing](./CONTRIBUTING.en.md) · [Security](./SECURITY.md)

</div>

Astra is an open-source UI automation platform for real Android and iOS devices. Testers describe preconditions, actions, and assertions in natural language. Astra combines multimodal AI with Appium to understand the screen, locate elements, and perform actions. Stable cases can be exported as standalone pytest + Appium scripts for repeatable regression without further AI calls.

Astra manages devices, app versions, cases, suites, plans, executions, and reports. Every successful AI run becomes a downloadable, auditable script. Devices, model endpoints, object storage, and runtime data stay under the control of the deployment.

See the [user guide](./docs/user-guide.md) for the full UI and workflow.

## Workflow

```mermaid
flowchart LR
    C["Natural-language case"] --> A["AI screen understanding"]
    A --> E["Appium actions on device"]
    E --> R["Step logs / screenshots / assertions"]
    E -->|successful run| S["Standalone pytest + Appium script"]
    S --> P["Script regression"]
    R --> P
    P --> D["Execution records and reports"]
```

Astra has two execution modes:

| Mode | Uses AI | Best for | Script behavior |
| --- | --- | --- | --- |
| AI execution | Yes | New cases, exploration, initial script generation | Generates a script after a manual, non-debug single-case success |
| Script execution | No | Stable daily and batch regression | Never generates or overwrites scripts |

## Features

- **AI execution and script capture** — Multimodal models read the page tree and screenshots; successful traces become standalone pytest + Appium scripts.
- **Multi-device scheduling** — Serial execution per device, parallel execution across devices, filtered by platform, group, tag, or explicit device.
- **Complete test management** — Apps, versions, modules, cases, suites, plans, schedules, executions, and reports.
- **Platform and language variants** — Android and iOS scripts are stored separately by target app language.
- **Per-host iOS signing** — Each Appium host can have its own Xcode Org ID, signing identity, and Keychain password.
- **Echobench import** — Import `app-steps.py` and AI case CSV exports into Astra cases and platform scripts.
- **Observability** — Step logs, screenshots, assertions, failure reasons, worker monitoring, operation logs, and Feishu notifications.
- **Deployable open source** — Docker Compose runs web, API, worker, and beat; Appium and the device agent remain independent device-host processes.

## Quick start

### Prerequisites

- MySQL 8.x with `utf8mb4`.
- Redis 6.x reachable from the API and Celery workers.
- Appium 2 with UiAutomator2 or XCUITest.
- An OpenAI-compatible multimodal model endpoint.
- An Alibaba Cloud OSS bucket for screenshots, packages, and scripts.
- LDAP for production login; `TEST_USERS` is for local development only.
- Docker Engine and Docker Compose v2 for the Compose deployment.

### Docker

```bash
git clone <repository-url>
cd Astra
cp backend/.env.example backend/.env
# Fill in MySQL, Redis, AI, and OSS settings
docker compose up -d --build

# Apply migrations when upgrading an existing database
docker compose exec backend alembic upgrade head
```

Verify the API:

```bash
curl http://localhost:8000/api/health
# {"status":"ok","service":"Astra"}
```

Open `http://localhost:3011`. Compose starts `frontend`, `backend`, `celery-worker`, and `celery-beat`; MySQL, Redis, Appium, OSS, and the AI endpoint are external dependencies.

### Device host

Every host connected to real devices must run Appium and the device agent. Both live in `runtime/` at the repository root:

| Entry | Purpose | Port |
| --- | --- | --- |
| `runtime/appium.sh` | Install, start, stop, and diagnose Appium 2 | 4723 |
| `runtime/device_agent.py` | Device discovery, ADB/iOS operations, WDA, and Keychain | 5070 |
| `runtime/celery.sh` | Worker and Beat for non-Docker deployments | None |
| `runtime/kill_celery.sh` | Force-stop Celery Worker and Beat | None |

First Appium start:

```bash
./runtime/appium.sh install
./runtime/appium.sh start
```

Start the device agent in another terminal:

```bash
source .venv/bin/activate
python runtime/device_agent.py
```

Verify both services:

```bash
curl http://127.0.0.1:4723/status
curl http://127.0.0.1:5070/health
```

In the UI, open **Device Center → Appium Servers → Add Server** and enter an Appium URL reachable by both the Astra API and Worker, such as `http://192.0.2.10:4723`. Astra derives the device agent on port `5070` from the same hostname; there is no separate agent URL field.

> **Test Connection** checks only Appium `/status`. The device agent may still be down. Run **Manual Sync** on the device page and confirm that real devices appear. See the [runtime guide](./runtime/README.md).

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
```

Initialize the database and start the API:

```bash
cd backend
alembic upgrade head
python run.py
```

Start the frontend in another terminal:

```bash
cd frontend
npm install
npm run serve
```

For non-Docker deployments, start Celery Worker and Beat:

```bash
./runtime/celery.sh start all
./runtime/celery.sh status
```

## Importing Echobench exports

Astra imports two artifact types exported by [Echoxiawan/echobench](https://github.com/Echoxiawan/echobench):

| File | Echobench export | Purpose |
| --- | --- | --- |
| `*-test-case.csv` | "AI Case" export | Create and bind the target case |
| `app-steps.py` | "Export Script → Python (Appium)" | Import an executable platform script |

The CSV columns are exactly `用例标题,序号,操作步骤,断言` (case title, step number, operation, assertion). Each row is one step; assertions may be empty. The PY file contains `PLAN = json.loads("...")`; Astra only extracts that constant and never executes code from the file.

Open **Test Cases → Import Script**.

- Script only: select `app-steps.py` and link an existing case.
- CSV and PY together: upload `app-steps.py`, choose "Create case from CSV and bind", then upload the CSV and fill in the app, module, preconditions, and postconditions. Astra creates the case first and then binds the script.
- CSV only: use **Test Cases → Import** to create cases without a script.

The UI previews each step's locator and assertion. Coordinate locators, missing element locators, and unsupported actions are reported explicitly. Re-importing the same platform and language for a case replaces the previous imported script; AI-generated scripts are unaffected.

## Configuration

See [`backend/.env.example`](./backend/.env.example) for all documented defaults. Common variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `DATABASE_URL` | `mysql+pymysql://astra:change-me@localhost:3306/astra` | MySQL connection |
| `REDIS_URL` | `redis://localhost:6379/2` | Cache and inter-process notifications |
| `CELERY_BROKER_URL` | `redis://localhost:6379/3` | Celery broker |
| `CELERY_RESULT_BACKEND` | `redis://localhost:6379/4` | Celery result backend |
| `CELERY_QUEUE_NAMESPACE` | empty | Queue namespace for shared Redis deployments |
| `OPENAI_CONFIGS` | empty | Multiple OpenAI-compatible providers as single-line JSON |
| `OPENAI_API_KEY` | empty | API key for the single-provider configuration |
| `OPENAI_API_BASE` | empty | Model endpoint base URL |
| `OPENAI_MODEL` | `gpt-4o` | Vision model name |
| `OSS_ACCESS_KEY_ID` | empty | Alibaba Cloud OSS access key ID |
| `OSS_ACCESS_KEY_SECRET` | empty | Alibaba Cloud OSS access key secret |
| `OSS_REGION` | `cn-shenzhen` | OSS region |
| `OSS_BUCKET_NAME` | empty | OSS bucket |
| `LDAP_SERVER` | `ldap://localhost:389` | LDAP endpoint |
| `JWT_SECRET_KEY` | `change-me-in-production` | JWT signing key; replace in production |
| `TEST_USERS` | empty | Local users that bypass LDAP; disable in production |
| `BASE_URL` | `http://localhost:8000` | External URL for reports and package downloads |
| `DEFAULT_APPIUM_URL` | `http://localhost:4723` | Default Appium node |
| `IOS_XCODE_ORG_ID` | empty | Global fallback Apple Team ID |
| `IOS_XCODE_SIGNING_ID` | `Apple Development` | Global fallback signing identity |
| `IOS_KEYCHAIN_PASSWORD` | empty | Legacy global Keychain password fallback |

Never commit `backend/.env` or write OSS, LDAP, AI, or device credentials into images, logs, or issues.

## Repository layout

```text
Astra/
├── runtime/                 # Independent Appium, device-agent, and Celery entries
│   ├── appium.sh
│   ├── device_agent.py
│   ├── celery.sh
│   └── kill_celery.sh
├── backend/
│   ├── app/api/             # HTTP API and WebSocket
│   ├── app/core/            # Execution engine, assertions, sessions, AI, logging
│   ├── app/services/        # Devices, AI, OSS, reports, and domain services
│   ├── app/tasks/           # Celery Worker and Beat tasks
│   ├── migrations/          # Alembic migrations
│   └── tests/               # pytest suite
├── frontend/                # Vue 2 UI and Nginx configuration
├── docker-compose.yml       # Web, API, Worker, and Beat
└── docs/                    # User guide, screenshots, and contact details
```

## FAQ

**Appium is online but the device list is empty.**

Verify that the device agent is running and reachable at `http://device-host:5070/health` and `/devices` from both the API and Worker networks. Then run **Manual Sync**. Android also requires ADB authorization; iOS requires a ready WDA.

**Containers cannot reach MySQL, Redis, or Appium.**

`localhost` inside a container refers to the container itself. On macOS/Windows use `host.docker.internal`; on Linux use a host address reachable from the Docker network and open the required ports.

**AI execution succeeds but no script is generated.**

Script generation requires OSS. Check `OSS_ACCESS_KEY_ID`, `OSS_ACCESS_KEY_SECRET`, `OSS_REGION`, and `OSS_BUCKET_NAME`. Only a manual, non-debug single-case success generates a script.

**The first iOS build fails.**

Check Xcode, the developer certificate, device trust, and WebDriverAgent signing. Configure signing per Appium host in the UI; `IOS_XCODE_ORG_ID` is only a global fallback.

**How do the Echobench CSV and PY files differ?**

The CSV is the AI case export used to create and bind the target case. The PY file is `app-steps.py`, used to import the executable platform script. You can use both together or import only one.

## Security

See [SECURITY.md](./SECURITY.md) for supported versions and vulnerability reporting.

- Appium and the device agent have no built-in authentication. Keep them on a trusted network and never expose them publicly.
- The device agent exposes privileged ADB, WDA, and Keychain operations. Run it only on controlled device hosts.
- Replace `JWT_SECRET_KEY`, database passwords, Redis passwords, and all sample credentials in production.
- Never store real passwords, tokens, device UDIDs, or business data in cases, logs, screenshots, or issues.

## Contributing

Issues, pull requests, and documentation improvements are welcome. Read [CONTRIBUTING.en.md](./CONTRIBUTING.en.md) and sign the [CLA](./CLA.md) before your first contribution. Corporate contributors use the [CCLA](./CCLA.md).

When a pull request is opened or updated, the CLA bot comments with the signature template and sets the `CLA Assistant` status check. Reply in the PR with the template; the bot validates the comment author, exact declaration, GitHub username, and date. Maintainers add the `cla-corporate` label after confirming a corporate CCLA.

Community expectations are described in [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## Contact

<table>
<tr>
<td align="center" width="33%">
<img src="docs/contact/wechat-personal.png" alt="Author's WeChat QR code" width="260"><br>
<b>Author's WeChat</b><br>
<sub>Please mention Astra when adding</sub>
</td>
<td align="center" width="33%">
<img src="docs/contact/wechat-official.png" alt="WeChat Official Account QR code" width="260"><br>
<b>WeChat Official Account</b><br>
<sub>Follow for project updates and articles</sub>
</td>
<td align="center" width="33%">
<a href="https://x.com/AiYouyisi"><img src="https://img.shields.io/badge/X-%40AiYouyisi-black?style=flat-square&logo=x&logoColor=white" alt="X (Twitter) @AiYouyisi"></a><br>
<b>X (Twitter)</b><br>
<sub>Follow for project news</sub>
</td>
</tr>
</table>

<sub>The QR codes are for project communication. Please read the FAQ before filing an issue.</sub>

## License

Astra is licensed under the [Apache License 2.0](./LICENSE).

Redistributions must retain the copyright notice, [LICENSE](./LICENSE), and [NOTICE](./NOTICE), and must indicate changes.

## Acknowledgments

Astra builds on Appium, FastAPI, SQLAlchemy, Celery, Vue, Element UI, and Alibaba Cloud OSS. Echobench provides a mobile recording and export workflow; Astra imports its AI case CSV and Python script exports.
