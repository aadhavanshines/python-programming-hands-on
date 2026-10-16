from operator import itemgetter

books = [
    ("Dune", 1965, 4.3),
    ("Educated", 2018, 4.5),
    ("The Hobbit", 1937, 4.6),
    ("Sapiens", 2011, 4.4),
]

by_year = sorted(books, key=lambda book: book[1])
print([title for title, _, _ in by_year])

best_first = sorted(books, key=itemgetter(2), reverse=True)
print([title for title, _, _ in best_first])

print(max(books, key=lambda book: len(book[0]))[0])

words = ["kiwi", "Apple", "fig", "banana"]
print(sorted(words, key=lambda w: (len(w), w.lower())))
