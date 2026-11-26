# smoothstone

![Twelve parts built by stone from its recipes, rendered in Blender](docs/gallery.jpg)

I wanted a small model running on my own computer to make 3D printable parts that actually look good, so I tested LFM3-1.7B writing OpenSCAD on its own and it failed every single time. Even with the best skill I could write it made a working fan guard only 2 times out of 5. smoothstone takes the hard part away from the small model, as the model never writes geometry at all. It picks a tested recipe and fills in the sizes from the request or a picture, and the stone tool builds the part, checks that it will print and keeps every step on disk, so the model can lose its whole context and still finish the part.

## Results

![Six parts LFM3-1.7B made with smoothstone on my CPU, rendered in Blender](docs/made_by_lfm3.jpg)

LFM3-1.7B made every part above on my own CPU through smoothstone, and each one passed every print check. I did not want to fool myself with requests I had tuned for, so a fresh agent that never saw the code wrote new requests from the parameter list alone and I sealed them before the run. Each request ran five times. On the last blind set the model finished the right part with the right sizes 39 out of 40 times, and 38 out of 40 when I wiped its memory in the middle of the job. Writing the 3D code itself it went 0 out of 15. Every set, every failed run and every fix is in [LOG.md](LOG.md), and the sets are in [evals](evals).

## Try it

```
stone go "A mini figure of Sam Altman, 90 mm tall, with \"SAM\" on the base"
```

