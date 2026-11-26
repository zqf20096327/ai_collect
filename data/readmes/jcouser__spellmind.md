<p align="center">
  <img src="art/source/logo.png" alt="Spellmind" width="120">
</p>

<h1 align="center">Spellmind: AI Companion</h1>

<p align="center">
  An AI companion for <b>World of Warcraft: Forever</b>. It knows your character as you play and helps with what you're deciding: your quest route, dungeons, gear, talents, spells, professions and gold.<br>
  <b>Free and open source. Advice only: it never plays for you.</b>
</p>

<p align="center">
  <a href="https://github.com/jcouser/spellmind/releases/latest">Download the app</a> ·
  <a href="https://www.curseforge.com/wow/addons/spellmind-ai-companion">The addon on CurseForge</a> ·
  <a href="docs/install.md">Install guide</a> ·
  <a href="docs/privacy.md">Privacy</a> ·
  <a href="docs/screen-reading.md">How it reads the game</a> ·
  <a href="docs/faq.md">FAQ</a>
</p>

<p align="center">
  <img src="docs/images/chat-gear-and-route.png" alt="Spellmind's chat window: a shift-clicked quest reward judged against the gloves you wear, then what's left to do in Westfall, with the quest givers and the road to Lakeshire, and follow-up questions" width="760">
</p>

> **Unofficial.** Spellmind isn't made, reviewed or endorsed by Blizzard Entertainment. World of Warcraft is a trademark of Blizzard Entertainment, Inc.

## What it does

Spellmind is two parts:

- **The addon**, in the game. It works on its own, with no app and no AI: a quest route built from your own quest log, what your quests lead to, which dungeons fit your level, gear and bag advice, talents to take next, spells to train, profession caps and gold. Quiet nudges by the minimap tell you when something's waiting.
- **The free desktop app** (Windows 10 and 11). It sends your question, with the game data you allow, to **your own AI**, and brings the answer back into the game's chat window.

| | Addon alone | Addon + app |
|---|---|---|
| The quest route: your steps, an arrow, the world map and minimap, where to go next | ✓ | ✓ |
| Quests, Dungeons, Gear, Talents, Spells, Professions, Gold tabs | ✓ | ✓ |
| Tooltip lines, nudges, waypoints on click | ✓ | ✓ |
| Chat: ask anything about your character | | ✓ |
| "Break it down" on quests, items, trainers and merchants | | ✓ |
| "Review my route": what to skip, and why | | ✓ |
| Read your leveling guide's page (talents, rotation) | | ✓ |

### Your quest route

Turn it on in the **Route tab** (or `/sm route`). Spellmind plans your leveling from your own quest log and where you stand, keeps the plan up to date as you play, and shows you the way: in a small window that stays on screen, with an arrow, and on the world map and minimap.

<p align="center">
  <img src="docs/images/route-wetlands-map.png" alt="The world map in the Wetlands: from Dun Algaz, a gold line to step 1, then numbered purple steps around Menethil Harbor, each objective's area shaded, joined by the route's line" width="900">
</p>

**How it plans**

- **The shortest order that works:** every pickup, objective and turn-in around you, in an order that keeps the quests' own rules. A quest is picked up before its objectives, the objectives come before the turn-in, and a chain goes in order. Follow-up quests are planned after the turn-in that opens them.
- **Quests that fit you:** quests above your level wait until you're ready (or in a group), and ones you can't take aren't listed.
- **The mobs nearest your way:** a kill or collect step goes to the group of mobs that's least out of your way, not just the biggest. In the Wetlands above, that turned 20,900 yards of walking into 16,100.
- **Worth the walk?** A far quest that gives little XP for the walk is marked "worth skipping?" and comes later. Skip any step; Back brings it back.
- **Up to date by itself:** steps tick off the moment you finish them, and the plan is made again when your quest log changes. It holds still while you're on a flight path, and picks up where you land.

**On your screen**

- **The route window:** your current step, then the next ones, numbered as on the map, each with what else is done at the same spot ("Also here: 2 to pick up"). It stays on screen through reloads, where you put it and at the size you left it, and folds down to the current step alone.
- **The arrow:** points to your next step with the yards to it, along the roads you've walked rather than straight through a mountain.
- **The world map:** numbered steps, the current one gold; each objective's area shaded; a line from you to the current step and on through the rest.
- **The minimap:** the current step and the next one, with thin lines to them. On the rim with an arrow when it's farther.
- **When you're there:** inside an objective's area, the arrow says "You're in the area", the minimap shades it faintly, and no line points at its middle.

