poem = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;"""

lines = poem.splitlines()
words = poem.replace(",", " ").replace(";", " ").split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(poem))
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
for number, line in enumerate(lines, start=1):
    print(f"{number}: {line[:20]:20} ... ({len(line)} chars)")
