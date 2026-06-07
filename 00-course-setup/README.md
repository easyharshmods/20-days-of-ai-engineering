# Course Setup: Python, uv, Ollama, VS Code, and Repo Structure

## What we are building

We prepare the local environment for the course and verify that Python, uv, VS Code, and Ollama are ready.

## Why this matters for AI engineering

Most AI app failures during learning are environment failures. A predictable local setup makes every later module easier to record, debug, and explain.

## Concepts covered

- Python 3.13.13
- uv virtual environments
- VS Code workflow
- Ollama installation
- model pulls
- repo structure
- troubleshooting basics

## Folder structure

```text
00-course-setup/
  README.md
  requirements.txt
  code/check_setup.py
```

## Prerequisites

- Python 3.13.13 recommended
- uv installed
- VS Code installed
- Ollama installed

Pull models when needed later:

```bash
ollama pull llama3.2:3b
ollama pull llama3.2:1b        # lower-RAM fallback
ollama pull nomic-embed-text
```

## Setup

```bash
cd 00-course-setup
uv venv .venv --python 3.13.13
source .venv/bin/activate              # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

When done:

```bash
deactivate
```

## Code walkthrough

`code/check_setup.py` prints the Python version and current folder. It is intentionally tiny so the setup is the focus.

## Run the project

```bash
python code/check_setup.py
```

## Expected output

A short environment summary prints in the terminal.

## Common issues and fixes

- If `uv` is missing, install uv first.
- If Ollama is missing, install and start Ollama before model modules.
- If the Python version is unavailable, install Python 3.13.13 with pyenv or your preferred tool.

## What would change in production

Production runtimes are pinned in CI, Docker images, deployment manifests, and IaC. Local setup still matters because it keeps the learning path stable.

## Key takeaways

- Use Python 3.13.13 for the course.
- Use uv for virtual environments.
- Pull Ollama models only when the module needs them.

## Next step

Continue to `01-python-foundation`.
