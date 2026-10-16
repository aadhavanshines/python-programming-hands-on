import functools
from contextlib import contextmanager


def retry(times, exceptions=(Exception,)):
    """Call the function up to `times` times until it doesn't raise."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    print(f"attempt {attempt} failed: {error}")
                    if attempt == times:
                        raise

        return wrapper

    return decorator


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@contextmanager
def temporary_value(mapping, key, value):
    """Set mapping[key] = value inside the with block, then restore it."""
    missing = object()
    old = mapping.get(key, missing)
    mapping[key] = value
    try:
        yield mapping
    finally:
        if old is missing:
            del mapping[key]
        else:
            mapping[key] = old


if __name__ == "__main__":
    answers = iter([ValueError("busy"), ValueError("busy"), "ok"])

    @retry(3)
    def flaky():
        result = next(answers)
        if isinstance(result, Exception):
            raise result
        return result

    print(flaky())

    @count_calls
    def hello():
        return "hi"

    hello()
    hello()
    print(hello.calls)

    settings = {"mode": "normal"}
    with temporary_value(settings, "mode", "test"):
        print(settings)
    print(settings)
