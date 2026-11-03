# StoryCraft

<p align="center">
  <img src="assets/storycraft-logo.jpg" alt="StoryCraft Logo" width="280" />
</p>

StoryCraft is a complete fiction writing methodology for your writing and coding agents, built on top of a set of composable literary craft skills and some initial instructions that make sure your agent uses them.

## Table of Contents

- [How it works](#how-it-works)
- [Getting Started](#installation)
  - [Claude Code](#claude-code)
  - [Antigravity](#antigravity)
  - [Codex App](#codex-app)
  - [Codex CLI](#codex-cli)
  - [Cursor](#cursor)
  - [Devin CLI](#devin-cli)
  - [Factory Droid](#factory-droid)
  - [Gemini CLI](#gemini-cli)
  - [GitHub Copilot CLI](#github-copilot-cli)
  - [Grok Build CLI](#grok-build-cli)
  - [Kimi Code](#kimi-code)
  - [OpenCode](#opencode)
  - [Pi](#pi)
  - [Qwen Code](#qwen-code)
  - [Hermes Agent](#hermes-agent)
  - [Muse](#muse)
- [Publishing Formats and Target Platforms](#publishing-formats-and-target-platforms)
- [The Basic Workflow](#the-basic-workflow)
- [When Something Goes Wrong](#when-something-goes-wrong)
- [Community](#community)
- [What's Inside](#whats-inside)
- [Philosophy](#philosophy)
- [Contributing](#contributing)
- [Security](#security)
- [Updating](#updating)
- [License](#license)
- [State persistence telemetry](#state-persistence-telemetry)

## How it works

It starts from the moment you fire up your agent. As soon as it sees that you want to write a novel or create narrative fiction, it *doesn't* just jump into generating generic, cliché-ridden prose. Instead, it steps back and asks you what you're really trying to do through Socratic creative interview techniques.

Once it has teased a premise and thematic core out of the conversation, it records it in structured format without overwhelming you. 

After you have signed off on the core concept and characters, your agent puts together a macro-level plot and chapter-by-chapter roadmap that breaks the entire book into clear, actionable scenes. It enforces strict scene-and-sequel mechanics, character internal misbeliefs (The Lie), external objectives (Want vs. Need), and measurable value shifts (+ to -).

Next up, once you say "write", it launches an autonomous drafting process using `novel-chapter-drafter` or `novel-scene-beater`. It reads preceding manuscript files, active injuries, and inventory state, and composes chapters grounded in Deep POV (zero filter words), sensory immersion (sound, smell, touch, temperature, somatics), and subtextual dialogue. It runs continuity audits between chapters and updates `story-state.md` after every milestone.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically via workflow slash commands or autonomous orchestration, you don't need to do anything special. Your writing agent just has StoryCraft.

## Installation

Installation differs by harness. If you use more than one, install StoryCraft separately for each one.

### Claude Code

StoryCraft is available via the Claude Code plugin ecosystem.

#### Official Marketplace

- Install the plugin from Anthropic's official marketplace:

  ```bash
  /plugin install storycraft@claude-plugins-official
  ```

#### StoryCraft Marketplace

- Register the marketplace:

  ```bash
  /plugin marketplace add leapwithluvi/storycraft-marketplace
  ```

- Install the plugin from this marketplace:

  ```bash
  /plugin install storycraft@storycraft-marketplace
  ```

- Alternatively, copy the instructions directly into your workspace:

  ```bash
  cp CLAUDE.md ./CLAUDE.md
  cp -r skills/ ./skills/
  ```

### Antigravity

Install StoryCraft as an Antigravity plugin from this repository:

```bash
agy plugin install https://github.com/leapwithluvi/storycraft-skills
```

Antigravity lists each installed skill's description, and the description of the `using-storycraft` skill prompts the model to load that skill at the start of a conversation. Reinstall with the same command to update.

Alternatively, copy the skills directly into your novel project's `.agents/skills` folder:

```bash
mkdir -p /path/to/your/novel-project/.agents/skills
cp -r skills/* /path/to/your/novel-project/.agents/skills/
```

All 23 skills are immediately available via native chat slash commands (e.g. `/using-storycraft`, `/novel-brainstorming`, `/novel-chapter-drafter`).

### Codex App

StoryCraft is available for the OpenAI Codex App.

- In the Codex app, click on Plugins in the sidebar.
- Search for `StoryCraft` in the Writing section.
- Click the `+` next to StoryCraft and follow the prompts.

### Codex CLI

StoryCraft is available for the Codex CLI.

- Open the plugin search interface:

  ```bash
  /plugins
  ```

- Search for StoryCraft:

  ```bash
  storycraft
  ```

- Select `Install Plugin`.

- Alternatively, copy `AGENTS.md` and `skills/` into your project root.

### Cursor

- In Cursor Agent chat, install from marketplace:

  ```text
  /add-plugin storycraft
  ```

- Or copy `AGENTS.md` and `skills/` into your novel project:

  ```bash
  cp AGENTS.md /path/to/your/novel-project/
  cp -r skills/ /path/to/your/novel-project/skills/
  ```

Cursor Agent automatically applies all 23 skills during your writing sessions.

### Devin CLI

- Install the plugin from this repository:

  ```bash
  devin plugins install leapwithluvi/storycraft-skills
  ```

- Update to the latest version with:

  ```bash
  devin plugins update storycraft-skills
  ```

### Factory Droid

- Register the marketplace:

  ```bash
  droid plugin marketplace add https://github.com/leapwithluvi/storycraft-skills
  ```

- Install the plugin:

  ```bash
  droid plugin install storycraft@storycraft
  ```

### Gemini CLI

- Install the extension:

  ```bash
  gemini extensions install https://github.com/leapwithluvi/storycraft-skills
  ```

- Update later:

  ```bash
  gemini extensions update storycraft
  ```

### GitHub Copilot CLI

- Register the marketplace:

  ```bash
  copilot plugin marketplace add leapwithluvi/storycraft-marketplace
  ```

- Install the plugin:

  ```bash
  copilot plugin install storycraft@storycraft-marketplace
  ```

### Grok Build CLI

- Install the plugin from xAI's official marketplace:

  ```bash
  grok plugin install storycraft@xai-official --trust
  ```

- Or open the marketplace in the TUI, search for StoryCraft, and install it:

  ```text
  /marketplace
  ```

### Kimi Code

StoryCraft is available in Kimi Code's plugin marketplace.

- Open Kimi Code's plugin manager:

  ```text
  /plugins
  ```

- Go to `Marketplace` > `StoryCraft` and install it.

- Or install directly from this repository:

  ```text
  /plugins install https://github.com/leapwithluvi/storycraft-skills
  ```

### OpenCode

OpenCode uses its own plugin install; install StoryCraft separately even if you already use it in another harness.

- Tell OpenCode:

  ```text
  Fetch and follow instructions from https://raw.githubusercontent.com/leapwithluvi/storycraft-skills/refs/heads/main/.opencode/INSTALL.md
  ```

### Pi

Install StoryCraft as a Pi package from this repository:

```bash
pi install git:github.com/leapwithluvi/storycraft-skills
```

For local development, run Pi with this checkout loaded as a temporary package:

```bash
pi -e /path/to/storycraft-skills
```

### Qwen Code

Qwen Code installs plugins from Claude Code marketplaces directly.

- Install the plugin from this repository, and pick `storycraft` when prompted:

  ```bash
  qwen extensions install leapwithluvi/storycraft-skills
  ```

- Update later:

  ```bash
  qwen extensions update storycraft
  ```

### Hermes Agent

Install StoryCraft as a Hermes plugin from this repository:

```bash
hermes plugins install leapwithluvi/storycraft-skills --enable
```

### Muse

StoryCraft is available as a native Muse plugin.

- Install from a local checkout:

  ```bash
  muse plugins install ./
  muse plugins approve storycraft
  ```

- Or clone and install:

  ```bash
  git clone https://github.com/leapwithluvi/storycraft-skills.git
  muse plugins install ./storycraft-skills
  muse plugins approve storycraft
  ```

## Publishing Formats and Target Platforms

Fiction is not one-size-fits-all. Publishing format dictates word count targets, pacing rhythms, and cliffhanger density. StoryCraft adapts its drafting and chapter outline engines based on your declared target format in `story-state.md` and `story-bible.md`:

### 1. Webnovel (Royal Road, Webnovel.com, Wuxiaworld, Wattpad, Kakao)
- **Chapter Length**: 1,500 to 2,200 words.
- **Pacing Cadence**: Rapid progression, early dopamine hooks, low travel bloat.
- **Scene/Sequel Ratio**: 80% proactive conflict / 20% compressed sequel.
- **Ending Hook**: Obligatory micro-cliffhanger or status/loot reveal on every chapter without exception.
- **Special Features**: Support for LitRPG status tables, cultivation ranks, and reader comment engagement hooks.

### 2. Traditional Commercial Novel (Trade Publishing, Kindle Direct)
- **Chapter Length**: 2,800 to 4,500 words. Total length: 75,000 to 110,000 words.
- **Pacing Cadence**: Three-Act Nine-Block or Dan Wells 7-Point structure.
- **Interiority**: Deep character psychological transformation (Want vs. Need, The Lie Believed).
- **Ending Hook**: Value shifts (+/-), thematic resonance, or unresolved questions driving act momentum.

### 3. Light Novel & Serial Fiction (Substack, Patreon, Radish)
- **Chapter Length**: 1,800 to 3,000 words. Total length: 40,000 to 60,000 words.
- **Pacing Cadence**: Dialogue-forward, dynamic kinetic scene beats, distinct character voice idiolects.
- **Episodic Structure**: Each chapter features a self-contained micro-climax while contributing to the volume arc.

## The Basic Workflow

1. **using-storycraft** - Activates at session start. Inspects project state, diagnoses bottlenecks, and routes you to the exact next skill needed.

2. **novel-brainstorming** - Activates before outlining or drafting. Draws out your intent, comp titles, tone, and emotional ending vision through Socratic questions.

3. **novel-premise-hook** - Formulates the irreducible 4-Element Logline and the binary Core Dramatic Question that fuels the entire novel.

4. **novel-character-architect** & **novel-worldbuilder** - Constructs the protagonist's Lie, Origin Wound (Ghost), and Want vs. Need, alongside setting sensory ecology and Sanderson's Laws of Magic.

5. **novel-genre-specialist** - Calibrates obligatory scenes, pacing expectations, and trope subversions for your specific genre and publishing format.

6. **novel-plot-architect** & **novel-twist-architect** - Maps macro acts (Three-Act / 7-Point), the tectonic Midpoint Shift, fair-play clue planting, and the 75% Dark Night of the Soul.

7. **novel-chapter-outline** - Decomposes acts into chapter-by-chapter roadmaps with McKee Value Shifts (+/-) and closing cliffhangers.

8. **novel-chapter-drafter** - Executes full chapter or multi-chapter batch drafting. Ingests state, applies Deep POV, sensory textures, and subtextual dialogue into `manuscript/chapter-[N].md`.

9. **novel-continuity-checker** & **novel-pacing-doctor** - Forensic audit of character injuries, inventory custody, and timeline distances; repairs saggy middles and ticking clocks.

10. **novel-session-memory** - Checkpoints project deltas into `story-state.md` and generates the Next Session Bootstrap Prompt to eliminate context-window amnesia.

The agent checks for relevant skills before any task. Mandatory workflows, not suggestions.

## When Something Goes Wrong

Sometimes an AI session misbehaves: the agent produces generic melodramatic dialogue, forgets a character's broken arm from the previous chapter, uses sensory filter words ("she saw"), or stalls in an endless Act 2 travel loop.

Ask your agent to "audit continuity and recent session decisions" and it will invoke `novel-continuity-checker` and `novel-structural-editor`. The skill cross-references recent chapter prose against `story-bible.md`, identifies timeline, inventory, or biometric violations, and provides line-by-line redline corrections.

To recover from a reset session or token truncation, invoke `novel-session-memory` or paste the Next Session Bootstrap Prompt located at the bottom of your `story-state.md` file.

## Community

StoryCraft is built by Leap With Luvi and the open-source fiction engineering community.

- **Issues**: https://github.com/leapwithluvi/storycraft-skills/issues
- **Discussions**: https://github.com/leapwithluvi/storycraft-skills/discussions

## What's Inside

### Skills Library

#### Meta and Discovery
- **using-storycraft** - Autonomous project diagnostic auditor and skill router.
- **novel-brainstorming** - Socratic interview method to uncover core themes, emotional catharsis, and comp titles before outlining.
- **novel-session-memory** - Manages `story-state.md`, tracks active narrative coordinates, and generates zero-latency resume bootstrap prompts.

#### Ideation and Worldbuilding
- **novel-premise-hook** - 4-Element Logline formula, Core Dramatic Question, and What-If escalation ladder.
- **novel-character-architect** - The Lie The Character Believes, Origin Wound (Ghost), Want vs. Need, and ensemble foil architecture.
- **novel-worldbuilder** - Sanderson's Laws of Magic, Iceberg Principle, and P.E.S.T.L.E. sensory ecology framework.
- **novel-genre-specialist** - Obligatory scenes, genre pacing ratios, and trope subversion across Fantasy, Sci-Fi, Mystery, Thriller, Romance, Horror, Historical, and Webnovels.
- **novel-market-analyst** - Commercial viability analysis across physical print and digital platforms (Royal Road, Webnovel, Wattpad, Amazon KDP, KBM/Fizzo, Substack), audience demographics, tag algorithms, and monetization models.

#### Plotting and Structure
- **novel-plot-architect** - Three-Act Nine-Block, Dan Wells 7-Point, Midpoint Reversals, and Kishotenketsu.
- **novel-twist-architect** - Fair-Play Clue Protocol, Recontextualization mechanics, red herring architecture, and Peripeteia & Anagnorisis.
- **novel-chapter-outline** - Deconstructs acts into chapter beats with Robert McKee Value Shifts (+/-), Swain's Scene/Sequel balance, and multi-POV scheduling.

#### Drafting and Scene Craft
- **novel-chapter-drafter** - Autonomous single-chapter and multi-chapter batch drafting workhorse that reads state, bible, and past manuscript chapters.
- **novel-scene-beater** - Jim Butcher Scene & Sequel dynamics, In Late / Out Early cutting, micro-tension injection, and "Yes, but / No, and" outcomes.
- **novel-sensory-immersion** - 5+1 sensory architecture (sound, smell, touch, temperature, somatics), defamiliarization, and objective correlative.
- **novel-deep-pov** - Eliminates sensory filter words ("she saw", "he heard"), Gardner Level 5 psychic distance, and neurobiological reaction sequences.

#### Dialogue and Prose Style
- **novel-dialogue-subtext** - Text vs. Subtext, conversational power dynamics, distinct character idiolect matrices, and prop stage business.
- **novel-prose-stylist** - Gary Provost sentence cadence, active verb surgery, precision nouns, and cliché elimination.

#### Revision and Editing
- **novel-pacing-doctor** - Saw-tooth tension curve diagnosis, time dilation vs. compression, and ticking clock injection.
- **novel-structural-editor** - Setup-and-Payoff matrices, Chekhov's Gun auditing, and Idiot Plot prevention.
- **novel-master-reviewer** - Quad-persona brutally honest developmental audit across 40 craft and commercial vectors, benchmarked against 10-15 industry-leading titles. Supports per-chapter, multi-chapter batch, arc, and full volume review scopes.

#### Continuity and Canon
- **novel-lore-bible** - Single Source of Truth `story-bible.md` management, relational taxonomies, and master timelines.
- **novel-continuity-checker** - 5-Vector forensic audits covering biometrics, biological wound decay curves, inventory custody, and spatial travel logistics.
- **novel-mega-serial-architect** - Hierarchical recursive ledger system for ultra-long serial fiction (500-5,000+ chapters). Prevents memory hallucination, power inflation, dropped subplots, and character drift via volume/arc/chapter ledgers and anti-hallucination sentinel protocols.

## Philosophy

- **Show, Don't Tell**: Emotion is experienced through somatic visceral shocks, objective correlatives, and physical choices—never through detached narration.
- **Fair-Play Narrative**: Plot twists must be seeded in plain sight under linguistic and emotional camouflage so that every reveal is shocking yet inevitable.
- **Cost-Governed Systems**: Limitations and consequences create more dramatic pressure than raw power.
- **Rhythmic Prose**: Sentences must have acoustic musical variety; alternating punchy fragments with lyrical periods.
- **Strict Continuity**: Physical wounds do not vanish overnight; characters do not carry infinite ammunition or teleport across continents.

## Contributing

The general contribution process for StoryCraft is below:

1. Fork the repository.
2. Switch to the `dev` or feature branch (`git checkout -b feat/my-new-skill`).
3. Follow the skill guidelines in `CONTRIBUTING.md` to scaffold new skills.
4. Ensure all 9 mandatory sections from the specification are fully populated with deep literary craft.
5. Run the validation and test suite:
   ```bash
   npm test
   ```
6. Submit a Pull Request with a clear summary of the literary methodologies introduced.

See `CONTRIBUTING.md` for the complete contribution guide and style standards.

## Security

StoryCraft operates under a **zero-dependency, zero-network, local-only** security model:

- **Zero external dependencies**: No `node_modules`, no third-party packages. All scripts use Node.js built-in modules exclusively.
- **Zero network access**: No script or skill file makes any network call. No `fetch()`, no `curl`, no `wget`.
- **Zero telemetry**: All state files (`story-state.md`, `story-bible.md`, manuscript chapters) remain 100% local. Nothing is transmitted to external servers.
- **Automated security scanning**: CI runs integrity checks on every push and PR, scanning for network calls, code execution vectors, obfuscation patterns, XSS injection, and secret material.
- **Pinned CI actions**: All GitHub Actions are pinned to immutable SHA hashes to prevent supply chain attacks.

To report a vulnerability, see `SECURITY.md` for the responsible disclosure process. Do not open public issues for security reports.

## Updating

StoryCraft updates are dependent on your agent harness, but can be updated via CLI or git:

```bash
git pull origin main
npm test
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## State persistence telemetry

Because skills and plugins do not transmit telemetry, StoryCraft relies entirely on local markdown state files (`story-state.md` and `story-bible.md`) stored inside your novel project. No private story data, prompt text, character dossiers, or manuscript prose is ever transmitted to external servers. It is 100% private, local, and confidential.