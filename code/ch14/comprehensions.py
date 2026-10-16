numbers = [3, 8, 1, 12, 7, 6]

squares = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(squares)
print(evens)
print(labels)

words = ["apple", "Banana", "cherry", "date"]
lengths = {word: len(word) for word in words}
initials = {word[0].lower() for word in words}
print(lengths)
print(sorted(initials))

grid = [[row * 3 + col for col in range(3)] for row in range(3)]
print(grid)
flat = [value for row in grid for value in row]
print(flat)
