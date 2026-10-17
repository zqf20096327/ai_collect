# Epicurean Roulette Build Guide

This handbook curates the essentials for enhancing and maintaining Epicurean Roulette, the dinner-decision experience that turns indecision into discovery.

---

## System Picture
| Layer | Notes |
| --- | --- |
| Interface | Next.js App Router with shared UI primitives |
| Styling | Tailwind CSS with motion accents |
| Data & Logic | Supabase services, contextual AI helpers, and restaurant feeds |
| Payments & Growth | Upgrade paths, referral incentives, and analytics instrumentation |

The app orchestrates mood cues, location context, and group choices to deliver a playful yet informative recommendation flow.

---

## Local Flight Plan
1. Clone the repository using your preferred workflow.
2. Install dependencies with `npm install`.
3. Launch the development server with `npm run dev` (default port `3003`).
4. Visit `/dinnerdecider` to explore the multi-step journey.

Keep `.env.local` untracked and managed privately; populate only the values you require for current workstreams.

---

## Architecture Highlights
```text
src/
 ├─ app/
 │   ├─ dinnerdecider/        # Core experience pages
 │   ├─ landing/              # Marketing surface
 │   └─ admin/analytics/      # Internal dashboards
 ├─ components/               # Presentation building blocks
 ├─ context/                  # Shared state (e.g., dinner context)
 ├─ lib/                      # Integrations, analytics, payments
 └─ utils/                    # Helper logic (time, formatting, etc.)
```

- `DinnerContext` synchronizes selections, signals, and session metadata.
- `aiRecommender`, `fetchNearbyRestaurants`, and companions encapsulate external requests and smart fallbacks.
- Shared components favor composable props; keep business logic inside lib/context layers.

---

## Working Agreements
- Branch from `main` with descriptive names (`feature/menu-highlights`, `fix/context-race`).
- Bundle meaningful commits; reference the feature or bug in the message title.
- Update `CHANGELOG.md` for anything user-facing or operationally relevant.
- Pair review is encouraged before merging substantial flows or state changes.

---

## Quality Gates
- `npm run lint` ensures style and accessibility conventions.
- `npm run build` verifies bundling and server route readiness.
- Manual paths worth a quick sweep:
  - `/dinnerdecider/randomize`
  - `/dinnerdecider/output`
  - `/dinnerdecider/group`
- Smoke test new integrations with mock data before toggling feature flags.

---

## Debugging Playbook
- Inspect server logs during `/api/*` calls for insight into restaurant, weather, and AI pipelines.
- Signal trackers inside `src/lib/track.js` annotate key metrics; extend responsibly when new events are added.
- Use context devtools to confirm the dinner session state transitions correctly between steps.

---

## Release Rhythm
- Target small, reviewable pull requests.
- Coordinate deploy windows with product stakeholders; note any migration steps in the PR description.
- Archive experiments or spikes in dedicated branches to keep `main` pristine.

---

## Future Opportunities
- Expand contextual signals (seasonality, dietary badges).
- Deepen group collaboration with asynchronous voting.
- Explore offline-friendly caching for repeated queries.

Treat this guide as the living memory of the project—refresh it whenever processes evolve or new discoveries emerge.
