# Pixel Character Generator

Generating 64×64 retro pixel game characters with generative adversarial networks (GANs) and autoencoders. The repository includes **TinyHero**, a dataset of 3648 pixel characters seen from four angles, and Jupyter notebooks that build the dataset and train four models: a DCGAN, a conditional DCGAN that generates a character from a chosen angle, a convolutional autoencoder, and a GAN combined with an autoencoder.

> **Note:** this is a project from 2020. In 2026 it got small updates only: new figures, a clearer README, a `requirements.txt`, and fixes for a few bugs in the notebooks. The dataset and the models are unchanged.

 ![](images/58.png)  ![](images/58_2.png)  ![](images/58_3.png)  ![](images/58_4.png)
 ![](images/212.png)  ![](images/212_2.png)  ![](images/212_3.png)  ![](images/212_4.png)
 ![](images/584.png)  ![](images/584_2.png)  ![](images/584_3.png)  ![](images/584_4.png)

 ![](images/111.png)  ![](images/111_2.png)  ![](images/111_3.png)  ![](images/111_4.png)
 ![](images/585.png)  ![](images/585_2.png)  ![](images/585_3.png)  ![](images/585_4.png)
 ![](images/586.png)  ![](images/586_2.png)  ![](images/586_3.png)  ![](images/586_4.png)

## Table of Contents

