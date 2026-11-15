# BugTrace-Agent

A bug-fixing workflow demo with a static web interface and a Python API. Follow a sample authentication bug from failing checks to a proposed fix and human review.

[Quick start](#quick-start) · [GitHub Pages](#github-pages) · [API](#api) · [Release notes](CHANGELOG.md)

## What you can run

| | Browser demo | Python backend |
| --- | --- | --- |
| Interface | HTML, CSS, JavaScript | FastAPI with interactive API docs |
| Setup | Open `docs/index.html` | Install Python dependencies |
| Verification | Four JavaScript checks on equivalent login logic | Runs pytest against the Python sample |
| Fix | Predefined Python proposal | Predefined fix in demo mode |
| Review | Local approval and file download | Approval endpoint and run status |
| Hosting | GitHub Pages or any static host | A server that runs Python |

**The working demo is deterministic.** Gemini and Vertex AI integrations are experimental; they do not yet provide a complete, verified autonomous debugging loop. Approval is simulated and does not create a pull request, merge, or push code.

## Quick start

Clone the release:

```sh
git clone --branch v2.0.0 https://github.com/ayushcmd/bug-trace-agent.git
cd bug-trace-agent
```

This checks out the release tag. For ongoing development, use the `static-website` branch.

### Browser demo

Open [`docs/index.html`](docs/index.html) in your browser. No installation, build step, or API key is needed.

1. Select **Trace sample bug**.
2. Inspect the failing baseline and proposed credential-validation fix.
3. Review the four passing browser checks.
4. Select **Approve demo fix** to download `auth.py`.

The demo runs locally in your browser and resets when refreshed. It does not execute Python or send code to an AI service. Google Fonts is optional; system fonts work offline.

### Python backend

The local demo was verified with Python 3.14.3. Use a virtual environment to isolate dependencies; the project does not currently pin package versions.

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:DEMO_MODE = "true"
$env:HOST = "127.0.0.1"
.\.venv\Scripts\python.exe run_local.py
```

**macOS / Linux**

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
DEMO_MODE=true HOST=127.0.0.1 .venv/bin/python run_local.py
```

Open [http://localhost:8080/docs](http://localhost:8080/docs) for the interactive API, or [http://localhost:8080/](http://localhost:8080/) for its health response. The Python server serves the API; the static website is a separate interface.

## GitHub Pages

The `docs/` directory is ready for static hosting:

1. Open the repository's **Settings → Pages**.
2. Set the source to **Deploy from a branch**.
3. Select **static-website** and **/docs**, then save.
4. Use the published URL shown by GitHub when deployment completes.

See the [hosting guide](docs/HOSTING.md) for details. GitHub Pages serves the browser demo only; it cannot run the FastAPI backend. Keep `.env` files and API keys outside the published directory.

## How the backend demo works

1. Accept a bug report through `/start_run`.
2. Retrieve the sample authentication file using keyword matching.
3. Run the sample pytest suite to observe the existing bug.
4. Temporarily apply a predefined credential-validation fix and run pytest again.
5. Restore the original sample file and retain the proposal and test output in memory.
6. Wait for approval, then mark the run complete.

The sample is deliberately buggy so the workflow can be repeated. The demo temporarily edits a shared file: run one demo request at a time. Approval changes session status only.

## API

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/` | Health, version, and selected provider |
| `POST` | `/start_run` | Start a bug-fixing run |
| `GET` | `/status/{issue_id}` | Inspect status, proposal, logs, and test output |
| `GET` | `/runs` | List in-memory runs |
| `POST` | `/approve/{issue_id}` | Complete a run awaiting review (simulated approval) |

Example request body for `/start_run`:

```json
{
  "issue_id": "BUG-101",
  "description": "Login in auth.py accepts invalid passwords and unknown users"
}
```

In demo mode, a successful run reaches `awaiting_approval`. Inspect `/status/BUG-101` before calling `/approve/BUG-101`.

## Configuration

Settings load from environment variables and an optional root `.env` file. Existing environment variables take precedence.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DEMO_MODE` | `false` | Set to `true` for the reproducible offline backend demo |
| `HOST` | `0.0.0.0` | Bind address; use `127.0.0.1` for local development |
| `PORT` | `8080` | API port |
| `ENVIRONMENT` | `development` | Environment label |
| `LOG_LEVEL` | `INFO` | Logging level |
| `GEMINI_API_KEY` | Empty | Selects the experimental Gemini API path |
| `GCP_PROJECT_ID` | Empty | Google Cloud project for the experimental Vertex path |
| `GCP_LOCATION` | `us-central1` | Vertex region |
| `GOOGLE_APPLICATION_CREDENTIALS` | Unset | Credential file path required by the current Vertex provider selection |

Provider selection: forced demo → Gemini key → GCP project plus credential path → demo fallback. Provider exceptions also fall back to the sample demo. Check the run's `provider` field to see what actually handled it. Use `.env.example` as a reference, replacing or removing placeholder credentials before enabling an AI provider.

## Verification

Run the API integration suite in demo mode:

```powershell
# Windows PowerShell
$env:DEMO_MODE = "true"
.\.venv\Scripts\python.exe -m pytest tests -q
```

```sh
# macOS / Linux
DEMO_MODE=true .venv/bin/python -m pytest tests -q
```

The suite covers health, request validation, the demo workflow, and unknown-issue approval. All four API tests passed during local verification.

Running plain `pytest` also collects `sample_target/test_auth.py`, which intentionally fails against the original buggy sample. Use `tests/` for the integration suite; the agent runs the sample tests before and after its temporary fix.

The browser demo was checked for tracing, verification, approval, and reset. JavaScript syntax can also be checked with `node --check docs/app.js` if Node.js is installed.

## Project layout

```text
app/
  config.py           Environment settings and provider selection
  main.py             FastAPI routes and request models
  engine/agent.py     Demo workflow and experimental AI integrations
  engine/memory.py    In-memory run state
  tools/rag.py        Sample retrieval using keyword matching
  tools/runner.py     Pytest subprocess runner
docs/                 Static website and hosting guide
sample_target/        Intentionally buggy login and its tests
tests/                API integration tests
run_local.py          Local API launcher
requirements.txt      Python dependencies
```

## Current limitations

- Retrieval uses sample keyword matching, not vector search or repository-wide semantic indexing.
- AI provider paths are incomplete. Their success messages are not evidence of an applied or tested fix.
- There is no GitHub integration for creating, merging, or pushing fixes.
- Run history is held in memory and disappears when the server restarts.
- The backend has no authentication or isolated code-execution sandbox. It is a development prototype, not a public production service.

Next steps include a verified AI tool loop, isolated per-run workspaces, persistent run history, authentication, and repository integration.

## Author

Built by **Ayush Raj** at **IIT Patna**, studying BS in Computer Science & Data Analytics. The project earned **3rd place at the Hack-N-Tech 24-hour hackathon** during its author's first year.

GitHub: [@ayushcmd](https://github.com/ayushcmd)
