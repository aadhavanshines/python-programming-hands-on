def is_palindrome(text):
    """True if text reads the same backwards, ignoring case,
    spaces and punctuation."""
    letters = ""
    for ch in text.lower():
        if ch.isalnum():
            letters += ch
    return letters == letters[::-1]


def count_vowels(text):
    """Return how many vowels (a, e, i, o, u) are in text."""
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def largest(numbers):
    """Return the largest number in a non-empty list, without max()."""
    best = numbers[0]
    for n in numbers[1:]:
        if n > best:
            best = n
    return best


if __name__ == "__main__":
    print(is_palindrome("Never odd or even"))
    print(is_palindrome("Python"))
    print(count_vowels("Programming in Python"))
    print(largest([3, 41, 7, 41, -2]))
