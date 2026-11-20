<p align="center">
  <img src="assets/banner.png" width="100%" alt="testectomy: 13 tests cut down to 6, one per spec rule, with 2 hidden bugs found">
</p>

<p align="center">One agent skill for tests: it stops low-value tests at write time, cuts an existing suite down to the tests that matter, and moves the rest of the intent into Markdown specs.</p>

<p align="center">
  <a href="https://github.com/felipebasurto/testectomy/actions/workflows/test.yml"><img src="https://github.com/felipebasurto/testectomy/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/format-Agent%20Skills-555" alt="Agent Skills format"></a>
</p>

Most tests in an agent-written repo are a second copy of the logic: they assert constants, mock the helpers the code calls, compute the expected value with the function under test, and stay green when the real bug ships. They also cost every agent run minutes and tokens.

Deleting all of them throws away the part that is not a copy: intent. "The total is never negative" lives in a README or an issue, not in the code, and nothing in the code can check it. `testectomy` keeps that part and drops the rest.

- **Intent goes into `SPEC.md`.** One file per area, next to the code: numbered rules, example tables, non-goals, open questions. Written from the README, issues and you, never copied from the code.
- **Only tests a reader can't replace survive.** External boundaries, money and security, concurrency and time, parsers, real past regressions, public contracts. One test per rule, named with the rule ID, at the public boundary.
- **Disagreements become bugs, not green tests.** When the code contradicts clear intent, the test is written from intent and marked as an expected failure, and the report lists it as a bug.
- **Every kept test is bite-checked.** The agent breaks the code the rule describes and confirms the test fails on an assertion, then reverts.
- **Test-only production code goes too.** Exports, reset hooks, injection parameters and dead paths that only tests called are deleted with the tests that kept them alive.

## Quick start

```bash
npx skills add felipebasurto/testectomy -g
```

Then, in your agent:

```
/testectomy
/testectomy src/billing
```

With no argument it works on the whole repo, one area at a time. Codex uses `$testectomy`, the Claude Code plugin uses `/testectomy:testectomy`.

### Three modes

| Mode | When | What it does |
|---|---|---|
| **Gate** | Automatically, whenever the agent writes, changes or reviews a test | Asks which rule the test guards, what regression makes it fail and why existing coverage misses it, and rejects it if it matches a junk pattern. Never deletes anything. |
| **Pass** | You run `/testectomy [path]` | Specs, a verdict for every test, deletions, gaps filled, bite checks, report |
| **Campaign** | You ask to prune a whole subsystem in a large repo | The pass split into lanes, with a written ledger per chunk of tests, a layer plan, and an independent review that hunts for contracts that lost their only proof ([`CAMPAIGN.md`](skills/testectomy/CAMPAIGN.md)) |

The gate loads on its own. Deleting tests only happens when you ask for a pass or a campaign.

