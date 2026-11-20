# 🍯 HoneyGPT — An LLM-Powered SSH/Telnet Honeypot

> **Turn a static honeypot into a catcher that thinks.** HoneyGPT extends [Cowrie](https://github.com/cowrie/cowrie) with large language models that **analyze each attacker's intent in real time** and **generate terminal responses tailored to it** — keeping intruders engaged longer while logging every move for analysis. It is the first honeypot to **break the trilemma** of flexibility, interaction depth, and deceptive realism *at once*, and does so at **low cost** through a hybrid emulated/LLM strategy.

[![Paper - Computer Networks 2026](https://img.shields.io/badge/Paper-Computer%20Networks%202026-b31b1b.svg)](https://doi.org/10.1016/j.comnet.2026.112223)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.comnet.2026.112223-1f6feb.svg)](https://doi.org/10.1016/j.comnet.2026.112223)
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-green.svg)](LICENSE.rst)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-3776AB.svg)](requirements.txt)
[![Docker ready](https://img.shields.io/badge/Docker-ready-2496ED.svg)](docker-compose.yml)
[![Stars](https://img.shields.io/github/stars/zyw-286/HoneyGPT?style=social)](https://github.com/zyw-286/HoneyGPT/stargazers)
[![Dataset](https://img.shields.io/badge/Dataset-Hugging%20Face-yellow?logo=huggingface&logoColor=white)](https://huggingface.co/datasets/Ziyang23423432/shell-attack-evolution-dataset)

📄 **Paper:** *HoneyGPT: Breaking the trilemma in honeypots with large language models*, **Computer Networks**, Vol. 282, Art. 112223, 2026 · [DOI: 10.1016/j.comnet.2026.112223](https://doi.org/10.1016/j.comnet.2026.112223)

---

## ✨ Why HoneyGPT?

Classic honeypots force you to pick two of three:

| | Flexibility | Interaction depth | Deceptive realism |
|---|:---:|:---:|:---:|
| **Programmatic (e.g. Cowrie)** | ✅ scalable & controllable | ⚠️ fixed command logic | ⚠️ rigid, fingerprintable |
| **Real-system honeypots** | ❌ hard to customize | ✅ authentic | ✅ authentic, but risky at scale |
| **🍯 HoneyGPT** | ✅ | ✅ | ✅ |

HoneyGPT reframes terminal interaction as an **LLM-driven question–answer process** while keeping Cowrie as the protocol-facing substrate — so you get authentic, context-aware behavior *and* the safety and scalability of an emulated honeypot.

## 🔑 Highlights

- **Breaks the honeypot trilemma** — flexibility, interaction depth, *and* deceptive realism at the same time, instead of trading one for another (the paper's central result).
- **Real-time intent analysis + structured logging** — for every command, the Prompt Manager infers the resulting system-state change and an **impact score**, writing intent/state to JSON logs ready for ATT&CK-style threat analysis. HoneyGPT doesn't just *answer* attackers — it *understands and records* what they are trying to do.
- **Intent-tailored responses** — generates terminal output that *caters to the attacker's goal*, keeping the deception convincing across an entire session.
- **Prolonged engagement** — a system-state register plus memory pruning keep long, multi-step attack sequences coherent, luring attackers deeper and capturing richer attack traces.
- **Low-cost, fast responses** — a hybrid emulated/LLM strategy serves simple or cached commands cheaply and bounds model latency, so only novel, high-value sequences ever reach the LLM.
- **Under the hood** — a **Prompt Manager** with **Question Enhancement** (decompose each command into output / state-change / impact) and **Memory Pruning** (decay + prune low-impact history) makes all of the above hold within the context window.
- **Validated in the wild** — 3-month live deployment alongside Cowrie (see [Field Results](#-field-results)); drop-in single Docker container on the usual Cowrie SSH/Telnet ports.

## 🆚 How HoneyGPT Differs from Other LLM Honeypots

A wave of recent work simply pipes attacker commands to an LLM and returns whatever it produces. That works for a few commands and then breaks down. HoneyGPT is engineered for *real, long, adversarial sessions*:

| | Typical "LLM-in-the-shell" honeypots | **HoneyGPT** |
|---|---|---|
| **Session consistency** | Drift & contradictions over long sessions (the model forgets prior state) | **System-state register + Memory Pruning** keep state coherent across many commands |
| **Attacker intent** | Generate output only | **Analyzes intent + assigns an impact score per command**, logged for threat intel |
| **Cost & latency** | One LLM call per command — expensive, slow, rate-limited | **Hybrid strategy** — cache/emulate the cheap commands; only novel ones hit the LLM |
| **Prompting** | Single-shot prompt | **Question Enhancement** (CoT decomposition into output / state-change / impact) |
| **Protocol & safety** | Often raw LLM wrappers | Built on **Cowrie**'s hardened SSH/Telnet substrate — isolation & scalability preserved |
| **Evidence** | Demos / short tests | **Baseline replay + 3-month real-world deployment** |

In short: others make the shell *talk*; HoneyGPT makes it *stay believable, understand the attacker, and scale affordably*.

## 📑 Table of Contents

- [Why HoneyGPT?](#-why-honeygpt)
- [Highlights](#-highlights)
- [How HoneyGPT Differs from Other LLM Honeypots](#-how-honeygpt-differs-from-other-llm-honeypots)
- [How It Works](#-how-it-works)
- [Quick Start (Docker)](#-quick-start-docker)
- [Configuration](#-configuration)
- [Dataset](#-dataset)
- [Field Results](#-field-results)
- [Three Cases That Prolong Engagement](#-three-cases-where-honeygpt-prolongs-engagement)
- [Roadmap](#-roadmap)
- [Related Research](#-related-research)
- [Security Notice](#-security-notice)
- [Citation](#-citation)
- [License & Attribution](#-license--attribution)
- [Contact](#-contact)

## 🧠 How It Works

HoneyGPT has three components:

- **Terminal Protocol Proxy** — reuses Cowrie SSH/Telnet handling to receive attacker commands and return terminal responses.
- **Prompt Manager** — converts each command into a structured prompt, parses the model response, and maintains honeypot state across the session.
- **OpenAI-compatible model** — generates terminal output and state-analysis results from the prompt.

![HoneyGPT framework and prompt constitution](docs/figures/honeygpt-framework.jpg)
*HoneyGPT framework and prompt constitution (adapted from the Computer Networks paper).*

For the `i`-th interaction, the model is asked to produce three values: terminal output `A_i`, new system change `C_i`, and impact factor `F_i`. The prompt is built from six parts: attacker command `Q_i`, question-enhancement instructions, honeypot principles `P`, honeypot settings `S`, system state register `SR_i`, and interaction history `H_i`.

- **Question Enhancement** decomposes each command into three sub-tasks — produce terminal output, describe how the system state changes, and assign an impact score. State changes feed forward so later commands reflect prior actions.
- **Memory Pruning** decays each history record's impact score with a weaken factor; when the prompt nears the context limit, low-impact history is pruned while the system state register is retained.

![Prompt Manager workflow](docs/figures/prompt-manager-workflow.jpg)
*Prompt Manager workflow: prompt construction, response parsing, memory updating, and pruning.*

![Question Enhancement example](docs/figures/question-enhancement-example.jpg)
*Question Enhancement tracking terminal output, system changes, and impact factors across related commands.*

![HoneyGPT hybrid deployment strategy](docs/figures/hybrid-deployment-strategy.png)
*Hybrid deployment: cheap/deterministic commands are cached or emulated; novel sequences are handled by the LLM.*

## 🚀 Quick Start (Docker)

```bash
git clone https://github.com/zyw-286/HoneyGPT.git
cd HoneyGPT
cp .env.example .env
# Edit .env: set OPENAI_API_KEY, OPENAI_MODEL, and (optionally) an OpenAI-compatible OPENAI_BASE_URL.
docker compose up --build
```

The container listens on:

- **SSH honeypot:** `localhost:2222`
- **Telnet honeypot:** `localhost:2223`

Logs are bind-mounted by default:

| Path | Contents |
|---|---|
| `./var/json` | HoneyGPT JSON interaction logs |
| `./var/log/cowrie` | Cowrie native logs |
| `./var/lib/cowrie/tty` | Cowrie TTY replay logs |
| `./etc` | Cowrie config |

Override with `HONEYGPT_JSON_LOG_DIR`, `COWRIE_LOG_DIR`, `COWRIE_TTY_DIR`, and `HONEYGPT_ETC_DIR` in `.env`.

<details>
<summary>Legacy single-container <code>docker run</code> command</summary>

```bash
mkdir -p /opt/honeygpt/logs/json /opt/honeygpt/logs/cowrie /opt/honeygpt/logs/tty /opt/honeygpt/etc
chown -R 1000:1000 /opt/honeygpt/logs

docker run --net=host --name=honeygpt -d \
  --env-file .env \
  -v /etc/localtime:/etc/localtime:ro \
  -v /opt/honeygpt/logs/json:/cowrie/cowrie-git/var/json \
  -v /opt/honeygpt/logs/cowrie:/cowrie/cowrie-git/var/log/cowrie \
  -v /opt/honeygpt/logs/tty:/cowrie/cowrie-git/var/lib/cowrie/tty \
  -v /opt/honeygpt/etc:/cowrie/cowrie-git/etc \
  honeygpt start -n
```

The image includes `share/cowrie/fs.pickle`. The old `docker cp fs.pickle ...` step is only needed to replace the default virtual filesystem. The image runs as UID/GID `1000:1000` (`cowrie`); make sure bind-mounted log directories are writable by that user.
</details>

## ⚙️ Configuration

HoneyGPT reads OpenAI-compatible API settings from environment variables:

| Variable | Description | Default |
|---|---|---|
| `OPENAI_API_KEY` | API key (keep it in local `.env`, never commit) | — |
| `OPENAI_MODEL` | Model name | — |
| `OPENAI_BASE_URL` | Leave empty for official OpenAI; set for a gateway/self-hosted endpoint | empty |
| `OPENAI_TIMEOUT` | Request timeout (s) — bounded so API failures don't stall sessions | `10` |

`.env.example` is a format template only. Set `dst_host` if you want JSON logs to report a fixed destination IP instead of auto-detecting from the host network.

## 📦 Dataset

HoneyGPT is built on and evaluated with the **Shell Attack Evolution Dataset** —
an ATT&CK-annotated corpus of real shell attacks with command→response pairs and
`Vi` severity labels. The deception-evaluation test set below is its 1,489-turn
`request_response/curated` split.

- 🤗 **Hugging Face:** https://huggingface.co/datasets/Ziyang23423432/shell-attack-evolution-dataset
- 💻 **GitHub:** https://github.com/zyw-286/shell-attack-evolution-dataset

## 📊 Field Results

In the paper's evaluation, HoneyGPT was assessed two ways:

- **Baseline replay** — replays Cowrie-captured attack sessions and compares HoneyGPT against Cowrie and real systems on deception, interaction level, and flexibility.
- **3-month live deployment** — HoneyGPT and Cowrie ran side by side against real attacker traffic.

Compared with Cowrie, HoneyGPT was able to:

- ✅ better satisfy attacker intent and sustain complex, multi-step command combinations;
- ✅ reduce rigid, fingerprintable honeypot behavior;
- ✅ surface additional ATT&CK-style attacker behaviors;
- ✅ stay cost-effective — with the hybrid strategy, only a small fraction of commands needed an LLM call.

### Deception evaluation

Each response is labeled on two binary axes — **attack-intent satisfaction** (the
command executed successfully, S/F) and **OS-logic compliance** (output is
consistent with real OS logic, LC/NLC) — over the **1,489-turn** curated test
set, giving four categories (`SALC / SALNLC / FALC / FALNLC`) and four metrics:

```
Accuracy            = SALC / (SALC + SALNLC)
Attack Success Rate = (SALC + SALNLC) / N      # attack-intent axis
OS Logic Compliance = (SALC + FALC) / N        # system-logic axis
Temptation          = separately labeled
```

| Metric | Cowrie | GPT-3.5-turbo | GPT-4o | GPT-4 | Real System |
|---|--:|--:|--:|--:|--:|
| Accuracy | 0.3635 | 0.9117 | 0.9058 | **0.9514** | 1.0000 |
| Temptation | 0.7537 | 0.8910 | 0.9052 | **0.9170** | 0.8106 |
| Attack Success Rate | 0.6669 | 0.8670 | 0.8845 | **0.9127** | 0.8106 |
| OS Logic Compliance | 0.3217 | 0.8872 | 0.8852 | **0.9469** | 1.0000 |

HoneyGPT (GPT-4) beats Cowrie on every axis and even exceeds a real system on
Attack Success Rate while staying highly logic-compliant. It also answers
near-100% of commands across every ATT&CK technique
([`evaluation/successful_response_rate.csv`](evaluation/successful_response_rate.csv))
and supports a broad range of system behaviors
([`evaluation/native_capability_test.csv`](evaluation/native_capability_test.csv)).

All results live in [`evaluation/`](evaluation/) as plain CSVs (transcribed
verbatim from the paper's authoritative figures). Reproduce the metrics from the
raw label counts, or score another honeypot against the dataset:

```bash
python evaluation/deception_metrics.py --counts 1293 66 117 13   # GPT-4 → matches the table
# intent_satisfaction.py + make_review_sheet.py label any candidate honeypot's responses
```

> See the [paper](https://doi.org/10.1016/j.comnet.2026.112223) for full metrics, tables, and case studies.

## 🎣 Three Cases Where HoneyGPT Prolongs Engagement

During the 3-month field deployment, for the **same attacker**, HoneyGPT kept the session alive in three recurring situations where Cowrie lost it. In each case Cowrie's response breaks the illusion and the attacker disconnects, while HoneyGPT fulfills the attacker's expectation so the attack proceeds.

### 1. Fulfillment of Attacker's Intent

Attackers combine `ps` and `grep` to hunt for `miner` processes — checking for competing mining malware, a precondition for continuing. Cowrie shows no such processes, so the attacker quits; HoneyGPT mimics the expected output, satisfies the intent, and the attacker keeps going.

![Case 1: Fulfillment of Attacker's Intent](docs/figures/case1-fulfillment-of-intent.jpg)
*Figure: Fulfillment of Attacker's Intent.*

### 2. Command Support Level

When attackers issue complex, multi-command structures, Cowrie cannot support all the sub-commands and the attacker gives up after repeated failures. HoneyGPT's generative capability handles the full command, enticing deeper engagement.

![Case 2: Command Support Level](docs/figures/case2-command-support.svg)
*Figure: Command Support Level.*

### 3. Content Rigidity

During reconnaissance, Cowrie returns rigid, easily fingerprinted responses; recognizing the honeypot, attackers leave early. HoneyGPT dynamically generates responses tailored to the configured honeypot profile, camouflaging its nature and sustaining engagement.

![Case 3: Content Rigidity](docs/figures/case3-content-rigidity.svg)
*Figure: Content Rigidity.*

## 🗺️ Roadmap

Contributions and ideas are welcome — open an [issue](https://github.com/zyw-286/HoneyGPT/issues) or a discussion.

- [x] Release the sanitized ATT&CK-labeled attack request–response **dataset** — [🤗 Hugging Face](https://huggingface.co/datasets/Ziyang23423432/shell-attack-evolution-dataset) · [GitHub](https://github.com/zyw-286/shell-attack-evolution-dataset)
- [ ] Pluggable model backends (local / open-weight LLMs via OpenAI-compatible servers).
- [ ] Configurable persona & system-profile presets.
- [ ] Extended protocol coverage and ICS/PLC-oriented honeypot scenarios.
- [ ] Lightweight analytics dashboard for captured sessions.

## 🔬 Related Research

HoneyGPT is part of a broader line of work on **LLM/Agent security and AI-for-Security**:

- **HoneyGPT** — *Breaking the trilemma in honeypots with large language models*, Computer Networks 2026.
- **Next-Generation Honeypot Data Analysis** — *Unveiling Evolving Threats*, SRDS 2025 (CCF-B).

## 🔒 Security Notice

This repository was reconstructed from the deployable Docker image; runtime logs, cached bytecode, local Docker metadata, and embedded credentials were removed before publication.

- **Never commit** `.env`, runtime logs, captured attacker files, private SSH host keys, or image archives. Rotate any key that was ever embedded in an image or runtime environment.
- **Do not** upload the publisher-formatted Computer Networks PDF unless the article license permits it — prefer linking the DOI or adding the accepted manuscript per journal policy.
- HoneyGPT is a **honeypot for security research**. Deploy only on infrastructure you are authorized to operate, and isolate it from production networks.

## 📚 Citation

If you use HoneyGPT in academic work, please cite:

```bibtex
@article{wang2026honeygpt,
  title   = {HoneyGPT: Breaking the trilemma in honeypots with large language models},
  author  = {Wang, Ziyang and You, Jianzhou and Wang, Haining and Yuan, Tianwei and Lv, Shichao and Wang, Yang and Sun, Limin},
  journal = {Computer Networks},
  volume  = {282},
  pages   = {112223},
  year    = {2026},
  doi     = {10.1016/j.comnet.2026.112223},
  url     = {https://doi.org/10.1016/j.comnet.2026.112223}
}
```

## 📜 License & Attribution

HoneyGPT is a derivative work of [Cowrie](https://github.com/cowrie/cowrie) and reuses its SSH/Telnet protocol handling, session management, and filesystem emulation.

Cowrie-derived components remain under the original Cowrie **BSD-3-Clause** terms; HoneyGPT-specific additions are released under the same BSD-3-Clause license for compatibility. See [LICENSE.rst](LICENSE.rst), [NOTICE](NOTICE), and [docs/LICENSE.rst](docs/LICENSE.rst).

This repository is **not** an official Cowrie release, and the Cowrie authors do not endorse HoneyGPT unless they have given explicit prior written permission.

## 📮 Contact

Questions, collaborations, or deployment notes are welcome via [GitHub Issues](https://github.com/zyw-286/HoneyGPT/issues) or email: **wangziyang2022@iie.ac.cn**. If HoneyGPT helps your research or product, a ⭐ helps others find it.
