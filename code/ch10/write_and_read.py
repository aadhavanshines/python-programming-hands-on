from pathlib import Path

notes = Path("notes.txt")

notes.write_text("Buy bread\nCall the plumber\n", encoding="utf-8")
with notes.open("a", encoding="utf-8") as f:  # "a" adds to the end
    f.write("Return library books\n")

print(notes.read_text(encoding="utf-8"))

with notes.open(encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.rstrip())

print("Exists?", notes.exists(), "| Size:", notes.stat().st_size, "bytes")
