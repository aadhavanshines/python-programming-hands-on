import pandas as pd


def busiest_day(sales):
    """The weekday name with the most copies sold."""
    copies = sales.groupby(sales["date"].dt.day_name())["quantity"].sum()
    return copies.idxmax()


def best_title_per_store(sales):
    """For each store, the title with the most copies sold."""
    copies = sales.groupby(["store", "title"])["quantity"].sum()
    return (
        copies.groupby(level="store")
        .idxmax()
        .map(lambda pair: pair[1])
        .to_dict()
    )


def month_on_month_growth(sales):
    """Percentage change in revenue from each month to the next."""
    revenue = (
        (sales["quantity"] * sales["unit_price"])
        .groupby(sales["date"].dt.month)
        .sum()
    )
    return (revenue.pct_change() * 100).round(1).dropna().to_dict()


if __name__ == "__main__":
    data = pd.read_csv("sales.csv", parse_dates=["date"])
    print(busiest_day(data))
    for store, title in best_title_per_store(data).items():
        print(f"  {store}: {title}")
    print(month_on_month_growth(data))
