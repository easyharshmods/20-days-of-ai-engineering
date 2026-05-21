# Day 01 Content Package

## video_title

Python Setup for AI Engineering - Day 01

## thumbnail_text

Python Setup for AI Engineers

## description

In Day 01 of 20 Days of AI Engineering, we set up the local Python foundation for the series. This lesson is for DevOps, cloud, platform, and AWS engineers who want a predictable Python workflow before building LLM apps.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why setup matters
- 00:00 Create the virtual environment
- 00:00 Walk through the code
- 00:00 Run the script
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Python Setup for AI Engineering

## Hook

If you have ever debugged a failed deployment only to find out the build agent used a different runtime, you already understand why setup matters.

AI engineering has the same problem. Before we call a model, build a UI, or deploy anything to AWS, we need a Python environment that is predictable.

## Intro

Welcome to Day 01 of 20 Days of AI Engineering.

This series is for DevOps, cloud, platform, and AWS engineers who want to move into AI engineering without skipping the software engineering basics.

Today we are not building a chatbot. We are building the local foundation that every later lesson will reuse: a lesson folder, a virtual environment, a requirements file, and a small Python script that confirms the setup works.

## Concept Explanation

Think of the local Python setup like a clean build runner.

The Python version is the runtime. The virtual environment is the isolated dependency boundary. The lesson folder is the unit of work.

In this repository, every day runs independently. That means you can jump directly to Day 07 or Day 15 later without copying files from previous lessons.

For that to work, every lesson follows the same convention: create `.venv` at the lesson root, install from `requirements.txt`, and run commands from inside that lesson folder.

## Hands-on Build

Start from the repository root and move into the Day 01 folder.

Create the virtual environment with `python -m venv .venv`.

Activate it with `source .venv/bin/activate` on macOS or Linux. On Windows, use `.venv\Scripts\activate`.

Then run `pip install -r requirements.txt`.

For Day 01, there are no third-party packages. The file still exists because the convention matters. Later lessons will add packages like Streamlit, requests, pypdf, FastAPI, and boto3.

Now open `code/main.py`.

The script reads the active Python version, gets the current project folder name, builds a short setup summary, and prints it.

Run it with `python code/main.py`.

You should see a setup check showing Python 3.14.5 and the Day 01 project folder.

## Production Thinking

In production, we usually do not depend on a manually activated `.venv`.

We pin runtime versions in CI, Docker images, deployment pipelines, or managed platforms. But the principle is the same: make the runtime explicit.

The local virtual environment is a teaching-friendly version of that idea. It keeps dependencies isolated and prevents one lesson from quietly breaking another.

## Recap

Today we set up the baseline Python workflow for the series.

That is enough foundation to start writing useful Python in Day 02.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Clone the repo, run Day 01 locally, and use the same setup pattern for the rest of the series.

## pinned_comment

## linkedin_post

I started a 20-day AI engineering series for DevOps, cloud, platform, and AWS engineers.

The main idea: AI engineering still needs boring, repeatable software engineering foundations.

## learning_objectives

- Set up a lesson-local Python virtual environment.
- Understand why each lesson is self-contained.
- Run a Python script from the lesson root.
- Connect local setup discipline to production runtime discipline.

## common_mistakes

- Creating `.venv` inside `code/` instead of the lesson root.
- Running commands from the repository root instead of the lesson folder.
- Forgetting to activate the virtual environment.
- Using a Python version other than 3.14.5.
- Deleting `requirements.txt` because the first lesson has no third-party packages.

## expected_output

```text
AI Engineering Setup Check
Python: 3.14.5
Project: day-01-python-setup
Status: ready for local Python lessons
```
