# Generative AI for Network Engineers — Companion Notebooks

**12 hands-on Google Colab notebooks** for the book  
*Generative AI for Network Engineers: From API to Production — Volume 1*

No local setup. No pip drama. Click a button, enter your API key, run cells.

---

## How to use these notebooks

1. Click **Open in Colab** on any chapter below
2. Go to **Runtime → Run all** (or run cells one by one)
3. When prompted, paste your [Anthropic API key](https://console.anthropic.com/) into the Secrets panel
4. Read the book chapter alongside — the notebook is the lab, the book is the theory

You need a free Anthropic account. New accounts get $5 of free credits — enough to run all 12 notebooks several times over.

---

## Chapter notebooks

| # | Chapter | What you build | Open |
|---|---------|----------------|------|
| 1 | What Is Generative AI? | Your first API call — ask Claude about a BGP session | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch01-what-is-generative-ai.ipynb) |
| 2 | LLMs, Tokens & Cost | Measure the token cost of your own configs | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch02-llms-tokens-and-cost.ipynb) |
| 3 | Choosing the Right Model | Run the same prompt on 3 models, compare price vs quality | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch03-choosing-the-right-model.ipynb) |
| 4 | API Basics & Resilience | Build a retry client with exponential backoff and jitter | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch04-api-basics-and-resilience.ipynb) |
| 5 | Prompt Engineering | Write zero-shot, few-shot, and chain-of-thought prompts for network tasks | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch05-prompt-engineering.ipynb) |
| 6 | Structured Outputs | Get Claude to return valid JSON — every time | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch06-structured-outputs.ipynb) |
| 7 | Context Management | Feed a full router config to Claude without hitting the token limit | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch07-context-management.ipynb) |
| 8 | Cost Optimization | Build a model router that picks cheap vs expensive models by task | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch08-cost-optimization.ipynb) |
| 9 | Working with Network Data | Parse multi-vendor CLI output with TextFSM, NTC Templates, and AI fallback | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch09-working-with-network-data.ipynb) |
| 10 | API Integration Patterns | Wrap Netmiko and NAPALM with AI analysis in 25 lines | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch10-api-integration-patterns.ipynb) |
| 11 | Testing & Validation | Write deterministic tests for non-deterministic AI responses | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch11-testing-and-validation.ipynb) |
| 12 | Responsible AI | Add bias checks, audit logging, and human-in-the-loop gates | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eduardd76/genai-for-network-engineers/blob/main/colabs/ch12-responsible-ai.ipynb) |

---

## What you'll be able to do after all 12 notebooks

- Call any major LLM API from Python — with proper auth, retries, and cost controls
- Write prompts that work reliably, not just once
- Parse multi-vendor CLI output without writing regex for every platform
- Add AI analysis to your existing Netmiko / NAPALM / Ansible scripts
- Test AI-powered tools so they don't fail silently in production
- Deploy AI in network operations with proper audit trails and human oversight

---

## Prerequisites

- Basic Python (you don't need to be a developer — network engineers pick this up in the first notebook)
- A Google account (to run Colab)
- A free [Anthropic API key](https://console.anthropic.com/)

No local Python installation needed. Everything runs in the browser.

---

## About the author

**Eduard Dulharu** is a network engineer with 25 years of experience across military radar systems, NATO comms infrastructure, and enterprise networks at AT&T, Kyndryl, and Infosys. In 2024 he built a 5-agent autonomous NOC using locally fine-tuned LLMs — troubleshooting, compliance checking, and risk prevention running up to 10× faster than manual operations with no data leaving the building. He is the founder of [vExpertAI](https://vexpertai.com) and a speaker at AutoCon5.

---

## The book

These notebooks accompany **Generative AI for Network Engineers: From API to Production — Volume 1**.

<!-- Add your book purchase link here -->

---

## License

Notebooks are released under [MIT License](LICENSE) — use them, adapt them, share them. A mention is appreciated but not required.

## Found a bug?

Open an issue or submit a PR. The notebooks are tested against the Anthropic Python SDK — if something breaks after a model update, please flag it.
