'''
Stock market themed exercise
Create a simple stock market application using object-oriented programming and server-client API communication.

1) Define a Stock class with attributes like symbol, name, price, and volume.
2) Create a StockMarket class that stores multiple Stock instances and allows for adding, removing, and updating stocks.
3) Create a StockMarketServer class that receives and processes requests for adding, removing, or updating stocks from clients.
4) Create a StockMarketClient class that sends requests to the StockMarketServer and receives responses.
5) Write test cases using pytest for all the methods implemented in tasks 1-4.
'''
#%% ad1)
class Stock:
    def __init__(self, symbol, name, price, volume):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.volume = volume

    def update_price(self, new_price):
        self.price = new_price

    def update_volume(self, new_volume):
        self.volume = new_volume
#%% ad2)
class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]

    def update_stock(self, symbol, price=None, volume=None):
        if symbol in self.stocks:
            if price is not None:
                self.stocks[symbol].update_price(price)
            if volume is not None:
                self.stocks[symbol].update_volume(volume)

    def get_stock(self, symbol):
        if symbol in self.stocks:
            return self.stocks[symbol]
        else:
            print(f"{symbol} not in stocks.")
#%% ad3) 
import json

class StockMarketServer:
    def __init__(self, stock_market):
        self.stock_market = stock_market

    def process_request(self, request):
        action = request.get('action')
        if action == 'add':
            stock_data = request.get('stock_data')
            stock = Stock(**stock_data)
            self.stock_market.add_stock(stock)
            return {'status': 'success', 'message': 'Stock added successfully'}
        elif action == 'remove':
            symbol = request.get('symbol')
            self.stock_market.remove_stock(symbol)
            return {'status': 'success', 'message': 'Stock removed successfully'}
        elif action == 'update':
            symbol = request.get('symbol')
            price = request.get('price')
            volume = request.get('volume')
            self.stock_market.update_stock(symbol, price, volume)
            return {'status': 'success', 'message': 'Stock updated successfully'}
        else:
            return {'status': 'error', 'message': 'Invalid action'}
#%% ad4)
class StockMarketClient:
    def __init__(self, server):
        self.server = server

    def send_request(self, request):
        response = self.server.process_request(request)
        return response
# %%
