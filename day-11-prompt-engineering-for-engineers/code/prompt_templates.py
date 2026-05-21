from typing import Literal


PromptMode = Literal["aws_explainer", "terraform_reviewer", "incident_summarizer"]


def build_aws_explainer_prompt(topic: str) -> str:
    return (
        "You are an AI engineering tutor for AWS and DevOps engineers.\n"
        f"Explain this AWS topic: {topic.strip()}\n\n"
        "Return:\n"
        "1. Plain-English definition\n"
        "2. Why it matters for AI systems\n"
        "3. Production trade-off\n"
        "4. One practical example"
    )


def build_terraform_reviewer_prompt(terraform_text: str) -> str:
    return (
        "You are reviewing Terraform for a platform engineering team.\n"
        "Focus on security, reliability, and operational clarity.\n\n"
        "Terraform:\n"
        "-----\n"
        f"{terraform_text.strip()}\n"
        "-----\n\n"
        "Return:\n"
        "1. What looks reasonable\n"
        "2. Risks or missing controls\n"
        "3. Suggested improvements"
    )


def build_incident_summarizer_prompt(notes: str) -> str:
    return (
        "You are summarizing incident notes for an engineering post-incident review.\n"
        "Be factual and avoid blame.\n\n"
        "Notes:\n"
        "-----\n"
        f"{notes.strip()}\n"
        "-----\n\n"
        "Return:\n"
        "1. Impact\n"
        "2. Likely cause\n"
        "3. Timeline highlights\n"
        "4. Follow-up actions"
    )


def build_prompt(mode: PromptMode, input_text: str) -> str:
    if mode == "aws_explainer":
        return build_aws_explainer_prompt(input_text)
    if mode == "terraform_reviewer":
        return build_terraform_reviewer_prompt(input_text)
    if mode == "incident_summarizer":
        return build_incident_summarizer_prompt(input_text)
    raise ValueError(f"Unsupported prompt mode: {mode}")
