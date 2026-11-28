<div align="center">

<a href="https://galley.fictiontribe.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/logo/lockup-reverse.svg">
    <img src="brand/logo/lockup.svg" alt="Galley" width="220">
  </picture>
</a>

<p><strong>The open-source AI CMS for static sites</strong><br>
Prompt it. Proof it. Publish it.</p>

<p>
<a href="https://www.npmjs.com/package/galley-cms"><img alt="galley-cms on npm" src="https://img.shields.io/npm/v/galley-cms?label=galley-cms&logo=npm"></a>
<a href="https://www.npmjs.com/package/create-galley"><img alt="create-galley on npm" src="https://img.shields.io/npm/v/create-galley?label=create-galley&logo=npm"></a>
<a href="https://github.com/fictiontribe/galley/actions/workflows/ci.yml"><img alt="CI on main" src="https://img.shields.io/github/actions/workflow/status/fictiontribe/galley/ci.yml?branch=main&label=CI&logo=github"></a>
<a href="https://github.com/fictiontribe/galley/actions/workflows/release.yml"><img alt="Release workflow" src="https://img.shields.io/github/actions/workflow/status/fictiontribe/galley/release.yml?label=release&logo=github"></a>
<br>
<a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/github/license/fictiontribe/galley"></a>
<a href="https://nodejs.org"><img alt="Node.js 20.11 or newer" src="https://img.shields.io/node/v/galley-cms"></a>
<a href="https://github.com/fictiontribe/galley/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/fictiontribe/galley"></a>
<a href="CONTRIBUTING.md"><img alt="Pull requests welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen"></a>
</p>

<p>
<a href="https://galley.fictiontribe.com">Website</a> ·
<a href="https://galley.fictiontribe.com/tour/">Tour</a> ·
<a href="https://galley.fictiontribe.com/how-to/">How-to guides</a> ·
<a href="https://galley.fictiontribe.com/docs/">Docs</a> ·
<a href="CHANGELOG.md">Changelog</a> ·
<a href="ROADMAP.md">Roadmap</a>
</p>

</div>

<p align="center">
  <img src="apps/site/public/screens/form.webp" width="880" alt="Galley's editor on Caddow, a made-up fashion label's site. On the left, a form for the home page with its Campaign hero section open and the heading field marked Edited; on the right, the page itself with the new heading “Coats for low sun.” over a photograph of a model in a rust coat.">
</p>

Galley opens a site whose content lives in git and lets anyone change it — in
a form, on the page or by asking the assistant. You check every change
beside the live site, then publish it as a commit to your own repository. No
database, no account, no telemetry.

## Try it

You need Node.js 20.11 or newer and git. A new site from one of the starters
(they are Astro 7 sites, so they need Node.js 22.23.4 or newer):

```sh
npm create galley@latest
```

A site you already have — run this in its folder:

```sh
npx galley-cms
```

