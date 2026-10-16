def ask_int(prompt, low, high):
    """Keep asking until the user types a whole number from low to high."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("  Please type a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Please choose from {low} to {high}.")


rating = ask_int("Rate the book (1-5): ", 1, 5)
print("Thanks! You gave it", "*" * rating)
