# pi-jewter

[![npm](https://img.shields.io/npm/v/pi-jewter)](https://www.npmjs.com/package/pi-jewter) [![license](https://img.shields.io/npm/l/pi-jewter)](LICENSE)

🎯 **Use the right model for each task without switching models by hand.** Small questions rarely need your most expensive model; architecture and difficult debugging often do. Jewter is a [Pi](https://pi.dev) extension that chooses among your configured models as the conversation moves between different kinds of work.

🔀 **Select `jewter/auto` once.** By default, before each agent step (including after tool results), Jewter uses the [Jev](https://typesafe.ai) classifier to identify the task and the model capability it needs, then selects a model and thinking level from your settings. Planning, implementation, review and verification can each use different combinations. A cache-switch penalty discourages marginal model changes; choose per-request routing instead in `/jewter` → **Routing**.

🧭 **You stay in control.** You choose the models and routing settings, can see what actually answered, and can switch back to a specific model at any time. Jewter does not automatically delegate work, run tests or enforce a development workflow.

💡 Jewter also offers optional context compaction and suggestions to verify changes. **Verification suggestions never send a request automatically.**

## 🚀 Quick start

Requires **Pi 1.5.0+**, **Node 22.19.0+**, a **TypeSafe or OpenRouter API key for Jev**, and at least one model you can already use in Pi.

### 1. Install

Choose **one** source:

```sh
pi install npm:pi-jewter                     # released version
pi install git:github.com/bobuk/pi-jewter    # current main
```

Run `/reload` if Pi is already open. Features marked [Unreleased](CHANGELOG.md#unreleased) are available only from Git; if npm does not list the package yet, use Git.

### 2. Give Jev an API key

Jev needs an API key from **TypeSafe or OpenRouter**. Set the matching variable in the environment that starts Pi:

```sh
export TYPESAFE_API_KEY='…'
# Or:
export OPENROUTER_API_KEY='…'
```

For TypeSafe, you can also enter the key inside Pi via `/jewter` → **Advanced** → **TypeSafe API key** (saved in global `jewter.json` by default; environment variables take precedence).

This key is for classification, **separate from your answering models**. Claude or ChatGPT subscription sign-ins do not authenticate Jev.

### 3. Choose your models

With a working model selected in Pi, open `/jewter` → **Configure in a chat with Pi**. The assistant proposes settings and asks before writing. Or configure **Models** manually.

Assign models to `fast`, `medium` and `strong` capability tiers; at least `medium` must be configured and authenticated. Jewter ships no model assignments. Roles such as planning, implementation and review can override those defaults.

Want a starting point? See the [price-oriented](examples/jewter.price.json) and [quality-oriented](examples/jewter.quality.json) profiles. Adapt their model IDs to your providers; both examples enable compaction, which is otherwise off by default.

### 4. Start routing

Use `/model` to select **`jewter/auto`**, then ask as usual. Select a specific model to bypass routing; verification hints and compaction have separate toggles.

**Model = capability; thinking = thoroughness.** A large mechanical change may need less capability than a short, high-stakes question. See [workflows and profiles](docs/workflows.md) for guidance.

## 🛠 Everyday commands

| Command | What it does |
| --- | --- |
| `/jewter` | Configure models, roles, subagents and optional features |
| `/jewter status` | Show the latest routing decision |
| `/jewter why` | Show its full details |
| `/jewter route <text>` | Preview a route without switching models |
| `/jewter verify` | Put the latest verification suggestion in the editor; does not send it |
| `/jewter on` / `/jewter off` | Enable or disable routing globally |
| `/psst <question>` | Ask a read-only Jev-routed side question outside the main transcript (`/psst inject`, `clear`, `abort`) |

Settings normally live in `~/.pi/agent/jewter.json`; trusted projects can override them in `.pi/jewter.json`. See the [configuration reference](docs/configuration.md) for all settings and commands.

## ⚠️ Know the limits

- Jev classification adds latency and may cost money. Switching models can reduce prompt-cache reuse.
- Prompt and context excerpts are sent to Jev. Verification and compaction may also send file paths, command summaries and tool output. See [privacy and behavior](docs/behavior.md) before using sensitive data.
- Verification hints are on by default; compaction is off. A hint is **not a test result**, and no hint does not mean the work passed.

## 📚 Learn more

- [Configuration](docs/configuration.md) — settings, credentials and model selection.
- [Workflows and profiles](docs/workflows.md) — roles, capability, thinking and subagents.
- [Behavior and limits](docs/behavior.md) — routing, verification, compaction, privacy and costs.
- [Troubleshooting](docs/troubleshooting.md).
- [Development and releases](docs/development.md) · [Changelog](CHANGELOG.md).

## Update or remove

Update using the source you installed, then run `/reload`:

```sh
pi update npm:pi-jewter
# Or:
pi update git:github.com/bobuk/pi-jewter
```

To uninstall, select a specific model first, remove any Jewter subagent bindings, then use `pi remove` with the same source. Your `jewter.json` is kept. See [troubleshooting](docs/troubleshooting.md) for cleanup details.

## License

[MIT](LICENSE)
