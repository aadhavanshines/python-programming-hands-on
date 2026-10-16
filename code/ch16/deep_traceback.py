def parse_price(text):
    return float(text.replace("€", ""))


def order_total(lines):
    total = 0
    for line in lines:
        name, price = line.split(":")
        total += parse_price(price)
    return total


def print_receipt(lines):
    print(f"Total: {order_total(lines):.2f}")


print_receipt(["coffee: €3.20", "cake: €4.75", "tea: free"])
