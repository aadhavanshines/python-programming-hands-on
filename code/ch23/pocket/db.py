import csv
import datetime
import sqlite3
from dataclasses import dataclass

SCHEMA = """
CREATE TABLE IF NOT EXISTS books (
    id      INTEGER PRIMARY KEY,
    title   TEXT NOT NULL,
    author  TEXT NOT NULL,
    year    INTEGER,
    rating  INTEGER CHECK (rating BETWEEN 1 AND 5),
    read_on TEXT,                     -- a date such as 2026-10-15, or NULL
    UNIQUE (title, author)
)
"""


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int | None
    rating: int | None
    read_on: str | None


def check_date(text):
    """Accept only real dates written as YYYY-MM-DD."""
    try:
        valid = datetime.date.fromisoformat(text).isoformat() == text
    except ValueError:
        valid = False
    if not valid:
        raise ValueError(f"not a date in the form YYYY-MM-DD: {text!r}")


class BookStore:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.conn.execute(SCHEMA)

    def close(self):
        self.conn.close()

    def add(self, title, author, year=None):
        try:
            with self.conn:  # commits, or rolls back on error
                cur = self.conn.execute(
                    "INSERT INTO books (title, author, year)"
                    " VALUES (?, ?, ?)",
                    (title, author, year),
                )
        except sqlite3.IntegrityError:
            raise ValueError(
                f"already in the library: {title} by {author}"
            ) from None
        return cur.lastrowid

    def get(self, book_id):
        row = self.conn.execute(
            "SELECT * FROM books WHERE id = ?", (book_id,)
        ).fetchone()
        if row is None:
            raise KeyError(book_id)
        return Book(*row)

    def list(self, unread_only=False, search=None):
        sql = "SELECT * FROM books WHERE 1 = 1"
        params = []
        if unread_only:
            sql += " AND read_on IS NULL"
        if search:
            sql += " AND (title LIKE ? OR author LIKE ?)"
            params += [f"%{search}%", f"%{search}%"]
        sql += " ORDER BY author, year"
        return [Book(*row) for row in self.conn.execute(sql, params)]

    def mark_read(self, book_id, date, rating=None):
        check_date(date)  # raises ValueError for a date that isn't real
        self.get(book_id)  # raises KeyError if there is no such book
        with self.conn:
            self.conn.execute(
                "UPDATE books SET read_on = ?, rating = ? WHERE id = ?",
                (date, rating, book_id),
            )

    def stats(self):
        total, read, avg = self.conn.execute(
            "SELECT COUNT(*), COUNT(read_on), AVG(rating) FROM books"
        ).fetchone()
        top = self.conn.execute(
            "SELECT author, COUNT(*) AS n FROM books GROUP BY author "
            "ORDER BY n DESC, author LIMIT 1"
        ).fetchone()
        return {
            "books": total,
            "read": read,
            "average_rating": round(avg, 1) if avg else None,
            "top_author": top[0] if top else None,
        }

    def export_csv(self, path):
        books = self.list()
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["id", "title", "author", "year", "rating", "read_on"]
            )
            for b in books:
                writer.writerow(
                    [b.id, b.title, b.author, b.year, b.rating, b.read_on]
                )
        return len(books)
