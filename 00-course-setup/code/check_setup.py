from pathlib import Path
import sys

print("AI Engineering Course Setup")
print(f"Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"Current folder: {Path.cwd().name}")
print("Next model to pull when needed: llama3.2:3b")
