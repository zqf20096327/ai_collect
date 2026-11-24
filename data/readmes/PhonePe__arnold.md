# PhonePe Arnold

AI-assisted code review for GitLab and GitHub. <br>Arnold gives reviewers a merge-request workspace (diffs, discussions,
draft reviews, a personal merge queue, review stats) and runs AI review workflows that post inline suggestions back to
the merge request or pull request.

**Documentation:** <https://phonepe.github.io/arnold>

![An Arnold AI review comment inline on a merge request diff](docs/docs/assets/screenshots/ai-comment-assessment.png)

## Quick start

Requires Docker (or Podman) with Compose.

```bash
git clone https://github.com/PhonePe/arnold.git && cd arnold
cp deploy/.env.example .env      # set GitLab/GitHub and LLM values as needed
docker compose up
```

Open <http://localhost:3000>. The quick start uses development authentication and a local review worker; do not expose
it as is.

## Deployment

Releases publish signed images to GitHub Container Registry:

```bash
docker pull ghcr.io/phonepe/arnold-server:v1.0.0
docker pull ghcr.io/phonepe/arnold-ui:v1.0.0
docker pull ghcr.io/phonepe/arnold-runner:v1.0.0
```

| Concern        | Configuration                                                                       |
|----------------|-------------------------------------------------------------------------------------|
| Sign-in        | UI `auth.providers`; backend `auth.jwt.issuers`                                     |
| GitLab         | Backend `gitlabConfiguration` (OAuth application, `api` scope)                      |
| GitHub         | Backend `githubConfiguration` (GitHub App)                                          |
| Review runners | Backend `runner.mode`: `LOCAL`, `GITLAB` or `GITHUB`                                |
| Storage        | Aerospike (state); Elasticsearch (analytics, optional)                              |

Reference configs: [backend](arnold-backend/arnold-server/config/local.yml),
[UI](arnold-ui/config/production.example.yaml). Secrets are read from environment variables. See the
[production guide](https://phonepe.github.io/arnold/setup/production/) for the full checklist.

## Documentation

- [Documentation site](https://phonepe.github.io/arnold) (source in [docs/](docs/docs/index.md))
- Module guides: [backend](arnold-backend/BACKEND.md), [UI](arnold-ui/README.md), [runner](arnold-runner/README.md)
- [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

## License

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
