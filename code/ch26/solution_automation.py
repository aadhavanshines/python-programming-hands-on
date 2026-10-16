# Solutions to the Chapter 26 exercises.
import re
from collections import Counter
from pathlib import Path


# Exercise 1: summarize a log file by level, and list the error messages
def log_summary(path):
    levels = Counter()
    errors = Counter()
    pattern = re.compile(r"^\S+ \S+ (INFO|WARNING|ERROR) (.*)$")
    for line in Path(path).read_text().splitlines():
        match = pattern.match(line)
        if match:
            level, text = match.groups()
            levels[level] += 1
            if level == "ERROR":
                errors[text] += 1
    return levels, errors


levels, errors = log_summary("app.log")
print(dict(levels))
for text, count in errors.most_common():
    print(f"  {count} x {text}")


# Exercise 2: sort files into folders by type, with a dry run first
FOLDERS = {
    ".pdf": "documents",
    ".txt": "documents",
    ".jpg": "pictures",
    ".xlsx": "spreadsheets",
}


def sort_by_type(folder, apply=False):
    moves = []
    for path in sorted(Path(folder).iterdir()):
        if path.is_file():
            target = (
                Path(folder)
                / FOLDERS.get(path.suffix.lower(), "other")
                / path.name
            )
            moves.append((path, target))
            if apply:
                target.parent.mkdir(exist_ok=True)
                path.rename(target)
    return moves


for old, new in sort_by_type("downloads"):
    print(f"  {old.name} -> {new.parent.name}/")
sort_by_type("downloads", apply=True)
for path in sorted(Path("downloads").rglob("*")):
    if path.is_file():
        print("  ", path.relative_to("downloads").as_posix())


# Exercise 3: the reading log as a text table, widest value sets the width
def text_table(rows):
    widths = {k: max(len(k), *(len(r[k]) for r in rows)) for k in rows[0]}
    lines = ["  ".join(k.ljust(w) for k, w in widths.items()).rstrip()]
    lines.append("  ".join("-" * w for w in widths.values()))
    for r in rows:
        lines.append(
            "  ".join(r[k].ljust(w) for k, w in widths.items()).rstrip()
        )
    return "\n".join(lines)


import csv  # noqa: E402  (imported here to keep each exercise together)

with open("reading_log.csv", newline="") as f:
    print(text_table(list(csv.DictReader(f))[:3]))
