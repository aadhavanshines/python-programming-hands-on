price = 1234.5
share = 0.256
item = "Notebook"

print(f"{price:.2f}")  # two decimal places
print(f"{price:,.2f}")  # with a thousands separator
print(f"{share:.1%}")  # as a percentage
print(f"[{item:<12}]")  # left-aligned in 12 characters
print(f"[{item:>12}]")  # right-aligned
print(f"[{item:^12}]")  # centered
print(f"{42:05d}")  # padded with zeros
print(f"{price=}")  # name and value, handy for debugging
