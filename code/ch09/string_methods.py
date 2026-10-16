raw = "   python is FUN   "
print(repr(raw.strip()))
print(raw.strip().capitalize())
print(raw.strip().title())

sentence = "red,green,,blue"
parts = sentence.split(",")
print(parts)
print(" | ".join(parts))

email = "meera@example.com"
print(email.startswith("meera"), email.endswith(".org"))
print(email.find("@"), email.count("e"))
print(email.replace("example.com", "example.org"))
print("2026".isdigit(), "20x6".isdigit())
