# Email classificator

Turn unread Gmail messages into a labeled to-do list: reply, read, skip, or flag as spam. Powered by a local LLM through Ollama.

| Without labels | With labels |
| --- | --- |
| ![Gmail without labels](docs/images/gmail_without_labels.png) | ![Gmail with labels](docs/images/gmail_with_labels.png) |

## How it works

The classifier fetches unread messages received within the last 14 days that do not
already have one of its labels. It normalizes their content, asks Ollama to choose
one label, and applies that label in Gmail. The search is not limited to the Inbox.

| Label | Intended meaning |
| --- | --- |
| `is_spam` | Scams, phishing, deceptive messages, or unsolicited junk. |
| `need_reply` | A legitimate message that needs a personal response. |
| `to_read` | Information to notice or an action to take that does not require a reply. |
| `can_skip` | A message that can be ignored without missing a meaningful obligation or update. |

Classification does not send replies, delete messages, or mark them as read.
`is_spam` is an app-owned label; applying it does not move a message into Gmail's
Spam folder. Model predictions can be wrong, so review labels before relying on them.

## Getting started

### Prerequisites

- Python 3.12+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).
- [Ollama](https://ollama.com/) running on a reachable endpoint.
- A Gmail account and a Google Cloud OAuth client with the Gmail API enabled.

Run the following commands from the repository root.

### 1. Install dependencies

```sh
uv python install
uv sync --locked --dev
```

### 2. Prepare Ollama

Start Ollama, then download the default model:

```sh
ollama pull gemma4:e4b
```

The app connects to `http://localhost:11434` by default. To use another installed
model or endpoint, export `OLLAMA_MODEL` or `OLLAMA_BASE_URL` before running it.

### 3. Authorize Gmail

Follow Google's [Gmail API Python setup guide](https://developers.google.com/workspace/gmail/api/quickstart/python)
to enable the API, configure the OAuth consent screen, and create a **Desktop app**
OAuth client. If the app is in testing mode, add your Gmail account as a test user.

Create a `secrets/` directory and save the downloaded client file as
`secrets/credentials.json`. Then run this on a desktop with a browser:

```sh
uv run email-classificator auth
```

Complete Google's authorization flow. The app saves `secrets/token.json` and creates
any missing classification labels. Running `auth` again forces reauthorization.
Classification and scheduled runs use the saved token noninteractively; the secrets
directory must remain writable so refreshed tokens can be saved.

**Privacy and permissions:** authorization requests Gmail read, compose, label,
and modify scopes. Classification sends message content to the configured Ollama
endpoint and modifies Gmail labels. Use an endpoint you trust. Keep OAuth files
and exported email datasets private; do not commit them.

### 4. Classify messages

```sh
uv run email-classificator classify
```

Omitting the command also runs classification. This is a live mailbox operation,
not a preview or dry run.

## Configuration and scheduling

| Environment variable | Local default | Purpose |
| --- | --- | --- |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama endpoint. |
| `OLLAMA_MODEL` | `gemma4:e4b` | Model used for mailbox classification. |
| `EMAIL_SECRETS_DIR` | `secrets` | Directory containing `credentials.json` and `token.json`. |
| `EMAIL_STATE_DIR` | `data` | State directory, including the classification lock file. |
| `TZ` | `Europe/Bratislava` | Time zone for scheduled runs. |
| `RUN_TIMES` | `09:00,21:00` | Comma-separated local times in 24-hour `HH:MM` format. |

Local commands read exported environment variables; they do not automatically load
`.env`. For example:

```sh
TZ=Europe/Bratislava RUN_TIMES=09:00,21:00 uv run email-classificator schedule
```

Keep this process running to classify at the configured times. It waits for a
matching time rather than classifying immediately on startup. Runs sharing the
same state directory use a lock to prevent overlap.

### Docker Compose

Authorize Gmail on your desktop first and securely place the OAuth files in the
deployment's `secrets/` directory. With Docker and Docker Compose installed:

```sh
docker compose up --build -d
docker compose logs -f classifier
```

Compose runs the scheduler and mounts `./secrets` and `./data` as writable persistent
directories. It defaults to host Ollama at `http://host.docker.internal:11434`;
ensure Ollama accepts connections from the container, while restricting access to
trusted clients. Ollama is not included as a Compose service.

Compose can read overrides from a root `.env` file; see [`.env.example`](.env.example).
Its container paths default to `/app/secrets` and `/app/data`. Set `APP_UID` and
`APP_GID` to match the owner of the mounted directories if needed (both default to
`1000`). The container user needs write access to both directories. Unlike Compose,
the Docker image defaults to a single `classify` run.

## Evaluation accuracy

Historical evaluation screenshots are preserved below. They show individual runs,
not a guarantee of accuracy on another mailbox or with the current model and prompt.

1. First accuracy evaluation

![Results of the first accuracy evaluation](docs/images/1_run_accuracy.png)

2. Second accuracy evaluation, after prompt changes

![Results of the second accuracy evaluation after prompt changes](docs/images/2_run_accuracy.png)

### Run your own evaluation

After setting up Gmail authorization and Ollama:

1. Export up to 100 recent Inbox messages:

   ```sh
   uv run python evaluation/generate_dataset.py
   ```

2. In `data/dataset/email_label.json`, replace every `null` label with your expected
   label: `is_spam`, `need_reply`, `to_read`, or `can_skip`.
3. Generate predictions and compare them with your labels:

   ```sh
   uv run python evaluation/generate_llm_answers_to_dataset.py
   uv run python evaluation/compare_datasets.py
   ```

Predictions are saved to `data/dataset/email_label_llm.json`. The comparison reports
mismatches, overall accuracy, and per-class recall. The prediction script currently
uses `gemma4:e4b` directly, regardless of `OLLAMA_MODEL`.

Both generation scripts refuse to overwrite existing output. Preserve earlier
datasets before starting another evaluation. These files contain private email
content and should not be shared without review.

## Development

Install the development dependencies as above, then run:

```sh
uv run ruff check .
uv run ruff format --check .
uv run pyright
```

Optional Git hooks are configured in [`.pre-commit-config.yaml`](.pre-commit-config.yaml):

```sh
uv run pre-commit install
```
