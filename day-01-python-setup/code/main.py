from pathlib import Path
import sys


def get_python_version() -> str:
    """Return the major.minor.patch version for the active Python interpreter."""
    version = sys.version_info
    return f"{version.major}.{version.minor}.{version.micro}"


def get_project_name() -> str:
    return Path.cwd().name


def build_setup_summary() -> list[str]:
    return [
        "AI Engineering Setup Check",
        f"Python: {get_python_version()}",
        f"Project: {get_project_name()}",
        "Status: ready for local Python lessons",
    ]


def main() -> None:
    for line in build_setup_summary():
        print(line)


if __name__ == "__main__":
    main()
