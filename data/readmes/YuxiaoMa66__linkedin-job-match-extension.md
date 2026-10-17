> **Current release: v0.6.4.** It combines the structured resume library, four-mode evidence policy, and separate sponsorship-risk review in the release package. See the [v0.6.4 release notes](./RELEASE_NOTES_v0.6.4.md) and the [scoring and resume contract](./docs/SCORING_v0.6.4.md).

<p align="center">
  <img src="./docs/assets/readme-hero.png" alt="LinkedIn Job Match. Know the fit before you apply." width="100%" />
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a>&nbsp;&nbsp;|&nbsp;&nbsp;<strong>English</strong>
</p>

<p align="center">
  <a href="https://github.com/YuxiaoMa66/linkedin-job-match-extension/tree/main"><img alt="v0.6.4 source" src="https://img.shields.io/badge/version-v0.6.4-9a4a30?style=flat-square" /></a>
  <img alt="Chrome Manifest V3" src="https://img.shields.io/badge/Chrome-MV3-9a4a30?style=flat-square" />
  <img alt="Vite 5" src="https://img.shields.io/badge/Vite-5-9a4a30?style=flat-square" />
  <a href="./LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-9a4a30?style=flat-square" /></a>
</p>

<p align="center">
  A local-first Chrome extension for resume matching, reusable job analysis, inline LinkedIn and Indeed signals, and Netherlands sponsorship context.
</p>

<p align="center">
  <a href="https://github.com/YuxiaoMa66/linkedin-job-match-extension/tree/main"><strong>Use v0.6.4 source on main</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#configuration">Configuration</a>
</p>

> [!NOTE]
> `v0.6.4` is the current source and latest downloadable package. It keeps the tested Netherlands Indeed adapter and LinkedIn workflows while making the evidence/scoring boundary explicit.
>
> Upgrade path: `v0.5.0 → v0.6.4`. Versions v0.6.0–v0.6.3 were internal development builds and were never published as separate releases.

> [!IMPORTANT]
> **Current v0.6.4 compatibility**
>
> v0.6.4 supports the Netherlands Indeed site (`nl.indeed.com`), LinkedIn Classic, and AI-powered Search. It reads visible Indeed job cards, the selected job detail, and `#jobDescriptionText`, then reuses the selected structured resume profile, analysis cache, title signals, history, and saved-position workflow. Refresh the Indeed or LinkedIn page after installing or reloading the extension.

> [!IMPORTANT]
> **Current LinkedIn compatibility**
>
> v0.6.4 supports both LinkedIn's **classic Jobs search** and the newer **AI-powered / semantic search** interface. On the AI layout, it reads the visible job cards and the selected job detail. After updating the extension or switching between search layouts, refresh the LinkedIn page so the content reader attaches to the current layout.

<p align="center">
  <img src="./docs/assets/classic-search-switch.png" alt="LinkedIn's Learn more menu with Switch back to classic search highlighted" width="100%" />
</p>

## Quick start

1. **First install:** download a built ZIP, extract it, and load the extracted folder from `chrome://extensions/` → `Developer mode` → `Load unpacked`.
2. **Update an existing v0.1.2+ installation:** extract the new ZIP, replace the files inside the original extension `Location`, keep the folder path unchanged, and click `Reload` on the original card.
3. **Use a supported job page:** v0.6.4 reads LinkedIn Classic, LinkedIn AI-powered search, and the Netherlands Indeed list. After switching sites/layouts or updating the extension, refresh the page.
4. Add one or more resumes in the side panel, choose the current structured profile, open a job or a visible job list, and run the analysis.

