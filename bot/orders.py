def place_order(client, symbol, side, order_type, quantity, price=None):
    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order_data["price"] = price
        order_data["timeInForce"] = "GTC"

    return client.create_order(**order_data)
