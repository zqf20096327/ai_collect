# Aura Agent

![Aura Dashboard](./dashboard.png)

**Aura** is an autonomous task orchestrator designed for ambitious, long-running projects that demand deep multi-faceted exploration — automatically decomposing complex goals into concrete subtasks, routing them to Pro or Flash Layer 2 workers, and continuously verifying results against acceptance criteria over hours or days of autonomous operation. It supports secure Docker-based execution, flexible API configuration, and multiple worker backends such as `Claude Code`, `Qwen Code`, `Codex CLI`, `ds_code`, and `OpenCode`.

---

## Architecture

![Aura Architecture Overview](./aura_architecture.png)

---

## Quick Start (Under 2 Minutes)

```bash
git clone https://github.com/erickong/aura-agent
cd aura-agent
python -m pip install -e .

# Run interactive setup to configure API keys and models
aura setup

# Go to your project
cd /path/to/your/project

# Create your task file (task.md for example), describe your goal.
# Aura your goal
aura start --task-file task.md
```

Edit `task.md` anytime while Aura is running. The agent detects changes, replans, and continues work automatically.

By default Aura starts with the Rich terminal dashboard. Use `--no-ui` for plain command-line output:

```bash
aura start --task-file task.md --no-ui
```

If Docker is enabled in your config but you want to run workers locally for one session:

```bash
aura start --task-file task.md --no-docker
```

Choose a worker delegation mode per run:

```bash
aura start --task-file task.md --worker-mode auto
aura start --task-file task.md --worker-mode flash-first

# Use local Codex CLI as the Pro worker for this run
aura task.md --workerpro-codex
aura start --task-file task.md --worker-mode pro-only
```

### Installation Notes

Aura does not pin a package index. `python -m pip install -e .` uses the user's local pip configuration, such as PyPI, a corporate mirror, or a regional mirror.

If editable install fails while installing build dependencies such as `setuptools` or `wheel`, the configured package index may be incomplete or unreachable. Use a working index, for example:

```bash
python -m pip install -e . --index-url https://pypi.org/simple
```

If `setuptools` and `wheel` are already installed in the environment, this can also avoid downloading isolated build dependencies:

```bash
python -m pip install -e . --no-build-isolation
```

---

## Pro / Flash Workers

Aura can use two independent Layer 2 worker roles:

| Worker | Purpose | Typical backend |
| ------ | ------- | --------------- |
| Pro | Rare expert path for very hard, long-context, high-risk, proof-heavy, or architecture-level tasks | Claude Opus/Sonnet, DeepSeek Pro |
| Flash | Default path for ordinary bounded work: simple and medium coding, debugging, scripts, focused analysis, tests, and normal docs | Qwen Coder, Claude Haiku |

The intended default is economical: use Flash for most clear, bounded tasks, and reserve Pro for tasks where the main risk is reasoning quality rather than execution effort. Modern Flash models can be strong; they are not only for trivial chores.

Worker modes:

| Mode | Behavior |
| ---- | -------- |
| `pro-only` | Everything goes to Pro. |
| `auto` | Aura routes ordinary bounded tasks to Flash and genuinely hard tasks to Pro. |
| `flash-first` | Aura tries Flash first and escalates to Pro only after a clear model-capability failure. |
| `flash-only` | Everything goes to Flash. |

Pro and Flash are configured separately: backend, API key, base URL, and model do not interfere with each other. For example, Pro can use `claude` while Flash uses `qwencode`.

For a one-off non-Docker run with your already configured local Codex CLI, pass `--workerpro-codex`. Aura will use Codex as the Pro worker and print the Codex model detected from `~/.codex/config.toml` at startup. If your config enables Docker workers, add `--no-docker`; otherwise Aura will stop with a clear error because local Codex is not a Docker worker backend.

Important: a Flash worker still needs real tool capability. It must be able to read/write files, run commands, use the project workspace, and produce final artifacts through its CLI backend. A cheap model without basic coding-agent tools is not a useful Flash worker for Aura.

For Qwen Code workers, Aura sets `QWEN_CODE_MAX_OUTPUT_TOKENS` from `AURA_QWENCODE_MAX_OUTPUT_TOKENS` (default `25000`). This avoids OpenAI-compatible servers such as vLLM rejecting requests because Qwen Code reserves a 32K/64K output budget on top of an already long prompt.

---

## Docker Isolation (Optional)

When enabled, Aura runs Layer 2 workers in Docker:

* Each worker runs in a separate container with a clean `/workspace`.
* Non-root user prevents host file or system access.
* Resource limits (CPU, memory, GPU) ensure rogue processes stay contained.
* Pre-built image automatically pulled from GHCR.

Configuration in `.env` or via `aura setup`:

```text
AURA_WORKER_MODE=auto
AURA_PRO_BACKEND=claude
AURA_PRO_API_KEY=<pro-key>
AURA_PRO_BASE_URL=<pro-base-url>
AURA_PRO_MODEL=<pro-model>
AURA_FLASH_BACKEND=qwencode
AURA_FLASH_API_KEY=<flash-key>
AURA_FLASH_BASE_URL=<flash-base-url>
AURA_FLASH_MODEL=<flash-model>
AURA_WORKERS_IN_DOCKER=1
AURA_DOCKER_BIN=docker
AURA_DOCKER_GPUS=all
AURA_DOCKER_EXTRA_ARGS=
```

Docker GPU access is controlled by `AURA_DOCKER_GPUS`:

