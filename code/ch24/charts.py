import matplotlib

matplotlib.use("Agg")  # draw to files, without opening a window
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

sales = pd.read_csv("sales.csv", parse_dates=["date"])
sales["revenue"] = sales["quantity"] * sales["unit_price"]
monthly = (
    sales.groupby([sales["date"].dt.to_period("M"), "store"])["revenue"]
    .sum()
    .unstack()
)

fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4))
monthly.index = monthly.index.strftime("%b")
monthly.plot(ax=left, marker="o")
left.set_title("Revenue per month")
left.set_xlabel("Month")
left.set_ylabel("Revenue")
left.grid(alpha=0.3)

by_category = sales.groupby("category")["revenue"].sum().sort_values()
by_category.plot.barh(ax=right, color="#3776ab")
right.set_title("Revenue by category, January to June")
right.set_xlabel("Revenue")
right.set_ylabel("")

fig.tight_layout()
fig.savefig("sales_charts.png", dpi=200)
print("Saved sales_charts.png")
