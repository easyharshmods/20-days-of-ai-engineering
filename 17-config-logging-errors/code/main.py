import logging
import os
import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
model = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

try:
    logging.info("calling %s", model)
    response = requests.post(
        f"{base_url}/api/generate",
        json={"model": model, "prompt": "Why does logging matter in AI services?", "stream": False},
        timeout=60,
    )
    response.raise_for_status()
except requests.RequestException as error:
    logging.error("request failed: %s", error)
else:
    print(response.json()["response"])
