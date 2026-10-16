# Pocket Library, version 6: a dataclass, and a Library that works
# like a collection.
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    read: bool = False


class Library:
    def __init__(self, books=None):
        self._books = list(books or [])

    def add(self, book):
        if book in self:
            raise ValueError(f"already in the library: {book.title}")
        self._books.append(book)

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __contains__(self, book):
        for b in self._books:
            if b.title.lower() == book.title.lower():
                return True
        return False

    def __repr__(self):
        return f"Library({len(self)} books)"


library = Library(
    [
        Book("The Hobbit", "J. R. R. Tolkien", 1937, True),
        Book("Dune", "Frank Herbert", 1965),
    ]
)
library.add(Book("Educated", "Tara Westover", 2018))
print(library, "| len:", len(library))
print(Book("DUNE", "?", 0) in library)
for book in library:
    print(f"- {book.title} ({book.year})")
try:
    library.add(Book("dune", "Frank Herbert", 1965))
except ValueError as error:
    print("Error:", error)
