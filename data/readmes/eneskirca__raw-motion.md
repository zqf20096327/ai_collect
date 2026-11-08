# raw-motion

**Motion graphics an AI can actually write. No animation library, just a `seek(t)` function.**

<p align="center"><a href="docs/demo.mp4"><img src="docs/demo.gif" width="720" alt="raw-motion demo: this video was made with raw-motion"></a><br><sub>This video was made with raw-motion (<a href="examples/demo/comp.js">source</a>). Click for the 60 fps version with sound.</sub></p>

---

## Animation libraries hold the model back

When you ask an AI to make a motion graphic, it usually reaches for an animation library: a
timeline API, a tween engine, a React video framework. That feels like the grown-up choice. In
practice **the library is what limits the result.**

- **The model starts thinking in the library's vocabulary instead of in motion.** Everything
  becomes "which API call does this", and it can only make the things that API makes easy. A
  staggered tween looks fine. Any motion the library has no word for gets approximated, or dropped.
- **The model only half-knows the API.** Libraries change between versions, and their
  documentation outweighs any one example. So the model's effort goes into getting the API right,
  and the result is plausible-looking code that does something slightly different.
- **Hidden state makes it hard to reason about.** Timelines, playheads, `onComplete` chains,
  real-time `requestAnimationFrame` loops. The model cannot tell what frame 431 looks like without
  running everything before it, and neither can you.

What models already know deeply is **math, the DOM, CSS, SVG and canvas.** So raw-motion gives
them exactly that and one rule:

```js
function seek(t) {
  // set every property on screen from t (seconds). Nothing else moves anything.
}
```

That turns out to work **much better** than any library we tried. The model writes easing curves,
springs and choreography directly, as ordinary code it fully understands. Because the scene is a
pure function of time:

- **Any frame is one call away.** `seek(4.2)` is frame 4.2. The model renders a few stills,
  *looks at them*, and fixes what's wrong before rendering the whole video. That loop is the
  single biggest quality win.
- **It is deterministic.** Same `t`, same pixels, on every machine, every time. Seeded randomness
  only.
- **It parallelizes for free.** N headless Chromes each take every Nth frame, in any order, and
  never coordinate.
- **Anything the browser can draw is fair game.** Type, SVG paths, 2 000-particle canvas swarms,
  video frames, WebGL.

The "engine" is deliberately small: [`engine/motion.js`](engine/motion.js) is about 130 lines of
math (easings, closed-form springs, keyframes, a seeded RNG) that you can read in one sitting. It
is a toolbox, not a framework. `seek(t)` is the only contract.

> We found this while making ~20 video ads with an AI agent in a few days. We started with the
> usual libraries and then threw them out. The ads got better when the model had fewer
> abstractions to fight, not more.

## What you get

- **60 fps with real motion blur.** Each frame is shot 4× across a 180° shutter and averaged. Fast
  moves can ask for more samples (`hi(t0, t1, 24)`), so a whip pan smears instead of strobing.
- **A soundtrack synthesized from the same timeline.** `ev(t, 'hit')` in your scene puts a sound
  on that exact frame. Kicks, whooshes, risers, impacts, pads and an optional music bed are
  generated with numpy, with no samples and no licensing. An optional `voice.wav` is mixed on
  top, and the music ducks under it.
- **One command.** `raw-motion build` renders, synthesizes the audio, encodes H.264 and deletes the
  gigabytes of intermediate frames.
- **Zero npm dependencies.** The renderer drives Chrome over the raw DevTools protocol with
  Node's built-in WebSocket. No Puppeteer, no Playwright.

## Quick start

```sh
git clone https://github.com/eneskirca/raw-motion ~/.raw-motion
alias raw-motion="node ~/.raw-motion/bin/raw-motion.mjs"

raw-motion doctor                          # checks node ≥ 22, Chrome, ffmpeg, python3 + numpy
raw-motion new my-video --w 1080 --h 1920 --dur 12
open my-video/index.html?play              # live preview in any browser (?t=3.5 to freeze a frame)
raw-motion stills my-video 1,3.5,7         # PNGs of exact frames → my-video/stills/
raw-motion build my-video                  # → my-video/out.mp4
```

