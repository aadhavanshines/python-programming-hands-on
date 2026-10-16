# Report what a folder tree contains: files per type, total size,
# the biggest files, and files with the same contents.
import hashlib
from collections import Counter, defaultdict
from pathlib import Path

root = Path("documents")
files = sorted(p for p in root.rglob("*") if p.is_file())

by_type = Counter(p.suffix or "(none)" for p in files)
total = sum(p.stat().st_size for p in files)
print(f"{len(files)} files, {total} bytes in {root}/")
for suffix, count in by_type.most_common():
    print(f"  {suffix:6} {count}")

print("Largest files:")
for p in sorted(files, key=lambda p: p.stat().st_size, reverse=True)[:3]:
    print(f"  {p.stat().st_size:5} bytes  {p.relative_to(root)}")

# Same contents = same fingerprint (hash), whatever the file is called
groups = defaultdict(list)
for p in files:
    groups[hashlib.sha256(p.read_bytes()).hexdigest()].append(
        p.relative_to(root)
    )
for same in groups.values():
    if len(same) > 1:
        print("Duplicates:", ", ".join(str(p) for p in same))
