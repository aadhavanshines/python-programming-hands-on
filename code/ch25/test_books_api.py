import pytest
from fastapi.testclient import TestClient

import books_api

client = TestClient(books_api.app)


@pytest.fixture(autouse=True)
def empty_library():
    books_api.books.clear()  # every test starts with no books


def add(title, author, year=None):
    return client.post(
        "/books", json={"title": title, "author": author, "year": year}
    )


def test_add_and_get():
    response = add("Dune", "Frank Herbert", 1965)
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Dune",
        "author": "Frank Herbert",
        "year": 1965,
    }
    assert client.get("/books/1").json()["title"] == "Dune"


def test_list_filters_by_author():
    add("Dune", "Frank Herbert")
    add("Emma", "Jane Austen")
    titles = [
        b["title"]
        for b in client.get("/books", params={"author": "austen"}).json()
    ]
    assert titles == ["Emma"]


def test_missing_book_is_404():
    response = client.get("/books/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "No book with id 99"}


def test_invalid_book_is_rejected():
    response = client.post("/books", json={"title": "", "author": "Nobody"})
    assert response.status_code == 422
    assert client.get("/books").json() == []


def test_delete():
    add("Dune", "Frank Herbert")
    assert client.delete("/books/1").status_code == 204
    assert client.delete("/books/1").status_code == 404


def test_docs_page_is_generated():
    assert client.get("/docs").status_code == 200
    schema = client.get("/openapi.json").json()
    assert "/books/{book_id}" in schema["paths"]
