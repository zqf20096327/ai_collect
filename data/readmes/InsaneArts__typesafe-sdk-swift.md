# TypeSafe AI Swift SDK

Swift community SDK for [TypeSafe AI](https://typesafe.ai).

## Quickstart

Add the package (Swift 6.0 or newer, macOS 13, iOS 16):

```swift
.package(url: "https://github.com/InsaneArts/typesafe-sdk-swift", from: "0.2.0")
```

Set `TYPESAFE_API_KEY` in your environment, then create and use the client:

```swift
import TypeSafe

let client = try TypeSafeClient()
let response = try await client.systemOne(
  state: ["document": "I was charged twice. Please fix this ASAP."],
  Choice("What is this ticket about?", options: ["billing", "technical", "other"])
)

print(response.answers.choice)
```

Answer types are inferred from your questions. With several questions, `answers` is a tuple in the order of the questions. The library has no dependencies.

The model sees the options of a `Choice` in the order you give them, and the order can change the probabilities.

To ask questions of different types under ids of your choice, wrap each one in `AnyQuestion`. Each answer is an `AnyAnswer`:

```swift
let response = try await client.systemOne(state: ticket, questions: [
  "topic": AnyQuestion(Choice("What is this ticket about?", options: ["billing", "other"])),
  "urgent": AnyQuestion(Noul("Does this ticket need an answer today?")),
])
print(response.answers["urgent"]?.noul?.noul ?? 0)
```

## Images

Image support is experimental. Send the `TypeSafe-Danger-Zone-Images: true` header to use it:

```swift
let client = try TypeSafeClient(defaultHeaders: ["TypeSafe-Danger-Zone-Images": "true"])
```

Create an `ImageAsset` from PNG or JPEG bytes, a file, or base64 text. The API detects the format from the bytes and rejects other formats with a 400. Use an image in one of three ways:

```swift
let photo = try ImageAsset(contentsOf: URL(filePath: "returns/RMA-1042.jpg"))

// 1. Put it in the content.
_ = try await client.systemOne(
  state: ["claim": "The mug arrived chipped.", "photo": .image(photo)] as JSONValue,
  Noul("Is the product in the photo damaged?"))

// 2. Interpolate it into a `JSONValue` string. A plain `String` does not carry the image.
_ = try await client.systemOne(state: "A customer returned \(photo)." as JSONValue, Noul("Is it damaged?"))

// 3. Name it in `assets`, and write the name in plain strings.
_ = try await client.systemOne(
  state: "A customer returned <delivered>.", assets: ["<delivered>": photo], Noul("Is it damaged?"))
```

Every name in `assets` must appear in the request. A request with images is sent as `multipart/form-data`, with each image in its own part.

A `Box` question locates what its instructions describe. Use the `jev-preview` model:

```swift
let response = try await client.systemOne(
  state: JSONValue.image(photo), model: "jev-preview", Box("The damaged area of the product"))
print(response.answers.box.top, response.answers.box.left)
```

The JavaScript SDK compresses large bodies with zstd. Apple platforms have no zstd encoder, so this SDK sends bodies uncompressed.

## Documentation

Learn what TypeSafe can do in the [TypeSafe docs](https://docs.typesafe.ai/).
See the SDK's [client](Sources/TypeSafe/Client.swift), [questions](Sources/TypeSafe/Questions.swift), and [retry policy](Sources/TypeSafe/RetryPolicy.swift) for API options and defaults.

## License

MIT. See [LICENSE](LICENSE).
