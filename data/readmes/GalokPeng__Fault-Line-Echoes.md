<h1 align="center"><img src="public/sigil.svg" width="34" alt=""> Fault Line Echoes</h1>

<p align="center">An original first-person browser adventure and an installable agent skill for building a game world of your own.</p>

<p align="center"><a href="README.zh-CN.md">中文版</a> · <a href="https://fault-line-echoes.vercel.app/">Play the game</a> · <a href="https://fault-line-echoes.vercel.app/world-skill.html">Get the skill</a> · <a href="https://fault-line-echoes.vercel.app/faultline-local.html">Single-file game</a></p>

![The Alabaster Crown, the starting city in Fault Line Echoes](public/atlas/capital.webp)

## Build your own game with the skill

Tell the agent **what the player does, which choice is difficult and what changes afterward**. You can speak English or Chinese. The agent asks about decisions that affect play, picks the technical approach, builds a working version and tests it. Your world gets its own geography, characters and story. A puzzle about allocating power can start with a switch and a meter; it doesn't need the systems of a first-person adventure.

**Install.** Open the bilingual guide, choose **Download the skill**, unzip it and put the entire `build-game-world` folder in **`.agents/skills/`** inside your game project. Open that project in a new Codex chat and type `$build-game-world` followed by your idea. If you cloned this repository, the skill is already in the project. The guide is a single HTML file: save it locally and it can still generate prompts and extract the complete installable ZIP offline. [Interactive guide](https://fault-line-echoes.vercel.app/world-skill.html) · [Skill source](.agents/skills/build-game-world/SKILL.md) · [Portable guide in Git](public/world-skill.html)

The first design choice is how people will play. If you've specified it, the agent can begin immediately.

| Choose | What your players get |
| --- | --- |
| Single HTML | One file they can double-click. Solo play works offline with the code, art and physics included. Share a new file when you update it. |
| Online link | Players visit a URL and receive updates on refresh. A solo game can use static hosting. Remote friends need a reachable room service to play together. |
| Both | The same rules power an offline solo game and a hosted edition. Players who want rooms can open the online link. |

### Prompts you can actually playtest

**An original small game**

> $build-game-world — Make a single offline HTML game about running a printing press through a two-day blackout. There is paper for two editions. What I print today should change tomorrow's letters and available stories. Show me the paper I have left. Build it and play through two different outcomes.

**An original multiplayer world**

> $build-game-world — Build both editions of a game about two glider pilots repairing a drifting observatory. One pilot can read air currents; the other can anchor a moving platform. In the first mission, either risk the short gap or repair the longer route. Ask me if a choice changes how cooperation feels. Build the mission, then connect two browsers and verify that both players see the same repair finish once.

**Reproduce the full technical example**

> $build-game-world — Rebuild Fault Line Echoes in a new directory using the pinned reference. Produce the offline HTML and the site with real room support. Test a branching quest, two characters, and create/join with two independent clients. Then show me where to build my own region.

The skill includes a source-to-system map and a Python helper that retrieves the exact playable revision. The agent can use a local clone containing that revision or fetch it from GitHub. For a new game, reuse the engineering patterns and write a new story from the player's decisions. [Reference build instructions](.agents/skills/build-game-world/references/reference-build.md)

### A place for character artists and VFX collaborators

Detailed 3D character sculpting is outside my specialty, so I've left room here for professional artists to take the lead. You can still use the skill to integrate your work into a playable game. A collaborator can attach a folder or ZIP, point the agent to it and describe the change in a sentence.

| Delivery | What to give the agent | What the agent checks in play |
| --- | --- | --- |
| Character or outfit | GLB or glTF with its textures, role/skin name, scale, facing, rig and clip names; add editable source and a pose reference if available. | First-person hands, third-person body, idle/move/cast transitions, skin switches and the other player's view. |
| Accessory | Model, target joint/socket, offset or placement image, materials and credit. | Size, handedness, clipping and visibility in the intended poses. |
| Skill effect | Sprite atlas, mesh animation or shader plus textures; action, cast/hit/block event, anchor, timing, blending and a short reference. | The effect follows the correct hand, projectile or surface. A miss and a confirmed block give different feedback, including remotely. |

> $build-game-world — My artist attached a courier GLB and a shield-spark atlas in `art-inbox/courier/`. Fit the coat to the courier's third-person rig. Show sparks at the contact point only on a confirmed block. Use the attached credit and license, verify an ordinary hit and a block, and give us an in-game comparison.

The included example pairs Gu Chao's actual wrist dial with a four-frame block-effect study. The preflight reads model nodes, named clips and referenced files. The agent then tests the result in the renderer. [Artist handoff guide](.agents/skills/build-game-world/references/art-handoff.md) · [Editable handoff manifest](.agents/skills/build-game-world/assets/handoff.example.json) · [Complete sample delivery](.agents/skills/build-game-world/assets/sample-delivery)

![Gu Chao’s wrist dial, the actual GLB included in the art handoff example](docs/images/phase-dial.webp)

## Play Fault Line Echoes

The game currently plays in Chinese. Click **进入主城 · 白砥城** to enter the capital plaza. You can explore freely, talk to residents or press **T** to find a commission. In this original campaign, a sluice rings a third time after a night of rain. The old register calls the downstream village empty. The people still drawing water there tell another story.

### The capital and four regions

The marble capital holds a council hall, working forge, pharmacy, cloth shop, inn, spring and food stalls. Citizens move between places; a witness can call guards if you take someone else's goods. The four gates are about 216 metres from the plaza. Walk through the light curtain to reach the matching **boundary** of the next region. Each wild region spans roughly 1,240 metres across and offers surface, underground and elevated routes.

| West · Verdant Basin | East · The Salt Expanse | North · The Elder Weald | South · The Sundering |
| --- | --- | --- | --- |
| ![Forested river basin](public/atlas/rain.webp) | ![Dunes and salt flats](public/atlas/salt.webp) | ![Root and canopy settlement](public/atlas/root.webp) | ![Sandstone gorge](public/atlas/gorge.webp) |
| Follow the river, ford and stepped falls. The woodland pass continues to the Elder Weald. | Visit the wells and wind tower. The salt-road pass continues to the gorge. | Climb canopy routes and descend into the root archive. | Choose elevated evacuation works or a low maintenance passage. |

### The travellers

All four start unarmed. Six outfit designs fit each traveller. Cosmetics can travel into a duel; equipment bonuses belong to the solo campaign. Open **行者** on the title screen to inspect roles, skill icons and timing hints.

| Traveller | Background and fighting style | Q · E · C · V and passive |
| --- | --- | --- |
| <img src="src/avatar-portraits/leaf-0.webp" width="78" alt="Ye Lan"> **Ye Lan · 叶岚** | A rainforest flood courier who remembers a way down from every high route. Mobile close-range fighter. | 穿步 · 折返 · 余波掌 · 断线. Dash, retreat, project a palm wave, then rush in. A strike after a burst of movement gains extra resonance. |
| <img src="src/avatar-portraits/stone-0.webp" width="78" alt="Xu Li"> **Xu Li · 许砾** | A former sluice mechanic who listens before entering a room. Close-range defender. | 沉肩 · 拨流 · 震台 · 合闸. Shoulder forward, time a parry, send a ground pulse, then land a heavy finisher. Blocking costs him less stamina. |
| <img src="src/avatar-portraits/tide-0.webp" width="78" alt="Gu Chao"> **Gu Chao · 顾潮** | A basin acoustics recorder who follows the third signal with her wrist dial. Ranged pressure. | 直脉 · 折浪 · 退声 · 三拍. Aim a pulse, spread a volley, retreat while casting, or release three distinct shots. Distant hits build extra resonance. |
| <img src="src/avatar-portraits/beam-0.webp" width="78" alt="Lu Heng"> **Lu Heng · 陆衡** | A bridge builder who reads the footings before crossing. Midrange lane control. | 扇潮 · 回折 · 锚步 · 槽涌. Fan a lane, focus a pulse, step in or launch a wide volley. Attack chains can deepen stagger. |

![Sixteen role-specific ability icons in Q, E, C and V order](docs/images/skill-icons.webp)

Move around walls to break aim, use height to change sightlines, chain light and heavy attacks, guard from the front and spend accumulated resonance on an ultimate. Projectiles take time to travel and solid cover intercepts them. Cast, hit and block have separate feedback. [Sixteen first-person casts](docs/images/abilities.webp)

### Quests with physical evidence

The handbook separates available, accepted and completed work. Select an offer for directions, find the giver and accept it in person. Town boards offer local jobs. Across maps, guidance points to the next gate. Several jobs can remain active while you follow one route.

| The field handbook | Evidence in the capital |
| --- | --- |
| ![Quest cards, rewards and guidance](docs/images/handbook.webp) | ![Marked flood gauge and warning bell](docs/images/evidence.webp) |

**The Unsealed Flood Report** starts with clerk Heng Shu. Read the highest fresh mud mark beside the well, sound the warning bell from its inscription, then return for the seal. The prologue leads into nine chapters across the basin. Later you reconstruct a resident list, choose an evacuation route and decide where to divert water. Twelve regional side quests include three hidden clues; the campaign has three endings.

**The Medicine Chest After Rain** starts with apothecary Xie Lanxin at 回春药铺. Leave 4 L free and take the west gate. A short stone ford and a longer high-bank bridge reach the east-bank ferryman. Deep water can tear away an unsecured chest. Follow its red tie downstream and haul it out with **R**. The clothier can secure the strap. Delivery pays eight travel tokens and a keepsake that reflects the recovery.

![High-bank crossing above the medicine route](public/field-guide/upper-bridge.webp)

### Life outside the walls

- **Movement and perception.** Walk, sprint, crouch, jump, swim and climb reachable holds. Stone, timber, sand, forest and water produce different footsteps. Holding quiet-walk suppresses footfall; an animal can still see you. Pursuers search the last known position and return when the chase exceeds their range.
- **Survival.** Exertion, load, heat, food and water affect the expedition. Ask the baker for a bun, fill water at a town well or boil questionable river water at a fire. Rest at an inn until dawn or night. A city guard can help you get a first torch.
- **Hunting and craft.** Thirteen common animals and eight day/night bosses occupy the four regions. Day runs from 06:00 to 18:00. Rest and check the map to find the current boss, habitat and clues. Take meat, hide, shell or another species-specific part. A river buffalo's meat can be cooked; two thick hides and fine linen make a 28 L pack. The smith can turn the salt boss's carapace and claw plates into a helmet.
- **Inventory.** The starting pack has 15 L. Icons show what you carry; volume determines what fits. Examine provenance and uses, eat, equip, trade, craft or put an item down. Equipment slots cover weapon, head, body, legs and feet. Progress and quest objects are saved in the current browser.

![The volume-based field pack, equipment and supply controls](docs/images/pack.webp)

### Two people in one room

Open **联机**, choose duel or co-op patrol, create a room and give your friend the six-digit code or invite link. Invitations last three minutes; a paired session can last up to six hours while both pages stay open. Duels use baseline roles and are first to two wins. In patrol, one player reports a signal from the rain tower while the other confirms it at the old sluice within 18 seconds. Both receive the patrol badge; each keeps a private solo journal. [Open multiplayer](https://fault-line-echoes.vercel.app/?multiplayer=1)

The room starts on a same-origin HTTPS relay, upgrades to WebRTC when available and returns to relay if the direct path drops. The host adjudicates hits, scores and the joint signal. The Vercel deployment uses regional Runtime Cache; local development and preview use an in-memory implementation of the same protocol. A disconnected HTML file plays solo. Its network menu links to the hosted lobby and offers manual connection-code exchange for reachable peers.

![A first-person duel between clients in the running game](docs/images/duel.webp)

### Controls

| Action | Input |
| --- | --- |
| Move and look | WASD and mouse; arrow keys can turn the camera |
| Light / heavy / guard | Left click / X / hold F |
| Skills / ultimate | Q, E, C / V |
| Sprint / silent walk / crouch | Shift / hold Caps Lock / hold Ctrl or tap to toggle |
| Jump / climb | Space / hold Space facing a reachable ledge, rope or tree hold |
| Interact / travel | R / walk through a gate curtain |
| Map / pack / quest handbook | Hold Tab and release to close / B / T |
| Torch / menu | G / Esc |

## Run the project and trace its sources

Use Node.js 22.12+ and npm. `npm ci` installs the locked dependencies. `npm run dev` starts development. `npm test` exercises the game rules, story branches, terrain, art contracts and room behaviour. `npm run build` produces the web edition and `dist/faultline-local.html`; `npm run preview` serves production output and the local room endpoint. On Vercel import the repository root and use the included configuration. For a double-click copy tracked in Git, save [the standalone game](play/faultline-local.html). Run `npm run snapshot:game` to refresh that tracked copy. To rebuild the portable skill guide after editing the skill, run `python scripts/package-world-skill.py`.

| What you see | Where it comes from |
| --- | --- |
| Rendering, character meshes, animation and GLB loading | Three.js (MIT). Original procedural actors and rigs in `src/actors.js` and `src/avatar*.js`. The wrist dial is generated by [its Python source](scripts/model-phase-dial.py) and can be edited in Blender. |
| Physical movement, terrain, water and town life | Rapier 3D (Apache-2.0) handles collisions. Terrain, channels, current, gates, jobs and perception are implemented in `src/biomes.js`, `src/water-*.js`, `src/capital*.js`, `src/settlement*.js` and `src/people.js`. |
| Story, sound and role abilities | The world, characters, storyline and quest chains were created for this game. See `src/story.js`, `src/handbook.js`, `src/medicine.js`, `src/audio.js` and `src/combat.js`. |
| Build and online service | Vite builds the browser client. Vercel Functions and the regional cache support the room API. The application implements transport and game authority in `src/room*.js`, `src/patrol.js`, `api/` and `server/`. |
| External art | Poly Haven CC0 ground and bark textures and two CC0 sky panoramas. The source lists identify individual assets and modifications. The screenshots and portraits shown above are from this project. |

Original code, programmatic art and skill are distributed under MIT. Production builds include dependency notices in `dist/licenses/third-party.md`; the single HTML embeds the notices. [Project license](LICENSE) · [Terrain credits](public/terrain-materials/CREDITS.md) · [Sky credits](public/sky/CREDITS.md) · [Three.js](https://threejs.org/) · [Rapier](https://rapier.rs/) · [Vite](https://vite.dev/)

## Star History

<a href="https://www.star-history.com/?repos=GalokPeng%2FFault-Line-Echoes&amp;type=date&amp;legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=GalokPeng/Fault-Line-Echoes&amp;type=date&amp;legend=top-left&amp;theme=dark" />
    <img alt="GitHub stars for Fault Line Echoes over time" src="https://api.star-history.com/chart?repos=GalokPeng/Fault-Line-Echoes&amp;type=date&amp;legend=top-left" />
  </picture>
</a>

## Community

[https://linux.do](https://linux.do)
