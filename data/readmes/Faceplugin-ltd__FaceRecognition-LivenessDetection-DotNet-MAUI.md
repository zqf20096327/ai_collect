<div align="center">
<img alt="FacePlugin" src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/brand/logo.png" width="400"/>
</div>

#### 🌐 Company Site - [Here](https://faceplugin.com)
#### 🤗 Hugging Face - [Here](https://huggingface.co/FacePlugin-Ltd)
#### 🛟 Help Center - [Here](https://doc.faceplugin.com)
#### 🐳 Docker Hub - [Here](https://hub.docker.com/r/faceplugin/face-recognition)

# FacePlugin Face Recognition + 1:N Identification + Liveness Detection — .NET MAUI (Fully On-Premise)

Jump: [Quick start](#quick-start) · [Get the runtimes](#get-the-runtimes) · [Run the demo](#run-the-demo) · [SDK License](#sdk-license) · [Setup on your own app](#setup-on-your-own-app) · [About SDK](#about-sdk)

## Quick start

- [ ] Clone [FaceRecognition-LivenessDetection-DotNet-MAUI](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-DotNet-MAUI)
- [ ] Install the [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0), then `dotnet workload install maui`
- [ ] Place the native runtimes — [Get the runtimes](#get-the-runtimes)
- [ ] `python run_android.py` (or `python run_ios.py` on macOS) with a **physical** phone connected
- [ ] The demo ships with license keys for `com.faceplugin.facerecognitionsdk` (Android) and `com.faceplugin.facerecognition.app` (iOS)

## Introduction

FacePlugin **Face Recognition + Liveness Detection for .NET MAUI** runs face recognition and passive liveness entirely on the device. Nothing is sent to a FacePlugin server, which is what banking, access control, and privacy-first identity apps need. Its headline capability is **1:N identification**: enroll your people once, then ask *who is this?* of a camera frame or a photo and get a ranked candidate list back — searched against the templates your app keeps on the device, so no face ever leaves it.

This repository is the whole product: the **MAUI app project**, the native bindings for Android and iOS (`FaceSdk`), and a **demo UI** built on top of them — so what you read here is what the demo runs.

The engine binaries are the same ones the native apps use, so you get identical scores on both platforms.

### Main Functionalities

| Feature | API |
| ------- | --- |
| **1:N identification** on a live camera feed | `StartVideoWorkerAsync` · `SyncDatabaseAsync` · `AddFrameAsync` · `PollEventAsync` |
| Face detection (bounding box, landmarks, pose, attributes) | `FaceSdk.DetectAsync` |
| Passive liveness (anti-spoofing) | `FaceSdk.DetectAsync` with the liveness flag, live worker events |
| Face template extraction | `FaceSdk.DetectWithTemplatesAsync` |
| Template similarity | `FaceSdk.SimilarityAsync` · `FaceSdk.SimilarityManyAsync` |
| Face crop for enrollment | `FaceSdk.CropFaceAsync` |
| License and engine lifecycle | `GetMachineCodeAsync` · `SetActivationAsync` · `InitAsync` · `GetLicenseStatusAsync` |

### Product List

| Platform | Repository |
| -------- | ---------- |
| Android | [FaceRecognition-LivenessDetection-Android](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android) |
| iOS | [FaceRecognition-LivenessDetection-iOS](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-iOS) |
| React Native | [FaceRecognition-LivenessDetection-ReactNative](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-ReactNative) |
| Flutter | [FaceRecognition-LivenessDetection-Flutter](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter) |
| **.NET MAUI** | **[FaceRecognition-LivenessDetection-DotNet-MAUI](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-DotNet-MAUI)** **(this repo)** |
| Ionic Cordova | [FaceRecognition-LivenessDetection-Ionic-Cordova](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Ionic-Cordova) |
| Ionic Capacitor | [FaceRecognition-LivenessDetection-Ionic-Capacitor](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Ionic-Capacitor) |

### Related products

- **Face Liveness Detection — Android** — [FaceLivenessDetection-Android](https://github.com/Faceplugin-ltd/FaceLivenessDetection-Android) — liveness only
- **Face Liveness Detection — iOS** — [FaceLivenessDetection-iOS](https://github.com/Faceplugin-ltd/FaceLivenessDetection-iOS) — liveness only
- **Face Recognition — Windows** — [FaceRecognition-Windows](https://github.com/Faceplugin-ltd/FaceRecognition-Windows) — on-premise server
- **Face Recognition — Docker** — [FaceRecognition-Docker](https://github.com/Faceplugin-ltd/FaceRecognition-Docker) — on-premise server

## Before you start

| Step | What you need |
| ---- | ------------- |
| 1 | .NET 8 SDK and the MAUI workload (Android Studio for Android, Xcode 15+ on macOS for iOS) |
| 2 | The Android AAR and the iOS frameworks — see [Get the runtimes](#get-the-runtimes) |
| 3 | A **physical** phone. Emulators and the simulator have no usable camera for liveness |
| 4 | A license key for your application ids ([contact us](#contact)). The demo already has keys for the ids above |

### System requirements

| Item | Minimum | Recommended |
| ---- | ------- | ----------- |
| Android | API 24, `arm64-v8a` | Android 10 or newer |
| iOS | 15.0, arm64 device | iPhone 11 or newer |
| .NET | 8.0 | 8.0 (latest patch) |
| RAM (device) | 4 GB | 6 GB or more |

This project targets `net8.0-android` and `net8.0-ios`.

## Get the runtimes

The native binaries are too large for GitHub, so they are published on the **Android** and **iOS** release pages. Both platforms use the same engine, so take them from the same release.

### Android — `facerecognitionsdk.aar`

**[Download from the Android release](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android/releases/tag/latest)**

```text
src/FaceRecognition.Net.Maui/Platforms/Android/libs/facerecognitionsdk.aar
```

The project references the AAR, and compiles `FaceBridge.java`, only when that file is present.

### iOS — frameworks

**[Download from the iOS release](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-iOS/releases/tag/latest)**

```text
src/FaceRecognition.Net.Maui/Platforms/iOS/Frameworks/
├── facerecognitionsdk.framework
├── FacePluginSDK.framework
├── FacePPlugin.framework
└── FaceDetect.framework
```

Device arm64 only. Each framework is linked only when that folder is present.

## Run the demo

```bash
git clone https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-DotNet-MAUI.git
cd FaceRecognition-LivenessDetection-DotNet-MAUI
dotnet workload install maui
# place the AAR and the iOS frameworks — see above
python run_android.py
python run_ios.py          # macOS
```

`global.json` keeps the build on .NET 8 when a newer SDK is the default. The run scripts are the same as:

```bash
# Android — phone connected, USB debugging on
dotnet build src/FaceRecognition.Net.Maui/FaceRecognition.Net.Maui.csproj -f net8.0-android -t:Run

# iOS — macOS + Xcode 15+, iPhone connected
dotnet build src/FaceRecognition.Net.Maui/FaceRecognition.Net.Maui.csproj -f net8.0-ios -r ios-arm64 -t:Run
```

Keep the demo ids so the included license activates:

| Platform | Identifier |
| -------- | ---------- |
| Android application id | `com.faceplugin.facerecognitionsdk` |
| iOS bundle id | `com.faceplugin.facerecognition.app` |

The demo has five tabs:

| Tab | What it shows |
| --- | ------------- |
| **Identity** | Live 1:N against everyone enrolled, with liveness, then a ranked result |
| **People** | Enroll from photos or the capture coach, search, edit, delete |
| **Attribute** | Every face in a photo: liveness, quality, pose, expression, age, gender, landmarks |
| **Liveness** | Live anti-spoofing check on the camera feed |
| **Settings** | Match, liveness, and pose thresholds; license status |

### Screenshots

<p align="center">
<img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/mobile/identify.gif" width="240" alt="FacePlugin Face Recognition — live 1:N identification with liveness"/>
&nbsp;
<img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/mobile/people.gif" width="240" alt="FacePlugin Face Recognition — enroll people with the guided capture coach"/>
&nbsp;
<img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/mobile/attribute.gif" width="240" alt="FacePlugin Face Recognition — face attributes, quality and landmarks from a photo"/>
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/mobile/liveness.gif" width="240" alt="FacePlugin Face Recognition — passive liveness check on the camera feed"/>
&nbsp;
<img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/screenshots/face-recognition/mobile/settings.png" width="240" alt="FacePlugin Face Recognition — match, liveness and pose thresholds in Settings"/>
</p>

## SDK License

The demo runs as it is: a FacePlugin key for `com.faceplugin.facerecognitionsdk` (Android) and `com.faceplugin.facerecognition.app` (iOS) is already in the code. Licenses are **offline** — once activated, nothing phones home — and each one is bound to your application id and bundle identifier, so your own app needs its own key.

### Set your SDK license

| What | File | What to find |
| ---- | ---- | ------------ |
| The keys | [`LicenseKeys.cs`](src/FaceRecognition.Net.Maui/LicenseKeys.cs) | `public const string Android`, `Ios` |
| Where they are used | [`FaceSdk.cs`](src/FaceRecognition.Net.Maui/FaceSdk.cs) | `SetActivationAsync(LicenseKeys.Demo)` |
| The ids they are bound to | [`FaceRecognition.Net.Maui.csproj`](src/FaceRecognition.Net.Maui/FaceRecognition.Net.Maui.csproj) | `<ApplicationId>` |

Find this, and put your key in place of the demo one:

```csharp
public const string Android =
    "FP1.RlBMMQMAAQDJx5NBpyjuxrTSuz8MAgAA…";
```

Rebuild for the target you ship. `LicenseKeys.Demo` picks the Android or iOS key at compile time, so set both.

### How to get a key

[Contact us](#contact) with the id you will ship. If we ask for a machine code, `FaceSdk.GetMachineCodeAsync()` returns it. After activation, `FaceSdk.GetLicenseStatusAsync()` reports what the key unlocks.

### License capabilities (Recognition + Liveness)

| Capability | Meaning |
| ---------- | ------- |
| **Recognition** | Detection, attributes, quality, templates, 1:1 similarity, and 1:N identification |
| **Liveness** | Passive anti-spoofing on camera frames and stills |

## Setup on your own app

You integrate from **this repository** — there is no NuGet package, and no package-server dependency to add.

1. Clone this repository and add `src/FaceRecognition.Net.Maui` to your solution, or copy `FaceSdk.cs` and the platform file for the target you ship.
2. Android: add `facerecognitionsdk.aar` as an `AndroidLibrary`, and keep `FaceBridge.java` on the compile classpath.
3. iOS: add `facerecognitionsdk.framework`, `FacePluginSDK.framework`, `FacePPlugin.framework`, and `FaceDetect.framework` as `NativeReference` items with `ForceLoad`.
4. Set **your** application ids and request a license for them.
5. Keep engine calls off the UI thread — `SdkGate` already serializes them.
6. Add camera and photo permissions for both platforms.

You do **not** need the demo pages. Full wiring and result JSON: [https://doc.faceplugin.com](https://doc.faceplugin.com)

## About SDK

Activate once at start-up, then call the engine. `0` means success.

**1. Activate and initialize**

```csharp
var machine = await FaceSdk.GetMachineCodeAsync();      // send this when you request a key
var code = await FaceSdk.SetActivationAsync(LicenseKeys.Demo);
if (code == 0)
    code = await FaceSdk.InitAsync();

var status = await FaceSdk.GetLicenseStatusAsync();
var message = FaceSdk.StatusLabel(code);
```

`SdkSession.BootstrapAsync()` does all of this for the demo, and publishes `Ready`, `Loading`, and `Message` for the UI.

**2. Read a face, and enroll it**

```csharp
var json = await FaceSdk.DetectAsync(jpeg, flags);                 // faces, pose, attributes, liveness
var withTemplates = await FaceSdk.DetectWithTemplatesAsync(jpeg, flags);
var crop = await FaceSdk.CropFaceAsync(jpeg, box);
// store the template and the crop in YOUR database

var score = await FaceSdk.SimilarityAsync(featureA, featureB);     // 1:1
```

**3. Live 1:N identification**

```csharp
await FaceSdk.StartVideoWorkerAsync(0.67f);
await FaceSdk.SyncDatabaseAsync(features, 0.67f);
await FaceSdk.AddFrameAsync(jpeg);
var evt = await FaceSdk.PollEventAsync();
await FaceSdk.StopVideoWorkerAsync();
```

**4. Status codes**

| Code | Meaning |
| ---- | ------- |
| 0 | Activate / init OK |
| 1 | Invalid license |
| 2 | Expired license |
| 3 | Not activated |
| 4 | Init failed |

Thresholds (match, liveness, pose, eye-close) are parameters you pass from C#, so you can tune them for your product. The Settings tab stores the demo defaults.

## Contact

<div align="left">
<a target="_blank" href="mailto:info@faceplugin.com"><img src="https://img.shields.io/badge/email-info@faceplugin.com-blue.svg?logo=gmail" alt="faceplugin.com"></a>&emsp;
<a target="_blank" href="https://t.me/FacePluginSupport"><img src="https://img.shields.io/badge/telegram-@FacePluginSupport-blue.svg?logo=telegram" alt="Telegram @FacePluginSupport"></a>&emsp;
<a target="_blank" href="https://wa.me/+14692784822"><img src="https://img.shields.io/badge/whatsapp-faceplugin-blue.svg?logo=whatsapp" alt="faceplugin.com"></a>
</div>