- [Dataset TinyHero](#dataset-tinyhero)
- [Models](#models)
  - [DCGAN](#dcgan)
  - [Conditional DCGAN](#conditional-dcgan)
  - [DC Autoencoder](#dc-autoencoder)
  - [GAN + autoencoder](#gan--autoencoder)
- [Running the notebooks](#running-the-notebooks)
- [Repository structure](#repository-structure)
- [License](#license)

## Dataset TinyHero

![Random characters from TinyHero](images/random_chars.png)

TinyHero contains 64×64 retro pixel characters. All characters were made with the [Universal LPC spritesheet by makrohn](https://github.com/makrohn/Universal-LPC-spritesheet/tree/7040e2fe85d2cb1e8154ec5fce382589d369bdb8). Each character has a random sex, body type, skin colour and equipment, and is shown from 4 angles.

![How the TinyHero dataset was made](images/tinyhero-pipeline.svg)

| Image size | Dataset size | Source | Download |
|------------|--------------|--------|----------|
| 64×64 | 3648 images (912 per class) | [LPC Spritesheet](https://github.com/makrohn/Universal-LPC-spritesheet/tree/7040e2fe85d2cb1e8154ec5fce382589d369bdb8) | [data.zip](data.zip) |

The images are in `data.zip`, in one folder per view angle:

| Folder | View |
|--------|------|
| `data/0/` | back |
| `data/1/` | left |
| `data/2/` | front |
| `data/3/` | right |

The same character has the same file name in all four folders. For example, `data/0/58.png` and `data/2/58.png` show one character from the back and from the front.

The dataset was built with two notebooks:

1. [`1_download_random_spritesheet.ipynb`](notebooks/1_download_random_spritesheet.ipynb) opens the online LPC character generator in Chrome with Selenium, picks a random sex, body, hair and 7 to 20 pieces of equipment, and saves the spritesheet.
2. [`2_extract_character.ipynb`](notebooks/2_extract_character.ipynb) cuts one 64×64 frame from each of the four direction rows of every spritesheet and saves it into the folder for that view.

 ![](images/587.png)  ![](images/587_2.png)  ![](images/587_3.png)  ![](images/587_4.png)
 ![](images/588.png)  ![](images/588_2.png)  ![](images/588_3.png)  ![](images/588_4.png)

## Models

![The four models in the notebooks](images/models.svg)

All models use the convolutional generator and discriminator from the [PyTorch DCGAN tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html), with changes listed below. All of them train on 64×64 images normalised to the range -1 to 1.

### DCGAN

[Notebook 3: DCGAN](notebooks/3_DCGAN.ipynb) · [Open in Colab](https://colab.research.google.com/github/AgaMiko/pixel_character_generator/blob/master/notebooks/3_DCGAN.ipynb)

Changes compared to the tutorial:

* Tested different latent sizes (generator input) and feature map sizes. The final notebook uses a latent size of 84 and 48 feature maps.
* Soft and noisy labels: real images get a random label between 0.95 and 1.05, fake images between 0 and 0.1. This makes the discriminator less sure of itself and keeps training more stable.
* Dropout (0.2) in the discriminator.
* Binary cross-entropy loss. A Wasserstein loss function is defined in the notebook as an option for [mode collapse](https://machinelearningmastery.com/practical-guide-to-gan-failure-modes/) ([about Wasserstein loss](https://developers.google.com/machine-learning/gan/loss)), but the training loop does not use it.

Training: 30 epochs, batch size 64, Adam with learning rate 2e-4.

#### Example results

![Real and generated characters](images/real_fake.png)

### Conditional DCGAN

[Notebook 4: Conditional DCGAN](notebooks/4_Conditional_DCGAN.ipynb) · [Open in Colab](https://colab.research.google.com/github/AgaMiko/pixel_character_generator/blob/master/notebooks/4_Conditional_DCGAN.ipynb)

A conditional DCGAN that generates a character seen from a chosen angle (back, left, front or right).

* The generator gets the angle from a trainable lookup table (embedding), which turns the angle number into 10 values. These are joined with the 40-value random input.
* The discriminator has two outputs: real or fake, and which of the 4 angles the image shows. The angle loss is computed on real images and added to the discriminator loss with weight 0.5.
* Different learning rates: 4e-4 for the discriminator and 1e-4 for the generator.
* Soft labels: real images get a random label between 0.8 and 1.1.
* Colour jitter on the training images (brightness, contrast, saturation and hue).

Training: 200 epochs, batch size 100.

![Generated and real characters for each angle](images/CGAN.PNG)

### DC Autoencoder

[Notebook 5: DC Autoencoder](notebooks/5_DC_Autoencoder.ipynb) · [Open in Colab](https://colab.research.google.com/github/AgaMiko/pixel_character_generator/blob/master/notebooks/5_DC_Autoencoder.ipynb)

A deep convolutional autoencoder with the same layers as the DCGAN above. The only difference is an extra fully connected layer at the end of the encoder, which turns the convolutional output into a code of the chosen size.

* A code of 40 values is enough for a good-quality reconstruction.
* The autoencoder removes noise well: it rebuilds clean characters from images with strong added noise.
* It is easier and more stable to train than a GAN.

Training: mean squared error loss, Adam with learning rate 1e-4, multiplied by 0.995 after each epoch.

![Autoencoder reconstructions](images/DCAE.png)

### GAN + autoencoder

[Notebook 6: GAN + autoencoder](notebooks/6_DCGAN_and_Autoencoder.ipynb) · [Open in Colab](https://colab.research.google.com/github/AgaMiko/pixel_character_generator/blob/master/notebooks/6_DCGAN_and_Autoencoder.ipynb)

This notebook trains the autoencoder and the conditional GAN separately. The GAN generates new characters, and the autoencoder then rebuilds them, which removes some of the GAN's noise and artifacts.

## Running the notebooks

The model notebooks (3 to 6) were written for Google Colab with a GPU:

1. Open a notebook with its **Open in Colab** link.
2. Run the upload cell and select `data.zip` from this repository. The next line unzips it into `data/`.
3. Run the remaining cells.

To run them locally instead:

```bash
pip install -r requirements.txt
cd notebooks
unzip ../data.zip
jupyter notebook
```

Then skip the `google.colab` upload cell in each notebook.

Notebook 1 also needs Google Chrome and a matching [chromedriver](https://developer.chrome.com/docs/chromedriver). Set `CHROME_DIR` and `DOWNLOAD_DIR` at the top of the notebook. You only need notebooks 1 and 2 to build a new dataset. TinyHero is already in `data.zip`.

## Repository structure

```
├── data.zip                                  # TinyHero dataset
├── notebooks/
│   ├── 1_download_random_spritesheet.ipynb   # downloads random LPC spritesheets
│   ├── 2_extract_character.ipynb             # cuts the 4 views from each spritesheet
│   ├── 3_DCGAN.ipynb
│   ├── 4_Conditional_DCGAN.ipynb
│   ├── 5_DC_Autoencoder.ipynb
│   └── 6_DCGAN_and_Autoencoder.ipynb
├── images/                                   # README images
├── requirements.txt
├── cc-by-sa-3.0.txt
└── gpl-3.0.txt
```

## License

Under the rules of the LPC, all art submissions are dual licensed under GNU GPL 3.0 and CC-BY-SA 3.0. The work in this repository is licensed under the same terms.

* CC-BY-SA 3.0: http://creativecommons.org/licenses/by-sa/3.0/ (see [cc-by-sa-3.0.txt](cc-by-sa-3.0.txt))
* GNU GPL 3.0: http://www.gnu.org/licenses/gpl-3.0.html (see [gpl-3.0.txt](gpl-3.0.txt))
