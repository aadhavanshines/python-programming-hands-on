point = (3, 4)
x, y = point  # unpacking
print("x =", x, "and y =", y)

red = (255, 0, 0)
print("Red has", len(red), "values")

a, b = 1, 2
a, b = b, a  # swap two values in one line
print(a, b)

point[0] = 10  # tuples can't be changed
