# Run tidy_names.py twice: first to see the plan, then to apply it.
import subprocess
import sys
from pathlib import Path

for extra in ([], ["--apply"]):
    command = ["tidy_names.py", "downloads", *extra]
    print("$ python", " ".join(command))
    subprocess.run([sys.executable, *command])
print("Now in downloads:")
for path in sorted(Path("downloads").iterdir()):
    print("  ", path.name)
