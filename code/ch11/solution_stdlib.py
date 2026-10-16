import random
from collections import Counter
from datetime import date


def roll_dice(rolls, seed=None):
    """Roll two dice `rolls` times; return a Counter of the totals."""
    rng = random.Random(seed)
    totals = Counter()
    for _ in range(rolls):
        totals[rng.randint(1, 6) + rng.randint(1, 6)] += 1
    return totals


def days_between(a, b):
    """Days between two dates given as 'YYYY-MM-DD' text."""
    return abs((date.fromisoformat(b) - date.fromisoformat(a)).days)


if __name__ == "__main__":
    totals = roll_dice(1000, seed=3)
    for total in range(2, 13):
        print(f"{total:2} {'#' * (totals[total] // 5)}")
    print(days_between("2026-01-01", "2026-10-15"))
