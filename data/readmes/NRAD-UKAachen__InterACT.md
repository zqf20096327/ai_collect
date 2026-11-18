# InterACT

[InterACT](https://www.ukaachen.de/en/kliniken-institute/klinik-fuer-diagnostische-und-interventionelle-neuroradiologie/forschung/ki-dateninfrastruktur/interact/)
is a research imaging platform developed at the Department of Diagnostic and
Interventional Neuroradiology, University Hospital RWTH Aachen (UKA): a DICOM
archive, a web viewer, single sign-on, and a set of neuroimaging and
segmentation pipelines that run against studies in the archive and write their
results back as DICOM.

It is assembled from established open-source components: dcm4chee-arc for the PACS, OHIF for the viewer, Keycloak for identity,
iRODS for data management, and Airflow for orchestration.

> **Research software handling patient data.** This is not a medical device and nothing it produces is a clinical read. If you point it at real patient data, read the [security model](Documentation/Project_Structure.md#security-model) and the [PHI access audit trail](Documentation/GUI.md#phi-access-audit-trail) first: the defaults here are for a trusted network.

## Available modules

InterACT consists of a **basis module**, which `docker compose up -d` always
starts, and **optional modules**, which sit behind Compose profiles so a first
run does not pull multi-gigabyte model weights you may not want. Every module
is reached through the same portal at `http://<PUBLIC_HOST>:5005`.

### Basis module

| Service | Port | |
|---|---|---|
| InterACT portal | 5005 | the Flask app users log into |
| OHIF viewer | 1081 | behind oauth2-proxy |
| dcm4chee admin UI | 1082 | behind oauth2-proxy, Admin group only |
| Keycloak | 8081 | identity provider |
| dcm4chee-arc | 11112 (DICOM) | the archive itself |
| processing API | 127.0.0.1:9200 | loopback only, no auth of its own |

These are the defaults from `.env.example` (each is a `PORT_*` variable) — see
[If you are running more than one InterACT instance](#if-you-are-running-more-than-one-interact-instance-on-the-same-server)
for the full list, including the lower-level dcm4chee ports not shown here.

### GUI pages of the basis module

**Home** — landing page and bug reports.

![Home page](Documentation/images/home.png)

**OHIF Viewer** — browse and view studies in the archive, and start the
processing tools (segmentation, morphometry, registration, …) from the toolbar.
Results are written back to the archive as DICOM.

![OHIF Viewer](Documentation/images/ohif_viewer.png)

**Batch Processing** — run one or more tools over a whole cohort, uploaded by
drag-and-drop (or picked from iRODS, if that module is running), and download
the results as a ZIP.

![Batch Processing](Documentation/images/batch_processing.png)

**Database** *(admin)* — the dcm4chee archive UI.

![Database](Documentation/images/database.png)

**PHI Access Log** *(admin)* — who viewed, searched, downloaded or edited which
patient data.

![PHI Access Log](Documentation/images/phi_access_log.png)

**Job Logs** *(admin)* — the processing API's log files, per job and per batch
case.

![Job Logs](Documentation/images/job_logs.png)

### Optional modules

| Module | Profile | GUI page | |
|---|---|---|---|
| iRODS | `irods` | iRODS, iRODS → Manage Users *(admin)* | research data management and sharing |
| Federated learning | `airflow` | Federated Learning *(admin)* | multi-site training, orchestrated by Airflow |
| SAMinRAD | `saminrad` | Interactive Segmentation | SAM2 interactive segmentation |
| LDCT | `ldct` | — (a tool in OHIF and Batch Processing) | low-dose CT simulation |

**iRODS** — browse, upload, download and share research data; use collections
as input for and output of Batch Processing.

![iRODS browser](Documentation/images/irods.png)

**Federated Learning** — register partner sites, manage local training data,
and start and monitor training rounds.

![Federated Learning](Documentation/images/federated_learning.png)

**Interactive Segmentation** — segment with SAM2 by clicking, and store the
result as DICOM-SEG.

![Interactive Segmentation](Documentation/images/interactive_segmentation.png)

**LDCT** — has no page of its own; it appears as the tool **LDCT** in the OHIF
toolbar and under CT → Image Simulation in Batch Processing.

## Prerequisites

| Requirement | | Needed for |
|---|---|---|
| Docker | with Compose v2 (`docker compose`, not `docker-compose`) | everything |
| GPU | NVIDIA Container Toolkit | the GPU-based tools of the processing API (basis), SAMinRAD, LDCT |
| FreeSurfer licence | free — see [secrets/freesurfer/README.md](secrets/freesurfer/README.md) | FastSurfer (basis, processing API) |
| TotalSegmentator licence | free for non-commercial use — see [secrets/totalsegmentator/README.md](secrets/totalsegmentator/README.md) | TotalSegmentator `brain_structures` only (basis, processing API) |
| FSL | host install, bind-mounted read only (`FSL_DIR`) | Hippocampus, SIENA, FSL registration, DTI (basis, processing API) |
| FreeSurfer | host install, 8.2 or later (`FREESURFER_DIR`) | SynthSeg (basis, processing API) |

If you don't have the required licenses or FSL and FreeSurfer installs yet, don't worry: You can still use the platform and all tools that do not depend on it.

## Quick start (basis module)

```sh
git clone https://github.com/NRAD-UKAachen/InterACT
cd InterACT
git submodule update --init   # pulls in the OHIF viewer (github.com/NRAD-UKAachen/Viewers)
cp .env.example .env
./generate-secrets.py                     # fill in the secrets
nano .env                                 # set PUBLIC_HOST
docker compose up -d
```

`.env` is the only file you edit. Every compose file in the repository reads
from it, so nothing in the subdirectories needs changing. `generate-secrets.py` automatically sets all required secrets in the `.env` file. If you prefer to do it by hand, please refer to [Details](#details).

**`PUBLIC_HOST`** is the name
**browsers** use to reach the machine, and it ends up in the OIDC redirect URIs,
the Keycloak realm and the portal's own links. `localhost` works only if you
browse from the machine itself; for anyone else, use a hostname their machine
resolves.

You should now see a login prompt at `http://<PUBLIC_HOST>:5005`:

<img src="Documentation/images/login.png" alt="Login page" width="400">

### Create platform users

No user accounts exist after deployment, so you have to create one first:

```sh
grep "KEYCLOAK_ADMIN_PASSWORD" .env  # this will show your password
cd keycloak-dev
cp users.csv.example users.csv       # only for the first user
nano users.csv          # set username and role (Admin or User)
KEYCLOAK_ADMIN_PASSWORD=<password from your .env file> ./create-users.sh
```

> [!CAUTION]
> Copy `users.csv.example` only once, for the very first user. Running the
> `cp` again later overwrites your existing `users.csv`.

This generates a `credentials-***.txt` file with a throwaway password for each
user you created.

Then open `http://<PUBLIC_HOST>:5005` and log in. After your first login, you are prompted to change your
password. Adding more users follows the same pattern, but make sure to not overwrite your `users.csv` file:

```sh
grep "KEYCLOAK_ADMIN_PASSWORD" .env  # this will show your password
cd keycloak-dev
nano users.csv          # add username and role (Admin or User)
KEYCLOAK_ADMIN_PASSWORD=<password from your .env file> ./create-users.sh
```

Passwords can be reset manually with

```sh
grep "KEYCLOAK_ADMIN_PASSWORD" .env  # this will show your password
cd keycloak-dev
KEYCLOAK_ADMIN_PASSWORD=<password from your .env file> ./reset-password.sh <username>
```

### What admins and users can see and do

| | User | Admin |
|---|:---:|:---:|
| Home, bug reports | ✓ (only their own bug reports) | ✓ |
| OHIF Viewer: view studies, run processing tools | ✓ | ✓ |
| Batch Processing: run tools, manage own jobs | ✓ | ✓ |
| Interactive Segmentation *(saminrad)* | ✓ | ✓ |
| iRODS: browse, upload, download, share *(irods)*  | not automatically, see [iRODS](#add-platform-users-as-irods-users) | not automatically, see [iRODS](#add-platform-users-as-irods-users) |
| Database (dcm4chee UI): browse, export, delete any study | | ✓ |
| PHI Access Log | | ✓ |
| Job Logs | | ✓ |
| iRODS → Manage Users *(irods)* | | only if rodsadmin, see [iRODS](#add-platform-users-as-irods-users)|
| Federated Learning *(airflow)* | | ✓ |


## Starting the optional modules

```sh
docker compose --profile irods    up -d   # iRODS data management
docker compose --profile airflow  up -d   # federated-learning orchestration
docker compose --profile saminrad up -d   # SAM2 interactive segmentation
docker compose --profile ldct     up -d   # low-dose CT simulation
docker compose --profile all      up -d   # everything
```

Profiles are additive and safe to re-run — adding one leaves the basis module
alone.

> **Platform users are not automatically iRODS users.** Every user created with
> `create-users.sh` is a Keycloak (platform) user only. Until they also get an
> iRODS account, the iRODS page tells them they have none, and they cannot use
> iRODS collections in Batch Processing.

### Add platform users as iRODS users

Make one user (must be Keycloak admin) an iRODS admin first, from the repository root:

```sh
docker compose exec irods-catalog-provider su - irods -c "iadmin mkuser <username> rodsadmin"        # user has no iRODS account yet
```

That user can then add everyone else
in the GUI under **iRODS → Manage Users**. Always use the exact username the
user already has in Keycloak, so single sign-on works.

If you want to upgrade an existing iRODS user to iRODS admin, run this from the repository root:
```sh
docker compose exec irods-catalog-provider su - irods -c 'iadmin moduser <username> type rodsadmin'  # user already has an iRODS account
```

## Layout

```
docker-compose.yml        all services via Compose `include:`
.env.example              adjustable variables
secrets/                  credentials you supply (e.g., Freesurfer license), gitignored

docker-context-gui/       portal (Flask): auth, audit, proxies
API/                      processing API: batch jobs, segmentation, surfaces
viewers/                  OHIF fork; the live recipe is
                          platform/app/.recipes/Nginx-Dcm4chee/
keycloak-dev/             Keycloak + InterACT realm
IRODS/                    iRODS catalog, provider, HTTP API
airflow/                  DAGs and trainer image for federated learning
docker-context-saminrad/  SAM2 interactive segmentation
LDCT_Alsaihati/           low-dose CT simulation
Documentation/            component documentation (start with Project_Structure.md)
```

Each stack keeps its own `docker-compose.yml`, pulled in by the root file. Always start
the project **from the repository root**.

## Configuration notes

**Behind a proxy.** `INTERACT_HTTP_PROXY` (and `INTERACT_HTTPS_PROXY`) is empty by default. Several containers
download model weights or atlases on first use; if this machine only reaches the
internet through a proxy, set it in `.env` and they will hang without it.

**Plain HTTP.** `COOKIES_INSECURE=1` ships as the default because a `Secure`
cookie is never sent over `http://`, and the login would loop forever. Set it
back to `0` as soon as there is TLS in front; see
`docker-context-gui/nginx-tls.conf` for a starting point.

**Storage paths.** `API_STORAGE_DIR` is bind-mounted at the *same path* inside
the containers as on the host. That is deliberate: the API launches sibling
containers through the host Docker socket and hands them paths it resolved
itself, so the two sides have to agree. Keep them equal if you change it.

### Details

`.env.example` marks all secrets you have to fill in with `<-- SET`. After copying it to `.env`,
generate all of them in one go:

```sh
./generate-secrets.py
```

This script fills in every blank secret, using a generator suited to each one's own
constraint. Secrets
that already have a value are left alone; pass `--force` to regenerate
everything, `--length N` to change the default length of the secrets that
don't have a fixed or capped size, and `--dry-run` to preview without writing.
It never touches `KC_SMTP_PASSWORD` -- that's your mail provider's password,
not something to generate.

Prefer to do it by hand instead? Here is how to do it:

```sh
openssl rand -base64 32                                    # most secrets
python3 -c 'import secrets; print(secrets.token_urlsafe(48))'   # Flask keys
python3 -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'
                                                           # OAUTH2_PROXY_COOKIE_SECRET
```


## If you are running more than one InterACT instance on the same server

Every container, network, volume, locally-built image, and every port
InterACT publishes to the host is derived from two things in `.env`:
`STACK_NAME` and the `PORT_*` variables. Give a second instance a different
`STACK_NAME` and a full set of non-overlapping `PORT_*` values and it runs
completely isolated alongside the first (separate
Keycloak realm and PACS data, separate Docker networks, nothing shared):

```sh
# second instance, e.g. a dev stack next to a production one
cp .env.example .env
nano .env    # STACK_NAME=dev, PUBLIC_HOST, and every PORT_* different from the other instance -- then fill in secrets
docker compose up -d
```

Two things to keep in mind:

- **`STACK_NAME`** must be lowercase letters, digits and hyphens only (it also
  has to be a valid Docker image-tag component). Two stacks with the *same*
  `STACK_NAME` on the same host are the same stack, not two. The second
  `docker compose up` just joins what the first already created.
- **Every `PORT_*` variable** in `.env.example` (not just the ones in the
  first block) has to differ between two instances running at once,
  including the lower-level dcm4chee (LDAP, Postgres, DICOM, HL7, WildFly
  admin) and `airflow-postgres` ports. None of these are used for
  container-to-container traffic (that always goes by service name over the
  shared network, regardless of `PORT_*`), so bumping them costs nothing —
  they only matter to tools outside Docker (a DICOM modality, a DB client)
  that need to reach a specific instance directly.

**Choosing the new ports.**

- Give each stack a fixed offset and add it to every default in
  `.env.example`, rather than picking numbers one at a time, e.g., the second instance is
  every default +1000 (`PORT_PORTAL=6005`, `PORT_KEYCLOAK=9081`,
  `PORT_DCM4CHEE_DICOM=12112`, ...).
- Check what's actually free before committing to a scheme:
  `ss -tlnp | grep LISTEN` (or `sudo lsof -iTCP -sTCP:LISTEN -P` if `ss` isn't
  installed) lists every port already bound on the host — including every
  other InterACT instance's dcm4chee ports, which won't show up any other
  way since they're not in that instance's own `docker ps`. This matters
  most for `arc`: it publishes seven ports on one container, so if even one
  collides the whole container — and everything depending on it — fails to
  start.
- Prefer ports above 1024. Nothing here requires a low port — 389 and 443 are
  only that low because they're LDAP's and HTTPS's conventional defaults, not
  because anything needs it — and staying above 1024 sidesteps any question of
  which user Docker needs privileges as to bind them.
- A `PORT_*` only needs to be reachable from outside the host if something
  outside Docker actually calls it. The
  dcm4chee admin ports (arc's own HTTPS, WildFly admin, LDAP, Postgres, HL7,
  DICOM-TLS) are therefore bound to `127.0.0.1` in the compose file: none of
  them go through Keycloak, and arc's HTTPS API/UI has no authentication at
  all. Use an SSH tunnel to reach them; Compose still needs a free number for
  each. Don't rely on a host firewall such as ufw instead — Docker-published
  ports bypass it.
- Every `PORT_*` value must be unique **within** a stack too, not just across
  stacks.

## Documentation

- [Project_Structure.md](Documentation/Project_Structure.md) — how the platform fits together: services, networks, configuration, data, security model
- [GUI.md](Documentation/GUI.md) — the portal: pages, proxies, batch page, PHI access audit trail, TLS
- [OHIF_Viewer_and_DCM4CHEE.md](Documentation/OHIF_Viewer_and_DCM4CHEE.md) — viewer, archive, oauth2-proxy, InterACT's changes to OHIF
- [API_and_API_storage.md](Documentation/API_and_API_storage.md) — processing API, batch pipeline, `API_storage/` and retention
- [Federated_Learning.md](Documentation/Federated_Learning.md) — multi-site training with Airflow
- [SAM.md](Documentation/SAM.md) — SAMinRAD interactive segmentation
- [iRODS.md](Documentation/iRODS.md) — research data management and sharing
- [Keycloak.md](Documentation/Keycloak.md) — identity, realm, user management
- [LDCT.md](Documentation/LDCT.md) — low-dose CT simulation
- [How_To_Add_New_Tools.md](Documentation/How_To_Add_New_Tools.md) — adding a tool to OHIF, batch processing and the GUI

## License

InterACT is released under the [MIT License](LICENSE).

Third-party components keep their own licenses: the OHIF viewer under
`viewers/` is MIT-licensed by the Open Health Imaging Foundation (see
[its LICENSE](https://github.com/OHIF/Viewers/blob/master/LICENSE)), and the container images InterACT pulls
(dcm4chee-arc, Keycloak, iRODS, Airflow, the segmentation models and others)
are licensed by their respective authors. Tools such as FreeSurfer, FSL and
TotalSegmentator have their own license terms, which you must obtain and comply
with separately.

## Funding

This project is funded by the European Union and the State of North
Rhine-Westphalia under the ERDF/JTF Programme NRW 2021–2027.

Dieses Projekt wird durch die Europäische Union und das Land
Nordrhein-Westfalen im Rahmen des EFRE/JTF-Programms NRW 2021-2027 gefördert.

