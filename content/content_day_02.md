# Day 02 Content Package

## video_title

Python Basics for Cloud Engineers - Day 02

## thumbnail_text

Python Basics for Cloud Engineers

## description

In Day 02 of 20 Days of AI Engineering, we use Python basics to process AWS-like account data.

This lesson covers variables, lists, dictionaries, loops, functions, and type hints through a practical operations report. We summarize account cost, identify accounts over budget, and list security or operations risk flags.

No LLM is called in this lesson. The goal is to build confidence with the Python data structures that later show up in prompts, API responses, document parsing, retrieval, and RAG pipelines.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Python data structures for cloud data
- 00:00 Account dictionaries
- 00:00 Loops and conditions
- 00:00 Functions and type hints
- 00:00 Run the report
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Python Basics for Cloud Engineers

## Hook

If you work in cloud or DevOps, you already deal with structured data every day: accounts, services, costs, alerts, logs, and configuration.

Python gives us a practical way to shape that data before we send it to an API, a dashboard, or eventually an AI model.

## Intro

Welcome to Day 02 of 20 Days of AI Engineering.

In Day 01, we set up Python and verified the local environment. Today we start writing useful Python.

We are going to build a small AWS account inventory report. It will calculate total monthly cost, find accounts over a budget threshold, and list accounts with risk flags.

## Concept Explanation

The main Python concepts today are variables, lists, dictionaries, loops, functions, and type hints.

A variable gives a name to a value.

A list holds multiple items.

A dictionary holds structured data with keys and values.

A loop lets us process every item in a list.

A function gives a name to a piece of logic we want to reuse.

Type hints help readers understand what kind of data a function expects and returns.

For a cloud engineer, this is like building an inventory report before making operational decisions.

## Hands-on Build

Open `code/main.py`.

We start with a `CloudAccount` type. It describes the shape of each account dictionary: account ID, name, owner team, monthly cost, enabled services, and risk flags.

Then we define a list called `ACCOUNTS`.

Each item in that list is one account. This looks similar to the kind of data you might get from an API or a configuration system.

Next we write `calculate_total_monthly_cost`. It starts with zero, loops over every account, and adds the monthly cost.

Then we write `find_accounts_over_budget`. It loops through the accounts and keeps only the ones above the budget limit.

After that, `find_accounts_with_risk_flags` checks which accounts have at least one risk flag.

Finally, `build_account_report` combines those helper functions and returns readable report lines.

Run the project with `python code/main.py`.

## Production Thinking

In production, this data would not be hardcoded.

You might pull it from AWS Organizations, Cost Explorer, Security Hub, a CMDB, or an internal platform API.

You would also add stronger tests, handle API errors, avoid logging sensitive details by default, and think carefully about who can see account metadata.

For this lesson, hardcoded data keeps the Python basics visible.

## Recap

Today we used Python to process cloud-style data.

We practiced lists, dictionaries, loops, conditions, functions, and type hints.

These basics matter because later AI apps still need normal data preparation before prompts, retrieval, and model calls become useful.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 02 locally, edit the account data, and watch how the report changes.

## pinned_comment

Day 02 uses AWS-like account data to practice Python basics: lists, dictionaries, loops, functions, and type hints. No LLM yet. This is the data handling foundation for later AI engineering work.

## linkedin_post

Day 02 of my 20 Days of AI Engineering series is about Python basics for cloud engineers.

I used AWS-like account data instead of abstract examples: account IDs, owner teams, monthly cost, services, and risk flags.

The lesson covers lists, dictionaries, loops, functions, and type hints. These are the same building blocks we will use later for prompts, API responses, document parsing, and RAG.

## learning_objectives

- Represent cloud account data with dictionaries.
- Store multiple records in a list.
- Use loops and conditions to process account data.
- Write small functions with type hints.
- Generate a readable operations report from structured data.

## common_mistakes

- Running commands from the repository root instead of the lesson folder.
- Forgetting that lists use numeric positions but dictionaries use keys.
- Mutating sample data when a function only needs to read it.
- Putting all logic inside `main()` instead of using helper functions.
- Skipping type hints that would make the data shape easier to understand.

## expected_output

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

