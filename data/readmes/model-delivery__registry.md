# Model Delivery Registry

**A self-hosted registry for AI models and datasets that existing Hugging Face tools can download from and upload to.**

Your models. Your infrastructure. Your rules. Website: <https://model.delivery>

Think of a Docker registry or Artifactory, built for model files. Mirror
repositories from Hugging Face, or push your own, and serve them from a
machine you control. Tools built on `huggingface_hub` (`transformers`,
`diffusers`, the `hf` CLI and others) download from it, and upload to it,
after changing one environment variable:

```bash
export HF_ENDPOINT=http://localhost:8080
```

It is one binary. Out of the box it needs nothing else: metadata in SQLite,
model files on disk. For larger deployments the model files can live in
any S3-compatible bucket instead. It runs the same on a Raspberry Pi, a
homelab box or a server.

> **Status: early release.** Downloading, uploading, mirroring, pull-through
> caching, backups, the CLI and the web UI work, for models and for
> datasets. The Hugging Face compatible routes are tested against the real
> `huggingface_hub` and `datasets` libraries.
> Read [what is not supported yet](#what-is-not-supported-yet) and the
> [compatibility table](#hugging-face-compatibility) before relying on it.

## Quick start

Mirror a model, cut the connection to Hugging Face, and download it with a
standard Hugging Face client.

**1. Start the registry.** Download `modelctl` from the
[releases page](https://github.com/model-delivery/registry/releases), or
use Docker (below).

```bash
modelctl serve
```

On first start it prints an admin token. Copy it:

```bash
export MODELCTL_TOKEN=md_...
```

**2. Mirror a model from Hugging Face.**

```bash
modelctl mirror hf-internal-testing/tiny-random-bert
```

```
Mirroring hf-internal-testing/tiny-random-bert at revision f171d7baecaf...: 10 files, 26.9 MiB
  downloaded    25.4 MiB  tf_model.h5
  ...
Mirrored hf-internal-testing/tiny-random-bert at revision f171d7baecaf37b5da5a3616d8833b9969753535
10 files verified: 26.9 MiB downloaded, 0 B already stored
```

Every file is checked against the digest Hugging Face publishes for it, and
the revision keeps its upstream id.

**3. Disconnect from Hugging Face** (unplug, or block `huggingface.co`).

**4. Download with a standard client**, pointed at your registry:

```bash
export HF_ENDPOINT=http://localhost:8080
python -c "from huggingface_hub import snapshot_download; print(snapshot_download('hf-internal-testing/tiny-random-bert'))"
```

The files arrive from your registry, under the same revision id they had
upstream. Browse what you have at <http://localhost:8080>.

This exact flow runs as an automated test (`task test:e2e:network`).

### With Docker

```bash
docker run -d --name registry -p 8080:8080 -v registry-data:/data ghcr.io/model-delivery/registry
docker logs registry        # the admin token is printed here on first start
```

Or `docker compose up -d` with the [`compose.yaml`](compose.yaml) in this
repository. That file publishes the port on `127.0.0.1` only; a comment in
it says how to serve other machines. The image contains the same
`modelctl` binary:

```bash
docker exec -e MODELCTL_TOKEN=md_... registry /modelctl mirror openai-community/gpt2
```

## What it does

| | |
|---|---|
| **Mirror** | Copy a repository from Hugging Face (or any compatible hub) at a branch, tag or revision id, or every branch and tag in one command. Private and gated repositories work with your Hugging Face token. |
| **Keep up to date** | Follow a mirrored repository and the registry checks the upstream on a schedule, or when CI tells it to, and mirrors what has moved: branches move forward, earlier revisions stay, tags never move and nothing is ever deleted. |
| **Datasets** | Everything here works for dataset repositories too: mirror, cache on demand, push, pull, upload and serve them to `snapshot_download(repo_type="dataset")`, `hf download --repo-type dataset` and `load_dataset`. A model and a dataset of the same name are two repositories. |
| **Cache on demand** | Optionally, let the registry fetch from Hugging Face what it does not have: the file listing the first time a model is asked for, and each file the first time it is downloaded. Point your tools at the registry and it fills itself, one requested file at a time. |
| **Serve** | Existing clients download through the Hugging Face compatible API, including range requests. |
| **Push and pull** | Store your own models: `modelctl push ./dir team/model`, `modelctl pull team/model`. |
| **Upload** | Hugging Face tools upload to it as they would to the Hub: `hf upload team/model ./dir`, `upload_folder`, `create_commit`. See [the note on large files](#hugging-face-compatibility). |
| **Version** | Every revision is immutable and addressed by id. Branches move, tags never do. |
| **Verify** | Files are stored under the SHA-256 of their content and verified on the way in. Identical files are stored once, across revisions and repositories. `modelctl verify` re-checks everything in storage later, to find damage. |
| **Store** | Local disk, or an S3-compatible object store. Verified against Cloudflare R2 and SeaweedFS (which CI runs on every change). It uses the standard S3 API, so AWS S3, Backblaze B2, Ceph and MinIO are expected to work but have not been tested. With S3, downloads can be redirected to signed bucket URLs so the bytes never pass through the registry. |
| **Control access** | Access tokens with read, write and admin roles. Downloads can be open or require a token. |
| **Back up** | The metadata database is snapshotted on a schedule or on demand, verified, and stored beside the model files; `modelctl restore` puts a snapshot back. |
| **Monitor** | `GET /metrics` reports, for Prometheus, the cache hit ratio, upstream failures, what is stored and pending, and the age of the last backup. No metric names a repository or a file. |
| **Browse** | A small web UI lists repositories, revisions, files and storage use. |

## Command line

```
modelctl serve                      run the registry
modelctl mirror <repo>              copy a repository from the upstream hub
modelctl follow list|stop           show or stop what the registry keeps up to date
modelctl sync <repo>|--all          check followed repositories against the upstream now
modelctl push <dir> <repo>          upload a directory as a new revision
modelctl pull <repo>                download a revision and verify it
modelctl list                       list repositories
modelctl inspect <repo>             show revisions, refs and files
modelctl delete <repo> --yes        delete a repository and free its storage
modelctl token create|list|revoke   manage access tokens
modelctl gc                         remove stored files nothing references
modelctl verify                     re-read every stored file and check it against its digest
modelctl backup now|list|download   back up the registry's metadata
modelctl restore <file>|--latest    put a backup back (registry stopped)
```

Client commands read `MODELCTL_ENDPOINT` (default `http://localhost:8080`)
and `MODELCTL_TOKEN`. Every one accepts `--json` for scripts. `mirror`,
`push`, `pull`, `list`, `inspect`, `delete`, `follow stop` and `sync` work
on models unless given `--repo-type dataset`, the same flag `hf download`
and `hf upload` take.

```bash
modelctl mirror meta-llama/Llama-3.2-1B --upstream-token "$HF_TOKEN"   # gated repository
modelctl mirror openai-community/gpt2 --revision <branch, tag or 40-character revision id>
modelctl mirror --repo-type dataset stanfordnlp/imdb                    # a dataset
modelctl mirror openai-community/gpt2 --all-refs --follow               # every branch and tag, kept up to date
modelctl sync openai-community/gpt2                                     # check it now, from CI
modelctl push ./my-model my-team/my-model --tag v1.0 --message "first release"
modelctl push ./my-data my-team/my-data --repo-type dataset
modelctl pull my-team/my-model --revision v1.0 --dir ./out
modelctl inspect my-team/my-model --revision main
modelctl list --repo-type dataset
modelctl token create ci --role write
```

The REST API behind these commands is described in [docs/api.md](docs/api.md).

## Configuration

`modelctl serve` is configured by flags or environment variables. Every
setting that is not a secret has both; a flag wins over its variable.
`modelctl serve --help` lists them all.

| Flag | Environment | Default | |
|---|---|---|---|
| `--addr` | `REGISTRY_ADDR` | `:8080` | Listen address |
| `--data` | `REGISTRY_DATA` | `./data` | Database and stored files |
| `--upstream` | `REGISTRY_UPSTREAM` | `https://huggingface.co` | Hub to mirror from |
| `--require-auth` | `REGISTRY_REQUIRE_AUTH` | `false` | Require a token for downloads and browsing too |
| `--require-admin-token` | `REGISTRY_REQUIRE_ADMIN_TOKEN` | `false` | Refuse to start without a supplied admin token instead of generating one and printing it. Use on Kubernetes and anywhere logs are collected |
| `--pull-through` | `REGISTRY_PULL_THROUGH` | `false` | Fetch a model from the upstream hub the first time a client asks for one the registry does not hold |
| `--pull-through-allow` | `REGISTRY_PULL_THROUGH_ALLOW` | all | Comma-separated patterns limiting which repositories pull-through may fetch, for example `meta-llama/*,google/*`. A dataset is matched as `datasets/namespace/name`, so `datasets/acme/*` names datasets and `acme/*` models only |
| `--pull-through-max-file-bytes` | `REGISTRY_PULL_THROUGH_MAX_FILE_BYTES` | `0` (no limit) | Largest file, in bytes, that pull-through fetches on demand. Larger files are refused with an error naming `modelctl mirror` |
| `--pull-through-stream` | `REGISTRY_PULL_THROUGH_STREAM` | `true` | Send a file to the clients waiting for it while pull-through is still fetching it, holding back its end until it is verified. `false` sends nothing until the file is stored. See [the first download](docs/operations.md#the-first-download-of-a-file) |
| `--max-blob-bytes` | `REGISTRY_MAX_BLOB_BYTES` | `0` (no limit) | Largest single file, in bytes, that an upload may store. Larger uploads are refused with `413` |
| `--storage` | `REGISTRY_STORAGE` | `filesystem` | Where model files are kept: `filesystem` or `s3` |
| `--backup-interval` | `REGISTRY_BACKUP_INTERVAL` | `0` (off) | Store a metadata backup this often, for example `1h`; at least a minute |
| `--backup-keep` | `REGISTRY_BACKUP_KEEP` | `48` | How many stored backups to keep; `0` keeps all |
| `--sync-interval` | `REGISTRY_SYNC_INTERVAL` | `0` (off) | Check each followed repository against the upstream this often and mirror what has moved, for example `1h`; at least five minutes. See [keeping mirrors up to date](docs/operations.md#keeping-mirrors-up-to-date) |
| `--restore-if-empty` | `REGISTRY_RESTORE_IF_EMPTY` | `false` | At start, if there is no database, restore the newest stored backup |

An on/off variable accepts `true` and `false`, and also `1`, `0`, `yes`,
`no`, `on` and `off`. Any other value stops the server at start with an
error naming the variable; before v0.3.1 it was read as off.

**Secrets** are read from the environment only. They have no flag, because
a command line shows in the process list and in shell history.

| Environment | |
|---|---|
| `REGISTRY_ADMIN_TOKEN` | Use this admin token instead of generating one |
| `REGISTRY_ADMIN_TOKEN_FILE` | Read the admin token from this file (a mounted secret) |
| `REGISTRY_UPSTREAM_TOKEN` | Default token for the upstream hub |
| `REGISTRY_S3_ACCESS_KEY`, `REGISTRY_S3_SECRET_KEY` | Credentials for S3 storage. `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` (with `AWS_SESSION_TOKEN`) are used if these are unset; with neither, the instance or pod role is used. |

**S3 storage.** Set `--storage s3` (or `REGISTRY_STORAGE=s3`), the
credentials above, and:

| Flag | Environment | |
|---|---|---|
| `--s3-bucket` | `REGISTRY_S3_BUCKET` | Required. The bucket must already exist. |
| `--s3-endpoint` | `REGISTRY_S3_ENDPOINT` | Service URL. Default `https://s3.amazonaws.com`. For other services, for example `https://<account>.r2.cloudflarestorage.com` or `http://seaweedfs:8333`. |
| `--s3-region` | `REGISTRY_S3_REGION` | Region, when the service needs one. `AWS_REGION` is used if this is unset. |
| `--s3-prefix` | `REGISTRY_S3_PREFIX` | Key prefix, to share a bucket. |
| `--s3-redirect` | `REGISTRY_S3_REDIRECT` | Send downloads to signed bucket URLs instead of streaming them through the registry. Clients must be able to reach the bucket. |

Metadata stays in SQLite in the data directory, so keep that directory on a
persistent disk and back it up. See [docs/operations.md](docs/operations.md#s3-storage).

**Pull-through caching.** With `--pull-through`, the registry fetches what
it is asked for and does not have. The first request for a model records
its file listing from the upstream hub, which takes a moment. Each file's
content is then fetched the first time someone downloads that file, checked
against its digest, and stored. Asking for one file of a large repository
fetches one file. That first download is sent to the client while the
registry is still fetching the file, so it takes about as long as the
fetch and starts at once; the end of the file is held back until the
whole of it has matched its digest, and a mismatch cuts the download
short (`--pull-through-stream=false` sends nothing before the file is
verified and stored, at the price of the first download of a large file
timing out). Anyone allowed to download can trigger a
fetch, so on a registry others can reach, combine it with `--require-auth`
or an allow list. A repository you pushed is never added to from upstream;
if you push your own models as well, use an allow list that leaves your
own namespaces out. To have a whole model available offline, run
`modelctl mirror`. See
[docs/operations.md](docs/operations.md#pull-through-caching).

**Access.** Writing (push, mirror) always needs a token with the `write`
role; deleting and managing tokens needs `admin`. By default anyone who can
reach the registry can download, which suits a home network. Set
`--require-auth` to require a `read` token for downloads too; clients then
send it the usual way:

```bash
export HF_ENDPOINT=https://models.example.com
export HF_TOKEN=md_...
```

**TLS.** The registry speaks plain HTTP. Put it behind a reverse proxy
(Caddy, nginx, Traefik) for HTTPS, and do that before exposing it beyond a
network you trust. See [docs/operations.md](docs/operations.md).

**Offline and air-gapped networks.** The server contacts the upstream hub
only when you run `modelctl mirror` or turn on pull-through, and its
storage bucket if you configured one. It makes no other outbound
connection: no telemetry and no update check, and the web interface loads
nothing from elsewhere. To serve models where there is no route to
Hugging Face, mirror them on a connected machine and carry the data
directory across, or `modelctl pull` there and `modelctl push` inside.

**Backups.** Set `--backup-interval 1h` and the registry stores a
verified snapshot of its metadata next to the model files on that
schedule; `modelctl backup` takes one on demand and `modelctl restore`
puts one back. See [docs/operations.md](docs/operations.md#backup-and-restore).

**Monitoring.** `GET /metrics` is a Prometheus endpoint; nothing has to be
turned on. It follows read access: open when downloads are open, and with
`--require-auth` it needs a token with the `read` role, which Prometheus
sends as a bearer token. The metrics, a scrape configuration and alerts
for a backup that is too old, a failing upstream and a full fetch queue
are in [docs/operations.md](docs/operations.md#monitoring). Namespaces
called `metrics` and `datasets` cannot be used for repositories, like
`api`, `ui`, `static` and `healthz`.

## Hugging Face compatibility

The rows marked "Supported" are run against the real `huggingface_hub`
and `datasets` Python libraries in CI (`test/e2e`).

| Capability | Status |
|---|---|
| `snapshot_download`, `hf_hub_download`, `hf download` | Supported |
| `model_info`, `list_repo_tree`, `list_repo_files`, `list_repo_refs`, `get_paths_info` | Supported |
| Datasets: the calls above with `repo_type="dataset"` (`--repo-type dataset`), `dataset_info`, uploads, mirroring and pull-through | Supported |
| `load_dataset("org/name")` from a repository of csv, jsonl or parquet files | Supported for split files at the top (csv, jsonl, parquet) and for config directories of parquet files declared in the dataset card, as `push_to_hub` writes them; both tested on datasets mirrored from huggingface.co (`rotten_tomatoes`, `mbpp`) and by pull-through, giving the same splits and rows as huggingface.co. Other layouts are expected to work but are not tested. The Hub's dataset viewer is not implemented and is not needed: the library reads the repository's files. See [Datasets](docs/compatibility.md#datasets) |
| Branches, tags and pinned revision ids | Supported |
| Private access with `HF_TOKEN` | Supported |
| Uploading with `hf upload`, `create_repo`, `upload_file`, `upload_folder`, `create_commit` | Supported, with one condition for large files: see Xet, below |
| Range requests, which clients use to resume an interrupted download | Served and tested at the HTTP level; a resumed `huggingface_hub` download is not part of the client tests |
| Libraries that download through `huggingface_hub` (`transformers`, `diffusers`, ...) | Expected to work; not individually tested yet |
| Xet transfer | Not implemented. **Downloads** need nothing: the registry does not offer Xet, so clients download over plain HTTP. **Uploads** of files over 10 MiB need `HF_HUB_DISABLE_XET=1` on a client that has the `hf_xet` package, which `huggingface_hub` installs by default; such a client sends large files through Xet without asking the server. Smaller files upload without it |
| Spaces | Not supported |
| The dataset viewer (parquet conversion, row previews, croissant) | Not implemented |
| Search and listing (`list_models`, `list_datasets`) | Not supported |
| `git clone` / git-lfs access | Not supported |
| Hub-only features (discussions, likes, inference, gating workflows) | Out of scope |

Details, including the exact routes, are in
[docs/compatibility.md](docs/compatibility.md).

## What is not supported yet

- **One server.** Model files can be in S3, but metadata is a SQLite file
  on the server's disk, so you run a single instance. No replication or
  high availability yet.
- **Keeping mirrors up to date is opt-in, per repository.** A mirror is a
  copy of what it fetched until you follow it (`modelctl mirror --follow`)
  and set `REGISTRY_SYNC_INTERVAL`, or ask for a sync. A sync only adds:
  a branch or tag deleted upstream stays in the registry, and a tag moved
  upstream is reported, not moved. Pull-through caching fetches what the
  registry lacks, but it never refreshes a branch it already holds; see
  [keeping mirrors up to date](docs/operations.md#keeping-mirrors-up-to-date).
- **One upstream.** Every mirror, sync and pull-through fetch goes to the
  one hub `REGISTRY_UPSTREAM` names.
- **`modelctl mirror` copies whole revisions.** To fetch only some files of
  a repository, use pull-through caching, which fetches each file when it
  is first downloaded.
- **Repository ids are `namespace/name`**, and are case-sensitive.
- **Uploads are not resumable.** An interrupted `modelctl push` re-sends the
  file it was in the middle of; files that finished are skipped.
- **Large uploads from Hugging Face tools need one setting**,
  `HF_HUB_DISABLE_XET=1`, because the registry does not speak Xet. See the
  [compatibility table](#hugging-face-compatibility).
- **No per-repository permissions.** A token's role applies to the whole
  registry.

The [roadmap](docs/roadmap.md) says what is planned and in what order.
[Alternatives](docs/alternatives.md) describes other open-source projects
in this space and when one of them is the better choice.

## How it works

One process serves three things: the Hugging Face compatible routes, its
own REST API, and the web UI. Metadata is a SQLite database; file content
is stored once per unique SHA-256, on disk or in a bucket. A revision is a list of
`path -> digest` entries, so revisions that share files share storage. See
[docs/architecture.md](docs/architecture.md).

## Building from source

Needs Go 1.27 or newer. [Task](https://taskfile.dev) runs the common
commands:

```bash
task build        # bin/modelctl
task check        # format, vet, lint, unit tests
task test:e2e     # the huggingface_hub compatibility tests (needs Python)
task test:s3      # storage and compatibility tests against a real S3 server (needs Docker)
task docker       # container image
```

## Contributing

Bug reports and pull requests are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md). To report a security problem, see
[SECURITY.md](SECURITY.md).

## License

Copyright 2026 [Spectrum Labs LLC](https://spectrumlabs.tech). Licensed under the
[Apache License 2.0](LICENSE); see [NOTICE](NOTICE).

Model Delivery is a Spectrum Labs project. It is not affiliated with or
endorsed by Hugging Face. "Hugging Face" is a trademark of Hugging Face, Inc.
