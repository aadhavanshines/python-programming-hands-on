def countdown(start):
    while start > 0:
        yield start
        start -= 1


def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def read_records(lines):
    """Turn 'name,score' lines into (name, score) pairs; skip bad ones."""
    for line in lines:
        name, _, score = line.partition(",")
        if score.strip().isdigit():
            yield name.strip(), int(score)


print(list(countdown(4)))
print(list(fibonacci(100)))

# No list of a million numbers is ever built in memory
total = sum(n * n for n in range(1, 1_000_001))
print(total)

data = ["asha, 91", "ben, absent", "chen, 78", "", "dev, 85"]
for name, score in read_records(data):
    print(name, score)

gen = countdown(2)
print(next(gen), next(gen))
print(next(gen, "finished"))
