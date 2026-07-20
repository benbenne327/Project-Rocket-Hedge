import csv

from indicators import (
    compare_moving_averages,
    relative_strength_index,
    macd,
    bollinger_bands,
)


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
        macd_data = macd(rows, coin) if len(rows) >= 35 else None
        bb = bollinger_bands(rows, coin)

        print(coin.upper())
        print(f"5 MA       : ${analysis['short_average']:,.2f}")
        print(f"10 MA      : ${analysis['long_average']:,.2f}")
        print(f"Difference : {analysis['difference_percent']:+.2f}%")
        print(f"RSI        : {rsi:.2f}")

        if macd_data is not None:
            print(f"EMA 12     : {macd_data['ema12']:.2f}")
            print(f"EMA 26     : {macd_data['ema26']:.2f}")
            print(f"MACD       : {macd_data['macd']:.2f}")
            print(f"Signal Ln  : {macd_data['signal']:.2f}")
            print(f"Histogram  : {macd_data['histogram']:.2f}")
        else:
            remaining = 35 - len(rows)
            print(f"MACD       : Collecting data ({remaining} more rows needed)")

        print()
        print("BOLLINGER BANDS")
        print(f"Middle    : {bb['middle']:.2f}")
        print(f"Upper     : {bb['upper']:.2f}")
        print(f"Lower     : {bb['lower']:.2f}")
        print(f"Bandwidth : {bb['bandwidth']:.2f}%")
        print(f"%B        : {bb['percent_b']:.2f}")

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
