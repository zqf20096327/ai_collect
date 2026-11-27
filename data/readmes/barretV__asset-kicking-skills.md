<p align="center"><img src="docs/showcase/hero.webp" alt="Painted game UI, a painted boss concept, a concept turned into a rigged 3D model, a pixel sprite and a painted chest icon" width="100%"></p>

<h3 align="center">Local AI game art, 3D models, animation and sound effects, on the GPU you already have.</h3>

<p align="center">
Concept art · painted game UI and icons · real pixel art · image to 3D · auto-rigging and animation · sound effects<br>
Everything runs on your machine. Built and tested on a <b>6 GB laptop GPU</b>. Commercial-use-friendly models only.
</p>

<p align="center"><b>Setup is one sentence to your coding agent:</b></p>

> Set up https://github.com/barretV/asset-kicking-skills on this machine. Follow its AGENTS.md.

Claude Code, Codex, Cursor or any agent that can run commands will check your hardware, show you every file it wants to download (with size and licence) and wait for your OK, then install everything, tune it to your GPU, test it and teach itself the skills. After that you just ask for art.

Every picture on this page came out of these tools on a 6 GB RTX 3060 laptop, for a game in development.

---

## 🎨 2D art and concept art

Not just pixel art: full painted illustration. Characters, creatures, props, key art, card art, portraits, items. The **forge loop** generates candidates, your agent **grades every one against a score bar** (default 9.5/10), writes the one fix that would raise the best one, and repeats until each piece passes. You get the best version, never a random roll.

<p align="center"><img src="docs/showcase/illustration_process.webp" alt="Rough Blender block-outs of a queen bee boss turned into painted concept art" width="100%"></p>

The trick that makes it controllable: **start from something rough** (a Blender block-out, a screenshot, a 10-second sketch, a box mock-up) and the loop keeps your silhouette and layout while painting everything else. Starting from nothing works too.

<p align="center"><img src="docs/showcase/turnaround.webp" alt="The same boss painted from side, three-quarter, front and back" width="100%"></p>

**Ask your agent:**
- *"Use art-forge-loop in illustration mode to paint a concept of a moss golem boss, side and 3/4 views, bar 9.0."*
- *"Here's a screenshot of my blocky Blender model. Paint it as a polished stylised creature, keep the pose."*
- *"Make 12 item icons in the same style as these two, one at a time, until each scores 9.5."*
- *"Fix only the hands in this image"* (draw a mask over the bad spot; only that area is repainted).
- *"Start the forge dashboard so I can watch the run."*

About a minute per 1024 px image on 6 GB, two seeds per round, two to four rounds per piece. Runs unattended. SVG export included.

**Watch it live, and call it yourself.** A zero-install dashboard shows what's generating, the queue, every candidate with its score, and a contact sheet per job against the bar. Happy with one before it reaches the bar? Hover it and click **✓ good enough**: that piece is done, and the loop stops spending rounds on it.

<p align="center"><img src="docs/showcase/forge_dashboard.webp" alt="The Art Forge dashboard: a contact sheet of a queen bee boss in four views, each candidate scored against a 9.0 bar, one target approved by the owner with a good-enough button" width="100%"></p>

---

## 🖼️ Painted game UI

Menus and HUDs drawn with CSS or vector shapes look generic. These screens are built from **painted parts with live text on top**: every frame, ribbon, medallion and icon came out of the forge loop, and every word is real text, so it stays sharp, translates and reuses the same art everywhere.

<p align="center"><img src="examples/ui/reward_card_pick.webp" alt="In-game reward card pick screen with three painted cards" width="49%"> <img src="examples/ui/hive_perk_comb_menu.webp" alt="In-game perk tree menu with painted honeycomb frame" width="49%"></p>

<p align="center"><img src="docs/showcase/ui_kit.webp" alt="The painted UI kit: card frame, panel, ribbon, medallion, wax seal, sword, chest and flame" width="100%"></p>

**Ask your agent:**
- *"Read art-forge-loop's UI.md, then make a UI kit for my game: card frame, panel, ribbon, button, medallion. Dark iron and glowing runes."*
- *"Rebuild my main menu with that kit, live text on the plates, and run a layout check until nothing overlaps or clips."*

The recipe (rules, job settings, prompt, export and the layout checks) is in [skills/art-forge-loop/UI.md](skills/art-forge-loop/UI.md).

---

## 👾 Real pixel art

