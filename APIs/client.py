import requests

# Get all stocks
response = requests.get('http://localhost:5000/stocks')
stocks = response.json()

# Buy a stock
response = requests.post('http://localhost:5000/stocks/buy', json={
    'symbol': 'AAPL',
    'shares': 10,
})
print(response.json()['message'])

# Sell a stock
response = requests.post('http://localhost:5000/stocks/sell', json={
    'symbol': 'AAPL',
    'shares': 5,
})
print(response.json()['message'])
