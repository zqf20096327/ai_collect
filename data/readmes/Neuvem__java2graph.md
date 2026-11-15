# java2graph → decypher-jvm

This repository is the JVM half of **Decypher v2** (the Go half is `../decypher`). It builds
`decypher-jvm`: a stateless extractor daemon spoken to over JSON-RPC 2.0 on stdio, plus the build-tool
integrations that produce the **build manifest**.

> The specification is [`../docs/design_doc.md`](../docs/design_doc.md) (DD-01 … DD-23); progress is tracked in
> [`../docs/implementation_log.md`](../docs/implementation_log.md). The previous (v1) implementation was removed at the M5 parity
> gate; it is in git history at the tag `v2-pre-legacy-removal`.

## Modules (Maven, parent `io.neuvem.decypher:decypher-jvm-parent`)

| Module | Release | Purpose |
|---|---|---|
| `manifest-schema` | 8 | Java types for `build-manifest.schema.json` |
| `dsh` | 17 | DSH1 shard writer/reader, symbol keys, xxh3, `Versions` |
| `extractor` | 17 | ASM extractor, dfsum, ABI hash, javac source map |
| `daemon` | 21 | JSON-RPC server, javac fast path, Gradle TAPI / BSP clients, Vineflower |
| `build-maven-ext` | 8 | Maven core extension → build manifest |
| `build-gradle-model` | 8 | Gradle plugin / `ToolingModelBuilder` → build manifest |
| `trace-agent` | 8 | Compiler trace java agent |
| `build-sbt-plugin` | — | sbt plugin (sbt build, not a Maven module) |

JDK 25 builds everything; each module compiles with its own `--release`. Dependencies are restricted
per module by `maven-enforcer-plugin` allow-lists (see each `pom.xml`).

## Build

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 25)     # any JDK >= 25
mvn -B verify                                       # all v2 modules
```

## Formats

The DSH1 shard format that `dsh` writes is specified in
[`../decypher/schemas/dsh1.md`](../decypher/schemas/dsh1.md) (META:
[`dsh1-meta.schema.json`](../decypher/schemas/dsh1-meta.schema.json)); the build manifest that the producers write is
[`../decypher/schemas/build-manifest.schema.json`](../decypher/schemas/build-manifest.schema.json).

## Versions

`dsh/src/main/resources/io/neuvem/decypher/dsh/versions.json` is the published source of the JVM
version numbers; `decypher/scripts/sync-versions.sh` vendors it into the Go repository, where a test
fails if the two sides disagree (DD-23.1).
