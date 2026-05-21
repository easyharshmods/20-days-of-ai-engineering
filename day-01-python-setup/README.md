# Day 01 - Python Setup for AI Engineering

## What we are building

Today we are building the smallest possible Python project for this series: a runnable command-line program that prints a short AI engineering readiness message.

The goal is not to build an AI app yet. The goal is to confirm that Python, the project folder, the virtual environment, and the run command all work the same way they will work for the rest of the series.

Think of this like preparing a clean workstation before touching production infrastructure. If the shell, interpreter, and folder layout are predictable, every later lesson is easier to debug.

## Why this matters for AI engineering

AI engineering still starts with normal software engineering. Before we call a model, build a Streamlit app, or deploy anything to AWS, we need a reliable local Python setup.

For DevOps and cloud engineers, this is the same principle as pinning a runtime in a build pipeline. The app should run because the environment is known, not because it happens to work on one laptop.

## Concepts covered

- Python 3.14.5
- `pyenv` as a Python version manager
- Local virtual environments
- Project folder structure
- Running Python from the lesson root
- Keeping generated files out of Git

## Folder structure

```text
day-01-python-setup/
  README.md
  requirements.txt
  code/
    main.py
```

`requirements.txt` is at the lesson root. The virtual environment also lives at the lesson root as `.venv`.

## Prerequisites

- Python 3.14.5 installed locally
- `pyenv` recommended for managing Python versions
- PyCharm or VS Code
- A terminal

This lesson does not call an LLM and does not require Ollama yet. Later lessons use the pinned local model:

```bash
ollama pull llama3.2:3b
```

Later LLM lessons also mention an optional, more capable alternative model. It is heavier than the default and needs more RAM, not less:

```bash
ollama pull gemma4:latest
```

## Setup

Run these commands from the repository root:

```bash
cd day-01-python-setup
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The `requirements.txt` file is present even though this first lesson only uses the Python standard library. That keeps the setup convention identical across all 20 days.

## Code walkthrough

The project has one Python file:

- `code/main.py` contains the runnable lesson code.

`main.py` does three simple things:

1. Reads the Python version from the running interpreter.
2. Builds a small setup summary.
3. Prints that summary when the file is executed.

This gives you a quick confirmation that your terminal is using the virtual environment you created for this lesson.

## Run the project

From inside `day-01-python-setup`, with the virtual environment activated:

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The output should look like this:

```text
AI Engineering Setup Check
Python: 3.14.5
Project: day-01-python-setup
Status: ready for local Python lessons
```

## Common issues and fixes

**`python` points to the wrong version**

Run:

```bash
python --version
```

You should see Python 3.14.5. If not, install Python 3.14.5 with `pyenv` and set the version from the repository root.

**Virtual environment is not active**

Your shell prompt may show `(.venv)`. You can also check:

```bash
which python
```

It should point somewhere inside `day-01-python-setup/.venv`.

**Permission error activating the environment on Windows**

Use the Windows activation command shown in the setup section:

```bash
.venv\Scripts\activate
```

## What would change in production

For production systems, you normally do not rely on a manually activated virtual environment on a developer laptop.

You would usually pin the runtime in CI, a container image, or a deployment platform. Later in this series, we will package the app with Docker and map the local workflow to AWS. The local `.venv` is still useful because it gives each lesson a clean, isolated workspace.

## Key takeaways

- Every lesson in this repository runs from its own folder.
- Every lesson uses its own `.venv` at the lesson root.
- `requirements.txt` always lives beside the lesson README.
- Day 01 uses only the Python standard library.
- A predictable local setup prevents confusing failures later.

## Next step

In Day 02, we will use Python basics to process AWS-like account and service data.
