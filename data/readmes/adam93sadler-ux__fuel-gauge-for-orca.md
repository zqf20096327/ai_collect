# ![Fuel Gauge for Orca — Route each tier to the provider with room.](docs/hero.svg)

Fuel Gauge pairs an Orca status-bar plugin with an agent skill. The plugin reads provider allowances and reset times. When an orchestrating agent assigns a job, the skill helps it find a model at the requested tier on a provider with enough room to finish. Use subscriptions before their allowances reset and save metered APIs for last.

![Provider readings flow through the plugin and local snapshot into the routing skill](docs/architecture.svg)

## Adaptive routing

The orchestrator chooses the tier. The skill compares usage windows, recent burn rate and upcoming resets across eligible subscriptions. For example, a Strong job can move from Codex to Claude when the Codex window is nearly spent. If no subscription can carry the job at its tier, the orchestrator presents the options to the owner before downgrading or spending money. The skill's model table is illustrative and should be updated for your account.

![Strong job moves from a nearly exhausted Codex window to Claude, with the API held in reserve](docs/tier-routing.svg)

The matrix shows four providers as an example. Fuel Gauge knows all **45 agents Orca can launch**: it detects which are installed, reads usage wherever the provider exposes it, and lists the rest as installed with no usage data. See [Supported providers](#supported-providers) and [docs/providers.md](docs/providers.md).

## Supported providers

| Provider | How billed | What Fuel Gauge can read | Status |
|---|---|---|---|
| claude | Subscription or API | ✓ OAuth windows | tested |
| claude-agent-teams | Shared Claude account | ✓ Shared Claude windows | experimental |
| codebuddy | Free or subscription credits | — Installation only | experimental |
| openclaude | Selected model backend | — Installation only | experimental |
| codex | ChatGPT plan or API | ✓ ChatGPT windows | tested |
| autohand | Plan credits | — Installation only | experimental |
| ante | Local inference or selected backend | — Installation only | experimental |
| trae | Free access or selected backend | — Installation only | experimental |
| opencode | Selected backend (hosted or local) | — Installation only | experimental |
| opencode2 | Selected backend (hosted or local) | — Installation only | experimental |
| mimo-code | Token plan or API | — Installation only | experimental |
| pi | Selected backend (hosted or local) | — Installation only | experimental |
| omp | Selected backend (hosted or local) | — Installation only | experimental |
| prime-agent | Inference API or selected backend | — Installation only | experimental |
| qoder | Plan or credits | — Installation only | experimental |
| qoder-cn | Plan or credits | — Installation only | experimental |
| gemini | Google plan or API | ~ Google OAuth quota buckets | experimental |
| antigravity | Google plan | ✓ Model pools | tested |
| aider | Selected backend (hosted or local) | — Installation only | experimental |
| goose | Selected backend (hosted or local) | — Installation only | experimental |
| amp | Plan or credits | ~ Free allowance and individual credit balance | experimental |
| kilo | Selected backend (hosted or local) | — Installation only | experimental |
| kiro | Plan or credits | — Installation only | experimental |
| crush | Selected backend (hosted or local) | — Installation only | experimental |
| aug | Plan or credits | — Installation only | experimental |
| cline | Selected backend (hosted or local) | — Installation only | experimental |
| freebuff | Free tier | — Installation only | experimental |
| codebuff | Plan or credits | — Installation only | experimental |
| command-code | Monthly model credits | — Installation only | experimental |
| continue | Selected backend (hosted or local) | — Installation only | experimental |
| cursor | Plan or credits | ~ File-backed CLI monthly usage | experimental |
| droid | Plan or credits | — Installation only | experimental |
| kimi | Plan or credits | ~ Managed OAuth quota | experimental |
| mistral-vibe | Plan or API | — Installation only | experimental |
| qwen-code | Selected model backend | — Installation only | experimental |
| rovo | Plan or credits | — Installation only | experimental |
| hermes | Selected backend (hosted or local) | ~ Default-profile Codex | experimental |
| openclaw | Selected backend (hosted or local) | — Installation only | experimental |
| copilot | Plan or credits | — Installation only | experimental |
| grok | Grok plan or API | — Installation only | experimental |
| muse | API token usage | — Installation only | experimental |
| dsh | API balance | ✓ DeepSeek balance | tested |
| zcode | Coding plan or API | ~ Legacy Coding Plan quota | experimental |
| devin | Plan or credits | — Installation only | experimental |
| jcode | Subscription or selected backend | — Installation only | experimental |

[Detection and account sources](docs/providers.md)

## Install

From the repository root, with Orca 1.4.248 or newer, run:

```sh
orca plugin install ./plugin
```

Review the trusted-worker access shown by Orca. Repeat the command with the fingerprint it prints:

```sh
orca plugin install ./plugin --approve <fingerprint>
```

If disabled, run `orca plugin enable local.fuel-gauge`, then repeat with `--approve <fingerprint>` using the fingerprint for that operation. Replace the angle-bracket placeholders before running.

Link the skill into your agent's skills directory. For an agent using the shared skills folder:

```sh
mkdir -p ~/.agents/skills
ln -s "$PWD/skill" ~/.agents/skills/fuel-gauge
```

Keep the checkout in place. The reader requires Bash and Python 3. Run `./skill/scripts/read-usage.sh` to inspect a reading.

## Configuration

![Status bar examples showing a recent refresh and an inactive gauge](docs/status-bar.svg)

Click **Fuel Gauge** in the status bar to open its controls. The minutes field shows the current interval. Enter a whole number from 1 to 1440 and choose **Save interval** or press Enter. Invalid input uses the 15-minute default. Choose **Refresh now** to check all providers immediately, or use **Fuel Gauge: Refresh now** from the command palette.

The same setting is available in Orca under **Settings → Plugins → Fuel Gauge**. Changes take effect immediately and apply to every provider.

During heavy testing, fixed polling missed allowances running out in time and some jobs stopped on usage limits. Use a shorter interval for heavy sessions and a longer one for light use. The default is 15 minutes.

The bar becomes inactive after 1.5 refresh intervals. Its age describes the last snapshot write. Check each provider’s status for individual failures.

To skip providers, create a JSON array at `~/.local/share/fuel-gauge/ignored-providers.json`, for example `["antigravity", "deepseek"]`. Remove an ID to resume collection.

## Snapshot format

The plugin atomically replaces `~/.local/share/fuel-gauge/latest.json`. This fictional snapshot has one configured provider. Percentages measure usage consumed and reset timestamps use UTC.

```json
{
  "updatedAt": "2026-01-01T10:00:00Z",
  "refreshMinutes": 15,
  "providers": {
    "codex": {
      "setUp": true, "ok": true, "lastOkAt": "2026-01-01T10:00:00Z", "error": null,
      "windows": [{"name": "5h", "usedPercent": 23, "resetsAt": "2026-01-01T12:00:00Z", "minutes": 300}]
    }
  }
}
```

Balance readings include a `balances` array of currency and total pairs. A failed reading includes an error and the last successful timestamp if known. Ignored providers are omitted.

## Privacy and limitations

The plugin uses local logins. Direct authenticated requests go only to the corresponding provider host and reject redirects. Antigravity delegates to the local provider CLI. Some usage endpoints are unofficial and may change. A missing login, incompatible CLI or changed response can leave a provider without a reading. The skill keeps up to 500 local history entries and tracks providers that stop reporting. Treat snapshots, balances and transcripts as private. See [Security](SECURITY.md).

## FAQ

**Does the plugin launch jobs?** The orchestrating agent makes the routing decision. The status bar collects readings and supports manual refresh.

**Can the skill run without the plugin?** When a snapshot is absent or older than twice its refresh interval, the reader checks local Codex session logs and Claude limit rejections. Antigravity quota and DeepSeek balance then require an owner-supplied reading.

## Contributing and license

See [contributing guidelines](CONTRIBUTING.md) and the [changelog](CHANGELOG.md). Released under the [MIT License](LICENSE).
