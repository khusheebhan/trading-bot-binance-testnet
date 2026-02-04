from binance.client import Client
import logging

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        # Futures testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def create_order(self, **kwargs):
        try:
            logging.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logging.info(f"Order response: {response}")
            return response
        except Exception as e:
            logging.error(f"API Error: {e}")
            raise
