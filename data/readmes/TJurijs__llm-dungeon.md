# Dungeon

A local, single-player RPG with an inventive DM, persistent world records, real d100 rolls, and English/Russian play. This implementation replaces the earlier application in this repository. Older versions remain available in Git history; their saved games are not migrated by copying this code.

## Run

Use **Node.js 22.13 or later**. No package installation is needed. Copy `.env.example` to `.env` and fill in the key for the provider you want to use. Keep `.env` private.

```powershell
npm start
```

Open **http://127.0.0.1:4317**. The server reads this folder's `.env` privately. Select **New campaign**, choose a starting template or write your own setting, scenario and character, and begin. Optional DM-only instructions can author a secret or ask the DM to invent one. A template's secrets stay hidden in its preview.

For Russian, select **Русский** for the interface and **Русский** when creating the campaign. Язык интерфейса можно менять отдельно от языка приключения.

Gemini `gemini-3.8-flash` is the requested default. **Settings** offers other provider connections, exact custom model IDs, an explicit paid compatibility check, and public model price references. Passing that small check establishes basic protocol compatibility, not the quality of a DM. The server still requires known billing rates before spending can be bounded.

**Settings** opens a dedicated page with **Models** and **Adventure templates** sections. Model suggestions come from each provider's official listing API (Gemini, OpenRouter, OpenAI, Anthropic, DeepSeek and xAI). Type to filter names and IDs; **Refresh list** checks for newly available models. Listing requests make no paid inference calls and are cached for one hour. Providers may require their configured key to list models. Custom IDs remain accepted when a catalog is incomplete or unavailable; availability is separate from game compatibility.

Optional `ARTIFICIALANALYSIS_API_KEY` in the server's `.env` enables the official Artificial Analysis Free data API. Its matched prices are preferred, with OpenRouter references as fallback. The model picker shows price only, with source and input/output rates available on hover. Missing or stale prices stay unknown. Manual route-pricing controls and the separate reference section are not shown. Artificial Analysis reference data is cached for six hours. These comparisons do not change billing rates or predict complete game-turn time. The key stays on the server and data lookups do not generate model responses.

Both desktop side panels can be hidden with matching left/right pane buttons. Drag their inner edges to resize; focused resize handles also support arrow keys and Home/End. Widths are remembered while the main game area keeps a readable minimum width. Narrow screens use drawers.

In **Adventure templates**, create, edit or copy an adventure with English/Russian content and named character choices, then choose **Use for a new game**. Language versions share one library entry; each can have its own setting, scenario and hidden instructions. Character choices have editable names and descriptions in either language. Built-in edits can be reset to their original version; custom templates can be deleted. Hidden instructions are preserved when editing or copying without revealing them. Changes apply to future games and are stored in `data/adventure-templates.json`.

For testing, open **Character & world → DM secrets · testing** and confirm the spoiler warning. This read-only viewer reveals authored secrets and established DM world records, including hidden facts and NPC activities. It does not teach the character anything or change the campaign. Closing it clears the displayed secrets; reopening requires confirmation again. Template secrets have the same confirmation before editing. Credentials and raw provider responses are never part of this viewer.

## Play

For a first adventure, choose **The Drowned Keep / Затонувший замок**. A drained lake has exposed an old castle, and a salvage crew needs help. Choose English or Russian for the adventure and DM, then pick the scout, apprentice mage, or a custom character. Each game has one player character; preset descriptions can be edited before starting. The apprentice knows Light, Telekinesis, and Warding, with their limits stated in the character description. For a custom template with a missing translation, the form identifies which language supplies the fallback text; the DM still uses the selected game language.

For direct DeepSeek, the tested new-selection profile is **`deepseek-v4-pro`** with native Responses and low reasoning. Explicit transport settings and existing saved selections are preserved. Pro has completed real gameplay but can take several minutes per turn; Flash did not pass the same gameplay checks. Gemini remains the recommended default.

- Describe what your character intends to do. The DM invents details within the setting and established history.
- Ordinary clear actions and impossible actions require no roll and have no dice badge. Meaningful checks show the base difficulty, each labeled modifier, the total before clamping, success chance and real d100 result. A calculated chance at 0 or 100 is guaranteed and uses no die. Older saves show their recorded aggregate modifier where available; individual reasons are not invented retroactively.
- Read a risk warning, then proceed or change your approach. Reconsideration spends no fictional time and rolls no dice. Severe consequences are possible.
- Use **Ask** or `/ask` for an out-of-game question. Use **Appeal** or `/appeal` to question a ruling or request a reasonable correction/undo. Proposed corrections need acceptance; original evidence is preserved. Fair failures do not earn free rerolls.
- **Character & world** shows carried equipment and sourced, dated knowledge about people, places, promises, and objects you left or lent. Knowledge of a distant object does not reveal its unseen current condition or grant access to it. Character and carried-item facts are dated from their saved wording origins, so an old “tomorrow” stays tied to its original day. An absent NPC's progress becomes visible when your character learns it; conditional promises retain their conditions without invented clock deadlines.
- **Journal** searches the retained public history. Its **Include superseded events** checkbox is off by default and reveals preserved undo evidence, clearly marked as outside the current history. Save/reload is automatic. Older saves retain their journals but may have sparse NPC/place/object panels until new observations are recorded.

