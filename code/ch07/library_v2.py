# Pocket Library, version 2: each book is a dictionary.
books = [
    {
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "year": 1937,
        "read": True,
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "year": 1965,
        "read": False,
    },
    {
        "title": "The Silmarillion",
        "author": "J. R. R. Tolkien",
        "year": 1977,
        "read": False,
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "year": 2018,
        "read": True,
    },
]

print(f"{'Title':<18}{'Author':<18}{'Year':>5}  Read")
for book in books:
    mark = "yes" if book["read"] else ""
    print(
        f"{book['title']:<18}{book['author']:<18}{book['year']:>5}  {mark}"
    )

print()
to_read = []
for book in books:
    if not book["read"]:
        to_read.append(book["title"])
print("Still to read:", ", ".join(to_read))

per_author = {}
for book in books:
    per_author[book["author"]] = per_author.get(book["author"], 0) + 1
print("Books per author:")
for author, count in per_author.items():
    print(f"  {author}: {count}")
