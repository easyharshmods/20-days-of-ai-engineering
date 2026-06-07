import requests

payload = {"model": "llama3.2:3b", "prompt": "Explain virtual environments to a DevOps engineer in three bullets.", "stream": False}
response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=60)
response.raise_for_status()
print(response.json()["response"])
