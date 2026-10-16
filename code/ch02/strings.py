first = "Ada"
last = "Lovelace"
born = 1815

full = first + " " + last
print(full)
print(len(full), "characters")
print(full.upper())
print(full.lower())
print("First letter:", full[0])
print("Last letter:", full[-1])
print(f"{first} was born in {born}.")  # an f-string: values go in {}
