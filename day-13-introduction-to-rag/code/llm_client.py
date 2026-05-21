from typing import Any

DEFAULT_MODEL = "llama3.2:3b"
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"
REQUEST_TIMEOUT_SECONDS = 90


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
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException as error:
        raise LocalLlmError(
            f"Could not reach Ollama at {OLLAMA_GENERATE_URL}: {error}. "
            f"Run `ollama serve` and `ollama pull {DEFAULT_MODEL}`."
        ) from error

    if response.status_code != 200:
        raise LocalLlmError(
            f"Ollama returned HTTP {response.status_code} from {OLLAMA_GENERATE_URL}: "
            f"{response.text[:160]}. Try `ollama pull {DEFAULT_MODEL}`."
        )

    return response.json().get("response", "").strip()
