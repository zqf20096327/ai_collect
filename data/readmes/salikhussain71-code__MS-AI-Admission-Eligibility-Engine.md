# MS AI Admission Eligibility Engine

A source-grounded Python eligibility engine for evaluating applicant profiles against published admission requirements for selected AI and computer science master's programs.

The system converts program-specific admission requirements into structured rules and evaluates applicant inputs such as:

* Undergraduate CGPA
* English-language proficiency
* GRE requirements, where applicable
* Academic prerequisites
* Program-specific eligibility conditions

The goal is not to predict admission.

It answers a narrower question:

> **Does the applicant's provided profile satisfy the published eligibility criteria represented in the system?**

## 🎯 Current Programs

The current implementation covers selected master's programs at:

* MBZUAI
* KAUST
* LUMS

All eligibility rules should be traceable to the corresponding university's official admissions documentation.

## ⚠️ Important Limitation

Eligibility is not admission.

Meeting published minimum requirements does not guarantee:

* admission,
* scholarship,
* interview selection,
* research-supervisor availability, or
* funding.

Admission requirements can also change between application cycles. Users should verify the current official university requirements before applying.
