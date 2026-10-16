import bisect


def has_duplicates(items):
    """True if any item appears twice: one pass, using a set."""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


def grade_for(score, cut_offs=(60, 70, 80, 90), grades="FDCBA"):
    """Find the grade with a binary search over the cut-off scores."""
    return grades[bisect.bisect(cut_offs, score)]


def pair_with_sum(numbers, target):
    """Return a pair of numbers adding up to target, or None. O(n)."""
    seen = set()
    for n in numbers:
        if target - n in seen:
            return (target - n, n)
        seen.add(n)
    return None


if __name__ == "__main__":
    print(has_duplicates([3, 1, 4, 1, 5]), has_duplicates(range(100_000)))
    print([grade_for(s) for s in (55, 60, 75, 89, 90, 100)])
    print(pair_with_sum([8, 3, 11, 5, 2], 13), pair_with_sum([1, 2], 10))
