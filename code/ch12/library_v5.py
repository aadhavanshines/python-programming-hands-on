# Pocket Library, version 5: a Book class and a Library class.
import json
from pathlib import Path


class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_read(self):
        self.read = True

    def describe(self):
        mark = "x" if self.read else " "
        return f"[{mark}] {self.title} by {self.author} ({self.year})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "read": self.read,
        }


class Library:
    def __init__(self, path):
        self.path = Path(path)
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find(self, word):
        found = []
        for book in self.books:
            if word.lower() in book.title.lower():
                found.append(book)
        return found

    def unread(self):
        found = []
        for book in self.books:
            if not book.read:
                found.append(book)
        return found

    def save(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def load(self):
        self.books = []
        for item in json.loads(self.path.read_text(encoding="utf-8")):
            self.books.append(Book(**item))


library = Library("my_books.json")
library.add(Book("The Hobbit", "J. R. R. Tolkien", 1937, read=True))
library.add(Book("Dune", "Frank Herbert", 1965))
library.add(Book("Dune Messiah", "Frank Herbert", 1969))
library.save()

again = Library("my_books.json")
again.load()
for book in again.find("dune"):
    print(book.describe())
again.find("dune")[0].mark_read()
print("Unread:", len(again.unread()))
for book in again.books:
    print(book.describe())
