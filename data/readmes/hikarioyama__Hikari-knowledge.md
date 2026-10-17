# Hikari-knowledge

Measured results, conditioned reports, and dead-end tombstones from **Hikari**'s local LLM systems work.

Serving, speculative decoding, quantization, MoE training, and activation steering — written so another engineer (or their agent) can reuse the mechanism, not the vibes.

- Every important number keeps conditions
- Dead ends stay as tombstones
- English only
- Curated public corpus (not a dump of a private vault)

## If you are an agent and only received this URL

User intent is probably one of:

1. **Install into my Obsidian/vault** (“導入して / merge / add to my notes”)  
2. **Answer from this knowledge** (“読んで / 調べて”)  
3. **Update an existing install** (“pull / 更新”)

**Do this immediately:**

```text
1. Clone or open https://github.com/hikarioyama/Hikari-knowledge
2. Read AGENTS.md
3. Read skills/hikari-knowledge/SKILL.md
4. If install/merge: follow Mode A + docs/OBSIDIAN_MERGE.md
   (copy-paste detail: prompts/obsidian-merge.md)
5. If Q&A only: read INDEX.md, then search nodes/
```

Default install shape: **subfolder clone** `{{vault}}/Hikari-knowledge/` + bridges from the user's notes.  
Do **not** flatten `nodes/` into the vault root.  
If the vault path is unknown, detect common workspace roots or ask **once** for the vault path, then proceed without more questions.

## Author

- **Hikari**
- GitHub: [hikarioyama](https://github.com/hikarioyama)
- X: [@Hikari_07_jp](https://x.com/Hikari_07_jp)
- Hugging Face: [Hikari07jp](https://huggingface.co/Hikari07jp)

## Start here

1. Read [`INDEX.md`](./INDEX.md)
2. Open a node under `nodes/`
3. Follow `links:` / `[[wikilinks]]`

## Use in an existing Obsidian vault

**Ideal merge:** keep this repo as a git subfolder and bridge from *your* notes.  
Do not flatten upstream files into your vault root if you want easy weekly pulls.

```bash
cd /path/to/your/vault
git clone https://github.com/hikarioyama/Hikari-knowledge.git Hikari-knowledge
```

Then:

1. Bookmark `Hikari-knowledge/INDEX.md`
2. From your project/MOC notes, add links like `[[serve-bench-discipline]]`
3. Update with `cd Hikari-knowledge && git pull --ff-only` (~weekly; watch [@Hikari_07_jp](https://x.com/Hikari_07_jp))

Full guide: [`docs/OBSIDIAN_MERGE.md`](./docs/OBSIDIAN_MERGE.md)  
Agent/copy-paste prompt: [`prompts/obsidian-merge.md`](./prompts/obsidian-merge.md)

## Use with an agent (files)

Point the agent at this repo URL or checkout and tell it to read:

1. [`AGENTS.md`](./AGENTS.md) — orientation + Obsidian/graph install
2. [`INDEX.md`](./INDEX.md) — map
3. [`skills/hikari-knowledge/SKILL.md`](./skills/hikari-knowledge/SKILL.md) — install / pull / read
4. [`skills/hikari-knowledge-curate/SKILL.md`](./skills/hikari-knowledge-curate/SKILL.md) — add/update nodes (subagents OK)

That is enough for most agents. No server required.

Longer operator notes: [`docs/AGENT_GUIDE.md`](./docs/AGENT_GUIDE.md).

## Optional MCP

A small local stdio MCP server is included under `mcp/` for clients that prefer tools:

- `kg_search`
- `kg_get`
- `kg_neighbors`
- `kg_index`

```bash
cd Hikari-knowledge
python3 -m venv mcp/.venv
mcp/.venv/bin/pip install -r mcp/requirements.txt
KG_ROOT=$PWD mcp/.venv/bin/python mcp/server.py
```

This runs **on your machine** against the files you cloned. The author does not host MCP for you.

## Updates

Cadence is **about once a week** — not a hard SLA, and quiet weeks are fine when nothing measured landed.

When notes ship, I announce on X: [@Hikari_07_jp](https://x.com/Hikari_07_jp)

Consumers should `git pull` (Obsidian subfolder or plain clone) after an announcement, or check weekly if you track silently.  
If you use the MCP adapter, restart is usually unnecessary — files are the source of truth.

See [`CHANGELOG.md`](./CHANGELOG.md).

## Layout

```text
AGENTS.md              start here if you are an agent
INDEX.md               human/agent map
nodes/methodology/     measurement, anti-inflation, eval design
nodes/serving/         engines, KV, kernels, offload
nodes/specdec/         MTP / draft heads / acceptance traps
nodes/training/        ESFT, MoE expansion, train gotchas
nodes/steering/        RepE / activation steering
nodes/papers/          short arXiv bridges (only if referenced)
skills/hikari-knowledge/         install / pull / read
skills/hikari-knowledge-curate/  mid-session curate + subagents
prompts/                 copy-paste prompts (Obsidian merge, …)
mcp/                   optional local MCP adapter
tools/                 graph build / check
docs/CONVENTIONS.md    writing rules
docs/AGENT_GUIDE.md    expanded agent operator notes
```

## License

MIT — see [`LICENSE`](./LICENSE).
