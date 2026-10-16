import json

import pytest


def load_titles(path):
    return [
        book["title"]
        for book in json.loads(path.read_text(encoding="utf-8"))
    ]


@pytest.fixture
def library_file(tmp_path):
    """A temporary library.json, made fresh for each test that uses it."""
    path = tmp_path / "library.json"
    path.write_text(
        json.dumps([{"title": "Dune"}, {"title": "Emma"}]), encoding="utf-8"
    )
    return path


def test_load_titles(library_file):
    assert load_titles(library_file) == ["Dune", "Emma"]


def test_empty_library(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("[]", encoding="utf-8")
    assert load_titles(path) == []
