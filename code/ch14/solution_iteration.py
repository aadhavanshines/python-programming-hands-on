def even_squares(numbers):
    """Squares of the even numbers, in order."""
    return [n * n for n in numbers if n % 2 == 0]


def word_lengths(text):
    """A dictionary from each word (lower case) to its length."""
    return {word.lower(): len(word) for word in text.split()}


def chunked(items, size):
    """Yield lists of up to `size` items at a time."""
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


if __name__ == "__main__":
    print(even_squares(range(10)))
    print(word_lengths("The quick brown Fox"))
    print(list(chunked("abcdefg", 3)))
