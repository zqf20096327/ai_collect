# VocalCanvas Studio

VocalCanvas Studio transforms text, images, and multi-page PDFs into expressive speech entirely in the browser with no server dependencies.

## Highlights
- Image OCR: Drop in a photo or scan to extract editable text in seconds.
- PDF Pipeline: Render each page, run OCR, and build a unified transcript automatically.
- Voice Studio: Preview voices, adjust rate, and queue narration segments before export.
- Local Workflow: Runs offline via WebAssembly OCR and built-in browser speech synthesis.

## Quick Start
1. Clone or download this repository.
2. Serve the project directory with any static web server, for example `python -m http.server` from the project root.
3. Open the served URL in a modern desktop browser (Chrome, Edge, or Firefox).

## Using the App
- Use the image uploader for PNG or JPG assets; use the PDF uploader for multi-page documents.
- Confirm each recognition result, edit the transcript inline, and save snapshots as needed.
- Select a voice, pitch, and rate, then generate narration for the full transcript or selected passages.
- Export audio-ready text or the recognized transcript to plain `.txt` files via the download button.

## Project Layout
- `index.html` hosts the interface shell and orchestrates the main workflow.
- `js/main.js` coordinates OCR, PDF rendering, and speech synthesis controls.
- `js/articulate.js` focuses on speech synthesis helpers and voice selection logic.
- `css/` contains layout and component styling, including Bootstrap overrides.
- `inputs/` and `outputs/` provide sample documents and generated transcripts for quick testing.

## Technology Stack
- Tesseract.js WebAssembly build for client-side OCR.
- Mozilla PDF.js for rendering PDF pages into canvas elements.
- Web Speech API for voice playback and narration controls.
- Vanilla JavaScript enhanced with Bootstrap 4 utilities for layout.

## Development Notes
- Web Speech API voice availability varies by browser and operating system; confirm support before demos.
- Large PDFs process page by page; keep the browser tab focused for faster OCR throughput.
- To customize styling, extend the utility classes in `css/main.css` instead of editing Bootstrap directly.

## License
This project is distributed under the Apache License 2.0. See `LICENSE-2.0.txt` for full details.
