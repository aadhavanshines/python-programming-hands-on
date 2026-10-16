def km_to_miles(km):
    return km * 0.621371


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def kg_to_pounds(kg):
    return kg * 2.20462


CONVERSIONS = {
    "1": ("km to miles", km_to_miles),
    "2": ("°C to °F", celsius_to_fahrenheit),
    "3": ("kg to pounds", kg_to_pounds),
}


def show_menu():
    for key, (label, _) in CONVERSIONS.items():
        print(f"  {key}. {label}")
    print("  q. quit")


def main():
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "q":
            print("Goodbye!")
            break
        if choice not in CONVERSIONS:
            print("Please choose 1, 2, 3 or q.")
            continue
        label, convert = CONVERSIONS[choice]
        value = float(input("Value: "))
        print(f"  {label}: {value} -> {convert(value):.2f}")


main()
