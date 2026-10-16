def year_of(book):
    return book[1]


dune = ("Dune", 1965, 4.3)
print(year_of(dune))
print((lambda book: book[1])(dune))  # the same function, without a name
