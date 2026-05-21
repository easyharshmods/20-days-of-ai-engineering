from typing import Any


DEFAULT_MODEL = "llama3.2:3b"
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"


class LocalLlmError(Exception):
    pass


def build_generate_payload(prompt: str) -> dict[str, Any]:
    return {"model": DEFAULT_MODEL, "prompt": prompt, "stream": False}


def generate_answer(prompt: str) -> str:
    import requests

    try:
        response = requests.post(
            OLLAMA_GENERATE_URL,
            json=build_generate_payload(prompt),
            timeout=120,
        )
    except requests.RequestException as error:
        raise LocalLlmError(f"Could not reach Ollama: {error}") from error
    if response.status_code != 200:
        raise LocalLlmError(f"Ollama returned HTTP {response.status_code}")
    return response.json().get("response", "").strip()
