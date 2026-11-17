<div align="center">

# tinythree

**A tiny 3D scene language that compiles to Three.js.**<br>
Designed so AI models can write 3D scenes with **3–7× fewer tokens**, faster and cheaper.

[![CI](https://github.com/muskec06/tinythree/actions/workflows/ci.yml/badge.svg)](https://github.com/muskec06/tinythree/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![three.js](https://img.shields.io/badge/three.js-r187-black?logo=three.js)](https://threejs.org)
[![dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](package.json)
[![Playground](https://img.shields.io/badge/try_it-playground-00e5ff.svg)](https://muskec06.github.io/tinythree/)

[**Playground**](https://muskec06.github.io/tinythree/) · [Gallery](#gallery) · [Benchmark](#benchmark) · [Language](spec/LANGUAGE.md) · [AI prompt](ai/SYSTEM_PROMPT.md) · [Türkçe](README.tr.md)

<img src="docs/hero.gif" width="400" alt="A detailed Eiffel Tower with 1,400 lattice beams, written in 57 lines of tinythree">

</div>

---

## Why

When a language model writes Three.js, most of what it types is ceremony: `new THREE.Mesh(new THREE.BoxGeometry(…), material)`, `.position.set(…)`, render loops, resize handlers, easing math. Output tokens are the slowest and most expensive part of a model's answer.

tinythree gives the model a notation that only describes the scene: what is where, made of what, moving how. A zero-dependency compiler turns it into plain Three.js. It targets the web, and frame-exact video as well.

<table>
<tr><th>tinythree: 57 lines, 1,117 tokens</th><th>Three.js: 165 lines, 3,028 tokens</th></tr>
<tr>
<td valign="top">

```
// four curved legs, each a lattice in three segments
truss leg1 2.6,2.1,3 @5,0,5 lean=-1.25,-1.25 iron mirror=xz
truss leg2 2.1,1.7,2.76 @3.75,3,3.75 lean=-.85,-.85 iron mirror=xz
truss leg3 1.7,1.25,5.84 @2.9,5.76,2.9 lean=-1.5,-1.5 iron mirror=xz
torus arch 3.4,.09 @0,.5,0 arc=180 ry=90 iron radial=4,4.55
box floor1 7,.3,7 @0,5.76,0 deck
truss gallery1 7.4,7.4,.8 @0,5.9,0 n=14 t=.03 iron
truss shaft1 4,2.9,4.4 @0,11.6,0 iron
```

</td>
<td valign="top">

```js
function truss(w0, w1, h, x, y, z, lx = 0, lz = 0, bays, t) {
  const P = (k, yy) => { /* corner k at height yy */ };
  const beams = [];
  for (let i = 0; i < bays; i++) { /* posts, rings, X braces */ }
  const m = new THREE.InstancedMesh(beamGeo, iron, beams.length);
  beams.forEach(([a, b, th], i) => { /* orient each beam */ });
  …
}
for (const [sx, sz] of [[1, 1], [-1, 1], [1, -1], [-1, -1]]) {
  truss(2.6, 2.1, 3, 5 * sx, 0, 5 * sz, -1.25 * sx, -1.25 * sz);
  …
```

</td>
</tr>
</table>

The tower has real proportions (1 unit = 10 m) and is built from about 1,400 lattice beams drawn as instanced meshes, standing on the Champ de Mars by the Seine. Full sources: [`examples/eiffel-tower.t3`](examples/eiffel-tower.t3) and [`bench/threejs/eiffel-tower.js`](bench/threejs/eiffel-tower.js).

## Benchmark

<img src="docs/benchmark.png" width="760" alt="Bar chart: tinythree uses 2.7× to 6.9× fewer tokens than hand-written Three.js across 11 scenes, 3.5× in total">

Each of the 11 scenes was written once in tinythree and once as compact, idiomatic Three.js. Loops and helper functions were allowed in the Three.js versions, and both versions were rendered to confirm they draw the same scene.

| | |
|---|---|
| **Tokens** | 14,151 → 4,057 in total, **3.5× fewer** (2.7×–6.9× per scene; scenes with parts, textures, models and labels save the most) |
| **Speed** | generation time grows roughly linearly with output tokens, so a scene takes about a third of the time to write |
| **One-time cost** | the [AI prompt](ai/SYSTEM_PROMPT.md) that teaches the language is ~1,500 tokens. It pays for itself after about two scenes and can be prompt-cached |
| **Edits** | changing one object means one short line, not a block of JavaScript |

Reproduce it with `npm run bench`, and see [bench/RESULTS.md](bench/RESULTS.md) for the full table. Counts use OpenAI's o200k tokenizer. Claude's tokenizer differs, but because both are BPE tokenizers the ratios come out similar. Even after subtracting the ~150 tokens of renderer setup that tinythree hides, the result is still 3.1× fewer.

## Gallery

Every scene below is a single `.t3` file of 7 to 57 lines. Click one to open it in the playground.

<table>
<tr>
<td align="center" colspan="3"><a href="https://muskec06.github.io/tinythree/#town-square"><img src="docs/gallery/town-square.jpg" width="480"><br><b>Town square</b></a><br><sub>464 tokens · 6.9× fewer · library parts, procedural textures, an animated glTF model and a text label</sub></td>
</tr>
<tr>
<td align="center"><a href="https://muskec06.github.io/tinythree/#eiffel-tower"><img src="docs/gallery/eiffel-tower.jpg" width="240"><br><b>Eiffel Tower</b></a><br><sub>1,117 tokens · 2.7× fewer · 1,400 beams</sub></td>
<td align="center"><a href="https://muskec06.github.io/tinythree/#leaning-tower-pisa"><img src="docs/gallery/leaning-tower-pisa.jpg" width="240"><br><b>Leaning Tower of Pisa</b></a><br><sub>316 tokens · 3.1× fewer</sub></td>
<td align="center"><a href="https://muskec06.github.io/tinythree/#giza-pyramids"><img src="docs/gallery/giza-pyramids.jpg" width="240"><br><b>Pyramids of Giza</b></a><br><sub>293 tokens · 2.8× fewer</sub></td>
</tr>
<tr>
<td align="center"><a href="https://muskec06.github.io/tinythree/#stonehenge"><img src="docs/gallery/stonehenge.jpg" width="240"><br><b>Stonehenge</b></a><br><sub>375 tokens · 3.0× fewer</sub></td>
<td align="center"><a href="https://muskec06.github.io/tinythree/#london-eye"><img src="docs/gallery/london-eye.jpg" width="240"><br><b>London Eye</b></a><br><sub>305 tokens · 3.3× fewer</sub></td>
<td align="center"><a href="https://muskec06.github.io/tinythree/#building"><img src="docs/gallery/building.jpg" width="240"><br><b>Construction site</b></a><br><sub>322 tokens · 3.1× fewer</sub></td>
</tr>
<tr>
<td align="center"><a href="https://muskec06.github.io/tinythree/#solar-farm"><img src="docs/gallery/solar-farm.jpg" width="240"><br><b>Solar plant</b></a><br><sub>253 tokens · 3.6× fewer</sub></td>
<td align="center"><a href="https://muskec06.github.io/tinythree/#atom"><img src="docs/gallery/atom.jpg" width="240"><br><b>Atom (education)</b></a><br><sub>234 tokens · 2.7× fewer</sub></td>
<td align="center"><a href="https://muskec06.github.io/tinythree/#vectors"><img src="docs/gallery/vectors.jpg" width="240"><br><b>Vector addition (education)</b></a><br><sub>122 tokens · 3.8× fewer</sub></td>
</tr>
</table>

## Quick start

### 1. In the browser, with nothing to install

Open the [playground](https://muskec06.github.io/tinythree/), pick an example and edit it. The scene updates as you type. You can view the generated Three.js, download a standalone HTML page, or copy the AI prompt.

### 2. With an AI model

1. Put [`ai/SYSTEM_PROMPT.md`](ai/SYSTEM_PROMPT.md) in the system prompt, or paste it into the chat. The playground has a **📋 AI prompt** button that copies it.
2. Ask for a scene: *"the Colosseum at sunset, camera slowly orbiting"*.
3. Paste the answer into the playground, or run `tinythree build`.
4. If the compiler reports `line N: …`, send that line back to the model. Errors are short and come with a suggested fix.

### 3. Command line

```bash
git clone https://github.com/muskec06/tinythree && cd tinythree && npm install
node bin/tinythree.js build   examples/eiffel-tower.t3 -o eiffel.html   # standalone page
node bin/tinythree.js compile examples/eiffel-tower.t3 -o eiffel.js     # ES module
node bin/tinythree.js check   examples/*.t3                              # validate
```

### 4. From JavaScript

```js
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { compile, mount } from './src/tinythree.js';

const code  = compile(source, { format: 'fn' });
const built = new Function('THREE', code + '\nreturn build(THREE);')(THREE);
const view  = mount(THREE, built, document.body, { OrbitControls });

built.objects.ring.material.color.set('hotpink'); // everything is addressable by name
view.seek(2.5);                                    // jump to t = 2.5 s
```

## The language at a glance

```
scene bg=#0b1020 cam=4,3,6 look=0,1,0 orbit shadows dur=8s   // camera, background, flags
sun 5,10,7 2                                                  // lights: amb, hemi, sun, point
mat wood #8b5a2b r=.7                                         // material: color, roughness, metal, glow, opacity
box top 2,.1,1 @0,1,0 wood                                    // type [name] [size] [material] [@position]
box leg .1,1,.1 @.9,.5,.4 wood mirror=xz                      // copies: mirror, array, grid, radial
group lamp @.5,1,0                                            // indent to nest
  sphere bulb .08 #fff
use lamp lamp2 @-.5,1,0                                       // clone
anim lamp rot.y spin 4s                                       // spin, wave, to … at= ease=
anim cam orbit 20s
```

| | |
|---|---|
| **Shapes** | `box` `sphere` `cyl` `cone` `torus` `plane` `capsule` `lathe` `extrude` `arrow` `truss` `group` `use` |
| **Content** | `text "label"` · `model chair.glb play` · `mat brick map=brick rep=4,2` (image or built-in texture) · `use lib:tree` (13 real-size parts) |
| **Copies** | `mirror=xz` · `array=n,dx,dy,dz` · `grid=nx,nz,dx,dz` · `radial=n,r` |
| **Animation** | `spin` · `wave` · chained `to` tweens with `at=` and `ease=` · `anim cam orbit` |
| **Escape hatch** | `js`, `tick` and `renderer` blocks take raw Three.js for anything else: GLTF models, shaders, particles, post-processing, environment maps, WebXR |

The full reference is in [spec/LANGUAGE.md](spec/LANGUAGE.md).

## Does it cover all of Three.js?

Yes. The coverage is checked by a browser test suite: [**39/39 capability probes pass**](docs/CAPABILITIES.md).

| | features | probes |
|---|---|---:|
| ✅ **tinythree syntax** | shapes, lattices, materials, image and procedural textures, text labels, glTF models with animations, a part library, lights, shadows, fog, copies, clones, animation, perspective and orthographic cameras, frame-exact video | 18 |
| 🧩 **`js` / `tick` blocks** | extra geometries, physical, toon and shader materials, spot and area lights, particles, lines, sprites, instancing, raycasting, keyframe, morph and skinned animation, async assets, audio | 16 |
| 🔧 **`renderer` block** | tone mapping, environment maps, post-processing (bloom, DOF, SSAO…), HTML labels, WebXR | 5 |

The token savings come from the first row. The other two are plain Three.js inside the scene file: they cost the same tokens as Three.js, but you never have to leave tinythree. Known limits are listed in [docs/CAPABILITIES.md](docs/CAPABILITIES.md#known-limits).

## Video rendering

`update(t)` is a pure function of time, so every frame is rendered at an exact timestamp and the output doesn't depend on machine speed. This makes tinythree useful for educational videos and motion graphics.

<img src="docs/building.gif" width="480" alt="A building rising floor by floor while a crane turns">

```bash
pip install playwright && playwright install chromium   # once; ffmpeg must be on PATH
python tools/render.py examples/building.t3 -o building.mp4                     # length from scene dur=
python tools/render.py examples/atom.t3 -o atom.mp4 --fps 60 --size 1920,1080
python tools/render.py overlay.t3 -o overlay.mov       # scene bg=none → ProRes 4444 with alpha
python tools/render.py examples/atom.t3 -o thumbnail.png --still 1.5
```

## How it works

```mermaid
flowchart LR
  A[scene.t3] --> B[parse<br/>line-based, indentation]
  B --> C[AST<br/>copies expanded]
  C --> D[codegen]
  D --> E["build(THREE)<br/>plain Three.js"]
  E --> F[mount<br/>renderer · orbit · loop]
  E --> G[toHTML<br/>standalone page]
  G --> H[render.py<br/>seek t → frame → ffmpeg]
```

- **One file:** [`src/tinythree.js`](src/tinythree.js), about 800 lines with zero dependencies, running in the browser and in Node.
- **Readable output:** the generated code is ordinary Three.js that you can keep editing.
- **Errors for models:** for example `line 7: unknown command "spehre" (did you mean "sphere"?)`. One line, one fix.

## Project layout

```
src/tinythree.js      parser, compiler, runtime (mount) and HTML export
bin/tinythree.js      CLI
ai/SYSTEM_PROMPT.md   compact language description for LLMs (~1.5k tokens)
spec/LANGUAGE.md      full language reference
examples/             11 example scenes (+ assets/windmill.glb)
playground/           live editor (GitHub Pages)
bench/                token benchmark, hand-written Three.js versions, chart, capability audit
tools/render.py       frame-exact video and PNG renderer
test/                 node:test suite
```

## Roadmap

- **Wall openings (CSG):** `box wall 6,3,.3 wall cut=door`. Measured: 143 → 41 tokens (3.5× fewer) than doing it today in a `js` block with three-bvh-csg.
- **Claude skill and MCP server** that write, compile and render a scene in one step.
- **First-try success rate** across several models, measured with each provider's own token counter.

## Contributing

Issues and pull requests are welcome, especially new example scenes. A good example comes with its hand-written Three.js twin in `bench/threejs/` so the benchmark grows with it. Run `npm test` and `npm run bench` before opening a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments

- [three.js](https://threejs.org), which does all the real work.

## License

[MIT](LICENSE) © muskec06
