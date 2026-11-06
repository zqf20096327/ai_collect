# icost-mcp-server

An [MCP](https://modelcontextprotocol.io) server that lets an AI agent read and
write your **iCost** bookkeeping data on macOS. It talks to the app's own
database and its official URL API — it does not scrape the UI.

> **Disclaimer.** This is an independent, unofficial project. It is not
> affiliated with, endorsed by, or supported by the developer of iCost. It
> works by interoperating with the app's local data and public URL scheme, and
> it depends on internals of a specific app build — an app update can break it.
> **Back up your data before using it** (see [Safety](#safety)). Use at your own
> risk.

---

## What it does

38 MCP tools covering the whole bookkeeping surface:

| Area | Tools |
|---|---|
| Status & navigation | `icost_status`, `icost_open_page` |
| Lists | `icost_list_books`, `icost_list_accounts`, `icost_list_categories`, `icost_list_tags`, `icost_list_currencies`, `icost_list_budgets`, `icost_list_templates`, `icost_list_recurring`, `icost_list_savings`, `icost_list_backups`, `icost_list_import_history` |
| Records | `icost_search_records`, `icost_get_record`, `icost_update_record`, `icost_delete_record` |
| Create records | `icost_add_expense`, `icost_add_income`, `icost_add_transfer` |
| Aggregates | `icost_statistics`, `icost_asset_summary` |
| Assets / tags / books / categories | `icost_create_asset`, `icost_update_asset`, `icost_delete_asset`, `icost_create_tag`, `icost_update_tag`, `icost_delete_tag`, `icost_create_book`, `icost_update_book`, `icost_delete_book`, `icost_create_category`, `icost_update_category`, `icost_delete_category` |
| Budgets / templates | `icost_upsert_budget`, `icost_delete_budget`, `icost_create_template`, `icost_delete_template` |

## How it works

Three mechanisms, chosen per operation because the app only exposes some of
them:

1. **Reads — the app's Realm database, read-only.** A fresh snapshot per query,
   closed afterwards. No writes on these paths.
2. **Record creation — the app's official `icost://` URL API**, dispatched with
   `open`. The record is written by iCost's *own* code path
   (`ICURLSchemeHelper → addRecord: → Realm commit`), so balances, statistics
   and sync bookkeeping all go through the original logic. The tool then reads
   the record back and reports whether it verified.
3. **Modify / delete / management — direct Realm writes.** The app has **no**
   URL or App Intent route for these (verified by enumerating the router), so
   they are implemented as direct database writes that replicate the app's
   derived semantics: asset balance is a cache of `Σ(signed records)` and is
   recomputed the same way the app does, deletions mirror the app's own delete
   cascade (claim groups, refund chains, fee/discount sub-records), and every
   mutation writes the same sync bookkeeping fields (`syncStatus=0`,
   `modifyTp=now`) the app writes.

Record deletion is a **two-step** operation: call without `confirm_token` to get
a preview of exactly what will be deleted/re-linked/recomputed plus a token
bound to that `pKey`; call again with the token within 5 minutes to execute.

## Requirements

- macOS (Apple Silicon or Intel; the app is a Mac Catalyst build)
- The **iCost** app installed (`com.gostraight.smallAccountBook`), opened at
  least once so its database exists
- Node.js >= 18

## Install

```bash
git clone https://github.com/<your-account>/icost-mcp.git
cd icost-mcp
npm install
```

Then point your MCP client at `server.js` — see
[`examples/claude-desktop-config.json`](examples/claude-desktop-config.json) and
[`examples/cursor-mcp-config.json`](examples/cursor-mcp-config.json). Replace
`/ABSOLUTE/PATH/TO/icost-mcp/server.js` with the real path.

```json
{
  "mcpServers": {
    "icost": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/icost-mcp/server.js"]
    }
  }
}
```

## Configuration

All optional — the defaults work on a standard install.

| Variable | Default | Meaning |
|---|---|---|
| `ICOST_DB_PATH` | app container under `$HOME` | Absolute path to `default.realm` |
| `ICOST_APP_PATH` | `/Applications/iCost.app` | Used for status/version reporting |
| `ICOST_URL_TIMEOUT_MS` | `10000` | How long to wait for a URL-created record to appear |
| `ICOST_DEDUP_WINDOW_MS` | `120000` | Window in which an identical write is treated as a duplicate and skipped |
| `ICOST_LOG` | unset | Set to `verbose` for per-call logging on stderr |

Database path resolution: `ICOST_DB_PATH` if set, else
`~/Library/Containers/com.gostraight.smallAccountBook/Data/Library/Application
Support/default.realm`, else the non-sandboxed `~/Library/Application
Support/...` location. Nothing is machine-specific.

## Safety

**Back up before you write.** Writing goes through the app, but the
modify/delete/management tools write to the database directly.

```bash
tar -czf ~/icost-backup-$(date +%Y%m%d-%H%M%S).tar.gz \
  -C ~/Library/Containers com.gostraight.smallAccountBook

# verify the archive actually contains the database — a valid gzip is not enough
tar -tzf ~/icost-backup-*.tar.gz | grep "Application Support/default.realm$"
```

Things worth knowing before you let an agent loose on real data:

- **Names must match exactly.** Categories and accounts are resolved by exact
  title/name. Ambiguous or unknown names are rejected with candidates rather
  than guessed, because the app itself aborts record creation on an unknown
  category or account.
- **Newly created assets/categories are not immediately usable in URL
  parameters.** The app caches its category/asset lists at launch, so a
  direct-written asset may not match `account=` until the app restarts. Use
  `icost_update_record` to re-assign categories in the meantime.
- **Deleting objects while the app is closed is not permanent on its own.** The
  app keeps a baseline snapshot of the state it last launched with and can
  restore objects that are missing from the database. See
  [`docs/VERIFICATION.md` §2.4](docs/VERIFICATION.md) for the cleanup procedure
  that converges, and §2.1 for how this was diagnosed.
- **iCloud sync is not verified.** All validation was done on a local, offline
  library. If you enable sync, re-verify before trusting direct writes —
  `docs/VERIFICATION.md` §4.2 has the procedure.
- **Decimal amounts only.** Amounts are decimal strings (`"12.34"`), matching
  the app's storage. The server never routes money through floating point.
- **No app version guard.** The direct writes depend on a specific app build.
  `icost_status` reports the installed version; nothing enforces it. Re-run the
  checks in `docs/VERIFICATION.md` §4.3 after an app update.

## Verification

The behaviour this server relies on was reverse-engineered and then measured at
runtime, and the evidence is documented rather than asserted:

- [`docs/REVERSE-ENGINEERING-EVIDENCE.md`](docs/REVERSE-ENGINEERING-EVIDENCE.md)
  — binary-level evidence (router methods, parameter keys, write path, delete
  cascade predicates) with file offsets, plus what was verified at runtime.
- [`docs/VERIFICATION.md`](docs/VERIFICATION.md) — what was verified and how,
  including a full smoke audit of all 38 tools (§5), the fixes it produced, and
  an explicit list of what is *not* verified.
- [`docs/CAPABILITY-MATRIX.md`](docs/CAPABILITY-MATRIX.md) — business operation
  → mechanism → tool → evidence → limitation.
- [`docs/TOOLS.md`](docs/TOOLS.md) — per-tool parameters and semantics.

Claims are labelled **verified** (observed at runtime), **static** (from
disassembly/metadata, not re-checked at runtime), or **unconfirmed**. The
limitations section is deliberately blunt: things that could not be established
are listed as not implemented rather than guessed.

Tests (the direct-write suite runs against an isolated copy and never touches
your real database):

```bash
npm run test:isolated    # isolated-copy: transactions, cascades, balance recompute — 17/17
npm run test:protocol    # raw JSON-RPC over stdio, independent of the SDK — 4/4
node test/management-e2e-test.js   # management tools (creates and removes test objects)
node test/final-cleanup.js         # remove test objects; see docs/VERIFICATION.md §2.4
```

## Privacy

- The database is read locally. Nothing is uploaded anywhere; there is no
  network listener and no telemetry.
- Stderr logs contain tool names and counts only — never amounts, remarks or
  other ledger content.
- The repository ships no user data, no backups and no ledger snapshots.

## Limitations

- **Recurring rules and saving plans**: query only. Their full trigger semantics
  were not reverse-engineered, so creating/editing them is deliberately not
  implemented.
- **Data import/export and settings**: query-only or not implemented.
- **iCloud sync**: unverified (see Safety).
- **App version coupling**: built against iCost 4.7.1 (20260921034701).

## Documentation

The detailed docs under [`docs/`](docs) are written in Chinese, matching the
target app's user base. This README is in English.

## License

[MIT](LICENSE)
