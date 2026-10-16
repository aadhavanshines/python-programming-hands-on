def apply_discounts(prices, percent):
    result = []
    for price in prices:
        breakpoint()  # stop here and look around
        result.append(price - price * percent // 100)
    return result


print(apply_discounts([19.99, 5.00], 10))
