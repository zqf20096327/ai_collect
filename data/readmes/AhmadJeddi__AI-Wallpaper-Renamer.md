# AI Wallpaper Renamer

A lightweight local tool that analyzes wallpaper images with **Qwen3.5-2B** and generates clean, descriptive filenames.

![AI Wallpaper Renamer Preview](preview.png)

## About

This project provides a simple local tool for organizing wallpaper filenames using a vision-language model.

The tool analyzes each image and combines visual information with the original filename when useful to create concise, human-readable filenames.

The AI naming process uses:

* **Qwen3.5-2B**
* **llama.cpp**

For example:

```text
Original:

192804-3840x2160-desktop-4k-tiger-background-photo.jpg

Renamed:

tiger-on-rock.jpg
```

The tool is included in:

```text
tools/rename_wallpapers.py
```

It can be used with any folder containing supported image files.

The repository includes a small set of sample wallpapers for testing and demonstration.

## How It Works

The renaming process follows a simple pipeline:

```text
Input image
    ↓
Extract useful words from the original filename
    ↓
Qwen3.5-2B analyzes the image
    ↓
Generate subject + suggested filename
    ↓
Validate and sanitize the filename
    ↓
Create a unique output name
    ↓
Copy the original image unchanged
```

The image is treated as the primary source of truth.
The original filename is used only as supporting context when it contains useful information.

The model returns a structured JSON response:

```json
{
  "subject": "tiger",
  "suggested_filename": "tiger-on-rock"
}
```

The Python script then validates the result, removes unwanted or technical terms, prevents duplicate words, and creates a safe filename.

## Requirements

* Python 3.10+
* llama.cpp with `llama-mtmd-cli`

### Windows

Install llama.cpp with:

```powershell
winget install --source winget ggml.llamacpp
```

The script automatically downloads the required **Qwen3.5-2B** model files when they are missing.

## Using the AI Naming Tool

The tool accepts an input folder and an output folder:

```bash
python tools/rename_wallpapers.py "path/to/input" "path/to/output"
```

It processes images one at a time, generates descriptive filenames, and copies the renamed files into the output directory without modifying the originals.

For each image, the script also performs basic input validation before running the VLM inference.

## Supported Images

```text
.jpg
.jpeg
.png
.bmp
```

## Repository Structure

```text
ai-wallpaper-renamer/
├── wallpapers/
├── tools/
│   └── rename_wallpapers.py
├── preview.html
├── preview.png
├── README.md
├── LICENSE
└── .gitignore
```

## Test & Preview Images

The sample images used for testing and `preview.png` were sourced from **Wikimedia Commons**. Their respective source pages and licensing information are listed below.

* [Cabourg Beach](https://commons.wikimedia.org/wiki/File:Cabourg,_Strand01.jpg) — Public Domain
* [Desert Panorama Landscape](https://commons.wikimedia.org/wiki/File:Desert_panorama_landscape.jpg) — Public Domain
* [Heaps Peak Arboretum in Autumn](https://commons.wikimedia.org/wiki/File:Heaps_Peak_Arboretum_in_Autumn_%2828021215917%29.jpg) — Public Domain
* [Kayak on a Mountain Lake](https://commons.wikimedia.org/wiki/File:Kayak_on_a_mountain_lake_%28Unsplash%29.jpg) — CC0
* [Landscape with Clouds](https://commons.wikimedia.org/wiki/File:Landscape_with_clouds.jpg) — CC0
* [Meadows Edge Picnic Area](https://commons.wikimedia.org/wiki/File:Meadows_Edge_Picnic_Area_%2841151609045%29.jpg) — Public Domain
* [Mountain Lake in Camera Lens](https://commons.wikimedia.org/wiki/File:Mountain_lake_in_camera_lens_%28Unsplash%29.jpg) — CC0
* [Mountain Landscape](https://commons.wikimedia.org/wiki/File:Mountain_Landscape_%28Unsplash%29.jpg) — CC0
* [Snow Landscape near Lake Meridian](https://commons.wikimedia.org/wiki/File:Snow_landscape_near_Lake_Meridian_%282025%29_-_0002.jpg) — CC0
* [Strawberry Peak](https://commons.wikimedia.org/wiki/File:Strawberry_Peak_%2842155558941%29.jpg) — Public Domain

The images remain subject to the licensing terms stated on their respective source pages.

## License

The source code is licensed under the [MIT License](./LICENSE).
