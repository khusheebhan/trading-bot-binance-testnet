# Binance Futures Trading Bot (Testnet)

## Setup
1. Create Binance Futures Testnet account
2. Generate API key and secret
3. Add the API key and secret in cli.py
4. Install dependencies:
   pip install -r requirements.txt

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 30000

## Notes
- This project uses Binance Futures Testnet (USDT-M)
- On the testnet, MARKET orders may initially return `NEW` status due to asynchronous matching
- Order status updates can be fetched after placement if needed
- Uses Binance Futures Testnet (USDT-M)
- Logs saved in bot.log
