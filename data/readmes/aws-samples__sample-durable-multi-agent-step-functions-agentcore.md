# Durable Multi-Agent Workflows with AWS Step Functions and Bedrock AgentCore

A sample "Product Discovery Assistant" demonstrating how to build durable multi-agent workflows using AWS Step Functions, Amazon Bedrock AgentCore, and the Strands Agents SDK.

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Key Patterns Demonstrated](#key-patterns-demonstrated)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Foundation Model Configuration](#foundation-model-configuration)
- [Running Tests](#running-tests)
- [Cleanup](#cleanup)
- [Security Considerations](#security-considerations)
- [Security Scan Suppressions](#security-scan-suppressions)
- [License](#license)

## Overview

This project implements a multi-session AI journey where a customer interacts with specialized agents to find electronic components for their design. The journey spans multiple sessions with pause/resume capability, demonstrating the hybrid value of:

- **AWS Step Functions**: Durable orchestration — pause for days, retry on failure, audit trail, exactly-once guarantees
- **Amazon Bedrock AgentCore**: Intelligent agent execution with long-term memory

### Architecture

The system orchestrates three specialized AI agents through a Step Functions state machine:

1. **RequirementsAgent** — Gathers customer design requirements (vehicle type, performance tier, powertrain, budget)
2. **SearchAgent** — Uses the Strands Graph pattern to coordinate catalog search, spec comparison, and recommendation sub-agents
3. **ValidationAgent** — Validates selected products against thermal, electrical, and compliance constraints

![Architecture diagram showing users connecting through Amazon API Gateway and AWS Lambda to AWS Step Functions, which orchestrates three specialized agents (RequirementsAgent, SearchAgent, ValidationAgent) running on Amazon Bedrock AgentCore, with Amazon DynamoDB for state storage and AgentCore Memory for cross-session context](./images/durable-agent-architecture.png)

Key features demonstrated:
- Pause/resume via callback tokens (zero-cost wait states)
- Cross-session memory via AgentCore Memory
- Exactly-once side effects for sample ordering
- DynamoDB-based journey tracking
- Production-grade error handling with retry policies

## How It Works

![AWS Step Functions state machine graph showing the workflow progression through RequirementsGathering, WaitForUser1, ProductSearch, WaitForUser2, DesignValidation, SampleRequest, and Complete states](images/stepfunctions_graph.svg)

1. **Start** — User submits design requirements via the UI or demo script
2. **RequirementsGathering** — The RequirementsAgent extracts structured specs from natural language
3. **Pause 1** — Workflow pauses; user can leave and return later (zero cost while waiting)
4. **ProductSearch** — The SearchAgent coordinates sub-agents to find matching products
5. **Pause 2** — Workflow pauses again for user review
6. **DesignValidation** — The ValidationAgent checks products against thermal/electrical/compliance constraints
7. **SampleRequest** — Exactly-once order submission to fulfilment system
8. **Complete** — Journey results are compiled and returned

## Key Patterns Demonstrated

| Pattern | Implementation |
|---------|---------------|
| Durable orchestration | Step Functions Standard workflow with 7 states |
| Zero-cost wait states | `.waitForTaskToken` callback pattern |
| Multi-agent collaboration | Strands Graph pattern within SearchAgent |
| Cross-session memory | AgentCore Memory with semantic + preference strategies |
| Exactly-once side effects | Idempotency key in DynamoDB |
| Production error handling | Retry with exponential backoff + catch blocks |

## Project Structure

```
├── agents/
│   ├── requirements-agent/   # Strands SDK agent for gathering requirements
│   ├── search-agent/         # Strands Graph pattern agent for product search
│   ├── validation-agent/     # Strands SDK agent for design validation
│   └── shared/               # Shared mock tools and utilities
├── step-function/
│   ├── state-machine.asl.json    # Step Functions ASL definition
│   ├── callback-handler/         # Lambda for pause/resume callback tokens
│   └── sample-request/           # Lambda for exactly-once sample ordering
├── infrastructure/
│   ├── template.yaml             # Pure CloudFormation template
│   └── deploy.sh                 # Single-command deployment script
├── ui/                           # Sample single-page web application
├── demo/
│   ├── start-journey.sh          # Start a new product discovery journey
│   └── resume-journey.sh         # Resume a paused journey
└── tests/                        # Integration and smoke tests
```

## Prerequisites

- Python 3.11+
- AWS CLI v2 configured with appropriate credentials
- Docker (for container builds)
- Node.js 18+ (for UI development)

### Cost Considerations

This sample application creates billable AWS resources including:

| Service | Billing Model |
|---------|--------------|
| AWS Lambda | Per invocation and duration |
| AWS Step Functions | Per state transition |
| Amazon DynamoDB | Storage and requests |
| Amazon API Gateway | Per API call |
| Amazon Bedrock AgentCore | Per invocation |
| Amazon CloudWatch Logs | Storage and ingestion |
| AWS KMS | Per key per month |
| Amazon ECR | Image storage |
| Amazon S3 | Object storage |

Estimated cost for testing: **$5–20** depending on usage. Remember to delete all resources after testing to avoid ongoing charges (see [Cleanup](#cleanup)).

## Quick Start

### 1. Install Python dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Create an S3 bucket for deployment artifacts

```bash
export DEPLOY_BUCKET="product-discovery-deploy-$(aws sts get-caller-identity --query Account --output text)-v2"
export AWS_REGION="${AWS_REGION:-us-east-1}"

aws s3 mb s3://$DEPLOY_BUCKET --region $AWS_REGION
```

### 3. Deploy infrastructure

```bash
cd infrastructure
chmod +x deploy.sh
./deploy.sh product-discovery-assistant $DEPLOY_BUCKET prod
```

Verify the deployment succeeded:

```bash
aws cloudformation describe-stacks \
  --stack-name product-discovery-assistant \
  --region $AWS_REGION \
  --query "Stacks[0].StackStatus" \
  --output text
```

You should see `CREATE_COMPLETE` or `UPDATE_COMPLETE`.

### 4. Run the demo

```bash
export API_URL=<api-gateway-url-from-deploy-output>

cd ../demo
./start-journey.sh

# Resume after the first pause
./resume-journey.sh <session-id>
```

### 5. Run the UI locally

```bash
cd ../ui
npm install
npm start
```

Open `http://localhost:3000` and set the **API Base URL** to match your deployment output.

**Sample prompts to try:**

- `I need a high-performance engine controller for an SUV, budget under $5000, prefer hybrid powertrain`
- `Looking for a battery pack and inverter for a compact electric vehicle, budget under $12000`
- `I need an engine controller for a truck, standard performance tier, diesel powertrain, budget $1000-$3000`

## Foundation Model Configuration

All three agents use **Claude Sonnet 4** (`us.anthropic.claude-sonnet-4-20250514-v1:0`) by default via the Strands SDK `BedrockModel`. This model requires a cross-region inference profile — the base model ID without a region prefix will not work.

To use a different model, set the `BEDROCK_MODEL_ID` environment variable on your AgentCore Runtime:

```bash
export BEDROCK_MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"  # Default (US regions)
export BEDROCK_MODEL_ID="eu.anthropic.claude-sonnet-4-20250514-v1:0"  # EU regions
export BEDROCK_MODEL_ID="us.anthropic.claude-haiku-4-20250514-v1:0"   # Cheaper alternative
```

Make sure the model is enabled in your AWS account via the Amazon Bedrock console (Model access) in the region you're deploying to.

> **Note:** Model availability changes over time. If a model ID returns an error, check the Amazon Bedrock console for the latest available models and update the `BEDROCK_MODEL_ID` parameter accordingly.

## Running Tests

```bash
# Unit and property tests (Python)
source .venv/bin/activate
MOCK_LATENCY_MS=0 pytest -v

# UI tests
cd ui
npm install
npm test
```

## Cleanup

To avoid ongoing AWS charges, delete all resources when you're done:

```bash
# Delete the CloudFormation stack
aws cloudformation delete-stack --stack-name product-discovery-assistant --region $AWS_REGION

# Wait for deletion to complete
aws cloudformation wait stack-delete-complete --stack-name product-discovery-assistant --region $AWS_REGION

# Delete ECR repos
for REPO in product-discovery-assistant-requirements-agent product-discovery-assistant-search-agent product-discovery-assistant-validation-agent; do
  aws ecr delete-repository --repository-name $REPO --force --region $AWS_REGION
done

# Empty and delete the S3 deployment bucket
aws s3 rm s3://$DEPLOY_BUCKET --recursive --region $AWS_REGION
aws s3 rb s3://$DEPLOY_BUCKET --region $AWS_REGION

# Unset exported environment variables
unset DEPLOY_BUCKET AWS_REGION API_URL
```

If you created the AgentCore Memory resource separately (via `setup-memory.sh`):

```bash
aws bedrock-agentcore list-memories --region $AWS_REGION
aws bedrock-agentcore delete-memory --memory-id <memory-id> --region $AWS_REGION
```

## Security Considerations

> ⚠️ **This is a sample/demo application.** The following items are intentional trade-offs for simplicity. For production deployments, address each one before going live.

### API Gateway Authentication

> ⚠️ **No authentication is configured.** All API endpoints are publicly accessible without any credentials.

The API Gateway endpoints use `AuthorizationType: NONE` — there is no authentication layer. This is intentional to simplify local testing and demonstration. **Anyone with the API URL can start journeys, resume sessions, and query status.**

**For production deployments, you must add an authentication layer before exposing this API.** Options include:

| Approach | Complexity | Best For |
|----------|-----------|----------|
| **Amazon Cognito User Pools** | Medium | Web/mobile apps with user sign-up/sign-in |
| **IAM authorization (SigV4)** | Low | Service-to-service or AWS-authenticated clients |
| **Lambda authorizer** | Medium–High | Custom token validation (JWT, OAuth, API tokens) |
| **API keys + usage plans** | Low | Rate-limiting machine-to-machine access |

**Recommended minimum for a public deployment:**

1. Create a Cognito User Pool and App Client
2. Add a Cognito Authorizer to the API Gateway
3. Change each method's `AuthorizationType` from `NONE` to `COGNITO_USER_POOLS`
4. Pass the `Authorization: Bearer <id_token>` header from the UI

See the [API Gateway access control documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) for detailed implementation guides.

### Dependency Version Pinning

All `requirements.txt` files pin dependencies to exact versions (`==`) matching the tested combination. When upgrading, test the full suite before updating pins.

### Lambda Event Logging

The `sample-request` Lambda handler logs structured metadata fields only. Avoid logging full event payloads from user-facing endpoints, as they may contain user-submitted data.

## Security Scan Suppressions

> The following security scan findings have been reviewed and suppressed as acceptable risks for a demonstration project. For production deployments, these should be re-evaluated.

> **Suppression mechanisms:** checkov uses `# checkov:skip=<ID>:<reason>` comments; cfn_nag uses `Metadata.cfn_nag.rules_to_suppress` blocks; bandit uses `# nosec <ID>` comments; semgrep uses `# nosemgrep: <rule-id>` comments. See each tool's documentation for details.

### Checkov

| Check ID | Severity | Reason |
|----------|----------|--------|
| CKV_AWS_117 | WARNING | Lambda VPC not required for blog sample |
| CKV_AWS_115 | WARNING | Concurrent execution limit not required for blog sample |
| CKV_AWS_173 | WARNING | Lambda env var encryption not required for blog sample |
| CKV_AWS_120 | WARNING | API Gateway caching not required for blog sample |
| CKV_AWS_59 | WARNING | Open API access intentional for demo (see [Security Considerations](#security-considerations)) |
| CKV_AWS_111 | WARNING | Wildcard resource intentional for demo IAM roles |
| CKV_DOCKER_2 | WARNING | Healthcheck not required for blog sample |

### cfn_nag

| Check ID | Severity | Reason |
|----------|----------|--------|
| W28 | WARNING | Explicit resource names intentional for demo |
| W89 | WARNING | Lambda VPC not required for blog sample |
| W92 | WARNING | ReservedConcurrentExecutions not required for blog sample |
| W11 | WARNING | Wildcard resource intentional for demo |
| W59 | WARNING | API Gateway auth NONE intentional for demo (see [Security Considerations](#security-considerations)) |
| W64 | WARNING | Usage plan not required for blog sample |
| W68 | WARNING | Usage plan not required for blog sample |

### Bandit

| Check ID | Severity | Reason |
|----------|----------|--------|
| B311 | INFO | Pseudo-random generators used for mock data, not security |
| B110 | INFO | Intentional error swallowing in non-critical memory operations |
| B603 | INFO | Subprocess calls in test infrastructure |
| B404 | INFO | Subprocess module import in test files |
| B103 | WARNING | Permissive chmod in deployment test tooling |
| B105 | INFO | Mock token test data, not real passwords |

### Semgrep

| Check ID | Severity | Reason |
|----------|----------|--------|
| logging-error-without-handling | WARNING | Error logged and re-raised intentionally |
| dockerfile-source-not-pinned | INFO | Acceptable for blog sample |
| unquoted-variable-expansion-in-command | INFO | Safe usage in controlled script |

### ACAT

No outstanding ACAT findings. The base image has been migrated from Docker Hub to ECR Public Gallery (`public.ecr.aws/docker/library/python:3.13-slim`).

## License

This library is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file.
