# 1 Basic socket connection:
a. Write a simple server that listens on a specific port (e.g., 5000) and accepts incoming connections.
b. Write a client that connects to the server and sends a stock symbol (e.g., 'AAPL') as a string.
c. The server should respond with a hardcoded stock price for that symbol (e.g., 150.0).
d. The client should print the received stock price.

# 2 Send multiple stock symbols:
a. Modify the client to send multiple stock symbols, one at a time (e.g., 'AAPL', 'GOOG', 'TSLA').
b. The server should respond with hardcoded stock prices for each symbol, in the same order.
c. The client should print the received stock prices.

# 3 JSON communication:
a. Modify the client and server to communicate using JSON messages instead of plain strings.
b. The client should send a JSON object containing a list of stock symbols (e.g., {"symbols": ["AAPL", "GOOG", "TSLA"]}).
c. The server should respond with a JSON object containing a list of stock prices (e.g., {"prices": [150.0, 1200.0, 700.0]}).
d. The client should print the received JSON object.

# 4 Concurrent server (single-threaded):
a. Modify the server to handle multiple clients concurrently using the select module.
b. Create two clients that connect to the server and send stock symbols simultaneously.
c. The server should respond to each client with the appropriate stock prices.
d. Each client should print the received stock prices.

# 5 Concurrent server (multi-threaded):
a. Modify the server to handle multiple clients concurrently using the threading module.
b. Create a function that handles a client connection, receives stock symbols, and sends stock prices.
c. When a new client connects, spawn a new thread to handle the connection using the client handling function.
d. Ensure that the server can handle multiple clients simultaneously and responds with the correct stock prices.

# 6 Stock price updates:
a. Modify the server to maintain a dictionary of stock symbols and their corresponding prices.
b. Implement a separate function to update the stock prices in the dictionary randomly every few seconds.
c. Spawn a separate thread for the stock price updating function.
d. Ensure that the server sends the updated stock prices to clients when they request stock information.

# 7 Persistent connections:
a. Modify the client and server to use persistent connections.
b. After connecting to the server, the client should continuously send stock symbols and receive stock prices.
c. The server should keep the connection open and continue to process the client's requests until the client sends a "disconnect" message.
d. The server should then close the connection and handle other clients.