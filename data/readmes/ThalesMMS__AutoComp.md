# AutoComp

AutoComp is a macOS 14+ menu bar app for Apple Silicon Macs that suggests text in the active field. Press Tab to accept the next word or the backtick key to accept the full suggestion.

## Run

```sh
./script/build_and_run.sh --verify
```

Grant Accessibility access during setup. Screen Recording is optional. Choose a backend in Settings > Model.

- **Remote OpenAI-compatible** sends autocomplete text to the configured endpoint.
- **Apple Intelligence** uses FoundationModels on supported systems.
- **Local Llama** runs in-process with a GGUF model and the optional llama.cpp runtime.

Remote fallback is opt-in. Settings > Privacy shows when autocomplete text may be sent off the Mac and controls access to optional context.

For a Local Llama build, run `./script/check_llama_pkg_config.sh` and build with `AUTOCOMP_ENABLE_LLAMA_RUNTIME=1`. You can also supply both `AUTOCOMP_LLAMA_CFLAGS` and `AUTOCOMP_LLAMA_LIBS` explicitly. Set the model path in Settings or via `AUTOCOMP_LOCAL_MODEL_PATH`.

For a development bundle without embedded `.env.local` settings, set `AUTOCOMP_EMBED_ENV_LOCAL=0` when running the build script.

## Development

Run `swift test` or `./script/ci_headless.sh`. Use `./script/release_build.sh --dry-run --version 0.0.0 --build 0` to verify the release plan. Use `./script/uninstall.sh --dry-run` to preview the files and settings removed by the uninstall script.

## License

[Apache 2.0](LICENSE)
