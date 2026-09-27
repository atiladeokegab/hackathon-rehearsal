"""Print whole minutes left until the "code freeze" deadline in HACKATHON.md."""
import re
from datetime import datetime, timezone
from pathlib import Path

text = (Path(__file__).parent / "HACKATHON.md").read_text()
when = re.search(r"^\|\s*code freeze\s*\|\s*(\S+)\s*\|", text, re.M | re.I).group(1)
freeze = datetime.fromisoformat(when)
print(int((freeze - datetime.now(timezone.utc)).total_seconds() // 60))
