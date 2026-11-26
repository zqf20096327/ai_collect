<p align="center">
  <a href="https://souslabs.ai"><img src="https://souslabs.ai/assets/songe-banner-v1.gif" alt="Songe: a bed on the moon, and the command pip install songe"></a>
</p>

<h3 align="center">A training engine for your local model, using your idle compute.</h3>

<p align="center">
  <a href="#-install">Install</a> •
  <a href="#-how-it-works">How it works</a> •
  <a href="#-commands">Commands</a> •
  <a href="ROADMAP.md">Roadmap</a> •
  <a href="https://discord.gg/6bYCjyjr5z">Discord</a> •
  <a href="https://souslabs.ai">Website</a>
</p>

<p align="center">
  <a href="https://discord.gg/6bYCjyjr5z"><img src="https://img.shields.io/badge/Join_our_Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" height="36"></a>
</p>

<p align="center">
  <a href="https://pypi.org/project/songe/"><img src="https://img.shields.io/pypi/v/songe.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/songe/"><img src="https://img.shields.io/pypi/pyversions/songe.svg" alt="Python versions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/sous-labs/songe.svg" alt="License: Apache-2.0"></a>
</p>

Songe is a training engine for the model you already run locally. It sits
between your agent and your model server as an OpenAI-compatible proxy, logs
how each of the model's actions turned out, and fine-tunes a LoRA adapter on
those lessons while the agent is idle. A new version is served only if it
does clearly better than the one in use, and everything stays on your machine
unless you enable the optional cloud learning.

Training requires Apple Silicon (MLX) or an NVIDIA or AMD GPU (PyTorch);
without one, Songe proxies and records only.

## ✨ Highlights

- **Learns from how you work.** Your corrections, stated preferences and the
  tools' errors become lessons for your own model.
- **Two kinds of Dreams.** A Quick Dream adds your preferences to the model's
  instructions in minutes; a Deep Dream trains the model itself while you
  are away.
- **Safe by default.** A new version is used only if it does better on your
  own conversations; one click goes back to any earlier version.
- **Stays out of the way.** Runs only when your agent is quiet, memory is free
  and the battery is fine, and stops the moment you are back.
- **Private.** No account, no telemetry, no cloud unless you opt in: `songe
  cloud on` lets the nightly Dream ask a cloud model you choose, with secrets
  redacted and a nightly budget. Songe never runs your tools.

## 📥 Install