**Where next, and the way there**

- **When a zone runs dry,** Spellmind ranks the best zones for your level by the quests actually left for you there, and the time to get there.
- **Pick one, and the route takes you there,** holding to it through the zones on the way, and a reload, until you arrive. "Quest here instead" changes your mind.
- **The way there, leg by leg:** the flight paths you know, the roads between zones, the tram, the boats and your hearthstone. The route window lists the legs, and the arrow and the map follow them.

**Ready for a dungeon:** pick a dungeon on the Route tab (or **Route** on the Dungeons tab). Spellmind routes you through its quests and the questlines that open them, across zones, to its door, and the turn-ins after the run.

**Your class quests:** the questlines for your class (a new form, a pet, a totem, a weapon), wherever they start. The Quests tab and the Route tab list them with the step you're on and where to go, one per level milestone: the versions offered in other races' starting areas fold under your own. **Route** plans the way through one, across zones, by boat and flight path, and the route window points out one that's ready while you quest. A nudge says when a new one opens at your level. Class quests, and quests whose reward is an upgrade for you, are never marked "worth skipping?".

<table>
  <tr>
    <td width="58%"><img src="docs/images/route-class-tab.png" alt="The Route tab for a level 25 dwarf rogue: Plan for, then the class questlines (The Touch of Zanzil, The Syndicate Sting, and two low level ones with their other versions under them), then the dungeons, each with Route or Prep"></td>
    <td width="42%"><img src="docs/images/route-class-window.png" alt="The route window on a class questline, Destiny Calls: pick up The Apple Falls in Teldrassil, the way there by the boats from Menethil Harbor to Auberdine and Rut'theran, then Darnassus"></td>
  </tr>
  <tr>
    <td><img src="docs/images/route-class-map.png" alt="The world map: the way to a class quest across the sea, from the Wetlands by boat to Auberdine, then on to Teldrassil"></td>
    <td><img src="docs/images/route-in-area-minimap.png" alt="The minimap among the crocolisks of the current step: no line from you to it, the line on to the next step"><br><img src="docs/images/route-in-area-arrow.png" alt="The arrow inside the step's area: You're in the area, Young Crocolisk Skins 0 of 6"></td>
  </tr>
</table>

<p align="center"><img src="docs/images/route-class-nudge.png" alt="A nudge by the minimap: Class quest ready, The Syndicate Sting, with Dismiss and Ask" width="380"></p>

**It learns your roads:** as you walk, swim and ride, Spellmind remembers the way you went, so the arrow and the lines follow real paths. They stay on your PC; **Forget my trails** on the Route tab clears them.

**Ask about it:** with the app, your AI sees the same route. "Review my route" says what to skip and why, with a **Skip** button for each, and "Why this order?" explains it. Without the app, `/sm route why <step>` says why a step is where it is.

