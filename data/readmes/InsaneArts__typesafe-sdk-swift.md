# TypeSafe AI Swift SDK

Swift community SDK for [TypeSafe AI](https://typesafe.ai).

## Quickstart

Add the package (Swift 6.0 or newer, macOS 13, iOS 16):

```swift
.package(url: "https://github.com/InsaneArts/typesafe-sdk-swift", from: "0.1.0")
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

## Documentation

Learn what TypeSafe can do in the [TypeSafe docs](https://docs.typesafe.ai/).
See the SDK's [client](Sources/TypeSafe/Client.swift), [questions](Sources/TypeSafe/Questions.swift), and [retry policy](Sources/TypeSafe/RetryPolicy.swift) for API options and defaults.

## License

MIT. See [LICENSE](LICENSE).
