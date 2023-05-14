# %% Set Up
import json
import csv
import sqlite3
import pickle
# %%
# Define Stock class
class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    def display(self):
        print(f"Symbol: {self.symbol}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print()

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "name": self.name,
            "price": self.price
        }
# Defione Portfolio class
class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def display_portfolio(self):
        for stock in self.stocks:
            stock.display()

    def to_dict(self):
        return {
            "stocks": [stock.to_dict() for stock in self.stocks]
        }

    def save_to_json(self, file_path):
        data = self.to_dict()
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def save_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Name", "Price"])
            for stock in self.stocks:
                writer.writerow([stock.symbol, stock.name, stock.price])

    def save_to_database(self, db_file):
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS portfolio (
                symbol TEXT,
                name TEXT,
                price REAL
            )
        ''')
        for stock in self.stocks:
            cursor.execute("INSERT INTO portfolio VALUES (?, ?, ?)", (stock.symbol, stock.name, stock.price))
        connection.commit()
        connection.close()

    def save_to_pickle(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_json(file_path):
        portfolio = Portfolio()
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data['stocks']:
                stock = Stock(item['symbol'], item['name'], item['price'])
                portfolio.add_stock(stock)
        return portfolio

    @staticmethod
    def load_from_csv(file_path):
        portfolio = Portfolio()
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                stock = Stock(row[0], row[1], float(row[2]))
                portfolio.add_stock(stock)
        return portfolio

    @staticmethod
    def load_from_database(db_file):
        portfolio = Portfolio()
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM portfolio")
        rows = cursor.fetchall()
        for row in rows:
            stock = Stock(row[0], row[1], row[2])
            portfolio.add_stock(stock)
        connection.close()
        return portfolio

    @staticmethod
    def load_from_pickle(file_path):
        with open(file_path, 'rb') as file:
            portfolio = pickle.load(file)
        return portfolio

# %% Test classes and methods
# Create a sample portfolio
portfolio = Portfolio()
portfolio.add_stock(Stock("AAPL", "Apple Inc.", 134.32))
portfolio.add_stock(Stock("GOOGL", "Alphabet Inc.", 2350.78))
portfolio.add_stock(Stock("MSFT", "Microsoft Corporation", 252.46))

# Display the portfolio
print("Portfolio:")
portfolio.display_portfolio()
# %%
# Save the portfolio to JSON file
json_file = 'portfolio.json'
portfolio.save_to_json(json_file)
print(f"\nPortfolio saved to {json_file}")
# %%
# Save the portfolio to CSV file
csv_file = 'portfolio.csv'
portfolio.save_to_csv(csv_file)
print(f"Portfolio saved to {csv_file}")
# %%
# Save the portfolio to SQLite database
db_file = 'portfolio.db'
portfolio.save_to_database(db_file)
print(f"Portfolio saved to {db_file}")
# %%
# Save the portfolio to pickle file
pickle_file = 'portfolio.pickle'
portfolio.save_to_pickle(pickle_file)
print(f"Portfolio saved to {pickle_file}")
# %%
# Load the portfolio from JSON file
loaded_portfolio_json = Portfolio.load_from_json(json_file)
print("\nLoaded portfolio from JSON file:")
loaded_portfolio_json.display_portfolio()
# %%
# Load the portfolio from CSV file
loaded_portfolio_csv = Portfolio.load_from_csv(csv_file)
print("\nLoaded portfolio from CSV file:")
loaded_portfolio_csv.display_portfolio()
# %%
# Load the portfolio from SQLite database
loaded_portfolio_db = Portfolio.load_from_database(db_file)
print("\nLoaded portfolio from SQLite database:")
loaded_portfolio_db.display_portfolio()
# %%
# Load the portfolio from pickle file
loaded_portfolio_pickle = Portfolio.load_from_pickle(pickle_file)
print("\nLoaded portfolio from pickle file:")
loaded_portfolio_pickle.display_portfolio()
# %%