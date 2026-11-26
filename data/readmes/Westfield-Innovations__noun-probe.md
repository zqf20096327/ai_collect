# noun-probe

The Noun Probe finds the words in a document that are doing more than one job. This package is its reader.

Created by Carl D. Hildebrandt · Westfield Innovations LLC

Official Noun Probe: https://azus.ai/tools/noun-probe/

The words of the Noun Probe live only at that address. People read them there. Programs read them there through this reader, which holds none of the words.

## Install

```
pip install noun-probe
```

It needs nothing beyond Python 3.11 or later.

## Use

```python
import noun_probe

def my_ai(text):
    # Send `text` to the AI you already use and return its answer.
    ...

report = noun_probe.run(
    document="...the text you want examined...",
    mode="AUDIT",  # or VISION
    boundary="...what is being examined, and what is not...",
    ask=my_ai,
)
```

The report comes back with the four credit lines at its end. `noun_probe.prompt(...)` gives the same text without calling your AI, and `noun_probe.read(edition=3)` fixes a program to one numbered edition, whose words never change.

To see exactly what the reader reads:

```
noun-probe            # or: python -m noun_probe
```

## What the reader does and never does

It makes one read-only request to the official address (two when fixed to an edition: the edition and the current title block), puts the words together with your document for your own AI, and puts the credit lines at the end of every report. It holds one reading in memory for five minutes.

It never holds the words, never sends your document, account or any identifier, never writes to disk, and never contacts any address except the official one. A proxy set for your system (`HTTPS_PROXY`) is used as usual. If the address cannot be read, it stops and runs nothing.

## Terms

Use of the Noun Probe, through this reader or the page, is governed by the terms published at https://azus.ai/tools/noun-probe/
