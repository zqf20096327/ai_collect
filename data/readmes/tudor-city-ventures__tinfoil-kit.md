<img src="site/public/icon.svg" width="72" alt="">

# Tinfoil Kit

An offline kit for when the internet goes down. One folder, on your computer or an external SSD, holds:

- **Local AI** (llama.cpp) that answers from the library and cites its sources.
- **An offline library** (Kiwix): Wikipedia, medical references, repair guides, preparedness manuals.
- **Offline maps** with address search, driving and walking directions, and "nearest hospital".

Open the kit's folder, `TinfoilKit` (on your computer, or on the drive it's on), double-click `Open Tinfoil Kit.command` (`Open Tinfoil Kit for Windows.bat` on Windows), and a browser page opens with Ask, Map and Library tabs, and Notes, Share with family, Print the essentials, AI chat and Help under More. No internet, account or install needed.

![The Ask tab: a question about making water safe with bleach, the Ask the AI and Search buttons, the AI's answer with numbered citations, and the three library articles it came from](docs/ask.png)

## How it works

The whole kit is one folder, with three inside: `app` (the kit's code, as released), `downloads` (everything it downloads) and `data` (your settings, notes and pins, and the kit's records). Beside them are a launcher for each kind of computer and `Read me first.txt`, which says what to open. A new version replaces `app` and leaves the other two as they are. Put the kit on an external drive to grab and go, or on your computer's own disk. While you're online, SETUP fills it. When the internet is down, Open Tinfoil Kit starts a few servers from it on your computer, and your browser talks to them. Nothing goes over the internet. Each is a file you double-click: `SETUP.command` and `Open Tinfoil Kit.command` on a Mac or Linux, `SETUP-Windows.bat` and `Open Tinfoil Kit for Windows.bat` on Windows.

![How it works: online, SETUP fills the kit folder (app, downloads, data) from Tinfoil Kit releases and the publishers' downloads. Offline, Open Tinfoil Kit starts the servers (AI, library, maps, notes and pins) for the kit page in your browser, and for phones and laptops at home when sharing is on](docs/how-it-works.svg)

### Setting up (online)

The first time, SETUP asks a few questions:

- **Where you live** (a US state or a country), and any places nearby. That sets the maps' area, directions, address search and home, and Wikipedia's language (`./kit region`, from the places in `tools/regions.json`). Places nearby get street detail and directions too.
- **How much of Wikipedia:** all of it, or just the best 50,000 articles (`./kit region --wikipedia-size`).
- **Where the kit goes:** an external drive (`<drive>/TinfoilKit`) or this computer (`~/TinfoilKit`, where it leaves 50 GB free; on a Mac, its downloads stay out of Time Machine). SETUP says which AI model the computer can run (`./kit fit`), lists the drives with their format (`./kit drives`), and checks that the kit fits with 10% of the computer's disk, or 5% of a drive, left free (`./kit space`). When it won't, it offers just the essentials (`./kit essentials on`: the AI, the medical, preparedness and repair books, the map, and Wikipedia's best articles as text). `./kit place` moves the kit there.

Then it times the connection for a few seconds and says how long the kit to try and all of it take to download. It gets the kit to try (`./kit starter on`: this computer's programs, a small AI, a few small books and the area's map, about 10 GB), checks it, opens it, and says how long the rest takes at the speed that download measured. Running SETUP again gets the rest: it asks what goes in the kit (`./kit pick --ask`, the website builder's choices) unless that was chosen already, then `./kit starter off`. Once the full kit checks out, the try-it files nobody picked go.

Every run of SETUP, the first included, comes down to three `./kit` commands:

1. **Update** (`./kit update`): installs the newest Tinfoil Kit release from GitHub into the app folder. Your `kit.json` (in `data`) keeps your changes and takes in the new version's. It installs only a release signed with the maintainer's key, and shows what's new and asks first.
2. **Download** (`./kit sync`): asks each publisher for the newest version of everything listed in `kit.json` and downloads only what changed, into `downloads`. Programs are the exception: each version of the kit names the exact build of each one it installs (`tools/pins.json`), so a new AI engine arrives with a kit update. A big book can wait for its next edition: Wikipedia (127 GB in English) keeps the one it has until it's a year old (`refresh_days` in kit.json). A big file comes over eight connections at once, which is often several times faster than one, downloads resume after a break, and the time left shows as they go. A file the kit already has is never downloaded again, even one an older version kept under another name. Every file with a published checksum is checked against it, and an old version is deleted only after the new one checks out.
3. **Check** (`./kit test`): starts every server offline and checks that each one answers.

A newer download of the kit doesn't start over: its SETUP finds a kit set up before, in the home folder or on a drive (`./kit kits`), and updates that one, so nothing it has downloads again. A kit whose app folder was deleted gets the download's.

Nothing needs installing first. The kit's own program (`tools/tinfoilkit-*`, one for each computer, built from the Go source in `tools/tinfoilkit/`) runs `./kit`, SETUP's steps and the servers, and only needs curl, which Macs and Windows come with. Every download of the kit carries it. A git checkout or GitHub's Download ZIP has none until `tools/tinfoilkit/build.sh` builds it, which needs Go; with Go installed, `./kit` builds it by itself.

### Using it (offline)

`Open Tinfoil Kit.command` (`Open Tinfoil Kit for Windows.bat` on Windows) runs `./kit open`, which starts these servers on your computer and opens the kit page at http://127.0.0.1:8888. It picks an AI model that fits the computer's memory. Every server listens only on 127.0.0.1, so nothing else on the network can reach them. (When the computer's loopback has a second address, kiwix-serve can't see 127.0.0.1: the library then listens on ::1, the other loopback address, and the launcher forwards 127.0.0.1 to it.) Sharing, off by default, adds one more on the network.

| Part | Program | Port | What it does |
| --- | --- | --- | --- |
| AI | `llama-server` (llama.cpp) | 8080 | Runs the AI model (Inkling 2 Mini by default). AI chat is its built-in chat page |
| Library | `kiwix-serve` (Kiwix) | 8888 | Serves the books (`.zim` files: Wikipedia, medical, repair, preparedness) with full-text search, and the kit page |
| Map | `pmtiles` | 8090 | Serves the map: street detail where you live (a US state, a country, or part of a big one) and a low-detail world |
| Addresses | Photon | 2322 | Finds addresses, places and the nearest hospital or pharmacy (the whole US by default) |
| Directions | GraphHopper | 8989 | Plans driving and walking routes in your region |
| Notes and pins | the kit's program | 8095 | Keeps Notes and the map's home and pins in `data`, so a new version keeps them and every browser on the kit sees the same ones |
| Sharing (off by default) | the kit's program | 8000 | Lets phones and laptops on your home network in once they type the access code, and passes their requests to the servers above. Share with family on the kit page turns it on and off, as does `./kit share on` (`.\kit.cmd share on` on Windows); `--share` for one run |

Photon and GraphHopper run on a Java that's in the kit. The kit has each program for Macs, Windows PCs and Linux PCs, so a drive set up on one starts on all three.

The kit page (`tools/portal.html`) is one HTML file with no build step. Each sync builds a copy with the map's code, fonts and icons inside, so the page needs nothing from the internet.

- **Ask:** two buttons. **Ask the AI**: the AI turns your question into short searches, `kiwix-serve` searches every book, and the AI answers from the top articles with numbered sources. **Search** skips the AI: the question's own words over the same indexes, and the best passages in seconds, on very little power; then **Have the AI answer from these** can turn them into an answer with no second search. With the AI off, Ask the AI shows the passages too. Map questions ("nearest pharmacy", "directions to the hospital") skip the library: the AI gets three map tools (search places, find nearby, get directions), and the answer shows on the Map tab.
- **Map:** MapLibre draws the map from `pmtiles`. Its search, directions and "nearest" buttons ask Photon and GraphHopper. Home and pins are saved in the kit (`data/places.json`).
- **Notes:** what the AI should know about your household (allergies, medicines, who to call, where to meet), in `data/notes.txt`, a plain text file. The AI reads them with every question on Ask, map questions included.
- **Print the essentials:** the few pages of the kit's books worth having on paper, most important first (making water safe, first aid, dehydration, power outages), each opening at the first page to print, and a page of the household's own (home and pins with their coordinates, the notes, and the nearest hospitals and pharmacies) that prints alone.

### What's in the folder

```text
TinfoilKit/
├── Open Tinfoil Kit.command      start the kit offline (Mac, Linux; the .bat on Windows)
├── Open Tinfoil Kit for Windows.bat
├── Read me first.txt             what to open, and what each folder is for
├── app/                          the kit's code, as released: a new version replaces it
│   ├── SETUP.command             set up, or update whenever you like (online; Mac, Linux)
│   ├── Open Tinfoil Kit.command  what the two at the top start (Mac, Linux)
│   ├── UNINSTALL.command         remove the kit and everything it downloaded (Mac, Linux)
│   ├── SETUP-Windows.bat         the same three, for Windows
│   ├── Open Tinfoil Kit for Windows.bat
│   ├── UNINSTALL-Windows.bat
│   ├── GUIDE.md                  the printable guide
│   ├── .claude/skills/           how-tos for AI agents: set up, update, change, check, share, remove
│   ├── kit, kit.cmd              the kit's command line (kit.cmd on Windows)
│   └── kit.json, tools/          the standard list of downloads, and the code
├── downloads/                    everything the kit downloads
│   ├── bin/                      programs: llama.cpp, Kiwix, Java, the map servers
│   ├── models/                   AI models
│   ├── library/                  books (.zim files)
│   ├── maps/                     map tiles, address database, road network
│   └── INVENTORY.md              what's installed, with versions and sizes
└── data/                         yours: no new version touches it
    ├── kit.json                  what goes in your kit, and its settings
    ├── notes.txt                 Notes on the kit page: what the AI should know about your household
    ├── places.json               the map's home and pins
    ├── logs/                     what each sync and launch did
    └── .kit/                     download progress, caches, the built kit page, the access code
```

Delete `app` any time and put a new version's app folder in its place: `downloads` and `data` stay as they are, and nothing downloads again. `data/kit.json` starts as a copy of `app/kit.json`, and when a new version's list differs, its changes go into yours and your own choices stay. A kit set up before these three folders moves into them by itself the first time a newer version runs (`./kit layout`, which SETUP runs), by renaming, so nothing downloads again. SETUP and UNINSTALL never move or delete a folder that holds other things besides the kit: an app folder put on the Desktop on its own stays where it is, and they say so.

The repo is the app folder, so `site/` (the website), `tests/` and `docs/` come along, but the kit doesn't use them. A git checkout keeps `downloads/` and `data/` inside it (git ignores them).

## Requirements

- A modern laptop or desktop: a Mac with Apple Silicon, or a Windows or Linux PC (x64). Windows and Linux are experimental for now: they're tested less than the Mac, so expect rough edges. Built around 32 GB of memory; the small model runs on 8-16 GB.
- Room for the kit: from about 20 GB for just the essentials to about 900 GB for everything, and 200 to 300 GB for the recommended kit, depending on the AI models the computer runs and the map. On the computer's own disk it leaves 50 GB free. An external SSD lets you grab it and go.

A nightly test sets the kit up on a Mac and on Windows, from a download onto the computer and onto an exFAT drive, and starts the Mac's drive on Windows and Linux. On Windows it also builds and serves a small real map, and on all three it shares the kit as a home server.

## Set up

Your AI sets it up: copy the prompt on [tinfoilkit.com](https://tinfoilkit.com) into ChatGPT, Claude or any AI chat. It asks what you want in the kit, then gives you one command to paste into Terminal (PowerShell on Windows). Or write the command yourself:

```sh
# Mac or Linux, in Terminal
mkdir -p ~/Downloads && cd ~/Downloads && curl -fsSL https://github.com/tudor-city-ventures/tinfoil-kit/releases/latest/download/TinfoilKit.tar.gz | tar -xz && bash TinfoilKit/app/SETUP.command --region texas --drive /Volumes/Kit --yes
```

```powershell
# Windows, in PowerShell
cd ~\Downloads; curl.exe -fsSL -o TinfoilKit.zip https://github.com/tudor-city-ventures/tinfoil-kit/releases/latest/download/TinfoilKit-Windows.zip; tar -xf TinfoilKit.zip; Remove-Item TinfoilKit.zip; .\TinfoilKit\app\SETUP-Windows.bat --region texas --drive E: --yes
```

It downloads the kit from the [latest release](https://github.com/tudor-city-ventures/tinfoil-kit/releases/latest) and runs SETUP, which moves it to the drive (or `--this-computer`), says how long the downloads take on your connection, then gets a small kit to try (about 10 GB), tests it and opens it. When you're ready for the rest, run `bash /Volumes/Kit/TinfoilKit/app/SETUP.command --yes` (`E:\TinfoilKit\app\SETUP-Windows.bat --yes` on Windows): it says how long that takes, gets it and tests again. `--help` lists the options, one for each setting of the website's kit builder: a preset (`--recommended`, `--essentials`, `--everything`), where you live, how much of Wikipedia, which AI models and books, a drive or this computer, sharing on the home network. Without `--yes`, SETUP asks whatever the options didn't answer. [llms.txt](site/public/llms.txt) has them all, and what to check first.

Or from a git checkout, on a Mac or Linux:

```sh
git clone https://github.com/tudor-city-ventures/tinfoil-kit ~/TinfoilKit    # or /Volumes/<drive>/TinfoilKit
cd ~/TinfoilKit
tools/tinfoilkit/build.sh    # the kit's own program, from its Go source (needs Go: https://go.dev/dl)
./kit plan    # preview what will download, and how long it takes
./kit sync    # download everything (hours)
./kit test    # start every server offline and check it answers
```

Then turn Wi-Fi off and double-click `Open Tinfoil Kit.command` in the kit's folder (`Open Tinfoil Kit for Windows.bat` on Windows). [GUIDE.md](GUIDE.md) is the printable guide that lives in the app folder.

## Update

Double-click SETUP again whenever you want the newest models, books and maps, or run `./kit update`, `./kit sync` and then `./kit test`. There's no schedule. It installs the kit's newest version first, so models and sources added to the kit since then arrive too, and then downloads only what changed (see [How it works](#how-it-works)). If an update is cut off, the kit keeps working with what it has.

Or replace the app folder yourself: delete it, put a new download's app folder in its place and run its SETUP. Or run a new download's SETUP from wherever you unzipped it: it finds your kit, puts its own app folder there and carries on. Either way `downloads` and `data` stay as they are.

## Remove

Double-click `UNINSTALL.command` (`UNINSTALL-Windows.bat` on Windows) in the kit's app folder. It says what it will delete and how much space that frees, and deletes the kit and everything it downloaded only after you type `delete`. On a drive, nothing else is touched. `--yes` skips the question.

## Home server

Experimental for now. A computer that stays on (Linux, a Mac mini or a Windows PC) can serve the kit to every phone and laptop at home. `bash SETUP.command --home-server` (`.\SETUP-Windows.bat --home-server` on Windows) sets it up as usual, then shares it on the home network behind an access code and starts it with the computer (a systemd user service on Linux, from boot; a LaunchAgent on a Mac or the Startup folder on Windows, once you log in). Phones open the address it shows and type the code, scan its QR code, or open the link that Share with family, on the kit page, copies in a message to text them. Programs can use the code as an API key for the AI's OpenAI-compatible API: `Authorization: Bearer <code>` at `http://<server>:8000/ai/v1`. Details: [GUIDE.md](GUIDE.md#a-home-server-advanced).

## Security

The kit downloads programs and runs them on your computer, so here is what protects you and what doesn't. Report problems privately, as [SECURITY.md](.github/SECURITY.md) says.

- **Signed updates.** `./kit update` installs new code only if the maintainer's release key signed it, checked against `tools/release-signers` in the copy you already have. That key never goes near GitHub, so someone who broke into the GitHub account or its Actions still couldn't ship an update your kit accepts. A new key arrives only in a release the old one signed, and the kit shows what's new and asks before it installs anything.
- **Downloads straight from their publishers,** over HTTPS (the list is in [THIRD-PARTY.md](THIRD-PARTY.md)). This project hosts none of them. Each release names the exact build of every program it installs, with that file's SHA-256, in `tools/pins.json`, signed with the rest: a program file that changes after the release is refused. Books, models and map data are checked against the checksum their publisher posts, before they replace the old version. Files without one, like the map tiles and fonts, rely on HTTPS alone.
- **No telemetry.** No accounts, analytics or reports home, in the kit or on tinfoilkit.com. The kit goes online only when you run SETUP, `./kit sync` or `./kit update`, and then only to GitHub and the places it downloads from.
- **No administrator password.** The kit runs as you, and starts only when you start it unless you set up a home server. UNINSTALL undoes everything setup did. The site's "What does setup change on my computer?" lists every change outside the kit folder.
- **Servers on 127.0.0.1.** The AI, library and maps answer only this computer. A website open while the kit runs can still reach them, as browsers allow: it could read the books and maps and use the AI as the kit page does (the directions server answers any page, and DNS rebinding opens the rest). Chrome asks your permission before a website reaches your computer's own servers; other browsers may not.
- **Sharing is off until you turn it on.** Then one gate, on port 8000 by default, stands in front of everything: it asks for an 8-digit code, stops answering a device after 10 wrong tries in 10 minutes, and refuses addresses and names outside a home network, so other websites can't reach it. It's plain HTTP, so share on your own Wi-Fi or hotspot: anyone on a public network who watches the traffic could read the code.
- **Readable code.** Go's standard library, shell scripts and one HTML page, with no packages to install. The one built file is the kit's own program (`tools/tinfoilkit-*`, from the Go source in `tools/tinfoilkit/`), and the same source builds the same bytes on any computer, so you can check that it's the code you read (below). It's written with AI coding tools; the tests in `tests/` run it against mocks of every download source and server on every change.
- **The repo.** Every GitHub Action is pinned to a commit and runs with a read-only token, except a few jobs that never run code from a pull request or a download. An outside pull request that touches the workflows, CODEOWNERS, the release key or the program pins fails a check that only the maintainer can merge past.
- **What it can't protect against:** a bad file from a hacked publisher, if it's a book, model or map (its checksum comes from the same place as the file) or a program that was already bad when a release pinned it; someone with your unlocked computer or drive, since the kit isn't encrypted (use FileVault, BitLocker or an encrypted drive for that); and an AI answer that's wrong, so check its sources.

To check a release before running it, download its `tinfoilkit-TAG.tar.gz` and `.sig` (the downloads the setup command gets are protected by HTTPS alone; the release's `SHA256SUMS`, signed the same way, lists them all) and run:

```sh
ssh-keygen -Y verify -f tools/release-signers -I tinfoilkit-release -n tinfoilkit-release \
  -s tinfoilkit-TAG.tar.gz.sig < tinfoilkit-TAG.tar.gz
# and that it's exactly the tagged code, with the kit's own program built from it, from a clone of this repo
# (it needs Go: brew install go, or go.dev/dl):
tools/tinfoilkit/build.sh archive tar tinfoilkit-TAG TAG | shasum -a 256
gunzip -c tinfoilkit-TAG.tar.gz | shasum -a 256
```

To check the program in a kit you already have, run `tools/tinfoilkit/build.sh verify` in its app folder, with Go installed. It builds the program again from the source beside it and compares the result with the copies in `tools/`. The Mac app's copy also carries Apple's signature, which macOS needs to open it, so for that one it compares everything but the signature. Add the release's `SHA256SUMS` (`build.sh verify SHA256SUMS`) to compare with that list too. Releases are built the same way: CI builds the program from the commit, the maintainer's Mac builds it again, and the release is published only if the two builds match.

## Customize

Everything the kit keeps is listed in `data/kit.json`, your copy of the standard list ([kit.json](kit.json)). Set `"enabled": false` to skip an item, or find more books with `./kit search WORDS`.

## Contributing

Bug reports and ideas are welcome as issues. A pull request needs an issue the maintainer has labeled `accepted` first: see [CONTRIBUTING](.github/CONTRIBUTING.md). Code rules, for people and their AI agents, are in [AGENTS.md](AGENTS.md). How it works inside, and why, is in [docs/DESIGN.md](docs/DESIGN.md).

## Built on

Tinfoil Kit is glue around free projects that do the work. If the kit helps you, give to them: [Kiwix](https://support.kiwix.org/), [Wikipedia](https://donate.wikimedia.org/), [OpenStreetMap](https://supporting.openstreetmap.org/), [Protomaps](https://github.com/sponsors/protomaps) and [MapLibre](https://opencollective.com/maplibre). [llama.cpp](https://github.com/ggml-org/llama.cpp) runs the AI, and [GraphHopper](https://github.com/graphhopper/graphhopper) and [Photon](https://github.com/komoot/photon) plan routes and find addresses: a star or a good bug report helps them.

## License

The kit's code is [MIT](LICENSE). Everything it downloads (models, books, maps, programs) comes from its publisher under its own license: see [THIRD-PARTY.md](THIRD-PARTY.md). Some of it forbids commercial use, so don't sell drives filled with the kit.
