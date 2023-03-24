# %% -------------------- OOP - Stock Market Theme --------------------

# %% 
# 1) Create a Stock class that has properties for the stock symbol, current price, and the date of the last trade. Write methods to get and set these properties.
from datetime import date

class Stock:
    def __init__(self, symbol, price, last_trade_date):
        self.symbol = symbol
        self.price = price
        self.last_trade_date = last_trade_date
      
    def get_symbol(self):
      return(self.symbol)
    
    def set_symbol(self, symbol):
      self.symbol = symbol
      return(f"Success. New symbol: {self.symbol}")
      
    def get_price(self):
      return(self.price)
    
    def set_price(self, price):
      self.price = price
      return(f"Success. New price: {self.price}")
      
    def get_last_trade_date(self):
      return(self.last_trade_date)
    
    def set_last_trade_date(self, last_trade_date):
      self.last_trade_date = last_trade_date
      return(f"Success. Last trade date: {self.last_trade_date}")

    def __repr__(self):
        return(self.symbol)

aapl = Stock("AAPL", 145.06, date(2023, 3, 24))
aapl.set_price(140.55)
aapl.get_price()
aapl.price
print(f"{aapl.symbol} was traded on {aapl.last_trade_date} at price of {aapl.price}.")
# %%
# 2) Create a Portfolio class that holds a collection of Stock objects. Write methods to add and remove stocks from the portfolio.

class Portfolio():
   
    def __init__(self):
      self.stocks = []

    def buy(self, stock):
      self.stocks.append(stock)
    
    def sell(self, stock):
       if stock in self.stocks:
          self.stocks.remove(stock)
          print(f"{stock.symbol} successfully sold at {stock.price}")
       else:
          print(f"{stock.symbol} not in Portfolio.")
    
    def __repr__(self):
       return(str([s.symbol + " " + str(s.price) for s in self.stocks]))
#%%
flatex = Portfolio()
flatex.buy(aapl)
flatex.sell(aapl)
msft = Stock("MSFT", 235.78, date(2023, 3, 24))
flatex.buy(msft)
flatex.buy(aapl)
print(flatex)
# %% 3) Add a method to the Stock class that calculates the percentage change in price from the last trade. Create a Stock object and print the result.

class Stock:
    def __init__(self, symbol, price, last_trade_date):
        self.symbol = symbol
        self.price = price
        self.last_trade_date = last_trade_date
      
    def get_symbol(self):
      return(self.symbol)
    
    def set_symbol(self, symbol):
      self.symbol = symbol
      return(f"Success. New symbol: {self.symbol}")
      
    def get_price(self):
      return(self.price)
    
    def set_price(self, price):
      self.price = price
      return(f"Success. New price: {self.price}")
      
    def get_last_trade_date(self):
      return(self.last_trade_date)
    
    def set_last_trade_date(self, last_trade_date):
      self.last_trade_date = last_trade_date
      return(f"Success. Last trade date: {self.last_trade_date}")

    def price_change(self, price):
       change = round((price - self.price) / self.price * 100, 2)
       print(f"{self.symbol}'s price has changed {change}% since your last trade on {self.last_trade_date}.")

    def __repr__(self):
        return(self.symbol)

aapl = Stock("AAPL", 145.06, date(2023, 3, 24))
aapl.price_change(105.23)

# %%
