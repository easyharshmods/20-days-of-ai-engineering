# Python Basics for AI Engineering

## What we are building

Learn the Python concepts needed for AI apps.

## Why this matters for AI engineering

This is a focused module in **AI Engineering for DevOps Engineers**. It teaches one concept first, then discusses production trade-offs after the code runs.

## Concepts covered

- variables
- strings
- numbers
- lists
- dictionaries
- loops
- conditions
- functions
- files
- JSON
- one requests API call

## Folder structure

```text
01-python-foundation/
  README.md
  requirements.txt
  code/01_variables.py
  code/02_lists_and_dictionaries.py
  code/03_loops_and_conditions.py
  code/04_functions.py
  code/05_files_and_json.py
  code/06_api_call.py
```

## Prerequisites

- Python 3.13.13
- No Ollama required

## Setup

```bash
cd 01-python-foundation
uv venv .venv --python 3.13.13
source .venv/bin/activate              # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

When done:

```bash
deactivate
```

## Code walkthrough

Start with the simplest working version. Keep production hardening in the explanation rather than hiding the core idea behind abstractions.

## Run the project

```bash
python code/01_variables.py
python code/02_lists_and_dictionaries.py
python code/03_loops_and_conditions.py
python code/04_functions.py
python code/05_files_and_json.py
python code/06_api_call.py
```

## Expected output

Each script prints a small result that demonstrates one Python concept.

## Common issues and fixes

- Run commands from the module root.
- Activate `.venv` before running code.
- Install packages with `uv pip install -r requirements.txt`.
- If Ollama is used, confirm `ollama list` shows the required model.

## What would change in production

Add validation, logging, observability, auth, rate limits, CI/CD, and security controls only after the simple version is understood.

## Key takeaways

- Make it work first.
- Explain the result.
- Discuss production improvements last.

## Next step

Next, call a local LLM.
