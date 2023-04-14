#%% Set Up
import pytest
from stock_market import Stock, StockMarket, StockMarketServer, StockMarketClient

#%% Test Stock class
def test_stock_creation():
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    assert stock.symbol == 'AAPL'
    assert stock.name == 'Apple Inc.'
    assert stock.price == 150.0
    assert stock.volume == 1000

def test_update_price():
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock.update_price(160.0)
    assert stock.price == 160.0

def test_update_volume():
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock.update_volume(1200)
    assert stock.volume == 1200

#%% Test StockMarket class
def test_add_stock():
    stock_market = StockMarket()
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    assert stock_market.get_stock('AAPL') == stock

def test_remove_stock():
    stock_market = StockMarket()
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    stock_market.remove_stock('AAPL')
    assert stock_market.get_stock('AAPL') is None

def test_update_stock():
    stock_market = StockMarket()
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    stock_market.update_stock('AAPL', price=160.0, volume=1200)
    assert stock_market.get_stock('AAPL').price == 160.0
    assert stock_market.get_stock('AAPL').volume == 1200

#%% Test StockMarketServer and StockMarketClient classes
@pytest.fixture
def setup_server_client():
    stock_market = StockMarket()
    server = StockMarketServer(stock_market)
    client = StockMarketClient(server)
    return stock_market, server, client

def test_process_request_add_stock(setup_server_client):
    stock_market, server, client = setup_server_client
    request = {
        'action': 'add',
        'stock_data': {
            'symbol': 'AAPL',
            'name': 'Apple Inc.',
            'price': 150.0,
            'volume': 1000
        }
    }
    response = server.process_request(request)
    assert response['status'] == 'success'
    assert stock_market.get_stock('AAPL') is not None

def test_process_request_remove_stock(setup_server_client):
    stock_market, server, client = setup_server_client
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    request = {'action': 'remove', 'symbol': 'AAPL'}
    response = server.process_request(request)
    assert response['status'] == 'success'
    assert stock_market.get_stock('AAPL') is None

def test_process_request_update_stock(setup_server_client):
    stock_market, server, client = setup_server_client
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    request = {'action': 'update', 'symbol': 'AAPL', 'price': 160.0, 'volume': 1200}
    response = server.process_request(request)
    assert response['status'] == 'success'
    assert stock_market.get_stock('AAPL').price == 160.0
    assert stock_market.get_stock('AAPL').volume == 1200

def test_send_request_add_stock(setup_server_client):
    stock_market, server, client = setup_server_client
    request = {
    'action': 'add',
    'stock_data': {
    'symbol': 'AAPL',
    'name': 'Apple Inc.',
    'price': 150.0,
    'volume': 1000
    }
    }
    response = client.send_request(request)
    assert response['status'] == 'success'
    assert stock_market.get_stock('AAPL') is not None

def test_send_request_remove_stock(setup_server_client):
    stock_market, server, client = setup_server_client
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    request = {'action': 'remove', 'symbol': 'AAPL'}
    response = client.send_request(request)
    assert response['status'] == 'success'
    assert stock_market.get_stock('AAPL') is None

def test_send_request_update_stock(setup_server_client):
    stock_market, server, client = setup_server_client
    stock = Stock('AAPL', 'Apple Inc.', 150.0, 1000)
    stock_market.add_stock(stock)
    request = {'action': 'update', 'symbol': 'AAPL', 'price': 160.0, 'volume': 1200}
    response = client.send_request(request)
    assert response['status'] == 'success'
    assert stock_market.get_stock('AAPL').price == 160.0
    assert stock_market.get_stock('AAPL').volume == 1200
