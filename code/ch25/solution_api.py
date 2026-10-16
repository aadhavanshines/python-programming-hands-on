# Solutions to the Chapter 25 exercises, checked with FastAPI's TestClient.
import warnings

# The same message pytest.ini hides for the tests (see the chapter)
warnings.filterwarnings(
    "ignore", message="Using `httpx` with `starlette.testclient`"
)

from fastapi import HTTPException  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

import books_api  # noqa: E402
from books_api import Book  # noqa: E402

app = books_api.app


# Exercise 1: mark a book as read, with a rating from 1 to 5
class Reading(BaseModel):
    rating: int = Field(ge=1, le=5)


ratings: dict[int, int] = {}


@app.put("/books/{book_id}/rating")
def rate_book(book_id: int, reading: Reading) -> dict[str, int]:
    if book_id not in books_api.books:
        raise HTTPException(
            status_code=404, detail=f"No book with id {book_id}"
        )
    ratings[book_id] = reading.rating
    return {"id": book_id, "rating": reading.rating}


# Exercise 2: statistics
@app.get("/stats")
def stats() -> dict[str, float | int | None]:
    years = [b.year for b in books_api.books.values() if b.year is not None]
    average = None
    if ratings:
        average = round(sum(ratings.values()) / len(ratings), 2)
    return {
        "books": len(books_api.books),
        "rated": len(ratings),
        "average_rating": average,
        "oldest": min(years, default=None),
    }


# Exercise 3: a client function that returns None instead of raising for 404
def find_book(client: TestClient, book_id: int) -> Book | None:
    response = client.get(f"/books/{book_id}")
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return Book(**response.json())


client = TestClient(app)
for title, author, year in [
    ("Dune", "Frank Herbert", 1965),
    ("Emma", "Jane Austen", 1815),
]:
    client.post(
        "/books", json={"title": title, "author": author, "year": year}
    )
print(client.put("/books/1/rating", json={"rating": 5}).json())
print(client.put("/books/2/rating", json={"rating": 4}).json())
print(client.put("/books/2/rating", json={"rating": 9}).status_code)
print(client.put("/books/7/rating", json={"rating": 3}).status_code)
print(client.get("/stats").json())
print(find_book(client, 2))
print(find_book(client, 7))
