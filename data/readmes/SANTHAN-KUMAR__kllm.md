<h1 align="center">kllm: free GPU LLMs for Claude Code, opencode and any OpenAI client</h1>

<p align="center">
  <img src="docs/assets/banner.svg" alt="kllm: free GPUs for your coding agent. pipx install kllm-gateway. OpenAI and Anthropic API on localhost" width="100%">
</p>

<p align="center">
  <a href="https://github.com/SANTHAN-KUMAR/kllm/actions/workflows/tests.yml"><img alt="tests" src="https://github.com/SANTHAN-KUMAR/kllm/actions/workflows/tests.yml/badge.svg"></a>
  <a href="https://pypi.org/project/kllm-gateway/"><img alt="PyPI" src="https://img.shields.io/pypi/v/kllm-gateway?label=pypi&color=blue&cacheSeconds=3600"></a>
  <img alt="Python 3.10 to 3.13" src="https://img.shields.io/badge/python-3.10%20to%203.13-3776ab">
  <img alt="Linux, macOS, Windows" src="https://img.shields.io/badge/os-linux%20%7C%20macos%20%7C%20windows-555">
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-green"></a>
  <a href="https://github.com/SANTHAN-KUMAR/kllm/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/SANTHAN-KUMAR/kllm?style=social&cacheSeconds=3600"></a>
</p>

**kllm runs open-weight LLMs on Kaggle's free GPUs and gives your coding tools a local API for them.**
It serves Qwen and other GGUF models (including abliterated ones) through llama.cpp on two free Tesla T4s,
behind an OpenAI and Anthropic compatible endpoint on `127.0.0.1`. No local GPU, no API bill.

Your laptop has no GPU. You still want Claude Code to refactor a 2,000-line module on a 35B model, with a
256K context window, without paying per token. With kllm you install one package, paste a Kaggle token once,
and run `claude-kllm`. Ten minutes later the model is answering from two Tesla T4s in a Kaggle notebook, and
Claude Code talks to it as if it were running on `127.0.0.1`.

### Six weeks of daily use, from the request log

<table align="center">
  <tr>
    <td align="center"><h3>15,481</h3>requests</td>
    <td align="center"><h3>98.95%</h3>succeeded</td>
    <td align="center"><h3>750M</h3>prompt tokens</td>
    <td align="center"><h3>89.8%</h3>served from cache</td>
    <td align="center"><h3>395K</h3>largest context</td>
  </tr>
</table>

<p align="center"><sub>One developer's coding sessions with Claude Code and opencode, Oct 6 to Nov 16 2026: 18.1M output tokens,
2,465 requests above 100K tokens of context, median time to first token 4.1 s, 12 runaway loops cut by the guard.</sub></p>

That raises a few questions, answered below:

