# Run Pocket Library from the command line, exactly as you would type it.
import shlex
import subprocess
import sys

commands = [
    'add "Dune" "Frank Herbert" --year 1965',
    'add "Children of Dune" "Frank Herbert" --year 1976',
    'add "Emma" "Jane Austen" --year 1815',
    'add "Educated" "Tara Westover" --year 2018',
    'add "Dune" "Frank Herbert"',
    "read 1 --date 2026-09-14 --rating 5",
    "read 4 --date 2026-10-02 --rating 4",
    "list",
    "list --unread",
    "list --search austen",
    "read 9 --date 2026-10-15",
    "read 2 --date 2026-02-30",
    "stats",
    "export books.csv",
]
for command in commands:
    print(f"$ python -m pocket {command}")
    result = subprocess.run(
        [sys.executable, "-m", "pocket", *shlex.split(command)],
        capture_output=True,
        text=True,
    )
    print(result.stdout + result.stderr, end="")
