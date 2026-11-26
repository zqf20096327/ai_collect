<h1><a href="https://eblan.basaltlabs.org">EBLAN</a> - the chat bot trained on CS2 chats</h1>

[Chat with it](https://eblan.basaltlabs.org/chat/) | [Benchmark](https://eblan.basaltlabs.org/benchmark/) | [Privacy Policy](https://eblan.basaltlabs.org/privacy/) | [Terms of Service](https://eblan.basaltlabs.org/terms/) | [License](LICENSE.md) | [YouTube](https://www.youtube.com/@FaceDevStuff)

## About

EBLAN is a small language model trained on Counter-Strike 2 match chat. It's a LoRA on Qwen3.5-4B-Base, refined to be as toxic as possible through multiple rounds of post-training.

You can talk to it on the website, for a limited time, by text or by voice. It's made for entertainment only, and it's 18+ due to the nature of the content.

> [!WARNING]
> This repository contains real insults posted online, and the replies EBLAN is trained to give are deliberately vile. Slurs, sexual content and threats appear uncensored in the data, the prompts and the word lists.

## Why make this?

CS2 is infamously toxic. I wanted to see what happens when you train a model on it and then push it as far as it goes, and how it stacks up against GPT-4chan, an older model trained on 4chan. EBLAN is a joke about that.

Some of the code mentions slurs. A few things:

- Slur spam is the lazy version of toxic. Left alone, the model collapsed into putting the same slur in almost every reply, which made it repetitive, robotic and bad at actually answering the user. The training caps how often any one of them can show up, so the model has to come up with real comebacks instead.
- The chat is 18+ only and filters its replies unless you turn that off. The benchmark page is censored by default and leaves out the worst replies entirely. The model inference will be available for a limited time, and it's only there to demonstrate the outcome.
- The model weights, and the training data, are not published.

None of the model's output reflects my views. It's trained on game chat, to be as obnoxious as possible.

## What's in here

- [`benchmark/`](benchmark) is the toxicity benchmark - 450 insults, the prompts, and a script that runs a model through them and has LLM judges grade the replies.
- [`training/`](training) is the training pipeline (roughly)

The model weights and the chat dataset aren't included

## License

The code is under the [MIT License](LICENSE.md). The insults in `benchmark/insults.jsonl` come from other sources and have their own terms, explained in [`benchmark/DATA.md`](benchmark/DATA.md).
