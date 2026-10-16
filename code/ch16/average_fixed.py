def average(numbers):
    if not numbers:
        raise ValueError("can't average an empty list")
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))
assert average([10, 20, 30]) == 20.0
assert average([5]) == 5.0
print("All checks passed.")
