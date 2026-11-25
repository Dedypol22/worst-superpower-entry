"""It predicts last Tuesday's weather with perfect accuracy, which is just reporting history as tomorrow's news."""

import os
from pathlib import Path

LINE = "I can predict the future with 100% accuracy, but only last Tuesday's weather."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
Path(output_dir).mkdir(parents=True, exist_ok=True)
(Path(output_dir) / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(LINE)