- [How do I get started?](#how-do-i-get-started)
- [What happens when I run it?](#what-happens-when-i-run-it)
- [Which models can I run, and how fast are they?](#which-models-can-i-run-and-how-fast-are-they)
- [How do I connect Claude Code, opencode or my own code?](#how-do-i-connect-claude-code-opencode-or-my-own-code)
- [What happens when Kaggle's 12-hour limit hits?](#what-happens-when-kaggles-12-hour-limit-hits)
- [Is my code and my Kaggle token safe?](#is-my-code-and-my-kaggle-token-safe)

## How do I get started?

<p align="center">
  <img src="docs/assets/quickstart.svg" alt="Terminal: pipx install kllm-gateway, then kllm finds the Kaggle token, writes the config and prints the panel URL, then claude-kllm" width="88%">
</p>

**1. Install** with one command. The one-line installers bring their own Python through [uv](https://docs.astral.sh/uv/).

| You have | Run |
| --- | --- |
| Nothing (Linux, macOS) | `curl -fsSL https://raw.githubusercontent.com/SANTHAN-KUMAR/kllm/main/install.sh \| sh` |
| Nothing (Windows) | `powershell -ExecutionPolicy ByPass -c "irm https://raw.githubusercontent.com/SANTHAN-KUMAR/kllm/main/install.ps1 \| iex"` |
| uv | `uv tool install kllm-gateway` |
| pipx | `pipx install kllm-gateway` |
| pip | `pip install kllm-gateway` |

The package is `kllm-gateway` on PyPI. It installs two commands: `kllm` and `claude-kllm`.

**2. Click the kllm icon, or run `kllm`.** Either starts the local relay and opens the control panel in your
browser. On a first run the panel shows a four-step setup: add your Kaggle account, pick a model, connect a tool,
say hello. The one-line installers put the icon on your desktop and in the app menu; after a pip, pipx or uv
install, `kllm shortcut` adds it.

<p align="center">
  <img src="docs/assets/panel-welcome.png" alt="The kllm panel's first-run page: open your Kaggle settings, verify your phone, create a token, then paste it or drop kaggle.json" width="92%">
</p>
<p align="center"><sub>First run: the panel links to your Kaggle settings and takes the token as a paste or a dropped <code>kaggle.json</code>. No file to edit.</sub></p>

You need a Kaggle account with a verified phone number, because Kaggle only gives GPUs to verified accounts.
If `~/.kaggle/kaggle.json` already exists, kllm finds it and skips the paste.

**3. Use it.**

```bash
claude-kllm                                  # Claude Code on the default model
kllm update                                  # upgrade when a new version is out (kllm tells you)
kllm uninstall                               # remove kllm completely (shows the list first)
opencode -m kllm/qwen3.6-35b-abliterated     # opencode
kllm down                                    # stop the GPU when you are done, to save quota
```

The first request starts a GPU if none is running. Expect about 8 to 10 minutes for a cold start, while
Kaggle boots the notebook and downloads the model. The request waits and then continues on its own.

## What happens when I run it?

Your tools never talk to Kaggle. They talk to a small relay on your PC (one Python process, about 55 MB of
RAM), and the relay does the Kaggle work.

```mermaid
sequenceDiagram
    autonumber
    participant T as Claude Code
    participant R as kllm relay (your PC)
    participant K as Kaggle notebook (2x T4)
    T->>R: first request for qwen3.6-35b-abliterated
    R->>K: push a private notebook with your Kaggle token
    Note over K: build llama.cpp, download the model, open a tunnel
    K-->>R: tunnel URL, sealed and signed
    R->>K: forward the request through the tunnel
    K-->>T: streamed answer (the relay sends keep-alives while it waits)
```
<p align="center"><sub>The relay holds the first request while the GPU starts, so the tool needs no retry logic.</sub></p>

After that, every request goes straight from the relay through the tunnel. The relay keeps each
conversation on the same GPU so the prompt cache stays warm: in measured sessions, 99% of each turn's
prompt came from the cache at 55K tokens of context. Details are in [How kllm works](docs/how-it-works.md).

## Which models can I run, and how fast are they?

These three are measured on two T4s, in benchmarks and in daily use. The panel lists 46 models in all, and
adds any GGUF or diffusers repo from Hugging Face.

| Model | Best for | Context | Measured speed | Real requests |
| --- | --- | --- | --- | --- |
| `qwen3.8-27b` (and its `-vision`, `-abliterated`, `-256k` variants) | Highest answer quality; dense 27B; the vision variant reads screenshots | 128K, or 256K | 16 to 19 tok/s | 6,889 at 99.3% success, up to 190K context |
| `qwen3.6-35b-abliterated` (default) | Long agent sessions at speed; MoE, thinks before answering | 256K | 70 tok/s short, 43 tok/s at 209K | 3,109 at 99.9% success, up to 236K context |
| `qwen3-coder-30b-abliterated` | Fastest turnaround, no thinking | 96K | 84 tok/s short, 35 tok/s at 84K | benchmarks only |

<sub>Speeds for the two MoE models come from benchmarks at the stated context. The `qwen3.8-27b` range is the median
decode speed over real Claude Code and opencode requests that produced at least 200 tokens.</sub>

<p align="center">
  <img src="docs/assets/panel-models.png" alt="The kllm panel's model library: 46 models, filterable by chat, image and video, with context size, quantisation and VRAM for each" width="92%">
</p>
<p align="center"><sub>The model library shows what fits two T4s before you launch anything.</sub></p>

Image and video models (SDXL Turbo, LTX-Video, Wan 2.1) run in the same notebook behind the OpenAI Images
API. Anything above 30 GB of VRAM does not fit. See [Models](docs/models.md) for adding models and calling
image and video endpoints.

## How do I connect Claude Code, opencode or my own code?

The relay speaks both the OpenAI and the Anthropic API at `http://127.0.0.1:8080`. Requests from your own
machine need no key.

| Tool | How |
| --- | --- |
| Claude Code | `claude-kllm`, which sets the model and the real context window for you |
| opencode, Codex CLI, Gemini CLI, Antigravity, Cursor | the panel's **Connect** page writes their config and keeps a backup for Undo |
| Any OpenAI client | base URL `http://127.0.0.1:8080/v1`, model `kllm` (whatever is running) |
| Any Anthropic client | `ANTHROPIC_BASE_URL=http://127.0.0.1:8080` |

From your own code it is a normal chat call:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="local")
reply = client.chat.completions.create(
    model="kllm",
    messages=[{"role": "user", "content": "Write a SQL query for the 5 newest orders."}],
)
print(reply.choices[0].message.content)
```

Other devices on your network, or a public URL, can use the same API with the gateway key shown in the
panel's Settings. See [Configuration](docs/configuration.md).

## What happens when Kaggle's 12-hour limit hits?

A Kaggle notebook stops after 12 hours. kllm plans for it: 25 minutes before the limit it starts a
successor, replays each conversation's latest prompt there so the cache is warm, and only then moves the
conversation.

```mermaid
gantt
    title One long Claude Code session across two Kaggle notebooks
    dateFormat HH:mm
    axisFormat %H:%M
    section Notebook A
    serving requests          :a1, 00:00, 11h
    section Notebook B
    starting (8 to 10 min)    :b0, 10:35, 10m
    warm handoff              :crit, b1, 10:45, 5m
    serving requests          :b2, 10:50, 6h
```
<p align="center"><sub>The successor is ready before the old notebook stops, so the session never sees the 12-hour cap.</sub></p>

The same handoff runs when a notebook dies early. In a 72-minute test with three agent sessions in parallel,
contexts grew to 165K tokens and generation held at 50 to 63 tok/s from empty to 175K
([full results](docs/how-it-works.md#how-well-does-it-hold-up-in-a-long-agent-session)).

Each Kaggle account gets about 30 GPU hours a week. `kllm down` stops the GPU, and an idle GPU stops by itself
after 25 minutes without requests.

## Is my code and my Kaggle token safe?

- **Your Kaggle token stays on your PC**, in your user folder. kllm uses it only to call Kaggle's API from your
  machine; it is never put into the notebook or sent anywhere else.
- **Your prompts go only to your notebook**, through a tunnel protected by a per-notebook API key.
- **The notebook's address is sealed.** The notebook reports its tunnel URL through [ntfy.sh](https://ntfy.sh),
  encrypted and signed with a secret generated on your PC, so nobody can read it or swap in a fake URL.
- **The panel is local only.** Requests from other machines need the gateway key and can reach only the model API.

kllm uses your Kaggle account and its free quota. Follow [Kaggle's Terms of Service](https://www.kaggle.com/terms),
which allow one account per person. kllm can manage several accounts (for example a team where each person adds
their own), but which accounts you add is your responsibility.

## Quick answers

**Is it really free?** Yes, within Kaggle's free tier: about 30 GPU hours a week per account. kllm stops
idle GPUs so the hours last.

**How is this different from Ollama or LM Studio?** Those run models on your own hardware. kllm runs them on
Kaggle's GPUs and keeps only a 55 MB relay on your machine, so a laptop without a GPU can run a 35B model.

**Can I run Claude Code on an open model?** Yes. `claude-kllm` starts Claude Code against the relay's
Anthropic-compatible endpoint, with the model's real context window.

**Does it work with Cursor, Continue, Aider or LangChain?** Anything that accepts an OpenAI base URL works:
use `http://127.0.0.1:8080/v1` and model `kllm`.

## What does not work yet?

- The first launch of a model on an account downloads about 20 GB, so it takes 8 to 10 minutes. Kaggle's GPU
  queue occasionally adds more.
- Models above about 28 GB of weights plus cache do not fit two T4s. A 230B model such as MiniMax-M2 cannot run.
- The bundled image and video entries are marked unverified: they were sized and checked, but not run on a GPU.
- Qwen3.6 sometimes thinks at length on trivial requests. That costs seconds, not quality.

## Back to that refactor

Claude Code is working through the 2,000-line module. It started on Notebook A at 09:00, the relay moved it
to Notebook B at 19:45 with its cache warm, and it is still answering at 43 tok/s with 200K tokens of
context. Nothing ran on your laptop but a 55 MB relay.

## More

| Read | For |
| --- | --- |
| [How kllm works](docs/how-it-works.md) | speed tuning, loop guard, tunnel keep-alive, GPU scheduling, the long-session test |
| [Models](docs/models.md) | choosing a model, adding one from Hugging Face, image and video endpoints |
| [Configuration](docs/configuration.md) | every tool's setup, remote access, gateway key, file layout |
| [Contributing](#contributing) | running the tests |

### Contributing

Issues and pull requests are welcome. Run the tests with `pip install -e ".[dev]"` and `python -m pytest`.
They never contact Kaggle, GitHub or ntfy, and never touch your home directory.

© 2026 SANTHAN-KUMAR. Released under the [MIT license](LICENSE).
