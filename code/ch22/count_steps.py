# Count the comparisons each search needs: a measure that doesn't
# depend on how fast your computer is.


def linear_search(items, target):
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            break
    return steps


def binary_search(items, target):
    """items must be sorted."""
    steps = 0
    low, high = 0, len(items) - 1
    while low <= high:
        steps += 1
        middle = (low + high) // 2
        if items[middle] == target:
            break
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return steps


for size in [1_000, 1_000_000]:
    numbers = list(range(size))
    target = size - 1  # the worst case for linear search
    linear = linear_search(numbers, target)
    binary = binary_search(numbers, target)
    print(
        f"{size:>9,} items: linear {linear:>9,} steps, "
        f"binary {binary:>2} steps"
    )
