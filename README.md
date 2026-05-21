# 20 Days of AI Engineering

**From DevOps Engineer to AI Engineer.**

A hands-on, practical, beginner-friendly series for cloud, DevOps, platform,
and AWS engineers transitioning into AI engineering and solution architecture.

Each day is a small, focused, fully runnable lesson. By day 20 you will have
gone from a local Python "hello world" to a containerized, document-aware
AI assistant mapped to a production AWS architecture.

---

## Who this is for

- Experienced DevOps, cloud, platform, or AWS engineers
- Engineers who understand infrastructure but are new to LLM applications
- Beginners in Python and GenAI who learn best by building

You do **not** need a GPU. Everything before Day 20 runs locally on a laptop
using [Ollama](https://ollama.com).

---

## What you will build

A progressive stack that ends in a production-shaped AI app:

- Days 1–4: Python and APIs for cloud engineers
- Days 5–10: Local LLM workflows, a chat UI, file and PDF assistants
- Days 11–17: Prompt engineering, chunking, embeddings, and a local RAG system
- Days 18–20: FastAPI, Docker, and an AWS production architecture

---

## Learning roadmap

| Day | Title                                  | Key concept                          | Output                                                  |
|-----|----------------------------------------|--------------------------------------|---------------------------------------------------------|
| 01  | Python Setup for AI Engineering        | pyenv, virtual environments, IDE     | A working Python "hello world" project                  |
| 02  | Python Basics for Cloud Engineers      | Variables, lists, dicts, functions   | A script processing AWS-like service/account data       |
| 03  | Files, JSON, and Config                | File I/O, JSON, config files         | A config-driven Python script                           |
| 04  | API Calls with Python                  | `requests`, HTTP, JSON               | A script that calls a public API                        |
| 05  | Local LLM with Ollama                  | Ollama, local LLM API                | A script that asks `llama3.2:3b` a question locally     |
| 06  | Modular Python Project                 | Modules, imports, separation         | A reusable local LLM client                             |
| 07  | Streamlit AI App                       | Streamlit, simple web UI             | A local web-based AI assistant                          |
| 08  | Chat UI and Session Memory             | `st.chat_*`, `st.session_state`      | A local chat assistant with memory                      |
| 09  | File Upload AI Assistant               | File upload, document Q&A            | An assistant that answers questions about text files    |
| 10  | PDF Summarizer                         | `pypdf`, text extraction             | A local PDF summarizer                                  |
| 11  | Prompt Engineering for Engineers       | Prompt templates, structured output  | A prompt-driven assistant with multiple modes           |
| 12  | Local Document Assistant               | Chat + files + PDFs combined         | A complete local document assistant                     |
| 13  | Introduction to RAG                    | Retrieval, generation, context       | A simple retrieval assistant (no vector DB yet)         |
| 14  | Text Chunking                          | Chunk size, overlap, metadata        | A chunking utility for documents                        |
| 15  | Embeddings Explained                   | Embeddings, semantic similarity      | A local similarity script using `nomic-embed-text`      |
| 16  | Vector Search                          | Vector search, top-k retrieval       | A numpy-based local vector search demo                  |
| 17  | Local RAG Assistant                    | Chunk + embed + retrieve + generate  | A local RAG app over uploaded documents                 |
| 18  | FastAPI Wrapper                        | FastAPI, request/response models     | A REST API around the local AI assistant                |
| 19  | Dockerize the AI App                   | Dockerfile, ports, local deploy      | A Dockerized AI application                             |
| 20  | AI Engineering on AWS                  | ECS, S3, Bedrock, IAM, cost          | Architecture README + optional starter deployment       |

---

## Prerequisites

- **Python 3.14.5** (managed with [`pyenv`](https://github.com/pyenv/pyenv) is recommended)
- **Ollama** installed and running: <https://ollama.com>
- An IDE: PyCharm or VS Code
- ~8 GB RAM minimum (the default model is small; the optional alternative model is heavier)

Pull the models used across the series:

```bash
ollama pull llama3.2:3b        # default LLM for all days
ollama pull nomic-embed-text   # embeddings, Days 15-17
```

Want a more capable alternative model? You can swap this one in wherever lessons call `llama3.2:3b`. Note it is heavier (~9.6 GB) and needs more RAM, not less:

```bash
ollama pull gemma4:latest
```

---

## How to run any lesson independently

Every lesson is fully self-contained. You can jump directly to any day.

```bash
cd day-XX-lesson-name
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Then run whatever the lesson uses:
python code/main.py                    # script lessons
streamlit run code/app.py              # Streamlit lessons
uvicorn code.api:app --reload          # FastAPI lessons
```

When you are done:

```bash
deactivate
rm -rf .venv
```

See [STANDARDS.md](STANDARDS.md) for the full convention.

---

## Recommended learning path

1. **Days 1–4** — Python, files, and APIs. Skip if you already know Python well.
2. **Days 5–10** — Local LLMs, Streamlit, and document workflows. Start here if
   you know Python but are new to LLM apps.
3. **Days 11–17** — Prompt engineering, embeddings, and RAG. The heart of the
   series.
4. **Days 18–20** — Production shape: API, Docker, AWS.

Each lesson takes roughly 30–60 minutes of hands-on time.

---

## YouTube series

Each lesson has a companion video.

> Playlist link: _coming soon_

---

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Spotted a bug or have a suggestion? Open an issue or PR. Keep changes scoped to
a single day where possible. Lessons must follow [STANDARDS.md](STANDARDS.md).
