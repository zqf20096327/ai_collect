<div align="center">
  <img src="./icon.png" width="180" height="180" alt="OpenLanguage logo" />
  <h1>OpenLanguage</h1>
  <p><strong>The free and open source conversational language tutor for iOS.</strong></p>
</div>

<p align="center">
  <a href="https://developer.apple.com/ios/"><img src="https://img.shields.io/badge/iOS-iOS%2016%2B-blue.svg" alt="iOS 18+" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" /></a>
</p>

<p align="center">
  <a href="https://apps.apple.com/app/openlanguage/id6774796758"><img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download on the App Store" height="40"></a>
</p>

# Overview

OpenLanguage pairs a capable AI tutor with voice I/O so you can practice speaking and listening the way you actually learn a language — by using it. 

The tutor adapts to your level, corrects you naturally mid-conversation, and never gets tired of your questions. Pre-made conversation topics for every level make jumping in a breeze.

- **Free and Open Source**: No accounts required, no subscription.
- **Bring Your Own Keys**: Plug in your own API key from OpenAI, Anthropic, or any compatible provider. You pick the model and pay only for what you use.
- **Zero Telemetry**: No analytics. No tracking. Your conversations stay on your device and between you and whichever API provider you configure.
- **Voice I/O**: Uses iOS's built in voice recognition and speech to text for free, on-device voice I/O.

OpenLanguage is built with Expo / React Native, using only native SwiftUI components via [expo-ui](https://docs.expo.dev/versions/latest/sdk/ui/).

## Supported AI Providers

AI APIs currently supported:
- OpenAI / OpenAI compatible
- Anthropic
- OpenRouter
- OpenResponses
- DeepSeek
- Fireworks
- Groq
- Mistral
- Moonshot
- TogetherAI
- Zhipu AI (Z.AI)
- MiniMax

Under the hood we use [ai-sdk](https://ai-sdk.dev/), so extra providers are easily added.

# Screenshots

![Screenshot 1](./screenshot-1.png "screenshot-1") ![Screenshot 2](screenshot-2.png "screenshot-2") ![Screenshot 3](screenshot-3.png "screenshot-3")

# Development

## Pre-requisites
- macOS
- pnpm
- Xcode

## Get Started
```shell
# Install dependencies
pnpm install

# Run dev server & start iOS simulator
pnpm ios
```

# Contributing

Issues and pull requests are welcome.

# License

OpenLanguage is available under the [MIT License](LICENSE).