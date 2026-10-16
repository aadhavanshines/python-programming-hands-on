size = 5
for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(f"{row * col:4}", end="")
    print()
