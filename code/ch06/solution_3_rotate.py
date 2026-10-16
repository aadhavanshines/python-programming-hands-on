items = [1, 2, 3, 4, 5]
steps = 2
rotated = items[-steps:] + items[:-steps]
print(rotated)