Not "a blurry image shrunk down". A pixel-art LoRA draws on a true **8×8 grid**, so a 512 px image *is* a 64 px sprite; a snap step cuts the background and locks it to the grid. Then your agent can draw, read and patch sprites cell by cell in Aseprite, animate them and export sprite sheets with a JSON manifest for any engine.

<p align="center"><img src="docs/showcase/pixel.webp" alt="Five pixel-art axolotl knights from one prompt, five seeds" width="100%"></p>

**Ask your agent:**
- *"Make a 64×64 pixel sprite of a frog wizard, 4 seeds, pick the best."*
- *"Upgrade this old sprite: same design, cleaner pixels"* (img2img keeps the silhouette).
- *"Animate a 6-frame idle and export a sprite sheet for Godot."*

~35 s per sprite on 6 GB. Comes with 60+ pixel-art craft rule modules (shading, outlines, animation timing, palettes) your agent reads before drawing.

---

## 🧊 Concept → 3D model → rigged and animated

Paint a concept, turn it into a 3D sculpt with **TRELLIS.2** (and optionally **Hi3D** for detail), then either measure your hand-built model against it or clean the sculpt into a game mesh. Rig it with **SkinTokens** (a learned auto-rigger, so no melting armpits), animate it in Blender, and **verify** the clips with measurements: loop seams, left/right symmetry, feet through the floor.

<p align="center"><img src="docs/showcase/concept_to_3d.webp" alt="A creature concept, its Hi3D sculpt, the finished rigged game model, and a frame of its attack animation" width="100%"></p>

**Why the finished badger looks so detailed:** it is a hybrid. The body *is* the Hi3D sculpt: its fur clumps, muscle masses and stance came straight from the 1024³ refine, then were cleaned, decimated to a game budget (~28k faces), colour-zoned from the concept and given smoothed toon shading normals. Generated sculpts go mushy in small parts, so the parts that carry the read (head and snarl, the stone back plates, claws, crystals) were rebuilt as clean geometry on top. Hi3D supplies the mass and detail, Blender supplies the crisp read. That version scored 9.0 against its concept; the earlier procedural build that only used the sculpt as a measuring stick scored 8.6, and the cleaned sculpt on its own 8.2. The full recipe is step 3b of [concept-to-3d](skills/concept-to-3d/SKILL.md).

**Ask your agent:**
- *"Use concept-to-3d to turn this side-view concept into a 3D sculpt."*
- *"Compare my Blender model to the sculpt and tell me which proportions are off."*
- *"Use blender-anim to rig this GLB with SkinTokens, add idle and walk clips, and verify them."*
- *"I resculpted my character. Move the old animations onto the new body."*

On 6 GB: TRELLIS.2 ~3.5 min, Hi3D refine ~10 min, rigging ~70 s. Measuring, cleanup and animation run on the CPU in Blender. Exports GLB for three.js, Godot, Unity or Unreal.

---

## 🔊 Sound effects

Two engines, one finishing pass. **Procedural** retro sounds with no GPU at all (coins, lasers, jumps, hits, explosions, power-ups). **AI sound design** with Stable Audio 3 Small-SFX for the things a synth can't fake: sword clangs, shattering crystal, monster roars, bee swarms, grinding stone doors, footsteps on gravel. Type what you want to hear; on a 6 GB laptop GPU each take is ready in **2 to 3 seconds** (under 2 GB of VRAM), so your agent makes several takes of every sound and keeps the best. Then one script makes everything game-ready: mono, trimmed, faded, loudness-matched, with a manifest of the prompt and seed behind each file.

https://github.com/user-attachments/assets/142760bb-eb5f-4118-8f24-e7294472cd4d

<p align="center"><img src="docs/showcase/sound.webp" alt="Waveforms: coin, laser, explosion and power-up from the synth; sword hit, crystal shatter, monster roar and stone door from Stable Audio 3" width="100%"></p>

**Listen** (each opens a player on GitHub):
- AI: [sword hit](examples/sound/ai/sword_hit.ogg) · [fireball](examples/sound/ai/fireball.ogg) · [spell charge](examples/sound/ai/spell_charge.ogg) · [crystal shatter](examples/sound/ai/crystal_shatter.ogg) · [monster roar](examples/sound/ai/monster_roar.ogg) · [bee swarm](examples/sound/ai/swarm_buzz.ogg) · [stone door](examples/sound/ai/stone_door.ogg) · [footsteps](examples/sound/ai/footsteps_gravel.ogg) · [explosion](examples/sound/ai/explosion.ogg)
- Procedural: [coin](examples/sound/coin_01.ogg) · [laser](examples/sound/laser_01.ogg) · [explosion](examples/sound/explosion_01.ogg) · [power-up](examples/sound/powerup_01.ogg)

