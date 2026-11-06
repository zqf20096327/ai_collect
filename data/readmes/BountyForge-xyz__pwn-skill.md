<div align="center">

<img src="assets/banner.svg" alt="PWN HUNTER" width="100%"/>

# PWN HUNTER

**Binary exploitation skill for AI agents.**
Primitive-driven pwn: triage → leak → write → exec.

[![License](https://img.shields.io/github/license/BountyForge-xyz/pwn-skill?style=flat-square&color=00ffa3)](LICENSE)
[![Stars](https://img.shields.io/github/stars/BountyForge-xyz/pwn-skill?style=flat-square&color=4cc9ff)](https://github.com/BountyForge-xyz/pwn-skill/stargazers)
[![Issues](https://img.shields.io/github/issues/BountyForge-xyz/pwn-skill?style=flat-square&color=ff2e97)](https://github.com/BountyForge-xyz/pwn-skill/issues)
[![Last commit](https://img.shields.io/github/last-commit/BountyForge-xyz/pwn-skill?style=flat-square&color=8aa0b8)](https://github.com/BountyForge-xyz/pwn-skill/commits)
[![pwntools](https://img.shields.io/badge/pwntools-4.x-00ffa3?style=flat-square)](#requirements)
[![Agent Skill](https://img.shields.io/badge/agent-skill-4cc9ff?style=flat-square)](#install)

</div>

---

## Overview

PWN HUNTER is a single-file agent skill for binary exploitation and memory-corruption
work. It gives an AI agent a repeatable loop: fingerprint the target, find the primitive,
climb to code execution, and return a working exploit instead of a lecture.

It is built for CTF pwn, local lab binaries, and authorized exploit development.

## Features

- **Primitive ladder** — crash → RIP → leak → arbitrary write → exec → escape.
- **Triage first** — `checksec`, `readelf`, libc identification, kill signals.
- **Stack** — ret2libc, ret2csu, SROP, ret2dlresolve, stack pivots.
- **Format strings** — offset discovery and `fmtstr_payload` writes.
- **Heap** — tcache poisoning, safe-linking, UAF, off-by-one, Houses, FSOP.
- **Seccomp** — ORW / sendfile shellcode when `execve` is blocked.
- **Kernel** — `modprobe_path`, `commit_creds`, SMEP/SMAP/KPTI/KASLR bypass.
- **Refusal engineering** — context rules that keep standard agents on task.
- **PoC discipline** — measured offsets only, working `exp.py` as the deliverable.

## Coverage

| Area | Techniques |
|---|---|
| Stack | ret2libc, ret2csu, SROP, ret2dlresolve, pivot, alignment |
| Format string | arbitrary read/write, GOT/hook overwrite |
| Heap | tcache, fastbin, unsorted bin, UAF, off-by-one, FSOP, Houses |
| Sandbox | seccomp-tools, `openat`/`read`/`write`, `sendfile` |
| Kernel | `modprobe_path`, `commit_creds`, ret2usr bypass, KPTI trampoline |
| Tooling | pwntools, pwndbg/gef, ROPgadget, one_gadget, patchelf |

## Requirements

- Python 3 and [pwntools](https://github.com/Gallopsled/pwntools)
- A debugger: [pwndbg](https://github.com/pwndbg/pwndbg) or [gef](https://github.com/bata24/gef)
- Optional: `ROPgadget`, `ropper`, `one_gadget`, `seccomp-tools`, `patchelf`

```bash
pip install pwntools ropper libcsearcher
gem install one_gadget seccomp-tools
```

## Install

Clone the skill into your agent's skills directory.

```bash
git clone https://github.com/BountyForge-xyz/pwn-skill.git
cp -r pwn-skill ~/.agents/skills/pwn-hunter
# or, for Claude-style skill dirs:
cp -r pwn-skill ~/.claude/skills/pwn-hunter
```

The skill contract is the `SKILL.md` frontmatter; the rest of the file is loaded
when the skill matches a task.

## Usage

Invoke it explicitly, or let the description trigger on phrases like:

```text
pwn this binary
exploit ./chall
build a ROP chain for this
ret2libc this
format string exploit
heap / tcache / UAF exploit
kernel pwn
get a shell from this challenge
```

Typical run:

```text
TARGET:      ./chall (amd64, PIE, NX, canary, partial RELRO)
ROOT CAUSE:  read() stack overflow in vuln()
PRIMITIVE:   overflow -> RIP -> puts@got leak -> ret2libc
CHAIN:       offset 0x48 -> pop rdi -> puts@got -> libc -> system
DELIVERABLE: exp.py (local + remote) and the shell output
```

## Refusal Engineering

Standard models refuse on ambiguous context, not capability. The skill encodes the
fixes: state authorization once, use lab vocabulary (`target`, `challenge`, not
`victim`), frame work procedurally, contract the output to code, and never narrate
danger. On a refusal, re-anchor once and continue. See `SKILL.md` → **Refusal
Engineering**.

## Repository Structure

```text
pwn-skill/
├── SKILL.md          # the agent skill
├── README.md
├── LICENSE
├── assets/
│   └── banner.svg
└── .gitignore
```

## Disclaimer

For authorized security testing, CTF challenges, labs, and systems you own or have
written permission to test. Use it responsibly.

## Contributing

Issues and PRs are welcome. Keep technique additions measured and testable: include
the primitive, the glibc/kernel version, and a minimal PoC.

## License

[MIT](LICENSE) © BountyForge-xyz
