from flask import Flask, render_template, jsonify
from data_request import Stock_api

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prices")
def get_prices():
    stock_list = ["AAPL","MSFT","GOOGL","AMZN","TSLA"]
    results = {}
    for s in stock_list:
        stock = Stock_api(s)
        results[s] = stock.get_stock_price()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)