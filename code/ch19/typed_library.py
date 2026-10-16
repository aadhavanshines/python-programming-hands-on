from dataclasses import dataclass, field
from operator import attrgetter
from typing import Protocol


@dataclass
class Book:
    title: str
    author: str
    year: int
    tags: list[str] = field(default_factory=list)


class Shelf(Protocol):
    """Anything with a books attribute counts as a Shelf."""

    books: list[Book]


@dataclass
class Library:
    books: list[Book] = field(default_factory=list)

    def by_decade(self) -> dict[int, list[str]]:
        result: dict[int, list[str]] = {}
        for book in self.books:
            result.setdefault(book.year // 10 * 10, []).append(book.title)
        return result

    def newest(self) -> Book | None:
        return max(self.books, key=attrgetter("year"), default=None)


def count_tagged(shelf: Shelf, tag: str) -> int:
    return sum(1 for book in shelf.books if tag in book.tags)


library = Library(
    [
        Book("Dune", "Frank Herbert", 1965, ["sci-fi"]),
        Book("Dune Messiah", "Frank Herbert", 1969, ["sci-fi"]),
        Book("Educated", "Tara Westover", 2018),
    ]
)
print(library.by_decade())
newest = library.newest()
if newest is not None:  # mypy insists on this check
    print("Newest:", newest.title)
print("Sci-fi:", count_tagged(library, "sci-fi"))
