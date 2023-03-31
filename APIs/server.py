from flask import Flask, jsonify, request

app = Flask(__name__)

stocks = {
    'AAPL': {
        'name': 'Apple Inc.',
        'price': 150.0,
        'shares': 1000,
    },
    'GOOGL': {
        'name': 'Alphabet Inc.',
        'price': 2500.0,
        'shares': 500,
    },
    'TSLA': {
        'name': 'Tesla Inc.',
        'price': 600.0,
        'shares': 200,
    },
}

@app.route('/stocks', methods=['GET'])
def get_stocks():
    return jsonify(stocks)

@app.route('/stocks/sell', methods=['POST'])
def sell_stock():
    data = request.json
    symbol = data['symbol']
    shares = int(data['shares'])

    if symbol not in stocks:
        return jsonify({'error': 'Invalid symbol.'}), 400

    stock = stocks[symbol]

    if shares > stock['shares']:
        return jsonify({'error': 'Insufficient shares.'}), 400

    total_cost = shares * stock['price']
    stock['shares'] -= shares

    return jsonify({
        'message': f'Successfully sold {shares} shares of {symbol} for ${total_cost:.2f}.'
    })

@app.route('/stocks/buy', methods=['POST'])
def buy_stock():
    data = request.json
    symbol = data['symbol']
    shares = int(data['shares'])

    if symbol not in stocks:
        return jsonify({'error': 'Invalid symbol.'}), 400

    stock = stocks[symbol]
    stock['shares'] += shares

    total_sale = shares * stock['price']

    return jsonify({
        'message': f'Successfully bought {shares} shares of {symbol} for ${total_sale:.2f}.'
    })

if __name__ == '__main__':
    app.run()
