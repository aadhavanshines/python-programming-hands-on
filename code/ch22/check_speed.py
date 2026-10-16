import timeit

# Checks that hold on any computer: compare, don't print raw times.
setup = "items = list(range(100_000)); lookup = set(items)"
in_list = timeit.timeit("99_999 in items", setup=setup, number=200)
in_set = timeit.timeit("99_999 in lookup", setup=setup, number=200)
print("Set at least 100 times faster than list:", in_list / in_set > 100)

setup = "data = [n % 3000 for n in range(20_000)]"
slow = timeit.timeit(
    "r = []\nfor x in data:\n    if x not in r: r.append(x)",
    setup=setup,
    number=1,
)
fast = timeit.timeit("list(dict.fromkeys(data))", setup=setup, number=1)
print("dict.fromkeys at least 50 times faster:", slow / fast > 50)
