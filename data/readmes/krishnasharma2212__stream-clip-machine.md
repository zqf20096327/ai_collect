# Stream Clip Machine (GTA 6)

A laptop that runs 24/7: it watches the biggest live GTA 6 streams, notices the moment a streamer's chat explodes,
cuts that moment, has **Claude** turn it into a vertical Short with a hook and captions, and posts up to 5 a day to
YouTube Shorts and Instagram Reels (TikTok later).

Windows · Python 3.13 · Node · ffmpeg · [Claude Code](https://claude.com/claude-code) · Playwright MCP

> **Only clip streamers who allow it.** Many streamers welcome clips; some don't. Clipping campaigns
> (approved footage, paid per 1,000 views) are the safe route. Every video credits and links the streamer, and
> `discovery.block` keeps anyone who says no (or files a claim) out for good. Grand Theft Auto VI is a trademark of
> Rockstar Games / Take-Two; this project isn't affiliated with them or with any streamer.

## How it works

```
discover (5 min) -> top English GTA 6 streams on Twitch + YouTube Live (personality streamers first)
watch            -> each stream: rolling 8-min recording + live chat
detect (1 s)     -> chat speed vs its own normal, many different chatters, mostly reactions = a moment
                    + audio watcher: the streamer 12 dB+ louder than their normal while chat is busy = a moment
cut              -> 35 s before .. 80 s after the spike, from the recording (+ how loud the streamer got)
prepare          -> captions transcript (Whisper), English check, frame sheets
triage  (Claude Sonnet, batches) -> would a stranger watch it to the end? 6/10+ kept
edit    (Claude Opus, one clip)  -> 30-75 s cut, hook (streamer / narrator / text style, rotated), layout,
                                    captions, title/description/tags; renders and checks the preview itself
post             -> one per platform per slot: YouTube via your logged-in Chrome (background tab, scripted, then
                    Game title "Grand Theft Auto VI" on the edit page), Instagram via an InstaAutoDM server (optional)
```

Why each part works this way (with sources): [RESEARCH.md](RESEARCH.md).

## What you need
- A Windows laptop that can stay on 24/7 (an NVIDIA GPU makes captions much faster; CPU works too).
- ~30 Mbps download for 4 streams at once, and a few GB of free disk (old moments are cleaned up automatically).
- Claude Code with a paid Claude plan (triage + editing run as Claude Code sessions).
- A YouTube channel, logged in to a Chrome profile for the bot, with the **Playwright Extension** installed.
- Optional: Instagram publishing through an InstaAutoDM server (`AUTODM_API_URL` / `AUTODM_API_KEY`),
  a free Twitch app key, TikTok.

## Quick start
```powershell
git clone https://github.com/krishnasharma2212/stream-clip-machine
cd stream-clip-machine
powershell -ExecutionPolicy Bypass -File .\setup.ps1     # add -Gpu on an NVIDIA laptop
claude                                                    # sign in once, then /exit
notepad .env                                              # fill it in: SETUP.md
.\gta.cmd doctor                                          # every line must say OK
.\gta.cmd task install                                    # keeps it running (starts at logon, restarts on crash)
```
Full walkthrough (Chrome profile, extension token, Instagram, TikTok): [SETUP.md](SETUP.md).
No Instagram server? Set `publish.instagram.enabled: false` in `config/settings.yaml`.
Your channel: put its ID in `config/seo.yaml` (`channel_id`) or `.env` (`YOUTUBE_CHANNEL_ID`).

## Everyday commands
```
.\gta.cmd status       what it's watching, moments today, what got posted (with links), next slot, errors
.\gta.cmd doctor       full check: tools, Claude login, Chrome extension + YouTube login, Instagram
.\gta.cmd list         moments and their state         .\gta.cmd report    views per hook style (A/B)
.\gta.cmd post-now     post the best waiting clip everywhere now
.\gta.cmd task install / remove     the Windows task that keeps it running
```
Each moment lives in `data/clips/<id>/`: raw.mp4, transcript, sheet.jpg, edit.json (Claude's decisions),
final.mp4, cover.jpg, preview.jpg. Logs: `logs/gta.log`; every Claude session: `logs/claude/`.

## Settings (config/settings.yaml)
- `game.*`: the game it follows. Change the name, Twitch category and YouTube queries to clip another game.
- `publish.per_day` / `slots_utc`: 5 a day at 10:00, 13:00, 16:00, 19:00, 22:00 US Eastern.
- `discovery.prefer` / `block`: streamers to favor / never clip (block anyone who files a claim).
- `discovery.max_streams`: how many streams are recorded at once (4 = ~30 Mbps download).
- `detector.*`: how big a chat spike must be. More moments: lower `z_threshold` (3.0) or `min_reaction_share`.
- `clip.final_seconds`: final length (30-75 s). `styles.rotation`: hook styles in the A/B test.
- `claude.*`: which model does triage / edit / upload fixes.
- `publish.youtube.visibility`: public / unlisted / private.
- `cleanup.*`: moments are ~90 MB each (~2 GB/hour on a busy day). Every 5 min, thrown-away moments (dropped / failed /
  expired / rejected) lose their video 10 min after the decision (`media_after_min`); a rejected 5+/10 keeps it for
  `rescue_hours` (the editor may still use it in a dry spell). meta.json / transcript / edit.json stay 1 day for reports.
  `protect`: moment folders never deleted. An error is logged under `warn_free_gb` free.

Channel text, tags and description: `config/seo.yaml`, then `.\gta.cmd channel-setup`.

## When something breaks
| `status` / `doctor` says | Fix |
|---|---|
| supervisor NOT RUNNING | `.\gta.cmd task install` (or run `.\gta.cmd run` in a window to see the error) |
| YouTube Studio FAIL / "wrong login" | Chrome isn't running, or `CHROME_PROFILE_DIR` in `.env` isn't the bot's profile, or the extension token changed (copy it again from the extension page into `.env`) |
| youtube `retry ... browser` | Chrome was closed: open it; the next slot retries |
| youtube `upload blocked: daily limit or phone verification` | verify the channel at youtube.com/verify; YouTube caps new channels' daily uploads |
| claude `FAILED ... limit` | Claude usage limit: it waits and retries; lower `publish.per_day` or the edit model if it keeps happening |
| instagram `code 10` | reconnect the Instagram account on the AutoDM server |
| instagram `missing a secret` / `402` | the AutoDM server isn't fully set up or is off; queued posts retry every <=2 h by themselves |
| no moments for hours | streams offline at night (normal) or chat thresholds too strict (`detector`) |
| a streamer complains / claims | add them to `discovery.block`; delete their videos in Studio |

Using Claude Code in this folder? [CLAUDE.md](CLAUDE.md) tells it how to check, tune and fix the machine.

## License
[MIT](LICENSE). The clips you make belong to the streamers: credit them, respect their clipping rules.
