import csv
import os
from datetime import datetime, timezone

from market_data import get_historical_prices, get_prices


DATA_FILE = "data/prices.csv"
FIELDNAMES = ["timestamp", "bitcoin", "ethereum", "solana"]


def format_timestamp(timestamp_ms):
    timestamp_seconds = timestamp_ms / 1000

    return datetime.fromtimestamp(
        timestamp_seconds,
        tz=timezone.utc,
    ).strftime("%Y-%m-%d %H:%M:%S")


def read_existing_timestamps():
    if not os.path.exists(DATA_FILE):
        return set()

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        return {
            row["timestamp"]
            for row in reader
            if row.get("timestamp")
        }


def bootstrap_history():
    rows = get_historical_prices(days=1)

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()

        for row in rows:
            writer.writerow(
                {
                    "timestamp": format_timestamp(row["timestamp"]),
                    "bitcoin": row["bitcoin"],
                    "ethereum": row["ethereum"],
                    "solana": row["solana"],
                }
            )

    print(f"✅ Historical database created with {len(rows)} rows.")


def append_live_price():
    prices = get_prices()
    timestamp = datetime.now(timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    existing_timestamps = read_existing_timestamps()

    if timestamp in existing_timestamps:
        print("ℹ️ Price timestamp already exists.")
        return

    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists or os.path.getsize(DATA_FILE) == 0:
            writer.writeheader()

        writer.writerow(
            {
                "timestamp": timestamp,
                "bitcoin": prices["bitcoin"]["usd"],
                "ethereum": prices["ethereum"]["usd"],
                "solana": prices["solana"]["usd"],
            }
        )

    print("✅ Live prices saved.")


def save_prices():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        bootstrap_history()
        return

    with open(DATA_FILE, "r", newline="") as file:
        row_count = sum(1 for _ in file)

    if row_count <= 1:
        bootstrap_history()
        return

    append_live_price()


if __name__ == "__main__":
    save_prices()
