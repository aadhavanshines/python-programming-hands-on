# Count the words in a text, then show the five most common.
text = """The cat sat on the mat. The dog sat on the log.
The cat and the dog are friends, and the mat is the cat's."""

counts = {}
for word in text.lower().split():
    word = word.strip(".,!?;:\"'")
    if word.endswith("'s"):
        word = word[:-2]
    counts[word] = counts.get(word, 0) + 1

print(len(counts), "different words")
most_common = sorted(counts, key=counts.get, reverse=True)
for word in most_common[:5]:
    print(f"{word:8} {counts[word]}")
