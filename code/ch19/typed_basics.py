def greeting(name: str, times: int = 1) -> str:
    return " ".join([f"Hi, {name}!"] * times)


def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def find_index(items: list[str], target: str) -> int | None:
    """Return the position of target, or None if it isn't there."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return None


scores: dict[str, int] = {"asha": 91, "ben": 78}
print(greeting("Zara", 2))
print(average([2.5, 3.5, 6]))
print(find_index(["a", "b", "c"], "c"), find_index(["a"], "z"))
print(greeting.__annotations__)
