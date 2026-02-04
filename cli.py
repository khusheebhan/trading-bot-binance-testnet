import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # VALIDATION
    validate_inputs(
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    # API KEYS 
    API_KEY = "YOUR_KEY_HERE"
    API_SECRET = "YOUR_SECRET_HERE"

    client = BinanceClient(API_KEY, API_SECRET)

    response = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    print("\nOrder Placed Successfully!")
    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Average Price: {response.get('avgPrice')}")

if __name__ == "__main__":
    main()
