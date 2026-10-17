# PolycryptZero (p0) - Hash Cracking

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-yellow.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-GPLv3-red.svg" alt="License">
  <img src="https://img.shields.io/badge/Release-v2.0-purple.svg" alt="Release">
  <img src="https://img.shields.io/badge/Release-Windows-lightgrey.svg" alt="Platform">
</p>

PolycryptZero is a desktop hash-cracking tool. It combines a Python/CPU hashing path, an optional hashcat/GPU backend, a SQLite-backed rainbow table store, and a small ONNX transformer that generates candidate passwords instead of enumerating them blindly. Everything runs behind a single `customtkinter` GUI with live progress reporting.

<p align="center">
  <img src="https://github.com/user-attachments/assets/2c6cce0f-dd50-4462-84b4-778718667444" alt="PolycryptZero screenshot" width="200"/> 
</p>

### Hash algorithm support

Algorithms are split into two tiers:

- **Native (Python `hashlib`/`bcrypt`)**: MD5, MD4, SHA-1, SHA-224/256/384/512, SHA3-256/384/512, BLAKE2b, BLAKE2s, RIPEMD160, Whirlpool, SHAKE128-256, SHAKE256-512, and bcrypt. A handful of these (MD4, RIPEMD160, Whirlpool) go through `hashlib.new()`, and the tool actually probes at startup whether your build of OpenSSL supports them — if it doesn't, they're silently dropped from the list rather than crashing later. Worth knowing if you're wondering why an algorithm you expect isn't showing up.
- **hashcat-only**: everything else in `hashcat_modes.json` that isn't already covered natively — NTLM, LM, md5crypt, sha256crypt/sha512crypt, phpass, various DB hash formats (MySQL, PostgreSQL, MSSQL, Oracle), Django hashes, Kerberos AS-REQ/TGS-REP, WPA-PBKDF2/PMKID, and archive/document formats (7-Zip, RAR3/5, ZIP, PDF, 1Password, macOS v10.8+). These only work if hashcat is installed and the mode maps cleanly.

Algorithm identification is layered, in order: prefix-based detection (e.g. recognizing `$2b$` as bcrypt), then `hashcat --identify` if hashcat is available, then a length-based fallback that hashes an empty string with each known algorithm and compares lengths. This last one is a heuristic, not a guarantee — several algorithms produce hashes of the same length, so it can return a plausible answer rather than the correct one. (This part could genuinely be improved — a candidate-list UI showing *all* plausible matches rather than just the first would be more honest about the ambiguity.)

### Attack modes

| Mode | What it does | Where it can run |
|---|---|---|
| **Wordlist** | Streams a file line-by-line, hashes each entry, compares to the target | CPU or hashcat |
| **Brute-force** | Exhaustive `itertools.product` over a charset for a given length range | CPU or hashcat |
| **Rule-based** | Takes a base word and applies a configurable rule set (below) | CPU or hashcat |
| **Probabilistic (AI)** | An ONNX transformer generates candidates token-by-token | CPU or hashcat |
| **Rainbow table** | Looks up the hash directly against precomputed tables | Local SQLite store |

bcrypt is the one exception across the board: it's deliberately excluded from the hashcat path (`supports_on_hashcat` hard-codes `False` for it) and always runs through the native `bcrypt` library instead, regardless of what backend mode is selected. This isn't a limitation so much as a correctness choice — bcrypt's cost factor makes GPU offload comparatively less valuable, and keeping it on one consistent code path avoids subtle mismatches.

**Rule-based transformations**, specifically, support: prepending/appending common prefixes and suffixes, capitalizing the first letter, reversing the word (with capitalization reapplied on top if both are enabled), toggling case per-character, appending a fairly large set of numeric/year/symbol suffixes (`NUMBERS_TO_APPEND` — recent years are generated dynamically off the current year), and leet-speak substitution via a simple character map (`a→@`, `e→3`, `s→$`, etc.). Rules compose — the candidate set is built up in stages, so enabling several rules at once produces the cross product of transformations, not just each one independently.

### Rainbow tables

The rainbow table engine (`rainbow_tables.py`) is a genuine little piece of infrastructure, not just a lookup dict:

- Backed by SQLite with WAL mode, a decent page cache, and memory-mapped I/O — reasonable defaults for a local, single-writer database
- A custom Bloom filter (SHA-256-seeded, configurable size/hash-count) sits in front of the DB to avoid disk hits on near-certain misses
- An in-memory LRU-ish cache on top of *that*, for hot lookups
- Batched inserts rather than one `INSERT` per discovery
- Every successful crack (from *any* attack mode, not just rainbow lookups) gets fed back into the table automatically — so the tool's rainbow store grows organically the more you use it

None of this is exotic, but it's a properly layered cache hierarchy (Bloom filter → in-memory cache → SQLite), which is more engineering than "rainbow table lookup" usually implies.

### Probabilistic / AI mode

This is the most distinctive part of the tool, so it deserves the most explanation.

Instead of generating candidates combinatorially, this mode runs a GPT-2-style autoregressive transformer (exported to ONNX — see `export_to_onnx.py`, which wraps a Hugging Face `AutoModelForCausalLM` with `use_cache=False` for ONNX-export compatibility) and samples token-by-token to produce plausible passwords directly. Generation uses standard decoding controls:

- **Temperature** (`0.8` default) — scales logits before sampling
- **Top-k** (`50` default) — restricts sampling to the k most likely next tokens
- **Top-p / nucleus sampling** (`0.95` default) — restricts to the smallest token set whose cumulative probability exceeds p

An optional seed keyword can prime generation (e.g. if you know the target likely used a name or word as a base). Generation runs in a bounded loop — up to `max(num_target_candidates * 50, 5000)` attempts — with periodic heartbeat signals back to the UI so a slow or stuck generation doesn't look like a frozen app. If the effective keyspace at a given length/seed combination is smaller than what you asked for, it says so explicitly rather than hanging silently.

To be clear about what this is and isn't: it's a pattern-completion model trained on password-like sequences, not a cryptographic attack — it doesn't "know" anything about a specific hash's plaintext. It's a smarter candidate generator than brute-force, not a shortcut around the hash function itself.

### GPU / hashcat backend

When hashcat is available on your `PATH` (or at a configured path), wordlist, brute-force, and rule-based attacks can be offloaded to it via `HashBackendRouter`, with three backend modes:

- **GPU** — forces hashcat; warns explicitly if only integrated GPUs are detected, since those often perform no better than CPU
- **CPU** — forces the native Python path

Device selection is exposed too (`list_devices()` parses hashcat's device listing across CUDA/OpenCL/HIP/Metal backends), so you can target a specific card rather than letting hashcat pick. The router also distinguishes discrete from integrated GPUs by name pattern-matching, mainly so it can warn you rather than let you assume you're getting discrete-GPU throughput when you're not.

## GUI
<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/2a73b108-ae7f-4726-91f9-5991091486dc" width="350"></td>
    <td><img src="https://github.com/user-attachments/assets/05165d5b-1ccc-4769-bd2a-780d6e67f979" width="350"></td>
  </tr>
</table>

## Installation

### Option 1 (Recommended) — Executable (Windows)

Grab the latest build from [Releases](https://github.com/serptail/p0-Password-Cracking-Tool/releases/tag/v2.0) and extract the `p0-Release-v2.0.7z` archive, then run `p0.exe`. You'll find the `gpt2-passwordmodel` folder for the probablistic attack mode, and `hashcat` already installed along side it. No Python needed.

### Option 2 — From source 

```bash
git clone https://github.com/serptail/p0-Password-Cracking-Tool.git
cd p0-Password-Cracking-Tool
pip install -r requirements.txt
python src/main.py
```

But you will need to install [hashcat](https://github.com/hashcat/hashcat/releases) manually, extract it, rename the folder to exactly `hashcat` and place it in the same directory as `main.py` script, or if on `PATH`. 

**Requirements**

- Python 3.11+
- `customtkinter`, `pycryptodome`, `numpy`, `onnxruntime`, `transformers`

## Usage

1. Paste the target hash. Let it auto-detect, or pick the algorithm manually if you already know it (faster and more reliable than the heuristic).
2. Pick an attack mode and set its parameters — wordlist path, charset + length range, rule set, or AI generation settings.
3. Pick a backend mode: GPU / CPU.
4. Start. Watch the live rate/ETA with the `Logs` button. Cancel any time — the stop event propagates cleanly through whichever backend is running.

## Remarks

### Wordlists

For wordlist and rule-based modes, I attached the `hashmob2025-medium.txt` in the [Releases](https://github.com/serptail/p0-Password-Cracking-Tool/releases/tag/v2.0) section, it's the best wordlist by far in terms of success crack rate (`~15%` according to [weakpass.com](weakpass.com))

You can also use any other wordlist, like the famous `rockyou.txt` wordlist
(see https://weakpass.com/wordlists/rockyou.txt#wordlist)
### Probabilistic mode setup

Point the tool at an exported ONNX model directory. The bundled `gpt2-passwordmodel` works as-is; to export your own model, run `export_to_onnx.py` against any Hugging Face causal LM checkpoint. Or use any other pre-trained ONNX model you want (must respect the format!)

## Roadmap

- Better model architecture for the probabilistic engine (current one is a fairly small GPT-2-style model — there's real headroom here)
- Linux release
- CUDA-specific tuning for probabilistic mode (currently ONNX Runtime CPU execution provider only)
- A less ambiguous hash-type detection UI (surface multiple candidates instead of one guess)

## Legal Notice

This tool is for educational and personal use only, meant to demonstrate how password hashing, security vulnerabilities, and cracking techniques actually work under the hood.

By using it, you agree that:

- You're responsible for how you use it and any consequences that follow
- Using it against accounts or systems you don't have explicit permission to access is not allowed
- The developers aren't liable for legal or ethical issues arising from misuse
- It must not be used for anything illegal or malicious

The name **PolycryptZero™** and its logo aren't covered by the open-source license and may not be reused in derivative projects or forks without permission.

## Support

Star it, share it, or open an issue — all of it helps.

<p align="center">
  <img src="https://github.com/user-attachments/assets/aeeda621-8287-4f89-bed3-8b89e09f85a5" alt="octodance" width="100" height="100"/>
</p>