The same-folder update keeps the extension ID and therefore preserves local settings, resume data, saved/manual positions, and compatible history. Loading a newly extracted folder creates a separate unpacked extension ID and separate `chrome.storage.local`; the detailed reason and recovery steps are in [Installation](#installation).

## See the decision surface

Match scores and job signals stay on the job page while the side panel keeps the resume, evidence, history, saved positions, and re-analysis controls together.

![LinkedIn Jobs search with the v0.6.4 side panel, selected resume profile, and cached list analysis](./docs/assets/v0.6.4-overview.png)

The LinkedIn and Indeed adapters share the same structured-resume, score, cache, history, and title-signal layer in v0.6.4.

![Indeed job list with v0.6.4 cached analysis, match score, and title capsules](./docs/assets/v0.6.4-indeed.png)

This verified v0.6.4 view shows an Indeed list and selected job detail working with the selected resume profile, cached result, match score, `JD` language, and required-language capsules.

![v0.6.4 LinkedIn list mode with current title signals](./docs/assets/v0.6.4-list-mode.png)

For the current capsule palette and provider starter reference, see the [Title signals reference](./docs/TITLE_SIGNALS.md).

Prefer a visual walkthrough? Open the [product homepage](./docs/index.html).

## What It Brings Together

| Capability | What it changes |
| --- | --- |
| Resume-to-role matching | Scores single jobs, visible Classic or AI-powered LinkedIn search results, and jobs pasted from other sources using the selected structured resume profile. |
| Inline job-page signals | Adds match scores and configurable title capsules for JD language, required language, experience, sponsorship, and JD keywords on LinkedIn and Indeed. |
| Reusable decision history | Caches compatible analyses by resume and scoring context, keeps separate LinkedIn, Indeed, and inserted-job history, and saves positions for later review. |
| Provider choice | Supports OpenAI, Anthropic, Gemini, OpenRouter, Poe, and custom OpenAI-compatible endpoints. |
| Netherlands sponsorship context | Checks organisation names against a bundled IND-derived dataset containing 12,927 unique names. |

## What's New In v0.6.4

- Turns each uploaded resume into a reusable `resume-v1` structured profile covering experience, education, skills, certifications, languages, and other sections
- Adds a resume library with `+ Add resume`, `Use for analysis`, `Re-read`, and `Remove`; the selected profile owns the active matching cache
- Reconstructs PDF text lines from page coordinates before structuring, reducing missed education headings, degrees, institutions, and dates
- Sends the configured model a dedicated evidence-preserving resume extraction prompt; failed or unavailable model parsing is visibly labeled `Local fallback`
- Keeps the exact extracted source locally for quotation verification while presenting the structured profile first to the matching prompt; the original PDF/DOCX file is not stored
- Migrates the legacy `persistentResume` record into the library automatically
- Removes empty JD dimensions from Breakdown instead of displaying a synthetic `Not scored` requirement
- Adds four analysis modes: `Strict`, `Balanced`, `Potential`, and `Sponsorship-first`; Balanced is the default, while each mode applies a different evidence boundary and scoring preference.
- Keeps `Sponsorship-first` focused on separate sponsorship risk/context; it has no `Sponsorship Fit` capability-score weight, so sponsorship never contributes a second percentage to the capability score.
- Bumps the matching prompt to `v10` so structured profiles and exact-source verification are part of the cache identity

Read the [v0.6.4 scoring and resume contract](./docs/SCORING_v0.6.4.md) and the [v0.6.4 release notes](./RELEASE_NOTES_v0.6.4.md) for the base public release details.

## Release history

v0.6.4 is the latest public release and the next install target after v0.5.0. Historical detail is kept in the [release archive](./docs/releases/README.md) so the homepage stays focused on the product people can install and test today.

| Version | Focus | Status |
| --- | --- | --- |
| v0.6.4 | Structured resume library and evidence scoring | Latest public release; [notes](./RELEASE_NOTES_v0.6.4.md) |
| v0.5.0 | Netherlands Indeed list adapter | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.5.0.md) |
| v0.4.0 | LinkedIn AI-powered search | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.4.0.md) |
| v0.3.1 | Title signals and provider starters | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.3.1.md) |
| v0.2.0 | Sponsor dataset and product homepage | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.2.0.md) |
| v0.1.2 | Library, saved positions, and inserted jobs | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.1.2.md) |
| v0.1.1 | Scoring modes and evaluation controls | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.1.1.md) |
| v0.1.0 | First public release | Public release; [notes](./docs/releases/RELEASE_NOTES_v0.1.0.md) |

