# Day 02 - Python Basics for Cloud Engineers

## What we are building

Today we are building a small Python script that reviews AWS-like account data and prints a simple operations report.

The script looks at account names, monthly spend, enabled services, and risk flags. It then summarizes which accounts need attention.

This is intentionally not an AI app yet. It is the Python foundation we will use before sending structured data into prompts, APIs, and local LLM workflows.

## Why this matters for AI engineering

AI applications often start with ordinary data: account metadata, logs, service lists, configuration files, API responses, and user input.

Before an engineer can build useful AI workflows, they need to be comfortable shaping that data in Python. Lists, dictionaries, loops, and functions show up everywhere: prompt construction, document parsing, retrieval pipelines, API handlers, and deployment scripts.

The analogy for this lesson is an inventory report. Before you automate decisions, you need a clear inventory of what exists and what needs attention.

## Concepts covered

- Variables
- Lists
- Dictionaries
- `for` loops
- Conditional logic
- Functions
- Type hints
- Formatting output for humans

## Folder structure

```text
day-02-python-basics/
  README.md
  requirements.txt
  code/
    main.py
```

## Prerequisites

- Python 3.14.5
- Day 01 setup knowledge, or equivalent comfort creating a virtual environment

This lesson does not call an LLM and does not require Ollama yet. Later lessons use:

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
cd day-02-python-basics
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`code/main.py` contains a small list of account dictionaries. Each dictionary represents one AWS-like account with:

- an account ID
- an owner team
- a monthly cost
- enabled services
- risk flags

The script uses functions to keep the logic readable:

- `calculate_total_monthly_cost()` adds cost across all accounts.
- `find_accounts_over_budget()` returns accounts above a budget threshold.
- `find_accounts_with_risk_flags()` returns accounts with security or operations flags.
- `build_account_report()` creates human-readable report lines.

The point is not to build a perfect cost tool. The point is to practice the Python building blocks used in later AI engineering lessons.

## Run the project

From inside `day-02-python-basics`, with the virtual environment activated:

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

You should see a report similar to:

```text
AWS Account Inventory Report
Total monthly cost: $1660.75
Accounts over $500.00: 2
- prod-platform owned by platform: $825.30
- prod-data owned by data: $640.20
Accounts with risk flags: 2
- prod-platform: public-s3-bucket
- dev-sandbox: unused-access-keys, no-budget-alert
```

## Common issues and fixes

Run the command from inside the lesson folder:

```bash
cd day-02-python-basics
```

**The virtual environment is not active**

Activate it again:

```bash
source .venv/bin/activate              # Windows: .venv\Scripts\activate
```

**The numbers look different after editing the data**

## What would change in production

In production, account data would usually come from APIs, AWS Organizations, Cost Explorer, Security Hub, or a configuration database.

You would also separate test data from application logic, add automated tests, handle API failures, and avoid printing sensitive account details to logs unless there is a clear operational reason.

For this lesson, hardcoded sample data is acceptable because it keeps the Python concepts visible.

## Key takeaways

- Lists are useful for collections of similar items.
- Dictionaries are useful for structured records.
- Loops let you process each item in a collection.
- Functions give names to repeatable pieces of logic.
- Type hints make beginner code easier to reason about.

## Next step

In Day 03, we will move the data out of the Python file and work with files, JSON, and configuration.