With [uv](https://docs.astral.sh/uv/) or [pipx](https://pipx.pypa.io/) (Python 3.11 or later):

```sh
uv tool install songe        # or: pipx install songe
songe init
```

No uv or pipx yet? Either installs in one line:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh    # uv (or: brew install uv)
brew install pipx                                  # pipx on macOS (Debian/Ubuntu: sudo apt install pipx)
```

Both give Songe its own environment in a lasting place, which its
background service needs.

macOS with Homebrew:

```sh
brew tap sous-labs/tap
brew trust sous-labs/tap     # newer Homebrew asks this once
brew install songe
songe init
```

`songe init` finds your model server and your agents, shows what it will
change, and asks once:

```console
$ songe init

  Models    3 from LM Studio, listed under Songe
  Agent     opencode → Songe models · default granite-4.2-3b-MLX-4bit
  Agent     pi → Songe models · choose one with /model
  Data      ~/Library/Application Support/songe
  Service   starts at login
  Learning  new conversations · starts when idle
  Replace   loaded copy when a better version is ready

Install? (Y/n)
```

Then pick a Songe model in your agent (opencode lists them as
`songe/songe/<name>`), and work as usual.

<details>
<summary>Plain pip, and what you need</summary>

`pip install songe` works inside a virtual environment; outside one,
Homebrew's and most Linux distributions' Python refuse it.

You need a model served locally, and an agent:

| | Supported | Tested end to end |
| --- | --- | --- |
| Model servers | LM Studio, vLLM, Ollama, llama.cpp, mlx-lm | LM Studio (macOS), vLLM (Linux) |
| Agents | opencode and pi (set up for you); any OpenAI-compatible tool | opencode, pi |
| Training | Apple Silicon (MLX); NVIDIA and AMD (PyTorch) | Apple Silicon, NVIDIA |

Machines without a GPU still serve and record, but do not train.
Tried Songe on another setup? Share the result on the
[testing board](https://github.com/sous-labs/songe/issues/15).
</details>

## 🌙 How it works

```text
 your agent ──► Songe (127.0.0.1:7613) ──► your model server
                   │ an OpenAI-compatible proxy: records what happened
                   ▼
            when you are away: a Dream
   read lessons ─► practice ─► train a LoRA adapter ─► check ─► use only if better
```

| | Quick Dream | Deep Dream |
| --- | --- | --- |
| Takes | a few minutes | an hour or more |
| Does | adds the preferences you stated or showed to the model's instructions | writes practice from your lessons and fine-tunes a LoRA adapter on it |
| You see | each new preference, with a before/after where the answer changes | why the new version was or was not used |
| Undo | undo the Quick Dream, or remove one preference | go back to any earlier version |

With **auto-dream** on, Dreams start when your agent has been quiet for a
while. Or press **Dream** in the dashboard (`songe open`). A Dream never just
disappears: it keeps going on the page, or says why it stopped.

<details>
<summary>How it learns, in more detail</summary>

- **Reading.** Songe reads each conversation for the moments that teach
  something: your corrections and stated rules, retries, tool errors.
- **Practice.** For each lesson your model writes short practice scenes in
  your agent's own tools. Your real conversations are never trained on.
- **Training.** The model as it was, shown the lesson, is the teacher; the
  same model with a LoRA adapter, shown only the scene, is the student
  (on-policy distillation). Earlier skills are rehearsed so they stay.
- **Checking.** At the moments you reacted to, the version in use and the new
  one each answer, and a judge compares what they do. The new version is used
  only if it does clearly better, does not change what already worked, and
  its answers stay healthy.

Before the first training Songe measures how much your computer can learn at
once, and trains on what fits. See [DESIGN.md](DESIGN.md).
</details>

## ⌨️ Commands

| Command | What it does |
| --- | --- |
| `songe` | what it is doing |
| `songe status --training [MODEL]` | resolved Deep Dream settings and where they come from |
| `songe open` | the dashboard in your browser |
| `songe models` | each model, and whether it dreams on its own |
| `songe models MODEL on\|off` | auto-dream for one model |
| `songe sleep` | start a Deep Dream now |
| `songe undo MODEL` | go back one version |
| `songe pause` / `songe resume` | stop and restart learning |
| `songe cloud on\|off\|status\|test` | optional: let Dreams ask a cloud model you choose |
| `songe doctor` | check the setup |
| `songe forget` | delete recorded conversations (learned versions stay) |
| `songe uninstall` | stop the service and restore your agent settings |

<details>
<summary>What it changes on your machine</summary>

- Its data folder: `~/Library/Application Support/songe` on macOS,
  `$XDG_DATA_HOME/songe` on Linux, `%LOCALAPPDATA%\songe` on Windows.
- A `songe/` folder in LM Studio's models folder with the current learned
  version. Your own models are never touched.
- One provider entry in opencode and pi, with a backup.
- A background service that starts at login.
</details>

<details>
<summary>Upgrade and remove</summary>

`uv tool upgrade songe`, `pipx upgrade songe` or `brew upgrade songe`: the
service moves to the new version by itself in a quiet moment.

`songe uninstall` stops the service and restores your agent settings; add
`--purge` to also delete its data and learned versions. Run it before
`brew uninstall songe`.
</details>

## 🧭 Roadmap and contributing

Where Songe is going: [ROADMAP.md](ROADMAP.md). Ideas and bugs are welcome as
[issues](https://github.com/sous-labs/songe/issues). Questions and results from your nights go in
[Discord](https://discord.gg/6bYCjyjr5z). To contribute, see
[CONTRIBUTING.md](CONTRIBUTING.md). Security reports: [SECURITY.md](SECURITY.md).

Licensed under [Apache-2.0](LICENSE).
