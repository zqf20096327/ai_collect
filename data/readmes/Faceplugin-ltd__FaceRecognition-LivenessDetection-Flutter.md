<div align="center">
<img alt="FacePlugin" src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/brand/logo.png" width="400"/>
</div>

#### 🌐 Company Site - [Here](https://faceplugin.com)
#### 🤗 Hugging Face - [Here](https://huggingface.co/FacePlugin-Ltd)
#### 🛟 Help Center - [Here](https://doc.faceplugin.com)
#### 🐳 Docker Hub - [Here](https://hub.docker.com/r/faceplugin/face-recognition)

# FacePlugin Face Recognition + 1:N Identification + Liveness Detection — Flutter (Fully On-Premise)

Jump: [Quick start](#quick-start) · [Get the runtimes](#get-the-runtimes) · [Run the demo](#run-the-demo) · [SDK License](#sdk-license) · [Setup on your own app](#setup-on-your-own-app) · [About SDK](#about-sdk)

## Quick start

- [ ] Clone [FaceRecognition-LivenessDetection-Flutter](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter)
- [ ] `dart run tool/bootstrap.dart`
- [ ] Place the native runtimes — [Get the runtimes](#get-the-runtimes)
- [ ] `python run_android.py` (or `python run_ios.py` on macOS) with a **physical** phone connected
- [ ] The demo ships with license keys for `com.faceplugin.facerecognitionsdk` (Android) and `com.faceplugin.facerecognition.app` (iOS)

## Introduction

FacePlugin **Face Recognition + Liveness Detection for Flutter** runs face recognition and passive liveness entirely on the device. Nothing is sent to a FacePlugin server, which is what banking, access control, and privacy-first identity apps need. Its headline capability is **1:N identification**: enroll your people once, then ask *who is this?* of a camera frame or a photo and get a ranked candidate list back — searched against the templates your app keeps on the device, so no face ever leaves it.

This repository is the whole product: the **Flutter plugin** (`face_recognition_sdk`), the native bridges for Android and iOS, and an **example app** built from that same plugin — so what you read here is what the demo runs.

The engine binaries are the same ones the native apps use, so you get identical scores on both platforms.

### Main Functionalities

| Feature | API |
| ------- | --- |
| **1:N identification** on a live camera feed | `startVideoWorker` · `syncVideoWorkerDatabase` · `applyLiveFrame` |
| Face detection (bounding box, landmarks, pose, attributes) | `faceDetection` |
| Passive liveness (anti-spoofing) | `faceDetection` with liveness, live `VideoWorker` events |
| Face image quality | `quality` |
| Face template extraction and similarity | `templateExtraction` · `similarity` |
| Face crop for enrollment | `cropFace` |
| License and engine lifecycle | `getMachineCode` · `setActivation` · `init` · `getLicenseStatus` |

### Product List

| Platform | Repository |
| -------- | ---------- |
| Android | [FaceRecognition-LivenessDetection-Android](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android) |
| iOS | [FaceRecognition-LivenessDetection-iOS](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-iOS) |
| React Native | [FaceRecognition-LivenessDetection-ReactNative](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-ReactNative) |
| **Flutter** | **[FaceRecognition-LivenessDetection-Flutter](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter)** **(this repo)** |
| .NET MAUI | [FaceRecognition-LivenessDetection-DotNet-MAUI](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-DotNet-MAUI) |
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
| 1 | Flutter 3.19+, and a mobile toolchain (Android Studio, and Xcode 15+ on macOS) |
| 2 | The Android AAR and the iOS frameworks — see [Get the runtimes](#get-the-runtimes) |
| 3 | A **physical** phone. Emulators and the simulator have no usable camera for liveness |
| 4 | A license key for your ids ([contact us](#contact)). The demo already has keys for the ids above |

### System requirements

| Item | Minimum | Recommended |
| ---- | ------- | ----------- |
| Android | `minSdk 24`, `arm64-v8a` | Android 10 or newer |
| iOS | 15.0, arm64 device | iPhone 11 or newer |
| Flutter | 3.19 | Latest stable |
| RAM (device) | 4 GB | 6 GB or more |

## Get the runtimes

The native binaries are too large for GitHub, so they are published on the **Android** and **iOS** release pages. Both platforms use the same engine, so take them from the same release.

### Android — `facerecognitionsdk.aar`

**[Download from the Android release](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android/releases/tag/latest)**

| Where | Path |
| ----- | ---- |
| The plugin | `android/libs/facerecognitionsdk.aar` |
| The example app | `example/android/libfacesdk/facerecognitionsdk.aar` |

`dart run tool/bootstrap.dart` wires the example module for you once the file is in place.

### iOS — frameworks

**[Download from the iOS release](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-iOS/releases/tag/latest)**

Place them in `ios/Frameworks/`, device arm64 only:

```text
ios/Frameworks/
├── facerecognitionsdk.framework
├── FacePluginSDK.xcframework
├── FacePlugin.xcframework
└── FaceDetect.xcframework
```

Then `cd example/ios && pod install`.

## Run the demo

```bash
git clone https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter.git
cd FaceRecognition-LivenessDetection-Flutter
dart run tool/bootstrap.dart
# place the AAR and the iOS frameworks — see above
python run_android.py
python run_ios.py          # macOS
```

Or run `flutter run` from `example`.

Keep the demo ids so the included license activates:

| Platform | Id |
| -------- | -- |
| Android `applicationId` | `com.faceplugin.facerecognitionsdk` |
| iOS bundle id | `com.faceplugin.facerecognition.app` |

The example app has five tabs:

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

The demo runs as it is: a FacePlugin key for `com.faceplugin.facerecognitionsdk` (Android) and `com.faceplugin.facerecognition.app` (iOS) is already in the code. Licenses are **offline** — once activated, nothing phones home — and each one is bound to your `applicationId` and bundle identifier, so your own app needs its own key.

### Set your SDK license

| What | File | What to find |
| ---- | ---- | ------------ |
| The keys | [`example/lib/core/constants/license.dart`](example/lib/core/constants/license.dart) | `androidLicense`, `iosLicense` |
| Where they are used | [`example/lib/shell/app.dart`](example/lib/shell/app.dart) | `_engine.start(demoLicense())` |
| The ids they are bound to | [`example/lib/core/constants/license.dart`](example/lib/core/constants/license.dart) | `androidApplicationId`, `iosBundleId` |

Find this, and put your key in place of the demo one:

```dart
const androidLicense =
    'FP1.RlBMMQMAAQDJx5NBpyjuxrTSuz8MAgAA…';
```

Rebuild the native app — a hot reload is not enough, because activation happens once at start-up. `demoLicense()` picks the Android or iOS key at runtime, so set both.

### How to get a key

[Contact us](#contact) with the id you will ship. If we ask for a machine code, `getMachineCode()` returns it. After activation, `getLicenseStatus()` reports what the key unlocks.

### License capabilities (Recognition + Liveness)

| Capability | Meaning |
| ---------- | ------- |
| **Recognition** | Detection, attributes, quality, templates, 1:1 similarity, and 1:N identification |
| **Liveness** | Passive anti-spoofing on camera frames and stills |

## Setup on your own app

You integrate from **this repository** — there is no pub.dev package, and no package-server dependency to add.

1. Clone this repository next to your app:

   ```bash
   git clone https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter.git
   ```

2. Add it as a **path** dependency in your `pubspec.yaml`:

   ```yaml
   dependencies:
     face_recognition_sdk:
       path: ../FaceRecognition-LivenessDetection-Flutter
   ```

   Then `flutter pub get`.

3. Copy the native runtimes — [Get the runtimes](#get-the-runtimes):

   | Platform | What to do |
   | -------- | ---------- |
   | Android | Copy `example/android/libfacesdk/` into **your app** at `android/libfacesdk/`, put `facerecognitionsdk.aar` there, and add `include(":libfacesdk")` to `settings.gradle(.kts)`. Do not add the AAR with `implementation(files(…))` inside the plugin — AGP fails `bundleDebugAar`. |
   | iOS | Put the frameworks in the plugin's `ios/Frameworks/`, then `pod install` in your app's `ios/` |

4. Set **your** `applicationId` / bundle id, and request a license for those ids.
5. Add camera and photo permissions (see the example's `AndroidManifest.xml` and `Info.plist`).

You do **not** need the `example/` app or its person database. Full wiring and result JSON: [https://doc.faceplugin.com](https://doc.faceplugin.com)

## About SDK

Activate once at start-up, then call the engine. `sdkSuccess` (`0`) means success.

**1. Activate and initialize**

```dart
import 'package:face_recognition_sdk/face_recognition_sdk.dart';

Future<void> activate() async {
  final machine = await getMachineCode();        // send this when you request a key
  final act = await setActivation('FP1.…');      // bound to YOUR applicationId / bundle id
  if (act != sdkSuccess) throw StateError(await lastLicenseError());

  final code = await init();
  if (code != sdkSuccess) throw StateError('init failed: $code');

  final status = await getLicenseStatus();
}
```

**2. Read a face, and enroll it**

```dart
final faces = await faceDetection(imagePath);
if (faces.length == 1) {
  final template = await templateExtraction(imagePath, faces.first);
  final crop = await cropFace(imagePath, faces.first);
  // store the template and the crop in YOUR database
}

final score = await similarity(templateA, templateB);   // 1:1
```

**3. Live 1:N identification**

```dart
await startVideoWorker(const VideoWorkerConfig(matchThreshold: 0.67));
await syncVideoWorkerDatabase(templates);
// feed camera frames with applyLiveFrame(...)
await stopVideoWorker();
```

**4. Status codes**

| Code | Constant | Meaning |
| ---- | -------- | ------- |
| 0 | `sdkSuccess` | Activate / init OK |
| 1 | `sdkLicenseInvalid` | Invalid license |
| 2 | `sdkLicenseExpired` | Expired license |
| 3 | `sdkNotActivated` | Not activated |

Thresholds (match, liveness, pose, eye-close) are parameters you pass from Dart, so you can tune them for your product. The example's Settings tab shows the defaults the native apps use.

## Contact

<div align="left">
<a target="_blank" href="mailto:info@faceplugin.com"><img src="https://img.shields.io/badge/email-info@faceplugin.com-blue.svg?logo=gmail" alt="faceplugin.com"></a>&emsp;
<a target="_blank" href="https://t.me/FacePluginSupport"><img src="https://img.shields.io/badge/telegram-@FacePluginSupport-blue.svg?logo=telegram" alt="Telegram @FacePluginSupport"></a>&emsp;
<a target="_blank" href="https://wa.me/+14692784822"><img src="https://img.shields.io/badge/whatsapp-faceplugin-blue.svg?logo=whatsapp" alt="faceplugin.com"></a>
</div>
