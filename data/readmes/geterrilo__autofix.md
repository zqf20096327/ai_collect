# Errilo Auto-fix

Fix production errors with an AI agent, straight from GitHub Actions. When [Errilo](https://errilo.com) reports a new issue or a regression, the agent ([Claude Code](https://github.com/anthropics/claude-code-action) by default) reads it through the Errilo MCP server, reproduces it with a failing test and fixes it. The action then opens a pull request and marks the issue "resolved in the next release".

The agent runs on your own Anthropic account. Errilo charges nothing for the MCP server or for this action, on every plan.

## How it works

One action, four steps, used in three jobs of your workflow so that the agent never holds a token that can write to your repository:

| Step           | Job          | GitHub token | What it does                                                  |
| -------------- | ------------ | ------------ | ------------------------------------------------------------- |
| `check`        | check        | read         | Decides whether the issue should be fixed.                    |
| `prepare`      | fix          | read         | Writes the agent's MCP configuration and instructions.        |
| `export`       | fix          | read         | After the agent: exports its commits as a patch.              |
| `pull-request` | pull-request | write        | Pushes `errilo/fix-<id>`, opens the PR, updates Errilo.       |

## Quick start

1. Copy [`examples/errilo-autofix.yml`](examples/errilo-autofix.yml) to `.github/workflows/` on your default branch, and replace the setup steps of the `fix` job with your project's.
2. Add the secrets `ANTHROPIC_API_KEY` and `ERRILO_TOKEN`, and the variable `ERRILO_ORG`.
3. In Errilo, create an alert rule with the **GitHub** channel, triggers **New issue** and **Regression**.

```yaml
- uses: geterrilo/autofix@v1
  with:
    step: check
    errilo-token: ${{ secrets.ERRILO_TOKEN }}
    errilo-org: ${{ vars.ERRILO_ORG }}
```

Requires Actions Runner v2.327.1 or later (GitHub-hosted runners are always up to date).

## Documentation

- [Setup](docs/setup.md): requirements, releases, tokens, alert, first run
- [Inputs and outputs](docs/reference.md), and how to use another agent
- [Security](docs/security.md): why three jobs, safeguards
- [Cost and limits](docs/cost-and-limits.md)

## License

[MIT](LICENSE)
