import argparse
import sys

from . import __version__
from .books import Book, Library


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="pocket", description="Your book collection."
    )
    parser.add_argument(
        "--version", action="version", version=f"pocket {__version__}"
    )
    parser.add_argument(
        "--file", default="library.json", help="where the books are kept"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="add a book")
    add.add_argument("title")
    add.add_argument("author")
    add.add_argument("year", type=int)
    commands.add_parser("list", help="list all books")
    read = commands.add_parser("read", help="mark a book as read")
    read.add_argument("title")

    args = parser.parse_args(argv)
    library = Library(args.file)
    try:
        if args.command == "add":
            library.add(Book(args.title, args.author, args.year))
            library.save()
            print(f"Added {args.title}.")
        elif args.command == "read":
            book = library.mark_read(args.title)
            library.save()
            print(f"Marked {book.title} as read.")
        elif args.command == "list":
            for book in library.books:
                mark = "x" if book.read else " "
                print(f"[{mark}] {book.title} ({book.author}, {book.year})")
    except ValueError as error:
        print(f"pocket: {error}", file=sys.stderr)
        return 1
    except KeyError:
        print(f"pocket: no book called {args.title!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
