def total_pages(books: list[dict[str, int]]) -> int:
    return sum(book["pages"] for book in books)


def label(year: int) -> str:
    return "Published in " + year  # mistake 1: adding str and int


pages = total_pages([{"pages": 310}, {"pages": 412}])
print(label(1965))
count: int = "twelve"  # mistake 2: wrong type
