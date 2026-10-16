import functools


def log_calls(func):
    """Print each call and its result."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}{args} -> {result!r}")
        return result

    return wrapper


def repeat(times):
    """A decorator with an argument: run the function several times."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@log_calls
def add(a, b):
    """Add two numbers."""
    return a + b


@repeat(3)
def cheer(name):
    print(f"Go, {name}!")


add(2, 3)
add(10, -4)
cheer("Ravi")
print(add.__name__, "|", add.__doc__)
