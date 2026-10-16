import timeit

setup = "items = list(range(100_000)); lookup = set(items); target = 99_999"
in_list = timeit.timeit("target in items", setup=setup, number=1_000)
in_set = timeit.timeit("target in lookup", setup=setup, number=1_000)
print(f"1,000 searches in a list: {in_list * 1000:8.2f} ms")
print(f"1,000 searches in a set:  {in_set * 1000:8.2f} ms")
print(f"The set was about {in_list / in_set:,.0f} times faster")

join = timeit.timeit("''.join(str(n) for n in range(1000))", number=1_000)
plus = timeit.timeit(
    "s = ''\nfor n in range(1000): s += str(n)", number=1_000
)
print(f"join: {join * 1000:.1f} ms, +=: {plus * 1000:.1f} ms")
