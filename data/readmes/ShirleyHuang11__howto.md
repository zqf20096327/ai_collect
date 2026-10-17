<div align="center">

# 📖 howto

### An open library of everyday procedural knowledge

**Structured how-to recipes for training agents 🤖 and robots 🦾, readable by humans 🧑**

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Recipes](https://img.shields.io/badge/recipes-2937-brightgreen.svg)](INDEX.md)
[![Journeys](https://img.shields.io/badge/journeys-4-00b3b3.svg)](journeys/)
[![Packs](https://img.shields.io/badge/packs-8-ff8c00.svg)](packs/)
[![Domains](https://img.shields.io/badge/domains-17-blueviolet.svg)](domains.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

[**Use it**](#use) · [**Why**](#why) · [**What's inside**](#inside) · [**Packs**](#packs) · [**Journeys**](#journeys) · [**Quick start**](#quickstart) · [**Roadmap**](#roadmap) · [**Contributing**](#contributing) · [**Citing**](#citing)

</div>

---

## 🐘 How do you put an elephant into a fridge?

<div align="center">
<img src="assets/elephant-in-fridge.png" alt="An elephant crammed into a fridge with the door held open" width="420">
</div>

Easy:

> 1. Open the fridge. 2. Put the elephant in. 3. Close the fridge.

That is how most datasets think tasks work. Here is how `howto` writes it:

```markdown
## Steps
1. **Open the fridge.** → *Expect:* door open, shelves visible, light on.
2. **Insert the elephant.** [BRANCH: elephant does not fit → F1]
3. **Close the fridge.** → *Expect:* door latched; no trunk protruding.

## Failure modes & recovery
- **F1 Elephant exceeds fridge capacity:** acquire a larger fridge, or a smaller elephant.

## Verification
Opening the fridge reveals one chilled elephant.
```

**Things are always more complicated than "open, put, close", and the complications are exactly the knowledge agents are missing.** Every human knows the real steps, the expected observations, the branches, the failure modes. No corpus writes them down. This one does.

And here is a real one, from [`transit/ride-a-subway.md`](transit/ride-a-subway.md):

```markdown
3. **Obtain or validate fare.** [BRANCH: tap-to-pay bank card | transit card with
   balance | ticket machine | transit app QR] At a machine: select destination or fare
   type, pay, take the ticket. ⚠️ *Irreversible:* multi-day passes and non-refundable
   tickets — confirm fare type before paying. → *Expect:* you hold a valid fare medium.
4. **Pass the fare gate.** Tap or insert; walk through on green/open. → *Expect:* gate
   opens and (on card systems) displays balance or fare; if rejected, F1.
...
- **F2 Boarded the wrong direction:** exit at the next station, cross to the opposite
  platform (may require staying inside the paid area), reverse.
```

---

<a id="use"></a>
## 🚀 Use it, don't just read it

Two ways to get value in under a minute:

- **🔎 Browse** — a live, searchable viewer over the whole corpus, filter by domain, and **copy any recipe as agent context** with one click: **[shirleyhuang11.github.io/howto](https://shirleyhuang11.github.io/howto/)**
- **🤖 Give it to your agent** — the **[MCP server](mcp/)** exposes `search_howto` / `get_howto` so Claude Code, Claude Desktop, or Cursor can pull the verified steps at inference time — warnings and all — instead of guessing:

  ```bash
  pip install -r mcp/requirements.txt
  claude mcp add howto -- python3 "$(pwd)/mcp/server.py"
  ```

---

<a id="why"></a>
## 🧠 Why this exists

Web agents, computer-use agents, and household robots fail at everyday tasks less from weak reasoning than from **missing grounded procedural knowledge**: canonical step order, the observation that confirms each step worked, the decision branches, the recovery paths, and which steps are irreversible.

[`agency-agents`](https://github.com/msitarzewski/agency-agents) (134k stars) covers **who an agent is**. `howto` is the complement: **what an agent knows how to do**. Ride a subway, buy and return a product, create an account, make coffee, load a dishwasher, wait in line, pay at a cashier.

The schema turns prose into training substrate. One corpus yields, simultaneously:

| Training product | Derived from |
|---|---|
| SFT / midtraining planning traces | Steps + expected observations |
| Agentic RL tasks with **verifiable rewards** | Goal + Preconditions + Verification |
| Curriculum / skill DAG | `prerequisites` links between recipes |
| Inference-time skill library (RAG) | Recipe chunks |
| Contamination-controlled evals | Held-out recipes and locale variants |
| Robot task plans & sim task generation | Embodied `objects` / `affordances` / `workspace` / `safety` |
| **Long-horizon planning traces** | **[Journeys](journeys/): milestone DAGs over recipes** (gates, waits, re-plan triggers) |

---

<a id="quickstart"></a>
## ⚡ Quick start

```bash
git clone https://github.com/ShirleyHuang11/howto.git && cd howto
pip install pyyaml                       # the only dependency

./scripts/validate.sh                    # validate every recipe against the schema
python3 scripts/stats.py                 # per-domain coverage dashboard
python3 scripts/export.py --format sft   # instruction-tuning pairs (JSONL)
python3 scripts/export.py --format eval  # task specs with success criteria (JSONL)
python3 scripts/export.py --format json  # full structured recipes
```

Or just read one: [`transit/ride-a-subway.md`](transit/ride-a-subway.md) · [`embodied/kitchen/load-a-dishwasher.md`](embodied/kitchen/load-a-dishwasher.md) · [`daily/social/pay-at-a-cashier.md`](daily/social/pay-at-a-cashier.md)

---

<a id="inside"></a>
## 🗂️ What's inside

One task = one markdown file, separated by domain ([`domains.json`](domains.json) is the registry, [`INDEX.md`](INDEX.md) is the full linked index, and the frontmatter is formally specified in [`schema/recipe.schema.json`](schema/recipe.schema.json)). Every recipe shares one skeleton:

```
Goal → Preconditions → Steps (every step ends with → *Expect:* …)
→ Decision points → Failure modes & recovery → Verification
→ Variations (locale/platform) → Safety & privacy (⚠️ irreversible steps inline)
```

<details open>
<summary><b>🧠 Common sense — <code>daily/</code></b> (the largest track: what everyone knows and no one wrote down)</summary>
<br>

| Subdomain | Recipes |
|---|---|
| `self-care/` | brush your teeth · floss · shower · tie shoelaces · bedtime · trim nails · dress for the weather |
| `food/` | boil water · make tea · cook rice · fry an egg · sandwich · cut an onion · microwave · instant noodles · pack a lunch · store leftovers · read food labels |
| `home/` | do the laundry · make a bed · sweep & mop · vacuum · clean a bathroom · sort recycling · unclog a drain · change a lightbulb · change batteries |
| `social/` | pay at a cashier · wait in line · order at a restaurant · split a bill · answer a phone call · greet a neighbor · give directions · ask for help in a store · small talk · borrow & return |
| `errands/` | use an ATM · mail a letter · refuel a car · vending machine · self-checkout · buy groceries · get a haircut · public library |
| `parenting/` | feed & burp a newborn · swaddle · safe infant sleep · introduce solids · potty-train · handle a tantrum · teach a kid to tie shoes / ride a bike · pack a school lunch · hire a babysitter |

</details>

<details>
<summary><b>🦾 Robot track — <code>embodied/</code></b> (recipes that compile into simulator tasks)</summary>
<br>

| Subdomain | Recipes |
|---|---|
| `kitchen/` | make drip coffee · load a dishwasher · set a table · store groceries · make toast |
| `household/` | fold a t-shirt · water houseplants · take out the trash · tidy a room |
| `mobility/` | open a door · use an elevator · carry & deliver · cross a street |
| `care/` | fetch an item for a person |

Embodied frontmatter specifies the sim scene:

```yaml
objects: [dishwasher, plates, cutlery, detergent-pod]
affordances: [door-open, rack-slide, grasp, place]
workspace: kitchen
safety: {sharp_objects: true, fragile: [glasses], human_proximity: pause}
```

</details>

<details>
<summary><b>💻 Digital — <code>accounts/</code> <code>shopping/</code> <code>digital/</code> <code>finance/</code></b></summary>
<br>

create an account · log in · enable 2FA · recover a password · delete an account · security review · buy & return a product · track a delivery · compare before buying · install an app · unsubscribe · back up files · connect to wifi · update safely · pay a bill · dispute a charge · send money to a friend

**Account security & privacy** (`accounts/security/`): migrate 2FA to a new phone · recover a hacked email · secure an account after a breach · find & remotely wipe a lost device · set up a legacy contact · revoke third-party app access · opt out of data-broker sites — the identity/access flows an agent has to get exactly right.

**Computer-use atomics** (the leaf layer agents can perform directly): rename a file · find text on a page · copy-paste · reopen a closed tab · a spreadsheet formula · crop an image · cc/bcc an email · take a region screenshot — 100 single-action primitives under `digital/`.

**Agentic commerce** (buy/sell/transact flows written as verifiable-reward tasks): sell on a marketplace · price an item to sell fast · stack coupons & cashback · bid on an auction · checkout under a budget · audit subscriptions · negotiate an APR or a bill · maximize card rewards · book the cheapest fare · use a virtual card — 200 transactional recipes across `shopping/`, `finance/optimize/`, `travel/booking/`, `digital/transactions/`, each with an explicit target and a checkable end-state.

</details>

<details>
<summary><b>💼 Business ops — <code>business/</code></b> (atomic workflows an agent can run end-to-end)</summary>
<br>

**Invoicing & books:** create an invoice · send a payment reminder · reconcile a statement · record an expense · issue a refund · P&L report · **CRM & sales:** add a lead · move a deal stage · log a call · forecast sales · **HR & hiring:** post a job · screen a resume · send an offer · run payroll · onboard a hire · **Project & support:** create a project · triage a ticket · run a standup · close a sprint · **Meetings, marketing & e-commerce:** schedule across time zones · set up an email campaign · process an order · handle a chargeback · update inventory · reprice inventory · run a shopping ad · fulfill a dropship order · calculate a product margin · flag a fraudulent order

</details>

<details>
<summary><b>🎓 Learning & academics — <code>education/</code></b> (the 14th domain)</summary>
<br>

**Study skills:** active recall · spaced repetition · Cornell notes · the Pomodoro technique · make a one-page study sheet · **Test prep:** SAT · ACT · GRE · GMAT · TOEFL/IELTS · manage test anxiety · **Language learning:** set a goal · daily habit · language exchange · comprehensible input · **Academic writing:** thesis statement · literature review · APA/MLA/Chicago citations (with copyable examples) · avoid plagiarism · **Admissions & aid:** build a college list · Common App essay · FAFSA · scholarships · compare aid offers · grad-school SOP · **Online & K-12:** finish a MOOC · earn a certificate · help with homework · IEP/504 meetings

</details>

<details>
<summary><b>🏋️ Fitness & exercise — <code>fitness/</code></b> (the 15th domain; coach-accurate form, measurable "done when")</summary>
<br>

**Strength:** squat · deadlift · bench · overhead press · row · pull-up & push-up progressions · progressive overload · **Cardio:** run a 5k → marathon · zone-2 · HIIT · rowing · pacing · **Mobility:** full-body & targeted stretches · dynamic warmups · hip/ankle/thoracic mobility · **Home & bodyweight:** no-equipment circuits · calisthenics · band & kettlebell routines · hotel-room workouts · **Sports skills:** basketball · tennis · golf · swimming · cycling · skating · **Recovery:** soreness · injury prevention · protein/sleep/hydration · rest days · **Planning:** goal-setting · splits · tracking · fat-loss/muscle-gain plans · building the habit

</details>

<details>
<summary><b>💻 Software engineering — <code>engineering/</code></b> (the 16th domain — the coding-agent workflows, agent-executable with a programmatic "done when")</summary>
<br>

The tasks a Claude Code / Cursor agent runs all day, each with a *checkable* Verification (tests exit 0, CI green, `curl` 200, migration applied):

**Version control:** open & review a PR · resolve a merge conflict · rebase · bisect a regression · recover a lost commit · **Testing:** write a failing test first · mocks & fixtures · coverage · fix a flaky test · **Debugging:** read a stack trace · reproduce a bug · memory leaks · race conditions · production-only bugs · **CI/CD:** pipelines · caching · matrix builds · required checks · deploy-on-merge · **Deploy:** zero-downtime · blue-green · canary · rollback · feature flags · safe DB migrations · **Database:** SQL & joins · schema design · indexes · backup/restore · prevent SQL injection · **API:** REST/GraphQL · OAuth2 · rate limits · retries with backoff · webhook signature verification · **Containers:** Dockerfiles · compose · Kubernetes · healthchecks · debug a crashloop · **Observability:** structured logs · tracing · SLOs · alerting · postmortems · **Security:** secret handling · key rotation · dependency scanning · XSS/CORS · JWTs. Destructive ops (prod migrations, key rotation, history rewrite) are marked ⚠️ and `risk: high`.

</details>

<details>
<summary><b>🤖 AI & LLM engineering — <code>ai/</code></b> (the 17th domain: how to build LLM apps, RAG systems, and agents)</summary>
<br>

Each of the 200 recipes carries a checkable Verification: an eval clears its threshold, structured output validates against a schema, or retrieval returns the gold document in the top k.

**Prompting:** system prompts · few-shot · chain-of-thought · structured JSON output · prompt-injection defense · **RAG:** chunking · embeddings · vector databases · hybrid search · reranking · answer faithfulness · **Agents:** tool-calling · ReAct loops · memory · planning · MCP servers · guardrails · human-in-the-loop · **Evals:** eval sets · LLM-as-judge · regression evals · contamination checks · significance tests · **Fine-tuning:** dataset prep · LoRA · DPO · quantization · the fine-tune vs RAG vs prompt decision · **LLMOps:** API calls · streaming · caching · model routing · cost caps · PII redaction · **Data:** cleaning · labeling · drift detection · pipelines · anonymization · **Multimodal:** captioning · OCR · transcription · image generation and QA · **Safety:** red-teaming · jailbreak filters · runtime injection detection · output moderation. Steps that send data to a third-party API or deploy to production are marked ⚠️ and `risk: high`.

</details>

<details>
<summary><b>🚇 Physical & services — <code>transit/</code> <code>travel/</code> <code>communication/</code> <code>government/</code> <code>healthcare/</code> <code>housing/</code></b></summary>
<br>

ride a subway · take a bus · hail a rideshare · navigate with maps · book a flight · book the cheapest fare for your dates · rebook after a price drop · claim delayed-flight compensation · check in · book a hotel · send a package · schedule a meeting · renew a passport · book a doctor's appointment · refill a prescription · set up utilities

**Car care** (`transit/vehicle/`): change a flat · jump-start a dead battery · check tire pressure & oil · replace wipers · handle a blowout or an overheating engine · what to do after a fender bender — hands-on, safety-first (hazard steps marked). **Civic & legal** (`government/civic/`): REAL ID · passports · small-claims filing · car titles · vital records · FOIA. **Health navigation** (`healthcare/navigation/`): patient portals · specialist referrals · advance directives · pre-op & discharge · financial assistance — the paperwork and coordination around care, not just first aid. **Home owning** (`housing/owning/`): mortgage preapproval to closing · sell & stage a home · HVAC/water-heater/roof upkeep · HOA · refinancing · roommate agreements.

</details>

📊 Live coverage anytime: `python3 scripts/stats.py`

---

<a id="packs"></a>
## 🎒 Packs — grab a whole kit, install it as a skill

Nobody assembles a scam-defense toolkit from a 2,900-recipe index. A [**pack**](packs/) is a curated, cross-domain kit for one real situation — and it installs into your agent as a self-contained **skill** in one command:

```bash
python3 scripts/build_skills.py scam-and-fraud-defense   # → packs/skills/.../SKILL.md
```

Drop it into Claude Code (`.claude/skills/`) or point your agent at the [MCP server](mcp/) and say *"use the scam-defense pack."* Your agent now follows verified steps — *Expect* observations and ⚠ warnings included — instead of guessing. Every pack's recipes are [machine-checked to resolve](scripts/validate_packs.py).

| 🛡️ [Scam & Fraud Defense](packs/scam-and-fraud-defense.md) | 🚑 [First-Aid & Emergencies](packs/first-aid-emergencies.md) | 📦 [Move Into a New Place](packs/move-into-a-new-place.md) | 🍳 [Kitchen Starter](packs/kitchen-starter.md) |
|---|---|---|---|
| 🦾 **[Robot Manipulation Primitives](packs/robot-manipulation-primitives.md)** | 🔐 **[Digital Security Basics](packs/digital-security-basics.md)** | 🚗 **[New Car Owner](packs/new-car-owner.md)** | 💰 **[Money Starter](packs/money-starter.md)** |

---

<a id="journeys"></a>
## 🗺️ Journeys — long-horizon tasks

Some tasks a single recipe can't hold: they span months, wait on third parties, accumulate state, and force **re-planning** when new information arrives. A [**journey**](journeys/) is a temporal DAG whose leaf nodes are the recipes above — each milestone carries a **gate** (what unblocks it), a **wait** (the third-party clock), a checkable **verify**, and a **re-plan trigger**. And **every leaf is a real recipe id, machine-checked** by [`scripts/validate_journeys.py`](scripts/validate_journeys.py) — 66 references across the four below, all resolving — so a journey can't decay into a listicle. Counted and validated separately from recipes.

| Journey | Horizon | Milestones | What's hard about it |
|---|---|---|---|
| [`recover-from-identity-theft`](journeys/recover-from-identity-theft.md) | 1mo–12mo | 8 | parallel bureau tracks, 30-day dispute clocks, a monitoring loop that can restart everything |
| [`buy-a-home`](journeys/buy-a-home.md) | 2mo–12mo | 7 | irreversible offer and closing; financing gated on appraisal + underwriting |
| [`get-out-of-debt`](journeys/get-out-of-debt.md) | 3mo–36mo | 6 | a control loop, not a one-shot; reward delayed over years |
| [`job-search-and-switch`](journeys/job-search-and-switch.md) | 4wk–4mo | 6 | never resign before the offer is signed; constant re-planning |

Export the planning traces with `python3 scripts/export.py --format journeys`. New journeys welcome — see [`journeys/README.md`](journeys/README.md).

---

## 📐 Design principles

1. **Every step states its expected observation.** A step list without expectations is prose; the *Expect:* clause is what makes a recipe executable and trainable.
2. **Verification is a predicate, not a vibe.** "You are done when…" must be checkable by a program or a stranger — it compiles into a reward function.
3. **Irreversible steps are marked ⚠️ inline** — payments, deletions, hot liquids, handed-over packages. Agents must learn *where to stop and confirm*, and that signal lives in the data.
4. **Failure modes are first-class.** Real procedures go wrong in known ways; the recovery paths are half the knowledge.
5. **Generic first, locale variants second.** The `generic` recipe stands alone; `us-nyc` / `jp-tokyo` / `cn-beijing` variants layer on top.
6. **Multimodal, with text as the floor.** Recipes can attach diagrams, photos, and clips per step via the `media` frontmatter (roles: action-demo, expected-observation, diagram, warning, overview), each with a full alt description so every recipe still trains text-only models. See the fare-gate diagram in [`transit/ride-a-subway.md`](transit/ride-a-subway.md) and the rack layout in [`embodied/kitchen/load-a-dishwasher.md`](embodied/kitchen/load-a-dishwasher.md).

---

<a id="roadmap"></a>
## 🗺️ Roadmap

The corpus spans **2937 recipes across all 17 domains** and keeps growing. Where help lands hardest:

- [ ] Locale variant packs: `jp-tokyo`, `cn-beijing`, `de-berlin`, and yours
- [ ] `reviewed` and `verified` promotions (agent-executability evidence; see CONTRIBUTING)
- [ ] Embodied recipes → simulator task compiler
- [ ] Multimodal coverage: a diagram for every embodied recipe
- [ ] Pre-built SFT/eval exports as tagged releases

---

<a id="contributing"></a>
## 🤝 Contributing

One recipe = one markdown file = one PR.

1. Copy [`TEMPLATE.md`](TEMPLATE.md) into the right domain directory
2. Write the procedure you actually know (original content only)
3. `./scripts/validate.sh` until green ✅
4. Open the PR

The short rules: every step needs an *Expect:* · verification must be checkable · irreversible steps get ⚠️ · embodied recipes need the robot frontmatter. Full rules in [CONTRIBUTING.md](CONTRIBUTING.md).

**🌍 Locale expertise is especially welcome.** Recipes for how things work in *your* city make agents useful beyond the defaults.

---

<a id="citing"></a>
## 📎 Citing and using the data

Recipe content is CC-BY-4.0: training (including commercial) is fine with attribution; see [LICENSE](LICENSE). Export formats are documented in [`scripts/export.py`](scripts/export.py)'s header, and each JSONL record carries the recipe `id` for attribution. If you use the corpus in research:

```bibtex
@misc{howto2026,
  title  = {howto: an open library of everyday procedural knowledge for training agents and robots},
  author = {{howto contributors}},
  year   = {2026},
  url    = {https://github.com/ShirleyHuang11/howto}
}
```

---

<div align="center">

Code: [MIT](LICENSE) · Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

**⭐ Star this repo if your agent ever confidently deleted the wrong file, skipped the step that actually mattered, and reported success.**

</div>
