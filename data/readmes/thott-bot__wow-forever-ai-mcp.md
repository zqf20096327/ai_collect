<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/media/mark-dark.svg">
  <img src=".github/media/mark-light.svg" width="88" alt="thott.bot">
</picture>

# thott.bot

**Everything about World of Warcraft: Forever in your AI, from every change to live auction prices.**<br>
Everything about WoW Forever, in the chat app you already use.

<a href="https://thott.bot/ai"><img src=".github/media/ai-questions.avif" width="100%" alt="An AI chat with thott.bot answering five World of Warcraft: Forever questions: where to get a sleeping bag, the most popular Retribution Paladin builds, what to cook, new gear for a level 28 warrior, and what's new for warriors at 20."></a>

**[Add to ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6ac3efb508348191a717c69b6e2f775d)** · **[Different AI?](#which-ai-apps-does-it-work-with)** · **[thott.bot](https://thott.bot)**<br>
**About 20 free questions** a month, no card needed.

</div>

## Close your other tabs.

Anything you'd look up is already in your chat.

## Why thott.bot

- **Everything, connected.** Quests, items, recipes, NPCs and maps are linked: what a quest needs, where that item drops, where you turn it in, what it crafts. Your AI gets the whole picture in one place, not scraps from dozens of random sites.
- **Current to the minute.** Every new build, patch and hotfix reaches thott.bot within minutes of landing, even the silent ones.
- **Straight from Blizzard.** Game facts come from Blizzard's own files and posts, not old guides or forum guesses. Community guides are labeled as such.

## What it knows

- **Your characters:** link Battle.net and your AI knows the characters you actually play, their gear, talents, quests and more, updated every time you log out.
- **Patch notes and changes:** every build and hotfix, and exactly what each changed.
- **Quests and leveling:** every quest, its chain, route and rewards, and leveling guides.
- **Talents and builds:** the builds players run right now, counted daily from millions of real characters at every level, every spec's talent pick rates, and every talent change.
- **Spells and abilities:** every spell and ability, and every change to each.
- **Classes and races:** every class, race and racial, and what Forever changed for each.
- **Items and gear:** every item and item set, where it drops and who sells it.
- **Crafting and professions:** every profession, recipe and reagent, what each reagent makes, and profession leveling guides.
- **Auction house:** live prices on every WoW Forever auction house, hourly.
- **The world:** zones, maps, flight paths, dungeons, raids and bosses, battlegrounds.
- **Collections:** mounts, pets, toys, achievements, reputations and holidays.
- **Interface and addons:** every setting, key binding and chat command, the addon API and banned addons.
- **Blizzard news:** news and developer posts (blue posts) from the official forums.

In ChatGPT and Claude, ask to see it: your characters' sheets with the gear and stats they logged out with, the game's own tooltips, clickable talent trees, quest chains, maps and before-and-after cards.

## Ask the way you already do

- Where do I get the sleeping bag in WoW Forever?
- What's the most popular Fire Mage build in WoW Forever right now?
- How do I level cooking cheaply in WoW Forever?
- What new gear should my level 28 warrior look out for in WoW Forever?
- I play a Paladin. What changed for me in WoW Forever this week?
- Build me a cooldown-tracker addon. What can the Forever client's API do in combat?

## Can't my AI already do this?

Yeah, badly. Your AI learned WoW once, the day its training stopped, and it has been behind on every change since. To
cover the gap, it searches the web and stitches together SEO spam, forum guesses and guides for older patches.
thott.bot connects it straight to the game, current within minutes of every change.

## Which AI apps does it work with?

Any app that supports MCP, including ChatGPT and Codex with the official thott.bot plugin, Claude on every plan,
Claude Code, Cursor and Hermes.

The first connection opens a sign-in page (Discord, Google or email), which creates a free account.

### ChatGPT and Codex

Install the [official thott.bot plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ac3efb508348191a717c69b6e2f775d),
then sign in.

### Claude

[Add thott.bot to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=thott.bot&connectorUrl=https%3A%2F%2Fmcp.thott.bot%2Fmcp)
opens Claude's Add custom connector dialog with the name and address filled in. Select Add, then Connect, and sign in.

### Claude Code

```
claude mcp add --transport http --scope user thott https://mcp.thott.bot/mcp
claude mcp login thott
```

### Codex CLI

```
codex mcp add thott --url https://mcp.thott.bot/mcp
```

That opens the sign-in itself; if it doesn't, run `codex mcp login thott`.

### Cursor

[Add thott.bot to Cursor](https://cursor.com/install-mcp?name=thott&config=eyJ1cmwiOiJodHRwczovL21jcC50aG90dC5ib3QvbWNwIn0%3D)
opens Cursor with thott.bot filled in. Then sign in.

### Hermes

```
hermes mcp add thott --url https://mcp.thott.bot/mcp --auth oauth
```

That opens the sign-in itself; if it doesn't, run `hermes mcp login thott`.

### Any other app

Add `https://mcp.thott.bot/mcp` wherever it adds a remote MCP server (Streamable HTTP, OAuth sign-in).

[Steps for each app](https://thott.bot/setup)

## Is this an MCP server?

Yes, a remote MCP server at `https://mcp.thott.bot/mcp`. Your AI signs in with OAuth and gets read-only tools to
search the game, open full entries, track every change between builds, and show answers as interactive displays.

## Is this just scraped from other sites?

No. thott.bot reads Blizzard's own game files, news and forum posts. Community data, like quest and loot details, comes
only from projects that explicitly allow it to be used this way, and it's always credited.

## Does thott.bot read my chats or train AI on them?

thott.bot only sees what your AI sends when it looks something up: the short search it writes and basic details like
which app and model. It never sees your conversation, your messages or your AI's replies, and none of it is used to
train AI models.

## What does it cost?

It's free for about 20 questions each month, no card needed. [Unlimited](https://thott.bot/plans) has no monthly limit.

## In your game, too.

Bring your AI into Azeroth with [thott.bot chat](https://github.com/thott-bot/chat), the free addon.

## What's in this repository

- `.cursor-plugin/` and `mcp.json`: the Cursor plugin.
- `hermes/`: the Hermes plugin.

There's no server code here: the plugins point your app at `https://mcp.thott.bot/mcp`.

[![thott.bot MCP connector](https://glama.ai/mcp/connectors/bot.thott/thott-bot/badges/score.svg)](https://glama.ai/mcp/connectors/bot.thott/thott-bot)
