import csv
from pathlib import Path

with open("books.csv", newline="", encoding="utf-8") as f:
    books = list(csv.DictReader(f))

print(f"{len(books)} books")
total_pages = 0
for book in books:
    total_pages += int(book["pages"])
    stars = "*" * int(book["rating"])
    print(f"{book['title']:<22}{book['pages']:>5} pages  {stars}")
print(f"Total: {total_pages} pages, average {total_pages / len(books):.0f}")

with open("favorites.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "rating"])
    for book in books:
        if book["rating"] == "5":
            writer.writerow([book["title"], book["rating"]])

print(Path("favorites.csv").read_text(encoding="utf-8"))
