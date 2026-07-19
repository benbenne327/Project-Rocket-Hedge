from analyze_prices import analyze, load_prices
from save_prices import save_prices


def main():
    print("=" * 44)
    print(" PROJECT ROCKET HEDGE")
    print("=" * 44)
    print()

    print("Collecting latest prices...")
    save_prices()
    print()

    rows = load_prices()

    if not rows:
        print("No price history available.")
        return

    analyze(rows)


if __name__ == "__main__":
    main()

