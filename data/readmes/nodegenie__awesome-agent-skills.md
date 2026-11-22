# Awesome Agent Skills

**2,043 agent skills** for Claude Code, Codex, Cursor and Gemini CLI, indexed weekly from 45 public repositories, each one scanned for the patterns a skill should never need. Searchable at **[usethisskill.com](https://usethisskill.com)**.

## Scan a skill before you install it

A skill is a folder of instructions an agent follows with your permissions. This one command checks every skill folder in a repository for fetch-and-execute commands, destructive commands, data sent to outside endpoints, obfuscated code, rules-override text, credential access, privilege escalation, persistence and force-pushes, with the file and line for each finding:

```
npx github:nodegenie/awesome-agent-skills scan
```

```
clear    .claude/skills/weather-fetcher  (1 files)
FLAGGED  skills/paperclip  (6 files)
         ! Downloads and executes code in one step
           skills/paperclip/references/installation.md:13  curl -fsSL https://example.com/install.sh | bash

2 skill folder(s): flagged. Rules: https://usethisskill.com/safety
```

Or on every pull request:

```yaml
- uses: actions/checkout@v4
- uses: nodegenie/awesome-agent-skills/scan@main
  with:
    fail-on: flag   # or review, or none
```

Across the directory today: **1,969 clear, 59 to review, 15 flagged.** Free for public repositories; private repositories use a Team key from [usethisskill.com/pricing](https://usethisskill.com/pricing). Every rule is explained at [usethisskill.com/safety](https://usethisskill.com/safety).

## Proven skills

Star counts show who found a skill. A proof shows what it changes. On [Use This Skill](https://usethisskill.com/proven), each proven skill was run through Claude twice on the same brief, on the same model, once without the skill and once with it. Both results are saved as live pages with the model, brief and the skill's exact commit recorded, so anyone can run the comparison again.

| Skill | Category | Source |
|---|---|---|
| [canvas-design](https://usethisskill.com/skills/canvas-design) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/canvas-design) |
| [frontend-design](https://usethisskill.com/skills/frontend-design) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| [theme-factory](https://usethisskill.com/skills/theme-factory) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/theme-factory) |
| [ui-ux-pro-max](https://usethisskill.com/skills/ui-ux-pro-max) | Design | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/ui-ux-pro-max) |
| [tailwind-design-system](https://usethisskill.com/skills/tailwind-design-system) | Design | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/frontend-mobile-development/skills/tailwind-design-system) |
| [web-design-guidelines](https://usethisskill.com/skills/web-design-guidelines) | Design | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) |
| [accessibility-compliance](https://usethisskill.com/skills/accessibility-compliance) | Design | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/ui-design/skills/accessibility-compliance) |
| [brand-guidelines](https://usethisskill.com/skills/brand-guidelines) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |
| [internal-comms](https://usethisskill.com/skills/internal-comms) | Other | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/internal-comms) |
| [changelog-generator](https://usethisskill.com/skills/changelog-generator) | Docs & Writing | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator) |
| [test-driven-development](https://usethisskill.com/skills/test-driven-development) | Testing | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [writing-plans](https://usethisskill.com/skills/writing-plans) | Docs & Writing | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/writing-plans) |
| [skill-creator](https://usethisskill.com/skills/skill-creator) | Testing | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| [systematic-debugging](https://usethisskill.com/skills/systematic-debugging) | Testing | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging) |
| [algorithmic-art](https://usethisskill.com/skills/algorithmic-art) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |
| [web-artifacts-builder](https://usethisskill.com/skills/web-artifacts-builder) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) |
| [brainstorming](https://usethisskill.com/skills/brainstorming) | Design | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [vercel-react-best-practices](https://usethisskill.com/skills/vercel-react-best-practices) | Frontend | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [vercel-composition-patterns](https://usethisskill.com/skills/vercel-composition-patterns) | Design | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) |
| [writing-guidelines](https://usethisskill.com/skills/writing-guidelines) | Testing | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/writing-guidelines) |
| [mcp-builder](https://usethisskill.com/skills/mcp-builder) | Design | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) |
| [vercel-react-view-transitions](https://usethisskill.com/skills/vercel-react-view-transitions) | Design | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions) |
| [tdd](https://usethisskill.com/skills/tdd) | Testing | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) |
| [improve-codebase-architecture](https://usethisskill.com/skills/improve-codebase-architecture) | Design | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) |
| [prototype](https://usethisskill.com/skills/mattpocock-prototype) | Design | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [triage](https://usethisskill.com/skills/triage) | Automation | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) |
| [grilling](https://usethisskill.com/skills/grilling) | Testing | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) |
| [design-taste-frontend](https://usethisskill.com/skills/design-taste-frontend) | Design | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/taste-skill) |
| [ui-styling](https://usethisskill.com/skills/ui-styling) | Design | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/.claude/skills/ui-styling) |

The first proof is free to try live. [See the proofs →](https://usethisskill.com/proven)

## Browse by category

| Category | Skills |
|---|---|
| [Automation](skills/automation.md) | 779 |
| [Design](skills/design.md) | 295 |
| [Testing](skills/testing.md) | 233 |
| [Backend](skills/backend.md) | 204 |
| [Data & Science](skills/data-science.md) | 158 |
| [Other](skills/other.md) | 134 |
| [Docs & Writing](skills/docs-writing.md) | 70 |
| [Security](skills/security.md) | 69 |
| [Frontend](skills/frontend.md) | 54 |
| [Motion](skills/motion.md) | 47 |

## Install a skill

Every skill has a one-line install command that copies the skill folder into your project:

```sh
npx degit anthropics/skills/skills/frontend-design .claude/skills/frontend-design
```

Claude Code reads `.claude/skills/` automatically. Codex, Cursor and other agents have equivalent folders; each skill's page on [usethisskill.com](https://usethisskill.com/skills) shows the command for yours.

## Where the skills come from

- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) · 864 skills
- [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) · 246 skills
- [wshobson/agents](https://github.com/wshobson/agents) · 185 skills
- [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) · 177 skills
- [Shaisolaris/solaris-dev-shop](https://github.com/Shaisolaris/solaris-dev-shop) · 100 skills
- [trailofbits/skills](https://github.com/trailofbits/skills) · 97 skills
- [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) · 74 skills
- [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) · 46 skills
- [mattpocock/skills](https://github.com/mattpocock/skills) · 38 skills
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) · 22 skills
- [anthropics/skills](https://github.com/anthropics/skills) · 20 skills
- [software-mansion/argent](https://github.com/software-mansion/argent) · 18 skills
- [obra/superpowers](https://github.com/obra/superpowers) · 15 skills
- [Grit-77/done-is-a-claim](https://github.com/Grit-77/done-is-a-claim) · 15 skills
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 13 skills
- [remotion-dev/skills](https://github.com/remotion-dev/skills) · 12 skills
- [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) · 11 skills
- [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) · 10 skills
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) · 9 skills
- [SAP/open-ux-tools](https://github.com/SAP/open-ux-tools) · 7 skills
- [chromedevtools/chrome-devtools-mcp](https://github.com/chromedevtools/chrome-devtools-mcp) · 7 skills
- [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) · 7 skills
- [browser-use/browser-use](https://github.com/browser-use/browser-use) · 6 skills
- [vercel/next.js](https://github.com/vercel/next.js) · 6 skills
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) · 6 skills
- [morluto/rea](https://github.com/morluto/rea) · 5 skills
- [callstack/agent-device](https://github.com/callstack/agent-device) · 4 skills
- [tester-army/e2e](https://github.com/tester-army/e2e) · 3 skills
- [getsentry/XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP) · 2 skills
- [zereight/gitlab-mcp](https://github.com/zereight/gitlab-mcp) · 2 skills
- [tobi/qmd](https://github.com/tobi/qmd) · 2 skills
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · 1 skills
- [flashfrogluo/second-take](https://github.com/flashfrogluo/second-take) · 1 skills
- [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) · 1 skills
- [chrisryugj/kordoc](https://github.com/chrisryugj/kordoc) · 1 skills
- [colorjs/color-space](https://github.com/colorjs/color-space) · 1 skills
- [dgunning/edgartools](https://github.com/dgunning/edgartools) · 1 skills
- [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) · 1 skills
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) · 1 skills
- [yamadashy/repomix](https://github.com/yamadashy/repomix) · 1 skills
- [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) · 1 skills
- [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) · 1 skills
- [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) · 1 skills
- [homeassistant-ai/skills](https://github.com/homeassistant-ai/skills) · 1 skills
- [designed-by-ai/skills](https://github.com/designed-by-ai/skills) · 1 skills

Skills belong to their authors. This list links to each source and only reproduces a skill's full text on usethisskill.com when its license allows it.

## For AI assistants and search engines

A machine-readable index of the catalog is published at [usethisskill.com/llms.txt](https://usethisskill.com/llms.txt) and [usethisskill.com/llms-full.txt](https://usethisskill.com/llms-full.txt).

## Submit a skill

Open an issue with the **Add a skill repository** template. Submissions are checked, scanned and indexed, and answered on the issue, within a few hours, around the clock. Nothing waits for months here.

## Use it from inside your agent

**Claude Code plugin** (adds a `/find-proven-skill` skill and the MCP server):

```
claude plugin marketplace add nodegenie/awesome-agent-skills
claude plugin install usethisskill@usethisskill
```

**MCP server** for Claude, Claude Code, Cursor and any MCP client: `https://usethisskill.com/mcp`. Setup for each client is at [usethisskill.com/connect](https://usethisskill.com/connect).

## Contributing

Skills are discovered automatically from the source repositories every week. To add a repository that publishes skills, [open an issue](https://github.com/nodegenie/awesome-agent-skills/issues/new) with the link.

---

Last refreshed October 24, 2026. Maintained by [Tineessa Nelson](https://x.com/tineessavm) · [usethisskill.com](https://usethisskill.com)
