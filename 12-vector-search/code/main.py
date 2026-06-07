import numpy as np

records = [
    {"text": "retry backoff", "vector": np.array([1.0, 0.0])},
    {"text": "cost review", "vector": np.array([0.0, 1.0])},
]
query = np.array([1.0, 0.1])

for record in records:
    record["score"] = float(
        np.dot(query, record["vector"]) / (np.linalg.norm(query) * np.linalg.norm(record["vector"]))
    )

for record in sorted(records, key=lambda item: item["score"], reverse=True):
    print(round(record["score"], 3), record["text"])
