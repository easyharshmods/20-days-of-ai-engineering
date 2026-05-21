def build_engineering_explainer_prompt(topic: str) -> str:
    return (
        "You are teaching a DevOps engineer who is new to AI engineering.\n"
        f"Explain this topic in practical terms: {topic}\n\n"
        "Use this structure:\n"
        "1. Short definition\n"
        "2. Why it matters in production\n"
        "3. One concrete example"
    )
