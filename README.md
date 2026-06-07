# AI Engineering for DevOps Engineers

Practical AI engineering with Python, uv, Ollama, local LLMs, prompt engineering, Streamlit, RAG, FastAPI, Docker, and AWS production architecture.

This is a multi-part course, not necessarily a daily release schedule.

## Prerequisites
- Python 3.13.13 recommended. Python 3.14 may work, but Python 3.13 is safer for public AI/data dependency compatibility.
- uv
- VS Code
- Ollama

```bash
ollama pull llama3.2:3b
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

## Run Any Module
```bash
cd 02-first-local-llm
uv venv .venv --python 3.13.13
source .venv/bin/activate
uv pip install -r requirements.txt
python code/main.py
deactivate
```

## Course Roadmap
| # | Module | Goal | Length |
|---|---|---|---|
| 00 | [Course Setup: Python, uv, Ollama, VS Code, and Repo Structure](00-course-setup/README.md) | Prepare the environment and understand the repo. | 25-35 min |
| 01 | [Python Basics for AI Engineering](01-python-foundation/README.md) | Learn the Python concepts needed for AI apps. | 35-60 min |
| 02 | [Run Your First Local LLM with Ollama and Python](02-first-local-llm/README.md) | Make the simplest local LLM call. | 10-15 min |
| 03 | [Build a Reusable Ollama Client in Python](03-reusable-ollama-client/README.md) | Refactor the raw Ollama call into reusable files. | 15-20 min |
| 04 | [Prompt Engineering for Practical AI Apps](04-prompt-engineering/README.md) | Structure prompts for engineering workflows. | 15-20 min |
| 05 | [Build a Streamlit AI Chat App](05-streamlit-chat/README.md) | Build a simple Streamlit UI connected to Ollama. | 15-20 min |
| 06 | [Add Chat Memory to Your AI Assistant](06-chat-memory/README.md) | Add short-lived session memory. | 12-18 min |
| 07 | [Upload a File and Ask Questions Locally](07-file-upload-assistant/README.md) | Ask questions about uploaded text files. | 15-20 min |
| 08 | [Build a Local PDF Summarizer](08-pdf-summarizer/README.md) | Extract PDF text and summarize locally. | 15-25 min |
| 09 | [RAG Explained for DevOps Engineers](09-rag-explained/README.md) | Explain RAG before building it. | 12-18 min |
| 10 | [Text Chunking Explained with Python](10-text-chunking/README.md) | Split text into retrieval-friendly chunks. | 12-18 min |
| 11 | [Embeddings Explained with Local Models](11-embeddings/README.md) | Generate local embeddings and compare meaning. | 15-20 min |
| 12 | [Vector Search Explained from Scratch](12-vector-search/README.md) | Rank chunks by vector similarity. | 15-25 min |
| 13 | [Build a Tiny RAG Pipeline in Python](13-tiny-rag-pipeline/README.md) | Combine chunking, embeddings, retrieval, and prompting. | 20-30 min |
| 14 | [Build a Local RAG Assistant with Streamlit](14-local-rag-assistant/README.md) | Build a complete local RAG app. | 25-35 min |
| 15 | [Wrap Your AI App with FastAPI](15-fastapi-ai-api/README.md) | Expose AI logic as an HTTP API. | 15-25 min |
| 16 | [Dockerize Your Local AI API](16-dockerize-ai-api/README.md) | Package the AI API in Docker. | 15-25 min |
| 17 | [Add Config, Logging, and Error Handling](17-config-logging-errors/README.md) | Add production-minded improvements after the app works. | 15-25 min |
| 18 | [Map the Local AI App to AWS Production Architecture](18-aws-production-architecture/README.md) | Map local components to AWS services. | 20-30 min |
| 19 | [Evaluation, Observability, and Next Steps](19-next-steps/README.md) | Explain what comes after the beginner course. | 20-30 min |

## Playlist
GitHub repo: link in description.
