class Ticket:
    price = 12.0  # a class attribute, shared by every ticket
    sold = 0

    def __init__(self, seat):
        self.seat = seat  # an instance attribute, one per ticket
        Ticket.sold += 1


a = Ticket("A1")
b = Ticket("A2")
print(a.seat, b.seat, "| price:", a.price, "| sold:", Ticket.sold)

Ticket.price = 14.0  # changes the price for every ticket
print(a.price, b.price)