Either way, Galley opens in your browser on your own computer, ready to edit
the site. To change Galley itself, run it from a clone:
[CONTRIBUTING.md](CONTRIBUTING.md#dev-setup).

## What it does

Statuses come from [the website](https://galley.fictiontribe.com/), which
keeps one list of them. Anything not marked is built.

**Change a page**

- **No set-up.** Point it at a site: it works out the framework, the
  content collections, every field's type and the page sections from your
  schemas and files, without running any of your code.
- **Three ways in.** A form made from the site's own content model; the words
  on the page, retyped in the live preview; or the assistant (Anthropic's
  Claude, with your own key). All three end in the same Proof.
- **One field changed, one value changed.** Comments, quoting, key order and
  the markdown body stay exactly as they were.
- **Build pages from the site's own sections.** *Preview.* Drag a section
  onto the page, move it, switch its options.

**Check and publish**

- **Proof.** Every change in the site's own words, marked up beside the live
  site. Put any one back.
- **Publish to your own repository.** A commit, or a branch and a pull
  request. Undo is a new commit; nothing is rewritten.

**Look after the site**

- **Forms and an inbox.** Send submissions to HubSpot, Marketo, Salesforce,
  Pardot, a webhook or Galley's own inbox.
- **Scripts with consent.** Tag Manager, Analytics and others, loaded after
  the visitor agrees.
- **Brand.** Read from the site, or from guidelines, logos and screenshots.
- **Search and AI checks.** Findings, with fixes that wait in Proof. On Astro
  sites with the site kit: a markdown copy of every page, `llms.txt`, and a
  switch per AI crawler written into `robots.txt`.
- **Redirects.** Paste a list; loops, chains and doubles are caught, and the
  host's redirects file stays in step.
- **Put it online.** On Cloudflare, with your own domain. Vercel is *in
  progress*.

**Grow**

- **Many sites, one app.** Filed by client, your brand on the app, client
  changes as pull requests.
- **Your own AI tool.** An MCP server gives Claude Desktop, Claude Code,
  Cursor, VS Code or any MCP client the same tools as the assistant.
- **Starters.** Caddow (fashion), Ferrow (B2B software), Lowfield Studio
  (small business) and Sarking (long-form blog with charts and tables), three
  looks each. A Shopify storefront is *in progress*.
- **Move from WordPress.** *New, in final checks.* Posts, pages, images and
  search details in four steps, as changes you check before anything goes
  live.
- **Plugins.** Image and video generation among them; a plugin can be one
  file.

<table>
  <tr>
    <td width="50%"><img src="apps/site/public/screens/assistant.webp" width="430" alt="The assistant beside the Caddow page. Asked to change the campaign heading and its first button, it replies with the exact new words, says both changes are waiting in Proof, and offers Review in Proof and Undo this change."></td>
    <td width="50%"><img src="apps/site/public/screens/proof-changes.webp" width="430" alt="Proof for the home page: “Coats for the long afternoon.” struck out and “Coats for low sun.” written in, the button “See the lookbook” renamed “See the eight looks”, and “begin” changed to “start” inside a heading, each with Put back."></td>
  </tr>
  <tr>
    <td>Ask, and the assistant says exactly what it changed.</td>
    <td>Proof: struck out, written in, put back.</td>
  </tr>
  <tr>
    <td><img src="apps/site/public/screens/arrange.webp" width="430" alt="Arrange on the Caddow home page: the Lookbook grid section selected with its tone and crop options in the side panel, and a library of section types to drag onto the page."></td>
    <td><img src="apps/site/public/screens/site-home.webp" width="430" alt="Site home for Caddow: a box to ask for a change, three pages waiting to publish, a card to put the site online, and a card for moving from WordPress."></td>
  </tr>
  <tr>
    <td>Arrange the site's own sections. <em>Preview</em></td>
    <td>Site home: what's waiting, and what to do next.</td>
  </tr>
</table>

## How it works

```text
  Prompt                      Proof                          Publish
  a form, the page,     →     each change beside the    →    a commit and a push,
  or the assistant            live site                      or a pull request
```

- **The working tree is the draft.** A pending change is an uncommitted change
  in your checkout.
- **Proof is the difference** between that draft and the last commit, shown
  field by field beside the live site.
- **Publish is `git commit` and `git push`** (or a branch and a pull request).
  Undo is `git revert`.
- **No database.** Nothing to migrate, nothing to export.
- **No lock-in.** Pages stay your files. Any editor, script or MCP client can
  work on them, and the app's own HTTP API is documented.

Changing a heading on the Lowfield Studio starter is exactly this:

```diff
-    heading: Make more of the *home you already have*.
+    heading: Make more of the *house you already have*.
```

The principles behind it are in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Works with

- **Astro fits deepest.** Galley reads `astro.config.*`, the content config
  and its zod schemas (discriminated unions become page sections) and the
  routes in `src/pages`, without running your code. The site kit and the
  starters are Astro.
- **Docusaurus, Nuxt, Next.js, SvelteKit, Eleventy, Hugo and Jekyll** each
  have a built-in adapter that reads the framework's own configuration
  statically, and any folder of markdown with front matter works.
- **Anything else** arrives through a small [adapter](docs/adapters.md), with
  a conformance kit to prove it and a worked
  [Eleventy example](examples/adapter-eleventy).

## Roadmap

Intent, not a promise. The longer version is [ROADMAP.md](ROADMAP.md).

**Now**

- The guided move from WordPress, in final checks
- The editor hosted on your own server, one site per install, in final
  checks

**Next**

- Vercel deploys, Cloudflare Bulk Redirects and attaching a fresh own domain,
  run on the real services
- The Shopify storefront starter
- Hosting the editor online from the app (Fly.io, Cloudflare, your own
  server), run on the real services
- The desktop app for Windows and Linux, tried by people and signed
- The site kit, adapter kit and plugin kit on npm

**Later**

- Galley Cloud: the editor, hosted for you

## Documentation

| Guide | What's in it |
| --- | --- |
| [Quickstart](https://galley.fictiontribe.com/docs/getting-started/quickstart/) | Your site in Galley: change a page, proof it, publish it |
| [Tour](https://galley.fictiontribe.com/tour/) | The whole app, in pictures |
| [How-to guides](https://galley.fictiontribe.com/how-to/) | Fourteen tasks, step by step |
| [Editing guides](https://galley.fictiontribe.com/docs/editing/tour/) | Every screen, for the people who change the site |
| [Running it](https://galley.fictiontribe.com/docs/running/hosted/) | The hosted editor, the [desktop app](https://galley.fictiontribe.com/docs/running/desktop/), [deploying](https://galley.fictiontribe.com/docs/running/deploy/) |
| [Reference](https://galley.fictiontribe.com/docs/reference/cli/) | The command line, the [configuration file](https://galley.fictiontribe.com/docs/reference/config/), the [HTTP API](https://galley.fictiontribe.com/docs/reference/api/) |
| [Adapters](https://galley.fictiontribe.com/docs/adapters/) | How frameworks plug in, and how to write one |
| [Plugins](https://galley.fictiontribe.com/docs/plugins/) | What a plugin can add, and how to write one |
| [MCP](https://galley.fictiontribe.com/docs/integrations/mcp/) | Connect Claude, Cursor, VS Code or any MCP client |

The documentation checks itself against the code on every build: a command,
option or setting it names has to exist.

## Repository layout

| Path | What |
| --- | --- |
| [`packages/core`](packages/core) | The engine: detection, surgical edits, the workspace and git, the preview, the assistant |
| [`packages/server`](packages/server) | The HTTP API, live events, the web UI, local and hosted security |
| [`packages/cli`](packages/cli) | `galley-cms` on npm, the `galley` command |
| [`packages/galleycms`](packages/galleycms) | `galleycms` on npm, alias for `galley-cms` (`npx galleycms`) |
| [`packages/create-galley`](packages/create-galley) | `create-galley` on npm, behind `npm create galley` |
| [`packages/web`](packages/web) | The React UI |
| [`packages/overlay`](packages/overlay) | The click-to-edit script in the preview |
| [`packages/mcp`](packages/mcp) | The MCP server behind `galley mcp` |
| [`packages/astro`](packages/astro) | The site kit for Astro: forms, scripts, agent-readable pages |
| [`packages/adapter-kit`](packages/adapter-kit) | Types and conformance checks for adapters |
| [`packages/plugin-kit`](packages/plugin-kit) | Types and checks for plugins |
| [`packages/import-wordpress`](packages/import-wordpress) | The WordPress importer |
| [`packages/plugins`](packages/plugins) | The plugins built into `galley-cms` |
| [`apps/desktop`](apps/desktop) | The desktop app (Tauri 2) |
| [`apps/site`](apps/site) | The website and documentation — a site Galley edits |
| [`starters`](starters) | The five starters `galley new` copies |
| [`examples`](examples) | A worked adapter and a worked plugin |
| [`brand`](brand) | The brand guide, voice, tokens and logo |

## Status

Galley is on npm as `galley-cms` and `create-galley`. While the version starts
with `0.`, the configuration file, the API and the command-line options can
change between minor versions ([what the numbers mean](RELEASING.md#what-the-version-numbers-mean-before-10)).

- **Built**: everything in [What it does](#what-it-does) that isn't marked
  otherwise, in the web app and the macOS desktop app.
- **New, in final checks**: the guided move from WordPress, run against an
  export file and a stand-in WordPress site, not yet a real one; a hosted
  editor, one site per install, run for real on its image and on a server
  behind HTTPS (multi-arch image published to `ghcr.io/fictiontribe/galley` on
  each release: [`docs/cloud-install.md`](docs/cloud-install.md)).
- **Preview**: the page builder.
- **In progress**: deploys to Vercel (built, not yet run on the real
  service); hosting the editor online on your own Fly.io, Cloudflare or
  server (run against stand-ins for Fly.io and Cloudflare, not the real
  services); the Shopify storefront starter.
- **Not verified yet**: the desktop app on Windows and Linux in a person's
  hands (both are built and checked automatically, and on Windows the
  installed app is opened; the macOS app is signed and notarised); the OpenAI
  and Google image providers; the assistant's fallback request profile;
  setting redirects on Cloudflare itself (Bulk Redirects); attaching a fresh
  own domain on the real services; a hosted editor's own key accepted by a
  code host end to end.
- **Kits (`@galleycms/*`)**: the site kit (`@galleycms/astro`, which sites
  can also carry vendored), `@galleycms/adapter-kit` and `@galleycms/plugin-kit`
  are wired into the release workflow. The plugins remain built into
  `galley-cms`.

Every push runs the type checks, the tests, the app build and the site build
in [GitHub Actions](.github/workflows/ci.yml).

## Contributing

Issues, ideas and pull requests are welcome. [CONTRIBUTING.md](CONTRIBUTING.md)
has the setup, the checks a pull request must pass and the copy conventions.
Every commit is signed off under the [DCO](DCO) (`git commit -s`); there is
no CLA. Good places to start:

- **Starters**: a new site for a kind of business the starters don't cover.
- **Adapters**: an adapter for a framework Galley doesn't ship with yet
  ([how](docs/adapters.md)).
- **Plugins**: a form destination, a script, an image service, a host
  ([how](docs/plugins.md)).

Questions and ideas go to [Discussions](https://github.com/fictiontribe/galley/discussions);
bugs to [Issues](https://github.com/fictiontribe/galley/issues). Everyone
follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

Report a vulnerability privately, never in a public issue:
[SECURITY.md](SECURITY.md) says how, and what is in scope.

## License

[Apache License 2.0](LICENSE); see also [NOTICE](NOTICE). "Galley" and the
Galley logo are marks of Fiction Tribe; [TRADEMARKS.md](TRADEMARKS.md) says
how they may be used.

Galley is made by [Fiction Tribe](https://www.fictiontribe.com). Astro,
WordPress and the other names here are trademarks of their owners; Galley is
not affiliated with or endorsed by them.
