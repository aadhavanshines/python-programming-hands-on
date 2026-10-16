import re


def caesar(text, shift):
    """Shift each letter by `shift` places in the alphabet, keeping case."""
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def my_title(text):
    """Capitalize the first letter of each word, like str.title()."""
    words = text.split(" ")
    fixed = []
    for word in words:
        fixed.append(word[:1].upper() + word[1:].lower())
    return " ".join(fixed)


def hashtags(text):
    """Return the hashtags in text, in order, without the # sign."""
    return re.findall(r"#(\w+)", text)


if __name__ == "__main__":
    secret = caesar("Meet at noon!", 3)
    print(secret)
    print(caesar(secret, -3))
    print(my_title("the lord OF the rings"))
    print(hashtags("Loving #Python and #100DaysOfCode! #python"))
