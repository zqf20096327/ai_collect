# RoleplayArena Barometer

Community-sentiment benchmark for AI roleplay chatbots — Character.AI, Janitor AI, SpicyChat, PolyBuzz, Talkie, Emochi — refreshed twice a day from a rolling 30-day window of what real users write in Reddit posts and app-store reviews. No vendor benchmarks, no self-reported numbers, no ad money in the ranking.

**Live ranking → [roleplayarena.com](https://roleplayarena.com/)**

## Current ranking

<!-- RANKING:START -->
| # | Service | Barometer | Reddit | Stores | Sample |
|---|---------|-----------|--------|--------|--------|
| 1 | [Emochi](https://roleplayarena.com/services/emochi) | **47** | 32 (n=181) | 70 (n=500) | 681 |
| 2 | [Janitor AI](https://roleplayarena.com/services/janitorai) | **47** | 35 (n=856) | 65 (n=494) | 1350 |
| 3 | [Talkie AI](https://roleplayarena.com/services/talkie) | **43** | 27 (n=108) | 66 (n=500) | 608 |
| 4 | [PolyBuzz](https://roleplayarena.com/services/polybuzz) | **41** | 34 (n=93) | 50 (n=1000) | 1093 |
| 5 | [SpicyChat](https://roleplayarena.com/services/spicychat) | **36** | 36 (n=282) | — | 282 |
| 6 | [Character.AI](https://roleplayarena.com/services/characterai) | **25** | 21 (n=196) | 29 (n=1000) | 1196 |

Window **2026-07-31 — 2026-08-30** · computed 2026-08-30
<!-- RANKING:END -->

Scores are 0–100 where 50 is neutral. Services "below the line" don't have enough evidence in the current window to be scored — we list them instead of hiding them.

## How it works (short version)

1. **Collect** the last 30 days of posts from each service's official subreddits, plus reviews from **verified official** store apps only (third-party clones are excluded even when they rank higher) — the registry with exact subreddits and app ids is [`lib/services.ts`](lib/services.ts).
2. **Label Reddit** posts `-1 / 0 / +1` by sentiment toward the service with an LLM. The full labeling rubric — the exact prompt — is in [`lib/classify.ts`](lib/classify.ts). The LLM never outputs scores or percentages, only per-post labels.
3. **Map store stars** directly: 1–2★ → −1, 3★ → 0, 4–5★ → +1 ([`lib/sources/stores.ts`](lib/sources/stores.ts)). Stars are the store sentiment; they are not discarded.
4. **Score** with ~40 lines of plain arithmetic ([`lib/score.ts`](lib/score.ts)): engagement-weighted mean of labels (unit weight for store reviews), Bayesian shrink toward the neutral 50, per-source weights renormalized. Ships with its tests ([`lib/score.test.ts`](lib/score.test.ts)).

The 30-day window is refreshed twice a day. Full technical write-up: [METHODOLOGY.md](METHODOLOGY.md) · reader-friendly version: [roleplayarena.com/methodology](https://roleplayarena.com/methodology)

## Data

| File | What it is |
|---|---|
| [`data/scores.json`](data/scores.json) | Latest window: per-service, per-source aggregates and the headline barometer |
| [`data/history.csv`](data/history.csv) | One row per service per published window — append-only |
| [`data/history/`](data/history) | Full per-window snapshots |
| [`data/labels/`](data/labels) | Per-post sentiment labels as `{Reddit post id, -1\|0\|+1}` |
| [`data/themes.json`](data/themes.json) | Recurring complaint/praise themes with evidence post ids |

The label files are **dehydrated**: post ids only, no content, no authors — rehydrate any id via the Reddit API (`https://www.reddit.com/by_id/t3_.json`) to check our labeling for yourself.

**Licensing:** data is [CC BY 4.0](data/LICENSE) — free to use in articles, videos, and research with attribution to *RoleplayArena Barometer (roleplayarena.com)*. Code is [MIT](LICENSE).

## Verify it yourself

```bash
npm install && npm test   # the scoring arithmetic, with edge cases
```

## Contributing

- **Suggest a service to track** → [open an issue](../../issues/new?template=suggest-a-service.md)
- **Spot a data error or a mislabeled post** → [report it](../../issues/new?template=data-error.md)
