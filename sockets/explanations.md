# 1 Basic socket connection:

## Server:

Create a server socket with AF_INET (IPv4) and SOCK_STREAM (TCP) options.
Bind the socket to 'localhost' and port 5000.
Start listening for incoming connections with a backlog of 1.
Accept a connection from a client.
Receive the stock symbol from the client.
Send the hardcoded stock price back to the client.
Close the client and server sockets.

## Client:

Create a client socket with AF_INET (IPv4) and SOCK_STREAM (TCP) options.
Connect to the server at 'localhost' and port 5000.
Send the stock symbol to the server.
Receive the stock price from the server and print it.
Close the client socket.

# 2 Send multiple stock symbols:

## Server (explained in the previous response):

Repeats the process for receiving and sending back stock prices in a loop until no more stock symbols are received.

## Client:

Same as the previous client, but now iterates over a list of stock symbols.
Sends each stock symbol to the server and receives the corresponding stock price.
Prints the stock price for each symbol.
Closes the client socket.

# 3 JSON communication:

## Server:

Similar to the basic server, but now receives a JSON object containing a list of stock symbols.
Sends back a JSON object containing a list of hardcoded stock prices.
Uses the json module to encode and decode JSON objects.

## Client:

Similar to the previous client, but now sends a JSON object containing a list of stock symbols.
Receives a JSON object containing a list of stock prices.
Uses the json module to encode and decode JSON objects.

# 4 Concurrent server (single-threaded):

## Server:

Uses the select module to handle multiple clients concurrently.
Maintains a list of connected clients.
Accepts new clients and adds them to the list.
Receives stock symbols and sends back stock prices to each client.

## Client (two instances):

Same as the previous clients, but now two instances of the client can connect to the server simultaneously.

# 5 Concurrent server (multi-threaded):

## Server:

Uses the threading module to handle multiple clients concurrently.
Spawns a new thread for each client connection, handling stock symbol reception and stock price sending.

# 6 Stock price updates:

## Server:

Maintains a dictionary of stock symbols and their corresponding prices.
Spawns a separate thread to update the stock prices randomly every few seconds.
Responds to client requests with updated stock prices.

# 7 Persistent connections:

## Server:

Modifies the client handling function to keep the connection open and continue processing client requests.
Closes the connection when the client sends a "disconnect" message.

## Client:

Sends stock symbols continuously and receives stock prices.
Sends a "disconnect" message to close the connection with the server.