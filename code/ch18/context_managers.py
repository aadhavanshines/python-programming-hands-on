from contextlib import contextmanager, suppress
from pathlib import Path


class Indented:
    """Indent everything printed through it, one level per 'with'."""

    level = 0

    def __enter__(self):
        Indented.level += 1
        return self

    def __exit__(self, exc_type, exc, tb):
        Indented.level -= 1
        return False  # don't hide exceptions

    def print(self, text):
        print("    " * Indented.level + text)


@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


with Indented() as out:
    out.print("Chapter 1")
    with Indented() as inner:
        inner.print("Section 1.1")
    out.print("Chapter 2")

with tag("ul"):
    for item in ["tea", "milk"]:
        print(f"  <li>{item}</li>")

with suppress(FileNotFoundError):
    Path("missing.txt").unlink()  # no error if it isn't there
print("Done.")
