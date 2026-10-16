# Zip a folder into backups/, named by date, and keep only the newest three.
import zipfile
from datetime import date, timedelta
from pathlib import Path

SOURCE = Path("documents")
BACKUPS = Path("backups")
KEEP = 3


def make_backup(day):
    """Zip SOURCE into backups/; None if today's backup already exists."""
    BACKUPS.mkdir(exist_ok=True)
    target = BACKUPS / f"documents-{day.isoformat()}.zip"
    if target.exists():  # never overwrite a backup silently
        return None
    with zipfile.ZipFile(
        target, "w", compression=zipfile.ZIP_DEFLATED
    ) as zf:
        for path in sorted(SOURCE.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(SOURCE.parent))
    return target


def remove_old_backups():
    # ISO dates (2026-10-15) sort in time order
    backups = sorted(BACKUPS.glob("documents-*.zip"))
    for old in backups[:-KEEP]:
        old.unlink()
        print("  removed", old.name)


# Pretend the script ran on five days in a row
# (normally you would use date.today()), then run again on the last day
start = date(2026, 10, 11)
days = [start + timedelta(days=n) for n in range(5)]
for day in [*days, days[-1]]:
    target = make_backup(day)
    if target is None:
        print("Skipped: a backup for", day, "already exists")
        continue
    print("Created", target.name)
    last = target
    remove_old_backups()

print("Kept:")
for path in sorted(BACKUPS.iterdir()):
    print("  ", path.name)
with zipfile.ZipFile(last) as zf:
    print(f"{last.name} contains {len(zf.namelist())} files:")
    for name in zf.namelist():
        print("  ", name)
    print("Archive test:", zf.testzip() or "all files OK")
