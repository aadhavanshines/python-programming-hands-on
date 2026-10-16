import argparse
import sys

from .db import BookStore


def build_parser():
    parser = argparse.ArgumentParser(
        prog="pocket", description="Track your books."
    )
    parser.add_argument(
        "--db",
        default="pocket.db",
        help="database file (default: pocket.db)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("add", help="add a book")
    p.add_argument("title")
    p.add_argument("author")
    p.add_argument("--year", type=int)

    p = sub.add_parser("list", help="list books")
    p.add_argument(
        "--unread", action="store_true", help="only books not read yet"
    )
    p.add_argument("--search", help="match part of a title or author")

    p = sub.add_parser("read", help="mark a book as read")
    p.add_argument("id", type=int)
    p.add_argument(
        "--date", required=True, help="date read, such as 2026-10-15"
    )
    p.add_argument("--rating", type=int, choices=range(1, 6))

    sub.add_parser("stats", help="show statistics")
    p = sub.add_parser("export", help="export all books to a CSV file")
    p.add_argument("file")
    return parser


def show(books):
    if not books:
        print("No books found.")
    for b in books:
        year = b.year or "?"
        if b.read_on:
            status = f"read {b.read_on}"
            if b.rating:
                status += ", " + "*" * b.rating
        else:
            status = "unread"
        print(f"{b.id:3}  {b.title} ({b.author}, {year})  [{status}]")


def main(argv=None):
    args = build_parser().parse_args(argv)
    store = BookStore(args.db)
    try:
        if args.command == "add":
            book_id = store.add(args.title, args.author, args.year)
            print(f"Added #{book_id}: {args.title}")
        elif args.command == "list":
            show(store.list(unread_only=args.unread, search=args.search))
        elif args.command == "read":
            store.mark_read(args.id, args.date, args.rating)
            print(f"Marked #{args.id} as read on {args.date}")
        elif args.command == "stats":
            for key, value in store.stats().items():
                print(f"{key.replace('_', ' '):15} {value}")
        elif args.command == "export":
            count = store.export_csv(args.file)
            print(f"Exported {count} books to {args.file}")
    except ValueError as error:
        print(f"pocket: {error}", file=sys.stderr)
        return 1
    except KeyError as error:
        print(f"pocket: no book with id {error.args[0]}", file=sys.stderr)
        return 1
    finally:
        store.close()
    return 0
