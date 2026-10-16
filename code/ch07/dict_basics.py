phone_book = {"Asha": "555-0101", "Ben": "555-0102"}

print(phone_book["Asha"])
phone_book["Chen"] = "555-0103"  # add a new entry
phone_book["Ben"] = "555-0199"  # change an existing one
del phone_book["Asha"]  # delete one

print(phone_book)
print("Dev's number:", phone_book.get("Dev", "unknown"))

for name, number in phone_book.items():
    print(f"{name:6} {number}")
print("Names:", list(phone_book.keys()))
