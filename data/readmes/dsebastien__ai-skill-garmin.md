# ai-skill-garmin

An [Agent Skill](https://agentskills.io) that connects to Garmin Connect and lets you query your watch data in natural language. Works with any skills-compatible agent (Claude, Cursor, Gemini CLI, OpenCode, Goose, and [many more](https://agentskills.io)).

Ask things like:

- "How did I sleep last night?"
- "How many gym sessions this week?"
- "What's my resting heart rate trending to?"
- "Did I hit my step goal yesterday?"
- "Show me my last 5 runs with pace."

The agent pulls the data and answers. No manual dashboards, no clicking through Garmin Connect.

## Why this exists

Garmin has no stable public API, and the community libraries (garth, python-garminconnect) break every few months when Garmin rotates endpoints, consumer secrets, or auth flows. This skill is a self-contained port of the March 2026 mobile JSON login flow with a thin CLI on top — zero npm dependencies, single TypeScript file, runnable via Bun.

## Requirements

- [Bun](https://bun.sh) (the only runtime)
- A Garmin Connect account
- Email-based MFA supported; SMS/app MFA would need a small extension

## Install

### Via the `skills` CLI ([vercel-labs/skills](https://github.com/vercel-labs/skills))

```bash
npx skills add dsebastien/ai-skill-garmin --skill garmin-connect
```

Preview: `npx skills add dsebastien/ai-skill-garmin --list`

### Manual install

```bash
git clone https://github.com/dsebastien/ai-skill-garmin.git
cp -r ai-skill-garmin/skills/garmin-connect ~/.claude/skills/
# Or the equivalent path for your agent (see https://agentskills.io for directory conventions)
```

The skill is auto-discovered from `SKILL.md`. You can also run the CLI directly without an agent.

### Validate the skill

```bash
npx skills-ref validate ai-skill-garmin/skills/garmin-connect
# Reference validator: https://github.com/agentskills/agentskills/tree/main/skills-ref
```

## Setup

```bash
export GARMIN_EMAIL="your@email.com"
export GARMIN_PASSWORD="yourpassword"
```

Persist in `~/.config/garmin-api/env` and source from your shell rc if you want.

## First login

```bash
bun run skills/garmin-connect/scripts/garmin.ts login
# → "[auth] MFA required (email) — code sent."

# Check email, then:
GARMIN_MFA=123456 bun run skills/garmin-connect/scripts/garmin.ts login
# → "[auth] authenticated as <displayName> — tokens cached."
```

Accounts without MFA: `login` completes in one call.

Tokens are cached at `~/.config/garmin-api/tokens.json` (mode 0600). The OAuth1 token lives ~1 year; the short-lived OAuth2 bearer is silently refreshed on every subsequent run. MFA is re-prompted only when OAuth1 expires or the cache is wiped.

## CLI usage

```bash
bun run skills/garmin-connect/scripts/garmin.ts <command> [args] [--pretty]
```

| Command | Purpose |
|---|---|
| `login` | Authenticate (phase 1, or phase 2 via `GARMIN_MFA`) |
| `whoami` | Print the cached display name |
| `daily <date>` | Daily totals (steps, calories, distance, floors, intensity minutes) |
| `sleep <date>` | Sleep stages, duration, score, HRV-during-sleep |
| `hrv <date>` | HRV summary (status, weekly avg, last-night avg) |
| `readiness <date>` | Training readiness score + contributors |
| `training <date>` | Aggregated training status |
| `activities --from <d> [--to <d>] [--limit N]` | Activity list for a date range |
| `summary <date>` | Bundle of all single-date data for one day |
| `weekly [<date>]` | 7-day window ending on `<date>` (default: today) |

All commands print JSON to stdout; logs go to stderr.

### Examples

```bash
# Last night
bun run skills/garmin-connect/scripts/garmin.ts sleep 2026-04-14 --pretty

# All workouts this week
bun run skills/garmin-connect/scripts/garmin.ts activities --from 2026-04-08 --to 2026-04-14 --pretty

# Everything about today in one shot
bun run skills/garmin-connect/scripts/garmin.ts summary $(date +%F) --pretty | jq .

# How many gym sessions in April?
bun run skills/garmin-connect/scripts/garmin.ts activities --from 2026-04-01 --to 2026-04-30 \
  | jq '[.[] | select(.activityType.typeKey | test("strength|fitness_equipment|indoor_cardio"))] | length'
```

## Using with an agent

Once installed as a skill, any [skills-compatible agent](https://agentskills.io) can invoke it autonomously. Ask questions in natural language; the agent picks the right subcommand, parses the JSON, and answers.

The skill manifest (`SKILL.md`) documents the query patterns agents use.

## Security

- Credentials are passed via env vars. Never committed, never logged.
- Tokens are cached with file mode `0600` under `~/.config/garmin-api/`.
- No third-party services are involved — all requests go directly to Garmin.

## When it breaks

Garmin rotates endpoints and consumer secrets occasionally. Known failure modes:

| Symptom | Likely cause | Remediation |
|---|---|---|
| `401 Invalid signature for signature method HMAC-SHA1` | Consumer secret rotated | Pull the current pair from `https://thegarth.s3.amazonaws.com/oauth_consumer.json` and update the constants at the top of `skills/garmin-connect/scripts/garmin.ts` |
| `404` on `/sso/mobile/api/login` | Endpoint moved | Check [garth](https://github.com/matin/garth) upstream for the new path |
| `429` or `403` on login | Cloudflare rate limit / UA block | Wait 10+ minutes before retrying |

The compatibility surface is small (auth flow + ~6 GET endpoints), so patching is usually a one-line change when something breaks.

## Credits

- [Agent Skills](https://agentskills.io) — the open standard this skill conforms to
- Auth flow ported from [garth](https://github.com/matin/garth) (MIT)
- Mobile JSON login pattern documented via [python-garminconnect #332](https://github.com/cyberjunky/python-garminconnect/issues/332) after Garmin's March 2026 overhaul
- [vercel-labs/skills](https://github.com/vercel-labs/skills) — the `skills add` CLI

## License

MIT. See `LICENSE`.
