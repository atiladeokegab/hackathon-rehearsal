"""Print the number of whitespace-separated words in IDEA.md, like `wc -w`."""
import sys
from pathlib import Path

try:
    text = (Path(__file__).parent / "IDEA.md").read_text(encoding="utf-8")
except FileNotFoundError:
    sys.exit("IDEA.md not found")  # message to stderr, exit status 1
print(len(text.split()))
