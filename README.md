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

