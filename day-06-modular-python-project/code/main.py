from config import DEFAULT_MODEL
from llm_client import LocalLlmError, generate_text
from prompts import build_engineering_explainer_prompt


def format_output(topic: str, answer: str) -> list[str]:
    return [
        "Local LLM engineering explainer",
        f"Model: {DEFAULT_MODEL}",
        f"Topic: {topic}",
        "",
        answer,
    ]


def main() -> None:
    topic = "why timeouts matter in API clients"
    prompt = build_engineering_explainer_prompt(topic)

    try:
        answer = generate_text(prompt)
    except LocalLlmError as error:
        print(f"LLM call failed: {error}")
        return

    for line in format_output(topic, answer):
        print(line)


if __name__ == "__main__":
    main()
