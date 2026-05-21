from typing import Any


OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3.2:3b"


class LocalLlmError(Exception):
    pass


def build_ollama_payload(prompt: str, model: str = DEFAULT_MODEL) -> dict[str, Any]:
    return {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }


def ask_ollama(prompt: str, model: str = DEFAULT_MODEL) -> str:
    import requests

    payload = build_ollama_payload(prompt, model)

    try:
        response = requests.post(OLLAMA_GENERATE_URL, json=payload, timeout=60)
    except requests.RequestException as error:
        raise LocalLlmError(f"Could not reach Ollama: {error}") from error

    if response.status_code != 200:
        raise LocalLlmError(
            f"Ollama returned HTTP {response.status_code}: {response.text[:160]}"
        )

    response_data = response.json()
    return response_data.get("response", "").strip()


def format_response(answer: str, model: str = DEFAULT_MODEL) -> list[str]:
    return [
        "Local LLM response",
        f"Model: {model}",
        "",
        answer,
    ]


def main() -> None:
    prompt = (
        "Explain virtual environments to a DevOps engineer "
        "in three practical bullets."
    )

    try:
        answer = ask_ollama(prompt)
    except LocalLlmError as error:
        print(f"LLM call failed: {error}")
        return

    for line in format_response(answer):
        print(line)


if __name__ == "__main__":
    main()
