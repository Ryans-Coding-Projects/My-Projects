#This program tracks the cost of 1 Bitcoin in real time

import requests

def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        return bitcoin_price
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    bitcoin_price = get_bitcoin_price()
    if isinstance(bitcoin_price, str):
        print(bitcoin_price)
    else:
        print(f"Bitcoin Price (USD): ${bitcoin_price}")
