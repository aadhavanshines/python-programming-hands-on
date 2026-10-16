tasks = ["Buy milk", "Call Priya", "Fix bike"]

for task in tasks:
    print("-", task)

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

days = ["Mon", "Tue", "Wed"]
hours = [7.5, 8, 6]
for day, h in zip(days, hours):
    print(f"{day}: {h} h")
