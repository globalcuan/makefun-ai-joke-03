"""Write the competition joke to entry.txt.
The output directory is selected by MAKEFUN_OUTPUT_DIR.
"""

import os
from pathlib import Path


JOKE = "My coding agent works at machine speed: it did in nine seconds what takes me all day, then spent six hours waiting for me to click 'Approve.'"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
