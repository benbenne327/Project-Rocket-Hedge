import csv
from pathlib import Path
from statistics import mean


DATA_FILE = Path("data/prices.csv")
ASSETS = ("bitcoin", "ethereum", "solana")


def load_prices() -> list[dict[str, str]]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "No price history found. Run collector.py first."
        )

    with DATA_FILE.open(newline="") as file:
        return list(csv.DictReader(file))


def percent_change(old_price: float, new_price: float) -> float:
    if old_price == 0:
        return 0.0

    return ((new_price - old_price) / old_price) * 100


def analyze_asset(
    rows: list[dict[str, str]],
    asset: str,
    periods: int = 5,
) -> None:
    prices = [float(row[asset]) for row in rows]
    latest_price = prices[-1]

    available_periods = min(periods, len(prices))
    recent_prices = prices[-available_periods:]
    moving_average = mean(recent_prices)

    if len(prices) >= 2:
        change = percent_change(prices[-2], latest_price)
    else:
        change = 0.0

    if latest_price > moving_average:
        trend = "ABOVE AVERAGE"
    elif latest_price < moving_average:
        trend = "BELOW AVERAGE"
    else:
        trend = "AT AVERAGE"

    print(f"{asset.title():<10}: ${latest_price:,.2f}")
    print(f" Last change : {change:+.4f}%")
    print(f" {available_periods}-sample avg: ${moving_average:,.2f}")
    print(f" Position : {trend}")
    print()


def main() -> None:c
    rows = load_prices()

    if not rows:
        print("No price records available.")
        return

    print("=" * 44)
    print(" PROJECT ROCKET HEDGE ANALYSIS")
    print("=" * 44)
    print(f"Samples available: {len(rows)}")
    print()

    for asset in ASSETS:
        analyze_asset(rows, asset)


if __name__ == "__main__":
    main()