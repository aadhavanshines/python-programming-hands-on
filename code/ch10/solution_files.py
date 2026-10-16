import csv
from pathlib import Path


def file_stats(path):
    """Return (lines, words, characters) for a text file."""
    text = Path(path).read_text(encoding="utf-8")
    return len(text.splitlines()), len(text.split()), len(text)


def average_rating(csv_path):
    """Return the average of the 'rating' column of a CSV file."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        ratings = []
        for row in csv.DictReader(f):
            ratings.append(int(row["rating"]))
    return sum(ratings) / len(ratings)


def divide(a_text, b_text):
    """Divide two numbers given as text; return a message on errors."""
    try:
        return f"{float(a_text) / float(b_text):g}"
    except ValueError:
        return "Please type numbers only."
    except ZeroDivisionError:
        return "You can't divide by zero."


if __name__ == "__main__":
    print(file_stats("books.csv"))
    print(f"{average_rating('books.csv'):.1f}")
    print(
        divide("7", "2"), "|", divide("7", "0"), "|", divide("seven", "2")
    )