The intermediate v0.6.0–v0.6.3 scoring/provider work was not released separately; its engineering notes and historical contracts are listed under [internal development notes](./docs/releases/README.md#internal-development-notes-included-in-v064).

## Core Features

### 1. Structured resume library

Uploaded resumes are normalized into profiles in `chrome.storage.local` and stay available after:

- page refresh
- side panel reopen
- browser restart

You can keep multiple profiles, select which one drives analysis, re-read a profile after changing model settings, or remove one profile. The extracted source text remains local for exact evidence quotes; the original PDF/DOCX file is not retained.

### 2. Single-job analysis

On a LinkedIn or Indeed job detail page, the extension reads:

- job title
- company
- location
- job description text

It then shows the result in the side panel and reuses cache when the same job has already been analyzed for the same resume and scoring context.

### 3. List mode analysis on LinkedIn and Indeed

On LinkedIn's Classic or AI-powered Jobs search results page, and on the Netherlands Indeed jobs list, the extension can:

- detect visible job cards on the page
- read AI-powered cards from their stable LinkedIn component keys and retain the job ID used by the existing cache
- read Indeed cards from their stable `data-jk` job IDs and the selected Indeed detail pane
- focus an AI-powered card and wait for the selected detail pane before reading the JD
- focus an Indeed card and wait for its detail pane and JD to finish rendering
- analyze the first `N` jobs automatically
- load and show more jobs from the same page
- reuse cached results instead of re-calling the model
- re-analyze the current job or the shown jobs
- open a second-level detail view inside the side panel when a list item is clicked

### 4. Library and saved positions

The new `Library` section lets users:

- switch between `History` and `Saved`
- switch between `LinkedIn`, `Indeed`, and `Inserted`
- reopen prior analyses in an in-card detail view
- remove single history entries
- remove single saved positions

### 5. Inserted jobs

The `Jobs from insert` section supports pasted jobs from other sources.

Users can:

- paste raw job text
- choose `Rule detect` for fast local extraction
- choose `Model detect` for AI-assisted structuring
- review detected fields
- save and analyze the inserted job
- reopen inserted job results later

### 6. Inline LinkedIn badges

The extension injects badges directly into LinkedIn's native UI.

Supported inline signals include:

- overall match score
- `KM` sponsorship marker
- JD language
- required experience
- required job languages

### 7. Configurable title capsules and JD keyword markers

Open Settings → Title signals to:

- choose the default or color-blind-friendly palette
- enter a separate custom hex color for every capsule
- toggle KM, JD language, required language, and experience years independently
- add up to five JD keywords and choose the marker style shown in the title

The keyword scan is based on the JD text already captured for an analyzed job. Saving new settings refreshes the visible LinkedIn page.

### 8. Multi-provider model support

The settings UI supports separate profiles for:

- `OpenAI`
- `Anthropic`
- `Gemini`
- `OpenRouter`
- `Poe`
- `Custom`

Each provider keeps its own:

- base URL
- API key
- active model
- saved models
- timeout
- retry settings

## Screenshots

### Current v0.6.4 workflow

The current workflow uses these verified v0.6.4 captures. Unchanged supporting workflows are labeled below; the full historical set remains available in the [visual archive](./docs/assets/archive/README.md).

![v0.6.4 LinkedIn overview with job context, selected resume, and list mode](./docs/assets/v0.6.4-overview.png)

![v0.6.4 Resume library with the current structured profile](./docs/assets/v0.6.4-resume-library.png)

![v0.6.4 LinkedIn list mode with cached results and title signals](./docs/assets/v0.6.4-list-mode.png)

![v0.6.4 Indeed list and selected job detail](./docs/assets/v0.6.4-indeed.png)

![v0.6.4 Highlights with strengths, gaps, and needs-verification checks](./docs/assets/v0.6.4-highlights.png)

![v0.6.4 Breakdown with requirement-level evidence](./docs/assets/v0.6.4-breakdown-detail.png)

![v0.6.4 Analysis preference showing Balanced and the active v10 policy](./docs/assets/v0.6.4-analysis-preference.png)

![v0.6.4 provider settings with an explicit active model and test controls](./docs/assets/v0.6.4-provider-settings.png)

### Supporting workflows retained from v0.5.0

These workflows were not changed by the v0.6.4 resume and scoring upgrade, so their earlier feature captures remain useful.

![History and saved positions](./docs/assets/archive/legacy/history-and-save.png)

![Inserted jobs from another source](./docs/assets/archive/legacy/inserted-jobs.png)

![Sponsorship-required analysis](./docs/assets/archive/legacy/sponsorship-required.png)

![Sponsorship-not-required analysis](./docs/assets/archive/legacy/sponsorship-not-required.png)

### Installation

The installation guide uses a separate, version-neutral Chrome loading reference.

![Chrome extension loading procedure screenshot](./docs/assets/chrome-procedure.png)

## Repository Structure

```text
assets/                  extension icons and static assets
data/                    IND-derived sponsor data and update script
public/                  build-time copied public files
docs/assets/             current product screenshots and archived historical visuals
docs/releases/           public release notes and development records
src/background/          service worker, cache, config, model integration
src/content/             LinkedIn/Indeed extraction and badge injection
src/prompts/             prompt templates
src/shared/              shared constants and validation helpers
src/sidepanel/           side panel UI
manifest.json            Chrome extension manifest
package.json             scripts and dependencies
setup_public.js          prepares build assets
vite.config.js           Vite build config
```

## Installation

Important:

- Do not load the project source root folder directly as the extension.
- Always load the built `dist/` folder, or use the GitHub release package and load the extracted extension folder.
- If the wrong folder is loaded, the UI may still open, but resume upload can fail because packaged parser files are missing.

### Option A: Run from source

```bash
npm install
npm run build
```

Then:

1. open `chrome://extensions/`
2. enable `Developer mode`
3. click `Load unpacked`
4. select the `dist/` folder

Reference:

![Chrome extension loading procedure screenshot](./docs/assets/chrome-procedure.png)

### Option B: Install from a GitHub release asset

1. download the release archive
2. extract it
3. open `chrome://extensions/`
4. enable `Developer mode`
5. click `Load unpacked`
6. select the extracted extension folder

Common mistake to avoid:

- GitHub source archives are not the same as the built extension package.
- If someone downloads the repository source and loads the root folder instead of `dist/`, resume parsing for `PDF` or `DOCX` files may fail.

To test the current v0.6.4 source, use the `main` branch with Option A and load its generated `dist/` folder, or download the package attached to the [v0.6.4 GitHub Release](https://github.com/YuxiaoMa66/linkedin-job-match-extension/releases/tag/v0.6.4).

### Update the existing extension without creating a second one

To keep the resume, settings, saved positions, manual jobs, and v0.1.2+ match history, update the extension in the same folder that Chrome already knows:

1. Open `chrome://extensions/`, open the existing extension's `Details`, and copy its `Location` path.
2. Back up that original folder before changing anything.
3. Prepare the update folder: use the `dist/` folder generated by `npm run build` on `main`, or extract `linkedin-job-match-v0.6.4.zip` for the latest published package.
4. Copy the contents inside the extracted package into the existing `Location`, replacing the old files. Keep the original parent folder and path unchanged; do not create a nested `dist/` folder.
5. Return to `chrome://extensions/` and click `Reload` on the existing extension card.
6. Refresh the LinkedIn or Indeed tab and reopen the side panel so the new content script is attached.

Do not click `Load unpacked` on the newly extracted folder, and do not drag it in as a separate unpacked extension. Chrome will assign that folder a separate extension ID and separate `chrome.storage.local`, which makes it look like a new plugin. If a duplicate was already loaded, remove only the duplicate card and update the original folder in place.

This release does not clear `ljm_config`, the migrated resume library, `ljm_saved_positions_v1`, `ljm_manual_jobs_v1`, or the v3 match cache. The legacy `persistentResume` entry is migrated into the resume library on first access. v0.1.2 and later analyzed results remain displayable when their resume and prompt identity still match; jobs that were never analyzed remain unanalysed. Existing cache expiry rules still apply. Chrome cannot automatically expose storage from a different extension ID, so a new folder cannot safely migrate old data by itself.

Why not drag the ZIP directly? A ZIP is only a package. Loading its extracted folder as a new unpacked extension creates a different extension ID and a separate `chrome.storage.local`; Chrome then shows an apparently empty plugin. Updating the files inside the original `Location` keeps the original extension entry and its local data.

## Configuration

After opening the side panel:

1. add a resume in `PDF`, `DOCX`, or `TXT` under `Resume library`
2. choose `Use for analysis` on the profile you want to match, or use `Re-read` after changing the parsing setup
3. go to `Settings`
4. choose a provider
5. enter the provider-specific `Base URL`
6. enter the provider-specific `API key`
7. choose an `Active model`; selecting OpenAI, Anthropic, or Gemini seeds the editable `Saved models` field with this release's fixed low-cost starter
8. edit `Saved models` or add multiple models with `Add active model` when needed
9. choose an `Analysis mode`
10. choose whether `I need employer sponsorship`
11. optionally enable `Full custom scoring`
12. open `Title signals` and choose the visible capsules
13. optionally select a color scheme, enter independent custom hex colors, enable keyword markers, and add up to five JD keywords
14. save settings

## Privacy and Data Handling

- the original PDF/DOCX file is not retained; extracted source text and the structured `resume-v1` profile are stored in local extension storage
- API keys are stored in local extension storage
- analyzed job caches may store a bounded local JD excerpt so keyword markers can be recalculated after settings changes
- model requests are only sent to the currently selected provider
- sponsorship checks use the bundled local sponsor dataset

For data attribution guidance, see [DATA_ATTRIBUTION.md](./DATA_ATTRIBUTION.md).

## License

This project is released under the [MIT License](./LICENSE).
