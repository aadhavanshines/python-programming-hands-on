counter = 0  # a global variable


def add_one(value):
    result = value + 1  # a local variable: it exists only in here
    return result


print(add_one(41))
print(counter)
print(result)  # result is not defined out here
