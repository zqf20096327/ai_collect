# SwiftOpenAI
<img width="1090" alt="repoOpenAI" src="https://github.com/jamesrochabrun/SwiftOpenAI/assets/5378604/51bc5736-a32f-4a9f-922e-209d950e28f7">

![iOS 15+](https://img.shields.io/badge/iOS-15%2B-blue.svg)
![macOS 13+](https://img.shields.io/badge/macOS-13%2B-blue.svg)
![watchOS 9+](https://img.shields.io/badge/watchOS-9%2B-blue.svg)
![Linux](https://img.shields.io/badge/Linux-blue.svg)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![swift-version](https://img.shields.io/badge/swift-5.9-brightgreen.svg)](https://github.com/apple/swift)
[![swiftui-version](https://img.shields.io/badge/swiftui-brightgreen)](https://developer.apple.com/documentation/swiftui)
[![xcode-version](https://img.shields.io/badge/xcode-15%20-brightgreen)](https://developer.apple.com/xcode/)
[![swift-package-manager](https://img.shields.io/badge/package%20manager-compatible-brightgreen.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNjJweCIgaGVpZ2h0PSI0OXB4IiB2aWV3Qm94PSIwIDAgNjIgNDkiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDYzLjEgKDkyNDUyKSAtIGh0dHBzOi8vc2tldGNoLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cDwvdGl0bGU+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxnIGlkPSJQYWdlLTEiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJHcm91cCIgZmlsbC1ydWxlPSJub256ZXJvIj4KICAgICAgICAgICAgPHBvbHlnb24gaWQ9IlBhdGgiIGZpbGw9IiNEQkI1NTEiIHBvaW50cz0iNTEuMzEwMzQ0OCAwIDEwLjY4OTY1NTIgMCAwIDEzLjUxNzI0MTQgMCA0OSA2MiA0OSA2MiAxMy41MTcyNDE0Ij48L3BvbHlnb24+CiAgICAgICAgICAgIDxwb2x5Z29uIGlkPSJQYXRoIiBmaWxsPSIjRjdFM0FGIiBwb2ludHM9IjI3IDI1IDMxIDI1IDM1IDI1IDM3IDI1IDM3IDE0IDI1IDE0IDI1IDI1Ij48L3BvbHlnb24+CiAgICAgICAgICAgIDxwb2x5Z29uIGlkPSJQYXRoIiBmaWxsPSIjRUZDNzVFIiBwb2ludHM9IjEwLjY4OTY1NTIgMCAwIDE0IDYyIDE0IDUxLjMxMDM0NDggMCI+PC9wb2x5Z29uPgogICAgICAgICAgICA8cG9seWdvbiBpZD0iUmVjdGFuZ2xlIiBmaWxsPSIjRjdFM0FGIiBwb2ludHM9IjI3IDAgMzUgMCAzNyAxNCAyNSAxNCI+PC9wb2x5Z29uPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+)](https://github.com/apple/swift-package-manager)
[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-048754?logo=buymeacoffee)](https://buymeacoffee.com/jamesrochabrun)

An open-source Swift package designed for effortless interaction with OpenAI's public API. 

🚀 Now also available as [CLI](https://github.com/jamesrochabrun/SwiftOpenAICLI) and also as [MCP](https://github.com/jamesrochabrun/SwiftOpenAIMCP)

## Table of Contents
- [Description](#description)
- [Getting an API Key](#getting-an-api-key)
- [Installation](#installation)
- [Compatibility](#compatibility)
- [Usage](#usage)
- [Collaboration](#collaboration)

## Description

`SwiftOpenAI` is an open-source Swift package that streamlines interactions with **all** OpenAI's API endpoints, now with added support for Azure, AIProxy, Assistant stream APIs, and the new **Realtime API** for low-latency bidirectional voice conversations.

### OpenAI ENDPOINTS

- [Audio](#audio)
   - [Transcriptions](#audio-transcriptions)
   - [Translations](#audio-translations)
   - [Speech](#audio-Speech)
   - [Realtime](#audio-realtime)
- [Chat](#chat)
   - [Function Calling](#function-calling)
   - [Structured Outputs](#structured-outputs)
   - [Vision](#vision)
- [Response](#response)
   - [Streaming Responses](#streaming-responses)
- [Embeddings](#embeddings)
- [Fine-tuning](#fine-tuning)
- [Batch](#batch)
- [Files](#files)
- [Images](#images)
- [Models](#models)
- [Moderations](#moderations)

### **BETA**
- [Assistants](#assistants)
   - [Assistants File Object](#assistants-file-object)
- [Threads](#threads)
- [Messages](#messages)
   - [Message File Object](#message-file-object)
- [Runs](#runs)
   - [Run Step object](#run-step-object)
   - [Run Step details](#run-step-details)
- [Assistants Streaming](#assistants-streaming)
   - [Message Delta Object](#message-delta-object)
   - [Run Step Delta Object](#run-step-delta-object)
- [Vector Stores](#vector-stores)
   - [Vector store File](#vector-store-file)
   - [Vector store File Batch](#vector-store-file-batch)
- [Agents](#agents)

## Getting an API Key

⚠️ **Important**

To interact with OpenAI services, you'll need an API key. Follow these steps to obtain one:

1. Visit [OpenAI](https://www.openai.com/).
2. Sign up for an [account](https://platform.openai.com/signup) or [log in](https://platform.openai.com/login) if you already have one.
3. Navigate to the [API key page](https://platform.openai.com/account/api-keys) and follow the instructions to generate a new API key.

For more information, consult OpenAI's [official documentation](https://platform.openai.com/docs/).

⚠️  Please take precautions to keep your API key secure per [OpenAI's guidance](https://platform.openai.com/docs/api-reference/authentication):

> Remember that your API key is a secret! Do not share it with others or expose
> it in any client-side code (browsers, apps). Production requests must be
> routed through your backend server where your API key can be securely
> loaded from an environment variable or key management service.

SwiftOpenAI has built-in support for AIProxy, which is a backend for AI apps, to satisfy this requirement.
To configure AIProxy, see the instructions [here](#aiproxy).


## Installation

### Swift Package Manager

1. Open your Swift project in Xcode.
2. Go to `File` ->  `Add Package Dependency`.
3. In the search bar, enter [this URL](https://github.com/jamesrochabrun/SwiftOpenAI).
4. Choose the version you'd like to install (see the note below).
5. Click `Add Package`.

Note: Xcode has a quirk where it defaults an SPM package's upper limit to 2.0.0. This package is beyond that
limit, so you should not accept the defaults that Xcode proposes. Instead, enter the lower bound of the
[release version](https://github.com/jamesrochabrun/SwiftOpenAI/releases) that you'd like to support, and then
tab out of the input box for Xcode to adjust the upper bound. Alternatively, you may select `branch` -> `main`
to stay on the bleeding edge.

## Compatibility

### Platform Support

SwiftOpenAI supports both Apple platforms and Linux.
- **Apple platforms** include iOS 15+, macOS 13+, and watchOS 9+.
- **Linux**: SwiftOpenAI on Linux uses AsyncHTTPClient to work around URLSession bugs in Apple's Foundation framework, and can be used with the [Vapor](https://vapor.codes/) server framework.

### OpenAI-Compatible Providers

SwiftOpenAI supports various providers that are OpenAI-compatible, including but not limited to:

- [Azure OpenAI](#azure-openai)
- [Anthropic](#anthropic)
- [Gemini](#gemini)
- [Ollama](#ollama)
- [Groq](#groq)
- [xAI](#xai)
- [OpenRouter](#openRouter)
- [Tuning Engines](#tuning-engines)
- [DeepSeek](#deepseek)
- [AIProxy](#aiproxy)

Check OpenAIServiceFactory for convenience initializers that you can use to provide custom URLs.

## Usage

To use SwiftOpenAI in your project, first import the package:

```swift
import SwiftOpenAI
```

Then, initialize the service using your OpenAI API key:

```swift
let apiKey = "your_openai_api_key_here"
let service = OpenAIServiceFactory.service(apiKey: apiKey)
```

You can optionally specify an organization name if needed.

```swift
let apiKey = "your_openai_api_key_here"
let oganizationID = "your_organixation_id"
let service = OpenAIServiceFactory.service(apiKey: apiKey, organizationID: oganizationID)
```

https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/1408259-timeoutintervalforrequest

For reasoning models, ensure that you extend the timeoutIntervalForRequest in the URL session configuration to a higher value. The default is 60 seconds, which may be insufficient, as requests to reasoning models can take longer to process and respond.

To configure it:

```swift
let apiKey = "your_openai_api_key_here"
let organizationID = "your_organization_id"
let session = URLSession.shared
session.configuration.timeoutIntervalForRequest = 360 // e.g., 360 seconds or more.
let httpClient = URLSessionHTTPClientAdapter(urlSession: session)
let service = OpenAIServiceFactory.service(apiKey: apiKey, organizationID: organizationID, httpClient: httpClient)
```

That's all you need to begin accessing the full range of OpenAI endpoints.

### How to get the status code of network errors

You may want to build UI around the type of error that the API returns.
For example, a `429` means that your requests are being rate limited.
The `APIError` type has a case `responseUnsuccessful` with two associated values: a `description` and `statusCode`.
Here is a usage example using the chat completion API:

```swift
let service = OpenAIServiceFactory.service(apiKey: apiKey)
let parameters = ChatCompletionParameters(messages: [.init(role: .user, content: .text("hello world"))],
                                          model: .gpt4o)
do {
   let choices = try await service.startChat(parameters: parameters).choices
   // Work with choices
} catch APIError.responseUnsuccessful(let description, let statusCode) {
   print("Network error with status code: \(statusCode) and description: \(description)")
} catch {
   print(error.localizedDescription)
}
```


### Audio

### Audio Transcriptions
Parameters
```swift
public struct AudioTranscriptionParameters: Encodable {
   
   /// The name of the file asset is not documented in OpenAI's official documentation; however, it is essential for constructing the multipart request.
   let fileName: String
   /// The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
   let file: Data
   /// ID of the model to use. Only whisper-1 is currently available.
   let model: String
   /// The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.
   let language: String?
   /// An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text/prompting) should match the audio language.
   let prompt: String?
   /// The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt. Defaults to json
   let responseFormat: String?
   /// The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit. Defaults to 0
   let temperature: Double?
   
   public enum Model {
      case whisperOne 
      case custom(model: String)
   }
   
   public init(
      fileName: String,
      file: Data,
      model: Model = .whisperOne,
      prompt: String? = nil,
      responseFormat: String? = nil,
      temperature: Double? = nil,
      language: String? = nil)
   {
      self.fileName = fileName
      self.file = file
      self.model = model.rawValue
      self.prompt = prompt
      self.responseFormat = responseFormat
      self.temperature = temperature
      self.language = language
   }
}
```

Response
```swift
public struct AudioObject: Decodable {
   
   /// The transcribed text if the request uses the `transcriptions` API, or the translated text if the request uses the `translations` endpoint.
   public let text: String
}
```

Usage
```swift
let fileName = "narcos.m4a"
let data = Data(contentsOfURL:_) // Data retrieved from the file named "narcos.m4a".
let parameters = AudioTranscriptionParameters(fileName: fileName, file: data) // **Important**: in the file name always provide the file extension.
let audioObject =  try await service.createTranscription(parameters: parameters)
```
### Audio Translations
Parameters
```swift
public struct AudioTranslationParameters: Encodable {
   
   /// The name of the file asset is not documented in OpenAI's official documentation; however, it is essential for constructing the multipart request.
   let fileName: String
   /// The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
   let file: Data
   /// ID of the model to use. Only whisper-1 is currently available.
   let model: String
   /// An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text/prompting) should match the audio language.
   let prompt: String?
   /// The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt. Defaults to json
   let responseFormat: String?
   /// The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit. Defaults to 0
   let temperature: Double?
   
   public enum Model {
      case whisperOne 
      case custom(model: String)
   }
   
   public init(
      fileName: String,
      file: Data,
      model: Model = .whisperOne,
      prompt: String? = nil,
      responseFormat: String? = nil,
      temperature: Double? = nil)
   {
      self.fileName = fileName
      self.file = file
      self.model = model.rawValue
      self.prompt = prompt
      self.responseFormat = responseFormat
      self.temperature = temperature
   }
}
```

Response
```swift
public struct AudioObject: Decodable {
   
   /// The transcribed text if the request uses the `transcriptions` API, or the translated text if the request uses the `translations` endpoint.
   public let text: String
}
```

Usage
```swift
let fileName = "german.m4a"
let data = Data(contentsOfURL:_) // Data retrieved from the file named "german.m4a".
let parameters = AudioTranslationParameters(fileName: fileName, file: data) // **Important**: in the file name always provide the file extension.
let audioObject = try await service.createTranslation(parameters: parameters)
```

### Audio Speech
Parameters
```swift
/// [Generates audio from the input text.](https://platform.openai.com/docs/api-reference/audio/createSpeech)
public struct AudioSpeechParameters: Encodable {

   /// One of the available [TTS models](https://platform.openai.com/docs/models/tts): tts-1 or tts-1-hd
   let model: String
   /// The text to generate audio for. The maximum length is 4096 characters.
   let input: String
   /// The voice to use when generating the audio. Supported voices are alloy, echo, fable, onyx, nova, and shimmer. Previews of the voices are available in the [Text to speech guide.](https://platform.openai.com/docs/guides/text-to-speech/voice-options)
   let voice: String
   /// Defaults to mp3, The format to audio in. Supported formats are mp3, opus, aac, and flac.
   let responseFormat: String?
   /// Defaults to 1,  The speed of the generated audio. Select a value from 0.25 to 4.0. 1.0 is the default.
   let speed: Double?

   public enum TTSModel: String {
      case tts1 = "tts-1"
      case tts1HD = "tts-1-hd"
   }

   public enum Voice: String {
      case alloy
      case echo
      case fable
      case onyx
      case nova
      case shimmer
   }

   public enum ResponseFormat: String {
      case mp3
      case opus
      case aac
      case flac
   }
   
   public init(
      model: TTSModel,
      input: String,
      voice: Voice,
      responseFormat: ResponseFormat? = nil,
      speed: Double? = nil)
   {
       self.model = model.rawValue
       self.input = input
       self.voice = voice.rawValue
       self.responseFormat = responseFormat?.rawValue
       self.speed = speed
   }
}
```

Response
```swift
/// The [audio speech](https://platform.openai.com/docs/api-reference/audio/createSpeech) response.
public struct AudioSpeechObject: Decodable {

   /// The audio file content data.
   public let output: Data
}
```

Usage
```swift
let prompt = "Hello, how are you today?"
let parameters = AudioSpeechParameters(model: .tts1, input: prompt, voice: .shimmer)
let audioObjectData = try await service.createSpeech(parameters: parameters).output
playAudio(from: audioObjectData)

// Play data
 private func playAudio(from data: Data) {
       do {
           // Initialize the audio player with the data
           audioPlayer = try AVAudioPlayer(data: data)
           audioPlayer?.prepareToPlay()
           audioPlayer?.play()
       } catch {
           // Handle errors
           print("Error playing audio: \(error.localizedDescription)")
       }
   }
```

### Audio Realtime

The [Realtime API](https://platform.openai.com/docs/api-reference/realtime) enables bidirectional voice conversations with OpenAI's models using WebSockets and low-latency audio streaming. For voice agents, the current recommended model is `gpt-realtime-2.1`; the API supports audio-to-audio interaction, voice activity detection, transcription, function tools, and MCP tools.

**Platform Requirements:** iOS 15+, macOS 13+, watchOS 9+. Requires AVFoundation (not available on Linux).

**Permissions Required:**
- Add `NSMicrophoneUsageDescription` to your Info.plist
- On macOS: Enable sandbox entitlements for microphone access and outgoing network connections

Parameters
```swift
/// Configuration for creating a realtime session
public struct OpenAIRealtimeSessionConfiguration: Encodable, Sendable {

   /// The input audio format. Options: .pcm16, .g711Ulaw, .g711Alaw. Encodes to GA audio format objects.
   let inputAudioFormat: AudioFormat?
   /// Configuration for input audio transcription.
   let inputAudioTranscription: InputAudioTranscription?
   /// Additional fields to include in server outputs.
   let include: [String]?
   /// System instructions for the model. Recommended default provided
   let instructions: String?
   /// Maximum tokens for response output. Can be .int(Int) or .infinite
   let maxResponseOutputTokens: MaxResponseOutputTokens?
   /// Output modalities: [.audio] or [.text]. GA Realtime does not request both at once.
   let modalities: [Modality]?
   /// The model used when creating client secrets.
   let model: String?
   /// The output audio format. Options: .pcm16, .g711Ulaw, .g711Alaw.
   let outputAudioFormat: AudioFormat?
   /// Whether the model may call multiple tools in parallel.
   let parallelToolCalls: Bool?
   /// Reasoning effort for reasoning-capable Realtime models.
   let reasoning: ReasoningConfiguration?
   /// Audio playback speed. Range: 0.25 to 1.5. Default is 1.0
   let speed: Double?
   /// Legacy beta field. Not encoded for GA Realtime requests.
   let temperature: Double?
   /// Array of tools/functions available for the model to call
   let tools: [Tool]?
   /// Tool selection mode: .none, .auto, .required, or .specific(functionName: String)
   let toolChoice: ToolChoice?
   /// Voice activity detection configuration. Options: .serverVAD or .semanticVAD
   let turnDetection: TurnDetection?
   /// The voice to use. Built-ins include "alloy", "ash", "ballad", "coral", "echo", "sage", "shimmer", "verse", "marin", and "cedar".
   let voice: String?

   /// Available audio formats
   public enum AudioFormat: String, Encodable, Sendable {
      case pcm16
      case g711Ulaw = "g711_ulaw"
      case g711Alaw = "g711_alaw"
   }

   /// Output modalities
   public enum Modality: String, Encodable, Sendable {
      case audio
      case text
   }

   /// Turn detection configuration
   public struct TurnDetection: Encodable, Sendable {
      /// Server-based VAD with customizable timing
      public static func serverVAD(
         prefixPaddingMs: Int = 300,
         silenceDurationMs: Int = 500,
         threshold: Double = 0.5
      ) -> TurnDetection

      /// Semantic VAD with eagerness level
      public static func semanticVAD(eagerness: Eagerness = .medium) -> TurnDetection

      public enum Eagerness: String, Encodable, Sendable {
         case low, medium, high
      }
   }
}
```

Response
```swift
/// Messages received from the realtime API
public enum OpenAIRealtimeMessage: Sendable {
   case error(String?)                    // Error occurred
   case disconnected(String?)             // WebSocket closed unexpectedly
   case sessionCreated                    // Session successfully created
   case sessionUpdated                    // Configuration updated
   case responseCreated(responseID: String?)
   case responseAudioDelta(itemID: String?, responseID: String?, delta: String)
   case inputAudioBufferSpeechStarted(itemID: String?, audioStartMS: Int?)
   case responseFunctionCallArgumentsDone(name: String, arguments: String, callID: String, itemID: String?, responseID: String?)
   case responseTranscriptDelta(itemID: String?, responseID: String?, delta: String)
   case responseTranscriptDone(itemID: String?, responseID: String?, transcript: String)
   case inputAudioBufferTranscript(String)           // User audio transcript
   case inputAudioTranscriptionDelta(itemID: String?, delta: String)
   case inputAudioTranscriptionCompleted(itemID: String?, transcript: String)
}
```

Supporting Types
```swift
/// Manages microphone input and audio playback for realtime conversations.
/// Full-duplex mode shares one voice-processing graph for capture, playback, and echo cancellation.
@RealtimeActor
public final class AudioController {

   /// Initialize with specified modes
   /// - Parameter modes: Array of .record (for microphone) and/or .playback (for audio output)
   public init(modes: [Mode]) async throws

   public enum Mode {
      case record   // Enable microphone streaming
      case playback // Enable audio playback
   }

   /// Installs the microphone tap, starts the shared audio engine, and returns its buffer stream
   /// - Throws: OpenAIError if .record mode wasn't enabled during initialization
   public func micStream() throws -> AsyncStream<AVAudioPCMBuffer>

   /// Plays base64-encoded PCM16 audio from the model
   /// - Parameter base64String: Base64-encoded PCM16 audio data
   public func playPCM16Audio(base64String: String, itemID: String? = nil)

   /// Interrupts playback and returns the heard duration of the current item
   public func interruptPlayback() -> Int?

   /// Waits until all currently queued audio buffers have played
   public func waitUntilPlaybackFinishes() async

   /// Stops all audio operations
   public func stop()
}

/// Utility for encoding audio buffers to base64
public enum AudioUtils {
   /// Converts AVAudioPCMBuffer to base64 string for transmission
   public static func base64EncodeAudioPCMBuffer(from buffer: AVAudioPCMBuffer) -> String?

   /// Checks if headphones are connected
   public static var headphonesConnected: Bool
}
```

Usage
```swift
// 1. Create session configuration
let configuration = OpenAIRealtimeSessionConfiguration(
   inputAudioFormat: .pcm16,
   inputAudioTranscription: .init(model: Model.gptRealtimeWhisper.value, delay: .low, language: "en"),
   instructions: "You are a helpful AI assistant. Be concise and friendly.",
   maxResponseOutputTokens: .int(4096),
   modalities: [.audio],
   outputAudioFormat: .pcm16,
   parallelToolCalls: true,
   reasoning: .init(effort: .low),
   turnDetection: .init(type: .semanticVAD(eagerness: .auto, createResponse: true, interruptResponse: true)),
   voice: "marin"
)

// 2. Create realtime session
let session = try await service.realtimeSession(
   model: Model.gptRealtime21.value,
   configuration: configuration
)

// 3. Initialize audio controller for recording and playback
let audioController = try await AudioController(modes: [.record, .playback])
var isSessionReady = false
var currentAudioItemID: String?
var pendingToolResponseID: String?

// 4. Handle incoming messages from OpenAI
Task {
   for await message in session.receiver {
      switch message {
      case .sessionUpdated:
         isSessionReady = true

      case .responseAudioDelta(let itemID, _, let audio):
         currentAudioItemID = itemID
         audioController.playPCM16Audio(base64String: audio, itemID: itemID)

      case .inputAudioBufferSpeechStarted:
         if
            let currentAudioItemID,
            let audioEndMS = audioController.interruptPlayback()
         {
            await session.sendMessage(OpenAIRealtimeConversationItemTruncate(
               itemID: currentAudioItemID,
               audioEndMS: audioEndMS))
         }
         currentAudioItemID = nil

      case .responseTranscriptDelta(_, _, let text):
         // Display partial model transcript
         print("Model (partial): \(text)")

      case .responseTranscriptDone(_, _, let text):
         // Display complete model transcript
         print("Model: \(text)")

      case .inputAudioTranscriptionCompleted(_, let text):
         // Display user's transcribed speech
         print("User: \(text)")

      case .responseFunctionCallArgumentsDone(let name, let args, let callId, _, let responseID):
         // Handle function call from model
         print("Function call: \(name) with args: \(args)")
         let result = executeFunction(name: name, arguments: args)
         await session.sendMessage(OpenAIRealtimeFunctionCallOutput(callID: callId, output: result))
         pendingToolResponseID = responseID

      case .responseDone(let responseID, let status, _):
         if pendingToolResponseID == responseID {
            pendingToolResponseID = nil
            if status == "completed" {
               await session.sendMessage(OpenAIRealtimeResponseCreate())
            }
         }

      case .error(let error):
         print("Error: \(error ?? "Unknown error")")

      default:
         break
      }
   }
}

// 5. Stream microphone audio to OpenAI
Task {
   do {
      for try await buffer in audioController.micStream() {
         guard isSessionReady else { continue }
         // Encode audio buffer to base64
         guard let base64Audio = AudioUtils.base64EncodeAudioPCMBuffer(from: buffer) else {
            continue
         }

         // Send audio to OpenAI
         try await session.sendMessage(
            OpenAIRealtimeInputAudioBufferAppend(audio: base64Audio)
         )
      }
   } catch {
      print("Microphone error: \(error)")
   }
}

// 6. Manually trigger a response (optional - usually VAD handles this)
try await session.sendMessage(
   OpenAIRealtimeResponseCreate()
)

// 7. Update session configuration mid-conversation (optional)
let newConfig = OpenAIRealtimeSessionConfiguration(
   instructions: "Be even more concise.",
   toolChoice: .auto
)
try await session.sendMessage(
   OpenAIRealtimeSessionUpdate(sessionConfig: newConfig)
)

// 8. Cleanup when done
audioController.stop()
session.disconnect()
```

Function Calling
```swift
// Define tools in configuration
let tools: [OpenAIRealtimeSessionConfiguration.RealtimeTool] = [
   .function(.init(
      name: "get_weather",
      description: "Get the current weather in a location",
      parameters: [
         "type": "object",
         "properties": [
            "location": [
               "type": "string",
               "description": "City name, e.g. San Francisco"
            ]
         ],
         "required": ["location"]
      ]
   ))
]

let config = OpenAIRealtimeSessionConfiguration(
   voice: "alloy",
   tools: tools,
   toolChoice: .auto
)

var pendingToolResponseID: String?

// Handle function calls in message receiver
case .responseFunctionCallArgumentsDone(let name, let args, let callId, _, let responseID):
   if name == "get_weather" {
      // Parse arguments and execute function
      let result = getWeather(arguments: args)

      // Send result back to model
      await session.sendMessage(OpenAIRealtimeFunctionCallOutput(callID: callId, output: result))
      pendingToolResponseID = responseID
   }

case .responseDone(let responseID, let status, _):
   if pendingToolResponseID == responseID {
      pendingToolResponseID = nil
      if status == "completed" {
         await session.sendMessage(OpenAIRealtimeResponseCreate())
      }
   }
```

Advanced Features
- **Voice Activity Detection (VAD):** Choose between server-based VAD (with configurable timing) or semantic VAD (with eagerness levels)
- **Transcription:** Enable input transcription with `gpt-realtime-whisper` or the supported transcription models
- **Session Updates:** Change voice, instructions, or tools mid-conversation without reconnecting
- **Response Triggers:** Manually trigger model responses or rely on automatic VAD
- **Client Secrets:** Use `createRealtimeClientSecret(parameters:)` for ephemeral credentials in WebRTC integrations
- **Full-Duplex Audio:** Record-and-playback controllers share one `AVAudioEngine` voice-processing graph so the microphone stays live for barge-in without treating model playback as user speech

For a complete implementation example, see `Examples/RealtimeExample/RealtimeExample.swift` in the repository.

### Chat
Parameters
```swift
public struct ChatCompletionParameters: Encodable {
   
   /// A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models)
   public var messages: [Message]
   /// ID of the model to use. See the [model endpoint compatibility](https://platform.openai.com/docs/models/how-we-use-your-data) table for details on which models work with the Chat API.
   /// Supports GPT-4, GPT-4o, GPT-5, and other models. For GPT-5 family: .gpt5, .gpt5Mini, .gpt5Nano
   public var model: String
   /// Whether or not to store the output of this chat completion request for use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or [evals](https://platform.openai.com/docs/guides/evals) products.
   /// Defaults to false
   public var store: Bool?
   /// Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. Defaults to 0
   /// [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/gpt/parameter-details)
   public var frequencyPenalty: Double?
   /// Controls how the model responds to function calls. none means the model does not call a function, and responds to the end-user. auto means the model can pick between an end-user or calling a function. Specifying a particular function via {"name": "my_function"} forces the model to call that function. none is the default when no functions are present. auto is the default if functions are present.
   @available(*, deprecated, message: "Deprecated in favor of tool_choice.")
   public var functionCall: FunctionCall?
   /// Controls which (if any) function is called by the model. none means the model will not call a function and instead generates a message. 
   /// auto means the model can pick between generating a message or calling a function. Specifying a particular function via `{"type: "function", "function": {"name": "my_function"}}` forces the model to call that function.
   /// `none` is the default when no functions are present. auto is the default if functions are present.
   public var toolChoice: ToolChoice?
   /// A list of functions the model may generate JSON inputs for.
   @available(*, deprecated, message: "Deprecated in favor of tools.")
   public var functions: [ChatFunction]?
   /// A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for.
   public var tools: [Tool]?
   /// Whether to enable parallel function calling during tool use. Defaults to true.
   public var parallelToolCalls: Bool?
   /// Modify the likelihood of specified tokens appearing in the completion.
   /// Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. Defaults to null.
   public var logitBias: [Int: Double]?
   /// Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the content of message. This option is currently not available on the gpt-4-vision-preview model. Defaults to false.
   public var logprobs: Bool?
   /// An integer between 0 and 5 specifying the number of most likely tokens to return at each token position, each with an associated log probability. logprobs must be set to true if this parameter is used.
   public var topLogprobs: Int?
   /// The maximum number of [tokens](https://platform.openai.com/tokenizer) that can be generated in the chat completion. This value can be used to control [costs](https://openai.com/api/pricing/) for text generated via API.
   /// This value is now deprecated in favor of max_completion_tokens, and is not compatible with [o1 series models](https://platform.openai.com/docs/guides/reasoning)
   public var maxTokens: Int?
   /// An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning)
   public var maCompletionTokens: Int?
   /// How many chat completion choices to generate for each input message. Defaults to 1.
   public var n: Int?
   /// Output types that you would like the model to generate for this request. Most models are capable of generating text, which is the default:
   /// ["text"]
   ///The gpt-4o-audio-preview model can also be used to [generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate both text and audio responses, you can use:
   /// ["text", "audio"]
   public var modalities: [String]?
   /// Parameters for audio output. Required when audio output is requested with modalities: ["audio"]. [Learn more.](https://platform.openai.com/docs/guides/audio)
   public var audio: Audio?
   /// Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. Defaults to 0
   /// [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/gpt/parameter-details)
   public var presencePenalty: Double?
   /// An object specifying the format that the model must output. Used to enable JSON mode.
   /// Setting to `{ type: "json_object" }` enables `JSON` mode, which guarantees the message the model generates is valid JSON.
   ///Important: when using `JSON` mode you must still instruct the model to produce `JSON` yourself via some conversation message, for example via your system message. If you don't do this, the model may generate an unending stream of whitespace until the generation reaches the token limit, which may take a lot of time and give the appearance of a "stuck" request. Also note that the message content may be partial (i.e. cut off) if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.
   public var responseFormat: ResponseFormat?
   /// Specifies the latency tier to use for processing the request. This parameter is relevant for customers subscribed to the scale tier service:
   /// If set to 'auto', the system will utilize scale tier credits until they are exhausted.
   /// If set to 'default', the request will be processed in the shared cluster.
   /// When this parameter is set, the response body will include the service_tier utilized.
   public var serviceTier: String?
   /// This feature is in `Beta`. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
   /// Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.
   public var seed: Int?
   /// Up to 4 sequences where the API will stop generating further tokens. Defaults to null.
   public var stop: [String]?
   /// If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) as they become available, with the stream terminated by a data: [DONE] message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions ).
   /// Defaults to false.
   var stream: Bool? = nil
   /// Options for streaming response. Only set this when you set stream: true
   var streamOptions: StreamOptions?
   /// What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
   /// We generally recommend altering this or `top_p` but not both. Defaults to 1.
   public var temperature: Double?
   /// An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
   /// We generally recommend altering this or `temperature` but not both. Defaults to 1
   public var topP: Double?
   /// A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
   /// [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
   public var user: String?
   
   public struct Message: Encodable {
      
      /// The role of the messages author. One of system, user, assistant, or tool message.
      let role: String
      /// The contents of the message. content is required for all messages, and may be null for assistant messages with function calls.
      let content: ContentType
      /// The name of the author of this message. name is required if role is function, and it should be the name of the function whose response is in the content. May contain a-z, A-Z, 0-9, and underscores, with a maximum length of 64 characters.
      let name: String?
      /// The name and arguments of a function that should be called, as generated by the model.
      @available(*, deprecated, message: "Deprecated and replaced by `tool_calls`")
      let functionCall: FunctionCall?
      /// The tool calls generated by the model, such as function calls.
      let toolCalls: [ToolCall]?
      /// Tool call that this message is responding to.
      let toolCallID: String?
      
      public enum ContentType: Encodable {
         
         case text(String)
         case contentArray([MessageContent])
         
         public func encode(to encoder: Encoder) throws {
            var container = encoder.singleValueContainer()
            switch self {
            case .text(let text):
               try container.encode(text)
            case .contentArray(let contentArray):
               try container.encode(contentArray)
            }
         }
         
         public enum MessageContent: Encodable, Equatable, Hashable {
            
            case text(String)
            case imageUrl(ImageDetail)
            
            public struct ImageDetail: Encodable, Equatable, Hashable {
               
               public let url: URL
               public let detail: String?
               
               enum CodingKeys: String, CodingKey {
                  case url
                  case detail
               }
               
               public func encode(to encoder: Encoder) throws {
                  var container = encoder.container(keyedBy: CodingKeys.self)
                  try container.encode(url, forKey: .url)
                  try container.encode(detail, forKey: .detail)
               }
               
               public init(url: URL, detail: String? = nil) {
                  self.url = url
                  self.detail = detail
               }
            }
            
            enum CodingKeys: String, CodingKey {
               case type
               case text
               case imageUrl = "image_url"
            }
            
            public func encode(to encoder: Encoder) throws {
               var container = encoder.container(keyedBy: CodingKeys.self)
               switch self {
               case .text(let text):
                  try container.encode("text", forKey: .type)
                  try container.encode(text, forKey: .text)
               case .imageUrl(let imageDetail):
                  try container.encode("image_url", forKey: .type)
                  try container.encode(imageDetail, forKey: .imageUrl)
               }
            }
            
            public func hash(into hasher: inout Hasher) {
               switch self {
               case .text(let string):
                  hasher.combine(string)
               case .imageUrl(let imageDetail):
                  hasher.combine(imageDetail)
               }
            }
            
            public static func ==(lhs: MessageContent, rhs: MessageContent) -> Bool {
               switch (lhs, rhs) {
               case let (.text(a), .text(b)):
                  return a == b
               case let (.imageUrl(a), .imageUrl(b)):
                  return a == b
               default:
                  return false
               }
            }
         }
      }
      
      public enum Role: String {
         case system // content, role
         case user // content, role
         case assistant // content, role, tool_calls
         case tool // content, role, tool_call_id
      }
      
      enum CodingKeys: String, CodingKey {
         case role
         case content
         case name
         case functionCall = "function_call"
         case toolCalls = "tool_calls"
         case toolCallID = "tool_call_id"
      }
      
      public init(
         role: Role,
         content: ContentType,
         name: String? = nil,
         functionCall: FunctionCall? = nil,
         toolCalls: [ToolCall]? = nil,
         toolCallID: String? = nil)
      {
         self.role = role.rawValue
         self.content = content
         self.name = name
         self.functionCall = functionCall
         self.toolCalls = toolCalls
         self.toolCallID = toolCallID
      }
   }
   
   @available(*, deprecated, message: "Deprecated in favor of ToolChoice.")
   public enum FunctionCall: Encodable, Equatable {
      case none
      case auto
      case function(String)
      
      enum CodingKeys: String, CodingKey {
         case none = "none"
         case auto = "auto"
         case function = "name"
      }
      
      public func encode(to encoder: Encoder) throws {
         switch self {
         case .none:
            var container = encoder.singleValueContainer()
            try container.encode(CodingKeys.none.rawValue)
         case .auto:
            var container = encoder.singleValueContainer()
            try container.encode(CodingKeys.auto.rawValue)
         case .function(let name):
            var container = encoder.container(keyedBy: CodingKeys.self)
            try container.encode(name, forKey: .function)
         }
      }
   }
   
   /// [Documentation](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools)
   public struct Tool: Encodable {
      
      /// The type of the tool. Currently, only `function` is supported.
      let type: String
      /// object
      let function: ChatFunction
      
      public init(
         type: String = "function",
         function: ChatFunction)
      {
         self.type = type
         self.function = function
      }
   }
   
   public struct ChatFunction: Codable, Equatable {
      
      /// The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
      let name: String
      /// A description of what the function does, used by the model to choose when and how to call the function.
      let description: String?
      /// The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/gpt/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format.
      /// Omitting parameters defines a function with an empty parameter list.
      let parameters: JSONSchema?
      /// Defaults to false, Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the parameters field. Only a subset of JSON Schema is supported when strict is true. Learn more about Structured Outputs in the [function calling guide].(https://platform.openai.com/docs/api-reference/chat/docs/guides/function-calling)
      let strict: Bool?
      
      public init(
         name: String,
         strict: Bool?,
         description: String?,
         parameters: JSONSchema?)
      {
         self.name = name
         self.strict = strict
         self.description = description
         self.parameters = parameters
      }
   }
   
   public enum ServiceTier: String, Encodable {
      /// Specifies the latency tier to use for processing the request. This parameter is relevant for customers subscribed to the scale tier service:
      /// If set to 'auto', the system will utilize scale tier credits until they are exhausted.
      /// If set to 'default', the request will be processed in the shared cluster.
      /// When this parameter is set, the response body will include the service_tier utilized.
      case auto
      case `default`
   }
   
   public struct StreamOptions: Encodable {
      /// If set, an additional chunk will be streamed before the data: [DONE] message.
      /// The usage field on this chunk shows the token usage statistics for the entire request,
      /// and the choices field will always be an empty array. All other chunks will also include
      /// a usage field, but with a null value.
      let includeUsage: Bool

      enum CodingKeys: String, CodingKey {
          case includeUsage = "include_usage"
      }
   }
   
   /// Parameters for audio output. Required when audio output is requested with modalities: ["audio"]
   /// [Learn more.](https://platform.openai.com/docs/guides/audio)
   public struct Audio: Encodable {
      /// Specifies the voice type. Supported voices are alloy, echo, fable, onyx, nova, and shimmer.
      public let voice: String
      /// Specifies the output audio format. Must be one of wav, mp3, flac, opus, or pcm16.
      public let format: String
      
      public init(
         voice: String,
         format: String)
      {
         self.voice = voice
         self.format = format
      }
   }

   enum CodingKeys: String, CodingKey {
      case messages
      case model
      case store
      case frequencyPenalty = "frequency_penalty"
      case toolChoice = "tool_choice"
      case functionCall = "function_call"
      case tools
      case parallelToolCalls = "parallel_tool_calls"
      case functions
      case logitBias = "logit_bias"
      case logprobs
      case topLogprobs = "top_logprobs"
      case maxTokens = "max_tokens"
      case maCompletionTokens = "max_completion_tokens"
      case n
      case modalities
      case audio
      case responseFormat = "response_format"
      case presencePenalty = "presence_penalty"
      case seed
      case serviceTier = "service_tier"
      case stop
      case stream
      case streamOptions = "stream_options"
      case temperature
      case topP = "top_p"
      case user
   }
   
   public init(
      messages: [Message],
      model: Model,
      store: Bool? = nil,
      frequencyPenalty: Double? = nil,
      functionCall: FunctionCall? = nil,
      toolChoice: ToolChoice? = nil,
      functions: [ChatFunction]? = nil,
      tools: [Tool]? = nil,
      parallelToolCalls: Bool? = nil,
      logitBias: [Int: Double]? = nil,
      logProbs: Bool? = nil,
      topLogprobs: Int? = nil,
      maxTokens: Int? = nil,
      n: Int? = nil,
      modalities: [String]? = nil,
      audio: Audio? = nil,
      responseFormat: ResponseFormat? = nil,
      presencePenalty: Double? = nil,
      serviceTier: ServiceTier? = nil,
      seed: Int? = nil,
      stop: [String]? = nil,
      temperature: Double? = nil,
      topProbability: Double? = nil,
      user: String? = nil)
   {
      self.messages = messages
      self.model = model.value
      self.store = store
      self.frequencyPenalty = frequencyPenalty
      self.functionCall = functionCall
      self.toolChoice = toolChoice
      self.functions = functions
      self.tools = tools
      self.parallelToolCalls = parallelToolCalls
      self.logitBias = logitBias
      self.logprobs = logProbs
      self.topLogprobs = topLogprobs
      self.maxTokens = maxTokens
      self.n = n
      self.modalities = modalities
      self.audio = audio
      self.responseFormat = responseFormat
      self.presencePenalty = presencePenalty
      self.serviceTier = serviceTier?.rawValue
      self.seed = seed
      self.stop = stop
      self.temperature = temperature
      self.topP = topProbability
      self.user = user
   }
}
```

Response
### Chat completion object
```swift
/// Represents a chat [completion](https://platform.openai.com/docs/api-reference/chat/object) response returned by model, based on the provided input.
public struct ChatCompletionObject: Decodable {
   
   /// A unique identifier for the chat completion.
   public let id: String
   /// A list of chat completion choices. Can be more than one if n is greater than 1.
   public let choices: [ChatChoice]
   /// The Unix timestamp (in seconds) of when the chat completion was created.
   public let created: Int
   /// The model used for the chat completion.
   public let model: String
   /// The service tier used for processing the request. This field is only included if the service_tier parameter is specified in the request.
   public let serviceTier: String?
   /// This fingerprint represents the backend configuration that the model runs with.
   /// Can be used in conjunction with the seed request parameter to understand when backend changes have been made that might impact determinism.
   public let systemFingerprint: String?
   /// The object type, which is always chat.completion.
   public let object: String
   /// Usage statistics for the completion request.
   public let usage: ChatUsage
   
   public struct ChatChoice: Decodable {
      
      /// The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence, length if the maximum number of tokens specified in the request was reached, content_filter if content was omitted due to a flag from our content filters, tool_calls if the model called a tool, or function_call (deprecated) if the model called a function.
      public let finishReason: IntOrStringValue?
      /// The index of the choice in the list of choices.
      public let index: Int
      /// A chat completion message generated by the model.
      public let message: ChatMessage   
      /// Log probability information for the choice.
      public let logprobs: LogProb?
      
      public struct ChatMessage: Decodable {
         
         /// The contents of the message.
         public let content: String?
         /// The tool calls generated by the model, such as function calls.
         public let toolCalls: [ToolCall]?
         /// The name and arguments of a function that should be called, as generated by the model.
         @available(*, deprecated, message: "Deprecated and replaced by `tool_calls`")
         public let functionCall: FunctionCall?
         /// The role of the author of this message.
         public let role: String
         /// Provided by the Vision API.
         public let finishDetails: FinishDetails?
         /// The refusal message generated by the model.
         public let refusal: String?
         /// If the audio output modality is requested, this object contains data about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).
         public let audio: Audio?
         
         /// Provided by the Vision API.
         public struct FinishDetails: Decodable {
            let type: String
         }
         
         public struct Audio: Decodable {
            /// Unique identifier for this audio response.
            public let id: String
            /// The Unix timestamp (in seconds) for when this audio response will no longer be accessible on the server for use in multi-turn conversations.
            public let expiresAt: Int
            /// Base64 encoded audio bytes generated by the model, in the format specified in the request.
            public let data: String
            /// Transcript of the audio generated by the model.
            public let transcript: String
            
            enum CodingKeys: String, CodingKey {
               case id
               case expiresAt = "expires_at"
               case data
               case transcript
            }
         }
      }
      
      public struct LogProb: Decodable {
         /// A list of message content tokens with log probability information.
         let content: [TokenDetail]
      }
      
      public struct TokenDetail: Decodable {
         /// The token.
         let token: String
         /// The log probability of this token.
         let logprob: Double
         /// A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
         let bytes: [Int]?
         /// List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned.
         let topLogprobs: [TopLogProb]
         
         enum CodingKeys: String, CodingKey {
            case token, logprob, bytes
            case topLogprobs = "top_logprobs"
         }
         
         struct TopLogProb: Decodable {
            /// The token.
            let token: String
            /// The log probability of this token.
            let logprob: Double
            /// A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
            let bytes: [Int]?
         }
      }
   }
   
   public struct ChatUsage: Decodable {
      
      /// Number of tokens in the generated completion.
      public let completionTokens: Int
      /// Number of tokens in the prompt.
      public let promptTokens: Int
      /// Total number of tokens used in the request (prompt + completion).
      public let totalTokens: Int
   }
}
```

Usage
```swift
let prompt = "Tell me a joke"
let parameters = ChatCompletionParameters(messages: [.init(role: .user, content: .text(prompt))], model: .gpt4o)
let chatCompletionObject = service.startChat(parameters: parameters)
```

Response
### Chat completion chunk object
```swift
/// Represents a [streamed](https://platform.openai.com/docs/api-reference/chat/streaming) chunk of a chat completion response returned by model, based on the provided input.
public struct ChatCompletionChunkObject: Decodable {
   
   /// A unique identifier for the chat completion chunk.
   public let id: String
   /// A list of chat completion choices. Can be more than one if n is greater than 1.
   public let choices: [ChatChoice]
   /// The Unix timestamp (in seconds) of when the chat completion chunk was created.
   public let created: Int
   /// The model to generate the completion.
   public let model: String
   /// The service tier used for processing the request. This field is only included if the service_tier parameter is specified in the request.
   public let serviceTier: String?
   /// This fingerprint represents the backend configuration that the model runs with.
   /// Can be used in conjunction with the seed request parameter to understand when backend changes have been made that might impact determinism.
   public let systemFingerprint: String?
   /// The object type, which is always chat.completion.chunk.
   public let object: String
   
   public struct ChatChoice: Decodable {
      
      /// A chat completion delta generated by streamed model responses.
      public let delta: Delta
      /// The reason the model stopped generating tokens. This will be stop if the model hit a natural stop point or a provided stop sequence, length if the maximum number of tokens specified in the request was reached, content_filter if content was omitted due to a flag from our content filters, tool_calls if the model called a tool, or function_call (deprecated) if the model called a function.
      public let finishReason: IntOrStringValue?
      /// The index of the choice in the list of choices.
      public let index: Int
      /// Provided by the Vision API.
      public let finishDetails: FinishDetails?
      
      public struct Delta: Decodable {
         
         /// The contents of the chunk message.
         public let content: String?
         /// The tool calls generated by the model, such as function calls.
         public let toolCalls: [ToolCall]?
         /// The name and arguments of a function that should be called, as generated by the model.
         @available(*, deprecated, message: "Deprecated and replaced by `tool_calls`")
         public let functionCall: FunctionCall?
         /// The role of the author of this message.
         public let role: String?
      }
      
      public struct LogProb: Decodable {
         /// A list of message content tokens with log probability information.
         let content: [TokenDetail]
      }
      
      public struct TokenDetail: Decodable {
         /// The token.
         let token: String
         /// The log probability of this token.
         let logprob: Double
         /// A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
         let bytes: [Int]?
         /// List of the most likely tokens and their log probability, at this token position. In rare cases, there may be fewer than the number of requested top_logprobs returned.
         let topLogprobs: [TopLogProb]
         
         enum CodingKeys: String, CodingKey {
            case token, logprob, bytes
            case topLogprobs = "top_logprobs"
         }
         
         struct TopLogProb: Decodable {
            /// The token.
            let token: String
            /// The log probability of this token.
            let logprob: Double
            /// A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be null if there is no bytes representation for the token.
            let bytes: [Int]?
         }
      }
      
      /// Provided by the Vision API.
      public struct FinishDetails: Decodable {
         let type: String
      }
   }
}
```
Usage
```swift
let prompt = "Tell me a joke"
let parameters = ChatCompletionParameters(messages: [.init(role: .user, content: .text(prompt))], model: .gpt4o)
let chatCompletionObject = try await service.startStreamedChat(parameters: parameters)
```

### Function Calling

Chat Completion also supports [Function Calling](https://platform.openai.com/docs/guides/function-calling) and [Parallel Function Calling](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling). `functions` has been deprecated in favor of `tools` check [OpenAI Documentation](https://platform.openai.com/docs/api-reference/chat/create) for more.

```swift
public struct ToolCall: Codable {

   public let index: Int
   /// The ID of the tool call.
   public let id: String?
   /// The type of the tool. Currently, only `function` is supported.
   public let type: String?
   /// The function that the model called.
   public let function: FunctionCall

   public init(
      index: Int,
      id: String,
      type: String = "function",
      function: FunctionCall)
   {
      self.index = index
      self.id = id
      self.type = type
      self.function = function
   }
}

public struct FunctionCall: Codable {

   /// The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.
   let arguments: String
   /// The name of the function to call.
   let name: String

   public init(
      arguments: String,
      name: String)
   {
      self.arguments = arguments
      self.name = name
   }
}
```

Usage
```swift
/// Define a `ToolCall`
var tool: ToolCall {
   .init(
      type: "function", // The type of the tool. Currently, only "function" is supported.
      function: .init(
         name: "create_image",
         description: "Call this function if the request asks to generate an image",
         parameters: .init(
            type: .object,
            properties: [
               "prompt": .init(type: .string, description: "The exact prompt passed in."),
               "count": .init(type: .integer, description: "The number of images requested")
            ],
            required: ["prompt", "count"])))
}

let prompt = "Show me an image of an unicorn eating ice cream"
let content: ChatCompletionParameters.Message.ContentType = .text(prompt)
let parameters = ChatCompletionParameters(messages: [.init(role: .user, content: content)], model: .gpt41106Preview, tools: [tool])
let chatCompletionObject = try await service.startStreamedChat(parameters: parameters)
```
For more details about how to also uploading base 64 encoded images in iOS check the [ChatFunctionsCalllDemo](https://github.com/jamesrochabrun/SwiftOpenAI/tree/main/Examples/SwiftOpenAIExample/SwiftOpenAIExample/ChatFunctionsCall) demo on the Examples section of this package.

### Structured Outputs

#### Documentation:

- [Structured Outputs Guides](https://platform.openai.com/docs/guides/structured-outputs/structured-outputs)
- [Examples](https://platform.openai.com/docs/guides/structured-outputs/examples)
- [How to use](https://platform.openai.com/docs/guides/structured-outputs/how-to-use)
- [Supported schemas](https://platform.openai.com/docs/guides/structured-outputs/supported-schemas)

Must knowns:

- [All fields must be required](https://platform.openai.com/docs/guides/structured-outputs/all-fields-must-be-required) , To use Structured Outputs, all fields or function parameters must be specified as required.
- Although all fields must be required (and the model will return a value for each parameter), it is possible to emulate an optional parameter by using a union type with null.
- [Objects have limitations on nesting depth and size](https://platform.openai.com/docs/guides/structured-outputs/objects-have-limitations-on-nesting-depth-and-size), A schema may have up to 100 object properties total, with up to 5 levels of nesting.

- [additionalProperties](https://platform.openai.com/docs/guides/structured-outputs/additionalproperties-false-must-always-be-set-in-objects)): false must always be set in objects
additionalProperties controls whether it is allowable for an object to contain additional keys / values that were not defined in the JSON Schema.
Structured Outputs only supports generating specified keys / values, so we require developers to set additionalProperties: false to opt into Structured Outputs.
- [Key ordering](https://platform.openai.com/docs/guides/structured-outputs/key-ordering), When using Structured Outputs, outputs will be produced in the same order as the ordering of keys in the schema.
- [Recursive schemas are supported](https://platform.openai.com/docs/guides/structured-outputs/recursive-schemas-are-supported)

#### How to use Structured Outputs in SwiftOpenAI

1. Function calling: Structured Outputs via tools is available by setting strict: true within your function definition. This feature works with all models that support tools, including all models gpt-4-0613 and gpt-3.5-turbo-0613 and later. When Structured Outputs are enabled, model outputs will match the supplied tool definition.

Using this schema:

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "steps": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "explanation": {
              "type": "string"
            },
            "output": {
              "type": "string"
            }
          },
          "required": ["explanation", "output"],
          "additionalProperties": false
        }
      },
      "final_answer": {
        "type": "string"
      }
    },
    "required": ["steps", "final_answer"],
    "additionalProperties": false
  }
}
```

You can use the convenient `JSONSchema` object like this:

```swift
// 1: Define the Step schema object

let stepSchema = JSONSchema(
   type: .object,
   properties: [
      "explanation": JSONSchema(type: .string),
      "output": JSONSchema(
         type: .string)
   ],
   required: ["explanation", "output"],
   additionalProperties: false
)

// 2. Define the steps Array schema.

let stepsArraySchema = JSONSchema(type: .array, items: stepSchema)

// 3. Define the final Answer schema.

let finalAnswerSchema = JSONSchema(type: .string)

// 4. Define math reponse JSON schema.

let mathResponseSchema = JSONSchema(
      type: .object,
      properties: [
         "steps": stepsArraySchema,
         "final_answer": finalAnswerSchema
      ],
      required: ["steps", "final_answer"],
      additionalProperties: false
)

let tool = ChatCompletionParameters.Tool(
            function: .init(
               name: "math_response",
               strict: true,
               parameters: mathResponseSchema))
)

let prompt = "solve 8x + 31 = 2"
let systemMessage = ChatCompletionParameters.Message(role: .system, content: .text("You are a math tutor"))
let userMessage = ChatCompletionParameters.Message(role: .user, content: .text(prompt))
let parameters = ChatCompletionParameters(
   messages: [systemMessage, userMessage],
   model: .gpt4o20240806,
   tools: [tool])

let chat = try await service.startChat(parameters: parameters)
```

2. A new option for the `response_format` parameter: developers can now supply a JSON Schema via `json_schema`, a new option for the response_format parameter. This is useful when the model is not calling a tool, but rather, responding to the user in a structured way. This feature works with our newest GPT-4o models: `gpt-4o-2024-08-06`, released today, and `gpt-4o-mini-2024-07-18`. When a response_format is supplied with strict: true, model outputs will match the supplied schema.

Using the previous schema, this is how you can implement it as json schema using the convenient `JSONSchemaResponseFormat` object:

```swift
// 1: Define the Step schema object

let stepSchema = JSONSchema(
   type: .object,
   properties: [
      "explanation": JSONSchema(type: .string),
      "output": JSONSchema(
         type: .string)
   ],
   required: ["explanation", "output"],
   additionalProperties: false
)

// 2. Define the steps Array schema.

let stepsArraySchema = JSONSchema(type: .array, items: stepSchema)

// 3. Define the final Answer schema.

let finalAnswerSchema = JSONSchema(type: .string)

// 4. Define the response format JSON schema.

let responseFormatSchema = JSONSchemaResponseFormat(
   name: "math_response",
   strict: true,
   schema: JSONSchema(
      type: .object,
      properties: [
         "steps": stepsArraySchema,
         "final_answer": finalAnswerSchema
      ],
      required: ["steps", "final_answer"],
      additionalProperties: false
   )
)

let prompt = "solve 8x + 31 = 2"
let systemMessage = ChatCompletionParameters.Message(role: .system, content: .text("You are a math tutor"))
let userMessage = ChatCompletionParameters.Message(role: .user, content: .text(prompt))
let parameters = ChatCompletionParameters(
   messages: [systemMessage, userMessage],
   model: .gpt4o20240806,
   responseFormat: .jsonSchema(responseFormatSchema))
```

SwiftOpenAI Structred outputs supports:

- [x] Tools Structured output.
- [x] Response format Structure output.
- [x] Recursive Schema.
- [x] Optional values Schema.
- [ ] Pydantic models.

We don't support Pydantic models, users need tos manually create Schemas using `JSONSchema` or `JSONSchemaResponseFormat` objects.

Pro tip 🔥 Use [iosAICodeAssistant GPT](https://chatgpt.com/g/g-qj7RuW7PY-iosai-code-assistant) to construct SwifOpenAI schemas. Just paste your JSON schema and ask the GPT to create SwiftOpenAI schemas for tools and response format.

For more details visit the Demo project for [tools](https://github.com/jamesrochabrun/SwiftOpenAI/tree/main/Examples/SwiftOpenAIExample/SwiftOpenAIExample/ChatStructureOutputTool) and [response format](https://github.com/jamesrochabrun/SwiftOpenAI/tree/main/Examples/SwiftOpenAIExample/SwiftOpenAIExample/ChatStructuredOutputs).

### Vision

[Vision](https://platform.openai.com/docs/guides/vision) API is available for use; developers must access it through the chat completions API, specifically using the gpt-4-vision-preview model or gpt-4o model. Using any other model will not provide an image description

Usage
```swift
let imageURL = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
let prompt = "What is this?"
let messageContent: [ChatCompletionParameters.Message.ContentType.MessageContent] = [.text(prompt), .imageUrl(.init(url: imageURL)] // Users can add as many `.imageUrl` instances to the service.
let parameters = ChatCompletionParameters(messages: [.init(role: .user, content: .contentArray(messageContent))], model: .gpt4o)
let chatCompletionObject = try await service.startStreamedChat(parameters: parameters)
```

![Simulator Screen Recording - iPhone 15 - 2023-11-09 at 17 12 06](https://github.com/jamesrochabrun/SwiftOpenAI/assets/5378604/db2cbb3b-0c80-4ac8-8fe5-dbb782b270da)

For more details about how to also uploading base 64 encoded images in iOS check the [ChatVision](https://github.com/jamesrochabrun/SwiftOpenAI/tree/main/Examples/SwiftOpenAIExample/SwiftOpenAIExample/Vision) demo on the Examples section of this package.

### Response

OpenAI's most advanced interface for generating model responses. Supports text and image inputs, and text outputs. Create stateful interactions with the model, using the output of previous responses as input. Extend the model's capabilities with built-in tools for file search, web search, computer use, and more. Allow the model access to external systems and data using function calling.

- Full streaming support with `responseCreateStream` method
- Comprehensive `ResponseStreamEvent` enum covering 40+ event types
- Enhanced `InputMessage` with `id` field for response ID tracking
- Improved conversation state management with `previousResponseId`
- Real-time text streaming, function calls, and tool usage events
- Support for reasoning summaries, web search, file search, and image generation events
- **NEW**: Support for GPT-5 models (gpt-5, gpt-5-mini, gpt-5-nano)
- **NEW**: Verbosity parameter for controlling response detail level
- **NEW**: Support for GPT-6 models (gpt-6-astra, gpt-6.1-sol) and the Ultrafast service tier

#### ModelResponseParameter

The `ModelResponseParameter` provides a comprehensive interface for creating model responses:

```swift
let parameters = ModelResponseParameter(
    input: .text("What is the answer to life, the universe, and everything?"),
    model: .gpt5,  // Support for GPT-5, GPT-5-mini, GPT-5-nano
    text: TextConfiguration(
        format: .text,
        verbosity: "low"  // NEW: Control response verbosity ("low", "medium", "high")
    ),
    temperature: 0.7
)

let response = try await service.responseCreate(parameters)
```

#### Available GPT-5 and GPT-6 Models

```swift
public enum Model {
    case gpt5        // Complex reasoning, broad world knowledge, and code-heavy or multi-step agentic tasks
    case gpt5Mini    // Cost-optimized reasoning and chat; balances speed, cost, and capability
    case gpt5Nano    // High-throughput tasks, especially simple instruction-following or classification
    case gpt6Astra   // Flagship model for complex reasoning and agentic tasks
    case gpt61Sol    // Near-Astra intelligence at a fifth of the price; 1M+ token context window
    // ... other models
}
```

#### Ultrafast Service Tier

The [Ultrafast service tier](https://developers.openai.com/api/docs/guides/ultrafast-mode) offers up to 6x faster token generation at a premium price. It is available in the Responses API for `gpt-6-astra` (broadly available) and `gpt-5.6-sol` (preview access):

```swift
let parameters = ModelResponseParameter(
    input: .text("Summarize this ticket in one sentence."),
    model: .gpt6Astra,
    serviceTier: ServiceTier.ultrafast.rawValue
)

let response = try await service.responseCreate(parameters)
```

#### TextConfiguration with Verbosity

```swift
// Create a text configuration with verbosity control
let textConfig = TextConfiguration(
    format: .text,       // Can be .text, .jsonObject, or .jsonSchema
    verbosity: "medium"  // Controls response detail level
)
```

Related guides:

- [Quickstart](https://platform.openai.com/docs/quickstart?api-mode=responses)
- [Text inputs and outputs](https://platform.openai.com/docs/guides/text?api-mode=responses)
- [Image inputs](https://platform.openai.com/docs/guides/images?api-mode=responses)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses)
- [Function calling](https://platform.openai.com/docs/guides/function-calling?api-mode=responses)
- [Conversation state](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses)
- [Extend the models with tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)

Parameters
```swift
/// [Creates a model response.](https://platform.openai.com/docs/api-reference/responses/create)
public struct ModelResponseParameter: Codable {

   /// Text, image, or file inputs to the model, used to generate a response.
   /// A text input to the model, equivalent to a text input with the user role.
   /// A list of one or many input items to the model, containing different content types.
   public var input: InputType

   /// Model ID used to generate the response, like gpt-4o or o1. OpenAI offers a wide range of models with
   /// different capabilities, performance characteristics, and price points.
   /// Refer to the model guide to browse and compare available models.
   public var model: String

   /// Specify additional output data to include in the model response. Currently supported values are:
   /// file_search_call.results : Include the search results of the file search tool call.
   /// message.input_image.image_url : Include image urls from the input message.
   /// computer_call_output.output.image_url : Include image urls from the computer call output.
   public var include: [String]?

   /// Inserts a system (or developer) message as the first item in the model's context.
   /// When using along with previous_response_id, the instructions from a previous response will be not be
   /// carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.
   public var instructions: String?

   /// An upper bound for the number of tokens that can be generated for a response, including visible output tokens
   /// and reasoning tokens.
   public var maxOutputTokens: Int?

   /// Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information
   /// about the object in a structured format, and querying for objects via API or the dashboard.
   /// Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.
   public var metadata: [String: String]?

   /// Whether to allow the model to run tool calls in parallel.
   /// Defaults to true
   public var parallelToolCalls: Bool?

   /// The unique ID of the previous response to the model. Use this to create multi-turn conversations.
   /// Learn more about conversation state.
   public var previousResponseId: String?

   /// o-series models only
   /// Configuration options for reasoning models.
   public var reasoning: Reasoning?

   /// Whether to store the generated model response for later retrieval via API.
   /// Defaults to true
   public var store: Bool?

   /// If set to true, the model response data will be streamed to the client as it is generated using server-sent events.
   public var stream: Bool?

   /// What sampling temperature to use, between 0 and 2.
   /// Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
   /// We generally recommend altering this or top_p but not both.
   /// Defaults to 1
   public var temperature: Double?

   /// Configuration options for a text response from the model. Can be plain text or structured JSON data.
   public var text: TextConfiguration?

   /// How the model should select which tool (or tools) to use when generating a response.
   /// See the tools parameter to see how to specify which tools the model can call.
   public var toolChoice: ToolChoiceMode?

   /// An array of tools the model may call while generating a response. You can specify which tool to use by setting the tool_choice parameter.
   public var tools: [Tool]?

   /// An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
   /// So 0.1 means only the tokens comprising the top 10% probability mass are considered.
   /// We generally recommend altering this or temperature but not both.
   /// Defaults to 1
   public var topP: Double?

   /// The truncation strategy to use for the model response.
   /// Defaults to disabled
   public var truncation: String?

   /// A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.
   public var user: String?
}
```

[The Response object](https://platform.openai.com/docs/api-reference/responses/object)

```swift
/// The Response object returned when retrieving a model response
public struct ResponseModel: Decodable {

   /// Unix timestamp (in seconds) of when this Response was created.
   public let createdAt: Int

   /// An error object returned when the model fails to generate a Response.
   public let error: ErrorObject?

   /// Unique identifier for this Response.
   public let id: String

   /// Details about why the response is incomplete.
   public let incompleteDetails: IncompleteDetails?

   /// Inserts a system (or developer) message as the first item in the model's context.
   public let instructions: String?

   /// An upper bound for the number of tokens that can be generated for a response, including visible output tokens
   /// and reasoning tokens.
   public let maxOutputTokens: Int?

   /// Set of 16 key-value pairs that can be attached to an object.
   public let metadata: [String: String]

   /// Model ID used to generate the response, like gpt-4o or o1.
   public let model: String

   /// The object type of this resource - always set to response.
   public let object: String

   /// An array of content items generated by the model.
   public let output: [OutputItem]

   /// Whether to allow the model to run tool calls in parallel.
   public let parallelToolCalls: Bool

   /// The unique ID of the previous response to the model. Use this to create multi-turn conversations.
   public let previousResponseId: String?

   /// Configuration options for reasoning models.
   public let reasoning: Reasoning?

   /// The status of the response generation. One of completed, failed, in_progress, or incomplete.
   public let status: String

   /// What sampling temperature to use, between 0 and 2.
   public let temperature: Double?

   /// Configuration options for a text response from the model.
   public let text: TextConfiguration

   /// How the model should select which tool (or tools) to use when generating a response.
   public let toolChoice: ToolChoiceMode

   /// An array of tools the model may call while generating a response.
   public let tools: [Tool]

   /// An alternative to sampling with temperature, called nucleus sampling.
   public let topP: Double?

   /// The truncation strategy to use for the model response.
   public let truncation: String?

   /// Represents token usage details.
   public let usage: Usage?

   /// A unique identifier representing your end-user.
   public let user: String?
   
   /// Convenience property that aggregates all text output from output_text items in the output array.
   /// Similar to the outputText property in Python and JavaScript SDKs.
   public var outputText: String? 
}
```

Input Types
```swift
// InputType represents the input to the Response API
public enum InputType: Codable {
    case string(String)  // Simple text input
    case array([InputItem])  // Array of input items for complex conversations
}

// InputItem represents different types of input
public enum InputItem: Codable {
    case message(InputMessage)  // User, assistant, system messages
    case functionToolCall(FunctionToolCall)  // Function calls
    case functionToolCallOutput(FunctionToolCallOutput)  // Function outputs
    // ... other input types
}

// InputMessage structure with support for response IDs
public struct InputMessage: Codable {
    public let role: String  // "user", "assistant", "system"
    public let content: MessageContent
    public let type: String?  // Always "message"
    public let status: String?  // "completed" for assistant messages
    public let id: String?  // Response ID for assistant messages
}

// MessageContent can be text or array of content items
public enum MessageContent: Codable {
    case text(String)
    case array([ContentItem])  // For multimodal content
}
```

Usage

Simple text input
```swift
let prompt = "What is the capital of France?"
let parameters = ModelResponseParameter(input: .string(prompt), model: .gpt4o)
let response = try await service.responseCreate(parameters)
```

Text input with reasoning
```swift
let prompt = "How much wood would a woodchuck chuck?"
let parameters = ModelResponseParameter(
    input: .string(prompt),
    model: .o3Mini,
    reasoning: Reasoning(effort: "high")
)
let response = try await service.responseCreate(parameters)
```

Image input
```swift
let textPrompt = "What is in this image?"
let imageUrl = "https://example.com/path/to/image.jpg"
let imageContent = ContentItem.imageUrl(ImageUrlContent(imageUrl: imageUrl))
let textContent = ContentItem.text(TextContent(text: textPrompt))
let message = InputItem(role: "user", content: [textContent, imageContent])
let parameters = ModelResponseParameter(input: .array([message]), model: .gpt4o)
let response = try await service.responseCreate(parameters)
```

Using tools (web search)
```swift
let prompt = "What was a positive news story from today?"
let parameters = ModelResponseParameter(
    input: .string(prompt),
    model: .gpt4o,
    tools: [Tool(type: "web_search_preview", function: nil)]
)
let response = try await service.responseCreate(parameters)
```

Using tools (file search)
```swift
let prompt = "What are the key points in the document?"
let parameters = ModelResponseParameter(
    input: .string(prompt),
    model: .gpt4o,
    tools: [
        Tool(
            type: "file_search",
            function: ChatCompletionParameters.ChatFunction(
                name: "file_search",
                strict: false,
                description: "Search through files",
                parameters: JSONSchema(
                    type: .object,
                    properties: [
                        "vector_store_ids": JSONSchema(
                            type: .array,
                            items: JSONSchema(type: .string)
                        ),
                        "max_num_results": JSONSchema(type: .integer)
                    ],
                    required: ["vector_store_ids"],
                    additionalProperties: false
                )
            )
        )
    ]
)
let response = try await service.responseCreate(parameters)
```

Function calling
```swift
let prompt = "What is the weather like in Boston today?"
let parameters = ModelResponseParameter(
    input: .string(prompt),
    model: .gpt4o,
    tools: [
        Tool(
            type: "function",
            function: ChatCompletionParameters.ChatFunction(
                name: "get_current_weather",
                strict: false,
                description: "Get the current weather in a given location",
                parameters: JSONSchema(
                    type: .object,
                    properties: [
                        "location": JSONSchema(
                            type: .string,
                            description: "The city and state, e.g. San Francisco, CA"
                        ),
                        "unit": JSONSchema(
                            type: .string,
                            enum: ["celsius", "fahrenheit"]
                        )
                    ],
                    required: ["location", "unit"],
                    additionalProperties: false
                )
            )
        )
    ],
    toolChoice: .auto
)
let response = try await service.responseCreate(parameters)
```

Retrieving a response
```swift
let responseId = "resp_abc123"
let response = try await service.responseModel(id: responseId)
```

#### Streaming Responses

The Response API supports streaming responses using Server-Sent Events (SSE). This allows you to receive partial responses as they are generated, enabling real-time UI updates and better user experience.

Stream Events
```swift
// The ResponseStreamEvent enum represents all possible streaming events
public enum ResponseStreamEvent: Decodable {
  case responseCreated(ResponseCreatedEvent)
  case responseInProgress(ResponseInProgressEvent)
  case responseCompleted(ResponseCompletedEvent)
  case responseFailed(ResponseFailedEvent)
  case outputItemAdded(OutputItemAddedEvent)
  case outputTextDelta(OutputTextDeltaEvent)
  case outputTextDone(OutputTextDoneEvent)
  case functionCallArgumentsDelta(FunctionCallArgumentsDeltaEvent)
  case reasoningSummaryTextDelta(ReasoningSummaryTextDeltaEvent)
  case error(ErrorEvent)
  // ... and many more event types
}
```

Basic Streaming Example
```swift
// Enable streaming by setting stream: true
let parameters = ModelResponseParameter(
    input: .string("Tell me a story"),
    model: .gpt4o,
    stream: true
)

// Create a stream
let stream = try await service.responseCreateStream(parameters)

// Process events as they arrive
for try await event in stream {
    switch event {
    case .outputTextDelta(let delta):
        // Append text chunk to your UI
        print(delta.delta, terminator: "")
        
    case .responseCompleted(let completed):
        // Response is complete
        print("\nResponse ID: \(completed.response.id)")
        
    case .error(let error):
        // Handle errors
        print("Error: \(error.message)")
        
    default:
        // Handle other events as needed
        break
    }
}
```

Streaming with Conversation State
```swift
// Maintain conversation continuity with previousResponseId
var previousResponseId: String? = nil
var messages: [(role: String, content: String)] = []

// First message
let firstParams = ModelResponseParameter(
    input: .string("Hello!"),
    model: .gpt4o,
    stream: true
)

let firstStream = try await service.responseCreateStream(firstParams)
var firstResponse = ""

for try await event in firstStream {
    switch event {
    case .outputTextDelta(let delta):
        firstResponse += delta.delta
        
    case .responseCompleted(let completed):
        previousResponseId = completed.response.id
        messages.append((role: "user", content: "Hello!"))
        messages.append((role: "assistant", content: firstResponse))
        
    default:
        break
    }
}

// Follow-up message with conversation context
var inputArray: [InputItem] = []

// Add conversation history
for message in messages {
    inputArray.append(.message(InputMessage(
        role: message.role,
        content: .text(message.content)
    )))
}

// Add new user message
inputArray.append(.message(InputMessage(
    role: "user",
    content: .text("How are you?")
)))

let followUpParams = ModelResponseParameter(
    input: .array(inputArray),
    model: .gpt4o,
    previousResponseId: previousResponseId,
    stream: true
)

let followUpStream = try await service.responseCreateStream(followUpParams)
// Process the follow-up stream...
```

Streaming with Tools and Function Calling
```swift
let parameters = ModelResponseParameter(
    input: .string("What's the weather in San Francisco?"),
    model: .gpt4o,
    tools: [
        Tool(
            type: "function",
            function: ChatCompletionParameters.ChatFunction(
                name: "get_weather",
                description: "Get current weather",
                parameters: JSONSchema(
                    type: .object,
                    properties: [
                        "location": JSONSchema(type: .string)
                    ],
                    required: ["location"]
                )
            )
        )
    ],
    stream: true
)

let stream = try await service.responseCreateStream(parameters)
var functionCallArguments = ""

for try await event in stream {
    switch event {
    case .functionCallArgumentsDelta(let delta):
        // Accumulate function call arguments
        functionCallArguments += delta.delta
        
    case .functionCallArgumentsDone(let done):
        // Function call is complete
        print("Function: \(done.name)")
        print("Arguments: \(functionCallArguments)")
        
    case .outputTextDelta(let delta):
        // Regular text output
        print(delta.delta, terminator: "")
        
    default:
        break
    }
}
```

Canceling a Stream
```swift
// Streams can be canceled using Swift's task cancellation
let streamTask = Task {
    let stream = try await service.responseCreateStream(parameters)
    
    for try await event in stream {
        // Check if task is cancelled
        if Task.isCancelled {
            break
        }
        
        // Process events...
    }
}

// Cancel the stream when needed
streamTask.cancel()
```

Complete Streaming Implementation Example
```swift
@MainActor
@Observable
class ResponseStreamProvider {
    var messages: [Message] = []
    var isStreaming = false
    var error: String?
    
    private let service: OpenAIService
    private var previousResponseId: String?
    private var streamTask: Task<Void, Never>?
    
    init(service: OpenAIService) {
        self.service = service
    }
    
    func sendMessage(_ text: String) {
        streamTask?.cancel()
        
        // Add user message
        messages.append(Message(role: .user, content: text))
        
        // Start streaming
        streamTask = Task {
            await streamResponse(for: text)
        }
    }
    
    private func streamResponse(for userInput: String) async {
        isStreaming = true
        error = nil
        
        // Create streaming message placeholder
        let streamingMessage = Message(role: .assistant, content: "", isStreaming: true)
        messages.append(streamingMessage)
        
        do {
            // Build conversation history
            var inputArray: [InputItem] = []
            for message in messages.dropLast(2) {
                inputArray.append(.message(InputMessage(
                    role: message.role.rawValue,
                    content: .text(message.content)
                )))
            }
            inputArray.append(.message(InputMessage(
                role: "user",
                content: .text(userInput)
            )))
            
            let parameters = ModelResponseParameter(
                input: .array(inputArray),
                model: .gpt4o,
                previousResponseId: previousResponseId,
                stream: true
            )
            
            let stream = try await service.responseCreateStream(parameters)
            var accumulatedText = ""
            
            for try await event in stream {
                guard !Task.isCancelled else { break }
                
                switch event {
                case .outputTextDelta(let delta):
                    accumulatedText += delta.delta
                    updateStreamingMessage(with: accumulatedText)
                    
                case .responseCompleted(let completed):
                    previousResponseId = completed.response.id
                    finalizeStreamingMessage(with: accumulatedText, responseId: completed.response.id)
                    
                case .error(let errorEvent):
                    throw APIError.requestFailed(description: errorEvent.message)
                    
                default:
                    break
                }
            }
        } catch {
            self.error = error.localizedDescription
            messages.removeLast() // Remove streaming message on error
        }
        
        isStreaming = false
    }
    
    private func updateStreamingMessage(with content: String) {
        if let index = messages.lastIndex(where: { $0.isStreaming }) {
            messages[index].content = content
        }
    }
    
    private func finalizeStreamingMessage(with content: String, responseId: String) {
        if let index = messages.lastIndex(where: { $0.isStreaming }) {
            messages[index].content = content
            messages[index].isStreaming = false
            messages[index].responseId = responseId
        }
    }
}
```

### Embeddings
Parameters
```swift
/// [Creates](https://platform.openai.com/docs/api-reference/embeddings/create) an embedding vector representing the input text.
public struct EmbeddingParameter: Encodable {
   
   /// ID of the model to use. You can use the List models API to see all of your available models, or see our [Model overview ](https://platform.openai.com/docs/models/overview) for descriptions of them.
   let model: String
   /// Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or an array of token arrays. Each input must not exceed the max input tokens for the model (8191 tokens for text-embedding-ada-002) and cannot be an empty string. [How to Count Tokens with `tiktoken`](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
   let input: String
   
   /// A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more.](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids)
   let user: String?
   
   public enum Model: String {
      case textEmbeddingAda002 = "text-embedding-ada-002"
   }
   
   public init(
      model: Model = .textEmbeddingAda002,
      input: String,
      user: String? = nil)
   {
      self.model = model.value
      self.input = input
      self.user = user
   }
}
```
Response
```swift
/// [Represents an embedding vector returned by embedding endpoint.](https://platform.openai.com/docs/api-reference/embeddings/object)
public struct EmbeddingObject: Decodable {
   
   /// The object type, which is always "embedding".
   public let object: String
   /// The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the embedding guide.[https://platform.openai.com/docs/guides/embeddings]
   public let embedding: [Float]
   /// The index of the embedding in the list of embeddings.
   public let index: Int
}
```

Usage
```swift
let prompt = "Hello world."
let embeddingObjects = try await service.createEmbeddings(parameters: parameters).data
```

### Fine-tuning
Parameters
```swift
/// [Creates a job](https://platform.openai.com/docs/api-reference/fine-tuning/create) that fine-tunes a specified model from a given dataset.
///Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.
public struct FineTuningJobParameters: Encodable {
   
   /// The name of the model to fine-tune. You can select one of the [supported models](https://platform.openai.com/docs/models/overview).
   let model: String
   /// The ID of an uploaded file that contains training data.
   /// See [upload file](https://platform.openai.com/docs/api-reference/files/upload) for how to upload a file.
   /// Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose fine-tune.
   /// See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.
   let trainingFile: String
   /// The hyperparameters used for the fine-tuning job.
   let hyperparameters: HyperParameters?
   /// A string of up to 18 characters that will be added to your fine-tuned model name.
   /// For example, a suffix of "custom-model-name" would produce a model name like ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel.
   /// Defaults to null.
   let suffix: String?
   /// The ID of an uploaded file that contains validation data.
   /// If you provide this file, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in the fine-tuning results file. The same data should not be present in both train and validation files.
   /// Your dataset must be formatted as a JSONL file. You must upload your file with the purpose fine-tune.
   /// See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.
   let validationFile: String?
   /// A list of integrations to enable for your fine-tuning job.
   let integrations: [Integration]?
   /// The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed is not specified, one will be generated for you.
   let seed: Int?
   
   /// Fine-tuning is [currently available](https://platform.openai.com/docs/guides/fine-tuning/what-models-can-be-fine-tuned) for the following models:
   /// gpt-3.5-turbo-0613 (recommended)
   /// babbage-002
   /// davinci-002
   /// OpenAI expects gpt-3.5-turbo to be the right model for most users in terms of results and ease of use, unless you are migrating a legacy fine-tuned model.
   public enum Model: String {
      case gpt35 = "gpt-3.5-turbo-0613" /// recommended
      case babbage002 = "babbage-002"
      case davinci002 = "davinci-002"
   }
   
   public struct HyperParameters: Encodable {
      /// The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.
      /// Defaults to auto.
      let nEpochs: Int?
      
      public init(
         nEpochs: Int?)
      {
         self.nEpochs = nEpochs
      }
   }
   
   public init(
      model: Model,
      trainingFile: String,
      hyperparameters: HyperParameters? = nil,
      suffix: String? = nil,
      validationFile: String? = nil)
   {
      self.model = model.rawValue
      self.trainingFile = trainingFile
      self.hyperparameters = hyperparameters
      self.suffix = suffix
      self.validationFile = validationFile
   }
}
```
Response
```swift
/// The fine_tuning.job object represents a [fine-tuning job](https://platform.openai.com/docs/api-reference/fine-tuning/object) that has been created through the API.
public struct FineTuningJobObject: Decodable {
   
   /// The object identifier, which can be referenced in the API endpoints.
   public let id: String
   /// The Unix timestamp (in seconds) for when the fine-tuning job was created.
   public let createdAt: Int
  /// For fine-tuning jobs that have failed, this will contain more information on the cause of the failure.
   public let error: OpenAIErrorResponse.Error?
   /// The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.
   public let fineTunedModel: String?
   /// The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.
   public let finishedAt: In