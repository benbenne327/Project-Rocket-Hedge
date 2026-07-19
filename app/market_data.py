import requests


BASE_URL = "https://api.coingecko.com/api/v3"

COINS = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "solana": "solana",
}


def get_prices():
    url = (
        f"{BASE_URL}/simple/price"
        "?ids=bitcoin,ethereum,solana"
        "&vs_currencies=usd"
    )

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    return response.json()


def get_historical_prices(days=1):
    """
    Download historical USD prices and combine the three coins
    into timestamped rows.

    A one-day range provides approximately 5-minute data.
    """

    histories = {}

    for coin_name, coin_id in COINS.items():
        url = f"{BASE_URL}/coins/{coin_id}/market_chart"

        response = requests.get(
            url,
            params={
                "vs_currency": "usd",
                "days": days,
            },
            timeout=20,
        )
        response.raise_for_status()

        histories[coin_name] = response.json()["prices"]

    shortest_length = min(len(history) for history in histories.values())

    rows = []

    for index in range(shortest_length):
        rows.append(
            {
                "timestamp": histories["bitcoin"][index][0],
                "bitcoin": histories["bitcoin"][index][1],
                "ethereum": histories["ethereum"][index][1],
                "solana": histories["solana"][index][1],
            }
        )

    return rows


if __name__ == "__main__":
    prices = get_prices()

    print("\n🚀 Live Crypto Prices\n")
    print(f"Bitcoin : ${prices['bitcoin']['usd']:,.2f}")
    print(f"Ethereum: ${prices['ethereum']['usd']:,.2f}")
    print(f"Solana  : ${prices['solana']['usd']:,.2f}")
