colors = ["red", "green", "blue"]
it = iter(colors)
print(next(it))
print(next(it))
print(next(it))
print(next(it, "no more colors"))  # a default instead of an error


class Countdown:
    """An iterator that counts down from start to 1."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for n in Countdown(3):
    print(n)
print(list(Countdown(5)))
