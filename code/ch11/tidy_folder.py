# Sort the files in a folder into sub-folders by type.
from pathlib import Path

FOLDERS = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".xlsx": "documents",
    ".mp3": "music",
}

folder = Path("files_to_tidy")
for path in sorted(folder.iterdir()):
    if path.is_file():
        target = folder / FOLDERS.get(path.suffix.lower(), "other")
        target.mkdir(exist_ok=True)
        path.rename(target / path.name)
        print(f"{path.name:12} -> {target.name}/")

print()
for path in sorted(folder.rglob("*")):
    print(path.relative_to(folder))
