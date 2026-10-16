def password_problems(password):
    """Return the ways a password is too weak (an empty list if none)."""
    problems = []
    if len(password) < 10:
        problems.append("use at least 10 characters")
    has_upper = has_lower = has_digit = has_symbol = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_symbol = True
    if not has_upper:
        problems.append("add an upper-case letter")
    if not has_lower:
        problems.append("add a lower-case letter")
    if not has_digit:
        problems.append("add a digit")
    if not has_symbol:
        problems.append("add a symbol such as ! or #")
    if password.lower() in ("password123", "qwertyuiop", "letmein123"):
        problems.append("don't use a well-known password")
    return problems


while True:
    password = input("Try a password (or press Enter to stop): ")
    if not password:
        break
    problems = password_problems(password)
    if problems:
        print("Weak:")
        for problem in problems:
            print("  -", problem)
    else:
        print("Strong password!")
