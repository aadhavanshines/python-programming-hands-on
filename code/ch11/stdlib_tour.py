import math
import random
import statistics
from collections import Counter, defaultdict
from decimal import Decimal

print(math.sqrt(2), math.floor(7.8), math.ceil(7.2), math.pi)

random.seed(1)  # same "random" results every run
print(random.randint(1, 6), random.choice(["red", "green", "blue"]))
deck = list(range(1, 11))
random.shuffle(deck)
print(deck)

marks = [72, 88, 95, 61, 79, 88]
print(
    "mean",
    statistics.mean(marks),
    "median",
    statistics.median(marks),
    "mode",
    statistics.mode(marks),
)

words = "the cat and the hat and the bat".split()
print(Counter(words).most_common(2))

by_letter = defaultdict(list)
for word in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    by_letter[word[0]].append(word)
print(dict(by_letter))

# Decimal: exact decimal arithmetic, for money
print(0.1 + 0.2, Decimal("0.10") + Decimal("0.20"))
price = Decimal("19.99")
print(price * 3, (price * Decimal("1.08")).quantize(Decimal("0.01")))
