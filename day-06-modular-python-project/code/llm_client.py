from typing import Any

from config import DEFAULT_MODEL, OLLAMA_GENERATE_URL, REQUEST_TIMEOUT_SECONDS


class LocalLlmError(Exception):
    pass


def build_generate_payload(prompt: str, model: str = DEFAULT_MODEL) -> dict[str, Any]:
    return {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }


def generate_text(prompt: str, model: str = DEFAULT_MODEL) -> str:
    import requests

    payload = build_generate_payload(prompt, model)

    try:
        response = requests.post(
            OLLAMA_GENERATE_URL,
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException as error:
        raise LocalLlmError(f"Could not reach Ollama: {error}") from error

    if response.status_code != 200:
        raise LocalLlmError(
            f"Ollama returned HTTP {response.status_code}: {response.text[:160]}"
        )

    response_data = response.json()
    return response_data.get("response", "").strip()
