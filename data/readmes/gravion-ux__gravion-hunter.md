# gravion-hunter

**Autonomous bug bounty agent framework — built for validity ratio, not volume.**

Most autonomous hunting frameworks optimise for how much they can submit.
gravion-hunter optimises for how much of what it submits is *valid*. It hunts
inside a locked scope, forces every finding through a hard validation gate,
dedupes before it drafts, and puts a brake on autopilot the moment the
programme starts answering "N/A".

## How it differs

| | Typical agent frameworks | gravion-hunter |
|---|---|---|
| Agents | 50 loosely-defined roles | 8 sharp roles, one job each |
| Scope | A markdown file the agent is asked to respect | Parsed and **enforced by the driver** — out-of-scope rows cannot be created |
| Validation | A checklist in a prompt | A **state machine gate**: a finding cannot reach `reported` until all 7 gate questions are recorded as passed |
| Dedupe | A step you can skip | A required transition with a minimum of 3 recorded dedupe sources |
| Autopilot | Submits until stopped | Submits until the **validity brake** trips (N/A + duplicate ratio > 30% over ≥5 outcomes), then halts itself |
| Submission default | Autonomous | Operator approval by default; autopilot is an explicit, logged opt-in |

## The pipeline

```
queued → working → confirmed → gated → deduped → reported → submitted
              ↘ ruled_out            (one failed gate question → killed)
              ↘ open_proof_gap
```

Every lead closes in exactly one honest state — `confirmed`, `ruled_out`, or
`open_proof_gap`. Nothing is silently dropped, and nothing is silently
promoted either.

## The 7-Question Gate

1. Exploitable **right now**, step by step, as a real HTTP request?
2. Impact on the programme's **accepted** list?
3. Root cause in an **in-scope** asset?
4. No unrealistic privileged access required?
5. Not already known / accepted behaviour?
6. Impact **proven** beyond "technically possible"?
7. Not a known-invalid class without a chain?

One wrong answer kills the finding. This is the discipline that keeps a
researcher account's validity ratio — and the account itself — alive.

## Quick start

```bash
pip install -e .

cat > scope.md <<'EOF'
# Example Programme
## In scope
- example.com
- *.example.com
## Out of scope
- staging.example.com
EOF

hunt init   --scope scope.md --state campaign.json            # add --autopilot to opt in
hunt add    --state campaign.json --host app.example.com --class idor --endpoint /v1/orders/{id}
hunt start  --state campaign.json --row 1
hunt close  --state campaign.json --row 1 --outcome confirmed
hunt gate   --state campaign.json --row 1 --answers all
hunt dedupe --state campaign.json --row 1 --sources programme-disclosed,vendor-changelog,cve-db
hunt report --state campaign.json --row 1
hunt submit --state campaign.json --row 1 --approve           # or autopilot mode
hunt status --state campaign.json
```

## Layout

- `src/gravion_hunter/` — the driver: scope parser/enforcer + campaign state machine + CLI
- `agents/` — the 8 agent role cards
- `skills/` — workflow, triage gate, report writing, scope discipline
- `SKILL.md` — the master skill that ties the framework together
- `tests/` — the driver's behaviour, pinned

## Agents

| Agent | Job |
|---|---|
| hunt-orchestrator | Owns the board; serves one row at a time, depth-first |
| recon-ranker | Turns recon into ranked candidate rows (in-scope only) |
| web-hunter | Browser-rendered surface: XSS, SSRF, injection, logic |
| api-hunter | API surface: BOLA/IDOR, auth, mass assignment, rate limits |
| validator | Runs the 7-Question Gate; can kill any finding |
| chain-builder | Links confirmed findings into higher-impact chains |
| dedupe-checker | Owns the dedupe transition; nothing drafts before it clears |
| reporter | Impact-first reports; never writes "could potentially" |

## Responsible use

For authorised security testing only — bug bounty programmes whose scope you
have accepted, or systems you own or are contracted to test. The scope lock
exists so the framework physically cannot wander outside the programme you
pointed it at. Autopilot is a tool, not an excuse: the operator is
responsible for every submission the framework makes.

## License

MIT © Priyanshu Kumar Thakur
