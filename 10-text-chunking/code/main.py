text = "Rollback starts by identifying the previous stable version. Pause deployments. Deploy previous artifact. Watch metrics."
words = text.split()
start = 0
size = 8
overlap = 2
chunk_number = 1

while start < len(words):
    print(f"chunk-{chunk_number}:", " ".join(words[start:start + size]))
    if start + size >= len(words):
        break
    start = start + size - overlap
    chunk_number += 1
