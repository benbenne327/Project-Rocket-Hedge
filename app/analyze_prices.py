import csv


def load_prices():
    prices = []

    try:
        with open("data/prices.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                prices.append({
                    "bitcoin": float(row["bitcoin"]),
                    "ethereum": float(row["ethereum"]),
                    "solana": float(row["solana"]),
                })

    except FileNotFoundError:
        print("No price history found.")

    return prices


def analyze(rows):
    print("\n===== ROCKET HEDGE ANALYZER =====\n")

    for coin in ["bitcoin", "ethereum", "solana"]:
        latest = rows[-1][coin]
        average = sum(row[coin] for row in rows) / len(rows)
        difference_percent = (latest - average) / average * 100

        if difference_percent >= 0.10:
            trend = "UP"
            signal = "BUY"
        elif difference_percent <= -0.10:
            trend = "DOWN"
            signal = "SELL"
        else:
            trend = "SIDEWAYS"
            signal = "HOLD"

        print(coin.upper())
        print(f"Current    : ${latest:,.2f}")
        print(f"Average    : ${average:,.2f}")
        print(f"Difference : {difference_percent:+.4f}%")
        print(f"Trend      : {trend}")
        print(f"Signal     : {signal}")
        print()


def main():
    rows = load_prices()

    if not rows:
        return

    analyze(rows)


if __name__ == "__main__":
    main()
