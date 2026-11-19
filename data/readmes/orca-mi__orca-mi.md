<div align="center">

# 🐋 ORCA-MI

**Open Radiology & Computational Analysis · Molecular Imaging**

*Agile intelligence, deep insight*

PET · SPECT · CT · MR &nbsp;—&nbsp; viewing, fusion, 3D, AI segmentation, quantification, dosimetry, registration

<br>

[![Download for Windows](https://img.shields.io/badge/Download-Windows-1f6feb?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/orca-mi/orca-mi/releases/latest/download/ORCA-MI-setup.exe)
&nbsp;
[![Download for Ubuntu](https://img.shields.io/badge/Download-Ubuntu%20(test)-e95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/orca-mi/orca-mi/releases/download/v0.1.3/ORCA-MI-0.1.3-ubuntu.tar.gz)
&nbsp;
[![Open in the browser](https://img.shields.io/badge/Open-Web%20viewer-2ea44f?style=for-the-badge&logo=webassembly&logoColor=white)](https://orca-mi.github.io/orca-mi-web-limited/)
&nbsp;
[![Website](https://img.shields.io/badge/Website-orca--mi.github.io-24292f?style=for-the-badge&logo=googlechrome&logoColor=white)](https://orca-mi.github.io/)
&nbsp;
[![Video tutorials](https://img.shields.io/badge/Tutorials-YouTube-c4302b?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@ORCA-MI)

[![Latest version](https://img.shields.io/github/v/release/orca-mi/orca-mi?label=version&color=1f6feb)](https://github.com/orca-mi/orca-mi/releases/latest)
[![Free for research · not for clinical use](https://img.shields.io/badge/free%20for%20research-not%20for%20clinical%20use-d29922)](#licence-and-citation)

</div>

<br>

---

**Why ORCA?** Like the orca, ORCA-MI is **fast** (native code, GPU 3D, swift processing), **intelligent** (deep
learning segmentation and image-to-image AI) and gives **deep insight** beneath the surface of your images
(quantification, kinetics, dosimetry).

A fast medical image workstation in one Windows program. Open DICOM, NIfTI and other formats, segment by hand or
with AI, measure SUV / MTV / TLG, analyse dynamic and multi-time-point scans, plan doses, and send the results back
to the PACS as DICOM.

> **For research use only.** ORCA-MI is not a certified medical device (no CE marking, no FDA clearance) and must
> not be used for clinical decisions. ORCA-MI is an independent research project, not affiliated with, or endorsed
> by, any company or product named ORCA.

## ⬇ Download

| | **Installer** | **Portable** |
|---|---|---|
| File | [**ORCA-MI-setup.exe**](https://github.com/orca-mi/orca-mi/releases/latest/download/ORCA-MI-setup.exe) | [**ORCA-MI-portable.zip**](https://github.com/orca-mi/orca-mi/releases/latest/download/ORCA-MI-portable.zip) |
| Administrator rights | not needed (installs for the current user) | not needed |
| Where it runs | `%LOCALAPPDATA%\Programs\ORCA-MI` | anywhere: Desktop, USB stick, shared folder |
| Start menu / desktop shortcut | ✔ (desktop optional) | – |
| "Open with ORCA-MI" for .nii .nrrd .mha .mhd .dcm | optional | – |
| Uninstall | Windows *Apps* list | delete the folder |

Both contain the same program, always the latest version ([all versions](https://github.com/orca-mi/orca-mi/releases)).
Settings, models and AI environments are kept in your user profile, so switching between the two, or updating, keeps
everything. **Updating:** ORCA-MI tells you when a new version is out (if you allow notifications) and installs it
for you, or run the new installer over the old one (no need to uninstall). Also on [orca-mi.github.io](https://orca-mi.github.io).

**Linux (Ubuntu), test version:** [**ORCA-MI-0.1.3-ubuntu.tar.gz**](https://github.com/orca-mi/orca-mi/releases/download/v0.1.3/ORCA-MI-0.1.3-ubuntu.tar.gz). ORCA-MI is made for Windows; the
Linux version (still 0.1.3, from the [v0.1.3 release](https://github.com/orca-mi/orca-mi/releases/tag/v0.1.3)) is the same program, updated less often, without session recording, the system monitor and automatic
updates. Ubuntu 20.04 or newer (or another Linux with glibc 2.30+), 64-bit: unpack it and start `./orca-mi`
(`tar -xzf ORCA-MI-0.1.3-ubuntu.tar.gz`, `cd ORCA-MI-0.1.3-ubuntu`, `./orca-mi`); the included README-LINUX.txt
lists what to install if it does not start. The trial and the free licence work as on Windows (a licence is made for
one computer, so a Linux PC needs its own).

**ORCA-MI Web, in the browser:** [**https://orca-mi.github.io/orca-mi-web-limited/**](https://orca-mi.github.io/orca-mi-web-limited/). Nothing to install (Chrome, Edge or Firefox):
a limited version with the viewer (DICOM, NIfTI, PET/CT fusion, 3D MIP, save as NIfTI) and the NEMA IEC phantom
analysis. Your images are opened inside the browser and never uploaded.

**Requirements:** Windows 10 or 11, 64-bit. A GPU is used for the 3D view; the AI features run on an NVIDIA GPU
when one is available, otherwise on the CPU.

▶ **Video tutorials:** [youtube.com/@ORCA-MI](https://www.youtube.com/@ORCA-MI) — short videos, one feature each.

**Windows SmartScreen:** ORCA-MI is not yet code-signed, so Windows may show *"Windows protected your PC"* the first
time. Click **More info → Run anyway**.

## What it does

| | |
|---|---|
| **View** | DICOM (CT, MR, PET, SPECT, X-ray, US, enhanced multi-frame, compressed), RTSTRUCT, RTDOSE, DICOM SEG, NIfTI, NRRD, MHA/MHD, Analyze, NumPy, PNG/JPEG/TIFF · drag-and-drop layouts up to 5×5, MPR and two MPRs side by side · PET/CT and SPECT/CT fusion · 60+ colour maps (incl. 3D Slicer's PET tables) · GPU 3D (MIP, DVR, surfaces) · 4D cine · a searchable patient database for PACS-like folders |
| **Hanging protocols** | PET/CT, SPECT/CT, PET/MR, CT and PET screens arranged automatically after loading; save your own |
| **Segment** | segmentations shown and edited on every image (as in 3D Slicer) · brush, eraser, polygon, region growing, threshold, morphology, interpolation, undo · **nnInteractive** (click / box / scribble / lasso) · **nnU-Net** · iterative PET lesion segmentation (XEOS) · one-click **body contour** |
| **Measure** | SUVbw / SUL / SUVbsa · volume (MTV), SUVmean, SUVmax, **SUVpeak**, **TLG** per segment or lesion · Dice, HD95 and other overlap metrics |
| **Dynamic / multi-time-point** | motion correction · time-activity curves per segment · **Patlak Ki** and Ki maps · effective half-life and time-integrated activity for therapy SPECT |
| **Q.SPECT** | quantitative SPECT: counts → Bq/mL with your conversion factors per scanner, isotope and reconstruction, scaled to the acquisition time (per projection or total, e.g. StarGuide); your scanner library is kept across updates and exported as JSON |
| **NEMA IEC phantom** | contrast recovery (mean / max / peak), NEMA QH, background variability, PDF and Excel reports; ROIs exchanged with ORCA-MI segmentations |
| **Scanner calibration & QC** | PET and SPECT calibration from a uniform phantom (SPECT factor to Q.SPECT, PET measured / true) · history of every scanner: calibration and NEMA IEC records compared with the previous and a reference record, your own ± % tolerances, EARL1 / EARL2 bands for FDG PET, trend charts, JSON export / import, Excel report |
| **Batch DICOM → NIfTI** | whole folder trees, Excel tables of the DICOM headers, PET in SUV, gantry-tilt and slice-spacing correction, file renaming, optional dcm2niix |
| **Decay & values** | decay correction of images and an activity calculator (Bq … Ci, common PET / SPECT / therapy nuclides) · data type conversion, clipping, normalisation, exact percentiles |
| **CT dose** | per-slice tube current, mAs, CTDIvol, water-equivalent diameter, SSDE, density / μ-maps |
| **Compare** | bias maps, ME / MAE / RMSE / SSIM / PSNR per region, gamma index, noise power spectrum |
| **Lesion tracking** | lesions of two time points linked one by one, per-lesion diameter / volume / SUVmax / SUVpeak / TLG, RECIST 1.1, PERCIST 1.0, TMTV |
| **Cardiac** | short-axis reorientation, 17-segment LV model, bull's-eye |
| **Dosimetry** | SIRT Y-90 local deposition, DVH and DVH constraints, isodose lines, dose colour wash |
| **Register** | manual, centre of mass, rigid / affine (MI, NCC, MSE) with masks or a focus sphere, deformable Demons |
| **Export** | **DICOM for the PACS: image series, SEG, RTSTRUCT and measurement SR** with anonymisation · NIfTI · figures, 3D rotation and cine GIFs · CSV / Excel report folders |
| **Safety net** | autosave every 2 minutes and crash recovery · workspaces |
| **AI** | one-click private Python + PyTorch installer, model library, train your own nnU-Net, fine-tune nnInteractive |
| **Reader studies** | blinded, randomised scoring sessions for physicians, results charts |
| **Automate** | every function from scripts and from Python (`import orcami`): load files, numpy arrays and SimpleITK images, measure, export |
| **Record** | training videos of your session (MP4, microphone and camera picture-in-picture, pointer, keys, watermark) · GIF / picture viewer |
| **Language** | English and French interface |

## Quick start

1. **Open images:** drag files or a DICOM folder onto the window, or use 📂 / 🏥 (patient database) in the
   toolbar. A PET/CT is arranged automatically by its hanging protocol.
2. **Look:** scroll = slices, right-drag = window/level, Ctrl+wheel = zoom, middle-drag = pan, double-click =
   maximise a view, 1–9 = window presets.
3. **Segment:** Segment tab → brush / threshold / nnInteractive, or AI tab → a model. *Statistics in segments*
   gives MTV, SUVmean, SUVmax, SUVpeak and TLG.
4. **Export:** File → *Export to DICOM / PACS* (SEG, RTSTRUCT, SR into the original study) or *Export images &
   GIFs*.
5. Your work is autosaved; after a crash ORCA-MI offers to restore it.

## Python in three lines

```python
import orcami as om                      # orcami.py is next to ORCA-MI.exe
v = om.Viewer()                          # starts or connects to the viewer
v.load("pet.nii.gz"); v.threshold(2.5, 1000); print(v.stats())
```

More in the [user guide → Automation](docs/USER_GUIDE.md#9-automation-scripts-and-python) and the
[examples](#-examples).

## 📂 Examples

Ready-to-run Python scripts (also installed in the `examples` folder next to `ORCA-MI.exe`). Examples 00, 05, 06
and 07 have a `DEMO = True` switch that makes small synthetic images, so they run without your data (set it to
`False` and fill in your own paths); in 01 – 04, write your own paths at the top.

| Script | What it shows |
|---|---|
| [00_load_images.py](examples/00_load_images.py) | the simplest loading: files, DICOM folders, numpy arrays, SimpleITK images; a PET fused on every view; case after case |
| [01_quick_start.py](examples/01_quick_start.py) | a PET/CT with a segmentation: SUVmean / SUVmax / SUVpeak / TLG per lesion, figures and GIFs |
| [02_batch_tlg_table.py](examples/02_batch_tlg_table.py) | one table of lesion measurements for many patients |
| [03_batch_crop_and_figures.py](examples/03_batch_crop_and_figures.py) | crop around the segments and export figures for many cases |
| [04_dynamic_and_time_points.py](examples/04_dynamic_and_time_points.py) | dynamic PET time-activity curves and multi-time-point SPECT |
| [05_segment_and_score_database.py](examples/05_segment_and_score_database.py) | **build a segmentation database and a scoring (reader study) database** and open them |
| [06_review_cases_one_by_one.py](examples/06_review_cases_one_by_one.py) | review a list of cases one by one with fusion, segmentation, colormaps and snapshots |
| [07_prepare_copy_segment_score_database.py](examples/07_prepare_copy_segment_score_database.py) | **prepare a self-contained copy of a segmentation / scoring database** to give to physicians, with their shortcuts |

The scripts need only Python 3 (numpy for the demos). `orcami.py` comes with ORCA-MI (installer and portable zip):
keep the scripts in the `examples` folder of ORCA-MI, or put `orcami.py` next to them.

## AI models

The AI features need a Python environment with PyTorch: **Tools → Install AI environment** sets up a private one
(no administrator rights, your own Python installations are not touched). Trained models are installed from
**Tools → Model library**. Most models have five folds of about 250 MB each: download only the folds you want, and
tick the folds to run in the AI tab. The GPU memory is released after every run.

Models you train or fine-tune yourself stay on your computer: they, their training data and their evaluation are
never uploaded or shared.

## 📖 Documentation

* **[User guide](docs/USER_GUIDE.md)** — also inside the program: **Help → 📖 User guide**.
* **[Video tutorials on YouTube](https://www.youtube.com/@ORCA-MI)** — also in the program: **Help → ▶ Video tutorials**.
* [Changelog](CHANGELOG.md)
* [Third-party licences](docs/third_party_licenses.html) — the open-source libraries built into ORCA-MI.

## Privacy

ORCA-MI never uploads your images or results. Anonymous usage statistics, your country (a separate question, sent
once from Windows' region setting) and notifications about new models are **off unless you agree** when ORCA-MI
asks, and never contain images, file names or patient data. Details:
[Feedback and privacy](docs/USER_GUIDE.md#10-feedback-and-privacy).

## Feedback

In the program: **Help → 🐞 Report a bug / 💡 Request a feature / 💬 Comment**, or open an issue in this
repository, or write to salimiyazdan@gmail.com.

## Licence and citation

ORCA-MI is free for non-commercial research and education; see [LICENSE](LICENSE) (not an open-source licence:
no commercial use, no clinical use, no modified copies, no reverse engineering). The open-source libraries it
contains keep their own licences. The Python helper `orcami.py` and the [example scripts](examples) are under the
**MIT licence**: use, change and share them freely, also in your own projects. ORCA-MI never sends images, patient
data or file names; what a licence request and the optional statistics send is listed in the LICENSE (section 5a)
and in the program (**Help → 🔒 Privacy & usage statistics**).

**Licence file:** ORCA-MI runs as a 7-day trial on each computer; for longer use, request your **free personal
licence** in the program (**Help → 🔑 Licence… → Request your free licence**) and load the `.lic` file you receive by
e-mail. Details: [Licence and trial](docs/USER_GUIDE.md#-licence-and-trial).

If you use ORCA-MI in a publication, please cite it ([CITATION.cff](CITATION.cff); GitHub's *Cite this repository*
button gives APA and BibTeX):

> Salimi, Y. (2026). *ORCA-MI: Open Radiology & Computational Analysis – Molecular Imaging* (Version 0.1.4)
> [Computer software]. https://github.com/orca-mi/orca-mi

---

Author: **Yazdan Salimi** · Built with the help of Jean-Claude (Claude by Anthropic).
