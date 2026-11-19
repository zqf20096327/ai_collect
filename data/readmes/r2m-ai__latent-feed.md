<div align="center">

<img src="./assets/logo.png" alt="Latent Feed" width="600">

*Your morning briefing, hand-picked from the places that matter.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**⭐ If this saves you time, give it a star.** It helps others find it.

</div>

---

## 🎯 Perfect for

Researchers · ML engineers · Obsidian users · Anyone who wants to stay current without the morning rabbit hole

---

## 🌟 What is this?

Latent Feed is a little tool that scours your favourite corners of the internet—papers, repos, threads, and discussions—then bundles the good stuff into one tidy digest. No more tab-hopping. Just set it up once, let it run daily, and wake up to a fresh batch of what’s worth reading.

You choose where it lands: your Obsidian vault, your inbox, or both.

---

## 📸 See it in action

<img src="./assets/demo.gif" alt="Latent Feed demo — Daily AI signal to Obsidian or Email" width="700">

**Features:** Run once a day · Clean digest by topic · Write to Obsidian or email

**[→ Examples](examples/)** — [Email](examples/email-example.md) · [Obsidian daily note](examples/obsidian-example.md)

<details>
<summary>Click to expand — quick sample</summary>

```markdown
## 🏢 Frontier Labs
**[Claude 4.5 Released](https://anthropic.com/...)**  · anthropic
> New model with improved reasoning.

## 📄 Research
**[Transformers Are Bayesian Networks](https://arxiv.org/...)**  · arxiv
> Connections between attention and probabilistic inference.

## 🔓 Open Source Repos
**[vLLM v0.6.0: Prefix Caching + LoRA](https://github.com/...)**  · github
> 5x faster serving.
```

</details>

---

## 📡 News Sources

We pull from six places. Toggle any on or off in your config.

| | Source | What you get |
|---|--------|--------------|
| 📄 | **ArXiv** | Fresh preprints (cs.CL, cs.LG, cs.AI) — the papers before they hit the mainstream |
| 📝 | **Blogs** | OpenAI, Anthropic, Karpathy — evals, interpretability, fundamentals from the source |
| ⭐ | **GitHub Trending** | Trending repos that match your interests — tools, libraries, and projects worth a star |
| 🧡 | **Hacker News** | Top stories and discussions — the pulse of the builder community |
| 🔗 | **Papers with Code** | Research papers with open implementations — read it, then run it |
| 💬 | **Reddit** | r/MachineLearning, r/LanguageModels, r/LocalLLM — what the community is talking about |

### 📚 Blog feed details

| Blog | Focus |
|------|-------|
| **OpenAI** | Evals, agent skills, reasoning |
| **Anthropic** | Interpretability, alignment, model behaviour |
| **Karpathy** | Fundamentals, systems-level understanding |

Add your own RSS feeds in `config.yaml` under `blogs.feeds`.

### 🏷️ Categories

Items are auto-tagged into 10 categories. Edit `processor/categorizer.py` to adjust keywords.

| Category | What you get |
|----------|--------------|
| 🏢 **Frontier Labs** | OpenAI, Anthropic, Google, Meta — model launches, API releases, product updates |
| 📄 **Research** | Papers from arXiv and labs — the core of Latent Feed |
| 🔓 **Open Source Repos** | GitHub, Hugging Face — repos, frameworks, tooling |
| 📊 **Benchmarks** | Evals, leaderboards, comparisons, failure analyses |
| 🤖 **Agents** | Coding agents, tool use, SWE agents |
| 🧠 **Reasoning** | CoT, RL, distillation, inference-time scaling |
| 🛡️ **Safety & Alignment** | Alignment, robustness, prompt injection, oversight |
| 🔬 **Interpretability** | Mechanistic interp, circuits, features, SAEs |
| 🎨 **Multimodal** | Vision, audio, video, robotics, world models |
| ⚡ **Systems** | Inference efficiency, training, kernels, compression |

### 📺 Recommended follows (manual)

Latent Feed doesn’t fetch these, but they’re worth following:

