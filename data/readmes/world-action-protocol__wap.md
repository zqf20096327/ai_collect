# WAP — World Action Protocol

**An experimental interoperability protocol for machine experience.**

WAP records what an agent observed, what it predicted would happen, what action it took, and what actually happened.

```text
State → Prediction → Action → Observation → Experience
```

A coding agent expects a configuration change to fix a build with 75% probability. The build still fails. WAP keeps the original prediction, the attempted action, the measured failure, and the prediction score in one portable record. A sequence preserves the later attempts that eventually solve the problem.

**Start with the [proposal and plain-language abstract](RFC.md).** Core 0.1 is a repository draft for review, not an IETF standard or published RFC.

## What is here

| Artifact                                           | Purpose                                                                                            |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [RFC.md](RFC.md)                                   | Normative format, lifecycle, scoring, integrity, sequences, HTTP binding, security, and privacy    |
| [schemas/](schemas/)                               | JSON Schema Draft 2020-12 contracts                                                                |
| [examples/](examples/)                             | Complete synthetic coding, robotics, MCP, and recovery-sequence records                            |
| [TypeScript SDK](sdk/typescript/README.md)         | Validation, canonicalization, commitments, signatures, scoring, execution wrapper, and MCP adapter |
| [test-vectors/](test-vectors/)                     | Fixed canonical bytes, digest, and Ed25519 fixtures                                                |
| [Extensions](docs/extensions.md)                   | Future work separated from the implemented core                                                    |
| [Standardization roadmap](docs/standardization.md) | Review and possible Internet-Draft publication steps                                               |

## Try it

Requires Node.js 22.18 or newer, npm, and Python 3 for the independent fixed-vector check. Dependencies are pinned in `package-lock.json`.

```sh
npm ci
npm run check
npm run demo
```

The demo wraps an in-process mock MCP tool, commits the prediction, invokes the tool, observes failing tests, and prints a valid Experience. No network service, credentials, model API, or robot is needed. The demo journal is in memory; applications must supply durable persistence before claiming Core producer conformance.

```typescript
import { execute } from "./sdk/typescript/src/index.ts";

// See examples/mcp-demo.ts for complete runnable inputs and callbacks.
const experience = await execute({
  intent, // actor, environment, state, selected action, predictions
  persistCommitment, // await durable storage before dispatch
  execute: runAction, // returns { status, result }; never automatically retried
  observe: measureOutcome,
  persistExperience,
});
```

The API snippet is illustrative; the complete runnable version is [examples/mcp-demo.ts](examples/mcp-demo.ts).

## Current boundaries

One reference SDK is implemented. HTTP storage is specified but no HTTP server ships here. The MCP adapter uses an already initialized client; the demo is mocked. Independent full-protocol interoperability, real operational datasets, external witness receipts, and an Internet-Draft submission remain future milestones.

A valid hash detects changes. A valid signature binds bytes to a key. Neither establishes honest observations, pre-outcome timing, or causation. See the [trust model](RFC.md#13-security-and-trust).

Feedback and independent implementations are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md). Code and repository documents use the [MIT license](LICENSE); operational datasets require their own rights and consent.
