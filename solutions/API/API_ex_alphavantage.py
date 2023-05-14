# %% -------------------- Session 3: accessing and creating APIs --------------------
'''
1) Accessing Stock Market Data Using an API
Use the Alpha Vantage API to fetch the latest stock market data for a specified ticker symbol in Python. Print out the retrieved data as a JSON object.

2) Parsing Stock Market Data from JSON
Parse the JSON response from Exercise 1 to extract the latest price, volume, and other relevant information for the specified stock. Print out the extracted information in a human-readable format.

3) Building a Simple Stock Market Portfolio Tracker
Create a Python script that allows the user to enter a list of ticker symbols and then fetches the latest stock market data for each stock using the Alpha Vantage API. Display the retrieved data in a table format, along with the total portfolio value and percentage change from the previous day.

4) Creating a Custom Stock Market API
Create a Python Flask application that exposes a custom API for retrieving stock market data. The API should have one endpoint that accepts a GET request with a ticker symbol and returns a JSON response with the latest price and volume data for the specified stock. Use the Alpha Vantage API to fetch the data and then format it into the desired JSON format.

5) Building a Simple Stock Market Watchlist
Create a Python script that allows the user to enter a list of ticker symbols and then fetches the latest stock market data for each stock using the Alpha Vantage API. Display the retrieved data in a table format and allow the user to add or remove stocks from the watchlist.

6) Building a Simple Stock Trading API (Client & Server)
Create an API server which keeps track of your trades. It can receive two POST requests to buy and sell stocks as well as a GET request to show all the stocks the user currently holds. Test the code using a client, which simulates the purchase and the sell of a stock.

7) Creating a Stock Market Data Visualization Tool
Create a Python script that uses the Matplotlib library to display a line chart of the historical stock price data for a specified ticker symbol. Use the Alpha Vantage API to fetch the data and then format it into a suitable format for plotting with Matplotlib.

8) Building a Simple Stock Market News Aggregator
Create a Python script that fetches the latest news articles related to a specified stock using the NewsAPI. Print out the headlines and URLs of the retrieved articles.

9) Creating a Custom Stock Market News API
Create a Python Flask application that exposes a custom API for retrieving news articles related to a specified stock. The API should have one endpoint that accepts a GET request with a ticker symbol and returns a JSON response with the latest news articles and URLs for the specified stock. Use the NewsAPI to fetch the data and then format it into the desired JSON format.

10) Building a Simple Stock Market Sentiment Analysis Tool
Create a Python script that uses the TextBlob library to perform sentiment analysis on a specified news article related to a stock. Use the NewsAPI to fetch the article text and then use TextBlob to analyze its sentiment.

11) Creating a Custom Stock Market Prediction API
Create a Python Flask application that exposes a custom API for making predictions about the future price of a specified stock. The API should have one endpoint that accepts a GET request with a ticker symbol and a date range, and returns a JSON response with the predicted price data for the specified date range. Use a simple linear regression model to make the predictions.
'''
# %% -------------------- Set Up --------------------
import config

API_KEY = config.token
#%%
# ad1) Accessing Stock Market Data Using an API
# Use the Alpha Vantage API to fetch the latest stock market data for a specified ticker symbol in Python. Print out the retrieved data as a JSON object.
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

latest_price = data['Global Quote']['05. price']
latest_volume = data['Global Quote']['06. volume']

print(f"Latest Price: {latest_price}")
print(f"Latest Volume: {latest_volume}")
# %%
# ad3) Building a Simple Stock Market Portfolio Tracker
# Create a Python script that allows the user to enter a list of ticker symbols and then fetches the latest stock market data for each stock using the Alpha Vantage API. Display the retrieved data in a table format, along with the total portfolio value and percentage change from the previous day.
import requests

class Portfolio():

    def __init__(self, stocks):
        self.value = 0
        self.stocks = stocks

flatex = Portfolio(stocks = {"AAPL": 3, "GOOGL": 2, "TSLA": 5})
# %%
current_portfolio_value = 0

for symbol, pieces in flatex.stocks.items():

    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    latest_price = float(data['Global Quote']['05. price'])
    
    total_value = latest_price * pieces
    
    current_portfolio_value += total_value
    
    print(f"Symbol: {symbol}")
    print(f"Latest Price: {latest_price}")
    print(f"Total Value: {total_value}")
    print()

# Get change
change = round((current_portfolio_value - flatex.value) / flatex.value * 100, 2) if flatex.value > 0 else 0
flatex.value = current_portfolio_value
print(f"Current Portfolio Value: {flatex.value}. Change since last time: {change}%.")
# %%
# ad4) Creating a Custom Stock Market API
# Create a Python Flask application that exposes a custom API for retrieving stock market data. The API should have one endpoint that accepts a GET request with a ticker symbol and returns a JSON response with the latest price and volume data for the specified stock. Use the Alpha Vantage API to fetch the data and then format it into the desired JSON format.
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/stock/<symbol>")
def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    latest_price = data['Global Quote']['05. price']
    latest_volume = data['Global Quote']['06. volume']
    
    return jsonify({
        "symbol": symbol,
        "latest_price": latest_price,
        "latest_volume": latest_volume
    })

if __name__ == "__main__":
    app.run()

# %%
# ad5) Building a Simple Stock Market Watchlist
# Create a Python script that allows the user to enter a list of ticker symbols and then fetches the latest stock market data for each stock using the Alpha Vantage API. Display the retrieved data in a table format and allow the user to add or remove stocks from the watchlist.

import requests

watchlist = ["AAPL", "GOOGL", "TSLA"]
data = {}

while True:
    for symbol in watchlist:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data[symbol] = response.json()['Global Quote']
    
    for symbol, quote in data.items():
        print(f"Symbol: {symbol}")
        print(f"Latest Price: {quote['05. price']}")
        print(f"Latest Volume: {quote['06. volume']}")
        print()
    
    add_remove = input("Do you wish to add (a) or remove (r) a stock from the watchlise?\n(Press anything else to skip) ")

    if add_remove.lower().startswith("a"):
        symbol = input("Which stock would you like to add? ").upper()

        if symbol in watchlist:
            print(f"{symbol} is already in the watchlist!")
        else:
            watchlist.append(symbol)
        
    elif add_remove.lower().startswith("r"):
        symbol = input("Which stock would you like to remove? ").upper()

        if symbol not in watchlist:
            print(f"{symbol} cannot be removed as it is not in the watchlist.")
        else:
            watchlist.remove(symbol)

    print(f"\nCurrent Watchlist: {watchlist}\n")
    break
# %%