from pathlib import Path

from llm_client import LocalLlmError, generate_answer
from prompt_templates import build_prompt


def main() -> None:
    terraform_text = Path("sample/terraform_snippet.txt").read_text(encoding="utf-8")
    prompt = build_prompt("terraform_reviewer", terraform_text)

    try:
        answer = generate_answer(prompt)
    except LocalLlmError as error:
        print(f"LLM call failed: {error}")
        return

    print("Prompt mode: terraform_reviewer")
    print(answer)


if __name__ == "__main__":
    main()
