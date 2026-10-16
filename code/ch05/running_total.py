# Add up numbers until the user types "done".
total = 0
count = 0
while True:
    entry = input("Number (or 'done'): ")
    if entry == "done":
        break
    total += float(entry)
    count += 1

if count > 0:
    print(f"{count} numbers, total {total}, average {total / count:.2f}")
else:
    print("No numbers entered.")
