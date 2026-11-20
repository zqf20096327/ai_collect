# <img src="assets/icon.svg" alt="" width="40" align="top"> Akinly

[![CI](https://github.com/valburkin/Akinly/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/valburkin/Akinly/actions/workflows/ci.yml?query=branch%3Amain)
[![CodeQL](https://github.com/valburkin/Akinly/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/valburkin/Akinly/actions/workflows/codeql.yml)
[![Coverage floor](https://img.shields.io/badge/coverage%20floor-95%25%20lines%20%7C%2090%25%20branches-brightgreen)](https://github.com/valburkin/Akinly/blob/main/.github/scripts/check_coverage.py)\
[![Akinly on NuGet](https://img.shields.io/nuget/v/Akinly?label=Akinly&logo=nuget)](https://www.nuget.org/packages/Akinly)
[![Akinly.AI on NuGet](https://img.shields.io/nuget/v/Akinly.AI?label=Akinly.AI&logo=nuget)](https://www.nuget.org/packages/Akinly.AI)
[![Akinly.VectorData on NuGet](https://img.shields.io/nuget/v/Akinly.VectorData?label=Akinly.VectorData&logo=nuget)](https://www.nuget.org/packages/Akinly.VectorData)\
[![.NET 10](https://img.shields.io/badge/.NET-10-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/download/dotnet/10.0)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/valburkin/Akinly/blob/main/LICENSE)
[![Built with Claude Code](https://img.shields.io/badge/built%20with-Claude%20Code-D97757?logo=claude&logoColor=white)](https://github.com/valburkin/Akinly#how-this-was-built)

Incremental clustering of short texts for .NET. Akinly groups items that say the same thing (support tickets, feedback, complaints, survey answers, posts) as they arrive, gives each group an id that lasts, and can leave the close calls to a judge: a language model of your choice, local or in the cloud, a rule, or a person.

## Why

You have a stream of short texts and want to know which of them describe the same thing, so you can count them, link to them, and act on each problem once. Three common approaches fall short:

- **A similarity threshold on embeddings.** Embeddings capture what a text is about well, and what exactly it says only roughly. "My landlord won't fix the heating" and "I can't find an apartment I can afford" are both about housing and close in embedding space, but they are different problems. A low threshold chains such texts into a few broad clusters; a high one splits texts that say the same thing in different words. No single number does both.
- **A language model for every item.** A model can tell "the same problem" from "the same topic", but asking it about every item against every candidate cluster costs a call per comparison, which does not scale to a stream.
- **Batch clustering (k-means, HDBSCAN).** It sees all items at once and returns new labels on every run, so a group has no id you can store, link to, or show on a page next month.

Akinly uses similarity where it is clear and asks a judge only where it is not. Clusters keep their ids for good: when two clusters merge, you are told which id lives on and which one now redirects to it.

## Features

- **Incremental.** Add items one at a time or in batches; each joins a cluster or starts one. Items that come back after months join the cluster they belong to.
- **Lasting cluster ids.** Ids are handed out in order and never reused. A merge reports `from` and `into`, so you can redirect links.
- **A judge for close calls only.** Clear cases are decided by similarity; only items in a middle band of similarity become questions.
- **Questions as data.** Questions come back as records with everything a judge needs except the texts. Answer them live, through a provider's batch API, from a queue, or by hand, minutes or days later.
- **Any model.** `Akinly.AI` works with any `IChatClient` and `IEmbeddingGenerator` from Microsoft.Extensions.AI: Ollama, OpenAI, Azure OpenAI and others.
- **Any vector database with a connector.** `Akinly.VectorData` keeps clusters in a Microsoft.Extensions.VectorData store; Qdrant and PostgreSQL with pgvector are tested. An in-memory store with JSON export comes in the core package.
- **Maintenance.** Clusters that turn out to be one are merged; loose clusters can be split in cosine-only setups; labels (one-sentence titles) are written and refreshed as clusters grow.
- **Safe to operate.** Options are validated at startup; a judge's failure never counts as a "no"; removals keep centroids exact; telemetry and logs never carry an item's text.

## Install

Akinly is on nuget.org as three packages. Add the ones you need:

| Package | What it holds | Use it when |
|---|---|---|
| [`Akinly`](https://www.nuget.org/packages/Akinly) | The clusterer, options, questions and verdicts, the in-memory store, dependency injection, telemetry | Always; on its own when you have embeddings and answer questions yourself |
| [`Akinly.AI`](https://www.nuget.org/packages/Akinly.AI) | `TextClusterer` (texts in, clusters out), `ChatClientJudge`, `ChatClientLabeler`, `JudgePrompts` | You want a model to embed texts, decide close calls, or write labels |
| [`Akinly.VectorData`](https://www.nuget.org/packages/Akinly.VectorData) | `VectorDataClusterStore` over any Microsoft.Extensions.VectorData connector | You want the clusters in Qdrant, PostgreSQL with pgvector, or another vector database |

```bash
dotnet add package Akinly.AI
```

`Akinly.AI` and `Akinly.VectorData` each bring `Akinly` with them. You add the model's or the database's own package yourself (OllamaSharp, Microsoft.Extensions.AI.OpenAI, a Semantic Kernel connector).

## Quick start

### Texts in, clusters out, with a local model

With [Ollama](https://ollama.com) running, the two models of the [evaluation](docs/evaluation/README.md)'s local setup pulled (`ollama pull qwen3-embedding:8b`, `ollama pull gemma4:12b`; about 13 GB, best on a GPU), and the OllamaSharp package added:

```csharp
using Akinly;
using Akinly.AI;
using Microsoft.Extensions.AI;
using OllamaSharp;
using OllamaSharp.Models.Chat;

var ollama = new Uri("http://localhost:11434");
using var embedder = new OllamaApiClient(ollama, "qwen3-embedding:8b");   // embeds the texts
using var chat = new OllamaApiClient(ollama, "gemma4:12b");               // decides close calls and writes labels

// Thresholds calibrated for qwen3-embedding:8b; the defaults are for OpenAI's text-embedding-3-small.
var options = new ClusteringOptions
{
    EmbeddingModel = "qwen3-embedding:8b",
    JoinSimilarity = 0.96,
    CheckSimilarity = 0.57,
    MergeSimilarity = 1.0,   // no similarity was safe without a judge
    MergeCheckSimilarity = 0.75,
};

// A short answer needs no reasoning: with thinking off, the model answers much faster.
var noThinking = new ChatOptions { RawRepresentationFactory = _ => new ChatRequest { Think = false } };
var textOptions = new TextClustererOptions { Judge = { ChatOptions = noThinking }, Labeler = { ChatOptions = noThinking } };

var clusterer = new TextClusterer(embedder, chat, options, textOptions);

await clusterer.AddAsync(
[
    new TextItem("t1", "The heating in my apartment has been broken for two weeks."),
    new TextItem("t2", "My landlord raised the rent by 30 percent this year."),
    new TextItem("t3", "There is no heat in our unit and it is freezing."),
    new TextItem("t4", "I can't afford the new rent after the increase."),
    new TextItem("t5", "Our radiators are cold and the landlord won't fix them."),
]);

await foreach (var cluster in clusterer.ListClustersAsync())
{
    var members = await clusterer.GetMembersAsync(cluster.Id);
    Console.WriteLine($"{cluster.Id} {cluster.Label ?? "(no label yet)"}: {string.Join(", ", members)}");
}
```

`AddAsync` embeds the texts, places them, asks the model about the close calls until every question is answered, checks for merges, and labels clusters that reached three members. Here it makes two clusters, heating (t1, t3, t5) and rent (t2, t4), and labels the first. What the clusters look like depends on the models and the thresholds; for another embedding model, [calibrate them](docs/how-to/calibrate-thresholds.md).

### Cosine only, no chat model

Without a judge, an item joins its nearest cluster at or above one threshold and starts its own below it. Pass no chat client and options without an ask zone:

```csharp
var clusterer = new TextClusterer(
    embedder,
    chat: null,
    ClusteringOptions.CosineOnly("qwen3-embedding:8b", joinSimilarity: 0.96));   // the join threshold calibrated for it
```

### Your own embeddings

The core package takes vectors from anywhere and needs no model. This example runs as is; three-dimensional vectors keep it short, where real embeddings have hundreds of dimensions:

```csharp
using Akinly;
using Akinly.Storage;

var clusterer = new Clusterer(new InMemoryClusterStore(), ClusteringOptions.CosineOnly("toy-3d", joinSimilarity: 0.85));

var step = await clusterer.AddAsync(
[
    new ClusterItem("ticket-1", new float[] { 1.00f, 0.00f, 0.00f }),   // "The heating is broken"
    new ClusterItem("ticket-2", new float[] { 0.82f, 0.57f, 0.00f }),   // "Heating and hot water are both out"
    new ClusterItem("ticket-3", new float[] { 0.97f, 0.26f, 0.00f }),   // "No heat in my apartment"
    new ClusterItem("ticket-4", new float[] { 0.00f, 0.00f, 1.00f }),   // "My rent went up 30 percent"
]);

foreach (var placement in step.Placements)
{
    Console.WriteLine($"{placement.ItemId} -> cluster {placement.ClusterId} ({placement.Reason})");
}
// ticket-1 -> cluster 1 (NewCluster)
// ticket-2 -> cluster 2 (NewCluster)
// ticket-3 -> cluster 1 (Similarity)
// ticket-4 -> cluster 3 (NewCluster)

// ticket-3 pulled cluster 1 toward cluster 2: maintenance finds that they are now one.
var maintained = await clusterer.MaintainAsync();
foreach (var merge in maintained.Merges)
{
    Console.WriteLine($"cluster {merge.FromId} merged into cluster {merge.IntoId}");
}
// cluster 2 merged into cluster 1
```

[Getting started](docs/getting-started.md) walks through this example and the next steps.

## How it works

Each item is compared with its nearest clusters. Its similarity to the nearest one decides what happens:

| Similarity to the nearest cluster | Zone | What happens |
|---|---|---|
| At or above `JoinSimilarity` (default 0.83) | Join | The item joins without a question |
| From `CheckSimilarity` (default 0.30) up to the join threshold | Ask | A judge picks the cluster the item belongs in among its nearest (up to `JoinChoices`, default 3), or none. On "none", the next nearest clusters are tried, up to `MaxChecksPerItem` (default 3) refusals |
| Below `CheckSimilarity` | New | The item starts a cluster of its own |

Only the middle zone costs a judge's answer, and it is where similarity alone cannot tell "the same thing" from "the same topic". The thresholds belong to an embedding model: the defaults were calibrated for OpenAI's `text-embedding-3-small` on public intent datasets, and `akinly-eval calibrate` (the evaluation tool in `tools/Akinly.Evaluation`, run from a clone of this repository) suggests values for another model from labeled data. Where the ask zone starts also depends on your data: `ThresholdCalibrator` sets it from your own judge's answers.

Placement happens in arrival order, so an early item can start a cluster that later turns out to duplicate another. **Maintenance** (`MaintainAsync`, which `TextClusterer` runs after each add) compares the clusters that changed with their neighbors and merges pairs in the same three zones, by the average similarity of their members: certain pairs at once, close pairs after a judge says a member of each belongs in the other. The larger cluster keeps its id. A judge's failure is never read as "different": the question is asked again, and after the last attempt similarity alone decides.

[Concepts](docs/concepts.md) explains each part in depth.

## Documentation

- [Getting started](docs/getting-started.md): install, the first clusterer, reading results, persisting.
- [Concepts](docs/concepts.md): items, clusters and lasting ids, zones, questions and verdicts, merges, splits, labels, the store.
- [Configuration](docs/configuration.md): every option, its default, and when to change it.
- How-to guides:
  - [Use a local Ollama model](docs/how-to/use-ollama.md)
  - [Use OpenAI, Azure OpenAI or any other provider](docs/how-to/use-openai.md)
  - [Cluster without a language model](docs/how-to/cluster-without-a-model.md)
  - [Answer questions yourself or through a batch API](docs/how-to/answer-questions-yourself.md)
  - [Keep chosen clusters apart with a merge policy](docs/how-to/merge-policy.md)
  - [Keep clusters in Qdrant](docs/how-to/use-qdrant.md)
  - [Keep clusters in PostgreSQL with pgvector](docs/how-to/use-postgresql.md)
  - [Label clusters](docs/how-to/label-clusters.md)
  - [Remove items](docs/how-to/remove-items.md)
  - [Calibrate thresholds for your embedding model](docs/how-to/calibrate-thresholds.md)
  - [Run in ASP.NET Core or a worker service](docs/how-to/dependency-injection.md)
  - [Observe with OpenTelemetry](docs/how-to/opentelemetry.md)
  - [Save and restore the in-memory store](docs/how-to/save-and-restore.md)
- [Troubleshooting](docs/troubleshooting.md) and [FAQ](docs/faq.md).
- [Design](docs/design.md): the design record, with the decisions and their reasons.
- [Changelog](CHANGELOG.md).

## Evaluation

Akinly 1.0 was measured on five public labeled datasets with `akinly-eval` (`tools/Akinly.Evaluation`), which anyone can rerun; 1.1's changes were measured on development samples, against 1.0's defaults ([Akinly 1.1 on development samples](docs/evaluation/README.md#akinly-11-on-development-samples)). Texts arrive one at a time, in one pass, and Akinly is never told how many groups there are (59 to 269 groups here). Four of the datasets are below (Tweets-T is in the full results). The table gives accuracy in percent on the test splits, and NMI over the whole News-T stream. The criterion is fitted to the data, and the thresholds are calibrated on other texts. The scores measure grouping quality only; lasting ids and incremental placement, which k-means lacks, are not scored. Each baseline uses the same embeddings as the Akinly row above it:

| Setup | Method | Banking77 | CLINC150 | MASSIVE | News-T (NMI) |
|---|---|---|---|---|---|
| Cloud: OpenAI `text-embedding-3-small`, Claude Haiku 5.5 | **Akinly** | **63.6** | **80.3** | **54.3** | **86.1** |
| | k-means, told the number of groups | 57.2 | 69.3 | 54.4 | 87.8 |
| | Akinly without a judge (similarity only, calibrated thresholds) | 17.2 | 34.4 | 8.5 | 81.9 |
| Local: `qwen3-embedding:8b`, `gemma4:12b` | **Akinly** | **57.8** | **76.2** | **50.7** | **87.6** |
| | k-means, told the number of groups | 67.9 | 69.5 | 57.7 | 86.4 |
| | Akinly without a judge (similarity only, calibrated thresholds) | 20.4 | 44.5 | 12.9 | 82.9 |

- **The judge is what makes incremental clustering work.** On the intent datasets it adds 32–46 points of accuracy over similarity alone at the calibrated thresholds, and 8–35 points over the threshold that scores best on the labels, at $0.05–0.13 per 1,000 texts with Claude Haiku.
- **Akinly roughly matches k-means without being told the number of groups.** In the cloud it is ahead on Banking77 and CLINC150 and level on MASSIVE. Locally it is ahead on CLINC150 and behind on Banking77 and MASSIVE.
- **It's level with recent LLM-based methods.** With Claude Haiku, it is level with LLM-MemCluster (GPT-4.1-mini, single pass, given a range for the number of groups) on MASSIVE, and with IntentGPT (GPT-4, starting from some known intents) on Banking77; it is 3 points behind IntentGPT on CLINC150. Methods given more help, such as the number of groups or an embedder fine-tuned per dataset, score higher. The protocols differ; see the full results.
- **The remaining gap is the judge's.** With a perfect judge (the labels answering), the same structure reaches about 94% accuracy on development samples of Banking77 and CLINC150.
- **Where it loses.** With OpenAI's embeddings on the News-T and Tweets-T streams, k-means told the number of groups beats Akinly, and so does a similarity threshold chosen on the stream's own labels (on Tweets-T, on accuracy and ARI, not NMI). On Tweets-T, batched stream methods score higher. Akinly also makes more clusters than there are groups: precision is high, recall lower.

The full results, the published methods, and the cluster counts are in [docs/evaluation](docs/evaluation/README.md).

## Requirements

- .NET 10 (`net10.0`). The SDK version used to build is pinned in [global.json](global.json).
- For `Akinly.AI`: a Microsoft.Extensions.AI adapter for your model provider.
- For `Akinly.VectorData`: a Microsoft.Extensions.VectorData connector for your database, built against Microsoft.Extensions.VectorData.Abstractions 10.x.

## Versioning

The packages follow [Semantic Versioning](https://semver.org/): a breaking change to the public API comes only in a major version. The public API is tracked in each package's `PublicAPI.Shipped.txt`, and each release after 1.0.0 is checked against the one before it. A newer Akinly reads every store an older one wrote. What changed in each version is in the [changelog](CHANGELOG.md).

## How this was built

Akinly was written with [Claude Code](https://claude.com/product/claude-code), Anthropic's AI coding assistant, working under the maintainer's direction: the code, the tests and the documentation, including this README. The maintainer chose the approach, decided what to measure, and decides what is published. Each change passes the build's gates (analyzers with warnings as errors, the tests, a coverage floor) and a review by a separate AI agent before it is committed.

The first nine commits in this repository replay the clusterer's earlier development and keep their original dates, but their files were rewritten for this repository when it became a standalone library: the names, the documentation and the build setup (SDK version, analyzers, packages) are those of the library, not of the code at the time. Measurements quoted from that earlier work (in [docs/design.md](docs/design.md#what-we-know-already)) were taken on private data; claims about Akinly itself rest on the public evaluation above.

## Contributing and security

Contributions are welcome: read [CONTRIBUTING.md](CONTRIBUTING.md) first, and open an issue before a large change. Everyone taking part follows the [code of conduct](CODE_OF_CONDUCT.md). Report a vulnerability privately, as [SECURITY.md](SECURITY.md) describes, never in a public issue.

## License

[MIT](LICENSE), © 2026 Valentin Burkin ([github.com/valburkin](https://github.com/valburkin)).
