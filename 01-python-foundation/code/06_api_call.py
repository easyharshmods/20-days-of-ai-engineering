import requests
response = requests.get("https://api.github.com/repos/ollama/ollama", timeout=10)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data["full_name"])
