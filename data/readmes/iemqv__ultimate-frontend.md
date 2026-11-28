# Ultimate Frontend

One skill for coding agents that design, build, and review web interfaces. Give your agent a brief, a mockup, or a bug without turning every task into a redesign.

From your project root:

```sh
npx ultimate-frontend install
```

Choose your agent and reload it. Requires Node.js 20 or later. Supports Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI, OpenCode, and Pi.

## Why

I kept reaching for the same frontend tools. On a new site I'd load several together; for a small fix I'd pick just the one I needed. Either way, I had to decide what to load before I could ask for the work.

I built Ultimate Frontend to make that a single call. It brings the design and interaction practices I rely on into one skill that chooses what fits the brief. A new portfolio can start with a bold composition; a keyboard fix should leave the rest of the page alone. Both deserve a check in the browser when one is available.

## Use it

Ask your agent to use `ultimate-frontend` and describe the task in your own words. For example:

- “Use ultimate-frontend to build a printmaker’s portfolio. Let visitors inspect the texture of each print.”
- “Use ultimate-frontend to make this sortable list work with a keyboard. Keep the layout.”
- “Use ultimate-frontend to review checkout against the approved mockup. Don’t edit code.”

The skill follows your project’s design system and approved mockups. It distinguishes what the agent saw in a browser from what it could only check in code. The [local verification engine](docs/engine-contract.md) is optional and is not part of the npm install.

## Fork or contribute

Start with [SKILL.md](skills/ultimate-frontend/SKILL.md) and its [references](skills/ultimate-frontend/references/). To try your fork, run `node /path/to/ultimate-frontend/bin/ultimate-frontend.mjs install` from a test project. Run `npm test` in the fork to check the installer and packaged skill. See the [distribution notes](docs/distribution.md) for releases.

## Credits

Ultimate Frontend adapts ideas from Anthropic’s [Frontend Design](https://github.com/anthropics/skills), Emil Kowalski’s [Apple Design](https://github.com/emilkowalski/skills), Leonxlnx’s [Taste Skill](https://github.com/Leonxlnx/taste-skill), Paul Bakaus’s [Impeccable](https://github.com/pbakaus/impeccable), and Damir Sokolovsky’s [Unslop](https://github.com/heydamir/unslop). Its approach to sequencing creative pages also draws on the [Awwwards skill](https://github.com/juliobsz/skills).

See [attribution and upstream licenses](ATTRIBUTION.md) and the [project license](LICENSE).
