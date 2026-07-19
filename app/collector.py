import time
from save_prices import save_prices

print("🚀 Rocket Hedge Collector Started")

while True:
    save_prices()
    print("Sleeping for 60 seconds...\n")
    time.sleep(60)