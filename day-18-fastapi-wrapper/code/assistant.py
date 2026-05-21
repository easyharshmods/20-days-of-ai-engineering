from typing import Any


DEFAULT_MODEL = "llama3.2:3b"
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"


class AssistantError(Exception):
    pass


def build_prompt(question: str) -> str:
    return (
        "You are a practical AI engineering assistant for DevOps and cloud engineers.\n"
        "Answer clearly, include trade-offs, and keep the response concise.\n\n"
        f"Question: {question.strip()}"
    )


def build_generate_payload(prompt: str) -> dict[str, Any]:
    return {"model": DEFAULT_MODEL, "prompt": prompt, "stream": False}


def answer_question(question: str) -> str:
    import requests

    try:
        response = requests.post(
            OLLAMA_GENERATE_URL,
            json=build_generate_payload(build_prompt(question)),
            timeout=90,
        )
    except requests.RequestException as error:
        raise AssistantError(f"Could not reach Ollama: {error}") from error

    if response.status_code != 200:
        raise AssistantError(f"Ollama returned HTTP {response.status_code}")

    return response.json().get("response", "").strip()
