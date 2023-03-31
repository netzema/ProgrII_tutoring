# %% -------------------- Session 3: accessing and creating APIs --------------------
# Set Up
import config

API_KEY = config.token
# %%
'''
1) Accessing Stock Market Data Using an API
Use the Alpha Vantage API to fetch the latest stock market data for a specified ticker symbol in Python. Print out the retrieved data as a JSON object.
'''
import requests

symbol = "AAPL"

url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)
# %%
# ad2) Parsing Stock Market Data from JSON
# Parse the JSON response from Exercise 1 to extract the latest price, volume, and other relevant information for the specified stock. Print out the extracted information in a human-readable format.
import requests

symbol = "AAPL"

url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

latest_price = data["Global Quote"]["05. price"]
latest_volume = data["Global Quote"]["06. volume"]

print(f"Latest Price: {latest_price}")
print(f"Latest Volume: {latest_volume}")
# %%
# ad3) Building a Simple Stock Market Portfolio Tracker
# Create a Python script that allows the user to enter a list of ticker symbols and then fetches the latest stock market data for each stock using the Alpha Vantage API. Display the retrieved data in a table format, along with the total portfolio value and percentage change from the previous day.
import requests

class Portfolio():

    def __init__(self, stocks):
        self.value = 4000
        self.stocks = stocks

    def calculate_today_value(self):
        pass

    def __repr__(self):
        return self.calculate_today_value()
    

flatex = Portfolio(stocks = {
    "AAPL": 3,
    "GOOGL": 2,
    "MSFT": 5
})
# %%
current_portfolio_value = 0

for symbol, pieces in flatex.stocks.items():

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    latest_price = float(data["Global Quote"]["05. price"])

    total_value = latest_price * pieces

    current_portfolio_value += total_value

    print(f"Symbol: {symbol}")
    print(f"Latest Price: {latest_price}")
    print(f"Total Value: {current_portfolio_value}")

# Get change
change = round((current_portfolio_value - flatex.value) / flatex.value * 100, 2) if flatex.value > 0 else 0
flatex.value = current_portfolio_value
print(f"Current Porftolio Value: {flatex.value}. Change since last time: {change}%.")
# %%
# ad4) Creating a Custom Stock Market API
# Create a Python Flask application that exposes a custom API for retrieving stock market data. The API should have one endpoint that accepts a GET request with a ticker symbol and returns a JSON response with the latest price and volume data for the specified stock. Use the Alpha Vantage API to fetch the data and then format it into the desired JSON format.

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/stock/<symbol>")
def get_stock_data(symbol):

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    latest_price = float(data["Global Quote"]["05. price"])
    latest_volume = float(data["Global Quote"]["06. volume"])

    return jsonify({
        "symbol": symbol,
        "latest_price": latest_price,
        "latest_volume": latest_volume
    })

if __name__ == "__main__":
    app.run()
# %%
