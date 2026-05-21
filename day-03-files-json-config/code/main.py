from pathlib import Path
from typing import Any
import json


def read_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")


def find_high_priority_risks(
    accounts: list[dict[str, Any]],
    high_priority_risk_flags: list[str],
) -> list[dict[str, Any]]:
    high_priority_accounts = []
    high_priority_set = set(high_priority_risk_flags)

    for account in accounts:
        matching_flags = [
            flag
            for flag in account["risk_flags"]
            if flag in high_priority_set
        ]

        if matching_flags:
            high_priority_accounts.append(
                {
                    "account_id": account["account_id"],
                    "name": account["name"],
                    "owner_team": account["owner_team"],
                    "matching_risk_flags": matching_flags,
                }
            )

    return high_priority_accounts


def build_account_report(
    accounts: list[dict[str, Any]],
    config: dict[str, Any],
) -> dict[str, Any]:
    budget_limit_usd = float(config["budget_limit_usd"])
    total_monthly_cost = sum(
        float(account["monthly_cost_usd"])
        for account in accounts
    )

    accounts_over_budget = [
        {
            "account_id": account["account_id"],
            "name": account["name"],
            "owner_team": account["owner_team"],
            "monthly_cost_usd": account["monthly_cost_usd"],
        }
        for account in accounts
        if float(account["monthly_cost_usd"]) > budget_limit_usd
    ]

    high_priority_risk_accounts = find_high_priority_risks(
        accounts,
        config["high_priority_risk_flags"],
    )

    return {
        "total_monthly_cost_usd": round(total_monthly_cost, 2),
        "budget_limit_usd": budget_limit_usd,
        "accounts_over_budget": accounts_over_budget,
        "high_priority_risk_accounts": high_priority_risk_accounts,
    }


def build_console_summary(report: dict[str, Any], output_file: Path) -> list[str]:
    return [
        "Config-driven account report",
        f"Total monthly cost: ${report['total_monthly_cost_usd']:.2f}",
        f"Accounts over budget: {len(report['accounts_over_budget'])}",
        "High-priority risk accounts: "
        f"{len(report['high_priority_risk_accounts'])}",
        f"Wrote JSON report to {output_file}",
    ]


def main() -> None:
    lesson_root = Path.cwd()
    accounts = read_json_file(lesson_root / "sample" / "accounts.json")
    config = read_json_file(lesson_root / "sample" / "config.json")
    output_file = lesson_root / config["output_file"]

    report = build_account_report(accounts, config)
    write_json_file(output_file, report)

    for line in build_console_summary(report, Path(config["output_file"])):
        print(line)


if __name__ == "__main__":
    main()
