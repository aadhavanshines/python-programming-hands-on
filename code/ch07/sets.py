alice = {"python", "chess", "hiking", "jazz"}
bob = {"jazz", "football", "python"}

print("Both like:", sorted(alice & bob))
print("Either likes:", sorted(alice | bob))
print("Only Alice:", sorted(alice - bob))

tags = ["red", "blue", "red", "green", "blue"]
print("Unique tags:", sorted(set(tags)))
print("Is 'chess' in alice?", "chess" in alice)
