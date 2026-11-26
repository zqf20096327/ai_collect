# Photo sweep

Clean up a Nextcloud photo library with a vision model that runs on your own
hardware. Photo sweep sorts every picture into screenshots, memes, documents,
junk, clutter, blurry shots and real photos, and finds duplicates by what the
picture shows rather than by file name or bytes. You review the results on one
page and delete what you choose. Every delete goes to Nextcloud's **Deleted
files**, so it can be undone.

Nothing leaves your network by default. There is no cloud service and no
account, and the telemetry onnxruntime would otherwise start is switched off. **No GPU is needed:** a small image classifier sorts the library on
the CPU, agreeing with the vision model on 98% of labels, and a vision model,
when you have one, is asked only about the pictures the classifier is unsure
of: [No GPU?](#no-gpu-the-cpu-classifier-duplicates-only-or-a-cloud-model).
You can also point it at a cloud model, and it will refuse to until you say yes
in writing.

![Duplicate groups, each led by its best copy](docs/screenshots/duplicates.png)

## What it does

- **Sorts the library.** Each picture is labelled a screenshot, meme,
  document, junk or photo. Photos then get two narrower questions: is it
  blurry, and is it clutter (a floor, a receipt, a photographed screen, a
  plain room, the garden) rather than a keeper (people, pets, places,
  occasions, work on the house, something a child made). Clutter is a pile to
  review, not a delete list, so the rule leans towards clutter: a keeper in
  it costs one Keep click, while clutter called a keeper is never looked at
  again. Two engines answer, and
  work together: an **image classifier on the CPU** (SigLIP, built in) and a
  **vision model** (default `qwen3-vl:8b` on [Ollama](https://ollama.com)),
  which is optional. The classifier answers first and settles what it is sure
  of; the vision model gets only the rest. How it works and how well it does:
  [The CPU classifier](#the-cpu-classifier).
- **Finds duplicates that file-based tools miss.** A WhatsApp forward of a
  camera photo, a HEIC next to its JPEG, an `IMG_0205_1` re-import: different
  files, same picture. They are matched by a 256-bit perceptual hash of the
  image, with no model involved: every picture is fingerprinted first, so the
  Duplicates tab fills in long before the labelling is done. The groups come
  in two tiers:
  - **Same** holds copies. Each group puts its best copy first (most pixels,
    then a camera in the EXIF, then the larger file), and *Select all extras*
    selects every other copy across the whole library at once. The server checks
    each file again before deleting it, so a group can never lose its best copy.
  - **Similar** holds burst shots and near-repeats. These are different photos,
    so there is deliberately no bulk select: you pick the ones to go. The
    classifier's embeddings add the look-alikes the hash misses (a crop, a
    rotation, a filter, a burst frame with movement), into Similar only:
    [how](#how-the-duplicate-cut-offs-were-chosen). Among them are **mirrored
    copies**, a selfie and its flipped forward, captioned *mirrored*.
    *Mirrored only* shows just the groups holding one, and there *Select all
    mirrored copies* takes the flipped copies and nothing else, never a best
    copy, a Keep or a burst frame.
- **Narrows a big tab.** Every tab but Duplicates filters by year, from a
  folder named for the year (`2024/`), else a date in the file name, else the
  EXIF capture date; and by source (camera, no camera, messaging apps). Blurry
  also splits into Dark, Bright and Normal exposure. Each filter's counts are
  within the others.
- **Deletes safely.** The photo folder is mounted read-only. Deleting goes
  through Nextcloud's WebDAV API with an app password you can revoke, so files
  land in Deleted files and Nextcloud's index stays correct. Every action is
  written to an append-only, hash-chained audit log.
- **Keeps up.** After the first pass it re-walks the folder every six hours and
  labels only new pictures. When a question is reworded, the photos it may
  change are asked again, those the classifier most disagrees with first, so
  the tabs correct themselves in the first hours rather than evenly over the
  whole queue. The status line shows how many are left, the pace and the time
  left.

![The viewer: what the model said, and why](docs/screenshots/viewer.png)

## Before you start

- **The photo folder readable by Docker.** Photo sweep reads the pictures
  from disk (read-only); the Nextcloud app password is used only to delete.
  Any of these works: Nextcloud on the same machine, its data folder shared to
  the Docker host over NFS or SMB, or the folder synced there by the Nextcloud
  desktop client. A Nextcloud reachable only over the web is not supported yet.
- **A GPU is optional.** With none, the built-in classifier sorts on the CPU
  and duplicates need no model at all; see below. With a GPU somewhere on your
  network, point `OLLAMA_URL` at an Ollama server and the vision model checks
  what the classifier is unsure of. On an RTX-class card, `qwen3-vl:8b` takes
  about 3 s a question; asked about every picture, 40,000 photos took a day and
  a half, and with the classifier in front it is asked about a fraction of
  them. The page is usable while it runs.
- **Memory and disk.** The scanner used about 300 MB of memory with the
  classifier loaded, and each picture's stored embedding takes 1.5 KB beside
  its thumbnail.
- **Docker with the compose plugin.**

## No GPU? The CPU classifier, duplicates only, or a cloud model

**The CPU classifier (the default with no GPU).** Set `MODEL=none` and keep
the classifier on (it is on unless `CLASSIFIER=none`). Every tab works:
the classifier answers all three questions for every picture, on the CPU,
and nothing is sent anywhere. It costs about 0.1 to 0.3 s a picture on one
core, on top of fingerprinting; on a 2-core box it worked through 37,500
stored thumbnails in about seventy minutes. Its answers are its best guess, and the viewer says
**Sorted by: image classifier** so you know which engine decided. Details and
measured figures: [The CPU classifier](#the-cpu-classifier).

**Duplicates only.** Set `MODEL=none` and `CLASSIFIER=none`. Every picture is
still fingerprinted (a thumbnail, its size and camera, a sharpness score and
the duplicate hash), the Duplicates tab works in full, and nothing is sent
anywhere. The sorting tabs are hidden. Fingerprinting is all decoding: on a
desktop CPU with four workers, 12-megapixel JPEGs went at about 40 ms each, so
40,000 photos in under half an hour. A small NAS, or a library of HEIC, will be
several times slower; that is an estimate, not a measurement.
`FINGERPRINT_WORKERS` sets how many pictures are decoded at once (default: up
to 4).

**A cloud model (read this first).** Photo sweep can send its questions to a cloud vision model over the
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
| `OLLAMA_URL`, `MODEL` | Your Ollama server, or keep the default to use the bundled one. `MODEL=none` to sort with the CPU classifier alone |
| `CLASSIFIER` | `siglip` (default) or `none`. With `none` and `MODEL=none`, duplicates only |
| `DUP_EMBED` | How alike two pictures' embeddings must be to show as look-alikes in Similar (default `0.96`; `0` turns it off) |
| `DUP_MIRROR` | How close, in bits, a picture must be to another's flipped hash to be called its mirrored copy (default `24`) |
| `CLASSIFIER_TRUST` | How sure the classifier must be to settle a question when a vision model is also set (default `0.95`). Lower sends fewer pictures to the model |
| `EXPOSE_DARK_MEAN`, `EXPOSE_DARK_SHARE`, `EXPOSE_BRIGHT_MEAN`, `EXPOSE_BRIGHT_SHARE` | Where Blurry's Dark and Bright filters cut: an average grey (0-255) under `50` or at least `0.5` of the picture crushed to black is Dark; over `190` or `0.25` blown to white is Bright. Measured from the thumbnail, no model |
| `AUTO_RETRAIN` | `1` (default) lets the scanner retrain the classifier on your own answers when idle, keeping the new heads only if they test better; `0` turns it off. `RETRAIN_MIN_NEW` (default `200`) and `RETRAIN_EVERY_S` (default one day) pace it |

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

**Look-alikes from the classifier.** The hash compares brightness edges, so a
crop, a rotation, a filter or a burst frame with movement lands far from its
twin. The classifier's embeddings do not have that blind spot, so pairs of
pictures whose embeddings are at least `DUP_EMBED` alike (default 0.96, cosine;
0 turns it off) are added, **to Similar only**: a look-alike never makes a Same
group and never joins one, so Same groups and Select all extras are exactly
what the hash alone gives, and the copy marked best is still chosen by pixels,
camera and file size. On a 26,551-picture live library
(counts only, no picture viewed):

| Cut-off | Pairs the hash missed | Taken within an hour | Same folder | Largest group |
|---|---|---|---|---|
| 0.98 | 379 | 43% | 99% | 25 |
| **0.96** | **2,547** | **81%** | **97%** | **55, 20 after the cap** |
| 0.95 | 5,168 | 81% | 92% | 146 |
| 0.92 | 24,583 | 54% | 62% | 529 |

Every one of those pairs was two photos; no two screenshots of one app came
out alike. Of the hash's own Same pairs, 98% are at least 0.96 alike. Below
0.95 groups chain, as the hash did at 50 bits, so every group is also capped at
`DUP_GROUP_MAX` (default 20): a bigger one is cut again at a higher similarity
until it falls apart, except where its pictures are at least 0.99 alike or
joined by the hash, so a long burst stays whole. With look-alikes added, the
groups on that library went from 497 to 1,518 and the pictures in them from
1,386 to 4,041, with no new group over 20. Linking the whole library took 13 s
on two cores, once; after that only new pictures are compared.

**Mirrored copies.** A flipped picture's hash is unrelated to the original's:
a WhatsApp selfie and its mirrored forward were 126 bits apart. So each
picture also stores the hash of its thumbnail flipped left to right, and a
Similar member within `DUP_MIRROR` bits (default 24) of the flipped hash of a
copy ranked above it, and closer that way than as it is, is called mirrored.
That pair came out 14 bits apart flipped; on the 37,500-picture library about
440 look-alike pairs fell within 24 bits, in 368 of 1,515 Similar groups, and
no random pair of 200,000 came within 20. The flipped hash is taken from the
pixels, not worked out from the plain hash: that shortcut is wrong wherever
neighbouring pixels are exactly equal (a blown sky, a white wall), 66 bits off
on a test picture. Hashing every thumbnail flipped took about 40 s, once.

Of a mirrored pair, the best copy is usually the camera original. With a
selfie, though, the camera's version is the world's view and the mirrored one
is what the screen showed; a line of text in the picture tells which reads
the right way round.

## The CPU classifier

**What it is.** Each picture's thumbnail goes through the image half of
[SigLIP](https://huggingface.co/google/siglip-base-patch16-224) (Google,
Apache-2.0), base size, 16-pixel patches, quantised to 8 bits and run by
[onnxruntime](https://onnxruntime.ai) on the CPU. That turns the picture into
768 numbers, an *embedding*, which places pictures that look alike near each
other. Three small trained layers, the *heads*, read the answers off the
embedding:

| Question | Head | Answers |
|---|---|---|
| What kind of picture | linear layer | screenshot, meme, document, junk, photo |
| Clutter or keeper | one hidden layer (256 units) | a probability |
| Blurry or sharp | one hidden layer (256 units) | a probability |

Every probability is calibrated on pictures the heads never saw, so 0.95 means
right about 95 times in 100. No GPU, no PyTorch and no network are involved; the
heads are a 1.6 MB file of numbers in `photosweep/heads/`.

**The model file** (about 100 MB, the int8 ONNX export by
[Xenova](https://huggingface.co/Xenova/siglip-base-patch16-224)) is downloaded
when the image is built, from one fixed revision, and refused unless its size
and SHA-256 match (`photosweep/fetch_model.py`). For an install without
Docker: `python -m photosweep.fetch_model /path/to/siglip-b16-int8.onnx`, then
set `CLASSIFIER_MODEL` to that path.

**How it works with a vision model.** The classifier answers first, for every
picture. With `MODEL=none` its answers are final. With a vision model set, an
answer is final only when the classifier is at least `CLASSIFIER_TRUST` sure
(default 0.95) either way; every other question waits for the vision model, so
the model's time goes to the hard pictures. On the library below, that settled
92% of labels, 88% of clutter questions and about half of blur questions
without the model. Taken together, the vision model was left with roughly a
quarter of the questions it would otherwise have been asked.

**How well it does.** Measured on one 37,519-picture family library against
`qwen3-vl:8b`'s answers and the owner's own keeps and deletes. Five-fold
cross-validation, every duplicate group kept in one fold, so no picture was
scored by heads trained on it or on a copy of it. "Agree" means agrees with the
vision model, which is itself an opinion, not ground truth.

| | Pictures | Result |
|---|---|---|
| Label, overall | 37,519 | **98.2%** agree |
| photo / screenshot / document / junk / meme | 34,282 / 1,897 / 977 / 135 / 228 | 98.5% / 95.5% / 93.7% / 97.0% / 85.1% agree |
| Label, when at least 0.95 sure | 92% of pictures | 99.7% agree; 0.28% of real photos called something else |
| Clutter (6% of these photos) | 31,073 | AUC 0.986; at its best guess 83% precision, 67% recall |
| Clutter, when at least 0.95 sure | 88% of photos | flagged clutter 98% precise; of 245 photos the owner kept, 3 flagged |
| Blur (14% of photos) | 29,204 | AUC 0.892; at its best guess 71% precision, 40% recall |
| Blur, when at least 0.95 sure | 52% of photos | flagged blurry 97% precise, but few are flagged |

The clutter question was reworded just before training, and again after,
from what the owner actually did with 2,133 reviewed Clutter photos (themes
matched by the classifier's text side, counts only): renovation and repair
were kept 38% of the time, damage 26%, children's drawings 24%, but the
outside of the house only 3%, the garden 12% and food, screens and paper 0
to 6%. So work on the house and something a child made are keepers, and a
plain room, the outside of the house and the garden are clutter. Photos
waiting for the vision model's new answer were left out of training, so the
clutter head learned from the owner's deletes and keeps and the model's
keeper answers. It is cautious for now: when sure it is almost always right,
but it settles only the plainest clutter itself and leaves the rest to the
vision model. It is retrained once the re-asks are in.

**Picking the best shot of a burst** needs no model. On 2,113 burst groups
where the owner kept some frames and deleted others, the ranking above (pixels,
camera, blur verdict, file size) put a frame the owner kept first 97% of the
time, against 50% by chance. The sharpest pixels and the blur head picked at
chance, 45 to 52%: whatever makes one frame better than the next, it is not a
blur they can see.

Blur is the weakest question: a thumbnail hides much of what makes a photo
soft, so with a vision model set, most blur questions still go to it. Memes are
the weakest label.

**Why this model.** Five candidates were compared on a 2,555-picture sample of
the same library, each with the same linear head (time is the median per
picture on one shared core):

| Model | Agree | Time |
|---|---|---|
| CLIP B/32, int8 | 93.0% | 77 ms |
| CLIP B/32, full precision | 93.1% | 118 ms |
| SigLIP 2 B/16, int8 | 93.3% | 274 ms |
| **SigLIP B/16, int8 (chosen)** | **95.2%** | 272 ms |
| SigLIP B/16, full precision | 95.1% | 439 ms |

Full precision bought nothing over 8 bits. Asking the model by text alone
("a screenshot", "a meme"), with no trained head, did badly: it called most
photos junk. A hidden layer in place of a linear head lifted clutter's AUC from
0.968 to 0.988 and changed nothing else much.

**Training it on your own library.** The bundled heads were trained on one
library, so your mix of pictures may differ. Every embedding is stored, and the
heads can be retrained from your own labels: what the vision model answered
(never the classifier's own guesses) and what you did, where a photo you kept
counts as a keeper whatever the model said, and an answer waiting on a
Recheck is left out. It needs a few thousand pictures
labelled by a vision model, so it is for libraries that had one at some point.

```sh
docker compose exec scanner python -m photosweep.train_heads --dry-run   # report only
docker compose exec scanner python -m photosweep.train_heads             # write /data/heads.npz
docker compose restart scanner
```

It prints the same out-of-fold figures as above, as counts only. Heads in
`/data/heads.npz` (or `CLASSIFIER_HEADS`) are used in place of the bundled ones
and survive image updates; delete the file to go back. Training took under two
minutes for 37,500 pictures on two cores.

**It also retrains itself.** When the scanner has nothing to do, at most once a
day, and once 200 new answers have come in since the heads in use were trained
(your keeps, your deletes of clutter, the vision model's answers), it trains new
heads at low priority and tests them against the old **on those new answers
only**, which the old heads cannot have learned from. The new heads must be no
worse on each question with at least 100 new answers, and must not file more
of your new keeps as clutter at `CLASSIFIER_TRUST` than the old would. If they
pass they replace the old, which are kept as `/data/heads.npz.prev.npz`;
otherwise nothing changes and the next try judges on more. Each answer is
dated by its own question, so a re-asked clutter question never makes an old
blur answer look new. The first time it runs it only notes the time, since the
heads in use may have been trained on everything already there. Each try is
logged, and the latest is kept in the `retrain_last` setting. To roll back,
copy the `.prev.npz` over `heads.npz` and restart the scanner. `AUTO_RETRAIN=0`
turns it off.

**What the bundled heads hold.** Only weights: 1.6 MB of numbers learned from
the author's library. No picture, thumbnail, embedding or file name is in
them, and they are no practical way to recover any.

## Limits

- The labels are an opinion, the vision model's or the classifier's. The
  vision model's confidence numbers cluster at 95 to 100, so treat them as a
  sort order; the classifier's are calibrated. Review before deleting; the page
  is built for that.
- The classifier's figures come from one library, labelled by one vision model.
  Yours may sort differently; [retrain it](#the-cpu-classifier) if you can.
- One library, one Nextcloud user per install.
- Photos must be readable as files on the Docker host (a local folder or a
  network mount); reading them over WebDAV alone is not built yet.
- The prompts were tuned on `qwen3-vl:8b`. A cloud model answers the same
  questions, but its labels have not been measured against a real library.

## Development

```sh
pip install -r requirements-dev.txt
python -m pytest -q   # the classifier tests fake the ONNX model; nothing is downloaded
scripts/smoke.sh     # builds the image (with the real model), runs the tests in it, then three passes:
                     # a stand-in vision model, the CPU classifier alone, and duplicates only
```

## Licence

[AGPL-3.0](LICENSE), the same licence as Nextcloud. The SigLIP model it
downloads is Google's, under Apache-2.0. Use it, change it and share
it freely; if you offer a changed version to others over a network, publish
your changes under the same licence.