Every part has its own switch on the Route tab: the window, the arrow, the steps on the world map, the minimap, and the lines on each. Works best with [Questie](https://www.curseforge.com/wow/addons/questie) installed: it adds the quests to pick up and where the mobs are. Without it, the route covers the quests in your log.

<table>
  <tr>
    <td width="45%"><img src="docs/images/route-wetlands-tracker.png" alt="The route window in the Wetlands: pick up Daily Delivery now, then numbered steps 2 to 7, some with what else is done there, where to go next with travel times, and quests elsewhere"></td>
    <td width="55%"><img src="docs/images/route-where-next.png" alt="Done in Redridge: next, Wetlands, with 13 quests to pick up about 8 minutes away by flight; or Stormwind City or Ashenvale by boat"><br><br><img src="docs/images/route-trail.png" alt="The world map at Lakeshire: the green line to the flight master follows the road you walked, across the bridge, not a straight line" width="300"></td>
  </tr>
  <tr>
    <td><img src="docs/images/route-minimap-line.png" alt="The minimap near Algaz Station: the line from you to your next step"></td>
    <td><img src="docs/images/route-map-steps.png" alt="The world map in Duskwood: numbered steps, the current one gold, and the area where step 2's skeletons are, shaded"></td>
  </tr>
</table>

### Ask your AI, in game

<table>
  <tr>
    <td width="55%"><img src="docs/images/break-it-down.png" alt="Break it down on a quest: beside the quest log, a card says to hand The Defias Brotherhood to Wiley the Black upstairs in the Lakeshire inn, and the road there from Duskwood"></td>
    <td width="45%"><img src="docs/images/chat-auction-house.png" alt="The chat answering what in your bags is worth selling on the Auction House: gems, leather and a recipe, and to keep the leatherworking materials for your own skill-ups"></td>
  </tr>
  <tr>
    <td><b>Break it down:</b> click the Spellmind mark on a quest, an item, a trainer or a merchant, and your AI explains that exact thing.</td>
    <td><b>Chat:</b> ask about your gear, bags, route, talents or gold. Shift-click items and quests into the box; the buttons under an answer ask the obvious next question.</td>
  </tr>
</table>

Things to ask:

- "Should I take [Dusty Mining Gloves] from this quest?"
- "What should I do next here?" or "Plan my next hour"
- "What in my bags is worth selling on the Auction House?"
- "Plan my next 5 talent points"

Answers use your real character: your gear, quest log, talents, gold and where you are. When an answer sends you somewhere it knows the coordinates of, a **Pin** button under it sets the game's map pin and arrow. With web search on, your AI can check quest and NPC details online, and answers that name places, NPCs or routes are double-checked before you see them (a switch in Settings turns that off).

### The panel, no AI needed

<table>
  <tr>
    <td width="50%"><img src="docs/images/quests-tab.png" alt="The Quests tab: quests ready to turn in with their XP and distance, how far they take you into your level, and the dungeon your quests are for"></td>
    <td width="50%"><img src="docs/images/dungeons-tab.png" alt="The Dungeons tab: the Deadmines quests in your log, the questlines that lead there with the step you're on and who to hand it to, and the dungeons at your level"></td>
  </tr>
  <tr>
    <td><b>Quests:</b> what to turn in, what to do now and here, and what's worth skipping, with Go to set a waypoint.</td>
    <td><b>Dungeons:</b> which dungeons your quests are for, the questlines that lead there, and what's at your level.</td>
  </tr>
  <tr>
    <td><img src="docs/images/gear-tab.png" alt="The Gear tab: quest rewards within reach that upgrade your hands and wrists, your weakest slots, and what's worth a look in your bags, from a sword you can't use yet to Leatherworking materials"></td>
    <td><img src="docs/images/spells-tab.png" alt="The Spells tab: what your trainer has for you now and what it costs, what comes next by level, and your guide's priority"></td>
  </tr>
  <tr>
    <td><b>Gear:</b> upgrades within reach from your quests' rewards, your weakest slots, and what your bags are good for.</td>
    <td><b>Spells:</b> what to train now and what it costs, what's coming, and your guide's rotation.</td>
  </tr>
  <tr>
    <td><img src="docs/images/talents-tab.png" alt="The Talents tab: your guide's next points and other builds"></td>
    <td><img src="docs/images/settings-tab.png" alt="The Settings tab: switches for each mark on the game's windows and each kind of nudge"></td>
  </tr>
  <tr>
    <td><b>Talents:</b> your leveling guide's build, read by your AI, with the next points to take.</td>
    <td><b>Settings:</b> every mark and nudge has its own switch, and you choose which game data your AI gets.</td>
  </tr>
  <tr>
    <td align="center"><img src="docs/images/nudge-toast.png" alt="A nudge: 5 spells to train, with Dismiss and Ask"></td>
    <td align="center"><img src="docs/images/tooltip-quest.png" alt="Spellmind's tooltip on a quest: its level against yours, what's left, where it is on the map and the rewards"></td>
  </tr>
  <tr>
    <td><b>Nudges:</b> a quiet toast by the minimap when something's waiting: spells to train, points to spend, gear about to break.</td>
    <td><b>Tooltips:</b> Spellmind's lines on quests and items: difficulty, what's left, upgrades, and what to sell, with its vendor price.</td>
  </tr>
  <tr>
    <td align="center"><img src="docs/images/tooltip-item.png" alt="An item tooltip with Spellmind's lines: the stat changes against the belt you wear, and worse than yours: sell, or the auction house, with its vendor price"></td>
    <td align="center"><img src="docs/images/tooltip-item-skill.png" alt="A mace tooltip with Spellmind's lines: no One-Handed Maces skill yet, a weapon master may teach it, so sell unless you'll learn it, with its vendor price"></td>
  </tr>
  <tr>
    <td><b>On items:</b> better or worse than what you wear, by how much, and what to do with it, with its vendor price.</td>
    <td><b>Knows your skills:</b> a weapon you can't use yet but can learn says so, instead of just "sell".</td>
  </tr>
  <tr>
    <td colspan="2" align="center"><img src="docs/images/minimap-button.png" alt="Spellmind's minimap button with its tooltip: click for the chat, right-click for your last tab, drag to move it around the map"></td>
  </tr>
  <tr>
    <td colspan="2"><b>Minimap button:</b> click for the chat, right-click for your last tab. <code>/sm minimap off</code> hides it.</td>
  </tr>
</table>

Also in the panel:

- **Professions:** what to do next for each profession, and when it's near its cap.
- **Gold:** what came in and went out this session and today (and per hour), what's coming up (spells to train, repairs), and what your bags are worth at a vendor, and on the Auction House from Auctionator's last scan if you have Auctionator.

#### In the game's own windows

- **Quest log:** Spellmind's mark on a quest's details. Hover for its level against yours, what's left, where it is and its rewards; click to have your AI break it down.
- **Item tooltips:** better or worse than what you wear and by how much, whether you can use it, and what to do with it, with its vendor price.
- **Quest rewards:** which reward to pick when you turn a quest in.
- **Character sheet:** a dot on a slot that has a better item waiting in your bags.
- **Merchant** and **class trainer:** what to sell, and what to train first.

#### Nudges

A small toast by the minimap, never in combat and never a stream of them: spells to train, a class quest ready, talent points to spend, gear about to break, bags nearly full, a dungeon you just entered, quests ready to turn in, professions near their cap. Each kind has its own switch, and **Dismiss** means not again for the same thing.

### The app

<p>
  <img src="docs/images/desktop-app.png" alt="The desktop app's window: connected to WoW, signed in with a ChatGPT plan, GPT-6 Luna at Medium thinking with web search on, and the addon up to date" width="420">
</p>

Pick your AI, its model and thinking level. It sits by the clock while you play, keeps the addon up to date and updates itself.

## Your AI, your choice

The app talks to the AI you pick. You pay that AI (or use a plan you already have); Spellmind itself is free and has no account or subscription.

- **ChatGPT plan** (Plus or Pro): sign in in your browser, no API key.
- **An API key** for Claude (Anthropic), ChatGPT (OpenAI), Grok (xAI) or Gemini (Google).
- **Other:** any OpenAI-compatible service, such as OpenRouter or Groq, or a model on your own computer with Ollama or LM Studio.

Keys and sign-ins stay in Windows' Credential Manager on your PC (on Linux, your desktop's keyring). The game never sees them.

