import csv
from collections import Counter, defaultdict

revenue_by_store = defaultdict(float)
revenue_by_month = defaultdict(float)
copies_by_title = Counter()

with open("sales.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        revenue = int(row["quantity"]) * float(row["unit_price"])
        revenue_by_store[row["store"]] += revenue
        revenue_by_month[row["date"][:7]] += revenue
        copies_by_title[row["title"]] += int(row["quantity"])

print("Revenue by store:")
for store, revenue in sorted(
    revenue_by_store.items(), key=lambda kv: kv[1], reverse=True
):
    print(f"  {store:10} {revenue:>10,.2f}")

print("Revenue by month:")
for month in sorted(revenue_by_month):
    print(f"  {month} {revenue_by_month[month]:>10,.2f}")

print("Best sellers (copies):")
for title, copies in copies_by_title.most_common(3):
    print(f"  {copies:4}  {title}")
