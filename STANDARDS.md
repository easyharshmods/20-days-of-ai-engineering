# STANDARDS

This file is the single source of truth for every lesson in this repository.
Every Day-XX lesson must follow these rules exactly. Do not deviate.

If you are writing a new lesson, read this file first.

---

## 1. Pinned environment

These versions and model tags are fixed. Do not introduce alternatives unless
the lesson explicitly says so.

| Item                    | Value                |
|-------------------------|----------------------|
| Python version          | `3.14.5`               |
| Package manager         | `pip`                |
| LLM runtime             | Ollama (local)       |
| Default LLM model       | `llama3.2:3b`        |
| Low-RAM fallback model  | `gemma2:2b`          |
| Embedding model         | `nomic-embed-text`   |

Rules:

- Every lesson that calls an LLM uses `llama3.2:3b`.
- Every lesson that needs embeddings uses `nomic-embed-text` via Ollama.
- Do **not** introduce `sentence-transformers`, `torch`, OpenAI, or any cloud
  LLM before Day 20.
- If a learner lacks RAM, the README points them at `gemma2:2b`.
- Lesson READMEs must show the exact pull command, e.g. `ollama pull llama3.2:3b`.
- Use `pip` and lesson-local `requirements.txt` files for dependency management.

---

## 2. Lesson folder standard

```
day-XX-lesson-name/
  README.md
  requirements.txt        # always present
  .env.example            # only when env vars are introduced
  sample/                 # only when sample input files are needed
  code/
    <runnable code files>
```

Locked decisions:

- `requirements.txt` lives at the **lesson root** (one level above `code/`).
- The virtual environment is created at the **lesson root** as `.venv`
  (never inside `code/`).
- All run commands are executed from the **lesson root**.
- This convention is identical for all 20 days.

---

## 3. Virtual environment strategy

Each lesson uses its own local virtual environment at the lesson root.

Why:

- Isolates per-lesson dependencies; no cross-day conflicts.
- Lets learners jump directly to any lesson and run it standalone.

Standard commands (copy-pasteable):

```bash
# Create and activate
cd day-XX-lesson-name
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run (pick the one the lesson uses)
python code/main.py                    # script lessons
streamlit run code/app.py              # Streamlit lessons
uvicorn code.api:app --reload          # FastAPI lessons

# Cleanup
deactivate
```

`.venv` is local and temporary. It is gitignored and never committed.
Delete it manually with `rm -rf .venv` if you want a fully clean folder.

---

## 4. The independence contract

**Independent lessons, progressive learning.**

- Each day is fully self-contained and runs on its own.
- A learner can jump directly to any day.
- Never require copying files from, editing, or assuming state from other lessons.
- Each day includes **all** the code it needs. Some duplication across days is
  fine and expected.
- Keep each day's code minimal and focused on that day's concept.
- Each README includes the exact commands to run from inside that folder.
- Prefer readability over clever abstractions. This is teaching code.

---

## 5. Coding standards

- Beginner-friendly Python with clear function names.
- `snake_case` for files, functions, variables. `PascalCase` for classes.
- Type hints where they aid understanding.
- Helpful, sparse comments. No line-by-line narration.
- Each lesson is small enough to cover in one video.
- Readability over cleverness.

---

## 6. Security requirements

- Never hardcode secrets or API keys.
- Never commit `.env`. It is in `.gitignore`. Provide `.env.example` instead.
- Explain local-only vs production security trade-offs.
- Note that uploaded files may contain sensitive data.
- AWS lessons use least-privilege IAM.

---

## 7. Lesson README template

Every lesson README must include these sections, in this order:

```markdown
# Day XX - Title

## What we are building

## Why this matters for AI engineering

## Concepts covered

## Folder structure

## Prerequisites
(Include exact `ollama pull` commands where relevant.)

## Setup
(The standard venv commands from section 3, copy-pasteable.)

## Code walkthrough

## Run the project

## Expected output

## Common issues and fixes

## What would change in production

## Key takeaways

## Next step
```

---

## 8. YouTube script template

Every `CONTENT.md` includes a script with these sections:

```markdown
# Video Title

## Hook
(Relates to a real DevOps / cloud problem.)

## Intro

## Concept Explanation
(Beginner-friendly. Explain what is being built before writing code.)

## Hands-on Build

## Production Thinking

## Recap

## CTA
(End with a GitHub repo CTA.)
```

---

## 9. Per-day deliverables

Every Day-XX folder must contain:

**Code and repo**

- `README.md` (using the lesson README template)
- Working, runnable Python code in `code/` with **no placeholders or TODOs**
- `requirements.txt` with pinned versions
- `.env.example` (only if env vars are used)
- Sample input files (only if needed)
- Sample files live inside that lesson folder only, usually under `sample/`.

**Content package** — written to a single file at the repo root:
`content/content_day_XX.md` (one file per day, kept outside the lesson folder
so the lesson stays focused on code and the docs/scripts live together).

- `video_title`
- `thumbnail_text`
- `description`
- `chapters` (timestamps as placeholders, e.g. `00:00`)
- `youtube_script` (using the YouTube script template)
- `pinned_comment`
- `linkedin_post` (short, first-person, engineer-sharing tone)
- `learning_objectives`
- `common_mistakes`
- `expected_output`

Content packaging style:

- Preferred series name: `20 Days of AI Engineering`.
- Acceptable alternate names: `From DevOps to AI Engineer`,
  `AI Engineering for Cloud Engineers`, `Local to Cloud GenAI`.
- Keep titles clear, tied to a real problem, hands-on, production-aware, and
  recap-friendly.

---

## 10. Verification checklist

Before considering a day done, confirm:

- The standard run commands work end-to-end (mentally trace them).
- Every `import` in the code is present in that lesson's `requirements.txt`.
- The README setup commands match the lesson folder standard exactly.
- No code references files outside its own day folder.
- Model and embedding tags match the pinned environment.
- The lesson is simple enough to execute live while recording without extra
  test files or hidden setup steps.

---

## 11. Generation workflow

Scaffold phase:

- Create root files: `README.md`, `STANDARDS.md`, `.gitignore`,
  `.python-version`, and `LICENSE`.
- Create all 20 lesson folders.
- Create the `content/` folder at the repo root.
- During scaffold only, each lesson folder contains a placeholder `README.md`
  with only the lesson title and `TODO`.
- Do not generate lesson code, `requirements.txt`, `.env.example`, `sample/`,
  or any `content/content_day_XX.md` files during scaffold.

Per-day phase:

- Generate lessons in small batches of 1-3 days.
- For each requested day, read this file first.
- Produce all per-day deliverables for that day.
- Verify the day using the checklist above.
- Commit that day with a clear message when requested by the workflow.
