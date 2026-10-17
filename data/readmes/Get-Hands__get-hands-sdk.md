<p align="center">
  <a href="https://gethands.nl/">
    <img src="https://gethands.nl/assets/brand/marks/hands-mark-dark-1024.png?v=20260820" alt="Hands" width="144">
  </a>
</p>

<h1 align="center">Hands SDK</h1>

<p align="center"><strong>Build Sages. Shape Hands. Connect inference.</strong></p>

<p align="center">
  The public developer home being prepared for connectors, semantic discovery, portable agent
  definitions, marketplace software, and inference-provider integration across the Hands ecosystem.
</p>

<p align="center">
  <a href="https://gethands.nl/">Hands</a>
  &nbsp;·&nbsp;
  <a href="docs/getting-started.md">Getting started</a>
  &nbsp;·&nbsp;
  <a href="docs/sdk-reference.md">SDK reference</a>
  &nbsp;·&nbsp;
  <a href="ROADMAP.md">Roadmap</a>
  &nbsp;·&nbsp;
  <a href="https://discord.gg/RNDB3Qz5Zk">Discord</a>
</p>

> [!IMPORTANT]
> **Developer Preview.** The current SDK is an internal TypeScript prototype being prepared for its first public source and package release. There is no public npm install yet, and interfaces may change. This repository must not be described as GA or production-ready until the published artifacts and end-to-end release evidence exist.

## What you will be able to build

Hands is not another AI model. It gives the AI you choose a persistent workspace, approved connections, explicit permission boundaries, and an execution path. The SDK is the public surface for extending that system without opening the private runtime.

| Builder path | What you create | Status |
| --- | --- | --- |
| Connectors | Typed actions, authentication declarations, schemas, generated projections, and deterministic packages | Prototype implemented; public release in progress |
| Semantic skills and Tools Discovery Graph | Discoverable capability definitions, graph inputs, queries, and public evaluation fixtures | Planned phased release |
| Sages | Portable definitions for persistent deep workers that coordinate specialist Hands around an outcome | Planned phased release |
| Custom Hands | Portable specialist-agent profiles with requested capabilities and explicit boundaries | Planned phased release |
| Sage Marketplace | Reference catalog, submission, review, preview, and distribution software | Planned phased release |
| Inference providers | Adapters, conformance evidence, a governed Router test path, and onboarding requests | Planned phased release |

A Sage definition or Custom Hand profile can request a capability; it cannot grant itself access. Discovery recommends relevant tools; it does not authorize execution.

## Capability is not authority

Hands keeps five facts separate: a schema can be valid; a graph can recommend a tool; a profile can request a capability; a provider can pass compatibility tests; and a deployed runtime can authorize an execution. Only the last permits the action.

Local validation, discovery results, Marketplace listings, package candidates, and conformance reports never create account access or execution authority. Changing a model or provider route must not expand data access, recipients, action scope, spending, locality, or approval class.

## See the Hands SDK in action

This 40-second silent product vignette shows the outcome SDK builders are working toward. A user gives a Sheets Hand one request: read three Q3 invoices, update a sales overview in Google Sheets, and prepare an email to the accountant. The Hand works across Google Drive, Google Sheets, and Gmail, then waits for the user's review before sending. The same governed session continues on mobile.

This is an end-user workflow demonstration, not footage of a released SDK or developer quickstart. Its on-screen captions are in Dutch; an English visual transcript is provided below.

https://github.com/user-attachments/assets/dfe8cfcf-6806-40db-a741-2ef4eeb5ac02

