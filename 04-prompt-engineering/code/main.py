import requests

prompt = """You are helping a DevOps team review an incident.
Context: checkout-api returned 500 errors after deployment.
Task: summarize impact, likely cause, and follow-up actions.
Output: concise bullets.
"""
payload = {"model": "llama3.2:3b", "prompt": prompt, "stream": False}
response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=60)
response.raise_for_status()
print(response.json()["response"])
