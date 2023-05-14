# %%
import pytest
import json
import csv
import sqlite3
import pickle
from data_persistence_solution import *
# %%
@pytest.fixture
def sample_stock():
    # Create a sample stock object
    return Stock("AAPL", "Apple Inc.", 134.32)

@pytest.fixture
def sample_portfolio(sample_stock):
    # Create a sample portfolio with a stock
    portfolio = Portfolio()
    portfolio.add_stock(sample_stock)
    return portfolio

def test_add_stock(sample_portfolio, sample_stock):
    # Test the add_stock() method
    assert len(sample_portfolio.stocks) == 1
    assert sample_portfolio.stocks[0] == sample_stock

def test_remove_stock(sample_portfolio, sample_stock):
    # Test the remove_stock() method
    sample_portfolio.remove_stock(sample_stock)
    assert len(sample_portfolio.stocks) == 0

def test_display_portfolio(sample_portfolio, capsys):
    # Test the display_portfolio() method
    sample_portfolio.display_portfolio()
    captured = capsys.readouterr()
    expected_output = "Symbol: AAPL\nName: Apple Inc.\nPrice: $134.32\n\n"
    assert captured.out == expected_output

def test_to_dict(sample_portfolio, sample_stock):
    # Test the to_dict() method
    expected_dict = {
        "stocks": [
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "price": 134.32
            }
        ]
    }
    assert sample_portfolio.to_dict() == expected_dict

def test_save_to_json(tmpdir, sample_portfolio):
    # Test the save_to_json() method
    file_path = tmpdir.join("portfolio.json")
    sample_portfolio.save_to_json(str(file_path))
    assert file_path.exists()

def test_save_to_csv(tmpdir, sample_portfolio):
    # Test the save_to_csv() method
    file_path = tmpdir.join("portfolio.csv")
    sample_portfolio.save_to_csv(str(file_path))
    assert file_path.exists()

def test_save_to_database(tmpdir, sample_portfolio):
    # Test the save_to_database() method
    db_file = tmpdir.join("portfolio.db")
    sample_portfolio.save_to_database(str(db_file))
    assert db_file.exists()

def test_save_to_pickle(tmpdir, sample_portfolio):
    # Test the save_to_pickle() method
    file_path = tmpdir.join("portfolio.pickle")
    sample_portfolio.save_to_pickle(str(file_path))
    assert file_path.exists()

def test_load_from_json(tmpdir):
    # Test the load_from_json() method
    file_path = tmpdir.join("portfolio.json")
    data = {
        "stocks": [
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "price": 134.32
            }
        ]
    }
    with open(file_path, "w") as file:
        json.dump(data, file)
    portfolio = Portfolio.load_from_json(str(file_path))
    assert len(portfolio.stocks) == 1
    assert portfolio.stocks[0].symbol == "AAPL"

def test_load_from_csv(tmpdir):
    # Test the load_from_csv() method
    file_path = tmpdir.join("portfolio.csv")
    data = [
        ["Symbol", "Name", "Price"],
        ["AAPL", "Apple Inc.", "134.32"]
    ]
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    portfolio = Portfolio.load_from_csv(str(file_path))
    assert len(portfolio.stocks) == 1
    assert portfolio.stocks[0].symbol == "AAPL"
    assert portfolio.stocks[0].name == "Apple Inc."
    assert portfolio.stocks[0].price == 134.32

def test_load_from_database(tmpdir):
    # Test the load_from_database() method
    db_file = tmpdir.join("portfolio.db")
    connection = sqlite3.connect(str(db_file))
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolio (
            symbol TEXT,
            name TEXT,
            price REAL
        )
    ''')
    cursor.execute("INSERT INTO portfolio VALUES (?, ?, ?)", ("AAPL", "Apple Inc.", 134.32))
    connection.commit()
    connection.close()
    portfolio = Portfolio.load_from_database(str(db_file))
    assert len(portfolio.stocks) == 1
    assert portfolio.stocks[0].symbol == "AAPL"
    assert portfolio.stocks[0].name == "Apple Inc."
    assert portfolio.stocks[0].price == 134.32

def test_load_from_pickle(tmpdir):
    # Test the load_from_pickle() method
    file_path = tmpdir.join("portfolio.pickle")
    portfolio = Portfolio()
    portfolio.add_stock(Stock("AAPL", "Apple Inc.", 134.32))
    with open(file_path, "wb") as file:
        pickle.dump(portfolio, file)
    loaded_portfolio = Portfolio.load_from_pickle(str(file_path))
    assert len(loaded_portfolio.stocks) == 1
    assert loaded_portfolio.stocks[0].symbol == "AAPL"
    assert loaded_portfolio.stocks[0].name == "Apple Inc."
    assert loaded_portfolio.stocks[0].price == 134.32
# %%
