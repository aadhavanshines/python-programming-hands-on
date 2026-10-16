# Cinema tickets: children and seniors pay less, and Tuesday is half price.
age = int(input("Age: "))
day = input("Day of the week: ").strip().lower()

if age < 0 or age > 120:
    print("That age doesn't look right.")
else:
    if age < 12:
        price = 6.00
    elif age >= 65:
        price = 7.50
    else:
        price = 11.00

    if day == "tuesday":
        price = price / 2

    print(f"Your ticket costs {price:.2f}.")
