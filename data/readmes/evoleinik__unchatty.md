# unchatty

Make Claude Code write plainly. Then measure whether it worked.

A `CLAUDE.md` block that cuts reply length and kills the dense, dash-heavy style, plus
the harness I used to prove it does something. Answers to the same question dropped from
393 words to 62.

```bash
git clone https://github.com/evoleinik/unchatty && cd unchatty
# paste COMMUNICATION.md near the top of your CLAUDE.md, then:
export ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MD=~/.claude/CLAUDE.md ./ab-test.sh "Why does X work this way?"
```

Three files:

- `COMMUNICATION.md` — paste into your `CLAUDE.md`, near the top
- `score.py` — scores a reply mechanically (words, sentence length, dashes, headers)
- `ab-test.sh` — runs the same questions with the rules on and off, then scores both

## Results

Same repo, same questions, headless `claude -p` sessions, rules on vs rules off.

| Question | Control | With rules |
|---|---|---|
| "What's the rate limit?" | 33 words | 14 |
| "Which cron runner should we use?" | 292 words | 70 |
| "Why did we move the catalog into the DB?" | 316 words | 190 |
| "Why is graph review the only merge gate?" | 393 words | 62 |
| "How does the edge snapshot work?" | 365 words | 253 |

Across the three long questions:

| Metric | Control | With rules |
|---|---|---|
| Mid-sentence em-dashes per 100 words | 1.3 / 1.8 / 0.8 | 0.0 / 0.0 / 0.0 |
| Longest sentence | 43 / 40 / 47 words | 29 / 19 / 26 |
| Sentences over 25 words | 5 / 7 / 3 | 2 / 0 / 1 |
| Markdown headers | 2 / 0 / 5 | 0 / 0 / 0 |

## The part that surprised me

Version one of the rule made long answers *worse*. It banned em-dashes, and the long
answers came back at 2.2 per 100 words against a control of 1.3.

The cause was the source material. My own repo docs run 1.1 to 1.9 em-dashes per 100
words. Short answers come from memory, so they were already clean. Long answers get
built by reading those files, and they pick up the punctuation on the way in.

The fix was not "be plainer". It was this line:

> NEVER INHERIT THE PUNCTUATION OF WHAT YOU ARE READING. Your docs are dense on purpose.
> A reply is not a doc.

That took mid-sentence dashes to zero on every long question.

## Two honest caveats

The rules only reach interactive Claude Code sessions. Anything that calls a model
directly with its own prompts never sees `CLAUDE.md`, so check before you assume a
rule is global.

My first scorer over-counted. It glued bullet lists into one giant sentence, and it
counted `**Label** —` list separators as if they were mid-sentence splices. Those are
a different construct and they read fine. `score.py` here is the corrected version.

## Run it yourself

```bash
export ANTHROPIC_API_KEY=sk-ant-...
./ab-test.sh "Why does X work the way it does?" "How does Y get built?"
```

It backs up your `CLAUDE.md`, runs each question twice, restores the file, and prints
the scores. It restores on Ctrl-C too.