One command runs the whole job: it follows stone's own NEXT lines, shows each step as it runs (a figure prints each long step as it starts), and ends with the STL and the views opened. When a step needs you, such as the size of the hole a cover must fit, it stops with a "Needs you:" line; do that and run `stone go` again. The request alone works too: `stone "A guard for a 120 mm PC fan"`.

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
PASS slicer: no non-manifold edges or zero-area faces
PASS bodies: 1 bodies (max 1)
PASS first_layer: 6344.7 mm2 on the bed (need 200.0 mm2)
PASS min_wall: thinnest wall 1.98 mm (need 0.8 mm)
PASS overhang: 0.0% of the surface hangs past 45 deg (max 5%)
PASS dims: size matches the recipe
Part ready: stone-job/fan_guard.stl
NEXT: none, the part is ready
```

That is shortened: each command prints a few more lines, and the build prints every check.

The build runs OpenSCAD with the Manifold backend and then checks the STL it ships, read the way a slicer reads it: watertight, no non-manifold edges or zero-area faces (the mesh is rebuilt through manifold3d at float32 first), one piece, flat on the bed, a real first layer, walls thick enough to print, no overhang past 45 degrees and the size the recipe promised. When a check fails, stone names the one setting to change and prints the command that changes it.

Every passing build also writes `build/views.png`: the part from eight sides, from straight above and from straight below. Look at every panel, because a phone holder or a bracket that is right from the front and wrong on one side still fails.

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

If the photo has a ruler, a bank card or a US quarter next to the thing, `stone measure photo.jpg` works out its real size in millimeters and the recipe takes that size, and the traced outline leaves the ruler out.

## Figures

```
stone new 'A mini figure of Jensen Huang, 90 mm tall, with "JENSEN" on the base'
```

I wanted the small model to make something cooler than a bin, so smoothstone can now make a mini figure of a person, a pet or a thing. When there is no photo, stone set tells the model to run `stone find "Jensen Huang"`, which downloads free licensed photos from Wikimedia Commons and writes who took each one and its license to credits.txt. You can give it your own photo with `stone image` instead. Then three small models run one at a time on the Mac: LFM3-VL-2B writes one sentence about how the person looks, FLUX.2 klein 4B turns the photo and that sentence into a clean render of a figure, and Hunyuan3D-2mini lifts the render into a mesh. stone closes the mesh, stands it on a plinth with the name on the front and runs the same print checks as every other part.

| Step | Model | Peak memory | Time on my Mac |
| --- | --- | --- | --- |
| drive stone | LFM3-1.7B, 4 bit, on the CPU | 1.2 GB | |
| describe | LFM3-VL-2B, 4 bit | 3.0 GB | under a minute |
| style | FLUX.2 klein 4B, 4 bit | 7.8 GB | about 2 minutes |
| lift | Hunyuan3D-2mini | 9.0 GB | about 4 minutes |

The sentence from the vision model matters more than I expected, as without it the render got the hair color and the glasses wrong on every try. Run `tools/figure/setup.sh` once on an Apple silicon Mac with 16 GB of memory. Hunyuan3D-2mini is under the Tencent Hunyuan Community License, which does not cover the EU, the UK or South Korea, so read it before you use the meshes there. Photos keep their own licenses, so credit them from credits.txt when you post a print.

## Colors

A figure printed in one color looks unfinished, so after a passing build of a figure `stone colors` splits it into regions by the colors of its style picture, lists them with a part name each (base, shoes, pants, jacket or top, hands, face, hair, glasses, other, in the words of the request) and draws them numbered in `build/regions.png`. Then one line gives each part a filament, by name or number (`jacket=black rest=white`), and stone writes a 3MF next to the STL with every triangle painted. Orca, Bambu Studio and Creality Print open it with the paint, and PrusaSlicer reads Bambu paint too. stone cuts each color edge as a smooth curve through the triangles, then reads the file back before it says so: watertight, clean for a slicer, the same volume as the STL. The color_edges check compares each edge's length with the same edge smoothed over 2 mm and fails one that is over 8% longer, because that edge zigzags; then no file is written. A color edge within 3 mm of the hem, the neck or a wrist moves onto that line of the shape, and where the sculpt has a groove there (a collar, a cuff) the edge follows the groove instead of a flat cut, on the side a viewer sees least (measured by ray casting from 48 directions). The ledges check then fails any edge with up-facing faces of the wrong color seen beside it, like a white strip along the top of a collar. Edges in a groove are exempt from the wobble limit, since a sculpted collar is not straight. `build/boundaries.png` shows every color edge close up from eight sides, and the collar from level and from 30 degrees up. Put your printer's filament slots in `stone.toml` as `[filaments]` with `1 = "white"`, `2 = "black"` and so on, in the job folder or once in `~/.config/smoothstone/stone.toml`. When a figure's request names colors, the build's NEXT line is `stone colors` and its suggestion follows those colors; any other part prints in one color, and the build names the filament to load.

```
$ stone colors
Color regions of figure.stl, largest first:
1  white   48% of surface  base
2  skin    17% of surface  face
3  white   14% of surface  hair
4  black   13% of surface  jacket
5  black   5% of surface  pants
6  black   2% of surface  glasses
7  skin    1% of surface  hands
8  skin    1% of surface  hands
Filaments: 1 red, 2 white, 3 blue, 4 black (stone.toml [filaments])
Give each part or region a color, by name or filament number (like jacket=black); rest= colors the others.
NEXT: stone colors jacket=black pants=black glasses=black rest=white
$ stone colors jacket=black rest=white
filament 2 white: 87% of surface; filament 4 black: 13%
Checked: the 3MF reads back watertight and clean for a slicer, 122138 faces, volume as the STL.
PASS color_edges: every color boundary is a smooth curve (worst 1.027, max 1.08; wobble 0.01 mm, max 0.15; 3 edges run in a sculpted groove, which the wobble limit does not apply to)
PASS ledges: no up-facing face of the wrong color is seen next to a part's edge; edges in the groove: neck up, wrist left down, wrist right down
Warning: the colors alternate on 50 layers: about 52 filament changes and 34 g purge.
3MF: stone-job/figure.3mf (Orca, Bambu Studio, Creality Print and PrusaSlicer open it with the paint)
Views: stone-job/build/views.png (look at every panel before you call it done)
In the slicer: filament 2 must be white, filament 4 must be black.
NEXT: none, the part is ready
```

## References

A small model cannot research the web well, so stone carries a reference library in `recipes/lib/refs` and applies it on its own. Every fact there has its value, the page it came from and the date it was checked: filament temperatures, heat deflection, UV, drying and food contact from Prusament and Polymaker data sheets, ISO 273 clearance holes, US screw clearances, fan screw spacing from Noctua, Gridfinity, keystone and wall plate sizes, the IP2X test finger, ADA 703.5 sign letters, WCAG contrast and FDM design guides. `stone show` prints the references that apply to the part, and a passing build picks the filament from the request and says why:

```
Material: PETG, nozzle 240 to 260 C, bed 70 to 90 C (outdoors in sun: PLA softens near 55 C, PETG holds to 68 C; Prusament PETG datasheet, Prusament PLA datasheet)
```

`stone refs PETG` or `stone refs fan` lists the facts on a topic with their sources. No FDM print is certified food safe, and stone says so rather than call one safe.

## Recipes

fan_guard, panel, cable_comb, vase, planter, gridfinity_bin, phone_stand, hook, spur_gear, box, keychain, cookie_cutter, sign, lithophane, relief, figure and fitted_case (a case for a product in the catalog, src/smoothstone/products, built from the maker's sourced sizes). Every recipe prints without supports and every default and example is built and checked in CI.

## Install

You need uv, OpenSCAD 2026 or newer (a nightly build has the Manifold backend) and potrace for pictures.

```
git clone https://github.com/Students-of-Local/smoothstone
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
