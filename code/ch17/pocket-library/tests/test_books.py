import pytest

from pocket_library.books import Book, Library
from pocket_library.cli import main


def test_add_and_reload(tmp_path):
    path = tmp_path / "books.json"
    library = Library(path)
    library.add(Book("Dune", "Frank Herbert", 1965))
    library.save()
    assert Library(path).books == [Book("Dune", "Frank Herbert", 1965)]


def test_no_duplicates(tmp_path):
    library = Library(tmp_path / "books.json")
    library.add(Book("Dune", "Frank Herbert", 1965))
    with pytest.raises(ValueError):
        library.add(Book("DUNE", "Frank Herbert", 1965))


def test_cli_add_list_read(tmp_path, capsys):
    file = str(tmp_path / "books.json")
    assert main(["--file", file, "add", "Emma", "Jane Austen", "1815"]) == 0
    assert main(["--file", file, "read", "emma"]) == 0
    assert main(["--file", file, "list"]) == 0
    assert (
        capsys.readouterr().out.splitlines()[-1]
        == "[x] Emma (Jane Austen, 1815)"
    )


def test_cli_unknown_title(tmp_path, capsys):
    assert (
        main(["--file", str(tmp_path / "b.json"), "read", "Nothing"]) == 1
    )
    assert "pocket:" in capsys.readouterr().err
