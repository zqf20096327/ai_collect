# GameArt Prompt Kit

[中文说明](./README.zh-CN.md)

Reusable prompt profiles for game art, pixel spritesheets, character concepts, and 2D environments.

The library is organized as practical Markdown profiles. Each profile describes what it is for, when to use it, what kind of input works best, and a reusable prompt template that can be copied into an image-generation model.

These prompt profiles are designed for mainstream image-generation models as well as local or self-hosted workflows such as ComfyUI, Stable Diffusion, and other node-based pipelines.

## Highlights

- 14 prompt profiles covering pixel spritesheets, creature animation sheets, character concept art, topdown maps, side-view environments, and arcade-style backgrounds.
- English and Simplified Chinese profile sets.
- Preview images for every prompt profile.
- Clear usage-mode labels so you know whether a profile is best for text-only generation, uploaded reference images, or both.
- Self-contained Markdown files that are easy to copy, adapt, and version.

## Usage Modes

| Mode | Meaning |
| --- | --- |
| `Text-to-image` | Use the prompt profile with a written description. No uploaded reference image is required. |
| `Reference-guided` | Upload a reference image and use the prompt profile to extend, refine, or preserve the visual design. |
| `Hybrid` | Works with either a written description or an uploaded reference image, depending on the workflow. |

## Quick Start

1. Pick a prompt profile from the table below.
2. Open the Markdown file and check its `Usage Mode`.
3. Copy the template section into your image-generation tool.
4. Replace the placeholder fields with your character, creature, scene, or style details.
5. If the profile is `Reference-guided` or `Hybrid`, upload the reference image when the workflow calls for it.
6. Generate, compare against the preview, and iterate on the variable fields.

## Repository Structure

```text
.
├── README.md
├── README.zh-CN.md
├── img/
│   ├── reference-input.png
│   └── *.png
└── profiles/
    ├── en/
    │   └── *.md
    └── zh-CN/
        └── *.md
```

## Prompt Profiles

| File | Purpose | Usage Mode | Preview |
| --- | --- | --- | --- |
| [five-direction-jrpg-run-cycle-sheet.md](./profiles/en/five-direction-jrpg-run-cycle-sheet.md) | Five-direction JRPG character run-cycle sheet | Hybrid | <img src="./img/five-direction-jrpg-run-cycle-sheet.png" width="120" alt="five direction jrpg run cycle sheet preview"> |
| [compact-8x8-action-platformer-sheet.md](./profiles/en/compact-8x8-action-platformer-sheet.md) | Compact 8x8 action-platformer character sheet | Hybrid | <img src="./img/compact-8x8-action-platformer-sheet.png" width="120" alt="compact 8x8 action platformer sheet preview"> |
| [four-by-eight-jrpg-adventurer-sheet.md](./profiles/en/four-by-eight-jrpg-adventurer-sheet.md) | 4x8 JRPG adventurer motion sheet | Hybrid | <img src="./img/four-by-eight-jrpg-adventurer-sheet.png" width="120" alt="four by eight jrpg adventurer sheet preview"> |
| [indie-character-grid-animation-sheet.md](./profiles/en/indie-character-grid-animation-sheet.md) | Indie character animation sheet with 8x8 and 9x8 grid modes | Hybrid | <img src="./img/indie-character-grid-animation-sheet.png" width="120" alt="indie character grid animation sheet preview"> |
| [reference-based-sideview-action-sheet.md](./profiles/en/reference-based-sideview-action-sheet.md) | Reference-based side-view character action sheet | Reference-guided | <img src="./img/reference-based-sideview-action-sheet.png" width="120" alt="reference based sideview action sheet preview"> |
| [humanoid-enemy-action-spritesheet.md](./profiles/en/humanoid-enemy-action-spritesheet.md) | Humanoid enemy action spritesheet template | Hybrid | <img src="./img/humanoid-enemy-action-spritesheet.png" width="120" alt="humanoid enemy action spritesheet preview"> |
| [aerial-creature-spritesheet.md](./profiles/en/aerial-creature-spritesheet.md) | Aerial creature spritesheet with 5x6 animation layout | Text-to-image | <img src="./img/aerial-creature-spritesheet.png" width="120" alt="aerial creature spritesheet preview"> |
| [mounted-character-gallop-sheet.md](./profiles/en/mounted-character-gallop-sheet.md) | Mounted character gallop animation sheet | Hybrid | <img src="./img/mounted-character-gallop-sheet.png" width="120" alt="mounted character gallop sheet preview"> |
| [comprehensive-character-action-grid.md](./profiles/en/comprehensive-character-action-grid.md) | Comprehensive 10x10 character action grid | Hybrid | <img src="./img/comprehensive-character-action-grid.png" width="120" alt="comprehensive character action grid preview"> |
| [impasto-inkwash-character-concept.md](./profiles/en/impasto-inkwash-character-concept.md) | Character concept art with impasto and ink-wash styling | Hybrid | <img src="./img/impasto-inkwash-character-concept.png" width="120" alt="impasto inkwash character concept preview"> |
| [orthographic-topdown-pixel-scene.md](./profiles/en/orthographic-topdown-pixel-scene.md) | Orthographic topdown pixel scene with object and ground modes | Text-to-image | <img src="./img/orthographic-topdown-pixel-scene.png" width="120" alt="orthographic topdown pixel scene preview"> |
| [angled-topdown-pixel-scene.md](./profiles/en/angled-topdown-pixel-scene.md) | Angled topdown pixel scene with asset and ground modes | Text-to-image | <img src="./img/angled-topdown-pixel-scene.png" width="120" alt="angled topdown pixel scene preview"> |
| [tilebased-sideview-pixel-environment.md](./profiles/en/tilebased-sideview-pixel-environment.md) | Tile-based side-view cross-section pixel environment | Text-to-image | <img src="./img/tilebased-sideview-pixel-environment.png" width="120" alt="tilebased sideview pixel environment preview"> |
| [parallax-sideview-arcade-environment.md](./profiles/en/parallax-sideview-arcade-environment.md) | Side-view arcade environment with parallax layers | Text-to-image | <img src="./img/parallax-sideview-arcade-environment.png" width="120" alt="parallax sideview arcade environment preview"> |

## Adding a New Profile

1. Create an English profile under `profiles/en/`.
2. Create the matching Simplified Chinese profile under `profiles/zh-CN/`.
3. Add an example image under `img/` using the same slug as the profile file.
4. Include an `Example`, `Purpose`, and `Usage Mode` section in each profile.
5. Add the profile to both README tables.

## Notes

- Prompt results vary by model, model version, sampling settings, and uploaded references.
- Grid-based spritesheet prompts may require several iterations for exact frame alignment.
- Preview images are examples, not strict output guarantees.

## License

Released under the [MIT License](./LICENSE). The prompt profiles, documentation, and example images in this repository are covered by the same license unless noted otherwise.
