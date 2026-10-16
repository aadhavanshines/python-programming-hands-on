item = input("Item: ")
quantity = int(input("Quantity: "))
unit_price = float(input("Unit price: "))
total = quantity * unit_price
print()
print(f"{'Item':<12}{'Qty':>5}{'Price':>10}{'Total':>10}")
print(f"{item:<12}{quantity:>5}{unit_price:>10.2f}{total:>10.2f}")
