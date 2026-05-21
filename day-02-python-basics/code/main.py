from typing import TypedDict


class CloudAccount(TypedDict):
    account_id: str
    name: str
    owner_team: str
    monthly_cost_usd: float
    enabled_services: list[str]
    risk_flags: list[str]


ACCOUNTS: list[CloudAccount] = [
    {
        "account_id": "111111111111",
        "name": "prod-platform",
        "owner_team": "platform",
        "monthly_cost_usd": 825.30,
        "enabled_services": ["ec2", "s3", "cloudwatch", "iam"],
        "risk_flags": ["public-s3-bucket"],
    },
    {
        "account_id": "222222222222",
        "name": "dev-sandbox",
        "owner_team": "engineering",
        "monthly_cost_usd": 195.25,
        "enabled_services": ["ec2", "lambda", "s3"],
        "risk_flags": ["unused-access-keys", "no-budget-alert"],
    },
    {
        "account_id": "333333333333",
        "name": "prod-data",
        "owner_team": "data",
        "monthly_cost_usd": 640.20,
        "enabled_services": ["s3", "glue", "athena", "cloudwatch"],
        "risk_flags": [],
    },
]


def calculate_total_monthly_cost(accounts: list[CloudAccount]) -> float:
    total = 0.0

    for account in accounts:
        total += account["monthly_cost_usd"]

    return total


def find_accounts_over_budget(
    accounts: list[CloudAccount],
    budget_limit_usd: float,
) -> list[CloudAccount]:
    over_budget: list[CloudAccount] = []

    for account in accounts:
        if account["monthly_cost_usd"] > budget_limit_usd:
            over_budget.append(account)

    return over_budget


def find_accounts_with_risk_flags(accounts: list[CloudAccount]) -> list[CloudAccount]:
    flagged_accounts: list[CloudAccount] = []

    for account in accounts:
        if account["risk_flags"]:
            flagged_accounts.append(account)

    return flagged_accounts


def build_account_report(
    accounts: list[CloudAccount],
    budget_limit_usd: float,
) -> list[str]:
    total_cost = calculate_total_monthly_cost(accounts)
    over_budget = find_accounts_over_budget(accounts, budget_limit_usd)
    flagged_accounts = find_accounts_with_risk_flags(accounts)

    report_lines = [
        "AWS Account Inventory Report",
        f"Total monthly cost: ${total_cost:.2f}",
        f"Accounts over ${budget_limit_usd:.2f}: {len(over_budget)}",
    ]

    for account in over_budget:
        report_lines.append(
            f"- {account['name']} owned by {account['owner_team']}: "
            f"${account['monthly_cost_usd']:.2f}"
        )

    report_lines.append(f"Accounts with risk flags: {len(flagged_accounts)}")

    for account in flagged_accounts:
        risk_flags = ", ".join(account["risk_flags"])
        report_lines.append(f"- {account['name']}: {risk_flags}")

    return report_lines


def main() -> None:
    budget_limit_usd = 500.00

    for line in build_account_report(ACCOUNTS, budget_limit_usd):
        print(line)


if __name__ == "__main__":
    main()