| Value | Effect |
| ----- | ------ |
| empty | Do not pass GPU access to Docker. CPU-only worker containers. |
| `all` | Pass all visible GPUs to worker containers (`docker run --gpus all`). |
| `device=0` | Pass only GPU 0. Other Docker `--gpus` values are also accepted. |

For finer control, `AURA_WORKER_CUDA_VISIBLE_DEVICES` sets `CUDA_VISIBLE_DEVICES` inside workers, while `AURA_WORKER_MAX_GPU_UTIL_PERCENT`, `AURA_WORKER_MAX_GPU_MEMORY_PERCENT`, and related resource settings control Aura's worker guard.

### Docker Image

The default image is `ghcr.io/erickong/aura-claude-cuda:latest`. Aura pulls it automatically on first use.

**If the automatic pull fails** (e.g., network issues, registry rate limits), pull it manually:

```bash
docker pull --platform linux/amd64 ghcr.io/erickong/aura-claude-cuda:latest
```

### Rebuilding with Custom Packages

To add your own Python or system packages to the Docker image, use the files in [docker_scripts/](./docker_scripts/):

1. Edit `docker_scripts/requirements.txt` to add your pip packages.
2. Edit `docker_scripts/Dockerfile` to add system packages or other dependencies.
3. Rebuild the image:

```bash
# Linux / macOS
bash docker_scripts/rebuild.sh

# Windows PowerShell
powershell -File docker_scripts/rebuild.ps1
```

The rebuild scripts tag the image as `ghcr.io/erickong/aura-claude-cuda:latest` locally, which Aura will use instead of pulling from the registry.

---

## Comparison with Other Agents

| Dimension           | Codex Goal                              | Aura Agent                                | GitHub Copilot Cloud Agent                  | Claude Chat                      |
| ------------------- | --------------------------------------- | ----------------------------------------- | ------------------------------------------- | -------------------------------- |
| **System level**    | Inside Codex                            | Above coding agents                       | Inside GitHub                               | General assistant                |
| **Task unit**       | One durable goal                        | Markdown goal → task tree                 | Issue / prompt → branch or PR               | Chat prompt                      |
| **Execution style** | Keep working until verifiable end state | Orchestrator spawns bounded workers       | Cloud agent edits branch and can open PR    | Interactive reasoning            |
| **Parallelism**     | Limited                                 | Explicit Layer 2 workers                  | Multiple sessions possible, but PR-centered | None by default                  |
| **Verification**    | Tests, logs, artifacts, benchmarks      | Evidence from artifacts/logs/result files | Diff, commits, tests, PR review             | User review                      |
| **Best fit**        | Focused repo work                       | Long-horizon autonomous projects          | Team software workflow                      | Thinking, drafting, analysis     |

---

## Example Use Cases

* Build a quantitative trading pipeline from scratch, testing multiple models until target Sharpe ratio is achieved.
* Generate research reports, whitepapers, or documentation automatically.
* Automate repetitive coding or data processing tasks with minimal supervision.

---

## FAQ / Common Issues

### Docker image pull fails (all workers blocked or failed)

If workers won't start and logs show Docker pull failures:

```bash
# Manually pull the image
docker pull --platform linux/amd64 ghcr.io/erickong/aura-claude-cuda:latest

# Or run without Docker entirely
aura start --task-file task.md --no-docker
```

This is the most common cause of "all task nodes blocked or failed" — the orchestrator retries spawns but the image never becomes available. After a pull failure, Aura auto-falls back to local mode for the rest of the session.

### Docker not installed (macOS / Linux)

macOS does not ship with Docker. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) or use `--no-docker` to run workers locally:

```bash
aura start --task-file task.md --no-docker
```

To permanently disable Docker, set in `.env`:

```text
AURA_WORKERS_IN_DOCKER=0
```

### macOS Terminal rendering glitches

macOS Terminal.app may not render the Rich dashboard correctly. Aura defaults to plain mode on macOS. If you want to try the dashboard, use a modern terminal (iTerm2, Warp, Kitty) and force Rich mode:

```bash
aura start --task-file task.md --ui rich
```

### API connection errors

If Aura cannot reach the LLM API, re-run interactive setup to configure endpoints and keys:

```bash
aura setup
```

Common checks:
- `AURA_API_BASE_URL` ends with `/anthropic` for DeepSeek-compatible proxies
- `AURA_API_KEY` is the correct API key for the configured endpoint
- `AURA_API_MODEL` matches a model available on the configured endpoint

### Workers spawn but do nothing (stuck at 0% CPU)

This is usually a config or environment issue inside the worker. Check:
- The configured Pro/Flash backend CLI is installed (`claude`, `qwen`, `ds-code`, `opencode`, or `codex`)
- `AURA_PRO_BACKEND` / `AURA_FLASH_BACKEND` matches an installed CLI
- The worker API key, base URL, and model are reachable
- For Flash workers: the backend must still support basic agent tools such as file reads/writes and command execution

### Verbose logging

To see more detail about what Aura is doing, check the state files:

```bash
# Decision log — every status change with reasons
cat .aura/<project>/state/decision_log.json

# Full prompt sent to the LLM each cycle
cat .aura/<project>/state/current_prompt.md

# Progress report with task tree and token stats
cat .aura/<project>/state/progress.md
```

---

## Topics / Tags (GitHub)

`ai-agents`, `coding-agent`, `deepseek`, `docker`, `autonomous-agents`, `Claude`, `OpenCode`, `ds_code`

---
