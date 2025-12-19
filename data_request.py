

import requests
import time

STOCK_LIST = ["AAPL","MSFT","GOOGL","AMZN","META","TSLA","NVDA","NFLX","AMD","INTC","ORCL","IBM","JPM","BAC","GS","V","MA","KO","PEP","MCD","NKE"]
API_KEY = "LVEW5D8G2Z97836S"

results = []

for stock in STOCK_LIST:
    response = requests.get(
        "https://www.alphavantage.co/query",
        params={
            "function": "GLOBAL_QUOTE",
            "symbol": stock,
            "apikey": API_KEY
        }
    )

    data = response.json()

    if "Global Quote" in data and data["Global Quote"]:
        price = float(data["Global Quote"]["05. price"])
        results.append({"symbol": stock, "price": price})
        print(f"{stock}: ${price}")
    else:
        print(f"{stock}: API error")

    time.sleep(12) 

print("\nFinal list:")
print(results)

