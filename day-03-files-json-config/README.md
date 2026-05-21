# Day 03 - Files, JSON, and Config

## What we are building

Today we are building a config-driven Python script.

Instead of hardcoding cloud account data inside Python, the script reads account records from `sample/accounts.json`, reads settings from `sample/config.json`, prints a report, and writes a JSON result to `output/account_report.json`.

This is the first step toward treating data and behavior as inputs instead of editing code for every change.

## Why this matters for AI engineering

AI apps constantly read and write files: prompts, logs, uploaded documents, extracted text, evaluation results, and configuration.

JSON is especially common because APIs, cloud services, and many model runtimes use it as the default structured format. If you can load JSON, validate the shape mentally, and write a clean output file, later lessons with APIs and local LLMs will feel much less mysterious.

The analogy for this lesson is moving from a shell one-liner to a repeatable runbook. The behavior should come from config, not from editing the script every time.

## Concepts covered

- Opening files with `with`
- Reading JSON with `json.load`
- Writing JSON with `json.dump`
- Using `pathlib.Path`
- Separating sample data from code
- Basic config-driven behavior
- Creating output directories

## Folder structure

```text
day-03-files-json-config/
  README.md
  requirements.txt
  sample/
    accounts.json
    config.json
  code/
    main.py
```

The script creates this file when it runs:

```text
output/account_report.json
```

## Prerequisites

- Python 3.14.5
- Basic Python lists, dictionaries, loops, and functions from Day 02

This lesson does not call an LLM. Later lessons use:

```bash
ollama pull llama3.2:3b
```

Optional more capable alternative model for later LLM lessons:

```bash
ollama pull gemma4:latest
```

## Setup

Run these commands from the repository root:

```bash
cd day-03-files-json-config
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`sample/accounts.json` contains AWS-like account records.

`sample/config.json` controls the report:

- the monthly budget limit
- which risk flags should be treated as high priority
- where to write the output file

`code/main.py` has small functions:

- `read_json_file()` loads JSON from disk.
- `write_json_file()` writes JSON with indentation.
- `build_account_report()` calculates cost and filters accounts.
- `main()` connects the config, input data, report, and output file.

This keeps the script easy to read and easy to change.

## Run the project

From inside `day-03-files-json-config`, with the virtual environment activated:

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The script should print:

```text
Config-driven account report
Total monthly cost: $1660.75
Accounts over budget: 2
High-priority risk accounts: 2
Wrote JSON report to output/account_report.json
```

The generated JSON file should include totals, over-budget accounts, and high-priority risk accounts.

## Common issues and fixes

**`FileNotFoundError` for `sample/accounts.json`**

Run the script from inside the lesson folder:

```bash
cd day-03-files-json-config
python code/main.py
```

**The output folder is missing**

That is okay. The script creates `output/` automatically.

**JSON syntax error**

JSON requires double quotes around keys and strings. It does not allow trailing commas.

## What would change in production

In production, you would validate input schemas more strictly, handle missing keys, log errors in a structured way, and avoid writing sensitive account data to broad-access locations.

You might also store config in environment variables, a parameter store, or a managed configuration service. For this lesson, local JSON files make the data flow easy to inspect.

## Key takeaways

- Keep data and config outside the Python code when behavior needs to change.
- Use `with` when reading and writing files.
- JSON maps naturally to Python dictionaries and lists.
- Generated files should go to a predictable output path.
- File paths should stay inside the lesson folder.

## Next step

In Day 04, we will call an HTTP API with Python and handle JSON responses from outside the local filesystem.
