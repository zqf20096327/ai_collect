# mproxy

LLM API proxy with a built-in web admin panel.

## Usage

```
go build -o mproxy
./mproxy -listen :8080
```

The `-config` flag is optional (defaults to `config.json`). If no config
file exists it is created for you; fill it with your keys. `-listen`
overrides the listen address from the config.

Open `http://localhost:8080/admin` for the web panel.

Proxy endpoints:

```
POST /v1/chat/completions
POST /v1/messages
GET  /v1/models
```

## Screenshot

![screenshot](res/screenshot.png)

## License

CC BY 4.0 — see [LICENSE](LICENSE). Credit to [yasakei](https://github.com/yasakei).
