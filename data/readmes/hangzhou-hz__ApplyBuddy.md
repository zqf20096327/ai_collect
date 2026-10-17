# ApplyBuddy

**English** | [简体中文](README.zh-CN.md)

> **Find the right jobs. Apply with your rules.**

ApplyBuddy is a rule-driven AI job application workspace for Codex. It helps you discover jobs, screen eligibility, choose the right resume, handle recurring questions, execute supported applications, and track results according to your rules.

> **One Profile, Multiple Workflows.**

## What ApplyBuddy helps with

- ✓ Discover jobs across configured sources
- ✓ Validate active postings and official application routes
- ✓ Check Hard Rules before applying
- ✓ Order suitable jobs using your preferences
- ✓ Route the right approved resume
- ✓ Reuse approved application answers
- ✓ Ask you instead of guessing consequential information
- ✓ Avoid duplicate applications
- ✓ Track application status, blockers, and follow-ups

## What you need to configure

Most users only need to work with two folders:

```text
config/     ← Your profile, job preferences, and approved answers
resumes/    ← Your approved resumes
```

The complete repository is the ApplyBuddy workspace. The remaining folders contain its workflows, shared rules, tracking schemas, and documentation and normally do not need manual editing.

## Why ApplyBuddy?

A typical auto-apply flow focuses on speed:

```text
Find job → Fill form → Submit
```

ApplyBuddy evaluates the opportunity before executing the application:

```text
Discover → Validate → Check Eligibility → Evaluate Fit
         → Select Resume → Apply → Verify → Track
```

**Eligibility comes before application execution.** A Preference—such as favoring healthcare roles—can affect processing order without rejecting every other role. A confirmed conflict with a Hard Rule—such as an explicit sponsorship incompatibility—may cause a job to be skipped according to your configuration.

## Ask instead of guessing

ApplyBuddy should not fabricate consequential candidate information. If work authorization, sponsorship, salary, employment, education, conflicts, legal attestations, demographic or sensitive information cannot be supported by your approved facts, the expected behavior is to ask you or stop for review.

## Choose your workflow

| Feature | ApplyBuddy | ApplyBuddy + Simplify |
|---|---|---|
| Job discovery | ✓ | ✓ |
| Eligibility screening | ✓ | ✓ |
| Resume routing | ✓ | ✓ |
| Approved answers | ✓ | ✓ |
| Form filling | Codex on supported pages | Simplify + Codex fallback |
| Verification | Codex/User | Codex/User |
| Tracking | ✓ | ✓ |
| Best for | Codex-native workflow | Faster repetitive autofill |

Both workflows use the same profile, preferences, approved answers, resumes, safety rules, and tracking workspace.

> **Configure once. Choose either workflow.**

## How it works

```text
Profile + Preferences + Approved Answers + Resumes
                       │
                       ▼
Discover → Validate → Eligibility → Fit → Select Resume
                       │
                       ▼
              Apply → Verify → Track
```

## Quick start

1. **Download ApplyBuddy** — download or clone the complete repository.
2. **Open it in Codex** — open the whole ApplyBuddy folder as your workspace.
3. **Start onboarding** — say:

   ```text
   Set up ApplyBuddy for me.
   ```

4. **Complete your configuration** — Codex guides you through `profile.yml`, `preferences.yml`, and `answers.yml` under `config/`.
5. **Add your resume** — put at least one approved resume in `resumes/`.
6. **Choose a workflow** — use `applybuddy` or `applybuddy-simplify`.
7. **Start searching**, for example:

   ```text
   Use ApplyBuddy to find Data Scientist jobs posted in the last 24 hours.
   ```

For detailed setup and optional Skill registration, see the [Setup Guide](docs/SETUP.md).

## Project structure

```text
ApplyBuddy/
├── config/       # Your profile, preferences, and approved answers
├── resumes/      # Your approved resumes
├── skills/       # ApplyBuddy and ApplyBuddy + Simplify workflows
├── references/   # Shared decision, application, and safety rules
├── tracking/     # Job and application tracking workspace
└── docs/         # Setup and workflow documentation
```

ApplyBuddy initializes and maintains live tracking files for discovered jobs, application attempts, blockers, follow-ups, and resume routing. Most users do not need to edit tracking CSVs manually.

## Documentation

- [Setup Guide](docs/SETUP.md)
- [How It Works](docs/HOW-IT-WORKS.md)
- [Workflow Comparison](docs/COMPARISON.md)
- [中文 README](README.zh-CN.md)
- [中文安装教程](docs/SETUP.zh-CN.md)
- [中文工作原理](docs/HOW-IT-WORKS.zh-CN.md)

## Current status

- Configuration architecture, Skill structure, shared references, and privacy defaults have been statically validated.
- Real-world ATS and browser behavior may vary and has not been comprehensively tested across every job platform.
- Simplify's interface and behavior may change; Codex must continue to verify its output.

## Safety and disclaimer

ApplyBuddy does not bypass CAPTCHA or human verification, guess credentials, or treat a Submit click as proof of receipt. Follow job-board terms, employer requirements, applicable laws, and platform automation policies. Review your configuration and completed applications whenever the context warrants it.

ApplyBuddy does not guarantee interviews, offers, application success, or support for every platform.

## License

ApplyBuddy is available under the [MIT License](LICENSE).
