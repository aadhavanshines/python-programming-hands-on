# Give messy file names a tidy form: lower case, hyphens instead of
# spaces, no brackets. Shows the plan first, and changes nothing
# until you add --apply.
import argparse
import re
from pathlib import Path


def tidy(name):
    stem, suffix = Path(name).stem, Path(name).suffix.lower()
    stem = stem.lower()
    stem = re.sub(r"[()\[\]]", "", stem)  # drop brackets
    # Spaces and underscores become one hyphen
    stem = re.sub(r"[\s_]+", "-", stem.strip())
    return stem + suffix


def plan_renames(folder):
    plan, taken = [], {p.name for p in folder.iterdir()}
    for path in sorted(folder.iterdir()):
        if not path.is_file():  # leave folders alone
            continue
        new_name = tidy(path.name)
        if new_name == path.name:
            continue
        if new_name in taken:  # never overwrite another file
            print(f"  skip {path.name!r}: {new_name!r} already exists")
            continue
        taken.add(new_name)
        plan.append((path, path.with_name(new_name)))
    return plan


parser = argparse.ArgumentParser(
    description="Tidy the file names in a folder."
)
parser.add_argument("folder", type=Path)
parser.add_argument(
    "--apply",
    action="store_true",
    help="really rename (default: only show)",
)
args = parser.parse_args()

plan = plan_renames(args.folder)
for old, new in plan:
    print(f"  {old.name!r:28} -> {new.name!r}")
if args.apply:
    for old, new in plan:
        old.rename(new)
    print(f"Renamed {len(plan)} files.")
else:
    print(f"{len(plan)} files would be renamed. Add --apply to do it.")
