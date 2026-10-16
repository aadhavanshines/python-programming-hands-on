# Chapter 23 exercises: two new BookStore methods, added in a subclass so
# that this file runs on its own. In your project, add them to db.py.
from pocket.db import BookStore


class BetterStore(BookStore):
    def remove(self, book_id):
        """Delete a book; KeyError if there is no such book."""
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM books WHERE id = ?", (book_id,)
            )
        if cur.rowcount == 0:
            raise KeyError(book_id)

    def books_per_author(self):
        """{author: number of books}, most books first."""
        rows = self.conn.execute(
            "SELECT author, COUNT(*) FROM books GROUP BY author "
            "ORDER BY COUNT(*) DESC, author"
        )
        return dict(rows.fetchall())


store = BetterStore(":memory:")  # a database that lives only in memory
store.add("Dune", "Frank Herbert", 1965)
store.add("Children of Dune", "Frank Herbert", 1976)
store.add("Emma", "Jane Austen", 1815)
print(store.books_per_author())
store.remove(3)
print([book.title for book in store.list()])
try:
    store.remove(3)
except KeyError as error:
    print("No book with id", error.args[0])
store.close()
