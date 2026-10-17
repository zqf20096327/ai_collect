<p align="center">
  <img src="assets/hermes-bumblebee-bridge.jpg" alt="hermes-bumblebee-bridge" width="640">
</p>

# hermes-bumblebee-bridge

> Read-only supply-chain scanning for your [Hermes Agent](https://github.com/NousResearch/hermes-agent), powered by [Perplexity's Bumblebee](https://github.com/perplexityai/bumblebee). Hermes scans daily, narrates the result in his own voice, and pings you the moment anything new appears.

![Hermes responding to "sweep the perimeter" via Telegram](assets/demo-telegram.png)

## What this is

Hermes Agent can run tools, but it can't *see* whether its own host has been compromised — and most local-agent setups have no continuous security signal at all. This bridge fixes that:

- **Daily automated scan** via systemd timer with catch-up — works on machines that aren't on 24/7.
- **Hermes-native skill** — when you ask "is the system clean?" Hermes runs the scan himself and narrates the result.
- **Push notifications** — opt-in alerts the moment a *new* finding appears against curated threat-intel catalogs. Channel-agnostic: ships with examples for Telegram (python-telegram-bot bridges) and generic webhooks (Slack / Discord / your own).
- **Zero new attack surface** — Bumblebee is read-only Go, no daemons, no sudo, no package-manager execution. This bridge adds bash glue and a systemd timer. That's it.

## Credit where it's due

- **[Bumblebee](https://github.com/perplexityai/bumblebee)** is by Perplexity Security. They did the hard part — the actual scanner, the threat-intel catalogs, the schema. This project is glue.
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** is by Nous Research. The skill / SOUL.md integration patterns come from their plugin conventions.

If you find this useful, star their repos too.

## Quick start

```bash
# One-line install (downloads Bumblebee v0.1.1, fetches catalogs, sets up timer + Hermes skill)
curl -sSfL https://raw.githubusercontent.com/Deconstruct2021/hermes-bumblebee-bridge/main/install.sh | bash

# Or clone and inspect first (recommended)
git clone https://github.com/Deconstruct2021/hermes-bumblebee-bridge.git
cd hermes-bumblebee-bridge
./install.sh
```

The installer:

1. Downloads the official Bumblebee `v0.1.1` Linux/macOS binary into `~/.local/share/hermes-bumblebee-bridge/bin/` (sha256-verified against the release `checksums.txt`).
2. Fetches all `threat_intel/*.json` catalogs from the upstream repo.
3. Drops the scan runner + summarizer into `~/.local/share/hermes-bumblebee-bridge/`.
4. Installs the systemd user timer (`OnCalendar=*-*-* 10:55:00`, `Persistent=true`) — catches up the run on next boot if the machine was off.
5. Installs a `bumblebee-scan` skill into `~/.hermes/skills/` so Hermes can call it.
6. Prints a one-page `SOUL-snippet.md` you can paste into your `~/.hermes/SOUL.md` so Hermes reaches for the skill on security questions.

Run once, then forget — daily scans land in `~/.local/state/hermes-bumblebee-bridge/bumblebee-summary.json`.

## How it works

```
                  ┌──────────────────────────────────────────────┐
                  │  ~/.local/share/hermes-bumblebee-bridge/      │
                  │   ├─ bin/bumblebee   (official Perplexity)    │
                  │   ├─ catalogs/*.json (Perplexity threat-intel)│
                  │   ├─ daily_scan.sh                            │
                  │   └─ summarize.py                             │
                  └──────────────────────────────────────────────┘
                                       │
                  ┌────────────────────┴────────────────────┐
                  ▼                                          ▼
  ┌─────────────────────────────┐         ┌─────────────────────────────┐
  │ systemd user timer          │         │ Hermes skill                │
  │ daily 10:55 + catch-up      │         │ ~/.hermes/skills/           │
  │   bumblebee-scan.service    │         │   bumblebee-scan/SKILL.md   │
  └──────────────┬──────────────┘         │   bumblebee-scan/scan.sh    │
                 ▼                         └──────────────┬──────────────┘
  ┌─────────────────────────────┐                         │
  │ summary.json + state.json   │◀────────────────────────┘
  │ ~/.local/state/             │
  │   hermes-bumblebee-bridge/  │
  └──────────────┬──────────────┘
                 │
                 ▼  (only on NEW findings vs last scan, opt-in)
  ┌─────────────────────────────┐
  │ Notifier of your choice     │
  │   • Telegram bot snippet    │
  │   • Generic webhook (curl)  │
  │   • Your own scripthook     │
  └─────────────────────────────┘
```

The summarizer normalizes Bumblebee's NDJSON into a tiny JSON blob (`packages_total`, `ecosystems`, `findings_total`, `findings_by_severity`, `findings_new_since_last`, redacted `findings_preview`). Everything downstream reads that file — your daily digest, your Hermes skill, your notifier.

## Hermes integration

After install, ask Hermes:

> "is the system clean?"

He will load the `bumblebee-scan` skill, run a fresh scan via `systemctl --user start --wait bumblebee-scan.service`, parse the summary, and reply in his own voice.

For best results, paste the snippet at `docs/SOUL-snippet.md` into your `~/.hermes/SOUL.md`. Smaller local models (qwen3, llama) sometimes deny they have a tool when asked to introspect — anchoring the skill in the persona/identity layer fixes that. Then start a fresh Hermes session (`hermes`, not `hermes --continue`) so the updated SOUL.md takes effect.

## Notification channels

### Telegram (recommended for solo developers)

If you already run a Telegram bridge for Hermes, see `examples/telegram-bridge-snippet/` — drop-in Python that adds a `/bumblebee` slash command, hooks the summary into your existing daily digest, and pushes urgent alerts via your outbound queue.

If you don't have one yet, the `examples/standalone-notifier/` directory has a minimal `notifier.sh` that takes a bot token + chat ID and pushes alerts directly via the Telegram Bot API. ~20 lines of shell.

### Slack / Discord / arbitrary webhook

`examples/standalone-notifier/webhook.sh` posts the alert as JSON to any URL — works with Slack incoming webhooks, Discord webhooks, or your own ingest endpoint.

### Custom

The summarizer calls `$BUMBLEBEE_NOTIFIER` (if set in the systemd unit's environment) with the path to the new alert text. Write any script you want.

## Enabling urgent alerts

By design, urgent push alerts are **off** until you opt in. This keeps you from getting paged at 3am by false positives during the first few scan cycles.

```bash
touch ~/.local/state/hermes-bumblebee-bridge/alerts-enabled
```

The next scan that produces a *new* finding ID (vs the prior scan's state) will fire the configured notifier. To disable: `rm` that file.

## What gets scanned

Bumblebee inventories installed packages in `$HOME` and matches them against curated `threat_intel/*.json` catalogs of known-compromised package versions. Covered ecosystems:

- npm, pnpm, Yarn, Bun
- PyPI (dist-info, egg-info)
- Go modules
- RubyGems
- Composer
- MCP server configs
- Editor extensions (VS Code, Cursor, Windsurf, VSCodium)
- Browser extensions (Chromium, Firefox per profile)

Bumblebee never executes package managers, never reads `.env` files, and runs as your normal user (no sudo). It matches **exact `(ecosystem, name, version)` tuples** against the catalogs — no version ranges, no heuristics → very low false-positive rate.

## Threat-intel catalog updates

Catalogs ship at install time. To pull the latest Perplexity-curated catalogs:

```bash
~/.local/share/hermes-bumblebee-bridge/refresh_catalogs.sh
```

Or install the optional weekly refresh timer (Sunday 03:00 local):

```bash
systemctl --user enable --now hermes-bumblebee-bridge-refresh.timer
```

## Privacy & redaction

The summarizer redacts paths matching `.env`, `.ssh/`, `.xurl`, and `(api_key|token|secret|bearer)=...` patterns from alert text **before** queuing notifications, so a finding whose `evidence` field happens to mention a sensitive path doesn't leak through your notification channel.

That said: don't pipe alerts to public channels. Keep them in a DM or a private room.

## Platform support

- ✅ Linux (tested on Ubuntu 24.04 in WSL2)
- ✅ macOS (Bumblebee ships native binaries; systemd timer step replaced by `launchd` plist — see `docs/MACOS.md`)
- ❌ Windows native (Bumblebee is Linux + macOS only — run under WSL2)

## Uninstall

```bash
./uninstall.sh
```

Removes the timer, the skill, the binary, the catalogs, and the state directory. Does not touch your SOUL.md (you added that snippet manually; you remove it manually).

## License

MIT. See [LICENSE](LICENSE).

Bumblebee itself is MIT-licensed by Perplexity; threat-intel catalogs in `~/.local/share/hermes-bumblebee-bridge/catalogs/` are fetched directly from the upstream repo and remain under Perplexity's license.

## Contributing

Issues and PRs welcome. Especially helpful:

- macOS `launchd` parity for the timer
- Notifier examples for other channels (PagerDuty, ntfy.sh, Mattermost, etc.)
- Test fixtures for catalogs that actually match something on a deliberately-vulnerable VM

## Roadmap

- [ ] macOS `launchd` plist generator
- [ ] Weekly catalog auto-refresh timer (currently manual)
- [ ] `--dry-run` flag on the installer
- [ ] Optional Hermes plugin manifest (`plugin.yaml`) for `hermes plugins install`
- [ ] HTML weekly report (separate from the Hermes-narrated daily)

## Acknowledgements

- **Perplexity Security** — for open-sourcing Bumblebee and the threat-intel catalog format.
- **Nous Research** — for Hermes Agent and the skill/SOUL conventions this plugin slots into.
