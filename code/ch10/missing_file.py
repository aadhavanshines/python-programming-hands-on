from pathlib import Path

path = Path("does_not_exist.txt")
try:
    text = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"No file called {path.name}; starting with an empty list.")
    text = ""
print("Lines:", len(text.splitlines()))

# The same again, without try: the program stops with a traceback
path.read_text(encoding="utf-8")