[Watch or download the demo](https://github.com/user-attachments/assets/dfe8cfcf-6806-40db-a741-2ef4eeb5ac02) · [Read the English visual transcript](docs/demo-transcript.md) · [Watch the source on Google Drive](https://drive.google.com/file/d/1jjB3sTo8zQIXD0H-lnULRasD4Jdo-lmD/view)

## The connector path today

The prototype already proves an internal vertical slice:

1. define a connector with typed actions and authentication;
2. compile it into canonical intermediate representation;
3. generate discovery projections;
4. find it through graph-only tool discovery;
5. create a deterministic unsigned package with a lock file, SPDX 2.3 SBOM, and provenance request;
6. invoke it in local-project mode with `execution_authorized=false`.

The current command surface under stabilization is:

```text
hands-connector <validate|generate|pack|invoke> [action] \
  [--input JSON] [--project DIR] [--json]
```

This documents the implemented prototype interface; it is **not** an installation command. The public quickstart will be added only when a clean external environment can install the released package and reproduce its expected output.

## Authoring surface under stabilization

The TypeScript SDK currently implements connector and action builders including `defineConnector`, `defineQueryAction`, `defineMutationAction`, `defineDestructiveAction`, `defineNoAuth`, `defineApiKeyAuth`, `defineOAuth2`, `defineSkillRegistration`, and `schema`.

Schema helpers cover strings, integers, numbers, booleans, literals, enums, arrays, objects, optional values, nullable values, and JSON. Current protocol profiles are `native-static-v1`, `remote-mcp-v1`, and compatibility profile `native-static-v0`. Current authentication declarations cover no auth, API key, and OAuth 2.0 authorization code with PKCE.

See the [SDK reference](docs/sdk-reference.md) for the exact implemented/planned split. Basic, bearer, and brokered authentication; broader lifecycle builders; testkit, emulator, conformance tooling; and an isolated Package ABI host are not yet public features.

## What is open—and what is not

| Surface | Public direction | Private boundary |
| --- | --- | --- |
| SDK and connector contracts | Authoring APIs, schemas, validators, compiler/projection contracts, packaging, fixtures, and docs | Secrets, signing material, tenant operations |
| Skills and discovery | Public definitions, graph implementation/adapters, sample catalog, provenance-aware evaluation | Tenant graphs, private connector data, proprietary indexes |
| Sages, profiles, and marketplace | Portable definitions, validators, reference software, examples, submission contracts | Live worker memory, account bindings, payment/abuse operations |
| Provider integration | Adapter contract, local conformance, sandbox client, report format, onboarding path | Router ranking, fallback policy, qualification data, commercial terms |
| Hands runtime | Documented external contract and public-safe fixtures | Runtime and orchestration implementation |
| Fathom | Public integration boundary where needed | Source, indexes, extraction and code-intelligence implementation |
| Hands Router | Provider-facing compatibility and test contract | Routing implementation and operational decisions |

All advertised local paths must eventually run without private packages, internal registries, employee credentials, or Fathom. Until that release gate passes, this repository remains a documentation preview.

## Fathom 2.0: future work

Fathom is Hands' private code-intelligence layer. Its existing private evidence plane helps agents navigate symbols, calls, dependencies, routes, and change impact without inventing relationships.

Fathom 2.0 is the roadmap for a second, temporal project-canon plane that can tell an agent what people have already decided before it changes a system. Planned Codemap work is the “Google Maps for your code” direction: start with the whole system, zoom through subsystems, packages, semantic communities, and symbols, and arrive at exact source evidence without losing context. Canonical maps are intended to be derived deterministically from immutable evidence—not generated as AI topology.

Fathom 2.0, Architecture Atlas, and Codemap are planned private capabilities. They are not shipped SDK features and Fathom is not included in this repository. Read the [public-safe roadmap](docs/fathom-2-roadmap.md).

## Documentation

- [Getting started and release gates](docs/getting-started.md)
- [Connector SDK reference](docs/sdk-reference.md)
- [Sages and Custom Hands](docs/sages-and-custom-hands.md)
- [Provider testing and onboarding](docs/provider-onboarding.md)
- [Open-source boundary](docs/open-source-boundary.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [Community Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)

## Community

Join the [Hands Discord](https://discord.gg/RNDB3Qz5Zk), watch [Hands on YouTube](https://www.youtube.com/@gethands), read the [Hands Handbook](https://gethands.nl/connect), or contact [support@gethands.nl](mailto:support@gethands.nl).

If you are building a connector, Sage, Custom Hand, semantic skill, discovery adapter, or inference integration, tell us the outcome you want to enable and the evidence you need from the public release.

> **License status:** no public SDK source release or license decision is claimed here. The applicable license and notices will be published before source packages are opened for reuse and contribution.
