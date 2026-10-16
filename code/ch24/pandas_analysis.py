import pandas as pd

sales = pd.read_csv("sales.csv", parse_dates=["date"])
sales["revenue"] = sales["quantity"] * sales["unit_price"]

print(sales.shape)
columns = ["date", "store", "title", "quantity", "revenue"]
print(sales[columns].head(3).to_string(index=False))
print()

by_store = (
    sales.groupby("store")["revenue"].sum().sort_values(ascending=False)
)
print(by_store.round(2).to_string())
print()

table = (
    sales.pivot_table(
        index="category", columns="store", values="revenue", aggfunc="sum"
    )
    .round(0)
    .astype(int)
)
print(table.to_string())
print()

monthly = sales.groupby(sales["date"].dt.to_period("M"))["revenue"].sum()
print(monthly.round(2).to_string())
print()

sales["weekend"] = sales["date"].dt.dayofweek >= 5
print(sales.groupby("weekend")["quantity"].mean().round(2).to_string())
