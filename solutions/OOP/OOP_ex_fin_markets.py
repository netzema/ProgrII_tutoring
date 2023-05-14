'''
1) Create a Stock class that has properties for the stock symbol, current price, and the date of the last trade. Write methods to get and set these properties.

2) Create a Portfolio class that holds a collection of Stock objects. Write methods to add and remove stocks from the portfolio.

3) Add a method to the Stock class that calculates the percentage change in price from the last trade. Create a Stock object and print the result.

4) Create a Trade class that holds information about a stock trade, including the stock symbol, the price at which it was bought or sold, and the date of the trade.

5) Modify the Portfolio class to keep track of trades made on each stock, including the number of shares bought or sold, the price paid or received, and the date of the trade.

6) Add a method to the Portfolio class that calculates the total value of all the stocks in the portfolio, based on their current prices.

7) Create a BrokerageAccount class that holds information about a customer's account balance and the stocks they own. Write methods to buy and sell stocks from the account.

8) Modify the Trade class to include information about the brokerage account used to make the trade.

9) Add a method to the BrokerageAccount class that calculates the customer's net worth, based on the value of their stocks and their account balance.

10) Create a MarketData class that provides information about the current price of a stock. Write a method to simulate the market, randomly updating the prices of all stocks in the portfolio.

11) Add a method to the Trade class that calculates the profit or loss from the trade, based on the current price of the stock and the price paid or received in the trade.
'''
#%% ad1)
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

aapl = Stock("AAPL", 145.06, date(2023, 3, 22))
print(f"{aapl.symbol} was traded on {aapl.last_trade_date} at a price of {aapl.price}.")

# %% ad2) 
class Portfolio:

    def __init__(self):
        self.stocks = []
    
    def buy(self, stock):
        self.stocks.append(stock)
        print(f"{stock.symbol} successfully bought at {stock.price}.")

    def sell(self, stock):
        if stock in self.stocks:
            self.stocks.remove(stock)
            print(f"{stock.symbol} successfully sold at {stock.price}.")
        else:
            print(f"{stock.symbol} not in Portfolio.")
    
    def __repr__(self):
        return(str([s.symbol + " " + str(s.price) for s in self.stocks]))

flatex = Portfolio()
flatex.buy(aapl)
flatex.sell(aapl)
msft = Stock("MSFT", 235.78, date(2023, 3, 22))
flatex.buy(msft)
flatex.buy(aapl)
print(flatex)
# %% ad3)
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
        print(f"{self.symbol}'s price changed {change}% since your last trade on {self.last_trade_date}.")

    def __repr__(self):
        return(f"Ticker: {self.symbol}, price: {round(self.price, 2)}\n")

aapl = Stock("AAPL", 145.06, date(2023, 3, 22))
aapl.price_change(105.23)
msft = Stock("MSFT", 235.78, date(2023, 3, 22))
# %% ad4) Create a Trade class that holds information about a stock trade, including the stock symbol, the price at which it was bought or sold, and the date of the trade.
class Trade:

    def __init__(self, symbol, price, amount, trade_type, trade_date):
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.trade_type = trade_type
        self.trade_date = trade_date

    def __repr__(self):
        return(f"Date: {self.trade_date}, symbol: {self.symbol}, price: {self.price}, amount: {self.amount}, trade: {self.trade_type}")


Trade("AAPL", 145.06, 2, "buy", date(2023, 3, 22))
#%% ad5) Modify the Portfolio class to keep track of trades made on each stock, including the number of shares bought or sold, the price paid or received, and the date of the trade.

class Portfolio:

    def __init__(self):
        self.stocks = []
        self.trades = []

    def buy(self, stock, amount):
        [self.stocks.append(stock) for n in range(amount)]
        self.trades.append(Trade(stock.symbol, stock.price, amount, "buy", stock.last_trade_date))
        print(f"{amount} share(s) of {stock.symbol} successfully bought at {stock.price}.")

    def sell(self, stock, amount):
        if stock in self.stocks:
            [self.stocks.remove(stock) for n in range(amount)]
            self.trades.append(Trade(stock.symbol, stock.price, amount, "sell", stock.last_trade_date))
            print(f"{amount} share(s) of {stock.symbol} successfully sold at {stock.price}.")
        else:
            print(f"{stock.symbol} not in Portfolio.")
    
    def __repr__(self):
        return(str([s.symbol + " " + str(s.price) for s in self.stocks]))
    
flatex = Portfolio()
flatex.buy(aapl, 3)
flatex.sell(aapl, 1)
print(flatex.stocks)
flatex.trades
# %% ad6) 
class Portfolio:

    def __init__(self):
        self.stocks = []
        self.trades = []

    def buy(self, stock, amount):
        [self.stocks.append(stock) for n in range(amount)]
        self.trades.append(Trade(stock.symbol, stock.price, amount, "buy", stock.last_trade_date))
        print(f"{amount} share(s) of {stock.symbol} successfully bought at {stock.price}.")

    def sell(self, stock, amount):
        if stock in self.stocks:
            [self.stocks.remove(stock) for n in range(amount)]
            self.trades.append(Trade(stock.symbol, stock.price, amount, "sell", stock.last_trade_date))
            print(f"{amount} share(s) of {stock.symbol} successfully sold at {stock.price}.")
        else:
            print(f"{stock.symbol} not in Portfolio.")

    def value(self):
        return(round(sum([s.price for s in self.stocks]), 2))
    
    def __repr__(self):
        return(str([s.symbol + " " + str(s.price) for s in self.stocks]))

