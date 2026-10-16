# A small web API for Pocket Library, built with FastAPI.
# Run it with:  python -m uvicorn books_api:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Pocket Library API")


class NewBook(BaseModel):
    """What a client sends to add a book."""

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int | None = Field(default=None, ge=0, le=2100)


class Book(NewBook):
    """What the API sends back: the book plus its id."""

    id: int


books: dict[int, Book] = {}  # kept in memory: empty again on every restart


@app.get("/books")
def list_books(author: str | None = None) -> list[Book]:
    found = list(books.values())
    if author:
        found = [b for b in found if author.lower() in b.author.lower()]
    return found


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    if book_id not in books:
        raise HTTPException(
            status_code=404, detail=f"No book with id {book_id}"
        )
    return books[book_id]


@app.post("/books", status_code=201)
def add_book(new: NewBook) -> Book:
    book_id = max(books, default=0) + 1
    book = Book(id=book_id, **new.model_dump())
    books[book_id] = book
    return book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int) -> None:
    if books.pop(book_id, None) is None:
        raise HTTPException(
            status_code=404, detail=f"No book with id {book_id}"
        )
