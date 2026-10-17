![validate](https://github.com/hassan-jahan/api-delta-manifest/actions/workflows/validate.yml/badge.svg)
![spec version](https://img.shields.io/badge/spec-1.0-blue)

# API Delta Manifest (ADM)

<p align="center">
  <img src="assets/delta-icon-light.jpg" alt="API Delta Manifest" width="100" />
</p>

**A machine-readable feed of API changes, built for both AI agents and humans so they can act on them easily**

## The problem

Every backend team eventually depends on APIs it doesn't control. When a provider changes something, that information usually arrives as a paragraph in a changelog, a blog post, or an email that gets filtered into a folder no one opens. Nothing in that format tells a computer *which* endpoint changed, *how severe* the change is, or *what code needs to move*. So teams find out at runtime, when a request starts failing in production.

Meanwhile, coding agents (Claude Code, Devin, Cursor, GitHub Copilot workspace agents, and similar tools) are now routinely trusted to read a codebase and open a pull request. That capability is underused here, because there's nothing structured for an agent to read on the provider side. Changelog text is written for humans skimming a page, not for a script deciding whether to touch `payment-service/src/charges.ts`.

**API Delta Manifest (ADM)** closes that gap. It defines a small, strict JSON format that API providers publish alongside their existing changelog, describing every change in a shape that a script — or an agent — can parse, filter, and act on without guessing.

This repository defines **v1 of the ADM spec**, scoped intentionally to one piece: **the manifest file itself.** Codemod delivery, webhooks, and consumer-side tooling are natural next steps but are out of scope for v1 so the core format can stabilize first.

## Design goals

- **Deterministic, not descriptive.** A field like `severity` must be one of a fixed set of values. No agent should have to infer meaning from freeform prose to decide whether a change is safe to ignore.
- **Diffable.** Each entry is addressable by a stable `id`, so consumers can track "which changes have I already applied" the same way they track applied database migrations.
- **Additive to what providers already do.** ADM does not replace a human-facing changelog page. It sits next to it as a structured export of the same information.
- **Small enough to hand-write, strict enough to validate.** A JSON Schema ships with this spec so a manifest can be checked in CI before publishing.

## Where it lives

Providers publish the manifest at a fixed, discoverable path:

```
https://api.example.com/.well-known/api-delta-manifest.json
```

This follows the existing `.well-known` convention (the same one used by `security.txt` and OAuth discovery documents), so consumers and agents don't need provider-specific configuration to find it — they can always check the same relative path.

## Manifest structure

```json
{
  "adm_version": "1.0",
  "provider": "acme-payments",
  "generated_at": "2026-09-01T12:00:00Z",
  "latest_snapshot": "2026-08-28",
  "entries": [
    {
      "id": "acme-2026-08-28-001",
      "released_at": "2026-08-28",
      "severity": "breaking",
      "kind": "field_rename",
      "title": "charges.source renamed to charges.payment_method",
      "description": "The `source` field on the Charge object is renamed to `payment_method`. The old field remains readable but not writable until the sunset date.",
      "surface": {
        "endpoints": ["POST /v1/charges", "GET /v1/charges/{id}"],
        "fields": ["charges.source"],
        "sdk_packages": [
          { "ecosystem": "npm", "name": "@acme/payments-node", "min_safe_version": "6.2.0" },
          { "ecosystem": "composer", "name": "acme/payments-php", "min_safe_version": "4.0.0" }
        ]
      },
      "action": {
        "required": true,
        "auto_fixable": true,
        "guidance": "Replace reads and writes of `source` with `payment_method`. No value transformation needed.",
        "codemod_url": "https://cdn.acme.com/adm/codemods/acme-2026-08-28-001.js",
        "docs_url": "https://docs.acme.com/changes/acme-2026-08-28-001"
      },
      "sunset_at": "2027-02-28",
      "supersedes": null
    }
  ]
}
```

### Top-level fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `adm_version` | string | yes | Spec version this document conforms to, e.g. `"1.0"`. |
| `provider` | string | yes | Short, stable, lowercase-hyphenated identifier for the API. Should not change once published. |
| `generated_at` | string (ISO 8601) | yes | Timestamp the file was generated. Consumers can use this to detect staleness. |
| `latest_snapshot` | string (ISO 8601 date) | yes | The date-based version identifier of the newest API revision described here. |
| `entries` | array of Entry objects | yes | One object per change. Newest first. Never delete or mutate a past entry; append instead. |

### Entry fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | Globally unique, stable, never reused. Recommended pattern: `{provider}-{date}-{sequence}`. |
| `released_at` | string (ISO 8601 date) | yes | When the change went live. |
| `severity` | enum | yes | One of: `breaking`, `deprecation`, `additive`, `patch`. See table below. |
| `kind` | enum | yes | One of: `field_rename`, `field_removal`, `field_addition`, `endpoint_removal`, `endpoint_addition`, `behavior_change`, `auth_change`, `rate_limit_change`, `other`. |
| `title` | string | yes | One line, plain text, no markdown. Should be understandable without reading `description`. |
| `description` | string | yes | Plain-language explanation. Markdown allowed. This is the only field meant primarily for a human reader; agents should rely on the structured fields, not parse this one. |
| `surface` | object | yes | See below. Describes exactly what changed. |
| `action` | object | yes | See below. Describes what a consumer (or their agent) should do about it. |
| `sunset_at` | string (ISO 8601 date) or `null` | no | Date after which the old behavior stops working. Omit or `null` if there is no deadline (e.g. purely additive changes). |
| `supersedes` | string or `null` | no | The `id` of an earlier entry this one revises or corrects, if any. |

### `surface` object

| Field | Type | Required | Notes |
|---|---|---|---|
| `endpoints` | array of strings | no | Each formatted as `"{METHOD} {path}"`, e.g. `"POST /v1/charges"`. Use the path template with parameter placeholders (e.g. `{id}`), not a resolved URL. Supports `ANY` in place of a method — see below. |
| `fields` | array of strings | no | Dot-notated, e.g. `"charges.source"`. |
| `sdk_packages` | array of objects | no | Each has `ecosystem` (`npm`, `composer`, `pip`, `gem`, `go`, etc.), `name`, and `min_safe_version` — the first package version where this change is already reflected. |

At least one of `endpoints`, `fields`, or `sdk_packages` must be present — an entry with an empty `surface` gives a consumer nothing to match against and should not validate.

#### Method and path matching

`endpoints` entries are `"{METHOD} {path}"` strings:

- **Path templates** use parameterized placeholders like `{id}` or `{customer_id}` for variable segments (e.g. `"GET /v1/customers/{id}/invoices"` or `"POST /v1/charges"`). Wildcards (like `*`) are not used in paths — route paths should be explicitly defined with parameter placeholders to ensure precise and deterministic matching.
- **`ANY` as the method** matches every HTTP method on that path. Use this when a change affects a route regardless of verb — for example, an auth change that applies to `GET`, `POST`, and `DELETE` on the same resource alike:
  ```
  "ANY /v1/charges/{id}"
  ```

If a change affects multiple endpoints across an API, list each specific endpoint template instead of using broad patterns. Consumers and AI agents rely on explicit route definitions in `surface` to target code patches accurately without having to guess.

### `action` object

| Field | Type | Required | Notes |
|---|---|---|---|
| `required` | boolean | yes | Whether a consumer must change anything to remain compatible. `false` for purely additive changes. |
| `auto_fixable` | boolean | yes | Whether a mechanical code transform can resolve this without human judgment. |
| `guidance` | string | yes | Plain-language instruction for what to change. Written so an agent can act on it even without `codemod_url`. |
| `codemod_url` | string (URL) or `null` | no | Link to a runnable transform (e.g. a jscodeshift script, a Rector rule, an ast-grep pattern). Present only when `auto_fixable` is `true`. |
| `docs_url` | string (URL) or `null` | no | Link to full human-readable documentation of the change. |

### `severity` values

| Value | Meaning |
|---|---|
| `breaking` | Existing integrations will fail or misbehave unless updated. |
| `deprecation` | Current behavior still works but is scheduled for removal by `sunset_at`. |
| `additive` | New capability. Nothing existing is affected. |
| `patch` | Bug fix or clarification with no expected impact on correctly-written integrations. |

## Example

[`examples/acme-payments.api-delta-manifest.json`](./examples/acme-payments.api-delta-manifest.json) is a complete, valid manifest for a fictional payments API. It deliberately covers all four severities and shows the `ANY` method and parameterized path templates in use (`acme-2026-08-10-004` and `acme-2026-08-28-001`), so it can double as a reference when writing or generating a manifest of your own.

## Validation

A [JSON Schema](./schema/adm-v1.schema.json) is provided in this repo. Providers should validate every manifest against it before publishing, ideally as a CI step that fails the build on an invalid document. 

### Validating locally

```bash
npm install
npm run validate
```

This runs [ajv-cli](https://github.com/ajv-validator/ajv-cli) against every file in `examples/` using `schema/adm-v1.schema.json`. Point it at your own manifest with:

```bash
npx ajv validate -s schema/adm-v1.schema.json -d path/to/your-manifest.json --strict=true
```

## Guidance for AI agents generating or consuming a manifest

If you are an agent tasked with producing an ADM file on behalf of an API provider:

1. **One entry per discrete change.** Do not bundle multiple unrelated field changes into a single entry — a consumer filtering by `surface.fields` needs each change isolated.
2. **Never omit `severity` or `kind`, and never invent values outside the enums above.** If a change doesn't cleanly fit an existing `kind`, use `"other"` and explain fully in `description` — do not create a new enum value.
3. **`id` must be stable and unique before you finalize the entry.** Once a manifest is published, treat every existing `id` as immutable. Re-publishing must append new entries, never rewrite old ones.
4. **Only set `action.auto_fixable: true` if `action.codemod_url` actually resolves to a working transform.** If no transform exists yet, set it to `false` and rely on `action.guidance` alone.
5. **Write `action.guidance` as an instruction, not a description.** Prefer "Replace `X` with `Y`" over "The `X` field was renamed to `Y`" — the former is directly actionable, the latter requires re-interpretation.
6. **If you are consuming a manifest to patch a codebase**, filter entries by `severity` and `surface` before reading `description`, cross-reference `surface.sdk_packages[].min_safe_version` against the consumer's installed version to skip changes already absorbed by a dependency bump, and only fall back to interpreting `description` in free text when `action.codemod_url` is absent and `action.guidance` is insufficient to write a mechanical patch.
7. **Prefer specific HTTP methods over `ANY` unless the change truly is method-agnostic.** Listing specific methods and route templates gives downstream consumers precision they rely on to avoid unnecessary inspection.

## Roadmap

This version defines only the manifest format and its hosting location. Deliberately excluded for now, to keep the core spec stable and reviewable:

- A push/webhook delivery mechanism for new entries
- A required format for `codemod_url` payloads (jscodeshift vs. Rector vs. ast-grep are all currently allowed; a follow-up spec may standardize this)
- A consumer-side lockfile format for tracking which entries have already been applied

Proposals for any of the above are welcome as issues in this repo.


## Contributing

This is a draft specification. See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose a change. In short: open an issue describing the problem before proposing a fix, and back up any change to `schema/adm-v1.schema.json` with a concrete example under `examples/` that demonstrates it. Backwards-incompatible changes to the spec itself bump `adm_version`, following the same discipline the spec asks of API providers — see [CHANGELOG.md](./CHANGELOG.md) for how that's tracked here.

## License
 MIT License. 
