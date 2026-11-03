# Jev / System One Reference

A practical technical reference for engineers and coding assistants building with Jev. It covers the API, implementation patterns, known limitations and a reusable project handover template.

Maintained by **Sebastian Bennis**. This is an independent reference, not an official TypeSafe AI publication.

**Start with [Jev_System_One_Reference.md](./Jev_System_One_Reference.md#s0).** This README explains how to use that file. It does not replace the technical reference.

This is a documentation repository, not an application, an SDK or a deployed service. The prompts and project brief below are worked examples, not evidence that an integration has been built or tested.

## Repository layout

Keep the documentation files together at the repository root:

```text
.
├── README.md
├── Jev_System_One_Reference.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
└── .gitignore
```

`README.md` is the entry point. The reference contains the API guidance, examples, known limitations, source catalogue and an unpopulated project handover in Section 0.4.

## How to use it

1. **Give the assistant access to the reference.** Attach the actual Markdown file to a session, or make it available in the project workspace and explicitly ask the assistant to read it. Do not assume that naming a file or sharing a repository URL means its contents have been read.
2. **Supply the project brief and available files.** Explain what you want built, what goes in and comes out, any language or integration constraints, and how success will be checked. For an existing project, also provide the current code and handover.
3. **Ask for implementation, verification and an updated handover.** The assistant should separate completed work from planned work and record checks that could not be run.

The coding assistant uses the reference to write the implementation. The resulting application calls Jev for typed judgements. The reference describes Jev as accepting text or structured state, not as a model for generating code, conversation or audio. See [what Jev does and cannot do](./Jev_System_One_Reference.md#s1).

For public repositories, keep the reference's handover template unpopulated. The workflow below uses a separate `HANDOVER.private.md` in a private project workspace as the live instance of Section 0.4. This is a suggested working file to create, not a file supplied by this repository.

## Worked example: build a support-ticket router

### The project brief

Build a local service that accepts a support message and returns a proposed team, an urgency judgement and a review status. It must not send messages, issue refunds or change a customer's account.

The [complete example in Section 3](./Jev_System_One_Reference.md#s3) uses this synthetic message:

> I have been charged twice for my order. I am frustrated and need this resolved today.

It asks three separate questions about the same message:

| Question | Jev type | Purpose |
|---|---|---|
| Which team should handle the main issue? | `choice` | Select `billing`, `technical`, `sales` or `other` |
| Does the message explicitly request urgent handling? | `noul` | Judge whether urgency is stated |
| How does the customer express frustration? | `score` | Evaluate the message against a descriptive rubric |

The reference's hand-authored response fixture selects `billing` and returns an urgency value of `0.95`. These values demonstrate the response format; they are not observed API results or guaranteed predictions.

The application should validate the response and apply its own review policy. For this first demo, return the proposed team for human review and keep automatic routing disabled. Later automation would require a separately validated policy, not an arbitrary confidence threshold. See [uncertainty and gates](./Jev_System_One_Reference.md#s10).

### Copy this prompt into a coding session

Provide the reference file alongside this prompt:

```text
Read Jev_System_One_Reference.md, starting with Section 0.
Follow its reading map for a first native-v1 integration.

Project:
Build a new local support-ticket routing demo in Python. There is no
existing application. Jev should evaluate a message; ordinary code
should validate the result and decide how to present it for review.

Requirements:
- Accept a non-empty support-message string.
- Use the question set from the complete example in Section 3.1:
  department, is_urgent and frustration.
- Retain the other option for messages outside the named departments.
- Return the proposed team, typed judgements and review status.
- Keep the demo review-only. Do not contact customers, issue refunds,
  update accounts, deploy or make paid API calls.
- Keep question definitions separate from application policy.
- Provide a clearly labelled mock mode that works without credentials.
- Prepare a live adapter, but mark it unverified until authorised testing.
- Read credentials from the environment; never embed a real key.
- Handle invalid input, malformed responses and API failures explicitly.
  Do not turn failures into successful routing results.

Before implementation:
Inspect the available workspace. Check the current official provider
contract before finalising live integration code. Preserve approved
pinned versions; do not silently switch providers or API formats.
If documentation or required tools are unavailable, record the gap
and continue only with work supported by the reference and fixtures.

Deliverables:
Provide the implementation, synthetic test cases, relevant offline
tests and exact setup/run instructions. Use mock behaviour where
live access is unavailable. Distinguish tests of code and fixtures
from tests of real model accuracy.

Handover:
Keep the public reference unchanged. In the private project workspace,
create HANDOVER.private.md using Section 0.4 as its template. Treat
that file as the live project handover. Record the actual files,
approved decisions, test results, unresolved issues, stopping point
and next action. Leave unsupported fields UNKNOWN.

At the end, state what was implemented, what passed, what failed and
what was not tested. Update the private handover. If you cannot edit
files, return the proposed files and handover content and say that
they have not been saved or executed.
```

To adapt this example, replace the project description, language, inputs, outputs and acceptance criteria. Retain the instructions about evidence, version handling, verification and private handovers. Do not force every feature into Jev; keep deterministic operations in code and text generation in an appropriate separate component, as described in [the integration checklist](./Jev_System_One_Reference.md#s15).

### What to check before calling the demo complete

The acceptance checks below are proposed for this example, not completed tests:

| Check | Expected behaviour |
|---|---|
| Mock execution | Runs without credentials and clearly identifies its output as synthetic |
| Empty or invalid input | Rejects the input before any model call |
| Valid synthetic response | Preserves the typed fields and returns a proposed team for review |
| An `other` result | Does not invent a team or force a match |
| Malformed response or simulated API failure | Returns an explicit failure/review outcome, not a successful routing result |
| Live adapter | Reported as unverified unless an authorised live check was actually run |

A mock returning `billing` proves the local handling of that fixture, not Jev's classification accuracy. Assess real outcomes separately using labelled examples from the intended task. The reference's [first-integration checklist](./Jev_System_One_Reference.md#s15) explains that distinction.

## Continue in another session or with another assistant

Supply the latest reference, current code and the private handover through an authorised private channel. A handover without the files it refers to is not enough to verify implementation progress.

```text
Continue this project using:
- Jev_System_One_Reference.md
- HANDOVER.private.md, the live instance of Section 0.4
- The available project files

Read Section 0 and the private handover, then inspect the referenced
code and available test evidence.

Briefly state the objective, verified progress, exact stopping point
and next authorised action. Flag missing files or any disagreement
between the handover and the actual workspace. Do not assume that
planned work exists or that implemented work has been tested.

Continue the next authorised action. Preserve approved decisions,
pinned versions and other contributors' work. Run the relevant
available checks and report anything that could not be verified.

Update HANDOVER.private.md with changed files, test outcomes,
remaining issues and the new stopping point. Keep the public
reference unchanged. If the handover is not editable, return its
updated contents for me to save.
```

The reference includes a [fresh-session continuation test](./Jev_System_One_Reference.md#s17). Use it with the assistants and tools intended for the project. It is a proposed test, not a guarantee that every model will continue reliably.

## Try the existing offline example

There is no application to install from this repository. The reference does, however, contain a complete request, a synthetic response and four offline example tests in [Section 3](./Jev_System_One_Reference.md#s3).

To run those checks, copy the corresponding blocks into a local folder as:

```text
request.json
response.example.json
test_reference_example.py
```

Then run with Python 3:

```bash
python3 -m unittest -v test_reference_example.py
```

These are snippets to save from the reference, not separate files supplied here. The checks validate example structure and internal arithmetic only. They require no API key and do not establish server acceptance or model accuracy. The optional live smoke call is documented separately in Section 3.2 and requires authorised access.

## Real-world example: Jev Ultrafast

[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) is an MIT-licensed browser agent from Browser Use that uses Jev for its decisions. It is a separate project, not affiliated with this reference, but it applies several patterns the reference describes:

| Pattern in this reference | How Jev Ultrafast applies it |
|---|---|
| [Speculative fan-out](./Jev_System_One_Reference.md#s12) | One request asks for the next operation and, alongside it, a target for each operation that could be chosen. Code uses only the target matching the chosen operation |
| [Keep generation out of Jev](./Jev_System_One_Reference.md#s1) | Jev chooses operations and page elements. A small LLM writes text only when the chosen operation is `TYPE_TEXT` |
| [Include a no-match option](./Jev_System_One_Reference.md#s2) | `DONE` and `BLOCKED` options let the model stop, or report that no operation can make progress |
| [Confidence is not permission](./Jev_System_One_Reference.md#s10) | Responses are validated before execution, and a `DONE` choice still requires independent outcome verification |
| [Adversarial content](./Jev_System_One_Reference.md#s11) | Page text is passed as untrusted data, never as instructions |

As reported by that project, a Google Flights search from a one-sentence goal completed in 7.1 seconds, using 17 Jev requests with a median latency of 178 ms. The project describes this as three repeats of one task, not a general reliability benchmark. Those figures have not been reproduced here; see its [performance report](https://github.com/browser-use/jev-ultrafast/blob/main/docs/performance.md) for the measurement boundaries.

## Keep project information private

The public repository should contain the reusable reference and this README, not a populated client or internal-project handover.

Keep the live `HANDOVER.private.md` outside the public repository in a private project workspace. Maintain one current handover there rather than competing summaries. Give a new assistant access only to the project material it is authorised to use.

Do not publish credentials, private repository paths, customer messages, client details, internal logs or sensitive test output. Use synthetic examples in public documentation. Record references to authorised evidence in the private handover rather than copying secrets or unnecessary personal data into it.

Review actual changes before publishing them. A blank template does not establish that a later populated version is suitable for public release. These practices follow the reference's [handover maintenance guidance](./Jev_System_One_Reference.md#s17).

## Find the right part of the reference

| Task | Start here |
|---|---|
| Understand Jev and select question types | [Sections 1–2](./Jev_System_One_Reference.md#s1) |
| Build a native-v1 integration | [Section 3](./Jev_System_One_Reference.md#s3), then follow the reading map in Section 0 |
| Use a gateway or migrate older code | [Section 4](./Jev_System_One_Reference.md#s4) |
| Improve questions and decision policy | [Section 7](./Jev_System_One_Reference.md#s7) and [Section 10](./Jev_System_One_Reference.md#s10) |
| Review failure modes | [Section 11](./Jev_System_One_Reference.md#s11) |
| See the patterns in a real project | [Real-world example: Jev Ultrafast](#real-world-example-jev-ultrafast) |
| Check sources and verification scope | [Section 16](./Jev_System_One_Reference.md#s16) and [Section 0](./Jev_System_One_Reference.md#s0) |
| Resume project work | [Section 0.4](./Jev_System_One_Reference.md#handover), instantiated in the private handover, and [Section 17](./Jev_System_One_Reference.md#s17) |

## Reference status

This README accompanies public reference edition `1.1.1`, prepared on 22 September 2026 from a source snapshot compiled on 20 September 2026. Technical descriptions above are drawn from that reference; the project workflow and prompts are illustrative guidance.

Check the official sources linked in the reference before relying on mutable details such as provider access, model availability, SDK versions, pricing or data terms. Record consequential changes and do not silently replace pinned versions.

The reference records limited documentation checks and offline fixture validation. It does not establish a live project integration, reproduced benchmark results or successful cross-model continuation. Its current verification scope and proposed continuation checks are recorded in [Section 17](./Jev_System_One_Reference.md#s17).

## Contributing

Corrections and practical improvements are welcome. Include a source, the relevant model or SDK version, and the reason for the change. Distinguish an observed result from a proposal, a mock response or a vendor-reported measurement.

Keep examples synthetic and the public handover template blank. Do not include credentials, private project information or customer data in an issue, pull request or test fixture.

## Licence and attribution

The repository's original contributions and original code examples are available under the [MIT licence](./LICENSE). Third-party quotations, excerpts and source material are not relicensed by this repository; see [third-party notices](./THIRD_PARTY_NOTICES.md).

The technical reference retains its [source catalogue](./Jev_System_One_Reference.md#s16) and the qualifications attached to reported results. Repository authorship does not imply authorship of the underlying TypeSafe documentation or third-party research.
