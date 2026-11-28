# Pirate Face CLI

Downloads HF models over BitTorrent from [Pirate Face](https://pirateface.co) seeders.

## Install

```sh
pip install pirateface
```

Or without installing: `uv run -p 3.13 --with pirateface python your_script.py`. Needs Python 3.12 or 3.13. With `uvx`, pass `-p 3.13`.

Anything that downloads through HF (transformers, diffusers, `hf download`) now pulls from the swarm. Files are checked against Hugging Face's SHA-256 before they are trusted; offline, with the cached index, the same bytes are checked against the torrent's own piece hashes. If a model isn't on Pirate Face or a peer stalls, that file comes from Hugging Face as usual. Set `PF_HF_FIRST=1` to reverse the order: Hugging Face first, swarm only when it fails.

## Commands

```sh
pf download org/model      # download into the Hugging Face cache (--local-dir DIR for a folder)
pf seed org/model [FOLDER] # seed a model, submitting it first if Pirate Face doesn't list it
pf submit --repo org/model FOLDER  # package and submit a folder (--dry-run to preview)
pf work                    # build torrents for queued model requests, streamed from Hugging Face
pf restore PATH            # upload .torrent files to fix a listing whose magnet stalls
pf index [--sync]          # the cached magnet index: what it holds, and mirror the newest build
pf find-model FILE         # which listed models hold this file (sha256)
pf dedupe                  # duplicate Hugging Face cache blobs (--apply to hardlink, default dry run)
```

`pf work` builds torrents for queued model requests, streamed from Hugging Face into memory; no model bytes are saved to disk. Progress is saved in a private checkpoint (completed pieces plus the unfinished piece's SHA-256 state, or file boundaries when the native hasher is unavailable) and an interrupted run resumes it on the next run while the lease is still active; a new lease for the same model revision and files can also reuse it. Completed file checkpoints are retained when the native hasher is unavailable. A checkpoint that does not check out (corrupt, missing block hashes, a different job) is discarded automatically and the job rebuilds from scratch. Piece-boundary checkpoints are saved at most every few seconds. `pf work --clear-progress` discards the saved hashes (keeping the lease), and `--name` keeps concurrent workers' checkpoints apart.

Run `pf <command> --help` for every flag.

## When Pirate Face is down

The site's magnet index lists every model's magnet as a weekly torrent, mirrored into `$PF_CACHE/index/shards/`. When Pirate Face cannot be reached, a listed model in that copy still downloads: checked against the Hugging Face fingerprint first, and when Hugging Face cannot answer, against the torrent's own piece hashes via the infohash the shard commits to.

```sh
pf index          # the build this copy holds, how many models, whether the site has a newer one
pf index --sync   # mirror the build the site names, replacing copies the build has changed
pf index --add    # add every magnet in the index to qBittorrent, your seeding tracker on new ones
```

## Settings

| Variable | |
|---|---|
| `PIRATEFACE_KEY` | Account key (otherwise asked once and saved) |
| `QBT_URL`, `QBT_USER`, `QBT_PASS` | qBittorrent Web UI (default `http://localhost:8080`) |
| `OLLAMA_MODELS` | Ollama model store root (default: the detected Ollama model directory) |
| `TR_HOST`, `TR_AUTH` | Transmission RPC (default `localhost:9091`), `user:pass` |
| `HF_TOKEN` | For gated repos |
| `PF_DISABLE` | Set to `1` to turn the download hook off |
| `PF_HF_FIRST` | `1` = download from Hugging Face first, swarm only when it fails |
| `PF_NO_BLOCK_PROOFS` | `1` = `pf work`, `submit` and `seed` submit without block proofs (default: they prove random 16 KiB blocks against the torrent's v2 hashes) |
| `PF_LISTEN` | libtorrent listen interfaces (default `0.0.0.0:0,[::]:0`) |

Downloads use libtorrent's defaults: listen on `0.0.0.0:0,[::]:0` (change via `PF_LISTEN`), UPnP and NAT-PMP port mapping, DHT and LSD peer discovery, and uncapped upload while downloading.

## Development

```sh
uv run --group dev ruff check
```

## Contributing

- One change per PR, small enough to read in one sitting.
- Please don't add tests for now. We're still settling how we test, so check your change by hand and say how in the PR.
- `uv run --group dev ruff check` and `ruff format --check` should pass with nothing new.
- When you replace code, delete the old code. No disabled flags or leftover branches.
- Fix problems where they start rather than adding special cases around them.
- If Pirate Face can't be reached, say so and carry on. Never crash, and never write outside the model folder.
- Add your Pirate Face username to the PR so we can credit you.

## Community Contributors

<p align="center">
  <a href="https://github.com/ZeroPointSynergy"><img src="https://github.com/ZeroPointSynergy.png" width="48" height="48" alt="ZeroPointSynergy"></a>
  <a href="https://github.com/dmitryrn"><img src="https://github.com/dmitryrn.png" width="48" height="48" alt="dmitryrn"></a>
  <a href="https://github.com/AndriiZvorygin"><img src="https://github.com/AndriiZvorygin.png" width="48" height="48" alt="AndriiZvorygin"></a>
  <a href="https://github.com/chloecaffeinexo"><img src="https://github.com/chloecaffeinexo.png" width="48" height="48" alt="chloecaffeinexo"></a>
</p>
