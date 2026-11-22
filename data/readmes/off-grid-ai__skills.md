# Stop babysitting your AI. Make it build, test and ship like a senior team.

[![graph-engineering on a real change: every screen the AI changed, before and after on one page. 105 screens from one ask across 7 apps, and only the calls that need you](assets/graph-engineering-demo.gif)](assets/graph-engineering-demo.mp4)

These are the skills I use every day. I built [Off Grid AI](https://github.com/off-grid-ai/OGAM) on my own with them, and it reached 250,000+ downloads on 7 platforms without spending a dollar on ads. Install them and your AI works the way mine does.

[![Off Grid AI, built by one person with these skills: 250,000+ organic downloads on 7 platforms](assets/built-with-these-skills.png)](https://github.com/alichherawalla)

## What these skills do

Vibe coding gets you a demo in an afternoon. Then your AI breaks things that already worked, every screen looks like every other AI app, and you're asked to approve 50 changed files you can't read.

Each skill is a short playbook your agent reads before it starts, so it tests every change in your real app and checks the design before you see anything. What you get back is one page with every screen before and after, and only the decisions that need you. They're free, MIT licensed, and work in Claude Code, Codex, Cursor and 60+ other agents.

- [Review like a senior engineer, without reading code](review)
- [Your AI stops breaking things that already worked](testing)
- [Change old code without breaking it](codebase)
- [UI that looks like Stripe's designers made it](design)
- [An AI that thinks like your CTO](cto)
- [Launch like a real startup](launch)
- [Get users without ads](growth)
- [Know what makes you money](revenue)
- [Make a game like a studio would](games)

![How it works: you ask for a change, your agent maps everything it touches, makes it, checks it, and hands you one page with only the calls that need you](assets/how-it-works.png)

## Install in one line

Paste this into your agent:

```text
Install the skills from github.com/off-grid-ai/skills
```

Or run it yourself:

```bash
npx skills add off-grid-ai/skills
```

<details>
<summary>Other ways: Claude Code plugin, Codex plugin, no Node</summary>

**Claude Code**
```bash
claude plugin marketplace add off-grid-ai/skills
for s in off-grid-review off-grid-testing off-grid-codebase off-grid-design off-grid-cto off-grid-launch off-grid-growth off-grid-revenue off-grid-games; do claude plugin install $s@off-grid-ai; done
```

**Codex**
```bash
codex plugin marketplace add off-grid-ai/skills
for s in off-grid-review off-grid-testing off-grid-codebase off-grid-design off-grid-cto off-grid-launch off-grid-growth off-grid-revenue off-grid-games; do codex plugin add $s@off-grid-ai; done
```

Each set is its own plugin, so you can drop any you don't want. Skills call each other across sets, so installing all 9 is the safe choice.

**Any agent, no Node**
```bash
curl -fsSL https://raw.githubusercontent.com/off-grid-ai/skills/main/install.sh | bash
```
It links every skill into each agent it finds on your machine. Run it again to update.

</details>

## Try these first

**[graph-engineering](review/skills/graph-engineering): review a change across your whole app on one page.** Ask for one change and you see every place it touches, every changed screen before and after, and only the calls that need you. [graph-engineering-loop](review/skills/graph-engineering-loop) learns the rule behind each call and applies it everywhere.


> *"Use graph-engineering to rename Folders to Projects across the app."*

**[test-like-a-user](testing/skills/test-like-a-user): tests that catch what your users would hit.** It opens the real screen, taps the real button and checks what you'd see. No mocks of your own code, so a green test means it really works.

> *"/test-like-a-user the checkout flow"*

**[argue-with-me](cto/skills/argue-with-me): an AI that tells you when you're wrong.** It checks the facts and keeps your whole goal in view instead of agreeing with whatever you said last.

> *"/argue-with-me we should rewrite the backend in Rust"*

**[resume-any-chat](cto/skills/resume-any-chat): never lose a chat again.** Find any past session by its name, even from another account or from Codex, and carry on where it stopped.

> *"/resume-any-chat the onboarding redesign"*

## All 49 skills

### [Review like a senior engineer, without reading code](review)

Your AI changes 50 files and you can't tell what broke. You get one page with every screen it touched, before and after, and only the calls that need you.

![How review like a senior engineer, without reading code works](assets/sets/review-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**graph-engineering**](review/skills/graph-engineering) | Ask for one change. See every place it touches, every screen before and after, on one page. |
| [**graph-engineering-loop**](review/skills/graph-engineering-loop) | Answer a few calls once. It learns your rule, applies it everywhere, and asks you less next time. |
| [**show-me**](review/skills/show-me) | Every screen of your app on one page. Pin a note on the exact spot, like Figma comments. |
| [**safe-to-merge**](review/skills/safe-to-merge) | Your pull request gets every review comment answered and fixed until it's safe to merge. |
| [**code-check**](review/skills/code-check) | A pass or fail on every change before it ships, against one clear bar. |
| [**never-twice**](review/skills/never-twice) | Every review teaches your AI, so the same mistake never comes back. |

### [Your AI stops breaking things that already worked](testing)

You fix one bug and two old features break. Every change gets tested by tapping through your app like a real user, with no mocks hiding the breakage.

![How your ai stops breaking things that already worked works](assets/sets/testing-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**test-like-a-user**](testing/skills/test-like-a-user) | Tests that open the real screen, tap the real button and check what you'd see. No mocks of your own code. |
| [**bug-trap**](testing/skills/bug-trap) | Every bug gets a test that fails first, so it can't sneak back in. |
| [**dont-break-it**](testing/skills/dont-break-it) | Your AI changes, checks and saves code so nothing half-done ships. |
| [**fix-it-for-real**](testing/skills/fix-it-for-real) | It fixes the cause, not the symptom, and reuses what someone already solved. |
| [**click-everything**](testing/skills/click-everything) | It clicks through every page of your web app and fixes what breaks. |

### [Change old code without breaking it](codebase)

You inherit a codebase nobody fully understands, and every change is a guess. Your AI maps it first, shows you what each change will break, and adds tests before it touches anything risky.

| Skill | What you get |
| --- | --- |
| [**learn-this-codebase**](codebase/skills/learn-this-codebase) | Ask anything about a codebase you've never seen, and get answers with the file and line. |
| [**blast-radius**](codebase/skills/blast-radius) | See everything a change will break before it's made. Risky edits wait for your yes. |
| [**tests-for-old-code**](codebase/skills/tests-for-old-code) | Tests for code that never had any, each one run and passing before you see it. |
| [**audit-a-module**](codebase/skills/audit-a-module) | Find out whether to refactor, rewrite or leave a module alone, on one screen. |
| [**stay-in-the-lines**](codebase/skills/stay-in-the-lines) | Your architecture stays the way you drew it, because every change gets checked against your rules. |
| [**plan-from-scratch**](codebase/skills/plan-from-scratch) | Starting fresh? An architect, a product lead and a security lead plan it, and show you where they disagree. |
| [**deploy-without-fear**](codebase/skills/deploy-without-fear) | Deploy on any day. It checks before and after, and tells you the moment to roll back. |

### [UI that looks like Stripe's designers made it](design)

Most vibe-coded apps look the same. Every screen has to clear a real design bar and reuse your best components, and a note on one screen fixes all of them.

![How ui that looks like stripe's designers made it works](assets/sets/design-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**make-it-look-expensive**](design/skills/make-it-look-expensive) | A design bar every screen has to clear before you see it: spacing, states, motion, polish. |
| [**match-the-design**](design/skills/match-the-design) | It builds from your component library with its animations, so no screen looks one-off. |
| [**fix-it-everywhere**](design/skills/fix-it-everywhere) | Leave notes on 3 screens. It turns them into one rule and fixes every screen. |

### [An AI that thinks like your CTO](cto)

No CTO? Your AI picks what's urgent, tells you when you're wrong, keeps building overnight and picks up any old chat where you left it.

![How an ai that thinks like your cto works](assets/sets/cto-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**be-my-cto**](cto/skills/be-my-cto) | Your AI decides what's urgent, does the clear work, and only asks you the real calls. |
| [**build-while-you-sleep**](cto/skills/build-while-you-sleep) | Several AI builders work at once while one checks everything that lands. |
| [**argue-with-me**](cto/skills/argue-with-me) | Your AI argues back with facts instead of agreeing with your worst ideas. |
| [**resume-any-chat**](cto/skills/resume-any-chat) | Pick up any past chat by its name and carry on. Works across Claude Code accounts and Codex. |
| [**no-fluff**](cto/skills/no-fluff) | Short answers, result first, no essays. |

### [Launch like a real startup](launch)

It worked on your laptop and broke on your phone. Every release gets tried on real phones first, then ships with notes people actually read.

![How launch like a real startup works](assets/sets/launch-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**ship-it**](launch/skills/ship-it) | Take any feature all the way to live: built, tested, seen working. |
| [**try-it-on-my-phone**](launch/skills/try-it-on-my-phone) | Your AI checks every release on real phones before your users do. |
| [**run-on-any-device**](launch/skills/run-on-any-device) | Your AI runs and taps through your app on a computer, an iPhone and an Android phone. |
| [**release-day**](launch/skills/release-day) | Clean releases with screenshots on every pull request. |
| [**whats-new**](launch/skills/whats-new) | Release notes your users actually read. |

### [Get users without ads](growth)

Your landing page reads like ChatGPT wrote it. With these, your copy sounds like a person, it sells, and AI search starts naming you.

![How get users without ads works](assets/sets/growth-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**make-it-sell**](growth/skills/make-it-sell) | Headlines and landing pages that sell, built on the rules Ogilvy and Bly wrote down. |
| [**sound-human**](growth/skills/sound-human) | Copy that sounds like a person wrote it, with zero AI tells. |
| [**write-like-me**](growth/skills/write-like-me) | Posts and emails in your own voice, learned from what you've already written. |
| [**get-cited-by-ai**](growth/skills/get-cited-by-ai) | Articles that rank on Google and get you named in ChatGPT-style answers. |
| [**find-threads-to-join**](growth/skills/find-threads-to-join) | The posts worth your reply each day, with two angles ready for each. |

### [Know what makes you money](revenue)

You have Stripe, analytics and store numbers but no idea what to change. You get the three moves that should grow revenue most, and big calls laid out on one page.

![How know what makes you money works](assets/sets/revenue-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**grow-my-revenue**](revenue/skills/grow-my-revenue) | Connect Stripe and your analytics. Get the three moves that grow revenue most. |
| [**help-me-decide**](revenue/skills/help-me-decide) | Any big decision on one page: the answer first, every claim sourced, options scored. |
| [**weekly-wins**](revenue/skills/weekly-wins) | What you shipped this week against last week, and what's next. |
| [**pick-the-best-ai-model**](revenue/skills/pick-the-best-ai-model) | The best AI models for your app on every device, backed by public benchmarks. |
| [**mission-control**](revenue/skills/mission-control) | One page of everything in flight across your projects, with what needs you on top. |

### [Make a game like a studio would](games)

Making a game alone with AI? You get a director, an art director and a QA team that playtests every scene.

![How make a game like a studio would works](assets/sets/games-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**game-director**](games/skills/game-director) | Your AI runs the game like a director: what's fun, what's urgent, what waits. |
| [**art-director**](games/skills/art-director) | Every screen, scene and animation held to one look. |
| [**playtest**](games/skills/playtest) | It plays through every scene and hands you a pass or fail with pictures. |
| [**ship-the-feature**](games/skills/ship-the-feature) | Any game feature taken all the way: built, seen working, pushed, shown. |
| [**prove-it**](games/skills/prove-it) | Proof a change works, with compile checks and renders. |
| [**boot-game**](games/skills/boot-game) | Your whole game stack started in the right order, every time. |
| [**devlog**](games/skills/devlog) | Push, document and show off your progress. |
| [**game-calls**](games/skills/game-calls) | Straight answers when you're making game decisions. |

## Get all 49

```bash
npx skills add off-grid-ai/skills
```

Or paste "Install the skills from github.com/off-grid-ai/skills" into your agent.

## Good to know

- Each skill is a folder with a `SKILL.md`, plain Markdown your agent reads when your request matches it. Nothing runs until you ask.
- Review pages publish as Claude Artifacts when you have them, and as a local HTML page when you don't.
- Skills mention each other by name. Install the whole set to get everything working together.
- The codebase skills started at [Wednesday Solutions](https://wednesday.is) and now need nothing else installed.
- MIT licensed. Third-party files keep their own licenses (see `NOTICE` files).

Made by [Mac](https://github.com/alichherawalla). Follow me on GitHub for new skills as they ship.
