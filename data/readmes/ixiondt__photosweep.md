# Photo sweep

Clean up a Nextcloud photo library with a vision model that runs on your own
hardware. Photo sweep sorts every picture into screenshots, memes, documents,
junk, clutter, blurry shots and real photos, and finds duplicates by what the
picture shows rather than by file name or bytes. You review the results on one
page and delete what you choose. Every delete goes to Nextcloud's **Deleted
files**, so it can be undone.

Nothing leaves your network by default. There is no cloud service and no
account. If you have no GPU, you can point it at a cloud model instead, and it
will refuse to until you say yes in writing: [No GPU?](#no-gpu-a-cloud-model-read-this-first)

![Duplicate groups, each led by its best copy](docs/screenshots/duplicates.png)

## What it does

- **Sorts the library.** A local vision model (default `qwen3-vl:8b` on
  [Ollama](https://ollama.com)) labels each picture as a screenshot, meme,
  document, junk or photo. Photos then get two narrower questions: is it
  blurry, and is it clutter (a floor, a receipt, a photographed
  screen) rather than a keeper (people, pets, places, occasions).
- **Finds duplicates that file-based tools miss.** A WhatsApp forward of a
  camera photo, a HEIC next to its JPEG, an `IMG_0205_1` re-import: different
  files, same picture. They are matched by a 256-bit perceptual hash of the
  image. The groups come in two tiers:
  - **Same** holds copies. Each group puts its best copy first (most pixels,
    then a camera in the EXIF, then the larger file), and *Select all extras*
    selects every other copy across the whole library at once. The server checks
    each file again before deleting it, so a group can never lose its best copy.
  - **Similar** holds burst shots and near-repeats. These are different photos,
    so there is deliberately no bulk select: you pick the ones to go.
- **Deletes safely.** The photo folder is mounted read-only. Deleting goes
  through Nextcloud's WebDAV API with an app password you can revoke, so files
  land in Deleted files and Nextcloud's index stays correct. Every action is
  written to an append-only, hash-chained audit log.
- **Keeps up.** After the first pass it re-walks the folder every six hours and
  labels only new pictures.

![The viewer: what the model said, and why](docs/screenshots/viewer.png)

## Before you start

- **The photo folder readable by Docker.** Photo sweep reads the pictures
  from disk (read-only); the Nextcloud app password is used only to delete.
  Any of these works: Nextcloud on the same machine, its data folder shared to
  the Docker host over NFS or SMB, or the folder synced there by the Nextcloud
  desktop client. A Nextcloud reachable only over the web is not supported yet.
- **A GPU somewhere on your network.** Point `OLLAMA_URL` at any Ollama
  server. On an RTX-class card, `qwen3-vl:8b` takes about 3 s per picture:
  roughly a day and a half for 40,000 photos, once. The page is usable while it
  runs. On a CPU it works, many times slower.
- **Docker with the compose plugin.**

## No GPU? A cloud model (read this first)

Photo sweep can send its questions to a cloud vision model over the
OpenAI-compatible API that most providers offer, several with a free tier.
**Doing so sends a copy of every photo it labels to that company.** That is
your whole library: family, children, documents, the inside of your home.

- **What leaves:** each photo as a 512-pixel JPEG (1024 for a Recheck), with
  the question being asked. Nothing else: no file names, no EXIF, no location.
- **What happens to it is set by the provider's terms, not by Photo sweep.**
  Free tiers are often paid for with your data: some providers may keep it,
  have people review it, or use it to improve their models. Paid tiers usually
  promise more. Read the terms of the plan you actually use.
- **Free tiers are slow for a library.** They cap requests per minute and per
  day, and each photo can take three requests (the label, then the blur and
  clutter questions). At a few hundred a day, 30,000 photos takes months. Set
  `MODEL_MIN_INTERVAL_S` to stay under the per-minute cap; when the daily cap
  runs out, the scanner waits and carries on.

**It will not happen by accident.** When the model address is outside your
network (anything but a loopback, private, link-local or Tailscale-range
address, and any name that does not resolve), the scanner sends nothing and
the page says why, until `.env` contains:

```sh
PHOTOS_LEAVE_THIS_SERVER=yes
```

From then on, the page shows where your photos are going on every visit.
Remove the line and restart to stop.

To set it up, put the API key in a file in the data volume and point the model
settings at the provider:

```sh
MODEL_API=openai
MODEL_URL=https://api.provider.example/v1   # the base that /chat/completions hangs off
MODEL=<a vision model from the provider's list>
MODEL_KEY_FILE=/data/model.key
MODEL_MIN_INTERVAL_S=4                      # 15 requests a minute
PHOTOS_LEAVE_THIS_SERVER=yes
```

```sh
docker compose exec web sh -c 'umask 077; cat > /data/model.key'   # paste the key, then Ctrl-D
```

Base URLs that speak this API, as of November 2026 (check the provider's
documentation; model names and free limits change often):

| Provider | `MODEL_URL` |
|---|---|
| Google Gemini (AI Studio key) | `https://generativelanguage.googleapis.com/v1beta/openai` |
| Groq | `https://api.groq.com/openai/v1` |
| OpenRouter (`:free` models) | `https://openrouter.ai/api/v1` |

If a provider refuses the structured-output request, set `MODEL_JSON=object`,
or `MODEL_JSON=none` to rely on the prompt alone; the answer is checked either
way. `MODEL_API=openai` also works for a server of your own (LM Studio, vLLM,
llama.cpp), and one on your network needs no `PHOTOS_LEAVE_THIS_SERVER`.

## Install

```sh
git clone https://github.com/ixiondt/photosweep.git && cd photosweep
cp .env.example .env
```

Edit `.env`:

| Setting | What to put |
|---|---|
| `PHOTOS_DIR` | The folder on this machine: `<nextcloud data>/<user>/files/<folder>` |
| `PUID` / `PGID` | The user that owns those files. `33` (www-data) for most installs |
| `NC_BASE`, `NC_USER`, `NC_PREFIX` | Your Nextcloud address, the user, and the same folder as Nextcloud names it. Leave `NC_BASE` empty to browse without deleting |
| `OLLAMA_URL`, `MODEL` | Your Ollama server, or keep the default to use the bundled one |

Start it, set a password, and open `http://127.0.0.1:8087`:

```sh
docker compose up -d                          # add --profile ollama for a bundled Ollama (NVIDIA)
docker compose exec ollama ollama pull qwen3-vl:8b   # only with the bundled Ollama
docker compose exec web python -m photosweep.passwd
```

To delete, choose **Connect Nextcloud** on the page and paste an app password
from Nextcloud's **Settings → Security**. It is checked before it is saved, and
it stays on your server.

### Reaching it from other devices

The port is bound to `127.0.0.1`. Put a reverse proxy with HTTPS in front of it
(Caddy, Traefik, nginx), and set `FORWARDED_ALLOW_IPS` to the proxy's address
so sign-in cookies are marked Secure. If the proxy already signs people in
(Authelia, Authentik, Tailscale serve), set `AUTH_MODE=header`, the header it
sends in `AUTH_HEADER`, and the allowed names in `OPERATORS`. Use header mode
only when nothing but that proxy can reach the port.

## Sign-in

- **Password** (default): one password, at least 15 characters, stored as a
  scrypt hash. Wrong guesses are rate-limited. Setting a new password signs
  every browser out.
- **Header**: the proxy in front decides, as above. An unrecognised
  `AUTH_MODE` lets nobody in.

## How the duplicate cut-offs were chosen

Distances are in bits out of 256. On a 32,000-photo library, true copies
(resizes, recompressions, forwards) sat at 0 to 12 bits, burst shots at about
15 to 40, and unrelated photos became common from about 55. At 50 bits,
unrelated photos started chaining into one large group. So **Same** is 12 or
less and **Similar** is 40 or less, both adjustable with `DUP_SAME` and
`DUP_SIMILAR`. One blind spot is known: plain flat images (a black frame, a
blank wall) all hash alike and land together in Same.

## Limits

- The labels are a model's opinion. Its confidence numbers cluster at 95 to
  100, so treat them as a sort order, not a probability. Review before deleting;
  the page is built for that.
- One library, one Nextcloud user per install.
- Photos must be readable as files on the Docker host (a local folder or a
  network mount); reading them over WebDAV alone is not built yet.
- The prompts were tuned on `qwen3-vl:8b`. A cloud model answers the same
  questions, but its labels have not been measured against a real library.

## Development

```sh
pip install -r requirements-dev.txt
python -m pytest -q
scripts/smoke.sh     # builds the image, runs the tests in it, brings the stack up against a stand-in model
```

## Licence

[AGPL-3.0](LICENSE), the same licence as Nextcloud. Use it, change it and share
it freely; if you offer a changed version to others over a network, publish
your changes under the same licence.