[![How testectomy works in four steps: write down the intent in SPEC.md, keep only tests a reader can't replace, turn code-vs-intent disagreements into known bugs, and prove every kept test can fail](assets/demo.gif)](assets/testectomy.mp4)

[Watch it with sound](assets/testectomy.mp4).

## For agents

If a user sent you this repo and said "use this":

1. **Install the skill**, unless `testectomy` is already in your skills folder: `npx skills add felipebasurto/testectomy -g` (drop `-g` for the current project only).
2. **Pick the scope.** The path the user named, or the whole repo. On large repos, do one area per pass.
3. **Run the skill.** Invoke `testectomy`, or open [`skills/testectomy/SKILL.md`](skills/testectomy/SKILL.md) and follow its nine steps by hand: baseline, inventory, intent, specs, classify, apply, bite-check, AGENTS.md, report.
4. **Don't commit** unless the user asked. End with the report the skill defines, including **Bugs** and **Open questions**: those need a human.

## How it works

Three layers, cheapest first:

| Layer | Holds | Checked by |
|---|---|---|
| `SPEC.md` | Rules, examples, non-goals, open questions | The agent, before and after every change |
| Types and schemas | Shapes, nullability, exhaustiveness | The compiler |
| Executable tests | Only rules that pass the keep bar | The test runner, filtered to the rules a change touches |

Every rule in a spec says how it's checked: `type`, `read` (the default) or `test`. A rule earns `test` only if at least one of these holds:

| Keep bar | Examples |
|---|---|
| 1. External boundary | Payment provider, third-party API, DB, file format, wire protocol |
| 2. Costly or irreversible failure | Money, auth, permissions, data deletion, migrations, privacy |
| 3. Hard to verify by reading | Concurrency, ordering, time zones, floating point, caching, retries |
| 4. Large input space | Parsers, serializers, formatters, renderers, validators |
| 5. A regression that actually happened | Linked issue or incident, plausible to come back |
| 6. Public contract | Library API, CLI output, plugin SDK, config format |

Each existing test then gets one verdict:

| Verdict | When |
|---|---|
| **Keep** | Guards a `test` rule at its public boundary. Renamed with the rule ID. |
| **Fix** | Guards a rule, but an assertion can't fail, or the test passes only by sleeping, retrying or a raised timeout. Repaired and bite-checked. |
| **Convert** | Guards a `test` rule through field-by-field asserts, mocks or private calls, or duplicates a stronger suite. Rewritten as one [expect test](skills/testectomy/expect-tests.md) or merged into the keeper. |
| **Fold** | A good input/output example for a `read` rule. Moved into the spec's table, then deleted. |
| **Delete** | Matches a junk pattern and guards no keep-bar rule. Needs one evidence line: what it could detect, and what proof remains. |

Junk is sorted by what the test depends on, because a test worth keeping depends only on intended behavior:

| Depends on | Example |
|---|---|
| **The past** | A removed feature, flag or old path asserted to stay gone. Agents add these when asked to remove something. |
| **Nothing** | No assertion, a mock of the unit under test, what the type system or the framework already guarantees. |
| **The implementation** | Expected value computed by the code under test, restated constants, layout numbers, debug seeds, private call order. |
| **Another test** | The same contract replayed at another layer with no new failure mode. |

Tests that pass by hiding a flake (fixed sleeps, polling to a deadline, retries, raised timeouts, real network calls) guard real behavior, so they get FIX: await the real signal, control the clock, and fake the network so unexpected requests fail. Tests disabled on every run are fixed and re-enabled, or deleted.

When unsure between keep and delete, it keeps the test and says why. Deletion count is not the goal.

### What a spec looks like

```markdown
### PRICE-3: A coupon worth more than the subtotal makes the order free
The total is 0, never negative.
Check: test (keep bar 2: money). Test: `tests/test_pricing.py › test_PRICE_3_…`
Source: README#pricing

| Subtotal | Coupon | Total |
|----------|--------|-------|
| 1000     | 5000   | 0     |
| 6000     | 7000   | 0     |
```

Rule IDs are stable, rule text never names internal functions (a rename can't make a spec stale), and open questions are resolved by a person, never by reading the code. Full format: [`spec-format.md`](skills/testectomy/spec-format.md).

### What it writes into AGENTS.md

So the next agent works the same way (abbreviated):

```markdown
## Tests and specs

- Each area's intent lives in its `SPEC.md`. Read it before changing that area.
- After a change, check every rule your diff touches. Run only the tests that
  cite those rule IDs (`pytest -k PRICE_3`).
- A new test needs a `Check: test` rule that meets the keep bar.
- A bug-fix regression test must fail on the code before the fix.
- Removing or moving code needs no test that it's gone.
- No sleeps, retries or raised timeouts in tests.
- Behavior changes start in the spec: update the rule, then the code.
- If code and spec disagree, stop and ask. Don't edit the spec to match the code.
```

## Example

[`examples/tinyshop`](examples/tinyshop) is a small checkout library with a README and 13 green tests. [`before`](examples/tinyshop/before) is the input. [`after`](examples/tinyshop/after) is the unedited output of one `/testectomy` run by an agent that had never seen the repo.

| | Before | After |
|---|---|---|
| Tests | 13, all passing | 6: 4 passing, 2 expected failures |
| Bugs found | 0 | 2 |
| Specs | none | [`tinyshop/SPEC.md`](examples/tinyshop/after/tinyshop/SPEC.md), 8 rules, 10 open questions |

The green suite was hiding two bugs:

- `test_total_big_coupon` asserted a total of **−3501**. The README says a coupon larger than the subtotal makes the order free, "never negative". The test now asserts 0 and is marked `xfail(strict=True)` until someone fixes the code.
- "Never charge twice for the same order id" held for sequential calls but not concurrent ones: two threads both reached the provider. Nothing tested it before.

<details>
<summary>The report, shortened</summary>

```markdown
Before → after: 13 tests → 6 tests (2 expected-failure)
Bugs (2):
- PRICE-3: coupon > subtotal returns -3501, README says 0. xfail strict.
- PAY-3: two concurrent charge() calls for one order both hit the provider. xfail strict.
Converted (4): retries test now uses a scripted fake provider instead of Mock; shipping
  threshold widened to a 5-row table including "coupon doesn't remove free shipping"
Gaps filled (2): PAY-2 never charged twice, PAY-3 concurrent
Bite check: 12 mutations, all failed on an assertion and were reverted
Deleted (8): restated constants (2), private helpers (3), mock wiring (1),
  expected value computed by the code under test (1), language trivia (1)
Open questions: coupon equal to subtotal, 0 or 499? Is the provider idempotent
  on retries? Dedupe lives in process memory only, is that enough? …
```

</details>

<details>
<summary>One converted test</summary>

```diff
-def test_retries_then_fails():
-    provider = mock.Mock()
-    provider.charge.side_effect = payments.ProviderTimeout()
-    with pytest.raises(payments.PaymentFailed):
-        payments.charge(provider, "o2", 100)
-    assert provider.charge.call_count == 3
+def test_PAY_1_timeouts_retry_twice_then_payment_failed():
+    attempt = ("<order>", 1299)
+    assert [_outcome(timeouts) for timeouts in (0, 2, 3)] == [
+        ("receipt-<order>", [attempt]),
+        ("receipt-<order>", [attempt] * 3),
+        ("PaymentFailed", [attempt] * 3),
+    ]
```

One table covers success, success after retries and failure, against a fake that behaves like the provider instead of a mock that replays the code's assumptions.

</details>

## Install

With the [skills CLI](https://github.com/vercel-labs/skills), for Claude Code, Cursor, Codex, Gemini CLI, OpenCode and other agents:

```bash
npx skills add felipebasurto/testectomy -g
```

As a Claude Code plugin:

```bash
claude plugin marketplace add felipebasurto/testectomy
claude plugin install testectomy@testectomy
```

As a Gemini CLI extension:

```bash
gemini extensions install https://github.com/felipebasurto/testectomy
```

By hand:

```bash
git clone https://github.com/felipebasurto/testectomy
cp -R testectomy/skills/testectomy ~/.claude/skills/   # or ~/.cursor/skills/, ~/.codex/skills/
```

| Agent | Invoke with |
|---|---|
| Claude Code | `/testectomy` (plugin: `/testectomy:testectomy`) |
| Cursor | `/testectomy` |
| Codex | `$testectomy` |
| Gemini CLI | "use the testectomy skill" |
| Any other agent | "Follow `skills/testectomy/SKILL.md` on this repo" |

## Any stack

The skill ships no scripts and no file patterns. Tests can be in any language, any folder, with any name, so the agent running the skill finds them the way a new engineer would: the test runner's config, the CI job, the build files that declare test targets, and the runner's own listing command. It writes down what it found and how, then works from that.

## Credits

The idea comes from a November 2026 thread: [Luke Parker](https://x.com/LukeParkerDev) deleted every test in his repo and banned them in AGENTS.md, [Lauren Tan](https://x.com/poteto) replied that she likes expect tests, and the replies pointed out what pure deletion loses: nobody can check the invariants anymore, and refactors lose their safety net. `testectomy` is the middle path.

- The gate, the retention rules and campaign mode are adapted from the [`test-audit`](https://github.com/openclaw/openclaw/blob/main/.agents/skills/test-audit/SKILL.md) skill in [OpenClaw](https://github.com/openclaw/openclaw).
- The "what does this test depend on" framing and the done checklist are adapted from [prune-tests](https://github.com/caldoai/skills/blob/main/skills/prune-tests/SKILL.md) by Caldo, and the git co-change signal from its sibling [untangle-codebase](https://github.com/caldoai/skills/blob/main/skills/untangle-codebase/SKILL.md).
- The flake patterns, their replacements and the shrink-only ratchet come from [landmines](https://github.com/interfere-inc/landmines) by Interfere.
- Expect tests follow Jane Street's [`ppx_expect`](https://github.com/janestreet/ppx_expect). Markdown specs follow the line of [Gauge](https://gauge.org), [Cucumber](https://cucumber.io), [specdown](https://github.com/corca-ai/specdown) and [bddfirst](https://github.com/c-k-x/bddfirst), without requiring any of them.

OpenClaw and Caldo are MIT; their notices are in [LICENSE](LICENSE).

## Pairs well with

[landmines](https://github.com/interfere-inc/landmines) enforces part of the gate in TypeScript as Oxlint rules: no test doubles, no fixed sleeps, no retries or raised timeouts, strict network mocking, with per-file allowances that only shrink.

[unslop-ui](https://github.com/felipebasurto/unslop-ui) does the same subtractive pass for interface copy and charts.

## License

[MIT](LICENSE)
