# VEXO

**ComfyUI to every art site, on autopilot.** Batch-post your images to Pixiv, DeviantArt, Civitai, X and SubscribeStar from one local app.

![VEXO](docs/screenshots/0-cover.png)

- Reads the prompt, model, LoRAs and seed straight from your ComfyUI / A1111 PNGs
- Edit title, tags and description for 1 or 50 images at once, with per-site overrides
- Auto-tags known characters (English or Japanese tags) and writes titles that fit each site
- Queue and schedule posts, one multi-image post or one post per image
- Warns you before posting characters that are minors in canon to DeviantArt or as R-18
- Posts through your own logged-in browser session: no API keys, no passwords stored, everything stays on your PC

## Install

1. Windows 10/11 with Microsoft Edge, and [Node.js](https://nodejs.org) 22.13 or newer.
2. [Download the zip](../../archive/refs/heads/main.zip) (or `git clone`), unzip anywhere.
3. Double-click `Start.bat`. The first launch installs dependencies, then VEXO opens at http://127.0.0.1:3210.

New here? Read the **[quick start](docs/quick-start.md)**.

| Library | Publish | Characters |
|---|---|---|
| ![](docs/screenshots/1-library.png) | ![](docs/screenshots/3-publish.png) | ![](docs/screenshots/4-characters.png) |

## Run
| Action | How |
|---|---|
| Start | double-click `Start.bat` → opens http://127.0.0.1:3210 |
| Stop | close the black window |
| Dev (hot reload) | `npm run dev` → http://localhost:5173 |

## Shortcuts
| Key | Effect |
|---|---|
| Click | select an image |
| Ctrl + click | add / remove from selection |
| Shift + click | select a range |
| Ctrl + A | select all (current filter) |
| Esc | deselect |
| Ctrl + Enter | apply changes |

## Auto-tag characters
1. **Characters** → type a name in the search box (e.g. `kohaku`) → pick the Danbooru tag. The Japanese name, the Pixiv-style tag and the series are filled in automatically. Edit if needed → *Add to list*.
2. Characters are detected in the **ComfyUI prompt** (the Danbooru tag, e.g. `kohaku_(dr._stone)`) and in **LoRA file names** (e.g. `kohaku`). Add your own triggers per character.
3. Detection runs **on import**, and with the **Auto-tag** button (Library toolbar, inspector, or *Auto-tag library* on the Characters page).
4. **Settings → Auto-tag**: tag language (English / 日本語), series tag, Pixiv-style tag `コハク(Dr.STONE)`, auto-title. Change the language and re-run Auto-tag: the tags are swapped, your other tags are kept.
   - Auto-titles follow the prompt order (main character first). When one is too long for a platform (Pixiv 32, DeviantArt 50), that platform gets its own short version: `Ishigami Senkuu & Kohaku & Chrome / Dr. Stone` → Pixiv `Ishigami Senkuu +2`. A title you typed yourself is never changed.
5. Inspector → *Detected characters*: ✗ removes a character's tags from that image.

Only images that still carry their ComfyUI / A1111 metadata (PNG straight out of ComfyUI) can be detected.

## DeviantArt age check 🔺
DeviantArt bans sexual or suggestive art of characters who are **minors in canon or look like minors** — stating they are 18+ / "aged up" does not count.
- When a character is added, VEXO fetches its **canon age from AniList** and how often it is **drawn as a child on Danbooru** (% of posts tagged `loli`).
- 🔺 red = canon age under 18 at some point, or ≥ 10 % `loli` · 🟠 orange = 3–10 % `loli` · ❔ = no age found (check it yourself).
- Shown in **Characters** (column + "N risky" counter + detail box), on the inspector's detected-character chips, and in the **Publish** dialog: sending a flagged character to DeviantArt needs a ticked "I understand the risk" box (stronger warning when R-18).
- Wrong age? Type it in the character's box (marked "typed by you"). *Re-check ages* refreshes everything (manual ages are kept).

## Tag presets
- **Presets** page: create / edit / delete sets of tags (*From selection* takes the tags of the selected images). *Add* / *−* apply a set to every image selected in the Library.
- **Inspector → Tag sets**: one click adds the set to all selected images; when they all have it (red chip), a click removes it. Dashed chip = only some images have it.

## Publish
1. **Platforms** → *Log in* (Pixiv, DeviantArt, Civitai, X, SubscribeStar): an Edge window opens, log in, it closes by itself.
2. **Library** → select → *Publish* → platform, 1 multi-image post or 1 post per image, now or scheduled, visibility.
3. **Queue**: posts go out one by one, spaced by the delay set in Settings (10 min by default).
4. **History**: link to each post, log on failure, *Retry*.

DeviantArt: pick the gallery folder (or Scraps) in the Publish dialog; up to 10 images per deviation; R-18 images are posted as **Mature** (explicit sexual content is not allowed on DeviantArt); "Created using AI tools" and "noai" are on by default (Settings).

| Site | Notes |
|---|---|
| Civitai | Posted through **civitai.red** (same account; since April 2026 civitai.com is SFW-only). SFW images also show on civitai.com, R-18 only on .red. Prompt, seed, sampler, model and LoRAs are sent with each image (required for R-18). Up to 20 images per post. |
| X | VEXO fills in X's own post form (no API keys). Text = title + description + #tags (≤ 280). R-18 images are marked as sensitive. Up to 4 images. |
| SubscribeStar | **subscribestar.adult**. Title in bold on the first line, then the description; tags as SubscribeStar tags. Choose *Public* or one or more tiers in the Publish dialog (remembered). Up to 20 images. |

The age warning (🔺) also blocks R-18 posts of flagged characters on Civitai, X and SubscribeStar until you tick "I understand the risk".

An Edge window opens while posting (Pixiv blocks invisible mode); you can move it off-screen in Settings.

## Data
Everything lives in `data/` (SQLite DB, originals, thumbnails, Edge profile). Delete the folder = start from scratch. Only `data/originals` and `data/thumbs` are served over HTTP.

See `SPEC.md` for decisions and steps.

## Disclaimer

VEXO is an unofficial tool, not affiliated with Pixiv, DeviantArt, Civitai, X or SubscribeStar. It uses the same upload steps as their websites; when a site changes them, the matching adapter breaks until it is updated. You are responsible for following each site's rules.

## License

[MIT](LICENSE)
