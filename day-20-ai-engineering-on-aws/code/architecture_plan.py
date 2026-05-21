from typing import TypedDict


class ArchitectureComponent(TypedDict):
    local_component: str
    aws_service: str
    reason: str
    production_note: str


ARCHITECTURE: list[ArchitectureComponent] = [
    {
        "local_component": "FastAPI app container",
        "aws_service": "ECS Fargate",
        "reason": "Runs containers without managing servers.",
        "production_note": "Use private subnets, autoscaling, health checks, and deployment rollbacks.",
    },
    {
        "local_component": "HTTP API ingress",
        "aws_service": "Application Load Balancer",
        "reason": "Routes HTTPS traffic to the service.",
        "production_note": "Add TLS, WAF rules, access logs, and request size limits.",
    },
    {
        "local_component": "Uploaded documents",
        "aws_service": "S3",
        "reason": "Durable object storage for source documents.",
        "production_note": "Use encryption, bucket policies, lifecycle rules, and per-tenant prefixes.",
    },
    {
        "local_component": "Logs and metrics",
        "aws_service": "CloudWatch",
        "reason": "Central place for app logs, metrics, and alarms.",
        "production_note": "Track latency, errors, model failures, token usage, and cost signals.",
    },
    {
        "local_component": "Local model runtime",
        "aws_service": "Bedrock",
        "reason": "Managed foundation model runtime option on AWS.",
        "production_note": "Evaluate model quality, cost, latency, region availability, and data policy.",
    },
    {
        "local_component": "Local permissions",
        "aws_service": "IAM",
        "reason": "Defines what the app can access.",
        "production_note": "Use task roles and least-privilege policies scoped to exact resources.",
    },
]


def build_architecture_summary(components: list[ArchitectureComponent]) -> list[str]:
    lines = ["AI Engineering on AWS - Architecture Map"]
    for component in components:
        lines.append(
            f"- {component['local_component']} -> {component['aws_service']}: "
            f"{component['reason']}"
        )
    return lines


def main() -> None:
    for line in build_architecture_summary(ARCHITECTURE):
        print(line)


if __name__ == "__main__":
    main()
