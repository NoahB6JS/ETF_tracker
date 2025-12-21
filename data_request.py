import requests

class Stock_api:
    def __init__(self, stock_tag):
        self.stock_tag = stock_tag
        self.base_url = "https://api.finazon.io/latest/finazon/us_stocks_essential/price"
        self.api_key = "b6d10dd6b57645cc8ddfd573ebb24005kv"

    def get_stock_price(self):
        try:
            response = requests.get(
                self.base_url,
                params={"ticker": self.stock_tag, "apikey": self.api_key}
            )
            data = response.json()

            # Check if 'p' exists
            if "p" in data:
                return float(data["p"])
            else:
                print(f"Warning: 'p' not found for {self.stock_tag}: {data}")
                return 0.0
        except Exception as e:
            print(f"Error fetching {self.stock_tag}: {e}")
            return 0.0