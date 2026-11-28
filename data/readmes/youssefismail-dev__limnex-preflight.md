# Limnex Preflight

**Scan machine-learning files for secrets, personal data and unsafe pickles *before* you publish them to Hugging Face,
Kaggle or GitHub.** It reads PyTorch and other pickles, safetensors, GGUF, ONNX, Keras/HDF5, NumPy, notebooks and archives.

Part of the Limnex family of AI-security tools ([limnex-uie](https://github.com/youssefismail-dev/limnex-uie)).

> **Status: v0.1, alpha.** Before you rely on it, read [what the evidence does and does not show](https://github.com/youssefismail-dev/limnex-preflight#evaluation-honest-version).
> In short: it is tested on cases I built, on 140 ordinary public models (80, then a fresh held-out set of 60, where it
> was also compared with gitleaks, TruffleHog and detect-secrets) and on my own ML projects. It has **not** been
> tested on real-world malicious model files.

**Quick start:** `pip install limnex-preflight`, then `limnex-preflight path/to/model-or-folder`. Exit code 1 means a
finding at MEDIUM or above. In GitHub Actions: `uses: youssefismail-dev/limnex-preflight@v0.1.2`
([setup](https://github.com/youssefismail-dev/limnex-preflight#use-in-github-actions)); before a commit: [pre-commit](https://github.com/youssefismail-dev/limnex-preflight#pre-commit).

> Why this exists: a model file I published contained my Kaggle user name inside a file path that the training
> framework had saved without my knowing. Nothing looked wrong in the file listing. This tool reads *inside* the file.

```text
$ limnex-preflight my-model/
my-model/sketchy.pkl
  [CRITICAL] unsafe-pickle-exec
      Pickle can execute code when loaded: os.system (os can run operating-system commands or import code)
      where: pickle offset 16 (STACK_GLOBAL)
      value: os.system    fingerprint: 430cb9a51931df9a

my-model/model.pt!/archive/data.pkl
  [HIGH    ] huggingface-token
      where: pickle offset 134 (BINUNICODE)
      value: hf_FA...45    fingerprint: c11e1c7ae9ab4438
  [MEDIUM  ] username-in-path
      Owner name inside a Kaggle models/datasets/notebooks path
      value: f********    fingerprint: 3b89230f4693ae18
  [LOW     ] hostname
      value: g********.corp.internal    fingerprint: 163f7124da9b8282

my-model/config.json
  [MEDIUM  ] email-address
      where: $.owner_email
      value: f***@g***.com    fingerprint: 5d0a7e21c94b3f86
  [MEDIUM  ] username-in-path
      where: $._name_or_path
      value: f********    fingerprint: 9be4c0a1d27f6e35

my-model/data/train.csv
  [MEDIUM  ] email-address  37 findings
      E-mail address
      first: line 2    value: a***@e***.org
      ... and 36 more in this file (-v lists each one with its fingerprint)

limnex-preflight 0.1.2: scanned 4 file(s): 1 critical, 1 high, 40 medium, 1 low
```

(Output shortened. Every value above is invented. Reports **never** contain a full secret or personal value.)

## Install and use

```bash
pip install limnex-preflight             # no dependencies
pip install "limnex-preflight[hdf5]"     # + h5py for Keras/HDF5
pip install git+https://github.com/youssefismail-dev/limnex-preflight     # or straight from the repository
```

```bash
limnex-preflight PATH...                    # files or folders; human-readable output
limnex-preflight models/ --format sarif --output report.sarif     # SARIF 2.1.0 (also: --format json); human report still printed
limnex-preflight models/ --json report.json --sarif report.sarif  # older spelling, same thing
limnex-preflight models/ --fail-on high     # exit 1 only for HIGH or CRITICAL findings (default: medium; none = report only)
limnex-preflight models/ --fail-on-incomplete   # exit 3 when any file could not be fully scanned
limnex-preflight model.pt --deep            # also carve provider-specific secrets out of raw tensor bytes (slow)
limnex-preflight -- -file-starting-with-a-dash.pkl
limnex-preflight --list-rules
```

In the human report, 4 or more findings at MEDIUM or below of the same rule and severity in one file are shown as one block
with a count and the earliest one as an example (the earliest line, or the smallest byte offset); `-v` lists each of
them with its fingerprint. HIGH and CRITICAL findings and unsafe-code findings are never grouped, because which secret or
which callable it is matters. Grouping is per file, so a folder of many files with one finding each still lists every
one. The totals, the exit code and the JSON and SARIF reports always count and list every finding, and the Action's job
summary lists each group's fingerprints in a fold-out list (up to 200 per group and 2000 in all; the rest are in the
SARIF and JSON reports).

`--format json|sarif` without `--output` writes only that report to stdout. A report file never replaces a path being
scanned or a file that is not a report of this tool (exit 2, nothing written), so a FILE right after `--json` or
`--sarif` cannot overwrite a model by mistake; inside a scanned folder only a JSON or SARIF report is replaced, so write a
text report (`-o`) outside it. Exit codes: `0` clean (or below `--fail-on`),
`1` findings at or above `--fail-on`, `2` usage error **or internal error** (an uncaught exception is never reported as `1`),
`3` some file could not be read/parsed, files were found but not one could be read ("nothing was checked"), or
(with `--fail-on-incomplete`) a file was not fully scanned (a corrupt file is not a clean
file; `--no-error-exit` turns the first case off). A path that does not exist is a usage error (`2`), whatever
`--no-error-exit` says. A truncated file is never reported clean: when only tensor data after a fully read header is lost
(`.npy`, safetensors, GGUF), every string was still scanned and it counts as reduced coverage (`0`, or `3` with
`--fail-on-incomplete`); when content that would be scanned is lost (a cut header, archive or compressed stream), it is an
error (`3`). The GitHub Action maps these to its own 0/1/2 contract, see below.

## Safety design

* **Nothing is ever loaded or executed.** Pickles are walked with `pickletools.genops` plus a small symbolic stack that
  tracks *data and references*; no callable is ever called, no module is ever imported
  (`tests/test_pickle.py::test_scanning_never_executes_anything` plants a pickle that would `touch` a file and a module
  that would write a marker on import, and checks neither happens). Every scanned file is treated as untrusted.
* **No network at scan time, no telemetry.** The package has no dependencies, imports no networking module
  (`tests/test_cli.py::test_no_network_imports`), and writes nothing except the reports you ask for.
* **Bounded.** Archive depth (6), members (20 000), per-stream decompression (512 MB), a zip-bomb ratio check, a total
  read budget. Zip and tar archives are read member by member, a compressed tar too (a `model.tar.gz` larger than 512 MB
  is still scanned; only a single member above the limit is left out and reported). A single compressed file (`.gz` of one
  file) is decompressed in memory up to 512 MB, and each member of a tar up to 512 MB is read whole, so a large archive
  can use up to about three times that member's size in memory for a moment (about 1.5 GB for a 512 MB member, measured
  by the fifth pre-release test; reading big members in
  pieces is planned for 0.2). An uncompressed zip member that is an HDF5 file (a `.keras` model's weights) is read in
  place, not copied into memory. At most 200 matches of one rule are reported per text (a file, a notebook cell, a
  string); when there are more, the report says so under "Reduced coverage". Nothing is ever extracted to
  disk. Symbolic links are followed only where that is safe: a path you name on the command line, a link from a Hugging
  Face cache snapshot to its own repository's `blobs/` folder or to the cache-wide blob store newer `huggingface_hub`
  versions keep (`<cache>/blobs/`; that is how the cache stores every file), or a link out of
  the scanned folder with `--follow-symlinks`; the Action never follows a link out of its workspace. A file's format is
  judged by its own name and its content, never by the name of a link to it; only a file without an extension (a Hugging
  Face cache folder keeps its files as hash-named blobs) is read by the name of a link to it, a model format's name
  before any other and a text name last, because `model.onnx` says more than the hash. No link is ever followed into
  `.git`, `.hg` or `.svn`. A file reached through several links is scanned once, under its own name when it is scanned
  anyway (in a Hugging Face cache, under the snapshot's name, never the blob's hash); a link to a folder that is scanned anyway is noted, not followed; a link into
  a place `--exclude` left out is left out too. A broken link named on the command line is a usage error (exit 2).
  Named pipes, sockets and devices are never opened (listed as not scanned). Only VCS internals (`.git`, `.hg`, `.svn`) are skipped by default;
  `.ipynb_checkpoints` and similar are scanned because they get published too. `--exclude` leaves out more, explicitly:
  there is no default list such as `node_modules` or `.venv`, because a folder name would then be enough to hide a file
  from the Action. Every exclusion is reported ("Left out on purpose"), and since it is a choice, not a gap, it does not
  count as incomplete for `--fail-on-incomplete`. In the Action, `exclude` applies with `changed-only` too.
  A length or count field in a damaged file never makes it allocate more than the file actually holds. Before the
  fuzzing round, a 14-byte pickle could ask for 4 GB and a 2.6 KB GGUF for 20 GB; see section 4 of the evaluation.
* Reports contain **masked values only** (`hf_ab...9Z` style: provider prefix + at most 2 characters on each side).
  Fingerprints are truncated SHA-256 of rule + file name + value; for secrets they cannot be reversed, for low-entropy
  personal values (a user name) a guesser who already has a candidate can confirm it.
* The optional HDF5 reader (`h5py`) parses with libhdf5, a C library. A hostile HDF5 file could in principle attack that
  parser. Without `h5py` the file is scanned as raw strings instead (and the report says so under "Reduced coverage").
  `h5py` runs in a separate process that reports its progress; when it makes no progress for 10 s (a damaged 11.5 KB file
  once made it loop forever on Linux builds) it is stopped and the file is scanned as raw strings, with the reduced
  coverage reported. A healthy file is never cut short for being big. `LIMNEX_PREFLIGHT_HDF5_STALL_SECONDS` changes the 10 s.

## What it scans

| Format | What is looked at | How |
|---|---|---|
| PyTorch `.pt` `.pth` `.ckpt` `.bin` (zip) | every pickle inside (`data.pkl`, `constants.pkl` ...), member names, small text members | zip + static pickle analysis; raw tensor storages skipped unless `--deep` |
| PyTorch legacy (pre-1.6) | the five pickles of the legacy layout | static pickle analysis |
| `.pkl` `.pickle` `.joblib` `.sav` `.dill` ... | every opcode string/bytes; imports (`GLOBAL`/`STACK_GLOBAL`/`INST`) | static pickle analysis; several pickles per file; under any other name too (a loader does not look at the name), a file that starts with the protocol 2+ marker or is one whole protocol-0/1 pickle; zlib/gzip/bz2/xz/lzma-compressed files (joblib's `lz4` mode cannot be decompressed without a dependency, so such a file is a MEDIUM "not analysed" finding under any name); joblib's inline NumPy number arrays are skipped by length, string arrays (class labels ...) are read element by element, in joblib files and in pickled arrays alike; pickles hidden in `bytes` objects are followed |
| NumPy `.npy` | header, object-array pickle, `U`/`S` string arrays (per element) | static |
| NumPy `.npz`, any `.zip`, `.whl`, `.keras` | every member, recursively; member names; zip comment | member by member |
| `.tar` `.tar.gz` `.tgz` `.tar.bz2` `.tar.xz` | members, recursively | member by member, straight from the decompressor |
| `.gz` `.bz2` `.xz` of one file | the decompressed content | in memory, up to 512 MB |
| safetensors | JSON header: `__metadata__`, tensor names | header only |
| ONNX | `producer_*`, `doc_string`, `metadata_props`, graph/node/tensor/value names, string attributes, string tensors, external-data paths | built-in protobuf reader (no `onnx` package); raw tensors skipped unless `--deep` |
| Keras / HDF5 `.h5` `.hdf5` `.keras` | all attributes (incl. `model_config` JSON, `training_config`), object names, small string datasets; Keras `Lambda` layers | `h5py` if installed, else raw strings |
| CatBoost `.cbm` | printable strings (training options JSON, paths, build info) | string carving |
| GGUF | metadata keys and values (names, authors, chat template, tokenizer data), tensor names | header parser; works on a truncated file |
| Jupyter `.ipynb` | source of code **and** markdown cells, **outputs** (stream, errors/tracebacks, display data), cell and notebook metadata; images skipped | structured, with `cell 3 (code) output 1 (stream stderr), line 2` locations |
| `.json` `.jsonl` `.yaml` `.yml` `.txt` `.cfg` `.ini` `.toml` `.md` `.env` `.conf` `.log` and small unknown text files | every string value and key; JSON locations like `$.config.layers[0].name` | structured for JSON, line-based otherwise |

Files that are not recognised are listed under **Not scanned** — never silently skipped.

## What it finds

Run `limnex-preflight --list-rules` for the full catalogue. Every finding has: file (with the archive chain, e.g.
`a.zip!/inner/model.pt`), location inside it (pickle offset, JSON path, notebook cell, line), rule, severity, masked
value and fingerprint.

| Category | Rules (severity) |
|---|---|
| **Secrets**, provider-specific | AWS access key ID and secret key/session token; Google API key, OAuth client secret, service-account key id; Azure storage/shared-access keys, SAS tokens, AD client secrets; GitHub (classic + fine-grained), GitLab; Hugging Face; OpenAI; Anthropic; Kaggle (`kaggle.json`, `KAGGLE_KEY`, `KGAT_`); Weights & Biases; Replicate; Groq; Databricks; Slack tokens + webhooks; Stripe; Twilio; SendGrid; npm; PyPI; DigitalOcean; Telegram; PEM / OpenSSH / PGP private keys; JWTs (header must decode and contain `alg`); passwords inside URLs; `Authorization:` headers (HIGH; PEM is CRITICAL; Stripe test keys MEDIUM) |
| Secrets, generic | `password`/`secret`/`api_key`/`token`-style assignments, also through environment variables in code (`os.environ['DB_PASSWORD'] = ...`, `os.environ.setdefault(...)`, `os.putenv(...)`), and `--password=...` style command lines (MEDIUM); high-entropy strings (LOW) |
| **Personal data** | user name in `C:\Users\<name>`, `/home/<name>`, `/Users/<name>`, WSL, `/kaggle/input/{datasets,models,notebooks}/<owner>/` (MEDIUM); `/kaggle/...` and `/content/drive/...` paths naming a dataset or folder (MEDIUM; the bare Kaggle working directory LOW); e-mail addresses (MEDIUM; role mailboxes such as `info@` LOW); IPv4 (private ranges always, public only with host-like context) and full-form IPv6 (LOW); internal/machine host names (`*.internal`, `*.corp`, `*.local`, cloud VM names, `runs/<date>_<host>` Trainer directories) (LOW); user-name and host-name fields |
| **Unsafe code** (a separate category and severity track) | pickle imports that run code: `os`, `posix`, `nt`, `subprocess`, `builtins.eval/exec/compile/__import__`, `runpy`, `importlib`, `ctypes`, `types.FunctionType`, ... (CRITICAL); network/file-system access: `socket`, `urllib`, `shutil`, `sys`, `builtins.open` (HIGH); `getattr(x, name)` is judged by its attribute name, fail-closed (see below): known-dangerous or computed names (`system`, `execvp`, `spawnvp`, `posix_spawn`, `run_path`, `exec_module`, `write_text`, any `__dunder__` ...) HIGH, a tiny allow-list (`forward`) and exact fastai (module, class, method) triples quiet (see "fastai learners" below), **every other name a MEDIUM `pickle-getattr-review` finding**; loaders such as `torch.load`/`pickle.loads` on data that could not be analysed (HIGH); Keras `Lambda` layers (HIGH); a pickle that could not be analysed to its end, or an import that cannot be resolved (MEDIUM); data after the last pickle (LOW); an archive member name that leaves the extraction folder, `../` or an absolute path (MEDIUM `archive-path-traversal`) |
| **Not the file** | a Git LFS pointer instead of the file it stands for (MEDIUM `git-lfs-pointer`: `actions/checkout` fetches LFS files only with `lfs: true`) |

### Detection thresholds (all constants in `limnex_preflight/detectors.py`)

| Setting | Value |
|---|---|
| High-entropy candidate length | 24–128 characters of `[A-Za-z0-9+/_-]`, not a UUID, not a hash-length pure-hex string (32/40/56/64/96/128), not a path/URL segment |
| Entropy threshold | **4.5 bits/char** (base64-like), **3.0 bits/char** (pure hex of other lengths); a candidate must contain letters *and* digits, and be less than 30 % made of 3+-letter words |
| Credential assignment value | ≥ 8 chars and entropy ≥ 3.0 (≥ 6 chars and ≥ 2.0 for `password`-style names); placeholders (`your…`, `example`, `<token>`, `${X}`, `xxxx`) and code references (`os.environ[`) are ignored |
| Standalone entropy hits are LOW | so the default `--fail-on medium` does not fail CI on them |

Provider-specific patterns do **not** go through the placeholder filter. The documented AWS example key
(`AKIA` + `IOSFODNN7EXAMPLE`) is reported; put it in `.preflightignore` if you really mean to ship it.

Several deliberate choices are visible in the rules, because they came out of testing on real models (see below):
generic account names (`ubuntu`, `runner`, `Public`, `jovyan` ...) are not "user names"; a
library's own `Author: Name <mail> ... commit_hash:` build block (CatBoost writes one into every `.cbm`) is not the
publisher's e-mail.

**How `getattr` is handled (fail-closed).** `getattr` cannot be banned by import: pickle stores an unbound method as
`getattr(Class, "forward")`, and common detection-model checkpoints contain exactly that. So it is judged at every
call opcode (`REDUCE`, `INST`, `OBJ`, `NEWOBJ`) by its attribute name: known-dangerous name, `__dunder__` name, module
alias (`_os`) or a *computed* name → HIGH `unsafe-pickle-io` (checked first, so no allow-list can make it quiet);
allow-listed name → quiet; **any other name → MEDIUM
`pickle-getattr-review`, never silently dropped** (so the default `--fail-on medium` stops until a human looks or accepts the
fingerprint). A `getattr` or loader that is merely *handed over* (e.g. to `functools.partial`) and never called directly is
reported as well. The allow-list (`GETATTR_ALLOWED` in `pickle_scan.py`) is `{"forward"}`, derived from data: the 80
evaluation repositories contain exactly three `getattr` calls, all of this benign `getattr(<model class>, "forward")` kind,
in the tuning set (none in the held-out set). It is small on purpose; extend it only with a benign checkpoint to point at.

**fastai learners (0.1.1).** fastai keeps some of its own methods on the objects it saves (`dataloaders`, a transform's
`before_call`, a U-Net hook's `hook_fn`) or takes them from a class (`PILMask.create`), so a fastai export holds
`getattr(<fastai object or class>, <method>)` (fastai 2.7 and earlier, saved with Python's pickle) or a bound method
written by cloudpickle (fastai 2.8, below), and in 0.1.0 every one of them failed the default threshold. The quiet
pairs now come from fastai's own source (2.7.19 and 2.8.12, read as text, never run): every fastai method that fastai's
code uses as a value, on every fastai class that reaches it by normal attribute lookup, 193 exact (module, class,
method) triples (`FASTAI_GETATTR_ALLOWED`; the list is generated, see `fastai_pairs.py`). A method that fastai adds to a
class from another module (fastcore's `@patch`) is listed under both modules, because Python 3.13 and later name the
class through the method's module. Only exact pairs count, and only on an object the pickle
creates by naming that class (`NEWOBJ`, `OBJ`, `INST`, `copyreg._reconstructor`) or on the class itself, and only while
its saved state cannot have changed its class (a `__class__` key in a state the scan can read, or a state it cannot
see, puts it back under review): fastcore's `GetAttr` hands a name that a class does not define to another object, which a
file could choose. The scan follows names as the file writes them; a file built to change what a name means while it
loads is outside what it models, the same limit as protocol-4 dotted names (below). A dangerous name stays HIGH on any class, a user's own subclass
(`__main__.MyLearner`) stays under review, and calling the method from the pickle is still `pickle-computed-callable`.
This gives a malicious file nothing new: fastai is not on the deny-list, so a pickle could already name the same fastai
function directly. Text models that tokenize with spaCy keep up to four review findings (`spacy`'s `pipe`, and the
regular-expression `search`, `match` and `finditer` that spaCy's tokenizer stores), all outside fastai.

**fastai 2.8 saves with cloudpickle.** From fastai 2.8, `Learner.export` uses cloudpickle, which writes the same bound
methods as `_builtin_type('MethodType')(<function>, <object>)`, a call on what a call returned. That is quiet under the
same rule: the function is named through its class with a listed triple, and the object was made by naming a class
listed for that name (and its state cannot have changed its class). Any other use of `_builtin_type`, functions and classes stored as code, bindings outside fastai, and
calling the bound method stay `pickle-computed-callable`. **fastai 2.8 image and segmentation learners still fail the
default threshold:** cloudpickle cannot write fastai's `PILImage.create` / `PILMask.create` (a classmethod that
`ImageBlock` and `MaskBlock` keep) by name, so it stores the compiled code of `PILBase.create` in the file:
one `pickle-computed-callable` finding for the code and one for each image or mask class it is bound to (2 for an
image classifier, 3 for a segmentation learner). A static scan cannot tell fastai's compiled code from anyone else's,
and that code runs when the model is used, so it stays reported. Functions and classes the model's author wrote (a
label function, a lambda in a `DataBlock`, a custom transform) are stored as code too, and are reported the same way.
For a model you exported yourself, look at the findings and accept their fingerprints; they include the position in
the file, so they can change when you export again (see the ignore file below). For someone else's fastai 2.8 image
model, Preflight cannot tell fastai's code from a modified version: accept it only if you trust where it comes from.
With the first list (11 pairs seen in 20 public repositories), on 20 held-out fastai repositories (23 files) that were
picked before the fix and opened only after it, files failing the default threshold went from 23 to 4. With the list
from fastai's source, on 20 further held-out repositories (20 files, picked by rank after the list was fixed), they went
from 20 to 1; the one left is a regular expression's `search`, outside fastai. On 20 public fastai 2.8 exports, opened
only after the cloudpickle rule was written, `pickle-computed-callable` findings went from 225 to 42 and no fastai method
was left under review, but all 20 still fail: 10 only on the stored `create` code, the others also on spaCy, their
author's own code or personal data. No other finding changed in any of the 110 files checked (the 64 of the earlier
sets, 24 of the fastai 2.8 study and 22 of its held-out set; the file lists are kept private) (CHANGELOG, 0.1.1).
The dangerous-name list is a prioritisation aid; the review finding is the safety net for surprises in honest files, not a
barrier that a file written to avoid it cannot get around (protocol-4 dotted names, below).

**Calls a static scan cannot identify (fail-closed, added in the pre-release review).** When a pickle calls an object that is
itself the *result of another call* (a resolver or factory returns a function, which is then called), what runs cannot be
known without executing it, so it is reported as a MEDIUM `pickle-computed-callable` review finding. Protocol-4 dotted names
(`pathlib.Path.unlink`) are judged by the method they reach, by the same dangerous-name list `getattr` is judged by, and
the C-module names of listed callables (`_operator.methodcaller`) are listed too. Unlike `getattr`, a dotted name that
reaches any *other* method is not sent to review: a pickle can name and call such a method with no finding, in 0.1.0
and 0.1.1 alike. So the `getattr` review tier catches surprises in honest files; a file written to avoid it can, and is
caught only if what it reaches is on the dangerous-name lists. These rules were added in review after probing the
deny-list; they hold on this repository's benign fixtures (scikit-learn, PyTorch, joblib), but, like the `getattr` review
tier, they have no real-world evidence yet.

## Accepting a finding: `.preflightignore`

```text
# .preflightignore  (one fingerprint per line; ./.preflightignore and one in each folder named on the command line are read)
f20fdec205d55c2c   # my own Colab folder is public on purpose
98f3c1926c87758e
```

* Entries are **fingerprints of individual findings** (shown in every report), never rule names. A line that is a rule
  name, a glob or anything but 16 hex digits is rejected (exit code 2). There is no way to switch a rule off.
* The fingerprint covers rule + file name (+ archive member) + value, not the directory and not the offset, so it
  survives moving the checkout and re-saving the file, but a *different* value in the same file is still reported.
  Two pickle rules have no value to name and use the opcode's position instead (`pickle-computed-callable`,
  `pickle-unresolved-global`): their fingerprints change when anything before them in the file changes length, for
  example when a model is exported again, and the finding comes back for review.
* `--show-ignored` lists what was suppressed; entries that matched nothing are reported as stale.
* The ignore file is read from the scanned folder, so when you scan **someone else's** repository or a downloaded model,
  add `--no-ignore`: its author could otherwise have accepted their own findings in advance. The summary always shows
  how many findings an ignore file suppressed.

## Use in GitHub Actions

The scanner is also a **composite GitHub Action** (`action.yml` at the root of the repository). It installs the scanner from
the action's own checkout (not from PyPI) into a private virtual environment, so your own Python and dependencies are not
touched. The examples use the `v0.1.2` tag for readability; in real workflows pin actions to a full commit SHA.

**Minimal** (scan `models/` on every pull request; fails on MEDIUM and above, the default):

```yaml
jobs:
  preflight:
    runs-on: ubuntu-latest
    timeout-minutes: 15                # a hung step must not hold the runner for GitHub's default 6 hours
    steps:
      - uses: actions/checkout@v7      # in real workflows pin to a full commit SHA, see examples/
        with:
          fetch-depth: 0               # on pull requests the ignore file is read from the base commit
          persist-credentials: false   # the job's token is not left in .git/config
          lfs: true                    # weights kept in Git LFS are checked, not their pointers
      - uses: youssefismail-dev/limnex-preflight@v0.1.2
        with: { path: models/ }
```

**Full** (pull requests: changed files only; pushes to main: everything; SARIF in the Security tab) is in
[`examples/github-action-full.yml`](https://github.com/youssefismail-dev/limnex-preflight/blob/main/examples/github-action-full.yml),
the minimal workflow in
[`examples/github-action-minimal.yml`](https://github.com/youssefismail-dev/limnex-preflight/blob/main/examples/github-action-minimal.yml).

```yaml
permissions:
  contents: read
  security-events: write         # only because upload-sarif is on
steps:
  - uses: actions/checkout@v7
    with: { fetch-depth: 0, persist-credentials: false, lfs: true }   # history for changed-only; LFS files
  - uses: youssefismail-dev/limnex-preflight@v0.1.2
    with:
      path: models/
      fail-on: medium
      changed-only: ${{ github.event_name == 'pull_request' }}
      sarif-file: preflight.sarif
      upload-sarif: "true"
      fail-on-incomplete: "true"
```

### Inputs

Yes/no inputs take `true` or `false` (any case, no surrounding spaces); anything else stops the run with exit 2.

| input | default | meaning |
|---|---|---|
| `path` | `.` | One file or folder (relative to the workspace). Spaces, newlines and a leading dash in the name are fine. |
| `fail-on` | `medium` | `high`, `medium`, `low` or `none` (report only). Fails when a finding at or above it exists. The default matches the CLI, so the MEDIUM review findings (`pickle-getattr-review`, `pickle-computed-callable`, an unresolved or incompletely analysed pickle) stop the build until a human looks. |
| `changed-only` | `false` | Scan only the files changed by the pull request (merge base → HEAD) or push (`before..sha`), on `push`, `pull_request` and `pull_request_target` (there only when the pull request's head is checked out: on that event the default checkout is the base branch, and then everything is scanned). Changed files are scanned **whole**, and each path is decided exactly as a full scan of `path` decides it (links, `exclude`, fingerprints). Needs enough git history (`fetch-depth: 0`); on the first push of a branch, a shallow clone, a missing base commit or any other event it scans **everything** and says so in the log and the job summary. Files outside `path` are ignored; deleted files are skipped; the ignore file of `path` applies exactly as in a full scan. |
| `sarif-file` | empty | Write a SARIF 2.1.0 report (masked values only) here. Empty = none. Never written through a symbolic link (exit 2). |
| `deep` | `false` | Also carve provider-specific secrets out of raw tensor payloads (slow). |
| `fail-on-incomplete` | `false` | Fail when a file could not be fully scanned: unreadable, "Not scanned", budget exhausted, reduced coverage. |
| `exclude` | empty | Patterns to leave out, one per line, as the CLI's `--exclude` (`.venv`, `data/*.csv`). Nothing is left out by default; every exclusion is reported. |
| `upload-sarif` | `false` | Upload the SARIF file with `github/codeql-action/upload-sarif`. Off by default. Without `sarif-file` nothing is uploaded, and the log warns. |
| `sarif-category` | `limnex-preflight` | Code-scanning category when uploading. |
| `base`, `head` | empty | Advanced: compare these revisions instead of the event's (for `changed-only`). Without `changed-only` they are ignored, and the log warns. |
| `python-version` | `3.12` | Python for the scanner's own virtual environment. |

### Outputs

`findings-total`, `findings-critical`, `findings-high`, `findings-medium`, `findings-low`, `findings-info`,
`highest-severity` (`critical` … `none`), `files-scanned`, `files-not-scanned` (the number of entries under "Not
scanned": an unsupported file, a link that is not followed, an archive member left out ..., and files whose scan failed;
the same number as in the log and the job summary), `sarif-path`, `exit-code`.

### Exit status (tested in `tests/test_ci_action.py`)

| code | meaning |
|---|---|
| **0** | nothing at or above `fail-on` (and, with `fail-on-incomplete`, every file was fully scanned) |
| **1** | findings at or above `fail-on` |
| **2** | scanner error: invalid input (bad `fail-on`, missing `path`, malformed ignore file), a crash — never reported as 1 —, a full scan that found files but could read none of them ("nothing was checked"; not with `changed-only`, where a change that touches no scannable file is normal), or, only with `fail-on-incomplete`, a file that was not fully scanned |

Findings win over "incomplete" when both apply. To react to the code yourself use `continue-on-error: true` and
`steps.<id>.outputs.exit-code` (best effort when the step fails) or `steps.<id>.outcome`.

### What you see in the run

* a **job summary** (Markdown table: counts per severity, the findings with masked values, the "Not scanned" list);
* **annotations** with file and line (`::error` for critical/high, `::warning` for medium, `::notice` for low), at most 10 per
  level, then a "+N more" line;
* optionally the **Security tab** (SARIF). Code scanning is **free on public repositories** and needs **GitHub Advanced
  Security on private ones**; without it leave `upload-sarif` off (the SARIF file is still written if you ask for it).

Everything shown contains **masked values only**. This includes the cases where a secret is not a value but a JSON key, a
tensor name or an archive member name: locations and member names are re-masked before they are printed
(`tests/test_ci_masking.py` plants every fixture secret in all those places and checks the SARIF, the summary, the
annotations and the log). The file path you passed in `path` is shown as is.

### Permissions

| you use | needs |
|---|---|
| scanning, summary, annotations | `contents: read` |
| `upload-sarif: "true"` | additionally `security-events: write` (and Advanced Security on private repositories) |

### Security properties of the action

* No `${{ inputs.* }}` or `${{ github.event.* }}` is ever placed inside a `run:` script: inputs travel through `env:` and are
  read by the scanner from the environment, so a path or ref cannot become shell code (`tests/test_ci_files.py` enforces
  this for every workflow and for `action.yml`).
* Every third-party action is pinned to a **full commit SHA** (version in a comment).
* Every Python call runs isolated: `python -I` (the install step's `venv` and `pip` too), and the scanner's h5py helper
  process with `-E` and without the working directory on its import path. So the scanned repository's working
  directory is never on `sys.path`, and a `json.py` in a pull request cannot shadow the standard library.
* No symbolic link is followed out of the workspace, not even when the scanned `path` itself is one: a pull request could
  otherwise turn that folder into a link to the runner's own files and get their findings printed in the log. No link
  is followed into `.git`, `.hg` or `.svn` either (`actions/checkout` keeps the job's token in `.git/config` unless
  `persist-credentials: false`, as in the examples); values are masked in any case.
* The SARIF report is never written through a symbolic link: if the `sarif-file` path, or a folder on the way to it inside
  the workspace, is a link (which a pull request could commit), the run stops with exit 2 instead of overwriting a file
  outside the workspace.
* The ignore file is never read through a symbolic link either: if `.preflightignore`, or a folder on the way to it, is
  a link (in the checkout, or on a pull request in the base commit), the run exits 2. A pull request could otherwise
  point it at any file on the runner. An invalid entry is reported by its line number only, so no file content reaches
  the log. On a pull request the pull request's own ignore file is not applied, so a problem in it does not stop the
  scan: everything is scanned and reported first, then the run exits 2.
* Workflow commands in file names (`::error::...`, `::set-output ...`) cannot be forged: output is wrapped in
  `::stop-commands::`, annotation text is escaped, and `$GITHUB_OUTPUT` uses random heredoc delimiters.
* Git is called with an allow-listed command line; revisions are validated and resolved to SHAs first.
* **A pull request cannot silence its own finding.** On `pull_request` events the action reads `.preflightignore` from
  the pull request's **base** commit, not from the pull request (`limnex_preflight/ci/trusted_ignore.py`). With
  `actions/checkout`'s default shallow clone the base commit is fetched (that commit only); if it still cannot be read,
  **no** ignore entry is applied and a warning annotation says so (`fetch-depth: 0` avoids it). Until the pre-release test
  this case fell back to the pull request's own file, which let a pull request silence its own finding. A direct push to a
  branch still uses that branch's file, so require code-owner review for `.preflightignore` as well.
* Network: the scanner has none. When the action installs itself, `pip` fetches the build backend (setuptools) and, for
  Keras/HDF5, `h5py` and `numpy` from PyPI, at the **exact versions pinned in `action-constraints.txt`**, which binds
  both the install and pip's build environment (`PIP_CONSTRAINT` and `PIP_BUILD_CONSTRAINT`; one pin per
  Python range, checked by `tests/test_ci_files.py`).

### What the action does NOT catch

The same limits as the CLI (see below): transformed secrets (base64, split, UTF-16), raw tensor bytes unless `deep`, images,
formats that are only listed as "Not scanned", unsafe pickle calls to unknown third-party code, and verification of live keys.
With `changed-only` it additionally cannot see a problem in an **unchanged** file; run a full scan on `main` or on a
schedule. A file that is not supported shows up under "Not scanned" and, with `fail-on-incomplete`, fails the run.

## pre-commit

`.pre-commit-config.yaml` of the repository that publishes the models (same options and default as the action:
`--fail-on medium`; add `--fail-on-incomplete` for the strict mode). The hook passes files by name: every extension the
scanner handles (in any case), `.env` files (`.env.local` too) and files without an extension. The CLI and the Action
also read other files by content (a pickle saved as `model.data`, a small `.csv`); to pass every staged file to the
hook as well, add `files: '.*'` under the hook in your config:

```yaml
repos:
  - repo: https://github.com/youssefismail-dev/limnex-preflight
    rev: v0.1.2
    hooks:
      - id: limnex-preflight
        files: '^models/.*'                        # optional
        # args: ["--fail-on", "medium", "--fail-on-incomplete", "--"]   # keep the trailing --
```

The hook passes every file type the scanner handles (the same extensions as the CLI, `.env` files included; a test keeps
the two lists in step).

## What it cannot find

Stated plainly, and pinned by tests in `tests/test_limits.py` and measured in `evaluation/results/fixture_detection.md`:

* **Anything transformed.** A secret that is base64-encoded, split over two fields, reversed, hex-escaped, or stored as
  UTF-16 inside a binary is not found. Compressed or encrypted payloads inside unsupported containers are not opened.
* **Raw tensor bytes** (default). Weights are skipped. `--deep` carves *provider-specific* patterns out of them (ASCII
  only); it does not run the entropy or personal-data rules there, because float bytes would make them meaningless.
  `--deep` reads at most the first 4 GiB of one payload and reports the rest as skipped.
* **Images** (notebook outputs, PNG metadata) are skipped; **ONNX/safetensors external data** files are separate files
  and only scanned if you pass them and they are a supported type; TensorFlow `SavedModel` (`.pb`), TFLite, Core ML,
  OpenVINO, `fasttext` `.bin` and other formats are reported as "not scanned".
* **Formats known only by name.** ONNX has no signature, so an ONNX file under another name (or a hash-named file
  reached through a link with another name) is read as text, not as a model; safetensors under a text name likewise.
  Pickles, compressed joblib files (zlib, bz2, gzip, xz, lzma) and the other formats are recognised by their content
  under any name.
* **Old pickles with other data after them.** A pickle in protocol 0 or 1 has no marker byte. Under a name that is not
  a pickle extension it is analysed when the whole file is that one pickle (joblib's array bytes after it included,
  read the way joblib reads them); followed by other bytes, it is scanned as text or reported "Not scanned", not
  analysed as a pickle. Inside joblib's own zlib or `.lzma` wrapper, or a compressed file with a pickle name, the
  content is always analysed as a pickle, and content that does not parse is a MEDIUM incomplete-analysis finding.
* **Personal data you wouldn't recognise as a pattern**: a real name in a free-text field, a face in a dataset
  sample, a user name that is not in a path or a user-name field, a company-internal URL on a public domain, a public
  IP address in running text.
* **Unsafe pickles are a deny-list.** It knows the usual dangerous callables, not what an arbitrary installed package
  does when called (`some_pkg.run_payload` is not flagged). A deny-list is weaker than an allow-list; for untrusted
  files the answer is still *do not unpickle them* — prefer safetensors. `getattr` is judged by its attribute name
  (allow-list / dangerous list / review), which is a heuristic: a benign-looking name from an unknown package ends up as a
  MEDIUM review finding, not as a pass. A review on 2026-11-11 found more callables that other public scanners list and
  this one does not yet; until an allow-list review tier replaces the deny-list as the main line (planned for 0.2), treat
  a clean result on an untrusted pickle as "nothing known found", not as "safe".
* **GGUF chat templates** are checked for secrets and personal data only. Some loaders run the template as code; whether
  a template does something unexpected is not judged (planned for 0.2).
* **Large HDF5 string datasets** (more than 10,000 entries) and HDF5 parts that h5py cannot read are reported as reduced
  coverage, not scanned. ONNX `training_info` graphs are not read.
* **Verification.** It never contacts a provider to check whether a key is live (no network is the point).
* **Git history.** It scans files, not commits.
* Strings shorter than 6 characters are never examined; very large text is capped (256 MB).
* **Datasets.** Data tables (`.csv`, `.tsv` and other unlisted extensions) are read as text only up to 8 MB; larger ones
  are reported as "not scanned". Scanning a whole dataset needs its own design (see section 5 of the evaluation).
* **Damage inside bytes it never parses.** A file cut short is reported as incomplete, except when the cut falls inside
  bytes that are skipped by design: the extra parts after a CatBoost model's core, and the raw tensor bytes at the end
  of a legacy (pre-1.6) PyTorch file. Those cuts are not detected (counted as "known limit" in `evaluation/results/fuzz.md`).
  An ONNX file cut exactly between two of its top-level fields is itself a complete, valid file (ONNX's own checker
  accepts it), so no reader can see that cut; what was cut off is simply not there to scan.

## Evaluation (honest version)

**What the evidence does and does not show, at a glance:**

| claim | evidence | how much it is worth |
|---|---|---|
| It finds the secrets, personal data and unsafe pickles it was built for | planted fixtures, all found (section 1) | a **regression suite**: I wrote both the fixtures and the rules |
| It is quiet on ordinary public models | 80 Hugging Face repositories (section 2) | the **held-out first look** is the honest figure: 2 false alarms in 2 of 40 repositories. The final numbers include fixes made after seeing the data |
| It stays quiet on a *fresh* sample and does not choke on large files | 60 more Hugging Face repositories (10 each of PyTorch pickle, safetensors, GGUF, ONNX, Keras, scikit-learn/joblib) plus 3 files of 4-6 GB, disjoint from section 2, drawn by a rule committed before the first download (section 6) | **held-out, benign only.** 528 files, 0 scan errors. 19 findings of MEDIUM or above, hand-labelled: 15 true or intended, 4 false or unclear. **False alarms in 2 of 60 repositories (3%, 95% CI 1-11%).** Hugging Face's own flags filtered the draw, so no malicious file could be in it |
| On real files it finds leaks that general secret scanners miss | the same 60 repositories, also scanned by gitleaks, TruffleHog and detect-secrets (section 3) | **keys and passwords: a benign sample cannot rank the tools on finding keys**; what separates them there is false alarms. **Personal data inside model files: 4 real leaks that only Preflight found** (the others have no rules for it) |
| It catches real-world attacks | **none** | **not tested on real-world malicious model files.** The 80 repositories contained no unsafe pickle and no real credential, so the unsafe-code and secret rules have no real-world true positive to show |
| It catches more than picklescan / ProtectAI `modelscan` | 19 malicious + 4 benign cases (section 3) | **home-field advantage**: every case was built by me, around what I had implemented. No cases come from the other tools' test suites |
| Damaged files do not crash it, hang it or pass as clean | 6,300 randomly damaged benign files (section 4) | 0 failures after fixing the 38 that the first run found. A pre-release test on Linux then found one damaged Keras file that hung h5py; fixed (section 4). Random damage, not a deliberate attacker |
| It is useful and quiet on real ML work | my own projects: 1,366 files, 72 trained models (section 5) | **one author's files**, not a sample. 0 unsafe-code false alarms, one real leak found in a published model; the scanner fixes it led to were made after seeing these files |

Everything below is regenerated by scripts in `evaluation/` and the raw (masked) outputs are in `evaluation/results/`.

**1. Planted fake values, 21 format fixtures × 31 planted items** (`evaluation/fixtures.py`; secrets are assembled from
fragments at run time, so no secret-shaped literal exists in this repo; AWS values are the documented examples):
651/651 detected, 0/21 clean twins with findings, 41/41 malicious pickle/Keras cases flagged (19 original + 22 `getattr` cases: 16 dangerous names, an unknown name, `INST`/`OBJ` call forms, a computed name, an indirect reference, a loader through `INST`), 0/4 benign flagged (including a YOLO-style `getattr(Detect, "forward")` checkpoint).
**Read this as a regression suite, not as an accuracy claim:** I wrote both the fixtures and the rules. It did find
real bugs while I was building it (fixed-width NumPy string arrays running neighbours together; nbformat tracebacks
having no line terminators), which is what it is for.

**2. Real public models: 80 Hugging Face repositories, 702 files, 2.6 GB** (`evaluation/hf_models*.txt`; pinned by commit
SHA in the manifests (dropped for pseudonymised repositories); full files for small weights, only the header for `.safetensors` and the first 16 MB for `.gguf`
— 42 files were read partially). Three gated repos (HTTP 401) were dropped and not replaced. Findings were each read in raw context by a
human (the raw context is not stored). I tuned the rules on the first 40 repos, then scanned a **disjoint 40** that I
had chosen before looking at any result:

| run | findings | real leaks | intended (e.g. README contact) | library-vendor data | **false alarms** |
|---|---|---|---|---|---|
| first version, tuning set | 100 | 1 | 3 | 4 | **92** (79 "entropy", 5 IP, 3 `getattr` rated HIGH, 3 non-pickle `.bin` weight files parsed as pickles, 1 code line, 1 tensor-by-value loader) |
| first version, held-out set | 69 | 6 | 6 | 10 | **47** |
| tuned rules, held-out, *first look* | 14 | 6 | 6 | 0 | **2** (code lines that read an API key from an object attribute) |
| final rules, both sets | 21 | 11 | 9 | 0 | **1** (a vocabulary entry) |

The honest held-out figure is the third row: 2 false alarms in 14 findings, in 2 of 40 repositories, after rules had
already been tuned on other data. The last row includes fixes made after seeing the second set, so it is optimistic.
No provider-specific credential and no unsafe pickle was found in any of the 80 popular/community models, so **the
secret and unsafe-code rules have no real-world true positives to show here** — only the fixtures. The real leaks
were all of the kind that motivated the tool: Windows/macOS/Linux user names in a joblib file, notebook outputs and a
README example; a Colab Drive folder in two of a model's settings files; machine names in
`runs/<date>_<host>` directories. They are low-to-medium sensitivity. The 7 repositories that have such a finding (2 in the tuning set, 5 held-out) are
replaced by pseudonyms (`community-repo-NNN`) in the two model lists and the manifests. The manifests keep no file list
for them (even pseudonymous file names keep a file count and an extension mix, which could be matched against the Hub),
and no commit SHA or download count, so nothing in the public files points back to them. The real ids exist only in a private mapping outside the
repository (`LIMNEX_PRIVATE_MAPPING=... pytest` greps the whole tree for them). Consequence: those 7 repositories cannot be
re-fetched from the public files. The other 73 are named in the lists and manifests, so the run can be repeated.
**No per-repository result is published**, only totals over each set (`hf_review.md`: findings by run, verdict, rule and
severity; `hf_totals.json`): a second pre-release test showed that even under pseudonyms, a repository's file count and
file types could be matched to the named manifests. The per-repository result files stay in the private development
repository: they are marked `export-ignore`, so the public tree (built with `git archive`) never contains them, and in
that tree `tests/test_results_consistency.py` fails if one is put back. So a finding is never shown next to a
person's or a team's name: a maintainer's contact e-mail in a README, or a vendor's build address inside a model file,
would otherwise read like that person's leak. Before release, the owners of the repositories with a leak finding were
told privately: by e-mail where they published a contact, otherwise through Hugging Face. If you
reproduce the run and find something, please tell the owner privately too. There is no ground
truth for what the tool *missed* on real models.

**Second review round (getattr and pseudonymisation) — old vs new, same data:**

| | before | after |
|---|---|---|
| fixture suite: planted values / clean twins with findings | 651/651 / 0 of 21 | 651/651 / 0 of 21 |
| fixture suite: malicious pickle+Keras cases flagged / benign flagged | 19/19 / 0 of 4 | 41/41 / 0 of 4 |
| comparison, original 19+4 cases (ours / picklescan / ProtectAI caught) | 19 / 11 / 10 | 19 / 11 / 10 (unchanged) |
| real models, tuning set: findings (leak / intended / false) | 7 (3 / 3 / 1) | 7 (3 / 3 / 1), identical fingerprints |
| real models, held-out set: findings (leak / intended / false) | 14 (8 / 6 / 0) | 14 (8 / 6 / 0), identical fingerprints |
| real models: `getattr` findings of any severity (the three `forward` calls) | 0 | 0 (`forward` is on the allow-list) |
| real models: new `pickle-getattr-review` findings | n/a | 0 |

The real-model numbers did not move because the 80 repositories contain only the three `forward` calls; the new rule
therefore had **no real-world evidence** for its review tier, only fixtures. The fresh set of section 6 gave the first:
one benign Keras 3 pickle in 67 pickle-bearing files raised it (two MEDIUM review findings, both false alarms). The tier
works as designed, and it is not free of false alarms.

**Which changes were made after seeing which data set** (the honest bookkeeping; none of these can be called blind):

* after the **tuning set** (first 40 repositories): entropy candidates exclude URL/path/identifier strings; public IPs need
  host-like context; the `os.environ[` code-reference filter; the CatBoost build-metadata e-mail exemption; `.bin` files
  without pickle magic are not parsed as pickles; the first `getattr`/`_load_from_bytes` call-site logic; `.ipynb_checkpoints`
  is scanned; degraded modes are reported.
* after the **held-out set's first look**: two further code-reference shapes (`UserSecretsClient()`, `self.api_key)`) and the
  `runs/<date>_<host>` host-name rule. These are the changes made with knowledge of held-out findings.
* after the **second review** (no new data): `getattr` judged fail-closed (allow-list from the tuning set's three `forward` calls,
  expanded dangerous list, review tier, all call opcodes, indirect references), pseudonymisation made complete. The held-out
  set contains no `getattr`, so nothing in this round was derived from it.
* after the **pre-release review** (no new data; a separate review session, not the one that wrote the code): more
  known code-execution callables on the deny-list, C-module aliases and protocol-4 dotted names judged, the
  `pickle-computed-callable` review finding, parser error text scrubbed before it reaches a report, truncated NumPy /
  safetensors / GGUF files reported as incomplete instead of clean, the ignore file read from the base commit on pull
  requests, and the Action's default `fail-on` aligned with the CLI (`medium`). Every change has a test; none was derived
  from the 80 repositories, and the real-model numbers above were not re-tuned.
* after the **fuzzing round** (random damage to the benign fixtures; no new real data): reads sized by a length field
  are bounded by the file (pickle, GGUF, the text and carving readers), and five kinds of cut-short file that came back
  clean are now reported as incomplete: a zip read as an inner or second archive, a cut zlib stream (and data after one),
  a NumPy header or object array cut short, a CatBoost model shorter than its core, and a container named `.zip`/`.npz`/
  `.gguf`/... whose content is something else. Each has a test in `tests/test_damaged_files.py` or `tests/test_limits.py`.
* after **dogfooding on my own projects** (section 5): the four scanner fixes listed there. None of them touches the
  unsafe-code rules. The 80-repository scan in this section was not re-run after them.
* after the **fresh held-out set** (section 6): two fixes, each test-first in its own commit. PyTorch's ONNX exporter
  labels (`pkg.torch.onnx.*` metadata keys) are no longer read as host-name fields, and `--deep` now says so when it stops
  at its 4 GiB per-payload cap. Both were found on that data, so the section 6 figures are reported from the scan made
  *before* the fixes, with the effect of each fix stated separately.
* after the **second pre-release review** (2026-11-11; no new data, harmless test files only): three fixes, each
  test-first in its own commit. The bytes joblib's loader treats as array data are also read the way a plain pickle
  loader reads them (as instructions), and definite findings there are reported; a PyTorch-style archive that Python's
  zip reader cannot read, but PyTorch's more tolerant reader may still load, is a MEDIUM finding
  (`unscannable-model-archive`) instead of a scan problem only; a later pickle in protocol 0 or 1 is analysed instead of
  being carved as trailing data. A second round on the other readers added two MEDIUM rules,
  `onnx-external-data-path` (external data outside the model's folder) and `unsafe-yaml-python-tag` (YAML tags that
  Python's unsafe YAML loaders turn into objects), scans the bytes after the last safetensors tensor, and reports HDF5
  parts that used to be skipped silently. The real-model figures above were measured before these fixes and were not
  re-run.

Speed: the 80 repositories (2.6 GB on disk) scan in about 90 s in total, single core, pure Python. Weights are skipped, so
cost follows metadata, not model size: 320 MB joblib, 500 MB PyTorch zip and 1 GB safetensors files each take ~0.2 s and
~45 MB of memory. (Release candidate 8 broke this for `.keras` files with `h5py` installed: the weights were copied into
memory, about twice the model's size; fixed before release, with a memory test.) On the fresh set of section 6, 60 repositories (20.5 GB) took 85 s, and 4-6 GB safetensors and GGUF
files took 0.2-1.1 s with 53-93 MB of memory. `--deep` reads every payload byte at roughly 20-30 MB/s with about 200 MB
of memory, and reads at most 4 GiB of one payload.

**3. Against existing tools, on the same files** (`evaluation/results/comparison.md`; picklescan 1.0.5, ProtectAI
`modelscan` 0.8.8 with its h5py and TensorFlow extras installed, detect-secrets 1.5.0 with default plugins):

| original suite | malicious pickle/Keras cases caught (19) | benign files wrongly flagged (4) |
|---|---|---|
| limnex-preflight | 19 | 0 |
| picklescan | 11 | 1 |
| ProtectAI modelscan | 10 | 1 |

The 22 `getattr` cases added in the second review round do not separate the tools: limnex-preflight flags 22/22 (as HIGH or
as a review finding), picklescan and ProtectAI `modelscan` 21/22 each (they flag every `getattr`; the one they pass is the
`torch.load` call through `INST`).

All three agree on the plain cases (`os.system`, `subprocess`, `eval`, a payload in a PyTorch zip). The others miss what
I built the harder cases around — payload after a corrupt opcode, inside joblib's inline array layout (including
zlib-compressed), in gzip, in a zip inside a zip, behind `torch.storage._load_from_bytes` — some of which are outside
what those tools claim to cover, and *I chose the cases*. Read the table as "it covers what it was built to cover", not as
"it is better at catching attacks": no case comes from the other tools' own test suites, and no case is a real-world
malicious file. Both also flag `getattr(Class, "forward")` and therefore
flag such checkpoints in the evaluation set (ProtectAI as CRITICAL); that is a real false alarm and the
most useful difference on real data.
For secrets, detect-secrets found 58 of the 462 planted credential instances (it only reads text files and has no
detectors for several providers I planted, e.g. Hugging Face, Google, Anthropic, Kaggle) and raised 7 alarms on the
clean twin files; limnex-preflight found all 462 with none on the twins — again on fixtures built for my own rules.
**On the same real files** (the 60 fresh repositories of section 6, all benign; `evaluation/REPORT_2026-11-05.md` and
`evaluation/COMPARE_LEAKS_2026-11-05.md`). Unsafe code first, with picklescan and ProtectAI `modelscan` as above:

| | picklescan | ProtectAI `modelscan` | Preflight |
|---|---|---|---|
| pickle-bearing files it could read (of 67) | 27 | 51 | **67** |
| joblib / scikit-learn pickles with inline arrays (12 files) | cannot parse | cannot parse or crashes | reads them (clean) |
| a standard Keras 3 pickle (`getattr` + an embedded archive) | scanned 0 files of it | **CRITICAL** | MEDIUM review finding (a false alarm) |
| time / peak memory for all 60 repositories | 5.9 s / 27 MB | 142 s / 592 MB | 85 s / 222 MB (it reads far more kinds of file) |

Where all three could read a file (23 files), they agreed: all clean. Nothing here is evidence about catching attacks,
because there is no malicious file in this data.

Then leaks, against three general secret scanners on default settings (gitleaks 8.30.1 `--no-git --redact`, TruffleHog
3.99.8 `--no-verification`, detect-secrets 1.5.0; the three ran with no network, so nothing was ever tried against a live
service). A hit by several tools on the same spot counts once; every finding was labelled from rule, file type, location
and masked value only:

| keys and passwords (all four look for these) | wrong or unclear | time, 60 repositories |
|---|---|---|
| Preflight | 4 | **94 s** |
| gitleaks | 3 | 3,498 s |
| TruffleHog | **0** | 842 s |
| detect-secrets | 134 | 319 s |

**Personal data** (only Preflight looks for it): **4 real leaks, all found by Preflight alone**, plus 11 intended contact
addresses and 4 wrong.

How much it is worth: a benign sample of 60 repositories is not built to measure how well a tool finds keys, so the
keys rows show false alarms only, and there TruffleHog was the quietest. The four leaks only Preflight found are personal
data (a user name inside ONNX metadata, a notebook folder in a training script, two third-party e-mail addresses), which
the other tools are not built to look for, so that row is extra coverage, not a fair contest. The time column is
indicative (the batches ran in parallel); the large gap comes from the others reading weight files as text. Redaction
hid most of the other tools' evidence, so 15 of their findings could only be labelled "unclear". The same author wrote the scanner and this harness.

Where Preflight is **worse or missing**: it has fewer maintained detectors than detect-secrets/gitleaks/trufflehog and
no plugin system, no verification of live keys, no git-history mode, no baseline workflow beyond fingerprints, no
TensorFlow SavedModel support, and it is a v0.1 written in days, not a mature project. ProtectAI's `modelscan` solves
a related problem (unsafe operators in model files) and is a sensible companion. This project is unrelated to it (it was
called `limnex-modelscan` during development and renamed before release to avoid the confusion).

**4. Damaged files: mutation fuzzing** (`evaluation/fuzz_formats.py`, report in `evaluation/results/fuzz.md`). 6,300
damaged copies (300 per format, 21 formats) of the benign clean-twin fixtures: bit flips, overwritten bytes, huge
values over length fields, inserted / deleted / duplicated chunks, truncation, and damage to one member of an
otherwise valid archive. Each file must not crash, not hang (20 s), not allocate more than 256 MB, and, when cut short,
must not come back clean. The first runs found two kinds of bug:
* **memory:** every text file reserved 256 MB, damaged pickles asked for up to 4 GB, and a damaged 2.6 KB GGUF for 20 GB;
* **cut-short files reported as clean:** zip, zlib, NumPy and CatBoost (37 of the 5,400 files in the first full run).

All of these are fixed and each has a regression test. The final run has **0 failures** and a highest peak of 8.7 MB.
The slowest file takes 10.0 s: a damaged Keras (HDF5) file on which `h5py` itself makes no progress, which the scanner
stops after 10 s and then scans as raw strings (see "Safety design"). One cut fell exactly between two top-level fields
of an ONNX file, which leaves a complete, valid file (see "What it cannot find"): the one "known limit". The run was
made on Windows (Python 3.14) with `h5py` 3.16.0, `onnx` 1.23.2, `joblib` 1.5.3, NumPy 2.4.4 and zlib-ng 1.3.1, and
`fuzz.md` lists every seed's SHA-256. The harness writes its own seeds with the same bytes on every system (fixed line
ends; zip entries without the time or the writing system) and gives each format its own random stream, so on another
system only the rows whose seed differs can change; the Keras, ONNX, joblib and NumPy seeds are written by those
libraries, and joblib's zlib seed by the zlib build Python links, so other versions can give other files. The fourth
and fifth pre-release tests regenerated the report on Linux with the same library versions (for earlier release
candidates): 0 failures, all 21 rows and the known-limit row the same, 20 of 21 seed hashes the same; the
`joblib-zlib` seed differed, because that system's zlib build compresses differently. Since then the credential rule
that also reads environment-variable assignments reports a few more damaged files as not clean (catboost 89 → 95,
json 25 → 29 of 300); the seeds and the 0 failures are unchanged. Earlier
runs were weaker: one had no `h5py` and never fuzzed the HDF5 reader (the
first pre-release test then found that Keras file on Linux), and the next had `h5py` installed but not loadable in the
isolated mode the scanner runs in, so on Windows it still fell back to raw strings for every HDF5 file (found by the
second pre-release test). Random damage finds robustness bugs; it is not a test against a deliberate attacker.

**5. Dogfooding: my own ML projects** (read-only, before release; the reports are not published because they contain my
own paths and names). About 14 GB in 1,366 files from two of my projects: 72 trained models (57 PyTorch, 12
scikit-learn/joblib, 3 CatBoost), notebooks, configs, logs and generated URL data.
* **No unsafe-code false alarm** on the 72 models, and no file that made the scan fail.
* **A real leak in a model I had already published:** my Kaggle user name, inside the model file of a public release.
  It also found my Windows user name in a README and in a log.
* **Four problems in the scanner, all fixed, each with a test:** non-ASCII UTF-8 text (Arabic notes, even many em dashes)
  with an unlisted extension was reported "not scanned"; `.py`/`.sh` files depended on the size-limited sniff; URL
  user-info (`http://a.com@b.com`, scheme-less `user@host/path`) was reported as an e-mail address; a file name that
  contains `api_key` (a manifest of hashes) and a call taking a string literal (`re.compile(r"...")`) were reported as
  credentials.
* After the fixes: 4 findings on the first project, all real (user names and Kaggle dataset paths); 95 on the second,
  almost all in generated URLs that contain e-mail-shaped or password-shaped strings. That data is synthetic by design,
  so those findings are correct, not noise.
* Adding `.csv` to the text formats made the first project's scan 8× slower (big URL datasets) and buried the model
  findings under about 2,300 values from third-party data, so it was reverted (see "What it cannot find").

How much it is worth: one author's files, made with one set of habits, so it says little about other people's models,
and the fixes were made after seeing these files. It says nothing about attacks.

**6. A fresh held-out set: 60 more Hugging Face repositories and 3 large files** (2026-11-05; rule in
`evaluation/HELDOUT_V2.md`, report in `evaluation/REPORT_2026-11-05.md`; real repository ids and per-repository results are
not published, only totals).
* **How it was drawn:** the rule (seed, listing, filters, size caps) was committed before the first download. Recent
  repositories (created in the last 12 months) with at least 100 downloads in 30 days, not gated, none from section 2,
  10 per format, at most 1 GB and 6 model files each, plus 3 separate stress files of 4-6 GB. **Never a repository that
  Hugging Face itself flags.** Two changes to the rule were decided from candidate counts before any download and are
  recorded in the rule file.
* **Selection bias, stated:** 32 of 42 scikit-learn repositories and 7 of 17 Keras repositories that the draw reached
  carried a Hugging Face flag and were skipped. The sample is "not flagged by Hugging Face", not "all of Hugging Face".
* **Result:** 528 files (20.5 GB) read in full: 0 errors, 0 damaged, 0 not scanned. 49 of 63 repositories had no
  finding. 196 findings in total (19 MEDIUM or above, 177 LOW); 167 of the 177 LOW ones were a single false-alarm class,
  fixed afterwards (see the bookkeeping list in section 2). The 19 MEDIUM+ findings, labelled from masked evidence: 15 true
  or intended (for example contact addresses in READMEs and licences, a notebook folder, a user name in an exporter path
  and third-party e-mail addresses), 4 false or unclear (2 on the standard Keras 3 pickle, 2 values in text files).
* **Large files:** the default scan read 4-6 GB files in 0.2-1.1 s without loading them. `--deep` turned out to stop
  silently at 4 GiB of a 6 GB file; it now reports the unscanned rest.
* **What it still does not show:** anything about real attacks; HDF5 (`.h5`) Keras files (the sample had only `.keras`);
  model files above 1 GB apart from the 3 stress files; how many leaks any tool *missed*.

## Development

```bash
pip install -e ".[dev]"
pytest                                   # ~700 tests (some skip without optional libraries or symlink rights)
python evaluation/run_fixture_eval.py    # regenerate evaluation/results/fixture_detection.md
python evaluation/run_comparison.py --picklescan ... --modelscan ... --detect-secrets ...
python evaluation/hf_fetch.py --cache /somewhere/outside/the/repo       # downloads untrusted files; never loaded
python evaluation/run_hf_scan.py --cache ... --manifest ... --out ...
```

Downloaded model files are untrusted data: keep them outside the repository and never import or load them.

## Credits and licence

Written with [Claude Code](https://claude.com/claude-code) (Anthropic's agentic coding tool) for
[youssefismail-dev](https://github.com/youssefismail-dev), who set the goals, the safety rules and the evaluation
protocol. Licensed under the Apache License 2.0 — see
[LICENSE](https://github.com/youssefismail-dev/limnex-preflight/blob/main/LICENSE).
