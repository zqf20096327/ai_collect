# dominantcolors

Gets the dominant colors from an image to use the most dominant one as background and the best candidate as foreground, adjusting its contrast if necessary.

It was created for the media player widget on my [AwesomeWM config](https://github.com/pablonoya/awesomewm-configuration).

![Popup](./screenshots/popup.webp)

## Installation

### Using uv

```shell
uv tool install git+https://github.com/pablonoya/dominantcolors
```

### Using pipx

```shell
pipx install git+https://github.com/pablonoya/dominantcolors.git
```

## Usage

Receives an image path as input and returns 2 hexadecimal colors.

```shell
$ dominantcolors [OPTIONS] /path/to/image

#f6f4f4
#4782b0
```

```
$ dominantcolors --help
Usage: dominantcolors [OPTIONS] IMAGE_PATH

  Extract dominant colors from IMAGE_PATH

Options:
  -c, --target-contrast FLOAT  Target contrast ratio  [default: 3.0]
  --help                       Show this message and exit.
```
