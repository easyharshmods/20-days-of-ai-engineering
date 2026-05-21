from typing import Any


OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3.2:3b"


class LocalLlmError(Exception):
    pass


def build_generate_payload(prompt: str, model: str = DEFAULT_MODEL) -> dict[str, Any]:
    return {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }


def generate_answer(prompt: str, model: str = DEFAULT_MODEL) -> str:
    import requests

    try:
        response = requests.post(
            OLLAMA_GENERATE_URL,
            json=build_generate_payload(prompt, model),
            timeout=120,
        )
    except requests.RequestException as error:
        raise LocalLlmError(f"Could not reach Ollama: {error}") from error

    if response.status_code != 200:
        raise LocalLlmError(
            f"Ollama returned HTTP {response.status_code}: {response.text[:160]}"
        )

    return response.json().get("response", "").strip()
