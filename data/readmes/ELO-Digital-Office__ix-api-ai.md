# ELO Indexserver REST API: AI Coding Agent Guide and Examples

This repository provides **ELO Indexserver REST API** documentation, schema
references, and practical **ELO API examples** for developers and **ELO AI
coding agents**. Use it to build or troubleshoot applications that communicate
with an ELO repository through the Indexserver REST API.

## Project scope

- **Product:** ELO Indexserver (IX), the REST API for accessing an ELO repository.
- **API:** Indexserver REST endpoints and JSON data models; the included OpenAPI
  reference is version **25.0.1.5**.
- **Examples:** JavaScript examples for browser and Node.js usage.
- **Not in scope:** SOAP/legacy APIs, ELO product UI development, or database
  access that bypasses the Indexserver.

## Start here

AI coding agents: load the skill
[skills/elo-indexserver-rest/SKILL.md](skills/elo-indexserver-rest/SKILL.md)
before writing code. Agents working *on* this repository additionally read
[AGENTS.md](AGENTS.md).

Developers: start with the [knowledge base](knowledge/README.md), then pick a
matching example in [examples/rest](examples/rest/README.md). Check API
signatures and data types in the generated references and adapt the example to
the target Indexserver version and environment.

## Repository layout

| Path | Content |
| --- | --- |
| [skills/elo-indexserver-rest/](skills/elo-indexserver-rest/SKILL.md) | Agent skill: core rules and compact task references (authentication, documents, metadata, search, workflows) |
| [knowledge/](knowledge/README.md) | Concepts, task guides, patterns, and troubleshooting |
| [api/v25.0.1.5/](api/v25.0.1.5/openapi.json) | OpenAPI definition and generated [operations](api/v25.0.1.5/generated/operations.md) and [schemas](api/v25.0.1.5/generated/schemas.md) |
| [examples/rest/](examples/rest/README.md) | JavaScript examples for browser and Node.js |
| [scripts/](scripts/) | Documentation generator and validation scripts |
| [.github/](.github/copilot-instructions.md) | Copilot instructions and CI workflow |

## Common tasks and examples

- **Authentication and session tickets:** [login.js](examples/rest/javascript/login.js)
- **REST request patterns:** [rest-call.js](examples/rest/javascript/rest-call.js)
- **Create and upload a document:** [insert-document.js](examples/rest/javascript/insert-document.js)
- **Create a folder:** [insert-folder.js](examples/rest/javascript/insert-folder.js)
- **Set Generation 1 metadata:** [metadata-gen1.js](examples/rest/javascript/metadata-gen1.js)
- **Set Generation 2 metadata and aspects:** [metadata-gen2.js](examples/rest/javascript/metadata-gen2.js)
- **Search documents and metadata:** [find-fulltext.js](examples/rest/javascript/find-fulltext.js), [find-metadata.js](examples/rest/javascript/find-metadata.js), and [find-aspects.js](examples/rest/javascript/find-aspects.js)
- **List folder contents or descendants:** [find-children.js](examples/rest/javascript/find-children.js) and [find-descendants.js](examples/rest/javascript/find-descendants.js)
- **Move or reference repository objects:** [move-sord.js](examples/rest/javascript/move-sord.js) and [create-reference.js](examples/rest/javascript/create-reference.js)
- **Start workflows, list and forward workflow tasks:** [workflow.js](examples/rest/javascript/workflow.js)

## Common mistakes

- **Mixing Gen1 and Gen2 metadata structures.** Use the structures of the
  generation the target object uses; see
  [Metadata Generations](knowledge/concepts/metadata-generations.md).
- **Assuming a search returns all results at once.** Search results are paged;
  continue until no more results are reported. See
  [Pagination](knowledge/patterns/pagination.md).
- **Leaving search resources open.** Close every search with `findClose` in a
  `finally` block. See [Resource Cleanup](knowledge/patterns/resource-cleanup.md).
- **Using unverified request fields.** Check operation and field names in
  [operations.md](api/v25.0.1.5/generated/operations.md) and
  [schemas.md](api/v25.0.1.5/generated/schemas.md) before sending a request.

## Search terms

ELO Indexserver REST API, ELO REST API, ELO API examples, ELO AI coding
agent, ELO Indexserver client, ELO repository, Indexserver authentication,
document upload, Sord metadata, Generation 1 metadata, Generation 2 aspects,
Indexserver search, ELO workflow, start workflow, forward workflow task,
JavaScript REST client.

## Maintenance

```bash
python3 scripts/generate-api-docs.py          # regenerate api/*/generated/*.md
python3 scripts/generate-api-docs.py --check  # fail if generated files are outdated
python3 scripts/validate-skill.py             # skill front matter and Markdown links
scripts/validate-examples.sh                  # syntax check of the JavaScript examples
```

To add an API version, create `api/<version>/openapi.json` and run the
generator.

## Version and correctness

The generated API and schema references describe the version identified in
those files. Indexserver installations may expose different versions or
configuration-dependent behavior. Confirm endpoint availability, permissions,
authentication settings, and data types against the target system before
deploying an integration. Treat the examples as starting points and never
commit real credentials or session tickets.

## License

[MIT](LICENSE)
