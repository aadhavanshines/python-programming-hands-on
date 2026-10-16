import json
from pathlib import Path

settings = {
    "theme": "dark",
    "font_size": 14,
    "recent": ["notes.txt", "todo.txt"],
}

Path("settings.json").write_text(
    json.dumps(settings, indent=2), encoding="utf-8"
)
print(Path("settings.json").read_text(encoding="utf-8"))

loaded = json.loads(Path("settings.json").read_text(encoding="utf-8"))
print(loaded["recent"][0], loaded["font_size"] + 2)
