# %% ad1) Basic socket connection:
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)

client_socket, addr = server_socket.accept()
stock_symbol = client_socket.recv(1024).decode('utf-8')
stock_price = 150.0
client_socket.send(str(stock_price).encode('utf-8'))

client_socket.close()
server_socket.close()
# %% ad2) Send multiple stock symbols:
import socket

def get_stock_price(stock_symbol):
    stock_prices = {'AAPL': 150.0, 'GOOG': 1200.0, 'TSLA': 700.0}
    return stock_prices.get(stock_symbol, 'Unknown stock symbol')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)

client_socket, addr = server_socket.accept()

while True:
    stock_symbol = client_socket.recv(1024).decode('utf-8')
    if not stock_symbol:
        break
    stock_price = get_stock_price(stock_symbol)
    client_socket.send(str(stock_price).encode('utf-8'))

client_socket.close()
server_socket.close()

# %% ad3) JSON communication:
import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)

client_socket, addr = server_socket.accept()
data = json.loads(client_socket.recv(1024).decode('utf-8'))
stock_prices = [150.0, 1200.0, 700.0]
client_socket.send(json.dumps({"prices": stock_prices}).encode('utf-8'))

client_socket.close()
server_socket.close()
# %% ad4) Concurrent server (single-threaded):
import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

clients = [server_socket]
count = 0
while True:
    read_sockets, _, _ = select.select(clients, [], [])
    for sock in read_sockets:
        if sock == server_socket:
            client_socket, addr = server_socket.accept()
            clients.append(client_socket)
        else:
            stock_symbol = sock.recv(1024).decode('utf-8')
            stock_price = 150.0
            sock.send(str(stock_price).encode('utf-8'))
            count += 1
    if count == 2:
        break
client_socket.close()
server_socket.close()
# %% ad5) Concurrent server (multi-threaded):
import socket
import threading

def handle_client(client_socket):
    stock_symbol = client_socket.recv(1024).decode('utf-8')
    stock_price = 150.0
    client_socket.send(str(stock_price).encode('utf-8'))
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

count = 0
while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
    if count == 2:
        break
client_socket.close()
server_socket.close()
# %% ad6) Stock price updates
import socket
import threading
import random
import time

def update_stock_prices():
    global stock_prices
    while True:
        time.sleep(3)
        for symbol in stock_prices:
            stock_prices[symbol] += random.uniform(-5, 5)

def handle_client(client_socket):
    stock_symbol = client_socket.recv(1024).decode('utf-8')
    stock_price = stock_prices[stock_symbol]
    client_socket.send(str(stock_price).encode('utf-8'))
    client_socket.close()

stock_prices = {'AAPL': 150.0, 'GOOG': 1200.0, 'TSLA': 700.0}
update_thread = threading.Thread(target=update_stock_prices)
update_thread.start()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

count = 0
while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
    if count == 2:
        break
client_socket.close()
server_socket.close()
# %% ad7) Persistent connections:
import socket
import threading

def handle_client(client_socket):
    while True:
        stock_symbol = client_socket.recv(1024).decode('utf-8')
        if stock_symbol == 'disconnect':
            break
        stock_price = stock_prices[stock_symbol]
        client_socket.send(str(stock_price).encode('utf-8'))
    client_socket.close()

stock_prices = {'AAPL': 150.0, 'GOOG': 1200.0, 'TSLA': 700.0}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

count = 0
while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
    if count == 2:
        break
client_socket.close()
server_socket.close()
# %%
