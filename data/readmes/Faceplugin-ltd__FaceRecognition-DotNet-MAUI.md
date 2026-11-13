<div align="center">
<img alt="FacePlugin" src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/brand/logo.png" width="400"/>
</div>

#### 🌐 Company Site - [Here](https://faceplugin.com)

#### 🤗 Hugging Face - [Here](https://huggingface.co/FacePlugin-Ltd)

#### 🛟 Help Center - [Here](https://doc.faceplugin.com)

#### 🐳 Docker Hub - [Here](https://hub.docker.com/u/faceplugin)

# FacePlugin Face Recognition SDK — .NET MAUI (Fully On-Premise)

> Android and iOS each call the Face Recognition SDK inside this app.
> Jump: [Quick Start](#quick-start) · [Get the runtimes](#get-the-runtimes) · [Run the demo](#run-the-demo) · [License](#sdk-license) · [Integrate](#setup-on-your-own-app)

Customer repo name: `FaceRecognition-DotNet-MAUI`

## Quick Start

- [ ] Clone [FaceRecognition-DotNet-MAUI](https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI)
- [ ] Install the **.NET 8** SDK and the `maui` workload. `global.json` pins the build to 8.0
- [ ] Download the Android AAR and the iOS frameworks from the **same** pack — [Get the runtimes](#get-the-runtimes)
- [ ] Keep the demo ids: Android `com.faceplugin.facerecognitionsdk` / iOS `com.faceplugin.facerecognition.app`
- [ ] Run on a connected phone — [Run the demo](#run-the-demo). Home shows **Enroll**, **Identify**, **Capture**, **Attribute**, **Settings**, and **About**

## Introduction

FacePlugin **Face Recognition SDK for .NET MAUI** is an on-device sample for Android and iOS. Enroll faces, identify in 1:N, capture with an oval coach, and read attributes with 2D liveness — the same demo as the Flutter, React Native, and Ionic apps.

All processing stays on the device. **No** biometric data is sent to FacePlugin cloud.

Native binaries are **not** in git. Download them from Google Drive and copy them into the paths below. Drop either the full **FaceRecognitionSDK** runtime or the **FaceRecognition-Liveness** runtime.

### Main Functionalities

| Feature | Supported |
| ------- | --------- |
| Gallery enroll (single-face template) | ✓ |
| Live 1:N identify with VideoWorker | ✓ |
| 2D liveness on capture | ✓ |
| Oval capture coach with a 2 second hold | ✓ |
| Gallery attributes, age, gender, emotion, landmarks | ✓ with the FaceRecognitionSDK pack |
| Local person database (demo) | ✓ |
| Settings (thresholds / clear DB) | ✓ |

Attribute fields come from the **FaceRecognitionSDK** pack. The **FaceRecognition-Liveness** pack returns detection, templates, 1:N identity, and the liveness score.

### Product List

| Platform | Repository |
| -------- | ---------- |
| Android (Recognition) | [FaceRecognition-Android](https://github.com/Faceplugin-ltd/FaceRecognition-Android) |
| iOS (Recognition) | [FaceRecognition-iOS](https://github.com/Faceplugin-ltd/FaceRecognition-iOS) |
| Android (Recognition-Liveness) | [FaceRecognition-Liveness-Android](https://github.com/Faceplugin-ltd/FaceRecognition-Liveness-Android) |
| iOS (Recognition-Liveness) | [FaceRecognition-Liveness-iOS](https://github.com/Faceplugin-ltd/FaceRecognition-Liveness-iOS) |
| React Native (Recognition) | [FaceRecognition-React-Native](https://github.com/Faceplugin-ltd/FaceRecognition-React-Native) |
| Flutter (Recognition) | [FaceRecognition-Flutter](https://github.com/Faceplugin-ltd/FaceRecognition-Flutter) |
| Ionic Capacitor (Recognition) | [FaceRecognition-Ionic-Capacitor](https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Capacitor) |
| Ionic Cordova (Recognition) | [FaceRecognition-Ionic-Cordova](https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Cordova) |
| **.NET MAUI (Recognition)** | **[FaceRecognition-DotNet-MAUI](https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI)** (**this repo**) |
| Windows (Recognition) | [FaceRecognition-Windows](https://github.com/Faceplugin-ltd/FaceRecognition-Windows) |
| Linux / Docker (Recognition) | [FaceRecognition-Docker](https://github.com/Faceplugin-ltd/FaceRecognition-Docker) |

---

## Before you start

| Step | What you need |
| ---- | ------------- |
| 1 | **.NET 8 SDK** and `dotnet workload install maui`, run from this folder so `global.json` selects SDK 8. iOS builds need **macOS + Xcode 15+** |
| 2 | Android `facerecognitionsdk.aar` and iOS `facerecognitionsdk.framework`, `FaceRecognitionEngine.framework`, `onnxruntime.framework` |
| 3 | Demo licenses are in `src/FaceRecognition.Net.Maui/LicenseKeys.cs` (Android `com.faceplugin.facerecognitionsdk`, iOS `com.faceplugin.facerecognition.app`). Request a new key only if you change the application id |

### System requirements

| Item | Android | iOS |
| ---- | ------- | --- |
| Host | Windows / macOS | **macOS only** |
| SDK | .NET 8, MAUI workload | Same, plus Xcode **15+** |
| OS | `minSdk` **24** | **15.0** |
| Device | Physical phone | Physical iPhone |
| Demo id | `com.faceplugin.facerecognitionsdk` | `com.faceplugin.facerecognition.app` |

---

## Get the runtimes

The copy paths below are the same for both packs. Place the Android AAR and the iOS frameworks from the **same** pack.

| Pack | What it includes | Android | iOS |
| ---- | ---------------- | ------- | --- |
| **FaceRecognitionSDK** | Detection, templates, 1:1, 1:N, 2D liveness, and attributes | [Google Drive](https://drive.google.com/drive/folders/1kpzYVv9Gbm_pEpDe9-x7FGB4NWZzvez0) | [Google Drive](https://drive.google.com/drive/folders/1PKmV-o7gq7s7dDtiNgXPfCi2ZlWaRy5H) |
| **FaceRecognition-Liveness** | Detection, templates, 1:1, 1:N, and 2D liveness | [Google Drive](https://drive.google.com/drive/folders/126bZhQ_ql3PkgwkH44Q6XiNe5aNn7rUW?usp=sharing) | [Google Drive](https://drive.google.com/drive/folders/1WnekMmLIFXsxw93vy7gLBuk15idN23U9?usp=sharing) |

### Android — `facerecognitionsdk.aar`

```text
src/FaceRecognition.Net.Maui/Platforms/Android/libs/facerecognitionsdk.aar
```

The project references the AAR, and compiles `FaceBridge.java`, only when that file is present.

### iOS

```text
src/FaceRecognition.Net.Maui/Platforms/iOS/Frameworks/
├── facerecognitionsdk.framework
├── FaceRecognitionEngine.framework
└── onnxruntime.framework
```

Each framework is linked only when that folder is present.

---

## Run the demo

`global.json` keeps the build on SDK 8 when a newer SDK is the default:

```json
{
  "sdk": {
    "version": "8.0.100",
    "rollForward": "latestFeature"
  }
}
```

Install the [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0), then from this folder:

```bash
git clone https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI.git
cd FaceRecognition-DotNet-MAUI
dotnet workload install maui
```

Place the Android AAR and the iOS frameworks first — [Get the runtimes](#get-the-runtimes). Keep the demo application ids so the included license activates.

```bash
# Android — phone connected, USB debugging on
dotnet build src/FaceRecognition.Net.Maui/FaceRecognition.Net.Maui.csproj -f net8.0-android -t:Run

# iOS — macOS + Xcode 15+, iPhone connected
dotnet build src/FaceRecognition.Net.Maui/FaceRecognition.Net.Maui.csproj -f net8.0-ios -r ios-arm64 -t:Run
```

| Platform | Identifier |
| -------- | ---------- |
| Android application id | `com.faceplugin.facerecognitionsdk` |
| iOS bundle id | `com.faceplugin.facerecognition.app` |

1. Wait for the home status line to show **Ready**.
2. **Enroll** picks one face from the gallery and stores a template on the device.
3. **Identify** runs VideoWorker 1:N against the enrolled list.
4. **Capture** holds for 2 seconds while the circle border fills green from 12 o'clock. The saved frame is the last frame of that hold. The hold restarts if the face leaves the gate.
5. **Attribute** reads liveness, age, gender, emotion, and the other estimators in the pack.
6. **Settings** stores the camera lens and the thresholds. Liveness defaults to **0.8**. Eye-close defaults to **0.5**.

### Screenshots

| Home | Identify | Capture |
| ---- | -------- | ------- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/home.png" alt="FacePlugin Face Recognition — Home with Enroll, Identify, Capture, Attribute, Settings, About" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/identify.png" alt="FacePlugin Face Recognition — live 1:N identify with face box, landmarks, and liveness" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/capture.png" alt="FacePlugin Face Recognition — oval capture coach with Move closer" width="240"/></p> |

| Capture result | Attribute | Attribute (emotion) |
| -------------- | --------- | ------------------- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/capture-result.png" alt="FacePlugin Face Recognition — capture result with liveness, quality, and Enroll" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/attribute.png" alt="FacePlugin Face Recognition — attributes: 14 landmarks, liveness, age, gender" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/attribute-emotion.png" alt="FacePlugin Face Recognition — attributes: landmarks, age, gender, emotion" width="240"/></p> |

| Attribute (quality) | Settings | About |
| ------------------- | -------- | ----- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/attribute-quality.png" alt="FacePlugin Face Recognition — quality: blur, noise, pose, bounding box" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/settings.png" alt="FacePlugin Face Recognition — Settings for camera lens and thresholds" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/about.png" alt="FacePlugin Face Recognition SDK — About, on-device identity" width="240"/></p> |

| Home (tiles) | Attribute (liveness) |
| ------------ | -------------------- |
| <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/home-tiles.png" alt="FacePlugin Face Recognition — six home action tiles" width="240"/></p> | <p align="center"><img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/android/attribute-liveness.png" alt="FacePlugin Face Recognition — liveness spoof score, age, gender" width="240"/></p> |

---

## SDK License

Licenses are **offline** and bound to your `applicationId` / bundle identifier.

The sample app already includes valid keys for Android `com.faceplugin.facerecognitionsdk` and iOS `com.faceplugin.facerecognition.app`. You only need a new key if you use a different id.

### How to get a license

The code below shows how to use the license:

[https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI/blob/e86ab6b726d34b6c263f061b438d661379aef7e0/src/FaceRecognition.Net.Maui/LicenseKeys.cs#L10-L21](https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI/blob/e86ab6b726d34b6c263f061b438d661379aef7e0/src/FaceRecognition.Net.Maui/LicenseKeys.cs#L10-L21)

[https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI/blob/e86ab6b726d34b6c263f061b438d661379aef7e0/src/FaceRecognition.Net.Maui/FaceSdk.cs#L103-L119](https://github.com/Faceplugin-ltd/FaceRecognition-DotNet-MAUI/blob/e86ab6b726d34b6c263f061b438d661379aef7e0/src/FaceRecognition.Net.Maui/FaceSdk.cs#L103-L119)

Please [contact us](#contact) to get a license for **your own app**.

Call order, off the UI thread: `GetMachineCodeAsync` → `SetActivationAsync` → `InitAsync`. `0` means success.

| Code | Meaning |
| ---- | ------- |
| 0 | Success |
| 1 | Invalid license |
| 2 | Expired license |
| 3 | Not activated |
| 4 | Init failed |

---

## Setup on your own app

Reference `FaceSdk` from this project, or copy `FaceSdk.cs` and the platform file for the target you ship.

1. Android: add `facerecognitionsdk.aar` as an `AndroidLibrary` and keep `FaceBridge.java` on the compile classpath.
2. iOS: add `facerecognitionsdk.framework`, `FaceRecognitionEngine.framework`, and `onnxruntime.framework` as `NativeReference` items with `ForceLoad`.
3. Keep calls off the UI thread. `SdkGate` already serializes them.
4. Enroll with `DetectAsync` (exactly one face) then `ExtractCroppedFeatureAsync`.
5. Identify with `StartVideoWorkerAsync`, `SyncDatabaseAsync`, `AddFrameAsync`, and `PollEventAsync`.
6. Capture uses the same VideoWorker feed plus `DetectAsync` for the pose, eye, and liveness gate.

You do not need `HomePage` in your own app.

---

## Contact

![faceplugin.com](https://img.shields.io/badge/email-info@faceplugin.com-blue.svg?logo=gmail)  ![Telegram @FacePluginSupport](https://img.shields.io/badge/telegram-@FacePluginSupport-blue.svg?logo=telegram)  ![faceplugin.com](https://img.shields.io/badge/whatsapp-faceplugin-blue.svg?logo=whatsapp)
