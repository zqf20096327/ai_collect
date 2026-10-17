# Travel Agent

A [Claude Code](https://claude.com/claude-code) skill that turns Claude into a world-class travel planner.

Modeled on how the world's most respected travel planners actually work (Wendy Perrin's [WOW List](https://www.wendyperrin.com/wow-list/), [Indagare](https://indagare.com/), [Black Tomato](https://www.blacktomato.com/us/about-us/), [Riveting Trips](https://rivetingtrips.com/), Travel Market Report's MasterAdvisor canon). Replaces ad-hoc "where should we go" chat with a 7-phase workflow that web-searches current intel, narrows ruthlessly, and pushes back on bad ideas with better alternatives.

## What it does

```text
plan a trip to Japan in July
help me figure out where to go for our anniversary
long weekend somewhere warm in February
build me an itinerary for 10 days in Italy
honeymoon ideas, mid-budget, beach + culture
where should we go for my 30th, no jet lag from LA
```

The skill fires on a soft match. It then runs a 7-phase workflow:

1. **Discovery** - one consolidated question batch, branched by what you already said
2. **Destination shaping** - three positioned options with tradeoffs (only if undecided)
3. **Logistics scaffold** - flights, lodging by neighborhood, visa, vaccines, weather, advisories (web-searched live)
4. **Day-by-day itinerary** - one named anchor + named backup per day, restaurants with the reason, true rest blocks
5. **Reservations tracker** - every advance booking with the deadline computed for *your* trip dates
6. **Packing and prep** - tailored to climate, activities, length, destination
7. **Deliverable** - polished PDF with cover, day-by-day pages, tracker, packing list, emergency contacts, budget summary

## Install

```bash
claude plugin marketplace add apljacob/travel-agent
claude plugin install travel-agent@travel-agent
```

Then open a Claude Code session and try `plan a trip to Lisbon in October` or any natural travel-planning phrasing.

## Why this exists

Most "AI trip planner" output is a top-10 list of generic recommendations, with stale hours, no advance-booking warnings, no Day-1 jet-lag rules, and no understanding that a food traveler in Rome wants a different trip than an art traveler in Rome. This skill encodes 13 principles drawn from real elite-planner methodology, then enforces them through the workflow:

- Web search before every concrete claim (prices, hours, closures, visa rules, festival dates)
- Three positioned options with tradeoffs spoken out loud, never a top-10 list
- The traveler's passion is the lens for the entire trip
- Pacing wins - two great days beat four exhausting ones
- One named anchor + named backup per day
- Push back on bad ideas (12 cities in 10 days, sightseeing on a jet-lag arrival, dinner reservations at chains in a food city) with better alternatives
- Surface advance-booking deadlines computed for your actual trip dates

Full principles with sources: [skills/travel-agent/references/elite-planner-principles.md](skills/travel-agent/references/elite-planner-principles.md).

## How it works

| Component | Purpose |
|---|---|
| `skills/travel-agent/SKILL.md` | Trigger description, 7-phase workflow, quality rules, pushback table for common bad ideas |
| `references/elite-planner-principles.md` | The 13 attributed principles (Wendy Perrin, Indagare, Black Tomato, Riveting Trips) |
| `references/discovery-questions.md` | The Phase 1 question batch with branching logic (skip what the user already said) |
| `references/itinerary-template.md` | Day structure - anchor + backup, named restaurants, jet-lag-day rules, pacing self-check |
| `references/reservations-tracker-template.md` | Categories to surface, how to compute deadline dates, status codes |
| `references/packing-prep-template.md` | Layered packing list, countdown prep checklist, emergency contacts block |

## Acceptance test queries

Five queries that verify the skill end-to-end after installing:

| # | Query | Verifies |
|---|---|---|
| 1 | `plan a trip to Tokyo in cherry blossom season` | Phase 1 discovery batch fires, branches on the destination already given |
| 2 | `where should we go for our 5-year anniversary, mid-October, mid-budget` | Phase 2 destination shaping with three positioned options |
| 3 | `5 days in Lisbon, food-focused, late September` | Phase 4 itinerary with anchor + backup, named restaurants, pacing |
| 4 | `weekend in Mexico City - we land Friday morning` | Push back on Friday-morning anchor experiences (jet-lag rule) |
| 5 | `12 cities in 10 days through Europe` | Push back on the cram-itinerary with a better alternative |

## Privacy and cost notes

- The skill does live web searches before claiming prices, hours, visa rules, or festival dates. Searches are scoped to specific facts and don't share your trip details with any service beyond what the search query implies.
- No personal data is stored by the skill itself. All trip details stay in your Claude Code session.
- The Phase 7 PDF deliverable saves locally - nothing is uploaded.

## What it is not

- Not a booking tool. The skill surfaces advance-booking deadlines and links to official sources, but you take the actions.
- Not a flight aggregator. It cites current price *ranges* from web search, but it does not search every fare class on every airline.
- Not a substitute for travel insurance, visa services, or vaccination clinics. It tells you what you need; you do the paperwork.

## Out of scope (v0.1.0)

Open to PRs:

- Cost estimation for the full trip (rough budget envelope shaping is in Phase 1, but no spreadsheet output yet)
- Integration with calendar to block travel dates automatically
- Multi-traveler preference reconciliation (group trips with conflicting passions)
- Live re-planning during the trip (weather pivot, cancellation pivot)
- Loyalty program optimization (which credit card or status to use)

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Open an issue first for non-trivial changes.

## License

**Source-available, non-commercial.** Released under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). You can read it, use it personally, learn from it, suggest changes, and submit PRs. You cannot repackage it, sell it, embed it in a paid product, or fork it commercially. Attribution required.

See [LICENSE](LICENSE) for full terms.

## Acknowledgments

- Built with [Claude Code](https://claude.com/claude-code).
- Methodology drawn from [Wendy Perrin's WOW List](https://www.wendyperrin.com/wow-list/), [Indagare](https://indagare.com/), [Black Tomato](https://www.blacktomato.com/us/about-us/), [Riveting Trips](https://rivetingtrips.com/), and [Travel Market Report's MasterAdvisor series](http://www.travelmarketreport.com/Training/articles/MasterAdvisor-73-Tips-for-Qualifying-Luxury-Clients).
