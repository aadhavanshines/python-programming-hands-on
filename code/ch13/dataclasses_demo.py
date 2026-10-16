from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    year: int
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int


dune = Book("Dune", "Frank Herbert", 1965)
dune.tags.append("novel")
print(dune)
print(dune == Book("Dune", "Frank Herbert", 1965, ["novel"]))

versions = sorted([Version(3, 15), Version(3, 9), Version(3, 12)])
print("Oldest:", versions[0])
print("Newest:", versions[-1])
v = Version(3, 15)
v.minor = 16
