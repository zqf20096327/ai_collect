<p align="center"><img src="docs/img/logo.png" alt="Synapse logo" width="120"></p>

# Synapse: a second brain with Symfony AI

Synapse is a folder of markdown notes that agents write to and read from, that other tools reach over MCP, and that can ask a second brain for help. It runs on Symfony AI 1.0.0-BETA1 and the PHP MCP SDK. I built it for the Symfony AI & MCP hackathon.

What you can do with it:

- **Capture.** Hand a piece of text to an agent. A rough thought lands in `notes/inbox/`. A clear piece of knowledge becomes a structured note in `notes/brain/`, in the Open Knowledge Format (OKF v0.2).
- **Ask.** A second agent answers from the notes with RAG and names the file it used. A question the notes cannot answer gets "not found" and no guess.
- **Browse.** A page in the browser shows the notes by type and status, answers questions word by word, and takes voice in and out. A person sets the status (`draft`, `stable`, `verified`, `deprecated`). No tool of the agents can.
- **MCP.** The brain is an MCP server behind an external authorization server. A token with `brain:read` can search and read. A token with `brain:write` can also write. A new tool is closed to readers unless it says it is read-only.
- **Federate.** `app:federate` asks a second brain over MCP and ranks both answers together with a reranker.
- **Providers.** Cohere and Hugging Face, switched with one variable.

The code is also the base of a [tutorial series](https://johanneswachter.dev/synapse/) of six parts. Each part is one branch of the [tutorial repository](https://github.com/wachterjohannes/synapse-tutorial). This repository is the finished state.

## Run it in five minutes

You need PHP 8.4 or newer and Composer. You also need one key: a `COHERE_API_KEY` ([dashboard.cohere.com](https://dashboard.cohere.com/api-keys)) or a `HUGGINGFACE_API_KEY`. Mind the limit of the Cohere trial key, see below. Voice needs an `ELEVENLABS_API_KEY` and is optional.

```bash
git clone https://github.com/wachterjohannes/synapse synapse
cd synapse
composer install
printf 'COHERE_API_KEY=...\nUI_PASSWORD=pick-something\n' > .env.local
php bin/console ai:store:setup brain
php bin/console ai:store:index brain
php bin/console app:doctor
PHP_CLI_SERVER_WORKERS=4 php -d variables_order=EGPCS -S 127.0.0.1:8080 -t public public/index.php
```

Open http://127.0.0.1:8080 and sign in as `synapse` with your `UI_PASSWORD` on the login page. `app:doctor` checks the setup and prints the fix for anything that is missing. The page shows the same list while `UI_PASSWORD` is empty, and a short banner when something else is missing. The workers are there because an answer streams while the page loads its files.

`ai:store:setup` and `ai:store:index` build the search index in `var/`. The repository ships a handful of example notes in `notes/brain/`, so there is something to ask right away, for example "What breaks when I upgrade to Symfony AI 1.0 beta?". `composer install` also builds the stylesheet. You need no Node.

On the command line:

```bash
php bin/console app:ask "What breaks when I upgrade to Symfony AI 1.0 beta?"
php bin/console app:capture "Decision: we use SQLite for the vector store, because it needs no service."
php bin/console app:status               # every note with its status
```

A note you capture, and a status you change, is indexed right away. If the index gets out of step, see [Providers](docs/providers.md).


### The Cohere trial key has a limit

Sign up at [dashboard.cohere.com](https://dashboard.cohere.com/api-keys) and copy the trial key from the API keys page. It is free, and it is limited to **1000 API calls a month**. One question can use several calls (the embedding of the question, the steps of the agent and its answer), and so can indexing and capturing, so a few demo sessions can use it up. There is also a limit per minute, which a large folder hits while indexing ([the note](notes/brain/topics/cohere-trial-key.md)).

When the limit is reached, Cohere answers `Rate limit exceeded`. Then `app:ask`, `app:capture` and the streamed answer in the page fail, while the rest of the page keeps working. Two ways out: create a production key on the same page, or run on Hugging Face with `SYNAPSE_PROVIDER=huggingface` ([providers](docs/providers.md)). Federation still reranks with Cohere.

## More

- [Providers, voice and re-indexing](docs/providers.md): Hugging Face instead of Cohere, ElevenLabs, updating the index.
- [The MCP server](docs/mcp.md): tokens, roles, what the endpoint answers.
- [Keycloak](docs/keycloak.md): a real authorization server.
- [Ask a second brain](docs/federation.md): `app:federate`.
- [What goes where, and what it costs](docs/security-and-costs.md): read this before you use notes you care about.
- [Code map and checks](docs/development.md): where things live, `bin/smoke`.

Symfony AI is at `1.0.0-BETA1`. The backwards compatibility promise starts with 1.0.0, so the code may need small changes when the final release ships.

## What I ran into upstream

Building this on Symfony AI 1.0.0-BETA1 and the PHP MCP SDK showed a few gaps. Each has an issue.

- [symfony/ai#2968](https://github.com/symfony/ai/issues/2968): the MCP bundle does not register the reference handler as a service. `ToolGuardPass` in this repository exists because of that. It wraps every tool call and closes a tool to readers unless it says `readOnlyHint: true`.
- [symfony/ai#2853](https://github.com/symfony/ai/issues/2853): the session store and the notification bus of the bundle are built on PSR-16 only.
- [symfony/ai#2846](https://github.com/symfony/ai/issues/2846), fixed in [#2848](https://github.com/symfony/ai/pull/2848): a tool without arguments is sent without `parameters`, and the Hugging Face router answers 422. `list_notes` has an optional `folder` argument until the fix is released.
- [symfony/ai#3007](https://github.com/symfony/ai/issues/3007), with [#3008](https://github.com/symfony/ai/pull/3008): a streamed tool call can fail with "Undefined array key name" when a provider sends the name after the id. I saw it once on the Hugging Face router and cannot reproduce it every time. The reader runs on `Qwen/Qwen3.8-27B:novita` and `stream_answers` can turn streaming off.

## License

MIT, see `LICENSE`.
