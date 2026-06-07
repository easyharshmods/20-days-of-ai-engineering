from pathlib import Path
import json
service = {"name": "checkout-api", "risk": "retry storm"}
path = Path("output/service.json")
path.parent.mkdir(exist_ok=True)
path.write_text(json.dumps(service, indent=2), encoding="utf-8")
print(json.loads(path.read_text(encoding="utf-8"))["risk"])
