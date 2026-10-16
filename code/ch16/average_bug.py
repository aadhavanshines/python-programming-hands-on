def average(numbers):
    total = 0
    # Bug: starts at 1, skipping the first number
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total / len(numbers)


print(average([10, 20, 30]))  # we expect 20.0
