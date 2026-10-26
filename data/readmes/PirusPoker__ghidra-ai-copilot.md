# Ghidra AI Copilot

An AI reverse-engineering assistant that lives inside **Ghidra**. Put your cursor on a
function, hit run, and Claude explains what it does — a plain-English summary, better
names for the variables, recovered types, the control flow, the algorithm it recognizes,
and any security issues — written right onto the function.

It works on **one function** or **every function** in a binary, and it caches results so
re-running is free. Everything runs locally except the model call.

```
  decompiled C  ──►  Claude  ──►  SUMMARY / SUGGESTED NAMES / TYPES /
  (from Ghidra)                    CONTROL FLOW / ALGORITHM / SECURITY NOTES
                                   → printed + attached as a comment on the function
```

---

## Example — what it produces

Run it on a license-check function and Claude writes this analysis right onto it:

```text
SUMMARY: Validates a license key — requires exactly 16 characters, computes a
reflected CRC-32 over them, and returns 1 only if the raw CRC equals the
hardcoded magic 0x74e3b2d5.

SUGGESTED NAMES: check_license -> validate_license_key, param_1 -> key,
uVar2 -> key_len, uVar4 -> crc, lVar3 -> i

TYPES: int validate_license_key(const char *key);   // effectively bool 0/1

CONTROL FLOW: strlen(key); if length != 16, return 0. Otherwise init
crc = 0xFFFFFFFF, loop the 16 bytes running 8 unrolled CRC steps (shift +
conditional XOR 0xEDB88320), then return (crc == 0x74e3b2d5).

ALGORITHM / PURPOSE: classic CRC-32 (reflected, polynomial 0xEDB88320) used as a
weak license check. Note the missing final ~crc complement — the compiler folded
it into the magic constant (0x74e3b2d5 = ~0x8b1c4d2a).

SECURITY NOTES: weak, non-cryptographic — CRC-32 is trivially reversible, so valid
keys can be forged; easily bypassed by patching the constant.
```

---

## What you need first

| Requirement | Notes |
|---|---|
| **Windows** | (These installers are `.bat`; macOS/Linux users can run the same scripts manually.) |
| **Ghidra 12.0+** | Free, from [ghidra-sre.org](https://ghidra-sre.org). Needs a **JDK 21** (the Ghidra download page links one). This tool uses Ghidra's built-in **PyGhidra**. |
| **Python 3.10+** | From [python.org](https://python.org) — tick **"Add Python to PATH"** during install. |
| **An Anthropic API key** | From [console.anthropic.com](https://console.anthropic.com) → *API keys*. A **console** key, not a Claude.ai subscription. Usage is billed to your account. |

---

## Install (~5 minutes)

**1. Get this folder** onto your machine (download the ZIP, or `git clone`).

**2. Set your API key** as a Windows environment variable so the tool can find it.
Open **Command Prompt** and run (paste your real key):

```
setx ANTHROPIC_API_KEY "sk-ant-your-key-here"
```

> Close and reopen any terminals afterward so the key takes effect. You can check it's
> set with `echo %ANTHROPIC_API_KEY%` in a **new** terminal.

**3. Point the launcher at Ghidra.** Open **`run.bat`** in a text editor and set this line
to wherever you unzipped Ghidra (the folder that contains `ghidraRun.bat`):

```bat
set "GHIDRA_INSTALL_DIR=C:\ghidra_12.1.3_PUBLIC"
```

**4. Run setup once.** Double-click **`setup.bat`**. It creates a local Python environment,
installs the two dependencies (`anthropic`, `pyghidra`), and copies the scripts into
Ghidra's script folder.

That's it. You're installed.

---

## Use it

1. **Double-click `run.bat`** — this launches Ghidra with the Copilot wired in.
   *(Use `run.bat`, not Ghidra's normal `ghidraRun.bat` — the launcher is what makes the
   AI available.)*
2. Import a binary (**File → Import File**) and let auto-analysis finish.
3. Click inside a function.
4. **Window → Script Manager**, category **`AI Copilot`**:
   - **Analyze Function** — analyzes the function under your cursor.
   - **Analyze All Functions** — analyzes the whole binary (asks first, shows a cost estimate, and hard-stops at a safety cap).
5. Read the analysis in the **Console**; it's also saved as a comment on the function.

> Tip: assign **Analyze Function** a keybinding in the Script Manager for one-key analysis.

---

## Cost

Each function costs about **$0.02–0.09** with the default model (Claude Opus). For bulk
work, open a script and change:

```python
MODEL = "claude-sonnet-5"   # ~3x cheaper and faster; great for whole-binary passes
```

**Analyze All Functions** shows an estimate before it starts and stops at a hard cost cap
(`COST_CAP`, default $5/run) so it can't surprise you.

---

## Your data

- Analyses are also appended to a local dataset at
  `%USERPROFILE%\.ghidra_ai_copilot\dataset.jsonl` (one `(code → analysis)` pair per unique
  function). It's yours, on your disk. Set `LOG_TRAINING = False` in the script to turn it off.
- Decompiled code you analyze **is sent to Anthropic** to produce the analysis. Don't run it
  on anything you're not allowed to share with a cloud API.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Scripts not in Script Manager | Click the "Manage Script Directories" (bundle) icon, add `%USERPROFILE%\ghidra_scripts`, refresh. |
| `ANTHROPIC_API_KEY is not set` | You didn't `setx` the key, or didn't reopen the terminal/relaunch after. |
| `'anthropic' not found` | You launched Ghidra with `ghidraRun.bat` instead of `run.bat`, or `setup.bat` hasn't run. |
| Ghidra won't start / "Java not found" | Set `JAVA_HOME` (uncomment the line in `run.bat`) to your JDK 21 folder. |
| `GHIDRA_INSTALL_DIR looks wrong` | Point it at the folder that actually contains `ghidraRun.bat`. |

---

## How it works (for the curious)

Ghidra 12 runs Python scripts through **PyGhidra** (real CPython). `run.bat` launches Ghidra
using a local virtual environment that has the `anthropic` package installed, so the scripts
can call Claude directly. Each script grabs the function under your cursor, decompiles it with
Ghidra's decompiler, sends the C to Claude with a fixed analyst prompt, and writes the result
back as a plate comment. No magic — just Ghidra's API + one model call.

## License

MIT — see [LICENSE](LICENSE). Built as a learning project; use it, fork it, improve it.
