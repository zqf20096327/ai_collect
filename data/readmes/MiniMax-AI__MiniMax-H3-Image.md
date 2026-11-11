<div align="center">
  <img width="100%" src="assets/minimax-h3-image.jpg" alt="MiniMax H3 image, Open Weights">
</div>

<p align="center">
  <a href="https://hailuoai.video" target="_blank"><img src="https://img.shields.io/badge/Hailuo%20AI-FF6C37?logo=minimax&logoColor=white" alt="Hailuo AI"></a>
  <a href="https://platform.minimax.io" target="_blank"><img src="https://img.shields.io/badge/API-FF6C37?logo=minimax&logoColor=white" alt="API"></a>
  <a href="https://www.minimax.io" target="_blank"><img src="https://img.shields.io/badge/MiniMax%20Website-FF6C37?logo=minimax&logoColor=white" alt="MiniMax Website"></a>
  <a href="https://github.com/MiniMax-AI/MiniMax-H3-Image" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://huggingface.co/MiniMaxAI/MiniMax-H3-Image" target="_blank"><img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black" alt="Hugging Face"></a>
  <br>
  <a href="https://modelscope.cn/models/MiniMax/MiniMax-H3-Image" target="_blank" rel="noopener noreferrer"><img alt="ModelScope MiniMax AI" src="https://img.shields.io/badge/ModelScope-MiniMax%20AI-white?labelColor=%23EF3D5D"></a>
  <a href="https://platform.minimax.cn/docs/faq/contact-us" target="_blank"><img src="https://img.shields.io/badge/WeChat-07C160?logo=wechat&logoColor=white" alt="WeChat"></a>
  <a href="https://discord.com/invite/dbMxutw7tP" target="_blank"><img src="https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/LICENSE-4CAF50?logo=creativecommons&logoColor=white" alt="LICENSE"></a>
</p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.ja.md">日本語</a>
</p>

<h1 align="center">MiniMax-H3-Image</h1>

<p align="center"><b><i>One idea with open weights. A world of uses.</i></b></p>

<p align="center">
  <a href="#prompt-writing-skill">Prompt Writing Skill</a> ·
  <a href="#showcase">Showcase</a> ·
  <a href="#use-online">Use Online</a> ·
  <a href="#overview">Overview</a> ·
  <a href="#run-locally">Run Locally</a> ·
  <a href="#prompting-tips">Prompting Tips</a> ·
  <a href="#license">License</a>
</p>

## Prompt Writing Skill

