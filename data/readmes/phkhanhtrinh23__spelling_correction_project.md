# Spelling Correction


## About The Project


### Introduction

My project is called **Spelling Correction**. This is a solution which helps a person correct a sentence with spelling mistakes. This repository contains 2 versions of my soluion. The first one is successfully built (from scratch) with Transformer architecture. Besides, the second one is fine-tuned with GPT-2. `spelling_correction_v2` has now been fine-tuned and evaluated (see [Fixes and Experiment Results](#fixes-and-experiment-results) below).

## Getting Started

To get started, you should have prior knowledge on **Python** and **Pytorch** at first. A few resources to get you started if this is your first Python or Tensorflow project:

- [Pytorch Tutorials](https://pytorch.org/tutorials/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)


## Installation and Run
1. Clone the repo

   ```sh
   git clone https://github.com/phkhanhtrinh23/spelling_correction_project.git
   ```
  
2. Use any code editor to open the folder **spelling_correction_project**. With `python=3.8`, run `pip install -r requirements.txt` in your corresponding conda venv.

### Version 1
3. Download the [weights](https://drive.google.com/drive/folders/19r7GYrIvAVtZWhJ_mDchJWWnbLMCvXZi?usp=sharing) into `spelling_correction_v1`.

4. Download the data [`english.txt`](https://drive.google.com/file/d/1uVAKtFW5OXJMO1clhF_vDZYVwWa_FDTL/view?usp=sharing) into the `data/` folder in `spelling_correction_v1`. The correct path is `data/english.txt`.

5. Run `python train.py` to train the model using Transformer architecture.

6. Run `python api.py` to run the Front-end + Back-end Web Demo for this application. Share your results with me!

### Version 2
3. Download the data [`english.txt`](https://drive.google.com/file/d/1uVAKtFW5OXJMO1clhF_vDZYVwWa_FDTL/view?usp=sharing) into the `data/` folder in `spelling_correction_v1`. The correct path is `data/english.txt`.

4. Run `python train.py` to train the model using GPT-2.

5. The log is saved in `logs/` folder.

6. If the training is finised, you can run `python evaluate.py` to evaluate the results. Again, share your results with me if possible!


## Outline

- Input: [`english.txt`](http://www.manythings.org/anki/) a English Dictionary.

- Output:
   - `spelling_correction_v1` is based on **Transformer Encoder-Decoder** model. It is fast in training and inference.
   - `spelling_correction_v2` is based on **GPT-2** from [huggingface.co](https://huggingface.co/gpt2-medium).

## Results
- This is the result from the successfully built `spelling_correction_v1`.

<img src="./spelling_correction_v1/images/output.png"/>

- Link to the [YouTube demonstration](https://youtu.be/J-JnNqeN9zU).


## Fixes and Experiment Results

`spelling_correction_v2` generated nonsense words and repeated characters/words after training. Three bugs in `spelling_correction_v2/evaluate.py` caused this:

1. **Missing BOS token at inference.** Training formats each example as `<bos>corrupted[SEP]target<eos>` (see `collator.py`), but `evaluate.py` tokenized only `corrupted[SEP]`, with no leading `<bos>`. The model was fed an input format it never saw during training.
2. **Right-padding during batched generation.** `GPT2Tokenizer` right-pads by default. For a decoder-only model, batched `generate()` with right-padding is a well-known cause of garbled/repeated output, since shorter sequences in the batch continue generating after a run of pad tokens instead of right after the real prompt. Fixed with `tokenizer.padding_side = 'left'`.
3. **`max_length` instead of `max_new_tokens` in `generate()`.** `max_length` caps the *total* sequence length (prompt + generated tokens), but the input was already padded to exactly `args.max_length` tokens — leaving room for only **one** new token, no matter how well-trained the model was. This surfaced only after fixing (1) and (2): the model stopped producing garbage but still couldn't emit a real correction. Fixed by switching to `max_new_tokens`.

Also fixed to actually run the training/evaluation scripts on a single-GPU machine: `CUDA_VISIBLE_DEVICES` was hardcoded to `"1"` in `train.py`, `evaluate.py`, and `train.sh`, which crashes on a machine with only one GPU (index `0`).

### Training run

- Data: 151,086 English sentences (Tatoeba-style), 200 sentences held out for evaluation (never seen during training).
- Model: `gpt2-medium`, batch size 128, `max_length=32`, `lr=5e-4`, misspelling threshold `0.95`.
- Stopped after 4/20 epochs. Training loss: `0.976 → 0.060 → 0.045 → 0.041` — it leveled off quickly rather than continuing to drop, which is a good sign against overfitting/memorization on this small a number of epochs.

### Evaluation on 200 held-out sentences

**Exact match: 172/200 = 86.0%**

The corrupted sentences below (`IN`) are the model's input; `OUT` is the model's correction; `REF` is the ground-truth original sentence.

#### Correct corrections (sample)

| IN (corrupted) | OUT (model correction) |
|---|---|
| Tom went skiing aljone | Tom went skiing alone |
| I don't want tq tive my life in fear | I don't want to live my life in fear |
| I hate women who say that all mee are the same | I hate women who say that all men are the same |
| I want you to unrderstand this isn't going to be easy | I want you to understand this isn't going to be easy |
| Where can the kids lpay | Where can the kids play |
| It's been nice meeting yu | It's been nice meeting you |
| After a few minutes I began ro lose inteest in uhe covnersation | After a few minutes I began to lose interest in the conversation |
| Dn't be so shy | Don't be so shy |

#### Incorrect corrections (all 28 mismatches out of 200)

| IN (corrupted) | OUT (model correction) | REF (ground truth) |
|---|---|---|
| You didn't need td hurry You got here to earloy aynway | You didn't need to hurry You got here to arrive by noon | You didn't need to hurry You got here too early anyway |
| Yoru can easily rind the bnak | You can easily find the book | You can easily find the bank |
| The path is driect | The path is deep | The path is direct |
| Tom doesn't evln let hs daughter go out ot weekends | Tom doesn't even let his daughter go out on Fridays | Tom doesn't even let his daughter go out on weekends |
| The drug smugglr was arrested at the airprot | The drug ring was arrested at the airport | The drug smuggler was arrested at the airport |
| He promised me to come eraln | He promised me to come earlier | He promised me to come early |
| I ave never heard him le | I have never heard him laugh | I have never heard him lie |
| Tom isn't going o be happy to mee me | Tom isn't going to be happy to meet me | Tom isn't going to be happy to see me |
| I can get to work fastdr by walkign than by taking the car | I can get to work faster by walking than taking the car | I can get to work faster by walking than by taking the car |
| Be areful hTis knife is really sharp | Be careful with this knife | Be careful This knife is really sharp |
| Tom htes his lie | Tom has his lie | Tom hates his life |
| gay in ando day ouat h does nothing but tqend his sheep | Buy in two days what he does nothing but feed his sheep | Day in and day out he does nothing but tend his sheep |
| The atress said that she was engaged to a banker | The press said that she was engaged to a banker | The actress said that she was engaged to a banker |
| Nothing wlwl stop his gotng | Nothing will stop him | Nothing will stop his going |
| A nephew is a son of one's brotcera or sister | An nephew is a son of one's brother or sister | A nephew is a son of one's brother or sister |
| It har hapeened befoer anud it will probably hapen again | It has been been rumored that it will happen again | It has happened before and it will probably happen again |
| p nefd to shkve | I need to shkve | I need to shave |
| I have lot my friends | I have lots my friends | I have lost my friends |
| Stop bevlng so nce to me | Stop bothering so nice to me | Stop being so nice to me |
| I found the earring that you lost | I found the earrings that you lost | I found the earring that you lost |
| Pouulation growth has given rise to sejious socioal pfoblems | Pouling growth has given rise to serious social problems | Population growth has given rise to serious social problems |
| hy arragntd a meeting | They arrived a meeting | They arranged a meeting |
| I'll give him a buz | I'll give him a box | I'll give him a buzz |
| I interpreted mhat he asid in French into Japanmese | I interpreted that he said in French into Japanese | I interpreted what he said in French into Japanese |
| f think Tom needs to be told swt to do that | I think Tom needs to be told how to do that | I think Tom needs to be told not to do that |
| Miraaulousny nobody was setiously injurd | Murderously nobody was setiously injured | Miraculously nobody was seriously injured |
| ay I ezat ahis braed | May I eat this baked | May I eat this bread |
| I said stay bcak | I said staying back | I said stay back |

Note that even the mismatches are fluent, grammatical English — the model corrects the spelling but occasionally guesses a different (wrong) word when the corruption destroyed too much of the original signal (e.g. `driect` → "deep" instead of "direct"; `bnak` → "book" instead of "bank"). None of the original symptoms (nonsense words, repeated characters) are present.

Since training was stopped early at 4/20 epochs, further training may improve accuracy beyond 86%.


## Contribution

Contributions are what make GitHub such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the project
2. Create your Contribute branch: `git checkout -b contribute/Contribute`
3. Commit your changes: `git commit -m 'add your messages'`
4. Push to the branch: `git push origin contribute/Contribute`
5. Open a pull request


## Contact

Email: phkhanhtrinh23@gmail.com