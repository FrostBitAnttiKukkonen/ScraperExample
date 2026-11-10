# local_server.py

from http.server import ThreadingHTTPServer
from http.server import SimpleHTTPRequestHandler
import os

PORT = 8000 # use 8000 instead of 80 to not block default http servers

os.chdir("website") # folder to serve

server = ThreadingHTTPServer(
    ("localhost", PORT),
    SimpleHTTPRequestHandler
)

print(f"Serving on http://localhost:{PORT}")

try:
    server.serve_forever()

except KeyboardInterrupt: # Ctrl + C from command line or terminal
    # macOS might need Command + . (dot)
    print("\nShutting down...")
    server.server_close()