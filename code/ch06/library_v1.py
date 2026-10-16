# Pocket Library, version 1: a list of book titles.
books = ["The Hobbit", "Dune", "Educated"]

print("Add books to your library. Press Enter on an empty line to stop.")
while True:
    title = input("Title: ").strip()
    if title == "":
        break
    if title in books:
        print("  You already have that one.")
    else:
        books.append(title)

print()
print(f"Your library has {len(books)} books:")
for number, title in enumerate(sorted(books), start=1):
    print(f"{number:2}. {title}")
