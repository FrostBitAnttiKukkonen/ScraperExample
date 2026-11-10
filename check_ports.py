# check_ports.py

import socket

host = input("Host: ") # User types an address

# Some common ports:
# Ports being open isn't vulnerability
# Server listening to ports is normal behavior
ports = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    25: "SMTP"
}

for port, service in ports.items():
    try:
        sock = socket.create_connection((host, port), timeout=1)
        print(f"{port} ({service}) is open")
        sock.close() # Always close sockets when not needed anymore

    except Exception as e:
        print(f"{port} ({service}) is closed")
        # Printing the error not needed here exactly, we are expecting this
        # this exception for closed ports
        # print(e)
