a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("The largest is", largest)
