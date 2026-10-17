English | [Tiếng Việt](./README.vi.md)

# opencode-subscription-gateway

**The freedom-of-choice gateway for AI-coding subscriptions in OpenCode v2.** A plugin that makes subscription-gated provider models native in OpenCode: one config line, one login step, and the free-tier models your provider serves appear in `opencode2 models` and chat like any built-in provider model.

No Cline CLI. No proxy server to run. No extra dependencies.

## Install

One command:

```bash
opencode2 plugin add opencode-subscription-gateway
```

Or add the package name to your `opencode.json` (global at `~/.config/opencode/opencode.json`, or project-level):

```json
{
  "plugins": ["opencode-subscription-gateway"]
}
```

Then log in to ClinePass through the native credential flow:

```bash
opencode auth login
```

Select `cline-pass` and paste your ClinePass credentials. The plugin reads the same store the native flow writes — no separate auth setup.

Setting this up through an AI coding agent? Hand it the [agent setup guide](./AGENTS.md) (Tiếng Việt: [AGENTS.vi.md](./AGENTS.vi.md)).

## What you get

- **The native models ClinePass already registers are served untouched** — 14 keys, byte-exact records.
- **6 free-bucket keys**, fetched live from the catalog on load and on rotation:

  | Key |
  |---|
  | `cline-pass/cline-free/muse-spark-1.3-contributor` |
  | `cline-pass/deepseek/deepseek-v4-flash` |
  | `cline-pass/z-ai/glm-5.3-flash` |
  | `cline-pass/cline-free/solar-pro4` |
  | `cline-pass/cline-free/longcat-2.0` |
  | `cline-pass/poolside/laguna-s-2.1:free` |

- **The key shape the host's chat path accepts** — deprecated alias keys are absent; the plugin emits full bucket-id keys only.
- **Streaming and tool calling work** through the native provider stack, including per-provider request headers.

That is 20 keys in total: 14 native + 6 free.

## How it works

- **Live catalog fetch** — the free-model catalog is fetched when the plugin loads and on rotation change; a failed fetch holds the previously published records instead of dropping keys.
- **Probe-attested, clamp-only limits** — emitted limits never exceed a bound the provider is actually serving, and the attested reference is stamped `probe-verified` provenance.
- **Host-native key shape** — one emitted key per free entry, exactly the id the provider serves; no hardcoded model ids anywhere.
- **Native provider stack** — streaming, tool calling, and per-provider request headers ride OpenCode's own provider machinery.
- **Credentials stay native** — the plugin reads the store `opencode auth login` writes; it never asks for, stores, or displays a key of its own.

## Privacy & trust

- **Zero runtime dependencies** — the published artifact is a plain ESM bundle.
- **No telemetry** — the plugin's only network call is the live catalog fetch to the ClinePass API.
- **A redacted local log** at `~/.ai-coding-subscription-router/router.log`, permission-locked `0600` — catalog fetch summaries, per-key emission deltas, credential-lane events, and classified upstream errors.
- **No secrets, key values, or prompts are ever written** — not to the log, not anywhere else.
- **Your credentials live in OpenCode's own auth store**, not in the plugin's config.

## Requirements

- [Bun](https://bun.sh) — the host runs plugins through Bun.
- OpenCode v2 beta with the `plugins` config key (the `opencode2` beta series).
- A ClinePass account with free-tier access.
- Outbound HTTPS to the ClinePass API for the live catalog fetch.

## Referral

Use [OpenCode GO](https://opencode.ai/go?ref=XMMCS33CM5) through the referral link — it supports development at no extra cost to you.

## Support the project

[Buy me a coffee](https://buymeacoffee.com/shynlee04l)

## Roadmap

| Stage | Status | What it delivers |
|---|---|---|
| 1 — ClinePass free-tier gateway | ✅ Shipped [VERIFIED] | This package |
| 1 — More out-of-the-box providers | Planned | Subscription bonuses through OpenCode GO, Kilo, Xiaomi MiMo; Z.ai ZCode under evaluation, pending provider policy approval |
| 2 — Platform-OAuth providers | Planned | Providers whose credentials require their platform's own login flow |
| 3 — Connect + routing + built-in UI | Planned | For openai-compatible providers not supported out of the box — the largest lift, designed as its own phase |
| Deferred | Idea | In-editor UI, rotation controls, control plane |

Full details: [ROADMAP.md](./ROADMAP.md) · Tiếng Việt: [ROADMAP.vi.md](./ROADMAP.vi.md)

## License

[MIT](./LICENSE) — © 2026 Hivemind x OpenCode
