# Photo Sorter, with Claude

**Back from a trip with 2,000 photos and no idea what's in there? Point Claude at the folder and watch every photo fly into its own folder.** Selfies, food, travel, screenshots, videos and duplicates, sorted on your own laptop in minutes.

![Photos flying out of the sphere into their folders](docs/preview.gif)

<sub>Recorded from the built-in demo, which uses drawn placeholder images, not real photos.</sub>

- **Sorts photos and videos** into folders like Selfies, People & family, Food & drinks, Travel & nature, Screenshots and Travel clips. Use the standard folders or make your own.
- **Finds duplicates**: identical copies, burst shots and re-saved screenshots go to a `_Review` folder, with a list of which copy was kept.
- **Never touches your originals.** It only reads them and makes sorted copies. On a Mac the copies take no extra space.
- **Private**: runs on your computer. Your photos are not uploaded anywhere.
- **No API key**: it uses the Claude plan you already have.

## Start here (no coding, no terminal)

You need a Mac (Windows and Linux work too) and a Claude Pro or Max plan.

1. Open the **Claude** desktop app and go to the **Code** tab. (Or [Claude Code](https://claude.com/claude-code) in a terminal.)
2. Paste this and press Enter:

   ```
   Install and run https://github.com/sukralia/claude-photo-sorter
   ```

3. Claude downloads it, sets it up and opens the dashboard in your browser. Then:
   - Click **Choose folder** and pick your trip photos.
   - Press **Start sorting**.

That's it. About 30 seconds to a few minutes for 1,000 photos, depending on your Mac. Sorted copies appear next to your photos in a folder called `<your folder> (sorted)`.

<details>
<summary>Photos still on your phone?</summary>

- **iPhone / Apple Photos:** in Photos on your Mac, select the photos, then File > Export > Export Unmodified Originals, into a new folder.
- **Android:** connect the phone by USB and copy `DCIM/Camera` to your computer.
- **Google Photos:** go to [takeout.google.com](https://takeout.google.com), select only Google Photos, download, and unzip everything into one folder.
</details>

## Just want to see it first?

After installing, ask Claude: **"open the photo sorter demo"**. It plays the whole sorting animation on a fake camera roll, no photos of yours needed.

## Opening it again

- Double-click **Open Photo Sorter** in the `claude-photo-sorter` folder (in your home folder), or
- just tell Claude **"open my photo sorter"**.

It opens in your browser and keeps running in the background until you restart your computer.

## What you can do in the dashboard

- **Start sorting**: scans, finds duplicates, lets Claude look at every photo, and builds the folders, with live progress.
- **Click a folder**: browse everything in it, open any photo full size, and **Move to** another folder if Claude got one wrong.
- **Edit folders**: rename folders, add your own (Beaches, Kids, Temples...), and describe what goes in each.
- **Sort with Claude** (after sorting): replays the whole animation. Perfect for a screen recording.
- **Advanced**: try 200 photos first before doing everything.
- **New sort**: sort another folder.
- **☾**: dark mode.

## How it works

1. **Scan**: makes a small preview and a fingerprint of every file. Originals are only read.
2. **Duplicates**: compares fingerprints, with an extra pixel check for screenshots so similar app screens aren't mistaken for copies.
3. **Claude looks**: runs Claude Code in the background (`claude -p`), four at a time, each looking at contact sheets of about 90 previews and choosing a folder for each.
4. **Folders**: copies every file into its folder (duplicates into `_Review/duplicates`) and writes `sorted.csv` and `duplicates.csv`.

It checks your Claude sign-in before starting, and if your plan's usage limit is reached it stops cleanly and carries on later where it left off.

## Privacy

- The dashboard only listens on `127.0.0.1`, so nothing else on your network can reach it.
- Previews, labels and the file list stay in `dashboard/data/` and `work/`, which are never committed.
- Small previews are read by Claude Code, the same as anything else you share with it. Your originals never leave your computer.

## Running it by hand

```bash
./setup.sh                 # once: checks Python, installs 3 small packages into .venv/
./start.sh                 # opens the dashboard in your browser
./start.sh --background    # same, but keeps running after the terminal closes
./start.sh --demo          # the demo camera roll
```

Every step is also a script in `scripts/` (`scan.py`, `dupes.py`, `label_claude.py`, `apply.py`). Agents read `CLAUDE.md` for the full playbook. Needs Python 3.9+, and ffmpeg for video previews (`brew install ffmpeg`, optional).

## Credits

Made by [Ashish Sukralia](https://github.com/sukralia). Built on [claude-photo-sorter](https://github.com/kairothq/claude-photo-sorter) by Divy Kairoth (MIT).

## License

MIT. See [LICENSE](LICENSE).