## Install

**The addon:** from [CurseForge](https://www.curseforge.com/wow/addons/spellmind-ai-companion) (WoW Forever), or the `Spellmind-<version>.zip` on the [releases page](https://github.com/jcouser/spellmind/releases/latest), unzipped into `World of Warcraft\_forever_\Interface\AddOns`. The zip carries the addon and its parts (`Spellmind_S001` to `Spellmind_S200`, which bring answers in); keep them all.

**The app:** `Spellmind-Setup-<version>.exe` from the [releases page](https://github.com/jcouser/spellmind/releases/latest). It needs no admin rights, finds your WoW folder, installs the addon if it isn't there, and walks you through setting up your AI. [The install guide](docs/install.md) covers checking the download, the SmartScreen warning, updating and removing it.

**The app on Linux (preview):** `Spellmind-<version>.AppImage` from the same page, for WoW Forever running under Proton or Wine (Faugus, Steam, Lutris, Heroic, Bottles). Make it executable and run it; it needs `python3`. [The install guide](docs/install.md#the-app-on-linux-preview) has the steps and what to do if it can't see the game.

Spellmind works alongside Questie and Auctionator, and uses their data when they're installed, but needs neither. It's made for WoW Forever (1.60.1).

## Commands

| Command | What it does |
|---|---|
| `/sm` | Open or close the chat |
| `/sm quests`, `dungeons`, `gear`, `talents`, `spells`, `professions`, `gold`, `settings` | Open that tab |
| `/sm <question>` | Ask your AI (with the app) |
| `/sm app` | Where to get the free app |
| `/sm route` | The quest route on or off (the Route tab has its switches) |
| `/sm route why <step>` | Why a step is where it is: what must come before it, and how long the route would be with it earlier |
| `/sm arrow` | The route's arrow on or off |
| `/sm news` | What's new in this version |
| `/sm welcome` | The first-time welcome again |
| `/sm guide <link>` | Import your leveling guide (with the app) |
| `/sm nudges on`, `off`, `reset` | The nudges |
| `/sm marks on`, `off` | Spellmind's marks on the game's windows and its tooltip lines |
| `/sm minimap on`, `off` | The minimap button |
| `/sm help` | All the commands |

## Privacy, in short

- **Never sent:** your character's name, realm or guild, your account, other players' names or chat.
- **Sent to your AI only, when you ask:** your question and the game data you allow (class, level, gear, quests, talents and so on; each part has a switch in Settings).
- **To the Spellmind authors, only the ground you walk:** with the app, the squares you walk help build the shared roads every player's route follows. No times, no character, no account; a crossing is shared only once 2 players walked it. "Share the ground I walk" on the Route tab turns it off.
- **No telemetry, no analytics.**

The details are in [docs/privacy.md](docs/privacy.md).

## How it works

An addon can't reach the internet or write files while you play, so the two parts talk through the screen and the addon folder:

1. The addon draws a small strip of colored squares in the corner of the game's window, holding your question.
2. The app reads only that strip, from the game's window, and sends the question to your AI. [What it reads, and what it doesn't](docs/screen-reading.md).
3. The answer comes back as files in the addon's own folders, which the addon loads.

The app never reads the game's memory, never sends keys or clicks, and never changes the game's files outside Spellmind's own addon folders. [The design notes](docs/design.md) have more.

## Building from source

Node 22.19 or newer.

```
npm ci
npm test                              # the addon (in a Lua VM), the app's core and the link
node tools/package-addon.mjs          # dist/Spellmind-<version>.zip, for CurseForge
cd app/desktop && npm ci && npm start # the app from source
npm run dist                          # (in app/desktop) the Windows installer and its SHA-256
```

The app's screen-reading helper is C, built with `npm run capture:build` (Git Bash with MinGW-w64's gcc) or `core/capture/windows/build.sh` (Zig 0.16.0). Releases are built by [GitHub Actions](.github/workflows/release.yml) from a tagged commit; [docs/releasing.md](docs/releasing.md) has the steps.

## Code signing policy

The Windows installer is unsigned for now, so Windows SmartScreen warns on its first run: check each download against its SHA-256 ([install guide](docs/install.md)). The project applied to [SignPath Foundation](https://signpath.org)'s free signing for open-source projects in November 2026; they asked it to come back once it has more of a community, and it will.

When it's signed: *Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation](https://signpath.org).*

- **Only this project's own files are signed:** the installer built from this repository's source by [the release workflow](.github/workflows/release.yml) on GitHub's own runners, from a tagged commit.
- **Committers and reviewers:** [jcouser](https://github.com/jcouser). Changes from anyone else come as pull requests and are reviewed before they're merged.
- **Approvers:** [jcouser](https://github.com/jcouser) approves each signing request by hand.
- **Privacy:** Spellmind sends the Spellmind authors only the ground you walk, for shared roads (a switch on the Route tab turns it off). It sends your questions and the game data you allow to the AI you chose, only when you ask, and checks this repository's releases for new versions (a switch turns that off). See [docs/privacy.md](docs/privacy.md).

## Support and security

- Questions and bugs: [GitHub issues](https://github.com/jcouser/spellmind/issues). Leave out your character's name, keys and anything personal.
- Security problems: see [SECURITY.md](SECURITY.md); please don't open a public issue.

## License

MIT, see [LICENSE](LICENSE). Parts come from NeverQuestAlone and wow-ai under the MIT license: see [NOTICE](NOTICE.md). The Spellmind name and artwork aren't covered by the license.
