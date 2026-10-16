def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  Can't divide {a} by zero.")
        return None
    else:
        print(f"  {a} / {b} = {result}")
        return result
    finally:
        print("  (finished trying)")


safe_divide(10, 4)
safe_divide(10, 0)

for text in ["42", "4.2", "forty-two"]:
    try:
        number = int(text)
        print(f"{text!r} -> {number}")
    except ValueError as error:
        print(f"{text!r} failed: {error}")
