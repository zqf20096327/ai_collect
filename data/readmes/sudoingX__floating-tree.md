# Floating Tree

A one-file prompt benchmark for agentic coding models, by [@sudoingX](https://x.com/sudoingX).

[FLOATING_TREE.md](FLOATING_TREE.md) is the whole benchmark. Hand it to any coding agent, frontier or local, vision or text-only, and it builds a 3D scene in Three.js starting from an empty folder. The file carries everything the build needs: the scene, the module contract, the full palette, the project files, 12 acceptance tests and a visual gate. This repo ships the prompt and nothing else, with no code from any model's build, so every run starts from the same text.

## What gets built

An ancient tree on a floating cliff island at golden hour, as a Vite + Three.js project. The canopy is thousands of individual leaves that fall in the wind, pile up on the grass and grow back. There is a day/night cycle with stars, a moon and fireflies, and wind through 8,000 grass blades. A goblin village of two houses with chimney smoke sits by a pond with lily pads, goblins fly above the island and the clouds are blocky voxels.

Text-only models get the same grade. Every colour, size and position is written out as a value, and the smoke test checks the render for them.

## Run it

1. Put `FLOATING_TREE.md` in an empty folder.
2. Give your agent the prompt in section 0 of the file.
3. Watch it build live at http://localhost:5173.

Needs Node.js 18 or newer with npm (tested on 20). The prompt has the agent install Chromium through Playwright for the visual gate.

## The grade

Done means `npm test` is 12 of 12 green and `npm run smoke` is green. The node suite grades structure, counts and state. The Playwright smoke test loads the page and checks the default view for sky, canopy, trunk and real colour variety, with zero console errors.

Report what section 8 asks for: the test result, the smoke stats line, screenshots, and the model, harness and hardware the run used.

## Share your run

Post your build and tag [@sudoingX](https://x.com/sudoingX) on X.

## License

Apache-2.0, see [LICENSE](LICENSE).