## Spending and data

All model calls share the durable authorized spending ledger, including setup, compatibility, repairs, playtests, appeals and compaction. The initial USD 20 authorization was explicitly extended for development; a smaller runtime ceiling can restrict a particular testing phase. The app does not automatically add budget. Subtle information icons show campaign and turn costs without a global development-budget banner. An unknown-cost failed request keeps its conservative reservation. This local accounting is an estimate, not the provider invoice or an account-wide spending limit.

The server stores campaigns in `data/campaigns.sqlite` and model accounting in `data/spend-ledger.json`. Private model results under `data/provider-results` can contain fictional secrets. Keep these local. Back up the whole `data` directory with the server stopped, including the ledger; deleting the ledger would erase the spending boundary. Keys are never served to the browser.

If a request is interrupted, use the recovery controls to reload or retry the same request identity. A completed result is not applied twice; an already generated die is retained. If the world changed in another tab, review it and submit a new action. An unfinished request from before a schema/prompt update may be refused because its fingerprint changed; inspect the unchanged saved scene before deliberately submitting a new action. Completed saves and pending decisions remain available.

## Validate

```powershell
npm test
npm run check
```

Local tests use mock providers. Optional browser tests run when `DUNGEON_PLAYWRIGHT_PATH` points to a Playwright `index.mjs`; without it they are explicitly skipped. Historical development tools under `tools/` include paid probes and scripts requiring private local evidence or retired templates. They are not setup steps and should not be run indiscriminately. Generated playtest evidence under `outputs/`, saved games, credentials, and spending records are excluded from Git.

Before committing a performed turn, a separate model review compares narration with saved effects, changes with the player's intent, current facts with the resulting scene, newly supplied equipment with its recorded placement, and event times with the action's sequence. It receives physical before/after records and proposed public disclosures. Gemini uses high reasoning for the DM's action proposals, medium for simpler continuity reviews, and high review for completed/cancelled tasks, resolved situations, severe stakes and appeals; an explicit configured thinking level is respected. Repeating an already-terminal task status alone does not require stronger review. Private NPC execution schedules are separate from the promises the player has actually heard. These checks can reject inconsistent drafts but remain fallible model judgments.

When a confirmation panel is needed, a small public presentation step writes its warning, possible outcomes and modifier labels using only current player knowledge and committed narration. It cannot read the private outcome drafts or author notes. The engine preserves the original numbers and consequences, and the existing continuity review checks the panel against the proposed result before publication. A private adjustment whose cause is unknown can have a neutral situational label. Routine actions skip this step; confirmation and reload reuse it without another model request.

The independent item-placement reader uses original intent and existing descriptions to distinguish similar objects, while requiring completed narration as evidence of each move. It does not receive the proposed after-state, and an intended transfer alone cannot establish a completed handoff.

New actions reuse a physical/current-fact reader's durable raw result during repairs only when its complete request and outcome branch are identical. The engine always validates that reading against the repaired state again. Reuse never crosses actions, providers, models or changed inputs. Independent readers can also overlap public-warning preparation; the broad review still checks the final public wording before anything is shown or saved. All dispatched work settles before an error returns, and interrupted older requests keep their original execution contracts.

`DUNGEON_REVIEW_SCHEDULING=sequential` in the server environment runs review calls one at a time within each new action for connections with restrictive concurrency limits. The default is `overlap`; `legacy` retains public-first scheduling followed by parallel reviews. This controls the action pipeline, not separate campaigns or background maintenance. It changes no prompts, reasoning settings, evidence requirements or provider features. Existing interrupted actions retain their saved scheduling mode.

Selected tasks and situations also bring related people and locations into planning and review, including the task's original wording before completion. A bounded reference pass includes other subjects whose current records refer to an affected participant. Their facts and sourced observations take priority over optional context, so a remote repair or departure can reconcile the related records without loading every unrelated place.

If a draft has an invalid record reference, review still examines its declared descriptions, conditions and active facts where possible. These provisional records are never treated as a valid world state. New turns allow at most two scoped repairs; all required checks must pass before committing. Older saved requests retain their original repair contract.

Proposed appeal corrections also require an explicit check of current descriptions, conditions and active facts, including unchanged remote records. A narrow correction must agree with established history and the rest of the saved world; it does not create an event or advance game time. Confirmation still applies the correction once and preserves the original evidence.

See `docs/design/pilot-implementation.md` for the chosen rules and `docs/playtest-evaluation.md` for findings. Saved autoplay reports preserve failures and recovery boundaries; not every run passed. Long-history storage and retrieval tests do not prove that a generated 1,000-turn campaign will remain consistent. The remaining hard problem is semantic judgment: plausible odds, narration matching effects, NPC knowledge, and relevant memory retrieval. The pilot makes those decisions inspectable and correctable; it cannot guarantee perfect DM behavior or any provider's gameplay quality.
