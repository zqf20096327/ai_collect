# Graal Script Agent

[![CI](https://github.com/graalvm/graal-script-agent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/graalvm/graal-script-agent/actions/workflows/ci.yml?query=branch%3Amain)
[![Maven Central](https://img.shields.io/maven-central/v/org.graalvm.scriptagent/scriptagent.svg?label=Maven%20Central)](https://central.sonatype.com/artifact/org.graalvm.scriptagent/scriptagent)
[![License: UPL 1.0](https://img.shields.io/badge/License-UPL%201.0-blue.svg)](LICENSE.md)

Graal Script Agent is an early-preview Java library for adding prompt-authored extensions to Java applications. Developers define where an application can be extended; users prompt for the behavior they need.

Unlike a regular coding agent, it produces reusable JavaScript or Python extensions rather than modifying a source repository. It is designed for bounded application behaviors such as searches, reports, routing rules, validation, and previewable workflows.

## How it works

The application defines a Java interface describing an extension point and the data and operations available to it. Given a user’s prompt, `ScriptAgent` guides a language model to implement that contract and returns a typed `Script<T>` that the application can inspect, store, and reuse.

The application binds the script to its own sandboxed GraalVM context and invokes it through the same Java interface. Execution is local and requires no further model call.

## Get started

Graal Script Agent artifacts are available from [Maven Central](https://central.sonatype.com/namespace/org.graalvm.scriptagent). See the latest [Getting Started guide](https://graalvm.github.io/graal-script-agent/latest/index.html#getting-started) for Maven and Gradle dependency setup, including model adapters and guest-language runtimes.

## Documentation

- [Getting Started](https://graalvm.github.io/graal-script-agent/latest/index.html#getting-started)
- [User manual](https://graalvm.github.io/graal-script-agent/latest/index.html)
- [API reference](https://graalvm.github.io/graal-script-agent/latest/javadocs/api/apidocs/index.html)
- [Complete example](examples/src/main/java/org/graalvm/scriptagent/examples/GettingStarted.java)
- [Release announcement: When prompts become plugins](https://medium.com/graalvm/when-prompts-become-plugins-34a737d30f54)

## Project

- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Release process](RELEASING.md)
- [License](LICENSE.md)

## Contributing Code

We welcome your code contributions. To get started, you will need to sign the Oracle Contributor Agreement (OCA). Only pull requests from committers that can be verified as having signed the OCA can be accepted.
