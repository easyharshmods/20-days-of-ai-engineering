from llm_client import ask_ollama
from prompts import explain_for_engineers
print(ask_ollama(explain_for_engineers("API timeouts")))
