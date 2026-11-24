# Samuriser

**Watch a one-hour talk in about half the time.** Samuriser is an AI summariser for YouTube videos and articles. It cuts the padding and keeps the rest exactly as it was made: the original footage, in the original order, playing in YouTube's own player. It cuts like a samurai.


https://github.com/user-attachments/assets/fd0faa61-732d-496a-9883-36f521ff455e


*Sound on for narration. Talks shown: ["Tightening every bolt"](https://youtu.be/Yr5fPxZvhOw) by Daniel Stenberg, FOSDEM 2025, and ["Autonomous Testing and the Future of Software Development"](https://youtu.be/fFSPwJFXVlw) by Will Wilson, The Linux Foundation. Both CC BY. Article shown: ["Information overload"](https://en.wikipedia.org/wiki/Information_overload), Wikipedia, CC BY-SA 4.0.*

<p align="center"><img src="docs/samuriser.gif" width="384" alt="A pixel-art samurai slicing videos and documents in half as they fly towards him"></p>

A 56-minute interview plays in 24 minutes, an 18-minute talk in 9. It also tells you when something only repeats ideas you've already seen, so you can skip it altogether.

## Quick start

You need an Apple Silicon Mac, Chrome, and either a signed-in [Claude Code](https://claude.com/claude-code) or an Anthropic API key.

**1. Install the tools** (with [Homebrew](https://brew.sh)):

```sh
brew install uv node
```

**2. Start Samuriser:**

```sh
uvx --python 3.12 --from git+https://github.com/bull-island/samuriser samuriser
```

The first start takes a few minutes while it downloads. Run the same line whenever you want to use it.

**3. Open http://127.0.0.1:8765**, paste a video or article link and press **Shorten it**.

**4. Add the Chrome extension** (optional, but it's the nicest way to use it): open `chrome://extensions`, turn on **Developer mode**, choose **Load unpacked** and pick `Samuriser/extension` in your home folder.

Your library is kept in the `Samuriser` folder in your home folder. If you use an API key instead of Claude Code, put `ANTHROPIC_API_KEY=<your key>` in a file called `.env` in that folder. To get the newest version, add `--refresh` after `uvx`.

## How it works

1. You save a video or article, from the Chrome extension, the local site, or a YouTube playlist.
2. Claude reads the transcript, writes a summary and key ideas, and decides which parts teach nothing: intros, recaps, repetition, sponsor reads and filler.
3. The player jumps over those parts as you watch. Every cut is listed with its reason, so you can restore any of them or switch back to the full video.

## What you get

- **Is it worth my time?** A verdict that compares the ideas with everything you've already seen.
- **How padded is it?** A badge on each item. Padded items are cut harder than dense ones.
- **Three lengths.** Each opens with one line saying what it's about.
- **No download for YouTube.** Videos play in YouTube's own player, on YouTube itself or in the local site.
- **Articles too.** A reader shows the shortened text and can read it aloud.
- **A library.** Thumbnails, search, publish dates, progress, and a history of what you've seen.
- **On your phone.** An optional read-only copy of your library, for when the Mac is off.

## Good to know

- **It runs on your computer.** There is no hosted service, no account and no telemetry.
- **It uses your Claude plan or credit.** Each item takes a few requests.
- **It doesn't block ads.** YouTube videos play in YouTube's own player, ads included.
- **It doesn't get every cut right.** The cuts are a model's judgement. If one looks wrong, restore it or play the full video.
- **Other systems are untested.** YouTube videos with captions and articles should work, because they need no speech-to-text on your machine.

## More detail

<details>
<summary><b>Chrome extension</b></summary>

It needs the local site running.

- **Toolbar button:** adds the page you're looking at, as you see it, which helps with sites you're logged in to. It also links to your library.
- **Right-click** any video thumbnail, link or page and choose **Add to Samuriser**. It's added and checked in the background.
- **Three-dot menu on YouTube thumbnails:** has an **Add to Samuriser** item. YouTube has no supported way to extend that menu, so expect it to need fixing when YouTube changes.
- **On a YouTube video:** one line shows whether it's added and lets you shorten it. A shortened video then plays in YouTube's own player by jumping over the cuts.

After changing the extension's files, press the reload arrow on its card at `chrome://extensions`.

</details>

<details>
<summary><b>Use it on your phone</b></summary>

The site only runs on your Mac. To use your library when the Mac is off, it can publish a read-only copy to any S3-style storage, such as Cloudflare R2. The copy holds summaries, cut lists and thumbnails. It never holds video files: YouTube videos stream from YouTube, and downloaded videos stay on the Mac.

The copy has no login. Anyone with its address can read it, so use an address that is hard to guess, such as R2's public development URL, and don't share it.

Put these in the `.env` file in your `Samuriser` folder:

```sh
SAMURISER_PUBLISH_BUCKET=<bucket name>
SAMURISER_PUBLISH_ENDPOINT=https://<account id>.r2.cloudflarestorage.com
SAMURISER_PUBLISH_KEY_ID=<access key id>
SAMURISER_PUBLISH_SECRET=<secret access key>
```

An article is published as its summary and key ideas, with a link to the original. To include the full text so you can read it on your phone, add `SAMURISER_PUBLISH_ARTICLE_TEXT=1`. That puts a complete copy of someone else's writing at a public address, so only do it for your own reading and keep the address to yourself.

While the site is running it republishes after every change. Then open `<public address>/index.html` on your phone.

Search, marking things as watched and changing cuts only work on the local site.

To add videos from your phone, make an unlisted YouTube playlist and add its link to `.env`:

```sh
SAMURISER_INBOX_PLAYLIST=https://www.youtube.com/playlist?list=<id>
```

While the site is running it checks the playlist every five minutes and shortens anything new, so saving a video to that playlist in the YouTube app adds it to your library. Videos saved while the Mac is off are picked up the next time the site runs.

</details>

<details>
<summary><b>Privacy: what leaves your machine</b></summary>

Everything is stored in your `Samuriser` folder on your computer. These are the only things that leave it:

- **To the sites you save from:** requests for the page, captions and thumbnail, as any browser would make.
- **To Anthropic:** the transcript or article text, and for downloaded videos a sample of frames, so Claude can summarise and decide the cuts. Claude runs with no tools, so text inside a transcript can't make it do anything.
- **To Hugging Face:** a one-time download of the speech model, the first time something is transcribed on your Mac.
- **To your own storage:** only if you set up the phone copy described above.

The local site listens on `127.0.0.1` only, and accepts changes only from its own pages and the extension, so other websites open in your browser can't add or delete things. The extension can read YouTube pages and the local site, and nothing else unless you use its button or right-click menu on a page.

</details>

<details>
<summary><b>Other things it can do</b></summary>

- **Videos from other sites** are downloaded, because there is nowhere else to play them. That needs `ffmpeg`.
- **Videos without captions:** only the audio is downloaded, and it is transcribed on your Mac.
- **Natural reading voices:** run [Kokoro](https://github.com/remsky/Kokoro-FastAPI) on `127.0.0.1:8880`. Without it, the reader uses the browser's voices.
- **A shortened video file,** with the timer and progress bars burned in, from a copy of the code: `uv run shorten <link> --ratio 0.3`.

</details>

<details>
<summary><b>Develop</b></summary>

```sh
git clone https://github.com/bull-island/samuriser.git
cd samuriser
uv sync
uv run samuriser
```

Run from the code, it uses the `extension` folder there, and keeps the library in a `runs` folder there if one exists.

```sh
uv run pytest
uv run ruff check .
uv run ruff format .
uv run mypy .
```

</details>

## Use and licence

This is a personal tool for getting through things you would otherwise watch or read in full. It is released under the [MIT licence](LICENSE).

Samuriser is not affiliated with or endorsed by YouTube, Google or Anthropic.

It reads videos and pages through [yt-dlp](https://github.com/yt-dlp/yt-dlp), which some sites' terms of service don't allow. You are responsible for how you use it: follow the terms of the sites you use it with, and don't share downloaded videos or copies of other people's work.
