# Chapter 17 exercise: a "stats" command for the pocket tool.
# In your own copy, put stats_lines in books.py and the new command in
# cli.py. Here, the package is imported from the chapter folder instead.
import sys

sys.path.insert(0, "pocket-library/src")

from pocket_library.books import Book, Library  # noqa: E402


def stats_lines(library):
    """Lines describing the library: totals, and the oldest book."""
    books = library.books
    if not books:
        return ["No books yet."]
    read = sum(1 for book in books if book.read)
    oldest = books[0]
    for book in books:
        if book.year < oldest.year:
            oldest = book
    return [
        f"{len(books)} books, {read} read, {len(books) - read} to read",
        f"Oldest: {oldest.title} ({oldest.year})",
    ]


# The changes to cli.main():
#     commands.add_parser("stats", help="show totals")
#     ...
#     elif args.command == "stats":
#         for line in stats_lines(library):
#             print(line)

library = Library("stats_demo.json")
print("\n".join(stats_lines(library)))
library.add(Book("Dune", "Frank Herbert", 1965, read=True))
library.add(Book("Emma", "Jane Austen", 1815))
library.add(Book("Educated", "Tara Westover", 2018))
print("\n".join(stats_lines(library)))