A project is a folder with `index.html` (the layers), `comp.js` (the `seek` function) and a copy
of `motion.js`. Size and duration live at the top of `comp.js`:

```js
const W = 1080, H = 1920, DUR = 12, FPS = 60;
const { $, set, spring, ease, inv, kf, ev, hi, finish } = RM;

ev(0.6, 'whoosh', .4);  ev(0.8, 'hit');          // sounds, placed on frames
hi(3.9, 4.3, 16);                                // extra motion blur for a fast move

function seek(t) {
  const u = spring(t - 0.8, 2.2, .45);           // 0 → 1 with overshoot, closed form
  set($('title'), { y: (1 - u) * 80, s: .9 + .1 * u, o: inv(0.8, 1.1, t) });
}

finish(seek, DUR, { bpm: 120, chords: [[0, DUR, [57, 60, 64], 33]], groove: [2, 10] });
```

## Using it with an AI agent

The companion skill **[raw-motion-skill](https://github.com/eneskirca/raw-motion-skill)** teaches
Claude (or any agent that reads skills) the whole workflow: it downloads this engine, scaffolds
the project, writes the scene, checks stills, fixes them and builds. It also carries the craft
notes and the pitfalls we hit on the way. Install it and ask for "a 15 second launch video for X".

## The API (`window.RM`)

| | |
|---|---|
| **numbers** | `clamp(x,a,b)` `lerp(a,b,u)` `inv(a,b,x)` (where x sits in [a,b] → 0..1) `map(x,a,b,c,d,ease)` |
| **easing** | `ease.outCubic`, `inOutExpo`, `outBack`, … and `ease.bezier(x1,y1,x2,y2)` |
| **physics** | `spring(t, freq, zeta)` (0 → 1 with overshoot) `impulse(t, freq, zeta)` (a kick that rings back to 0) |
| **keys** | `kf(t, [[t0,v0],[t1,v1,ease],…])` (numbers or arrays) `stagger(t,t0,i,gap)` |
| **random** | `rng(seed)` (mulberry32) `noise1(seed)` (smooth 1-D noise) |
| **DOM** | `set(el,{x,y,s,sx,sy,r,o,blur})` `vis(el,on)` `text(el,s)` `typeOn(str,t,t0,cps)` |
| **timeline** | `ev(t,type,v)` (sound cue) `hi(t0,t1,samples)` (motion-blur window) `finish(seek,dur,music)` |

Sound types: `whoosh` `whoosh_out` `hit` `impact` `drop` `pop` `click` `key` `tick` `blip`
`chime` `riser` `swell` `glitch` `kick` `clap`. Adding one is an `elif` in
[`engine/audio.py`](engine/audio.py).

## Rules that keep a scene correct

1. **No CSS transitions or `@keyframes`.** Every property comes from `t` in `seek`.
2. **Compute, don't accumulate.** Workers seek out of order, so a frame can't depend on the
   previous one. No `x += v`; use closed forms (`spring`, `kf`).
3. **Toggle with `vis()` (`display`), and set everything a frame needs, every frame.**
4. **Seed all randomness.** `Math.random()` gives a different swarm on every worker.
5. **Look at stills before you build.** It takes seconds; a build takes minutes.

## Requirements and cost

Node ≥ 22, Google Chrome or Chromium (`CHROME_BIN` to override), ffmpeg, python3 with numpy.
macOS and Linux are tested. A 15 s 1080p build writes about 10 GB of temporary PNGs, which are
deleted afterwards. The 6 s starter builds in about 1.5 minutes and the 12 s demo (2 200 particles, 24-sample blur) in about 8 minutes on an M-series laptop. `build` checks free disk first
and runs one build at a time per machine.

## License

MIT
