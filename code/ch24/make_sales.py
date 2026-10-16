# Make the fictional sales data used in this chapter: six months of
# sales at the three branches of "Paper Lantern Books". The seed makes
# it the same every time.
import csv
import random
from datetime import date, timedelta

random.seed(2026)
STORES = {"Riverside": 1.0, "Old Town": 0.8, "Station": 1.3}
CATALOG = {
    "Fiction": [
        ("The Lighthouse Keeper", 12.99),
        ("Salt and Stars", 9.99),
        ("Northbound", 14.50),
    ],
    "Children": [("Milo the Brave Mouse", 7.99), ("The Moon Kite", 6.50)],
    "Science": [("Tiny Worlds", 18.00), ("How Rivers Think", 21.50)],
    "Cookery": [("One Pan Suppers", 16.99), ("Spice Road Kitchen", 24.00)],
    "Travel": [("Walking the Coast", 13.50)],
}
SEASON = {1: 0.8, 2: 0.85, 3: 1.0, 4: 1.05, 5: 1.1, 6: 1.25}

rows = []
day = date(2026, 1, 1)
while day <= date(2026, 6, 30):
    for store, size in STORES.items():
        for _ in range(random.randint(0, 2)):
            category = random.choice(list(CATALOG))
            title, price = random.choice(CATALOG[category])
            weekend = 1.4 if day.weekday() >= 5 else 1.0
            quantity = max(
                1,
                round(
                    random.gauss(3, 1.5)
                    * size
                    * weekend
                    * SEASON[day.month]
                ),
            )
            rows.append(
                [day.isoformat(), store, category, title, quantity, price]
            )
    day += timedelta(days=1)

with open("sales.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(
        ["date", "store", "category", "title", "quantity", "unit_price"]
    )
    writer.writerows(rows)
print(f"Wrote {len(rows)} sales to sales.csv")
