import requests

API_KEY = "LVEW5D8G2Z97836S"
URL = (f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}")

response = requests.get(URL)

data = response.json()
print(data)