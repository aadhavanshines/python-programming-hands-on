class BankAccount:
    """A simple bank account that won't let the balance go below zero."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"only {self.balance} available")
        self.balance -= amount

    def describe(self):
        return f"{self.owner}: balance {self.balance}"


meera = BankAccount("Meera", 100)
tom = BankAccount("Tom")

meera.deposit(50)
tom.deposit(20)
print(meera.describe())
print(tom.describe())

try:
    tom.withdraw(500)
except ValueError as error:
    print("Withdrawal refused:", error)
print(tom.describe())