**Ask your agent:**
- *"Use game-sfx with Stable Audio to make a heavy stone door grinding open, 4 takes, finish the best two as ogg."*
- *"Make hit sounds for my three enemy types: a beetle shell crunch, a slime squelch, a metal golem clang."*
- *"Make 6 coin pickups and 4 UI blips with the synth."* (bright UI tones are the synth's job)
- *"Layer a recorded door slam with a short noise burst and level the whole folder."*

AI sounds are Stable Audio 3 Small-SFX, **Powered by Stability AI**: free for commercial use under USD 1M annual revenue (see [Licences](#licences-in-plain-words)).

---

## How it works

```
your agent ── reads AGENTS.md
  1. checks your PC        GPU + VRAM, RAM, disk, Python, Blender      (changes nothing)
  2. picks a tier          6 GB (tested) · 8 · 12 · 24 GB+ · CPU-only
  3. shows the shopping list   every file, source, size, licence  → waits for your yes
  4. installs              ComfyUI, custom nodes, Blender/FFmpeg if missing, weights from official sources
  5. tunes + tests         launch scripts for your tier, one test image
  6. learns the skills     copies them where your agent loads them
```

Want to see what you'd get first, without installing anything?

```bash
python setup/detect.py --dry-run
```

```
GPU       NVIDIA GeForce RTX 3060 Laptop GPU, 6.0 GB VRAM
RAM       15.7 GB
Blender   5.3.0
TIER: 6gb  -  6 GB VRAM (tested baseline, e.g. RTX 3060 Laptop)
  models    about 21 GB for the default set, 31 GB with every optional bundle
```

## Hardware

| Tier | GPU | What changes | Status |
|---|---|---|---|
| `cpu` | no NVIDIA GPU | pixel-art editing, Blender animation, sound only | works |
| `6gb` | 6 GB NVIDIA (RTX 3060 Laptop, RTX 2060...) | the baseline everything was built on | **tested** |
| `8gb` | 8 GB | bigger sprites, batch 2, Hi3D 1536 | extrapolated |
| `12gb` | 12 GB | batch 4, fp16 Hi3D, models stay loaded | extrapolated |
| `24gb` | 24 GB+ | full precision, batch 8 | extrapolated |

16 GB RAM and ~40 GB free disk recommended. Windows is tested; Linux should work; macOS is CPU-only for now. Details: [TIERS.md](TIERS.md).

**One GPU job at a time.** Small GPUs can hang or reboot when jobs pile up, so the skills wait their turn.

## Licences, in plain words

- **This repo:** MIT.
- **Every default model allows commercial use.** A few have conditions: Hi3D asks for credit only if you build Hi3D itself into a product (shipping meshes is fine); Stable Audio is free under USD 1M revenue (register with Stability, credit "Powered by Stability AI").
- **Left out on purpose:** non-commercial or region-locked models (Hunyuan3D, FLUX.1-dev, Qwen Image, several audio models).
- No model weights are stored here; they download from the official source on your machine, after you approve them.

Full table: [LICENSES.md](LICENSES.md). Not legal advice.

## The skills

| Skill | For | Docs |
|---|---|---|
| `art-forge-loop` | 2D illustration, concept art, UI parts, icons, pixel sources: generate → grade → refine | [SKILL.md](skills/art-forge-loop/SKILL.md) · [UI.md](skills/art-forge-loop/UI.md) |
| `pixel-art` | 8:1 pixel sprites, Aseprite grid editing, animation, sprite sheets | [SKILL.md](skills/pixel-art/SKILL.md) |
| `concept-to-3d` | TRELLIS.2 + Hi3D sculpts, measuring, sculpt cleanup | [SKILL.md](skills/concept-to-3d/SKILL.md) |
| `blender-anim` | SkinTokens rigging, clips, retargeting, verification, GLB | [SKILL.md](skills/blender-anim/SKILL.md) |
| `game-sfx` | procedural SFX, CC0 workflow, Stable Audio drafts, finishing | [SKILL.md](skills/game-sfx/SKILL.md) |

Agents: start at [AGENTS.md](AGENTS.md). Doing it by hand: the same file, step by step.

## Credits

Standing on ComfyUI, MOSS-Image and the moss-pixelart LoRA, TRELLIS.2, Hi3D and the Aero-Ex ComfyUI nodes, SkinTokens, Stable Audio 3 (Powered by Stability AI), Blender, Aseprite and aseprite-mcp, the Pebbly pixel-art rules, and FFmpeg. Thank you.
