def factorial(n):
    """Return n! = n * (n - 1) * ... * 1."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def count_down(n):
    if n == 0:
        print("Go!")
        return
    print(n)
    count_down(n - 1)


print(factorial(5))
print(factorial(20))
count_down(3)
