from typing import Any


GITHUB_REPOSITORY_API_URL = "https://api.github.com/repos/ollama/ollama"


class ApiError(Exception):
    pass


def fetch_repository(url: str = GITHUB_REPOSITORY_API_URL) -> dict[str, Any]:
    import requests

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as error:
        raise ApiError(f"Request failed: {error}") from error

    if response.status_code != 200:
        raise ApiError(
            f"API returned HTTP {response.status_code}: {response.text[:120]}"
        )

    return response.json()


def build_repository_summary(repository: dict[str, Any]) -> dict[str, Any]:
    return {
        "full_name": repository["full_name"],
        "description": repository.get("description") or "No description provided",
        "stars": repository["stargazers_count"],
        "forks": repository["forks_count"],
        "open_issues": repository["open_issues_count"],
        "default_branch": repository["default_branch"],
    }


def format_summary(summary: dict[str, Any]) -> list[str]:
    return [
        "GitHub Repository Summary",
        f"Repository: {summary['full_name']}",
        f"Description: {summary['description']}",
        f"Stars: {summary['stars']}",
        f"Forks: {summary['forks']}",
        f"Open issues: {summary['open_issues']}",
        f"Default branch: {summary['default_branch']}",
    ]


def main() -> None:
    try:
        repository = fetch_repository()
        summary = build_repository_summary(repository)
    except ApiError as error:
        print(f"Could not fetch repository data: {error}")
        return

    for line in format_summary(summary):
        print(line)


if __name__ == "__main__":
    main()
