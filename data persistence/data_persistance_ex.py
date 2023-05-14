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