# Pocket Library, version 4: books are saved in library.json between runs.
import json
from pathlib import Path

DATA = Path("library.json")


def load_books():
    if not DATA.exists():
        return []
    try:
        return json.loads(DATA.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("library.json is damaged; starting with an empty library.")
        return []


def save_books(books):
    DATA.write_text(json.dumps(books, indent=2), encoding="utf-8")


def ask_year(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("  The year must be a number, such as 1997.")


books = load_books()
print(f"Loaded {len(books)} books.")
while True:
    title = input("New title (Enter to finish): ").strip()
    if not title:
        break
    author = input("Author: ").strip()
    year = ask_year("Year: ")
    books.append(
        {"title": title, "author": author, "year": year, "read": False}
    )

save_books(books)
print(f"Saved {len(books)} books to {DATA}.")
for book in books:
    print(f"- {book['title']} ({book['year']})")
