# Day 03 Content Package

## video_title

Files, JSON, and Config for AI Engineering - Day 03

## thumbnail_text

JSON + Config in Python

## description

In Day 03 of 20 Days of AI Engineering, we move from hardcoded Python data to files, JSON, and configuration.

We build a config-driven Python script that reads AWS-like account data from JSON, reads report settings from a config file, prints a summary, and writes a JSON report to an output file.

This matters because AI engineering workflows constantly deal with files: prompts, logs, uploaded documents, extracted text, API responses, and generated outputs.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why JSON matters
- 00:00 Review the sample files
- 00:00 Read JSON with Python
- 00:00 Build the report
- 00:00 Write JSON output
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Files, JSON, and Config for AI Engineering

## Hook

In cloud work, editing code every time a setting changes is usually a bad sign.

The same is true in AI engineering. Prompts, file paths, thresholds, and inputs should often be data or config, not hardcoded logic.

## Intro

Welcome to Day 03 of 20 Days of AI Engineering.

In Day 02, we processed AWS-like account data directly inside Python. Today we move that data into JSON files and make the script config-driven.

We will read account records from a sample file, read settings from a config file, build a report, and write the result back to JSON.

## Concept Explanation

JSON is one of the most common formats you will see as an AI engineer.

APIs return JSON. Cloud services often expose JSON. Many model runtimes accept or return JSON-shaped payloads.

In Python, JSON maps naturally to dictionaries and lists.

A JSON object becomes a dictionary. A JSON array becomes a list. Strings, numbers, booleans, and null values map to normal Python values.

The other concept today is config-driven behavior. Instead of changing Python code to adjust the budget threshold or output path, we put those settings in `sample/config.json`.

## Hands-on Build

Open the Day 03 folder.

In `sample/accounts.json`, we have account records with IDs, names, owner teams, monthly costs, services, and risk flags.

In `sample/config.json`, we define the budget limit, which risk flags are high priority, and where the output report should be written.

Now open `code/main.py`.

The `read_json_file` function opens a file with `with` and loads it using `json.load`.

The `write_json_file` function creates the output folder if needed and writes formatted JSON with `json.dump`.

The report function calculates the total monthly cost, finds accounts over budget, and finds accounts with high-priority risk flags from config.

Run the project with `python code/main.py`.

You should see a short console summary and a generated file at `output/account_report.json`.

## Production Thinking

In production, you would validate the JSON schema more carefully.

You would handle missing files, malformed JSON, missing keys, and permissions errors. You would also be careful about writing account or security data into logs or shared output locations.

For local teaching code, JSON files are useful because they make the data flow visible.

## Recap

Today we read JSON, wrote JSON, used config to control behavior, and generated an output file.

This is a practical foundation for the API, document, and RAG lessons coming later.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 03 locally, edit the config file, and see how the report changes without editing Python code.

## pinned_comment

Day 03 moves the account report from hardcoded data to JSON files and config-driven behavior. This is the foundation for later API responses, document processing, and AI workflow outputs.

## linkedin_post

Day 03 of my 20 Days of AI Engineering series is about files, JSON, and config.

The lesson takes AWS-like account data out of the Python file and moves it into JSON. The script reads account data, reads config, builds a report, and writes a JSON output file.

This is basic, but important. AI workflows still need clean data loading, config handling, and predictable outputs.

## learning_objectives

- Read JSON files with Python.
- Write JSON output with indentation.
- Use config values to control script behavior.
- Keep sample data outside application code.
- Generate output files inside the lesson folder.

## common_mistakes

- Running the script from the wrong folder.
- Using single quotes or trailing commas in JSON.
- Forgetting to create the output directory before writing a file.
- Hardcoding paths that only work on one machine.
- Mixing sample data, config, and code into one file.

## expected_output

```text
Config-driven account report
Total monthly cost: $1660.75
Accounts over budget: 2
High-priority risk accounts: 2
Wrote JSON report to output/account_report.json
```

