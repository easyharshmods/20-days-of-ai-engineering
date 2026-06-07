from pathlib import Path
import json

items = json.loads(Path("sample/aws_architecture.json").read_text(encoding="utf-8"))
for item in items:
    print(f"{item['local']} -> {item['aws']}")
