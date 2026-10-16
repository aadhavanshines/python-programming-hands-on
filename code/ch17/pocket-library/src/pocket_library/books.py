import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Book:
    title: str
    author: str
    year: int
    read: bool = False


class Library:
    def __init__(self, path):
        self.path = Path(path)
        self.books = []
        if self.path.exists():
            self.books = [
                Book(**item)
                for item in json.loads(
                    self.path.read_text(encoding="utf-8")
                )
            ]

    def add(self, book):
        if any(b.title.lower() == book.title.lower() for b in self.books):
            raise ValueError(f"already in the library: {book.title}")
        self.books.append(book)

    def mark_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.read = True
                return book
        raise KeyError(title)

    def save(self):
        data = [asdict(book) for book in self.books]
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")
