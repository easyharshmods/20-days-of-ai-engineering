from os import getenv
from typing import Any


DEFAULT_MODEL = "llama3.2:3b"
OLLAMA_BASE_URL = getenv("OLLAMA_BASE_URL", "http://localhost:11434")


def build_generate_url() -> str:
    return f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"


def build_prompt(question: str) -> str:
    return f"Answer for a DevOps engineer with trade-offs:\n\n{question.strip()}"


def build_generate_payload(prompt: str) -> dict[str, Any]:
    return {"model": DEFAULT_MODEL, "prompt": prompt, "stream": False}


def answer_question(question: str) -> str:
    import requests

    response = requests.post(
        build_generate_url(),
        json=build_generate_payload(build_prompt(question)),
        timeout=90,
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()
