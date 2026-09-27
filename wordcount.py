"""Print the number of whitespace-separated words in IDEA.md, like `wc -w`."""
from pathlib import Path

print(len((Path(__file__).parent / "IDEA.md").read_text(encoding="utf-8").split()))
