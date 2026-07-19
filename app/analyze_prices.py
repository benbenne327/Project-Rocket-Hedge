import csv

from indicators import compare_moving_averages, relative_strength_index


def load_prices():
    prices = []

    try:
        with open("data/prices.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                prices.append(
                    {
                        "bitcoin": float(row["bitcoin"]),
                        "ethereum": float(row["ethereum"]),
                        "solana": float(row["solana"]),
                    }
                )

    except FileNotFoundError:
        print("No price history found.")

    return prices


def analyze(rows):
    print("\n===== ROCKET HEDGE ANALYZER =====\n")

    for coin in ["bitcoin", "ethereum", "solana"]:
        analysis = compare_moving_averages(rows, coin)
        rsi = relative_strength_index(rows, coin)

        print(coin.upper())
        print(f"5 MA       : ${analysis['short_average']:,.2f}")
        print(f"10 MA      : ${analysis['long_average']:,.2f}")
        print(f"Difference : {analysis['difference_percent']:+.2f}%")
        print(f"RSI        : {rsi:.2f}")
        print(f"Trend      : {analysis['trend']}")
        print(f"Signal     : {analysis['signal']}")
        print()


def main():
    rows = load_prices()

    if not rows:
        return

    analyze(rows)


if __name__ == "__main__":
    main()
