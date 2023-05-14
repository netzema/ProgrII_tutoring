# %% ad4) Concurrent server (single-threaded):
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

stock_symbol = 'AAPL'
client_socket.send(stock_symbol.encode('utf-8'))
stock_price = float(client_socket.recv(1024).decode('utf-8'))
print(f'{stock_symbol}: {stock_price}')
# %%
client_socket.close()
# %% ad7) Persistent Connections:
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

stock_symbols = ['AAPL', 'GOOG', 'TSLA', 'disconnect']

for symbol in stock_symbols:
    client_socket.send(symbol.encode('utf-8'))
    if symbol == 'disconnect':
        break
    stock_price = float(client_socket.recv(1024).decode('utf-8'))
    print(f'{symbol}: {stock_price}')

client_socket.close()
# %%