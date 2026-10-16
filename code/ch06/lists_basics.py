fruits = ["mango", "banana", "apple"]
print(fruits)
print("First:", fruits[0])
print("Last:", fruits[-1])
print("How many:", len(fruits))

fruits.append("cherry")  # add to the end
fruits.insert(1, "kiwi")  # add at position 1
print(fruits)

fruits.remove("banana")  # remove by value
last = fruits.pop()  # remove and return the last item
print("Popped:", last)
print(fruits)

print("Is apple there?", "apple" in fruits)
fruits.sort()
print("Sorted:", fruits)
