# freetime

Got free time? freetime picks the best thing to do with it: a game from your Steam library,
a YouTube video that fits the time you have, a sport that suits the weather, or something new
(learn, create, chill, cook, see friends).

Tell it how much time you have, your energy, who's with you, whether you'll go outside and your
budget. It ranks ideas from every source, explains why, and learns from your 👍 / 👎.

**Download for Windows:** <https://osmvision.github.io/freetime/> (or the
[latest release](https://github.com/osmvision/freetime/releases/latest)) ·
[Privacy policy](docs/privacy.md) · [Code signing policy](docs/code-signing.md)

## Desktop app (Tauri)

```sh
cargo run -p freetime-desktop          # build and open the app
```

For live reload while editing the UI (`desktop/ui/`), use the Tauri CLI:

```sh
cd desktop
npm install
npm run dev        # tauri dev
npm run build      # installer in target/release/bundle
```

## Terminal app

```sh
cargo run                              # asks a few questions
cargo run -- -m 45 -e high --quick     # flags, no questions
cargo run -- surprise                  # one pick, no questions
cargo run -- setup                     # city, interests, Steam import, YouTube
cargo run -- history
```

## What it uses, and when

Nothing is required: the first launch works with built-in ideas, the Steam store's top sellers and
deals, and new uploads from a set of YouTube channels.

| Source | What you get | When it's read |
| --- | --- | --- |
| Windows region | Steam prices in your currency | At startup, from the regional settings (no network) |
| City | Outdoor ideas follow the live weather ([Open-Meteo](https://open-meteo.com/), no key) | Asked once on first launch (skippable), editable in Settings |
| Places nearby | Parks, pools, courts, libraries... near your city for ideas that happen somewhere ([OpenStreetMap](https://www.openstreetmap.org/copyright) through Overpass, no key) | Only when you click **Nearby** on an idea, then cached for a month |
| Your own ideas | Ideas you add in Settings, ranked with the built-in ones | Stored with your settings, never sent |
| Steam games | Backlog, old favorites and comfort picks from games you own | Only when you click **Import my games from Steam on this PC**, then from freetime's own cache |
| YouTube channels | New uploads, per idea category (`youtube_channels.toml`, editable) | At startup, public RSS feeds, cached 2 h |
| YouTube search | Videos matching your interests and your free time | At startup, through freetime's search proxy (no key), refreshed daily |
| `YOUTUBE_API_KEY` | The same search, straight to YouTube on your own quota | At startup, if set |
| `STEAM_API_KEY` | Every game on your account, with playtime | Only during an import |

**Network at startup:** the Open-Meteo forecast (if a city is set), the Steam store lists and prices
(with your region's `cc`), and the YouTube feeds. All run in the background with a 5 s timeout.
Nothing looks up your IP address.

**The Steam import** reads only the `SteamPath` registry value, the folder names under
`<Steam>\userdata\` (account IDs), `steamapps\libraryfolders.vdf`, each library's
`appmanifest_*.acf` and `userdata\<id>\config\localconfig.vdf` (playtime only). Nothing in
`<Steam>\config\` and no `ssfn*` file is ever opened: every read goes through an allow-list
(`core/src/providers/steam_import.rs`, tested). You can also paste a SteamID64 or a
`steamcommunity.com/profiles/…` URL.

**Keys** are read at runtime from the environment, the workspace `.env` or
`%APPDATA%\freetime\.env` (where keys typed in Settings go). Copy `.env.example` to `.env` to start.
They are never compiled in, unless you build with `--features freetime-core/embed-keys` for a
personal copy that never leaves your PC.

## Layout

```
core/      shared logic: ideas catalog, scoring, history, Steam, YouTube, weather, region
  data/youtube_channels.toml   default channels per idea category
  data/activities.toml   built-in ideas, add your own
cli/       terminal app
desktop/   Tauri app
  src/commands.rs        commands the UI calls
  ui/                    HTML, CSS and JS (no build step)
```

## Building on Windows

The Rust toolchain used here is `stable-x86_64-pc-windows-gnu` with MinGW-w64 (WinLibs) on the PATH,
so no Visual Studio install is needed.

With the GNU toolchain, MinGW's `windres` (which embeds the app icon) breaks when the project path
contains spaces. If yours does, copy `.cargo/config.toml.example` to `.cargo/config.toml` and set a
build folder without spaces. That file is personal and ignored by git. With the MSVC toolchain, or a
path without spaces, nothing is needed.

## Contributing

Bugs go in [issues](https://github.com/osmvision/freetime/issues), ideas and questions in
[Discussions](https://github.com/osmvision/freetime/discussions). Before a pull request, see
[CONTRIBUTING.md](CONTRIBUTING.md); everyone follows the [Code of Conduct](CODE_OF_CONDUCT.md).
Security problems are reported privately ([SECURITY.md](SECURITY.md)), and accessibility
barriers are bugs ([ACCESSIBILITY.md](ACCESSIBILITY.md)).

## License

The code is under the [MIT License](LICENSE), © 2026 osmvision and Julien-13. The photos, fonts and
icons bundled with the app, and the data it fetches, keep their own licences: see
[THIRD-PARTY.md](THIRD-PARTY.md). The licence covers the code, not the name "freetime".

## Code signing policy

Free code signing provided by [SignPath.io](https://about.signpath.io/), certificate by
[SignPath Foundation](https://signpath.org/) (application in progress: releases are not signed yet).

- Committers and reviewers: [osmvision](https://github.com/osmvision), [Julien-13](https://github.com/Julien-13)
- Approvers: [osmvision](https://github.com/osmvision)
- Privacy policy: [docs/privacy.md](docs/privacy.md)

The full policy, covering how releases are built, approved and signed, is in [docs/code-signing.md](docs/code-signing.md).
