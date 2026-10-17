
[Docs](https://diffgram.readme.io/docs)
•
[Diffgram.com](https://diffgram.com/)
•
[Request Slack Invite](https://www.jotform.com/form/222377866413058)

# News
June 22 2026: New from the team behind Diffgram: [fak](https://github.com/anthony-chaudhary/fak) — *the agent kernel*, an open source Go binary that governs what AI agents are allowed to *do* at serve time (capability gating, tool-result quarantine, audit). See the section below.

June 12 2026: New from the team behind Diffgram: [DOS (dos-kernel)](https://github.com/anthony-chaudhary/dos-kernel) — an open source trust kernel that verifies what AI agents actually did, instead of believing their self-reports. See the DOS section below.

Sept 28 2023: New [Diffgram license version 2 (DLv2)](https://diffgram.readme.io/docs/diffgram-license-v2-dlv2). Featuring [new contributor license (CL)](https://diffgram.readme.io/docs/diffgram-contributor-license-cl) available at no financial cost. MSA customers will receive a financial credit for all contributions.

# The AI Datastore
The AI Datastore for Schemas, BLOBs, and Predictions. Use with your apps or integrate built-in Human Supervision, Data Workflow, and UI Catalog to get the most value out of your AI Data.

[**Learn more**](https://diffgram.readme.io/docs)

# Use Cases

* **Use with your AI Apps** - One place for Compliant PII AI data.
* **Human Supervision (Data Labeling)** - Label all media types and scale your annotation.
* **AI Data Application Workflow** - Move data between your AI Apps and control your AI through a friendly UI/UX exp.
* **UI Catalog** - Visually Explore your AI Datastore.

## Data
Diffgram is installed by you and you have control over your data.

## Supervision (Data Labeling) Media Types
A popular use case is for human supervision
* [Grid & Multi-Modal](https://diffgram.readme.io/docs/multi-modal-annotation)
* [Conversational & LLM (Preview)](https://diffgram.readme.io/docs/conversational-annotation)
* [Image](https://diffgram.readme.io/docs/image-annotation)
* [Video](https://diffgram.readme.io/docs/video-introduction)
* [3D](https://diffgram.readme.io/docs/3d-annotation-overview)
* [Text](https://diffgram.readme.io/docs/text-annotation)
* [Audio](https://diffgram.readme.io/docs/audio-annotation)
* [GeoSpatial](https://diffgram.readme.io/docs/geospatial-annotation)
* [Document (Roadmap)](https://diffgram.readme.io/docs/annotation#document)
* [HTML (Roadmap)](https://diffgram.readme.io/docs/annotation#html)
* [DICOM (Roadmap)](https://diffgram.readme.io/docs/annotation#dicom)
* [Custom/Other](https://diffgram.readme.io/docs/annotation#custom)

## Getting Started
Watch the [Video Explainer](https://www.youtube.com/watch?v=dws6J3bDbcU), 
read the commercial open source [license](https://github.com/diffgram/diffgram/blob/master/LICENSE.md).

* [Install Diffgram](https://diffgram.readme.io/docs/install)
* [Sales Info](https://diffgram.readme.io/docs/sales)
* [Join us on Slack](https://www.jotform.com/form/222377866413058)
* [Contribute](https://diffgram.readme.io/docs/contribute)

## From the Team Behind Diffgram: Trust & Serving Infrastructure for AI Agents

Diffgram is built for humans supervising AI *data*. Our newer open source projects are built for
supervising the AI *agents* themselves — and they sit on opposite sides of the same moment.

**[DOS (dos-kernel)](https://github.com/anthony-chaudhary/dos-kernel)** is a small, deterministic
trust kernel that verifies what autonomous AI agents and coding agents *actually did* — from git
evidence and other witnesses an agent cannot forge — instead of trusting the agent's own "done"
report.

If you train or fine-tune models on agent-generated data, DOS's `reward()` verdict decides
whether an agent trajectory may enter the training set at all, rejecting "resolved" claims
that a non-forgeable witness refutes — training data quality for the agent era, the same
problem Diffgram's human supervision solves for labels.

* GitHub: [anthony-chaudhary/dos-kernel](https://github.com/anthony-chaudhary/dos-kernel)
* Install: `pip install dos-kernel` ([PyPI](https://pypi.org/project/dos-kernel/))
* Docs: [DOS documentation](https://anthony-chaudhary.github.io/dos-kernel/)

**[fak](https://github.com/anthony-chaudhary/fak)** — *the agent kernel* — is the other side of
that moment. Where DOS verifies what an agent *already did*, fak governs what an agent is
*allowed to do, as it happens*: a single static Go binary that sits in front of your model and
adjudicates every tool call at the boundary — a capability gate, tool-result quarantine, and
audit trail in one process. If Diffgram is where humans supervise AI data, fak is where the
agents working over that data are kept on a leash at serve time — the inline gate to DOS's
after-the-fact referee.

* GitHub: [anthony-chaudhary/fak](https://github.com/anthony-chaudhary/fak)
* Install: `go install github.com/anthony-chaudhary/fak/cmd/fak@latest`
* Docs: [fak documentation](https://anthony-chaudhary.github.io/fak/)

## More
Commercial firms have been using Diffgram since 2018 and we continue to stay up to date with the latest advances. Diffgram has 706 tests (E2E, unit etc) and we care greatly about quality.
* [News](https://diffgram.readme.io/docs/news)
* [Roadmap](https://diffgram.readme.io/docs/roadmap)
* [Development System](https://diffgram.readme.io/docs/development-system)
* [Updating Existing Install](https://diffgram.readme.io/docs/updating-an-existing-installation)
* [Training Data Book](https://www.oreilly.com/library/view/training-data-for/9781492094517/)
* [Ecosystem](https://diffgram.readme.io/docs/ecosystem)
* [Vision](https://diffgram.readme.io/docs/vision)
* [Features](https://diffgram.readme.io/docs/versions)
* [All Media Types](https://diffgram.readme.io/docs/annotation)
* [ML Program Integrations](https://diffgram.readme.io/docs/automation-and-prelabels)



