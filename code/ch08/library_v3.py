# Pocket Library, version 3: the same data, organized into functions.


def make_book(title, author, year, read=False):
    return {"title": title, "author": author, "year": year, "read": read}


def add_book(books, book):
    for existing in books:
        if existing["title"].lower() == book["title"].lower():
            return False
    books.append(book)
    return True


def books_by(books, author):
    found = []
    for book in books:
        if author.lower() in book["author"].lower():
            found.append(book)
    return found


def show(books):
    for book in books:
        mark = "x" if book["read"] else " "
        print(
            f"[{mark}] {book['title']} ({book['author']}, {book['year']})"
        )


library = []
add_book(
    library, make_book("The Hobbit", "J. R. R. Tolkien", 1937, read=True)
)
add_book(library, make_book("Dune", "Frank Herbert", 1965))
add_book(library, make_book("The Silmarillion", "J. R. R. Tolkien", 1977))
print(
    "Added again?",
    add_book(library, make_book("dune", "Frank Herbert", 1965)),
)

show(library)
print()
print("By Tolkien:")
show(books_by(library, "tolkien"))
