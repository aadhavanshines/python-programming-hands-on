# Tip calculator: split a restaurant bill, including the tip.
bill = float(input("Bill amount: "))
tip_percent = float(input("Tip (%): "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
each = total / people

print()
print(f"Tip:        {tip:8.2f}")
print(f"Total:      {total:8.2f}")
print(f"Each pays:  {each:8.2f}")
