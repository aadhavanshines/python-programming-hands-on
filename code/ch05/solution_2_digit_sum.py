number = int(input("A whole number: "))
total = 0
n = abs(number)
while n > 0:
    total += n % 10
    n //= 10
print(f"The digits of {number} add up to {total}.")
