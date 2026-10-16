class Money:
    """An amount of money in one currency, stored in cents."""

    def __init__(self, amount, currency="EUR"):
        self.cents = round(amount * 100)
        self.currency = currency

    def __repr__(self):
        return f"Money({self.cents / 100!r}, {self.currency!r})"

    def __str__(self):
        return f"{self.cents / 100:,.2f} {self.currency}"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("can't add different currencies")
        return Money((self.cents + other.cents) / 100, self.currency)

    def __eq__(self, other):
        return (self.cents, self.currency) == (other.cents, other.currency)

    def __lt__(self, other):
        return self.cents < other.cents

    def __bool__(self):
        return self.cents != 0


coffee = Money(3.20)
cake = Money(4.75)
print(coffee + cake)
print(repr(coffee + cake))
print(Money(0.1) + Money(0.2) == Money(0.3))
print(sorted([cake, coffee]))
print(bool(Money(0)), bool(coffee))
