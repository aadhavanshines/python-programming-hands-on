import csv

import pytest

from pocket.cli import main
from pocket.db import BookStore


@pytest.fixture
def store(tmp_path):
    s = BookStore(tmp_path / "test.db")
    yield s
    s.close()


def test_add_and_get(store):
    book_id = store.add("Dune", "Frank Herbert", 1965)
    book = store.get(book_id)
    assert (book.title, book.year, book.read_on) == ("Dune", 1965, None)


def test_duplicate_is_refused(store):
    store.add("Dune", "Frank Herbert")
    with pytest.raises(ValueError):
        store.add("Dune", "Frank Herbert")


def test_unread_and_search(store):
    a = store.add("Dune", "Frank Herbert", 1965)
    store.add("Emma", "Jane Austen", 1815)
    store.mark_read(a, "2026-10-01", 5)
    assert [b.title for b in store.list(unread_only=True)] == ["Emma"]
    assert [b.title for b in store.list(search="herb")] == ["Dune"]


def test_stats(store):
    store.add("Dune", "Frank Herbert")
    store.add("Children of Dune", "Frank Herbert")
    store.mark_read(1, "2026-10-01", 4)
    assert store.stats() == {
        "books": 2,
        "read": 1,
        "average_rating": 4.0,
        "top_author": "Frank Herbert",
    }


@pytest.mark.parametrize("bad", ["not-a-date", "2026-02-30", "20261001"])
def test_mark_read_rejects_bad_dates(store, bad):
    book_id = store.add("Dune", "Frank Herbert")
    with pytest.raises(ValueError):
        store.mark_read(book_id, bad)
    assert store.get(book_id).read_on is None


def test_mark_read_unknown_id(store):
    with pytest.raises(KeyError):
        store.mark_read(99, "2026-10-01")


def test_export_csv(store, tmp_path):
    store.add("Emma", "Jane Austen", 1815)
    out = tmp_path / "books.csv"
    assert store.export_csv(out) == 1
    rows = list(csv.DictReader(out.open(encoding="utf-8")))
    assert rows[0]["title"] == "Emma"


def test_cli_rating_must_be_1_to_5(tmp_path):
    with pytest.raises(SystemExit):
        main(
            [
                "--db",
                str(tmp_path / "x.db"),
                "read",
                "1",
                "--date",
                "2026-10-01",
                "--rating",
                "9",
            ]
        )
