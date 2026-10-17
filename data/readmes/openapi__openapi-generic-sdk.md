# 🐙 Openapi® Generic SDK

> **⚠️ This is a Reference Implementation** - pseudocode and reference materials only, not a functional SDK.
> For working SDKs, see language-specific SDKs below.
> | Languages |
> |:---------:|
> | [Java](https://github.com/openapi/openapi-generic-sdk/issues/1) &nbsp; [Kotlin](https://github.com/openapi/openapi-generic-sdk/issues/2) &nbsp; [JavaScript](https://github.com/openapi/openapi-nodejs-sdk) &nbsp; [TypeScript](https://github.com/openapi/openapi-nodejs-sdk) &nbsp; [Python](https://github.com/openapi/openapi-python-sdk) &nbsp; [PHP](https://github.com/openapi/openapi-php-sdk) &nbsp; [Go](https://github.com/openapi/openapi-go-sdk) &nbsp; [Rust](https://github.com/openapi/openapi-rust-sdk) <br> [C# / .NET](https://github.com/openapi/openapi-dotnet-sdk) &nbsp; [Ruby](https://github.com/openapi/openapi-generic-sdk/issues/3) &nbsp; [Swift](https://github.com/openapi/openapi-generic-sdk/issues/4) &nbsp; [Objective-C](https://github.com/openapi/openapi-generic-sdk/issues/5) &nbsp; [Shell / Bash](https://github.com/openapi/openapi-shell-sdk) &nbsp; [CLI Tools](https://github.com/openapi/openapi-cli) |


This repository contains a language-agnostic blueprint for implementing Openapi® client libraries. Also contains standardized patterns, test specifications, and reference implementation.

## Project Structure

```
src/                  # Pseudocode specifications (oauth_client, api_client, types)
tests/                # Test case specifications
examples/             # Usage examples
docs/                 # Implementation guide
reference/            # Rust reference implementation
```

## Core Components

- **OauthClient** - Token management with Basic auth (`username:api_key`)
- **ApiClient** - HTTP client with Bearer token auth
- **Types** - Standardized data structures and error handling

## Quick Example

```pseudocode
// 1. Generate a token
oauth = new OauthClient("username", "api_key", test=true)
token_response = oauth.create_token(["GET:test.imprese.openapi.it/advance"], 3600)
access_token = parse_json(token_response)["token"]

// 2. Make API calls
client = new ApiClient(access_token)
response = client.get("https://test.imprese.openapi.it/advance", {"denominazione": "altravia"})
```

## For SDK Developers

1. Study `src/*.pseudo` files as reference
2. Implement `OauthClient`, `ApiClient`, and type definitions
3. Follow the test cases in `tests/`
4. See `docs/implementation-guide.md` for detailed guidance

## License

MIT - See [LICENSE](LICENSE) for details.
