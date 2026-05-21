from typing import Literal, TypedDict


Role = Literal["user", "assistant"]


class ChatMessage(TypedDict):
    role: Role
    content: str


SYSTEM_INSTRUCTIONS = (
    "You are a practical AI engineering tutor for DevOps and cloud engineers. "
    "Answer clearly, explain trade-offs, and avoid hype."
)


def create_message(role: Role, content: str) -> ChatMessage:
    return {
        "role": role,
        "content": content.strip(),
    }


def build_chat_prompt(messages: list[ChatMessage], max_messages: int = 6) -> str:
    recent_messages = messages[-max_messages:]
    transcript_lines = [f"System: {SYSTEM_INSTRUCTIONS}", ""]

    for message in recent_messages:
        label = "User" if message["role"] == "user" else "Assistant"
        transcript_lines.append(f"{label}: {message['content']}")

    transcript_lines.append("")
    transcript_lines.append("Assistant:")
    return "\n".join(transcript_lines)
