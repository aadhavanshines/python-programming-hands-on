text = "Mississippi"
counts = {}
for letter in text.lower():
    counts[letter] = counts.get(letter, 0) + 1
for letter in sorted(counts):
    print(letter, counts[letter])
