# VNOnDB_extractor
Converts VNOnDB InkML files to PNG images and ground-truth text.

## Dataset access
Request access to the original TUAT Nakagawa Lab. HANDS-VNOnDB dataset through the [official Zenodo record](https://zenodo.org/records/23864366). Follow the application instructions and obtain approval from TUAT before downloading or using the data, then run this extractor on your authorized local copy.

Under TUAT's Version 2.0 Conditions of Use, access is for authorized non-commercial research and education. The database and derived data, including converted images, must not be redistributed. Commercial use requires a separate agreement with TUAT. See the official record for the full terms.

The [MIT license](LICENSE) applies to this extractor's code only. HANDS-VNOnDB and data derived from it are subject to TUAT's separate Conditions of Use.

## What is VNOnDB?
HANDS-VNOnDB (VNOnDB in short) provides 1,146 Vietnamese paragraphs of handwritten text composed of 7,296 lines, more than 480,000 strokes and more than 380,000 characters written by 200 Vietnamese. Writers were asked to write freely ground-truth text from a corpus of Vietnamese text. Our ground-truth text is derived from the VieTreeBank corpus, which contains all of the Vietnamese characters and some special symbols since it bases on Vietnamese newspapers. 

More at: [ICFHR2018-VOHTR-VNOnDB](https://sites.google.com/view/icfhr2018-vohtr-vnondb/database-tools?authuser=0)

## Usage:
After obtaining authorized access, place the original InkML files for each requested subset directly in `InkData_word/`, `InkData_line/`, or `InkData_paragraph/` in the repository root. Run the corresponding script(s) from the repository root to convert your local copy:

```bash
pip install -r requirements.txt
python InkData_word.py
python InkData_line.py
python InkData_paragraph.py
```
All data after extracting will be stored in `InkData_word_processed`, `InkData_line_processed` and `InkData_paragraph_processed` folder. Sample output:
<p align="center"> 
<img src="example.png">
</p>
