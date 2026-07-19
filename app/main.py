from datetime import datetime


class RocketHedge:
    VERSION = "0.1.0"

    def startup(self):
        print("=" * 50)
        print("🚀 PROJECT ROCKET HEDGE")
        print(f"Version {self.VERSION}")
        print("=" * 50)
        print()
        print("Mission Status : ONLINE")
        print(f"Startup Time : {datetime.now():%Y-%m-%d %H:%M:%S}")
        print()
        print("Market Scanner : OFFLINE")
        print("AI Analyst : OFFLINE")
        print("Risk Engine : OFFLINE")
        print("Portfolio : OFFLINE")
        print("Coinbase : NOT CONNECTED")
        print()
        print("Ready to begin development.")


if __name__ == "__main__":
    RocketHedge().startup()