flatex = Portfolio()
flatex.buy(aapl, 3)
flatex.buy(msft, 5)
flatex.value()
# %% ad7) Create a BrokerageAccount class that holds information about a customer's account balance and the stocks they own. Write methods to buy and sell stocks from the account.

class BrokerageAccount:

    def __init__(self, balance):
        self.balance = balance
        self.stocks = []

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def buy_stock(self, stock, amount):
        cost = stock.price * amount
        if cost > self.balance:
            print("Error: Not enough balance!")
        else:
            [self.stocks.append(stock) for n in range(amount)]
            self.balance -= cost 
            print(f"Bought {amount} share(s) of {stock.symbol} at a price of {stock.price}. New balance: {round(self.balance, 2)}")
    
    def sell_stock(self, stock, amount):
        count = self.stocks.count(stock)
        if amount > count:
            print("Error: Not enough shares!")
        else:
            cost = stock.price * amount
            [self.stocks.remove(stock) for n in range(amount)]
            self.balance += cost
            print(f"Sold {amount} share(s) of {stock.symbol} at a price of {stock.price}. New balance: {round(self.balance, 2)}")

dadat = BrokerageAccount(1000)
dadat.buy_stock(aapl, 4)
dadat.sell_stock(aapl, 1)
# %% ad8)
class Trade:

    def __init__(self, broker, stock, amount, trade_type):
        self.stock = stock
        self.symbol = stock.symbol
        self.price = stock.price
        self.amount = amount
        self.trade_type = trade_type
        self.trade_date = stock.last_trade_date

        if self.trade_type == "buy":
            broker.buy_stock(self.stock, self.amount)
        else:
            broker.sell_stock(self.stock, self.amount)

    def __repr__(self):
        return(f"Date: {self.trade_date}, symbol: {self.symbol}, price: {self.price}, amount: {self.amount}, trade: {self.trade_type}")

Trade(dadat, aapl, 2, "buy")
# %% ad9)
class BrokerageAccount:

    def __init__(self, balance):
        self.balance = balance
        self.stocks = []

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Not enough balance!")
        else:
            self.balance -= amount

    def buy_stock(self, stock, amount):
        cost = stock.price * amount
        if cost > self.balance:
            print("Error: Not enough balance!")
        else:
            [self.stocks.append(stock) for n in range(amount)]
            self.balance -= cost 
            print(f"Bought {amount} share(s) of {stock.symbol} at a price of {stock.price}. New balance: {round(self.balance, 2)}")
    
    def sell_stock(self, stock, amount):
        count = self.stocks.count(stock)
        if amount > count:
            print("Error: Not enough shares!")
        else:
            cost = stock.price * amount
            [self.stocks.remove(stock) for n in range(amount)]
            self.balance += cost
            print(f"Sold {amount} share(s) of {stock.symbol} at a price of {stock.price}. New balance: {round(self.balance, 2)}")

    def get_net_worth(self):
        return(f"Net worth: {sum([s.price for s in self.stocks]) + self.balance}")
dadat = BrokerageAccount(1000)
dadat.buy_stock(aapl, 4)
dadat.sell_stock(aapl, 1)
dadat.deposit(200)
dadat.withdraw(50)
dadat.get_net_worth()
# %% ad10) Create a MarketData class that provides information about the current price of a stock. Write a method to simulate the market, randomly updating the prices of all stocks in the portfolio.
import random

class MarketData:

    def __init__(self, stocks):
        self.stocks = stocks
    
    def get_prices(self):
        for s in self.stocks:
            s.price *= 1+random.gauss(0, .05)
        return(self.stocks)

market = MarketData([aapl, msft, Stock("GOOA", 97.03, None)])
market.get_prices()
# %% ad11)
class Trade:

    def __init__(self, broker, stock, amount, trade_type):
        self.stock = stock
        self.symbol = stock.symbol
        self.price = stock.price
        self.amount = amount
        self.trade_type = trade_type
        self.trade_date = stock.last_trade_date

        if self.trade_type == "buy":
            broker.buy_stock(self.stock, self.amount)
        else:
            broker.sell_stock(self.stock, self.amount)

    def get_return(self, current_price):
        returns = (current_price - self.price) / current_price * 100
        return(f"Paid: {self.price}. Current return: {returns}%")

    def __repr__(self):
        return(f"Date: {self.trade_date}, symbol: {self.symbol}, price: {self.price}, amount: {self.amount}, trade: {self.trade_type}")

dadat.deposit(10000)
aapl_trade = Trade(dadat, aapl, 2, "buy")
aapl_trade.get_return(144.41)
# %%