The `h3-image-prompt-writing` skill turns a short idea, a brief or a set of reference images into a
full MiniMax-H3-Image prompt, and can render it through the MiniMax API. It works in any agent that
reads a `SKILL.md`, such as Claude Code, Codex and Cursor. Install it with the
[skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/MiniMax-AI/MiniMax-H3-Image --skill h3-image-prompt-writing
```

Then ask your agent, for example:

```text
Use h3-image-prompt-writing to make a 3:4 poster of a night market in the rain,
titled "雨夜集市", and render it.
```

Rendering needs `MINIMAX_API_KEY`, and `MINIMAX_API_BASE=https://api.minimax.cn` on the China
platform. See [`skills/README.md`](skills/README.md) for details.

## Showcase

<!-- BEGIN showcase-grid -->
<table>
<tr><th colspan="4" align="left">Advanced Open-Source Capabilities</th></tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/multi-reference.md#sixteen-people-six-scenes"><img src="assets/showcase/tiles/multi-ref-group-a-output.jpg" alt="Sixteen people, six scenes"></a><br><sub><a href="showcase/multi-reference.md#sixteen-people-six-scenes">Sixteen people, six scenes</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/multi-reference.md#outfit-color-coordination"><img src="assets/showcase/tiles/multi-ref-outfit-color-output.jpg" alt="Outfit color coordination"></a><br><sub><a href="showcase/multi-reference.md#outfit-color-coordination">Outfit color coordination</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/multi-reference.md#living-room-from-10-references"><img src="assets/showcase/tiles/furniture-room-output.jpg" alt="Living room from 10 references"></a><br><sub><a href="showcase/multi-reference.md#living-room-from-10-references">Living room from 10 references</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#biology-figure-from-a-paper-page"><img src="assets/showcase/tiles/bio-figure-output.jpg" alt="Biology figure from a paper page"></a><br><sub><a href="showcase/instruction-following.md#biology-figure-from-a-paper-page">Biology figure from a paper page</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#red-panda-infographic"><img src="assets/showcase/tiles/red-panda-infographic.jpg" alt="Red panda infographic"></a><br><sub><a href="showcase/instruction-following.md#red-panda-infographic">Red panda infographic</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#staff-selection-puzzle"><img src="assets/showcase/tiles/staffing-logic-puzzle.jpg" alt="Staff-selection puzzle"></a><br><sub><a href="showcase/instruction-following.md#staff-selection-puzzle">Staff-selection puzzle</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#electric-motorcycle-exploded-view"><img src="assets/showcase/tiles/e-motorcycle-exploded.jpg" alt="Electric motorcycle, exploded view"></a><br><sub><a href="showcase/instruction-following.md#electric-motorcycle-exploded-view">Electric motorcycle, exploded view</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#jet-engine-exploded-view"><img src="assets/showcase/tiles/jet-engine-exploded.jpg" alt="Jet engine, exploded view"></a><br><sub><a href="showcase/instruction-following.md#jet-engine-exploded-view">Jet engine, exploded view</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#moka-pot-blueprint"><img src="assets/showcase/tiles/moka-pot-blueprint.jpg" alt="Moka pot blueprint"></a><br><sub><a href="showcase/instruction-following.md#moka-pot-blueprint">Moka pot blueprint</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#ant-inspired-hexapod-mech-line-art"><img src="assets/showcase/tiles/ant-hexapod-mech-lineart.jpg" alt="Ant-inspired hexapod mech, line art"></a><br><sub><a href="showcase/instruction-following.md#ant-inspired-hexapod-mech-line-art">Ant-inspired hexapod mech, line art</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#quadruped-mech-cad-drawing"><img src="assets/showcase/tiles/quadruped-mech-cad.jpg" alt="Quadruped mech, CAD drawing"></a><br><sub><a href="showcase/instruction-following.md#quadruped-mech-cad-drawing">Quadruped mech, CAD drawing</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#mech-beast-exploded-cad-view"><img src="assets/showcase/tiles/mech-monster-exploded-cad.jpg" alt="Mech beast, exploded CAD view"></a><br><sub><a href="showcase/instruction-following.md#mech-beast-exploded-cad-view">Mech beast, exploded CAD view</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#ceiling-rail-courier"><img src="assets/showcase/tiles/ceiling-rail-courier.jpg" alt="Ceiling rail courier"></a><br><sub><a href="showcase/instruction-following.md#ceiling-rail-courier">Ceiling rail courier</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/instruction-following.md#wheel-legged-delivery-robot"><img src="assets/showcase/tiles/wheel-leg-robot.jpg" alt="Wheel-legged delivery robot"></a><br><sub><a href="showcase/instruction-following.md#wheel-legged-delivery-robot">Wheel-legged delivery robot</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/visual-challenges.md#corner-mirrors"><img src="assets/showcase/tiles/mirror-reflection.jpg" alt="Corner mirrors"></a><br><sub><a href="showcase/visual-challenges.md#corner-mirrors">Corner mirrors</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/visual-challenges.md#a-hand-in-the-projection"><img src="assets/showcase/tiles/projection-hand-shadow.jpg" alt="A hand in the projection"></a><br><sub><a href="showcase/visual-challenges.md#a-hand-in-the-projection">A hand in the projection</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/visual-challenges.md#game-map-to-3d-game-view"><img src="assets/showcase/tiles/game-map-to-3d.jpg" alt="Game map to 3D game view"></a><br><sub><a href="showcase/visual-challenges.md#game-map-to-3d-game-view">Game map to 3D game view</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/visual-challenges.md#pelican-graduation-pyramid"><img src="assets/showcase/tiles/pelican-graduation-pyramid.jpg" alt="Pelican graduation pyramid"></a><br><sub><a href="showcase/visual-challenges.md#pelican-graduation-pyramid">Pelican graduation pyramid</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/visual-challenges.md#pelican-christmas-tree"><img src="assets/showcase/tiles/pelican-christmas-tree.jpg" alt="Pelican Christmas tree"></a><br><sub><a href="showcase/visual-challenges.md#pelican-christmas-tree">Pelican Christmas tree</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/visual-challenges.md#pelican-balancing-act"><img src="assets/showcase/tiles/pelican-challenge-3.jpg" alt="Pelican balancing act"></a><br><sub><a href="showcase/visual-challenges.md#pelican-balancing-act">Pelican balancing act</a></sub></td>
</tr>
<tr><th colspan="4" align="left">Creative Applications</th></tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#frontier-rider"><img src="assets/showcase/tiles/frontier-rider.jpg" alt="Frontier rider"></a><br><sub><a href="showcase/game-worlds.md#frontier-rider">Frontier rider</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#gathering-in-the-desert"><img src="assets/showcase/tiles/desert-gathering.jpg" alt="Gathering in the desert"></a><br><sub><a href="showcase/game-worlds.md#gathering-in-the-desert">Gathering in the desert</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#cold-mineral-plain-aerial-view"><img src="assets/showcase/tiles/cold-mineral-aerial.jpg" alt="Cold mineral plain, aerial view"></a><br><sub><a href="showcase/game-worlds.md#cold-mineral-plain-aerial-view">Cold mineral plain, aerial view</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#red-mineral-plain-aerial-view"><img src="assets/showcase/tiles/desert-mineral-aerial.jpg" alt="Red mineral plain, aerial view"></a><br><sub><a href="showcase/game-worlds.md#red-mineral-plain-aerial-view">Red mineral plain, aerial view</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#forest-amphitheater"><img src="assets/showcase/tiles/forest-amphitheater.jpg" alt="Forest amphitheater"></a><br><sub><a href="showcase/game-worlds.md#forest-amphitheater">Forest amphitheater</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#palace-above-a-sea-of-clouds"><img src="assets/showcase/tiles/mountain-temple.jpg" alt="Palace above a sea of clouds"></a><br><sub><a href="showcase/game-worlds.md#palace-above-a-sea-of-clouds">Palace above a sea of clouds</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#wizard-casting-a-fan-of-fire"><img src="assets/showcase/tiles/fire-mage-vfx.jpg" alt="Wizard casting a fan of fire"></a><br><sub><a href="showcase/game-worlds.md#wizard-casting-a-fan-of-fire">Wizard casting a fan of fire</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#explosion-in-two-stages"><img src="assets/showcase/tiles/explosion-two-state.jpg" alt="Explosion in two stages"></a><br><sub><a href="showcase/game-worlds.md#explosion-in-two-stages">Explosion in two stages</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#armored-knight-character-sheet"><img src="assets/showcase/tiles/armored-knight-sheet.jpg" alt="Armored knight, character sheet"></a><br><sub><a href="showcase/game-worlds.md#armored-knight-character-sheet">Armored knight, character sheet</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#beast-king-with-a-lions-mane-close-up"><img src="assets/showcase/tiles/lion-king-face.jpg" alt="Beast king with a lion&#x27;s mane, close-up"></a><br><sub><a href="showcase/game-worlds.md#beast-king-with-a-lions-mane-close-up">Beast king with a lion&#x27;s mane, close-up</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#forest-dragon"><img src="assets/showcase/tiles/forest-dragon.jpg" alt="Forest dragon"></a><br><sub><a href="showcase/game-worlds.md#forest-dragon">Forest dragon</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#first-person-shooter-scene"><img src="assets/showcase/tiles/fps-wasteland.jpg" alt="First-person shooter scene"></a><br><sub><a href="showcase/game-worlds.md#first-person-shooter-scene">First-person shooter scene</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#untextured-render-to-film-still"><img src="assets/showcase/tiles/moon-rover-render.jpg" alt="Untextured render to film still"></a><br><sub><a href="showcase/game-worlds.md#untextured-render-to-film-still">Untextured render to film still</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#hydro-station-in-a-canyon-matte-painting"><img src="assets/showcase/tiles/hydro-station-canyon.jpg" alt="Hydro station in a canyon, matte painting"></a><br><sub><a href="showcase/game-worlds.md#hydro-station-in-a-canyon-matte-painting">Hydro station in a canyon, matte painting</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#abandoned-station"><img src="assets/showcase/tiles/abandoned-station.jpg" alt="Abandoned station"></a><br><sub><a href="showcase/game-worlds.md#abandoned-station">Abandoned station</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#industrial-ruins"><img src="assets/showcase/tiles/industrial-ruins.jpg" alt="Industrial ruins"></a><br><sub><a href="showcase/game-worlds.md#industrial-ruins">Industrial ruins</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#shipwrecks-in-a-frozen-bay"><img src="assets/showcase/tiles/frozen-shipwreck-bay.jpg" alt="Shipwrecks in a frozen bay"></a><br><sub><a href="showcase/game-worlds.md#shipwrecks-in-a-frozen-bay">Shipwrecks in a frozen bay</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#combat-pilot"><img src="assets/showcase/tiles/combat-pilot.jpg" alt="Combat pilot"></a><br><sub><a href="showcase/game-worlds.md#combat-pilot">Combat pilot</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#polar-outfit-costume-board"><img src="assets/showcase/tiles/polar-costume-board.jpg" alt="Polar outfit, costume board"></a><br><sub><a href="showcase/game-worlds.md#polar-outfit-costume-board">Polar outfit, costume board</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#helmet-on-a-red-plain-key-art"><img src="assets/showcase/tiles/helmet-key-art.jpg" alt="Helmet on a red plain, key art"></a><br><sub><a href="showcase/game-worlds.md#helmet-on-a-red-plain-key-art">Helmet on a red plain, key art</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#sci-fi-fighter"><img src="assets/showcase/tiles/scifi-fighter.jpg" alt="Sci-fi fighter"></a><br><sub><a href="showcase/game-worlds.md#sci-fi-fighter">Sci-fi fighter</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/game-worlds.md#modified-muscle-car"><img src="assets/showcase/tiles/modded-muscle-car.jpg" alt="Modified muscle car"></a><br><sub><a href="showcase/game-worlds.md#modified-muscle-car">Modified muscle car</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#farm-in-the-fog-documentary-film-photo"><img src="assets/showcase/tiles/farm-documentary-film.jpg" alt="Farm in the fog, documentary film photo"></a><br><sub><a href="showcase/real-world.md#farm-in-the-fog-documentary-film-photo">Farm in the fog, documentary film photo</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#picnic-on-film"><img src="assets/showcase/tiles/picnic-film.jpg" alt="Picnic on film"></a><br><sub><a href="showcase/real-world.md#picnic-on-film">Picnic on film</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#close-up-portrait-on-film"><img src="assets/showcase/tiles/film-portrait-closeup.jpg" alt="Close-up portrait on film"></a><br><sub><a href="showcase/real-world.md#close-up-portrait-on-film">Close-up portrait on film</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#snapshot-from-an-old-phone"><img src="assets/showcase/tiles/iphone7-snapshot.jpg" alt="Snapshot from an old phone"></a><br><sub><a href="showcase/real-world.md#snapshot-from-an-old-phone">Snapshot from an old phone</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#flash-portrait-on-film"><img src="assets/showcase/tiles/flash-film-portrait.jpg" alt="Flash portrait on film"></a><br><sub><a href="showcase/real-world.md#flash-portrait-on-film">Flash portrait on film</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#grandmas-birthday-home-video"><img src="assets/showcase/tiles/grandma-birthday-dv.jpg" alt="Grandma&#x27;s birthday, home video"></a><br><sub><a href="showcase/real-world.md#grandmas-birthday-home-video">Grandma&#x27;s birthday, home video</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#rooftop-at-dusk"><img src="assets/showcase/tiles/rooftop-bedsheets.jpg" alt="Rooftop at dusk"></a><br><sub><a href="showcase/real-world.md#rooftop-at-dusk">Rooftop at dusk</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#a-pause-before-tea"><img src="assets/showcase/tiles/tea-portrait.jpg" alt="A pause before tea"></a><br><sub><a href="showcase/real-world.md#a-pause-before-tea">A pause before tea</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/real-world.md#flamingos-at-dawn"><img src="assets/showcase/tiles/flamingo-salt-lake.jpg" alt="Flamingos at dawn"></a><br><sub><a href="showcase/real-world.md#flamingos-at-dawn">Flamingos at dawn</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/surreal-worlds.md#a-cloud-in-a-barber-chair"><img src="assets/showcase/tiles/surreal-cloud-barber-chair.jpg" alt="A cloud in a barber chair"></a><br><sub><a href="showcase/surreal-worlds.md#a-cloud-in-a-barber-chair">A cloud in a barber chair</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/surreal-worlds.md#slicing-the-moon"><img src="assets/showcase/tiles/surreal-long-table.jpg" alt="Slicing the moon"></a><br><sub><a href="showcase/surreal-worlds.md#slicing-the-moon">Slicing the moon</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/surreal-worlds.md#a-pear-as-a-dressing-room"><img src="assets/showcase/tiles/surreal-pear-dressing-room.jpg" alt="A pear as a dressing room"></a><br><sub><a href="showcase/surreal-worlds.md#a-pear-as-a-dressing-room">A pear as a dressing room</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/surreal-worlds.md#cut-paper-collage"><img src="assets/showcase/tiles/blue-collage.jpg" alt="Cut-paper collage"></a><br><sub><a href="showcase/surreal-worlds.md#cut-paper-collage">Cut-paper collage</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/surreal-worlds.md#sticker-residue-type-poster"><img src="assets/showcase/tiles/sticker-type-poster.jpg" alt="Sticker-residue type poster"></a><br><sub><a href="showcase/surreal-worlds.md#sticker-residue-type-poster">Sticker-residue type poster</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/surreal-worlds.md#pixel-cat-poster"><img src="assets/showcase/tiles/pixel-white-cat.jpg" alt="Pixel cat poster"></a><br><sub><a href="showcase/surreal-worlds.md#pixel-cat-poster">Pixel cat poster</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#mandarin-ducks-old-master-oil-painting"><img src="assets/showcase/tiles/baroque-mandarin-ducks.jpg" alt="Mandarin ducks, Old Master oil painting"></a><br><sub><a href="showcase/artistic-worlds.md#mandarin-ducks-old-master-oil-painting">Mandarin ducks, Old Master oil painting</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#fishermen-and-a-pelican-caravaggio-style"><img src="assets/showcase/tiles/caravaggio-pelican.jpg" alt="Fishermen and a pelican, Caravaggio style"></a><br><sub><a href="showcase/artistic-worlds.md#fishermen-and-a-pelican-caravaggio-style">Fishermen and a pelican, Caravaggio style</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#table-tennis-caravaggio-style"><img src="assets/showcase/tiles/caravaggio-ping-pong.jpg" alt="Table tennis, Caravaggio style"></a><br><sub><a href="showcase/artistic-worlds.md#table-tennis-caravaggio-style">Table tennis, Caravaggio style</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#mandarin-ducks-in-a-suzhou-garden-impressionist-oil-painting"><img src="assets/showcase/tiles/impressionist-suzhou-garden.jpg" alt="Mandarin ducks in a Suzhou garden, Impressionist oil painting"></a><br><sub><a href="showcase/artistic-worlds.md#mandarin-ducks-in-a-suzhou-garden-impressionist-oil-painting">Mandarin ducks in a Suzhou garden, Impressionist oil painting</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#the-sun-illuminated-manuscript"><img src="assets/showcase/tiles/illuminated-manuscript-a.jpg" alt="The Sun, illuminated manuscript"></a><br><sub><a href="showcase/artistic-worlds.md#the-sun-illuminated-manuscript">The Sun, illuminated manuscript</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#the-jade-rabbit-illuminated-manuscript"><img src="assets/showcase/tiles/illuminated-manuscript-b.jpg" alt="The Jade Rabbit, illuminated manuscript"></a><br><sub><a href="showcase/artistic-worlds.md#the-jade-rabbit-illuminated-manuscript">The Jade Rabbit, illuminated manuscript</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#space-station-repair-dunhuang-mural"><img src="assets/showcase/tiles/dunhuang-space-station.jpg" alt="Space station repair, Dunhuang mural"></a><br><sub><a href="showcase/artistic-worlds.md#space-station-repair-dunhuang-mural">Space station repair, Dunhuang mural</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#pelican-shadow-puppet"><img src="assets/showcase/tiles/shadow-puppet-pelican.jpg" alt="Pelican shadow puppet"></a><br><sub><a href="showcase/artistic-worlds.md#pelican-shadow-puppet">Pelican shadow puppet</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#circuit-board-textile-gongbi"><img src="assets/showcase/tiles/gongbi-circuit-textile.jpg" alt="Circuit-board textile, gongbi"></a><br><sub><a href="showcase/artistic-worlds.md#circuit-board-textile-gongbi">Circuit-board textile, gongbi</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#pelican-at-a-mirror-gongbi-painting"><img src="assets/showcase/tiles/gongbi-pelican-mirror.jpg" alt="Pelican at a mirror, gongbi painting"></a><br><sub><a href="showcase/artistic-worlds.md#pelican-at-a-mirror-gongbi-painting">Pelican at a mirror, gongbi painting</a></sub></td>
<td align="center" valign="top" width="25%"><a href="showcase/artistic-worlds.md#golden-flames-eastern-fantasy-illustration"><img src="assets/showcase/tiles/eastern-fantasy-lineart.jpg" alt="Golden flames, Eastern fantasy illustration"></a><br><sub><a href="showcase/artistic-worlds.md#golden-flames-eastern-fantasy-illustration">Golden flames, Eastern fantasy illustration</a></sub></td>
</tr>
</table>

Select an image to see it larger with its prompt, or browse [by section](showcase/README.md).
<!-- END showcase-grid -->

## Use Online

| | Global | China |
| --- | --- | --- |
| Web app | [hailuoai.video](https://hailuoai.video/) | [hailuoai.com](https://hailuoai.com/) |
| Desktop app | [agent.minimax.io](https://agent.minimax.io/) | [agent.minimax.cn](https://agent.minimax.cn) |
| API platform | [platform.minimax.io](https://platform.minimax.io/docs/guides/image-generation) | [platform.minimax.cn](https://platform.minimax.cn/docs/guides/image-generation) |
| API reference | [Text-to-image](https://platform.minimax.io/docs/api-reference/image-generation-h3-generations) · [Image editing](https://platform.minimax.io/docs/api-reference/image-generation-h3-edits) · [Prompt expansion](https://platform.minimax.io/docs/api-reference/image-generation-h3-context-ir) | [Text-to-image](https://platform.minimax.cn/docs/api-reference/image-generation-h3-generations) · [Image editing](https://platform.minimax.cn/docs/api-reference/image-generation-h3-edits) · [Prompt expansion](https://platform.minimax.cn/docs/api-reference/image-generation-h3-context-ir) |

## Overview

MiniMax-H3-Image is a state-of-the-art open-source model for image generation and editing from the
[MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) family, with text-to-image and
multi-image editing in one checkpoint.

- **16 MP at a practical cost.** It generates images of about 16 MP at every aspect ratio directly,
  without an upscaler, in 6 sampling steps.
- **Rich detail, real-world realism.** Its images go beyond the familiar "AI look".
- **Strongest instruction following among open-source models.** It takes up to 16 reference images.

### Specifications

These are the specifications of the MiniMax API. A local server takes the fields in
[Request Parameters](#request-parameters).

| Parameter | Specification |
| --- | --- |
| Model ID | `MiniMax-H3-Image` |
| Tasks | Text-to-image, image editing |
| Image size | `width` + `height`, or `area` + `aspect_ratio`. Default `auto`: 4K area, automatic aspect ratio |
| Output area | `1K`, `2K` or **`4K` (best results 👍)**; a custom `width` × `height` covers 655,360 to 20,000,000 pixels |
| Aspect ratio | 1:3 to 3:1 |
| Prompt | Up to 32,000 characters; content beyond 4,096 tokens is truncated |
| Reference images | Up to 16, each at most 64 MiB, with sides of 128 to 8192 pixels and an aspect ratio from 1:4 to 4:1 |
| Reference formats | JPG, PNG, WebP, HEIC or HEIF, sent as an HTTP(S) URL, Base64 or MiniMax file ID |
| Images per request | 1 to 10 |
| Prompt expansion | On by default for text-to-image and can be turned off; always on for image editing; the expanded prompt can be returned |
| Output | PNG (default), JPEG or WebP, with `output_compression` from 0 to 100; returned as a URL (default) or Base64 |
| Not yet supported | Mask-based inpainting, transparent backgrounds, user-specified seeds, preview images |

### Model Zoo

| Model | Role | Precision | Size | Hugging Face |
| --- | --- | --- | --- | --- |
| **MiniMax-H3-Image** | Text-to-image and image editing | BF16 (DiT) | 68.65 GB | [MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) |
| **MiniMax-H3-Image-PE** (optional) | Prompt expander for text-to-image | NVFP4 | 17.9 GB | [MiniMaxAI/MiniMax-H3-Image-PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE) |

### Model Architecture

MiniMax-H3-Image follows the H3-Base design with the audio branch removed. The text prompt and the
reference images are encoded by the H3 text encoder; the reference images are also encoded by the
image VAE. All tokens form one packed sequence for a single-stream transformer, which predicts the
latent of the target image. The VAE decodes that latent into the image.

- **Text encoder**: the full Qwen3-VL text encoder of MiniMax-H3, unchanged. The DiT reads the
  hidden states of its 50th layer.
- **Image VAE**: a CNN encoder and a 2D ViT decoder (24 layers), with 16x spatial downsampling and
  24 latent channels. The DiT patchifies the latent with a 2x2 patch, so each transformer token
  covers 32x32 pixels.
- **Diffusion transformer**: 33.1B parameters, a dense single-stream transformer with 50 layers
  (hidden size 5376, 56 attention heads, FFN size 14336) and 3D multimodal RoPE, the same as the
  H3-Omni-Transformer. The weights are BF16; the embedding, timestep and output layers are FP32.

## Run Locally

### Download

| Component | Content | Size |
| --- | --- | --- |
| `transformer/` | DiT weights. | 66.28 GB |
| `pdd_fused_heads.safetensors`, `pdd_config.json` | The per-step output heads that replace the transformer's output layer, and the sampling schedule. | 12 MB |
| `vae/` | Image VAE, FP32. | 2.34 GB |
| `tokenizer/`, `processor/` | Qwen3-VL tokenizer and processor, identical to MiniMax-H3. | 23 MB |
| Text encoder | Not part of the original checkpoint. `model_index.json` loads it from [`MiniMaxAI/MiniMax-H3`](https://huggingface.co/MiniMaxAI/MiniMax-H3), folder `text_encoder/`. If you already have MiniMax-H3, it is not downloaded again. | 66.7 GB |

The Hugging Face repository holds this original checkpoint alongside the diffusers format, about
204 GB in total. SGLang and vLLM-Omni need only the original checkpoint and the MiniMax-H3 text
encoder, about 135 GB:

```bash
hf download MiniMaxAI/MiniMax-H3-Image model_index.json "pdd_*" "processor/*" "tokenizer/*" \
  "transformer/*" "vae/*"
hf download MiniMaxAI/MiniMax-H3 --include "text_encoder/*"
# optional prompt expander
hf download MiniMaxAI/MiniMax-H3-Image-PE
```

diffusers fetches its own files with `ModularPipeline.from_pretrained("MiniMaxAI/MiniMax-H3-Image")`.

### Deployment

We recommend the following inference frameworks to serve the model:

- [SGLang](https://docs.sglang.io/) - see [cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3-Image)
- [vLLM-Omni](https://github.com/vllm-project/vllm-omni) - see [vllm-omni recipe](https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3-Image)
- [diffusers](https://github.com/huggingface/diffusers) - see [diffusers docs](https://huggingface.co/docs/diffusers/main/en/api/pipelines/minimax_h3_image)
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) - see [Comfy tutorial](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image); use [T2I template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_t2i.json) / [Edit template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_edit.json)

#### SGLang

Install SGLang from the main branch with its diffusion dependencies
([installation guide](https://docs.sglang.io/docs/sglang-diffusion/installation)):

```bash
git clone https://github.com/sgl-project/sglang.git
cd sglang
python3 -m pip install -e 'python[diffusion]'
```

Serve on one GPU (SGLang offloads model components when less than 130 GiB is free), or split each
request over several GPUs with sequence parallelism (Ulysses) for lower latency:

```bash
sglang serve --model-path MiniMaxAI/MiniMax-H3-Image --host 0.0.0.0 --port 30000 --warmup-mode off
# 4 GPUs
sglang serve --model-path MiniMaxAI/MiniMax-H3-Image --host 0.0.0.0 --port 30000 --warmup-mode off \
  --num-gpus 4 --ulysses-degree 4
```

Add `--text-encoder-path <path to text_encoder>` to use a local copy of the MiniMax-H3 text encoder.
The [SGLang cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3-Image) has
recipes for other GPUs, from B300 down to 12 GB cards.

#### vLLM-Omni

Install vLLM 0.33.0, then vLLM-Omni from source:

```bash
uv venv --python 3.12 --seed && source .venv/bin/activate
uv pip install vllm==0.33.0 --torch-backend=cu130
git clone https://github.com/vllm-project/vllm-omni.git && cd vllm-omni && uv pip install -e .
```

Serve on 4 GPUs with sequence parallelism (Ulysses), or on one GPU: a B200 or B300 holds the whole
model in about 135 GiB, and one H200 offloads the text encoder:

```bash
vllm serve MiniMaxAI/MiniMax-H3-Image --omni --host 0.0.0.0 --port 8000 \
  --num-gpus 4 --usp 4 --text-encoder-tp-size 4
# one B200 or B300
vllm serve MiniMaxAI/MiniMax-H3-Image --omni --host 0.0.0.0 --port 8000 --num-gpus 1
# one H200: offload the text encoder
vllm serve MiniMaxAI/MiniMax-H3-Image --omni --host 0.0.0.0 --port 8000 --num-gpus 1 \
  --diffusion-offload-config '{"mode":"layer","components":["text_encoder"]}'
```

The [vLLM-Omni recipe](https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3-Image) covers AMD Instinct and
other GPUs.

### Request Parameters

SGLang takes text-to-image requests as JSON at `/v1/images/generations` and image editing requests
as multipart form data at `/v1/images/edits`; both return the PNG in `data[0].b64_json`. vLLM-Omni
takes slightly different fields; see its [recipe](https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3-Image).

| Field | Text-to-image | Image editing | Notes |
| --- | --- | --- | --- |
| `prompt` | Required | Required | Used as given, truncated to 4096 tokens |
| `size` | Required | Required | `WIDTHxHEIGHT`. The returned image has exactly this size; see [Sizes](#sizes) |
| `image` | — | One or more files | In upload order they are `<Picture 1>`, `<Picture 2>`, ... in the prompt |
| `seed` | Recommended | Recommended | Integer |
| `generator_device` | `cpu` recommended | `cpu` recommended | Same seed, same initial noise on every machine |
| `response_format` | `b64_json` | `b64_json` | |
| `min_generation_area` | Optional | Optional | Minimum generated area in pixels, 1024-16777216, default 4194304 (2048x2048). A smaller `size` is generated at the same aspect ratio on a larger canvas and resized back with LANCZOS; pass 1024 to turn this off. All sizes in the table below are above the default |
| `num_inference_steps` | Omit or 6 | Omit or 6 | Other values return HTTP 400 |
| `guidance_scale` | Omit or 1 | Omit or 1 | Other values return HTTP 400 |
| `negative_prompt` | Not supported | Not supported | Rejected |

### Sizes

The model works at about 4 MP to 20 MP and generally gives the best results at about 16 MP. Common
16 MP sizes:

| Aspect ratio | Size (width x height) |
| --- | --- |
| 1:1 | 4096x4096 |
| 4:3 / 3:4 | 4736x3552 / 3552x4736 |
| 3:2 / 2:3 | 5024x3360 / 3360x5024 |
| 16:9 / 9:16 | 5472x3072 / 3072x5472 |
| 21:9 | 6272x2688 |

For another aspect ratio, keep about 16 MP with both sides a multiple of 32. `size_for()` in
[`examples/context_ir.py`](examples/context_ir.py) computes it:

```bash
cd MiniMax-H3-Image/examples
python3 -c "from context_ir import size_for; print(size_for('5:4'))"   # 4576x3648
```

### Full Workflow

The MiniMax API expands a short prompt in any language into a detailed English description of the
whole image with **H3-Image-Context-IR** before generating. A local server uses the prompt as
given, so expand it first, as in the cases below. The scripts in [`examples/`](examples) reproduce
the API results with the SGLang server above, using only the Python standard library:

```bash
git clone https://github.com/MiniMax-AI/MiniMax-H3-Image.git
cd MiniMax-H3-Image/examples
export MINIMAX_API_BASE="https://api.minimax.io"   # China: https://api.minimax.cn
export MINIMAX_API_KEY="<api-key>"
```

`t2i.py` and `edit.py` send requests to `http://127.0.0.1:30000`; pass `--url` to use another
address.

#### case-T2I

[`instruction.t2i.txt`](examples/instruction.t2i.txt).

<table>
<thead>
<tr><th colspan="2">Stage</th><th>Request</th><th>Result</th></tr>
</thead>
<tbody>
<tr><td rowspan="3">Prompt Enhancement</td><td>H3-Image-Context-IR (MiniMax API)</td><td><code>python3 context_ir.py t2i</code> (<a href="examples/context_ir.py">script</a>)</td><td><code>revised_prompt.txt</code>, <code>revised_size.txt</code>; our run: <a href="examples/revised_prompt.t2i.txt"><code>revised_prompt.t2i.txt</code></a>, <a href="examples/revised_size.t2i.txt"><code>revised_size.t2i.txt</code></a> (4736x3552)</td></tr>
<tr><td>local alternative: <a href="https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE">MiniMax-H3-Image-PE</a></td><td><code>scripts/expand_prompt.py</code> in the PE repository</td><td>Save <code>expanded_caption</code> as <code>revised_prompt.txt</code> and the size for <code>aspect_ratio</code> as <code>revised_size.txt</code></td></tr>
<tr><td>agent alternative: <a href="#prompt-writing-skill">h3-image-prompt-writing</a></td><td>Ask your agent to write a prompt and an aspect ratio for <code>instruction.t2i.txt</code> with the skill</td><td>Save the prompt as <code>revised_prompt.txt</code> and the <a href="#sizes">size</a> for that aspect ratio as <code>revised_size.txt</code></td></tr>
<tr><td colspan="2">MiniMax-H3-Image generation: local SGLang</td><td><code>python3 t2i.py --prompt revised_prompt.txt --size $(cat revised_size.txt)</code> (<a href="examples/t2i.py">script</a>)</td><td><code>t2i.png</code></td></tr>
<tr><td colspan="2">E2E API Reference: text-to-image by directly calling the MiniMax API</td><td><code>python3 api_generate.py t2i</code> (<a href="examples/api_generate.py">script</a>)</td><td><code>api_t2i.png</code></td></tr>
</tbody>
</table>

<p align="center">
<img src="assets/workflow_t2i.jpg" alt="Left: t2i.png from local SGLang with the enhanced prompt. Right: api_t2i.png from the MiniMax API. Both show an overhead farm-to-table feast with bread, vegetables and cheeses on a weathered wooden table" width="100%"/>
</p>
<p align="center"><em>t2i.png from local SGLang (left) and api_t2i.png from the MiniMax API (right), 4736x3552 (4:3 picked by H3-Image-Context-IR)</em></p>

#### case-Edit

[`instruction.edit.txt`](examples/instruction.edit.txt) with the reference image
[`reference1.png`](examples/reference1.png) as `<Picture 1>`.

| Stage | Request | Result |
| --- | --- | --- |
| Prompt Enhancement: H3-Image-Context-IR (MiniMax API) | `python3 context_ir.py edit` ([script](examples/context_ir.py)) | `revised_prompt.txt`, `revised_size.txt`; our run: [`revised_prompt.edit.txt`](examples/revised_prompt.edit.txt), [`revised_size.edit.txt`](examples/revised_size.edit.txt) (4096x4096) |
| Prompt Enhancement, agent alternative: [h3-image-prompt-writing](#prompt-writing-skill) | Ask your agent to rewrite `instruction.edit.txt` for `reference1.png` with the skill | Save the prompt as `revised_prompt.txt` and `4096x4096` as `revised_size.txt` |
| MiniMax-H3-Image generation: local SGLang | `python3 edit.py --prompt revised_prompt.txt --size $(cat revised_size.txt)` ([script](examples/edit.py)) | `edit.png` |
| E2E API Reference: image editing by directly calling the MiniMax API | `python3 api_generate.py edit` ([script](examples/api_generate.py)) | `api_edit.png` |

<p align="center">
<img src="assets/workflow_edit.jpg" alt="Left: reference1.png, the reference image of two podcast hosts with the man wearing headphones. Middle: edit.png from local SGLang with the enhanced prompt. Right: api_edit.png from the MiniMax API. In both results the headphones are gone and the hosts bump fists above the MONEY TALKS sign" width="100%"/>
</p>
<p align="center"><em>Reference image reference1.png (left), edit.png from local SGLang (middle) and api_edit.png from the MiniMax API (right), 4096x4096 (1:1 picked by H3-Image-Context-IR)</em></p>

## Prompting Tips

These tips from the official user guide apply to the MiniMax API and to a local server alike; the
[Prompt Writing Skill](#prompt-writing-skill) follows them for you.

- **Task before style, layout before details.** Say what the image is for and what is in it, then
  the layout, then the style through visible color, material and light instead of words like
  "premium".
- **Quote every word to show**, with its position and line breaks. Write "no text, letters or
  numbers in the image" when you want none.
- **Give exact data** for charts and educational images, with units and time ranges, and mark
  example data as such.
- **Give each reference image a role**, and say what changes and what stays: "Change the cup on the
  left to blue, keeping its shape, material, position and size."
- **Write grids as rows and columns**, such as "2 rows and 3 columns", not "2×3".

## License

- MiniMax-H3-Image is released under the [MiniMax-H3-Image Community License Agreement](LICENSE).
- The T2I PE Model ([MiniMax-H3-Image-PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE)) is part of MiniMax-H3-Image and is accordingly subject to [MiniMax-H3-Image Community License Agreement](LICENSE).
- The separate written authorization described in Section IV of the license is requested through [Application form](https://platform.minimax.io/console/license)

## Contact Us

Contact us at [model@minimax.io](mailto:model@minimax.io).
