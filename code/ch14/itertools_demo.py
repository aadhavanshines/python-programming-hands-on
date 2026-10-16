import itertools

print(list(itertools.islice(itertools.count(10, 5), 4)))
print(list(itertools.chain([1, 2], (3, 4), "ab")))
print(list(itertools.accumulate([5, 3, 8, 1])))
print(list(itertools.product("AB", [1, 2])))
print(list(itertools.combinations(["tea", "coffee", "juice"], 2)))


def region_of(row):
    return row[0]


sales = [
    ("north", 120),
    ("north", 80),
    ("south", 50),
    ("south", 70),
    ("east", 30),
]
for region, rows in itertools.groupby(sales, key=region_of):
    print(region, sum(amount for _, amount in rows))
