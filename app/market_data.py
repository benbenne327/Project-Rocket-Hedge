import requests


URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum,solana"
    "&vs_currencies=usd"
)


def get_prices():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    prices = get_prices()

    print("\n🚀 Live Crypto Prices\n")

    print(f"Bitcoin : ${prices['bitcoin']['usd']:,}")
    print(f"Ethereum: ${prices['ethereum']['usd']:,}")
    print(f"Solana : ${prices['solana']['usd']:,}")