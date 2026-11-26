<div align="center">
<img alt="FacePlugin" src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/brand/logo.png" width="400"/>
</div>

#### 🌐 Company Site - [Here](https://faceplugin.com)
#### 🤗 Hugging Face - [Here](https://huggingface.co/FacePlugin-Ltd)
#### 🛟 Help Center - [Here](https://doc.faceplugin.com)
#### 🐳 Docker Hub - [Here](https://hub.docker.com/r/faceplugin/face-recognition)

# FacePlugin Face Recognition + 1:N Identification + Liveness Detection — React Native (Fully On-Premise)

Jump: [Quick start](#quick-start) · [Get the runtimes](#get-the-runtimes) · [Run the demo](#run-the-demo) · [SDK License](#sdk-license) · [Setup on your own app](#setup-on-your-own-app) · [About SDK](#about-sdk)

## Quick start

- [ ] Clone [FaceRecognition-LivenessDetection-ReactNative](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-ReactNative)
- [ ] `yarn`, then `cd example && yarn`
- [ ] Place the native runtimes — [Get the runtimes](#get-the-runtimes)
- [ ] `python run_android` (or `python run_ios` on macOS) with a **physical** phone connected
- [ ] The demo ships with license keys for `com.faceplugin.facerecognitionsdk` (Android) and `com.faceplugin.facerecognition.app` (iOS)

## Introduction

FacePlugin **Face Recognition + Liveness Detection for React Native** runs face recognition and passive liveness entirely on the device. Nothing is sent to a FacePlugin server, which is what banking, access control, and privacy-first identity apps need. Its headline capability is **1:N identification**: enroll your people once, then ask *who is this?* of a camera frame or a photo and get a ranked candidate list back — searched against the templates your app keeps on the device, so no face ever leaves it.

This repository is the whole product: the **React Native plugin** (`face-recognition-sdk`), the native bridges for Android and iOS, and an **example app** built from that same plugin — so what you read here is what the demo runs.

The engine binaries are the same ones the native apps use, so you get identical scores on both platforms.

### Main Functionalities

| Feature | API |
| ------- | --- |
| **1:N identification** on a live camera feed | `startVideoWorker` · `syncVideoWorkerDatabase` · `addVideoWorkerFrame` |
| Face detection (bounding box, landmarks, pose, attributes) | `faceDetection` |
| Passive liveness (anti-spoofing) | `faceDetection` with liveness, live `VideoWorker` events |
| Face image quality | `quality` |
| Face template extraction and similarity | `templateExtraction` · `similarity` · `similarityMany` |
| Face crop for enrollment | `cropFace` |
| License and engine lifecycle | `getMachineCode` · `setActivation` · `init` · `getLicenseStatus` |

### Product List

| Platform | Repository |
| -------- | ---------- |
| Android | [FaceRecognition-LivenessDetection-Android](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android) |
| iOS | [FaceRecognition-LivenessDetection-iOS](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-iOS) |
| **React Native** | **[FaceRecognition-LivenessDetection-ReactNative](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-ReactNative)** **(this repo)** |
| Flutter | [FaceRecognition-LivenessDetection-Flutter](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter) |
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
| 1 | Node 18+, Yarn, and a React Native toolchain (Android Studio, and Xcode 15+ on macOS) |
| 2 | The Android AAR and the iOS frameworks — see [Get the runtimes](#get-the-runtimes) |
| 3 | A **physical** phone. Emulators and the simulator have no usable camera for liveness |
| 4 | A license key for your ids ([contact us](#contact)). The demo already has keys for the ids above |

### System requirements

| Item | Minimum | Recommended |
| ---- | ------- | ----------- |
| Android | `minSdk 24`, `arm64-v8a` | Android 10 or newer |
| iOS | 15.0, arm64 device | iPhone 11 or newer |
| Node | 18 | 20 |
| RAM (device) | 4 GB | 6 GB or more |

## Get the runtimes

The native binaries are too large for GitHub, so they are published on the **Android** and **iOS** release pages. Both platforms use the same engine, so take them from the same release.

### Android — `facerecognitionsdk.aar`

**[Download from the Android release](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android/releases/tag/latest)**

| Where | Path |
| ----- | ---- |
| The plugin | `android/libs/facerecognitionsdk.aar` |
| The example app | `example/android/libfacesdk/facerecognitionsdk.aar` |

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

Then run `pod install` in `example/ios`.

> Enrolled people are stored **locally** by the example app. The release holds the native runtime only, never a person gallery.

## Run the demo

```bash
git clone https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-ReactNative.git
cd FaceRecognition-LivenessDetection-ReactNative
yarn
cd example && yarn
# place the AAR and the iOS frameworks — see above
python run_android
python run_ios          # macOS
```

From `example` you can also use `yarn android` / `yarn ios --device`.

Keep the demo ids so the included license activates: Android `applicationId` `com.faceplugin.facerecognitionsdk`, iOS bundle id `com.faceplugin.facerecognition.app`.

The example app has five tabs:

| Tab | What it shows |
| --- | ------------- |
| **Identify** | Live 1:N against everyone enrolled, with liveness, then a ranked result |
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
| The keys | [`example/src/license.ts`](example/src/license.ts) | `ANDROID_LICENSE`, `IOS_LICENSE` |
| Where they are used | [`example/src/engine.ts`](example/src/engine.ts) | `setActivation(demoLicense())` |
| The ids they are bound to | [`example/src/license.ts`](example/src/license.ts) | `ANDROID_APPLICATION_ID`, `IOS_BUNDLE_ID` |

Find this, and put your key in place of the demo one:

```ts
const ANDROID_LICENSE =
  'FP1.RlBMMQMAAQDJx5NBpyjuxrTSuz8MAgAA…';
```

Rebuild the native app — a JavaScript reload is not enough, because activation happens once at start-up. `demoLicense()` picks the Android or iOS key at runtime, so set both.

### How to get a key

[Contact us](#contact) with the id you will ship. If we ask for a machine code, `getMachineCode()` returns it. After activation, `getLicenseStatus()` reports what the key unlocks.

### License capabilities (Recognition + Liveness)

| Capability | Meaning |
| ---------- | ------- |
| **Recognition** | Detection, attributes, quality, templates, 1:1 similarity, and 1:N identification |
| **Liveness** | Passive anti-spoofing on camera frames and stills |

## Setup on your own app

You integrate from **this repository** — there is no npm package to install, and no package-server dependency to add.

1. Clone this repository next to your app:

   ```bash
   git clone https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-ReactNative.git
   ```

2. Add the local plugin to your app's `package.json`, pointing at that clone:

   ```json
   {
     "dependencies": {
       "face-recognition-sdk": "file:../FaceRecognition-LivenessDetection-ReactNative"
     }
   }
   ```

   Then `yarn install` (or `npm install`).

3. Copy the native runtimes into the plugin folder — [Get the runtimes](#get-the-runtimes):

   - Android AAR → `<plugin>/android/libs/facerecognitionsdk.aar`
   - iOS frameworks → `<plugin>/ios/Frameworks/`, then `pod install` in your app's `ios/`

4. Set **your** `applicationId` / bundle id, and request a license for those ids.
5. Add camera and photo permissions (see the example's `AndroidManifest.xml` and `Info.plist`).
6. For the capture coach (`FaceCapture`), also install the peers `react-native-vision-camera` and `react-native-svg`.

You do **not** need the `example/` app. Full wiring and result JSON: [https://doc.faceplugin.com](https://doc.faceplugin.com)

## About SDK

Activate once at start-up, then call the engine. `SDK_SUCCESS` (`0`) means success.

**1. Activate and initialize**

```ts
import {
  getMachineCode,
  setActivation,
  init,
  getLicenseStatus,
  lastLicenseError,
  SDK_SUCCESS,
} from 'face-recognition-sdk';

const machine = await getMachineCode();          // send this when you request a key
const code = await setActivation('FP1.…');       // bound to your applicationId / bundle id
if (code !== SDK_SUCCESS) throw new Error(await lastLicenseError());
await init();
const status = await getLicenseStatus();
```

**2. Read a face, and enroll it**

```ts
import { faceDetection, templateExtraction, cropFace, similarity } from 'face-recognition-sdk';

const faces = await faceDetection(imagePath);
if (faces.length === 1) {
  const template = await templateExtraction(imagePath, faces[0]);
  const crop = await cropFace(imagePath, faces[0]);
  // store the template and the crop in YOUR database
}

const score = await similarity(templateA, templateB);   // 1:1
```

**3. Live 1:N identification**

```ts
import {
  startVideoWorker,
  syncVideoWorkerDatabase,
  addVideoWorkerFrame,
  stopVideoWorker,
  subscribeVideoWorker,
} from 'face-recognition-sdk';

await startVideoWorker({ matchThreshold: 0.67 });
await syncVideoWorkerDatabase(templates);
const off = subscribeVideoWorker(event => { /* match, liveness, tracking */ });
// feed camera frames with addVideoWorkerFrame(...)
await stopVideoWorker();
```

**4. Status codes**

| Code | Constant | Meaning |
| ---- | -------- | ------- |
| 0 | `SDK_SUCCESS` | Activate / init OK |
| 1 | `SDK_LICENSE_INVALID` | Invalid license |
| 2 | `SDK_LICENSE_EXPIRED` | Expired license |
| 3 | `SDK_NOT_ACTIVATED` | Not activated |

Thresholds (match, liveness, pose, eye-close) are parameters you pass from JavaScript, so you can tune them for your product. The example's Settings tab shows the defaults the native apps use.

## Contact

<div align="left">
<a target="_blank" href="mailto:info@faceplugin.com"><img src="https://img.shields.io/badge/email-info@faceplugin.com-blue.svg?logo=gmail" alt="faceplugin.com"></a>&emsp;
<a target="_blank" href="https://t.me/FacePluginSupport"><img src="https://img.shields.io/badge/telegram-@FacePluginSupport-blue.svg?logo=telegram" alt="Telegram @FacePluginSupport"></a>&emsp;
<a target="_blank" href="https://wa.me/+14692784822"><img src="https://img.shields.io/badge/whatsapp-faceplugin-blue.svg?logo=whatsapp" alt="faceplugin.com"></a>
</div>
