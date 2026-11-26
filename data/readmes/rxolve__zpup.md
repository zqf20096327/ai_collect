# Zpup

Describe a small 3D scene as JSON and get a flat SVG picture of it from any angle. Inspired by [Zdog](https://zzz.dog/).

Pronounced "zee-pup".

![One lighthouse scene drawn from four angles](examples/lighthouse-views.svg)

These four pictures come from [one scene](examples/lighthouse.ts): eleven solids with one color each, plus a door and a window, placed in 3D. Only the view angle differs. Zpup works out what hides what and how each face is shaded, and writes a plain SVG with no JavaScript, so the picture works in an `<img>` tag, an email or a README. One view of the lighthouse is 5.5 KB.

**[Try it in the playground](https://rxolve.github.io/zpup/)**: edit a scene as JSON, drag the picture to turn it, and export the SVG.

**[Play a small game drawn with it](https://rxolve.github.io/zpup/game/)**: a person, a tree, a cabin and three animals, each written once as JSON by an AI model and drawn in every direction and pose as a sprite sheet.

**[Use it from an AI model](#with-an-ai-model)**: an MCP server lets Claude and other models write a scene, look at the picture and correct it. In Claude Code, `claude mcp add zpup -- npx -y @zpup/mcp`.

## Compared with Zdog

![The same lighthouse turning in Zdog and in Zpup](examples/zdog-vs-zpup.svg)

Both halves are the same solids at the same places and sizes ([Zdog script](examples/lighthouse.zdog.js), [Zpup scene](examples/lighthouse.ts)); the Zdog half is a flip-book of Zdog's own SVG output, one frame every 3 degrees. Watch the hut and the boulder as they pass behind the tower: in Zdog the island is painted over them.

Zdog orders shapes by one point each, so a large shape such as the ground covers smaller ones that sit on it once they are farther away than its center. In Zdog the fix is done by hand, with groups or by cutting the large shape up. Zpup compares every pair of shapes that overlap on screen and works out which one is in front. In [the benchmark](bench/README.md), the median share of a picture painted in the wrong order was 2.9% and 4.2% for Zdog in two runs, and 0.4% and 0.3% for Zpup.

## What it is for

Small illustrations with volume: icons, mascots, props, a little building. And sprites for a game: one scene gives the same character in every direction and every pose, so the frames agree with each other. The scene is data, so a person, a script or an AI model can write it, and mistakes come back as errors that say where and how to fix them.

<p>
  <a href="examples/pup.ts"><img src="examples/pup.svg" alt="A sitting pup" width="130"></a>
  <a href="examples/rocket.ts"><img src="examples/rocket.svg" alt="A rocket on its pad" width="130"></a>
  <a href="examples/cake.ts"><img src="examples/cake.svg" alt="A two-tier cake with candles" width="130"></a>
  <a href="examples/robot.ts"><img src="examples/robot.svg" alt="A small robot" width="130"></a>
  <a href="examples/cactus.ts"><img src="examples/cactus.svg" alt="A cactus in a pot" width="130"></a>
</p>

Each picture links to its scene, 60 to 150 lines of TypeScript. The cactus uses [soft shading](#soft-shading).

It is not a 3D engine. There is no perspective, no textures and no light to place, and shapes that cut deep into each other are not drawn correctly. There is no text shape and no clipping either. For that, use three.js or a modeling tool.

## Status

1.0. The scene format and the exported functions are stable: within 1.x a scene that is valid stays valid and every option keeps its meaning. How a picture is worked out can still get better, so the exact SVG a scene produces may change between versions; [docs/decisions.md](docs/decisions.md#what-10-promises) says what is promised and what is not.

Not planned: perspective, lighting, textures, a text shape and clipping.

Motion is possible, and it is the caller that plays it. A scene is plain data: change it (turn a joint, move a part, turn the view) and draw it again, and the new picture is the next frame. A game either does that as it runs, or draws the poses beforehand onto a sprite sheet, as [the MCP server](mcp/README.md#poses) does for a walk. The one thing a single SVG file does by itself is a constant turn about one axis (see [Turning in place](#turning-in-place)); other animation inside the file is not planned.

Not built: a canvas renderer and framework bindings. `compileScene` returns the sorted list of things to paint, which is what either would start from.

## Install

```bash
npm install @zpup/core
```

Zpup is ESM-only and has no runtime dependencies. It is built for ES2022 and tested on Node 24; it uses no Node APIs, so it also runs in browsers. Bundled and minified, the whole library is 75 KB (27 KB gzipped), and `renderSvg` alone is 55 KB (20 KB gzipped).

## Usage

A scene is a plain object tree. `renderSvg` turns it into an SVG string, with no DOM, so it works on a server and the first paint needs no JavaScript. Here is [a pup](examples/pup.ts) built from thick dots and lines, `renderSvg(pup)`:

![A small sitting pup drawn with Zpup](examples/pup.svg)

A smaller scene:

```ts
import { dot, ellipse, renderSvg } from '@zpup/core';

const svg = renderSvg({
  width: 120,
  height: 120,
  rotate: { x: -20, y: 30 },
  children: [
    dot({ stroke: 40, color: '#e62' }), // a thick dot is a sphere
    ellipse({ diameter: 70, stroke: 5, color: '#636', rotate: { x: 90 } }), // a ring around it
  ],
});
```

The helpers only add a `type` field, so the same scene can be written, stored and sent as JSON:

```json
{
  "width": 120,
  "height": 120,
  "rotate": { "x": -20, "y": 30 },
  "children": [
    { "type": "dot", "stroke": 40, "color": "#e62" },
    { "type": "ellipse", "diameter": 70, "stroke": 5, "color": "#636", "rotate": { "x": 90 } }
  ]
}
```

To see the scene from another side, change `rotate` on the scene and render again. Nothing else in the scene has to change:

```ts
const front = renderSvg({ ...scene, rotate: { x: -16, y: 24 } });
const back = renderSvg({ ...scene, rotate: { x: -16, y: 204 } });
const above = renderSvg({ ...scene, rotate: { x: -62, y: 24 } });
```

### The basics

- **Axes:** x right, y down, z toward the viewer. The origin is the center of the image.
- **Angles:** degrees. Positive `rotate.z` turns clockwise on screen.
- **Nodes:** `group`, `dot`, `path`, `ellipse`, `rect`, `polygon`, and the solids `box`, `cylinder`, `cone` and `hemisphere`. Every node takes `translate`, `rotate`, `scale`, `visible` and `children`; children inherit their parent's transform.
- **Shapes:** `color` (hex, `rgb()` and other CSS functions, or one of the CSS color names; a misspelled name is an error), `stroke` (round-capped width; thick strokes give volume) and `fill`.
- **Solids:** `box`, `pyramid`, `cylinder`, `cone` and `hemisphere`, always filled. One `color` is enough: each face gets a fixed lighter or darker version of it by the direction it faces in the scene, so a box does not collapse into a flat hexagon. Face options such as `topFace` or `frontFace` set a face's exact color, or leave the face out with `false`. As in Zdog, cylinders, cones and hemispheres point along z; `rotate: { x: 90 }` stands them up. A box and a pyramid stand upright as they are.
- **Errors:** an invalid scene or option throws a `ZpupValidationError` that lists every problem with its path, what was expected and how to fix it. Each issue has the path as a string (`path`) and as keys and indices (`pathSegments`), and the message with (`message`) and without (`detail`) the path in front. `checkScene(scene)` returns the same list without throwing. `checkSceneWarnings(scene)` lists things that are valid but probably unintended, such as angles in radians, shapes placed outside the image, or shapes of different colors that pass through each other.

### Solids

![A lighthouse on a rock built from cylinders, cones, hemispheres and a box](examples/lighthouse.svg)

[The lighthouse](examples/lighthouse.ts) is made of eleven solids, each with a single color, plus a door and a window drawn as rectangles on the tower:

```ts
import { cone, cylinder } from '@zpup/core';

const up = { x: 90 }; // round solids point along z; this stands them up
cylinder({ diameter: 60, length: 36, rotate: up, color: '#f4f1ea' }); // a band of the tower
cone({ diameter: 44, length: 18, rotate: up, color: '#d8463c' }); // the hut's roof
```

A `pyramid` stands on a rectangular base with its top straight above the middle. Its `ridge` turns the point into an edge, which gives the three usual roofs from one shape ([scene](examples/roofs.ts)):

![Three huts with a pointed roof, a hip roof and a gable roof](examples/roofs.svg)

```ts
pyramid({ width: 68, depth: 52, height: 30 }); // a point
pyramid({ width: 68, depth: 52, height: 30, ridge: 30 }); // a hip roof
pyramid({ width: 68, depth: 52, height: 30, ridge: 68 }); // a gable roof, or a wedge
```

A `cone` takes `tipDiameter`, which cuts its tip off: a lamp shade, a plant pot, a cup. Here the far end is a face in a darker color, which reads as soil or coffee ([scene](examples/pots.ts)):

![A lamp, a plant pot and a cup, each a cone with its tip cut off](examples/pots.svg)

A face option set to `false` leaves that face out, and the solid is open: you see its inside through the opening, and what stands in it is drawn there, in front of the far wall and behind the near one. `inside` sets the color of the inside; without it, a darker `color` is used. The walls have no thickness ([scene](examples/open.ts)):

![A cup of pencils, an open crate with two balls in it and a bowl of fruit](examples/open.svg)

```ts
cylinder({ diameter: 44, length: 52, rotate: up, color: '#3f7fbf', frontFace: false }); // a cup
box({ width: 84, height: 40, depth: 60, color: '#c8975a', topFace: false }); // a crate
hemisphere({ diameter: 76, rotate: { x: -90 }, color: '#6fb1c4', backface: false }); // a bowl
```

Solids are depth-sorted like everything else, against each other and against flat shapes. Rest one solid on a flat face of another; solids that cut into each other cannot be drawn correctly.

### Soft shading

By default every shape has one flat color. `shading: "soft"` on the scene shades round things from their color, as if lit from the upper left: dots and the round surfaces of solids (the side of a cylinder or cone, the dome of a hemisphere) with a gradient, and thick lines as tubes. Flat shapes and lines stay as they are.

```ts
renderSvg({
  width: 120,
  height: 120,
  shading: 'soft',
  children: [dot({ stroke: 80, color: '#e62' })],
});
```

The light belongs to the picture, not to the scene: it stays in the upper left when the view changes. In a turning picture, a ball keeps its shading all the way round, and so does the side of an upright cylinder or cone turning about the vertical axis. A side that is tilted changes direction on screen as it turns, and its shading follows in steps of 15 degrees.

Shapes of the same color that cut into each other look like one shape when flat. With soft shading each has its own highlight, so the seam shows, and in a turning picture the moment one passes in front of the other shows too. Keep such shapes just touching, or leave the shading flat.

### Faces that turn away

A flat shape takes `backface`, as in Zdog: `true` (the default) draws it from both sides, `false` leaves it out while its front (its local +z side) faces away, and a color paints its back in that color.

This is what keeps a turning character clean. Zpup paints whole shapes back to front, so an eye drawn as a dot on a head has to jump from in front of the head to behind it as the head turns, and it does so while it still covers part of the head: the eye flickers. Built this way instead, a model turns without popping:

- Parts of different colors touch but do not cut into each other.
- Parts that cut into each other have the same color.
- Color on a surface (eyes, cheeks, a patch on the belly) is a flat, filled shape with no stroke and `backface: false`, on the plane that touches the surface, just outside it. It disappears at the moment it is seen edge-on, when it covers nothing.

```ts
import { dot, ellipse, group } from '@zpup/core';

const head = [
  dot({ stroke: 80, color: '#f4c95d' }),
  group({
    rotate: { x: 15, y: -25 }, // points the eye's +z up and to the left
    children: [
      ellipse({
        translate: { z: 40.5 },
        width: 8,
        height: 11,
        fill: true,
        stroke: 0,
        color: '#222',
        backface: false,
      }),
    ],
  }),
];
```

### Turning in place

A scene can also be shown turning. `renderSpinSvg` returns an SVG that turns the scene one full rotation, forever, using SMIL animation. It needs no JavaScript, so it also plays inside an `<img>` tag and in a GitHub README. It suits small scenes; the file grows quickly with the number of shapes (see the limits below).

![The pup, turning around](examples/pup-spin.svg)
![The lighthouse, turning around](examples/lighthouse-spin.svg)

```ts
import { renderSpinSvg } from '@zpup/core';

const svg = renderSpinSvg(scene, {
  axis: 'y', // which angle of scene.rotate turns: 'x', 'y' (default, a turntable) or 'z'
  duration: 8, // seconds per turn
  keyframes: 36, // exact angles per turn; the browser interpolates in between
  direction: 'positive', // or 'negative'
  precision: 1, // decimals kept in coordinates
});
```

Every option is optional, and bad values throw a `ZpupValidationError` like an invalid scene does. Renderers without SMIL show the first frame, which is the same picture `renderSvg` draws. The pictures on this page were checked in Chrome, Safari's engine (WebKit) and Firefox. It is synchronous and depth-sorts the scene at 720 angles: about 60 ms for a small scene and 0.6 s for the lighthouse on a laptop, so in a browser run it in a worker (the playground does).

Limits:

- Only a constant-speed turn about one axis. Nothing else moves, and there is no interaction or pausing.
- It does not respect `prefers-reduced-motion`; SMIL cannot query it. A page that cares can show the still picture instead with a `<picture>` element and a `(prefers-reduced-motion: reduce)` media query.
- Outlines are drawn one segment at a time, so a translucent color shows darker spots where the segments meet.
- File size grows quickly with the number of pieces: every piece is listed once per change of paint order, and those changes grow with the number of overlapping pairs. The turning pup is 43 KB, 6 KB gzipped; the turning lighthouse is 129 KB, 24 KB gzipped. A still picture of either is 2 to 6 KB. Lower `keyframes` and `precision` make it smaller.

See [docs/decisions.md](docs/decisions.md#turning-animation) for how it works.

There is no perspective and no light to place, by design; soft shading is a fixed look, not a lighting model. See [docs/decisions.md](docs/decisions.md) for the reasoning behind these and other choices, and [llms.txt](llms.txt) for a compact reference written for AI coding tools.

## With an AI model

[`@zpup/mcp`](mcp/README.md) is an MCP server that lets a model write a scene, get its mistakes back as errors that say where they are and how to fix them, and see a PNG of the picture from several angles in one call. It remembers the scene, so after the first picture the model sends only what changes. For a game it can also draw the scene from 8 or 16 directions as one sprite sheet, with the frame list engines read, and in several poses, such as the steps of a walk, with one row per direction and one column per pose. [The game](https://rxolve.github.io/zpup/game/) is drawn this way.

```json
{
  "mcpServers": {
    "zpup": { "command": "npx", "args": ["-y", "@zpup/mcp"] }
  }
}
```

In Claude Code:

```bash
claude mcp add zpup -- npx -y @zpup/mcp
```

A model that can run code needs only the library and [llms.txt](llms.txt).

[![rxolve/zpup MCP server](https://glama.ai/mcp/servers/rxolve/zpup/badges/score.svg)](https://glama.ai/mcp/servers/rxolve/zpup)

## Goals

- Round, flat, designer-friendly pseudo-3D illustrations, in the spirit of Zdog
- One scene, any view angle, as a still SVG picture
- TypeScript and ESM from the start
- A declarative API that is easy for both people and AI coding tools to write correctly
- SVG output that can be rendered on the server
- Depth sorting that holds up when shapes overlap

## Development

Requires Node.js 22.18 or later (the example script runs TypeScript directly) and [pnpm](https://pnpm.io/).

```bash
pnpm install
pnpm test        # unit and snapshot tests
pnpm typecheck
pnpm lint
pnpm build       # writes dist/
pnpm example     # writes the pictures in examples/
pnpm playground:build  # builds the playground into playground/dist/, servable as static files
```

The MCP server is a second package in [`mcp/`](mcp), built with `pnpm --dir mcp build`. Its tests run with the rest.

### Releasing

Raise the version in `package.json` (and, for the server, in `mcp/package.json` and both places in `mcp/server.json`), add the changes to the changelog, and push a tag:

```bash
git tag v1.0.1 && git push origin v1.0.1
```

[The release workflow](.github/workflows/release.yml) then publishes whatever version is not out yet: `@zpup/core` and `@zpup/mcp` to npm, and the server's entry to the MCP Registry. It uses no tokens; npm trusts the workflow by name. A tag starting with `mcp-v` does the same, for a release of the server alone.

## Credits

Zpup is inspired by [Zdog](https://github.com/metafizzy/zdog) by David DeSandro. It is a new implementation that shares no code with Zdog. It is an independent project and is not affiliated with Zdog or Metafizzy.

## License

MIT