**YouTube** — [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy), [Stanford Online](https://www.youtube.com/@StanfordOnline) (CS25), [Anthropic](https://www.youtube.com/@AnthropicAI), [Yannic Kilcher](https://www.youtube.com/@YannicKilcher), [DeepLearning.AI](https://www.youtube.com/@DeepLearningAI), [Dwarkesh Patel](https://www.youtube.com/@DwarkeshPatel)

**Courses** — [Karpathy: Zero to Hero](https://karpathy.ai/zero-to-hero.html), [Stanford CS25: Transformers](https://cs25.stanford.edu/)

---

## ✨ What it does

| | Feature |
|---|--------|
| 📥 | **One place for everything** — ArXiv, blogs, GitHub, HN, Papers with Code, Reddit, in one feed |
| 🔍 | **Filters by your interests** — Set keywords once; only relevant items get through |
| ✨ | **Short summaries** — Optional one- or two-line summaries so you can skim before clicking |
| 🏷️ | **Organised by category** — Frontier Labs, Research, Open Source Repos, Benchmarks, Agents, Reasoning, Safety & Alignment, Interpretability, Multimodal, Systems |
| 📓 | **Obsidian-ready** — Drops straight into your daily note |
| ✉️ | **Or straight to your inbox** — Email digest to you (and anyone else you add) |

---

## 🚀 Get started

### 1️⃣ Install

```bash
pip install -r requirements.txt
```

### 2️⃣ Set up your config

```bash
cp config/config.example.yaml config/config.yaml
```

Open `config/config.yaml` and at least set your vault path:

```yaml
vault_path: "/path/to/your/obsidian-vault"
daily_notes_subfolder: "LatentFeed"
```

### 3️⃣ Optional: Turn on summaries

If you want short summaries for each item, set your API key:

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

And in `config.yaml`:

```yaml
use_summarization: true
llm_provider: "claude"
```

### 4️⃣ Optional: Get it by email

Add this to `config.yaml`:

```yaml
email:
  enabled: true
  subscribers:
    - "you@example.com"
  smtp:
    host: "smtp.gmail.com"
    port: 587
    from_addr: "your-bot@gmail.com"
  subject: "Latent Feed — {date}"
```

Then set your SMTP credentials (prefer env vars):

```bash
export SMTP_USER="your-bot@gmail.com"
export SMTP_PASSWORD="your-app-password"
```

> 💡 Gmail users: use an [App Password](https://support.google.com/accounts/answer/185833), not your usual login.

### 5️⃣ Run it

```bash
python main.py
```

**Try it in 30 seconds** — preview the digest with no config:

```bash
git clone https://github.com/<you>/latent-feed && cd latent-feed
pip install -r requirements.txt
python main.py --dry-run
```

| Flag | What it does |
|------|--------------|
| `--dry-run` | Prints the digest to the terminal without writing anywhere |
| `--email-only` | Skips Obsidian, sends only to email subscribers |

---

## ⏰ Run it every morning

Add a cron job so it runs at 8 AM:

```bash
crontab -e
# Add this line:
0 8 * * * cd /path/to/latent-feed && /path/to/python main.py
```

---

## 🔄 GitHub Actions (optional)

If your vault lives in a Git repo, you can run Latent Feed on a schedule:

1. Add these **Secrets** in your repo settings:
   - `ANTHROPIC_API_KEY` (if you use summaries)
   - `VAULT_PATH` (path to your vault)
   - `SMTP_USER`, `SMTP_PASSWORD` (if you use email)

2. If the vault is in another repo, clone it in the workflow first, then pass `VAULT_PATH`.

> ⚠️ Most local vaults can’t be reached from GitHub. For email-only, use `--email-only` with your SMTP secrets.

---

## 🔒 Keep your stuff private

These files are in `.gitignore` and **must never be committed** to GitHub:

| File | Contains |
|------|----------|
| `config/config.yaml` | Vault path, email, SMTP settings, `project_url`, `buymeacoffee` |
| `.env` | `SMTP_USER`, `SMTP_PASSWORD`, `ANTHROPIC_API_KEY` — all secrets |

- Copy `config/config.example.yaml` to `config/config.yaml`
- Copy `.env.example` to `.env` and fill in your real values
- **Never commit** `config.yaml` or `.env` — they hold private data

---

## 📁 Project structure

```
latent-feed/
├── main.py              # Entry point
├── sources/             # News sources
├── processor/           # Filter, dedup, categorize, summarize
├── output/              # Markdown, Obsidian, email
├── models/              # Data models
├── config/              # Configuration
└── .github/workflows/   # GitHub Actions
```

---

## 📖 Docs

- [CONTRIBUTING.md](./CONTRIBUTING.md) — How to contribute

---

## 🙌 Spread the word

Found this useful? Star the repo, share it with a colleague, or post about it. Every bit helps.

---

## 📄 License

MIT
