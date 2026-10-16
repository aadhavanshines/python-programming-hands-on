import logging

log = logging.getLogger(__name__)


def median(numbers):
    """Return the median; fixed version of the buggy one in the exercise."""
    if not numbers:
        raise ValueError("median of an empty list")
    ordered = sorted(numbers)  # the bug: the list wasn't sorted
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    # The second bug: both middle values are needed
    return (ordered[middle - 1] + ordered[middle]) / 2


def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        log.warning("not a whole number: %r; using %d", text, default)
        return default


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s")
    print(median([7, 1, 3]), median([4, 1, 3, 2]))
    print(safe_int("42"), safe_int("4x2"))
