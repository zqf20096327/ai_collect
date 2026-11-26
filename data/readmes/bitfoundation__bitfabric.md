<p align="center">
  <img src="src/Fabric/src/Client/Bit.Fabric.Client.Core/wwwroot/images/bit-logo.svg" alt="bit Fabric" width="72" />
</p>

<h1 align="center">bit Fabric</h1>

<p align="center"><b>Build with AI. Own everything.</b></p>

<p align="center"><a href="https://bitfabric.co">bitfabric.co</a></p>

---

This repository holds the three parts of bit Fabric:

| Folder | What it is | Ships as |
|---|---|---|
| [`src/Fabric`](src/Fabric) | bit Fabric itself: the site and app at bitfabric.co, its server, and the Workbench | bitfabric.co |
| [`src/Cli`](src/Cli) | bit CLI: creates a project, sets it up on any computer, makes its keys and keeps it up to date | [`Bit.Cli`](https://www.nuget.org/packages/Bit.Cli) on nuget.org |
| [`src/Boilerplate`](src/Boilerplate) | bit Boilerplate: the project template `bit new` starts from | [`Bit.Boilerplate`](https://www.nuget.org/packages/Bit.Boilerplate) on nuget.org |

The UI libraries they build on, such as bit BlazorUI and bit Butil, live in
[bitfoundation/bitplatform](https://github.com/bitfoundation/bitplatform) under MIT. Report a problem with a library
there, and a problem with bit Fabric, bit CLI or the template here.

## Building

Each part has a `global.json` above it that names its .NET SDK.

```sh
# bit Fabric (Aspire runs the server, the web app and their services)
cd src/Fabric && bit setup && aspire start

# bit CLI and its tests
dotnet build src/Cli/Bit.Cli.slnx && dotnet test --project src/Cli/Tests/Bit.Cli.Tests

# bit Boilerplate: pack the template, then make a project from this checkout
dotnet pack src/Boilerplate/Bit.Boilerplate.ProjectTemplate.csproj -c Release -o packages
bit new MyApp --template-package src/Boilerplate/Bit.Boilerplate
```

The workflows in `.github/workflows` build and test each part on every pull request.

## License

Source-available under the [Fair Core License 1.0, MIT Future License](LICENSE.md) (FCL-1.0-MIT). You may use, change
and share the code for any purpose except a competing product, and each version becomes MIT two years after it is
released. The lines at the top of the license say how it applies to the apps you build with bit Fabric: they are yours.
