# Day 20 - AI Engineering on AWS

## What we are building

Today we are mapping the local AI app to a production AWS architecture.

The lesson includes an architecture README, a small Python script that prints the proposed service map, and an optional starter IAM policy skeleton for least-privilege thinking.

## Why this matters for AI engineering

Local AI engineering teaches the application shape. Production AI engineering adds identity, networking, deployment, observability, cost controls, storage, and security boundaries.

## Concepts covered

- ECS Fargate
- EKS
- ALB
- S3
- CloudWatch
- Bedrock
- IAM
- Cost and security
- Least-privilege IAM

## Folder structure

```text
day-20-ai-engineering-on-aws/
  README.md
  requirements.txt
  sample/
    least_privilege_policy.json
  code/
    architecture_plan.py
```

## Prerequisites

- Python 3.14.5
- AWS account knowledge
- Basic understanding of Docker and FastAPI from Days 18-19

Local model pulls from earlier days:

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
ollama pull gemma4:latest
```

Day 20 discusses AWS production architecture. It does not deploy cloud resources by default.

## Setup

```bash
cd day-20-ai-engineering-on-aws
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`architecture_plan.py` models the AWS service choices as data and prints a readable architecture plan.

The sample IAM policy is intentionally narrow and illustrative. It shows the direction of least privilege rather than a copy-paste production policy.

## Run the project

```bash
python code/architecture_plan.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The script prints a local-to-AWS mapping:

- FastAPI container to ECS Fargate or EKS
- ALB for ingress
- S3 for document storage
- CloudWatch for logs and metrics
- Bedrock as the managed model runtime option
- IAM for least-privilege access

## Common issues and fixes

**Should I use ECS or EKS?**

Use ECS Fargate when you want simpler operations. Use EKS when your organization already has Kubernetes maturity or needs Kubernetes-specific controls.

**Should I use Bedrock or self-hosted models?**

Bedrock reduces model runtime operations. Self-hosting gives more control but adds infrastructure, scaling, and operational burden.

**Can I deploy this directly?**

No. This lesson is an architecture starting point, not a production deployment module.

## What would change in production

Production needs infrastructure as code, CI/CD, private networking, secrets management, least-privilege IAM, WAF rules, request logging, cost alarms, model evaluation, data retention policies, and incident runbooks.

Uploaded files may contain sensitive data. Store them with encryption, access controls, lifecycle policies, and audit trails.

## Key takeaways

- Local app architecture maps cleanly to AWS services.
- ECS Fargate is a pragmatic first deployment target.
- Bedrock is the managed model runtime option on AWS.
- S3 stores documents, but access control and retention matter.
- CloudWatch and IAM are part of the product, not afterthoughts.

## Next step

Use the 20-day repository as a portfolio project: polish the README, record the companion videos, and build one production-grade extension.
