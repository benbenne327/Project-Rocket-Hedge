import csv
import os
from datetime import datetime

from market_data import get_prices


DATA_FILE = "data/prices.csv"


def save_prices():

    prices = get_prices()

    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "bitcoin",
                "ethereum",
                "solana"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            prices["bitcoin"]["usd"],
            prices["ethereum"]["usd"],
            prices["solana"]["usd"],
        ])

    print("✅ Prices saved.")


if __name__ == "__main__":
    save_prices()