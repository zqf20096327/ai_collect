English | [繁體中文](README.zh-TW.md)

# Game DNA

**103 game elements for your coding agent. Pick one, bring your browser game, and the agent wires it into your code,
from damage numbers to dynamic lights.**

### ▶ [Open the gallery](https://game-dna.pages.dev)

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![elements](https://img.shields.io/badge/elements-103-orange)](https://game-dna.pages.dev/site/preview/) [![cold-tested](https://img.shields.io/badge/cold--tested-on_unseen_games-brightgreen)](https://game-dna.pages.dev/site/preview/tests/) [![live demo](https://img.shields.io/badge/live_demo-game--dna.pages.dev-ff69b4)](https://game-dna.pages.dev/site/preview/)

<p align="center">
<a href="https://game-dna.pages.dev/site/preview/#video"><img src="docs/media/promo-cover.jpg" width="720" alt="Watch the Game DNA promo video (35 s)"></a>
</p>

<p align="center">
<a href="https://game-dna.pages.dev/site/preview/dna/damage-numbers/"><img src="docs/media/damage-numbers.gif" width="32%" alt="Bouncing damage numbers"></a>
<a href="https://game-dna.pages.dev/site/preview/dna/bullet-patterns/"><img src="docs/media/bullet-patterns.gif" width="32%" alt="Bullet-pattern emitter"></a>
<a href="https://game-dna.pages.dev/site/preview/dna/kart-racer-3d/"><img src="docs/media/kart-drift.gif" width="32%" alt="Arcade kart racer (3D starter game)"></a>
</p>

## How it works

1. **Pick an element** in the [gallery](https://game-dna.pages.dev).
2. **Play its demo** to see what it adds.
3. **Tell your agent one sentence** in your game's folder:

```text
Add Game DNA's damage-pop element to my game: follow https://github.com/lucemia/game-dna/blob/main/elements/damage-pop/prompt.md and use the module in https://github.com/lucemia/game-dna/tree/main/elements/damage-pop/module.
```

More: [How it is built and tested](https://game-dna.pages.dev/site/preview/blog/how-game-dna-works/) · [Start in 5 minutes](https://game-dna.pages.dev/site/preview/start/) · [step by step](#give-one-to-your-agent)

## Why

Ask a coding agent to "add damage numbers" and it will. Then the numbers overlap the HUD, the boss fight stops
working, or the old save screen quietly breaks. A one-line ask leaves the agent guessing at everything that makes a
feature feel right.

Game DNA gives the agent three things instead of a guess:

- **a module**: a small, dependency-free JavaScript file that does the work (MIT);
- **a prompt** (at most 600 words) that says where to hook it into *your* game, what not to touch and the usual mistakes;
- **a way to check it**: self-checks without a browser and acceptance checks you can see.

Every element also has a playable demo. 83 are add-ons that drop into any game (feel, effects, UI, audio,
lighting); 20 are systems (battles, map flows, a kart racer) that come as a starter game your agent extends.
All art is original; most of it is drawn in code.

## Mix several elements

The [Basket](https://game-dna.pages.dev/site/preview/basket/) on the site lets you pick several elements, checks that they work together, and writes one
combined prompt plus a zip of the modules for your agent.

<a href="https://game-dna.pages.dev/site/preview/basket/"><img src="docs/media/basket.png" width="720" alt="The Basket: three elements picked and the combined prompt"></a>

## The elements

All 103, by category. Click **play** for the element's page with its live demo and prompt. ✦ = the demo uses AI-generated art.

<a href="https://game-dna.pages.dev/site/preview/dna/horde-survival/"><img src="docs/media/og-horde-survival.jpg" width="360" alt="Horde survival auto-attacker"></a>

<details><summary><b>Battle systems</b> (15)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Active-time gauge battle** | Every combatant's gauge fills in real time at a speed-based rate; a full hero gauge opens that hero's command window. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/active-time-battle/) |
| **Auto-resolved squad clash with forecast** ✦ | Two squads on 2x3 grids (front row takes melee, back row is shielded from it while the front stands) meet; before committing. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/squad-clash/) |
| **Bullet-pattern emitter** | Enemies cast bullet patterns described as data: fans and aimed bursts, rings, spirals, flowers whose speed dips between petals, weaving waves. | [play](https://game-dna.pages.dev/site/preview/dna/bullet-patterns/) |
| **Card battle with intents** ✦ | A turn-based card battle: draw a fanned hand each turn, drag a card onto a foe (a target arrow follows; keys and taps work too) and pay its cost from a small… *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/card-battle/) |
| **Combat forecast window** | Before an attack is confirmed, a two-sided window shows what will happen: both units' HP now and after, damage, hit and critical chances. | [play](https://game-dna.pages.dev/site/preview/dna/combat-forecast/) |
| **Conditional tactic rules** ✦ | Every unit decides with an ordered list of rules, "condition → action (target)": ally HP under a threshold, a flying or armoured foe, a back-row target. | [play](https://game-dna.pages.dev/site/preview/dna/tactic-rules/) |
| **Four-move menu battle with type matchups** | Turn-based creature battle, one on one (or two on two): each creature has up to four moves with uses left and a type; a type chart doubles. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/four-move-battle/) |
| **Horde survival auto-attacker** ✦ | The hero only walks (keys, WASD or a touch stick); weapons fire by themselves on timers: orbiting blades, a bolt at the nearest foe. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/horde-survival/) |
| **Match-3 battle board** ✦ | A puzzle battle on an 8 x 8 gem board: swap two neighbours to line up 3 or more; matches clear, gems fall and cascades chain (each step worth more). *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/match3-battle/) |
| **Motion-input special moves** | Reads the stick and buttons once per fixed step into a short input buffer and recognises special-move motions written relative to the way the hero faces. | [play](https://game-dna.pages.dev/site/preview/dna/motion-inputs/) |
| **On-map skirmish exchange** | The attack exchange plays on the map itself instead of cutting to a side-view scene (the alternative to Side-view clash cut-in clash-cutin). | [play](https://game-dna.pages.dev/site/preview/dna/on-map-skirmish/) |
| **Real-time sword combat** | Top-down real-time melee on the map: a 4- or 8-way sword swing with anticipation, active and recovery frames and a sweeping arc hitbox. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/sword-combat/) |
| **Side-view clash cut-in** | When a turn or tactics battle confirms an attack, the game cuts to a staged side-view scene. | [play](https://game-dna.pages.dev/site/preview/dna/clash-cutin/) |
| **Squad formation grid** | Each side fights as squads on a 2x3 grid: a front row that faces the enemy and a back row behind it. | [play](https://game-dna.pages.dev/site/preview/dna/squad-formation/) |
| **Tower placement & wave spawner** | A tower-defense core: foes march along a fixed road through a grid (one or more paths from waypoint cells); towers go on the grass cells beside it. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/tower-defense/) |

</details>

<a href="https://game-dna.pages.dev/site/preview/dna/modern-particles/"><img src="docs/media/og-modern-particles.jpg" width="360" alt="Modern particle system"></a>

<details><summary><b>Effects &amp; feel</b> (15)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Bouncing damage numbers** | On the frame a hit lands, the amount pops above the target, each digit bouncing in turn with a small overshoot, holds, then fades; heals, criticals, misses. | [play](https://game-dna.pages.dev/site/preview/dna/damage-numbers/) |
| **Dissolve-out defeat** | A defeated unit blinks white and dissolves from a snapshot of its sprite (dither-noise fade, horizontal slice wipe, pixel crumble with gravity,… | [play](https://game-dna.pages.dev/site/preview/dna/dissolve-defeat/) |
| **Hit sparks & spell bursts** | On the frame a blow lands, a few frames of impact at the contact point (slash streak, star burst, cross spark or ring shockwave) with pooled pixel sparks… | [play](https://game-dna.pages.dev/site/preview/dna/hit-sparks/) |
| **Hit-stop, shake & flash** | On a hit the world freezes for a few frames (hit-stop), the play field shakes by whole pixels and decays, and the struck sprite turns white for a frame or two. | [play](https://game-dna.pages.dev/site/preview/dna/hit-stop-shake/) |
| **Loot drops with rarity beams** ✦ | Defeated foes and opened chests pop loot that arcs out with a ground shadow, lands with a bounce on free ground (landing spot and whole flight path tested… | [play](https://game-dna.pages.dev/site/preview/dna/loot-beams/) |
| **Modern particle system** ✦ | One pooled, seeded engine for thousands of smooth particles: emitter shapes (point, line, circle, rect, sprite outline). | [play](https://game-dna.pages.dev/site/preview/dna/modern-particles/) |
| **Physics debris & breakables** ✦ | Breakable props, either the game's own art (painted or pixel) or built-in crates, barrels, pots, statues and crystals. | [play](https://game-dna.pages.dev/site/preview/dna/physics-debris/) |
| **Procedural IK creatures** | The game's ground-walking foes become many-legged creatures (spider, crab, centipede) whose feet plant on the game's own ground with 2-bone IK and step when… | [play](https://game-dna.pages.dev/site/preview/dna/ik-creatures/) |
| **Ribbon trails** ✦ | Smooth tapered ribbons behind anything fast: a sword swing leaves a swept crescent from hilt to tip, a dash or lunge a soft body-wide ribbon. | [play](https://game-dna.pages.dev/site/preview/dna/ribbon-trails/) |
| **Shatter battle transition** | When a battle starts, the current frame is captured, cracks from the point of contact and breaks into shards that spin and fall (or swirls, pixelates… | [play](https://game-dna.pages.dev/site/preview/dna/battle-transition/) |
| **Spring water surface and splashes** ✦ | Pits, ponds and lakes of a side-view game get a surface made of springs: anything that falls in throws a crown of droplets and a curved splash sheet… | [play](https://game-dna.pages.dev/site/preview/dna/water-surface/) |
| **Squash, stretch & anticipation** | Every sprite the game already draws gets procedural squash and stretch about its feet, with no new frames: a crouch before jumps, swings and spells. | [play](https://game-dna.pages.dev/site/preview/dna/squash-stretch/) |
| **Time rewind** ✦ | Hold a key (or the touch button) and the world runs backwards: every fixed step the game's state is deep-copied into a ring buffer. | [play](https://game-dna.pages.dev/site/preview/dna/time-rewind/) |
| **Verlet rope & cloth** ✦ | Capes, scarves, ribbons, hair tufts, banners, hanging ropes and chains that swing with movement and wind. | [play](https://game-dna.pages.dev/site/preview/dna/verlet-cloth/) |
| **Weather & ambient particles** | Seeded weather drawn in three depth layers behind and in front of the sprites: rain that splashes on the game's own ground line, snow, drifting dust motes. | [play](https://game-dna.pages.dev/site/preview/dna/weather-particles/) |

</details>

<details><summary><b>Generated art</b> (12)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Art-direction lock** ✦ | Generate one style-reference sheet for the game (a character, a prop, a floor patch and an item), lock it. | [play](https://game-dna.pages.dev/site/preview/dna/art-direction-lock/) |
| **Card illustrations** ✦ | Painted 2:3 card illustrations generated once and locked to one style (light from the top-left, the subject in the upper safe area, a calm darker lower half… | [play](https://game-dna.pages.dev/site/preview/dna/card-art/) |
| **Expressive portraits** | Hand-made-looking 16-bit bust portraits built from a small seeded spec (head, skin, eyes, brows, mouth, hair style and colour, ears, hood / helmet / circlet… | [play](https://game-dna.pages.dev/site/preview/dna/expressive-portraits/) |
| **Layered cutout characters** ✦ | HD painted characters built from cut-out parts and moved by a small bone rig in code instead of frame-by-frame drawing. | [play](https://game-dna.pages.dev/site/preview/dna/cutout-characters/) |
| **Material & normal maps** ✦ | A script turns every generated bitmap with alpha into a height map (alpha distance field rounded into a dome, plus the painting's own local light and dark as… | [play](https://game-dna.pages.dev/site/preview/dna/normal-maps/) |
| **NPC generator** | Seeded townsfolk built from parts (age, body type, skin, hair style and colour, clothes, hats, glasses or beards, satchels and scarves). | [play](https://game-dna.pages.dev/site/preview/dna/npc-generator/) |
| **Painted parallax layers** ✦ | The flat background of a side-view HD game becomes 3-5 hand-painted layers (far sky and ridges, drifting clouds, mid hills, near silhouettes, and an opaque… | [play](https://game-dna.pages.dev/site/preview/dna/painted-parallax/) |
| **Palette-swap variants** | One sprite, many looks without new art: the module finds the sprite's colour ramps (clothing, body, skin, steel, outline) and maps them dark-to-light onto… | [play](https://game-dna.pages.dev/site/preview/dna/palette-swap/) |
| **Paper doll** | A layered pixel hero (body, hair, hat, top, legs, boots, weapon, shield) with swappable parts and palette tints. | [play](https://game-dna.pages.dev/site/preview/dna/paper-doll/) |
| **Portrait set with expressions** ✦ | Painted bust portraits for dialogue, generated once: a neutral base per character and each expression made as an edit of that base with the base as… | [play](https://game-dna.pages.dev/site/preview/dna/painted-portraits/) |
| **Talking portraits** | Portraits animated by the dialogue: a typewriter that owns the line (or follows the game's own). | [play](https://game-dna.pages.dev/site/preview/dna/talking-portraits/) |
| **UI frames & icon sheet** ✦ | A generated, style-locked UI kit (nine-slice window and small frames, a selection frame, an item slot, a pointer and a 24-icon sheet). | [play](https://game-dna.pages.dev/site/preview/dna/painted-ui/) |

</details>

<a href="https://game-dna.pages.dev/site/preview/dna/damage-pop/"><img src="docs/media/og-damage-pop.jpg" width="360" alt="Modern damage numbers"></a>

<details><summary><b>UI &amp; text</b> (12)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Bevelled window + pointer cursor** | A drop-in replacement for plain text boxes and menus: bevelled gradient windows that grow from their centre when they open. | [play](https://game-dna.pages.dev/site/preview/dna/window-cursor/) |
| **Big banner text** | Phase, wave and result moments ('PLAYER PHASE', 'WAVE 2', 'STAGE CLEAR', 'VICTORY') get large chunky shaded letters that slide in over a translucent… | [play](https://game-dna.pages.dev/site/preview/dna/big-banner/) |
| **Draining HP bar** ✦ | A hit drops the fill at once while a pale loss segment holds where the health was, then drains down; quick hits extend the hold and merge into one segment. | [play](https://game-dna.pages.dev/site/preview/dna/draining-hp-bar/) |
| **Keyword tooltips** ✦ | Rich text whose keywords (statuses, stats, terrain, rules) open a tooltip on mouse hover, touch long-press or tap and keyboard focus: icon, title. | [play](https://game-dna.pages.dev/site/preview/dna/keyword-tooltips/) |
| **Minimap** | A corner map of the level that the player fills in by exploring: the tile grid (or collision boxes) baked once into a cached image per zoom. | [play](https://game-dna.pages.dev/site/preview/dna/minimap/) |
| **Modern damage numbers** ✦ | 2020s damage numbers: each hit arcs out of the target and lands, crits pop with a big overshoot, a burst and a short shake. | [play](https://game-dna.pages.dev/site/preview/dna/damage-pop/) |
| **Pixel bitmap font** | Every letter on a low-res canvas drawn from an original 1-bit bitmap font at whole pixels, so text is as crisp as the sprites at any scale. | [play](https://game-dna.pages.dev/site/preview/dna/pixel-font/) |
| **Springy UI motion** ✦ | Motion design for the windows and menus a game already draws: panels open with an elastic pop, slide or unfold and close faster than they open. | [play](https://game-dna.pages.dev/site/preview/dna/springy-ui/) |
| **Title screen & menu flow** | A title screen built on the game's own art (its name as a bold pixel logo with a glint, a tagline, PRESS START), a menu (continue, new game, options, quit). | [play](https://game-dna.pages.dev/site/preview/dna/title-menu/) |
| **Toasts & unlock pop-ups** ✦ | Achievement, quest-update and item-get notices slide in from a screen edge, stack and glide, leave on a visible timer line. | [play](https://game-dna.pages.dev/site/preview/dna/toasts/) |
| **Turn-order bar** | A strip of small portraits showing who acts next: the current actor sits first in a gold frame and bounces, the next 6-10 units follow in team-coloured frames. | [play](https://game-dna.pages.dev/site/preview/dna/turn-order-bar/) |
| **World-space HUD** | HUD pieces that live in the world and follow the camera: a ring under every unit's feet with an HP arc whose pale loss segment drains after a hit. | [play](https://game-dna.pages.dev/site/preview/dna/world-hud/) |

</details>

<a href="https://game-dna.pages.dev/site/preview/dna/tactics-grid-3d/"><img src="docs/media/og-tactics-grid-3d.jpg" width="360" alt="3D tactics battlefield on a heightmap grid"></a>

<details><summary><b>3D &amp; 2.5D</b> (10)</summary>

| Element | What it does | Demo |
|---|---|---|
| **3D tactics battlefield on a heightmap grid** | A small three.js battlefield of terraced tiles (grass, stone, sand, water) with trees, rocks and ruins. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/tactics-grid-3d/) |
| **Arcade kart racer (3D)** | A low-poly 3D kart race: a track built from a closed spline (road, kerbs, barriers, ramps, boost pads, start gantry with countdown lamps). *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/kart-racer-3d/) |
| **Belt depth (beat-'em-up lanes)** | Gives every character in a side-view game a depth z on a walkable floor band, as in classic street brawlers. | [play](https://game-dna.pages.dev/site/preview/dna/belt-depth/) |
| **Camera director** ✦ | Replaces a hard-follow camera with a directed one: a critically damped spring with a dead zone, eased look-ahead in the facing or moving direction. | [play](https://game-dna.pages.dev/site/preview/dna/camera-director/) |
| **Painted billboard sprites in a 3D diorama** ✦ | Painted 2D characters stand in a three.js world as camera-facing billboards: yaw-only quads with their feet on the floor or tile top. | [play](https://game-dna.pages.dev/site/preview/dna/billboard-sprites-3d/) |
| **Raycast dungeon** | A first-person grid dungeon crawler drawn by raycasting: one DDA ray per screen column with the perpendicular distance (no fisheye, no gaps). *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/raycast-dungeon/) |
| **Sprite stacking (pseudo-3D props from pixel slices)** | Turns props (crates, barrels, trees, rocks, houses, wells, stalls, carts, a vehicle, lamps, fences) into pseudo-3D objects made of stacked pixel slices. | [play](https://game-dna.pages.dev/site/preview/dna/sprite-stacking/) |
| **Third-person 3D character and camera** | A low-poly adventurer on a small 3D island seen from a smooth follow camera: camera-relative movement (keys or touch stick). *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/third-person-3d/) |
| **Toon outlines and cel shading for a three.js scene** | One call turns an existing three.js scene cel-shaded: every lit material becomes a toon copy with 2-4 light bands, a cool shadow tint. | [play](https://game-dna.pages.dev/site/preview/dna/toon-outlines-3d/) |
| **Wave-collapse town builder (3D)** | A cosy three.js town builder on a grid: click a cell to raise it (sea, land, a house, more storeys) and wave function collapse resolves every wall, door. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/wfc-town-3d/) |

</details>

<a href="https://game-dna.pages.dev/site/preview/dna/vision-cones/"><img src="docs/media/og-vision-cones.jpg" width="360" alt="Stealth vision cones"></a>

<details><summary><b>Maps &amp; movement</b> (10)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Enemy threat range** | One key or button paints every tile any enemy could move to or strike this turn as a red tinted zone with a crisp marching outline. | [play](https://game-dna.pages.dev/site/preview/dna/threat-range/) |
| **Fog of war** | On a tile map, everything outside your units' sight sinks under a slowly drifting, dithered fog with a soft one-tile edge; terrain stays faintly readable. | [play](https://game-dna.pages.dev/site/preview/dna/fog-of-war/) |
| **Grappling hook & swing** | Fire a hook at iron rings (aim assist) or any rock surface, hang on a rope of fixed length and swing like a pendulum, pump with left / right, reel in and out. | [play](https://game-dna.pages.dev/site/preview/dna/grapple-swing/) |
| **Grid movement range + path arrow** | Select a unit on a tile map to see every tile it can reach (blue, terrain-cost aware) and every tile it can strike (red). *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/grid-range-path/) |
| **Isometric height & jump** | A 2:1 isometric tactics map where every tile has a height: units climb at most their jump, shoot farther from high ground, hit harder from above or behind. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/iso-height-map/) |
| **Level-select path reveal** | An overworld map between levels: level, secret, castle, save-hut, shop and bonus nodes joined by paths; the hero walks node to node along the paths. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/level-select-map/) |
| **Platformer movement feel** | Side-view hero movement and tile collision that feels good: acceleration curves on the ground and in the air, variable jump height, coyote time. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/platformer-feel/) |
| **Procedural dungeon floors** | A turn-based dungeon crawl on seeded floors: rooms placed at random, joined by a minimum spanning tree of corridors plus a few loops, doors and arches. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/dungeon-floors/) |
| **Pseudo-3D flight ground** | Call a mount on the top-down map and the ground zooms, turns and tilts into a perspective, scanline-scaled plane with a horizon sky band. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/pseudo3d-flight/) |
| **Stealth vision cones** | Guards see through view cones clipped by walls (a ray-cast visibility polygon, the same rays that decide who is seen). | [play](https://game-dna.pages.dev/site/preview/dna/vision-cones/) |

</details>

<details><summary><b>Economy &amp; growth</b> (8)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Branching run map** ✦ | The roguelite route between fights: a seeded map of floors whose battle, elite, event, shop and rest nodes are joined by paths that never cross. | [play](https://game-dna.pages.dev/site/preview/dna/run-map/) |
| **Crafting recipes** ✦ | A recipe book with discovery and a slot bench over the game's own inventory: learned recipes in colour (a green dot when craftable now, a sparkle when new). | [play](https://game-dna.pages.dev/site/preview/dna/crafting-recipes/) |
| **Farming plots** | A farm loop on a tile grid: till, plant, water, crops grow one stage-step per watered night with every stage drawn, harvest once. *(starter game)* | [play](https://game-dna.pages.dev/site/preview/dna/farming-plots/) |
| **Level-up stat growth** | Experience and levels for a party: after a fight a results window counts EXP and gold up, each unit's gauge fills and wraps with LV UP! | [play](https://game-dna.pages.dev/site/preview/dna/level-up-growth/) |
| **Shaped inventory packing** ✦ | A grid bag where every item takes its real shape (1x1 potions, 1x3 staves, a 5-cell axe, L, T, S and plus pieces). | [play](https://game-dna.pages.dev/site/preview/dna/shaped-inventory/) |
| **Shop & inventory grid** | A modal shop window: buy and sell lists with icons, prices and an amount picker, a bag grid with stacks, a max stack and a capacity, tooltips. | [play](https://game-dna.pages.dev/site/preview/dna/shop-inventory/) |
| **Stamina & outpost rest** | Squads (or a hero) spend stamina on every march and every attack; at zero they are exhausted. | [play](https://game-dna.pages.dev/site/preview/dna/stamina-rest/) |
| **Upgrade draft (pick 1 of 3)** ✦ | The roguelite level-up choice: at a moment the game chooses (level-up, chest, wave clear) the world pauses and three upgrade cards deal in with a fan. | [play](https://game-dna.pages.dev/site/preview/dna/upgrade-draft/) |

</details>

<details><summary><b>Foundations</b> (6)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Multi-layer parallax backdrop** | A flat single background becomes 3-6 generated, original pixel-art layers (dithered sky, clouds or a cave ceiling, far range, back range, a tree / cliff /… | [play](https://game-dna.pages.dev/site/preview/dna/parallax-layers/) |
| **Native resolution + integer scaling** | A game that stretches its small canvas with CSS (blurry, uneven pixels) becomes pixel-perfect: the canvas keeps drawing at its native size. | [play](https://game-dna.pages.dev/site/preview/dna/pixel-scaler/) |
| **Save & load slots** | A save/load screen with three slots (plus an autosave slot): each shows a tiny thumbnail point-sampled from the game's own screen at native resolution. | [play](https://game-dna.pages.dev/site/preview/dna/save-slots/) |
| **Seeded replay & ghost** | Records every run as its seed plus the player's raw input on each fixed step, and plays it back through the game's own step function to the identical end… | [play](https://game-dna.pages.dev/site/preview/dna/seeded-replay/) |
| **Touch controls with edge-latched input** | A pixel-style D-pad or virtual stick with A/B buttons and a START pill appears on phones, below the game canvas. | [play](https://game-dna.pages.dev/site/preview/dna/touch-controls/) |
| **WebGL post-process pipeline** | The game keeps drawing on its own 2D canvas; each frame that canvas becomes a texture on a WebGL layer laid exactly over it. | [play](https://game-dna.pages.dev/site/preview/dna/webgl-post/) |

</details>

<details><summary><b>Audio &amp; rhythm</b> (5)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Adaptive music** | Layered music that follows the game's state over chip music: each chip channel is a stem (bass, drums, melody, a tense danger line), drums come in for fights. | [play](https://game-dna.pages.dev/site/preview/dna/adaptive-music/) |
| **Beat judge** | A beat clock and an input reviewer for rhythm actions: every press the game accepts is rated Perfect, Good or Miss against the nearest beat. | [play](https://game-dna.pages.dev/site/preview/dna/beat-judge/) |
| **Chip music** | A four-channel chip band synthesized in Web Audio from pattern data: two pulse leads with duty cycle, a stepped triangle bass and a noise drum kit. | [play](https://game-dna.pages.dev/site/preview/dna/chip-music/) |
| **Procedural sound effects** | Fourteen game sounds (hit, crit, coin, jump, land, footstep, menu move / confirm / cancel, explosion, laser, power-up, heal, hurt) synthesized live with Web… | [play](https://game-dna.pages.dev/site/preview/dna/procedural-sfx/) |
| **Timing-bar minigame** | Any 'skill check' moment (picking a lock, a timed attack bonus, forging, reeling in a fish) opens a small window with a bar. | [play](https://game-dna.pages.dev/site/preview/dna/timing-bar/) |

</details>

<details><summary><b>Dialogue &amp; story</b> (5)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Branching choices with flags** | After a line of dialogue, a small window of 2 to 4 options opens beside the text box: arrows move a hand cursor, Z / tap picks. | [play](https://game-dna.pages.dev/site/preview/dna/dialogue-choices/) |
| **Quest log & objectives** | Quests as data with ordered steps and counters: the game only reports what happened (kill, collect, talk, reach) and the module advances the right step. | [play](https://game-dna.pages.dev/site/preview/dna/quest-log/) |
| **Scripted cutscenes** | A small script plays a scene in the game's own world: characters walk to points with real walk frames that advance with the distance they cover and always… | [play](https://game-dna.pages.dev/site/preview/dna/scripted-cutscenes/) |
| **Typewriter dialogue box** | Story text in a framed box at the bottom (or top) of the screen: each line types out letter by letter with small pauses at punctuation. | [play](https://game-dna.pages.dev/site/preview/dna/dialogue-box/) |
| **World-space bark bubbles** ✦ | Short lines in speech bubbles above characters, in the world, while the game keeps running: guards shout "Halt!" in a yellow alarm bubble when they spot you. | [play](https://game-dna.pages.dev/site/preview/dna/bark-bubbles/) |

</details>

<a href="https://game-dna.pages.dev/site/preview/dna/dynamic-lights/"><img src="docs/media/og-dynamic-lights.jpg" width="360" alt="Dynamic 2D lights &amp; soft shadows"></a>

<details><summary><b>Light &amp; post-processing</b> (5)</summary>

| Element | What it does | Demo |
|---|---|---|
| **Bloom & glow** ✦ | Bright areas bleed soft light: a soft-knee threshold (0..1) picks the bright pixels. | [play](https://game-dna.pages.dev/site/preview/dna/bloom-glow/) |
| **Colour grading LUT** ✦ | The whole picture is graded through a 32x32x32 colour lookup table (a 1024x32 strip texture) on the WebGL post-process pipeline WebGL post layer. | [play](https://game-dna.pages.dev/site/preview/dna/color-grade-lut/) |
| **Dynamic 2D lights & soft shadows** | Point lights and spotlights with soft falloff, colour and deterministic flicker; lights that ride on actors (a torch on the hero, glowing projectiles)… | [play](https://game-dna.pages.dev/site/preview/dna/dynamic-lights/) |
| **Normal-mapped sprite lighting** ✦ | Sprites catch the light: every sprite drawn through the module writes its normals (from an Material & normal maps normal map, or derived from the drawn… | [play](https://game-dna.pages.dev/site/preview/dna/normal-lighting/) |
| **Screen-space distortion** ✦ | The finished picture bends like hot air, water and lenses: heat haze rising over fires, a slow wobble under water. | [play](https://game-dna.pages.dev/site/preview/dna/screen-distortion/) |

</details>

## Give one to your agent

Works with any coding agent: Claude Code, Codex, Cursor or similar. You need a browser game (one HTML file is enough).

1. **Pick an element.** Play a few demos on the [site](https://game-dna.pages.dev/site/preview/) and choose one. Small add-ons are the easiest first try.
2. **Copy the prompt** from its page (or `elements/<id>/prompt.md`) and put the module from `elements/<id>/module/`
   in your game's folder. Systems also come with a starter game in `elements/<id>/starter/`.
3. **Paste the prompt to your agent** in your game's folder and add one line about your game, e.g.
   *"My game is index.html; hits happen in attack()."* Then play it: the element shows up where the demo showed it,
   the game still plays to the end, and the console is clean.

What a prompt looks like (from [`elements/damage-numbers/prompt.md`](elements/damage-numbers/prompt.md), shortened):

```markdown
# Add bouncing damage numbers to my game

You are given `damage-numbers.js`, a finished module (glyphs, motion, all kinds, stacking, drawing). **Include it verbatim** (`<script src>` before the game script, or pasted unchanged into its own `<script>`). Never rewrite or "fix" it. It defines one global, `GameDNA_DamageNumbers`.

Only wire it in. Add code; never replace or rename existing functions.

**Integration points** …

**Acceptance checks** (screenshots if you can)
1. A sword hit shows a white number above the target on the hit frame. Its digits pop up one after another, bounce, hold, then fade.

…
```

## How it's tested

An element counts only when an agent that has never seen it can add it to a game it has never seen.

- **Cold tests.** A separate agent gets only the prompt and the module, plus a host game written by yet another agent
  that never saw the modules: a turn-based battle, a tactics map, a side-scroller, a top-down adventure and two HD
  games. Most elements run three times on each of two hosts and must work at least two times out of three on each.
- **A judge that plays.** A different agent opens the result in Playwright and plays it: does the element show up where
  and when it should, does the game still reach its end, any console errors? More than 700 judged runs so far.
- **A strict visual critic.** Every demo is judged against commercial indie games, characters and UI zoomed in, and
  "parts not joined, programmer art, debug leftovers, clashing style" each fail it. When we first applied it, only 18 of
  the 61 demos then existing passed; after new character rigs, shared hand-drawn casts and a pixel scene kit, 60 of 61.

What it taught us: the first version had no modules, only prompts. Three elements, three runs each: 3 of 9 worked.
Rewriting the prompts to forbid each failure made it worse: 1 of 9. Shipping a module that does the work and letting
the prompt only explain how to plug it in: 9 of 9. (Re-run later with one pinned model, prompt alone reached 7 of 9;
prompt plus module stayed 9 of 9.) Four stories like this are in the [method post](https://game-dna.pages.dev/site/preview/blog/how-game-dna-works/).

Every element's rounds, scores and failures, old results included: **[test records](https://game-dna.pages.dev/site/preview/tests/)**.

## License and art

Code, modules and prompts: MIT ([`LICENSE`](LICENSE)). Bundled third-party code:
[`THIRD-PARTY-NOTICES.txt`](THIRD-PARTY-NOTICES.txt) (three.js, MIT).
Most art is drawn in code. Some demo art was made with an AI image generator and is marked ✦ AI art on the site;
what came from where is in [`PROVENANCE.md`](PROVENANCE.md). The modules themselves never call an image generator.
No screenshots, sprites, logos or names from existing games; not affiliated with any game company.

## Feedback

Issues and pull requests are welcome, from one-line bug reports to whole new elements.

- An element broke in your game? **[Tell us what happened](https://github.com/lucemia/game-dna/issues/new?template=element-broke-my-game.yml)**:
  which element, your engine and which coding agent you used.
- Want an effect or system that isn't here? **[Request an element](https://github.com/lucemia/game-dna/issues/new?template=request-an-element.yml)**:
  describe it in words; genre words are enough, no game names needed.
- Want to build one yourself? Read [`CONTRIBUTING.md`](CONTRIBUTING.md#propose-or-add-an-element) and open a pull request.

**If Game DNA saved your agent a few rounds, a ⭐ helps others find it.**
