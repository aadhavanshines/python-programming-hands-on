def median(numbers):
    """Return the middle value of a list of numbers. (It has two bugs.)"""
    middle = len(numbers) // 2
    return numbers[middle]


print(median([7, 1, 3]))  # we expect 3
print(median([4, 1, 3, 2]))  # we expect 2.5
