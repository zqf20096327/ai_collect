# smoothstone

![Twelve parts built by stone from its recipes, rendered in Blender](docs/gallery.jpg)

I wanted a small model running on my own computer to make 3D printable parts that actually look good, so I tested LFM3-1.7B writing OpenSCAD on its own and it failed every single time. Even with the best skill I could write it made a working fan guard only 2 times out of 5. smoothstone takes the hard part away from the small model, as the model never writes geometry at all. It picks a tested recipe and fills in the sizes from the request or a picture, and the stone tool builds the part, checks that it will print and keeps every step on disk, so the model can lose its whole context and still finish the part.

## Results

![Six parts LFM3-1.7B made with smoothstone on my CPU, rendered in Blender](docs/made_by_lfm3.jpg)

LFM3-1.7B made every part above on my own CPU through smoothstone, and each one passed every print check. I did not want to fool myself with requests I had tuned for, so a fresh agent that never saw the code wrote new requests from the parameter list alone and I sealed them before the run. Each request ran five times. On the last blind set the model finished the right part with the right sizes 39 out of 40 times, and 38 out of 40 when I wiped its memory in the middle of the job. Writing the 3D code itself it went 0 out of 15. Every set, every failed run and every fix is in [LOG.md](LOG.md), and the sets are in [evals](evals).

## How it works

Every stone message ends with one line that says what to run next, and `stone status` prints that line again along with the request, the recipe, the sizes so far and the last build. A model that forgets everything runs `stone status` and keeps going.

```
$ stone new "A guard for a 120 mm PC fan, 3 mm thick."
NEXT: stone recipes
$ stone recipes
fan_guard  Fan guard  (default size 120 x 120 x 3 mm)
NEXT: stone show fan_guard
$ stone show fan_guard
From the request: size=120 thickness=3
NEXT: stone set fan_guard size=120 thickness=3
$ stone set fan_guard size=120 thickness=3
Expected size 120 x 120 x 3 mm.
NEXT: stone build
$ stone build
Size: 120.0 x 120.0 x 3.0 mm
PASS watertight: closed surface
PASS bodies: 1 bodies (max 1)
PASS first_layer: 6344.7 mm2 on the bed (need 200.0 mm2)
PASS min_wall: thinnest wall 1.98 mm (need 0.8 mm)
PASS overhang: 0.0% of the surface hangs past 45 deg (max 5%)
PASS dims: size matches the recipe
Part ready: stone-job/fan_guard.stl
NEXT: none, the part is ready
```

That is shortened: each command prints a few more lines, and the build prints every check.

The build runs OpenSCAD with the Manifold backend and then checks the mesh: watertight, one piece, flat on the bed, a real first layer, walls thick enough to print, no overhang past 45 degrees and the size the recipe promised. When a check fails, stone names the one setting to change and prints the command that changes it.

## Tiers

The skill gives each model a card that fits it.

| Tier | Models | What the model does |
| --- | --- | --- |
| S | about 3B and under | picks a recipe and sets its numbers, nothing else |
| M | about 4B to 30B | also picks the look: style, pattern, rounding, text |
| L | frontier models | writes new recipes in OpenSCAD with BOSL2 and the stone library |

Set it with `STONE_TIER=S` or `tier = "S"` in `stone.toml`. `stone status` prints the card's rules every time, so they come back after a compaction too.

## Pictures

```
stone new "A keychain of my dog" --image dog.png
```

stone traces the outline for keychains, cookie cutters and signs, and makes a height map for lithophanes and reliefs. The model never has to look at the picture to use it.

## Recipes

fan_guard, panel, cable_comb, vase, planter, gridfinity_bin, phone_stand, hook, spur_gear, box, keychain, cookie_cutter, sign, lithophane and relief. Every recipe prints without supports and every default and example is built and checked in CI.

## Install

You need uv, OpenSCAD 2026 or newer (a nightly build has the Manifold backend) and potrace for pictures.

```
git clone https://github.com/baney75/smoothstone
cd smoothstone
uv tool install -e .
stone status
```

stone finds OpenSCAD through `STONE_OPENSCAD`, then `openscad` on your PATH, then `vendor/openscad/AppRun`.

## Use it with your agent

The skill is the `skill` folder. Link it where your agent looks for skills:

```
ln -s "$PWD/skill" ~/.claude/skills/smoothstone      # Claude Code
ln -s "$PWD/skill" ~/.codex/skills/smoothstone       # Codex
ln -s "$PWD/skill" ~/.pi/agent/skills/smoothstone    # pi
```

For a local model on llama.cpp, give it one tool named `stone` that runs a stone command line, and put `skill/tiers/S.md` in the system prompt. `evals/run.py` does exactly this against `llama-server` and is the harness behind the numbers above.

## Make a new recipe

A recipe is a folder in `recipes` with `recipe.scad` and `recipe.json`. The json lists every setting with its range and unit, the size the part should come out at and examples. `uv run python tools/sheet.py <name>` builds the defaults and every example through stone and shows the previews. The L card has the full format.

## License

MIT. BOSL2 in `vendor/BOSL2` is BSD 2-Clause. The cat, rabbit and tree pictures in `examples/images` are Material Design Icons under Apache 2.0.
