# idea-generation

A Claude and OpenAI Codex skill for brainstorming ideas that are unusual and still workable. The ideas can be anything: research questions, essay topics, stories, side projects, small businesses, fundraisers. It works by first listing the ideas any chatbot would give, banning them, generating from structured prompts, and then running every idea past a skeptical judge before anything reaches you. If it can run Python, it also checks every idea against the obvious ones with a small local embedding model, so the sameness check is actual math.

## Why AI ideas all sound the same

Ask three chatbots for side-project ideas and you get the same ten answers. Research points to a few causes:

- Preference training flattens the output. RLHF cuts output diversity compared with fine-tuning alone ([Kirk et al., ICLR 2024](https://arxiv.org/abs/2310.06452)). Human raters prefer familiar, typical text, so the reward pushes models toward the most stereotypical answer ([Zhang et al. 2025, Verbalized Sampling](https://arxiv.org/abs/2510.01171)). Base models beat their aligned versions on randomness and creativity tasks ([West and Potts 2025](https://arxiv.org/abs/2505.00047)).
- Different models give the same answers. LLM answers to creativity tests look much more like each other than human answers do ([Wenger and Kenett 2025](https://arxiv.org/abs/2501.19361)). Across 26,000 open-ended prompts, different models produced strikingly similar outputs, which the authors call the "Artificial Hivemind" ([Jiang et al., NeurIPS 2025](https://arxiv.org/abs/2510.22954)). Switching apps doesn't help.
- Idea lists run dry fast. GPT-4 idea pools were less diverse than pools from groups of people, and unique ideas got used up quickly ([Meincke, Mollick and Terwiesch 2024](https://arxiv.org/abs/2402.01727)). When thousands of research ideas were generated, most were duplicates ([Si, Yang and Hashimoto 2024](https://arxiv.org/abs/2409.04109)).
- Temperature isn't a creativity dial. It barely tracks novelty and does track incoherence ([Peeperkorn et al., ICCC 2024](https://arxiv.org/abs/2405.00492)).
- The judge has the same bias. LLM evaluators recognize and favor their own output ([Panickssery et al., NeurIPS 2024](https://arxiv.org/abs/2404.13076)), so a model scoring its own ideas drifts back toward the typical ones.

## What the skill does about it

1. It pins down the brief: who it's for, skills, budget, time, limits. If you say "just go", it assumes and lists its assumptions. It also names the kind of idea, which sets what "workable" means (the payoff test in the next section).
2. It writes a cliché wall. It starts with the exact list it would give with no skill, then adds the other ideas any AI would give, plus "clever-sounding defaults" like "AI-powered X" or "a marketplace for Y". Nothing later may be a reworded version of these. You can see the wall in a collapsed section.
3. It draws a map of two axes that matter for the brief, such as who it's for × how it works. The goal is ideas spread across cells, a version of quality-diversity search ([Bradley et al., ICLR 2024](https://arxiv.org/abs/2310.13032)). Only cells where the payoff test can pass count.
4. It generates ideas with forcing techniques: collision with an unrelated field, inversion, underserved users, extreme constraints, time shifts, scale shifts, annoyance mining and outsider views. Each idea gets a rough probability that a typical AI would suggest it, and common ones are cut ([verbalized sampling](https://arxiv.org/abs/2510.01171)). Then a pass rewrites each idea so it works in a bolder way while keeping the same audience ([Meincke et al.](https://arxiv.org/abs/2402.01727)).
5. It runs the vector check (next section) when it can run code: ideas that land in the crowded zone get dropped or reworked, and it writes a few more ideas toward open space.
6. It switches to a skeptical judge. The ideas are rewritten as a bare list with no labels or reasoning and judged as if someone else wrote them. If subagents are available, a separate one does this. Checks: typicality, originality, reality (including licenses, liability and ethics approval), fit, payoff, and a red-team case.
7. It shortlists across the map. A finalist needs Feasibility 4+ and Payoff 3+; novelty breaks ties. Each finalist gets one more check against the cliché wall. You also get one line naming the safest obvious option, so you can weigh the odd ideas against the proven one.
8. It shows its work: the map, finalists with the hardest part, the red-team case and a first step that takes under a week, and a table of dropped ideas so you can rescue anything cut too harshly.

The skill names no example fields or jobs on purpose (see the test results for why).

## Kinds of ideas

The steps stay the same for every brief. What changes is the payoff test, which decides whether an idea is workable, and the skeptic who applies it:

| Kind of idea | Workable means | The skeptic |
|---|---|---|
| Business, product, side project, fundraiser | Someone pays or signs up, and the rough math reaches your goal | An investor |
| Research question | Nobody has answered it yet, you can test it with data and methods you can get, and every possible result tells the field something | A reviewer |
| Essay, thesis or talk topic | The claim is arguable, there is enough evidence for the length, and it says something the standard take doesn't | An editor or grader |
| Story, game, art | The premise can carry the form and length, and a specific audience would pick it over what they already have | A jaded reader |

For anything else, the skill asks what success looks like, or states its own guess. A finalist from a research brief comes with the data or experiment that would answer it and what each result would mean; a finalist from an essay brief comes with a one-sentence thesis, the strongest counterargument and the kinds of sources that back it.

## The vector check

An embedding model turns a sentence into a list of numbers (a vector) that captures its meaning, so ideas that mean similar things end up near each other. Researchers measure the sameness of AI output this way, and AI ideas for a given brief bunch up in one small, crowded region.

`idea-generation/scripts/novelty.py` uses that directly:

1. The skill writes 20 or more obvious ideas for the brief to `obvious.txt`. Embedded, these map the crowded region.
2. The script measures how close the obvious ideas sit to their nearest neighbours. The median of that is the radius of the crowded zone, so the threshold adapts to each brief.
3. Each candidate idea gets embedded and compared with its nearest obvious idea. INSIDE means it sits as close to an obvious idea as obvious ideas sit to each other, and the skill drops or reworks it. EDGE is close but outside. OUT is clear.
4. It also flags near-duplicate candidates and lists the candidates farthest from both the wall and each other. The skill writes a few more ideas in those directions, as long as someone already pays for something similar there.

Distance only measures how unusual an idea is, so the feasibility and demand checks still decide what makes the shortlist.

The model is all-MiniLM-L6-v2, about 80 MB, and it runs on your CPU. There is no API key, and your ideas never leave your machine. On the ideas from the earlier tests, the INSIDE verdict lined up well with a blind judge's "this is an obvious idea" flags (AUC 0.79 to 0.98 across the three briefs).

Setup is optional. Either of these works:

```bash
pip install sentence-transformers          # uses PyTorch
pip install onnxruntime tokenizers numpy   # lighter; the script downloads the ONNX model once to ~/.cache/idea-generation
```

If neither is installed, or the environment can't run code (for example, a Claude.ai chat without code execution, or Codex's sandbox before the model is cached), the script exits with `NO_EMBEDDINGS` and the skill falls back to its word-based check: it estimates how likely a typical AI is to suggest each idea and drops the common ones.

## Install

**Claude.ai / Claude desktop:** zip the `idea-generation` folder (with `SKILL.md` and `scripts/`) and upload it in the Skills section of Claude's settings.

**Claude Code:** copy the folder into your skills directory:

```bash
git clone https://github.com/bndrwe/idea-generation
cp -r idea-generation/idea-generation ~/.claude/skills/
```

Optionally install one of the embedding packages above. Then ask for ideas as normal ("give me side project ideas, I have 5 hours a week"). The skill triggers on brainstorming requests.

**OpenAI Codex (CLI, IDE extension, app):** Codex reads the same `SKILL.md`, so the folder works as is. Copy it into your Codex skills directory:

```bash
git clone https://github.com/bndrwe/idea-generation
mkdir -p ~/.agents/skills
cp -r idea-generation/idea-generation ~/.agents/skills/
```

You can also ask Codex's built-in installer for it: `$skill-installer install https://github.com/bndrwe/idea-generation/tree/main/idea-generation`. If you start Codex inside a clone of this repo, it finds the skill without any install, through `.agents/skills/idea-generation` (a link to the skill folder).

Codex picks up new skills on its own; restart it if the skill doesn't show up. Ask for ideas as normal and it triggers, or call it by name with `$idea-generation` (type `$` or run `/skills` to pick it). `agents/openai.yaml` only sets the display name and a starter prompt for the Codex app.

The vector check needs one extra step under Codex. Its default sandbox blocks network access and writes outside the project, so the script can't download the model to `~/.cache` on its first run. Install one of the embedding packages and run the script once yourself to cache the model:

```bash
printf 'a\nb\nc\nd\ne\n' > /tmp/o.txt && python3 ~/.agents/skills/idea-generation/scripts/novelty.py /tmp/o.txt /tmp/o.txt
```

After that it runs offline. If you skip this, Codex either asks to run the script outside the sandbox or falls back to the word-based check.

## Test results

I tested it on three ordinary briefs: a side project for a solo developer with 5 hours a week, a small business for a retired nurse with $10k, and a $3,000 fundraiser for a high school robotics club. Each brief ran twice with no skill, with the first version of the skill (v1), with a research-based rewrite (v2), and with this version. A fresh model, blind to which version wrote what, grouped duplicate ideas, flagged ones that matched a plain list of obvious answers, and rated workability from 1 to 5.

| | No skill | v1 | v2 | This version |
|---|---|---|---|---|
| Final picks matching the obvious list | 23 of 30 | 9 of 30 | 2 of 30 | 3 of 28 |
| Same idea in both runs | 9 | 6 | 2 | 6 |
| Workability (1-5) | 3.7 | 3.1 | 3.1 | 3.3 |

What the tests changed:

- The skill's own examples became the new cliché. v1 and v2 listed sample fields for the collision technique (beekeeping, maritime law, geology and so on). Those words showed up in 10 of 12 runs, including a beehive voice log as a *software* side project. This version names no examples and has the model list ten unrelated fields and use the last three. The leak went to 0 of 6 runs.
- An obvious idea won. v2 ranked "mobile foot care nurse" first, which the plain model also suggests. Finalists now get a last check against the cliché wall.
- Workability dropped. Unusual ideas are harder to pull off. The strict feasibility and demand bar and the demand math brought it back up to 3.3, and the "safest obvious option" line keeps the proven choice on the table.

Caveats: two runs per brief and one judge, so read the numbers as a direction. The stricter bar also makes runs agree more often (6 repeats). The skill still has a few favorite ideas of its own, like a corporate robot-building night for the robotics club.

### Vector check test

Same three briefs, three runs each, with the model allowed to run code. I compared the previous version (no vector check), a first version of the vector check, and the shipped version, which keeps EDGE ideas and only steers toward open space where people already pay. One blind judge rated all 111 final ideas together.

| | Previous version | Vector check, first try | Vector check, shipped |
|---|---|---|---|
| Final ideas | 39 | 35 | 37 |
| Same idea in two or more runs | 6 | 3 | 3 |
| Match the obvious list | 2 | 0 | 2 |
| Novelty (1-5) | 3.69 | 3.97 | 3.81 |
| Workability (1-5) | 3.23 | 3.23 | 3.32 |
| Rated 4+ on both | 4 | 6 | 7 |

The first try was the most novel, but when the same version was judged against the previous one alone, its workability came out 0.3 lower. The shipped version gives up a little novelty and comes out ahead of the previous version on every row except obvious matches, where it ties. The model ran the script in 17 of 18 runs. Nine runs per version and one judge is still a small sample.

### Research brief test

To check the skill outside business ideas, I ran it twice on a research brief, with code and web search allowed, and once with no skill: *"I'm a first-year PhD student in public health. I can use public datasets and have about $1,000 for collecting my own data. Give me research question ideas for my first paper. Just go, don't ask questions."*

With no skill, the five picks were Medicaid unwinding, heat and mental health, paid sick leave, a message framing experiment, and loneliness. Three of them (Medicaid unwinding, heat, loneliness) are on the skill's own obvious list. The two skill runs gave ten finalists between them, none on the obvious list, and only one (the over-the-counter hearing aid rule) came up in both. Each finalist named its data, its hardest part and what each possible result would mean. Both runs ran the vector check and searched the literature. With two runs and no judge, treat this as a spot check.

## Example output

### A fundraiser

Brief: *"Our high school robotics club needs to raise about $3,000 for competition fees. Give us fundraiser ideas. Just go, don't ask questions."*

With no skill, both runs gave the same list: business sponsorships, a kids' STEM camp, a robot demo booth, crowdfunding, restaurant spirit nights.

With the skill (trimmed):

> **Obvious ideas (skipped):** car wash, bake sale, sponsorship letters, GoFundMe, restaurant spirit nights, raffle, t-shirts, cookie-dough sales, summer robotics camp, robot demo with a donation jar, 3D-printed keychains, trivia night, can drive. *Clever-sounding defaults:* AI tutoring service, marketplace for student 3D prints, gamified donation leaderboard, STEM subscription box, maker community app.
>
> **Safest obvious option:** sponsorship tiers for local businesses ($100, $250 or $500 for a logo on the robot and banner). It's proven, and it pairs well with any idea below.
>
> **1. Gift Assembly Depot.** Parents drop off boxed bikes, playhouses and trampolines at school. The team assembles them and stores them out of sight until pickup on Dec 22-23.
> - Twist: home assemblers charge $60-100 an hour and come to your house. This is cheaper, and it hides the gifts from your kids.
> - Hardest part: secure storage and damage liability. Needs school approval, a signed waiver, intake photos and a locked room.
> - Red team: "Parents won't hand gifts to teenagers." Answer: the advisor supervises, and it's pitched to families who already know the school.
> - Math: about 40 jobs at an average of $55 comes to about $2,200.
> - Scores: Novelty 4, Feasibility 4, Demand 4. First step: get a storage room signed off and post a pricing flyer to the parent list this week.
>
> **2. Office Robot League.** Local companies pay $400 a team to build and battle kit robots over three evenings, coached by students.
>
> **3. Saturday Sharpening Bench.** Walk-up knife, scissor and garden-tool sharpening at holiday markets for $7 each. Math: 60-100 items a market day comes to $400-700, so four or five days bring in about $2,000.
>
> **4. Animated Shop Windows.** Rent simple moving holiday window displays to downtown shops for $250 a season, with a "Built by [School] Robotics" sign.
>
> **Dropped:** wedding cake toppers (Etsy undercuts it), fix-it clinic (Repair Café exists), broken-toy hospital ($10 tickets can't reach $3,000), middle school scrimmage (a standard move for FIRST teams), senior tech help (on every AI list), laser engraving (needs a laser over budget).

### A research question

Same research brief as the test above. Three of the five no-skill picks were on the obvious list below (Medicaid unwinding, heat and mental health, loneliness). With the skill (trimmed):

> **Obvious ideas (skipped):** social media and teen depression, food insecurity and diabetes, Medicaid expansion difference-in-differences, PM2.5 and asthma ED visits, loneliness and mortality, heat waves and mortality, green space and depression, firearm laws, cannabis legalization and youth use, Medicaid unwinding, pharmacy deserts, and 13 more. *Clever-sounding defaults:* machine-learning risk prediction, Google Trends surveillance, wearables, climate anxiety, long COVID and employment.
>
> **Safest obvious option:** food insecurity and cardiometabolic markers in NHANES. It's fast and publishable, but crowded.
>
> **1. Snow days as a test of detection.** Do unplanned weather-related school closures reduce child maltreatment reports, and do reports rebound afterward?
> - Twist: earlier work studied *scheduled* closures, and the COVID studies are confounded. Their open question is whether fewer reports means abuse goes unseen or abuse actually drops. A short, random, weather-driven closure plus a test for a rebound can separate the two. The search found no published snow-day study.
> - Hardest part: no national dataset records closures, so heavy weekday snowfall from NOAA stands in for them. NCANDS gives county codes only for larger counties.
> - Red team: "Snow also changes parents' stress, so it isn't a clean experiment." Answer: split reports by who made them. If detection is lost, reports from school staff fall and then rebound. If abuse actually drops, reports from every source fall and don't rebound.
> - Payoff: a rebound means school staff are the detection system, which argues for maltreatment screening during long closures. No rebound weakens the "hidden abuse" argument against closures.
> - Scores: Novelty 5, Feasibility 4, Payoff 4. First step: start the free NCANDS data application and pull snowfall for the target counties.
>
> **2. OTC hearing aids and the income gap.** Did the 2022 FDA over-the-counter hearing aid rule narrow the income gap in hearing aid use among older adults (NHATS)?
>
> **3. Locked-case health products.** In one metro area, are naloxone, condoms, emergency contraception and pregnancy tests locked up more often in stores in Black and Hispanic neighborhoods? About 100 store visits fit the $1,000.
>
> **4. Where lead pipe status is unknown.** In the EPA-required service line inventories, are "unknown material" lines concentrated in low-income and Black areas after adjusting for housing age?
>
> **Dropped:** elected coroners and heat deaths (the vector check flagged it as too close to "heat and mortality"; the run said it was worth reviving), hospital medical-debt lawsuits (already studied), grey-market insulin listings (no historical data), snow-plow routes and dialysis access (no health outcome).

## License

MIT. See [LICENSE](LICENSE).
