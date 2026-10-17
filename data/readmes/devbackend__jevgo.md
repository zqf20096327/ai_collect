# jevgo

Go client for the [TypeSafe AI](https://docs.typesafe.ai) System One API (`jev` models).

> **Unofficial.** This is an independent community SDK. It is not affiliated with, endorsed by,
> or supported by TypeSafe. "TypeSafe" and "Jev" are names of their respective owners.
> For the official SDKs see [Python](https://github.com/typesafe-ai/typesafe-sdk-python)
> and [JavaScript](https://github.com/typesafe-ai/typesafe-sdk-js).

Send a `state` and a map of typed questions (Noul, Choice, Score), get typed answers back — in one call.
The library imports only the standard library (testify is used in tests only).

```sh
go get github.com/devbackend/jevgo
```

Requires Go 1.24 or later.

## Quick start

```go
client, err := jevgo.New() // reads TYPESAFE_API_KEY
if err != nil {
	log.Fatal(err)
}

resp, err := client.SystemOne(ctx, jevgo.SystemOneRequest{
	State: "Help! My payouts have been failing for 3 days.",
	Questions: jevgo.Questions{
		"is_urgent": jevgo.Noul("Does this convey urgency?").
			WithCriteria("Explicitly time-sensitive", "No urgency expressed"),
		"department": jevgo.Choice("Which team should handle this?", map[string]any{
			"billing":   "Payments, invoicing, refunds",
			"technical": "Bugs, outages, integrations",
			"sales":     nil,
		}),
		"frustration": jevgo.ScoreOf("How frustrated is the customer?", "Calm", "Frustrated", "Very angry"),
	},
})
if err != nil {
	log.Fatal(err)
}

urgent, _ := resp.Answers.Noul("is_urgent")        // urgent.Noul == 0.95
dept, _ := resp.Answers.Choice("department")       // dept.Choice, dept.Probabilities, dept.Confidence
frustration, _ := resp.Answers.Score("frustration") // frustration.Score, .Level(), .Legend
```

`resp.Model` is the versioned model that answered (e.g. `jev-1.13.0`), `resp.Usage` holds token counts,
`resp.RequestID` the `x-typesafe-request-id` header.

## Questions

| Constructor | Wire type | Answer |
|---|---|---|
| `Noul(instructions)` / `.WithCriteria(yes, no)` | `noul` | `NoulAnswer{Noul}` — probability of "yes" |
| `Choice(instructions, map[string]any)` / `ChoiceOf(instructions, options...)` | `choice` | `ChoiceAnswer{Choice, Probabilities, Confidence}` |
| `Score(instructions, levels...)` / `ScoreOf(instructions, levels...)` | `score` | `ScoreAnswer{Score, Legend, Probabilities, Confidence}` |

`State`, instructions and every criteria description accept any JSON-encodable value — a string, map, slice
or struct — so you can pass [structured](https://docs.typesafe.ai/primitives/advanced) data:

```go
jevgo.Noul(map[string]any{
	"potential_duplicate": map[string]any{"name": "John Smith", "location": "Oakland, California"},
	"question":            "Is the resume for the same person as `potential_duplicate`?",
})
```

Answers of a type this SDK version does not know decode into `UnknownAnswer` with the raw JSON,
so a new server-side primitive never breaks existing code.

## Configuration

| Option | Env variable | Default |
|---|---|---|
| `WithAPIKey` | `TYPESAFE_API_KEY` | required |
| `WithBaseURL` | `TYPESAFE_BASE_URL` | `https://api.typesafe.ai` |
| `WithDefaultModel` | `TYPESAFE_DEFAULT_MODEL` | `jev-latest` |
| `WithTimeout` | — | 10s per attempt |
| `WithRetryPolicy` | — | `DefaultRetryPolicy()` |
| `WithHTTPClient`, `WithHeaders`, `WithLogger` | — | — |

Explicit options win over environment variables. Per-call overrides:
`WithRequestTimeout`, `WithRequestRetryPolicy`, `WithRequestHeaders`.

## Retries

`DefaultRetryPolicy()` matches the official SDKs: 2 retries, exponential backoff 0.5s → 5s with 25% jitter,
retries on 408, 429 and 5xx (including `529 Overloaded`), connection errors and per-attempt timeouts,
honors `Retry-After` / `retry-after-ms` up to 60s, and stops once the total 30s budget would be exceeded.

```go
policy := jevgo.DefaultRetryPolicy()
policy.MaxRetries = 5
client, _ := jevgo.New(jevgo.WithRetryPolicy(policy))

// disable retries for one call
client.SystemOne(ctx, req, jevgo.WithRequestRetryPolicy(jevgo.RetryPolicy{}))
```

## Errors

HTTP failures are `*jevgo.APIError` (status, body, headers, request id, `RetryAfter`) and match sentinels via `errors.Is`:

```go
_, err := client.SystemOne(ctx, req)
switch {
case errors.Is(err, jevgo.ErrRateLimited): // 429
case errors.Is(err, jevgo.ErrOverloaded): // 529
case errors.Is(err, jevgo.ErrUnprocessableEntity): // 422, see apiErr.Body for the offending field
case errors.Is(err, jevgo.ErrAuthentication): // 401
case errors.Is(err, jevgo.ErrTimeout), errors.Is(err, jevgo.ErrConnection):
}

var apiErr *jevgo.APIError
if errors.As(err, &apiErr) {
	log.Printf("status=%d request_id=%s body=%s", apiErr.StatusCode, apiErr.RequestID, apiErr.Body)
}
```

## Models

```go
models, err := client.ListModels(ctx)
for _, m := range models.Models {
	fmt.Println(m.Name, m.ReleaseDate, m.Description)
}
```

## Testing

```sh
go test -short ./...                                  # unit tests only, no network
set -a; source .env; set +a; go test ./...            # plus integration tests against the live API
```

Integration tests spend tokens on the key's account and are skipped when `-short` is passed
or `TYPESAFE_API_KEY` is unset. Keep the key in `.env` (`TYPESAFE_API_KEY=...`), which is gitignored.

## License

[MIT](LICENSE). The software is provided "as is", without warranty of any kind.
