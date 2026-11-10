# server_connection.py

import socket

host = "example.com" # Domain/host name, or IP address
# Try "ping example.com" in terminal/command line and use the IP
# host = "104.20.23.154"

port = 80 # Default port for HTTP
# Try also:
# port = 9999

try:
    sock = socket.create_connection((host, port), timeout=5) # After 5s, stop trying
    print(f"Connected to {host}:{port}")
    sock.close() # Always close sockets when not needed anymore
    
except Exception as e:
    # General exceptions can be difficult to track later
    # Remember to print or log also the exception message or type, e
    print("Connection failed")
    print(e)
