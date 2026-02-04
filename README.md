# Binance Futures Trading Bot (Testnet)

## Setup
1. Create Binance Futures Testnet account
2. Generate API key and secret
3. Install dependencies:
   pip install -r requirements.txt

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 30000

## Notes
- Uses Binance Futures Testnet (USDT-M)
- Logs saved in bot.log
