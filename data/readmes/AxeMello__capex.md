# capex

A Flutter mobile app that scans documents with the device camera, extracts text via on-device OCR (Google ML Kit), parses the combined text into structured fields, and writes the result to Google Sheets. Includes an in-app Sheets viewer to browse and manage saved scans.

## Features

- **Multi-page scanning**: capture up to 4 photos per scan session
- **On-device OCR**: text extraction using **Google ML Kit**
- **AI parsing**: converts OCR text into structured JSON (see `lib/ai_parser.dart`)
- **Google Sheets export**: writes parsed results to a target spreadsheet (service account)
- **Sheets viewer inside the app**:
  - list available sheets/tabs
  - view values in a table
  - refresh
  - open in browser
  - delete a sheet/tab (when allowed)

## Tech stack

- Flutter (Dart)
- `camera`
- `google_ml_kit`
- Google Sheets API: `googleapis` + `googleapis_auth`
- `webview_flutter`, `url_launcher`

## Project structure (high level)

- `lib/main.dart` — camera capture flow + navigation + orchestration
- `lib/ocr.dart` — OCR helper (ML Kit text recognizer)
- `lib/ai_parser.dart` — AI parsing of combined OCR text into structured data
- `lib/write_scan_to_sheet.dart` — writes parsed scan results to Google Sheets
- `lib/google_sheets_service.dart` — Sheets API client using a service account
- `lib/sheet.dart` — in-app sheet list + table viewer UI
- `lib/scan_result_store.dart` — holds the latest scan result in memory

## Getting started

### Prerequisites

- Flutter SDK installed
- Android Studio / Android SDK (for Android builds)
- A Google Cloud project with:
  - **Google Sheets API** enabled
  - a **Service Account** with access to the destination spreadsheet

### Install dependencies

```bash
flutter pub get
```

### Run on a device/emulator

```bash
flutter run
```

## Google Sheets setup

1. Create a Google Cloud **Service Account** and download its JSON key.
2. Share your target Google Spreadsheet with the service account email (Editor access).
3. Place the JSON key at:

`assets/service_account.json`

4. Ensure it’s included in `pubspec.yaml` under `flutter/assets`.

### Spreadsheet configuration

The app uses this spreadsheet ID:

- `lib/google_sheets_service.dart` → `spreadsheetId`

Update that constant to point to your spreadsheet if needed.
