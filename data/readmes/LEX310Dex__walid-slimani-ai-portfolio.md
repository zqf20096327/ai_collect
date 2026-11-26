<div align="center">

# Walid Slimani — AI / ML Portfolio

**Learning systems that solve.**
The interactive portfolio of an AI / ML engineer and AI PhD researcher at ELTE Budapest.

[![Live site](https://img.shields.io/badge/live-walid--slimani.vercel.app-dcf99b?style=for-the-badge&logo=vercel&logoColor=111412&labelColor=111412)](https://walid-slimani.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-walidslimani310-dcf99b?style=for-the-badge&logo=linkedin&logoColor=111412&labelColor=111412)](https://www.linkedin.com/in/walidslimani310)

[![Verify site](https://github.com/LEX310Dex/walid-slimani-ai-portfolio/actions/workflows/verify.yml/badge.svg)](https://github.com/LEX310Dex/walid-slimani-ai-portfolio/actions/workflows/verify.yml)
![Three.js](https://img.shields.io/badge/Three.js-r180-111412?logo=threedotjs&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-3.13%20ScrollTrigger-111412?logo=greensock&logoColor=88CE02)
![WebGL](https://img.shields.io/badge/WebGL-GLSL%20shaders-111412?logo=webgl&logoColor=white)
![No build step](https://img.shields.io/badge/build-zero%20dependencies-111412)
![License](https://img.shields.io/badge/code-MIT-111412)

<a href="https://walid-slimani.vercel.app"><img src="docs/screenshots/hero.jpg" alt="Portfolio hero: a GPU particle field morphing into a graph next to the headline 'Learning systems that solve.'" width="100%"></a>

</div>

---

## About

I'm an **AI / ML engineer and researcher**. I solve hard problems with machine learning, whatever the domain: deep reinforcement learning, graph neural networks, transformers, physics-informed models, cascade ensembles and LLMs.

This repository is the source of my portfolio site. The site makes one point: **the domain changes, the method is AI.** Turbine blades, antennas, MIMO precoding, network routing and ERP assistants are the problems. The models are the work.

## Selected work

| Project | Method | Reported result |
|---|---|---|
| **EACID**: AI inverse design for wind turbine blades *(PhD, ongoing)* | Physics-informed cascade ML, icing-aware geometry generation, distributional site conditioning | End-to-end automated design, no human in the loop |
| **Cascade ML inverse design** for patch antennas | 4-stage cascade of voting ensembles (GB + RF + ET), automated CST data pipeline of 6,450 samples, full-stack web platform | **R² > 0.99** geometry · R² ≈ 0.96 resonant frequency |
| **TD3-MoE**: deep RL expert routing for MU-MIMO | TD3 actor-critic as an attention-supervised mixture-of-experts router, curriculum learning | **33.434 bits/s/Hz** mean sum rate (aggregate benchmark) · CV: 34.01 bits/s/Hz, 99.76 % of optimal |
| **GNN + TabTransformer** 5G signal prediction | Hybrid GCN + TabTransformer on 38,610 real-world measurements (386,100 KNN edges), leakage-audited | **R² = 0.906** · MAE 2.49 dB · 81.1 % quality accuracy on held-out data, beating spatial interpolation |
| **RL-enhanced AODV** | Q-learning agent embedded in AODV route-request handling (ns-2, C++) | **−50 % delay** · −15 % routing overhead · −8 % route errors vs AODV in a 500-node network |
| **LLM assistant for Odoo ERP** | LLM chatbot integration, intent handling | Installed module with chat sessions, logs and intents |

> Results are as reported in my CV and project evaluations. Each project page on the site explains which evaluation every number comes from.

## Screenshots

<table>
  <tr>
    <td width="50%"><img src="docs/screenshots/statement.jpg" alt="Statement section reading 'The domain changes. The method is AI.' above a scrolling marquee of AI methods"></td>
    <td width="50%"><img src="docs/screenshots/work.jpg" alt="Selected AI work section with the EACID project card"></td>
  </tr>
  <tr>
    <td width="50%"><img src="docs/screenshots/hero-antenna.jpg" alt="Hero particle field morphed into a patch antenna with its radiation lobe"></td>
    <td width="50%"><img src="docs/screenshots/about.jpg" alt="About section: From computer systems to applied intelligence"></td>
  </tr>
</table>

<p align="center"><img src="docs/screenshots/mobile.jpg" alt="Mobile layout of the hero section" width="280"></p>

## Engineering highlights

**GPU particle morphing (custom GLSL).** The hero is a 14,000-point field (7,000 on mobile) that morphs between four procedurally generated point clouds:

1. a neural network
2. a turbine blade, built from a NACA-style section law
3. an inset-fed patch antenna with a radiation lobe
4. a k-nearest-neighbour graph

All interpolation, staggered timing, the arc trajectories between shapes, cursor repulsion and the scroll-driven scatter run in the vertex shader ([`dist/shaders/`](dist/shaders)). JavaScript updates only a handful of uniforms per frame.

**Scroll choreography.** GSAP ScrollTrigger drives:
- a sticky three-stage case study
- an exploded three-layer antenna with a manual override slider
- colour-block sections that expand from inset cards
- aperture reveals on project art

A scroll marquee also reacts to scroll velocity and direction.

**Interaction details.**
- Headlines rise word by word from masks.
- Labels "decode" from noise, like a model converging on its output.
- Metrics count up to their exact published values.
- A cursor lens turns into a "View" button over project art, and some buttons pull toward the cursor.
- A short CSS-only intro plays once per session.

**Performance.**
- Rendering runs only for visible scenes in visible tabs.
- Device pixel ratio is capped, and the morph geometry is generated once from a seeded random generator.
- The page has no runtime dependencies and makes no CDN calls for 3D: Three.js and GSAP are bundled locally.

**Accessibility and resilience.**
- `prefers-reduced-motion` and a persistent **Pause motion** control stop every decorative animation.
- Every effect is progressive enhancement, isolated in its own error boundary, and keyboard-reachable where interactive.
- Canvas and SVG fallbacks render when WebGL is unavailable.
- Project dialogs trap focus and return it to the control that opened them.

**Reproducible assets.** The interface sounds are built from two CC0 recordings by [`tools/prepare_audio.py`](tools/prepare_audio.py), which uses ffmpeg filtering plus NumPy trimming, normalisation and eased fades. Re-running it reproduces the shipped `.wav` files byte for byte.

**Supply-chain integrity.** Every deployed file is pinned by SHA-256 in [`manifest.json`](manifest.json). The build step ([`prepare.mjs`](prepare.mjs)) refuses to deploy if any file doesn't match, and [CI](.github/workflows/verify.yml) re-checks integrity, JavaScript syntax and asset references on every push.

## Tech stack

| Layer | Choice |
|---|---|
| Markup & styling | Semantic HTML5, modern CSS (`:has()`, `clip-path`, individual transform properties, container-safe layouts) |
| 3D | Three.js r180 with custom `ShaderMaterial`; GLSL vertex and fragment shaders |
| Motion | GSAP 3.13 + ScrollTrigger, Web Animations API, IntersectionObserver |
| Audio | Web Audio API at runtime; Python (NumPy) + ffmpeg asset pipeline |
| Hosting | Vercel static output with a checksum-verified build |
| CI | GitHub Actions |

No framework and no bundler: the browser runs the code as written.

## Project structure

```text
.
├── dist/                    # The deployed site (served as-is)
│   ├── index.html           # Content, structure, metadata
│   ├── styles.css           # Design tokens, layout, typography
│   ├── app.js               # Project cards, dialogs, galleries, 2D fallback field
│   ├── projects.js          # Project data: copy, metrics, case-study details
│   ├── galleries.js         # Evidence images and captions per project
│   ├── spatial.js           # Three.js scenes + particle morph (ES module)
│   ├── shaders/             # GLSL vertex + fragment shaders for the morph
│   ├── motion-pro.js/.css   # Scroll choreography, reveals, cursor, marquee
│   ├── details-motion.*     # Artwork depth, line traces, orbit motion
│   ├── sound.*              # Opt-in Web Audio interface sounds
│   ├── assets/              # CV, project figures, audio, logos
│   └── vendor/              # Three.js, GSAP, ScrollTrigger (local copies)
├── manifest.json            # SHA-256 pin for every file in dist/
├── prepare.mjs              # Build step: integrity verification
├── vercel.json              # Static hosting configuration
├── tools/                   # Python asset pipeline (interface sounds) + CC0 sources
├── docs/screenshots/        # README imagery
└── .github/workflows/       # CI: syntax, integrity, asset-reference checks
```

## Run locally

No install is needed. Any static server works:

```bash
git clone https://github.com/LEX310Dex/walid-slimani-ai-portfolio.git
cd walid-slimani-ai-portfolio
python -m http.server 4173 --directory dist   # or: npx serve dist
```

Then open <http://localhost:4173>.

To verify integrity the same way CI does:

```bash
node prepare.mjs   # → "Ready: 68 verified static files."
```

After editing anything in `dist/`, regenerate the matching `sha256` entries in `manifest.json`, or the build will reject the change.

## Deploy

The site deploys to **Vercel** as static output. Settings are in [`vercel.json`](vercel.json): framework `null`, build command `node prepare.mjs`, output directory `dist`.

## Credits & licenses

- **Code:** MIT, see [LICENSE](LICENSE).
- **Personal content** (résumé, research figures, project screenshots, biography): © Walid Slimani, all rights reserved.
- **Three.js:** MIT. **GSAP / ScrollTrigger:** [GSAP Standard License](https://gsap.com/standard-license/).
- **Interface sounds:** CC0 derivatives, see [`dist/assets/audio/CREDITS.md`](dist/assets/audio/CREDITS.md).
- Microsoft and Cisco logos identify certification issuers, and the ELTE and ENPO-MA logos identify academic institutions; all remain their owners' trademarks.

---

<div align="center">

**Open to AI research collaborations and ML engineering roles.**
Bring the problem. I'll bring the model.

[Portfolio](https://walid-slimani.vercel.app) · [LinkedIn](https://www.linkedin.com/in/walidslimani310) · [Résumé](dist/assets/Walid-Slimani-CV.pdf)

</div>
