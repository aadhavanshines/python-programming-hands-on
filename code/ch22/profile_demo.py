import cProfile
import pstats


def slow_unique(items):
    result = []
    for item in items:
        if item not in result:  # searching a list: slow for big lists
            result.append(item)
    return result


def fast_unique(items):
    return list(dict.fromkeys(items))  # keeps the order, uses hashing


data = [n % 3000 for n in range(20_000)]
profiler = cProfile.Profile()
profiler.enable()
a = slow_unique(data)
b = fast_unique(data)
profiler.disable()
print("Same result:", a == b)
pstats.Stats(profiler).sort_stats("cumulative").print_stats(4)
