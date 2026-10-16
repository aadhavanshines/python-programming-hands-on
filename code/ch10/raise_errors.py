def set_rating(book, rating):
    if not 1 <= rating <= 5:
        raise ValueError(f"rating must be 1 to 5, not {rating}")
    book["rating"] = rating


book = {"title": "Dune"}
set_rating(book, 4)
print(book)
try:
    set_rating(book, 9)
except ValueError as error:
    print("Error:", error)
