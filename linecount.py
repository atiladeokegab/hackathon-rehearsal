"""Print the line count of HACKATHON.md, like `wc -l`."""
import sys
from pathlib import Path

try:
    text = (Path(__file__).parent / "HACKATHON.md").read_text(encoding="utf-8")
except FileNotFoundError:
    sys.exit("HACKATHON.md not found")  # message to stderr, exit status 1
print(text.count("\n"))
