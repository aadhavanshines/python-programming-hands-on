import functools

calls = 0


@functools.cache
def fibonacci(n):
    global calls
    calls += 1
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(80))
print("Function calls:", calls)  # without the cache: about 76 quadrillion
print(fibonacci.cache_info())
