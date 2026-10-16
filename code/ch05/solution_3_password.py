PASSWORD = "open sesame"
for attempt in range(1, 4):
    entry = input(f"Password (attempt {attempt} of 3): ")
    if entry == PASSWORD:
        print("Welcome in!")
        break
    print("Wrong password.")
else:
    print("Too many attempts. Locked out.")
